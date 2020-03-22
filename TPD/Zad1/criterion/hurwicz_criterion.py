from pandas import DataFrame

from Zad1.criterion.criterion import Criterion


class HurwiczCriterion(Criterion):

    def __init__(self, security_coefficient):
        self._security_coefficient = security_coefficient

    def decision(self, data_frame: DataFrame):
        decisions = []

        for index, row in data_frame.iterrows():
            decisions.append((index, self._calculate(row.min(), row.max())))

        return max(decisions, key=lambda item: item[1])[0]

    def _calculate(self, minimum, maximum):
        return self._security_coefficient * minimum + ((1 - self._security_coefficient) * maximum)

    def __str__(self):
        return f"{self.highlight_criterion_name('HurwiczCriterion')} " \
            f"Security Coefficient = {self._security_coefficient}"
