# Transverse NA-Stokes surface-curvature — forward geometric route (does NOT close the deuteron magnitude; the object is bracketed but transport-unpinned)

**Date:** 2026-08-08 · **Branch:** `claude/nastokes-transverse-curvature-2026-08-08` ·
**Bean:** `qou-prjo` (LEAD-2, geometric surface-curvature route; LEAD-1 is the
parallel algebraic ≥3-body cumulant route) · **Epic:** `qou-r2nh` (Δ_λ arc) ·
**Tier:** 1 sorry-free Lean structure + 1 forward 0-fit probe (scope-(a) negative).
**No fit, no AME inversion, nothing wired, q₀-free.**

## 0. TL;DR

The transverse NA-Stokes surface-curvature pairing `Ω₂ = ½ P ∮∮ [𝓕,𝓕]` — the
named surviving carrier of the deuteron binding *magnitude* after braid-word /
scale / level / edge / DT-count are all excluded — was attacked **forward and
geometrically**. Committing to the geometric definition *before* comparing to
AME:

1. **Structure formalized, sorry-free** (`lean`-direct exit 0, `#print axioms`
   clean): the Seifert-surface Betti combinatorics (`b₁ = c−s+1 = 2g`) and the
   ordered transverse pairing over a generic ring, including **THE WALL** —
   a nonzero transverse magnitude *forces* position-dependent (transport-
   twisted) curvature, i.e. requires exactly the surface-2-form data the corpus
   lacks.
2. **Forward magnitude does NOT close it (scope-(a)).** With the trefoil anchor
   `b₁=2` and `A−1` inter-nucleon links, the AME binding ratios sit **between**
   the diagonal (additive `∝ b₁`, undershoots) and off-diagonal (full pairing
   `∝ C(b₁,2)`, overshoots) envelopes — the same bracketing shape as the
   na-Stokes `ℏ⁰`(diverge)/`ℏ²`(undershoot) leg.
3. **sorry-free ≠ derived.** The magnitude is *not* derived: the interpolating
   weight between the two envelopes is the transport `U(x,O)` across the Seifert
   surface, which is the missing canonical discretization (the wall stands).

## 1. The forward geometric definition (committed before matching)

The order-2 Magnus term of the surface-ordered exponential is
`Ω₂ = ½ P ∮∮ [𝓕,𝓕]`, `𝓕(x) = U(x,O)⁻¹ F_q U(x,O)`, quadratic in the germ
commutator q-curvature `F_q = [δq₁,δq₂]`
([`germ-commutator-q-curvature.md`](../../content/quantum-observable-universe/quantum-observable-universes/germ-commutator-q-curvature.md)).
It is **transverse** to the strand ordering (the two-observer-parallelogram
direction), so it survives on the single-generator `σ₁³` deuteron channel where
every *inter-crossing* Magnus commutator vanishes (`[a,a]=0`;
[`2026-07-24-eunit-magnus-order2.md` §2](2026-07-24-eunit-magnus-order2.md)).

