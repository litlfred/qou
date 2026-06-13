**Remark (calibrated; shape derived).**
*The per-nucleon binding energy of an atomic nucleus $(Z, N)$
admits the structural decomposition*

$$
  \frac{B(Z, N)}{A}
  \;\approx\;
  \alpha \cdot \frac{T_6(Z, N)}{A^3}
  \;+\;
  \beta
  \;+\;
  \delta_M(Z, N),
$$

*where $A = Z + N$, $T_6(Z, N)$ is the level-$3$ Gröbner-Shirshov
spectral-sequence stratum contribution
([prop:gb-spectral-sequence](#prop:gb-spectral-sequence)),
$\alpha, \beta$ are calibration coefficients fit to the AME panel,
and $\delta_M(Z, N)$ is an operator-level magic-shell enhancement.*

## Term 6 explicit form

The level-$3$ stratum contribution per
[`prop:gb-spectral-sequence`](#prop:gb-spectral-sequence)'s
identification of $E_\infty^{\ell \geq 3, *}$ with Term 6 is

$$
  T_6(Z, N)
  \;=\;
  z^3 \sum_{(i, j, k) \in \mathcal{S}_3(Z, N)} \Phi_q\!\bigl(\, |\mathrm{tr}_M(\xi_{ijk})| \,\bigr),
$$

where $\mathcal{S}_3(Z, N)$ is the set of ordered triples of
nucleons in the atom, $\xi_{ijk} \in H_9(R, q)$ is the canonical
$9$-strand sub-braid acting on the three nucleons indexed
$(i, j, k)$, and $z$ is the Markov parameter
([thm:jones-markov-trace](#thm:jones-markov-trace)).

By [thm:markov-trace-factorization](#thm:markov-trace-factorization),
the $9$-strand Markov trace decomposes by triple-type:

See [Table 1](#tbl:term6-binding-density-table1-data).

so $T_6$ is computed with four atom-independent traces
(one per triple-type) plus the four binomial coefficients.

## $A^3$ normalization

The $A^3$ in the denominator is canonical: $T_6$ counts triples
($\sim \binom{A}{3} \sim A^3 / 6$), so $T_6 / A^3$ is the
per-cubed-A density — the natural intensive quantity matching
binding-energy-per-nucleon dimensions. This normalization arises
**before** any AME data; it follows from the combinatorial
structure of the level-$3$ stratum.

## Magic-shell correction $\delta_M$

The operator-level magic correction adds binding at doubly-magic
shells per
[`prop:categorical-neutrality-saturated-shells`](../../content/quantum-observable-universe/braids-and-knots/categorical-neutrality-saturated-shells.md)
in the **operator-level** sense (not the Plancherel-character
sum, which vanishes — see
[reframing memo](../../../docs/audits/-self-conj-support-reframing.md)).
Empirically:

$$
  \delta_M(Z, N) \approx
  \begin{cases}
    +\Delta_M & (Z, N) \in \mathfrak{M} \times \mathfrak{M} \\
    +\Delta_P / A^{1/2} & Z \text{ even} \wedge N \text{ even} \\
    0 & \text{otherwise}
  \end{cases}
$$

with $\Delta_M \approx 2.5$ MeV at the lightest doubly-magic
$^4\mathrm{He}$ and $\Delta_P \sim 0.5$ MeV at $A \sim 12$ scale.
At heavier doubly-magic atoms ($^{40}\!\mathrm{Ca}$, $^{56}\!\mathrm{Ni}$),
$\delta_M \to 0$: the smooth $T_6/A^3$ formula already absorbs
the magic enhancement at large $A$.

## Empirical calibration

Fit on the 16-atom panel D, 3He, 3H, 4He, 6Li, 7Li, 9Be, 12C,
16O, 20Ne, 24Mg, 28Si, 32S, 40Ca, 48Ca, 56Ni, 58Ni against AME
2020 binding energies:

$$
  \alpha \approx 339.4 \;\mathrm{MeV},
  \quad
  \beta \approx 1.14 \;\mathrm{MeV},
  \quad
  R^2 = 0.84,
  \quad
  \sigma_{\mathrm{resid}} = 0.76 \;\mathrm{MeV}.
$$

Per-atom residuals (B/A AME minus prediction):

See [Table 2](#tbl:term6-binding-density-table2-data).

Witness: [`Term6-scaling-heavy.witness.json`](../../../docs/audits/-Term6-scaling-heavy.witness.json).

## What is structurally derived

* The **shape** $\alpha \cdot T_6/A^3 + \beta + \delta_M$ follows
  from
  [`prop:gb-spectral-sequence`](#prop:gb-spectral-sequence)'s
  identification of $E_\infty^{\ell \geq 3, *}$ with Term 6
  plus the combinatorial $\binom{A}{3} \sim A^3$ structure of
  triples.
* The **definition** of $T_6$ in terms of $9$-strand Markov
  traces is structurally derived from the Hecke-trace
  factorization theorem.

## What is empirical (not yet derived)

* The **values** $\alpha = 339.4$ MeV and $\beta = 1.14$ MeV
  are **calibrated** to the AME panel. A categorical derivation
  predicting these from $q_0$ + $m_e$ + $Q_\beta$ alone is open;
  candidate expressions like
  $m_e \cdot [7]_q [8]_q [9]_q = 361.2$ MeV are within $7\%$ of
  the fit but outside the $\pm 3\%$ fit window
  ([attempt witness](../../../docs/audits/-alpha-categorical-derivation.witness.json)).
* The **form** of $\delta_M$ is operator-level — proper
  derivation requires the operator structure of $\Phi_n$ on
  self-conjugate isotypical Wedderburn blocks, which is the
  content of `prop:categorical-neutrality-saturated-shells`.
