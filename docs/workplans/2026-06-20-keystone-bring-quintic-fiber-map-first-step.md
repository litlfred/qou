# Keystone geometric fibre map — Bring-quintic first-step workplan

**Date.** 2026-06-20.
**Bean.** s5bb (s5-so3 keystone) / `conj:s5-so3-fiber-action`.
**Status.** WORKPLAN ONLY — no construction in this doc. Scopes the *next*
(dedicated, coordinated) session. Owner-authorised 2026-06-20.

## The exact open object

[`S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean)
states the conditional class but provides **no instance**:

```lean
class BringFiberAction where
  irrepToRotation : A5Irrep → IcosahedralRotation
  five_distinct_classes :
    Function.Injective (fun r : A5Irrep => (irrepToRotation r).asSO3.angle)
```

The combinatorial backbone (dim²-sum = 120, conjugation involutive,
`Res^{S₅}_{S₃}` dimension-consistency, the `icosBranchingMult` table, the McKay
2I↔E₈ anchors) is **already sorry-free**. The single open step is a **derived**
`irrepToRotation`: each of the five A₅ irreps `{A, T₁, T₂, G, H}` ↦ a specific
icosahedral rotation, **induced by Bring's quintic geometry**, hitting five
distinct angles.

## Discipline guard (read before writing any instance)

- **No arbitrary instance.** Assigning the five icosahedral angles
  `{0, π, 2π/3, 2π/5, 4π/5}` to the five irreps in any hand-picked order
  satisfies `five_distinct_classes` *vacuously-of-content* — it is a non-geometric
  map and is **rejected** (the file docstring + `2026-06-13-bring-fiber-action-falsification.md`
  already record the falsified `: True` / trivial-instance pattern). The
  instance must be **derived** from Bring's automorphism action, and the
  derivation — not the injectivity — is the deliverable.
- **210 ppb is NOT the target.** #2520 (consumer side) showed the geometric
  frontier carries the **O(1) generation skeleton** (weight ratio
  `y_(3,2)/y_(3,1,1)=3.68` at q₀), and **none** of the 210 ppb fine shift
  (2.1e-7, anchor artifact, refuted as a vector path). Do not aim the
  construction at the muon ppb.
- **Period-axis ≠ coupling-axis.** The cyclotomic-Galois / `Li₃(ζ₅)` period
  facts are the **z-side** (quantum-dilog completion), orthogonal to the
  **q-side** keystone coupling (#2517 inoculation). Verify the axis before
  treating any Galois fact as keystone-bearing.

## The geometry (grounded facts)

- Bring's curve `Σ₄`: genus **4** (`brings_genus := 4`), `Aut(Σ₄) = S₅` (order
  120) — the maximal automorphism group for genus 4 (corpus:
  [`bring-trefoil-cinquefoil-channel.md`](../../content/quantum-observable-universe/brings-surface/bring-trefoil-cinquefoil-channel.md)).
- `H¹(Σ₄, ℂ)` has dim `2g = 8`; the holomorphic differentials `H⁰(Σ₄, Ω¹)`
  have dim `g = 4` and form a **4-dimensional S₅-representation**.
- **Classical fact to confirm in-session:** `H⁰(Ω¹) ≅ V_(4,1)` (the standard
  4-dim irrep). Restricting to `A₅`: `V_(4,1)|_{A₅} = G` (the 4-dim A₅ irrep).
  So the geometric A₅-action on holomorphic differentials *is* the `G` irrep —
  the anchor the rotation map must be consistent with.

## Candidate sources for `irrepToRotation` (rank in-session, pick the derived one)

| candidate | construction | gives 5 distinct angles? | verdict-to-test |
|---|---|---|---|
| **(a) SO(3)-tower first-appearance ℓ** | each A₅ irrep ↦ rotation of the lowest `ℓ` it appears at in `icosBranchingMult` (already in Lean: A@0, T₁@1, H@2, T₂@3, G@3) | **NO** — T₂ and G collide at ℓ=3 | reuse existing Lean facts; **insufficient alone** — needs a tie-break from the curve |
| **(b) icosahedral class–irrep duality** | the 5×5 character table pairs 5 irreps ↔ 5 conjugacy classes; map irrep ↦ the class' rotation angle via a *canonical* pairing (e.g. Springer / principal-element eigenvalue) | candidate YES | the pairing must be **canonical**, not hand-chosen — this is the real math |
| **(c) action on a distinguished configuration** | the rotation each irrep induces on the 12 icosahedron vertices / 5 inscribed tetrahedra / the 5 "Bring points" of `Σ₄` | candidate YES | most directly "Bring-induced"; needs the explicit `Σ₄` automorphism matrices |
| **(d) McKay/E₈ exponent grade** | use the 2I↔affine-E₈ marks `[1,2,3,4,5,6,4,2,3]` / E₈ exponents to grade the irreps | partial | already anchored in Lean (`binaryIcosahedralIrrepDims`); ties irreps to exponents, not directly to angles |

**Recommended attack:** (c) as primary (most literally "induced by Bring's
quintic"), cross-checked against (b); use (a)+(d)'s existing Lean facts as
consistency constraints (the map must respect `icosBranchingMult` and the McKay
grading). The injectivity `five_distinct_classes` then *follows from* the
derivation rather than being imposed.

## Deliverable chain for the construction session

1. **Extract the `Σ₄` S₅-automorphism matrices** on `H⁰(Ω¹)` (4-dim) — confirm
   `≅ V_(4,1)`, restrict to `A₅` → `G`.
2. **Define the canonical `irrepToRotation`** via (c)/(b); record the 5 angles.
3. **Provide the honest `BringFiberAction` instance**; prove `five_distinct_classes`
   from the derived angles (not by fiat). Verify sorry-free via lean-direct
   (restore `lake-cache/qou-v4-24-0` oleans + `LEAN_PATH` — recipe proven this
   session).
4. **Connect to the W_λ frontier:** check whether the derived rotation grades
   reproduce the q-Plancherel weights `W_λ = d_q²/[n]_q!` and the defect
   `1−Z(n) = −n(n−1)(2n−13)/144` (#2527) — the algebraic shadow the geometry must
   match. **Refute-or-constrain**, no fit.

## Coordination (do this first, in-session)

- The active W_λ cluster — **#2516 / #2517 / #2519 / #2520 / #2528** (+ the A≥3
  compute #2369/#2371/#2372) — owns the **algebraic/consumer** side (`W_λ`,
  `1−Z` defect, f_pn wiring). The geometric leg (this workplan) touches **only**
  `S5SO3FiberAction.lean` + a new construction script — **no overlap** with their
  files. Post one intent comment on the keystone ledger / the most active sibling
  before starting, declaring the geometric-leg scope.

## Honest risk flags

- The construction may come out **null/under-determined** (the geometric map may
  not be canonical without extra input) — this is acknowledged up front; a
  refutation that pins *why* it is under-determined is a valid outcome.
- Effort: **multi-session** (1 session for steps 1–3 if `H⁰(Ω¹)` matrices are
  clean; step 4 + any q-deformation is further). Not a session-tail task — hence
  this workplan rather than a thin start.
