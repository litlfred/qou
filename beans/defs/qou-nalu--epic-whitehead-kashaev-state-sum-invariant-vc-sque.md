---
# qou-nalu
title: 'EPIC: Whitehead Kashaev — state sum → invariant → VC squeeze proof → c_σ'
status: todo
type: epic
created_at: 2026-08-01T19:45:01Z
updated_at: 2026-08-01T19:45:01Z
---


## Arc map (2026-08-02) — status
COMPUTE (all done, MERGED to main via #4382/#4310/#4394):
  qou-kkog ✓ invariant pinned + VC→4G   qou-x76e ✓ van der Veen positive-sum
  qou-4zup ✓ c_σ≈0.595, p=3/2, factor 2  qou-xvy1 ✓ #4394 merged (d655e2d0)
LEAN (in #4532, sorry-free so far):
  qou-t2sc  — squeeze reduction (10 bricks) ✓ + conditional VC ✓
  qou-dw20  — saddle VALUE = 4·clausen(π/2)=4G ✓
  qou-1gkf  — convergence (brick 1 per-term ✓); remaining: catalanG bridge
              (qou-kvvu) + Riemann sandwich (the multi-session bulk)
NEXT-ARC beans:
  qou-e1dc  — land PR #4532 (Lean)
  qou-kvvu  — catalanG = clausen(π/2) bridge
  qou-e7yh  — downstream: van der Veen witness → b1-hyperbolic-rows Step-3
  qou-k00d  — (optional) exact c_σ closed form (torsion)
Owner plan (2026-08-02): 1 land merges → 2 convergence → 3 downstream → 4 c_σ.
