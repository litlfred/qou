> **DEPRECATED on 2026-05-24.** Superseded by [`2026-05-18-1ppb-workplan-v7-100x-experimental.md`](../2026-05-18-1ppb-workplan-v7-100x-experimental.md) (the latest in the 1ppb-workplan chain). Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T4 for the deprecation rationale.

# Refocused 1-ppb workplan v3 — post §3b-cond scaffolding pass

**Date:** 2026-05-09 (UTC)
**Predecessor:** [`2026-05-06-refocused-1ppb-workplan-v2.md`](2026-05-06-refocused-1ppb-workplan-v2.md)

This version supersedes v2 in light of four PRs merged on
2026-05-08/09 (#569, #574, #575, #576). Major changes:

- **α_EM derivation chain** is now §3b-cond conditional and
  sorry-free at every theorem; substantive content reduced to
  named class instances.
- **BlochGroup F quotient** constructed concretely; `pentagonSubgroup`
  built from constrained Rogers-form generators (not the
  over-permissive arbitrary 5-tuple set).
- **Two PSLQ negative-result witnesses** ([Tier-0 atlas](../../computations/tier-0-atlas-pslq-check.witness.json),
  [Tier-1 hyperbolic 3-braid](../../computations/tier-1-hyperbolic-3braid-pslq.witness.json))
  pin the K-theoretic open question for `BringHyperbolicDecomposition`:
  small-coeff $\mathbb{Z}$-linear combinations of hyperbolic 3-braid
  Bloch-Wigner values do **not** span $2/(3\pi)$.
- **`gb_filtration_jet_tracker.py`** extended to figure-8 ($4_1$),
  deuteron ($6_2$), tritium ($8_{11}$) — canonical $T_w$ in $H_3(q)$
  available for 4 of 5 atlas hyperbolic objects ($L_{6a4}$ folds
  into Borromean via the $8G$ identity).
- **Term 7 height-6 partition basis** enumerated for $A \in \{2..6\}$:
  1, 3, 11, 26, 58 partitions. Wedderburn weights $w_\lambda$
  computed at $q_0$. Provides the basis for α_5 fit.
- **Mathlib infrastructure** added: $\mathrm{Cl}_2$ family
  (zero, neg, periodic, reflection at $2\pi$, $\pi$, double-angle
  class), $\mathrm{complexLiTwo} + $ summability on $|z| \leq 1$,
  $\mathrm{blochWigner}$, BlochGroup `QuotientAddGroup` with
  `quot_rogersGenerator_eq_zero` sorry-free.
- **Validate gate:** went from 322 issues → 0 in PR #579 by fixing
  4 enum-mismatch `.ts` files. Future PRs no longer inherit
  cascade failures.

## 1. The 1-ppb floor — current state

The hard floor identified in v1/v2 — $^4\text{He}$ at $+5.87\%$
relative deviation — remains the gating numerical gap. The
structural diagnosis is unchanged:

- $^4\text{He}$ deviation is structurally tied to the **W-2 / $N_v$
  derivation gap**.
- The $\rho_F = 2$ scaling factor in the magic-A formula is tied to
  Wedderburn-pair volumes $|V_X V_Y|_{\rm Wedd}$.

But the route to closure has been substantively re-shaped by the
§3b-cond pass:

**Old route (v2).** Author 3 conjectures (linking, Weinberg
angle, Hoefsmit assignment) → derive $N_v$ → close ⁴He.

**New route (v3).** Three of those conjectures (linking, Hoefsmit,
Higgs) now carry §3b-cond Lean class scaffolding. Two of them
(Term 7, chirality, z-Habiro) are reduced to **finite crystal-graph
computations** via `prop:crystal-basis-resolves-mass-tower-open-problems`.
The α_EM thread shows the pattern: **the 1ppb closure no longer
requires net new theorem-level content** — it requires inhabiting
the §3b-cond class instances numerically/symbolically using the
new compute infrastructure.

## 2. Inventory: what's closed vs open

### Closed (post-#569 through #579)

| Item | How |
|---|---|
| α_EM bare formula via trace ratio | `prop:alpha-em-categorical-trace-ratio` |
| $\tau_{\rm arch}$ uniqueness | `prop:archimedean-functor-uniqueness` (§3b-cond) |
| Additive Bring zero-mode form | `prop:em-coupling-bring-zero-mode` (§3b-cond) |
| Bloch-Suslin pentagon-uniqueness pattern | `BlochSuslinUniqueness` class + Lean theorem |
| Multiplicative gluon-octet form ruled out | superseded banner; structural argument in `alpha-em-derivation-open-problems.md` |
| Block-diagonal Gram deformation ruled out | rank-1 PSLQ of correction term, documented |
| Pre-archimedean concern ($\pi \notin R$) | resolved via `prop:archimedean-functor-uniqueness` |
| BlochGroup F as quotient | `bloch-group-quotient-construction.lean` with constrained Rogers generators |
| Pentagon non-triviality | `validPentagonRelationGenerators_nonempty` (PR #579) |
| Type-B folded crystal cancellation | `prop:type-b-folded-crystal-combinatorics` |
| Cl₂ functional family | zero, neg, periodic, reflection_2π, π, double-angle class |
| blochWigner on unit circle | `BlochWigner_unit_circle θ := Cl_2 θ` |
| complexLiTwo summability on $|z| \leq 1$ | sorry-free with `Summable.of_norm` (PR #575 review fix) |
| GS-NF for figure-8/deuteron/tritium | `gb_filtration_jet_tracker.py` extension |
| Term 7 height-6 partition basis | `term7_height6_partition_enum.py`, A=2..6 |
| Two PSLQ negatives (BringHyperbolicDecomposition) | Tier-0 + Tier-1 witnesses |

### Open — gating 1ppb closure

| Tier | Item | Type | Pathway |
|------|------|------|---------|
| **A** | $N_v$ categorical derivation | substantive math | requires Hoefsmit cell-content + Categorical Higgs (v2 Tier A unchanged) |
| **A** | Linking operation `Lk_R^(k)` | substantive math | properties 2–5 still open (property 1 = linearity proved in v2) |
| **A** | Weinberg angle categorical | substantive math | gated on linking + Hoefsmit + Higgs-vev automorphism |
| **B** | $\rho_F = 2$ derivation in magic-A formula | sibling integration | wedderburn_pair_volumes integration; on-branch since v2 |
| **B** | Term 7 α_5 magnitude | **compute** | partition basis (v3) + Hecke characters from tracker (v3) → numerical fit |
| **B** | Chirality ⟨c⟩_β | **compute** | tracker T_w (v3) + Hoefsmit χ^λ + Type-B folded sum |
| **B** | BringHyperbolicDecomposition | **compute** | Tier-2 PSLQ extension to bridge ≥ 3 hyperbolic knots |
| **C** | ⁴He +5.87% closure | **compute** | depends on Tier-A $N_v$ + Tier-B $\rho_F$ |
| **D** | `BlochSuslinUniqueness` instance | Mathlib upstream | Real.dilog + BlochGroup F + Suslin map |
| **D** | `ArchimedeanLimit x` instance for $x \in (0,1)$ | Mathlib upstream | uniform Tauberian for q-Pochhammer |

**Net change vs v2:** Tier A item 1 ("Hoefsmit assignment
justification") is now half-complete via `gb_filtration_jet_tracker`
+ height-6 partition basis. Tier B has *expanded* from 2 items
to 4, but 3 of those are **compute-driven** rather than
theorem-driven, dramatically lowering the per-item authoring effort.

## 3. What's closeable now (no Mathlib upstream, no new conjectures)

Ordered by yield × tractability:

1. **Tier-2 PSLQ extension** (compute): bridge ≥ 3 hyperbolic knots
   in $H_n$ for $n \in \{4..8\}$. Mechanical extension of the
   existing tier_1 script. Yields a third negative witness or
   the elusive positive hit. **Half-day.**

2. **Term 7 α_5 numerical fit** (compute): combine the partition
   basis ([term7-height6-partition-enum.witness.json](../../computations/term7-height6-partition-enum.witness.json))
   with the Hecke-character data from the tracker
   ([gb-filtration-jet-order.witness.json](../../computations/gb-filtration-jet-order.witness.json))
   plus Hoefsmit seminormal forms, fit α_5 against the AME
   residual. Inhabits `Term7ShellCorrectionClass` with magnitude
   (not just sign-witness). **1–2 days.**

3. **Chirality ⟨c⟩_β concrete computation** (compute): tracker
   gives canonical $T_w$ for $4_1$ and $\mathcal{B}_3$; Hoefsmit
   $\chi^\lambda$ at these → Wedderburn-weighted character average.
   Type-B folded crystal cancellation
   (`PartitionWithCells.content_sum_plus_transpose_content_sum_eq_zero`)
   reduces the sum to the Demazure imbalance. **1–2 days.**

4. **`wedderburn_pair_volumes.py` LP/SDP integration** (sibling-coord):
   v2 §5 noted this as ready-for-pull; on `main` since #569's
   merge cascade. Wire into `prop:knot-operator-lp-selection`
   for the EW-sector dual basis. **Half-day.**

5. **`gb_filtration_jet_tracker.py` extension to $H_n$ for n ≥ 4**
   (compute): the existing infrastructure handles $H_3$; extending
   to higher $n$ unlocks the 4He / 6Li / etc. atomic-knot canonical
   forms required for the magic-A integration. **2–3 days.**

## 4. Critical-path graph (v3)

```
                           ┌─── §3b-cond chain ───┐
                           │ Cl_2 family          │
                           │ blochWigner          │
                           │ BlochGroup quotient  │
                           │ Pentagon nontriv     │
                           └──────────┬───────────┘
                                      │
            ┌─────────────────────────┴──────────────────────┐
            │                                                │
            ▼                                                ▼
   K-theoretic search                              Crystal-basis reduction
   (Tier-0 ⊥, Tier-1 ⊥, Tier-2 next)              (Type-B folding for chirality;
            │                                       height-6 enum for Term 7)
            │                                                │
            └────────── α_EM 1ppb closure ──────────┐        │
                              ▲                     │        │
                              │                     │        │
                              │            Term 7 α_5 fit ◄──┤
                              │                              │
                              │            Chirality ⟨c⟩ ◄───┘
                              │                              │
                              │                              │
              ┌───── N_v derivation (Tier A) ────────┐        │
              │                                      │        │
              │   Hoefsmit cell-content (HALF DONE   │        │
              │   via tracker + partition basis)     │        │
              │                                      │        │
              │   Categorical Higgs (3 conjectures)  │        │
              └──────────────────┬───────────────────┘        │
                                 │                             │
                                 ▼                             ▼
                          ⁴He +5.87% closure
                                 │
                                 ▼
                          1-ppb floor across all observables
```

## 5. Recommended next actions

**This session:**
- (1) Tier-2 PSLQ extension — add to existing PSLQ chain.
- (4) `wedderburn_pair_volumes.py` LP/SDP wiring — pure
  integration, no new content.

**Next 1–2 sessions:**
- (2) Term 7 α_5 fit — first numerical α_5 estimate.
- (3) Chirality ⟨c⟩_β — closes a §3b-cond class with structural
  content.

**Substantive multi-week work (Tier A):**
- Discharge `conj:hoefsmit-ew-cell-content` structural assignment.
- Author `conj:linking-operation` properties 2–5.
- Author `conj:weinberg-angle-categorical`.
- These remain the gating items for $N_v$ and ⁴He.

## 6. Estimated path to 1-ppb closure (v3 update)

| Tier | v2 estimate | v3 estimate | Change |
|------|-------------|-------------|--------|
| A (3 conjectures) | 1–3 weeks each | 1–3 weeks each | unchanged |
| B (integration) | 1–2 weeks | 0.5–1 week | reduced (3 items now compute, not theorem) |
| C (PSLQ closure) | days | days | unchanged |
| **Total** | **4–10 weeks** | **3–8 weeks** | **−1 to −2 weeks** from compute reduction |

The §3b-cond pass has **not** shortened the substantive math
(Tier A unchanged) but has **shortened Tier B by 1–2 weeks** by
converting open theorem-level questions into compute-bound
class-instance closures. The major risk remains the same:
whether the cross-sector PSLQ converges on a clean $N_v$ closed
form, or whether deeper categorical input is required.
