---
# qou-hah0
title: 'precision-gates.sh: preflight let 4 phantom REDs through; the 6 real reds diagnosed'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T09:30:50Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
---

## The gate defect — FIXED in this branch

`scripts/precision-gates.sh` carries a preflight block whose stated purpose is
*"an unimportable dependency is NOT a red gate"*, with a 2026-08-09 measurement in
its own comments showing four of five REDs vanishing once `mpmath` was installed.
**It checks exactly one module: `mpmath`.** That is not enough and the same failure
recurred.

MEASURED 2026-08-30 on `main` `86a708a4250`, container with `mpmath` present and
`qou_substrate` absent — 8 blocking REDs, exit 1. Installing `qou_substrate`
**alone** took it to 6: `mpf(<float>) source` and `mixed mpf/f64 -> serializer`
were **phantoms**, dying on `ModuleNotFoundError` before examining anything.

**Why it matters more than two gates.** AGENTS.md calls this script the *whole*
gate for precision work now that CI is dispatch-only and no external reviewer
arrives. A bare container is the documented **default** here, so the gate read red
regardless of the change under test — unusable exactly where it is the only signal.

**Second half of the trap:** `qou_substrate` is **not on PyPI**, so the old
`pip install $missing` hint would itself have failed. Hints are now per-module;
this one is `pip install -e tools/qou-substrate`. Which modules to list was
measured by an AST walk over every gate script and its in-repo import cone —
exactly two non-stdlib, non-bootstrap imports: `mpmath` and `qou_substrate`.

Verified both directions: dep absent → `PREFLIGHT FAILED`, **exit 2**, correct
hint; dep present → the real run proceeds.

## The 6 REAL reds — diagnosed, NOT fixed

Each needs a producer re-run or an author call. Recorded so the next agent starts
from measurement. **None of these is my work and none is new** — all are `main`'s.

1. **q0-anchor flip** — exactly **1** witness. `hadron-knot-table.witness.json`
   has `anchor=muon` but `q0Value=1.10997859555733…` where the audit expects
   `1.109978595642…`. ⚠ **Do not assume the witness is wrong**: AGENTS.md gives
   the canonical muon pin as `1.1099785955573347…`, which matches the *witness*,
   not the audit's expectation. Settle which is right before touching either.
   Note `hadron_knot_table` is the producer AGENTS.md measures at **>50 min for
   one bound atom, killed by its own timeout** — a re-run is not a cheap fix.
   Corpus counters at this run: `Q0_ANCHOR_MISSING 1617`, `Q0_AUDIT_EXEMPT 81`,
   `Q0_INDEPENDENT 68`, `Q0_FLIP 1`.

2. **q0-anchor refill ratchet** — 7 witnesses newly unstamped. The gate's own
   output names the mechanism and an existing bean: the stamp is written only
   `if _a in ("muon", "proton")`, so an `ambiguous` entry resolves and is then
   **discarded**; 19 stems are declared ambiguous, 9 of their witnesses unstamped.
   **Bean `qou-fl0a` already owns this** — do not open a second one.

3. **float64-padding ratchet** — 4 fields in
   `computations/option-e-phase1-gram-h6.witness.json`, e.g.
   `data.h3.blocks.3.w0_det` *claims*
   `1.36755183695138526900336728431284427642822265625…` and *really* carries
   `1.3675518369513853`. A genuine precision defect: float64 dressed as 50-digit.
   Fix at the producer (carry `mpf`, serialize with `_precision.fmt`); never
   hand-edit the number.

4. **raw-float64 ratchet** — 154 files drained, but **2 regressed**:
   `phase-transition-q-ideal-gas` 6 → 11 and
   `seifert-volume-meson-n7-extension` 51 → 55. Those are the actionable ones.

5. **q0-value drift ratchet** — 2 values at **−0.0769 ppb**
   (`qbeta-meridian-holonomy-anchor-swing` `per_anchor.muon.q0`,
   `rho-binding-constancy` `substrate.q0`), plus **25 values matching no anchor**
   that the gate says need a human look — including several at `1.1097`,
   `1.10998` and `1.109709024899…`, which are neither pin.

6. **witness scriptFile provenance** — `NOT_A_PRODUCER 1` out of 2611 claims
   (`WRITES 2584`, `UNCONFIRMED 26`). **I did not identify which witness**; the
   audit's default output does not name it and my walk of its witness JSON did not
   surface a per-entry status. Read the audit source or find a verbose flag.

## Method notes

- `git checkout -- .` after a gates run is indiscriminate — it reverted my own
  script edit along with the audit-regenerated witnesses, and the loss was silent
  until `git commit` said "nothing to commit". Scope the revert to the witness
  paths.
- A gates run regenerates `q0-anchor-consistency-audit`, `witness-provenance-audit`
  and `witness-raw-float64-audit`. Reverting them protects the committed
  environment stamp from this container's versions.


## CORRECTION 2026-08-30 — red #1 is SETTLED, and my item 1 above had it backwards

Item 1 warned *"do not assume the witness is wrong: AGENTS.md gives the canonical
muon pin as 1.1099785955573347…, which matches the witness, not the audit's
expectation."* **That is wrong, and so was the AGENTS.md line it leaned on.**

The muon anchor was migrated to CODATA 2022 in `fca08de7d29` (2026-08-28,
*'derive it, stop the self-certification'*), on the owner's **2026-08-22** ruling —
six days before I wrote that warning. Measured on main `3a919ad14fe`:

- `computations/q-pinning-50-digit.witness.json` = `1.109978595642739046681795129380001752700065561029011556974045769999095` (C, not A)
- `muon_pin_stored_vs_live_gate.py`: stored vs live gap **0.0 ppb**, 0.0 sigma
- `q0_anchor_consistency_audit.py`: **Q0_FLIP = 1**, `hadron-knot-table.witness.json`, still carrying A

So the **audit is right and the witness is stale** — the reverse of what item 1
said. `_EXPECTED_PREFIX['muon'] = '1.109978595642'` in the audit is not a
hardcoded guess; it agrees with the anchor the tree now serves.

**Remaining work on red #1 is one producer re-run, and it is NOT cheap:**
`hadron_knot_table` is the producer AGENTS.md measures at >50 min for one bound
atom before its own timeout kills it. Claim it as its own bean with a real
compute budget; do not attempt it in an idle pass.

## Merged from this bean's diagnosis (all on main)

- `2b768409987` — the preflight defect itself (PR #6160): per-module dep check
  + hints; the 4 phantom REDs are gone.
- `ba4c0cf3e1a` — red #3 float64-padding (PR #6176): the `dim == 1` branch in
  `gram_matrix_seminormal_h6.py` kept a float64 round trip the general branch
  had lost. **CLEARED.**
- `6209615ecf6` — red #4 raw-float64 (PR #6182): both regressed producers
  drained to **0** raw floats. **Ratchet green. CLEARED.**

**Reds still open: 2, 5, 6** (anchor-refill ratchet — owned by `qou-fl0a`;
q0-value drift ratchet; witness scriptFile provenance, 1 unnamed witness).
Red 1 is diagnosed but blocked on the long compute above.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-30 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8345, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
