---
# qou-looi
title: compound_shift_nf carried the 2026-05-19 TR_M[5] bug for 3 months after gram.py was fixed
status: completed
type: task
priority: normal
created_at: 2026-08-30T03:02:22Z
updated_at: 2026-08-30T03:03:04Z
---

## The bug

`computations/compound_shift_nf.py::tr_m_weights_mp` returned

    TR_M = [1, z, z, z^2, z^2, z^3]

The last entry is for `NF_BASIS[5] = (0,1,0) = sigma_0 sigma_1 sigma_0` (`e^-`).
The Markov recursion gives **h*z^2 + z**, not z^3. This is the 2026-05-19
TR_M[5] bug (`docs/audits/2026-05-19-trm5-markov-bug.md`) — the same defect,
in a second file, **three months after the fix landed in
`tools/pyhecke/python/pyhecke/gram.py`**.

The file's own comment at NF_BASIS says it "matches pyhecke.gram &
hecke_core_symbolic conventions". It did not.

## Why the gate never caught it

The registry validator's R11 rule exists for exactly this ("It has a track
record. TR_M[5] was z^3 rather than h*z^2+z until…"), but R11 is
**registry-driven**: it checks derived quantities that are registered in
`docs/coordination/trace-convention-registry.json`. `compound_shift_nf` is not
registered, so the gate could not see it. A detector that only inspects what
is declared to it cannot find an undeclared instance — the same shape as the
convention-C detector-blindness taxonomy.

## Magnitude — not a rounding-scale defect

At the substrate the two values differ by **4.4x**:

    z^3        = 0.124490943242
    h*z^2 + z  = 0.551443414318

## Blast radius, measured

`tr_m_weights_mp` is called at three sites inside its own file (the Gram
build, the LP `n_target`, and `cat_mass = sum(nf_mp[i] * tr_w[i])`), and by
one external consumer, `computations/probes/ground_state_ordering_a3_probe.py`.

Re-running the producer after the fix moved **114 fields** of the committed
`compound-shift-nf.witness.json`:

    categorical_mass   0.2902825133592566 -> 0.2533772638013514   (-12.7 %)
    y0_star           -0.798459866213944  -> -10.07772160280673   (LP dual)
    y_star[0]          0.167807744674391  ->   6.16059988673509
    x_star[0]          0.196554823401574  -> -15.25883677278375

The LP duals move by more than an order of magnitude. Per the LP/SDP-duals
rule in AGENTS.md these shadow prices are the binding-energy structure, so
this is not a cosmetic delta.

## Verification

1. **Baseline established first**: re-running the producer BEFORE the fix
   reproduced the committed witness with **0** differing fields (modulo
   volatile keys), so the deltas above are the fix and nothing else.
2. **The corrected form matches the canonical source**: `pyhecke/gram.py:220`
   is `TR_M = np.array([1.0, z, z, z**2, z**2, h * z**2 + z])` — identical
   shape. This is the check that settles it; the audit doc alone would have
   been a secondary source.
3. The correction is **convention-independent** — the Markov recursion gives
   h*z^2 + z for any z. This file is separately convention C, which is a
   different question and stays open (bean `qou-t9r1`).

## Caveat on the witness diff

One moved field, `/environment/pyhecke_native_build`, is an environment stamp
from the re-run rather than an effect of the fix.
