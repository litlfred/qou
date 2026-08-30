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
updated_at: 2026-08-30T19:30:00Z
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

### Gap 4 follow-through (2026-08-30) — the shrink is done, and it does NOT need steepest descent

Owner: "Shrink the axiom and see if we can prove it." Done, in
`QOU/Archimedean/FiveTwoOhtsukiBridge.lean`. The headline: **the volume half
separates from the analytic half, and only the analytic half needs the missing
Mathlib.**

Ohtsuki's Theorem 1.1 (extracted verbatim from `library/ki52`, §1) is

    ⟨5₂⟩_N = e^{Nζ}·N^{3/2}·ω·(1 + Σᵢ κᵢ(2πi/N)ⁱ + O(N^{-d-1}))

with `y₀` the positive-imaginary root of `(y−1)³ = y`, `x₀ = 1 − 1/y₀`, and

    ζ = (1/2πi)·( Li₂(x₀y₀) + Li₂(1/x₀y₀) + Li₂(y₀) − Li₂(1/y₀) − Li₂(1/x₀) − π²/6 )

Splitting on that gives four parts, of which **one** is the hard analysis:

| part | content | status |
|---|---|---|
| (A) | the asymptotic form above | axiom — the 67-page part, not attempted |
| (B) | `2π·Re ζ = 3·D(y₀)` | **pure dilogarithm identity — provable** |
| (C) | (A) ⟹ growth rate `= 2π·Re ζ` | elementary analysis |
| (D) | `Vol(5₂) = 3·D(y₊)` | **already** axiomatised as `FiveTwoTriangulation` |

**(B) is the finding.** It looks like it needs hyperbolic geometry and does
not: `π²/6` is real, so it drops from the imaginary part, and what remains is
an identity among dilogarithms at the root of a cubic — reachable from the
Bloch–Wigner functional equations already in
`QOU/Archimedean/BlochWignerLobachevsky.lean`. Neither (B) nor (C) touches the
method of steepest descent. That is needed only to prove (A), which we are not
attempting, so **Gap 4 does not block the rigor gain** — it blocks only the
elimination of the last axiom.

### The corpus was already further along than the survey suggested

`BlochWignerLobachevsky.lean` already carries `fiveTwoSaddleCubic`,
`fiveTwoShapeCubic`, a proved `landen_root`, and a `FiveTwoTriangulation`
class with **no instance** stating exactly `Vol(5₂) = 3·D(y₊)`. So part (D) was
done before this session; what was missing was the bridge from the *Kashaev
asymptotic* to that geometry.

**Two cubics, reconciled — not a discrepancy.** Ohtsuki's is `y³−3y²+2y−1`;
the corpus's `fiveTwoSaddleCubic` is `y³−2y²+3y−1`. Measured: the corpus root
`y₊ = conj(1/y₀)` **exactly**, and since `D(1/z) = −D(z)` and `D(z̄) = −D(z)`
the two sign flips cancel, giving `D(y₀) = D(y₊)` to 40 digits. The algebraic
half of that reconciliation is proved in the new file
(`inv_root_of_ohtsuki_cubic`, a `field_simp`/`linear_combination` one-liner).

### Numerically verified before writing anything

* `y₀` and `ζ` reproduce Ohtsuki's printed constants
  (`0.3376410213…+0.5622795120…i`, `0.4501096100…+0.4813049796…i`);
* `2π·Re ζ = Vol(5₂)` to **4.6e-41**;
* `3·D(y₀) = Vol(5₂)` to **5.3e-50**;
* `Im S = 3·D(y₀)` to machine zero;
* `D(x₀) = D(y₀)` and `D(x₀y₀) = D(y₀)/2` exactly — both should fall out of the
  five-term relation rather than be assumed, and step 4 of the proof strategy
  in the file says so.

### Honest state of the new file

Three `sorry`s, each with a written strategy, and **not type-checked** — same
container limitation as `qou-9ilw` (no Mathlib oleans; toolchain ships no
`libLean.a` so `lake exe cache get` cannot be built). The `Li₂` is taken as a
*parameter with hypotheses* rather than constructed, so the statement does not
depend on which polylogarithm the corpus or Mathlib eventually supplies —
Mathlib has none (Gap 1 extension).

- [ ] Prove (B). This is the real target and it is a dilogarithm problem.
- [ ] Prove (C). Elementary; Mathlib has what it needs.
- [ ] Leave (A) cited. Proving it is the steepest-descent programme.

### Gap 4, second follow-through (2026-08-30) — the unblock is SMALLER than the gap

Owner: "add in missing mathlib infra so we can unblock". Investigated what the
`5₂` shrink actually needs, and the answer reverses the earlier framing.

**No polylogarithm is required.** `FiveTwoOhtsukiBridge` originally took `Li₂`
as a parameter with hypotheses, because Mathlib has none (Gap 1 extension). But
`BlochWigner_lob` is *not* defined via `Li₂` — the sibling module defines it as

    D(z) = Λ(arg z) + Λ(arg (1/(1−z))) + Λ(arg (1 − 1/z))

