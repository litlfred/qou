# Phase 3b audit — mass-table downstream (partial)

**Status**: The parallel audit agent's transcript completed but
did not write a full report (agent exited mid-investigation with
one concrete finding surfaced).  This doc captures the **single
confirmed gap** plus a manual scoping pass for the remaining
downstream files; full line-by-line audit is queued for follow-up.

## Confirmed gap (from agent)

**`prop:atomic-mass-via-rho-k` is not a defined content block.**

The script
[`atomic_mass_via_rho_k.py`](../../computations/atomic_mass_via_rho_k.py)
references this label as its `contentBlock` field in the witness
`atomic-mass-via-rho-k.witness.json`, but **no content block with
this label exists** in
`/home/user/qou/content/quantum-observable-universe/`.

Closest existing blocks:
- `prop:rho-k-h3a-refinement` (the `ρ_K^full` derivation race;
  PR #564 deuteron-only proof-of-concept)
- `prop:rho-k-graded-expansion` (the graded-expansion form)

**Fix candidates** (one of):
1. Update `atomic_mass_via_rho_k.py`'s `contentBlock` field to
   reference `prop:rho-k-h3a-refinement` (the canonical
   neighbouring block).
2. Create a new content block
   `content/quantum-observable-universe/braids-and-knots/atomic-mass-via-rho-k.{md,ts}`
   wrapping the LO-formula `M(K) = ρ_K · m_e · |tr_M(K)|` with
   ρ_K = (Z·m_p + N·m_n) / (m_e · |tr_M|).  The script's docstring
   acknowledges that the LO form is **tautological** (the |tr_M|
   cancels in numerator and denominator) — this WOULD be a
   one-paragraph remark, not a substantial proposition.

Either fix is small (15–30 minutes).  **Not done on this PR** —
out of scope; line-flagged for the immediate follow-up PR.

## Manual scoping (without line-by-line audit)

### `binding_K_direct.py` (216 LoC)

Implements the direct binding-energy formula

    B(K) = m_e · Σ_λ y_λ(q) · χ^λ(β_K) · Δ_λ(K)

Paper backing: this formula is the explicit motivator of the
`prop:rho-k-h3a-refinement` block (existence claim on Δ_λ) and
the still-open compute frontier (PRs #602 / #603 / #613).

**Lean status**: `rho-k-h3a-refinement.lean` exists; per
CLAUDE.md §3b-cond it likely class-axiomatises the Δ_λ existence.
The script's role is to **consume** the Δ_λ catalog once
available; currently reports `delta_lambda_unavailable` for every
atom (catalog blocked on the derivation — per Phase 1 audit).

**Verdict** (manual): BACKED-Path-A.  No fitting; honest pending
reporting.  Anti-staleness adopted (3 upstream hashes recorded on
this PR per Phase 1).

### `atomic_mass_via_rho_k.py` (~400 LoC)

Implements the LO ρ_K formula

    M(K)_LO = ρ_K · m_e · |tr_M(K)|
            = (Z·m_p_CODATA + N·m_n_CODATA)/(m_e · |tr_M|) · m_e · |tr_M|
            = Z·m_p_CODATA + N·m_n_CODATA       ⟸ tautology when
                                                  m_p/m_n are CODATA
                                                  inputs

**This is the calibration-tautology that PR #663 exposes.**  The
script's docstring acknowledges this; the legacy ¹H "derived"
status on the mass-table was a 1:1 echo of m_p_CODATA - m_p_pred.

**Verdict** (manual):
- Paper backing: **missing block** (per agent's finding above).
  `prop:atomic-mass-via-rho-k` is referenced but undefined.  GAP.
- Mathematical content: tautological by construction; the
  script's purpose is now **comparison-anchor** rather than
  prediction-producer (the production m_p chain is the full-tower
  path on this PR).
- Anti-staleness: adopted on this PR (7 upstream hash records).

### `paper_six_term_isotope_sweep.py` (~1100 LoC)

Implements the **calibrated M2 mass table** (per-derivation
pathway with CODATA m_p / m_n / Q_β inputs).  This is the
calibrated form (4 calibrations vs no-cal's 2); achieves 0.19 %
MAE per `docs/audits/2026-05-16-m2-mass-table-cos-q-beta.md`.

**Cherry-picked from PR #662 onto this branch**: the
`q_beta_substrate_cos_tightened_MeV()` helper and the
`q_beta_source` flag.

Paper backing for the cos closure:
- `prop:q-beta-cos-resummation` ([q-beta-cos-resummation.md](../../content/quantum-observable-universe/particle-interactions/q-beta-cos-resummation.md))
  — Form A · cos((z−1)·h/2) with c_2 = b² Kashiwara correction
- `prop:hopf-jones-c3-categorical` (PR #664, open) — c_3 = J_Hopf(q=1)
- `prop:q-beta-c2-categorical-proof` (PR #661, merged) — c_2 = b²
  via V_(2,1) Hoefsmit

**Verdict** (manual): BACKED on the cos additions.  The legacy
M2 chain itself has its own audit story (per
`2026-05-16-m2-mass-table-cos-q-beta.md`); not re-audited here.

## Aggregate (Phase 3b)

| file | LoC | claims (manual count) | BACKED | GAP | LEAN_PROVED |
|---|---:|---:|---:|---:|---:|
| `binding_K_direct.py` | 216 | 3 | 3 | 0 | 1 |
| `atomic_mass_via_rho_k.py` | ~400 | 5 | 4 | **1** (missing prop) | 0 |
| `paper_six_term_isotope_sweep.py` | ~1100 | (cos additions only) ~5 | 5 | 0 | 0 (cos refs to PR #661 Lean class) |
| **total** | **~1,716** | ~13 | 12 | **1** | 1 |

## Concrete gap from Phase 3b

**One additional concrete fixable gap**:
6. `atomic_mass_via_rho_k.py` references content block
   `prop:atomic-mass-via-rho-k` that doesn't exist.

(GAPs 1–5 are in Phase 1 + Phase 3a doc summaries; this is gap #6.)

## Roll-up to master INDEX

Updated total: **18 files / ~7,000 LoC / ~74 math claims / 6 concrete
GAPs** across Phases 1–3.  See
[`2026-05-16-compute-paper-lean-audit-INDEX.md`](2026-05-16-compute-paper-lean-audit-INDEX.md)
for the consolidated picture.

**Note**: This Phase 3b doc is **partial** because the parallel
agent completed without writing its full line-by-line report.
The single agent-confirmed gap (atomic-mass-via-rho-k missing
content block) is captured here; a follow-up PR should run the
full per-line audit on `atomic_mass_via_rho_k.py` and
`paper_six_term_isotope_sweep.py` (the two large files that
weren't fully walked in this session).
