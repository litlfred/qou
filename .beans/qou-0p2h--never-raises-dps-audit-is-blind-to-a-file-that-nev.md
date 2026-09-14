---
# qou-0p2h
title: never_raises_dps_audit is blind to a file that never NAMES mpmath — 5 live, 1 fixed, all computing at dps=15
status: todo
type: task
priority: normal
created_at: 2026-09-14T15:57:17Z
updated_at: 2026-09-14T15:58:10Z
---

## The blind spot, measured on the same file at two revisions

`computations/never_raises_dps_audit.py` exists to catch exactly this class and
does **not** see `computations/probes/casimir_epsilon_vacuum_probe.py`, which
computed its entire Casimir force table at mpmath's default `mp.dps = 15`.

Verified by running the audit against the pre-fix file, not by reading its code:

    $ git show HEAD~1:...casimir_epsilon_vacuum_probe.py > <the file>
    $ grep -c set_compute_dps <the file>        ->  0
    $ python3 never_raises_dps_audit.py | grep casimir_epsilon_vacuum
    (no output)                                 <- NOT flagged
      runnable producers never raising dps : 9
      NEW (not baselined)                  : 4

**Why it is invisible.** The pre-fix file names mpmath **zero times** —
`grep -cE "mpmath|\bmpf\(" ` returns 0. Its only mpf enters by IMPORT
(`from experimental_constants import HBAR_MEV_S`), and every subsequent
operation — `HBAR_MEV_S * 1e6 * _EV_TO_J_SI_EXACT`, then
`-pi_sq * HBAR_C_J_M / (240.0 * d_m**4)` — is mpf arithmetic performed at
dps 15. The audit counts "mpmath value CONSTRUCTIONS", so a file that
constructs none and inherits one is outside its population by design.

This is the mirror image of a bucket the audit already reports. It has a
"raise dps only VIA AN IMPORT" tier (7 files) for producers that *do*
construct mpf and inherit the RAISE. The blind spot is the other direction:
inherit the **value**, construct nothing, never raise.

## How it surfaced, which is the reusable part

Not by reading the audit. By the **float64-padding ratchet** contradicting the
**raw-float64 ratchet** on a change I had just made and believed clean:

    raw-float64      12 -> 0     looked like a drain
    float64-padding   0 -> 9     `claims 0.100000000000000005551115123125...`
                                 `really  0.1`

`fmt` had serialized a 53-bit value to 60 digits. `_precision.py`'s own
docstring predicts this verbatim. **The two ratchets are not redundant:
draining one while feeding the other is the failure mode, and only the second
one sees it.** Fixed in `6d620dfbcfc`; 12 -> 0 raw and 0 padding, 58 fields in
/ 58 out, max move 3.483e-15.

## The live class: 5 files, and it is NOT 23

Narrowed by TYPE, not by name. A first pass looked for "arithmetic on a
constant imported from a known constants module, never names mpmath, never
raises dps" and returned **23** — but most import `Q` / `HBAR_Q` / `HBAR_Q_SQ`
from `q_parameter`, and those are **float64** (`Q = float(_d["q"])`), so
arithmetic on them is a plain float64 path, i.e. the qou-840k class, not this
one. Resolving each imported name's runtime type (`experimental_constants` has
24 mpf exports, `q_parameter` 11, `knot_volumes` 7) leaves **5**:

    computations/atom_mass_derived.py                      via M_P_MEV
    computations/b_over_a_evaluator.py                     via ALPHA_EM_INV
    computations/d_density_derivation.py                   via M_E_MEV
    computations/gap_a1_binding_k_sdp_feasibility.py        via M_E_MEV
    computations/probes/homflypt_operator_valued_probe.py  via Q_NEUTRON_MEV

Do not quote 23. It over-matches by ~4.6x on exactly the distinction that
makes this a separate defect from qou-840k.

## Not yet done, and deliberately

Each of the 5 needs its own verified fix — run unmodified first, diff every
field, check BOTH ratchets — because `set_compute_dps()` moves published
numbers (here, 10 fields at ~3e-15; in a cancelling quantity it would be
larger). Fixing them qualifies under the ASK-FIRST exemption "it increases
precision", so no owner sign-off is needed; what is **not** authorised is
doing it as a blind 5-file sweep.

**Recommendation (my judgement, not a finding):** fix the 5 one at a time in
the current raw-float64 drain arc, and separately widen
`never_raises_dps_audit.py` to count arithmetic on an imported mpf-valued
name. The detector change is the durable half — without it the next file of
this shape is invisible again.

## Related, and distinct from all three

- `qou-yh08` / `qou-fl9i` — files that set `mp.dps` **too low** (952 / 838
  sites at 50/40/30, sub-canonical). This bean is files that set it **not at
  all**, i.e. 15, and that the dedicated audit cannot see.
- `qou-840k` — `float()`-casts and imports of float64 constants. Adjacent, and
  the reason the 23 over-matched.
- `qou-j6gb` — `mpf_import_time_dps_audit` not wired into `precision-gates.sh`.
  A different audit; this one IS wired and still misses the file.

Row 46 for `docs/audits/2026-08-15-detector-blindness-taxonomy.md` (45 rows as
of 2026-09-14). Its family is 22/25/26 — *the interesting thing is assumed to
appear syntactically at this site* — one level up: here the assumption is that
a file computing in mpmath will MENTION mpmath.
