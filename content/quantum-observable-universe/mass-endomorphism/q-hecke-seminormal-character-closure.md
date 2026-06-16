**Proposition (q-Hecke partition-sum closure).** *Let $\mathcal{B}_K$ be the
canonical atomic-braid word for atom $(Z, N)$ — i.e. the
$(c, d, \mathrm{gen\_idx})$ word produced by
[`atom_braid_word_3A`](../../../computations/mass_at_3A_proper.py)
($\mathcal{B}_p \cdot I \cdot \mathcal{B}_n$ with $I = \sigma_{n_1} - \frac{h}{2} \cdot 1$
the inter-nucleon interface). For each $\lambda \vdash 3A$ let
$\rho_\lambda^q$ be the Hoefsmit seminormal representation at $q$
([`hecke_characters.build_seminormal_matrices`](../../../computations/hecke/hecke_characters.py))
and let $y_\lambda(q)$ be the Jones-Markov weight via Wenzl's Schur
principal specialization
([`markov_weights_symbolic.solve_y_lambda`](../../../computations/markov/markov_weights_symbolic.py)).
Then the partition-sum form of the canonical Markov trace,*

$$
  \mathrm{tr}_M^{\mathrm{partition\text{-}sum}}(\mathcal{B}_K)
  \;:=\;
  \sum_{\lambda \vdash 3A} y_\lambda(q) \cdot \mathrm{tr}_{V_\lambda}\!\bigl(\rho_\lambda^q(\mathcal{B}_K)\bigr),
$$

*equals the canonical Markov-axiom reducer*
$\mathrm{tr}_M(\mathcal{B}_K)$ ([`prop:markov-trace-recursive-reducer`](#prop:markov-trace-recursive-reducer))
*to numerical precision at $q = q_0$.*

## Why it matters

The partition-sum form is the standard rewriting of the Markov
trace via the Wedderburn–Artin decomposition $H_n(q) \cong \bigoplus_\lambda M_{f^\lambda}(\mathbb{C})$.
`prop:hecke-branching-trace-decomposition`
relies on this decomposition; downstream consumers (binding-energy
analysis via $\rho_K$ refinement, force-carrier saturation
identities) need a partition-by-partition decomposition of $\mathrm{tr}_M$
that the recursive reducer does not directly expose.

The two formulas — recursive Markov-axiom ascent, and
partition-sum Wedderburn — must agree. The agreement was previously
**broken** at q $\ne$ 1 by a wrong character convention: the legacy
`schur_weyl_symbolic.specht_character_atomic` returned the q = 1
classical Murnaghan–Nakayama character $\chi^\lambda_{\mathrm{MN}}(\pi(\beta))$
instead of the q-Hecke character $\chi^\lambda_q(\beta)$. That bug
appeared in two layers (audit log
[`docs/audits/-p3-h-3a-divergence.md`](../../../docs/audits/-p3-h-3a-divergence.md)):

1. **Weight layer:** `schur_weyl_symbolic.schur_weyl_weight` used
   the 2-variable Schur $s_\lambda(q, q^{-1}) / H_q(\lambda)$,
   which **vanishes for partitions with $\geq 3$ rows**.
2. **Character layer:** `specht_character_atomic` returned the
   q = 1 limit of the Hecke character.

Both are now fixed:

- The weight is `y_\lambda(q)` via Wenzl Schur principal
  specialization. Audit + module:
  `prop:hecke-branching-trace-decomposition`.
- The character is `\chi^\lambda_q(\mathcal{B}_K) = \mathrm{tr}\,\rho_\lambda^q(\mathcal{B}_K)`
  via Hoefsmit seminormal matrices at $q_0$. Audit:
  [`docs/audits/-q-hecke-character-gap-closure.md`](../../../docs/audits/-q-hecke-character-gap-closure.md).

## Numerical verification

[`computations/tr_m_q_hecke_seminormal.py`](../../../computations/tr_m_q_hecke_seminormal.py)
produces
[`tr-m-q-hecke-seminormal.witness.json`](../../../computations/tr-m-q-hecke-seminormal.witness.json)
(10 / 10 assertions pass — five atoms $\times$ two tolerance bands at
$10^{-3}$ and $10^{-6}$):

| Atom | $|\mathrm{tr}_M|$ canonical | partition-sum (q-Hecke) | rel err |
|---|---:|---:|---:|
| proton | 1.06530622859 | 1.06530622859 | $3.96 \times 10^{-15}$ |
| neutron | 0.92323329717 | 0.92323329717 | $4.21 \times 10^{-15}$ |
| deuteron | 0.38828647155 | 0.38828647155 | $7.01 \times 10^{-15}$ |
| tritium | 0.10405211868 | 0.10405211868 | $1.07 \times 10^{-14}$ |
| ${}^3$He | 0.20654085856 | 0.20654085856 | $1.03 \times 10^{-14}$ |

The numerical agreement is at **machine epsilon** for all five
atoms (hybrid precision: 30-dps sympy `Float` for $y_\lambda$ +
float64 for $\chi^\lambda_q$). 's
[`rho_k_h3a_refinement.py`](https://github.com/litlfred/qou/blob/claude/refactor-computation-framework-iCqhG/computations/rho_k_h3a_refinement.py)
implements the same closure with **mpmath at 50 dps**, achieving
$1.4 \times 10^{-16}$ on the deuteron (commit
[`c068550c`](https://github.com/litlfred/qou/commit/c068550c)).

## Three production paths

| Path | Module | Use case |
|---|---|---|
| Recursive Markov-axiom | [`markov_trace_recursive.markov_trace_of_word`](../../../computations/markov/markov_trace_recursive.py) | Production $\mathrm{tr}_M$ for mass-table predictions |
| Symbolic partition-sum (50-dps mpmath) | [`rho_k_h3a_refinement.py`](https://github.com/litlfred/qou/blob/claude/refactor-computation-framework-iCqhG/computations/rho_k_h3a_refinement.py) | Per-block $\rho_K$ binding-fraction $\Delta_\lambda$ analysis |
| Float64 partition-sum | [`wedderburn_jones_markov.global_wedderburn_sum_q_hecke_seminormal`](../../../computations/wedderburn_jones_markov.py) | Fast cross-check + reusable API |

All three agree at the precision floor of their respective layers.
The cross-check witness gates this on every CI run.
