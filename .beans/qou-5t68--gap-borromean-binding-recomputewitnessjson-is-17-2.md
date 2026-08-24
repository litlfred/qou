---
# qou-5t68
title: 'GAP: borromean-binding-recompute.witness.json is 17-23% stale — and the assertion that should catch it passes because both sides are'
status: todo
type: task
priority: normal
created_at: 2026-08-24T10:01:14Z
updated_at: 2026-08-24T10:13:39Z
---

Found while converting `probe_9b_perlambda_brane_tower.py` for the convention-C
excision (`qou-cds1`, PR #5622). The conversion broke an assertion, and chasing
why produced this instead.

## The measurement

`computations/borromean_binding_recompute.py` re-run with **NO source change**:

    isotopes[0].B_can0            committed 2.0898131  ->  fresh 1.6166217   (-23%)
    isotopes[0].B_tower           committed 2.4802963  ->  fresh 2.0630769   (-17%)
    isotopes[0].delta_K_residual  committed 0.8968981  ->  fresh 1.0782792
    isotopes[1].B_can0            committed 3.5638785  ->  fresh 3.1372256
    isotopes[1].B_tower           committed 4.9190261  ->  fresh 4.7419664

26 fields total. The producer is convention **D** and says so explicitly
(`borromean_binding_recompute.py:111` `z = q**3/(q**2+1)`; docstring at :123-124
"y_(1^3) = 0; z = q^3/(q^2+1) ... NOT convention C"). The COMMITTED witness is a
stale convention-C-era artifact.

## Why nothing caught it

`probe_9b_perlambda_brane_tower.py` carries an assertion named exactly for this:

    scalar_baseline_matches_committed_witness
    computed=max_base_dev, expected=0.0, tolerance=1e-6
    source="scalar Jones tower vs borromean-binding-recompute.witness.json
            per-isotope B_tower (q-string precision difference only)"

It PASSES, at **computed = 0.0 exactly**. It passes because probe_9b was ALSO
convention C, so a C-frame scalar tower was being compared against a C-era
committed witness. Two stale things agreeing is not a check.

Converting probe_9b to D flips it: computed 0.0 -> 0.17767, passed True ->
False. The assertion only became informative once one side moved.

## Ordering consequence for the excision

`probe_9b` CANNOT be converted before its upstream is refreshed. The correct
order is:

  1. refresh `borromean-binding-recompute.witness.json` (producer re-run, no
     source change) -- a 17-23% value movement in the BINDING channel;
  2. then convert `probe_9b` to D;
  3. the assertion should return to ~0 against D-vs-D.

Step 1 is deliberately NOT done in the excision PR. A 17-23% movement in
committed binding numbers deserves its own review with its own attribution, not
a footnote in a convention-migration commit. It is also plausibly the binding
channel owner's call rather than mine.

## Generalisation worth checking

Any assertion of the form "my value matches a committed upstream witness" is
only as good as that witness's freshness. If both sides drifted together the
assertion reports success. This one sat at EXACTLY 0.0, which reads as strong
agreement and was actually two stale artifacts matching. Worth sweeping for
other `*_matches_committed_*` assertions on the same pattern.


## Sweep result (2026-08-24): this is ISOLATED, not a class

I flagged in the commit message that *"any assertion of the form 'my value
matches a committed upstream witness' is only as good as that witness's
freshness"* and said it was worth sweeping. Swept. **It is one site.**

Name-shaped grep (`matches_committed|_vs_committed|committed_witness`) over
`computations/` returns 9 hits; the broad grep (files carrying both
`add_assertion` and a `committed`/`.witness.json` mention) returns 625, which
is noise — nearly every probe *mentions* a committed witness. Resolving the 9:

| site | shape | verdict |
|---|---|---|
| `probe_9b_perlambda_brane_tower.py:500` | fresh vs committed, **both convention C** | **the defect** (this bean) |
| `borromean_3d_index_graded.py:496` | fresh q-series vs `REF_I0_Q6`, a hardcoded exact-integer constant in the file | not vulnerable — integer coefficients, no z, no anchor |
| `qbeta_c3_ladder_trace_convention_sensitivity_probe.py:199` | C ladder vs committed C corpus values | **deliberate** — it is the named `C_frame_regression`, both sides C on purpose |
| `qbeta_dladder_ecalle_acceleration_probe.py:591` | symbolically **rebuilds** the ladder (~1-2 min) and compares exact ℚ pairs | genuine recomputation; C-frame scoping is a `qou-cds1` question, not staleness |
| `qbeta_5two_barodd_antisym_offdiagonal_probe.py:164` | see below | real content, **mislabelled** |
| `qbeta_c3_qstar_k31_repin_probe.py:257`, `habiro_witness_convention_adjudication_probe.py:353` | `add_data` fields, not assertions | n/a |
| `gen_q0_anchor_manifest.py`, `ground_state_ordering_a3_probe.py:852` | enumeration / presence flags | n/a |

So the answer to my own question is **no class** — `probe_9b` stays the one
blocked conversion, and the excision does not need to widen.

## One incidental finding (small, separate)

`qbeta_5two_barodd_antisym_offdiagonal_probe.py:152` — I initially read this as
a tautology and **that was wrong**; recording the correction because the near
miss is the same error this bean is about. Both `N` and `N_odd` are read from
the *one* GK witness, which looks like `x == x`. It is not, because the two are
not built the same way:

    producer:  N   = Winv · Bm · Wq^T          N_odd = ½(N − Nt),  Nt = Wq · Bm · Winv^T
    consumer:  compares N_odd against ½(N − N^T)   -- the true matrix transpose

`N^T = Wq · Bm^T · Winv^T`, so `Nt = N^T` **iff `Bm` is symmetric**. The gate
therefore certifies the symmetry of the B-matrix — real content that can fail.

What is wrong is only its `source` string, which claims it shows *"the committed
antisymmetric assembly IS the block home of the ι-odd off-diagonal
contraction"*. It shows no such thing; it shows `Bm = Bm^T`. Cosmetic, no
number moves, not worth a commit on this branch — noted here so the next reader
of that probe does not inherit the stronger reading.
