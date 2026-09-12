---
# qou-k1xe
title: he4_magnus_mpfr_probe and the sparse probe write ONE witness path; the mpfr one cannot emit the Wenzl column, so a re-run erases the A=4 weight-family result
status: in-progress
type: task
priority: high
created_at: 2026-09-12T18:16:10Z
updated_at: 2026-09-12T18:16:54Z
---

## What

`computations/deltalambda/he4-magnus-omega2-sign.witness.json` has **two**
producers:

| producer | emits Wenzl? | cross-A signs |
|---|---|---|
| `he4_magnus_omega2_sign_sparse_probe.py` (named in the witness's own `scriptFile`) | yes — 18 mentions; declares `headline_pairing = "P_total_wenzl"` | derived from the sibling witnesses |
| `he4_magnus_mpfr_probe.py` | **no — 0 mentions** | were **hardcoded** |

A plain `he4_magnus_mpfr_probe.py --skip-gate` would overwrite the committed
witness and **delete 8 `results` keys** — `weight_family`,
`weight_family_note`, `headline_pairing`, `P_total_wenzl`,
`P_total_wenzl_sign`, `sign_indefinite_across_partitions`, `sign_flip_vs_A3`,
`germ_hecke_check_partitions_measured` — plus **10 top-level keys** including
`scriptHash`, `commitSha`, `q0Anchor`, `q0Value`, `method`, `inputs`.

Among them is the entire Wenzl/Ocneanu column, which **is** the A=4
weight-family result landed in #7197. The overwrite would read as a routine
refresh: same filename, same `computation` name, a plausible verdict string.

## The hardcoded sign — fixed, and worth reading for why it survived

```python
"A2_P_total_sign": -1, "A3_P_total_sign": -1,
```

`run_gate()` **in the same file** loads `triton-magnus-omega2-sign.witness.json`,
whose `results.P_total_sign` is **+1**. So the file asserted `A3 = -1` against an
artifact it opens itself.

`-1` is the A=3 sign in the **Wenzl** column (`P_total_wenzl = -13.93…`). The
hardcode was a Wenzl value under a Plancherel field name — and it is *correct at
A=2*, because that is the one atom where the two families agree in sign. A
two-entry hardcode that is right on one entry reads as plausible, which is why
nothing caught it.

Fixed in `99b305e60` (PR #7218): `_sibling_sign` reads both from the committed
witnesses, mirroring the sparse probe's `_sign`; an unreadable sibling renders
`?` rather than being assumed.

## Guarded, not redirected — and the open question is WHICH producer owns the path

`_refuse_to_clobber` now exits naming the owning `scriptFile` and the fields it
would destroy; `--allow-clobber` is the deliberate override. That is a **holding
action**, not the answer.

The real question is a design one and it is **not an agent's to settle by moving
a filename**: `he4_magnus_mpfr_probe.py` is measured **4× faster** on the inner
arithmetic (0.24 vs 0.97 µs/op at 466 bits) and its own docstring says *"Same
object, same math, same precision … only the arithmetic backend changes"* — so
it may well be the intended **successor**, in which case the fix is to teach it
the Wenzl column, not to move it aside. Options are framed for the owner in
`qou-za3q`'s follow-up.

## 🛑 THIS IS THE SECOND INSTANCE OF A CLASS, and the first one is still open

`qou-pgdw` (2026-08-15, `todo`, priority high): `scripts/precision-gates.sh`
invokes `witness_raw_float64_audit.py` **twice** — a full-corpus gating run and a
narrow `--scan-root docs/audits/scripts` advisory run — and **both write
`computations/witness-raw-float64-audit.witness.json`**, so the narrow run
clobbers the full one (`dirty_witnesses` 1561 → 5).

Same shape: **two writes to one witness path, the narrower silently replacing the
richer.** Neither is a detector blind spot — both detectors work fine. The hazard
is in the *write surface*, which nothing audits.

**It cost me directly this session.** My first read of `precision-gates.sh
--changed` showed two `RAW-FLOAT64 AUDIT` blocks, both `NEW 0 / REGRESSED 0`, and
I came close to reporting the ratchet clean. The unconditional run and a pristine
`origin/main` baseline both in fact report **`REGRESSED: 3`**, byte-identical to
the three named in
`docs/audits/2026-09-08-raw-float64-ratchet-is-regressed-on-pristine-main.md`.
The `0`s were the *advisory* run's numbers standing in for the gating run's —
exactly what `qou-pgdw` describes.

## Worth building: nothing audits the write surface

Two instances found independently, three weeks apart, both by accident. A cheap
audit would enumerate every `*.witness.json` path written anywhere in
`computations/` and flag any path with **more than one writer**, then compare the
key sets the writers emit. That is a static scan over write sites, not over
witness contents — no compute, no producer runs. Not built; scoped here so it is
not re-discovered a third time.
