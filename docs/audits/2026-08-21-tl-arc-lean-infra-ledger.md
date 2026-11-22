# TL-arc Lean infrastructure ledger — proved / conditional / assumed / vacuous

Branch `claude/tl-arc-lean-infra-2026-08-21`, PR #5352, off `origin/main` @ `9c6e9834cb`.

The arc proved `y_λ = 0 ⟺ ℓ(λ) > r` at Wenzl level `r`; that convention D **is**
level `r = 2`; that radical `= ⟨E⁽³⁾⟩` as ideals, measured at `n = 3,4,5,6`
(corank `n! − Catalan(n)` = 1/10/78/588); and the two-row cap at sum level. Two
follow-on fronts were blocked on knowing what Lean infrastructure exists.

"Mathlib has zero Hecke/Specht/Schur content" is true of **Mathlib** and false of
**QOU**, which carries 94 files under `MathlibExt/` plus a large `QBeta/`,
`BraidsAndKnots/` and `Machinery/` tree. This is the survey.

## Method, and its one real limitation

52 arc-relevant files, **784 declarations**, extracted by parser and then
hand-read wherever the classification was load-bearing. Classification is by
**reading signatures**, not by running the axiom checker: `#print axioms` cannot
see a conditional class (bean `qou-fpjy`), so an axiom-clean report is not
evidence of unconditionality.

Two detector passes were run. The first keyed only on `[X …]` instance brackets
inside a declaration's own signature. That misses section-level `variable [Foo]`
and the explicit-argument style `(ctx : FooContext)` this repo uses heavily, both
of which would silently mis-report an assumption as proved. The second pass added
`variable`-scope tracking and explicit-binder head matching against the
corpus-wide set of **728** QOU class names. The counts did not move, so the
conditional list below is complete rather than merely un-refuted.

