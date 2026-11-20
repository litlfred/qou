---
# qou-k6ks
title: S-polynomial reduction needs R to have no quasi-zeros (Lei-Pawlowski); check the QOU assumption is stated and used
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T16:22:40Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-q4oa
---


The folio's own chapter states the hypothesis, in
`content/unital-groebner-bases/unital-groebner-bases-chapter/monomial-basis.md`:

> Throughout, $R$ is a commutative ring with unity and $A$ is an $R$-algebra
> **without quasi-zeros** (i.e. elements $a \in A$ such that $bac = 0$ for all
> $b, c \in A$ not both $1$).

and it is carried through every statement of the main theorem —
`ugb-main-theorem-statement.md`, `main-theorem.md`, `groebner-basis.md`,
`division-algorithm.md`, `remainder-module.md`, `remainder-modules.md`,
`unital-groebner-basis.md`. Source: Pawloski–Leitner, *Unital Gröbner Bases over
Arbitrary Commutative Ground Rings*, arXiv:math/0409565v2 (reference key
`leitner-pawlowski` in `content/schema/references.ts`).

## The gap

In Lean it appears **only in docstrings** — `UGB/UnitalGroebner/unital_groebner_decomposition.lean:23`
and `UGB/Introduction/main_theorem_statement.lean:24` — and never as a hypothesis
on any declaration. Worse, the framework that actually does the S-polynomial work,
`UGB/GrobnerShirshov/*`, does not mention it at all: `RewritingSystem`,
`OverlapComposition`, `InclusionComposition` and `IsGrobnerShirshovBasis` are
stated over a bare `[Ring k]` with no condition on the algebra.

That matters exactly where the user flagged it: the composition/S-polynomial
argument. A quasi-zero `a` satisfies `b·a·c = 0` for all `b, c` not both `1`, so
it is annihilated by every non-trivial context. Any argument that concludes "the
S-polynomial reduces to zero, therefore the corresponding overlap is resolved"
silently assumes no such element can make a reduction vacuous.

## Check, then fix

1. **Check**: enumerate every UGB declaration whose informal statement needs the
   hypothesis and whose Lean statement omits it. Start with the main-theorem
   chain (`unital_groebner_decomposition`, `main_theorem_statement`,
   `buchberger_theorem`, `ugb_pbw_corollary`, `s_poly_decomposition`) and the
   whole `GrobnerShirshov` framework.
2. **State it**: a `NoQuasiZeros` predicate —
   `∀ a : A, (∀ b c : A, ¬(b = 1 ∧ c = 1) → b * a * c = 0) → a = 0` — as a class
   or an explicit hypothesis, matching the chapter's wording exactly.
3. **Thread it** through the S-polynomial results that need it, rather than
   adding it everywhere.
4. **Discharge it** where the ground ring is concrete: over a field, and for the
   free associative algebra the GS framework works in.

## Interaction with qou-auq3

qou-auq3 is the repair of `leadingMonomial` / `SingleStepReduction` /
`OverlapComposition.spoly` needed before `hecke_is_gs_basis` can have a
non-vacuous proof. This hypothesis belongs in the *same* repair: a corrected
S-polynomial condition that is not degenerate is precisely where "no quasi-zeros"
starts doing work. Do not land the two separately — the corrected definitions
should carry the hypothesis from the start.

---

## 2026-08-09 — stated, threaded, discharged; and where it genuinely bites

Landed together with the qou-auq3 repair, as this bean asked. The corrected
S-polynomial definitions carry the hypothesis from the start.

### 1. Check — what omitted it

The audit confirms the bean: before this change **no** UGB declaration carried
the hypothesis; it appeared only in two docstrings
(`UnitalGroebner/unital_groebner_decomposition.lean:23`,
`Introduction/main_theorem_statement.lean:24`). The declarations whose
informal statement needs it are exactly those that route through the
S-polynomial half of the composition lemma:

