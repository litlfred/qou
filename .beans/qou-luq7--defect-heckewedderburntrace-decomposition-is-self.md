---
# qou-luq7
title: 'DEFECT: Hecke/Wedderburn.trace_decomposition is SELF-ASSUMING -- tr_M = sum y_lambda chi_lambda is a class FIELD, and the class has no instance'
status: todo
type: task
priority: normal
created_at: 2026-08-09T18:03:43Z
updated_at: 2026-08-24T20:03:10Z
---


Branch: claude/anchor-followups-2026-08-08. Found while executing the owner's
"lean prove y_lambda is the Wedderburn weight of the Markov trace --
tr_M = sum_lambda y_lambda chi_lambda", which turns out to be ALREADY STATED on
main and NOT proved.

## THE DEFECT

content/quantum-observable-universe/lean/QOU/Hecke/Wedderburn.lean (merged in
PR #4857, now on main):

    theorem trace_decomposition (x : A) :
        MT.trace x = WD.all_parts.sum (fun lam =>
          WD.y_lambda lam . MT.trace (x * WD.pi_lambda lam)) := by
      exact WD.trace_decomp x

`trace_decomp` is a FIELD of `class WedderburnDecomp`. The theorem projects the
field. It derives nothing.

This is EXACTLY the defect shape PR #4857's OWN Part 1 named and refuted
nineteen times:

    #1 self-assuming | the class carries the CONCLUSION, as a field |
                       theorem projects it; proves nothing

and it is what AGENTS.md section 3b-cond item 5 forbids: "the class axiomatises
hypotheses, not the conclusion ... the theorem must DERIVE its conclusion from
them."

AND THE CLASS HAS NO INSTANCE. `grep "instance.*WedderburnDecomp"` across the
tree returns nothing. Ten modules take `[WedderburnDecomp ...]` as a hypothesis,
so every downstream consequence is conditional on an uninhabited class whose key
field is the thing to be shown.

## WHAT THE CLASS ALREADY HAS, AND WHAT IT SHOULD HAVE HAD

It already carries `complete : sum_lambda pi_lambda = 1`. And its own docstring
states, in PROSE, the fact that actually does the work:

    "The Markov trace's restriction to each block is the matrix trace scaled by
     the central coefficient y_lambda."

THAT SENTENCE IS NOT ENCODED AS A FIELD. Encode it and the weighted
decomposition follows in four lines from completeness, additivity of the trace,
and right-distributivity -- no Schur orthogonality, no Mathas section 3.43, no
representation theory at all.

## PROVED, in my own territory, so nobody has to wait on this bean

QOU/QBeta/WedderburnTraceDecomposition.lean (NEW). Sorry-free, axioms
[propext, Quot.sound] only -- not even Classical.choice. Three statements in
increasing strength, and reading them in order is the whole argument:

  trace_eq_sum_blocks              completeness ALONE gives the UNWEIGHTED
                                   tr x = sum_lambda tr(x pi_lambda). Free.
  trace_decomposition_of_blocks    naming the block terms
  trace_eq_sum_weighted_characters WITH hblock : tr(x pi_lambda)
                                     = y_lambda * chi_lambda(x),
                                   the target identity. DERIVED.

So the weights do NOT come from completeness -- which is why assuming the
conclusion was never necessary -- and are NOT free either -- which is why the
honest axiom is the block scaling.

Everything is on a bare AddMonoidHom and an arbitrary index Finset: no Hecke
algebra, no partitions, no q, no convention. It applies to the merged
WedderburnDecomp unchanged.

## THE FIX ON THEIR SIDE (their file, do not edit unilaterally)

  [ ] 1. Add to WedderburnDecomp a field
             block_scaling : forall lam x, MT.trace (x * pi_lambda lam)
                               = y_lambda lam * chi lam x
         (with chi the block character), and DELETE `trace_decomp`.
  [ ] 2. Reprove trace_decomposition from complete + block_scaling, citing
         QBeta.WedderburnTraceDecomposition.trace_eq_sum_weighted_characters.
         It is a four-line proof.
  [ ] 3. Separately: the class still has no instance. That is the larger debt
         and it is theirs -- Wedderburn-Artin existence plus Schur uniqueness.
  [ ] 4. Coordinate on litlfred/qou#4857's successor before touching
         QOU/Hecke/**. See docs/coordination/hecke-tower-and-trace-parameter.md.

## WHAT IS STILL NOT PROVED, and I will not claim otherwise

Existence of the y_lambda and chi_lambda, and their uniqueness. Existence is
Wedderburn-Artin; uniqueness is Schur orthogonality (Mathas 1999 section 3.43),
not in Mathlib. Both remain open.

What IS settled: the summation identity is not an independent axiom. It was
never the thing that needed assuming.


## 2026-08-24 — the self-assuming half is FIXED; the instance half is not

`trace_decomp` is gone. `QOU.Hecke.WedderburnDecomp.trace_decomposition` is now
a derivation from `complete` (via `trace_exhaustive`) plus a new `block_scaling`
field, and neither input is the conclusion. Commit `722761c0eb`.

### The defect was worse than "self-assuming", and that is machine-checked

`trace_exhaustive` already **derived** `tr_M(x) = Σ_λ tr_M(x·π_λ)` from
`complete` alone, in the same file. `trace_decomp` **assumed**
`tr_M(x) = Σ_λ y_λ · tr_M(x·π_λ)` — the same terms, weighted. Subtracting them
is a constraint on the weights:

```
weights_inert                  Σ_λ (1 − y_λ) · tr_M(x·π_λ) = 0
weight_one_or_block_trace_zero (1 − y_μ) · tr_M(π_μ) = 0
```

Both sorry-free, in commit `9e8b712fa2`, where they can still be run.

**So the class was uninhabitable in its intended regime** — not uninhabitable
outright (all `y_λ = 1` satisfies it, as does a trivial algebra), but
uninhabitable with the nontrivial `y_λ` its own `y_lambda` docstring specifies
(*"a rational function in q given by `s_λ(1,Q,…)/Σ d_μ s_μ(…)`"*) and nonzero
block traces. That is a better explanation of "the class has no instance" than
"nobody got to it": **an honest instance could not be built.** It can now.

The encoding was at fault, not the mathematics. `tr_M(x) = Σ_λ y_λ · χ^λ(x)`
needs `χ^λ` to be the *block character*; `trace_decomp` substituted
`tr_M(x·π_λ)` for it, which already carries `y_λ`, and so applied the weight
twice.

### What is left of this bean

The instance. `qou-0cyu` names the route — Mathlib's
`exists_algEquiv_pi_matrix_divisionRing_finite` plus `IsHeckeOfFullRank`
(finrank = n!) — and that route is now unobstructed. Leaving this `todo` for
that half rather than closing on the half that is done.
