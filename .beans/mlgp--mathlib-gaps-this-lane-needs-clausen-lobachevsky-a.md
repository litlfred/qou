---
# mlgp
title: 'Mathlib gaps this lane needs: Clausen/Lobachevsky, Λ″ = −cot, constrained concavity'
status: todo
type: epic
priority: high
tags:
    - lean
    - mathlib-gap
    - hyperbolic-volume
created_at: 2026-08-09T19:45:00Z
updated_at: 2026-08-30T17:30:00Z
---

Inventory of what Mathlib does **not** have that the volume lane needs, with what
QOU already has in its place. Checked against the vendored Mathlib 2026-08-09.

## Gap 1 — Mathlib has no Clausen and no Lobachevsky function at all

`find Mathlib -iname '*Clausen*' -o -iname '*Lobachevsky*'` → **nothing**. QOU
carries its own: `QOU/Knot/Clausen.lean` (`clausen`, `hasDerivAt_clausen`,
duplication, minimum) and `QOU/Archimedean/BlochWignerLobachevsky.lean` (`Cl_2`,
`Lob`, `tetAngle₁/₂/₃`, `tetAngles_sum_eq_pi`, `BlochWigner_lob`, and
`Vol(S(z)) = Λ(α)+Λ(β)+Λ(γ) = D(z)` as a theorem).

⚠ Correct the stale note while here: `QOU/Knot/M004AngleStructure.lean` says
"Mathlib has no ideal-tetrahedron volume theory". True of **Mathlib**, false of
**QOU** — the corpus has one. The genuinely missing piece is narrower (Gap 2).

**This is upstreamable.** `Cl₂` with its FTC derivative, duplication formula and
`Λ` normalisation is a clean, self-contained Mathlib contribution.

## Gap 2 — `Λ″ = −cot` — ✅ **CLOSED 2026-08-09**

`hasDerivAt_clausen : Cl₂′(θ) = −log(2 sin(θ/2))` on `(0, 2π)` exists, sorry-free,
by `integral_hasDerivAt_right`. Since `Λ(t) = Cl₂(2t)/2`, that gives
`Λ′(t) = −log(2 sin t)` by the chain rule, and then
`Λ″(t) = −cos t / sin t = −cot t` by one more differentiation — Mathlib has
`Real.hasDerivAt_log` and `Real.hasDerivAt_sin`, so this is short.

Why it matters: bean `rvnc` proved the *algebraic* half of Rivin concavity
(`cot_quadratic_pos`, sorry-free — the Hessian quadratic form is positive on the
tangent space). Without `Λ″ = −cot` that is a fact about a quadratic form
*asserted* to be the Hessian rather than *proved* to be. This closes it.

Delivered in `QOU/Knot/RivinConcavity.lean`: `hasDerivAt_Lob`
(`Λ′ = −log(2 sin)`), `hasDerivAt_deriv_Lob` (`Λ″ = −cot`), `deriv_deriv_Lob`.
All on `(0, π)`, sorry-free, standard axioms, build exit 0 / 3157 jobs with the
`.olean` deleted first. It was short, as predicted. **Next: Gap 3.**

## Gap 3 — strict concavity on an affine subspace

Mathlib has `StrictConcaveOn` and second-derivative tests on intervals, but the
statement needed is concavity of `Σ Λ(θᵢ)` **restricted to the affine slice** cut
out by the gluing equations. Check what `Mathlib.Analysis.Convex.*` offers for
"negative-definite Hessian on the tangent space of an affine constraint ⟹ strictly
concave on that slice" before writing anything; this may be assemblable rather
than new.

Note the boundary behaviour found in `rvnc`: strict positivity of the Hessian form
is **pointwise on the open simplex and not uniform** — the normalised minimum over
300k samples degenerates as `α → π`. Any Mathlib-shaped lemma wanting a uniform
modulus will not apply.

## Gap 4 — `SurrealField ℝ*` / nonstandard transfer (see bean `hypr`)

Not missing from Mathlib so much as un-wired: `Hyperreal` exists with `IsSt`, `st`,
`Infinitesimal`, and `ℝ*` already instances `Field`/`LinearOrder`/
`IsStrictOrderedRing`. What Mathlib lacks is the *working* NSA toolkit — there is
no "for all infinite hypernaturals" transfer, and `IsSt (ofSeq f) r` only gives
convergence along `hyperfilter ℕ ≤ atTop`, strictly weaker than `atTop`, converse
false. So this cannot replace an ε–δ whose goal is `Tendsto … atTop`. Scope
accordingly; see `hypr`.

