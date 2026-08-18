# Chapters 1–2: every Lean sibling swept — 11 of 148 did not elaborate

**Date:** 2026-08-17
**Bean:** `qou-n4jv` (*Audit ch1+ch2 for the prose-says-more-than-type defect class*)
**Branch:** `claude/ribbon-downstream-mass-2026-08-17` (PR #5262)
**Scope:** `content/quantum-observable-universe/quantum-universes/` (ch 1) and
`content/quantum-observable-universe/quantum-observable-universes/` (ch 2).

## What was measured, and how

Every `.lean` content-block sibling in ch1 + ch2 — **148 files** (25 + 123) —
was run through `lean`-direct with `LEAN_PATH` pointed at the **root**
workspace's Mathlib oleans, against a `CategoricalFoundations.olean` rebuilt
from current source.

Two environment notes that materially affect the result, recorded because a
later agent repeating this will hit both:

- The restored cache is **partial**. The paper-local
  `content/quantum-observable-universe/lean/.lake/packages/mathlib` carries only
  **1916** oleans and is missing `Mathlib.LinearAlgebra.ExteriorAlgebra.Basic`,
  which `QOU.Basic` needs; the **root** `.lake/packages/mathlib` carries **6990**
  and has it. Point `LEAN_PATH` at the root or nothing in ch1/ch2 elaborates,
  and the failure looks like a source bug when it is not.
- The tree is a **restored** cache (`oleans=7268 traces=0`). A root `lake build`
  would evict it (the `qou-r13s` failure). Everything here is `lean`-direct.
- The shipped `CategoricalFoundations.olean` **predated its own source by five
  minutes**. Any result obtained without rebuilding it first is measuring the
  wrong file — this is the stale-olean trap, and it is why the sweep rebuilds
  the cone before starting.

## Result

| | count |
|---|---|
| swept | **148** |
| genuinely broken as-found | **11** (7.4 %) |
| environment artifact, *not* a defect | 1 (`maximal-torus-su2`) |

`maximal-torus-su2.lean` fails only because its dependency
`QOU.ParticleInteractions.AtomicityLieRank` has no olean in this partial cache.
**The source exists.** It is not a defect and must not be counted as one.

### Disposition

**All 11 now elaborate** (`lean`-direct exit 0, no bare sorries), verified
across the 20 `.lean` files this branch touches.

The four that needed real work rather than a mechanical fix:

| file | what it actually needed |
|---|---|
| `braiding-eigenvalue-extraction`, `categorical-q-ext-deriv` | F1 — restate `x⁻¹` multiplicatively over the ring |
| `braiding-induced-ordering` | F6 — a **new, sound** well-foundedness proof (axiom 1) |
| `substrate-parameter-exists` | F8 — rebuild over `ℝ`; see the correction below |

Error counts **rose** on two files mid-work (`substrate-parameter-exists`
3 → 11, `braiding-eigenvalue-extraction` 3 → 9) because a parse error hides
every line after it. That was better diagnosis, not a worse file — and it is
why the raw count is a poor progress metric here.

> **Correction to this document's own first reading of F8.** An earlier
> revision called `substrate-parameter-exists` *"a half-finished `R_q`
> migration needing a signature decision"* and left it. The decision turns out
> to be **forced, and in the opposite direction from the one the migration
> assumed** — see F8 below. Recorded rather than silently overwritten, because
> the wrong reading is the more tempting one.

## Why nothing caught this

Content-block `.lean` siblings are checked by **nothing**:

- CI is `workflow_dispatch`-only repo-wide (Actions-billing directive,
  2026-06-30), so no push triggers a build.
- `lean-content-siblings.yml` gates content-block siblings, but it does not run
  on push either.
- No `.qa.json` criterion compiles a sibling.

So a `.md` block can present a result as Lean-backed while its `.lean` has never
elaborated. That is the failure mode this sweep exists to measure, and it is the
same argument as §"QA is agent-owned; CI is a backup" — with CI down, the
agent's own verification *is* the gate, and no agent had run this one.

## Root causes — ten families, not eleven bugs

### F1 — `Inv R_q` (SUBSTANTIVE)

`R_q = LaurentPolynomial ℤ` has **no `Inv` instance**, yet files write `x⁻¹`.
Hits `braiding-eigenvalue-extraction` (`anti_eq_neg_inv`,
`hecke_polynomial_roots`) and `categorical-q-ext-deriv`.

This is not a typo. `braiding-eigenvalue-extraction`'s own docstring says *"the
rest is pure algebra over ℝ (proved here without sorry)"* — it was written over
a field, and the ground ring later became `ℤ[q, q⁻¹]`. In `R_q` the element `q`
*is* invertible, but a general element is not, and there is no `⁻¹` operation to
write. Re-expressing `lamAnti = -(lamSym)⁻¹` multiplicatively (as `lamSym *
lamAnti = -1`, already a field of the structure, or via `IsUnit`) **changes what
is stated**, so it is beaned rather than patched here.

This is the same distinction the corpus already draws elsewhere: over a field
"nonzero" and "invertible" coincide; over a ring they do not, and the stronger
one is meant.

### F2 — docstring immediately before `noncomputable section` (mechanical)

```lean
/-- Ground ring `R_q = ℤ[q, q⁻¹]` … -/
noncomputable section          -- ← docstring cannot attach to `section`
abbrev R_q := LaurentPolynomial ℤ
```

`unexpected token 'section'; expected 'lemma'`, and the two `def`s below then
fail the IR check because the `noncomputable` never took effect. Present
verbatim in **two** files (`braiding-eigenvalue-extraction`,
`substrate-parameter-exists`) — a copy-paste family, along with `su2-emergence`
which carries the same `R_q` boilerplate.

### F3 — missing imports (mechanical)

`Complex.I`, `Real.pi`, `CategoryTheory.Preadditive`, `End`, `LaurentPolynomial`
all used without importing `Mathlib.Data.Complex.Basic`,
`…Trigonometric.Basic`, `…Preadditive.Basic`, `…CategoryTheory.Endomorphism`,
`…Polynomial.Laurent` respectively.

### F4 — Mathlib rename (mechanical)

`Prod.lex_wf A B` → `A.prod_lex B` (`WellFounded.prod_lex`).

### F5 — notation collision (mechanical, but worth knowing)

Identifiers named **`λ_sym` / `λ_anti`** lex as the left-unitor token `λ_`
followed by `sym`, because `MonoidalCategory` is opened. 27 sites; renamed to
`lamSym` / `lamAnti`. Any identifier beginning `λ_` is unusable in a file that
opens `MonoidalCategory`.

### F6 — `degLex_wellOrdered`'s proof strategy is unsound (SUBSTANTIVE)

The proof derives well-foundedness of DegLex by embedding into
`ℕ ×ₗ List (Fin n)` and applying `WellFounded.prod_lex`, which requires **both**
components well-founded. The second is not:

> `List.Lex (· < ·)` on `List (Fin n)` (`n ≥ 2`) is **not** well-founded.
> `[0,1] > [0,0,1] > [0,0,0,1] > …` descends forever — each step is `Lex.cons`
> down to `Lex.rel 0 < 1`.

So this is not a stale-name repair; the route cannot be made to work. **The
theorem is true** — at fixed length there are finitely many words, and length
strictly decreases otherwise — but it needs a different argument (e.g. a
base-`n` encoding `w ↦ (|w|, encode w)` into `ℕ ×ₗ ℕ`, plus
`encode w < n^{|w|}`).

This matters beyond one file: `degLex_wellOrdered` is the Lean content of
**axiom 1 (temporal braiding)** — the axiom that makes time an ordering rather
than a coordinate, justified in `quantum-universe-axiom-motivation.md` by *"what
makes a 'before' is that the reduction stops."* That justification currently
rests on a proof that does not compile and could not compile as written.

### F7 — `β_ A A |>.hom` misparses (mechanical)

`(β_ A A).hom` works.

### F8 — an archimedean structure migrated to a ring that has no order (SUBSTANTIVE)

`substrate-parameter-exists` was the last file to fall, and the reason is worth
stating precisely, because the obvious reading is wrong.

The surface symptom is a **comment that swallowed its own closing delimiter**:

```lean
  { field := fun _ => q₀
    -- field_pos := fun _ => hq_pos              -- (archimedean; not meaningful over R_q)
    -- not_root_of_unity := fun _ k hk => hq_root k hk }   -- ← the `}` is INSIDE the comment
```

