# Authoring traps under Lean v4.24.0 / this Mathlib pin — and one working recipe

Read on demand from `MEMORY.md`. Moved here 2026-09-03 to keep `MEMORY.md` under
the 200-line injection window; nothing was dropped.

## Module moves (a "cache miss" error that is really a dead import path)

Symptom is identical to an uncached olean — `object file … does not exist` — so
distinguish source-bug from cache-gap by checking the mathlib **source** tree for
a `.lean` at that path and grepping whether any mathlib file imports it.

- `import Mathlib.Data.Matrix.Notation` **does not exist**. The `!![a,b;c,d]`
  literal notation lives in `Mathlib.LinearAlgebra.Matrix.Notation`
  (seen 2026-08-29, `QOU/MassTheory/MagnusPairingSignStructure.lean`).
- `import Mathlib.Data.Matrix.Kronecker` **does not exist** (confirmed
  2026-08-31). `⊗ₖ` (`open scoped Kronecker`), `Matrix.mul_kronecker_mul`,
  `Matrix.trace_kronecker`, `Matrix.one_kronecker_one` live in
  `Mathlib.LinearAlgebra.Matrix.Kronecker`. Decisive discriminator: the source
  tree has `LinearAlgebra/Matrix/Kronecker.lean` and no `Data/Matrix/Kronecker.lean`
  while `Data/Matrix/` is otherwise full. Several `Data.Matrix.*` modules moved
  to `LinearAlgebra.Matrix`.
- `import Mathlib.Algebra.BigOperators.Ring` **is not a module**: it is a
  directory (`Ring/Finset.lean`, `List.lean`, `Multiset.lean`, `Nat.lean`) with
  no aggregator; zero mathlib files import the bare path. `Finset.mul_sum` is in
  `Mathlib.Algebra.BigOperators.Ring.Finset` (seen 2026-08-31,
  `QOU/MassTheory/MagnusOmega2LocalDecomposition.lean`).
- `Finset.sum_powerset_card` **does not exist**; the lemma is
  `Finset.sum_powerset s f` (additive of `prod_powerset`,
  `Mathlib.Algebra.BigOperators.Group.Finset.Powerset`), then
  `Finset.card_univ`; `rw [esymm]` only AFTER `intro j` (seen 2026-09-02,
  `QOU/MassTheory/MagnusHookExteriorPower.lean`).
- The aggregator `Mathlib.olean` is ABSENT from the QOU-cone partial restore
  (3470 mathlib oleans), so `import Mathlib` errors `Mathlib.olean does not
  exist` — verify such a file via a byte-identical-tactics temp copy with
  narrowed imports (a strict subset of Mathlib).

## Lexer / elaboration traps

- Under `import Mathlib.Tactic`, `₊`/`₋` (U+208A/U+208B) are **notation
  tokens** (PosPart etc.): a binder named `ρ₊` fails to lex (`unexpected token
  '₊'; expected ','`). Rename the binder (`ρ₊`→`ρp`); pure alpha-renaming. Fine
  in comments/docstrings.
- Imports must precede a `/-!` module docstring; Lean rejects any `import`
  after it (seen 2026-08-30, `EmCouplingBarParity.lean`).
- `omit [inst] in` must precede the docstring (seen 2026-08-30,
  `BrunnianIsotypeExclusion.lean`).

## Recipe — explicit small determinant with rational entries (measured 2026-09-03)

`QOU.Shared.DetFin` ships `Matrix.det_fin_four / det_fin_five / det_fin_six`
(explicit Leibniz sums, generic `CommRing`, sorry-free, `#print axioms` = the
standard three). For a `Fin 5` principal submatrix of a `Fin 6` table whose
entries are a Fin-literal pattern-matching def (`| 2, 3 => …`):

```lean
rw [Matrix.det_fin_five]
simp only [<apply-lemma>, Matrix.of_apply, Fin.castSucc_zero, Fin.castSucc_one,
  Fin.reduceCastSucc, <table def>]
field_simp
ring
```

The core dsimprocs `Fin.reduceCastSucc` / `Fin.reduceSucc`
(`Lean/Meta/Tactic/Simp/BuiltinSimprocs/Fin.lean`) reduce `Fin.castSucc 3` to
`3`; the table's equation lemmas then fire on numerals with NO `fin_cases`.
`field_simp; ring` closed a degree-20 identity with `(q²+1)`-power denominators
and 120 Leibniz terms in seconds (whole scratch file: 29 s `user`, cold-cache
wall 1m52s). Corollary lemma names, all confirmed in this pin:
`Matrix.IsSymm.submatrix (h : A.IsSymm) (f)`, `div_neg_of_neg_of_pos`,
`neg_neg_of_pos`, `eq_div_iff (hc : c ≠ 0) : a = b / c ↔ a * c = b`,
`LT.lt.ne`. Real-rootless quadratics: `nlinarith [sq_nonneg (2*q - 1)]`.

