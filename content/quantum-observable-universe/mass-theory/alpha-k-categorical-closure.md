The categorical mass formula
([unified mass](#prop:unified-curvature-rank-mass-formula))
expresses the vortex mass as a stratum-graded sum

$$
  \mathfrak{m}_{q,\mathcal{K}}
  \;=\;
  \sum_{k \geq 0} \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}(1)
  \;+\; m_e \cdot \tau(C_{\dim_q}),
$$

where $\alpha_k$ are the **stratum prefactors** at depth $k$,
computed via the Markov-pairing procedure of
[`prop:alpha-k-derivation-procedure`](#prop:alpha-k-derivation-procedure)
as $\alpha_k = \langle \mathrm{tr}_M, r_k \rangle$ with $r_k$ a
depth-$k$ reduced word representative.

At the **substrate level** (vortex-free, evaluated at a single
Planck-tick expansion variable $x = \hbar_q^2$) the resummation
should give a single dimensionless **tower correction factor**
multiplying the leading energy scale $E_0^{(N=0)} = m_e/(q_0(q_0-1))$,
producing the brane-tower-summed value
$E_0^{\text{full}} = E_0^{(N=0)} \cdot \mathcal{F}(\hbar_q^2)$
([`rem:beta-decay-energy-scale`](../particle-interactions/beta-decay-energy-scale.md)
§"tower-summed form").

## Statement

**Conjecture.**
*The categorical resummation $\mathcal{F}(\hbar_q^2)$ admits a
closed form in $q$, and that closed form lies in one of the two
families below (or is uniquely determined as a third closed
form that interpolates them):*

| Candidate | Closed form $\mathcal{F}(x)$ | Substrate $E_0^{\text{full}}$ | CAL-3 residual |
|-----------|-------------|--------------------------:|---------------:|
| **(a) Geometric** | $1/(1-x) = \sum_{k\geq 0} x^k$ | $:val[E_0_full_MeV]{precision=4}$ MeV | overshoots by $\approx +1.75\%$ |
| **(b) Symmetric q-dilogarithm** | $1 + (-\mathrm{Li}_2^q(-x)) = 1 + \sum_{n\geq 1} (-1)^{n+1} x^n/(n \cdot [n]_q)$ | $:val[E_0_full_li2q_MeV]{precision=4}$ MeV | overshoots by $\approx +1.74\%$ |
| **(c) Unknown / interpolating** | open | open | open |

(The dimensionless factor $\mathcal{F}(\hbar_q^2)$ at $q_0 \approx 1.110$ is the ratio of either column to $:val[E_0_N0_MeV]{precision=4}$ MeV — computed live from the witness.)

*The conjecture has three substantive sub-claims:*

1. **Existence:** *the resummation $\mathcal{F}(\hbar_q^2)$
   admits a closed form in $q$ derivable from the categorical
   $\alpha_k$ (no fitting, no opt-in parameter).*

2. **Selection:** *exactly one of the families (a), (b), or (c)
   is the correct closure, and the selection is fixed by the
   Frobenius pairing on $A$ via the Markov reduction structure of
   [`prop:categorical-mass-markov`](#prop:categorical-mass-markov).*

3. **CAL-3 closure direction:** *the correct closed form lies
   **below** $\mathcal{F}_{\mathrm{geom}}(\hbar_q^2) \approx 1.00992$,
   producing a framework-derived $E_0$ that **agrees** with the
   CODATA-calibrated $E_0^{(\text{cal})} \approx 4.155$ MeV instead
   of overshooting it.*

## Why the naive geometric recursion fails

A naive bridging would assert $\alpha_k = \hbar_q^{2(k-1)} \cdot \alpha_{k-1}$
for $k \geq 1$, so that $\sum_k \alpha_k \cdot \hbar_q^{2k} = \alpha_0 / (1 - \hbar_q^2)$.
**This recursion does not match the explicit $\alpha_k$ values at
$H_3$** computed by the Markov-pairing procedure
([`prop:alpha-k-derivation-procedure`](#prop:alpha-k-derivation-procedure)
"Worked example: $H_3(R, q)$"):

$$
  \alpha_0 = 1, \qquad
  \alpha_1 = 0, \qquad
  \alpha_2 = z^2, \qquad
  \alpha_3 = z(1 + q^{1/2} - q^{-1/2}),
$$

with $z = 1/(q^{1/2} + q^{-1/2}) \approx 0.499$ the Markov
parameter. The naive recursion would require $\alpha_2 = \hbar_q^2 \cdot \alpha_1 = 0$,
but the actual value is $z^2 \neq 0$. So the geometric closure
(a) is **not** the naive substitution; if it holds, it does so as
a non-obvious resummation identity over the $\alpha_k$ family.

## Why the bounded Li_2^q candidate is plausible

The mass-endomorphism tower
([`prop:mass-endomorphism-tower`](#prop:mass-endomorphism-tower)
lines 162–183) **proves** that the brane-tower integral evaluates
to $-\mathrm{Li}_2^q(-V)$ (symmetric q-dilogarithm), not
$\Phi_q(V)$ (Faddeev quantum dilogarithm — empirically off by
$10^6$ per
[`kashaev-integration-identity.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/kashaev-integration-identity.witness.json)).
At the substrate level (single Planck-tick variable $x = \hbar_q^2$)
the bounded analog $\mathcal{F}_{\mathrm{Li}_2^q}(x)$ matches the
geometric form $1 + x + O(x^2)$ at leading order and stays
bounded as $x \to 1$.

**However**, the substrate Li_2^q form **does not** close CAL-3 in
the correct direction (it gives $\approx +1.74\%$ vs the geometric
$\approx +1.75\%$ — a $0.01\%$ improvement). The per-atom Li_2^q
evaluation (per the prop's proper form $-\mathrm{Li}_2^q(-|\hat V_i|)$
summed over generators with atom-specific volumes
$|\hat V_i^{\text{full}}|$) may give a different and possibly
correct closure; that evaluation requires atomic-braid input and
is not a substrate-only computation.

## Numerical evidence (substrate level)

Computed in
[`folio-assistant/computations/derived_masses.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/derived_masses.py)
at $q_0 \approx 1.110$:

- $E_0^{(N=0)} \approx :val[E_0_N0_MeV]{precision=4}$ MeV — single Planck-tick (CAL-1 + CAL-2)
- $E_0^{\text{full,geom}} = :val[E_0_full_MeV]{precision=4}$ MeV — geometric closure
- $E_0^{\text{full,}Li_2^q} = :val[E_0_full_li2q_MeV]{precision=4}$ MeV — bounded q-dilogarithm closure
- $E_0^{(\text{cal})} \approx :val[E_0_calibrated_MeV]{precision=4}$ MeV — CODATA cross-check

The two candidate closures agree to four significant figures at
the substrate level. The CAL-3 residual remains an open finding
in the same direction for both.

## Discussion

**Open conjecture.** All three sub-claims (existence, selection,
direction) require categorical derivation. The closure proposal
is the recommended **first follow-up** after the E_0 disentanglement
([``](https://github.com/litlfred/qou/pull/673)) and is
listed as item 6 in the post-PR-#665 R&D inventory
(`rem:post-pr665-open-rd-inventory`).
The required input infrastructure (per-irrep $\chi_\lambda$ closed
forms, Wedderburn-block scaffolding) is in place and ready for the
categorical resummation analysis.
