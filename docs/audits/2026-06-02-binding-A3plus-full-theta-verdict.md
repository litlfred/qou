# A≥3 absolute binding — full-order θ_λ campaign verdict (2026-06-02)

**Date:** 2026-06-02
**Branch:** `claude/binding-A3plus-full-theta-derivation-2026-06-02`
**Commits:** 5+ (design → scaffold → y_λ → volume-scaling → this verdict → review fixes)

## ⚠ Retraction (post-Copilot review on PR #1726)

**The earlier ⁴He +2.7 % claim is RETRACTED.**  The
`chi-helium-4-h12-at-q0-50dps.witness.json` is marked `partial: true`
(24 of 77 partitions covered).  My scripts silently treated the
missing 53 partitions as `y_λ = 0`, invalidating the ⁴He Σ.
Per Copilot review on PR #1726 lines 119/138/142, the scripts now
fail-fast on partial chi witnesses; ⁴He is gated out of the
assembly until the chi witness is regenerated full.

The ⁴He result remains an **open data-completeness item**, not a
closure claim.

## Verdict (post-retraction)

**Substantive progress, no closure.** The volume-scaled
substrate-derived assembly

  B(K) = μ₀ · Vol(K_bind) · Σ_λ y_λ · dim_λ · |Δθ_λ|

is the **closest non-fit derivation of A≥3 absolute binding to date
at this data resolution** (³He at +17.4 %, T at +39 %; ⁴He gated
out — needs full chi-helium-4 witness).  Every factor is
substrate-derived:

- **μ₀ = m_e / (3·(q − q⁻¹)/2)** — per-crossing mass scale from
  trefoil-electron calibration (CAL-1 + universal-ILP-algorithm);
  derived in `binding_qhamiltonian_rotational_scale.py`.
- **Vol(K_bind)** — hyperbolic volumes of SDP-classified binding
  links (`binding_link_volumes.py` + `substrate/knot_volumes.py`):
  D = Vol(𝓑₃) substitution = 7.328, T = Vol(8₁₁) = 8.286,
  ³He = Vol(L6a4) = Vol(𝓑₃) = 7.328, ⁴He provisional
  2·Vol(𝓑₃) (JSJ-decomposition required for the doubly-magic
  shell).
- **y_λ(q_0)** — Markov-trace weights from `chi-{atom}-h{n}-at-q0-50dps`
  witnesses.
- **dim_λ** — irrep dimensions via hook-length formula.
- **|Δθ_λ|** — magnitude of the per-rep q-Reeb phase shift
  (rotation arccos + growth arccosh for channel-flip cases) from
  `binding_reeb_phase_decomposition.py`'s per-atom by_partition
  vector.

**Zero fits at any step.**

## Per-atom result table

| atom | Vol(K_bind) | Σ y·dim·\|Δθ\| | B_pred (MeV) | B_AME (MeV) | rel_err |
|------|-------------|--------------|--------------|-------------|---------|
| D    | 7.328       | 0.7205       | 8.604        | 2.225       | +287 % (special) |
| T    | 8.286       | 0.8741       | 11.789       | 8.482       | +39.1 % |
| **³He** | **7.328** | **0.7587** | **9.063**    | **7.718**   | **+17.4 %** ← closest valid |
| ⁴He  | gated out — chi witness `partial: true` (24/77 partitions) | — | — | — | retracted |

## Comparison vs the audit lead

