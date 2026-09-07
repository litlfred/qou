---
# qou-octr
title: Small-instance check the 34 sorries the drain made visible — never reported by any build
status: completed
type: task
priority: normal
created_at: 2026-08-09T09:57:23Z
updated_at: 2026-09-05T17:57:39Z
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


## Re-measured 2026-09-05 — the eight are all sorry-free now, and four of the fixes went the WRONG way

I had quoted "8 of 8 context-class sorries unclosable" three times in reports
without checking it. Checking it.

**First, a tooling correction, because the naive measurement is wrong in both
directions.** `grep '\bsorry\b'` over these files returns 21 hits. **Zero of
them are proof terms** — every one is inside a `/-- … -/` docstring or a `--`
comment, in prose *about* `sorry`. Strip block and line comments first
(`scratchpad/sorrycount.py`, 30 lines) and the count is **0 real / 21 raw**
across all eight. A file whose whole docstring explains why a `sorry` would be
unsound reads, to a naive grep, as the file with the most `sorry`s in the
corpus. Two of the eight also came back "decl not found" on a first pass: one
was a `timeout 30` on a recursive grep silently expiring (`skein_mass_from_linking`
is in `BraidsKnots/`, not `BraidKnot/`), and one was a **rename** the bean's own
2026-08-14 update records (`finite_cascade_depth` → `finite_cascade_depth_of_cutoff`).

**So the bean's population no longer exists as sorries.** All eight
declarations are present and every one is sorry-free. But they were
dispositioned two different ways, and only four honestly:

**Derived — 4.** The conclusion is obtained *from* structure the class carries,
not returned by it.

| decl | what discharges it |
|---|---|
| `mass_categorical_descent` | `descent_decomposition` — splitting a finite sum along a decidable centre predicate. Plus a tranche-2 operator-level centrality (`IsCentral` = membership in `Set.center A`). |
| `finite_cascade_depth_of_cutoff` | logs of the dissipation cutoff `q^N ≤ Re_q^{3/4}`, divided by `log q > 0`. Real tactic proof. |
| `neutron_proton_splitting` | pinned numerics + `norm_num`; and the exact-equality conjunct was correctly **demoted to a tolerance** per §7ab rather than kept and dodged. |
| `skein_mass_from_linking` | demoted to `def … : Prop` (named, not asserted), with a *derived* torus specialisation and a standing counterexample so a later "finish it with a `sorry`" fails against a compiled obstruction. |

**Projected — 4.** Each conjunct of the conclusion is verbatim one class field;
the proof term is `ctx.field` or `⟨ctx.f₁, …, ctx.fₙ⟩`.

- `volume_perturbation` — `:= ctx.perturbation_formula`
- `parity_regime_selection` — `⟨ctx.sign_identity, ctx.odd_regime, ctx.even_regime, ctx.neutron_regime⟩`
- `lp_dual_stability` — `⟨ctx.primal_stable, ctx.dual_price_bound, ctx.partial_unstable, ctx.strong_duality⟩`
- `confinement_frobenius_reciprocity` — a six-tuple of fields

**That is this bean's own defect, inverted.** The finding here was *"the class
carries too little — nothing constraining the fields the conclusion names"*.
The fix for these four moved the class to carrying **exactly the conclusion**,
which is AGENTS.md §3b-cond item 5's self-assuming projection. The honest
middle is what the other four did: carry structure the conclusion is *derived*
from.

**This is not new work, and mostly not new information.** Per §3b a disclosed
projection is policy-compliant; the defect is an *undisclosed* one, and that
population is already scoped as epic `qou-5p7n` (125 of 147 undisclosed).
Measured on these four: `parity_regime_selection` **discloses** in its module
docstring; `volume_perturbation` half-discloses ("Proved from the upstream
class field constraint" names the mechanism but reads as a proof claim);
`lp_dual_stability` and `confinement_frobenius_reciprocity` carry **no
disclosure at all** — zero hits for any disclosure phrasing. Those two belong
in `qou-5p7n`'s "98 bare" bucket, not here.

**One thing WAS new: the detector could not see one of them.**
`volume_perturbation` is the cleanest projection of the four — one field,
returned verbatim — and `proof-no-self-assuming-projection` reported the other
three CRITICAL and not this one. Cause: the class field spells the balanced
q-integer `QOU.QInteger.qIntBalZ`, the theorem spells `qIntSym`, a file-local
`noncomputable abbrev` for that head applied to its own binders. An `abbrev` is
reducible so the projection typechecks; the detector's character-exact
comparison sees two strings. Closed in this branch by `fileHeadAliases`
(admits an `abbrev` only when its body is a dotted head applied to its binders
in order, then normalises both sides through the head map). Whole-corpus
before/after: **exactly one new hit, no other line changed** — 75 defect
candidates both runs, files 115 → 116, exempt 65 → 66. Blind-spot taxonomy:
the abbrev-alias row.

**Status.** This bean's stated scope is discharged: all three originally
ill-posed statements now carry the missing hypotheses or an honest demotion,
and the 2026-08-14 note's "remaining: `mass_categorical_descent` and
`np_splitting`" is stale — both are done. The four projections are `qou-5p7n`
work, not a reopening of this one.
