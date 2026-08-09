---
# qou-k6ks
title: S-polynomial reduction needs R to have no quasi-zeros (Lei-Pawlowski); check the QOU assumption is stated and used
status: todo
type: task
priority: normal
created_at: 2026-08-09T16:22:40Z
updated_at: 2026-08-09T16:23:35Z
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
