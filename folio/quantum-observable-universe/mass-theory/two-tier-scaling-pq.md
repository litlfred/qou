**Remark (two-tier scaling of the confined Laurent polynomial $P_K(q)$).**
*The map from a braid word to a physical mass passes through two logically separate scaling factors. We separate topological constants (intrinsic to the Hecke trace) from dimensional constants (set by the choice of physical anchor).*

## Tier 1: topological scaling — quantum dimension $[N]_q$

Before the Markov trace
([categorical mass as Markov trace](#prop:categorical-mass-markov))
qualifies as an isotopy invariant on the closure $\hat{\beta}$, the
raw graded Euler characteristic of the braid word must be normalised
so that an unbraided strand contributes a factor independent of the
ambient brane content. That normalising factor is the **quantum
dimension** of the fundamental fibre,

$$
  [N]_q
  \;=\;
  \frac{q^{N} - q^{-N}}{q - q^{-1}}.
$$

In Hecke language, $[N]_q$ is the Markov-trace normalisation that
ensures invariance under stabilisation $\beta \mapsto \beta\sigma_n^{\pm 1}$
([axiomatic Markov closed form](#prop:markov-trace-axiomatic-closed-form)).
Physically, it acts as a vacuum subtraction: $P_K(q)$ measures the
*excess* topological complexity of the knot $K$ relative to the
unbraided substrate, not the absolute count of strands. Without
this normalisation the polynomial would grow with every additional
trivial component, and Reidemeister-I invariance would fail
([Reidemeister mass invariance](#conj:reidemeister-mass-invariance)).

## Tier 2: physical scaling — base mass $m_0$

Evaluating the normalised $P_K(q)$ at the substrate parameter
$q_0 = 1.109978595642739\ldots$ (muon pin, 16 dps) produces a dimensionless real number; converting
to MeV requires multiplication by a base mass scale,

$$
  \mathfrak{m}_{\mathcal{K}} \;\approx\; m_0 \cdot \bigl| P_K(q_0) \bigr|.
$$

The choice of $m_0$ is a **boundary condition** of the framework, not
a derivation. Three natural anchors appear in the literature:

| Anchor | Value | Setting |
|--------|-------|---------|
| Leptonic mass | $m_e \approx 0.511\;\mathrm{MeV}$ | adopted by QOU as **CAL-1** ([calibration inputs](#rem:calibration-inputs)) |
| Higgs VEV | $v \approx 246\;\mathrm{GeV}$ | electroweak-localised models |
| Planck mass | $M_{\mathrm{Pl}} \approx 1.22 \times 10^{19}\;\mathrm{GeV}$ | spacetime-fabric models |

QOU selects $m_0 = m_e$ on empirical grounds: $m_e$ is the most
precisely measured particle mass in the Standard Model, and the
leptonic brane tower is fully computable from $q_0$ alone via
$m_e(\text{natural}) = \mathrm{Li}_2(q^{-2})/\hbar_q^2$
([three calibration inputs](#conj:three-calibration-inputs)). The
electroweak ($v$) and Planck ($M_{\mathrm{Pl}}$) choices correspond to
different fibre-functor normalisations and produce algebraically
equivalent predictions for dimensionless ratios such as
$m_\mu/m_e$ and $m_n - m_p$, but require independent calibration of
the leptonic sector to match observed masses.

## Significance of the separation

The two tiers commute with disjoint operations:

- $[N]_q$ acts **inside** the trace (Tier 1 is a categorical
  normalisation; it depends only on the rank $N$ of the fundamental
  fibre and on $q$).
- $m_0$ acts **outside** the trace (Tier 2 is a unit conversion; it
  has dimensions of mass and is independent of the braid word).

Mixing the two — for instance, by absorbing a power of $[N]_q$ into
$m_0$ — would make $m_0$ depend on the local Wedderburn channel and
break the parameter count of [three calibration inputs](#conj:three-calibration-inputs).
The volume-density factorisation
$\mathfrak{m}(K) = \mathrm{Vol}(K) \cdot \rho_q$
([Kashaev volume density](#rem:kashaev-volume-density)) inherits the
same separation: $\rho_q = 1/\hbar_q^2$ is Tier-1 (topological,
substrate-only), while the conversion of $\mathfrak{m}$ to MeV is
Tier-2 (physical, set by $m_e$).

## Summary

The substrate-bound polynomial $P_K(q)$ is a dimensionless
topological multiplier; its Markov normalisation by $[N]_q$ is fixed
by the categorical structure, while the conversion to a macroscopic
mass requires a separate dimensional anchor $m_0$ chosen by
calibration ([three calibration discipline](#def:three-calibration-discipline)).
QOU pins $m_0 = m_e$; the Higgs-VEV and Planck-mass choices are
mathematically admissible alternatives that re-route the calibration
through the electroweak or gravitational sector respectively.
