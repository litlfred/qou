# Chasing lead (iii): the ED ↔ S²(2,3,5) A₅-action identification does NOT nail directly — it is a C₅/ζ₅ pentagon, and the icosahedral bridge is Klein's, not a base action

**Date:** 2026-06-28
**Branch:** `claude/q-askey-scheme-gaps-wubsmv`
**Status:** Scope-limited negative **(a)** + re-scope. Corrects part (iii) ("a lead") of
[`2026-06-28-ed-ambient-s3-gauge-embedding-wlambda-scope.md`](2026-06-28-ed-ambient-s3-gauge-embedding-wlambda-scope.md).
**Check:** [`scripts/keystone_ed_a5_orbit_obstruction.py`](../../scripts/keystone_ed_a5_orbit_obstruction.py) (parameter-free, exit 0).
**Keystone bean:** `s5bb`; ledger [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md).

## The lead and the chase

The prior audit proposed (part iii) that the exceptional divisor `ED ≅ ℂP¹`
carries the icosahedral `A₅` action with quotient `ED/A₅ ≅ S²(2,3,5)`,
geometrically forcing the keystone's Poincaré-sphere arena `S³/2I` from Bring's
symmetry. The "open step" it flagged was: *confirm the QOU ED literally carries
that `A₅` action*. Chasing that step settles it — **negatively, as stated.**

## What the corpus base actually is (not icosahedral)

Three corpus blocks pin the base/ED geometry, and it is a **pentagon, not an
icosahedron**:

- [`brings-surface/hyperelliptic-quintic.md`](../../content/quantum-observable-universe/brings-surface/hyperelliptic-quintic.md):
  the base `ℂP¹` has **6 branch points `{ζ₅ᵏ : k=0..4} ∪ {∞}`** — the five
  fifth-roots of unity plus `∞`.
- [`brings-surface/brings-riemann-hurwitz.md`](../../content/quantum-observable-universe/brings-surface/brings-riemann-hurwitz.md):
  the canonical covering `π : Σ₄ → ℙ(V)` has **degree 4**, total ramification
  `R = 14`, over **6 branch points** distributed by `S₅`.
- [`brings-surface/fivefold-symmetry.md`](../../content/quantum-observable-universe/brings-surface/fivefold-symmetry.md):
  `S₅` acts as the **monodromy** of the sheeted covering `Σ₄ → ℙ¹` (the five
  coordinate-sheets, branch monodromy = transpositions `(xᵢxⱼ)`), **not** as
  Möbius transformations of the base.

So the symmetry *manifest on the base* `ℂP¹` is the **cyclic `C₅` / dihedral
`D₅` pentagon** of the marked set `{ζ₅ᵏ, ∞}` (the `ζ₅` rotation), with `S₅`
entering as deck/monodromy of the covering — **not** an icosahedral `A₅` Möbius
action.

## Two structural obstructions to the naive A₅ identification

**Obstruction 1 — `S₅ ⊄ PSL(2,ℂ)`.** The finite subgroups of the Möbius group
`PSL(2,ℂ)` are exactly `{Cₙ, Dₙ, A₄, S₄, A₅}` (Klein). `S₅` (order 120) is not
among them. So the full `Aut(Bring) = S₅` **cannot** act on the base `ℂP¹` by
holomorphic automorphisms; at most a proper subgroup can. (Consistently, the
corpus has `S₅` as *monodromy*, not as base Möbius maps.)

