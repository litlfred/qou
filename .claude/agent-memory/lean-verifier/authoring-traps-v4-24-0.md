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

## TRAP — raise `maxHeartbeats` BEFORE believing a `whnf` timeout

`(deterministic) timeout at whnf, maximum number of heartbeats (200000)` reads
as "the proof is fine, this machine is slow". Measured 2026-09-04 on
`chi_v21_matrix_trace_identity`: at 4 000 000 heartbeats the declaration
elaborates in **28 seconds** and reports the actual failure, which was a `rw`
that never applied because `ring_nf` had already normalised its pattern away.
The tactic script had never proved the theorem at any budget.

So a timeout makes a **broken** proof indistinguishable from a **slow** one, and
the cheap test settles it. Do this before concluding anything about a timeout,
and certainly before recording one as an environment limitation.

## TRAP — a forward reference reports `Unknown identifier`

Lean is order-sensitive, so a declaration used above its own definition says
`Unknown identifier X` — the same message as a name that was renamed or deleted.
Same file, 2026-09-04: `hoefsmit_v21_b_sq_rational` was declared at the end and
consumed at line 247. Grep the file itself before grepping the tree or the
oleans for a rename.

## TRAP — an enumerated reduction table is sized against the wrong quantity

`lagrange-resolvent-transform` carried seven lemmas reducing `ζ^5 … ζ^16`,
justified as "the products k·j for k,j ∈ {0,…,4} range over {0,…,16}". True of
the products; irrelevant to the proof, because `ring_nf` multiplies in a further
`ζ^4` and exponents reach 32. The `k = 4` case had never been proved.

Prefer a general conditional simp lemma — `ζ^n = ζ^(n-5)` given `5 ≤ n` — which
terminates (exponent decreases, side condition fails below 5) and cannot go
stale when a normaliser changes. Size a table against what the *normaliser*
produces, not against the inputs.

## TRAP — an UNUSED hypothesis is a correctness defect, not a lint nit

Three files in one sweep carried an instance or hypothesis binder their proof
never consumed. The linter calls it "unused variable"; what it actually does is
**overstate the dependency** — an unconditionally true fact reads as conditional
on whatever the binder names. `dominant_subbraid_consistency` had
`[hd : DominantSubBraidAtEps6]` on a closure fact independent of it;
`sigma1_v21_param_sq_trace` had `hq : q ≠ 0` on a polynomial identity.

This is the mirror of the §3b-cond violations (a conditional result stated
unconditionally), and **neither direction is visible to `#print axioms`** —
both proofs are clean. Only reading the signature against the statement catches
either.

## TRAP — ANY `… in` modifier goes ABOVE the docstring, never between it and the declaration

Third instance this sweep, once each for `set_option … in`, `open … in`, and
`omit … in`. All three produce the same shape of parse error naming whatever
token follows:

```
error: unexpected token 'omit'; expected 'lemma'
error: unexpected token '/--'; expected 'lemma'
```

Correct:

```lean
omit [CommRing R] in
/-- docstring -/
theorem foo …
```

The second spelling of the error is the one that misleads — `unexpected token
'/--'` reads as a broken docstring, and the actual defect is a modifier placed
after it. Same root cause when a docstring is left orphaned by a deleted
declaration; check what precedes the docstring, not just the docstring.

## TRAP — `opaque x : T` ASSERTS `Nonempty T`, and that may be the conjecture

`failed to synthesize Inhabited (GroupLikeDepth q 2)` on an
`opaque Li2_zeta_6 (q : R) : GroupLikeDepth q 2` is not a request for an
instance. An `opaque` constant of type `T` may only be introduced once `T` is
known non-empty, so declaring one **asserts inhabitedness globally**.