`sympy` is absent by default in this container; `python3 -m pip install --user
sympy` works through the proxy (got 1.14.0, matching the witness environment).

## TRAP — `ring` on a NONCOMMUTATIVE ring: "ring_nf made no progress"

`ring` needs `CommSemiring`. In a file over `{A} [Ring A] [Algebra R A]` it
fails on pure *associativity* rearrangements (`ρ * (y * x) = ρ * y * x`) with
`error: ring_nf made no progress on goal` — a message that reads like a
tactic-strength problem, not a typeclass one. `congr 1` before it does not
help; the residual goal is still noncommutative.

Fix, cheapest first: **explicit `mul_assoc` inside the `rw` chain**
(`rw [← mul_assoc, hcyc (ρ * y) x, mul_assoc]`), which also collapses a
`have … := by ring; rw [this]; congr 1; ring` block to one line. `noncomm_ring`
exists (`Mathlib.Tactic.NoncommRing`) for genuine ring-normalisation, but is
overkill when the only content is reassociation. Measured 2026-09-03,
`MagnusCurvatureCommutator.lean`: 3 `ring` errors → 8 lines deleted, 2 added,
EXIT 0, statements untouched.

Direction check for `rw [mul_assoc]` (`(a*b)*c = a*(b*c)`): it fires on the
FIRST `(a*b)*c` in goal-traversal order, then rewrites every occurrence of that
instantiated term. `ρ * (x*y)` does NOT match (first arg is not a `*`), so a
goal `tr (ρ*(x*y)) - … = tr (ρ*x*y) - …` closes with `← mul_assoc`, not
`mul_assoc`.

## Lean notation tokens used as binder names — a whole parse-failure class

Measured 2026-09-03 across the 908 content-block siblings. Four of them failed
at the PARSER, and two were this: a Unicode identifier that Lean 4 has already
claimed as notation cannot be a binder name.

- **`Σ` is `Sigma`.** `axiom foo (Σ : ElectroweakSlice)` gives
  `unexpected token 'Σ'; expected '_' or identifier`, once per use.
  `observations/n-v-bring-action.lean` had **8** such errors and had been dead
  for some time.
- **`λ` is the lambda.** `cs.partitions.prod fun λ => …` gives
  `unexpected token '=>'`, because `fun λ` parses as one lambda and then
  another. `mass-theory/gram-determinant-plancherel-ratio.lean`.

**Scan for the lowercase one too.** A first pass here checked
`Σ Π Λ ∑ ∏ ⋀ ⋁ ∫` and missed `λ` entirely — capital `Λ` is NOT reserved
(17 library files use it happily), and the one that bites is the lowercase.
Confirm any candidate with a two-line file rather than by eye:

```lean
example (l : List ℕ) : List ℕ := l.map fun λ => λ + 1
-- error: unexpected token '=>'  ⇒ λ is not a legal binder
```

**Fixing the parse error reveals what it was masking, every time.** In all
four files the count went UP or sideways before it went down: `Σ` 8 → 3
(`opaque … : ℝ` needs `Inhabited ℝ`, never imported); `section` 13 → 12 → 4
(no `Mathlib.Algebra.Polynomial.Laurent`, then an unclosed
`noncomputable section` that could not surface while the section never
opened). Budget for a second and third round; do not read the first drop as
the fix.

## Orphaned docstrings — the other half of that parse class

The remaining two were a `/-- … -/` with **no declaration under it**, which is
a parse error however harmless it looks. Both were left behind by editing:
one theorem deleted with its docstring kept, and one where the file's own next
docstring says *"Auto-extracted from the single-sorry theorem body in this
file"* — i.e. a tool lifted the declaration out and left the comment.

Symptom is `unexpected token '/--'; expected 'lemma'`, or `unexpected token
'section'` when the next thing is `noncomputable section`. Same cause: a
docstring must attach to a **declaration**, and `section` is not one, nor is
another docstring. Demote to `/- … -/` or merge into the real docstring —
do not delete, the text is usually the only record of why a claim is unproved.

