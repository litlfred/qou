---
# qou-iagg
title: Re-score the Q_β / m_n / Δ_pn dashboard rows a SECOND time once a c_k ladder exists on the z_D base
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-12T17:55:54Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---

**Owner-authorised 2026-09-12.** Asked whether item (iii) of the 2026-09-08
ruling should re-score now or wait for the ladder, the owner picked **both**
"re-score now to z_D" and "re-score after qou-pdix". Read as: move the rows to
the ruled base immediately (done, PR #7221), **and** re-score again once a
`c_k` ladder exists on that base. This bean is the second half.

**Blocked on:** `qou-pdix` (the phase question) → `qou-cds1` (the ladder
re-derivation on the z_D base). Nothing to do here until a ladder exists; this
is not idle-pass work.

**What the first re-score published**, so the delta is measurable when the
ladder lands (`per-observable-100x-status.witness.json`, 2026-09-12):

| row | err_ppb on the ruled z_D base | miss factor |
|---|---|---|
| `Q_β` | 4.316e+8 | 5.535e+7 |
| `m_n` | 3.594e+5 | 7.034e+7 |
| `Δ_pn` | 2.611e+8 | 6.021e+7 |

These carry **zero rungs**. On the retired `z = 1` base the five rungs bought
1 677 569 → 37.7 ppb, about 4.5 orders, so a z_D ladder could move all three a
long way. That is precisely why the figures above must not be quoted as
"convention D's accuracy" — see the note the producer now writes onto each row.

**Where the wiring already is.** `per_observable_100x_status.py::_qbeta_ruled_base()`
evaluates `|tr_M(Δ_S)(z_D)|·E₀` from q₀ alone and is calibrated against
`qbeta-published-form-is-the-inadmissible-z1.witness.json`. When the ladder
exists, the change is to apply its rungs to that base — the base itself needs
no rework, and `ck_rungs_applied: 0` in the emitted block is the field that
flips.

**Do not** apply the existing `c_k` ladder to the z_D base as a shortcut. It
was derived in convention C on the `z = 1` cell, and
`QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (sorry-free) makes the C-frame
ladder and the mass channel's three-row forcing mutually exclusive — so
substituting `z_D` into it is not a valid move. That is the whole content of
`qou-cds1`.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: BLOCKED.** Blocked on qou-cds1, not on qou-pdix. Because of the proved ladder-form exclusion it may never unblock in the current form. The recorded baseline has moved (Q_β now 1.668e8 ppb on the scored cell), so re-read the witness rather than this table.

Evidence: Waits for a c_k ladder on the z_D base (qou-cds1). Its stated chain "pdix → cds1" is wrong on the ruled base (see cds1 row). The "first re-score" figures it records (Q_β 4.316e8 ppb) are already stale: the live witness has Q_β err_ppb 1.668e+8 at the scored cell (pred 0.651856 MeV) and m_n 1.389e+5. `ck_rungs_applied: 0` is still the field that would flip.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
