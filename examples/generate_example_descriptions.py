#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自然语言处理示例脚本

这个脚本演示了CHS-SDK的自然语言处理功能：
1. 配置文件到自然语言的转换
2. 自然语言到配置文件的转换
3. 支持所有四种配置文件类型

作者: CHS-SDK Team
版本: 1.0.0
创建时间: 2024
"""

import os
import sys
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from core_lib.nlp.config_to_language_converter import ConfigToLanguageConverter
from core_lib.nlp.language_to_config_converter import LanguageToConfigConverter
from core_lib.config.unified_config_manager import ConfigType

def demo_config_to_language():
    """演示配置文件到自然语言的转换"""
    print("=" * 60)
    print("配置文件到自然语言转换演示")
    print("=" * 60)
    
    converter = ConfigToLanguageConverter()
    
    # 示例配置文件路径
    example_configs = [
        "examples/watertank/base/config.yml",
        "examples/demo/unified_config.yml",
        "config/universal_config.yml"
    ]
    
    for config_path in example_configs:
        if os.path.exists(config_path):
            print(f"\n处理配置文件: {config_path}")
            print("-" * 40)
            
            try:
                # 转换为自然语言
                description = converter.convert_config_to_language(config_path)
                
                # 显示部分结果
                print(f"配置类型: {description.config_type}")
                print(f"仿真名称: {description.simulation_name}")
                print(f"建模描述: {description.modeling_description[:200]}...")
                print(f"情景描述: {description.scenario_description[:200]}...")
                
                # 保存完整描述
                output_file = f"reports/generated_description_{Path(config_path).stem}.md"
                converter.save_description_to_file(description, output_file)
                print(f"完整描述已保存到: {output_file}")
                
            except Exception as e:
                print(f"转换失败: {e}")
        else:
            print(f"配置文件不存在: {config_path}")

def demo_language_to_config():
    """演示自然语言到配置文件的转换"""
    print("\n" + "=" * 60)
    print("自然语言到配置文件转换演示")
    print("=" * 60)
    
    converter = LanguageToConfigConverter()
    
    # 示例自然语言描述
    example_descriptions = [
        {
            "name": "简单水库系统",
            "description": """
仿真名称：简单水库控制系统
仿真时长：3600秒
时间步长：1.0秒

系统组件：
- 水库1：水库，容量1000立方米，初始水位5米
- 闸门1：闸门，最大流量50立方米每秒
- 传感器1：传感器，监测水位

系统连接：
- 水库1连接闸门1

控制策略：
- 采用PID控制策略控制闸门开度
- 目标水位：5米

分析要求：
- 进行控制性能分析
- 生成水位变化图表
            """
        },
        {
            "name": "多组件水利系统",
            "description": """
仿真名称：复杂水利调度系统
仿真时长：7200秒
时间步长：0.5秒

系统统计：
- 水库：2个
- 闸门：3个
- 水泵：1个
- 传感器：4个

控制策略：
- 采用模型预测控制
- 优化目标：最小化能耗
- 约束条件：水位在安全范围内

分析要求：
- 系统辨识分析
- 优化性能评估
- 统计分析报告
            """
        }
    ]
    
    # 测试不同的配置类型
    config_types = [
        (ConfigType.UNIFIED_SINGLE, "unified"),
        (ConfigType.UNIVERSAL_CONFIG, "universal"),
        (ConfigType.TRADITIONAL_MULTI, "traditional"),
        (ConfigType.HARDCODED, "hardcoded")
    ]
    
    for desc_info in example_descriptions:
        print(f"\n处理描述: {desc_info['name']}")
        print("-" * 40)
        
        for config_type, type_name in config_types:
            try:
                output_dir = f"examples/converted/{desc_info['name'].replace(' ', '_')}_{type_name}"
                
                # 转换为配置文件
                config_data = converter.convert_language_to_config(
                    desc_info['description'],
                    config_type,
                    output_dir
                )
                
                print(f"  {type_name} 配置已生成到: {output_dir}")
                
            except Exception as e:
                print(f"  {type_name} 配置生成失败: {e}")

def demo_round_trip_conversion():
    """演示往返转换（配置->自然语言->配置）"""
    print("\n" + "=" * 60)
    print("往返转换演示（配置->自然语言->配置）")
    print("=" * 60)
    
    config_converter = ConfigToLanguageConverter()
    language_converter = LanguageToConfigConverter()
    
    # 选择一个示例配置文件
    original_config = "examples/watertank/base/config.yml"
    
    if os.path.exists(original_config):
        print(f"原始配置文件: {original_config}")
        
        try:
            # 第一步：配置文件 -> 自然语言
            print("\n第一步：配置文件转换为自然语言...")
            description = config_converter.convert_config_to_language(original_config)
            
            # 保存自然语言描述
            nl_file = "examples/converted/round_trip_description.md"
            config_converter.save_description_to_file(description, nl_file)
            print(f"自然语言描述已保存到: {nl_file}")
            
            # 第二步：自然语言 -> 配置文件
            print("\n第二步：自然语言转换为配置文件...")
            
            # 组合完整的描述文本
            full_description = f"""
{description.modeling_description}

