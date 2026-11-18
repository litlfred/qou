---
# qou-8mtd
title: Define the volume of a topological 3-manifold and connect it to the triangulation volume
status: in-progress
type: task
priority: high
tags:
    - hyperbolic-volume
    - mathlib-gap
    - open-problem
    - reorg-2026-10-04
created_at: 2026-08-10T18:00:39Z
updated_at: 2026-10-04T15:14:49Z
parent: b9cj
---

**The gap the exposition arc made visible but did not narrow.**

`QOU/MathlibExt/IdealTriangulation.lean` now defines the volume **of a triangulation** —
`IdealTetrahedron.volume = D(z)`, `IdealTriangulation.volume = Σᵢ D(zᵢ)` — with
`volume_rotate` proving it independent of the edge labelling, so it is a property of the
tetrahedron rather than of the bookkeeping. All sorry-free and pinned in the axiom guard.

**What is still undefined: the volume of a topological 3-manifold.** Nothing connects an
`IdealTriangulation` to a knot complement. So the corpus can say "the volume of *this
triangulation* is `3·D(y₁)`" and cannot say "`Vol(5₂) = 3·D(y₁)`", because the left-hand
side has no referent. `VOL_5_2` is *defined* as `3·D(y₁)` (`FiveTwoVolumeConstant.lean`)
— a definition, not a computation of an invariant.

## What closing this requires

1. **A notion of hyperbolic 3-manifold** — Mathlib has none. Minimally a complete
   finite-volume hyperbolic structure, enough to state that a volume exists and is a
   number.
2. **Volume as a topological invariant** — Mostow rigidity. This is what makes "the
   volume of the complement" well-posed independently of any triangulation.
3. **The bridge: a triangulation *of* a manifold.** That an ideal triangulation whose
   shapes satisfy the gluing equations, all positively oriented, realises the complete
   structure — Thurston hyperbolisation. Only then does `Σᵢ D(zᵢ) = Vol(M)` become a
   theorem rather than a definition.

## Discipline (do not shortcut)

- **Do not axiomatise the bridge and call it discharged.** A `class` carrying
  `triangulationVolumeEqManifoldVolume` as a field, consumed downstream, is
  §"Axiomatization is NOT a Proof". The honest intermediate is a *conditional* result in
  the §3b-cond shape, with the hypothesis named and visible in the type.
- **Do not restate `VOL_5_2 := 3·D(y₁)` as evidence.** It is a definition; the numerical
  agreement with the literature (2.828122088330783) is evidence the definition was chosen
  well, not proof that it is the invariant.
- Numerical agreement at more knots is **not** progress on this bean. The gap is
  definitional, not quantitative.

## Realistic scoping

Step 1 alone is a Mathlib-scale project. A defensible smaller win: state the bridge as a
named conditional hypothesis (content-bearing class, no instance — the honest "open"
state per §3b-tax) so downstream statements can be *explicitly* conditional rather than
silently ambiguous about which volume they mean.

Surfaced by PR #4925 (`thm:ideal-tetrahedron-volume-well-defined`); the same caveat is
stated in every block of the gluing/volume arc.

### Status 2026-08-29 — this is now the arc's SOLE open item

The gluing/volume arc has landed on main: the exposition blocks, the strategy-matrix
probe and witness, the reach correction, and the axiom-guard pins (verified 27/27 clean
by proof term under `qou-0r4e`, which also found and fixed a guard bug that made a primed
declaration silently unverifiable).

Everything measurable in the arc is therefore done, and what remains is exactly the
definitional gap recorded above: **the volume of a topological 3-manifold is undefined,
so nothing connects an `IdealTriangulation` to a knot complement.** No amount of further
measurement moves it — the constraint is that Mathlib has no hyperbolic 3-manifolds.

Unchanged and worth re-reading before anyone starts: numerical agreement at more knots is
**not** progress here, and axiomatising the bridge as a class field is the
§"Axiomatization is NOT a Proof" failure. The honest smaller win remains a content-bearing
conditional class with no instance.

### DONE 2026-08-29 — the bridge is now stated as a conditional, with no instance

`QOU/MathlibExt/ManifoldVolumeBridge.lean`. The smaller win this bean scoped is
implemented, and the gap is unchanged: **the volume of a topological 3-manifold is still
undefined.** What changed is that downstream statements can now carry the dependence in
their type instead of being silently ambiguous.

**§1 is unconditional and real.** `volume_rotateAt` — relabelling any single tetrahedron
of a triangulation leaves the total volume unchanged. This lifts the arc's proved
one-tetrahedron `volume_rotate` to triangulations; no class involved.

**§2 is the hypothesis.** `class HyperbolicVolumeBridge M` carries `vol`, a `Realises`
relation, the transport `Realises T m → vol m = T.volume` (this is Thurston's theorem,
an INPUT), and non-triviality. **No instance is provided, and providing one would be a
defect** absent a real theory of hyperbolic 3-manifolds.

**§3 derives rather than projects** — the §3b-cond item 5 trap. `vol_eq_of_two_realisations`
applies transport twice and cancels; `vol_eq_rotateAt` composes it with §1's proved
invariance. Neither is `fun h => h.field`.

#### Two traps hit while writing it, both recorded in the module header

1. **A vacuous corollary, caught by the structure's own field.** "A triangulation of flat
   tetrahedra has volume zero" is *unstatable*: `IdealTetrahedron` carries
   `im_pos : 0 < shape.im`, so no such triangulation exists. The theorem would have been
   vacuously true over an empty hypothesis.
