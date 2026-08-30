---
# qou-rq9n
title: Five q-NS conjecture carriers carry a FABRICATED trivial-zero instance
status: in-progress
type: milestone
priority: normal
created_at: 2026-08-29T19:45:34Z
updated_at: 2026-08-30T09:05:52Z
---

`lean/QOU/AlgebraicSubstrate/ConditionalClasses.lean` declares five `Prop`
carriers named after open fluid-dynamics problems and supplies an
**unconditional global instance for each**, discharging every one with zero:

    instance ns_counterexample_canonical : NSCounterexample where
      exists_singularity_time := fun _ _ => <0, le_refl 0>

The file introduces the block as the "canonical instance bundle ... via the
trivial-zero discharger", so this is a recorded design decision, not a slip.
The defect is what it does downstream.

## Why this is the exact shape the `cj*` beans exist to prevent

The 23 `cj*` beans each say: *"The sorry IS the conjecture (per AGENTS.md
3b) -- do NOT fabricate an instance (audit-dodge)."* These five ALREADY HAVE
the fabricated instance. Not one of the 23 names any of them.

## Measured on main, 2026-08-29

- File UNTOUCHED since 2026-08-24 (`git log --since` returns nothing).
- Bound as `[C]` hypotheses in **5 / 5 / 5 / 4 / 5** files respectively.
- `lean-vacuity-review-ledger.json`: **0 entries** for any of the five, and
  0 for `PvsNPQou`. The ledger is not out of scope here -- it covers 187
  files, **144 of them under `/lean/QOU/`**. In scope and missed.
- My `vacuous-prop-carrier-probe.py --check` ratchet: exit 0, all 23
  self-contained carriers in baseline, these five among them.

## Why no shipped criterion fires

AGENTS.md 3b-tax cites THIS FILE as the exemplar of doing it right --
"parameter-quantified inequality in the *shape* of the claim". That is
accurate. The shape is right and the content is absent, and nothing tests
the difference: fields are not `True`, nothing projects them, no `sorry`,
docstring property-count matches field-count. See
docs/audits/2026-08-24-shape-of-claim-is-not-content.md.

## Disposition -- AUTHORIAL, do not "fix" mechanically

Demoting the instances alone leaves carriers that still assert nothing. The
fix is to encode what the q-Aubin-Lions compactness claim, the blow-up rate
bound and the critical exponent actually say. That is mathematics.

Children: one per carrier.



## UPDATE 2026-08-30 — the fabricated instance is REMOVED; the carriers are not fixed

Half of this bean is closed, and it is the half that was mine.

**Done (PR #6068).** The five unconditional global instances -- the "canonical
instance bundle ... via the trivial-zero discharger" -- are gone from
`lean/QOU/AlgebraicSubstrate/ConditionalClasses.lean`. AGENTS.md §3b-tax
mandates this directly: an unproved primary is honestly represented by a
content-bearing class with NO instance.

**Why it was safe, measured rather than assumed.** Every consumer takes the
carriers as explicit `[C]` hypotheses -- all nine theorems in
`ConditionalCorollaries.lean` plus `surreal_rate_calculus_conditional` in
`SurrealRateCalculus.lean`, the only two modules importing this one -- and
**no declaration in the corpus applies any of those nine** (0 external
references each). Verified lean-direct against the real import cone: all three
modules exit 0, 0 errors.

**Why it was worth doing, which "nothing broke" alone would not show.**
"Nothing broke" is equally consistent with nothing ever having been
connected. A probe applying a conditional corollary with no instance now fails:

    example : (3 * 4 : ℕ) = 12 := critical_exponent_identity
    error: failed to synthesize CriticalExponent

Before the removal that typechecked. That is the hole: a conditional theorem
going unconditional at its call site, in an importable library module.

**STILL OPEN, and unchanged by the above.** Inhabitability is a property of the
carriers' FIELDS, and the fields were not touched. All five remain provable
with no hypotheses -- re-proved in
`docs/audits/2026-08-30-conditional-classes-still-vacuous-after-bundle-removal.lean`
(exit 0, 0 errors), which exists because the removal deleted the evidence the
baseline had been citing.

So the five children stay open. What each needs is the real statement encoded:

- `qou-3ytx` QAubinLions -- "K scales linearly with the energy bound" is
  claimed in prose and absent from the field.
- `qou-5nj1` NSCounterexample -- the field binds `D₀` and never mentions it
  again; needs the vorticity blow-up.
- `qou-93hu` CriticalExponent -- the field is a closed numeral identity with
  **no exponent variable in it**; needs α as a parameter. Probably the most
  tractable of the five, since "α = 4/3" is already stated in its docstring:
  `class CriticalExponent (α : ℝ) : Prop where alpha_eq : α = 4/3`. Note this
  changes the class signature, so every `[CriticalExponent]` binder in the
  two consumer modules moves with it.
- `qou-88nf` BlowupYekutieli -- the encoded bound `r ≤ 1 + T` involves no
  substrate scale, and `r = 0` (no blow-up) satisfies it.
- `qou-m7a2` RegularityBreakdown -- needs measure-zero concentration.

Four of the five need analytic setup the docstrings only gesture at; that is
the author's mathematics, not a cleanup.

STATUS CORRECTED 2026-08-30: four of five, not zero and not five.

Closed: qou-93hu (CriticalExponent, main 33d9eb4b414/5f019815d56), and
qou-3ytx / qou-5nj1 / qou-m7a2 (PR #6122, merged).
OPEN: qou-88nf (BlowupYekutieli).

This bean sat at 'todo' on main while four of its five children were completed,
which understated the work done. It is not 'completed' either: qou-88nf is
genuinely open and is different IN KIND from its siblings -- conj:blowup-yekutieli
is declared by NO content block, so unlike the other four there is no upstream
statement to transcribe. Closing it requires recovering or re-authoring the
missing conjecture block, which is authorial mathematics, not encoding.

I briefly closed qou-88nf by inventing an affine bound C*(1+T) off its
docstring; that was retracted (see its body). Do not repeat it.
