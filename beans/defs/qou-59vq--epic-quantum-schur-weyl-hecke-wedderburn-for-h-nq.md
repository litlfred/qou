---
# qou-59vq
title: 'EPIC: quantum Schur-Weyl / Hecke Wedderburn for H_n(q) in Mathlib'
status: in-progress
type: epic
priority: normal
created_at: 2026-08-02T19:32:20Z
updated_at: 2026-11-17T11:53:03Z
parent: qou-rtxm
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


## Arc status measured 2026-08-19 (not inferred from child bean statuses)

**The whole SchurWeyl tree is sorry-free** — 22 files, 0 `sorry`. That is a real
milestone but it is NOT the same as the epic being met: several children are
proved only at concrete n or concrete shape, and their bean statuses had drifted
badly (SW-1/2/4 sat at `todo` for a week while their code was sorry-free on main;
now corrected).

| child | general-n? | actual state |
|---|---|---|
| SW-1 `qou-2xre` H_n(q) def | yes | CLOSED |
| SW-2 `qou-rsbf` SYT / d_lambda | yes | CLOSED |
| SW-3 `qou-wtny` sum d_lambda^2 = n! | **no** | n <= 12 by `decide`; general RSK open |
| SW-4 `qou-u86i` Hoefsmit rho_lambda | yes | CLOSED (#5279) |
| SW-5 `qou-jfr8` irreducibility | **no** | shape (2,1) only |
| SW-6 `qou-j377` semisimplicity | **no** | Burnside-span half, concrete |
| SW-7 `qou-0h5k` Wedderburn iso | **no** | n = 3 only (`wedderburn3`) |
| SW-7-gen `qou-uoal` dim <= n! | yes | CLOSED — spanning bound only |
| SW-8 `qou-tpl5` Markov trace | n=3 | CLOSED as scoped |
| SW-9 `qou-us0a` double centralizer | no | not started |
| SW-JM `qou-t8qh` JM eigenvalue | yes | CLOSED (#5290) |

**The binding constraint is SW-3, and it is upstream of SW-6 and SW-7.** The
lower bound `dim H_n(q) >= n!` (the other half of `uoal`) needs either
sum d_lambda^2 = n! plus joint injectivity of the rho_lambda, or the GS normal-form
route — the latter is `qou-auq3`, actively owned by a sibling. Do not duplicate
auq3; the representation-theoretic route runs through SW-3.



## Reorganisation 2026-10-04

Now the epic for P3.SW under Lean / Mathlib foundations.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.


## Round 58 Progress (lane-e667)
- **PR:** https://github.com/litlfred/qou/pull/8276 (`1909a7bd3bec6ebbdc594cc42f836c8a59fb6451`)
- **Module:** `QOU.Foundations.IsotypicBlockSpolyLaurentHolonomy` (`folio/quantum-observable-universe/lean/QOU/Foundations/IsotypicBlockSpolyLaurentHolonomy.lean`), wired into `QOU.lean`.
- **Theorem:** `isotypic_three_block_projection_and_trace_add` — proves three-stratum central idempotent decomposition (`e0 + e1 + e2 = 1`, `e0² = e0`, `e0 e1 = 0`, `e0 e2 = 0`), orthogonal block projection, and weighted character trace additivity over generic `CommRingCarrier R`, verified at 80 dps in `isotypic-block-spoly-laurent-holonomy.witness.json`.
- **Status:** Kept at `in-progress` pending Merge Manager merge and full dependency verification.

## Progress 2026-11-17 (Round 65 — PR #8331)

- Formalized in `folio/quantum-observable-universe/lean/QOU/Foundations/CumulativeSwapCentralityTabloidTransitionCellProductFactorialCurlTrace.lean` (Lean 4.24.0, `0` `sorry`, `0` `axiom`, `0` warnings, `0` directory-mode static vacuity & borrowed-name advisories).
- 80-dps `mpmath` numerical witness stamped in `computations/probes/cumulative-swap-centrality-tabloid-transition-cell-product-factorial-curl-trace.witness.json` (`scriptHash = 9e4c62bb8c28`, `scriptCommitSha = 4331c3d6858037c7a16d08f2202e77af0fee8a52`, `HEAD = 69f8f329d2048eae2ceddcc8d14985dd544d587f`).
- PR: https://github.com/litlfred/qou/pull/8331 (`ready: 69f8f329d2048eae2ceddcc8d14985dd544d587f`).
