from pandas import DataFrame


class Criterion:
    def decision(self, data_frame: DataFrame):
        pass

    def highlight_criterion_name(self, algorithm_name: str) -> str:
        return f'\033[93m{algorithm_name}\033[0m'
