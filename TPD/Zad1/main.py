from Zad1.criterion.bayes_laplace_criterion import BayesLaplaceCriterion
from Zad1.criterion.hurwicz_criterion import HurwiczCriterion
from Zad1.criterion.optimistic_criterion import OptimisticCriterion
from Zad1.criterion.savage_criterion import SavageCriterion
from Zad1.criterion.wald_criterion import WaldCriterion
from Zad1.data.data_provider import FootballDataProvider, FarmerDataProvider, TiresDataProvider, FuelDataProvider


def decide_data(data_provider):
    print("Tested Data:")
    print(data_provider.get_data())
    for criterion in criterions:
        decision = criterion.decision(data_provider.get_data())
        print(f"For algorithm: {criterion}, the best option is: {decision}")


criterions = [HurwiczCriterion(0.25), OptimisticCriterion(), SavageCriterion(), WaldCriterion()]
decide_data(FootballDataProvider())
decide_data(FarmerDataProvider())
decide_data(TiresDataProvider())

provider = FuelDataProvider()
print("Tested Data:")
data, possibilities = provider.get_data()
print(data)
print("Possibilities:")
print(possibilities)
laplace_criterion = BayesLaplaceCriterion(possibilities)
decision = laplace_criterion.decision(data)
print(f"For algorithm: {laplace_criterion}, the best option is: {decision}")
