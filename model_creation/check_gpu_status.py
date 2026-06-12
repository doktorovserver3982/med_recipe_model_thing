#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Check GPU availability and status in Kaggle"""

import subprocess
import os


def check_gpus():
    print("=" * 10)
    print("GPU STATUS CHECK")
    print("=" * 10)

    # Check NVIDIA GPUs
    try:
        result=subprocess.run(['nvidia-smi', '--query-gpu=index,name,memory.total,memory.used', '--format=csv'],
                              capture_output=True, text=True)
        print("\n📊 NVIDIA GPU Info:")
        print(result.stdout)
    except:
        print("nvidia-smi not available")

    # Check CUDA_VISIBLE_DEVICES
    visible=os.environ.get('CUDA_VISIBLE_DEVICES', 'Not set')
    print(f"\n🔧 CUDA_VISIBLE_DEVICES: {visible}")

    # Test PyTorch GPU access
    try:
        import torch
        print(f"\n🔥 PyTorch version: {torch.__version__}")
        print(f"   CUDA available: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"   GPU count: {torch.cuda.device_count()}")
            for i in range(torch.cuda.device_count()):
                print(f"   GPU {i}: {torch.cuda.get_device_name(i)}")
                print(f"      Memory: {torch.cuda.get_device_properties(i).total_memory / 1e9:.1f} GB")
    except ImportError:
        print("PyTorch not installed")

    print("=" * 60)


if __name__ == "__main__":
    check_gpus()