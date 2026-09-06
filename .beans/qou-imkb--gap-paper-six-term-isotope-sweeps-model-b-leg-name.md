---
# qou-imkb
title: 'GAP: paper_six_term_isotope_sweep''s Model B leg names a producer that does not exist'
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T12:14:04Z
updated_at: 2026-09-05T18:21:53Z
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


## 2026-08-30 (worked) — TWO CORRECTIONS to this bean, and the real blocker

### Correction 1: there are TWO consumers, not one

I wrote *"`paper_six_term_isotope_sweep.py` is the only reader"*. Wrong.
**`computations/build_six_term_substrate_model_b.py`** carries the same loader
(`_load_model_b_t1`, ~line 96), reads the same missing witness, keys on the
same `data.results.<atom>.tr_M_wenzl_schur`, and raises the same message. It is
the *primary* Model B consumer — the sweep is the secondary one. So the blast
radius is the whole Model B six-term pipeline, not one sweep column.

That producer **exits 1 outright**; the sweep degrades to per-row `ERR`.

### Correction 2 — 🛑 THE REAL BLOCKER: one input is RETIRED BY OWNER RULING

The producer is not merely unwritten. **It cannot be written correctly today**,
and the reason is not difficulty.

`MODEL_B_BRAID_REGISTRY[(1, 1)]` — the deuteron — assigns knot **`6_2`**. The
owner ruled on exactly this on **2026-08-29**
([`docs/audits/2026-08-29-deuteron-knot-owner-decision.md`](../docs/audits/2026-08-29-deuteron-knot-owner-decision.md),
bean `qou-e5jf`):

> **OWNER RULING (2026-08-29): Option A.** The deuteron knot is the canonical
> braid closure (trefoil / Hopf, Vol = 0) … **the 6₂ census assignment is
> retired as a bare lookup.**

**Option B was literally *"the deuteron knot is 6₂ (Vol = 4.40)"* and it was
put to the owner and rejected.** So this is a ruling about the **knot
identity**, not only about whether the binding is a volume term — I checked that
distinction specifically, because "grep the claim SHAPE, not only the topic"
is exactly the trap here.

**Consequence: writing the producer against the registry as it stands would
compute `tr_M(6₂)` for the deuteron — implementing the rejected option.** That
converts this bean from *"someone should write a producer"* into *"one registry
row must be resolved first, and the resolution is an owner ruling that already
exists."*

Checked the other two rows: **`8_11` (T) and `L6a4` (³He) are live and not
retired** — both appear in current, non-deprecated audits, and `L6a4` carries
an exact hyperbolic identity with the Borromean volume. Only the deuteron row
is affected.

### What I changed (no fabricated numbers)

1. **Both error messages now tell the truth.** They used to say *"Run
   `probe_sdp_canonical_paper_formula.py` first"* — an instruction nobody could
   follow. They now say the producer does not exist, give the evidence, and
   point here. This also lands in the sweep's committed witness, where a reader
   of the `ERR` rows will actually see it.
2. **The retired registry row is flagged in place**, citing the ruling, with
   the reason it was *not* silently changed.

**I deliberately did NOT pick a replacement knot.** At A=2 the canonical braid
closure is the object Model A already uses, so adopting it may collapse Model
B's deuteron T1 into Model A's — and whether that is correct, or means Model B
simply has no distinct A=2 entry, is a modelling decision with real
consequences for what "Model B" means. That is the owner's call, not a fix I
should smuggle into a registry comment.

### The decision this now needs

- **What replaces `6_2` in `MODEL_B_BRAID_REGISTRY[(1,1)]`?** The ruling names
  the object (canonical braid closure, trefoil/Hopf) but not what Model B's
  low-strand entry should therefore be.
  - If it becomes Model A's canonical braid, the row should route via
    `t1_atom_a` like `p` and `n` do, and Model B has no independent deuteron.
  - If Model B is meant to keep a distinct A=2 object, that object needs
    naming, and the ruling does not name one.
- **Only after that** is writing the producer a well-posed task: emit
  `data.results.<atom>.tr_M_wenzl_schur` for deuteron / tritium / he3 (p and n
  come from the Model A registry; ⁴He is explicitly `open` in the registry).

**Default if nothing is done:** unchanged and safe. Both consumers refuse
loudly, the sweep prints `ERR` rather than fabricating, and nothing downstream
reads a Model B number — because there is no Model B number to read.


## 2026-08-30 (second pass) — the retired assignment has THREE live sites, not one

Found while scoping the `qou-46ab` residue. My earlier note named one site; the
`6_2` deuteron assignment the 2026-08-29 ruling retired is live in **three**
places, in **two** files:

| # | site | kind |
|---|---|---|
| 1 | `build_six_term_substrate_model_b.py::MODEL_B_BRAID_REGISTRY[(1,1)]` | `"knot": "6_2"` |
| 2 | `derivation_chain.py:188::MODEL_B_BRAID_META["D"]` | `"knot": "6_2"` |
| 3 | `derivation_chain.py:178::TR_M_CANONICAL_B_AT_Q0["D"] = 0.288326` | a **value** derived from the retired knot |

Site 2 is an **AST-verified live string constant**, not a comment — checked
specifically, because four of the five `6_2` matches in that file *are*
comments and a grep-level reading would have called the whole file clean.

Site 3 is the one that would actually propagate: it is a number, not a label,
and it already carries a `#1422-recompute pending` marker — so it was known to
be stale for a *different* reason before the knot ruling made it stale for this
one too.

All three are now **flagged in place, not changed**, for the same reason: at
A=2 the canonical braid closure is the object Model A already uses, so adopting
it may collapse Model B's deuteron entry into Model A's, and whether that is
correct is the modelling decision this bean is waiting on.

**This does not change the decision, it changes its cost.** The one registry
row I described is three edits across two files, one of which is a recomputed
number rather than a relabel — so "resolve the row" is not a one-line follow-up
once you rule.

**And it sharpens why nothing is urgent:** every one of the three sits behind
the missing Model B T1 producer. The path raises before reaching any of them.



## Verified 2026-09-05 — a live defect, not an owner decision

Re-measured on this branch rather than taken from the bean:

- `probe_sdp_canonical_paper_formula.py` — **0 files on disk**
- `probe-sdp-canonical-paper-formula.witness.json` — **0 files on disk**
- `git log --all` for either name — **0 commits** in this clone
- the raising site is still live: `paper_six_term_isotope_sweep.py:185`,
  `f"missing Model B T1 witness: {path}. "`

So the error message still instructs a user to run a producer that has never
existed here, and the Model B leg of the six-term sweep is unreachable. That is
a defect to fix, not a preference to adjudicate — the only genuine question
("what does Model B mean?") is answerable from the corpus. Off the owner-gated
queue; open as work.
