---
# qou-42u7
title: 'ATTACK #2: does cyclotomic-coeff sign realise Delta_lambda row-grading (-1)^{n(lambda)}? (KL-prune evasion test)'
status: completed
type: task
priority: normal
created_at: 2026-07-19T00:19:26Z
updated_at: 2026-07-19T03:59:53Z
---


## RESULT (2026-07-19) — HONEST NEGATIVE, scope-(a). Test RUN + decisive.

Probe `deltalambda_cyclotomic_sign_map_probe.py` (4/4, exit 0):
- **Identity CONFIRMED**: `sgn(w_0^{S_{λ'}}) = (-1)^{n(λ)}` exactly (n=2..7). The Δ_λ
  chirality sign IS the row-grading. Per-n spread 1+/2- (n=3), 6+/5- (n=6)
  **reproduces the corpus PROBE-4 deltaSign exactly** — cross-validation.
- **Masbaum coeffs ARE mixed-sign**: `sgn(C_{5₂,n}) = (-1)^n`.
- **WALL (decisive)**: `(-1)^{n(λ)}` is mixed WITHIN each n (per-partition), but the
  cyclotomic coefficient carries ONE sign per INTEGER n — wrong resolution, cannot
  resolve the per-λ sign. And the SYT-weighted aggregate `Σ(-1)^{n(λ)}f^λ` does not
  even sign-match `(-1)^n` (n=1,2,4,5,6), so it isn't the signed tr_M aggregate either.
- **CONCLUSION**: the naive cyclotomic-sign → Δ_λ transfer is CLOSED (refuted as a
  direct source). NARROWING: any cyclotomic→Δ_λ route must go through a
  partition-refinement splitting C_{K,n} into per-λ pieces — the GS-filtration
  bridge, **bean qou-my68**. That bridge is the true remaining step; this rules out
  the shortcut around it. scope-(a); no fit; no c_k.

Status: test complete. Follow-up = qou-my68 (GS-filtration partition-refinement).

## FOLLOW-UP CORRECTION (2026-07-19, ATTACK 1) — cyclotomic route fully CLOSED; my qou-my68 pointer was WRONG
Probe `computations/deltalambda/deltalambda_sign_valuation_not_coefficient_probe.py` (3/3, scope-(b)):
- The Δ_λ sign (-1)^{n(λ)} is the fake-degree VALUATION (bottom jet-order monomial q^{2n(λ)}),
  ALREADY DERIVED (witness deltalambda-grho-jet-order-derivation; n(λ)=min maj(SYT), Steinberg/Lusztig).
- route V (valuation) reproduces it ∀λ; route C (cyclotomic residue R_λ(i) of the FULL trace) is
  NON-REAL ((2,1)→-1+i), ZERO ((2,2)), or sign-mismatched — the cyclotomic COEFFICIENT does NOT carry
  the sign. The "cyclotomic→Δ_λ refinement" collapses to the derived valuation → CLOSED.
- CORRECTION: my earlier "route through qou-my68" pointer was WRONG — qou-my68 is the Q_β Habiro
  same-element task (HabiroGBSameElement), NOT the Δ_λ bridge. The Δ_λ sign is not blocked on it.
- OPEN Δ_λ leg (redirect): the MAGNITUDE assembly Δ_λ = tr(g_ρ) into B = m_e Σ y_λ χ^λ Δ_λ — a
  magnitude problem, not a sign/cyclotomic one.
