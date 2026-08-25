---
# qou-octr
title: Small-instance check the 34 sorries the drain made visible — never reported by any build
status: in-progress
type: task
priority: normal
created_at: 2026-08-09T09:57:23Z
updated_at: 2026-08-14T16:07:49Z
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

---

## Result: 8 of 8 context-class sorries are unclosable

Every `sorry` in the newly-visible set that is stated over a §3b context class
has now been attempted with the adversarial-instance method. **All eight are
refutable.** None is an open gap.

| declaration | class fields | what refutes it |
|---|---|---|
| `mass_categorical_descent` | 6, 0 constraining the conclusion | `B := 0, B_desc := 1, B_trans := 0` |
| `neutron_proton_splitting` | 5, all bare | `m_n := 1`, rest `0` |
| `finite_cascade_depth` | 9 | `q := 2, N_modes := 1000000` |
| `volume_perturbation` | 5 | `Vol_41 := 0, δΦ := fun _ => 1` |
| `skein_mass_from_linking` | 8 | `n := 0, Q := 0, mass := 1` |
| `parity_regime_selection` | 13 | `A := 1, sign_val := 0` (ℕ sub: `(-1)^(1-1) = 1`) |
| `lp_dual_stability` | 13, all bare | all-zero context; the `… < 0` conjunct |
| `confinement_frobenius_reciprocity` | 12, all bare | `y_0_star := 0`; the `0 < y_0_star` conjunct |

Proofs: `docs/audits/2026-08-09-unclosable-context-sorries.lean.txt`. Each
compiles clean against the tree at `main` @ `258d802ed6`.

Note how little the refutations need. No junk values, no degenerate limits — in
five of the eight it is enough to set one field to `0` and another to `1`. Three
do not even need the substantive conjunct: `lp_dual_stability` and
`confinement_frobenius_reciprocity` assert a strict inequality (`… < 0`,
`0 < y_0_star`) about data the class never constrains, and `parity_regime_selection`
falls to `ℕ` subtraction at `A = 1`.

**8/8 is the finding, not the 8.** A sample that size with no survivors says the
defect is structural: it is how conjectural-class blocks in this corpus are
being written, not a handful of slips. The hypotheses these theorems need were
never put in the classes, so every one of the `sorry`s is unclosable — and each
carries a `-- Ref:` citation that makes it read as a tracked gap.

### Scope of the claim

- **8 context-class sorries: all refuted.**
- **13 remaining sorry-theorems in the newly-visible set take no context class.**
  Different shape — the §9 small-instance check applies to them instead, and
  they are **not** covered by this result. Unaudited, not cleared.
- The whole population is only the *newly-visible* set (modules outside the
  pre-drain import closure). Context-class sorries in the 870 modules that
  always compiled have not been swept.

If the rate holds outside this set, that is the more important number, and it
is cheap to get: the method is one instance per statement.

## Update 2026-08-14 (q-NS session)

One of the three ill-posed statements is FIXED: `cascade_depth` — PR #5019
replaces the undischargeable flat sorry with the explicit dissipation-cutoff
class `QTurbulenceCascadeModel` + derived `finite_cascade_depth_of_cutoff`
(sorry-free, lean-direct exit 0). Remaining on this bean:
`mass_categorical_descent` and `np_splitting` (same fix shape: give the
context class the hypotheses the derivation needs). Status reverted to
in-progress (a prior update to completed was premature — scope is all 3).
