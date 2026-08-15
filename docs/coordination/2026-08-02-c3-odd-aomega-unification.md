# Coordination ledger — c₃-odd / A_ω / S unification (2026-08-02)

**Goal.** Close the c₃-odd leg of the Δ_λ magnitude chain, i.e. the
fibre→observable evaluation of the bar-odd channel `S = Q_β/E₀` (CAL-2 /
Subgoal-2). This ledger synthesizes the 2026-08-01/02 convergence — it does
**not** supersede the older topic ledgers (`2026-07-25-meridian-holonomy-c3-anchor.md`,
`2026-07-26-q0-varies-imq-c3.md`, `1ppq-qbeta.md`, the `deltalambda-*` set),
it indexes them and records where the arc now stands.

## TL;DR — the arc collapsed onto ONE question

Everything below reduces to: **derive which integer / normalization the
fibre→observable (τ / archimedean) functor applies to the bar-odd channel.**
`c = √A` (the boost-rapidity factor) and `A_ω = 3` (the G3 Stokes integer) are
the **same** question — the measured `A ≈ 2.054` reads as a *reduced Stokes
`A_ω`*, not a dropped Neumann–Zagier ½.

**Search redirect (keystone finding, PR #4554, 2026-08-02):** the integer
target is the **q-exact** GGM symmetry constant `S₁₂+S₂₁ = 3·S₁₁`
(`StokesSymmetryConstant.symmetryConstant_const`, sorry-free). A q-independent
quantity equals its own q→0 value ⇒ **the integer has NO resurgent tail.**
Deriving `A_ω=3` internally therefore collapses to a **decidable q→0 3d-index /
DT count** from Hecke/Bring data — **drivers 11/13 (Lobachevsky volume / crystal
q→0), NOT driver-12 resurgence.** The c₃-via-Borel scaffold is for the c₃
*value/normalization*, not the integer. The precise remaining gap is a
**categorical formula for the q→0 DT count reproducing the pair {3,4} across
knots** — an open problem in DT/3d-index *categorification*, not a QOU wiring
gap.

## Established (proved / closed, on `main`)

| Result | Where | Status |
|---|---|---|
| Fibre→observable **bridge exists** (quantum modularity → Ohtsuki tower at imaginary substrate `b`, `2πb² = i·ln q₀`) | `OhtsukiTowerBarParity.lean` `even_rung_real` / `odd_rung_imaginary`; bridge-verdict audit `2026-08-01-fibre-to-observable-bridge-verdict.md` (PR #4520) | Lean-proved sorry-free |
| **c₃-even CLOSED** — substrate-exact ℚ(√3) ũ-ladder, archimedean face π²/5; never needed Borel | bridge-verdict audit; `2026-07-07-c3-even-solved-s-complex-volume-rigidity.md` | closed |
| **A_ω = 3 is a DT / 3d-index count** (not an assumed value), certified through q⁴⁰⁰; rotated 3d-index of T[4₁] (GGM Conj 4, a theorem for 4₁) | `StokesQZeroDTCount.lean` (q→0 base case `=3`, sorry-free, PR #4534); `StokesSymmetryConstant.lean` (conditional `(S₁₂+S₂₁)/S₁₁=3`) | q→0 certified; internal derivation OPEN |
| FW eq.(14) state-integral **lattice finite-generation** (rank ≤ max{A,B}) | `StateIntegralRecursionLattice.lean` (PRs #4492 + #4522) | sorry-free |
| G3 **realness** (shared conjugation law ⇒ ratio real) | `G3RealnessConjugationBrick.lean` (PR #4485) | sorry-free (covariance hypothesis still conditional) |
| 5₂ **Z[q^±] Stokes** matrices + inversion `S⁺ᵀS⁻=I` (to O(q⁸)) / `det` identities | `FiveTwoStokesMatrixIdentities.lean` (PR #4493); ri9w prefactor (PR #4487) | sorry-free algebraic identities (note: `det W₋₁ = −2` over ℚ, not `+2`) |
| **Φ = 2·𝔙** object dictionary (κ_shape = Im Φ = 2·κ_pot = 2·Im 𝔙) | `ObservableComplexVolumeVsFullPotential.lean` (PR #4552) | sorry-free |
| **`c = √A` is at the precision ceiling** — σ_A ≈ 40% at the ppb q₀-pin; {A=2, Vol(4₁), q₀+q₀⁻¹, q₀²+q₀⁻²} indistinguishable (≤2.63%) | `BoostFactorNZNormalization.lean` (PR #4541) | proved — the number CANNOT be identified numerically |

## The single open question (the keystone)

**Derive the fibre→observable functor integer / normalization internally** — get
the Stokes integer (`A_ω=3`) and the bar-odd normalization from QOU's *own*
categorical drivers (τ-functor action / Wedderburn multiplicity / holonomy
index), **not** by importing GGM's q-series `W₋₁(0)`. Two equivalent faces:

- **A_ω face** — close the gap between "certified as GGM's DT count" and
  "derived from the 13 drivers." Beaned `qou-ujmw` / `qou-sfuo`.
- **Normalization face** — does the observable inherit `κ_shape` (⇒ NZ ½
  dropped ⇒ A=2, c=√2) or `κ_pot` (⇒ the CS invariant)? **Structurally open**
  (`qou-yh67`); physical reading favours `κ_pot`, making c=√2 a
  within-ceiling coincidence rather than a derivation.

**Live convention bug (`qou-pzzl`):** the *same* observable `S` is normalized
`κ_shape=√3/2` in `ArgUPhaseBranchSelection.lean` / `NZBarEvenVolumeFace.lean`
(full potential Φ) but `κ_pot·A_ω=√3/4·A_ω` in the `SDeformedVolumeChannel`
keystone (`PhiBSArgumentIdentification.lean`, complex volume). One is wrong; the
fix depends on `qou-yh67`, so it is beaned, not silently edited.

## Anti-numerology guards (recorded, do not re-trip)

- **`c=√A` cannot be pinned better than ~2.6%** at the ppb q₀-pin — chasing
  `1.4305` vs `√2` vs `Vol(4₁)` below that floor is numerology (PR #4541).
- **`3 = #connections` / `3 = |disc|` are single-knot coincidences** — 5₂'s
  block is 3×3; do not generalize (PR #4534 audit).
- **Importing GGM's `W₋₁` / axiomatizing a class / fitting to 3 is NOT a
  derivation** (anti-laundering). A `κ_shape` pick to *get* c=√2 is a fit.
- The Δ_λ A=3-magnitude side has multiple **scope-(a) negatives** on `main`
  ("no derived element supplies A=3 r*"; "Berezinian cross-term is a fit") —
  corpus-grep before re-declaring any of these open.

## PR / branch map (2026-08-01/02)

**Merged to main (14 PRs):** #4467 (lit/refs/verdict trail), #4474 (4₁ Stokes =
divisor fn), #4475 (5₂ AK integral), #4476 (Borel⇒state-integral class), #4485
(realness), #4487 (Stokes prefactor), #4492 + #4522 (eq14 lattice + FG capstone),
#4493 (Stokes identities), #4520 (bridge verdict), #4530 (Subgoal-2 S bound),
#4534 (A_ω=3 DT q→0), #4541 (c=√A NZ-½ + precision ceiling).

**Open / in-flight:**

| PR | Scope | Note |
|---|---|---|
| #4554 | **keystone** — A_ω internal derivation → q-exact symmetry constant | originating agent still running as of this ledger |
| #4552 | `qou-yh67` NZ-½ observable normalization (structurally open) | ready; merge pending |
| #4553 | Resurgent-bridge Δ_λ → **DT/3d-index unification** (consolidates #4525/#4521/#4519/#4540/#4538/#4551) | **overlaps #4554** — converge, don't duplicate |
| #4521 | A_ω=3 resurgent large-order route (`qou-fgte`) | sibling angle |
| #4515 | c3 dir1 exact figure-8 Im 𝔙₄₁ → A≈2.05 boost enhancement (`qou-iyj5`) | converged with the c=√A / yh67 thread |
| #4555 | `/dispatch-merge` command (tooling) | unrelated; lands the background-merge command repo-wide |

**Convergence note:** #4553 (DT unification) and #4554 (functor integer) are
attacking the same object from two angles; whichever lands the DT-count →
observable bridge first should be cross-cited by the other (coordinated on
#4553 2026-08-02).

## Bean map

- `qou-qnnq` — parent gap (fibre→observable / braid→data), re-scoped with the
  cusp-shape fork.
- `qou-ujmw` / `qou-sfuo` — A_ω=3 DT q→0 landing + open internal-derivation +
  normalization legs.
- `qou-yh67` — NZ-½ observable normalization (structurally open).
- `qou-pzzl` — the κ_shape/κ_pot convention split (reconcile once yh67 resolves).
- `qou-0pym` / `qou-iyj5` — muon-magnitude / boost-rapidity `c=√A` (converged).
- `qou-l7vf` — the program roast + corrected (b)-partial verdict.
- `qou-9dvz` — median-Borel resummation residual (fibre-side).

## How to resolve — routes + literature verdict (2026-08-02)

Resolving the `κ_shape`/A=2 vs `A_ω·κ_pot`/A=3 fork (= `qou-pzzl` = `qou-yh67`),
most-decisive first:

1. **Cross-knot `{3,4}` test on 5₂ — the clean lever, dodges the precision
   ceiling.** The integer target is the *scalar* symmetry constant 3, but the DT
   *spectrum* is the **pair `{3,4}`**; 5₂'s block is 3×3 (vs 4₁'s 2×2). Whether
   `S` carries the scalar constant or the full spectrum is a **structural**
   distinction, decidable by the 5₂ analogue — *not* blocked by `σ_A ≈ 40%`.
   The keystone flagged this as the tentative re-opening (an unchecked
   cross-knot test).
2. **Categorical q→0 DT count from Hecke/Bring (drivers 11/13)** reproducing
   `{3,4}`, and read off whether the S-channel Jacobian keeps `A_ω=3` (PhiBS) or
   drops to `κ_shape=2κ_pot` (ArgU). The keystone's "precise missing ingredient."
3. **A `u=0` anchor** pinning the order-`u²` coefficient (yh67 noted its
   absence). Least likely to materialize.

**Literature verdict (thin/absent for the exact bridge — itself informative):**
- Khovanov–Lauda–Webster ([1005.4559](https://arxiv.org/abs/1005.4559),
  [1309.3796](https://arxiv.org/abs/1309.3796)) categorify the **colored Jones /
  quantum knot invariants**, NOT the 3d-index / DT count.
- The DT / 3d-index side (Garoufalidis topological-invariance
  [1303.5278](https://arxiv.org/abs/1303.5278) in `library/`; DGG state
  integrals) gives `{3,4}` from **triangulation** data, not crystal/Hecke.
- **No categorification of the q→0 DT count `{3,4}` from crystal/Hecke data
  appears to exist** — confirming the keystone's "open problem in DT/3d-index
  categorification" verdict. The resolution is not in a paper; route 1 (the
  structural 5₂ cross-knot test) is the tractable next probe.

## Next concrete, non-overlapping tasks

1. **Wait for #4554 to stabilize, then merge-prep it** (`/dispatch-merge` after
   the originating agent is idle — it correctly refuses while the branch moves).
2. **Reconcile `qou-pzzl`** once `qou-yh67` resolves (mechanical once the
   normalization is fixed).
3. **The keystone**: the internal fibre→observable functor-integer derivation —
   owned jointly by #4554 / #4553; do not open a third parallel attack without
   a genuinely distinct angle.
