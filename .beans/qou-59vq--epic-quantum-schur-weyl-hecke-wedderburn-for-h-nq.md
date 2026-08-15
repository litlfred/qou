---
# qou-59vq
title: 'EPIC: quantum Schur-Weyl / Hecke Wedderburn for H_n(q) in Mathlib'
status: todo
type: epic
created_at: 2026-08-02T19:32:20Z
updated_at: 2026-08-02T19:32:20Z
---

The load-bearing gap for the whole QOU->SM program: no Schur-Weyl in Mathlib at all. Goal: construct HeckeWedderburnData (QOU.SchurWeyl) for the real H_n(q) -- H_n(q) iso ⊕_{λ⊢n} M_{d_λ}(K), d_λ=#SYT(λ), tr_M=Σ_λ w_λ χ_λ; Phase 3 the Jimbo double-centralizer U_q(gl_N)×H_n(q) on V^⊗n. Realizes R2-inst under qou-mpq5. Dependency-ordered children SW-1..SW-9.

## Mathlib support map (2026-08-02 recon agent, v4.24.0)

| Piece | Mathlib status | Bean |
|---|---|---|
| FreeAlgebra + RingQuot universal property | ✅ ergonomic (`RingQuot.liftAlgHom`, `FreeAlgebra.lift`) | SW-1 |
| Coxeter type-A (=S_n) scaffolding | ✅ `CoxeterSystem`/`CoxeterMatrix` | SW-1 |
| Iwahori–Hecke / Temperley–Lieb / braid algebra | ❌ absent — build it | SW-1 |
| Partitions `Nat.Partition` (+Fintype) | ✅ | SW-2 |
| StandardYoungTableau / #SYT / hook-length | ❌ Mathlib; ✅ in-repo `QOU.Mathlib` | SW-2 |
| RSK, Σ(#SYT)²=n! | ❌ Mathlib; partial in-repo (`rskBurnsideHolds_le12`, n≤12 by decide) | SW-3 |
| Wedderburn–Artin ⊕Mₙ | ⚠️ EXISTENCE only (`exists_algEquiv_pi_matrix_of_isAlgClosed`); blocks/dims existential, not partition-indexed | SW-6/7 |
| K[S_n] semisimple (Maschke) | ✅ free instance | SW-6 |
| Tits deformation / generic-q transfer | ❌ absent — hand work (discriminant/Gram nonvanishing) | SW-6 |
| Specht modules / S_n irreps↔λ | ❌ absent (chars ✅); count via cycle-type=partition assemblable | SW-5/7 |
| Matrix.trace_blockDiagonal, char orthogonality | ✅ | SW-8 |
| double centralizer / Jacobson density | ❌ absent — LARGE gap, the heart of SW duality | SW-9 |

**Critical-path takeaway:** SW-1 (RingQuot) and SW-2 (in-repo reuse) are the
easy wins. The three dominating gaps with zero Mathlib support are (a) the
generic-q semisimplicity transfer (SW-6), (b) the partition-indexed
Wedderburn iso beyond bare existence (SW-7), and (c) Jacobson density /
double-centralizer (SW-9). SW-7 may be reachable via the existence form +
dim-count (Σd_λ²=n!) matching rather than SW-9's full duality — so the
`HeckeWedderburnData` instance (SW-8/R2-inst) does NOT require SW-9.
