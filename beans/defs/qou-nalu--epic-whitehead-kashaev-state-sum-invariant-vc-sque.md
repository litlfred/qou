---
# qou-nalu
title: Whitehead Kashaev — state sum → invariant → VC squeeze proof → c_σ
status: in-progress
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T19:45:01Z
updated_at: 2026-11-22T21:15:45Z
parent: qou-n4nr
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



Former title (before 2026-10-04, when this became a story under a programme epic): EPIC: Whitehead Kashaev — state sum → invariant → VC squeeze proof → c_σ

## Round 83 Progress (PR #8392)
- Branch: `feat/round83-lambdasum-taupos-pairenergy-c1eval-nobranch-43c1`
- Commit 1 (code + probe): `e226ba66ce53cea91430549ce1efc48cd1eeef24`
- Commit 2 (witness): `17c21a76b062fd76e16d4f84b23687e02fc0050c` (`scriptSha256 = 0635fcc96bfd3bd66e7452f9553ce1314e6829b0b1a6b7202ea86d48b4b232a6`)

## 2026-11-22 — wave-2 drain (thread "Work the volume conjecture beans")

Arc map refreshed: compute done (#4382/#4310/#4394); Lean squeeze done (`qou-t2sc` and `qou-e1dc` closed today with evidence, `whitehead_vc_innerSum_half` unconditional on `main`); `qou-kvvu` done; `qou-k00d` is answered by `qou-vdvS` (see that bean). Open: `J_N(W)` outer sum (`VdVWhiteheadLemma4`, `qou-r75d`), `qou-1gkf` placeholder port, `qou-e7yh` downstream. The latest note above points at batch PR #8392, which is still open and unmerged; its theorems are short algebraic identities with the bean's quantities as free variables, and they do not bear on this bean's question. Treat this bean's state as what the earlier text says.
