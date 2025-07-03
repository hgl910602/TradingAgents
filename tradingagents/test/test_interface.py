import sys
import os
import traceback  # 新增：导入traceback模块

# 添加项目根目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

import unittest
from tradingagents.dataflows.interface import get_fundamentals_openai, get_global_news_openai, get_stock_news_openai

class TestGetFundamentalsOpenAI(unittest.TestCase):
    def test_get_fundamentals_valid_input(self):
        """测试使用有效参数调用get_fundamentals_openai方法"""
        ticker = "AAPL"
        test_date = "2025-06-30"
        try:
            result = get_fundamentals_openai(ticker, test_date)
            # 验证返回结果不为空
            self.assertIsNotNone(result)
            self.assertIsInstance(result, str)
            self.assertTrue(len(result) > 0)
            print(f"测试成功: 获取到{test_date}的{ticker}基本面数据")
        except Exception as e:
            # 新增：打印完整堆栈跟踪信息
            print("===== 异常详细信息 ======")
            traceback.print_exc()  # 打印异常堆栈，包含行号信息
            print("=========================")
            self.fail(f"测试失败: {str(e)}")

class TestGetGlobalNewsOpenAI(unittest.TestCase):
    def test_get_global_news_valid_input(self):
        test_date = "2025-06-30"
        try:
            result = get_global_news_openai(test_date)
            self.assertIsInstance(result, str, "全球新闻接口应返回字符串类型结果")
            self.assertGreater(len(result), 0, "全球新闻接口返回结果不应为空")
            print("全球新闻接口连通性测试通过")
        except Exception as e:
            self.fail(f"全球新闻接口测试失败: {str(e)}")

class TestGetStockNewsOpenAI(unittest.TestCase):
    def test_get_stock_news_valid_input(self):
        ticker = "AAPL"
        test_date = "2025-06-30"
        try:
            result = get_stock_news_openai(ticker, test_date)
            self.assertIsInstance(result, str, "股票新闻接口应返回字符串类型结果")
            self.assertGreater(len(result), 0, "股票新闻接口返回结果不应为空")
            self.assertIn(ticker, result, "股票新闻结果应包含查询的股票代码")
            print("股票新闻接口连通性测试通过")
        except Exception as e:
            self.fail(f"股票新闻接口测试失败: {str(e)}")

if __name__ == '__main__':
    unittest.main()