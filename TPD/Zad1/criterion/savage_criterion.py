from pandas import DataFrame

from Zad1.criterion.criterion import Criterion


class SavageCriterion(Criterion):
    def decision(self, data_frame: DataFrame):
        new_matrix = data_frame.copy()

        for col_index, col in data_frame.iteritems():
            col_max = col.max()
            for row_index, val in col.iteritems():
                new_matrix.at[row_index, col_index] = col_max - val

        maxs = []

        for index, row in data_frame.iterrows():
            maxs.append((index, row.max()))

        return max(maxs, key=lambda item: item[1])[0]

    def __str__(self):
        return f"{self.highlight_criterion_name('SavageCriterion')}"
