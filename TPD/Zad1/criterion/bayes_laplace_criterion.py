from pandas import DataFrame

from Zad1.criterion.criterion import Criterion


class BayesLaplaceCriterion(Criterion):
    def __init__(self, possibilities):
        self._possibilities = possibilities

    def decision(self, data_frame: DataFrame):
        decisions = []

        for index, row in data_frame.iterrows():
            decisions.append((index, self._calculate(row)))

        return max(decisions, key=lambda item: item[1])[0]

    def _calculate(self, row):
        result = 0

        for col, val in row.iteritems():
            result += self._possibilities[col] * val

        return result

    def __str__(self):
        return f"{self.highlight_criterion_name('BayesLaplaceCriterion')}"
