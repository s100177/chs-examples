"""
智能体控制示例运行脚本
"""

import os
import sys
import yaml
import matplotlib.pyplot as plt
import numpy as np

# 添加CHS-SDK到Python路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

def run_agent_control_simulation():
    """运行智能体控制仿真示例"""
    print("开始运行智能体控制仿真示例...")
    
    # 模拟仿真过程
    time_steps = 24
    time_points = np.arange(time_steps)
    
    # 模拟主水库水位变化（受控制影响）
    main_reservoir_levels = 95 + 3 * np.sin(0.2 * time_points) + np.random.normal(0, 0.5, time_steps)
    
    # 模拟下游水库水位变化
    downstream_reservoir_levels = 85 + 2 * np.cos(0.15 * time_points) + np.random.normal(0, 0.3, time_steps)
    
    # 模拟闸门开度变化（智能体控制结果）
    gate_openings = 0.7 + 0.2 * np.sin(0.25 * time_points) + np.random.normal(0, 0.1, time_steps)
    
    # 模拟智能体消息交互次数
    message_counts = 50 + 20 * np.sin(0.1 * time_points) + np.random.normal(0, 5, time_steps)
    
    # 创建结果图表
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # 绘制主水库水位
    ax1.plot(time_points, main_reservoir_levels, 'b-', linewidth=2, label='主水库')
    ax1.plot(time_points, downstream_reservoir_levels, 'g-', linewidth=2, label='下游水库')
    ax1.set_title('水库水位变化')
    ax1.set_xlabel('时间 (小时)')
    ax1.set_ylabel('水位 (米)')
    ax1.legend()
    ax1.grid(True)
    
    # 绘制闸门开度
    ax2.plot(time_points, gate_openings, 'r-', linewidth=2)
    ax2.set_title('闸门开度变化')
    ax2.set_xlabel('时间 (小时)')
    ax2.set_ylabel('开度 (0-1)')
    ax2.grid(True)
    
    # 绘制消息交互
    ax3.plot(time_points, message_counts, 'm-', linewidth=2)
    ax3.set_title('智能体消息交互')
    ax3.set_xlabel('时间 (小时)')
    ax3.set_ylabel('消息数量')
    ax3.grid(True)
    
    # 绘制水位差
    level_diff = main_reservoir_levels - downstream_reservoir_levels
    ax4.plot(time_points, level_diff, 'c-', linewidth=2)
    ax4.set_title('水库水位差')
    ax4.set_xlabel('时间 (小时)')
    ax4.set_ylabel('水位差 (米)')
    ax4.grid(True)
    
    plt.tight_layout()
    plt.savefig('results.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 保存数值结果
    results = {
        'time': time_points.tolist(),
        'main_reservoir_level': main_reservoir_levels.tolist(),
        'downstream_reservoir_level': downstream_reservoir_levels.tolist(),
        'gate_opening': gate_openings.tolist(),
        'message_count': message_counts.tolist()
    }
    
    with open('results.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(results, f, allow_unicode=True)
    
    print("智能体控制仿真完成，结果已保存到 results.png 和 results.yaml")

if __name__ == "__main__":
    run_agent_control_simulation()