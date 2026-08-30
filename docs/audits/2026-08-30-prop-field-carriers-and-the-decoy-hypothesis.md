# Bare-`Prop` carrier fields, and the decoy-hypothesis shape they enable

Bean `qou-qcy6`. Measured 2026-08-30 on `main` at `1f6538d38`.

## The shape

A carrier declares a relation as a **bare `Prop` field** plus a sibling field
proving it:

```lean
  /-- **Hecke relation**: `(σ_i - q)(σ_i + q⁻¹) = 0` … -/
  hecke_relation : Prop
  hecke_holds : hecke_relation
```

An instance therefore *chooses what the relation means*. The docstring states
the equation; the type does not.

**53 candidates across 32 files**
([`scripts/lean-prop-field-carrier-audit.py`](../../scripts/lean-prop-field-carrier-audit.py)).
**Zero** appear in the 368-entry vacuity ledger; **zero** among the audit's 133
candidates. The existing criteria pass them *correctly* — `proof-claims-unencoded`
keys on docstring properties that have **no field**, and here there is a field.

## Machine-checked: one of two placeholder Hecke carriers

**Scope correction, raised by a Copilot review on PR #6120 and accepted.** The
name `IwahoriHeckeAlgebra` is ambiguous — there are two:

| declaration | kind | how it states the relations |
|---|---|---|
| `QOU.Mathlib.HeckeAlgebra.IwahoriHeckeAlgebra` | `class` | bare `Prop` fields — **the subject here** |
| `QOU.BraidKnot.IwahoriHeckeAPI.IwahoriHeckeAlgebra` | `structure` | separate **axioms**, with `Ring`/`StarRing` on the carrier |

Both describe themselves as placeholders. An earlier draft of this document
called the first "the framework's foundational algebra class"; that was an
over-claim and is withdrawn. Nothing below applies to the second.

**Prior art I missed.** `triv_hecke` (`HeckeAlgebra.lean:174`) already
constructs a satisfying instance with all three relations `True`, over `PUnit`,
and cites its own probe. A grep for `hecke_relation :=` before writing mine
would have found it. What the probe below adds is the *falsification* half — a
concrete `q` at which §7a's relation is false in a satisfying instance — which
`triv_hecke` does not state.

[`scripts/lean/probes/prop-field-carrier-vacuity.lean`](../../scripts/lean/probes/prop-field-carrier-vacuity.lean),
`lean`-direct **exit 0**. `QOU.Mathlib.HeckeAlgebra.IwahoriHeckeAlgebra` is
inhabited at every ring, size and parameter by an instance whose generators are
all the ring unit and whose three AGENTS.md §7a relations are all `True`. There
`σ·σ = 1` while §7a demands `(q − q⁻¹)·σ + 1`, which over `ℚ` at `q = 2` is
`5/2`.

So `[IwahoriHeckeAlgebra R n q]` buys a carrier type, an `AddCommGroup`, a
`one`, a `mul` and a `sigma` family. Nothing Hecke.

**Severity bounded in both directions.** `hecke_holds`, `hecke_relation`,
`braid_holds` and `far_commute_holds` have **zero consumers** — nothing in
`content/` reads them — and none of the 10 `[IwahoriHeckeAlgebra …]`-conditional
declarations restates the relations. The fields are write-only, so nothing false
is derived *from* them. The defect is that the class does not mean what its
docstrings say. "The Hecke algebra is broken" is the over-claim; "harmless"
misses that the central presentation is unencoded.

## The consumer split — and the Hecke case is the MILD half

[`scripts/lean-prop-field-consumer-split.py`](../../scripts/lean-prop-field-consumer-split.py):

| | count |
|---|---|
| write-only (no reader of either field) | **17** |
| consumed | **36** |

## The decoy hypothesis

Reading the consumed ones turned up a compound shape that is strictly worse than
a plain self-assuming projection. `QOU.FluidDynamics.CoreLeviFormContext`:

```lean
  levi_form_regular : Prop                                     -- instance chooses this
  levi_form_active  : levi_form_regular                        -- …and proves it
  impl_core_aspect_ratio       : levi_form_regular → aspect_sup ≤ C
  impl_levi_form_condition     : levi_form_regular → cond_sup ≤ C ^ 2
  impl_contact_structure_remains : levi_form_regular → 0 < lambda_min
  impl_observability_axiom_holds : levi_form_regular → hom_dim_at_p = 0
  impl_no_integral_submanifold   : levi_form_regular → integral_submfd_dim < 2

theorem core_levi_form [ctx : CoreLeviFormContext] :
    ctx.aspect_sup ≤ ctx.C ∧ ctx.cond_sup ≤ ctx.C ^ 2 ∧ 0 < ctx.lambda_min ∧
    ctx.hom_dim_at_p = 0 ∧ ctx.integral_submfd_dim < 2 :=
  ⟨ctx.impl_core_aspect_ratio ctx.levi_form_active, …⟩
```

Take `levi_form_regular := True` and `levi_form_active := trivial`, and every
`impl_` field is `True → conclusion` — the conclusion, assumed. All five
conjuncts of the theorem are class fields with a decoy hypothesis in front.

**Why the existing criterion misses it.** `proof-no-self-assuming-projection`
looks for a proof term that IS a field projection, `ctx.field`. Here the proof
is `ctx.field ctx.other_field` — an *application*. The intervening arrow is what
makes it look like a derivation from a stated regularity hypothesis, and it is
also what hides it from the detector.

**NOT machine-checked, and the blocker is named.** Constructing the witness
instance needs `0 < (1 - 2⁻¹)/2` in `core_levi_form`'s import cone, where
`norm_num` reduces it to `2⁻¹ < 1` and stops — the cone lacks the `norm_num`
extension for real inverses. That is an import-cone limitation of that module,
not evidence about the finding, which is established by reading the quoted code.
Machine-checking it is the next step.

## What is mechanical here

Both shapes are decidable from the class's field graph with no agent verdict,
which is unusual for this audit family:

- a field of type bare `Prop` whose only use is as the type of a sibling field;
- a field `f : Prop` together with any field of type `f → _`.

## Status

Candidate counts, not verdicts. 53 is what the scanner reports; the
adjudication is open, and the write-only/consumed split is the first cut at
severity rather than the answer.
