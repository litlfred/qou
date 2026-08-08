---
# qou-t4cv
title: 'VACUITY: LiftingDescent ''open inputs'' are tautologies (zero-count / unit definitions)'
status: todo
type: task
created_at: 2026-08-08T09:07:46Z
updated_at: 2026-08-08T09:07:46Z
---


## Finding

Three `QOU/LiftingDescent/tm_*.lean` files declare theorems labelled
**"Open input 1/2/3"** whose docstrings explicitly say *"body is `sorry`"*.
None of them contains a `sorry`. They are discharged by defining the objects
so the statement collapses:

```lean
def descendedBlowupCount : ℕ := 0        -- ⇒ ∏ over Finset.range 0 is the empty product
def descendedMIdisc (i : ℕ) : ℝ := 1     -- ⇒ "disc contribution is trivial" is rfl
def descendedMI : ℝ := unknotHolonomy
def descendedMIcore : ℝ := unknotHolonomy

theorem descended_MI_factorises :
    descendedMI = descendedMIcore * ∏ i ∈ Finset.range descendedBlowupCount, descendedMIdisc i := by
  simp [descendedMI, descendedMIcore, descendedBlowupCount]
```

That statement reduces to `unknotHolonomy = unknotHolonomy * 1`. It does not
prove Yekutieli multiplicativity over a blow-up decomposition; it proves
`x = x` after the decomposition has been defined empty.

Same shape:

- `tm_descended_is_holonomy` — `descendedBlowupCount := 0`,
  `descendedMIdisc := 1`; `descended_exceptional_disc_trivial` is `intro i; rfl`.
- `tm_transient_localisation` — `transientBlowupCount := 0`, same collapse.
- `tm_dilogarithm_evaluation` — `Phi_q w = ∫ … := rfl` is a definitional
  restatement presented as "Integral representation of `Φ_q`".

This is the AGENTS.md §1a / §Strict Lean Discipline item 5 anti-pattern:
tautological conclusions that assert nothing falsifiable about the domain.
The docstrings are honest about the intent (`body is sorry`); the code is not.

## Why this is being recorded now

**Pre-existing — not introduced by the namespace-drift sweep (PR #4722).** But
that sweep repaired the forward-reference errors in these files, so they now
build lean-direct at `sorry=0`. A green, sorry-free module here **overstates**
soundness: the sweep fixed the compile errors and in doing so removed the only
outward signal that anything was wrong.

## Honest disposition (per §1a)

For each of the three "open inputs", one of:

1. **State it for real and `sorry` it** with a `-- Ref:` citation — the honest
   "stated, not yet proved" marker. This is almost certainly the right call:
   the docstrings already say that is the intent.
2. **Demote to a `conjecture` carrier** with content-bearing fields.
3. **Prove it** for a genuinely non-empty blow-up decomposition — i.e. stop
   defining `*BlowupCount := 0`.

Do **not** simply leave them: they currently read as proved.
