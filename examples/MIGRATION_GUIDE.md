# CHS-SDK 配置迁移指南

## 概述

本指南帮助您将现有的传统配置文件迁移到新的通用配置系统。通用配置系统提供了更丰富的功能、更好的标准化和更强的可扩展性。

## 迁移优势

### 🚀 功能增强
- **调试功能**: 集成数据收集、Web仪表板、控制台监控
- **性能监控**: 自动跟踪时间、内存、CPU使用情况
- **可视化**: 自动生成多种类型的图表和仪表板
- **智能分析**: 控制性能分析、统计分析、系统识别
- **日志管理**: 多级别、多处理器、结构化日志
- **错误处理**: 分类处理、恢复策略、通知机制

### 📊 标准化结构
- 统一的配置文件格式
- 模块化设计，易于维护
- 向后兼容现有配置
- 支持多环境配置

### 🔧 易于使用
- 简单的API接口
- 丰富的示例和文档
- 自动化配置验证
- 智能默认值

## 迁移步骤

### 步骤1：了解现有配置

首先分析您现有的配置文件结构：

```yaml
# 传统配置示例 (config.yml)
simulation:
  duration: 100.0
  time_step: 1.0
  output_interval: 5.0

debug:
  log_level: INFO
  enable_performance_monitoring: true

output:
  save_results: true
  plot_results: true
```

### 步骤2：创建通用配置文件

基于 `universal_config_template.yml` 创建新的配置文件：

```yaml
# 新的通用配置 (universal_config.yml)
simulation:
  name: "您的仿真名称"
  description: "仿真描述"
  time:
    end_time: 100.0      # 对应原配置的 duration
    time_step: 1.0       # 对应原配置的 time_step
    output_interval: 5.0 # 对应原配置的 output_interval

debug:
  enabled: true
  log_level: "INFO"     # 对应原配置
  data_collection:
    enabled: true       # 对应原配置的 enable_performance_monitoring

visualization:
  enabled: true
  plots:
    enabled: true       # 对应原配置的 plot_results

output:
  enabled: true
  save_history: true    # 对应原配置的 save_results
```

### 步骤3：更新运行脚本

将原有的运行脚本更新为使用新的配置系统：

```python
# 原有方式
from core_lib.io.yaml_loader import SimulationBuilder

builder = SimulationBuilder(scenario_path="path/to/scenario")
simulation = builder.build_simulation()
results = simulation.run()

# 新的方式
from core_lib.config.enhanced_yaml_loader import load_universal_config

builder = load_universal_config(
    config_file="universal_config.yml",
    scenario_path="path/to/scenario"
)
results = builder.run_enhanced_simulation()
```

### 步骤4：验证迁移结果

运行测试确保迁移成功：

```bash
python run_universal_config.py
```

## 配置映射表

### 基础仿真配置

| 原配置 | 新配置 | 说明 |
|--------|--------|------|
| `simulation.duration` | `simulation.time.end_time` | 仿真持续时间 |
| `simulation.dt` | `simulation.time.time_step` | 时间步长 |
| `simulation.output_interval` | `simulation.time.output_interval` | 输出间隔 |

### 调试配置

| 原配置 | 新配置 | 说明 |
|--------|--------|------|
| `debug.log_level` | `debug.log_level` | 日志级别 |
| `debug.log_file` | `debug.log_file` | 日志文件 |
| `debug.enable_performance_monitoring` | `performance.enabled` | 性能监控 |
| `debug.enable_data_collection` | `debug.data_collection.enabled` | 数据收集 |
| `debug.data_collection_interval` | `debug.data_collection.interval` | 收集间隔 |
| `debug.session_id` | `debug.session_id` | 会话ID |

### 输出配置

| 原配置 | 新配置 | 说明 |
|--------|--------|------|
| `output.save_results` | `output.save_history` | 保存结果 |
| `output.output_directory` | `output.output_directory` | 输出目录 |
| `output.plot_results` | `visualization.plots.enabled` | 生成图表 |
| `output.save_plots` | `visualization.plots.save_plots` | 保存图表 |
| `output.variables_to_plot` | `visualization.plots.charts[].variables` | 绘图变量 |

### 验证配置