**Obstruction 2 — the 6 branch points are not `A₅`-invariant.** Even restricting
to the largest admissible Möbius subgroup `A₅`: a point-stabiliser of any
`SO(3)` action on `S² = ℂP¹` is **cyclic**, and the cyclic subgroups of `A₅`
have orders only `{1,2,3,5}` (the element orders of `A₅`). By orbit–stabiliser
the orbit sizes are `60/{1,2,3,5} = {60,30,20,12}` — the classical 12 vertices /
20 faces / 30 edges / 60 generic. The **minimum nonzero orbit is 12**, and every
finite `A₅`-invariant subset of `ℂP¹` is a union of orbits, so **no
`A₅`-invariant set has 6 points**. The ED's 6-point branch divisor `{ζ₅ᵏ, ∞}` is
therefore **not** `A₅`-invariant — `A₅` is not a symmetry of the marked ED.
(Verified: [`keystone_ed_a5_orbit_obstruction.py`](../../scripts/keystone_ed_a5_orbit_obstruction.py),
orbit sizes `{12,20,30,60}`, `6 ∉`.)

The deeper reason the two pictures don't coincide: the pentagon "5" (the cyclic
`C₅` of fifth-roots `ζ₅ᵏ`) and the icosahedral "5" (the `5 = [A₅ : A₄]` cosets /
the five inscribed tetrahedra) are **different fives**. `C₅` is a point-stabiliser
*inside* `A₅`, not the whole group; promoting the manifest `C₅` to `A₅` would
require the order-2 and order-3 generators, which do not preserve `{ζ₅ᵏ, ∞}`.

## Re-scope: the icosahedral bridge is Klein's, not a base action

This is a **scope-limited negative (a)**, not a structural exclusion of the
icosahedral connection: it refutes the *direct* "ED carries `A₅`" route, while
the genuine link between the `ζ₅`-pentagon base and the icosahedral
`A₅`/`S²(2,3,5)`/`S³/2I` arena is **Klein's icosahedral–quintic correspondence**
— the classical theory in which the quintic (whose Bring-radical normal form is
exactly the `Σxⱼ = Σxⱼ² = Σxⱼ³ = 0` Bring curve) is solved via the icosahedral
equation, with `Gal = A₅`. That correspondence relates the pentagon data to the
icosahedral `ℂP¹` *through the quintic's resolvent*, **not** by an `A₅` action on
the branch-marked base. It is real and classical, but a nontrivial bridge to
build — not a one-line geometric forcing.

This is consistent with how the keystone *actually* reaches `S³/2I`: via the
**WRT / `E₈`-residue icosahedral selector** of the modular data (the
`{1,11,19,29}` residues; ledger + Schur–Weyl capstone), i.e. at the level of the
representation/`V_λ` modular data, **not** a base-manifold `A₅` action. The
keystone never claimed the geometric forcing that part (iii) hoped for; this
chase confirms why.

## Net (corrects prior part iii)

| Prior claim (part iii) | This chase |
|---|---|
| ED carries `A₅`, `ED/A₅ ≅ S²(2,3,5)`, arena geometrically *forced* | **does not hold as stated** — ED is `C₅/ζ₅` pentagon (6 branch points); `S₅ ⊄ PSL(2,ℂ)`; 6 ∉ `A₅`-orbit sizes `{12,20,30,60}` |
| "open step: confirm the `A₅` action on the ED" | **settled: there is no such direct action**; re-scoped (a) |
| icosahedral connection | real, but via **Klein's icosahedral–quintic / Bring-radical** correspondence and the WRT `E₈` selector — not a base action |

Falsifiable keystone content is untouched: the defect cubic
`144·C(n) = −n(n−1)(2n−13)` (Lean-proved) and Identity I `M(n) = n(3n−1)/2`
(proved `n ≤ 12`) remain the gates. Parts (i) (ambient volume-S³ = Hopf-over-ED =
gauge `SU(2)`) and (ii) (gauge → `W_λ` excluded, Schur–Weyl dual) of the prior
audit stand; only part (iii) is re-scoped here.

**Productive next step (if pursued):** formalize the Klein icosahedral–quintic /
Bring-radical map as the actual `ζ₅`-pentagon ↔ icosahedral-`ℂP¹` bridge — that
is where any geometric tie between the ED and the `S³/2I` arena must come from,
and it is a classical construction rather than the (refuted) direct base action.
