---
# qou-42u7
title: 'ATTACK #2: does cyclotomic-coeff sign realise Delta_lambda row-grading (-1)^{n(lambda)}? (KL-prune evasion test)'
status: completed
type: task
priority: normal
created_at: 2026-07-19T00:19:26Z
updated_at: 2026-07-19T03:08:45Z
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
