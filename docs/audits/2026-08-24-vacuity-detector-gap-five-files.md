# The vacuity detector's 5-file gap: mostly benign, and one real defect

**Date:** 2026-08-24
**Branch:** `claude/bring-surface-categorical-trace-wtrwtb`
**Beans:** `qou-lo1t` (the drain batch), `qou-tsnp` (free-`Prop` wiring)

## What prompted this

Draining the 42-candidate vacuity batch from `b67ee924e84` closed the ledger
(`--check-ledger` exit 0; genuine 123 · legit 25 · advisory 6 · needs-agent 0).
But the adjudication covered only what the audit *sees*. Measured against the
ledger keys, **5 of the 15 `.lean` files in that commit raise no candidate at
all**, having received the same "remove a `sorry`, add a class field"
treatment:

- `appendix-qvalues/qbeta-ck-truncation-canonical.lean`
- `lean/QOU/Archimedean/HyperbolicVolumeIndependence.lean`
- `lean/QOU/q_gl_obstruction_calc.lean`
- `mass-theory/phi-q-tower-jsj-bridge.lean`
- `mass-theory/prop-rigid-monoidal-structural-gap-invariance.lean`

`q_gl_obstruction_calc` is the conspicuous one: AGENTS.md §3b-tax already names
it as the failure mode where *"a real claim hidden behind a tautology"* was
*"repeatedly mis-called legit"* by heuristic triage.

> **"Raises no candidate" means `flagged` and the ledger, not the whole audit
> JSON.** Verified for all five: `flagged: 0`, `ledger: 0`. But
> `phi-q-tower-jsj-bridge.lean` *does* appear in that JSON — as
> `conjecture_graph.primary` (`TowerSummandRealization`), a **carrier record**,
> which is derived from the Lean rather than asserted as a defect. A grep of the
> JSON therefore hits the file without contradicting anything here. Its line
> number moving `50 → 53` in this branch is the three import lines added below.

## The shared shape, and why wiring a detector on it would be wrong

All five carry an **axiom shim**: a `Foo` carrier holding the content, a
companion `FooAxiom` / `FooExists` holding the same field, and a forwarder
returning `ctx.field`.

**Do not wire this.** Measured: four of the five axiom classes have **no
instance anywhere in `content/`** (each is mentioned in exactly one file), so
nothing is silently discharged — the shim relocates an assumption, it does not
resolve one. That is §3b-tax's honest representation of an unproved primary: a
content-bearing class with no instance.

And `HyperbolicVolumeIndependence.lean` documents the shim as **the repair of a
prior vacuity**:

> This file previously declared a *duplicate* `HyperbolicVolumeIndependence`
> class with a placeholder shape (`residual : ℝ` / `residual_eq_zero`) and a
> **vacuous** global instance `{ residual := 0, rfl }`. That was unsound as a
> conjecture encoding: the trivial instance silently discharged every
> `[HyperbolicVolumeIndependence]` hypothesis with no mathematical content.

A detector on the shim shape flags the fix. **This half of the gap is a
measured negative.**

## What does separate the one defect from the four benign cases

Not the shim — whether the instance is **guarded**. Both files below fill a
field with `0`; only one is harmful.

```lean
-- phi-q-tower-jsj-bridge.lean -- UNCONDITIONAL, discharges globally
instance skeletonRealisation (q : ℝ) : TowerSummandRealization q where
  realisation := fun _ _ => 0

-- prop-rigid-monoidal-structural-gap-invariance.lean -- guarded, inert
instance canonical (α : Type*) [ctx : RigidMonoidalStructuralGapInvarianceAxiom α] :
    RigidMonoidalStructuralGapInvariance α where
  categorical_trace _ := (0 : ℝ)
  convention_factorisation := ctx.convention_factorisation
```

The first satisfies every `[TowerSummandRealization q]` binder in its file —
including `bridge` and `bridge_nonneg`, which then read as claims about an
arbitrary realisation while the only realisation in scope is `0`. Under it
`PerPieceBridgeAxiom.bridge_per_piece` reads `0 = rho q * pieceVolume q β S`,
asserting `pieceVolume ≡ 0` for `q > 1`. This is the `triv_hecke` /
`triv_wedderburn` shape demoted in PR #5581, and it is now demoted to `def` for
the same reason.

