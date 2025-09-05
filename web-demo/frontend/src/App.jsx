import React, { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [examples, setExamples] = useState([])
  const [selectedExample, setSelectedExample] = useState(null)
  const [simulationResult, setSimulationResult] = useState(null)

  // 获取示例列表
  useEffect(() => {
    // 模拟API调用
    const mockExamples = [
      {
        id: "basic-reservoir",
        name: "基础水库仿真",
        description: "演示基础水库仿真的配置和运行",
        category: "基础仿真"
      },
      {
        id: "agent-control",
        name: "智能体控制",
        description: "演示多智能体协同控制水系统",
        category: "智能体控制"
      },
      {
        id: "ai-modeling",
        name: "AI建模",
        description: "演示使用大语言模型进行自然语言建模",
        category: "AI建模"
      }
    ]
    setExamples(mockExamples)
  }, [])

  const handleRunSimulation = (example) => {
    setSelectedExample(example)
    // 模拟运行仿真
    setSimulationResult({
      simulation_id: "sim_12345",
      status: "completed",
      results: {
        data: [
          { time: 0, value: 100 },
          { time: 1, value: 105 },
          { time: 2, value: 110 },
          { time: 3, value: 115 },
          { time: 4, value: 120 }
        ]
      }
    })
  }

  return (
    <div className="App">
      <header className="app-header">
        <h1>CHS-SDK 水系统仿真演示平台</h1>
        <p>基于多智能体架构的专业水系统仿真与控制平台</p>
      </header>

      <main className="app-main">
        <section className="examples-section">
          <h2>示例场景</h2>
          <div className="examples-grid">
            {examples.map(example => (
              <div key={example.id} className="example-card">
                <h3>{example.name}</h3>
                <p>{example.description}</p>
                <button onClick={() => handleRunSimulation(example)}>
                  运行示例
                </button>
              </div>
            ))}
          </div>
        </section>

        {simulationResult && (
          <section className="results-section">
            <h2>仿真结果 - {selectedExample?.name}</h2>
            <div className="chart-container">
              <h3>水位变化趋势</h3>
              <div className="chart-placeholder">
                {/* 这里应该是一个实际的图表组件 */}
                <p>图表展示区域</p>
              </div>
            </div>
            <div className="data-table">
              <h3>数据表格</h3>
              <table>
                <thead>
                  <tr>
                    <th>时间</th>
                    <th>数值</th>
                  </tr>
                </thead>
                <tbody>
                  {simulationResult.results.data.map((item, index) => (
                    <tr key={index}>
                      <td>{item.time}</td>
                      <td>{item.value}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        )}
      </main>

      <footer className="app-footer">
        <p>CHS-SDK &copy; 2025 - 专业的水系统仿真与控制解决方案</p>
      </footer>
    </div>
  )
}

export default App