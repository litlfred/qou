---
# qou-sal4
title: 'GAP: both q0/float64 ratchets are RED on this branch — 3 unstamped + iterative-lp-dual 96->99'
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T18:10:19Z
updated_at: 2026-08-30T18:22:35Z
---


Surfaced 2026-08-30 while closing `qou-l2we`. **Neither red is caused by that
change** — both predate it and neither file is in that commit.

## `q0_anchor_ratchet.py --strict` — FAIL, 3 newly unstamped

    computations/deltalambda/c-knot-tau-transfer-artifact.witness.json
        73567a64e  witness(takeover): regenerate c-knot tau-transfer witness
    computations/probes/toffoli-published-vs-construction.witness.json
        2f3e5b2f8  audit: universality fails under the block's OWN indexing too
    computations/probes/toffoli-trio-rederivation.witness.json
        04f14b7c2  derive(qou-3j5m): the Toffoli trio is RESOLVED

Each is a regenerate/derive commit whose producer does not stamp `q0Anchor`.
Fix at the PRODUCER (`save(extra=...)`, never `add_data` — bean `qou-kx04`), not
by widening `q0-anchor-missing-baseline.json`. If a producer genuinely never
reads q0 the correct stamp is `'independent'` + `q0AnchorReason`, NOT silence.

## `witness_raw_float64_audit.py --strict` — FAIL, 1 regressed

    96 -> 99   computations/iterative-lp-dual-h6-deuteron.witness.json
        ac6310b31  fix(qou-mjcd): a declared-proton producer was multiplying...

That one is **mine** (qou-mjcd). The fix was correct; the re-run re-added three
raw f64 the drain had removed. Same mechanism as the one just fixed in
`qbeta_ck_basis_constrained_pslq.py`.

## The general defect this is an instance of

`bc8131bd5` ("drain(float64): 1232 declared tolerances in 499 witnesses")
drained the **artifacts** but left the **producers** emitting floats. So every
drained witness silently un-drains the next time anything re-runs its producer,
and the ratchet only notices later, attributing it to whoever re-ran it.

`qbeta_ck_basis_constrained_pslq.py` is now fixed at the producer (emits
`"tolerance"` as a string, 18 -> 17). **The other 498 are not.** Estimating that
population and fixing the producers is the real work here — a drain that any
re-run reverses is not a drain.

Do not widen either baseline. `raw-float64-baseline.json` says so itself:
"Adding a file here to silence a failure defeats the gate — fix at the producer
instead."

## 2026-08-30 — q₀ ratchet: FIXED (PASS). float64: root cause found, fix BLOCKED.

### q₀ ratchet — `PASS (--strict): no new unstamped witnesses`

All three stamped at the PRODUCER, verified by RESOLVING imports (not `grep -rl`):

- `toffoli_published_vs_construction_audit.py`, `toffoli_trio_rederivation.py`
  → `q0Anchor: "independent"`. Their only non-stdlib imports are `_path_bridge`
  (a sys.path shim), mpmath/sympy, `_precision.set_compute_dps` and
  `witness_base` — none carries a substrate q₀, and neither file holds a q₀
  literal. Both are symbolic in the free variable q. (The trio's
  `antisymmetry_is_FALSE_convention_C/_D` assertions are symbolic Markov-frame
  comparisons, not anchor choices.)
- `c_knot_tau_transfer_artifact_probe.py` → `q0Anchor: "ambiguous"`. It DOES
  read a q₀, but `Q0_STR` (line 63) is the muon vintage-A pin RETIRED
  2026-08-22, hardcoded and TRUNCATED to 24 sig digits instead of resolved via
  `q_at()`. Its prefix `1.10997859555` is exactly the superseded-vintage prefix
  the staleness guard watches. `muon` would assert a live anchor for a retired
  vintage; `independent` would be false. Repinning moves published numbers →
  belongs to `qou-cds3`, not a restamp.

**Zero value drift** on all three (verified field-by-field against snapshots).
The only non-ephemeral change anywhere was `engineVersion: mpmath 1.3.0 →
1.4.1` — this container has a newer mpmath than the committed witnesses were
built with, worth knowing before any mass re-run.

### float64 96→99 — root cause found; the documented fix is LOSSY

Not a discipline defect. My `ac6310b31` switched the producer from a static
table to `load_y_lambda_for_q0(6, …)`, i.e. from the MUON table to the PROTON
table. Seven values moved — exactly the seven **≥3-row** partitions of n=6:

    (1,1,1,1,1,1) (2,1,1,1,1) (2,2,1,1) (2,2,2) (3,1,1,1) (3,2,1) (4,1,1)
    muon table   : 0.0            <- exact; y_λ ≡ 0 for ≥3 rows (Wenzl r=2 under D)
    proton table : ~1e-72         <- numerical residue

So the **proton table is stale**, and the live closed form proves it — computing
`y_lambda_wenzl_bridge_numeric((4,1,1), q, 50)` directly gives:

    muon pin C  -> 0.0
    proton pin  -> 0.0        <- the table says 2.188…e-72
    pin A       -> -1.6146…   (retired)

I first suspected the `str(q_val)` precision trap (passing `q_parameter.Q`, a
17-digit float, rather than `Q_50_DIGIT_STR`). **That is not it** — float and
50-dps string give identical results here. Ruled out by direct test.

### Why the fix is blocked — and a trap that should be fixed first

🛑 `regenerate_y_lambda_mpfr.py --anchor proton` is **DESTRUCTIVE**. It writes
only n≤12 and overwrites the file wholesale, silently dropping `tables_by_n`
n=13..18 **and** the entire `extension.closed_form_tower` block. Caught only
because the run was snapshotted first.

**And that lossy command is what the corpus tells you to run.** The
`FileNotFoundError` in `tr_m_wenzl_bridge_mpfr.py::load_y_lambda_for_q0` says
verbatim: *"generate it with `regenerate_y_lambda_mpfr.py --anchor proton`"*.
Anyone following that instruction destroys n=13..18. Fix the message and the
script together.

The non-destructive path is two steps — `regenerate_y_lambda_mpfr.py --anchor
proton`, then `y_lambda_tower_infra.py 18` (18, NOT the default 24, which would
extend past the committed extent). Ran both; the closed-form≡symbolic gate
passed (`4.29e-70 < 1e-40`). **But the result moved 1285 values and did NOT fix
the target**: zero ≥3-row entries became exact 0, while n=13 entries went
`0.0 → nonzero` — the wrong direction. So the committed proton table is **not
reproducible from its own documented producers**, which is a bigger problem than
the staleness it was meant to fix.

Everything restored from snapshot; both tables byte-identical to HEAD. Nothing
regenerated was committed.

### Left open

1. Fix the lossy `--anchor proton` path + the FileNotFoundError message that
   recommends it.
2. Establish why the two-step regeneration does not reproduce the committed
   proton table (1285 entries).
3. Only then: refresh the proton table's stale ≥3-row residues, which closes
   the float64 96→99.

Do not widen `raw-float64-baseline.json` to clear (2) — the count is a true
report of a stale table.
