---
# qou-0gqn
title: 'STALE: canonical-with-proper-tower.witness.json does not reproduce -- E_0 collapses 3.59e6x, taking every B_MeV with it'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-28T20:29:47Z
updated_at: 2026-10-04T15:24:36Z
parent: qou-5vkl
---

MEASURED 2026-08-28 on branch `claude/witnessbuilder-provenance-migration-2026-08-28`.
Found incidentally: the file was swept into a migration commit by a sample re-run
and had to be reverted, which is how the delta surfaced.

## What was measured

`computations/canonical-with-proper-tower.witness.json` as committed (timestamp
`2026-06-14T01:35:07Z`) does not reproduce from today's tree. Committed vs a
fresh run on `main`+this branch, all 16 result rows:

    field                    committed        fresh          rel move
    m_atom_per_irrep_total   6.30 .. 30.75    3.56 .. 19.88  0.35 - 0.45
    m_free_per_irrep_total   8.40 .. 49.53    4.96 .. 33.13  0.33 - 0.43
    E_0_MeV_per_cat          243.5284428      6.788428e-05   1.00
    E_0_MeV_per_cat (mode2)  249.4029733      1.200143e-04   1.00
    B_MeV                    510 .. 6218      9.5e-5 .. 2.8e-3

## The B_MeV collapse is entirely E_0's

`B_MeV = (m_free - m_atom) * E_0` holds in both files:

    committed  (8.396533659 - 6.302378037) * 243.5284428 = 509.986   (matches)
    fresh      (4.964617151 - 3.561992542) * 6.788428e-05 = 9.5216e-5 (matches)

So there are two independent moves, not one:

  1. the per-irrep mass totals moved ~40 % -- consistent in sign and rough
     magnitude across every row;
  2. `E_0_MeV_per_cat`, a single scalar shared by all rows within a `pair_mode`,
     collapsed by **3.587e6** (243.5284428 -> 6.788428e-05) and by **2.078e6**
     in the other mode. A clean 6-order collapse of one shared scalar reads like
     a unit or normalisation change upstream, not accumulated drift.

The fresh run also serialises these as `_precision.fmt` STRINGS where the
committed file has float64 numbers, i.e. the NO-FLOAT64 discipline has since
reached this producer's cone. That is a separate, expected change and is not
the cause of either move.

## Scope -- what this does NOT establish

scope-(a). This says the committed artifact does not reproduce. It does **not**
say which set of numbers is right, and both look wrong on their face: a light
nucleus does not have a 4573 MeV binding energy (committed) and does not have a
9.5e-5 MeV one (fresh). This is an exploratory tower probe, not production
compute, so "neither is a physical binding energy" is not itself news -- the
finding is that the file's own numbers are no longer derivable from its own
producer.

I did NOT bisect the cause. `E_0` is the thing to chase first, because it is one
scalar and it carries the whole B_MeV story.

## Relation to qou-wlaf

Same class, different artifact. `qou-wlaf` is
`probes/gram-norm-binding-probe.witness.json` failing its own cross-check
assertion by seven orders. This is a second instance in the same population
(June-era binding witnesses that stopped reproducing), which is weak evidence
that the population is larger than the two known members -- but only weak: two
is two, and I have not swept for more.

## Next step

1. Locate what sets `E_0_MeV_per_cat` in the producer and diff that expression
   against its June version (`git log -p` on the producer since 2026-06-14).
2. Decide whether this probe is still wanted at all before regenerating it -- a
   regenerated exploratory witness that nothing consumes is churn, and the
   committed one at least records what was believed in June.


---

## DIAGNOSED 2026-08-29 — PR #5940, branch `claude/tower-e0-collapse-2026-08-29`

Probe: `computations/probes/tower_e0_pole_conditioning_probe.py` (5/5 pass).

### Root cause

`phi_q_safe` clamps to `cap_frac * q` to hold its argument off the pole at
`|z| = q`. With `cap_frac = 0.98` and `q = 1.1099785828` the cap is **1.0877790**.
The proton's canonical `V_hat = [0.66295, 1.06463]`, and the larger entry is
**95.91 % of q — BELOW the cap**. The clamp never fires; Phi_q is evaluated
essentially at its singularity and returns **7.81e6** for that one generator,
against the ~3.85 total the June witness implies.

The cap does not regularise this. It bounds Phi_q at 2.66e7 — still seven orders
above the June total — so it relocates the blow-up rather than removing it.
Across the whole band it declares safe, `[0.90, cap]`, Phi_q spans a factor 303.