| declaration | file | needs it? |
|---|---|---|
| `local_confluence` | `GrobnerShirshov/CompositionLemma.lean` | **yes** — this is the S-polynomial step itself |
| `confluence` | same | yes, via local confluence |
| `normal_form_unique` | same | yes, via confluence |
| `composition_lemma`, `retraction_property` | same | yes, via `normal_form_unique` |
| `buchberger` | `UnitalGroebner/buchberger.lean` | yes, via `confluence` |
| `pbw_corollary`, `main_theorem_statement` | `UnitalGroebner/`, `Introduction/` | yes, via `normal_form_unique` |
| `ugb_pbw_corollary` | `BuchbergerPBW/` | yes — discharged in place |
| `heckeCost_well_defined`, `threading_cost_unique` | `GrobnerShirshov/HeckeGS.lean` | yes — discharged in place for the second |
| `normal_form_exists`, `reduction_well_founded` | `Basic.lean`, `CompositionLemma.lean` | **no** — termination only, no composition reasoning |
| `unital_groebner_decomposition` | `UnitalGroebner/` | **no** — uses existence + `gs_implies_flat`, never uniqueness (its docstring mentions quasi-zeros; the Lean statement does not need it) |
| `buchberger_theorem` | `BuchbergerPBW/` | **no** — it is the definitional unfolding of `IsGrobnerShirshovBasis`, proved by `⟨hgs.overlap_resolves, hgs.inclusion_resolves⟩` |
| `descended_gs_inherited`, `jet_stratified_gs_criterion` | `GrobnerShirshov/JetOrder.lean` | **no** (judgement call) — they assemble the GS predicate out of resolution conditions rather than invoking confluence |

### 2. State — `Basic.lean` §7

Two forms, because `AlgElement G k` carries no `Ring` instance (there is no
general multiplication on it, only multiplication by monomials — see
`Elem.lean`), so the chapter's wording cannot be applied to the algebra the
framework actually works in without an instantiation:

```lean
def NoQuasiZeros (A : Type*) [Ring A] : Prop :=
  ∀ a : A, (∀ b c : A, ¬(b = 1 ∧ c = 1) → b * a * c = 0) → a = 0

def NoQuasiZerosFree (G : Type u) (k : Type v) [Ring k] [DecidableEq G] : Prop :=
  ∀ f : AlgElement G k,
    (∀ a b : Monomial G, ¬(a = [] ∧ b = []) →
      (AlgElement.contextMul a f b).isZero) → f.isZero
```

The first is the chapter's wording verbatim. The second is its instantiation
at the free algebra, with the contexts `b, c` taken to be monomials (which
span, so nothing is lost) and "not both `1`" reading as "not both the empty
word".

### 3. Thread — the results that need it

`local_confluence`, `confluence` and `normal_form_unique` (all three still
axioms) now take `(hnqz : NoQuasiZerosFree G k)` after `hgs`, and it is passed
through `composition_lemma`, `retraction_property`, `buchberger`,
`pbw_corollary`, `main_theorem_statement` and `heckeCost_well_defined`. It was
*not* added anywhere else — see the table above.

### 4. Discharge

* `noQuasiZeros_of_neg_one_ne_one : (-1 : A) ≠ 1 → NoQuasiZeros A` — take the
  context `(1, -1)`.
* `noQuasiZerosFree_of_generator (g : G) : NoQuasiZerosFree G k` — left
  multiplication by a single generator is injective, which is all the
  condition asks.
* Used at `ugb_pbw_corollary` (free algebra on `SU2Gen`, witness `SU2Gen.K`)
  and `threading_cost_unique` (`HeckeGen (n+1)`, witness `⟨0⟩`).

All `#print axioms`-clean (`[propext, Classical.choice, Quot.sound]`).

### 5. Honest limitation — where it would really bite, and why it cannot yet

`NoQuasiZerosFree` is **automatic for the free algebra as soon as there is one
generator**. It is not vacuous — it fails for `G` empty, where `k⟨G⟩ = k` has
no non-trivial context at all (and e.g. `NoQuasiZeros (ZMod 2)` is genuinely
false: every pair `(b,c) ≠ (1,1)` there has `b·c = 0`, so `1` is a quasi-zero)
— but in the setting the Lean framework models, the hypothesis records the
manuscript's standing assumption rather than constraining anything.

The reason is structural, and worth stating plainly: **Leitner–Pawloski's `A`
is the quotient algebra `R⟨X⟩/I`, and this development has no quotient at
all.** `UGB.GrobnerShirshov` works entirely in the free algebra — there is no
`AlgElement`-level ideal, no quotient type, and no statement that normal-form
monomials are an `R`-basis *of the quotient*. That is where a quasi-zero can
appear (the free algebra over a domain never has one) and where the hypothesis
does real work. Threading it through the free-algebra statements is correct
and is what the bean asked for; making it load-bearing requires the quotient,
which is a separate and much larger piece of work — the same missing piece
that keeps the "monomial basis of `A`" half of the main theorem informal.

### 6. Interaction with qou-auq3

Landed together, as required. Note the outcome there: with the repaired
definitions the Hecke system is **not** a GS basis (`hecke_not_gs_basis_four`),
so `heckeCost_well_defined`'s new `hgs` hypothesis is currently unsatisfiable
at `n = 4` — the "no quasi-zeros" hypothesis is not what is blocking the Hecke
route; the missing Bokut–Shiao completion is.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8467, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
