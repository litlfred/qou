---
# qou-mjcd
title: y_lambda muon cache is at RETIRED pin A, and a declared-proton producer straddles on it
status: in-progress
type: bug
priority: high
created_at: 2026-08-30T12:32:00Z
updated_at: 2026-08-30T12:32:00Z
---

Found while closing `qou-0hnz`; measured before filing.

## The cache

`computations/y-lambda-mpfr-witness.json` is stamped `q0Anchor: muon` and holds
`q_0_50dps = 1.1099785955573347198997632204832250266562084087802` — **pin A**,
the vintage `fca08de7d2` RETIRED on 2026-08-22 (owner ruling "A -> CODATA 2022").
The current muon pin is C, `1.109978595642739…`. So this table is stale *as a
muon table*, independently of anything else.

**13 files read it on a non-comment line** (resolved, not `grep -rl`):
`atomic_tr_m_mpfr_50dps`, `audits/y_lambda_two_row_cap_gate`, `binding_K_direct`,
`chi_dual_path_xref_audit`, `iterative_lp_dual_h6_deuteron`,
`regenerate_y_lambda_mpfr`, `tr_m_wenzl_bridge_mpfr`, `witness_regen_wave`,
`y_lambda_macdonald_telescope`, + 4 more.

## The live straddle, quantified

`computations/iterative_lp_dual_h6_deuteron.py` is **manifest-declared
`physical_proton`** and `q_parameter.Q` resolves to `1.1099785827513808` for it.
But:

- `:155` `y_at_q0` <- `y-lambda-mpfr-witness.json`  (muon / pin A)
- `:174` `chi_at_q0` <- `chi_lambda_numerical(..., q_val)` where `q_val =
  float(Q0_FLOAT)` (**proton**)
- `:185` `tr_M_check = sum(y_at_q0[p] * chi_at_q0[p] ...)` — **the product mixes
  the two layers**

Consequence, measured in the committed witness: it declares `q0Anchor: proton`
and records `parameters.q_0 = 1.1099785827513808`, yet
`tr_M_check_at_q0 = 0.5751722457697738` sits **3.22 ppb** from the corpus
canonical proton `tr_M(beta_D) = 0.5751722439177718708265`. That gap IS the
straddle. A declared-proton witness is asserting proton over a mixed number.

## Todo

- [x] Decide the fix at the consumer: a declared-proton producer should read the
      PROTON table (`y-lambda-mpfr-proton-witness.json`), which
      `tr_m_wenzl_bridge_mpfr._Y_LAMBDA_BY_ANCHOR` already maps.
- [x] Confirm the proton table covers partitions of 6 before swapping.
- [x] Audit the other 12 readers for the same mixed-product shape.
- [x] Separately: the muon table is at a RETIRED vintage. Regenerated at pin C on
      owner instruction 2026-08-30.
- [x] Regenerate affected witnesses (qou-jjge).


## Progress 2026-08-30

**Consumer fixed and verified.** `iterative_lp_dual_h6_deuteron` now takes its
weights from `tr_m_wenzl_bridge_mpfr.load_y_lambda_for_q0(6, Q0_FLOAT)`, which
selects the table from the q0 it is handed and refuses to serve the other
layer's. Measured on the regenerated witness:

| | tr_M_check_at_q0 | gap from canonical proton |
|---|---|---|
| before | 0.5751722457697738 | **3.22e-9** (the straddle) |
| after  | 0.5751722439177743 | **4.22e-15** (float64 round-off) |

All 3 assertions still pass.

**Audit of the other 12 readers — one more live instance found, and it was
already failing.** `y_lambda_symbolic_validate.load_mpfr_witness()` hardcoded
the muon table, while `Q0_STR = q_parameter.Q_50_DIGIT_STR` (PROTON) is in
`PROBES`, so `test_1_cross_q` used muon weights as the reference for the proton
probe at `TOL_CROSS_Q = 1e-30`. Run before fixing:

```
q=1.05                     4.41e-51  PASS
q=1.08                     4.57e-52  PASS
q=1.10997858275138080759…  5.93e-10  FAIL   <- the only probe reading this table
q=1.15                     2.16e-51  PASS
q=1.20                     9.36e-52  PASS
```

Fixed by selecting the table from `anchor_of_q0(Q0_STR)`, raising rather than
guessing. After: the proton probe passes at **1.93e-51**, same order as the rest.