**The parser over-reports.** Its declaration regex matches prose lines inside
docstrings, so a handful of "declarations" it found are words: `class supplies`
(`WenzlWeightVanishing.lean:366`, from "the class supplies only the bridge"),
`axiom beyond` (`Hecke/Wedderburn.lean:204`, from "no new axiom beyond the
`WedderburnDecomp` class"), and the STRUCT entries `at`, `is`, `so`, `LP`, `TL`.
Every entry in the tables below has been opened and read; the artefacts are named
here so nobody re-derives them from the raw counts.

| Class | Count | Meaning |
|---|---|---|
| PROVED | 551 | real theorem, sorry-free, no conditional class in the signature |
| DEF | 207 | definitions/abbrevs/instances — carry no claim |
| ASSUMED | 16 | the declaration **is** a `class`/`axiom` (14 real classes + 1 real axiom + 1 parse artefact) |
| STRUCT | 2 real | `WenzlPartitionData`, `Hecke.Wedderburn.Partition` |
| CONDITIONAL | 2 | carries a class hypothesis |
| VACUOUS | **0** | — see below |
| SORRY | 0 | no `sorry` anywhere in the 52 files |

## VACUOUS is genuinely zero — and the near-misses are honest

An independent `: True` grep (not the classifier) over `QBeta/`, `MathlibExt/`,
`BraidsAndKnots/`, `MassTheory/`, `Hecke/`, `Knots/`, `Shared/` returns five
`: True` **class fields**:

- `QBeta/FMapStructuralPaths.lean:37,51,65` — `is_modular_dual`,
  `is_hexagon_derived`, `is_cyclotomic_reconstruction`
- `MathlibExt/SDP.lean:141,150` — `dual_feas`, `obj_eq`

All five are **explicitly marked `@marker` / `opaque marker`** with docstrings
that say what is missing ("Genuinely-open: the construction is not yet in place,
so this is a tracked opaque placeholder, not a fabricated content-bearing
claim"), and `SDP.lean` names the content-bearing ℝ-specialised fields to consume
instead (`RealStrongDualityPair.dualSlack_psd`,
`RealStrongDualityPair.obj_eq_dualObj`). `@marker` is the sanctioned opt-out for
`proof-claims-unencoded`. **These are not defects and are not reported as such.**

## ASSUMED — the 14 classes and 1 axiom

| Declaration | `file:line` | Instance? | Notes |
|---|---|---|---|
| `IsOcneanuWeightSystem` | `QBeta/WenzlWeightVanishing.lean:376` | none, **deliberately** | the exemplar — see below |
| `SchurElementCriterion` | `MathlibExt/WenzlSchurElement.lean:240` | 1 | |
| `QSchurYLambdaClosedFormClaim` | `BraidsAndKnots/QSchurYLambdaClosedForm.lean:171` | **0** | |
| `YLambdaRecipeFromPartitionContext` | `BraidsAndKnots/y_lambda_recipe_from_partition.lean:21` | **0** | self-assuming projection |
| `WenzlQmnSynergyContext` | `BraidsAndKnots/wenzl_qmn_synergy.lean:22` | **0** | self-assuming projection |
| `WedderburnBratteliRecursionContext` | `BraidsAndKnots/wedderburn_bratteli_recursion.lean:22` | **0** | self-assuming projection |
| `WenzlBranching` | `BraidKnot/QSchurWeightsGeneral.lean:51` | **0** | |
| `SpechtDimension` | `Hecke/Wedderburn.lean:54` | **0** | assumes `dim : ℕ`, `0 < dim` — weaker than a proved `dimIrrep`; see gap **F2-b** |
| `WedderburnDecomp` | `Hecke/Wedderburn.lean:72` | **0** | carries `trace_decomp` as a field — bean `qou-luq7` |
| `MarkovTrace` | `Hecke/MarkovTrace.lean:38` | — | |
| `markov_trace_unique_axiom` | `Hecke/MarkovTrace.lean:137` | **real `axiom`** | Markov-trace uniqueness, cited `[jones1987]`; consumed by the CONDITIONAL `markov_trace_unique` at :145. Being an `axiom` it **is** visible to `#print axioms` |
| `MyWedderburnClaim`, `WedderburnBlockDecompositionContext` | `Shared/WedderburnBlockDecomposition.lean:29,43` | **0** | the file contains **no theorems at all** |
| `MyBlockClaim`, `MarkovTraceContext` | `Shared/MarkovTraceClaim.lean:21,47` | **0** | |

### The arc's own class is the exemplar, not a defect

`IsOcneanuWeightSystem` (`QBeta/WenzlWeightVanishing.lean:376`) is how a §3b-cond
class should be written, and it is worth copying:

- It is deliberately **not** an `instance` — the source says so: *"Deliberately
  not an `instance`, so typeclass resolution can never use it to silently
  discharge an `[IsOcneanuWeightSystem …]` hypothesis."*
- It is **bracketed from both sides**. `isOcneanuWeightSystem_schurPrincipal`
  (:526) shows the hypothesis is satisfiable, so the conditional theorems are not
  vacuous; `not_isOcneanuWeightSystem_const_one` (:541) shows the constant
  function `1` fails it at `Q = 2` on `(1³)`, so the class genuinely constrains.
- The conclusion is **derived**, not projected: `y μ = 0 ↔ ℓ(λ) > r` comes from
  the class *plus* the unconditional `schurPrincipal_eq_zero_iff`, which is the
  §3b-cond item-5 non-degeneracy requirement.
- Its docstring states plainly what remains: *"Producing an instance for the real
  trace weights is exactly Wenzl's theorem, and is exactly what remains
  unformalised."*

### Three self-assuming projections

`y_lambda_recipe_from_partition.lean:49`, `wenzl_qmn_synergy.lean`, and
`wedderburn_bratteli_recursion.lean` each declare a `def` whose body is exactly a
context-class field:

```lean
def y_lambda_recipe_from_partition [ctx : YLambdaRecipeFromPartitionContext] :
    ∀ lam : ℕ, ctx.denom lam ≠ 0 ∧ ctx.y_lambda lam = ctx.num lam * (ctx.denom lam)⁻¹ :=
  ctx.claim_y_lambda_recipe_from_partition
```

The class field **is** the conclusion (§3b-cond item 5). These are labelled
honestly — *"the substantive mathematical content is carried by the context-class
axioms, and a full derivation from substrate primitives remains pending"* — so
they are ASSUMED rather than VACUOUS, but they prove nothing and must not be
cited as if they did. **No new bean** — they are already covered by epic
`qou-5p7n` ("125 of 147 self-assuming projections lack the disclosure sentence")
and `qou-q407`; the detector blind spot is `qou-24m2`.

### One contained laundering defect

`Mathlib/HeckeAlgebra.lean:151 instance triv_hecke` sets `carrier := PUnit`,
`hecke_relation := True`, `hecke_holds := True.intro`; `:166 instance
triv_wedderburn` does the same for `WedderburnDecomposition`. Both are registered
as **`instance`**, so typeclass resolution discharges those hypotheses for any
`R, n, q`, and the docstring admits the purpose: *"Discharges the §3b-cond
hypothesis at the audit level."* That is AGENTS.md §1a audit-dodging.

**Its blast radius is two, and both are in the same file.** A grep for
`[IwahoriHeckeAlgebra` / `[WedderburnDecomposition` / `[WenzlBridge` across all of
`QOU/` returns 2 hits total, both inside `Mathlib/HeckeAlgebra.lean` itself. So
this is a self-contained defect and **not** ten silently-laundered modules. It
should be fixed, and it should not be inflated. Bean `qou-a4dr`.

`Mathlib/WenzlBridgeConcrete.lean` (93 theorems) is unaffected — it is explicitly
*"independent of the abstract `HeckeAlgebra.lean` class hypotheses"* and computes
scalar values in `ℝ`.

## CONDITIONAL — both of them

| Declaration | `file:line` | Hypotheses |
|---|---|---|
| `conventionD_ocneanuWeight_ne_zero_of_two_rows_of_wenzl` | `QBeta/WenzlWeightVanishing.lean:500` | `[IsOcneanuWeightSystem (q^2) z r y]` |
| `markov_trace_unique` | `Hecke/MarkovTrace.lean:145` | `[HeckeAlgebra]`, `[MarkovTrace]` + `markov_trace_unique_axiom` |

## The gap list, scoped to the two fronts

### Front 2 — all-`n` corank. Not one hole; three.

The target is `dim radical = n! − Σ_{ℓ(λ)≤2}(dim V_λ)²`, then that the sum is
`Catalan(n)`. The three ingredients come apart cleanly:

**F2-a — Gram diagonal in the Wedderburn basis with entries ∝ `y_λ`. PARTLY
PROVED; the bridge is the hole.** `QBeta/MarkovGramDegenerate.lean` has, proved
and generic: `gram (tau) (b) : Matrix ι ι R` (:113), `wedderburnGram y :=
Matrix.diagonal y` (:316), `IsLive y i := y i ≠ 0` (:326), `wedderburnGram_det`
(:330), `_det_eq_zero_of_dead` (:341), `_det_ne_zero_iff_all_live` (:360),
`_restrict_live_det_ne_zero` (:377), and the rank bounds `gram_rank_add_le_card`
(:256) / `gram_rank_le_card_sub` (:278).

**What does not exist is any theorem connecting `gram tau b` to `wedderburnGram
y`** — i.e. that the Markov-trace Gram matrix in the Wedderburn basis *is*
diagonal with entries `y_λ`. That statement is precisely `tr_M = Σ_λ y_λ χ_λ`,
which the corpus carries as a **class field**, not a theorem: bean `qou-luq7`,
`Hecke/Wedderburn.WedderburnDecomp.trace_decomp`. Size: this is the arc's real
structural debt, not a lemma. Mathlib has nothing.

**F2-b — `dim V_λ`. PROVED, but on the wrong type.** `Partition.dimIrrep :=
Nat.factorial n / Λ.hookProduct` (`BraidKnot/DeltaLambdaSignRule.lean:130`) with
`dimIrrep_eq_numSYT` proved sorry-free at `BraidKnot/PartitionHookProductBridge.lean:163`
(the ℕ-division is exact, witnessed by `numSYT_mul_hookProduct_partition`). So the
hook-length dimension **is** available and **is** tied to the standard-tableau count.

The catch is a type collision, and it is the §"grep the claim SHAPE" hazard
exactly: `dimIrrep` lives on `QOU.BraidKnot.DeltaLambdaSignRule.Partition`
(`:46`), while `SpechtDimension` — the class that *assumes* a dimension exists —
is stated over a **different** local `structure Partition`
(`Hecke/Wedderburn.lean:45`). `DeltaLambdaSignRule`'s own docstring already warns
of a third collision with `QOU.BraidKnot.Partition`. So `SpechtDimension` cannot
be discharged from `dimIrrep` without a type bridge; today an *assumption* stands
where a *proof* is two files away. Size: small-to-medium, and it is a pure
plumbing job. Bean `qou-0pe3`.

**F2-c — `Σ_{ℓ(λ)≤2}(dim V_λ)² = Catalan(n)`. GENUINELY OPEN, already
catalogued.** This is item **G5** of bean `qou-0cyu`. `Mathlib/BallotNumbers.lean`
defines `ballot n j = C(n,j) − C(n,j−1)` (the SYT count of the two-row shape
`(n−j, j)`) and proves the engine `ballot_succ_succ` and the crux
`ballot_boundary_zero` sorry-free — but the identity itself only at **n = 3, 4,
5** (`ballot_sq_sum_catalan_small`, :139), against Mathlib's own `catalan`. The
general `n` is open: by RSK it says 321-avoiding permutations are Catalan, and
Mathlib has `catalan` but neither RSK nor pattern avoidance. Two routes are
already costed in `qou-0cyu`: (a) formalise enough RSK — LARGE; (b) direct
induction on the ballot recursion — MEDIUM, and to be tried first.

A related bean needs re-checking before anyone starts: `qou-9ojy` ("WIRE: burnside
bridge (1) dimIrrep=numSYT") appears **stale** — `dimIrrep_eq_numSYT` is proved
sorry-free on `main` at `9c6e9834cb`.

Note that `TemperleyLiebTower.catalan_three/_four/_five` (`1²+2²=5`, `1²+3²+2²=14`,
`1²+4²+5²=42`) and `MarkovGramDegenerate.corank_three/_four/_five` are **numeral
arithmetic** — the dimensions appear as literals, so they carry no partition
content and are not partial evidence for the general identity.
`ballot_sq_sum_catalan_small` is strictly stronger: it *computes* the dimensions
from `ballot` and compares against Mathlib's `catalan`.

**F2-d — `Σ_λ (dim V_λ)² = n!`. OPEN, and easy to miss.** `corank_blockDiagonal`
below yields `(∑_λ d λ²) − ∑_{live} d λ²`. Turning the first term into the `n!`
the arc quotes is the Burnside/RSK identity `Σ_λ (dim V_λ)² = n!`, which is *not*
proved here: `qou-r0jg` (milestone, "HLF-gated; dimension side proved") and
`qou-oh6k` carry it. Front 2 therefore needs **two** separate sum evaluations —
`n!` on the left (F2-d) and `Catalan(n)` on the right (F2-c) — and neither is
available. Both are needed only to *evaluate*; neither is needed to *state*.

**So: is Catalan the only hole? No.** But the answer to the second half is yes —
**the corank is statable at all `n` with the sum kept symbolic**, and that is now
done on this branch (below).

### Front 3 — discharge Wenzl 1988 through `TL_n`

The costed cheap route is to prove only the **vanishing set** through `TL_n`,
skipping the symmetric-function stack, since downstream consumes the vanishing
set and not the weight values. Given what exists, that route needs:

1. **A `TL_n` object.** `qou-0cyu` item **G3**: Temperley–Lieb is not in Mathlib
   at all, and this tree has no algebra-level `TL_n` either — `Knots/KauffmanTL3.lean`
   is `n = 3` with 43 definitions, and `QBeta/TemperleyLiebTower.lean` (1027 lines,
   48 theorems) is about the *trace* and the *tower*, not a carrier. Sized LARGE in
   `qou-0cyu`, and that sizing still holds.
2. **The vanishing set itself, which is already there.** This is the good news
   and it is why the cheap route is cheap. `MathlibExt/TLContentStratification.lean`
   proves, sorry-free, `schurElement_tl_ne_zero_iff_numCols_le` (:135),
   `_eq_zero_iff_numCols_gt` (:143) and `_ne_zero_iff_length_le` (:151) — the
   vanishing set characterised by column count and by row count. `QBeta/WenzlWeightVanishing.lean`
   proves `schurPrincipal_eq_zero_iff` (:185) **unconditionally**, and
   `conventionD_weight_eq_zero_iff_rowLens` (:250) and
   `conventionD_weight_ne_zero_of_two_rows` (:259) likewise.
3. **The bridge from the `TL_n` carrier to that set** — which is the whole of
   item 1's cost.

So front 3's cost is dominated entirely by constructing `TL_n`; the vanishing-set
half is already proved and unconditional. What Wenzl 1988 supplies and this tree
does not is an *instance* of `IsOcneanuWeightSystem` for the real Markov-trace
weights — which the class docstring already identifies as the residual debt.
Whether `TL_n` is worth building is a decision, not a default; `qou-0cyu` says the
same about G3.

## Filled on this branch

`QOU/MathlibExt/BlockDiagonalCorank.lean` — `lean`-direct exit 0, sorry-free,
`#print axioms` on all four declarations reports `[propext, Classical.choice,
Quot.sound]` (no `sorryAx`). Generic `[Field R]` per §7c; **no Hecke algebra, no
Markov trace, and no conjecture class appears in any statement**.

| Declaration | Statement |
|---|---|
| `card_blockIdx` | `Fintype.card (Σ λ, Fin (d λ) × Fin (d λ)) = ∑ λ, (d λ)^2` |
| `card_live` | live basis elements `= ∑_{y λ ≠ 0} (d λ)^2` |
| `corank_blockDiagonal` | `card − (Matrix.diagonal (blockConst d y)).rank = (∑ λ, d λ²) − ∑_{y λ ≠ 0} d λ²` |
| `corank_eq_of_live_iff` | the same against any vanishing criterion `P` — for convention D, `P λ = (ℓ λ ≤ 2)` |

This is the general-`n` skeleton that `corank_three/_four/_five` are numeral
instances of, and it answers the "statable without Catalan" question
affirmatively: `corank_eq_of_live_iff` leaves the surviving sum symbolic, so F2-c
is needed only to *evaluate* it, never to state it. The file includes a check that
the general statement reproduces `corank_three`'s `6 − (1²+2²) = 1` from the block
data `d = ![1,2,1]` rather than from a literal.

It does **not** close F2-a: it assumes the Gram form is block-constant diagonal,
which is what `qou-luq7` says is class-carried. That assumption is a hypothesis of
the statement, not a hidden one.

## Bean ledger for this survey

| Bean | State | Covers |
|---|---|---|
| `qou-a4dr` | **new** | the `triv_hecke` / `triv_wedderburn` PUnit instances |
| `qou-0pe3` | **new** | F2-b, the `SpechtDimension` / `dimIrrep` type bridge |
| `qou-luq7` | existing | F2-a, `tr_M = Σ y_λ χ_λ` carried as a class field |
| `qou-0cyu` G5 | existing | F2-c, the Catalan identity at general `n` |
| `qou-0cyu` G3 | existing | front 3's `TL_n` carrier |
| `qou-r0jg`, `qou-oh6k` | existing | F2-d, `Σ_λ (dim V_λ)² = n!` |
| `qou-5p7n`, `qou-q407`, `qou-24m2` | existing | the three self-assuming projections |
| `qou-fpjy` | existing | why `#print axioms` cannot see any of the class-carried inputs above |

Every ID above was resolved with `beans show` before being written here.
