from pandas import DataFrame

from Zad1.criterion.criterion import Criterion


class WaldCriterion(Criterion):

    def decision(self, data_frame: DataFrame):
        mins = []

        for index, row in data_frame.iterrows():
            mins.append((index, row.min()))

        return max(mins, key=lambda item: item[1])[0]

    def __str__(self):
        return f"{self.highlight_criterion_name('WaldCriterion')}"