The remaining readers are clean: anchor-aware via the accessor
(`atomic_tr_m_mpfr_50dps`, `chi_dual_path_xref_audit`, `binding_K_direct`,
`y_lambda_two_row_cap_gate`), the writer/accessor themselves
(`regenerate_y_lambda_mpfr`, `tr_m_wenzl_bridge_mpfr`), muon-only consumers, or
already fixed for this exact defect (`y_lambda_tower_infra`, whose comment
documents it).


## 2026-08-30 — muon table regenerated at pin C (owner-instructed)

`regenerate_y_lambda_mpfr.py --anchor ideal`. `--anchor ideal` writes ONLY the
muon cache, so the proton table is untouched (verified unmodified).

    before  q_0_50dps = 1.1099785955573347198997632204832250266562084087802  (pin A, RETIRED)
    after   q_0_50dps = 1.1099785956427390466817951293800017527000655610290  (pin C, current)

The anchor source is `q-pinning-50-digit.witness.json` → `derived_50_digit.q`,
which already held C; the table was simply behind it.

**This was only possible because of `f4cafc561`.** `load_y_lambda_for_q0`'s
straddle guard reads the TABLE's own declared pin and raises when it disagrees
with the requested anchor. Before that fix `anchor_of_q0` recognised muon ONLY
as vintage A, so a C-valued muon table would have resolved to `None` and the
guard would have raised "declares the None pin" — the muon cache could not have
been moved to the live pin at all. Verified after regenerating:
`anchor_of_q0(C) = muon`, and both anchors now serve their own table
(`muon → 0.115324226225387`, `proton → 0.115324224902066`).

**Movement is small**: 47 of 270 entries changed, worst relative move 3.06e-10.
The other 223 are the exact zeros convention D forces for partitions with ≥3
rows (Wenzl level r = 2), which do not move at any q. For scale, A→C is 0.0769
ppb against the 11.5371 ppb μ–p gap — this is the small correction, not the
large one.

**A `q0Value` gap was found and closed in the same pass.**
`stamp_staleness_metadata` writes `q0Value` only inside
`if "q0Anchor" not in payload`. This producer declares its own `q0Anchor`
deliberately, so the stamper's block was skipped and the explicit
`q0_value=q0_str` it was handed was silently dropped — the first regenerated
table came out with `q_0_50dps` and NO `q0Value`. That is not the stamper
misbehaving: the 2026-08-24 change removed a carry-forward that paired a fresh
label with the previous run's number. A producer stating its own anchor is
expected to state its own value, so it now does, from the same `q0_str`. Label
and number are byte-identical and cannot disagree.

**Downstream, measured** by searching for the 42 pin-A y_λ values that actually
moved: only **2** committed artifacts still carry one —
`y-lambda-macdonald-telescope.witness.json` (42 values) and
`qbeta-c8-c10-pell-lucas-closed-form-predictions.witness.json` (1).

### Still open on this bean

- [x] Regenerate those 2 downstream artifacts (qou-jjge).
- [ ] `y-lambda-symbolic-validation.json` is stale corpus-wide now and needs a
      FULL pass; it was left at HEAD rather than committed half-fresh. n=11's
      Test 3 does not complete in 50 min, which is what blocks it.


### Downstream regenerated — and one of the two was misdiagnosed

`y-lambda-macdonald-telescope.witness.json` — a genuine consumer of the muon
table. Regenerated: all 42 stale pin-A values gone, all 42 fresh pin-C values
present, 16 assertions still pass. Its `truncation_eps` was a bare `0.0`
float64; drained to `"0"`, which is also more honest — the computation is
symbolic in q, so the truncation error is exactly zero, not zero-to-53-bits.

`qbeta-c8-c10-pell-lucas-closed-form-predictions.witness.json` — **not a muon
table consumer at all.** My value-matching search flagged it because its
`b_squared_at_q0` coincided with the pin-A y_λ for n=2, λ=(2,) — the same
Hoefsmit quantity, so the collision is substantive rather than accidental. Its
producer takes b² from `q-beta-operator-valued-N3.witness.json`, which is
`q0Anchor: proton`. The witness was simply STALE against its own upstream:

    recorded   0.752702113845204172470…
    upstream   0.752702113251965401593779

differing at the 10th digit. Regenerated; it now matches the upstream exactly.
Pre-existing staleness, unrelated to the pin-C move — surfaced by it, not caused
by it.
