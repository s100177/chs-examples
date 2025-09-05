# CHS-SDK Examples

CHS-SDK示例应用集合，帮助用户快速上手和使用CHS-SDK。

## 项目介绍

CHS-SDK Examples是CHS-SDK产品的官方示例库，包含丰富的示例应用，展示如何使用CHS-SDK的各种功能。本项目旨在为用户提供完整的学习路径，从基础仿真到高级AI建模，帮助用户掌握CHS-SDK的强大功能。

## 目录结构

```
chs-examples/
├── examples/               # 示例应用目录
│   ├── basic-simulation/   # 基础仿真示例
│   ├── agent-control/      # 智能体控制示例
│   └── ai-modeling/        # AI建模示例
├── docs/                   # 文档目录
├── templates/              # 模板目录
├── web-demo/               # Web演示应用
│   ├── frontend/           # 前端代码 (React)
│   └── backend/            # 后端API (FastAPI)
├── scripts/                # 工具脚本
├── tests/                  # 示例测试
└── README.md               # 项目说明
```

## 快速开始

### 前置条件
- Python 3.8+
- Node.js 14+ (仅Web演示需要)

### 安装依赖
```bash
# 克隆仓库
git clone <repository-url>
cd chs-examples

# 安装Python依赖
pip install -r requirements.txt

# 安装Web演示前端依赖 (可选)
cd web-demo/frontend
npm install
cd ../..
```

### 运行示例
```bash
# 列出所有可用示例
python scripts/run-example.py --list

# 运行基础仿真示例
python scripts/run-example.py basic-simulation

# 运行智能体控制示例
python scripts/run-example.py agent-control

# 运行AI建模示例
python scripts/run-example.py ai-modeling
```

### 运行Web演示
```bash
# 启动后端API服务
cd web-demo/backend
uvicorn main:app --reload

# 在新终端中启动前端开发服务器
cd web-demo/frontend
npm run dev

# 访问 http://localhost:3000 查看Web演示
```

## 示例列表

### 基础仿真示例
展示如何使用CHS-SDK进行基础的水系统仿真，包括水库、管道和闸门等基本组件的配置和运行。

### 智能体控制示例
演示如何使用CHS-SDK的多智能体系统(MAS)来控制水系统，包括感知智能体、控制智能体和中央协调智能体的配置和协同工作。

### AI建模示例
展示如何使用CHS-SDK集成的大语言模型(LLM)进行自然语言建模，通过自然语言描述快速构建水系统仿真场景。

## 文档资源

- [快速开始指南](docs/getting-started.md) - 完整的安装和运行说明
- [详细教程](docs/tutorials.md) - 分步教程和最佳实践
- [API参考](docs/api-reference.md) - 完整的API文档

## 贡献指南

欢迎贡献新的示例！请参考[贡献指南](CONTRIBUTING.md)了解详情。

## 许可证

本项目采用MIT许可证，详情请见[LICENSE](LICENSE)文件。

## 贡献指南

欢迎贡献新的示例！请参考[贡献指南](CONTRIBUTING.md)了解详情。

## 许可证

本项目采用MIT许可证，详情请见[LICENSE](LICENSE)文件。