so the structure literal never closes. Worth generalising on its own: commenting
out the *last* field of a `{ … }` literal, or the last argument of an
application, silently eats the delimiter that closes it, and the resulting error
points at the **next** declaration rather than at the comment. The same edit also
commented out three *declaration headers* while leaving their bodies as orphaned
text, deleted the `q₀` binder while the bodies still referenced it, and left a
`/-- … -/` docstring between binders (only `--` is legal there).

But restoring the brace fixes nothing, and *"decide the new signature"* — this
document's first reading — mis-states the problem. **The signature is forced.**
`SubstrateParameter` is defined in the library as

```lean
structure SubstrateParameter (M : Type*) where
  field         : M → ℝ
  field_pos     : ∀ p, 0 < field p
  field_ge_one  : ∀ p, 1 ≤ field p
  not_root_of_unity : ∀ p k, k ≥ 1 → field p ^ k ≠ 1
```

> **Correction (owner question, 2026-08-18).** An earlier revision of this
> section said *"this structure lives past the wall"* and *"the file is
> archimedean throughout"*, and removed the `R_q` ground-ring banner as
> misleading. **That over-framed it, and the banner was right.** `ℝ` here is the
> **codomain of the archimedean evaluation** `ι : R_q → ℝ, q ↦ q₀` — the
> specialisation named in the standard ground-ring note carried by every
> `braids-and-knots` block — **not** the ground ring of the theory. The
> categorical content upstream of `ι` stays over `R_q`. The banner has been
> restored and the framing corrected in the file.

