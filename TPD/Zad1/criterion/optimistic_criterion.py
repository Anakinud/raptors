from pandas import DataFrame

from Zad1.criterion.criterion import Criterion


class OptimisticCriterion(Criterion):

    def decision(self, data_frame: DataFrame):
        maxs = []

        for index, row in data_frame.iterrows():
            maxs.append((index, row.max()))

        return max(maxs, key=lambda item: item[1])[0]

    def __str__(self):
        return f"{self.highlight_criterion_name('OptimisticCriterion')}"
