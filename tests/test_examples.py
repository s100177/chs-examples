"""
CHS-SDK示例测试
"""

import os
import sys
import unittest

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestExamples(unittest.TestCase):
    """示例测试类"""
    
    def test_basic_simulation_example_exists(self):
        """测试基础仿真示例是否存在"""
        example_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'examples', 'basic-simulation'
        )
        self.assertTrue(os.path.exists(example_path))
        self.assertTrue(os.path.exists(os.path.join(example_path, 'run.py')))
        self.assertTrue(os.path.exists(os.path.join(example_path, 'README.md')))
    
    def test_agent_control_example_exists(self):
        """测试智能体控制示例是否存在"""
        example_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'examples', 'agent-control'
        )
        self.assertTrue(os.path.exists(example_path))
        self.assertTrue(os.path.exists(os.path.join(example_path, 'run.py')))
        self.assertTrue(os.path.exists(os.path.join(example_path, 'README.md')))
    
    def test_ai_modeling_example_exists(self):
        """测试AI建模示例是否存在"""
        example_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'examples', 'ai-modeling'
        )
        self.assertTrue(os.path.exists(example_path))
        self.assertTrue(os.path.exists(os.path.join(example_path, 'run.py')))
        self.assertTrue(os.path.exists(os.path.join(example_path, 'README.md')))
    
    def test_run_example_script_exists(self):
        """测试运行示例脚本是否存在"""
        script_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'scripts', 'run-example.py'
        )
        self.assertTrue(os.path.exists(script_path))

if __name__ == '__main__':
    unittest.main()