import model
from scipy import stats


class Model(model.PlanetsModel):

        def planets_per_system(self, n, size):
            return stats.binom.rvs(n, .5, size=size)

        def planet_b(self, n, sigma):
            return stats.norm.rvs(scale=sigma, size=n)


class ABC(model.ABC):

        def distance_function(self, simulation, observed):
            return stats.ks_2samp(simulation, observed)[0]
