# CHS-SDK Examples 教程

## 1. 基础仿真教程

### 1.1 创建简单的水库仿真

本教程将指导您创建一个简单的水库仿真系统。

#### 步骤1：定义物理组件
在[components.yml](../examples/basic-simulation/config/components.yml)中定义水库组件：

```yaml
reservoir_1:
  type: "Reservoir"
  parameters:
    name: "主水库"
    initial_level: 100.0
    capacity_curve: [[0, 1000000], [100, 2000000]]
```

#### 步骤2：定义连接关系
在[topology.yml](../examples/basic-simulation/config/topology.yml)中定义组件连接：

```yaml
connections:
  - from: reservoir_1
    to: downstream
    type: "outflow"
```

#### 步骤3：配置仿真参数
在[config.yml](../examples/basic-simulation/config/config.yml)中设置仿真参数：

```yaml
simulation:
  duration: 24
  time_step: 1
```

#### 步骤4：运行仿真
执行运行脚本：
```bash
cd examples/basic-simulation
python run.py
```

### 1.2 分析仿真结果

运行完成后，您将获得：
- 水库水位变化图表
- 数值结果文件(results.yaml)
- 仿真过程日志

## 2. 智能体控制教程

### 2.1 构建多智能体系统

本教程将指导您构建一个包含感知智能体和控制智能体的多智能体系统。

#### 步骤1：定义智能体
在[agents.yml](../examples/agent-control/config/agents.yml)中定义感知智能体：

```yaml
reservoir_1_perception:
  type: "ReservoirPerceptionAgent"
  parameters:
    name: "主水库感知智能体"
    model_id: "reservoir_1"
    publish_topic: "reservoir_1/state"
```

#### 步骤2：定义控制智能体
在同一个文件中定义控制智能体：

```yaml
gate_control:
  type: "GateControlAgent"
  parameters:
    name: "闸门控制智能体"
    model_id: "gate_1"
    subscribe_topics: 
      - "reservoir_1/state"
    control_strategy: "pid"
```

#### 步骤3：运行多智能体仿真
```bash
cd examples/agent-control
python run.py
```

### 2.2 监控智能体交互

通过查看消息交互图表，您可以了解：
- 智能体间通信频率
- 控制指令传递过程
- 系统响应时间

## 3. AI建模教程

### 3.1 使用自然语言建模

本教程将指导您使用自然语言描述创建水系统仿真。

#### 步骤1：编写自然语言描述
创建[natural_language_prompt.txt](../examples/ai-modeling/natural_language_prompt.txt)文件：

```
创建一个包含上游水库、输水管道和下游水库的水系统仿真场景...
```

#### 步骤2：运行AI建模示例
```bash
cd examples/ai-modeling
python run.py
```

#### 步骤3：查看生成的配置
检查[generated_config/](../examples/ai-modeling/generated_config/)目录中的自动生成配置。

### 3.2 自定义LLM提示

您可以通过修改自然语言描述来定制生成的系统：
- 指定不同的组件类型
- 设置特定的初始条件
- 定义控制目标

## 4. Web演示应用教程

### 4.1 启动Web应用

#### 启动后端服务
```bash
cd web-demo/backend
uvicorn main:app --reload
```

#### 启动前端应用
```bash
cd web-demo/frontend
npm run dev
```

### 4.2 使用Web界面

1. 打开浏览器访问 http://localhost:3000
2. 选择示例场景
3. 点击"运行示例"按钮
4. 查看实时仿真结果

### 4.3 扩展Web功能

#### 添加新的示例
1. 在[examples/](../examples/)目录中创建新的示例目录
2. 实现示例的运行逻辑
3. 在Web后端API中注册新的示例

#### 自定义可视化
1. 修改[App.jsx](../web-demo/frontend/src/App.jsx)文件
2. 添加新的图表组件
3. 实现数据可视化功能

## 5. 高级主题

### 5.1 创建自定义组件

1. 继承基础组件类
2. 实现必要的接口方法
3. 注册组件到系统中

### 5.2 实现自定义控制策略

1. 创建新的智能体类
2. 实现控制算法
3. 配置智能体参数

### 5.3 集成外部数据源

1. 创建数据接入智能体
2. 实现数据解析逻辑
3. 配置数据订阅关系

## 6. 故障排除

### 6.1 常见错误及解决方案

#### 错误：ModuleNotFoundError
解决方案：确保已安装所有依赖包

#### 错误：配置文件格式错误
解决方案：检查YAML语法是否正确

#### 错误：仿真结果异常
解决方案：检查组件参数设置是否合理

### 6.2 性能优化建议

1. 合理设置仿真时间步长
2. 优化组件计算逻辑
3. 减少不必要的日志输出

## 7. 最佳实践

### 7.1 配置管理
- 使用版本控制管理配置文件
- 为不同场景创建独立的配置目录
- 使用模板简化重复配置

### 7.2 代码组织
- 遵循模块化设计原则
- 保持代码简洁易读
- 添加必要的注释说明

### 7.3 测试验证
- 为关键功能编写测试用例
- 验证仿真结果的合理性
- 定期运行回归测试