# NS-Lean retrofit — agent brief

**Status:** the algebraic-side framework is **fully retrofitted** under
CLAUDE.md §3b-cond ([commit `4049f96dc`](https://github.com/litlfred/qou/commit/4049f96dc)
on `claude/audit-math-framework-FXlp2`). The propagation audit shows
**13 violators** remaining — all in the fluid-dynamics cone.

This memo is a complete brief for an agent to close the remaining 13
by class-axiomatising the fluid-dynamics conjectures.

## Audit count to drive to zero

```
$ bun run content/pipeline/conjectural-propagation-audit.ts
Class-axiomatised conjectures (§3b-cond eligible): 33
Violators (cone touches non-class-axiomatised conjecture): 13   ← TARGET 0
Conditional-on-class (cone fully class-axiomatised): 221
```

Witness file: `docs/audits/2026-05-01-p3-1-conjectural-propagation.witness.json`.
The `violators` array lists every block needing class coverage in
its transitive `uses[]` cone.

## The 13 violators — current cones

All 13 transitively touch one or more of these **6 fluid conjectures
that lack a Lean class**:

| conjecture label | location |
|------------------|----------|
| `conj:critical-exponent` | `content/quantum-observable-universe/fluid-dynamics/` |
| `conj:blowup-yekutieli` | same |
| `conj:regularity-breakdown` | same |
| `conj:q-aubin-lions` | same |
| `conj:ns-counterexample` | same |
| `conj:levi-degeneracy` | same |

The 13 violators fall into two groups:

**Group A — fluid-dynamics blocks (close to the conjecture itself).**
These are inside `fluid-dynamics/` and structurally need their
upstream conjecture; class-axiomatising the conjecture flips them
to "conditional-on-class".

**Group B — cross-chapter blocks (a few `prop:vorticity-lower-bound`
references that leaked across).** Same fix.

Run the audit to enumerate the exact 13:

```bash
bun run content/pipeline/conjectural-propagation-audit.ts
```

## Pattern to follow

Look at the canonical retrofitted bridge conjectures already on
this branch:

- `content/quantum-observable-universe/braids-and-knots/shell-correction-term-seven.lean` (existing template)
- `content/quantum-observable-universe/molecular-construction/shell-closure-nf-term-count.lean` (just-added)
- `content/quantum-observable-universe/observations/borromean-quark.lean` (just-added)
- `content/quantum-observable-universe/lean/QOU/BraidKnot/KnotFactorFrobeniusPairing.lean` (new file, lean.ref pattern)
- `content/quantum-observable-universe/lean/QOU/AppendixSurreals/ClassicalLimitStpart.lean` (new file, lean.ref pattern)

Each follows the same template:

```lean
-- ── Conjecture class (CLAUDE.md §3b-cond axiomatisation) ───────

class C where
  -- fields encoding the conjecture's content
  fact1 : <Type>
  fact2 : <Type>
  /-- The conjecture proper. -/
  conj_holds : Prop
  conj_holds_witness : conj_holds

theorem downstream_result [inst : C] (...) : ... :=
  inst.conj_holds_witness    -- or inst.fact1, etc.
```

Plus the .ts manifest must have:

```typescript
lean: {
  ref: "qou:QOU.<Subdir>.<ClassName>",
  validation: "not_checked",
},
```

## Per-conjecture content sketches

Below are starting points for each of the 6 fluid conjectures.
Each conjecture's `class C` should encode its mathematical content
in fields, with the conjectural assertion as the only field
discharged by `sorry` in instances.

### `conj:critical-exponent`

```lean
class CriticalExponent where
  /-- The critical Reynolds-number exponent. -/
  alpha_c : ℝ
  /-- Conjectured value α_c = 5/2 (or whatever the manuscript states). -/
  alpha_c_value : alpha_c = 5/2  -- or via sorry
  /-- For Re < α_c · Re_0, NS solutions are smooth. -/
  smooth_below_alpha_c : Prop
  smooth_below_alpha_c_holds : smooth_below_alpha_c
```

Open the existing `.md` (`fluid-dynamics/critical-exponent.md`) to
get the exact statement.

### `conj:blowup-yekutieli`

```lean
class BlowupYekutieli where
  /-- The Yekutieli blow-up profile. -/
  T_star : ℝ
  /-- ‖∇u‖_∞ → ∞ as t → T_star (Yekutieli profile). -/
  blowup_at_T_star : Prop
  blowup_at_T_star_holds : blowup_at_T_star
```

### `conj:regularity-breakdown`

```lean
class RegularityBreakdown where
  /-- A specific solution profile that breaks H^k regularity at
      finite time T_break. -/
  T_break : ℝ
  T_break_pos : T_break > 0
  regularity_breaks_at_T_break : Prop
  regularity_breaks_at_T_break_holds : regularity_breaks_at_T_break
```

### `conj:q-aubin-lions`

```lean
class QAubinLions where
  /-- q-deformation of the Aubin-Lions compactness lemma. -/
  q_compact_embedding : Prop
  q_compact_embedding_holds : q_compact_embedding
```

### `conj:ns-counterexample`

```lean
class NSCounterexample where
  /-- A specific divergence-free initial datum producing finite-time
      blow-up — i.e., a Millennium counterexample under the QOU
      brane-tower modification. -/
  initial_datum_exists : Prop
  initial_datum_exists_holds : initial_datum_exists
```

### `conj:levi-degeneracy`

```lean
class LeviDegeneracy where
  /-- The Levi-form degeneracy locus. -/
  D_levi : Set ℝ³
  /-- Levi degeneracy occurs precisely on the QOU substrate. -/
  levi_degenerate_on_substrate : Prop
  levi_degenerate_on_substrate_holds : levi_degenerate_on_substrate
```

## Process for the agent

For each of the 6 conjectures:

1. **Read the `.md`** to get the exact mathematical statement.
2. **Locate the `.lean`** (sibling or via `lean.ref`).  If absent,
   create one at the lean.ref-resolved path:
   `content/quantum-observable-universe/lean/QOU/FluidDynamics/<Name>.lean`.
3. **Add a `class`** with fields encoding the statement; the
   conjecture is the only field needing `sorry` in instances.
4. **Update the `.ts`** to ensure `lean.ref` points to the right
   path (test with the audit; the script falls back to lean.ref so
   either sibling or `lean/QOU/FluidDynamics/...` works).
5. **Run validation:** `bun run validate` (must stay `✓ Valid`).
6. **Run the propagation audit** and observe violator count.
7. **Iterate** until violators = 0.

## Validation checks (must remain green)

```bash
# Content schema validation — must stay green
bun run validate
# Should report: ✓ Valid — 177 issue(s)  (warnings only)

# §3b-cond audit — must reach 0 violators
bun run content/pipeline/conjectural-propagation-audit.ts
# Target output: Violators (cone touches non-class-axiomatised
# conjecture): 0

# Lean build (if working in the qou Lake package)
lake build QOU
# Must compile without errors (warnings/sorries ok in *.lean)

# LP-dual witness validator — should stay clean
python3 computations/lp_dual_witness_validator.py
# Should report: OK — all flagged witnesses include LP dual.
```

## Out of scope for this brief

- **Proving** any of the conjectures (research-grade math).
- **Removing the `sorry`** in instances — these ARE the conjecture.
- **Touching algebraic-side blocks** — they're already done.
- **Modifying** the conjectural-propagation audit script — it's
  correct as-is for the fluid case (will pick up new classes
  automatically).

## What "done" looks like

```
$ bun run content/pipeline/conjectural-propagation-audit.ts
Class-axiomatised conjectures (§3b-cond eligible): 39
Violators (cone touches non-class-axiomatised conjecture): 0
Conditional-on-class (cone fully class-axiomatised): 234
```

Then commit with message `P3.1 fluid-dynamics retrofit: 13 violators
→ 0 (class-axiomatise NS conjectures)`. Push to your branch and
open a PR.

## Pre-work survey

Before starting: read these for context.

- `CLAUDE.md` §3b-cond — the conditional-class exception protocol
- [`shell-correction-term-seven.lean`](https://github.com/litlfred/qou/blob/claude/audit-math-framework-FXlp2/content/quantum-observable-universe/braids-and-knots/shell-correction-term-seven.lean) — original canonical pattern
- [`shell-closure-nf-term-count.lean`](https://github.com/litlfred/qou/blob/claude/audit-math-framework-FXlp2/content/quantum-observable-universe/molecular-construction/shell-closure-nf-term-count.lean) — recent retrofit example
- [`KnotFactorFrobeniusPairing.lean`](https://github.com/litlfred/qou/blob/claude/audit-math-framework-FXlp2/content/quantum-observable-universe/lean/QOU/BraidKnot/KnotFactorFrobeniusPairing.lean) — example creating a brand-new .lean class file

Estimated effort: **1-2 days per conjecture × 6 conjectures = 1-2 weeks** for a focused agent.

## Branch / PR

Open a fresh branch from `main` (do NOT extend
`claude/audit-math-framework-FXlp2`):

```bash
git checkout main
git pull origin main
git checkout -b claude/p3-1-fluid-dynamics-retrofit
```

Open the PR as ready for review (not draft).
