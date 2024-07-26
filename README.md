# Welcome to WAGGON: WAssrestein Global Gradient-free Optimisation

<!-- [![PyPI version](https://badge.fury.io/py/probaforms.svg)](https://badge.fury.io/py/probaforms)
[![Tests](https://github.com/HSE-LAMBDA/probaforms/actions/workflows/tests.yml/badge.svg)](https://github.com/HSE-LAMBDA/probaforms/actions/workflows/tests.yml)
[![Docs](https://github.com/HSE-LAMBDA/probaforms/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/HSE-LAMBDA/probaforms/actions/workflows/pages/pages-build-deployment)
[![Downloads](https://static.pepy.tech/badge/probaforms)](https://pepy.tech/project/probaforms)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) -->

`WAGGON` is a python library of black box gradient-free optimisation. Currently, the library contains implementations of optimisation methods based on Wasserstein uncertainty and baseline approaches from the following papers:

- Tigran Ramazyan, Mikhail Hushchyn and Denis Derkach. "Global Optimisation of Black-Box Functions with Generative Models in the Wasserstein Space." Arxiv abs/2407.1117 (2024). [[arxiv]](https://arxiv.org/abs/2407.11917)

## Implemented methods
- Wasserstein Uncertainty Global Optimisation (WU-GO)
- Bayesian optimisation: via Expected Improvement (EI), Lower and Upper Confidence Bounds (LCB, UCB)

## Installation

```
pip install waggon
```
or
```
git clone https://github.com/hse-cs/waggon
cd waggon
pip install -e
```

## Basic usage

(See more examples in the [documentation](TBD).)

The following code snippet (does this and that)

```python
import waggon
from waggon.acquisition import WU
from waggon.optim import Optimiser
from waggon.surrogates.gan import WGAN_GP as GAN
from waggon.test_functions import three_hump_camel

# initialise the function to be optimised
func = three_hump_camel()
# initialise the surrogate to carry out optimisation
surr = GAN()
# initialise optimisation acquisition function
acqf = WU()

# initialise optimiser
opt = Optimiser(func=func, surr=surr, acqf=acqf)

# run optimisation
opt.optimise()

# visualise
waggon.display()
```


## Support

- Home: [https://github.com/hse-cs/waggon](https://github.com/hse-cs/waggon)
<!-- - Documentation: [https://hse-cs.github.io/waggon](https://hse-cs.github.io/waggon) -->
- For any usage questions, suggestions and bugs please use the [issue page](https://github.com/hse-cs/waggon/issues).

<!-- ## Thanks to all our contributors

<a href="https://github.com/HSE-LAMBDA/probaforms/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=HSE-LAMBDA/probaforms" />
</a> -->
