# The `Prop`-field convention inverts the implication it is written to express

**Measured 2026-09-03 on `origin/main`, 2552 `.lean` files, with
[`scripts/lean-cited-not-proved-audit.py`](../../scripts/lean-cited-not-proved-audit.py)
(`--kind prop-field`).** Third correction to the same count; see the
count-history section at the end before quoting any number here.

## The claim

Across the corpus a recurring encoding is used for a *stated implication*:

```lean
class C where
  X       : Prop            -- the antecedent, named but not stated
  h_X     : X               -- ...and its witness, supplied by the class
  impl_t  : X → Q           -- "X forces Q"

theorem t [ctx : C] : Q := ctx.impl_t ctx.h_X
```

**This is inhabitation-equivalent to a single field `: Q`.** Take `X := True`
and `h_X := trivial`; the instance must then supply `Q` outright. So the
antecedent is *free*, the implication conveys nothing beyond its consequent, and
a docstring reading *"X forces Q"* is, in the Lean, *"Q"*.

That is the defect. It is **not** that the field is typed `Prop`.

## The measurement

| | count |
|---|---|
| `Prop`-typed fields, corpus-wide | 95 |
| **parameterised** — the `Prop` is a component of another field's statement | 56 |
| **self-nominating** — a companion field's type *is* the `Prop` field | 39 |
| — **consumed**: a proof term projects the witness → **the defect** | **24** |
| — unconsumed: an open input carried as an input → honest §3b | 15 |

Only the 24 are actionable. The 56 are legitimate (an abstract predicate used as
a parameter of a relation — the same move as taking `(P : α → Prop)` as an
argument), and the 15 are the honest conjecture-class pattern.

## The two discriminators, and how each was found

Both came from a **false positive on a file opened intending to fix it**. That is
worth stating plainly: in each case the detector's own output would have produced
work that damaged a correct file, and only reading the file stopped it.

**parameterised vs self-nominating** — from
`QOU/Archimedean/noble_gas_characterization.lean`, whose header says outright
that both sides are abstract `Prop`s at this stage. Its `IsNobleGas` and
`IsFullOfCurls` are parameters of the relation `claim_noble_iff_curls`; an
instance choosing `True` for both still has to make the iff hold.

**consumed vs unconsumed** — from `QOU/BraidKnot/BringWPlaneMonodromy.lean`,
which is exemplary. Its

```lean
is_seifert_gauss_manin : Prop
seifert_holds : is_seifert_gauss_manin
```

is self-nominating, yet the proposition is a deliberately-abstract *geometric
identification* — the open half of a numerology-guarded §3b conjecture — and the
file's theorem `monodromy_satisfies_recurrence` derives from the content-bearing
`unimodular : M.det = 1` via the proved `unimodular_two_recurrence`, explicitly
**not** from the witness. Carrying an open input as an input is exactly right.

## What a mechanical collapse would and would not do

Collapsing `X : Prop` + `h_X : X` + `impl : X → Q` to a single field `: Q` is a
faithful simplification: it changes nothing logically. It therefore **closes no
gap**, and doing it as a bulk pass would be AGENTS.md §1a audit-dodging.

It is not, however, detector-destroying: `scripts/lean-self-assuming-audit.py`
has a class-field mode that flags `class field ctx.f : T ⊢ T`, so a collapsed
carrier lands in *that* population (11 corpus-wide at the time of writing, over 8
files **disjoint** from these 22). The signal moves; it does not vanish. A
collapse is defensible as a legibility fix and must be reported as one — never as
progress on derivation.

## What actually closes one

A proved upstream lemma to build on. That is what made
`QOU/LiftingDescent/tm_eigenspace_decomp.lean` tractable: the *splitting* it had
been assuming is `QOU.LiftingDescent.JetChain.decomposition`, proved in
`JetProlongation` from the retraction identity, so the class was left carrying
only the two genuinely-open inputs — as equations in its own data, neither
dischargeable by `trivial`.

Files checked and **rejected** as targets, with the reason:

| file | why not |
|---|---|
| `QOU/Mathlib/NonAbelianStokes.lean` | its own docstring names the carrier self-certifying and says genuine models await a Mathlib Lie-valued-forms library. PR #6512 established Mathlib has none. |
| `QOU/Torsion/MassGap.lean` | `impl_witness : mass_gap_holds → YangMillsMassGap` already forces a content-bearing structure with real inequalities; collapsing is logically identical. |
| `QOU/FluidDynamics/qou_ns_in_qou.lean` | scrupulously scoped under an owner directive. See the note below — its prose outruns its Lean in one place, which is worth reporting, not silently reshaping. |

## The sharpest instance: cited, not proved

`QOU/AppendixSurreals/B1TorusKnotRowsTheorem.lean` carries

```lean
bloch_suslin    : Prop
garoufalidis_le : Prop
```

with witnesses fed straight into `b1_from_tate_rationality` to yield the
theorem's conclusion. **Two named literature results — Bloch–Suslin, and
Garoufalidis–Lê on Tate-rationality of the Chern–Simons invariant of torus
knots — are laundered through opaque `Prop`s.** The conclusion's predicate
`b1_holds : ℕ → ℕ → Prop` is itself an instance-chosen parameter, so an instance
takes `b1_holds := fun _ _ => True` and the theorem is fully vacuous.

This is the literal answer to *"what is only cited and not Lean-proved"*, and it
is **not fixable here**: neither result is in Mathlib, and neither is derivable
from the corpus.

## One place where prose outruns Lean

`qou_ns_in_qou.lean` states in prose: *"There is no NS-regular QOU: a `χ = 0`
(regular) object has `NS(A) = 0`, which violates observability, so it is a
quantum universe but not a quantum observable universe."* The converse
`χ = 0 → NS(A) = 0` is **not** in the Lean, and the file's `observability : Prop`
+ free witness means `observability_forces_chi` is equivalent to asserting
`eulerChar ≠ 0` — `descartesQOU` literally sets `observability := True`. Steps 2
and 3 of its chain *are* genuine implications between content-bearing data; step
1 is not. Reported, not changed: the file is under an explicit owner directive
(2026-07-24) and its scope discipline is deliberate.

## Count history — do not quote a number without its date

| when | claim | what was wrong |
|---|---|---|
| #6491 | "96 `Prop`-valued fields", one defect class | two shapes wear the same syntax |
| #6530 | 39 self-nominating + 56 parameterised | a self-nominating field nothing projects is not a defect |
| #6543 (this) | **24 consumed** + 15 unconsumed | — |

Two further corrections fell out of the third pass, in **opposite** directions.
All eleven `QOU/Mathlib/HeckeAlgebra.lean` fields are *unconsumed*, so the
`qou-ar7f` shadow-trio decision blocks no `Prop`-field work and gains no urgency
from it. And the actionable count is 24, not the 28 obtained by subtracting those
11 — **higher**, because the unconsumed fields are spread over three files rather
than concentrated in one.

Tracked on `qou-tsnp` (the canonical bean for this defect class, open since
2026-08-09) and `qou-ar7f`.
