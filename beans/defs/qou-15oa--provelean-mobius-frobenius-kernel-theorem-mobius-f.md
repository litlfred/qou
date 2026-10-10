---
# qou-15oa
title: 'PROVE(lean): mobius_frobenius_kernel — theorem mobius_frobenius_kernel {E : Type*} [NormedAddCommGroup E] [ctx : MobiusFrobeniusK [cited manuscript]'
status: completed
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:04Z
updated_at: 2026-10-04T15:13:34Z
parent: qou-k1mq
---

**File:** `QOU/BraidsKnots/mobius_frobenius_kernel.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/BraidsKnots/mobius_frobenius_kernel.lean

### `mobius_frobenius_kernel`  —  line 82  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem mobius_frobenius_kernel {E : Type*} [NormedAddCommGroup E] [ctx : MobiusFrobeniusKernelContext E] (s t : ℝ) (_hst : ctx.γ s ≠ ctx.γ t) : Filter.Tendsto (fun q => ctx.K_FH q s t) (nhdsWithin 1 {q : ℝ | q ≠ 1}) (nhds (1 / ‖ctx.γ s - ctx.γ t‖ ^ 2)) `
- **Cited:** `[manuscript]`, `[manuscript]`
  - [manuscript] lem:mobius-energy-frobenius-kernel,
- **Tractability:** q→1 limit (Tendsto) of the Möbius–Frobenius kernel over a context; real-analysis over context class, repo-internal.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.


## THE BEAN WAS STALE, AND WHAT IT NAMED IS A DIFFERENT DEFECT (2026-09-13)

This bean says "1 cited sorry(s)" and "Blocked on in-repo scaffolding". Both
are wrong, and the second is wrong in a way that matters.

THERE IS NO SORRY, and there never was. The theorem's body is
`ctx.classical_limit s t hst`; `#print axioms` reports no `sorryAx`. The file's
own docstring recorded this correction on 2026-09-03 and the bean was never
updated.

WHAT IT ACTUALLY WAS: a self-assuming projection, AGENTS.md section 3b-cond
item 5. `classical_limit` was a class field stating the theorem's conclusion
verbatim, with the same binders, and the theorem projected it. The class
docstring read "All fields are inputs; none is the conclusion" while the
conclusion was field three of three.

NOT "blocked on scaffolding". Nothing was missing; the file assumed its
conclusion and said it did not.

## WHAT WAS DONE

The class now carries the TWO reductions the theorem's own docstring says the
proof requires, neither of which is the conclusion:

  kernel_tendsto_killing      the q-Hodge star reduces to the classical one,
                              so the q -> 1 limit EXISTS and is the Frobenius
                              pairing's classical kernel. Limit point is the
                              abstract killingKernel, not the target value.
  killing_eq_inverse_square   the Frobenius pairing reduces to the SU(2)
                              Killing form, which evaluates to 1/r^2. A
                              pointwise identity; no limit in it.

and the theorem DERIVES: rewrite the target through reduction 2, discharge
with reduction 1. Plus `inverseSquareContext` and
`nonempty_mobiusFrobeniusKernelContext` — because qou-z9ws fixed the
discriminator that a projection is the legitimate accessor idiom ONLY when
something builds the bundle, and every one of the twelve it sampled was
uninhabited.

4/4 declarations [propext, Classical.choice, Quot.sound], 0 sorryAx, 0 sorry
or axiom in the file, lean -DautoImplicit=false -s 65536 exit 0 against the
real import cone.

STATED PLAINLY, because it is the obvious objection: the CONJUNCTION of the two
new fields is equivalent to the old single field. Splitting an assumption does
not discharge it and this file still proves no analysis. What improves is that
the obligation is LOCALISED onto the two named unformalised reductions, and
that the theorem derives rather than projects.

One thing did get stronger. Sections 7-8 of QOU.MobiusMutualChannel (merged
2026-09-13, ea1220654e) prove the inverse square is the UNIQUE Mobius-invariant
separation kernel, on unconstrained and on geometrically realisable triples
both. So killing_eq_inverse_square now asserts the Killing form lands on the
kernel symmetry independently forces, rather than on a value chosen to match.

## AND THE DETECTOR NEVER REPORTED IT — bean qou-metc

Measured by stashing the change and re-running: the vacuity audit reports 0
defect candidates on that subtree BEFORE the fix as well as after. The body
shape `ctx.field arg arg arg` — an APPLIED single projection — matches none of
the detector's four patterns, so it returns before reaching its own structural
fallback. 16 further cases are invisible for the same reason (26 counted
becomes 42 with one regex added). Sized and written up as qou-metc; no detector
change made here.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] k1mq child: no real sorry left in target file. mobius_frobenius_kernel theorem uncond, 0 sorry | previously stalled; last update 2026-09-13