{description.scenario_description}

{description.query_description}

{description.analysis_description}
            """
            
            # 生成新的配置文件
            new_config_data = language_converter.convert_language_to_config(
                full_description,
                ConfigType.UNIFIED_SINGLE,
                "examples/converted/round_trip_config"
            )
            
            print("往返转换完成！")
            print("原始配置 -> 自然语言 -> 新配置")
            print("可以比较原始配置和新生成的配置文件")
            
        except Exception as e:
            print(f"往返转换失败: {e}")
            import traceback
            traceback.print_exc()
    else:
        print(f"原始配置文件不存在: {original_config}")

def create_sample_descriptions():
    """创建示例自然语言描述文件"""
    print("\n" + "=" * 60)
    print("创建示例自然语言描述文件")
    print("=" * 60)
    
    # 确保输出目录存在
    output_dir = Path("examples/converted/sample_descriptions")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 示例描述
    samples = {
        "水库调度系统.txt": """
仿真名称：水库调度控制系统
仿真描述：模拟水库在不同入流条件下的调度控制过程
仿真时长：86400秒（24小时）
时间步长：60秒
求解器：rk4

系统组件：
- 主水库：水库，容量5000000立方米，初始水位120米，最大水位130米，最小水位100米
- 泄洪闸：闸门，最大流量1000立方米每秒，初始开度0%
- 发电机组：水轮机，额定功率50000千瓦，效率0.9
- 水位传感器：传感器，测量范围90-140米，精度0.01米
- 流量传感器：传感器，测量范围0-1200立方米每秒，精度0.1立方米每秒

系统连接：
- 主水库连接泄洪闸
- 主水库连接发电机组
- 水位传感器监测主水库
- 流量传感器监测泄洪闸出口

控制策略：
- 采用模型预测控制策略
- 控制目标：维持水位在安全范围内，同时最大化发电效益
- 预测时域：3600秒
- 控制时域：600秒

优化目标：
- 最大化发电量
- 最小化弃水量
- 确保防洪安全

分析要求：
- 控制性能分析：评估水位控制精度和响应时间
- 经济效益分析：计算发电收益和运行成本
- 安全性分析：评估极端工况下的系统响应
- 生成实时监控图表和历史趋势分析
        """,
        
        "灌区配水系统.txt": """
仿真名称：智能灌区配水系统
仿真描述：模拟大型灌区的智能化配水调度过程
仿真时长：604800秒（7天）
时间步长：300秒
求解器：adams

系统统计：
- 干渠：1条
- 支渠：5条
- 斗渠：20条
- 闸门：30个
- 水泵：8台
- 传感器：50个

主要组件：
- 总干渠：渠道，长度50公里，设计流量100立方米每秒
- 分水闸群：闸门组，包含5个主要分水闸
- 提水泵站：泵站，总装机容量2000千瓦
- 监测网络：传感器网络，实时监测各节点水位和流量

控制策略：
- 采用分层递阶控制
- 上层：全局优化调度
- 中层：区域协调控制
- 下层：局部反馈控制

优化目标：
- 满足各灌区用水需求
- 最小化输水损失
- 最小化能耗
- 保证供水公平性

智能化功能：
- 需水量预测
- 自适应调度
- 故障诊断
- 远程监控

