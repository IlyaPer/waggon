import utils
import argparse
from acqusition import WU, EI, CB
import test_functions as f
from optim import Optimiser
from surrogates.gan import WGAN_GP as GAN

FUNCS = {'ackley': f.ackley,
         'himmelblau': f.himmelblau,
         'holder': f.holder,
         'levi': f.levi,
         'rosenbrock': f.rosenbrock,
         'tang': f.tang,
         'thc': f.three_hump_camel}

SURR = {'gan': GAN(),}

ACQF = {'wu': WU(), 'ei': EI(), 'lcb': CB(minimise=True), 'ucb': CB(minimise=False)}

SEEDS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 73]

def main():
    # TODO: make experiment configurations; add model configuration files
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--function', help='optimise the given function', default='thc', choices=['thc', 'ackley', 'levi', 'himmelblau', 'rosenbrock', 'tang', 'holder'])
    parser.add_argument('-d', '--dimensions', type=int, help='dimensionality of the experiment', default=None)
    parser.add_argument('-s', '--surrogate', help='surrogate for optimisation', default='gan', choices=['gan', 'bnn', 'de', 'dgp', 'gp'])
    parser.add_argument('-a', '--acquisition', help='acqusition function to use for optimisation', default='wu', choices=['wu', 'ei', 'lcb', 'ucb'])
    parser.add_argument('-v', '--verbosity', type=int, help='increase output verbosity', choices=[0, 1, 2], default=1) #TODO: make varbosity compatible with all surrogates

    args = parser.parse_args()

    if (args.surrogate == 'gan' and args.acquisition != 'wu') or (args.surrogate != 'gan' and args.acquisition == 'wu'):
        raise ValueError(f'Surrogate {args.surrogate} is not compatible with {args.acquisition} acquisition function')

    for i, seed in enumerate(SEEDS):

        print(f'Experiment #{i}')

        opt = Optimiser(func=FUNCS[args.function](args.dimensions) if args.dimensions else FUNCS[args.function](),
                        surrogate=SURR[args.surrogate],
                        acqf=ACQF[args.acquisition],
                        verbosity=args.verbosity,
                        seed=seed)
        opt.optimise()
        utils.save_results(opt)
    
    utils.plot_results(opt_eps=opt.opt_eps, max_iter=opt.max_iter)

if __name__ == '__main__':
    main()