2. **The class was DEGENERATE on its first draft.** With three fields it admitted
   `Realises := fun _ _ => False` on `Unit`, under which transport holds vacuously and
   the class asserts nothing. That instance was written out and **typechecked** — which
   is why this is stated as fact, not suspicion. It is the same defect the corpus records
   for the birthday axioms. The `realisable` field closes it; the degenerate instance now
   fails with `Fields missing: realisable`.

Verified: `lean` exit 0; `#print axioms` on all six = `[propext, Classical.choice,
Quot.sound]`, zero `sorryAx`; pinned in the axiom guard; registered in `QOU.lean` so it
is not orphaned (this arc had 11 orphaned modules once).

**Still open, and unchanged:** steps 1–3 above — hyperbolic 3-manifolds in Mathlib,
Mostow rigidity, Thurston hyperbolisation. This bean stays open for those.

### 2026-08-29 (later) — the reuse pass found the corpus already had a SECOND volume

Running the prepare-merge reuse pass against 114 new commits on main turned up
something the first pass of this bean missed entirely, and it changes what the
bean's second clause ("connect it to the triangulation volume") means.

**`QOU.Encounter.MostowRigidity` already carries a manifold-side volume**, and it
has *instances*: `figureEight` sets `volume := 2.02988321281930`, a decimal
literal kept in sync with `hyperbolic-volumes.witness.json` by
`codemod-leanval.ts`. So `volumeInvariant FigureEight = 2.0298…` holds by `rfl`.

That is the SAME disease this bean is about, one file over: the number is
**entered**, not computed, and nothing in that module mentions a triangulation.
So the corpus had two carriers for one quantity, in different namespaces, with no
theorem relating them — and this arc was about to add the second without noticing
the first. Whichever a reader picks, nothing tells them the other exists.

**Not a duplicate, but it needed connecting.** New
`QOU/Encounter/MostowTriangulationBridge.lean` (layering: Encounter imports
MathlibExt, never the reverse) spends the bridge's transport on the Mostow
invariant:

- `mostow_volume_eq_triangulation_volume` — the invariant equals the
  Bloch–Wigner sum, composed from three inputs, projecting none.
- `figureEight_literal_eq_triangulation_volume` — what the bridge buys: under it
  the entered literal *is* the sum of a realising triangulation. It does **not**
  verify the literal; `compat` remains assumed.
- `volumeInvariant_eq_of_two_realisations` — well-definedness in the form the
  Mostow module can consume.

`compat` (that the two notions agree) is an **explicit hypothesis argument, not a
class field**, deliberately: a field would be inferred silently at every use site
and would read as established.

**A distinction worth keeping straight, since this arc recorded its sibling.**
The corollary `ManifoldVolumeBridge` could not state was over a hypothesis
**provably uninhabited** (`IdealTetrahedron.im_pos`) — vacuous. The hypotheses
here are **open**: no instance exists, but nothing proves none can. Same shape on
the page, opposite epistemic status.

Verified: `lean`-direct exit 0 on both modules; `#print axioms` on all 10
declarations = `[propext, Classical.choice, Quot.sound]`, zero `sorryAx`; all 9
registry entries confirmed by `lean-axiom-guard.py` against freshly-rebuilt
oleans (the guard refuses to report on a stale olean set, which is why the
rebuild came first).

**Still open, unchanged:** hyperbolic 3-manifolds in Mathlib, Mostow
hyperbolisation, Thurston. The bean stays open.


---

## 2026-08-29 (later still) — CORRECTION to this bean's own framing

This bean says the volume of a 3-manifold is undefined and adds that Mathlib has no
hyperbolic 3-manifolds. The second half is true of Mathlib and **misleading about this
corpus**, and I wrote it. Measured on main, `QOU/Archimedean/` already carries:

| module | state |
|---|---|
| `HyperbolicVolumeMeasure` | `upperHalfSpace`, `hypDensity = 1/z³`, `hypVolume` — **0 sorries** |
| `IdealTetrahedronRegion` | chimney regions — **0 sorries** |
| `TotallyGeodesicFaces` | vertical planes + hemispheres totally geodesic — **0 sorries** |
| `HyperbolicMetric` | `dH` path metric, `IsDHIsometry` — 3 sorries |
| `IdealTriangulation` | shape triple `param_prod = -1`, `param_im_pos`, `volume_rotate` — proved |

Anyone reading this bean's wording would conclude the hyperbolic layer is absent and
rebuild a good deal of it. **The gap was never "H³ is missing" — it was "no group is
acting."** No discrete subgroup, no quotient, which is the whole distance between
having H³ and having a hyperbolic 3-manifold. That is why `MostowRigidity.volume` is an
entered literal and `HyperbolicVolumeBridge.vol` an assumed field: neither had anything
to attach to.

Addressed in child bean `qou-hq3m` (`QOU/Archimedean/HyperbolicQuotient.lean`), which
supplies the acting group and derives a quotient volume instead of positing one.

**This bean stays open**, and its genuinely open parts are unchanged and untouched:
Mostow rigidity, Thurston hyperbolisation, and a route from a knot complement to a
triangulation. `Vol(4₁)` is still not computable and the `figureEight` literal is still
unverified.

## Round 71 Update (PR #8483)
- De-vacuified and extended in PR `litlfred/qou#8483` (`claude/round71-devacuify-6qbv-b9cj`, HEAD `ccf4b5dbe70005deb5de8ba21a4dcf809c5178db`, C1 `7580772c921dba1792c7df67cfdeb7db65a5b8f8`), compiled with Lean 4.24.0 (`0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 major, 0 advisory` across all 6 directory-mode static audit scripts) and verified with 80-dps `mpmath` witness `computations/probes/round71-devacuify-6qbv-b9cj.witness.json`.
