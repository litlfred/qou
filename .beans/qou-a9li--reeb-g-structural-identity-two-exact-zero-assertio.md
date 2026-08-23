---
# qou-a9li
title: 'reeb_g_structural_identity: two exact-zero assertions carry tolerance=None'
status: completed
type: task
priority: normal
created_at: 2026-08-23T08:05:32Z
updated_at: 2026-08-23T08:06:07Z
---

Exposed 2026-08-23 re-running the `load_q_50dps` callers (PR #5494).

    I1_polynomial_identity            0.0 -> 7.2445e-71   expected 0.0, tolerance=None
    I2_g_equals_inverse_deformed_eig  0.0 -> 4.5278e-72   expected 0.0, tolerance=None

**The identities still hold** — to 71 and 72 digits, far inside the 50-dps
arithmetic floor. The assertions carry `tolerance=None`, i.e. they demand
*exact* `0.0`. Under the muon pin the arithmetic happened to cancel exactly;
under the proton pin it lands at ~1e-71 instead.

So this is **assertion strictness, not a mathematical regression**. An
exact-zero identity evaluated in floating/mpmath arithmetic should carry a
tolerance at the precision floor (the sibling assertions in this corpus use
`tolerance=1e-40`).

Fix: give both a tolerance rather than 'fixing' the number. Do **not** widen
anything else — the value is correct, the comparison is what is wrong.

## DONE 2026-08-23 — fixed at the producer, PR #5494 (`0d97cb2c`)

Confirmed the diagnosis by reading `Assertion.passed`: with `tolerance=None`
it falls through to **string equality** (`self.computed == self.expected`),
so `"7.2445e-71" == "0.0"` is False. I1/I2 passed only while the residual
happened to format as a bare zero.

Reproduced before touching anything: I1 = `7.2445e-71`, I2 = `4.5278e-72`
— the identities hold to 71 digits, so this was never a regression.

Fix: `tolerance="1e-45"` on both, string-valued per the drained no-float64
convention. The threshold is the bar the sibling assertion I3 **already**
uses in the same block (`10**-45`); the residuals sit 26+ orders of
magnitude beneath it, so it is the file's own convention, not a number
fitted to make a red run green. Computed values byte-identical before and
after — only the two verdicts moved. Witness now `allPassed: true`.

`scripts/precision-gates.sh --changed`: all blocking gates green, exit 0.

**Three things worth carrying forward, found doing this:**

1. A degraded `environment` block is **sticky**. The first regenerated
   copy recorded a weaker env (this container lacked clarabel/numpy/scipy
   and had mpmath 1.3.0 vs the recorded 1.4.1). Installing the libraries
   and re-running did **not** repair it: the builder refreshed
   `computedAt` while **preserving the on-disk environment block** because
   the payload was unchanged, and the guard compares against what is on
   disk — so it went **silent** rather than re-flagging the weak record it
   had just warned about. Only deleting the witness and re-running restored
   the true block. Opened as `qou-dc0n`.
2. **This bean's own id is doubly claimed** — `qou-a9li--em-linking-
   crossing-number-minimisation-crux-from.md` and this file. Appending by
   `ls .beans | grep ^qou-a9li -- | head -1` landed in the WRONG one and
   had to be reverted. A live instance of `qou-uoad`, hit minutes after
   writing that bean up.
3. `pyhecke_native` 0.9.0 **is** importable in this container, and cargo +
   maturin are both present. AGENTS.md's project-structure note implies a
   container without it is the default; that is not true of this image.