## TRAP — `unknown tactic` is an IMPORT failure, and its second error lies

Measured 2026-09-04 on three content-block siblings in one pass. Each
produced a PAIR of errors, and the pair is the trap:

```
he4-channel-active-set.lean:168:20         unknown tactic     -> `ring`
he4-two-row-dominance.lean:97:3            unknown tactic     -> `linarith`
hyperelliptic-z5-classification.lean:48:3  unknown tactic     -> `interval_cases`
```

followed in each case by an `unsolved goals` dump of the *untouched* goal.

A missing **term** import says `unknown identifier` and names the name. A
missing **tactic** import says `unknown tactic` and names only a column,
then buries it under the goal state. The goal dump is what you read first
and it looks like the mathematics failed. It has not — the proof is
correct and untouched; only the import is absent.

Fix is one line each: `Mathlib.Tactic.Ring`, `Mathlib.Tactic.Linarith`,
`Mathlib.Tactic.IntervalCases`. All three went to **0 errors and 0
warnings** with no proof step changed.

Check the import list before reading the goal. `he4-two-row-dominance`
imported only `QOU.BraidKnot.TwoRowStratum`; `hyperelliptic-z5` only
`Mathlib.Algebra.Ring.Parity`.

## TRAP — a tactic that closes the goal turns the NEXT tactic into an error

`No goals to be solved` at a `ring`/`rfl` line almost always means the
preceding tactic already finished. Seen three times in one sweep:

- `rw [...]` then `ring` — `rw` tries `rfl` afterwards
  (`typed-b3-sub-braid-extraction:216`)
- `field_simp` then `ring`, twice (`u-coordinate-discharges:82,104`)

Delete the trailing tactic. It is not proof drift in the mathematics, it
is a Mathlib tactic that got stronger.

## TRAP — `(x : Aut X)` silently loses the group structure

`CategoryTheory.Aut X` is a plain `def` for `X ≅ X`, so a type ascription
UNFOLDS it and you lose the `Group` instance:

```lean
(β_ V V : Aut (V ⊗ V)) ^ 2     -- failed to synthesize OfNat (V ⊗ V ≅ V ⊗ V) 1
show Aut (V ⊗ V) from β_ V V   -- works
```

Useful once you are there: `(f * g).hom = g.hom ≫ f.hom` and
`(1 : Aut X).hom = 𝟙 X` are both `rfl` (confirmed by `exact?`), so a
categorical equation and its group form are interchangeable by
`congrArg Iso.hom` after `pow_two`.

## TRAP — a sibling cannot import a sibling, and `autoImplicit` hides it

Content-block siblings live outside the Lake globs (`globs = ["QOU",
"QOU.+"]`), so `bn-mtc-action.lean` cannot import `observable-mtc.lean`
even though they sit in the same directory. Writing the instance binder
anyway does not fail with a missing-module error — `autoImplicit`
auto-binds the class NAME as a variable and you get

    invalid binder annotation, type is not a class instance ?m.5

The fix is to take the needed property as an explicit hypothesis, not to
chase the import. `set_option autoImplicit false` makes this say what it
means.

## The shape to check FIRST on any sibling failure: is it a stranded shadow?

Measured across this sweep, the single most common cause is not a broken
proof — it is that the LIBRARY declaration moved or was rewritten and the
sibling, which nothing rebuilds, was left on the old shape. Three of them
were pure duplicates of a complete library theorem and the right fix was
`git rm`:

- `delta-max-uniform-bound.lean` — `theorem … : sorry := sorry`, i.e.
  `sorry` in the TYPE, shadowing a proved
  `QOU.MassEndomorphism.delta_max_uniform_bound`. Both its imports were
  also dead (`QOU.MassEndomorphism.JetTower` has no source anywhere).
- `pentagon-uv-commutation.lean` — a verbatim copy of the library theorem
  under an unreferenced `_mass_theory` suffix, stale in one conjunct
  because a `: Prop` field had been migrated to carry a real equation.
- (and `bloch-group-quotient-construction.lean`, earlier in the sweep.)

So before debugging a sibling: find the library declaration its `.ts`
`ref` names, verify THAT compiles, and check whether the sibling adds
anything. Resolution is sibling-first **by file**, so a sibling wins even
when it declares a different name than the ref — which is also how the
ref in `bn-mtc-action.ts` stayed wrong (`QOU.ObservableMTC.bnAction` for a
declaration actually named `QOU.bnAction`) without anything noticing.
