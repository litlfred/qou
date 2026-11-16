---
# 46ke
title: 'Integration: canonical watcher - hidden codata literals rollup (53 scripts)'
status: in-progress
pr: 8188
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-06-21T21:44:26Z
updated_at: 2026-11-16T20:23:00Z
parent: qou-2002
---


## 2026-06-22 — PR #2606 (branch claude/tender-wright-oyyyky)
Routed 3 high-value production scripts off hardcoded CODATA literals:
- meson_mass_from_hecke.py (7 literals → registry; output bit-identical)
- beta-decay-from-q.py (m_e/m_e_err → M_E_MEV/M_E_MEV_ERR; output unchanged)
- canonical_isotope_witness.py (u→MeV → new public U_MEV export; identical)
Added public U_MEV alias + __all__ entry to codata_constants.py.
Deferred: option_e_*/probe_*/delta_lambda_* probe tail (low value);
docstring/narrative-print false positives (canonical_tower, derive_m_n,
free-neutron-decay) left alone.

## 2026-06-23 — coordination (branch claude/cool-johnson-t1wveh)
Sibling branch `claude/codata-46ke-rollup-2026-06-22` is ACTIVELY
draining this bean (last seen: "batch 7 — ³He/D/T/⁴He AME binding
literals"). To avoid double-routing:
- Already routed by me (PR #2606, see above): meson + beta-decay +
  isotope-witness production scripts, plus the public U_MEV export.
- Owned by the sibling now: the AME-binding literal sweep
  (³He/D/T/⁴He and the rest of the AME batches).
- Remaining unclaimed tail: the `option_e_*/probe_*/delta_lambda_*`
  exploratory scripts (low value — diminishing returns).
Handing the remaining production sweep to the sibling; not picking up
further 46ke work from this branch to prevent collisions.

## 2026-06-30 — PR (branch claude/46ke-codata-literals-rollup-2026-06-30)
Audit + safe down-payment, NOT a blanket sweep. Key finding: the registry
`codata_constants.py` stores values at a FIXED 50-dps snapshot (plain
validation constants M_MU/U_MEV/M_K/M_PI at default ~15 dps). Routing is:
- raw-bit-identical ONLY for M_E_MEV / M_P_MEV_VALIDATION at <=50 dps
  (set_compute_dps() DEFAULT is 65 → many `_50dps` scripts actually run 65,
   witness-identical but not raw-identical);
- precision-LOSING for M_MU/U_MEV/M_K0 (registry made at default dps) → would
  change numbers even at 50 dps. Needs a registry fix first (= me3r scope).
Routed (proven bit-identical at dps=50): yekutieli_volume_join.py:456 (m_e).
Data-integrity handoff (do NOT silently route — changes numbers):
- WRONG u→MeV `931.49410372` (vs 931.49410242) in mass_binding_dashboard.py:178
  + m_sym_error_budget.py:50 → ce18 (genuine bug, production scripts).
- proton/neutron variant edition `938.27208943/939.56542194` in
  probes/hecke_channel_binding_probe + probes/deuteron_fpn_wlambda_wiring → me3r.
- truncated 8-fig m_e `0.51099895` across many scripts → me3r truncation class.
Deferred (low value per prior drains): probes/qbeta/phase5/ocneanu/mmu/_deprecated.
Full partition: docs/audits/2026-06-30-codata-literals-rollup-precision-partition.md

## 2026-06-30 — CORRECTION (u→MeV direction was backwards)
NIST-verified: m_u c² = 931.49410372(29) MeV is CODATA-2022; 931.49410242(28)
is CODATA-2018. The registry U_MEV (931.49410242, from AME2020 metadata) is the
2018 edition → STALE. The scripts mass_binding_dashboard/m_sym_error_budget
using 931.49410372 are CORRECT (2022). So this is an edition inconsistency, NOT
a bug in those scripts. Fix = bump the registry + AME2020-derived constants to
CODATA 2022 (value-changing for AME binding witnesses → owner-gated, me3r/ce18).
Do NOT route those scripts down to the stale registry value.

> **Investigated 2026-07-05 (swarm 2, PR #3344) — deferred, kept OPEN.** 307 files/521 occ; ~495 docstrings/anchors (out of scope), 17 in _deprecated/, 0 bit-safe inline literals remain. ~5 active float live-inputs unpinnable: root blocker is truncated registry witness codata-2022-validation-masses (m_e=0.51099895, 8 figs) — pinning fuller values loses precision. Gated behind bean me3r (owner, value-changing).



## 2026-08-10 — re-scoped with a measurement (PR #4960)

The 2026-06-23 note files the remaining tail as *"low value — diminishing
returns"*. That is measurably wrong, and the reason is a distinction this bean
never drew. A hand-typed CODATA value is one of two things:

- **duplication** — the literal equals the canonical value. Bad practice, goes
  stale on the next revision, but computes the right number today.
- **truncation** — the literal is a short *prefix* of the canonical value. It
  computes a **different number**, silently, forever.

Only the second changes results, and no precision gate in the tree can see it:
the NO-FLOAT64 family checks how a value is *carried and serialized*, never
whether it was *right when typed*. Wrapping a truncated literal in `mpmath.mpf`
— the standard drain — removes the float64 and preserves the error, and reads
as a fix.

Three landed on main in a single day (2026-08-10), all via float64 drains:

| literal | canonical | cost |
|---|---|---|
| `m_e = 0.51099895000` | 0.51099895069 | 1.35e-9 in kappa |
| `q0 = 1.10998` | 1.1099785827… | 1.9e-7 in contRatio |
| `proton = 938.272` | 938.27208943 | ~1e-9 in vol ratios |

all orders of magnitude above the L1 1-ppQ (1e-15) target. The m_e figure is
measured, not assumed: f64 arithmetic on the *same* inputs contributes
5.06e-16, so the literal was the entire discrepancy.

**Current size, measured rather than estimated** —
`computations/codata_truncation_audit.py` (new, PR #4960):

    TRUNCATED   86 occurrences in 70 files
      q0  35   m_e 25   m_p 15   m_n 9   u_MeV 2
    exact duplicates (not blocking)  158

So the bean's "53 scripts" undercounts the files and, more importantly, mixes
the two classes. The **86 truncations are the urgent subset**; the 158 exact
duplicates are the original scope and stay low-priority.

The audit reads its canonical table from `codata_constants` / `q_parameter` at
run time rather than typing the values — a checker for hardcoded constants that
hardcodes them would go stale in exactly the way it exists to detect.
`--strict` blocks on truncations only. **The drain itself is NOT done**: 70
files is its own sweep.

## Progress Update (2026-11-16, PR #8188)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/CodataTruncationAndQ0AnchorRecentering.lean` (wired into `QOU.lean`, `0` `sorry`, `0` vacuity advisories across all 7 static audits).
- [x] Paired with 50-dps `mpmath` + `sympy` verification probe `computations/probes/codata_truncation_and_q0_anchor_recentering_probe.py` and stamped witness `computations/probes/codata-truncation-and-q0-anchor-recentering.witness.json` (`allPassed: true`, `0` raw `float64` fields, `scriptCommitSha: 4f0055fd85b9bb82232f9b87ef757139e895bd6d`).
- [ ] Awaiting merge of PR [`litlfred/qou#8188`](https://github.com/litlfred/qou/pull/8188) (`548ed6acbe88e5772065a0fdb4d623f3472d3430`).

