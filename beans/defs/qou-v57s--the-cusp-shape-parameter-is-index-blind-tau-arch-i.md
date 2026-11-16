---
# qou-v57s
title: 'The cusp shape parameter is INDEX-BLIND: tau_arch is not a function of the algebraic seed (scope-(b), pigeonhole)'
status: in-progress
pr: 8187
type: task
created_at: 2026-10-10T12:34:17Z
updated_at: 2026-11-16T20:22:00Z
parent: qou-n4nr
---

Measured 2026-10-10 (PR #7586, issue #7585) while working `qou-3kni`'s cusp
leg. Parent subject: `conj:shared-denominator-cusp-holonomy`, carrier
`folio/quantum-observable-universe/mass-theory/shared-denominator-cusp-holonomy.md`.

## The finding

The conjecture says the `n` roots `q_0^{-k}` of `(x; q_0)_n` "address" the
cusps. `snappy_cusp_seeding.py` measured `|q_0^{-k} - z_k| ~ 0.4-0.9` against
SnapPy's shapes and concluded the bijection must be of **labels**, *"with the
actual shape parameter being a non-trivial function `tau_arch(q_0^{-k})` of the
algebraic seed; the shape of that function is the subject of further work."*

**There is no such function, and showing it needs no distance -- only
counting.** From the COMMITTED witness (SnapPy not re-run):

| manifold | `n` roots, pairwise distinct | distinct shape VALUES | tetrahedra up to ISOMETRY | cusps |
|---|---|---|---|---|
| m004 | 2 | 1 | **1** | 1 |
| m003 | 2 | 1 | **1** | 1 |
| L6a4 | 8 | 2 | **1** | 3 |

The isometry column is not what the witness records. An ideal tetrahedron has
THREE shape parameters -- the edge-relabelling orbit -- so two recorded values
can be one tetrahedron, and L6a4's are: `(1+i)/2` is `rotate` twice from `1+i`
(`rotate(1+i) = i`, `rotate(i) = (1+i)/2`), both with angles
`{pi/4, pi/4, pi/2}`. m004/m003 are two copies of the REGULAR tetrahedron,
whose orbit is a FIXED POINT -- and that fixed-point property IS regularity.

So `tau_arch` (seed -> shape) is **CONSTANT** on all three: `n` distinct inputs,
one isometry class out.

**Scope: (b) structural exclusion. Invariant: pigeonhole on a finite set.** A
map from an `n`-set onto a 1-set is not injective and carries no information
about its argument. This excludes `tau_arch` AS A FUNCTION OF THE SEED VALUE,
on the three triangulations the corpus probes -- every injective candidate
(Moebius, exponential, any reparametrisation) AND every non-constant one. It
does NOT exclude the conjecture.

## 🛑 The orbit identity was ALREADY PROVED, sorry-free -- cite the Lean

`QOU/MathlibExt/IdealTriangulation.lean` (0 sorries) carries `param`,
`rotate` (docstring: *"The same tetrahedron, relabelled"*), `shape_cycle2`,
`shape_cycle3`, `rotate_angles`, `param_prod`. Its section header states the
very thing the probe re-measured: *"`z -> 1/(1-z)` does not change the
tetrahedron ... **This is not a coincidence to be checked numerically.**"*

The probe's identity section is downgraded in its own docstring to a
consistency check of its arithmetic against that proof, directing a citer to
`shape_cycle2` / `rotate_angles`. **What is genuinely new here is only the DATA
step** -- that the committed values lie in one orbit -- plus the counting
consequence. Recorded this way because the probe nearly published proved Lean
as a numerical finding.

## Why the conjecture SURVIVES, and what to measure instead

Its displayed RHS is **holonomy**: `Hol_{mu_k}(z_k) = Hol_{lambda_k}(z_k) = 1`.
A holonomy is a product of shape parameters along a meridian/longitude PATH, so
it is path-dependent and therefore index-dependent **even when every shape is
equal** -- exactly the property shapes lack. So the conjecture's EQUATION is
better than its own table row (*"pole of Phi_n <-> complete cusp"*) and better
than the witness's reading: the existing probe measured the one object in the
statement that cannot carry the index.

**The object to measure is the residual `|Hol_{mu_k} - 1|` at the algebraic
seeds, not `|q_0^{-k} - z_k|`.** `snappy_cusp_seeding.py`'s SECOND caveat
already says a genuine test needs the gluing system.

## Two smaller corrections to the recorded negative

1. **ARITY.** The equivalence ranges `k` over `n` roots on the left and over
   CUSPS on the right, and `n != c` in all three cases (2v1, 2v1, 8v3). The
   carrier's own table row already says *"n ideal tetrahedra in JSJ piece"*, so
   **the carrier is internally inconsistent**: table tetrahedron-indexed,
   equation cusp-indexed. Tetrahedron-indexing is the consistent reading and is
   what the producer pairs against (`M.tetrahedra_shapes`).
2. **The 0.4-0.9 is mostly the probe's own knob.** Seeds are lifted by a fixed
   `IM_PERTURBATION = 0.1` while the true `Im` is `sqrt(3)/2 = 0.866`. Matching
   the lift collapses m004 from `0.8646/0.9148` to `0.4009/0.5`. The knob-free
   part is the REAL part, floor **0.400918284** on m004, which no lift can
   move -- a STRONGER negative than the recorded one, since it holds for every
   lift.

## What is NOT established here

- **Whether anything in the corpus already computes the holonomy residual.**
  `IdealTriangulation.lean` has `SatisfiesEdgeEquations` /
  `SatisfiesAngleEquations` and ZERO cusp/meridian/longitude hits, but per-knot
  meridian work exists elsewhere -- `QOU/Knot/FigureEightDeformedMeridianWinding.lean`,
  `QOU/Mass/FiveTwoGluingFromFareyWord.lean`,
  `QOU/Mass/FiveTwoAPolynomialFromFareyWord.lean` -- and none was read closely.
  The six-path corpus-grep gates the claim and was NOT run to completion. A
  `corpus-grepper` pass was in flight when this was written; **read its result
  before citing any novelty here.**
- **Generality beyond these three triangulations.** SnapPy's triangulation is
  not canonical; a different one changes `n`. The conjecture ties `n` to
  GB-depth `k_star(T_w) = n`, an ALGEBRAIC quantity, so whether `n = c` is
  achievable at all is a separate question not settled here. Do not read the
  arity row as a general theorem.

## The decision this leaves with the owner

**Default if nothing is done:** nothing changes. The probe is additive, the
carrier keeps its cusp-indexed equation beside its tetrahedron-indexed table,
and the witness keeps its lift-dependent distance as the published negative.
Under AGENTS.md's ASK-THE-OWNER rule a content edit to a conjecture statement
is not an agent's call, so it has not been made.

- **Re-index the carrier** from cusps to tetrahedra in the displayed
  equivalence, matching its own table row. Costs one `.md` + `.ts` + `.lean`
  sibling edit on `shared-denominator-cusp-holonomy`; risks that the
  cusp-indexed form is the INTENDED one and the table row is the error --
  which only the author knows. Commits the conjecture to the tetrahedron
  reading.
- **Record the prune in the carrier's own §"Empirical scope"** without
  touching the equivalence: replace *"the shape of that function is the subject
  of further work"* with the counting argument. Costs one paragraph; risks
  nothing; commits to nothing, and stops the next agent spending a session
  searching for `tau_arch`.
- **Build the holonomy residual** -- the positive route. Costs a real compute
  leg (Thurston gluing system per manifold, meridian/longitude paths, mpmath);
  risks being duplicated if the corpus-grep finds it exists; commits to the
  tetrahedron/holonomy reading. This is the only option that could CLOSE
  anything.

**My recommendation, as judgement not finding:** take option 2 now (one
paragraph, no risk, and it is the thing that stops wasted search), hold option
1 until you say which indexing you meant, and schedule option 3 only after the
corpus-grep result lands -- because if `FiveTwoGluingFromFareyWord` already
carries the residual machinery, option 3 is a wiring job rather than a compute
leg.

## Status

`in-progress`, not completed. **The conjecture is open** and this bean's
subject is a constraint on it, so per AGENTS.md it does not close on the
recording being done.

---

## 🛑 CORRECTION, same day — the six-path corpus-grep landed and cut this bean down three ways

The measurement stands. The write-up over-claimed, and two of the three
corrections are the checklist catching this bean. Verified at the source, not
taken from the grep agent's report.

### 1. `τ_arch` is a GLYPH COLLISION and this bean walked into it

`τ_arch` is an **established** corpus object and it is **not** a seed→shape
map. It is the archimedean evaluation of the fibre functor, typed
`τ_arch = π_∞ ∘ τ : C → ℝ` — read directly at
`QOU/MotivesArchimedean.lean:98` and `mass-theory/vol-through-tau.lean:49`,
catalogued in `docs/audits/2026-07-11-archimedean-functor-taxonomy.md` (whose
TL;DR is that these objects are not functors at all). It is **real-valued**,
so it cannot produce a shape with `Im z > 0`. The `τ_arch(q₀^{-k})` of the
carrier's caveat is a **different, wished-for object with an incompatible
codomain**, sharing a glyph across 16 files. **The discriminator is the
codomain.**

This bean's title and body use the glyph for the hypothetical map. Read them
that way; nothing here is about the real `τ_arch`. The title is left as
published rather than rewritten, since the bean ID is already cited in a PR
and a probe — but it is **wrong as a name**, and that is the point of this
entry. AGENTS.md registry §2: attributes do not transfer across overloaded
symbols. Same defect class as the `BlochWignerD : ℝ → ℝ` typing one file over.

### 2. "The seed is not the shape" is ALREADY a sorry-free theorem — naming these same three manifolds

`mass-theory/shared-denominator-cusp-holonomy.lean:178`,
`seed_is_not_the_cusp_shape`, proves `shape k ≠ (r : ℂ)` for every real `r`.
Its docstring, verbatim: *"`m004`, `m003` and `L6a4`, and concludes the
identity `q₀^{-k} = z_k` cannot hold. Here it follows from the conjecture
itself, since `im_pos` excludes every real shape."*

So the headline is **not this bean's**. What is this bean's is stronger and
different in kind: that theorem says the shape is not **real**, which leaves
open that the shapes distinguish the indices. The isometry collapse says
**the shapes do not distinguish the indices at all.**

### 3. The composition was removed on purpose, and a cardinality refutation is already committed

- **Bean `qou-rj44` (`completed`)**: the class field `shape` is typed
  `UpperHalfPlane` and **supplied by the instance**, precisely because
  composing seed→shape *was* the defect. The dilog carrier's docstring: *"The
  repair is to **un-compose** the map … it is not the shape."* And
  `shape : Fin n → ℂ` is **label**-indexed — an assignment the caller
  supplies. There is no function of the seed in either Lean file to refute.
- **Bean `qou-mfdq` Finding 1** (`todo`, priority **high**, on `origin/main`,
  380 lines) already refutes the pole-to-cusp bijection **scope-(b), invariant
  = cardinality**, by a *different* count: the `n` roots against the **four**
  ideal vertices of one tetrahedron, forcing `n = 4` while clause (2) sends
  `n → ∞`. Its own scoping — *"excludes the claim as literally written; does
  not exclude the intent"* — is the same shape as this bean's.

**The arity row in this bean is a THIRD count** — `n` roots against `c`
**cusps** (2v1, 2v1, 8v3) — independent of and consistent with `qou-mfdq`.
Cite `qou-mfdq` for the bijection refutation. Cite this bean only for the two
things below.

### What survives as this bean's own

1. **The isometry collapse of the committed data.** L6a4's two recorded shape
   values are ONE tetrahedron (`rotate` twice), so all three manifolds have
   exactly **one** isometry class. Searched on `origin/main` by content for
   `index-blind`, `up to isometry`, `regular ideal tetrahedron`,
   `IM_PERTURBATION`, `isometry class` — **in no committed artifact**, and
   neither `qou-3kni` nor `qou-mfdq` contains `isometry`, `pigeonhole` or
   `index-blind`.
2. **The lift knob.** ~half the published 0.4–0.9 is `IM_PERTURBATION = 0.1`;
   lift-free real-part floor **0.400918284** on m004. Also in no committed
   artifact.

### Three further findings from the grep, NOT acted on here

- **A live type defect, unbeaned.** `mass-theory/archimedean-functor-uniqueness.lean:113`
  `archimedean_functor_uniqueness` takes `(D τ_arch : ℝ → ℝ)`. The corpus
  *proves* Bloch–Wigner vanishes on the reals — `eq_zero_of_conjAntisymm_ofReal`,
  sorry-free, in **two** files — so instantiating `D : ℝ → ℝ` as the real
  restriction of genuine Bloch–Wigner forces `D ≡ 0`, hence `τ_arch ≡ 0`. Its
  `figure8_calibration` docstring writes `Vol(4₁) = c · 2 · D(e^{iπ/3})` while
  the theorem is over `z₀ : ℝ`, and `e^{iπ/3}` is not real. **This is the
  defect `qou-rj44` fixed one file over, not propagated here.** Nearest bean
  `qou-n226` (`todo`) does not cover it. Owner call; not beaned by me yet.
- **Citation holes on a 63-citer arc.** Murakami–Murakami 2001 is
  **registered but not held** (`references.ts:5934`, zero `library:` lines),
  cited from `archimedean-functor-uniqueness.lean:139`. `library/0803219`
  (Murakami's volume-conjecture survey) is **held but unregistered**
  (`grep -c 0803219 references.ts` = 0), so no block can cite it.
  `thurston1978` is held **Ch. 1–2 only** — §4.5, the gluing equations, is
  **not held**, and is cited by locator at
  `shared-denominator-cusp-holonomy.lean:91`.
- **A stale figure inside the constraint probes.** `qbeta_c3_barodd_*` rest
  their "a smooth `m(q₀)` is excluded" on `dc₃/dq ≈ 4.66e6` at 5 sites. That
  is the **superseded** value; live is `3.8375e6` (bean `qou-kt8o`). AGENTS.md
  states the prune **stands** either way, so do not re-derive on the stale
  number and do not read its staleness as weakening the exclusion.

### The open link, already named by the corpus — and it is not "what is τ_arch"

`computations/qbeta/qbeta_c3_barodd_gluing_newton_solve.py:42-49`: *"**THE
OPEN LINK (single, named): the map `q₀ → m`** (the meridian holonomy the
substrate assigns to 4₁). … This probe computes `𝔙(m)` for any given `m` but
does **NOT** fit `m(q₀)` (that would be a fit)."*

That is the correct statement of the question. The machinery that consumes `m`
exists and is committed (`gluing_residual(z, m)`, Newton-solved, recovering
`Vol(4₁) = 2.029883213` to 10 digits with `CS = 0`), and `algebraic_seeds(q, n)`
exists at `snappy_cusp_seeding.py:60`. **Measured: the two have never met** —
of 8 files carrying a gluing residual, seven have zero seed references and the
eighth uses `x = q^{-k}` only as a coordinate label. So the forward measurement
is a **composition, not a derivation**. Inverting `m` against a target would be
a fit and is forbidden.

### Status

Still **`in-progress`**. The conjecture is open; three of this bean's four
claims now belong to other artifacts, and the two that remain are narrow.

---

## 2026-10-10 — THE FORWARD MEASUREMENT: the pole-seeding claim converges to the wrong root

Owner-selected option (c). `computations/qpochhammer_newton_seed_basin_probe.py`,
composing `gluing_residual(z, m)` (from
`computations/qbeta/qbeta_c3_barodd_gluing_newton_solve.py`) with
`algebraic_seeds(q, n)` (`snappy_cusp_seeding.py:60`) — the two halves the
corpus had and had never joined.

**Nothing is fitted.** `m = 1` is the complete hyperbolic structure (parabolic
meridian), recorded as such in the cited probe's own docstring.

### The root structure

At `m = 1` the equation is `(z² − z)² = 1`, which **factors** (verified at a
probe point to `1.5e-51`):

    (z² − z − 1)(z² − z + 1) = 0
      z² − z − 1 = 0  ->  φ = 1.6180339887, −1/φ = −0.6180339887   REAL
      z² − z + 1 = 0  ->  e^{±iπ/3}                                 geometric

Four roots, **half degenerate** — the real pair is not in ℍ, so not shapes.

### Five findings

1. **The `k=0` seed is a CRITICAL POINT, for every `q₀`.**
   `R'(z) = 2(z²−z)(2z−1)` vanishes at `z = 0, ½, 1`, and the `k=0` seed is
   `q₀⁰ = 1` identically. The Newton step is **undefined** there, independently
   of the substrate value — measured `STUCK` at iteration 1. The carrier's
   claim that the poles are *"isolated in the cusp variety"* so the step
   *"avoids local-minimum traps"* is inverted at `k=0`.
2. **The real seeds cannot reach a geometric root at all. Scope-(b);
   invariant = a Newton step on a real-coefficient rational function maps the
   reals into the reals.** Measured: `k=1` converges in 14 iterations to
   `−1/φ`, with `|Im| = 0` at every step.
3. **The imaginary lift is mandatory and undetermined.** The algebraic side
   gives a real number, the geometric side needs a point of ℍ, and both
   producers lift by a hardcoded `IM_PERTURBATION = 0.1`.
4. **At the corpus's own lift, NEITHER seed reaches the geometric root.**
   Swept `δ = 0.001 … 2.0`: at `δ = 0.1`, `k=0` lands on the geometric
   *conjugate* `e^{−iπ/3}` (wrong half-plane) and `k=1` on the degenerate
   root. Both reach `e^{+iπ/3}` only from `δ = √3/2` — the answer's own
   imaginary part.
5. **The CONTROL says the seeds are not faster, and that is the claim.** The
   carrier's claim is comparative (`O(1)` *"instead of"* a generic `z_q`), so
   a bare count cannot test it. With any control point that IS a root excluded
   (at `δ = √3/2`, `re = 0.5` is exactly `e^{iπ/3}`): at `δ = 0.1` no
   algebraic seed reaches GEOM while a generic one does; at `δ = √3/2` best
   generic **7** against best algebraic **8**. So the recorded "9–11
   iterations" sits inside the generic range and is not evidence.

### Scope

(b) for findings 1 and 2, invariants named. **The conjecture is NOT excluded**
— only the seeding claim as stated with the real poles. Confined to the
figure-eight complete structure, where the residual is this quartic.

### What this leaves

The gap is the one the corpus already names, in
`qbeta_c3_barodd_gluing_newton_solve.py:42-49`: *"THE OPEN LINK (single,
named): the map `q₀ → m`"*, which that probe explicitly declines to fit. This
measurement adds that the *seeding* route to it does not work either, and says
what a replacement must supply: **the imaginary part**, which no part of the
conjecture currently determines.

### Also landed, owner option (a)

The carrier's §Empirical scope now records the counting prune, cites
`seed_is_not_the_cusp_shape` and the `rotate` / `rotate_angles` orbit lemmas
rather than presenting either as new, corrects the bullet's "pole-to-cusp" to
tetrahedron-indexed (which is what the producer measures), drops the `τ_arch`
glyph collision, and leaves the cusp-vs-tetrahedron indexing **in tension with
the resolution marked open** — because substituting the word is not a repair
(a holonomy is cusp data; the tetrahedron-indexed datum is the **edge**
equation). Render-QA grep battery clean, `qa-sweep` exit 0, not
machine-render-validated (`render-latex.ts` absent at that path here).

**Status: `in-progress`.** The conjecture is open.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `(none)` → `qou-n4nr`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## Progress 2026-11-16 (PR #8187)

- [x] Added `l6a4_orbit_step_one`, `l6a4_orbit_step_two`, `l6a4_orbit_step_three`, `tau_arch_not_injective_of_lt_roots`, `tau_arch_constant_of_single_isometry_class`, and `snappy_cusp_seeding_non_injective` in `folio/quantum-observable-universe/mass-theory/shared-denominator-cusp-holonomy.lean` + 80-dps `mpmath` probe (`litlfred/qou#8187`, `28237151a70df9ecb11495b374e141771a7b4a76`).
- [ ] Await review and merge of `litlfred/qou#8187`.
