# Topic 1 VolDensity(𝓑₃) refinement — session status (2026-06-01)

**Branch:** `claude/vol-density-bz3-refinement-2026-06-01` (PR #1664)
**User direction:** Pursue A + B + C (all three queued research routes; NOT D-stop)
**Outcome this session:** Each option scoped + baseline measured. No closure (research-grade horizon 1-4 weeks per option).

## Baseline measurement (verified this session)

`m_p_borromean_verification_50dps.py`:

| Predicted | CODATA | Δ |
|---|---|---|
| m_avg | 938.92 MeV | +28896 ppm (+2.89 %) |
| Δm/M_N | 0.001377 | +305 ppm (0.030 %) |

The +2.89 % is on m_avg; the p/n split is already 99.97 % correct.

Confirmation via `linking_weight_canonical_object_lwfix.py` (sibling branch):
- Family A H_4 average λ_A = 5/2 + (3/4)h² = **2.532780** at q_0
- CODATA-implied λ (round-trips m_p): **2.461648**
- Gap: **+2.890 %** exactly = the m_avg residual
- Switching to H_3 per-block REGRESSES to −56.7 % (RULED OUT)

## Option A — Bring color-tube to base mass scale: tested, doesn't close

`closed_form_tau_M.bring_color_weighted` is IMPLEMENTED (not NotImplementedError as the cheat sheet says). Measured shift on atomic ratios at q_0:

| atom | strict_averaged | bring_color_weighted | shift |
|---|---|---|---|
| D | 0.39479 | 0.39486 | +0.018 % |
| ⁴He | 0.057218 | 0.057228 | +0.018 % |

**0.018 % is ~160× smaller than the 2.89 % m_avg gap** (`2.89 / 0.018 ≈ 161`). The existing color_weighted convention is a per-p-n-interface correction (closes the 0.030 % p/n split toward 0.14 %); it does NOT contribute to the base mass scale. (Note: a separate later analysis using the symmetric δ² term — base-scale extension via `bring_color_weighted_linking_weight` — measures the m_avg shift as 842.8 ppb, which is the ~34290× gap to the +2.89 % residual at the BASE scale; that is a distinct quantity from this per-interface 160× number.)

To shift m_avg, Option A would need a DIFFERENT categorical formalism — e.g. per-sheet PL integration on Bring's surface contributing to the BASE m_avg, not just the per-interface asymmetry. This is research-level (color-sheet ↔ quark-flavor mapping not in the paper). 1-2 weeks.

## Option B — g·g' substrate-derived couplings: 3 Lean theorems scaffolded

`content/quantum-observable-universe/lean/QOU/BraidKnot/SubstrateEWHypotheses.lean` has 3 conjectural-class theorems with documented derivation gaps:

| Hypothesis | Empirical | Lean theorem | Gap to close |
|---|---|---|---|
| g = π·h_0 | +0.26 % | `g_eq_pi_h_substrate_hypothesis` | Yekutieli MI connection-1-form integration |
| v_framework / v_SM = log(\|S_3\|) | −0.50 % | `v_ratio_eq_log_S3_hypothesis` | Chern-Simons partition function on S_3 |
| 171/143 = 6/5 | +0.35 % | `scalar_gauge_ratio_eq_six_fifths_hypothesis` | Explicit categorical scalar/gauge mass-factor formulas |

Structural anchor theorems already closed-rfl:
- `gsNFBasisCardinalityB3_eq_six` ✓ (PROVED `:= rfl`)
- `partitionsOfFour_eq_five` ✓ (PROVED `:= rfl`)
- `cardS3_eq_six` ✓ (PROVED `:= rfl`)

The structural anchors (6 = \|S_3\|, 5 = partitions of 4) are PROVED unconditionally; the empirical-match-to-formula step is the open `sorry`. Each closure is 1-2 weeks per audit `2026-05-24-ew-couplings-substrate-empirical-matches.md`.

**Note:** Option B does NOT directly close the m_avg gap. It closes Lean targets for EW couplings derivation. Closing the m_avg gap is a separate problem.

## Option C — Bloch-Wigner higher-rank Lake-wiring: queued under PR #956 roadmap

Per PR #956 roadmap (cited in `lambda-scale-absorbed-into-vol-density.md`):
1. Lake-wire `QOU.Archimedean.BlochWigner_unit_circle` into module tree
2. Strengthen `BringZeroModeBlochClass.bringZeroModeValue` field from
   `∃ z : ℝ, z = ...` (literal-rfl loophole)
   to `∃ θ : ℝ, BlochWigner_unit_circle θ = ...` (substantive)
3. Auxiliary to `VolDensity` refinement — provides ONE potentially-novel categorical class beyond the refuted unit-circle Bloch-Wigner.

This is Lean infrastructure work; the categorical-novel class itself (higher-rank Bloch-Wigner) hasn't been identified yet.

## What this session did NOT do (honest scope)

- DID NOT close the m_avg gap (research-grade per the canonical reference; 5+ routes refuted)
- DID NOT close any of the 3 Lean sorrys in SubstrateEWHypotheses.lean (each is 1-2 weeks)
- DID NOT find a novel attack vector beyond the existing queued routes
- DID NOT touch the owner-active **per-isotope Borromean-tower + operator-valued branching combiner** (cited as the actual Subgoal-1 closure path in `docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`)

## Relation to recent main landings (Items A/B/C from triage)

Triage report (Explore agent, this session) confirmed:
- Item A (m_n standard-channel correction NULL): refuted at higher-rank
- **Item B (Bring zero-mode reframing): the real open question is "WHY does EM couple to H_3's sign block?" — substrate QCD color-singlet + Wedderburn projection.** Does NOT close m_avg but reframes a related open question.
- Item C (deuteron Plancherel NULL): refuted

None of A/B/C close m_avg. The +2.89 % is confirmed genuine and structural.

## Recommendation

PR #1664 should LAND this status doc (concrete baseline + scope assessment) and the branch should pause. Real progress on Topic 1 requires:

1. **Owner-active Subgoal-1 work** (per-isotope Borromean-tower + operator-valued branching combiner) — this IS the path, owner is on it.
2. **NEW categorical attack vectors** not yet on the refuted list (operator-valued linking_weight, q-Plancherel weights, higher-rank H_n basis, different fibre functor).
3. **Long-horizon Lean work** on Option B (1-2 weeks per theorem).

Topic 1 is genuinely multi-session, multi-person research. Closing the +2.89 % m_avg gap requires either (a) the owner's Subgoal-1 infrastructure to land, or (b) a categorical insight not yet identified.

## Cross-references

- Canonical reference: [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md)
- L2 100× status (3 failing shared root): [`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`](../audits/2026-05-30-l2-100x-status-3-failing-shared-root.md)
- linking_weight-residual confirmation: [`docs/audits/2026-06-01-linking-weight-residual-fix.md`](../audits/2026-06-01-linking-weight-residual-fix.md)
- bring_color_weighted implementation: [`computations/closed_form_tau_M.py:178`](../../computations/closed_form_tau_M.py)
- SubstrateEWHypotheses Lean targets: [`content/quantum-observable-universe/lean/QOU/BraidKnot/SubstrateEWHypotheses.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/SubstrateEWHypotheses.lean)
- Cheat sheet §5: [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
