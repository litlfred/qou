# Five open problems, discharged by zero — and the audit cannot see them

**Date:** 2026-08-24 · **Bean:** `qou-hjf4`
**Tool:** [`scripts/vacuous-prop-carrier-probe.py`](../../scripts/vacuous-prop-carrier-probe.py) (`--self-test`)
**Probe:** [`2026-08-24-core-levi-form-vacuous-classes-probe.lean`](2026-08-24-core-levi-form-vacuous-classes-probe.lean)

---

## The finding

[`lean/QOU/AlgebraicSubstrate/ConditionalClasses.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/ConditionalClasses.lean)
declares five `Prop` carriers named after open problems — `QAubinLions`,
`NSCounterexample`, `CriticalExponent`, `BlowupYekutieli`,
`RegularityBreakdown` — and **supplies an unconditional global instance for
each**, discharging it with zero:

```lean
class NSCounterexample : Prop where
  exists_singularity_time : ∀ (D₀ : ℝ), 0 ≤ D₀ → ∃ T : ℝ, 0 ≤ T

instance ns_counterexample_canonical : NSCounterexample where
  exists_singularity_time := fun _ _ => ⟨0, le_refl 0⟩
```

`CriticalExponent`'s entire content is `alpha_three_eq_four : (3 * 4 : ℕ) = 12`,
discharged `rfl`.

Corpus-wide these are bound at **16 / 10 / 10 / 14 / 12** sites. Because the
instances are unconditional and this is an **importable library module**, every
`[NSCounterexample]`-conditional theorem reachable from it is unconditional.

## This is not concealed — the file says so

Three of the five docstrings state it outright:

> *"For every initial-data norm `D₀ ≥ 0`, there exists a singularity time
> `T* ≥ 0`. **Trivially: `T* = 0` works.**"*
> *"the blow-up rate `r ≥ 0` satisfies `r ≤ 1 + T`. **Trivially: `r = 0`
> works.**"*
> *"the breakdown measure `μ ≥ 0` satisfies `μ ≤ s`. **Trivially: `μ = 0`.**"*

and the instance block is introduced as the **"canonical instance bundle …
via the trivial-zero discharger"**. So this is a recorded design decision, not
a slip. The defect is what the design does downstream, and what the docstrings
one line up claim in its place:

> *"Concrete content: `K` scales linearly with the energy bound (the
> Aubin–Lions embedding constant)."*

The field says `∃ K, 0 ≤ K ∧ K ≤ 2·E` — *some* non-negative `K` under `2E`,
satisfied by `0`. "Scales linearly" is not encoded. **The prose promises
content the field does not carry**, which is exactly what
`proof-claims-unencoded` exists to catch.

## Why the audit misses it — shape of claim ≠ content of claim

AGENTS.md §3b-tax cites **this very file** as the exemplar of doing it right:

> Class fields must carry the conjecture's **content** — a parameter-quantified
> inequality in the *shape* of the claim (the Round-11 pattern in
> `ConditionalClasses.lean`) — never a bare `True` or an empty body.

That description is accurate: these fields *are* parameter-quantified
inequalities in the shape of the claim. **The shape is right and the content is
absent**, and no shipped criterion tests the difference:

| criterion | why it does not fire |
|---|---|
| `proof-no-empty-prop-carrier` | the carriers have fields |
| `proof-claims-unencoded` (`true-class-field`) | no field is typed `: True` |
| `proof-claims-unencoded` (doc enumerates ≥2 properties, <2 encoded) | each docstring names ~1 property and there is 1 field, so the counts match |
| `proof-no-self-assuming-projection` | there is no projection; the instances construct witnesses |
| `proof-docstring-sorry-mismatch` | no `sorry` is mentioned or present |

Measured: `ConditionalClasses.lean` raises **0** lines in a fresh
`lean-vacuity-axiom-audit.ts` run, and the five carriers have **0** entries in
`lean-vacuity-review-ledger.json`. They have never been adjudicated.

The missing test is the one this probe performs: **try to inhabit the carrier
with no hypotheses.** If that succeeds, the carrier asserts nothing, whatever
shape its fields have.

## Method, and its honest limit

`vacuous-prop-carrier-probe.py` scans 3117 files, finds **85**
`class … : Prop where` carriers, and keeps the **23** that are *self-contained*
— every field type mentioning nothing but ℝ/ℕ/ℤ, numerals and logical
vocabulary. A carrier referring to `pieceVolume` or `Phi1_of_ordering` is
**skipped, not judged**: proving it vacuous would need its own import cone.

That restriction is not a weakness of the finding, it is its shape — *a
carrier whose fields mention no domain object cannot say anything about the
domain.*

It then emits a Lean file re-declaring each candidate and attempting to inhabit
it. **The generic tactic list discharges 12 of 23.** Counting the carriers proved
by *any* route — that list, the hand-written probes, and the corpus's own
instance bundle — the baseline is now **fully adjudicated: 22 proved-vacuous,
1 uninhabitable-by-design, 0 undecided**, recorded per-carrier with its
evidence in
[`vacuous-prop-carrier-baseline.json`](vacuous-prop-carrier-baseline.json).

> **Both figures here were lower when first written (8 of 23; 16 vacuous, 7
> undecided), and the reason is a bug in this probe rather than anything about
> the carriers.** `first` advances to the next alternative only when the
> previous one FAILS, and `norm_num` rewriting `∃ q : ℝ, q > 0` to `∃ q, 0 < q`
> makes progress without closing — so `first` committed to it and left the goal
> open. Adding `done` to every alternative moved the generic list 8 → 12. The
> remaining ten are reached only by hand proofs, and the baseline says so per
> entry rather than implying the tool found them.
>
> The one `uninhabitable-by-design` entry is
> `QOU.Machinery.SeparateLambdaScale_Antipattern`, whose single field is
> `is_antipattern : False`. That is the honest opposite of a vacuous carrier —
> it marks the purged `λ_scale` construction and can only be used, never proved.

The direction matters:

- a probe that **succeeds** settles the question — the carrier is inhabited
  with no hypothesis;
- a probe that **fails** settles nothing. It means the tactic list found no
  witness, not that the carrier has content.

**A probe count is a lower bound, and demonstrably so.** Even after the `done`
fix the generic list does not discharge `QAubinLions`, `BlowupYekutieli` or
`RegularityBreakdown` — yet all three are provable, as the hand-written probe
committed alongside shows (`⟨0, le_refl 0, by linarith⟩`), and as this file's
own instance bundle proves in the corpus itself. Read a probe's failures as
*undecided*, never as content.

## What is new here, and what is not

**New:** the five `ConditionalClasses.lean` carriers and their trivial-zero
instance bundle. Invisible to the audit, unadjudicated in the ledger,
importable, 10–16 binder sites each.

**Already reported** (2026-08-24, same bean): the five same-named carriers in
`fluid-dynamics/core-levi-form.lean`. Those are *not* importable, so their
collision is latent; these are.

**Known and deliberately exempt — not a finding:** the three `FMap*` carriers
in `QBeta/FMapStructuralPaths.lean`, whose single field is typed `: True`. The
audit *does* flag all three, as
`proof-claims-unencoded [EXEMPT(explicit @marker / opaque-tag opt-out)] —
honestly framed; tracked not counted`. That opt-out is sanctioned by §3b-tax
for a genuinely-open opaque field. The probe rediscovered them; they were
already declared.

## Disposition

Nothing changed in `content/`. The fix is to encode the real statements — what
*is* the q-Aubin–Lions compactness claim, the blow-up rate bound, the critical
exponent — and that is authorial, not a cleanup. Demoting the instances alone
would leave carriers that still assert nothing.

The **detector** gap is separately actionable and is not authorial: a criterion
that attempts to inhabit each self-contained `Prop` carrier would have caught
all ten of these (five here, five in `core-levi-form`) without any judgement
call. Recorded for `qou-hjf4`.
