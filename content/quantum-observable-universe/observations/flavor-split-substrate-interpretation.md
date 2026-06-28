**Remark (Bring-surface origin of the formula).**
The closed-form $(q-1)^2 (1 - q^{-4}) / 3$ emerges accordingly from per-sheet
Picard-Lefschetz integration on Bring's color-tube cubic. At the C2
inflection $a_{C2} = 0.4066$, the three color sheets give integrals
$A_1 \in \mathbb{R}$ (one "asymmetric" real sheet) and
$A_{2,3} \in \mathbb{C}$ (complex conjugate pair). Averaging the
flavor-weighted sum $\sum_q \mu_q A_{\text{sheet}(q)}$ over the three
possible placements of the asymmetric flavor recovers the per-quark
averages $(2\mu_u + \mu_d)/3$ and $(\mu_u + 2\mu_d)/3$ for proton and
neutron respectively, with the $1/3$ factor in (5) reflecting this
permutation average. See `probe_per_sheet_flavor_nonin.py` for the
explicit numerical confirmation.

**Remark (limitation).**
The $-0.10\%$ residual on (5) exceeds the formal precision of $q_0$
(~10 ppb from CAL-2), so the substrate ansatz (2) is approximate at
the level of a sub-leading correction. Refining (2) to the
multi-percent precision floor requires either a higher-order
substrate atom (next-to-leading $(q-1)^k$ correction) or a refined
categorical derivation of the per-quark splitting. See the
`witness_dependency_drift.py` validator for the residual budget.
