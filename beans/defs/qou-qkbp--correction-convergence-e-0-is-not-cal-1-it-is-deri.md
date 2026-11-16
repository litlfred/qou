---
# qou-qkbp
title: 'CORRECTION + CONVERGENCE: E_0 is NOT CAL-1 — it is derived as m_e.c_q^2.hbar_q = the energy of one Hecke reduction step, which is exactly what log_z tr_M counts. Remaining freedom is the ~1% brane-tower truncation, and the two derived forms BRACKET the measured peak.'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T06:17:21Z
updated_at: 2026-11-16T18:02:18Z
parent: qou-wp3h
---

`computations/qbeta/qbeta_e0_is_derived_probe.py` (6/6).

## 1. The correction

`qou-59j5` closed with *"E_0 is the corpus's, but it is CAL-1, a calibration, not
a derivation. So neither side is pinned, and until one is, no N× claim about the
extensive term means anything."* **That is a mislabel.**
`folio/quantum-observable-universe/nuclear-interactions/energy-scale-planck.md`
(`rem:energy-scale-planck`) derives the form from two independently defined
substrate constants:

    c_q = 1/(q-1)      hbar_q = (q-1)/q      t_P = 1/hbar_q
    E_0 = m_e . c_q^2 . hbar_q = m_e/(q-1)^2 . (q-1)/q = m_e/(q(q-1))

Verified identical at 30 dps. So `q(q-1)` is `c_q^-2 . hbar_q^-1`, a product of
constants that exist anyway — not a shape reverse-engineered to land. `m_e` is
CAL-1, `q_0` is fixed by CAL-2 (`m_mu/m_e`), and `E_0` consumes no further
calibration; `calibration-inputs.md` says so explicitly ("framework-derived from
(m_e, q_0) ... a cross-check, not a fourth calibration").

The algebra is dimensionless, so ONE dimensionful anchor is unavoidable — a
necessity, not a defect. The only question was whether the FORM was derived, and
it is.

## 2. The convergence — the two sides of this arc meet

`rem:energy-scale-planck` reads `E_0` as **the energy of one Hecke reduction
step**, the cost of resolving a single `sigma^2 -> h.sigma + 1`.

This arc reached the same object from the trace: the Markov relation makes
`nu(x) = log_z tr_M(x)` the tower's additive counter, and `b_pp = z` is a derived
identity, so **a p-p bond IS exactly one Markov reduction**. Hence

    B = E_0 . (number of reduction steps)

is the framework's own reading of the additive law, not a functional imposed on
it — and that is *why* the law is extensive. Neither side showed this alone.

## 3. What is actually left

Two DERIVED values, differing by the brane-tower truncation:

    E_0^(N=0) = 4.185981 MeV      E_0^full = E_0/(1-hbar_q^2) = 4.227483 MeV
    span 1.00991x = the block's own N=0 residual bound hbar_q^2/(1-hbar_q^2)

Against the measured peak `B/A = 8.794555` at `A = 62`, with `delta = [2]_q`
pinned (`qou-xf14`) and 3 strands/nucleon:

    3 . E_0^(N=0) . ln[2]_q = 8.772739   **-0.248 %**
    3 . E_0^full  . ln[2]_q = 8.859716   **+0.741 %**

**The two derived forms bracket the peak.** Neither is chosen here; the corpus's
binding pipeline uses N=0, which is why it is listed first.

## What this closes, and what it does not

**Closes:** the premise that the scale is an unpinned unit. Residual freedom is a
~1 % truncation ORDER, not a 33 % convention family (`qou-xf14`) and not an
arbitrary calibration.

**Does not close:** the factor of 3 — the colour tube is unrealisable in this
construction family (`qou-0c19`), and the 3 above is the strand count put in by
hand.

**Successor question:** decide N=0 versus tower-summed from the axioms. The
residual and the remaining freedom are both ~1 %, which is the same structural
situation `qou-59j5` flagged at 33 % — two orders of magnitude smaller, but not
gone.

## OWNER RULING 2026-09-05 — brane-tower axioms preferred

`E_0 = m_e.c_q^2.hbar_q/(1 - hbar_q^2) = 4.227483` MeV (tower-summed), not the
single-Planck-tick `4.185981`. The last ~1 % scale freedom is closed.

**Consequence, measured** (`qbeta_tower_ruling_bound_probe.py`, 6/6): the law
becomes ONE-SIDED. Nuclides whose measured binding exceeds `3.E_0.S` drop from
**10 to 1** of 2548, so under the ruling the additive law is an **upper bound on
nuclear binding for 2547 of 2548 measured nuclides**, saturated at the iron peak
to 0.6 % (Fe-54 0.9941, Ni-56 0.9938, Ni-58 0.9930, Co-55 0.9918).

The sign is right structurally: every SEMF correction SUBTRACTS from the volume
term, so a law omitting all of them belongs above the data. `E_0^(N=0)` sat below
the peak and let ten nuclides climb over it — the wrong position for this shape.

The sole exception is **4He at 1.0758** — the corpus's own most-worked anomaly
(19 open beans on the magic surplus: `qou-ooqh`, `qou-foh0`, `w5tg`, `qou-3wvl`,
`qou-guyb`). This is a STRUCTURAL argument, not a proximity one: boundedness is a
property of the whole table and cannot be tuned by moving a scale 0.99 % toward
one point.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Verification & Audit Note (2026-11-16 — Owner Ruling `Q-WP3H-1 = 1`)

- Verified on `main` that both probes and their witnesses are landed and current:
  1. `computations/qbeta/qbeta_e0_is_derived_probe.py` (+ `computations/qbeta/qbeta-e0-is-derived.witness.json`): landed in commit `b9c56a4a59` (`2026-09-05`, *"qou-qkbp: E_0 is NOT CAL-1 — it is derived, and it is the object this arc counts"*) and updated in `1f4123f29d` (`2026-10-13`, `q0Anchor: "proton"`).
  2. `computations/qbeta/qbeta_tower_ruling_bound_probe.py` (+ `computations/qbeta/qbeta-tower-ruling-bound.witness.json`): landed in commit `534794e799` (`2026-09-05`, *"Wrap up the binding-law arc: tower ruling adopted, sweep landed, synthesis written"*) and updated in `1f4123f29d` (`2026-10-13`).
- Kept at `status: in-progress` per owner rule (no unilateral bean closure; ready for owner review).