## Gap 5 — oscillatory asymptotics (only if bean `thmb` route C is taken)

Formalising Ohtsuki §3–§5 needs saddle-point/stationary-phase with error control
and Poisson summation. Mathlib has neither in usable form. This is the expensive
one and should not be started before Gaps 1–3.

## Ordering

~~Gap 2~~ (done) → **Gap 3** (now the critical path) → Gap 1 (upstream) → Gap 4 →
Gap 5.

---
**2026-08-09 — new Gap 6, and it is PARTLY CLOSED: no volume functor.**

Working `Vol(5₂)` surfaced something sharper than "unproved":
**`Vol(5₂) = 3·D(y₁)` was not a statable Lean proposition at all.** The only
objects named "volume" in Lean were decimal literals
(`MassDerivation.vol_figure_eight := 2.029883212819307250042408`) and the
placeholder `HyperbolicVolume : Knot → ℝ := fun k => 0 * (k : ℝ)`
(`AppendixSurreals/Conjectures.lean`) — which **returns zero**. You cannot prove
an equation against those, only write a false or vacuous one. That is a
*definitional* gap, not a proof gap, and it is a different kind of work.

Precedent confirming this is the real trap: `FigureEightVolumeLiterature.lean`
records that the 4₁ volume conjecture was unstateable while `VOL_4_1` was "a
truncated rational decimal ≈ 1e-30 away from `2·Cl₂(π/3)`, **making the statement
literally false**" (`qou-yf47`).

**Partly closed 2026-08-09**: `QOU/MathlibExt/IdealTriangulation.lean`,
sorry-free, standard axioms, build exit 0 / 3252 jobs:

* `IdealTetrahedron` — a shape with `0 < Im z` (degenerate/flat shapes excluded);
  `angle₁/₂/₃`, `angle_sum` (`= π`), the three angle ranges, `law_of_sines`;
* `IdealTetrahedron.volume := BlochWigner_lob shape`, with **both** forms proved
  equal — `volume_eq_lob_sum` (angles) and `volume_eq_dilog` (Neumann–Zagier
  eq. (38)/(39)), the latter being a direct consequence of `KummerRadial.kummer`
  and *unwritable before it*;
* `IdealTriangulation n`, `volume := ∑ volumes`, `volume_eq_dilog`, `const`.

Consequence: `fiveTwoTriangulation_volume : fiveTwoTriangulation.volume = VOL_5_2`
is now a **theorem about a defined object**, where before it was a sentence with
no subject.

**⚠ STILL OPEN, and this is the honest residue.** The step from an
`IdealTriangulation` to a **topological 3-manifold** — Thurston hyperbolisation
plus Mostow rigidity (volume is a topological invariant, independent of the
triangulation). That needs hyperbolic 3-manifolds; neither Mathlib nor QOU has
them, and this file deliberately does not pretend otherwise. `Vol(S³ ∖ 5₂) = …`
remains a sentence with no subject.

Note also what is **not** modelled: the combinatorial data (face pairings, edge
classes) and the gluing equations they impose. `IdealTriangulation` carries only
the shapes, so it cannot currently express "this triangulation is *of* that
manifold". Adding the gluing equations is the natural next increment, and is
where `qou-m015` (the 5₂ angle-structure polytope) would attach.

**Gap 6, second increment — the GLUING EQUATIONS (2026-08-09).**

`IdealTriangulation.lean` now also carries the combinatorial layer, sorry-free,
build exit 0 / 3252 jobs:

* `IdealTetrahedron.param : Fin 3 → ℂ` — the three edge parameters
  `z`, `z′ = 1/(1−z)`, `z″ = 1 − 1/z`;