### The point is ill-conditioned

A **0.188 % change in V_hat moves Phi_q by 9.06 %** — a **48x** relative-error
amplification, inherited whole by `E_0 = M_P / Phi_q`. Recomputed in mpmath at
50 dps, not through the float64 function under test.

### Causes EXCLUDED (checked, not assumed)

1. **`8cf5569648`, the Lean towerTerm swap — NOT the cause.** It deliberately
   pins the calibration to `term="phi_q"`, and `_tower_spec` threads `cap_frac`
   faithfully. The calibration uses the same function June used.
2. **Caches — not the cause.** `_E0_PI_CACHE` / `_E0_TOWER_CACHE` are both keyed
   by `pair_mode`.
3. **`full` == `adjacent` today is CORRECT, not a defect.** The calibration is
   A=1, one generator, so there are no pairs and `pair_mode` is a no-op by
   construction. June's two DISTINCT values (243.5284 / 249.4030) are the thing
   that wants explaining.

### The V_hat moved too

Reproducing June's total via Phi_q needs `V_hat = 0.14317` (12.90 % of q), 7.4x
smaller than today's 1.06463. `tower_term_li2q` on today's V_hat gives
`E_0 = 649.44`. **Neither current term at today's V_hat reproduces the witness.**

### Still open

* **Which commit moved V_hat.** Bisect not done. `23b9c4f5ba perf(qou-9ohz): the
  A>=3 V_hat is a scalar collapse` is a candidate but is scoped to A>=3 and the
  calibration is A=1, so it is not an obvious fit.
* **Whether Phi_q is the right form for the mass context at all.** Tightening
  `cap_frac` does not obviously help — it only moves where the clamp bites, and
  the clamped value is itself 7 orders from the target. `tower_term_li2q` gives
  a sane 1.44 on the same V_hat. That is a design call for the owner, not a bug
  fix, and I have not made it.

### Method note

My first draft claimed "0.09 % -> 9.1 %, ~100x". That compared a two-sided Phi_q
change against a one-sided V_hat window and doubled the factor. The probe's own
threshold (`amp > 50`) failed at 48.24 and forced the correction. Recorded in the
module docstring so the wrong figure cannot be re-derived from an old draft.


---

## DIAGNOSED 2026-08-29 — PR #5940, branch `claude/tower-e0-collapse-2026-08-29`

Probe: `computations/probes/tower_e0_pole_conditioning_probe.py` (5/5 pass).

### Root cause

`phi_q_safe` clamps to `cap_frac * q` to hold its argument off the pole at
`|z| = q`. With `cap_frac = 0.98` and `q = 1.1099785828` the cap is **1.0877790**.
The proton's canonical `V_hat = [0.66295, 1.06463]`, and the larger entry is
**95.91 % of q — BELOW the cap**. The clamp never fires; Phi_q is evaluated
essentially at its singularity and returns **7.81e6** for that one generator,
against the ~3.85 total the June witness implies.

The cap does not regularise this. It bounds Phi_q at 2.66e7 — still seven orders
above the June total — so it relocates the blow-up rather than removing it.
Across the whole band it declares safe, `[0.90, cap]`, Phi_q spans a factor 303.

### The point is ill-conditioned

A **0.188 % change in V_hat moves Phi_q by 9.06 %** — a **48x** relative-error
amplification, inherited whole by `E_0 = M_P / Phi_q`. Recomputed in mpmath at
50 dps, not through the float64 function under test.

### Causes EXCLUDED (checked, not assumed)

1. **`8cf5569648`, the Lean towerTerm swap — NOT the cause.** It deliberately
   pins the calibration to `term="phi_q"`, and `_tower_spec` threads `cap_frac`
   faithfully. The calibration uses the same function June used.
2. **Caches — not the cause.** `_E0_PI_CACHE` / `_E0_TOWER_CACHE` are both keyed
   by `pair_mode`.
3. **`full` == `adjacent` today is CORRECT, not a defect.** The calibration is
   A=1, one generator, so there are no pairs and `pair_mode` is a no-op by
   construction. June's two DISTINCT values (243.5284 / 249.4030) are the thing
   that wants explaining.

### The V_hat moved too

Reproducing June's total via Phi_q needs `V_hat = 0.14317` (12.90 % of q), 7.4x
smaller than today's 1.06463. `tower_term_li2q` on today's V_hat gives
`E_0 = 649.44`. **Neither current term at today's V_hat reproduces the witness.**

