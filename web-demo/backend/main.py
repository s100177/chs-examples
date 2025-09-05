"""
CHS-SDK Web演示应用后端主程序
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import os
import sys

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = FastAPI(
    title="CHS-SDK Web演示应用API",
    description="CHS-SDK水系统仿真平台的Web演示应用后端API",
    version="0.1.0"
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 数据模型
class SimulationRequest(BaseModel):
    example_id: str
    parameters: Dict[str, Any] = {}

class SimulationResponse(BaseModel):
    simulation_id: str
    status: str
    message: str

class ExampleInfo(BaseModel):
    id: str
    name: str
    description: str
    category: str

# API路由
@app.get("/")
async def root():
    """根路径"""
    return {"message": "欢迎使用CHS-SDK Web演示应用API"}

@app.get("/api/examples", response_model=List[ExampleInfo])
async def get_examples():
    """获取示例列表"""
    examples = [
        ExampleInfo(
            id="basic-reservoir",
            name="基础水库仿真",
            description="演示基础水库仿真的配置和运行",
            category="基础仿真"
        ),
        ExampleInfo(
            id="agent-control",
            name="智能体控制",
            description="演示多智能体协同控制水系统",
            category="智能体控制"
        ),
        ExampleInfo(
            id="ai-modeling",
            name="AI建模",
            description="演示使用大语言模型进行自然语言建模",
            category="AI建模"
        )
    ]
    return examples

@app.post("/api/simulate", response_model=SimulationResponse)
async def run_simulation(request: SimulationRequest):
    """运行仿真"""
    # 这里应该调用CHS-SDK的实际仿真功能
    # 暂时返回模拟响应
    return SimulationResponse(
        simulation_id="sim_12345",
        status="running",
        message=f"开始运行示例 {request.example_id}"
    )

@app.get("/api/results/{simulation_id}")
async def get_results(simulation_id: str):
    """获取仿真结果"""
    # 这里应该返回实际的仿真结果
    return {
        "simulation_id": simulation_id,
        "status": "completed",
        "results": {
            "data": [
                {"time": 0, "value": 100},
                {"time": 1, "value": 105},
                {"time": 2, "value": 110}
            ]
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)