| 原配置 | 新配置 | 说明 |
|--------|--------|------|
| `validation.enable` | `output.validation.enabled` | 启用验证 |
| `validation.expected_results` | `output.validation.expected_results` | 期望结果 |
| `validation.tolerance` | `output.validation.tolerance` | 容差 |

## 示例迁移

### Example 1: 基础物理仿真

**原配置文件**: `mission/example_1/config.yml`
**新配置文件**: `mission/example_1/universal_config.yml`
**运行脚本**: `mission/example_1/run_universal_config.py`

主要改进：
- 增加了详细的调试和监控功能
- 自动生成多种类型的图表
- 集成性能分析和报告生成
- 支持实时可视化

### Example 2: 闭环控制系统

**原配置文件**: `mission/example_2/config_2_1.yml`
**新配置文件**: `mission/example_2/universal_config.yml`

主要改进：
- 增加了控制性能分析
- 支持实时控制仪表板
- 集成系统识别功能
- 增强的错误处理和恢复机制
- 专门的控制系统日志

## 迁移检查清单

### ✅ 迁移前准备
- [ ] 备份现有配置文件
- [ ] 了解现有配置的功能需求
- [ ] 确定需要启用的新功能
- [ ] 准备测试数据和验证标准

### ✅ 配置文件迁移
- [ ] 创建新的通用配置文件
- [ ] 映射所有现有配置项
- [ ] 配置新增的功能模块
- [ ] 设置合适的日志级别和输出格式
- [ ] 配置可视化和分析功能

### ✅ 代码更新
- [ ] 更新导入语句
- [ ] 修改配置加载方式
- [ ] 更新运行脚本
- [ ] 添加错误处理

### ✅ 测试验证
- [ ] 运行基础功能测试
- [ ] 验证输出结果一致性
- [ ] 测试新增功能
- [ ] 检查日志和报告生成
- [ ] 性能对比测试

### ✅ 文档更新
- [ ] 更新README文件
- [ ] 添加配置说明
- [ ] 更新使用示例
- [ ] 记录迁移过程和注意事项

## 常见问题

### Q1: 迁移后性能是否会受影响？

**A**: 通用配置系统经过优化，性能影响很小。新增的监控和分析功能可以按需启用，不会显著影响仿真性能。

### Q2: 是否需要修改现有的组件和智能体代码？

**A**: 不需要。通用配置系统与现有的组件和智能体完全兼容，只需要更新配置文件和运行脚本。

### Q3: 如何处理自定义配置项？

**A**: 可以在通用配置文件中添加自定义配置节，或者使用 `environment.variables.custom_vars` 来定义自定义变量。

### Q4: 迁移后如何调试问题？

**A**: 新系统提供了更强大的调试功能：
- 启用 `debug.dashboard.web_dashboard` 获得实时监控
- 查看详细的日志文件
- 使用自动生成的分析报告
- 利用性能监控功能定位瓶颈

### Q5: 是否可以逐步迁移？

**A**: 是的。您可以：
1. 先创建通用配置文件，保留原有运行方式
2. 逐步启用新功能进行测试
3. 最后完全切换到新的运行方式

## 技术支持

如果在迁移过程中遇到问题，可以：

1. **查看示例**: 参考 `mission/example_1` 和 `mission/example_2` 中的迁移示例
2. **阅读文档**: 查看 `core_lib/config/README.md` 获取详细说明
3. **运行测试**: 使用 `test_universal_config.py` 验证系统功能
4. **查看日志**: 启用详细日志获取调试信息

## 最佳实践

### 1. 配置管理
- 为不同环境创建不同的配置文件
- 使用版本控制管理配置文件
- 定期备份重要配置

### 2. 功能使用
- 开发阶段启用详细调试和监控
- 生产环境优化性能设置
- 根据需要选择性启用功能模块

### 3. 监控和分析
- 定期查看性能报告
- 利用可视化功能分析结果
- 设置合适的错误处理策略

### 4. 文档维护
- 记录配置变更历史
- 维护配置说明文档
- 分享最佳实践经验

---

通过遵循本迁移指南，您可以顺利地将现有项目迁移到新的通用配置系统，并享受更强大的功能和更好的开发体验。