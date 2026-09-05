# Partition-sum Wedderburn decomposition of the Markov trace

$$
  \mathrm{tr}_M^{\mathrm{partition\text{-}sum}}(\mathcal{B}_K)
  \;:=\;
  \sum_{\lambda \vdash 3A} y_\lambda(q) \cdot \mathrm{tr}_{V_\lambda}\!\bigl(\rho_\lambda^q(\mathcal{B}_K)\bigr),
$$

This partition-sum form equals the canonical Markov-axiom reducer $\mathrm{tr}_M(\mathcal{B}_K)$ ([`prop:markov-trace-recursive-reducer`](#prop:markov-trace-recursive-reducer)) to numerical precision at $q = q_0$.

## Significance

The partition-sum form rewrites the Markov trace via the Wedderburn–Artin decomposition $H_n(q) \cong \bigoplus_\lambda M_{f^\lambda}(\mathbb{C})$. The result `prop:hecke-branching-trace-decomposition` relies on this decomposition. Downstream consumers (such as binding-energy analysis via $\rho_K$ refinement and force-carrier saturation identities) require a partition-by-partition decomposition of $\mathrm{tr}_M$ that the recursive reducer does not directly expose.

The recursive Markov-axiom ascent and partition-sum Wedderburn formulas must agree. The agreement was previously broken at $q \ne 1$ due to a character convention error. `schur_weyl_symbolic.specht_character_atomic` incorrectly returned the classical Murnaghan–Nakayama character $\chi^\lambda_{\mathrm{MN}}(\pi(\beta))$ at $q = 1$ instead of the $q$-Hecke character $\chi^\lambda_q(\beta)$.

Two layers have to be got right, and each has a natural wrong answer:

1. **Weight layer.** The two-variable Schur function $s_\lambda(q, q^{-1}) / H_q(\lambda)$ vanishes for partitions with three or more rows and so cannot serve as the weight. The correct weight is $y_\lambda(q)$, the Wenzl Schur principal specialisation (`prop:hecke-branching-trace-decomposition`).
2. **Character layer.** The $q = 1$ limit of the Hecke character is not the character required here; the trace must be taken of the $q$-Hecke character $\chi^\lambda_q(\mathcal{B}_K) = \mathrm{tr}\,\rho_\lambda^q(\mathcal{B}_K)$, via Hoefsmit seminormal matrices at $q_0$.

## Numerical verification

| Atom | $|\mathrm{tr}_M|$ canonical | partition-sum ($q$-Hecke) | Relative error |
|---|---:|---:|---:|
| Proton | $1.06530622859$ | $1.06530622859$ | $3.96 \times 10^{-15}$ |
| Neutron | $0.92323329717$ | $0.92323329717$ | $4.21 \times 10^{-15}$ |
| Deuteron | $0.38828647155$ | $0.38828647155$ | $7.01 \times 10^{-15}$ |
| Tritium | $0.10405211868$ | $0.10405211868$ | $1.07 \times 10^{-14}$ |
| ${}^3$He | $0.20654085856$ | $0.20654085856$ | $1.03 \times 10^{-14}$ |

> **⚠ This table is in the EXCISED convention C** (measured 2026-09-05,
> `qou-i229`; probe
> `the_character_closure_block_and_a_lean_file_publish_convention_c_probe.py`,
> 5/5). The canonical Hoefsmit + Wenzl bridge witness computes these same five
> atoms by **this block's own stated method**, $\sum_\lambda y_\lambda
> \chi_\lambda$, and agrees with none of them:
>
> | atom | published | canonical bridge | ratio |
> |---|---:|---:|---:|
> | Proton | $1.06530622859$ | $1.14575969245730087$ | $1.0755$ |
> | Neutron | $0.92323329717$ | $0.98774368811580957$ | $1.0699$ |
> | Deuteron | $0.38828647155$ | $0.57517224391777187$ | $1.4813$ |
> | Tritium | $0.10405211868$ | $0.22931010210455651$ | $2.2038$ |
> | ${}^3$He | $0.20654085856$ | $0.40376703685142817$ | $1.9549$ |
>
> The proton ratio is the signature `qou-46ab` established to 50 digits:
> C-frame $1.0653062286131670594$ against D-frame $1.1457597822878355047$,
> $|D-C|/C = 0.0755215$.
>
> **The "relative error" column below is agreement between two *C-frame* paths.**
> Two paths agreeing tells you nothing about which convention both are in, and
> that column has been read as a verification of the table. It is not one.
>
> **Not recomputed.** Migrating to convention D is `qou-46ab`'s scoped job: it
> moves all five published figures by 7–120 %, and
> [`MarkovPeelH3.lean`](../lean/QOU/Interactions/MarkovPeelH3.lean) carries the
> same C value and must move in the same pass. Labelled rather than changed, the
> precedent `df13e845cee` set.
>
> `qou-46ab`'s own sweep could not see this block: it scanned for the literal
> `1.06530622861316`, and this table renders the same quantity as
> `1.06530622859`.

## Production paths

The canonical values are rigorously evaluated via formal trace definitions. All
three paths agree at the precision floor of their respective layers — **within
convention C**; see the box above. The declaring witness,
`q-hecke-seminormal-character-closure-probe`, verifies the character-closure
identity on five **abstract** $B_3$ braids (identity, $\sigma_1$, the Coxeter
element, the figure-8, the full twist) and contains no nucleon, so it is a
structural verifier of the identity and not the producer of this table.
