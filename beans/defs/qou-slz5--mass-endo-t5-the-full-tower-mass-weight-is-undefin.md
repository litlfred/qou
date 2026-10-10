---
# qou-slz5
title: 'MASS-ENDO T5: the full-tower mass weight is undefined (D7 scopes convention D to decay only)'
status: todo
type: epic
priority: normal
created_at: 2026-10-10T06:48:53Z
updated_at: 2026-10-10T07:44:03Z
---

Thread (session https://claude.ai/code/session_01ST9RpvTF7JHNdUNafrjf9J). OWNER DECISION gating this thread: D7 (docs/coordination/2026-09-05-owner-gated-bean-triage.md, 2026-09-07) puts mass/binding on the full tower, but production tr_M_via_wenzl_bridge still applies D's two-row cap (keeps 0.0434% of H_12 at 4He). No full-tower mass weight is defined. Candidates: Molien (ruled only for Phi_k), C y_λ (excised), Ocneanu N≠2 (changes the trace).
Children: qou-oots, qou-fq0f, qou-24w9, qou-zf9n, qou-8jq2. Results built on D-weights for mass (zf9n TL-support 16.48%, 24w9 option table) lapse or need re-statement once the weight is chosen.


## 2026-10-10 rerun results
zf9n: TL support survives; the 3.4× cancellation, 16.48% capture and the 10A−5 near-match are grouped-word artifacts (sign flips on borromean words). Two committed witnesses (rho-w-crystal-vertex-trace, delta-lambda-canonical-residual) are stale — regeneration is owner-gated.


## 2026-10-10 — owner said 'try both': two-arm probe (session_01ST9RpvTF7JHNdUNafrjf9J)
computations/deltalambda/full_tower_weight_two_arm_probe.py (+witness), 8/8 checks; control reproduces binding_canonical Δtr < 1e-51. Arms are measures μ_λ (Σμ=1) entering tr = Σ(μ_λ/f^λ)χ^λ; borromean words; all p(3A) partitions; proton q0. Molien uses the Lean-proved balanced form f·q^{−κ_λ}·dim_q (molienSum_eq_qFactorial); the untwisted f·dim_q/[n]_q! sums to 0.922/0.824/0.703 at n=6/9/12.
TL-quotient |share| of Δtr: Molien 7.3% / 0.54% / 0.79% / 0.011% (D/T/³He/⁴He); Plancherel 16.9% / 3.4% / 4.5% / 0.35%. Under either full-tower weight the closure is NOT TL-supported. Molien tr(W_atom) ≈ 1e-75 at ³He/⁴He (zero to working precision; consistent with the regular trace picking the identity coefficient; exact vanishing NOT proved) so B_log undefined there. No ranking, no adoption (anti-fit).