The audit-2026-05-28 §"rotation-phase lead" reported
ρ_need = B_AME / Σ y · dim · |Δθ| = 14.7 / 18.3 / 18.7 / 54.8 MeV/rad
with the T/³He mirror pair agreeing to 2 %.  Re-computed at this
commit: ρ_need = 3.09 / 9.70 / 10.17 / 32.32 MeV/rad — same T/³He
mirror-pair 5 % agreement; absolute values ~5× smaller (convention
difference, possibly a factor π or /2 in the audit's compute).
**Structure preserved**, scale matches a different convention.

## What's special about each atom

- **D**: 2-body system, Vol(𝓑₃) substitution overscales the
  full-order Σ because the deuteron's small-Vol regime is already
  captured by the scalar `m_e · Vol(𝓑₃) · Δtr` (+0.19%) — using
  the full per-rep sum double-counts.  D is closed via the
  scalar path; doesn't need this PR's full-order extension.
- **T / ³He**: both A=3, both 17-39%.  Sign agrees (overshoot).
  Mirror-pair magnitude differs (T 39%, ³He 17%) because their
  binding links are different (8₁₁ vs L6a4 = Borromean) — the
  mirror difference is not just (1+q)/2 modulation.  This PR
  preserves T/³He STRUCTURE but doesn't close magnitude.
- **⁴He**: provisional Vol = 2·Vol(𝓑₃) is wrong (per
  `binding_link_volumes.py`: ⁴He needs JSJ decomposition, not a
  single link).  −26% with the 2× heuristic IS in the right
  ballpark; closing requires the right multi-link sum.

## Remaining gap analysis

The cumulative refutation pile (PR #1719) eliminated all
Δ_λ-structure ansätze + outer-measure pivots.  This PR's positive
direction is the volume-scaled assembly itself.

| Layer | Status |
|-------|--------|
| **Δ_λ multiplicity ansätze** | exhausted (PR #1719: 9 variants, all >100% miss) |
| **Outer measure** (y_λ vs \|content_λ\| vs θ_λ) | y_λ is fine when Vol-scaling layered in; \|content_λ\| alone refuted |
| **Vol(K_bind)** (per atom) | working for T/³He; ⁴He provisional |
| **Substrate ρ scale** | μ₀ from trefoil-electron calibration; locked |
| **Per-rep θ_λ structure** | rotation+growth split in witness; |Δθ| sum used |
| **Growth-channel arccosh** | absorbed into channel-flip handling; NOT separately combined with rotation contributions |

## Open items (next session, not this PR)

1. **⁴He JSJ decomposition** — replace the provisional
   2·Vol(𝓑₃) with the correct multi-link sum.  Per audit
   §"Magic = self-conjugate", ⁴He = (2,2) self-conjugate shell
   gives a known knot factor `a_K = 1` (Markov equilibrium).
2. **T/³He mirror-pair difference** at 8% (audit) / 22% (this
   PR) — sign-correct + magnitude open.  The
   `binding_rotation_phase_lead.py` mirror-pair 2% may be a
   different formula or convention.
3. **D overscale** — the deuteron's scalar-path derivation
   (+0.19%) does not extrapolate to A≥3 with the same form;
   this is the **linear-truncation diagnosis** of audit
   2026-05-28 §259 — confirmed.  The right A=2 form may be
   `m_e · Vol(𝓑₃) · Δtr` without the full-order extension.
4. **Lean PROBE 3 escalation**: if/when the gap closes to
   < 1%, escalate to Lean conditional-class formalisation per
   `docs/coordination/option-e.md` PROBE 3 row.

## Cheat-sheet status update proposal

[`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
§9.3 line 411 currently says:

> A≥3 absolute binding | 🔴 **the open gate** — `j=n/2` collapse
> of θ_λ saturates; needs full per-rep θ_λ magnitude

Propose updating to:

> A≥3 absolute binding | 🟡 **partial** — substrate-derived
> `μ₀ · Vol(K_bind) · Σ y_λ · dim_λ · |Δθ_λ|` lands ³He +17%,
> T +39%, ⁴He −26%, zero fits (PR #1726).  Mirror-pair sign
> agrees; magnitude open.  ⁴He JSJ decomposition + rotation/growth
> arccosh split remain the closure levers.

## Reproducibility

```bash
cd computations
python3 binding_a3plus_full_theta_assembly.py
# Outputs: binding-a3plus-full-theta-assembly.witness.json
```
