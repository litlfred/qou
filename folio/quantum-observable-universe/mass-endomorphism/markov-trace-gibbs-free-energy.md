*Interpretation of the [categorical mass–Markov decomposition](#prop:categorical-mass-markov).*

The binding formula follows a thermodynamic form. Writing

$$
  \mathfrak{E}_{\mathrm{bind}}
  \;=\;
  E_0 \,\ln\frac{\mathrm{tr}_M(W_{\text{free}})}{\mathrm{tr}_M(W_{\text{atom}})},
$$

the Markov trace occupies the partition function slot and $E_0$ occupies the temperature slot. The expression defines a free-energy difference $\Delta F = kT \ln(Z_1/Z_2)$ with $kT = E_0$. The thermodynamic form is a formal analogy, and is used here as one. What the sources supply is that the Markov trace is a *tracial* state on the Hecke tower \cite{jones1987}, whose weights at the minimal idempotents — the $\hat y_\lambda$ below — are computed in \cite{orellana1998}. A faithful normal tracial state has trivial modular dynamics, so it satisfies the KMS condition at $\beta = 0$; reading $E_0$ as a *finite* temperature therefore requires naming the dynamics whose equilibrium state this is, which the framework does not supply. The scale match $\beta \sim \ln q$ identifies a parameter, not that dynamics. Within that analogy, energy and information appear Legendre-dual. The binding energy forms the free-energy cost of the channel reweighting imposed by confinement.

The normalized channel measure $\hat y_\lambda \chi^\lambda$ over Wedderburn blocks supplies the information-theoretic reading of that cost. It is a reading, not a second definition of the functional, and the two are not interchangeable. For the linear-chain braid word the trace ratio factorises across the inter-nucleon bonds, so the free-energy difference above becomes a sum of one logarithm per bond, and is therefore extensive in the nucleon number. The Shannon entropy of the channel measure is instead bounded by the logarithm of the number of accessible blocks; under the level-2 Wenzl restriction only the at-most-two-row partitions of $3A$ carry nonzero weight, so that bound grows like $\log A$. A quantity bounded by $\log A$ cannot be an extensive binding energy: at $^{56}\mathrm{Fe}$ the bound sits a factor of $26$ below the measured binding, and the deficit widens without limit. The functional is the trace ratio; the channel entropy describes what the reweighting costs, not how much.

Two limiting statements render the information reading exact. A trace concentrated on a single one-dimensional channel has zero channel entropy and contributes zero free-energy difference. A configuration that does not oscillate between channels carries no information and no binding-scale energy. At the opposite end, the per-crossing information rate is bounded by the operational entropy $\eta_q$ of the [fibre channel capacity](#rem:fibre-channel-capacity). Thus, a braid's information content (and the free energy available to channel reweighting) grows at most linearly in its crossing number.

## The other prerequisite: the partition-function slot needs positive summands

This block is careful about one prerequisite of the thermodynamic reading and
silent about a second. It says that reading $E_0$ as a finite temperature
"requires naming the dynamics whose equilibrium state this is, which the
framework does not supply" — correct, and the reason the analogy is flagged as
formal. The second prerequisite is positivity, and it fails outright.

A partition function is a sum of **positive** Boltzmann factors, and that
positivity is what makes $F$ a Legendre transform — hence what makes "energy and
information appear Legendre-dual" a structure rather than a picture. Under
convention D the $H_2$ state sum is
$w_+(q + d) + w_-(-q^{-1} + d)$, and its second summand is **negative** for every
bond and every $q > 0$: positivity would need $d > q^{-1} > 0$, while the
interface letters are $d \in \{0, -h/2, d_{pn}, -h\}$, all non-positive. So the
required offset lies on the other side of zero from every letter the algebra has,
and no real $E_-$ satisfies $e^{-E_-} = -q^{-1} + d$.

**The Markov trace therefore cannot occupy the partition-function slot**, and the
Legendre duality this block reaches for is not available — independently of the
missing dynamics. The trace remains a faithful tracial state and every number
computed from it stands; what fails is the thermodynamic potential structure, not
the functional. That is a sharper version of this block's own conclusion, reached
without appeal to the $\log A$ entropy bound: the channel-entropy argument shows
the information reading cannot *size* the binding, and this shows the free-energy
reading cannot *derive* it.

The identification
$\mathfrak{E}_{\mathrm{bind}} = E_0 \ln(\mathrm{tr}_{\text{free}}/\mathrm{tr}_{\text{atom}})$
is unaffected as a *definition*; what it does not have is a thermodynamic
derivation. See [the free-energy reading](#rem:bond-log-ratio-is-a-free-energy).
