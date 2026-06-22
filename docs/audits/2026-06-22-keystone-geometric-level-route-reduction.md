# The geometric-level route is reduced to one owner-gated object — all three reducible surfaces are now closed

**Date:** 2026-06-22
**Branch:** `claude/keystone-geometric-level-functional-2026-06-22`
**Status:** Consolidation — combines this session's trace-surface refutation (#2584) with the
prior eigenvalue-resonance and contact-geometry obstructions to localise the single remaining
open object. No new probe run (the tractable surfaces are corpus-refuted); no fit; nothing wired.
**Bean:** [`s5bb`](../../.beans/s5bb--s5-so3-keystone.md) (q-deformed closure)

## Why no new probe

The owner asked to "try the geometric level" — the trace-free direction the q-deformed
projector probe ([#2584](https://github.com/litlfred/qou/pull/2584),
[`2026-06-22-keystone-qdeform-projector-shift.md`](2026-06-22-keystone-qdeform-projector-shift.md))
pointed to. A corpus-grep (per the formalize-first / corpus-grep discipline) shows the geometric-level
route has three forms reducible to a computation, and **all three are now closed**. Running another
arithmetic or trace probe would re-tread refuted ground — and the 2026-06-16 resonance doc explicitly
warns future agents *not* to re-fit the ℓ=1,2 coincidence.

## The three reducible surfaces — all closed

| Surface | Object | Verdict | Source |
|---------|--------|---------|--------|
| **Eigenvalue resonance** | SO(3) Casimir `ℓ(ℓ+1)` ↔ colour content sum `c(λ)` | **Refuted** — the ℓ=1,2 match (`c=ℓ(ℓ−1)`) is non-unique and fails the ℓ=3 (tau) anchor; tau is multi-block ((3,1,1)+(4,1)) so a single colour eigenvalue is ill-defined | [`2026-06-16-s5so3-reeb-resonance-probe-negative.md`](2026-06-16-s5so3-reeb-resonance-probe-negative.md) |
| **q-deformed Markov-trace projector weight** | `T_g = y_{λ_g}^{H5}·χ^{λ_g}(ι(β_Bor))`, muon (3,2) vs electron (3,1,1) | **Refuted** — non-null (`δ=0.207`, the q-weighting *does* break the (2,1) symmetry the classical multiplicity preserved), but O(1) (67% of `T_μ`), 6–7 orders too large for 210 ppb, not the 207× generation ratio, and bar-MIXED | [`2026-06-22-keystone-qdeform-projector-shift.md`](2026-06-22-keystone-qdeform-projector-shift.md) (this session, #2584) |
| **Contact-geometric equivariant index** | colour-Sasakian Reeb equivariant index = Ocneanu weights `W_λ` | **Owner-gated, multi-session** — and the originally-proposed `SU(3)/SO(3)` (Wu-manifold) arena is *obstructed* | [`2026-06-16-keystone-wu-manifold-reeb-obstruction.md`](2026-06-16-keystone-wu-manifold-reeb-obstruction.md) |

The first two are *arithmetic/algebraic* (a number match or a trace reweighting); both are refuted.
The third is *genuinely geometric* and is the irreducible research core.

## What the canonical Lean already gives (and what it does not)

The on-main Reeb-Casimir Lean (`QOU/BraidsAndKnots/ReebChiralitySeparation.lean`, main `8f343e10`,
sorry-free) establishes the **separation** input of `BringFiberAction.five_distinct_classes`:

- `reebCasimir` (= `ℓ(ℓ+1)` at first SO(3)-tower appearance) gives A:0, T₁:2, H:6, T₂:12, G:12 —
  **not injective** (T₂/G collide at Casimir 12);
- the composite `(reebCasimir, chirality)` **is injective** — it separates all five A₅ irreps,
  with chirality `±1` breaking the T₂/G degeneracy.

This is a **separation of classes**, *not* a mass functional: the key
`(0,0),(2,1),(6,0),(12,−1),(12,0)` distinguishes the irreps but does not *produce* the lepton
masses. Adding chirality as a second coordinate does **not** rescue the resonance route: the ℓ=3
tau is still multi-block, and a `(level, chirality) → mass` map is unforced (a fit) unless derived
from the contact geometry. So the Lean separation does not open a new tractable mass probe.

## The single remaining open object (corrected arena)

Post the Wu-manifold obstruction, the one open object is sharpened to:

> Find the nowhere-zero `U(1) ⊂ SU(3)` colour Reeb **outside the isotropy** (the isotropy `SO(3)`
> fixes the basepoint, so its Killing field cannot be a Reeb), with spacetime and colour as
> **independent factors** (Schur rules out a spacetime-fixing Reeb *inside* an irreducibly-embedded
> `SO(3)⊂SU(3)`), reconcile it with the icosahedral `A₅`, and compute its **equivariant index against
> the Ocneanu weights `W_λ`**.

This is regular-vs-irregular Sasakian geometry on a specific 5-manifold plus an equivariant-index
localisation — genuine differential geometry, **multi-session, not derivable in-session** without
geometry tooling/references (per the Wu-manifold doc's own verdict).

## Net for `conj:s5-so3-fiber-action`

- **Combinatorial backbone:** verified (14/14, on main).
- **Functor:** identified (`Res^{S₅}_{S₃}`).
- **Class separation:** Lean-proved via `(Reeb-Casimir level, chirality)` (main `8f343e10`).
- **q-deformed closure:** the two algebraic surfaces (eigenvalue resonance, Markov-trace projector
  weight) are **refuted**; the conjecture's remaining content is **exactly one** owner-gated object —
  the colour-Sasakian equivariant index `= W_λ` on the corrected independent-factor arena. There is
  **no in-session tractable probe left**; the route is fully reduced to that geometric core.

No fit; nothing wired; `c_k`/`Δ_λ` cal-anchored.

## Cross-references

- [`2026-06-16-s5so3-reeb-resonance-probe-negative.md`](2026-06-16-s5so3-reeb-resonance-probe-negative.md) — eigenvalue-resonance refutation.
- [`2026-06-22-keystone-qdeform-projector-shift.md`](2026-06-22-keystone-qdeform-projector-shift.md) — Markov-trace projector refutation (this session).
- [`2026-06-16-keystone-wu-manifold-reeb-obstruction.md`](2026-06-16-keystone-wu-manifold-reeb-obstruction.md) — corrected arena (independent spacetime⊥colour factors).
- [`content/quantum-observable-universe/lean/QOU/BraidsAndKnots/ReebChiralitySeparation.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/ReebChiralitySeparation.lean) — the (level, chirality) separation (main `8f343e10`).
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — keystone ledger.