分析要求：
- 供水效率分析
- 能耗优化分析
- 系统可靠性分析
- 用户满意度评估
        """,
        
        "城市排水系统.txt": """
仿真名称：城市智能排水防涝系统
仿真描述：模拟城市在暴雨条件下的排水防涝过程
仿真时长：21600秒（6小时）
时间步长：30秒
求解器：rk4

系统组件：
- 雨水收集系统：包含100个雨水口，总收集面积500平方公里
- 排水管网：管道网络，总长度1000公里，管径范围0.5-3米
- 泵站群：包含15个排水泵站，总排水能力5000立方米每秒
- 调蓄设施：包含8个调蓄池，总容量200万立方米
- 闸门系统：包含50个智能闸门，用于流量调节
- 监测系统：包含200个水位传感器和100个流量传感器

控制策略：
- 采用实时自适应控制
- 基于降雨预报的预见性控制
- 多目标协调优化控制

控制目标：
- 防止城市内涝
- 减少雨水溢流
- 优化泵站运行
- 保护水环境

智能化特性：
- 降雨预报集成
- 内涝风险预警
- 应急响应自动化
- 运行状态实时监控

分析要求：
- 防涝效果评估
- 系统运行效率分析
- 环境影响评价
- 应急响应能力评估
- 生成实时预警和调度建议
        """
    }
    
    # 保存示例文件
    for filename, content in samples.items():
        file_path = output_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content.strip())
        print(f"已创建示例描述文件: {file_path}")
    
    print(f"\n所有示例描述文件已保存到: {output_dir}")
    return output_dir

def test_sample_descriptions(sample_dir):
    """测试示例描述文件的转换"""
    print("\n" + "=" * 60)
    print("测试示例描述文件转换")
    print("=" * 60)
    
    converter = LanguageToConfigConverter()
    
    # 获取所有示例文件
    sample_files = list(Path(sample_dir).glob("*.txt"))
    
    for sample_file in sample_files:
        print(f"\n处理文件: {sample_file.name}")
        print("-" * 40)
        
        try:
            # 读取描述文件
            with open(sample_file, 'r', encoding='utf-8') as f:
                description = f.read()
            
            # 转换为不同类型的配置文件
            base_name = sample_file.stem
            
            # 统一配置文件
            unified_dir = f"examples/converted/{base_name}_unified"
            converter.convert_language_to_config(
                description, ConfigType.UNIFIED_SINGLE, unified_dir
            )
            print(f"  统一配置已生成: {unified_dir}")
            
            # 通用配置文件
            universal_dir = f"examples/converted/{base_name}_universal"
            converter.convert_language_to_config(
                description, ConfigType.UNIVERSAL_CONFIG, universal_dir
            )
            print(f"  通用配置已生成: {universal_dir}")
            
        except Exception as e:
            print(f"  转换失败: {e}")

def main():
    """主函数"""
    print("CHS-SDK 自然语言处理功能演示")
    print("=" * 60)
    
    # 确保必要的目录存在
    os.makedirs("examples/converted", exist_ok=True)
    os.makedirs("reports", exist_ok=True)
    
    try:
        # 1. 演示配置文件到自然语言的转换
        demo_config_to_language()
        
        # 2. 演示自然语言到配置文件的转换
        demo_language_to_config()
        
        # 3. 演示往返转换
        demo_round_trip_conversion()
        
        # 4. 创建示例描述文件
        sample_dir = create_sample_descriptions()
        
        # 5. 测试示例描述文件
        test_sample_descriptions(sample_dir)
        
        print("\n" + "=" * 60)
        print("所有演示完成！")
        print("生成的文件位于:")
        print("- examples/converted/ (转换后的配置文件)")
        print("- reports/ (自然语言描述报告)")
        print("=" * 60)
        
    except Exception as e:
        print(f"演示过程中出现错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-
"""
为examples目录下的示例生成自然语言描述报告
包含建模、情景、查询、分析四个维度的描述
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
import yaml
import json

# 添加项目根目录到路径
sys.path.append(str(Path(__file__).parent.parent))

