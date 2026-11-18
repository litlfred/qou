---
# qou-a3lh
title: 'OWNER CALL: is a Z-clustered SnapPy pseudo-volume the right geometric input to A(K) at all?'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-09-12T20:15:44Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-v2om
---

**This is an owner decision, not agent work**, and it is the successor to
`qou-46ys` (the convention migration, which is complete — see PR #7240 §2).

**The decision.** The `A(K)` factor that every A3/A4 binding probe rests on is
proportional to a quantity the producers call `Vol_hyp`:

```
A(K) = VOL(K)/[8]_q · [3]_q^{2(Z−1)} · (√q + 1/√q)^{4N}
VOL = { D: 12.776,  ³He: 12.554,  ⁴He: 12.554 }
```

**Should `VOL` be this quantity at all?** Three measured facts say the question
is live (probe `a3_vol_is_pseudovolume_not_convention_probe.py`, 7/7):

1. **It is not a hyperbolic volume.** `2026-05-19-delta-lambda-thread-closure.md`,
   verbatim: *"Not legitimate hyperbolic volumes (degenerate tetrahedra)"*; they
   are *"SnapPy's pseudo-volume sum across the degenerate triangulation"*,
   encoding *"a combinatorial-braid invariant of the simplification path, NOT a
   Mostow-rigidity-protected hyperbolic invariant"*. So its value depends on the
   **triangulation simplification path**, which is not a knot invariant.
2. **It clusters by `Z`, not by knot.** `VOL(³He) == VOL(⁴He)` *exactly* while
   `VOL(D)` differs. `2026-06-05-gap-a4-L1-retrospective.md` already flagged this
   as *"suggesting they're not the genuine Path B `Vol(K)`"* and asked for a
   re-derivation. Unresolved since.
3. **It is a different object from the one you retired.** Your 2026-08-29 ruling
   retires `Vol(6₂) = 4.40083251612` and rules the canonical closure flat
   (`Vol = 0`). `12.776` is neither, and `12.776/4.40083 = 2.9031` is not an
   integer multiple — **so that ruling does not reach it.** Recorded because a
   reader meeting *"the deuteron binding is NOT a hyperbolic-volume term"* beside
   a variable named `Vol_hyp` will conclude it does.

**The four options, and what each costs.**

- **(A) Keep `VOL` as-is, relabel only.** *Means:* the pseudo-volume is accepted
  as the intended combinatorial invariant; only the name was wrong. *Costs:* the
  label fix is already done (#7240), so nothing further. *Risks:* a
  simplification-path-dependent number stays load-bearing in every A3/A4 probe.
  *Commits to:* defending "SnapPy's simplification path" as a derivation step.
- **(B) Re-derive `VOL` from the canonical braid closure under the production
  convention** — what the 2026-06-05 retrospective asked for. *Costs:* real
  compute, SnapPy on the canonical closures, plus re-running every A3/A4 probe.
  *Risks:* the values move, and every A3/A4 conclusion moves with them. *Commits
  to:* a geometric input that is a genuine invariant.
- **(C) Drop the volume factor entirely**, consistent with your 2026-08-29
  corollary that deuteron binding is not a volume term. *Costs:* `A(K)` loses its
  `VOL/[8]_q` factor and the whole A3/A4 family needs re-deriving. *Risks:*
  largest blast radius here. *Commits to:* sourcing binding from the
  Gram/Frobenius + confinement-SDP channel only, which is what that ruling names.
- **(D) Do nothing.** *Default:* `VOL` stays, correctly labelled as a
  pseudo-volume, and the A3/A4 probes keep reporting on it. Safe — nothing is
  currently quoted as a live result off them, since the A3 overshoot is already
  refuted and both its audits are bannered.

**Blast radius in real terms.** `VOL_PHASE4_Z1/Z2` is hardcoded in **8+**
producers/probes: `gap_a3_overshoot_robustness_check.py`,
`gap_a3_deuteron_A_D_overshoot.py`, `probes/gap_a3_plambda_bar_even_admissibility_probe.py`,
`probes/gap_a4_He3_residual_probe.py` (+`_perknot_rerun`),
`probes/gap_a4_cross_isotope_residual_probe.py`, `probes/gap_a4_S_K_additive_probe.py`.
None currently feeds a reader-facing prediction — the A3 overshoot is refuted and
the L2 dashboard's binding rows do not consume `A(K)`.

**My judgement, not a finding:** **(D) for now, (B) when the binding arc next needs
a real `A(K)`.** The refutation already removed the thing `VOL` was supporting, so
re-deriving it buys nothing until a live claim depends on it — and (C) is the
largest change of the four on the strength of an inference from a ruling that, as
measured above, does not actually reach this input.

**It also re-frames the A3 refutation:** if `VOL` is the wrong input, that negative
is about the **route**, not merely the convention frame. Worth knowing before
anyone re-attempts the trend.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `(none)` → `qou-v2om`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.

In-progress in Round 99 PR litlfred/qou#8444.
