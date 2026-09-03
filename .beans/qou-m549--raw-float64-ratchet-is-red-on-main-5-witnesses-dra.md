---
# qou-m549
title: 'Raw-float64 ratchet is RED on main: 5 witnesses, drained at the producer (PR #6453)'
status: in-progress
type: bug
priority: normal
created_at: 2026-09-03T20:35:04Z
updated_at: 2026-09-03T20:35:37Z
---

## Measured, and re-measured after main took 55 commits

`python3 computations/witness_raw_float64_audit.py --strict` on `origin/main`:

| head | NEW | REGRESSED | exit |
|---|---|---|---|
| `d502ed06ce` (2026-09-03) | 2 | 3 | 1 |
| `fbbd7d5364` | 2 | 3 | 1 |
| `2a7dfce761` (2026-09-03, +55 commits) | 2 | 3 | 1 |

Identical across all three, so no sibling has drained any of them and this is
not a stale reading. The five:

    NEW        4  computations/probes/arc-count-diagnostic-degeneracy.witness.json
    NEW        2  computations/probes/bpp-higher-a-sparse.witness.json
    REGRESSED  12 -> 22   computations/delta-n2-lp-dual-extraction.witness.json
    REGRESSED  89 -> 91   computations/audits/braid-encoding-audit.witness.json
    REGRESSED  18 -> 20   computations/meson-spectrum-predictions.witness.json

It was red in main's **own committed witness** too — `new_not_baselined: 1,
regressed: 1` from a run on 2026-08-31 — i.e. a red result was committed rather
than fixed, and that record is stale in the direction that *understates* it.

## Fix — PR #6453, `claude/ratchet-red-drain-2026-09-03` @ `43e0526fe5`

Merged onto `2a7dfce761`: clean merge, **NEW 0 / REGRESSED 0 / exit 0**.

Every witness re-run from its producer; none hand-edited. **No baseline entry
added, widened, or rebaselined.**

Four are bucket A (the `float()` cast IS the defect). One is bucket B
(`meson-spectrum-predictions`, float64 at the `build_seminormal_matrices`
library boundary) and is written at the double's own shortest exact width with
the limitation stated in the witness — the remaining 18 stay counted, because
draining them needs `build_seminormal_matrices` ported to mpmath, which moves
`m_K/m_pi`, the one scoreable L2 result. That is bean `qou-p77d` bucket B, not
a ratchet drain.

## TRAPs recorded

- **`seconds` is not a detector gap.** I first called `bpp-higher-a-sparse` one
  and proposed widening the audit's filter. Wrong: the carve-out matches
  *declared provenance names* from `_EPHEMERAL_META_FIELDS`, and
  `.data.rows[].seconds` is payload. Fixed at the producer by *renaming* to
  `elapsed_sec`. A `/time/` test would have excused 177 fields.
- **`fmt` is not universally right.** `_mpf50("493.677")` is correctly built
  from a string, but an mpf is *binary*, so `fmt` at 50 dps prints
  `493.677000...000169688486` — 59 digits of a quantity measured to 6. Same
  false-precision defect as float64 padding, reached from the other direction.
  `mp.nstr(x, 6)` for an experimental input.
- **A single witness field can carry two Python types.** In
  `braid-encoding-audit`, `d` is int `0` for a sigma letter and mpf for
  sigma-inverse; `c` is int `1` for isospin-symmetric letters and mpf `1` for
  the three colour-weighted p-n interfaces. `fmt` spells those differently, so
  a new exact-equality assertion read 84/161 until both slots were coerced
  through `mpf`. I had asserted in a docstring that `c` was always an int; the
  diff against `origin/main` said otherwise.
- **Committed value stale against an upstream that had NOT moved.**
  `markov_trace_assembly_chain` recorded `1.0653062285923893` while
  `markov-trace-assembly-proton.derivation.json` carries `1.1457596924573008`,
  identical on disk and on `origin/main`. A diff-keyed sweep cannot see this.
  The `qou-soj6` disagreement is **39.20% / 64.46%**, not the recorded
  43.46% / 76.88% — smaller than advertised, still four orders outside the
  derivation's claimed `1e-9`, so the finding stands.
- **The raw-float64 ratchet does NOT self-perturb**, contra a sibling's
  question on #6489: three consecutive runs on an unchanged tree (runs 2-3 with
  its own output already dirty) gave identical NEW 2 / REGRESSED 3. Mechanism
  is `SELF_OUTPUTS` / `SELF_OUTPUT_PREFIX` / `AUDIT_SUFFIX` at
  `witness_raw_float64_audit.py:102-128`. I then suggested porting the same
  treatment to `q0_anchor_ratchet.py`; **that suggestion was wrong** — it
  already imports `AUDIT_SUFFIXES` and filters at `_is_in_scope`. I asserted a
  gap from the shape of a report without opening the file.

## Status

Open, `mergeable_state: clean`, waiting only on merge permission. No CI run
exists (Actions are `workflow_dispatch`-only), so the ratchet IS the gate.