## The file had never compiled

Verifying that demotion turned up something larger. `lean`-direct against the
real import cone:

| state | errors |
|---|---|
| before `b67ee924e84` | 4 |
| after, on `main` | 6 |
| now | **0**, no warnings, no `sorry` |

Nothing compiles this file. It is a content-block sibling under `mass-theory/`,
outside the Lake library, so `lake build QOU` never reaches it — the gap
AGENTS.md warns about under §"QA is agent-owned", in the direction where the
file *has* a sidecar but no compiler ever runs on it.

The two errors the drain added are the point: it copied the pre-existing
malformed `TowerSummandRealization.realisation β S` (the braid lands in the
`(q : ℝ)` slot) into the new `PerPieceBridgeAxiom`, which then failed to
elaborate as a class, which is why `[ctx : PerPieceBridgeAxiom q]` was rejected
as "not a class instance". **The drained `sorry` was replaced by something that
does not type-check** — and no gate anywhere would have said so.

## Census of the shape that does discriminate

[`scripts/trivially-inhabiting-instance-census.py`](../../scripts/trivially-inhabiting-instance-census.py)
(`--self-test`, four hand-read cases):

    3112 .lean under content/
      instances filling >=1 field with constant content : 37
      of those, UNGUARDED (no conditional-class binder)  : 23
      of those, class is consumed as a hypothesis        : 14   <-- actionable

Three hand-read, three confirmed harmful — `TowerSummandRealization` (fixed
here), `MassEndomorphism.trivial_int_zero` (global zero instance over an
*arbitrary* `β`), `QIntegerMassFormula.canonical` (`f_magic := fun _ => 0`,
discharging the `[QIntegerMassFormula]` of `fits_AME_conditional`). The other
11 are unread candidates, not findings.

### Two corrections to my own first run

The first version reported **273 actionable**, and both causes independently
invalidate the number:

1. **Scope.** `rglob` reached `content/…/lean/.lake/packages/mathlib` — 11125
   files where the audit scans 3112. Every high-consumer row was Mathlib.
2. **`rfl` on a proof field is a real proof.** It flagged `one_smul := rfl`,
   `mul_assoc := rfl`, `bot_le`. Those fields are *obligations* that the
   instance's data fields make hold definitionally. What is content-free is a
   constant in a **data** field. That restriction is what took 273 to 14.

A third bug was caught by the self-test rather than by reading output: a field
whose type begins on the next line captures an *empty* type, and an empty
string contains no Prop marker, so `realisation_nonneg : ∀ β S, 0 ≤ …` read as
data. Same trap as in `free-prop-field-audit.py`. The self-test now pins both
halves of that one instance, so it cannot return silently.

## Disposition

| file | verdict |
|---|---|
| `HyperbolicVolumeIndependence` | benign — shim with no instance, documents itself as the repair of a prior vacuity |
| `qbeta-ck-truncation-canonical` | benign — `[…Exists]` binder, no instance, honest conditional |
| `prop-rigid-monoidal-…-invariance` | benign — forwarder guarded by the axiom class |
| `q_gl_obstruction_calc` | **prose defect, fixed** — docstrings said `sorry` for two parts that are now assumptions |
| `phi-q-tower-jsj-bridge` | **real, fixed** — global zero instance demoted; file made to compile, 6 → 0 |

Not adjudicated in the ledger: these are not ledger entries, so there is nothing
to adjudicate. A criterion gap, not a queue item.

### Separately noted, out of scope here

`qbeta-ck-truncation-canonical.lean`'s docstring asserts *"`c_2 = -1` is PROVED
Taylor-exact"*. AGENTS.md corrects exactly that phrasing — **"PROVED IS
wrong"**; *structural* is the defensible word, and *Taylor* is under-specified
without naming which series. A docstring defect, not a vacuity one; left for a
`c_k`-scoped change rather than folded in here.