The three axioms do **not** all sit on the same side of `ι`:

| axiom | needs | side of `ι` |
|---|---|---|
| `not_root_of_unity : field p ^ k ≠ 1` | ring only | **categorical** — the Hecke semisimplicity condition, meaningful over `R_q` itself |
| `field_pos : 0 < field p` | linear order | evaluated |
| `field_ge_one : 1 ≤ field p` | linear order | evaluated |

So `SubstrateParameter` **conflates one ring-level condition with two
evaluation-level ones**. A cleaner split would state `not_root_of_unity`
upstream over `R_q` and keep only the two ordering bounds on the image of `ι`.
That is a change to the *library* structure, and is recorded rather than made.

What the migration actually got wrong is narrower than "wrong ring": it applied
*"keep a generic ring `R` as long as possible"* to the two **ordering** axioms —
which genuinely require an order and cannot be stated over `R_q` — and, when they
would not typecheck, commented them out as *"not meaningful over R_q"* rather
than recognising that they are conditions on `ι(q)`, not on `q`.

**The lesson, restated correctly.** "Keep `R` generic" governs content *upstream*
of `ι`. When a declaration will not typecheck over `R_q`, the candidate
conclusions are *"weaken it"*, *"this is a condition on the evaluation `ι(q)`"*,
and *"this object is genuinely archimedean"* — and commenting out an ordering
axiom silently picks the first. The right question is not "which side of the wall
is this structure on" (my first framing, too coarse) but **"is this axiom a
condition on `q`, or on `ι(q)`?"** — which can differ field by field inside one
structure, as it does here.

#### A prose-over-type finding uncovered by the repair

`SubstrateParameter.ofReebDecomposition` **discards its Reeb input.** Its
docstring describes a three-step construction, but the term binds `_interp` and
`wd_reeb_compat` to `_` and never uses them; the result is
`{ field := fun _ => q₀, … }` — definitionally the value `ofConstant` returns.
It is therefore *not* an existence proof "from the Reeb decomposition": `wd`,
`reeb`, and the compatibility proof are inert hypotheses. A scope warning now
says so in the file. Do not cite it as evidence that the Reeb data determines
`q₀`.

`WeightDecomposition` and `CategoricalReeb` exist only in *sibling* content
blocks, which cannot be imported, so both are mirrored into the file **in full**
— every field of the canonical definitions, so the hypothesis is no weaker than
the real one. This is the device `su2-emergence.lean` already uses for
`SpinDecomposition`.

