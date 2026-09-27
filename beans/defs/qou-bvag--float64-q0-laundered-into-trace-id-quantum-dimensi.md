---
# qou-bvag
title: float64 q0 laundered into trace_id_quantum_dimension_probe — 17 digits feeding a 50-dps probe
status: in-progress
type: task
priority: normal
created_at: 2026-09-27T06:05:10Z
updated_at: 2026-09-27T06:08:07Z
---

## 2026-09-27 — FIXED. The `f64_into_mpmath` LAUNDERED tier is drained 1 -> 0.

Found by mining the full `precision-gates.sh` log from clean `origin/main`
(already paid for while attributing #7464's reds), which named exactly one site
and called it a defect in its own words:

    LAUNDERED — mpf(str(<f64>)): 1 file(s), 1 site(s). These are defects.
      computations/audits/trace_id_quantum_dimension_probe.py:75  <- qou_substrate.constants.Q

`qou_substrate.constants.Q` is a Python **`float`** (`_solve_q_proton_f64`), so
`mp.mpf(str(Q))` recovers the binary64 exactly and nothing more — **~17
significant digits**. The file sets `mp.mp.dps = 50` and derives every `[n]_q`
and `dim_q` from that one value, so **33 of its 50 digits were noise.**

MEASURED: `1.1099785827513808` vs `q_at(50)` = `1.109978582751380807591669…`,
**rel err 6.84e-18**. Propagated: `[n]_q` differs at 7.1e-19 (n=2) through
5.6e-18 (n=5). Below the L1 1 ppQ target, so no recorded result was invalidated
— but it is a float64 path, and exemption 1 does not have a magnitude threshold.

**Fix:** `Q0 = q_at(50)`, import switched `Q` -> `q_at`. `q_at(dps)` is a Newton
solve on the proton substrate identity, exact at any dps, so this is the **same
pin with the digits it should always have had** — not an anchor change. The
probe's own banner already says "proton pin" and `q_at` is proton.

**Exemption 2 as well as 1: the corpus had already settled this.** Four files
carry the identical fix with the reasoning in a comment —
`log_ratio_binding_prototype:90`, `derived_bond_graph_binding:89`,
`deltalambda/two_row_support_recount:100`,
`deltalambda/l1_ceiling_d_frame_remeasure:115`. This site had simply been
missed. A reviewer can check the change against those four.

**VERIFIED:** probe **8/8 PASSED, exit 0**; gate now prints `LAUNDERED — none.`;
raw-float64 ratchet NEW dirty 0 / REGRESSED 0. Witness moved exactly 3
non-ephemeral fields, all of them the point of the fix: `q0Value`
`1.1099785827513808` -> `1.1099785827513808076`, `dim_q_V1_is_2q`
`2.01089686670712229832263` -> `2.010896866707122299752492` (diverging at the
18th significant digit, as measured), plus `commitSha` provenance.

### 🛑 A grep finds FOUR sites and three of them are NOT defects — I nearly filed that as a detector blind spot

`grep 'mpf(str(Q))'` also hits `casimir_d6_qcorrection_structure:81`,
`probe3qrv:38` and `casimir_xi_2_dig_deeper:111`. All three import
**`Q_MP as Q`** — an `mpf` — so their round-trip is full-precision and carries
no float64. **The gate's count of 1 is correct and the grep is the blunt
instrument**: `f64_into_mpmath_audit` resolves the import to its type, and I
did not. Recorded in the source comment so the next agent does not "also fix"
them.

### NOT actioned — a population, not a site

The same gate reports `F64_CAST — float(<f64>) in a value position: 104
file(s), 184 site(s). These are defects.` That is a corpus-wide sweep and is
**not** covered by either exemption under the 2026-09-07 override; it needs the
owner. Unmeasured by me beyond the gate's own count.
