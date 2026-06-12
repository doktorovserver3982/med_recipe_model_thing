#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kaggle-optimized training script for parallel GPU execution
Run this in your Kaggle notebook instead of train.py -all
"""

import os
import sys
import subprocess
from multiprocessing import Process, Queue
from pathlib import Path
import time
from datetime import datetime

# Add current directory to path
sys.path.append(str(Path.cwd()))


def setup_environment(gpu_id, experiment_name):
    """Setup environment variables for a specific GPU"""
    env=os.environ.copy()
    env['CUDA_VISIBLE_DEVICES']=str(gpu_id)
    env['PYTHONPATH']=str(Path.cwd())
    return env


def run_experiment(experiment_name, gpu_id, queue=None):
    """
    Run a single training experiment on specified GPU
    """
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting {experiment_name} on GPU {gpu_id}")

    env=setup_environment(gpu_id, experiment_name)

    # Create experiment-specific log file
    log_dir=Path.cwd() / "logs"
    log_dir.mkdir(exist_ok=True)
    log_file=log_dir / f"{experiment_name}_gpu{gpu_id}.log"

    # Run the training
    cmd=[sys.executable, "-c", f"""
from train import train
import os
print(f"Running {experiment_name} on GPU {{os.environ.get('CUDA_VISIBLE_DEVICES', 'unknown')}}")
train("{experiment_name}")
"""]

    try:
        with open(log_file, 'w') as f:
            result=subprocess.run(
                cmd,
                env=env,
                stdout=f,
                stderr=subprocess.STDOUT,
                text=True
            )

        success=result.returncode == 0

        if success:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ {experiment_name} completed successfully on GPU {gpu_id}")
        else:
            print(
                f"[{datetime.now().strftime('%H:%M:%S')}] ❌ {experiment_name} failed on GPU {gpu_id} (check {log_file})")

        if queue:
            queue.put((experiment_name, success, gpu_id))

        return success

    except Exception as e:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ❌ {experiment_name} crashed on GPU {gpu_id}: {e}")
        if queue:
            queue.put((experiment_name, False, gpu_id))
        return False


def run_parallel_experiments(experiment_pairs, max_parallel=2):
    """
    Run experiments in parallel

    Args:
        experiment_pairs: List of (experiment_name, gpu_id) tuples
        max_parallel: Maximum number of parallel processes
    """
    results={}
    processes=[]
    queue=Queue()

    # Start experiments
    for i, (exp_name, gpu_id) in enumerate(experiment_pairs):
        if len(processes) >= max_parallel:
            # Wait for a process to complete
            for p in processes:
                p.join(timeout=1)
            processes=[p for p in processes if p.is_alive()]

        p=Process(target=run_experiment, args=(exp_name, gpu_id, queue))
        p.start()
        processes.append(p)

        # Small delay to avoid initialization conflicts
        time.sleep(2)

    # Wait for all to complete
    for p in processes:
        p.join()

    # Collect results
    while not queue.empty():
        exp_name, success, gpu_id=queue.get()
        results[exp_name]=success

    return results


def run_sequential_experiment(experiment_name, gpu_id=0):
    """Run a single experiment sequentially"""
    return run_experiment(experiment_name, gpu_id)


def main():
    """Main execution function"""
    print("=" * 60)
    print("Kaggle Parallel Training Launcher")
    print(f"Working directory: {Path.cwd()}")
    print("=" * 60)

    # Define your experiments with GPU assignments
    # First batch: Run baseline and highres in parallel
    parallel_batch_1=[
        ("baseline", 0),  # baseline on GPU 0 (1280px, batch=8)
        ("highres", 1),  # highres on GPU 1 (2048px, batch=4)
    ]

    # Second batch: Run highres_nomosaic alone (since only 2 GPUs)
    final_experiment="highres_nomosaic"

    # Run first parallel batch
    print("\n🚀 Starting parallel experiments...")
    print(f"   GPU 0: baseline (1280px)")
    print(f"   GPU 1: highres (2048px)")
    print("-" * 60)

    results=run_parallel_experiments(parallel_batch_1)

    # Check results
    print("\n📊 First batch results:")
    for exp_name, success in results.items():
        status="✅ PASSED" if success else "❌ FAILED"
        print(f"   {exp_name}: {status}")

    # Run final experiment
    print(f"\n🚀 Starting final experiment: {final_experiment} on GPU 0")
    print("-" * 60)

    final_success=run_sequential_experiment(final_experiment, gpu_id=0)

    # Final summary
    print("\n" + "=" * 60)
    print("📊 TRAINING SUMMARY")
    print("=" * 60)
    for exp_name, success in results.items():
        status="✅ PASSED" if success else "❌ FAILED"
        print(f"   {exp_name}: {status}")
    print(f"   {final_experiment}: {'✅ PASSED' if final_success else '❌ FAILED'}")
    print("=" * 60)

    # Print output locations
    print("\n📁 Output locations:")
    models_dir=Path.cwd() / "models"
    if models_dir.exists():
        for exp_dir in models_dir.iterdir():
            if exp_dir.is_dir():
                weights_file=exp_dir / "weights" / "best.pt"
                if weights_file.exists():
                    print(f"   {exp_dir.name}: {weights_file}")

    logs_dir=Path.cwd() / "logs"
    if logs_dir.exists():
        print(f"\n📄 Logs saved to: {logs_dir}/")


if __name__ == "__main__":
    main()