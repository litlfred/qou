---
# qou-xapv
title: 'GAP: which Frobenius coproduct does the framework fix (density u in m = |∫(u·ϱ)|)?'
status: in-progress
type: task
priority: high
created_at: 2026-10-13T17:34:21Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-v2om
---

Owner, 2026-10-13: option A2 (keep the antipode, general coproduct). Measured that A2 is already the general form: def:mass-identity has m(ϱ) = ‖∫(u·ϱ)‖ with u = (∫⊗id)Δ(1). MassTraceIdentity.lean proves massIntegrand_eq_leftMul_density, frobeniusForm_massIntegrand and massTrace_eq_functional_hol with no counit hypothesis. The four _of_frobeniusForm_eq_counit theorems are the special case u = 1.

THE OPEN QUESTION. On semisimple H_n(q) = ⊕_λ M_{d_λ}, a Frobenius-compatible Δ is fixed by Δ(1) = Σ_λ c_λ Σ_ij E^λ_ij ⊗ E^λ_ji, so ε = Σ_λ c_λ⁻¹ χ_λ. With ∫ = tr_M = Σ y_λ χ_λ, u = Σ_λ (y_λ/ε_λ) p_λ, so the effective Δ_λ = y_λ/ε_λ. EVERY central invertible u is reachable by choosing ε. A free Δ is therefore a per-block Δ_λ in disguise, which the no-fitting rule forbids.

ADMISSIBLE ANSWERS (derived, not chosen against data):
(a) Δ induced by ∫ itself (ε = tr_M, u = 1): the current state.
(b) Δ induced by the Plancherel trace τ_P(p_λ) ∝ dim_q(λ)·d_λ/[n]_q!: computed in computations/deltalambda/plancherel_density_u_probe.py (PR from claude/frobenius-counit-axiom2-2026-10-13).
(c) a Δ fixed by some other framework principle, not yet identified.

The open part is a structural argument selecting the coproduct. Selecting by agreement with binding data is FORBIDDEN.

ALSO. Under convention D y_(1³) = 0, so tr_M is degenerate on H_n for n ≥ 3. The Frobenius object is then H/rad ≃ TL (proved over CharZero fields, #7768), and u vanishes on three-row blocks.

Do not close until the coproduct is derived (AGENTS §13a).

2026-10-13: Plancherel-density probe landed (computations/deltalambda/plancherel_density_u_probe.py; docs/audits/2026-10-13-plancherel-density-u-vs-cocasimir.md). Results:
- u^(b)_λ = y_λ[n]_q!/dim_q(λ). It is not proportional to the co-Casimir.
- It is non-negative on every block, so it cannot equal the signed Δ_λ (scope b).
- It fails the deuteron test (scope a).
- It vanishes on blocks with 3 or more rows.
- ε = tr_M is not a counit on H_n for n ≥ 3; it is one only on TL.
Neither (a) nor (b) yields a usable density. Candidate (c), a coproduct fixed by some other framework principle, stays open.
Side finding: the corpus carries two distinct 'Plancherel trace' objects (with and without q^{-κ_λ}).
Side finding: the Lean coCasimirSum constant 0.14496 is stale against the witness value 0.17312. The inequalities still hold.

2026-11-15: the stale coCasimirSum is fixed. DeltaLambdaRefutation.lean now carries the regenerated witness figures (rho-k-h3a-co-casimir.witness.json, 2026-10-05, proton pin): coCasimirSum 0.173120471677, targetSigned -4.353367491256, closureGap 4.526487962933 (12-figure truncations; the gap identity is exact over Q). lean-direct exit 0, axioms [propext, Classical.choice, Quot.sound]. The refutation verdict is unchanged. The two-"Plancherel trace" rename is still open and waits on the owner.

2026-11-15: renamed across the corpus on the owner's choice. "Plancherel trace" was three objects, not two: the canonical trace (with q^{-κ_λ}, MolienFakeDegree), the unweighted Plancherel functional τ_P (frobenius-codim-universal.lean), and the q-Plancherel measure trace tr_qP (weights dim_q²/[n]_q!, hoefsmit_symbolic.py). General Σ W_λ χ^λ sums are now "W-weighted traces". Docstrings and prose only; no values, function names or file names changed. Table in docs/audits/2026-10-13-plancherel-density-u-vs-cocasimir.md §Naming.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `(none)` → `qou-v2om`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.

## Round 79 progress (PR #8358)
- Advanced in PR #8358 (`3d5e94f03a32259e850c4108650709877896bfd7`).
