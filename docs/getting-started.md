# 快速开始指南

## 简介

CHS-SDK Examples是CHS-SDK产品的官方示例库，包含丰富的示例应用，帮助用户快速上手和使用CHS-SDK的各种功能。

## 安装步骤

### 1. 环境要求
- Python 3.8或更高版本
- pip包管理器
- Node.js 14+ (仅Web演示需要)

### 2. 克隆仓库
```bash
git clone https://github.com/your-username/chs-examples.git
cd chs-examples
```

### 3. 安装依赖
```bash
# 安装核心依赖
pip install -r requirements.txt

# 安装Web演示依赖（可选）
cd web-demo
pip install -r requirements.txt
cd frontend
npm install
```

## 运行示例

### 命令行运行
```bash
# 运行基础仿真示例
cd examples/basic-simulation
python run.py

# 运行智能体控制示例
cd examples/agent-control
python run.py

# 运行AI建模示例
cd examples/ai-modeling
python run.py
```

### Web演示运行
```bash
# 启动后端服务
cd web-demo/backend
uvicorn main:app --reload

# 启动前端开发服务器
cd web-demo/frontend
npm run dev
```

## 示例说明

### 基础仿真示例
演示如何使用CHS-SDK进行基础的水系统仿真，包括水库、管道和闸门等基本组件的配置和运行。

### 智能体控制示例
演示如何使用CHS-SDK的多智能体系统(MAS)来控制水系统，包括感知智能体、控制智能体和中央协调智能体的配置和协同工作。

### AI建模示例
演示如何使用CHS-SDK集成的大语言模型(LLM)进行自然语言建模，通过自然语言描述快速构建水系统仿真场景。

## 项目结构

```
chs-examples/
├── examples/                    # 示例应用目录
│   ├── basic-simulation/       # 基础仿真示例
│   ├── agent-control/          # 智能体控制示例
│   └── ai-modeling/            # AI建模示例
├── docs/                       # 文档目录
├── templates/                  # 模板目录
├── web-demo/                   # Web演示应用
├── scripts/                    # 工具脚本
└── tests/                      # 示例测试
```

## 常见问题

### 1. 安装依赖时出现错误
确保使用Python 3.8或更高版本，并尝试升级pip：
```bash
pip install --upgrade pip
```

### 2. 运行示例时找不到模块
确保已正确安装CHS-SDK及其子产品：
```bash
pip install chs-core chs-agent chs-ai chs-analyze
```

### 3. Web演示无法启动
确保已安装所有前端依赖：
```bash
cd web-demo/frontend
npm install
```

## 下一步

- 查看[详细教程](tutorials.md)了解更高级的功能
- 参考[API文档](api-reference.md)了解完整的接口说明
- 阅读[最佳实践](best-practices.md)获取开发建议