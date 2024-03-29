from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
import FinanceDataReader as fdr
fdr.__version__

class SmaCross(Strategy):
    def init(self):
        Close = self.data.Close
        self.ma1 = self.I(SMA, Close, 10)
        self.ma2 = self.I(SMA, Close, 20)

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()

class BackTest():
    def run_test(self, code, start_date, end_date):
        # 셀트리온, 2018년~2019년6월
        data = fdr.DataReader(code, start_date, end_date)
        print(data.head())

        # 초기투자금 10000, commission 비율 0.002 임의 지정
        bt = Backtest(data, SmaCross,
                      cash=10000, commission=.002)

        bt.run()
        print(bt._results)
        # print(bt._results['Return [%]'])
        bt.plot(filename='D:\\jbdesk\\Dropbox\\jbmini\\project\\my\\stock\\alza-stock\\port\\templates\\port\\btest_graph.html', open_browser=False)