### F9 — a transparent type ascription loses its instance (mechanical)

`categorical-reeb-derivation` wrote `reeb : obj ⟶ obj` and then
`(reeb : End obj) ^ period = 1`. `End obj` is *definitionally* `obj ⟶ obj`, so
the ascription is transparent: elaboration unfolds it and instance search asks
for `HPow (obj ⟶ obj) ℕ _`, which does not exist. Typing the **field** as
`End obj` fixes it; `reeb ≫ contact` still elaborates, because that unfolding
goes the harmless way.

### F10 — a sibling not importing the library (mechanical)

`categorical-jet` and `poisson-object` used `FrobeniusHopfData` /
`CategoricalConnection` without importing them. Content-block siblings cannot
import *each other*, but they **can** import the library tree — the two live in
`QOU.QuantumObservableUniverse.CategoricalFoundations` and
`…GaugeTheory`. One import cascaded through all four of `categorical-jet`'s
errors.

## Incidental Mathlib gap filled

Mathlib's `List.Lex.append_left` gives a common **prefix** only; there is no
suffix companion. `lex_append_suffix` was written for
`degLex_admissible_lex`, and the reason Mathlib's absence is not an oversight is
that **the suffix statement is false without equal lengths**:

> `w = []`, `w' = [0]`, `v = [1]`: `Lex (· < ·) [] [0]` holds by `Lex.nil`, but
> `Lex (· < ·) [1] [0,1]` fails — heads `1 ≠ 0` and `1 < 0` is false.

Equal length rules the `Lex.nil` constructor out, which is exactly why
`degLex_admissible_lex` carries `hlen`. The lemma is proved by recursion on the
`Lex` derivation, sorry-free.

## The prose-over-type findings

The bean's actual subject: places where an `.md` (or a docstring) asserts more
than its type delivers.

### P1 — `RankOneGaugeData`: "three constraints", one constraint

Documented as *"the three constraints that together force SU(2)"*. Measured:

| field | what it actually does |
|---|---|
| `fund_dim_two` | arithmetic fact about the **literal** `{ twice_j := 1 }`, discharged by `decide` (verified, exit 0). **Never mentions `qou`** — so it does not say this QOU's fundamental object has dimension 2. |
| `volume_nondeg` | genuine constraint on `qou.volumeForm` ✓ |
| `adjoint_trivial` | carries the default `:= qou.adjoint_vanishing`, so **every** QOU satisfies it automatically |

So `su2_emergence` should be read as *"volume non-degeneracy (plus the QOU
axioms) yields a spin decomposition"*, not as a three-legged derivation.

The `fund_dim_two` gap is **structural, not a typo**: tying it to
`qou.fundamentalObj` needs the spin indexing that `SpinDecomposition` supplies,
and that is the *conclusion* `su2_emergence` produces — the hypothesis cannot
reference it without circularity. Not restructured inline, because this is the
most depended-upon declaration on the critical path; a scope warning was added
to the docstring and the restructure is beaned.

Separately: `su2_emergence` is an **`axiom`**, not a `sorry`-with-citation or a
conjecture class. It is honest in its docstring about Tannaka duality being
absent from Mathlib, but per §"Axiomatization is NOT a Proof" an `axiom` is the
one disposition that hides from `#print axioms`' `sorryAx` and from the vacuity
audits. Recorded, not changed here.

### P2 — `Observation.substrate_shift`: "determined by", but free

Documented as *"the induced shift `δq` is determined by the Hopf coaction"*. The
field is `(𝟙_ qou.C) ⟶ (𝟙_ qou.C)` with **nothing** tying it to `qou.frobHopf`'s
comultiplication or to `morphism` — any endomorphism of the unit inhabits it. A
scope warning now says so.

### P3 — the snake identities were sourced to a structure a QU does not have

`frobenius-pairing-exists-proof.md` said non-degeneracy *"is equivalent to the
snake identities … which are part of **the rigid monoidal structure** applied to
the Frobenius object `A`."*