* `param_prod` — **`z·z′·z″ = −1`**, "pure algebra, and the source of the `π`"
  (reusing the corpus's `tet_shape_prod`);
* `param_im_pos` — all three lie in the upper half plane, so the two Möbius maps
  preserve it; `arg_param` — their arguments *are* the three dihedral angles;
* `GluingData n e` — exponent data `exp k i j`: how many times edge-pair `j` of
  tetrahedron `i` meets edge class `k`;
* `SatisfiesEdgeEquations` — `∏ param^exp = 1`, the full gluing equation;
* `SatisfiesAngleEquations` — the dihedral angles around each edge sum to `2π`.

**The two conditions are deliberately kept apart, because they are NOT
equivalent.** The product form constrains modulus *and* argument; the angle form
is the argument half only — and the angle form is exactly the *angle-structure*
condition of Casson–Rivin, i.e. what the corpus's m004/L6a4 polytopes encode.
That is the seam where `qou-m015` and `qou-rvnc` attach to this layer.

**⚠ What is STILL not modelled, unchanged:** neither condition, alone or
together, certifies that a triangulation **is** a triangulation of a given
manifold. That is topology — Thurston hyperbolisation, Mostow rigidity — and
needs hyperbolic 3-manifolds, which neither Mathlib nor QOU has. No claim here
is about `S³ ∖ 5₂`, and the 5₂ triangulation defined in
`FiveTwoVolumeConstant.lean` is **not** asserted to satisfy any gluing data —
that would need the actual SnapPy combinatorics (`qou-m015`).

---

## Gap 4 (added 2026-08-30) — Mathlib has NO method of steepest descent, and that is what blocks upgrading the literature-cited VC instances

Owner asked: upgrade the literature-cited volume-conjecture instances (5₂, 6₁,
6₂, 6₃ — see bean `qou-ckbv`) from *asserted* to *Lean-derived*. Surveyed
against the vendored Mathlib on this date, that is blocked on a missing
**analysis** theory, not on knot theory and not on effort.

### Why the corpus's own proof route cannot reach them

The in-repo discharges (4₁, Borromean, 2-belt Whitehead chain) all use the
positive-sum squeeze: Riemann sums of `log(2 sin)` against the Clausen
primitive, saddle, two envelopes. Its precondition is a **single positive sum**
at the Kashaev point. The corpus's own transfer scan
(`2026-07-27-squeeze-architecture-transfer-scan.md`) tabulates:

    | 5₂, 8₁₁, generic knots | no | oscillatory sums (structural) | — |

No positivity ⇒ no squeeze. That is precisely why Ohtsuki needed the saddle
point method for 5₂ and the 6-crossing family.

### The gap

Ohtsuki's route is: integral presentation of `(q)_n` → Poisson summation →
**saddle point method** → and the load-bearing part, an explicit homotopy of the
real-3-dimensional integration domain in ℂ³ keeping its boundary inside the
region controlled by the potential.

Measured against Mathlib (`grep -rli` over `Mathlib/`, this date):

| ingredient | Mathlib files |
|---|---|
| Poisson summation | **2** — `Analysis/Fourier/PoissonSummation.lean` ✅ |
| stationary phase | **0** |
| steepest descent | **0** |
| Laplace method | **0** |
| saddle-point analysis | **0** — the 18 `saddle` hits are Haar-measure and `ToAdditive` word-list files, none complex-analytic |
| Lobachevsky | **0** (Gap 1) |
| polylogarithm | **0** |
| quantum dilogarithm / q-Pochhammer | **0** |

Correction to a plausible reading of Gap 1: Mathlib's three `Clausen` hits are
`Probability/Distributions/Exponential.lean` and two `Condensed/` files — that is
**Dustin Clausen**, the mathematician, not the Clausen function. Mathlib has
none, exactly as Gap 1 says.

So the first milestone of "formalize Ohtsuki" is *build the method of steepest
descent in Mathlib* — in several variables, with hypothesis verification — a
major library contribution with no knot theory in it. This is not a session or
a sprint; it is a programme whose payoff is years out, and it should not be
scoped as a QOU task.

### What IS reachable — shrink the axiom instead of eliminating it

The §3b-cond pattern the corpus already uses for `VolumeBridge` applies exactly
here: axiomatise **only the open analytic input** and *derive* the conclusion.
Rather than assuming "VC holds for 5₂" (a conjecture), assume Ohtsuki's
**specific quantitative asymptotic estimate** (a named, cited, published lemma)
and derive VC-for-5₂ from it in Lean. That is formalizable with what exists,
and it moves the assumed surface from a conjecture to a theorem-someone-proved.

It does not make 5₂ tier-1. It makes the tier-2 assumption *minimal and
precise* instead of blanket — which is the same improvement `VolumeBridge` was
built to make, applied one level down.

Sources for extracting that estimate are already in `library/`: `ki52`,
`104171-qt-83` (Ohtsuki, 5₂) and `ki6c` (Ohtsuki–Yokota, 6-crossing).

### Upstreamable, and worth flagging as such

Gap 1 already notes `Cl₂` is a clean Mathlib contribution. Add: **`Li₂` /
polylogarithm and the Lobachevsky function are equally self-contained**, and
QOU has working versions of both. Steepest descent is a much larger piece and a
different kind of contribution.
