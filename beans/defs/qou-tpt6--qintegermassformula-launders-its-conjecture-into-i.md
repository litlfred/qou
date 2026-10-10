---
# qou-tpt6
title: QIntegerMassFormula launders its conjecture into IsAMEValue.fits_bound, a class with zero instances
status: completed
type: bug
priority: high
created_at: 2026-08-24T19:38:09Z
updated_at: 2026-08-24T19:38:09Z
---

`QOU/Interactions/QIntegerMassFormula.lean:185`, verified present 2026-08-24.

## The instance

```
noncomputable instance canonical : QIntegerMassFormula where
  f_magic := fun _ => 0
  tolerance := 1 / 100
  tolerance_bound := <by norm_num, by norm_num>
  fits_AME := fun q m_e Z N B_AME inst => inst.fits_bound q m_e
```

`qou-hjf4` already records the `f_magic := fun _ => 0` half — a degenerate
magic-number correction discharging the `[QIntegerMassFormula]` of
`fits_AME_conditional`. **This bean is the other half, which hjf4 does not
name**, and it changes the diagnosis.

## Where the conjecture went

`fits_AME` is not discharged by an argument. It is *forwarded* to a field of a
second class:

```
class IsAMEValue (Z N : N) (B_AME : R) : Prop where
  has_nucleon : 1 <= Z + N
  binding_nonneg : 0 <= B_AME
  /-- Trivialized bound hypothesis to close sorry -/
  fits_bound : forall (q m_e : R), exists d : R, |d| <= 1/100 /\ B_AME = (1 + d) * binding_energy_bw q m_e Z N 0 0
```

`fits_bound` **is the conjecture**, restated with `f_magic` inlined as `0`, and
its own docstring says what it is for: *"Trivialized bound hypothesis to close
sorry"*. So the seven-term-fit conjecture is not carried by
`QIntegerMassFormula` at all. It is carried by the hypothesis class that every
statement of the conjecture takes as an instance binder.

## The precise defect: not vacuity, misrepresentation

`grep -rn IsAMEValue` over the corpus returns **five** lines, all in this file,
and **no instance of `IsAMEValue` anywhere**. Consequences:

- `fits_AME_conditional` is not vacuously true. It is **unsatisfiable as
  stated** — you cannot apply it, because you cannot produce the `[IsAMEValue Z
  N B_AME]` it needs, and producing one means proving the conjecture for that
  nuclide.
- So the honest reading is that this file states a conjecture *in the antecedent
  of its own theorem*. The theorem's content is "if the fit holds, the fit
  holds". That is a self-assuming projection (`qou-q407` family) wearing a
  two-class disguise.
- The `[QIntegerMassFormula]` binder is doing no work either: it is satisfied
  unconditionally by the `instance` above.

## Correction to the brief that produced this bean

The working note said "13 hypothesis-uses across 6 files". Measured:
`[QIntegerMassFormula]` appears as a binder **once** (`fits_AME_conditional`,
line 175), and `IsAMEValue` **twice** as a binder, both in this file. Nothing
outside `QOU/Interactions/QIntegerMassFormula.lean` mentions either class. Blast
radius is one file, which is the good news and the reason to fix it now.

## Disposition (design decision — do not drive-by)

Two coherent options, and they are not the same paper:

1. **State the conjecture where it lives.** Drop `fits_bound` from `IsAMEValue`,
   leaving it as what its name says — a predicate identifying a real AME entry
   (`has_nucleon`, `binding_nonneg`, and a lookup). `QIntegerMassFormula.fits_AME`
   then has nothing to forward to, and the `instance` must carry a `sorry`
   marked conjecture per AGENTS.md 3b, which `#print axioms` can see.
2. **Keep the forwarding but demote the instance** to a `def` and say in its
   docstring that it discharges the conjecture by assuming it. Cheaper, weaker,
   and leaves `IsAMEValue` misnamed.

Option 1 is the one that makes `#print axioms` tell the truth. Either way,
`f_magic := fun _ => 0` (hjf4) still needs a verdict.


## Resolved 2026-08-24 — neither option 1 nor 2: the file was not needed

Asked whether we need this at all. Measured, and the answer is no. Deleted
`QOU/Interactions/QIntegerMassFormula.lean` and dropped its import from
`QOU.lean`.

**What the measurement found — a second declaration this bean did not know
about.** `content/quantum-observable-universe/mass-theory/q-integer-mass-formula.lean`
declares `QOU.Interactions.QIntegerMassFormula` too: **same namespace, same
class name**, and it is the honest one.

|  | `lean/QOU/Interactions/…` (deleted) | `content/…/mass-theory/…` (kept) |
|---|---|---|
| states `fits_AME` | forwards to `IsAMEValue.fits_bound` | **directly, as the conjecture** |
| `IsAMEValue` | yes — carries the conjecture in a class named for a lookup | none |
| instance | `canonical`, with `f_magic := fun _ => 0` | **none** — the conditional is genuinely conditional |
| compiled | yes | no — `content/*.lean` sit outside `lean/` |

So the deleted file was the strictly worse of two same-named declarations, and
the honest one is the one the content block resolves to:
`content/…/mass-theory/q-integer-mass-formula.ts` carries
`lean.ref: "qou:QOU.Interactions.QIntegerMassFormula"` and resolves siblings
first.

**Consumers: none.** `grep` over the whole compiled tree for
`QIntegerMassFormula` / `IsAMEValue` returns, outside the file itself, only the
root aggregator's `import` line and three `QOU.Molecular` classes that happen
to share the name — different namespace, self-contained, no import of this
module. Verified rather than assumed.

**This removes one of `qou-hjf4`'s candidates, and does not close it.**
`f_magic := fun _ => 0` was in the deleted instance, so that candidate is gone
— but `hjf4` is a triage of **11** trivially-inhabiting-instance candidates and
the other ten are untouched. Noted on that bean rather than claimed here.

Deleting was preferable to either option in this bean. Option 1 (state the
conjecture with a `sorry` so `#print axioms` sees it) is what the surviving
sibling already does by supplying no instance at all; re-doing it here would
have produced a *third* statement of the same conjecture. Option 2 would have
kept a misnamed class alive in a file nothing reads.

**Not fixed, and now the residue:** two declarations of the same fully-qualified
name still existed a moment ago, one compiled and one not. That is a hazard
worth its own look — the same shape agent-B hit on `CrystalRMatrixSubLemma`,
and the same shape as `qou-znut`'s three `BorromeanQuark` classes. Whether
`content/*.lean` siblings should be allowed to shadow compiled module paths is
a platform question, not a QOU one.
