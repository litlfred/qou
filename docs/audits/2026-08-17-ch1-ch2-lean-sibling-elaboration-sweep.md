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

**Now `exit 0` (7).** `su2-emergence`, `categorical-fourier-transform`,
`u1-equivariant-reduction`, `commutative-qou`, `categorical-reeb-derivation`,
`categorical-jet`, `poisson-object`.

**Still failing (4), all substantive — none mechanical.**
`braiding-eigenvalue-extraction` and `categorical-q-ext-deriv` (F1, `Inv R_q`);
`braiding-induced-ordering` (F6, unsound strategy); `substrate-parameter-exists`
(F8, half-finished migration).

Error counts **rose** on two files while they were being worked
(`substrate-parameter-exists` 3 → 11, `braiding-eigenvalue-extraction` 3 → 9),
because a parse error hides every line after it. That is better diagnosis, not
a better file — and it is why the raw count is a poor progress metric here.

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

### F8 — a comment that swallowed its own closing delimiter (SUBSTANTIVE)

`substrate-parameter-exists` is a **half-finished `R_q` migration**, and it is
worse than its error count suggested. A previous edit commented out the
archimedean fields of a structure literal **and took the closing brace with
them**:

```lean
  { field := fun _ => q₀
    -- field_pos := fun _ => hq_pos              -- (archimedean; not meaningful over R_q)
    -- not_root_of_unity := fun _ k hk => hq_root k hk }   -- ← the `}` is INSIDE the comment
```

so the literal never closes. Restoring the brace does **not** fix the file: the
same edit deleted the `(q₀ : R_q)` and `(hq_pos …)` binders of
`SubstrateParameter.ofReebDecomposition` while the body still references both,
and left a `/-- … -/` docstring inside a parameter list (only `--` and `/- -/`
are legal between binders). Completing it requires **deciding the signature**,
which is a content call, so it is beaned rather than guessed at.

Worth generalising: commenting out the *last* field of a `{ … }` literal, or
the last argument of an application, silently eats the delimiter that closes
it. The resulting error points at the *next* declaration, not at the comment.

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
| `qou-hg2z` | F8 — `substrate-parameter-exists`: finish the abandoned `R_q` migration (decide the signature). The other three files on this bean now elaborate. |
