#!/usr/bin/env python3
"""
CHS-SDK示例运行脚本
"""

import os
import sys
import argparse
import subprocess

def run_example(example_name):
    """运行指定的示例"""
    # 定义示例路径
    example_paths = {
        'basic-simulation': 'examples/basic-simulation',
        'agent-control': 'examples/agent-control',
        'ai-modeling': 'examples/ai-modeling'
    }
    
    if example_name not in example_paths:
        print(f"错误: 未知的示例 '{example_name}'")
        print("可用的示例:")
        for name in example_paths.keys():
            print(f"  - {name}")
        return 1
    
    # 构建示例路径
    example_path = example_paths[example_name]
    full_path = os.path.join(os.path.dirname(__file__), '..', example_path)
    
    # 检查示例目录是否存在
    if not os.path.exists(full_path):
        print(f"错误: 示例目录 '{full_path}' 不存在")
        return 1
    
    # 运行示例
    print(f"正在运行示例: {example_name}")
    print(f"路径: {full_path}")
    
    try:
        # 切换到示例目录并运行
        original_cwd = os.getcwd()
        os.chdir(full_path)
        
        # 运行示例脚本
        result = subprocess.run([sys.executable, 'run.py'], 
                              capture_output=True, text=True)
        
        # 恢复原始工作目录
        os.chdir(original_cwd)
        
        # 输出结果
        if result.returncode == 0:
            print("示例运行成功!")
            print(result.stdout)
        else:
            print("示例运行失败!")
            print(result.stderr)
            return result.returncode
            
    except Exception as e:
        print(f"运行示例时发生错误: {e}")
        return 1
    
    return 0

def list_examples():
    """列出所有可用的示例"""
    print("可用的CHS-SDK示例:")
    print("  basic-simulation  - 基础仿真示例")
    print("  agent-control     - 智能体控制示例")
    print("  ai-modeling       - AI建模示例")

def main():
    parser = argparse.ArgumentParser(description='CHS-SDK示例运行工具')
    parser.add_argument('example', nargs='?', help='要运行的示例名称')
    parser.add_argument('--list', '-l', action='store_true', help='列出所有可用示例')
    
    args = parser.parse_args()
    
    if args.list:
        list_examples()
        return 0
    
    if not args.example:
        print("请指定要运行的示例，或使用 --list 查看可用示例")
        return 1
    
    return run_example(args.example)

if __name__ == "__main__":
    sys.exit(main())