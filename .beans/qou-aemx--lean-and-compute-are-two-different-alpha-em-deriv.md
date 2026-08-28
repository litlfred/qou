---
# qou-aemx
title: 'The Lean and the compute are two DIFFERENT alpha_em derivations (470 ppb apart); the scorecard rests on the one the paper does not cite'
status: in-progress
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


## 2026-08-28 — half answered: NOT one object; and my own emphasis corrected

**"Are they the same object under a reparametrisation?" — NO, settled
symbolically.** Lean's prefactor is `45(q⁶−1)/(q²(q²−1))`; the compute's is a
degree-32 cyclotomic product over `q¹⁶`. They differ by 1.5× at q→1 and by
~1973× at q=2, and **cross at q\* = 1.11015574, 0.016 % from q₀**. The 1049 ppm
agreement is where the crossing sits, not shared structure — and is expected,
since both target ≈137 near the same point.

**Genericity test on both κ** (window giving |err| < 100 ppb):

| | claimed | window | width | % of claimed | inside? |
|---|---:|---|---:|---:|:--:|
| Lean `8q` | 8.8798 | [8.4744, 9.2648] | 0.790 | 8.9 % | yes |
| compute Gram | 1.7216 | [1.8739, 1.9567] | 0.083 | 4.8 % | no |

- `8q` is **in range, not forced** — the window also admits the integer 9
  (33 ppb).
- But bare `κ = 8`, the file's own *"dim su(3) gluon octet"* reading, gives
  **−220 ppb and misses**. The `q` factor does the work, not the 8.
- The Gram κ misses a *relatively tighter* window by 10 % — behaving like a
  prediction that is not quite right.

**RETRACTING MY OWN EMPHASIS.** The original entry (and PR #5886's body) called
the 181× gap an *"anti-fit signature pointing the wrong way"*. Over-stated: a
loosely-constrained empirical parameter beating a tightly-constrained derived
one is near what neutral assumptions predict. The measured facts stand; the
inference from them does not. Corrected in audit §8.

## Still open — the canonical question

Which construction is canonical is **not** settled. What is settled is that the
choice is real (they are different objects), and that the derived one is the
one making a falsifiable, currently-failing claim. Deciding it needs an owner
or a structural argument for one prefactor over the other — `45·[3]_q` vs
`q·[9]_q·[10]_q` — which nothing in the corpus currently supplies.


## 2026-08-28 (later) — the `8` IS structural, and I withdraw "nothing in the corpus argues"

I closed the previous entry with *"nothing in the corpus argues for `45·[3]_q`
over `q·[9]_q·[10]_q`."* I had not run all six grep paths. Running them:

**`8 = Vol(𝓑₃)/G`, exactly.** The Borromean rings `L6a4` — this framework's
**nucleon** knot — have `Vol = 2·V_oct = 8G` with `V_oct = 4G`, G Catalan.
Machine-checked to 30 digits; residual exactly 0. Already live and
load-bearing: the nucleon row of `fundamental-knots-operator-basis`, and the
binding scale `α = m_e·8G` in `binding-knots-visual-inventory`. And stated as
the κ reading outright in
`computations/_deprecated/alpha_em_q9_q10_derivation.py`: **`κ = 8q =
q · Vol(𝓑₃)/G`**.

**The live `.lean` carried the weaker of two available readings** — `dim su(3)
= gluon octet`, which it correctly called post-hoc — while the corpus held an
exact one it did not cite. Docstring corrected this tranche, caveats kept.

**This revises my own §7 framing.** *"The q does the work, not the 8"* is wrong
under the corpus reading: `q·Vol(𝓑₃)/G` is **one object**, so the `q` is part
of the claimed structure. Bare `κ = 8` missing at −220 ppb is *consistent with*
that, not damaging to it. The measurement is unchanged.

**A chronology also exists, and I missed it.** The same deprecated file shows
`45·[3]_q` **replaced** `q·[9]_q·[10]_q` — *"REFINED FORMULA (replaces the
troublesome 1.6 mystery constant)"*, the older form's correction needing a
`1.6` that PSLQ could not identify. So **production compute uses the superseded
prefactor**, now with a Gram κ instead of the 1.6 — a later, different
development.

## Still open, and now sharper

1. **The combination.** The identity fixes the `8`; it does not fix the power
   of `q` multiplying it. `Vol/G` and `q²·Vol/G` are not excluded.
2. **The cross-sector step — the load-bearing gap.** Why should a **nucleon**
   knot's volume set a coefficient in an **electromagnetic** coupling? Nothing
   found addresses this.
3. **Genericity unmoved.** κ ∈ [8.474, 9.265] still admits the integer 9
   (33 ppb): `8q` is in range, not forced.
4. **Does the revival supersede the supersession?** `q·[9]_q·[10]_q` was
   retired for needing an unidentifiable constant, then revived with a derived
   Gram κ. Whether that reinstates it is the canonical question, still open.
