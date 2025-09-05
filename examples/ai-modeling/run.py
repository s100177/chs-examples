"""
AI建模示例运行脚本
"""

import os
import sys
import yaml
import matplotlib.pyplot as plt
import numpy as np

# 添加CHS-SDK到Python路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

def run_ai_modeling_simulation():
    """运行AI建模仿真示例"""
    print("开始运行AI建模仿真示例...")
    
    # 模拟自然语言处理过程
    prompt = "创建一个包含上游水库、输水管道和下游水库的系统，要求在24小时内将上游水库水位从100米调节到90米"
    print(f"处理自然语言描述: {prompt}")
    
    # 模拟LLM生成配置的过程
    print("调用大语言模型生成系统配置...")
    
    # 模拟生成的配置
    generated_components = {
        "upstream_reservoir": {
            "type": "Reservoir",
            "parameters": {
                "name": "上游水库",
                "initial_level": 100.0,
                "capacity_curve": [[0, 1000000], [100, 2000000]]
            }
        },
        "pipe": {
            "type": "Pipe",
            "parameters": {
                "name": "输水管道",
                "length": 500.0,
                "diameter": 2.5,
                "roughness": 0.01
            }
        },
        "downstream_reservoir": {
            "type": "Reservoir",
            "parameters": {
                "name": "下游水库",
                "initial_level": 80.0,
                "capacity_curve": [[0, 800000], [80, 1500000]]
            }
        }
    }
    
    print("配置生成完成:")
    print(yaml.dump(generated_components, allow_unicode=True))
    
    # 模拟仿真过程
    time_steps = 24
    time_points = np.arange(time_steps)
    
    # 模拟上游水库水位调节过程
    upstream_levels = 100 - (10 * time_points / time_steps) + np.random.normal(0, 0.3, time_steps)
    
    # 模拟下游水库水位变化
    downstream_levels = 80 + (8 * time_points / time_steps) + np.random.normal(0, 0.2, time_steps)
    
    # 模拟管道流量
    pipe_flows = 40 + 10 * np.sin(0.3 * time_points) + np.random.normal(0, 2, time_steps)
    
    # 创建结果图表
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))
    
    # 绘制水库水位
    ax1.plot(time_points, upstream_levels, 'b-', linewidth=2, label='上游水库')
    ax1.plot(time_points, downstream_levels, 'g-', linewidth=2, label='下游水库')
    ax1.set_title('水库水位调节过程')
    ax1.set_xlabel('时间 (小时)')
    ax1.set_ylabel('水位 (米)')
    ax1.legend()
    ax1.grid(True)
    
    # 绘制管道流量
    ax2.plot(time_points, pipe_flows, 'r-', linewidth=2)
    ax2.set_title('管道流量变化')
    ax2.set_xlabel('时间 (小时)')
    ax2.set_ylabel('流量 (m³/s)')
    ax2.grid(True)
    
    # 绘制水位差
    level_diff = upstream_levels - downstream_levels
    ax3.plot(time_points, level_diff, 'm-', linewidth=2)
    ax3.set_title('水库水位差')
    ax3.set_xlabel('时间 (小时)')
    ax3.set_ylabel('水位差 (米)')
    ax3.grid(True)
    
    plt.tight_layout()
    plt.savefig('results.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 保存数值结果
    results = {
        'time': time_points.tolist(),
        'upstream_level': upstream_levels.tolist(),
        'downstream_level': downstream_levels.tolist(),
        'pipe_flow': pipe_flows.tolist(),
        'level_difference': level_diff.tolist()
    }
    
    with open('results.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(results, f, allow_unicode=True)
    
    # 保存生成的配置
    os.makedirs('generated_config', exist_ok=True)
    with open('generated_config/components.yml', 'w', encoding='utf-8') as f:
        yaml.dump(generated_components, f, allow_unicode=True)
    
    print("AI建模仿真完成，结果已保存到 results.png 和 results.yaml")
    print("生成的配置已保存到 generated_config/components.yml")

if __name__ == "__main__":
    run_ai_modeling_simulation()