Discretize the Seifert surface of a connected positive-braid diagram (`s`
strands, `c` crossing letters, Seifert's algorithm):

- Euler characteristic `χ = s − c`; first Betti number `b₁ = 1 − χ = c − s + 1 = 2g`
  — the number of independent transverse 2-cycles (handles) carrying curvature.
- Two envelopes of the magnitude, with `κ² = ‖F_q‖²` universal (cancels in ratios):
  - **diagonal / additive** — one `κ²` per handle: `M_diag ∝ b₁`;
  - **off-diagonal / full surface-ordered pairing** — all handle-pair
    commutators `[𝓕_i,𝓕_j]`: upper envelope `M_off ∝ C(b₁,2)`.
- The **true** magnitude sits between, weighted by the transport twists.

## 2. Lean (sorry-free, `lean`-direct exit 0)

[`QOU/MassTheory/TransverseSurfaceCurvature.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/TransverseSurfaceCurvature.lean)
(registered in `QOU.lean`; `#print axioms` = `propext, Classical.choice,
Quot.sound` only — no `sorryAx`):

| Declaration | Content |
|---|---|
| `seifertBettiOne s c := c − s + 1` | `b₁ = 2g` of the diagram's Seifert surface |
| `seifertBettiOne_trefoil : … = 2` | deuteron `σ₁³` (s=2,c=3), genus 1 — concrete, falsifiable |
| `seifertBettiOne_link_additive` | `b₁(c+k)=b₁(c)+k` — **exact linearity = the pairwise cap** |
| `seifertBettiOne_extensive` | `b₁(3A, ρA)=(ρ−3)A+1` — extensive iff crossing density `ρ>3` |
| `curvComm`, `curvComm_antisymm` | `⟦a,b⟧=a·b−b·a`, antisymmetric 2-form (generic `Ring`) |
| `listPairing` | discrete ordered `½P∮∮[𝓕,𝓕]` |
| `listPairing_eq_zero_of_all_comm`, `listPairing_const` | flat / commuting surface ⇒ pairing `= 0` |
| **`transverse_nonzero_needs_noncommuting_curvature`** | **THE WALL** — nonzero pairing forces position-dependent transported curvature |
| `transverseMagnitudeDiagonal` (+ trefoil/flat/link-additive) | `½·b₁·κ²` diagonal envelope |

**Discipline.** Axiomatizing the curvature is NOT deriving its magnitude. The
Lean proves the *structure* (vanishing conditions, combinatorics, the wall),
never the numerical magnitude. `listPairing_pair` shows the object is not
vacuously zero (nonzero for non-commuting curvatures).

## 3. Forward probe (0 free parameters)

[`computations/probes/nastokes_transverse_curvature_seifert_probe.py`](../../computations/probes/nastokes_transverse_curvature_seifert_probe.py)
(witness `nastokes-transverse-curvature-seifert.witness.json`, 6 assertions).
Geometric inputs — **pure geometry, not fitted**: trefoil anchor `b₁_link = 2`;
inter-nucleon links `L = A−1` (spanning tree = the color-tube audit's "A−1
inter-nucleon Hecke generators"); `b₁(A) = 2(A−1)`. AME as **fixed ratios only**.

| iso | A | links | b₁=2g | AME/D | diag/D (∝b₁) | off/D (∝C(b₁,2)) |
|-----|---|-------|-------|-------|--------------|-------------------|
| D   | 2 | 1 | 2 | 1.000 | 1.000 | 1.000 |
| T   | 3 | 2 | 4 | 3.813 | 2.000 | 6.000 |
| ³He | 3 | 2 | 4 | 3.469 | 2.000 | 6.000 |
| ⁴He | 4 | 3 | 6 | 12.720 | 3.000 | 15.000 |

**Forward findings (facts, not fits):**

1. The additive/diagonal envelope **undershoots** ⁴He (3.00 vs 12.72).
2. The off-diagonal envelope **overshoots** ⁴He (15.00 vs 12.72).
3. AME is **bracketed** between the two envelopes at every isotope — the same
   shape as the na-Stokes `ℏ⁰`(diverge)/`ℏ²`(undershoot) bracketing
   ([`2026-08-02-brane-resummation-nastokes-volume-difference.md`](2026-08-02-brane-resummation-nastokes-volume-difference.md)).
4. The additive envelope is **exactly linear** in link count (mirrors the Lean
   `seifertBettiOne_link_additive`) — i.e. **pairwise-capped**, so the diagonal
   reading **cannot** be the ≥3-body super-pairwise term the corpus proves is
   required ([`2026-08-02-deltalambda-value-proved-…-additive-term.md` §4](2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md)).
5. **Isospin-blind:** T and ³He (both A=3) get *identical* geometry but AME
   differs by ~8% (the p/n mirror split) — genus/Betti topology alone cannot
   produce the T vs ³He splitting (consistent with the color-tube weight being
   a *separate* object from the extensive magnitude).

## 4. Verdict (honest, scope-(a))

- **Does NOT close the deuteron magnitude.** Neither geometric envelope
  reproduces the AME ratios: the diagonal reading undershoots and is
  pairwise-capped; the off-diagonal reading overshoots. This is a
  **scope-(a)** result ("this construction, as-read, does not reproduce the
  numbers"), not a scope-(b) exclusion of the transverse object itself.
- **Scope-(b), proved sub-exclusion:** the *diagonal / Betti-count reading* is
  excluded as the ≥3-body carrier — invariant cited: exact linearity of `b₁`
  in crossing count (`seifertBettiOne_link_additive`, Lean-proved) ⇒
  pairwise-capped. A genuinely ≥3-body enhancement can only come from the
  *off-diagonal* cross-handle commutators.
- **The wall stands, now formalized.** A nonzero transverse magnitude forces
  position-dependent transported curvature `𝓕(x) = U(x,O)⁻¹ F_q U(x,O)`
  (`transverse_nonzero_needs_noncommuting_curvature`). The interpolating weight
  between the diagonal and off-diagonal envelopes **is** the transport `U(x,O)`
  across the Seifert surface — the canonical surface-2-form discretization the
  corpus lacks.

## 5. Precise surviving sub-question (the next honest unit)

> **Compute the surface-ordered transport `U(x,O)` on the trefoil (genus-1)
> Seifert surface and evaluate the off-diagonal cross-handle pairing
> `Σ_{i<j} [U_i⁻¹ F_q U_i, U_j⁻¹ F_q U_j]`.** The forward probe shows the true
> magnitude lands between `b₁·κ²` (diagonal) and `C(b₁,2)·κ²` (all handle-pairs);
> the transport twists select the interpolation. Two concrete inputs are still
> missing: (i) the Seifert-surface cell complex + a canonical band-transport for
> `σ₁³` (deuteron) and for the multi-nucleon channels — **the corpus has no
> canonical multi-nucleon Seifert braid word** (only the deuteron trefoil is
> pinned); (ii) whether the cross-handle term is genuinely non-additive over
> links (super-pairwise) — required to escape the diagonal pairwise cap.

Until (i) and (ii) exist the deuteron magnitude stays open. This route
**localizes** the missing physics to the off-diagonal transport weighting, and
proves (Lean) that the diagonal Betti-count reading is a dead end for the
≥3-body term.

## 6. Coordination

LEAD-1 attacks `qou-prjo` via the **algebraic ≥3-body cumulant** route; this is
the **geometric surface-curvature** route. Convergence test: if the
off-diagonal cross-handle pairing (this route) is genuinely non-additive over
links, it *is* a ≥3-body cumulant (LEAD-1's object) — the two routes should meet
at the same super-pairwise term. Do NOT redo any diagonal/additive/Betti-count
closure — Lean-proved pairwise-capped here.

## Files
- Lean: [`content/quantum-observable-universe/lean/QOU/MassTheory/TransverseSurfaceCurvature.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/TransverseSurfaceCurvature.lean)
- Probe: [`computations/probes/nastokes_transverse_curvature_seifert_probe.py`](../../computations/probes/nastokes_transverse_curvature_seifert_probe.py)
- Witness: [`computations/probes/nastokes-transverse-curvature-seifert.witness.json`](../../computations/probes/nastokes-transverse-curvature-seifert.witness.json)
- This report: `docs/audits/2026-08-08-nastokes-transverse-surface-curvature-geometric-route.md`
