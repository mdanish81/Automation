import unittest
from src.core_engine import AutomationEngine

class TestAutomationEngine(unittest.TestCase):
    def test_engine_initialization(self):
        engine = AutomationEngine("TestWorkflow")
        self.assertEqual(engine.workflow_name, "TestWorkflow")
        self.assertEqual(engine.status, "Initialized")

    def test_pipeline_execution(self):
        engine = AutomationEngine("TestWorkflow")
        result = engine.execute_pipeline({"items": [1, 2, 3]})
        self.assertEqual(result["status"], "Success")
        self.assertEqual(result["processed_count"], 3)

if __name__ == "__main__":
    unittest.main()
