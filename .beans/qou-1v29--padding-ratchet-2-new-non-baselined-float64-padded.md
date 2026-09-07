---
# qou-1v29
title: 'Padding ratchet: 2 NEW non-baselined float64-padded witnesses (casimir-q-zeta-probe, rho-k-h3a-lp-dual)'
status: completed
type: bug
priority: normal
created_at: 2026-09-07T09:21:12Z
updated_at: 2026-09-07T11:12:07Z
---

Found incidentally on 2026-09-07 while running `scripts/precision-gates.sh` before a
commit for bean `qou-igjo`. **Not caused by that change** — the gate run regenerated
`computations/witness-float64-padding-audit.witness.json`, which is a contended
tree-measuring audit that must not be committed from a feature branch (bean
`qou-v0t8`), so the regenerated file was reverted and only this record kept.

The audit moved:

    occurrences        22 -> 24
    distinct_values    18 -> 20
    files               7 ->  9
    live_files          2 ->  4
    new_not_baselined  10 -> 12

The two NEW non-baselined entries:

| witness | field | stored | real |
|---|---|---|---|
| `computations/probes/casimir-q-zeta-probe.witness.json` | `parameters.substrate_q` | `1.10997858275138083783417641825508326292037963867187500000000` | `1.1099785827513808` |
| `computations/rho-k-h3a-lp-dual.witness.json` | `parameters.m_n_MeV` | `939.5654217899999594010296277701854705810546875` | `939.56542179` |

Both are the textbook signature the padding audit exists for: a float64 serialized far
past ~17 digits so the binary-expansion tail reads as measured precision. `m_n_MeV`
is especially clear — the neutron mass is a CODATA input known to 9 decimals and is
stored to 46, of which 37 are an artifact of the double.

**Fix at the producer**, per the audit's own instruction: do not baseline these and do
not hand-edit the numbers. Each is a `parameters` field, so the producer is passing a
Python float into the serializer instead of an `mpf` built from the literal, or instead
of the literal string.

Distinct from `qou-5sg8` (`categorical-bypass-volmatch-demo`) and `qou-txru`
(`chi_sym_alt_closed_form`), which name different files.



---

## Fixed 2026-09-07 — both are ONE root cause: import-time dps

Neither was a bad literal. Both producers hold the right value and lose it on the
way out.

### 1. `casimir-q-zeta-probe` — imported the float64 twin of q_0

`q_parameter` carries q_0 as a **70-digit decimal string** and exposes it twice:

    Q    = float(_d["q"])   # float64
    Q_MP = mpf(_d["q"])     # the full value

The probe did `from q_parameter import Q` then `q = mpf(Q)`, which lifts the
**double's binary expansion**; `fmt()` then serialized it at 60 dps. The two
diverge at digit 17:

    mpf(Q) = 1.109978582751380 837834176418255083262920379638671875   <- committed
    Q_MP   = 1.109978582751380 807591669095610768879874499121873577636 <- true

**Fix:** import `Q_MP`. The witness now carries the true q_0 to all 50 digits.
Downstream values moved from digit ~17 onward — a precision improvement, not a
result change; the leading 16 digits and every assertion are unchanged.

### 2. `rho-k-h3a-lp-dual` — constants imported ABOVE `set_compute_dps()`

`experimental_constants` is imported at line 83; `set_compute_dps()` runs at line
87. So the mpf constants are built while `mp.dps` is still mpmath's default 15 —
they hold 53 bits — and are later serialized at 50 dps, emitting the dyadic tail.
Reproduced bit-for-bit:

    import at dps 15, render at dps 50  ->  939.5654217899999594010296277701854705810546875
    the committed witness value          ->  939.5654217899999594010296277701854705810546875

`m_n_derived_3input` is the visible one because it is a **sum** of three such
values, so the error compounds into the 14th digit instead of the 50th.

**Fix:** serialize with `str_at_true_precision` (already imported at line 69,
just unused here) instead of `str`. Its test is exact and per value — an mpf
equal to its own float64 holds 53 bits and nothing more — so it shortened
`m_n_MeV` to `939.56542179` and correctly left `M_codata_MeV`, `m_e_MeV` and
`m_p_MeV` untouched, because those genuinely carry more than 53 bits.

Moving `set_compute_dps()` above the imports would fix the root cause for every
consumer, but it changes the precision of shared constants across the corpus and
so belongs in its own change, not here.

### Measured

Padding audit, flagged witness files: **10 -> 8**, exactly these two removed and
nothing else moved (before/after run on the same tree). `probe-float64-guard`
reports 25 hits in these two files both before and after — all pre-existing
`float(...)`/numpy/scipy lines, none on a changed line.

**Not addressed:** `rho-k-h3a-lp-dual` carries 67 raw float64 from the LP
solver's solution vector, unchanged by this fix and identical to what was already
committed. That is the raw-float64 backlog, not padding.

`clarabel==0.11.1` was installed in this container before regenerating, so the
LP-dual witness records the same solver as the committed copy rather than
degrading its environment block (the witness guard refuses the weaker record).
