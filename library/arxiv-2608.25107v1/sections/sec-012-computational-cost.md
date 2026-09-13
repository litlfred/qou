---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland"
section_id: sec-012-computational-cost
section_title: "Computational cost"
section_number: null
pages: 14-15
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland — 17 sections: ADoNIS: A Differe"
---
Built-in derivative information can be exploited at ev-
ery computational stage of the inference demonstrated
above. We benchmark its impact in three representative
tasks: locating the best fit, evaluating the curvature en-
tering uncertainty quantification, and sampling the full
posterior with MCMC. Unless otherwise stated, all per-
formance tests are carried out in double precision on the
same NVIDIA A100 GPU. JAX compilation is excluded
from the reported timings; for MCMC, warm-up and
adaptation are also excluded from the sampling times.
Optimisation times are quoted as medians over repeated
statistically fluctuated fits. In each case the statistical
target is unchanged; what changes is how efficiently the
information required by the calculation can be obtained.
For optimisation, we compare three choices on the
same objective: MIGRAD [186, 187] without derivative
information, MIGRAD supplied with the exact gradient
fromADoNIS, and Gauss–Newton (GN), which uses
the full Jacobian supplied byADoNISto construct a
curvature-aware step without requiring second deriva-
tives of the generator. For GN, the step is controlled
by a trust region whose size is updated according to how
accurately the local model predicts the reduction actu-
ally achieved inχ 2. Physical parameter bounds are in-
corporated into the step itself, slowing directions as they
approach a boundary and reflecting otherwise infeasible
steps back into the allowed domain [191, 192].
For the representative 17-parameter fit with statisti-
cal fluctuations, using 1.25×10 5 events per sample, GN
converges in a median 1.6 s, compared with 4.8 s for MI-
GRAD supplied with the exact autodifferentiated gradi-
ent and 12.3 s without one. Supplying derivative infor-
mation therefore accelerates the fit substantially. In a
separate hardware comparison, the same fit was approx-
imately 120 times slower on a single AMD EPYC CPU
core than on the A100, excluding compilation in both
cases.
The number of events and the number of parameters
naffect the computational cost differently. At fixedn,
the arithmetic workload of each model or derivative pass
grows linearly with the number of events; the total cost
then depends on how many such passes the inference
algorithm requires. Increasingnadditionally changes
the cost of obtaining the derivative information required
by the optimiser. MIGRAD without supplied deriva-
tives must estimate the gradient numerically, so a cen-
tral finite-difference estimate requires approximately 2n
evaluations of the objective. When MIGRAD is supplied
with derivatives fromADoNIS, automatic differentia-
tion instead obtains all components of the gradient of
the scalar objective together, avoiding a separate pair
of model evaluations for each parameter. The same ad-
vantage applies to GN, although it uses the full residual
Jacobian rather than only∇χ 2.
Repeating the statistically fluctuated fits while increas-
ing the number of parameters from 2 to 17 makes this
15
distinction explicit. Over the range tested, the measured
GN wall time grows approximately asn 0.8, gradient-
supplied MIGRAD asn 0.9, and MIGRAD with numerical
derivatives asn 1.5. Both autodifferentiated approaches
therefore scale much more mildly than numerical differ-
entiation as the parameter space grows.
The same advantage propagates to uncertainty quan-
tification, where the appropriate construction depends on
the dimensionality of the reported result and the avail-
able computational budget. The local Gaussian covari-
ance is the least expensive option and is already available
from the Jacobian used by GN. For low-dimensional non-
Gaussian results, profile scans require a conditional fit at
every grid point, so each point benefits from the same
derivative information as the central fit.
Marginalisation on the same low-dimensional grids
additionally requires the nuisance curvature entering
Eq. 21. Reusing the Gauss–Newton/Fisher matrix of
Eq. 17 is essentially free, but away from the minimum
it omits the residual-dependent part of the exact Hes-
sian. At representative profile points in this fit, that
approximation changes log detVnuis by up to about 0.25,
motivating the exact calculation used above. Automatic
differentiation assembles the exact Hessian withO(n)
Hessian–vector products, compared withO(n 2) objec-
tive evaluations for a finite-difference calculation. This
requires 48 event passes and about 0.18 s per point, com-
pared with roughly 285 passes and 1.35 s for MINUIT
HESSE, making the exact autodifferentiated calculation
about seven times faster.
For fully correlated high-dimensional inference, HEP
analyses commonly turn to Markov chain Monte Carlo
(MCMC). Here the analogous distinction is between
random-walk algorithms such as Metropolis–Hastings
(MH), which require only likelihood evaluations, and
Hamiltonian methods such as NUTS, which also exploit
its gradient. SinceADoNISsupplies that gradient di-
rectly, gradient-based MCMC can use it without con-
structing numerical derivatives of the generator.
Because MCMC efficiency depends strongly on the
posterior geometry, we compare MH and NUTS on the
same 17-parameter posterior. Both sample the same like-
lihood, physical bounds and dataset through a shared
objective. MH uses a Gaussian random-walk proposal
preconditioned by the Laplace covariance, with its scale
adapted to a target acceptance of 0.234 [193]; NUTS tar-
gets 0.80 and uses dual averaging with windowed met-
ric adaptation as implemented in Stan [194, 195]. Ef-
ficiency is compared only after both samplers satisfy a
rank-normalised, folded split- ˆR<1.01 convergence crite-
rion [196] and their one-dimensional marginals are found
to agree.
Sampling efficiency is quantified through the effective
sample size (ESS), estimated with the initial monotone
positive sequence [197]. Because ESS is parameter de-
pendent, we quote both its minimum across parameters,
which captures the slowest-mixing direction, and its me-
dian. Per unit wall-clock time, NUTS yields 2.0 times
the minimum ESS of MH and 1.4 times the median ESS
on this posterior. The gain rises to 3.4 for the tail ESS
at the 5% and 95% quantiles bounding a 90% credible
interval. Gradient-based NUTS therefore produces more
statistically effective posterior samples per unit time than
the tuned random-walk MH comparison, with the largest
gain in the tails relevant to quoted interval endpoints.