class ExampleDescriptionGenerator:
    """示例描述生成器"""
    
    def __init__(self, examples_dir: str = None):
        self.examples_dir = Path(examples_dir) if examples_dir else Path(__file__).parent
        self.output_dir = Path(__file__).parent.parent / "reports"
        self.output_dir.mkdir(exist_ok=True)
        
        # 示例分类定义
        self.example_categories = {
            "agent_based": {
                "name": "智能体分布式控制系统",
                "description": "基于多智能体架构的分布式水利控制系统示例",
                "modeling_approach": "多智能体建模",
                "scenarios": ["分层控制", "事件驱动", "复杂网络", "应急接管", "扰动处理"]
            },
            "canal_model": {
                "name": "渠道系统建模与控制",
                "description": "渠道水力学建模和控制算法示例",
                "modeling_approach": "水力学建模",
                "scenarios": ["PID控制", "MPC控制", "故障场景", "分层分布式控制"]
            },
            "mission_example_1": {
                "name": "任务场景1：基础仿真与控制",
                "description": "从基础仿真到高级控制的渐进式示例",
                "modeling_approach": "渐进式建模",
                "scenarios": ["基础仿真", "高级控制", "容错控制", "数字孪生", "中央MPC调度"]
            },
            "mission_example_2": {
                "name": "任务场景2：流域协调控制",
                "description": "流域级别的协调控制示例",
                "modeling_approach": "流域建模",
                "scenarios": ["本地控制", "分层控制", "流域协调"]
            },
            "distributed_digital_twin_simulation": {
                "name": "分布式数字孪生仿真",
                "description": "分布式数字孪生系统的扰动分析和控制验证",
                "modeling_approach": "数字孪生建模",
                "scenarios": ["扰动分析", "参数辨识", "控制验证", "性能优化"]
            },
            "identification": {
                "name": "参数辨识示例",
                "description": "水利系统关键参数的辨识方法示例",
                "modeling_approach": "参数辨识建模",
                "scenarios": ["水库库容曲线", "闸门流量系数", "管道糙率"]
            }
        }
    
    def generate_category_description(self, category_key: str, category_info: Dict[str, Any]) -> Dict[str, str]:
        """为单个示例类别生成描述"""
        
        # 建模维度描述
        modeling_description = self._generate_modeling_description(category_key, category_info)
        
        # 情景维度描述
        scenario_description = self._generate_scenario_description(category_key, category_info)
        
        # 查询维度描述
        query_description = self._generate_query_description(category_key, category_info)
        
        # 分析维度描述
        analysis_description = self._generate_analysis_description(category_key, category_info)
        
        return {
            "modeling": modeling_description,
            "scenario": scenario_description,
            "query": query_description,
            "analysis": analysis_description
        }
    
    def _generate_modeling_description(self, category_key: str, category_info: Dict[str, Any]) -> str:
        """生成建模维度描述"""
        modeling_templates = {
            "agent_based": """
### 建模方法

**多智能体分布式建模**

本示例采用多智能体架构对水利系统进行建模，将复杂的水利控制系统分解为多个自主智能体：

1. **物理智能体**：负责水利设施的物理建模，包括水库、闸门、渠道等水工建筑物的水力学行为
2. **控制智能体**：实现各种控制算法，如PID控制、MPC控制等
3. **监控智能体**：负责系统状态监测和数据采集
4. **协调智能体**：实现多个控制单元之间的协调和调度

**建模特点**：
- 分布式架构，每个智能体具有自主决策能力
- 基于消息传递的通信机制
- 支持动态重构和故障恢复
- 可扩展的层次化结构
""",
            "canal_model": """
### 建模方法

**渠道水力学建模**

本示例基于一维水力学方程对渠道系统进行建模：

1. **连续性方程**：描述水量守恒
2. **动量方程**：描述水流运动规律
3. **边界条件**：定义上下游边界
4. **初始条件**：设定系统初始状态

**建模特点**：
- 基于物理原理的精确建模
- 考虑渠道几何特性和糙率
- 支持非恒定流计算
- 适用于复杂渠系建模
""",
            "mission_example_1": """
### 建模方法

**渐进式系统建模**

本示例采用从简单到复杂的渐进式建模方法：

1. **基础物理建模**：建立水利设施的基本物理模型
2. **控制系统建模**：添加控制算法和反馈机制
3. **故障建模**：引入故障场景和异常处理
4. **数字孪生建模**：构建高保真数字孪生系统
5. **优化调度建模**：实现系统级优化调度

**建模特点**：
- 循序渐进的复杂度递增
- 模块化设计便于理解
- 每个阶段都有明确的学习目标
- 支持不同层次的应用需求
""",
            "mission_example_2": """
### 建模方法

**流域级协调建模**

本示例针对流域级水利系统进行协调控制建模：

1. **流域拓扑建模**：建立流域内各水利设施的连接关系
2. **多尺度建模**：结合局部详细模型和全局简化模型
3. **协调机制建模**：设计多级协调控制架构
4. **约束建模**：考虑水资源分配和环境约束

**建模特点**：
- 大尺度系统建模
- 多目标优化考虑
- 分层分布式架构
- 实时协调决策
""",
            "distributed_digital_twin_simulation": """
### 建模方法

**分布式数字孪生建模**

本示例构建分布式数字孪生系统：

1. **物理系统建模**：高保真物理模型
2. **数字孪生建模**：实时同步的数字副本
3. **扰动建模**：各种扰动和不确定性建模
4. **预测建模**：基于数据驱动的预测模型

**建模特点**：
- 物理-数字双向映射
- 实时状态同步
- 扰动感知和适应
- 预测性维护支持
""",
            "identification": """
### 建模方法

**参数辨识建模**

本示例专注于水利系统关键参数的辨识：

1. **参数化建模**：建立含待辨识参数的数学模型
2. **观测建模**：设计观测方程和测量模型
3. **辨识算法建模**：实现各种参数辨识算法
4. **验证建模**：建立参数验证和评估机制

**建模特点**：
- 基于观测数据的参数估计
- 多种辨识算法支持
- 参数不确定性量化
- 在线辨识能力
"""
        }
        
        return modeling_templates.get(category_key, f"### 建模方法\n\n{category_info['modeling_approach']}建模方法的详细描述。")
    
    def _generate_scenario_description(self, category_key: str, category_info: Dict[str, Any]) -> str:
        """生成情景维度描述"""
        scenarios = category_info.get('scenarios', [])
        
        scenario_desc = f"### 仿真情景\n\n**{category_info['name']}**包含以下主要仿真情景：\n\n"
        
        for i, scenario in enumerate(scenarios, 1):
            scenario_desc += f"{i}. **{scenario}**：针对{scenario}的专门仿真场景\n"
        
        scenario_desc += "\n每个情景都设计了特定的初始条件、边界条件和扰动输入，以验证系统在不同工况下的性能表现。"
        
        return scenario_desc
    
    def _generate_query_description(self, category_key: str, category_info: Dict[str, Any]) -> str:
        """生成查询维度描述"""
        query_templates = {
            "agent_based": """
### 典型查询问题

1. **系统性能查询**
   - 各智能体的响应时间如何？
   - 系统的协调效率如何评估？
   - 在故障情况下系统如何重构？

2. **控制效果查询**
   - PID控制与MPC控制的性能对比？
   - 分布式控制相比集中式控制的优势？
   - 系统的鲁棒性如何？

3. **扩展性查询**
   - 如何添加新的智能体？
   - 系统支持的最大规模是多少？
   - 通信延迟对系统性能的影响？
""",
            "canal_model": """
### 典型查询问题

1. **水力学性能查询**
   - 渠道的水位变化规律？
   - 流量调节的响应特性？
   - 不同控制策略的效果对比？

2. **控制系统查询**
   - PID参数如何优化？
   - MPC控制的预测精度？
   - 控制系统的稳定性分析？

3. **故障处理查询**
   - 传感器故障如何检测？
   - 执行器故障的应对策略？
   - 系统的容错能力评估？
"""
        }
        
        return query_templates.get(category_key, """
### 典型查询问题

1. **系统性能查询**：关于系统运行性能的各种问题
2. **控制效果查询**：关于控制算法效果的分析问题
3. **参数优化查询**：关于参数调优和系统优化的问题
""")
    
    def _generate_analysis_description(self, category_key: str, category_info: Dict[str, Any]) -> str:
        """生成分析维度描述"""
        analysis_templates = {
            "agent_based": """
### 分析方法与结果

**性能分析**
- 响应时间分析：统计各智能体的平均响应时间和最大响应时间
- 通信效率分析：分析消息传递的延迟和成功率
- 资源利用率分析：评估计算资源和网络资源的使用情况

**控制效果分析**
- 控制精度分析：计算控制误差的均值、方差和最大值
- 稳定性分析：评估系统的稳定裕度和鲁棒性
- 协调效果分析：分析多智能体协调的一致性和效率

**故障恢复分析**
- 故障检测时间：统计故障检测的平均时间
- 恢复时间分析：分析系统从故障中恢复的时间
- 降级运行分析：评估系统在部分故障下的运行能力
""",
            "canal_model": """
### 分析方法与结果

**水力学分析**
- 水位波动分析：分析水位变化的幅度和频率特性
- 流量调节分析：评估流量控制的精度和响应速度
- 水力学稳定性：分析渠道系统的水力学稳定条件

**控制性能分析**
- PID控制分析：分析PID控制器的调节时间、超调量和稳态误差
- MPC控制分析：评估模型预测控制的预测精度和优化效果
- 控制策略对比：比较不同控制策略的优缺点

**鲁棒性分析**
- 参数敏感性分析：分析系统对参数变化的敏感程度
- 扰动抑制分析：评估系统对外部扰动的抑制能力
- 模型不确定性分析：分析模型误差对控制效果的影响
"""
        }
        
        return analysis_templates.get(category_key, """
### 分析方法与结果

**性能指标分析**：对系统关键性能指标进行定量分析
**对比分析**：不同方法或策略之间的对比评估
**敏感性分析**：参数变化对系统性能的影响分析
**优化建议**：基于分析结果提出的改进建议
""")
    
    def generate_comprehensive_report(self) -> str:
        """生成综合报告"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report_content = f"""
