---
# qou-fpjy
title: 'Class-carried external inputs are invisible to #print axioms and the vacuity audit'
status: todo
type: task
priority: normal
tags:
    - lean
    - audit
    - honesty
created_at: 2026-08-16T12:55:03Z
updated_at: 2026-08-16T12:55:03Z
---

## What PR #5230 surfaced

#5230 axiomatised Wenzl (1988) as a Lean class,
`QOU.QBeta.WenzlWeight.IsOcneanuWeightSystem`, threaded as an `[Instance]`
hypothesis into the statements that depend on it (AGENTS.md §3b-cond).

Then `#print axioms` was run on all 20 declarations in the file. **Every one
returned the same three axioms:**

```
'…schurPrincipal_eq_zero_iff'                 [propext, Classical.choice, Quot.sound]   -- unconditional
'…ocneanuWeight_eq_zero_iff_of_wenzl'         [propext, Classical.choice, Quot.sound]   -- conditional on Wenzl
'…conventionD_ocneanuWeight_eq_zero_iff_of_wenzl' [propext, Classical.choice, Quot.sound] -- conditional on Wenzl
```

The conditional and the unconditional declarations are **indistinguishable** in
the axiom report. That is correct behaviour — a class hypothesis is a binder,
not an axiom, so nothing is being hidden from the kernel — but it means the
repo's axiom-facing tooling cannot see this class of dependency at all.

## Why this matters here specifically

The repo leans on `#print axioms` as the honesty gate. AGENTS.md §Phase-4
verification gate requires *"`#print axioms` on the new declarations showing no
`sorryAx`"* — which these pass, truthfully, while still depending on an
unformalised published theorem. `lean-vacuity-axiom-audit.ts` likewise keys on
`sorry` / `axiom` / trivial-true / empty-carrier patterns; a **content-bearing
class carrying a cited external theorem** matches none of them.

So the corpus can accumulate `[SomeExternalTheorem]`-conditional results with no
enumerable inventory of which external inputs are load-bearing and where. Today
that inventory is: read the docstrings.

This is NOT an argument for using `axiom` instead — see #5230's rationale
(an axiom can never be discharged, and would have to be stated at a fixed
instantiation or over a Hecke formalisation the repo lacks). The class is the
right construct; the **tooling** is what is missing.

## Note the existing machinery is close but does not cover it

`lean-vacuity-axiom-audit.ts` already computes a `conjecture_graph` by
classifying carriers primary vs dependent over `[Instance]` binders (AGENTS.md
§3b-tax). That is exactly the right mechanism — it walks instance binders
already. What it does not do is distinguish a carrier that encodes an **open
conjecture of this framework** from one that encodes a **published theorem
nobody has formalised**. Those have different dispositions: the first is a
research target, the second is a formalisation target.

## Tasks

- [ ] Introduce a marker distinguishing the two — e.g. a docstring convention
      `@external-input: [wenzl1988]` on the class, parallel to the existing
      `@conjecture: primary` / `@marker` conventions.
- [ ] Extend `lean-vacuity-axiom-audit.ts` to emit an **external-input
      inventory** alongside `conjecture_graph`: for each such class, the
      citation key and the transitive set of declarations whose signatures
      carry it. That set is the honest scope of "conditional on <paper>".
- [ ] Require the citation key to resolve in `content/schema/references.ts`
      (same rule as `-- Ref:` on a `sorry`, §1).
- [ ] Decide whether the Phase-4 verification-gate wording should require
      reporting external-input classes alongside `#print axioms`, since the
      latter provably does not show them.
- [ ] Seed the inventory with the known instances. `IsOcneanuWeightSystem`
      (`[wenzl1988]`) is one; sweep for others — the pattern predates #5230,
      e.g. `S5bbClosure` in `QOU/BraidKnot/S5bbGeometricIndex.lean` sits over
      `opaque` declarations and is worth classifying.

## Scope note

Nothing here is a refutation and no existing result is called into question.
This is a **visibility** gap in the audit surface, of exactly the kind AGENTS.md
§"QA is agent-owned" anticipates: a standalone library `.lean` file has no
`.qa.json` sidecar, so nothing but an agent's own reading covers it.

Surfaced by PR #5230; see `docs/audits/2026-08-16-ocneanu-weight-axiomatisation.md`.
