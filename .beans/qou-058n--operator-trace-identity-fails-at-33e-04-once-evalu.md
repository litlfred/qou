---
# qou-058n
title: operator-trace identity fails at 3.3e-04 once evaluated consistently in mpmath — tolerance is 1e-6
status: todo
type: task
priority: normal
created_at: 2026-08-22T20:59:12Z
updated_at: 2026-08-22T20:59:58Z
---

Found while draining `mass_tower_operator_valued` for `qou-ishr`. **This is a
negative result, not a drain artifact**, and it should be adjudicated by whoever
owns prop:mass-tower-operator-valued before anyone reads the witness as a pass.

## What the witness now says

    assertion  operator_trace_identity_forward
    computed   0.0003323927637415258486
    tolerance  1e-6
    passed     FALSE

The committed witness said `4.0077220649510574e-08`, **passed: true**.

## Why that committed value cannot be compared to this one

    committed mass-tower witness   2026-07-05          (seven weeks old)
    evaluate_word_matrix ported    2026-08-22 09:41    416285fc174 [qou-zck8]
    consumer re-run since          NEVER

And it could not have been: on `main` this producer **crashes**, because
qou-zck8 changed `evaluate_word_matrix` to return `mp.matrix` while the
consumer still called the numpy attribute `.size`:

    AttributeError: 'matrix' object has no attribute 'size'

So the 4.0e-08 was computed against the **old float64 upstream**, and nothing
has evaluated this identity against the current one until now.

## Ruling out my own conversion first

- `_kron_mp` and `_trace_prod_mp` were checked against `np.kron` / `np.trace`
  on a worked 4x4 case: **exact match**, both.
- The A-operator witness is **current**, not stale — regenerated in the very
  same commit as the qou-zck8 port, so the A side and the matrix side agree.
- `np.kron(mp.matrix, mp.matrix)` gives **`dtype=object`** and a flattened
  shape (measured). That is what the old code was feeding `np.trace`, then
  casting through `complex()` — so the old path had both an object-array
  detour and a float64 floor.

## What is actually open

Evaluated consistently at 50 dps, with a current A operator, the identity
`Σ_{(μ,ν)} Tr(A^λ_{μν}·(ρ_μ(β_p) ⊗ ρ_ν(β_n))) = χ^λ(β)` holds only to
**3.3e-04**, i.e. **332× outside its own stated tolerance**.

Either the tolerance was calibrated against float64 noise and the identity was
never this tight, or something in the A extraction is off. I did not widen the
tolerance and did not touch the threshold — that is the move this repo's
discipline explicitly forbids.

Note the sibling result for contrast: `sublemma_2_1_deuteron_branching`, drained
the same way in the same session, produces `max_rel = 1.83e-15` and passes
comfortably. So high-precision evaluation is not generically inflating residuals
in this chain — this one is specific.