a sum of Lobachevsky values at the three dihedral angles. Verified numerically:
this Lobachevsky form agrees with the `Li₂` form to `0.0` at `y₀` and to
`2.3e-41` at `x₀`. So `D` is already available without any dilogarithm.

Reducing (B) through `Im Li₂(z) = D(z) − arg(1−z)·log|z|` and `D(1/z) = −D(z)`
leaves exactly two obligations:

* **(i) `D(x₀) = D(y₀)` where `x₀ = 1 − 1/y₀`** — measured `1.1e-41`;
* **(ii) the `arg`–`log` corrections cancel** — measured sum `2.9e-42`.

**(i) is now proved**, in `QOU/Archimedean/BlochWignerSymmetry.lean`, and the
proof is combinatorial. `z ↦ 1 − 1/z` is the order-3 Möbius rotation of the
ideal tetrahedron; under it the three angle-arguments are *permuted*, because of
three field identities

    1 − w = 1/z        1/(1 − w) = z        1 − 1/w = 1/(1 − z)

verified exactly, and provable by `field_simp`/`ring`. So `D(1 − 1/z) = D(z)` is
a reordering of a three-term sum. No analysis, no dilogarithm, no steepest
descent — **nothing Mathlib lacks**.

`tetAngle₁ (1 − 1/z) = tetAngle₃ z` is even `rfl`: both sides are literally
`(1 − 1/z).arg`.

### Revised conclusion for this gap

Gap 4 said the steepest-descent absence blocks upgrading the literature-cited
instances. That stands **for proving Ohtsuki's expansion**. It does *not* block
the volume-carrying half, which is what the shrink isolated. The infra actually
needed to unblock was eight elementary lemmas about a Möbius 3-cycle, now
written, not a polylogarithm library and not steepest descent.

What is still open in (B) is obligation (ii), the `arg`–`log` cancellation, plus
`D(x₀y₀) = D(y₀)/2`. Both are elementary in kind; neither needs new Mathlib
theory.

**Still genuinely missing from Mathlib, and still upstreamable** (unchanged):
`Cl₂`, `Λ`, `Li₂`, and steepest descent. The point of this entry is only that
the `5₂` bridge does not depend on them.

**Not type-checked** — same container limitation (no Mathlib oleans; the
toolchain ships no `libLean.a`, so `lake` cannot build `cache:exe`). One bug was
caught by re-reading before commit: the first draft proved a `≠ 0` side
condition with `linarith` on a **ℂ**-valued hypothesis, and `linarith` does not
work over ℂ. Rewritten to rewrite `1 − 1/z` as `(z−1)/z` first so `field_simp`
has both non-vanishing facts in hand.

## Gap 4, third follow-through — the axiom shrank again, and not via Mathlib

Read Ohtsuki's Theorem 1.1 out of `library/ki52` instead of paraphrasing it,
and a second hypothesis turned into a proof. He does not leave the prefactor
as an unknown constant:

```
ω = e^{√−1 π/4}·((y₀−1)/(2y₀+1))^{1/2}      so      ω² = √−1·(y₀−1)/(2y₀+1)
```

A rational function of `y₀` times `i`. So `FiveTwoOhtsukiBridge`'s
`OhtsukiAsymptotic` now states `ω² = ohtsukiOmegaSq y` in place of a bare
`omega_ne_zero` field, and non-vanishing is **derived** — from the cubic, not
from `Im y₀ > 0`: none of `0`, `1`, `−1/2` is a root, so `y ≠ 0`, `y ≠ 1` and
`2y + 1 ≠ 0` are three `norm_num` calls. Also derived, where they were assumed
or `sorry`'d: `two_I_mul_ohtsukiOmegaSq`, and `volume_conjecture_five_two`
itself, which is now a rewrite of (C) rather than an axiom.

**The pattern is the point for this bean.** Gap 4 recorded that upgrading the
literature-cited VC instances needs the method of steepest descent, which
Mathlib lacks entirely. That is true of proving Ohtsuki's *expansion*. It has
now twice been false of the surrounding structure — first `D(x₀) = D(y₀)`,
which is a Möbius reordering (`BlochWignerSymmetry.lean`), and now the whole
prefactor, which is algebra over a cubic. **Both times the Mathlib gap survey
was measuring the wrong thing: what it costs to prove the hard theorem, not
what it costs to state it at the smallest surface and derive the rest.** The
survey stands; its scope was overstated.

Two guards recorded while doing this, both from the ingest agents:

* `library/ki52`'s extracted section text **drops `π`** (it renders as a glyph
  the extractor discards), so the definition of `ζ` reads `1/2√−1` there. With
  the `π` missing every constant is off by a factor of π — I hit exactly this
  and only caught it because `2π·Im ζ` matched Chern–Simons to 26 digits while
  `2π·Re ζ` missed the volume at 1e-16. Read constants from the PDF, or check
  them numerically before trusting a section file.
* Ohtsuki–Takata and Garoufalidis–Yoon prove `1-loop = torsion` for two-bridge
  knots **unconditionally**, which covers `8₁₁ = b(27,10)`. That is a statement
  about `ω`, not `ζ`, and does **not** give the VC. See `qou-b5h9`.