# CHS-SDK 示例系统自然语言描述报告

**生成时间**: {timestamp}  
**版本**: 1.0  
**作者**: CHS-SDK 自动生成系统  

## 概述

本报告为CHS-SDK水利系统仿真平台的示例系统提供详细的自然语言描述，涵盖建模方法、仿真情景、典型查询和分析结果四个维度。这些示例展示了平台在不同应用场景下的能力和特点。

## 示例分类概览

"""
        
        # 生成每个类别的描述
        for category_key, category_info in self.example_categories.items():
            if self._check_category_exists(category_key):
                report_content += f"\n## {category_info['name']}\n\n"
                report_content += f"**描述**: {category_info['description']}\n\n"
                
                descriptions = self.generate_category_description(category_key, category_info)
                
                for dimension, content in descriptions.items():
                    report_content += content + "\n\n"
                
                report_content += "---\n\n"
        
        # 添加总结
        report_content += """
## 总结

通过以上示例的详细描述，我们可以看到CHS-SDK平台具有以下特点：

1. **多样化的建模方法**：支持从简单的物理建模到复杂的多智能体建模
2. **丰富的仿真情景**：涵盖正常运行、故障处理、优化调度等多种场景
3. **灵活的查询机制**：支持各种性能分析和系统评估查询
4. **全面的分析能力**：提供定量分析、对比评估和优化建议

这些示例为用户学习和应用CHS-SDK平台提供了完整的参考和指导。

---

*本报告由CHS-SDK自动生成系统创建*
"""
        
        return report_content
    
    def _check_category_exists(self, category_key: str) -> bool:
        """检查示例类别是否存在"""
        category_path = self.examples_dir / category_key
        return category_path.exists() and category_path.is_dir()
    
    def save_report(self, content: str, filename: str = None) -> str:
        """保存报告到文件"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"examples_natural_language_descriptions_{timestamp}.md"
        
        report_path = self.output_dir / filename
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return str(report_path)
    
    def run(self):
        """运行描述生成器"""
        print("🚀 开始生成示例自然语言描述报告...")
        
        # 生成综合报告
        report_content = self.generate_comprehensive_report()
        
        # 保存报告
        report_path = self.save_report(report_content)
        
        print(f"✅ 报告生成完成: {report_path}")
        print(f"📊 包含示例类别数: {len([k for k in self.example_categories.keys() if self._check_category_exists(k)])}")
        
        return report_path

if __name__ == "__main__":
    generator = ExampleDescriptionGenerator()
    report_path = generator.run()
    print(f"\n📁 报告文件: {report_path}")