# CHS-SDK Web演示应用

CHS-SDK的Web演示应用，提供交互式界面来运行和展示各种水系统仿真示例。

## 功能特性

- 可视化建模界面
- 实时仿真结果展示
- 多种示例场景展示
- 交互式参数调整
- 结果导出功能

## 技术栈

- 前端: React + TypeScript
- 后端: FastAPI + Python
- 仿真引擎: CHS-SDK
- 可视化: D3.js + Chart.js

## 目录结构

```
web-demo/
├── frontend/          # 前端代码
├── backend/           # 后端API
├── public/            # 静态资源
└── README.md
```

## 安装与运行

### 前置条件
- Python 3.8+
- Node.js 14+

### 安装依赖
```bash
# 安装Python依赖
pip install -r requirements.txt

# 安装前端依赖
cd frontend
npm install
```

### 运行应用
```bash
# 启动后端服务
cd backend
uvicorn main:app --reload

# 启动前端开发服务器
cd frontend
npm run dev
```

## API接口

### 仿真控制
- `POST /api/simulate` - 运行仿真
- `GET /api/examples` - 获取示例列表
- `GET /api/examples/{id}` - 获取示例详情

### 结果查询
- `GET /api/results/{simulation_id}` - 获取仿真结果
- `GET /api/results/{simulation_id}/chart` - 获取图表数据

## 开发指南

请参考[开发者指南](docs/development.md)了解如何扩展Web应用功能。