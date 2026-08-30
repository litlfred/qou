---
# qou-imkb
title: 'GAP: paper_six_term_isotope_sweep''s Model B leg names a producer that does not exist'
status: todo
type: task
priority: normal
created_at: 2026-08-30T12:14:04Z
updated_at: 2026-08-30T12:14:45Z
---

## What is wrong

`computations/sweeps/paper_six_term_isotope_sweep.py::_load_canonical_t1_model_b`
(line ~174) raises, for D, T and ³He:

    FileNotFoundError: missing Model B T1 witness:
      .../computations/sweeps/probe-sdp-canonical-paper-formula.witness.json.
      Run probe_sdp_canonical_paper_formula.py first.

**That instruction cannot be followed by anyone.** Measured 2026-08-30:

- `probe_sdp_canonical_paper_formula.py` — **not on disk anywhere** in the repo.
- `probe-sdp-canonical-paper-formula.witness.json` — **not on disk anywhere**.
- `git log --all` for either name across the **32183 commits this clone has**:
  **no commit ever touched them.** (Caveat, stated because it matters: agent
  clones here are **shallow**, so "never" is bounded by the fetched window. It
  is not bounded enough to make the producer runnable, which is the operative
  point.)

So the Model B (SDP-canonical low-strand Wenzl–Schur) leg of the six-term
sweep has no way to produce its input, and the error message points at a file
that has never existed in reachable history.

## What this is NOT

**Not a regression, and not caused by the convention-D regeneration.** Checked
both directions before filing:

- The **committed** witness contains **zero** `model_b` fields — so the leg was
  already inert when that witness was written.
- D, T and ³He main rows are **byte-identical** before and after the re-run
  (`M_predicted`, `err_pct`, `term1..term4` all unchanged). Only `p`, `n` and
  `⁴He` moved, and those moves are the C→D `tr_M` correction plus its
  downstream, at 1e-9 to 1e-6.

The sweep exits 0 and writes its witness with the leg reporting `ERR`, which is
honest — it is not silently substituting a value.

## Why it matters, in paper terms

The sweep is the six-term isotope table. Model B is one of the two T1
(canonical-knot `|tr_M|`) sources it is designed to compare — the SDP-canonical
route against the Wenzl-bridge route. With Model B unrunnable, **the sweep
reports one source where it was built to report two**, and the comparison that
would discriminate them cannot be run at all. A reader of the table has no
signal that a designed cross-check is absent.

## Options

1. **Write the producer.** It must emit `data.results.<atom>.tr_M_wenzl_schur`
   for at least p, n, D, T, ³He — that is the entire contract the loader reads.
   Cost: a real SDP-canonical low-strand computation, unknown size. Buys back
   the cross-check the sweep was designed around.
2. **Retire the Model B leg** from the sweep and say in the witness that the
   table is single-source. Cost: ~20 lines. Risk: loses a designed comparison
   rather than fixing it, and a later reader may re-add it from the paper text.
3. **Leave it.** The sweep already reports `ERR` per row, so nothing is
   fabricated.

**Recommendation (my judgement, not a finding): option 3 until someone knows
whether Model B was ever computed.** The deciding fact is not in this repo —
if the producer existed in a working tree and was never committed, its author
may still have it, and writing a second one from scratch would be the expensive
way to find that out. Someone with a **full-depth** clone should re-run the
`git log --all` check first; that is minutes of work and it settles which of
options 1 and 2 is even the right question.

**Default if nothing is done:** unchanged. The sweep keeps running, keeps
exiting 0, and keeps printing `ERR` for the Model B columns on D, T and ³He.

## Blast radius

`computations/sweeps/paper_six_term_isotope_sweep.py` is the only reader of
`_load_canonical_t1_model_b`. Nothing else in the tree references
`probe-sdp-canonical-paper-formula`. So this is contained to one sweep and the
`paper-six-term-isotope-sweep.witness.json` it emits — but that witness is
paper-facing, which is why it is filed rather than left in a commit message.

Found 2026-08-30 while draining the last three convention-C witnesses
(`qou-46ab`); previously mis-recorded by me as "waiting on the Model B T1
witness for ³He", which understated it three ways — it is D, T *and* ³He, it is
not merely *waiting*, and it is not a missing witness but a missing producer.
