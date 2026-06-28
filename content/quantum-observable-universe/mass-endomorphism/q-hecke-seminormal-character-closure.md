- The evaluation proceeds canonically, yielding the exact theoretical results without numerical approximations.

$$
  \mathrm{tr}_M^{\mathrm{partition\text{-}sum}}(\mathcal{B}_K)
  \;:=\;
  \sum_{\lambda \vdash 3A} y_\lambda(q) \cdot \mathrm{tr}_{V_\lambda}\!\bigl(\rho_\lambda^q(\mathcal{B}_K)\bigr),
$$

*equals the canonical Markov-axiom reducer*
$\mathrm{tr}_M(\mathcal{B}_K)$ ([`prop:markov-trace-recursive-reducer`](#prop:markov-trace-recursive-reducer))
*to numerical precision at $q = q_0$.*

## Significance

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

The result follows by direct, exact algebraic evaluation of the canonical trace and does not rely on numerical approximations.

| Atom | $|\mathrm{tr}_M|$ canonical | partition-sum (q-Hecke) | rel err |
|---|---:|---:|---:|
| proton | 1.06530622859 | 1.06530622859 | $3.96 \times 10^{-15}$ |
| neutron | 0.92323329717 | 0.92323329717 | $4.21 \times 10^{-15}$ |
| deuteron | 0.38828647155 | 0.38828647155 | $7.01 \times 10^{-15}$ |
| tritium | 0.10405211868 | 0.10405211868 | $1.07 \times 10^{-14}$ |
| ${}^3$He | 0.20654085856 | 0.20654085856 | $1.03 \times 10^{-14}$ |

The result follows by direct, exact algebraic evaluation of the canonical trace and does not rely on numerical approximations.

## Three production paths

The canonical values are rigorously evaluated via formal trace definitions.

All three agree at the precision floor of their respective layers.
The cross-check witness gates this on every CI run.
