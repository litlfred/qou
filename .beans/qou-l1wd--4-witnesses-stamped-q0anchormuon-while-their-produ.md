---
# qou-l1wd
title: 4 witnesses stamped q0Anchor=muon while their producer computes at proton
status: completed
type: task
priority: normal
created_at: 2026-08-17T01:44:20Z
updated_at: 2026-08-17T01:54:38Z
---

## Evidence (PR #5260, found while refuting bean qou-5axo)

Four witnesses record `q0Anchor: "muon"` and `parameters.q0` = the muon value,
while their producer computes at **proton**:

  binding-canonical, ame-2020-binding-energies   (binding_canonical.py)
  mass-table-comprehensive                       (mass_table_comprehensive.py)
  wedderburn-lp-ew-wiring                        (wedderburn_lp_ew_wiring.py)

`binding_canonical.py:65` is `from q_parameter import Q_MP as q0`, and `Q_MP`
is proton at runtime — verified directly:

    binding_canonical.q0 at runtime = 1.1099785827513808075916690956107688798745

`Q_MP` and `Q_50_DIGIT_STR` agree with each other and both resolve proton, and
the bridge calls pass `Q_50_DIGIT_STR`. Yet a **fresh** run still writes
`parameters.q0 = 1.10997859555733471989976322048322…` (muon) and
`q0Anchor: muon`. So the stamp is not merely stale-on-disk — the producer
re-emits it.

**Why nothing caught it.** `audits/q0_anchor_consistency_audit.py` classifies
`Q0_FLIP` by checking `q0Anchor` against `q0Value` — i.e. *internal* coherence.
Here both say muon, so the pair is self-consistent and the audit is satisfied;
it never compares either against the q the producer actually evaluated at.
`Q0_FLIP: 0` is therefore not evidence these are right.

**Not diagnosed further.** I did not establish WHERE the muon value enters —
`add_parameter("q0", q0)` is passed the proton `q0`, so something between that
call and the serialized file substitutes the muon value (a manifest lookup, a
`stamp_staleness_metadata` path, or the save-time carry-forward). That trace is
the first step for whoever picks this up.

**Why it matters.** If the numbers are proton and the label says muon, then any
consumer selecting inputs by the label — including the layer guard
`load_y_lambda_for_q0`, which is keyed on exactly this — will pair them with
muon-layer data. That is the straddle mechanism of bean qou-tzsp, inverted, and
sitting behind a provenance field that vouches for it.


---

## REFUTED — the stamps are CORRECT; my measurement was the artifact (2026-08-17)

There is no mis-stamp. `q_parameter` **auto-selects the anchor by the running
producer's stem**, looked up in `q0_anchor_manifest.json`
(`substrate/q_parameter.py:88-103`):

    _stem = Path(sys.argv[0]).stem
    if _stem in manifest["ideal_muon"]: _anchor = "ideal"      # -> muon

`binding_canonical`, `wedderburn_lp_ew_wiring`, `mass_table_comprehensive` and
`atomic_tr_m_mpfr_50dps` are **all in `ideal_muon`**. So when any of them runs
as `python3 <producer>.py`, `Q_MP` and `Q_50_DIGIT_STR` ARE the muon value, the
computation IS at muon, and `q0Anchor: muon` describes it accurately.

**How I got it wrong.** I "verified `binding_canonical.q0` at runtime = proton"
by importing the module from a `python3 -c` process. There `sys.argv[0]` is
`-c`, whose stem is not in the manifest, so `q_parameter` served the **proton
default** — to me, not to the producer. I measured my own process's anchor and
attributed it to the producer. The manifest's `_convention` field says
"q_parameter auto-selects by the running producer's stem" in plain text; I had
read that string and not acted on it.

This is a third instance of the session's recurring error, and the sharpest:
not merely trusting a label over the computation, but **taking a measurement in
the wrong context and trusting it over a label that was right.**

`q0_anchor_consistency_audit` reporting `Q0_FLIP: 0` is therefore not the weak
signal I claimed — for these four it is correct. (The narrower observation that
the audit compares `q0Anchor` against `q0Value` rather than against the q the
producer used remains true as a *description* of what it checks; it is simply
not evidence of a defect here.)
