# 贡献指南

感谢您对CHS-SDK Examples项目的关注！我们欢迎各种形式的贡献。

## 贡献方式

### 1. 报告问题
如果您发现bug或有功能建议，请在GitHub Issues中提交。

### 2. 贡献代码
1. Fork本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

### 3. 改进文档
您可以通过提交PR来改进文档或添加新的示例。

### 4. 添加示例
您可以创建新的示例来展示CHS-SDK的功能。请参考[示例模板](../templates/example-template/)。

## 示例贡献规范

### 示例结构
每个示例应包含以下文件：
```
example-name/
├── config/              # 配置文件目录
│   ├── components.yml   # 组件配置
│   ├── topology.yml     # 拓扑配置
│   ├── agents.yml       # 智能体配置
│   └── config.yml       # 仿真配置
├── data/                # 数据文件目录（可选）
├── results/             # 结果文件目录（可选）
├── README.md            # 示例说明
└── run.py               # 运行脚本
```

### README.md模板
```markdown
# 示例名称

## 简介
简要介绍示例的目的和功能。

## 使用方法
说明如何运行该示例。

## 配置说明
解释关键配置项的含义。

## 结果展示
展示仿真结果和分析。

## 扩展示例
提供可以扩展和修改的建议。
```

## 代码规范

### Python代码规范
- 遵循PEP 8规范
- 使用类型提示
- 编写必要的注释
- 保持代码简洁易读

### 提交信息规范
- 使用英文编写提交信息
- 首字母大写
- 使用祈使句
- 包含相关issue编号（如果适用）

## 测试

请确保您的贡献包含适当的测试，并且所有现有测试都能通过。

```bash
# 运行所有测试
pytest tests/

# 运行特定测试
pytest tests/test_examples.py
```

## 文档

请确保为您的贡献添加适当的文档：
- 更新README.md文件
- 添加必要的教程文档
- 更新API文档（如果适用）

## 问题和讨论

如有任何问题，请在GitHub Issues中提出。