Measured 2026-09-04 in `gb-depth-period-correspondence`: the type's
non-emptiness is *exactly* the `sharpness` field of the file's own conjecture
class (`∀ n ≥ 1, Nonempty (GroupLikeDepth q n)`, traced in its docstring to
Borel's theorem). Supplying an `Inhabited` instance to satisfy the elaborator
would have made the file compile by assuming, unconditionally and outside the
class, the very thing every theorem in it is conditional on.

Before adding `Inhabited` to silence this: check whether the type's
inhabitedness is a conjectural claim somewhere in the same file. If it is, take
the element as a parameter and derive existence from the class instead. Note an
`opaque` FUNCTION into the type does the same thing as a constant.

## TRAP — repairing a sibling can turn a VISIBLY broken file into a SILENTLY divergent one

`lean.ref` resolves **sibling-first by file** (§0a candidate 1). If a sibling
declares the same fully-qualified name as a library file, with a different
statement, the sibling is what a reader reaches. While it does not compile that
is loud. Once it compiles it is quiet, and nothing else checks the two agree.

Measured 2026-09-04 across 38 sibling files repaired in one sweep: **6 appear in
`scripts/lean-sibling-library-divergence-audit.py`'s 195 divergences, 4 verified
real.** Type case: `QOU.planck_classical_limit` is declared in both
`quantum-planck-constant.lean` and `QuantumObservableUniverse/Propositions.lean`
— the sibling proving it of `quantumPlanckConstantSibling`, the library of
`quantumPlanckConstant`.

So run that script over anything you make compile, and check whether the block's
`.md` means the sibling's statement or the library's. Repairing is not neutral.

## TRAP — that script over-reports; verify a pair against BOTH files first

Same run, 2 of the 6 were **false positives**: it paired
`QOU.LiftingDescent.descent_cocycle_deviation` with
`LiftingDescent/ccg_crossed_module_structure.lean`, which declares only
`CrossedModuleContext` and `ccg_crossed_module_structure`, and
`QOU.BraidKnot.ConfinementPhaseStratification` with a `ConfinementLevel.lean`
that declares no such name.

Its own header explains why: it builds a fully-qualified name by concatenating
**every** `namespace` line in the file, wrong for a file that opens and closes
several in sequence — 6.1 % of sibling and 8.5 % of library files.

One `grep -cE '^(theorem|lemma|def|structure|class) <name>' <libfile>` settles
it. Skipping that nearly cost a retraction of a correct repair here, on the
strength of a tool a sibling agent wrote and I had not checked. **Another
agent's audit script is not a primary source.**

## `pow_le_pow_left` does not exist — and prefer `gcongr` over chasing the name

`unknown identifier 'pow_le_pow_left'` (2026-09-04,
`QOU/Hecke/BindingExtensivity.lean`). It is `pow_le_pow_left₀`
(`Mathlib/Algebra/Order/GroupWithZero/Unbundled/Basic.lean:449`). **The fix that
does not rot is `gcongr`** — it discharged the goal from the hypotheses already
in context and does not move when a lemma is renamed. Same discriminator as the
module moves above: grep the mathlib **source** tree.

Bernoulli itself is `one_add_mul_le_pow (H : -2 ≤ a) (n : ℕ) : 1 + n*a ≤ (1+a)^n`
in `Mathlib.Algebra.Order.Ring.Pow`.

## TECHNIQUE — the degenerate-model test, and it is sharper than reading the docstring

From bean `bday`, and it generalises well past its origin. For any `structure` or
`class` whose fields are **pure data with no relating hypotheses**, construct the
degenerate instance and see what survives:

- `flatBirthday x := if x = 0 then 0 else 1` — two-valued — satisfies **all six**
  birthday axioms of `SurrealField`. So any theorem proved from those axioms
  alone is true in the flat model, and if it degenerates to something trivial
  there, it carries no content whatever its statement looks like.
- `qou-k4ul`: `OperatorSelectionLpContext` carries only data, so
  `operator_selection_lp` is **refutable** — `d = 1, n_target = 1, x_star = 0`
  makes its first conjunct say `0 = 1`.
- Same mechanism, 2026-09-04: `CategoricalTransferMatrix` carries `base`,
  `filtration`, `vertex_volume` as free fields, and
  `transfer_matrix_level_independence` asserted a relation among them for every
  instance. Refuted by two instances sharing a base with volumes `0` and `1`.

Why it beats "read the statement against the `.md`": it is **mechanical and
decides**, where reading raises a suspicion. `ope_is_skein` — an axiom whose
`OPE` carries the eigenvalues as fields — falls to it in one step.

**So when a `structure`'s fields are data and a theorem over it concludes a
relation among them, try to refute before trying to prove.**

## TRAP — check `.beans/` (checklist path 6) BEFORE calling a finding new

Measured 2026-09-04: a four-axiom table was written up as "the single most useful
thing this sweep found" and the `.beans/` grep, run afterwards, turned up
`qou-k4ul` (completed 2026-08-16) carrying the *same mechanism* on a different
declaration, and `bday` (in-progress) carrying the *general method*. The sweep
contributed instances, not the class.

`.beans/` is not under `docs/`, `content/`, `computations/` or `library/`, so no
other checklist path reaches it, and a `completed` bean is the one that bites —
it means the question was answered, sometimes in a single sentence with no
artifact anywhere else.

---

## TRAP — `Matrix.trace_fin_two` leaves APPLICATIONS; `Matrix.trace_fin_two_of` projects

Measured 2026-09-04 on `chi_v21_matrix_trace_identity` (bean `qou-18b6`), an
11-fold product of 2×2 matrices over `q`, `q⁻¹` and a square root.

The two names give no hint of the difference and it is the whole proof:

- `Matrix.trace_fin_two` rewrites `trace M` to **`M 0 0 + M 1 1`** — index
  *applications*, which every later tactic then has to see through.
- `Matrix.trace_fin_two_of` rewrites `trace !![a,b;c,d]` to **`a + d`**.

With the first, after `Matrix.mul_fin_two` folds the eleven factors into one
`!![_,_;_,_]`, `field_simp` runs on the un-projected expression and
**exhausts 2 000 000 heartbeats**. With the second the same proof closes.

**Two consequences worth internalising.**

*The off-diagonal entries are where the mess is.* Only EVEN powers of the
off-diagonal parameter `b` reach the trace — each symmetric factor moves you
between diagonal slots, and a path back to the same slot takes an even number
of steps. Odd powers do exist (`b^3` appeared 20 times in the normalised
matrix) but only in the entries the trace discards. So projecting first is not
merely tidier: it is what makes a plain `rw [hb4, hb2]` substitution
sufficient and removes the need for any `linear_combination` certificate.

*Substitute the higher power first.* `rw [hb2]` where `hb2 : b^2 = c` does NOT
touch `b^4` — it is not a syntactic subterm. Use `rw [hb4, hb2]`, deriving
`hb4` by `rw [show (4:ℕ) = 2*2 from rfl, pow_mul, hb2]`.

Also: `reduceIte` does **not** fire on `if (1 : Fin 2) = 0`. A local
`have hif : ∀ A B, (if (1 : Fin 2) = 0 then A else B) = B := by intro A B; norm_num`
does. `if_true` handles only the index-0 side.

## TRAP — do not blame a TACTIC for a defect in the goal you handed it

Same session, and this is the more transferable half.

I recorded in a commit message, as a property of the tactic, that **"`ring_nf`
re-folds matrix literals back into `Matrix.mul` applications, undoing
`Matrix.mul_fin_two`"** — with the evidence that a subsequent `rw [hb2]` failed
with *"did not find `b ^ 2`"* and the goal visibly contained `!![…] * …` again.

**Retracted.** `ring_nf` did nothing of the sort. In that run the
`if (1 : Fin 2) = 0` guards were still unreduced, so four matrix factors had
never been folded in the first place — `ring_nf` was acting on a goal that
genuinely still contained matrix multiplication. Add the `hif` helper and the
same `ring_nf` behaves correctly, and the proof *requires* it.

**The generalisable shape:** a tactic that "misbehaves" on a goal you did not
fully inspect is usually reporting the goal's state, not its own. Before
writing a tactic's behaviour into memory, a commit message or a bean, re-run it
on a goal you have *verified* is in the form you assume. The cost of getting
this wrong is high and asymmetric: a false trap steers every later agent away
from the tactic that actually closes the proof.

Note also the failure text was `rewrite failed: Did not find an occurrence of
the pattern b ^ 2` — nearly identical in shape to this file's older
`√(hoefsmit_v21_b_sq q) ^ 2` failure, and a *different* cause. Same message,
different diagnosis, twice in one file.

## STABLE — `div_le_iff` is GONE; the name is `div_le_iff₀`

Measured 2026-09-05, `QOU/Hecke/GeometricTailBound.lean`:
`error(lean.unknownIdentifier): Unknown identifier 'div_le_iff'`. Not deprecated
— **absent**, with no alias to warn you. A `grep` of the whole Mathlib checkout
for a deprecation of the unprimed name returns nothing.

```
-- Mathlib/Algebra/Order/GroupWithZero/Unbundled/Basic.lean:1100
lemma div_le_iff₀ (hc : 0 < c) : b / c ≤ a ↔ b ≤ a * c
```

So `rw [div_le_iff hpos]` → `rw [div_le_iff₀ hpos]`. Expect the `₀` family
generally: these moved to the `GroupWithZero` hierarchy in this era.

## TRAP — `rw [h] at *` rewrites nothing and then fails the tactic block

Same file, same run:

```
Tactic `rewrite` failed: Did not find an occurrence of the pattern
⊢ (1 - x)⁻¹ < C
```

The pattern was `tail_eq`'s LHS `(1-x)⁻¹ - (1+x)`, which occurs in **no**
hypothesis and not in the goal — the goal has `(1-x)⁻¹` alone. `at *` reads as
"apply wherever it fits" but is "apply everywhere, and fail if it fits nowhere".

The fix is not a better rewrite target — it is to stop rewriting. Build the
equation you actually want with `have`, then finish linearly:

```lean
have hinv : (1 - x)⁻¹ = (1 + x) + x ^ 2 / (1 - x) := by
  have h := tail_eq (x := x) (ne_of_lt h1); linarith
```

`linarith` treats `(1-x)⁻¹` and `x^2/(1-x)` as atoms, so re-arranging an
identity into the shape you need is free.

## STABLE — two things I was about to record as traps, and both are FALSE

Recording these because the near-miss is the point (cf. the `ring_nf` retraction
at the end of this file). Before the run I had convinced myself that:

- **`linarith` cannot prove a `≠` goal.** It can. `have hne : x ≠ 1 := by
  linarith` from `h1 : x < 1` produced `hne : x ≠ 1` in the very error context
  that reported the *other* failures — the proof state is the evidence.
- **`positivity` cannot prove `0 < x^2/(1-x)`** because `1 - x` is not
  syntactically positive. It can, with `hpos : 0 < 1 - x` in context; `htail`
  likewise appears in the failing context, established.

Both "fixes" I wrote (`ne_of_lt h1`, `div_pos (pow_pos h0 2) hpos`) are fine and
more explicit, but neither was necessary. **The error log names every failure it
found; a tactic that does not appear in it succeeded.** Read the whole log
before theorising about a tactic — the failing hypotheses printed *above* the
error are a free proof that everything producing them worked.

## TRAP — a structure with `add_*`/`neg_*` simp projections but NO binary-`sub` ones

`QOU.MathlibExt.HeckeRankTwoMarkov.Hecke2` carries `@[simp]` projections for
`0`, `1`, `+`, unary `-`, `*` and `•` — and **none for binary `-`**. So after a
`map_sub` the goal `(σ - h • 1).const = -h` is stuck: `ext <;> simp [...]` leaves
`unsolved goals` with the subtraction sitting unreduced, and the error names the
*projection* goals, which reads like a missing `sigma`/`sigmaInv` unfolding
rather than a missing `Sub` lemma. (Measured 2026-09-12, `HeckeTowerWitness.lean`
`collapse_twGenInv`; it was the only error in the file.)

**Fix at the consumer: add `sub_eq_add_neg` to the `simp` set.** `Sub` comes from
`AddCommGroup`'s default `a + -b`, so that one rewrite routes the goal through
the `add_*`/`neg_*` projections that *do* exist:
`ext <;> simp [sigma, sigmaInv, sub_eq_add_neg]`.

Prefer this to adding `sub_const`/`sub_gen` upstream when the defining file is
already merged on `main` — the consumer-side fix touches one branch, the
upstream one re-opens a file other branches are importing.

**Generalisable check:** before debugging a stuck projection goal, list which
operations the structure actually has `@[simp]` lemmas for. An absent one is
invisible in the error message, which shows only the un-reduced term.

## STABLE — `Set.image_subset` is deprecated at mathlib `f897ebcf72cd`

→ **`Set.image_mono`**, and the signature changed shape: `f` went from an
**explicit** argument to an **implicit** one.

```lean
Set.image_subset : ∀ {α β} {a b : Set α} (f : α → β), a ⊆ b → f '' a ⊆ f '' b   -- old
Set.image_mono   : ∀ {α β} {f : α → β} {s t : Set α}, s ⊆ t → f '' s ⊆ f '' t   -- new
```

So the migration is not a rename alone — **drop the explicit `_` placeholder**:
`Set.image_subset _ hsub` becomes `Set.image_mono hsub`. Leaving the `_` in
gives a confusing arity error rather than a deprecation notice. The deprecation
itself is a **warning**, so it passes `lake build` and only fails a
zero-warnings gate.

## TRAP — `field_simp; ring` residual `2⁻¹ * 2` over a generic `[Field R]` = the STATEMENT is false in char 2 (2026-09-14)

Symptom, in a file obeying AGENTS.md §7c (generic `{R : Type*} [Field R]`, no `ℝ`):

```
⊢ -1 + q ^ 2 + q ^ 2 * 2⁻¹ * 2 + 2⁻¹ * 2 = q ^ 2 * 2
Try this: ring_nf
  Note that `ring` works primarily in *commutative* rings … consider `noncomm_ring`
```

**The "noncommutative ring" hint is a RED HERRING** — `R` is a field. The real
content is that `2⁻¹ * 2 = 1` needs `(2 : R) ≠ 0`, which `Field` does **not**
give: `Mathlib` defines `0⁻¹ = 0`, so in characteristic 2 any `x / 2` silently
collapses to `0` and no tactic can close the goal. **A leftover `2⁻¹ * 2` (or
`3⁻¹ * 3`, …) that `ring` will not discharge is a characteristic obstruction,
not a tactic-selection problem.** Anything whose definition divides by a numeral
— a half-sum, an average, a midpoint, `(q + q⁻¹)/2` — carries it.

Fixes, in order of preference: add `(h2 : (2:R) ≠ 0)`; or `[CharZero R]` (then
`have h2 : (2:R) ≠ 0 := two_ne_zero`); or move the statement past the
archimedean wall to `ℝ`. `field_simp` picks `h2` up from context automatically —
it does **not** need to be passed, and passing `hq` alone is what leaves the
residual.

**Do not report this as "unproved" — report it as FALSE, with the witness.**
A red tactic alone is only evidence about the tactic (MEMORY.md §19). The
three-line decisive form, all sorry-free, ~5 s:

```lean
theorem aniso_char_two (h2 : (2:R) = 0) (q : R) : (q + q⁻¹)/2 = 0 := by
  rw [div_eq_mul_inv, h2, inv_zero, mul_zero]
theorem sub_inv_ne_zero_char_two (h2 : (2:R) = 0) {q : R} (hq : q ≠ 0) (hq1 : q ≠ 1) :
    q - q⁻¹ ≠ 0 := by
  intro h
  have hinv : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  have hsq : q * q = 1 := by linear_combination q * h + hinv
  have hz : (q - 1) * (q - 1) = 0 := by linear_combination hsq + (1 - q) * h2
  exact hq1 (sub_eq_zero.mp (mul_self_eq_zero.mp hz))
```

`linear_combination`, not `linarith` — `linarith` needs an **order** and `R` has
none; over a bare field it fails with the unhelpful "failed to find a
contradiction".

**Inhabiting the counterexample.** `ZMod 2` is often NOT enough: its only
nonzero element is `1`, so an identity failing only at `q ∉ {0,1}` still holds
there. (It *does* refute a claim of the shape `… / 2 = q`, since LHS collapses to
`0 ≠ 1`.) For the rest use **GF(4) = `GaloisField 2 2`**, and note two gotchas:
there is **no `Fintype` instance** (get one with `haveI : Fintype F4 :=
Fintype.ofFinite F4`), `GaloisField.card` is stated in **`Nat.card`** (bridge with
`Nat.card_eq_fintype_card`), and both need a `local instance : Fact (Nat.Prime 2)
:= ⟨Nat.prime_two⟩`. `∃ q, q ≠ 0 ∧ q ≠ 1` then follows from
`card = 4 > 2 ≥ card {0,1}` by `Finset.card_le_card` + `omega`. Also: `decide`
gets **stuck** on `ZMod 2` field division (`ZMod.decidableEq` will not reduce
through `Field.inv`) — route through the abstract lemma with `(by decide)` for the
`(2 : ZMod 2) = 0` and `q ≠ 0` side conditions instead.

**Why it matters at the gate:** an erroring declaration is still ADDED to the
environment with `sorryAx`, so `#print axioms` on it reads
`[propext, sorryAx, Classical.choice, Quot.sound]`. That is the tell that
separates "this decl failed" from "this decl is fine" when a multi-error file
still produces axiom output.

## TRAP — applying a matrix EXPRESSION to an index: "Function expected … ?m" (2026-11-15)

`(A * B - C * D) ((i, j), (k, l)) = …` does not elaborate: the `HSub`/`HMul` result type is a
metavariable at application time, so Lean reports `Function expected` and the statement becomes
`sorry () = …` (the file is red, not vacuous). Two fixes, both needed: ascribe the type,
`(A * B - C * D : Matrix ι ι R)`, and apply CURRIED, `… (i, j) (k, l)` — a `Matrix` is `ι → ι → R`,
so a single pair argument is ill-typed even once ascribed. Same for helper lemmas `(P * M) a b`.
Also: an 81-case `fin_cases <;> simp` over `Fin 3 × Fin 3` matrix products hit the 200k heartbeat
cap; at `q = qi = 1` `rCheckN` is the flip matrix, and `(flip * M) a b = M a.swap b` closes the
identity for a GENERIC `x` in 3 s with no case split (`QOU/IwahoriHecke/JimboClassicalLimit.lean`).
