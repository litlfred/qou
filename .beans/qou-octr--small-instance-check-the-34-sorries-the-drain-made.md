---
# qou-octr
title: Small-instance check the 34 sorries the drain made visible — never reported by any build
status: in-progress
type: task
created_at: 2026-08-09T09:57:23Z
updated_at: 2026-08-09T09:57:23Z
---


## What the drain exposed, measured

Recomputed the pre-drain import closure from `QOU.lean` (that is exactly what
`lake build` covered before the glob widened):

| | count |
|---|---|
| modules in tree | 1692 |
| reachable from `QOU.lean` | 870 |
| **outside — never compiled** | **822** |

Of the 37 modules the build now reports `sorry` in, **26 were outside** that
closure. **34 sorries had never been reported by any build**, and they carry 51
`-- Ref:` citation lines between them — i.e. they look audited.

## Finding: three of them are not open gaps, they are ill-posed

Machine-checked refutations, all compiling clean:

```lean
theorem mass_categorical_descent_unconstrained_false :
    ¬ ∀ ctx : MassCategoricalDescentContext, ctx.B = ctx.B_desc + ctx.B_trans
theorem np_splitting_unconstrained_false :
    ¬ ∀ ctx : NeutronProtonSplittingContext,
        ctx.m_n - ctx.m_p = ctx.α * |ctx.Φ_udd - ctx.Φ_uud|
theorem cascade_depth_unconstrained_false :
    ¬ ∀ ctx : QTurbulenceSpectrumContext,
        (ctx.N_modes : ℝ) ≤ 3/4 * Real.log ctx.Re_q / Real.log ctx.q
```

Each is refuted by an instance that simply picks disagreeing numbers —
`B := 0, B_desc := 1, B_trans := 0`; `m_n := 1` with everything else `0`;
`q := 2, N_modes := 1000000`. No junk values needed, no cleverness.

**This is a distinct defect from the two the skill already covers.** Not §1
(the class carrying its own conclusion and the theorem projecting it) and not
§9 (a statement admitting a degenerate input the textbook excludes). Here the
class carries **neither the conclusion nor any hypothesis relating the fields
the conclusion mentions**, so there is nothing to derive from and the `sorry`
**can never be discharged** — discharging it would prove something false.

AGENTS.md §3b-cond item 5 already requires exactly what is missing: *"the class
axiomatises hypotheses, not the conclusion... the theorem must **derive** its
conclusion from them."* The rubric's own verified exemplar,
`QOU/FluidDynamics/q_bkm_criterion.lean`, shows the shape that works —
`QBKMContext` carries the two directions as **implications**
(`vorticityIntegralFinite → extendsSmoothly` and its converse) and the theorem
composes them with `Iff.intro`, sorry-free. `MassCategoricalDescentContext`
carries four bare `ℝ` and asserts a relation among them.

So item 5 has been read as forbidding only one direction (class carries too
much). These fail it in the other direction: the class carries too little.

## Prevalence: unknown, and the syntactic route does not work

I tried twice to count how widespread this is and both attempts were wrong:

1. Flagging junk-value smells by regex — matched doc-comment slashes, returned
   26/33, useless.
2. Flagging classes whose fields are all bare data — returned 1 of 11, but
   `mass_categorical_descent` **has** a hypothesis field and is still
   refutable, because that field does not mention `B`, `B_desc` or `B_trans`.

The property that matters is *"do the class's hypotheses constrain the fields
the conclusion mentions"*, and that is not a grep. **The reliable test is to
construct an adversarial instance** — the small-instance check of §9,
generalised from "instantiate the parameter" to "instantiate the class". It
takes about two minutes per statement and either compiles or does not.

So: 3 confirmed. The other 31 are unaudited, not cleared.

## Not done here

The three refutations are **not committed into the content files**. Fixing
these means adding the missing hypotheses to each context class — a claim
change, and the author's call, exactly as with qou-zzhw. What is offered here
is the diagnosis plus a proof for each that the current form is unclosable.