### Still open

* **Which commit moved V_hat.** Bisect not done. `23b9c4f5ba perf(qou-9ohz): the
  A>=3 V_hat is a scalar collapse` is a candidate but is scoped to A>=3 and the
  calibration is A=1, so it is not an obvious fit.
* **Whether Phi_q is the right form for the mass context at all.** Tightening
  `cap_frac` does not obviously help — it only moves where the clamp bites, and
  the clamped value is itself 7 orders from the target. `tower_term_li2q` gives
  a sane 1.44 on the same V_hat. That is a design call for the owner, not a bug
  fix, and I have not made it.

### Method note

My first draft claimed "0.09 % -> 9.1 %, ~100x". That compared a two-sided Phi_q
change against a one-sided V_hat window and doubled the factor. The probe's own
threshold (`amp > 50`) failed at 48.24 and forced the correction. Recorded in the
module docstring so the wrong figure cannot be re-derived from an old draft.


---

## DIAGNOSED 2026-08-29 — PR #5940, branch `claude/tower-e0-collapse-2026-08-29`

Probe: `computations/probes/tower_e0_pole_conditioning_probe.py` (5/5 pass).

### Root cause

`phi_q_safe` clamps to `cap_frac * q` to hold its argument off the pole at
`|z| = q`. With `cap_frac = 0.98` and `q = 1.1099785828` the cap is **1.0877790**.
The proton's canonical `V_hat = [0.66295, 1.06463]`, and the larger entry is
**95.91 % of q — BELOW the cap**. The clamp never fires; Phi_q is evaluated
essentially at its singularity and returns **7.81e6** for that one generator,
against the ~3.85 total the June witness implies.

The cap does not regularise this. It bounds Phi_q at 2.66e7 — still seven orders
above the June total — so it relocates the blow-up rather than removing it.
Across the whole band it declares safe, `[0.90, cap]`, Phi_q spans a factor 303.

### The point is ill-conditioned

A **0.188 % change in V_hat moves Phi_q by 9.06 %** — a **48x** relative-error
amplification, inherited whole by `E_0 = M_P / Phi_q`. Recomputed in mpmath at
50 dps, not through the float64 function under test.

### Causes EXCLUDED (checked, not assumed)

1. **`8cf5569648`, the Lean towerTerm swap — NOT the cause.** It deliberately
   pins the calibration to `term="phi_q"`, and `_tower_spec` threads `cap_frac`
   faithfully. The calibration uses the same function June used.
2. **Caches — not the cause.** `_E0_PI_CACHE` / `_E0_TOWER_CACHE` are both keyed
   by `pair_mode`.
3. **`full` == `adjacent` today is CORRECT, not a defect.** The calibration is
   A=1, one generator, so there are no pairs and `pair_mode` is a no-op by
   construction. June's two DISTINCT values (243.5284 / 249.4030) are the thing
   that wants explaining.

### The V_hat moved too

Reproducing June's total via Phi_q needs `V_hat = 0.14317` (12.90 % of q), 7.4x
smaller than today's 1.06463. `tower_term_li2q` on today's V_hat gives
`E_0 = 649.44`. **Neither current term at today's V_hat reproduces the witness.**

### Still open

* **Which commit moved V_hat.** Bisect not done. `23b9c4f5ba perf(qou-9ohz): the
  A>=3 V_hat is a scalar collapse` is a candidate but is scoped to A>=3 and the
  calibration is A=1, so it is not an obvious fit.
* **Whether Phi_q is the right form for the mass context at all.** Tightening
  `cap_frac` does not obviously help — it only moves where the clamp bites, and
  the clamped value is itself 7 orders from the target. `tower_term_li2q` gives
  a sane 1.44 on the same V_hat. That is a design call for the owner, not a bug
  fix, and I have not made it.

### Method note

My first draft claimed "0.09 % -> 9.1 %, ~100x". That compared a two-sided Phi_q
change against a one-sided V_hat window and doubled the factor. The probe's own
threshold (`amp > 50`) failed at 48.24 and forced the correction. Recorded in the
module docstring so the wrong figure cannot be re-derived from an old draft.

- **Round 91 (`https://github.com/litlfred/qou/pull/8413`, head `1d95d75db1b41a96e3b4987d5771f9fd945187c9`)**: Formalized theorem + 80-dps witness (`status: in-progress`).
