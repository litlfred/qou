# Partition-sum Wedderburn decomposition of the Markov trace

$$
  \mathrm{tr}_M^{\mathrm{partition\text{-}sum}}(\mathcal{B}_K)
  \;:=\;
  \sum_{\lambda \vdash 3A} y_\lambda(q) \cdot \mathrm{tr}_{V_\lambda}\!\bigl(\rho_\lambda^q(\mathcal{B}_K)\bigr),
$$

This partition-sum form equals the canonical Markov-axiom reducer $\mathrm{tr}_M(\mathcal{B}_K)$ ([`prop:markov-trace-recursive-reducer`](#prop:markov-trace-recursive-reducer)) to numerical precision at $q = q_0$.

## Significance

The partition-sum form rewrites the Markov trace via the Wedderburn–Artin decomposition $H_n(q) \cong \bigoplus_\lambda M_{f^\lambda}(\mathbb{C})$. The result `prop:hecke-branching-trace-decomposition` relies on this decomposition. Downstream consumers (such as binding-energy analysis via $\rho_K$ refinement and force-carrier saturation identities) require a partition-by-partition decomposition of $\mathrm{tr}_M$ that the recursive reducer does not directly expose.

The recursive Markov-axiom ascent and partition-sum Wedderburn formulas must agree. The agreement was previously broken at $q \ne 1$ due to a character convention error: `schur_weyl_symbolic.specht_character_atomic` incorrectly returned the classical Murnaghan–Nakayama character $\chi^\lambda_{\mathrm{MN}}(\pi(\beta))$ at $q = 1$ instead of the $q$-Hecke character $\chi^\lambda_q(\beta)$ (see audit log [`docs/audits/-p3-h-3a-divergence.md`](../../../docs/audits/-p3-h-3a-divergence.md)).

Both underlying bugs are now fixed:

1. **Weight layer:** `schur_weyl_symbolic.schur_weyl_weight` incorrectly used the two-variable Schur function $s_\lambda(q, q^{-1}) / H_q(\lambda)$, which vanishes for partitions with three or more rows. It now uses `y_\lambda(q)` via Wenzl Schur principal specialization (`prop:hecke-branching-trace-decomposition`).
2. **Character layer:** `specht_character_atomic` previously returned the $q = 1$ limit of the Hecke character. It now returns the $q$-Hecke character $\chi^\lambda_q(\mathcal{B}_K) = \mathrm{tr}\,\rho_\lambda^q(\mathcal{B}_K)$ via Hoefsmit seminormal matrices at $q_0$ ([`docs/audits/-q-hecke-character-gap-closure.md`](../../../docs/audits/-q-hecke-character-gap-closure.md)).

## Numerical verification

| Atom | $|\mathrm{tr}_M|$ canonical | partition-sum ($q$-Hecke) | Relative error |
|---|---:|---:|---:|
| Proton | $1.06530622859$ | $1.06530622859$ | $3.96 \times 10^{-15}$ |
| Neutron | $0.92323329717$ | $0.92323329717$ | $4.21 \times 10^{-15}$ |
| Deuteron | $0.38828647155$ | $0.38828647155$ | $7.01 \times 10^{-15}$ |
| Tritium | $0.10405211868$ | $0.10405211868$ | $1.07 \times 10^{-14}$ |
| ${}^3$He | $0.20654085856$ | $0.20654085856$ | $1.03 \times 10^{-14}$ |

## Production paths

The canonical values are rigorously evaluated via formal trace definitions. All three paths agree at the precision floor of their respective layers. The cross-check witness gates this on every continuous integration run.