A quantum universe is **not rigid**. There is no ambient duality functor, no
ambient `A^∨`, and no ambient snake identities to invoke. The snake identities
come from **axiom 2 on `A` alone** — the `coevaluation` field of
`FrobeniusHopfData` together with `pairing_snake_left/right` — which is
precisely what *exhibits `A` as its own dual*. The Lean docstring already said
this correctly (*"derives the non-degeneracy from the structural snake-identity
axioms of the Frobenius–Hopf object"*), so the `.md` was contradicting its own
sibling. Rewritten.

This is the same two-level boundary the chapter states correctly elsewhere
(`rigid-monoidal-intro.md`, `monoidal-justification.md`,
`outro-quantum-universes.md`): a QU is braided; a QOU is braided **and** rigid,
because duals carry the antiparticles.

### P4 — prose claimed ring-generality the types refused

`base-field-independence.md` asserts *"the existence result holds over any
commutative ring `R`"* — while **nine** ch1/ch2 declarations still demanded
`[Field k]` on QU/QOU hypotheses. The `CommRing` switch had landed on the
*structures* and never reached their *consumers*.

Six were pure field projections (`Q.frobHopf`, `Q.fibreFunctor`,
`Q.adjoint_vanishing`, `Q.volumeForm`, `qu.frobHopf.nonDegeneratePairing`,
`Subsingleton.elim` on `adjoint_vanishing`) with no field-specific content in
any proof body — `[Field]` was dead weight. Generalized to `[CommRing R]`, all
verified `exit 0`, which makes them apply to the framework's own ground ring
`R_q = ℤ[q, q⁻¹]` per the standing *"keep generic ring `R` as long as possible,
so we can work in char p"* directive.

`su2-emergence`'s `[Field k]` was **deliberately left**: it guards an unproved
`axiom`, and generalizing an axiom's hypothesis makes it assert *more* without
proof — the wrong direction.

> **Correction to my own first reading.** I recorded the stale `[Field k]` on
> `frobenius-pairing-exists.lean` as *build-breaking*, reasoning that
> `QuantumUniverse.{u, v} k` could no longer elaborate once the structure took
> `[CommRing R]` and five universe parameters. It elaborates fine: `Field`
> implies `CommRing`, and Lean auto-binds trailing universe parameters.
> `lean`-direct is exit 0 both before and after. The finding is gratuitous
> narrowness, not breakage. This is the third time in this arc that reasoning
> about the elaborator instead of *asking* it produced a wrong claim; the
> earlier two were the `LeftRigidCategory` refutation and the
> `KeystonePivotalSpherical` instance-diamond claim.

### P5 — `Vect_R` over a commutative ring

`fibre-functor-atlas.md` and `fibre-functor-atlas-affine-charts.md` sent the
fibre functor to `\mathbf{Vect}_R`, and `fibre-functor-atlas-proof.md` called
`τ'(X)` *"a vector space"* — over a commutative ring. Now `R\text{-}\mathbf{Mod}`
and *"an `R`-module"*, matching ch1's definition, which already says the fibre
functor lands in `R`-**Mod**.

## What this audit did *not* cover

Stated plainly so the next agent does not read more into it than was measured:

- **Only elaboration was checked**, not `#print axioms`, not sorry-freeness, not
  whether each `.lean` proves what its `.md` claims. A file that elaborates may
  still be vacuous — see P1, which elaborates perfectly.
- **Only ch1 and ch2.** The same sweep has not been run on any other chapter,
  and the 7.4 % rate should not be extrapolated to them without measuring.
- **The `.md` prose sweep was axis-scoped**, not exhaustive: rigidity leaks,
  field/ground-ring leaks, trace/sphericality conflation, `q`-as-data, and
  nonzero-vs-invertible. A different axis could surface different findings
  across the same 372 `.md` blocks.

## Follow-ups

| Bean | Item |
|---|---|
| `qou-mbar` | F1 — `Inv R_q`: restate the eigenvalue/`q`-ext-deriv results multiplicatively or over a localisation (2 files) |
| `qou-qk51` | F6 — reprove `degLex_wellOrdered` (axiom 1) via a base-`n` encoding; current route is unsound |
| `qou-0tiw` | P1 — restructure `RankOneGaugeData` so `fund_dim_two` constrains `qou`, breaking the circularity |
| — | **All four beans discharged.** All 11 files elaborate; see the per-bean notes for what each needed. |