Transcription checked at 120 dps against a root polished to residual 1.9e-121:
`y₀`, `ζ`, `ω` and `κ₁` all reproduce Ohtsuki's printed digits, and three
independent routes to `Vol(5₂)` agree to 121 digits.

## Gap 3 — ✅ **CLOSED 2026-08-30**, end to end, sorry-free

And closed for a triangulation, not just a tetrahedron. Six new declarations,
all `#print axioms`-clean (`propext`, `Classical.choice`, `Quot.sound` only).

**The gap, measured rather than asserted.** This container has a working Lean
setup — 7268 Mathlib oleans plus 1926 QOU oleans restored from the
`lake-cache/qou-v4-24-0` orphan branch, driven by `scripts/lean-direct-cone.sh`
— and a Mathlib source checkout at the pinned rev `f897ebcf`. So the survey
below is grep over the actual pinned source:

| wanted | in Mathlib at `f897ebcf`? |
|---|---|
| `strictConcaveOn_of_deriv2_neg` | **yes**, but 1-D only (interval in ℝ) |
| any multi-dim convexity-from-second-derivative | **no** — `StrictConvexOn.*fderiv`, `ConvexOn_of_hasFDeriv`: zero hits |
| `ConvexOn.comp_affineMap` / `ConcaveOn.comp_affineMap` | **yes** |
| the **strict** `comp_affineMap` | **no** |
| `Finset`-indexed sum of concave functions | **no** — `ConvexOn.sum`, `concaveOn_sum`: zero hits |
| Hall / max-flow–min-cut | **yes**, `Finset.all_card_le_biUnion_card_iff_exists_injective` |

**What was actually missing was one sentence.** `QOU.Knot.RivinConcavity` already
proved concavity along a *line*, and its docstring said "strict concavity on a
convex set is exactly strict concavity along every segment". True, and asserted
in prose. `QOU.MathlibExt.strictConcaveOn_of_segments` is that sentence as a
theorem, and `StrictConcaveOn.restrict_segment` is its converse — the two
together make it an iff.

**Gap 3's framing overstated the cost, exactly as Gap 4's did.** It was recorded
as wanting "negative-definite Hessian on the tangent space of an affine
constraint", which suggests affine subspaces, tangent spaces and restricted
Hessians. None is needed: *every segment between two points of `S` already has
its direction in the directions of `S`*, so quantifying over pairs in `S` **is**
quantifying over tangent directions. For `S ⊆ {Σθ = π}` the direction
automatically satisfies `u+v+w = 0` — precisely the tangency `cot_quadratic_pos`
consumes. The general lemma is nine lines and mentions no geometry.

That is now twice this bean has costed a gap by the price of the hard theorem
rather than the price of stating it minimally and deriving the rest. Worth
treating as the bean's standing bias, not a coincidence.

**Delivered**

* `QOU/MathlibExt/StrictConcaveOnSegments.lean` — `strictConcaveOn_of_segments`,
  `strictConcaveOn_of_deriv2_neg_along_segments`, `StrictConcaveOn.comp_affineMap`
  (strict, injective), `StrictConcaveOn.restrict_segment`.
* `QOU/MathlibExt/ConcaveOnSum.lean` — `ConcaveOn.sum`, `ConvexOn.sum`,
  `StrictConcaveOn.sum_of_mem`. The last takes **one** strict summand and lets
  the rest be concave; that asymmetry is forced, because a per-tetrahedron
  volume read on the whole polytope is constant in the other tetrahedra and so
  never strictly concave there.
* `QOU/Knot/RivinConcavitySimplex.lean` — `strictConcaveOn_tetVol` (one ideal
  tetrahedron, on the simplex in ℝ³) and `strictConcaveOn_totalVol` (a whole
  triangulation, on any convex tetrahedron-wise-admissible set). The gluing
  equations never appear: they are linear, so whatever polytope they cut out is
  convex, and concavity does not care which convex set it is handed.

**Also fixed while here:** `BlochWignerSymmetry.lean` and
`FiveTwoOhtsukiBridge.lean` were landed unverified last session and had two real
errors — `field_simp` matches non-vanishing hypotheses *syntactically*, so
`z − 1 ≠ 0` does not discharge a `(1 − z)⁻¹`; and `Complex.abs` does not exist at
this rev. 11 of their 12 declarations are now confirmed sorry-free, the
exception being `volume_conjecture_five_two`, which routes through the still-open
part (C).

**Not done, and why.** The corpus's `lean-axiom-guard.py` cannot render a verdict
here: ~120 registry modules have missing or stale oleans, all pre-existing
(SchurWeyl, Torsion, Schensted — none touched by this work) because the restored
cache predates HEAD. Rebuilding them is unrelated to this change.

**Ordering update.** ~~Gap 2~~ → ~~Gap 3~~ → Gap 1 (upstream `Cl₂`/`Λ`; the corpus
already has them, so this is a contribution, not a blocker) → Gap 4 → Gap 5.
All five new `MathlibExt` lemmas are written to be upstreamable unchanged.
