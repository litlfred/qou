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

### 🛑 CORRECTION to my first reading, same day

An earlier revision of this section said: take `levi_form_regular := True` and
each `impl_` field "is the conclusion, assumed", implying the class permits
**false** conclusions. **That is wrong, and building the counter-instance is
what showed it.** An instance must supply *both* `levi_form_active : P` and
`impl_… : P → C`, so it must supply `C`. The conclusions therefore hold in every
instance; the class does constrain them.

**The defect is not unsatisfiability — it is ELIMINABILITY.** The decoy carries
no information, so a class asserting the conclusion outright is interderivable
with it, and the theorem's proof derives nothing: it projects an assumption
through an arrow that could be deleted.

Machine-checked on the simplest instance of the shape,
[`scripts/lean/probes/decoy-hypothesis-eliminable.lean`](../../scripts/lean/probes/decoy-hypothesis-eliminable.lean),
`lean`-direct **exit 0**, subject `QOU.Torsion.KnotParticleGenerationContext`
(chosen because its import cone needs no real arithmetic — see the blocker
note below). It exhibits `toStripped` and `ofStripped` in both directions,
`ofStripped` taking the decoy proposition to be `True`, plus a round-trip
theorem.

### Why the existing criterion misses it

`proof-no-self-assuming-projection` looks for a proof term that **is** a
projection, `ctx.field`. Here the term is `ctx.field ctx.other_field` — an
**application**. The intervening arrow is exactly what makes it read as a
derivation from a stated hypothesis, and exactly what hides it from the
detector.

### The population

[`scripts/lean-decoy-hypothesis-audit.py`](../../scripts/lean-decoy-hypothesis-audit.py)
finds **17 decoy carriers across 17 files, carrying 34 `impl_` fields** — so 34
conclusions currently reached by projecting an assumption through an eliminable
arrow.

**That number was 12 twice before it was 17, and both wrong readings looked
plausible.** The parser dropped any field whose type begins on the *next* line —
`impl_x :` with the arrow below it — because the field regex demanded at least
one character after the colon; such a line then fell through to the
continuation branch and was appended to the *preceding* field, swallowing the
very `impl_` fields the detector exists to find. A first "fix" made it 11.

It was caught by one observation: `KnotParticleGenerationContext`, the class
with a machine-checked probe in this same PR, was **absent from its own
detector's results**. That is now a `--self-test` assertion in the script — it
exits 1 and refuses to let the count be quoted if the worked example is missing.
Same discipline as `valueOnlyProjects` in #6093, where the first cut returned
zero across five modules chosen for containing the defect.

### On `CoreLeviFormContext` specifically

Still read-verified rather than machine-checked, and the blocker is named: the
witness instance needs `0 < (1 − 2⁻¹)/2` in `core_levi_form`'s import cone,
where `norm_num` reduces it to `2⁻¹ < 1` and stops — that cone lacks the
`norm_num` extension for real inverses. An import-cone limitation, not evidence
about the finding. The shape is identical to the machine-checked one above, with
five `impl_` fields instead of one.

## What is mechanical here

Both shapes are decidable from the class's field graph with no agent verdict,
which is unusual for this audit family:

- a field of type bare `Prop` whose only use is as the type of a sibling field;
- a field `f : Prop` together with any field of type `f → _`.

## Status

Candidate counts, not verdicts. 53 is what the scanner reports; the
adjudication is open, and the write-only/consumed split is the first cut at
severity rather than the answer.
