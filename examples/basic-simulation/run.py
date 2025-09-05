"""
基础仿真示例运行脚本
"""

import os
import sys
import yaml
import matplotlib.pyplot as plt
import numpy as np

# 添加CHS-SDK到Python路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

def run_basic_simulation():
    """运行基础仿真示例"""
    print("开始运行基础仿真示例...")
    
    # 模拟仿真过程
    time_steps = 24
    time_points = np.arange(time_steps)
    
    # 模拟水库水位变化（初始100m，逐渐下降）
    reservoir_levels = 100 - 0.5 * time_points
    
    # 模拟管道流量变化
    pipe_flows = 50 + 5 * np.sin(0.5 * time_points)
    
    # 模拟闸门开度变化
    gate_openings = 0.8 - 0.2 * np.cos(0.3 * time_points)
    
    # 创建结果图表
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))
    
    # 绘制水库水位
    ax1.plot(time_points, reservoir_levels, 'b-', linewidth=2)
    ax1.set_title('水库水位变化')
    ax1.set_xlabel('时间 (小时)')
    ax1.set_ylabel('水位 (米)')
    ax1.grid(True)
    
    # 绘制管道流量
    ax2.plot(time_points, pipe_flows, 'g-', linewidth=2)
    ax2.set_title('管道流量变化')
    ax2.set_xlabel('时间 (小时)')
    ax2.set_ylabel('流量 (m³/s)')
    ax2.grid(True)
    
    # 绘制闸门开度
    ax3.plot(time_points, gate_openings, 'r-', linewidth=2)
    ax3.set_title('闸门开度变化')
    ax3.set_xlabel('时间 (小时)')
    ax3.set_ylabel('开度 (0-1)')
    ax3.grid(True)
    
    plt.tight_layout()
    plt.savefig('results.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 保存数值结果
    results = {
        'time': time_points.tolist(),
        'reservoir_level': reservoir_levels.tolist(),
        'pipe_flow': pipe_flows.tolist(),
        'gate_opening': gate_openings.tolist()
    }
    
    with open('results.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(results, f, allow_unicode=True)
    
    print("仿真完成，结果已保存到 results.png 和 results.yaml")

if __name__ == "__main__":
    run_basic_simulation()