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

| Atom | $|\mathrm{tr}_M|$ (convention **D**, muon pin) |
|---|---:|
| Proton | $0.62932842249$ |
| Neutron | $0.47513351767$ |
| Deuteron | $0.15196834396$ |
| Tritium | $0.02914404235$ |
| ${}^3$He | $0.05859625835$ |

> **Ordering corrected 2026-09-05** (`qou-hu1f`). Earlier the same day these
> values were migrated C → D from `atomic-tr-m-mpfr-50dps.witness.json` — which
> was computed **2026-08-29, before** the intra-ordering owner ruling, and had
> never been regenerated. The producer has now been re-run under the ruling and
> the table takes its output:
>
> | atom | grouped (superseded) | **borromean (the ruling)** |
> |---|---:|---:|
> | Proton | $1.14575978232$ | $0.62932842249$ |
> | Neutron | $0.98774375682$ | $0.47513351767$ |
> | Deuteron | $0.57517232973$ | $0.15196834396$ |
> | Tritium | $0.22931014615$ | $0.02914404235$ |
> | ${}^3$He | $0.40376713691$ | $0.05859625835$ |
>
> A factor of $1.8$ to $7.9$, growing with $A$ — far larger than the convention
> migration that preceded it. `atom_braid_word_3A` lays each nucleon's
> confinement core down alternating, `(σ₀σ₁⁻¹)³`, because `σ₀` and `σ₁` do not
> commute and only the alternating word is `β_Bor`.
>
> Both axes are now current: **convention D** and the **borromean** ordering, at
> the muon pin, all three taken from the producer rather than substituted by hand.

> **Migrated C → D, 2026-09-05** (`qou-i229` → `qou-46ab`, owner-approved:
> *"refresh and migrate"*). Source: the canonical Hoefsmit + Wenzl bridge witness
> `atomic-tr-m-mpfr-50dps.witness.json`, which computes these five atoms by this
> block's own stated method $\sum_\lambda y_\lambda \chi_\lambda$ at
> `q0Anchor: muon`.
>
> | atom | was (convention C) | now (convention D) | ratio |
> |---|---:|---:|---:|
> | Proton | $1.06530622859$ | $1.14575978232$ | $1.0755$ |
> | Neutron | $0.92323329717$ | $0.98774375682$ | $1.0699$ |
> | Deuteron | $0.38828647155$ | $0.57517232973$ | $1.4813$ |
> | Tritium | $0.10405211868$ | $0.22931014615$ | $2.2038$ |
> | ${}^3$He | $0.20654085856$ | $0.40376713691$ | $1.9549$ |
>
> The proton ratio is `qou-46ab`'s signature, established there to 50 digits:
> C-frame $1.0653062286131670594$ against D-frame $1.1457597822878355047$,
> $|D-C|/C = 0.0755215$.
>
> **The anchor is unchanged.** The C table was muon-anchored — its per-atom
> $D/C$ ratios match `qou-46ab`'s convention ratio at the muon pin to 8 digits
> and at the proton pin only to 7 — so this is a convention migration, not a
> re-anchoring. The muon pin used is the live one, the same target as the
> `q₀` refresh in this pass.
>
> **The two-column form is withdrawn, not recomputed.** The table used to print
> $|\mathrm{tr}_M|$ *canonical* against *partition-sum* with a $\sim 10^{-15}$
> "relative error", and that column read as a verification of the values. It was
> not: it was the agreement of **two C-frame paths**, which says nothing about
> which convention both are in. The character-closure identity is
> convention-independent and the declaring probe verifies it on abstract braids,
> so the two paths agree under D as well — but **that agreement has not been
> re-measured at these five nuclei**, because the second path is `markov_peel`,
> whose proton and neutron entries `qou-46ab` deliberately removed as unreliable
> (`canonical_tr_m_three_path_comparison.py`). Printing a residual nobody has
> measured would repeat the defect this migration is fixing.

## Production paths

The values above come from the canonical Hoefsmit + Wenzl bridge,
`atomic-tr-m-mpfr-50dps.witness.json`, under the production convention **D**.

The earlier claim that "all three paths agree at the precision floor of their
respective layers" is **withdrawn as stated**: that agreement was measured
within convention C, and `canonical_tr_m_three_path_comparison.py` records that
the three paths do *not* all agree under D — `pyhecke` SW disagrees by orders of
magnitude and the legacy path by ~15 % — while `markov_peel`'s proton and
neutron entries were deliberately removed as unreliable (`qou-46ab`). What holds
is the narrower statement the block actually needs: bridge ≡ `markov_peel` where
both are recorded.

The declaring witness, `q-hecke-seminormal-character-closure-probe`, verifies the
character-closure identity on five **abstract** $B_3$ braids (identity,
$\sigma_1$, the Coxeter element, the figure-8, the full twist) and contains no
nucleon, so it is a structural verifier of the identity — which is
convention-independent — and not the producer of this table.
