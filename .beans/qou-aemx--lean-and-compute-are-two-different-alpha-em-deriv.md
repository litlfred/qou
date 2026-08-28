---
# qou-aemx
title: 'The Lean and the compute are two DIFFERENT alpha_em derivations (470 ppb apart); the scorecard rests on the one the paper does not cite'
status: todo
type: task
priority: high
created_at: 2026-08-28T16:32:49Z
updated_at: 2026-08-28T16:32:49Z
---

Found while re-examining the two open knobs on `m_K/m_pi` (the framework's
only scoreable L2 result). Probe:
[`computations/alpha_em_lean_vs_compute_divergence_probe.py`](../computations/alpha_em_lean_vs_compute_divergence_probe.py).
Audit: `docs/audits/2026-08-28-alpha-em-lean-vs-compute-divergence.md`.

## The finding

Two constructions of `alpha_em^-1` live in the corpus and share **no**
ingredient:

| | prefactor | kappa | value | vs CODATA |
|---|---|---|---|---|
| `em-coupling-chern-simons.lean` | `45*[3]_q` = 136.9668 | `8*q` = 8.8798 | 137.035999532 | **+2.59 ppb** |
| `meson_em_sinh_closed_form.py` | `q*[9]_q*[10]_q` = 136.8232 | det ratio = 1.7216 | 137.035935094 | **-467.6 ppb** |

Prefactors differ by 1049 ppm; the kappas by a factor of 5.16; the results by
470 ppb.

Three consequences:

1. **The cited formalisation is not the computation.**
   `per_observable_100x_status.py` imports `alpha_em_inv_derived`, i.e. the
   -467.6 ppb one. So "m_K/m_pi is conditional on the Chern-Simons conjecture
   class in `em-coupling-chern-simons.lean`" names a premise the number does
   not rest on.
2. **The empirical form fits 180x better.** The .lean's own docstring says
   `kappa = 8q` is empirical -- *"The '8 = dim(su(3)) = gluon octet'
   interpretation is post-hoc; no structural derivation links su(3) gluon
   dimension to alpha_EM."* The derived Gram-ratio form is the one 467 ppb out.
   A more-empirical construction fitting better is the anti-fit signature.
3. **The .lean docstring contradicts its own def.** It describes kappa as "a
   Gram-determinant ratio from the Chern-Simons ..." while the `def` is
   `8 * q`. The producer computes the actual determinant ratio: 1.7216.

## What is NOT claimed

Not that either is wrong -- that is the open question. Not that the scorecard
moves: it does not, this is about what the number is conditional ON.

## Corrections to the red-team audit (2026-08-22) this implies

- **"imports experimental alpha_em" is STALE.** The literal
  `mp.mpf("137.035944")` is gone; alpha_em is computed from framework objects.
- **"conditional on an open Lean `sorry`" is STALE IN MECHANISM.**
  `em-coupling-chern-simons.lean` compiles exit 0 with **zero** sorries; the
  single `sorry` token in it is the word inside a comment describing its own
  past. It carries two unproved conjecture *classes* with no instance.
  **The epistemic status is UNCHANGED** -- a class-axiomatised conjecture is not
  a proof (AGENTS.md "Axiomatization is NOT a Proof") -- so **0/5 unconditional
  still stands**. Do not report the missing `sorry` as an improvement.

## Next

Decide which construction is canonical, or establish that they are the same
object under a reparametrisation (the 1049 ppm prefactor gap says they are not).
Until then the corpus asserts two incompatible alpha_em values.
