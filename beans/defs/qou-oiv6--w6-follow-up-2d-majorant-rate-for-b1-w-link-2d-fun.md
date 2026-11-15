---
# qou-oiv6
title: 'W6 (follow-up): 2D majorant rate for b=1 W-link (2D functional max f(x,y) <= 4*Lambda(pi/4))'
status: completed
type: task
created_at: 2026-08-02T09:05:43Z
updated_at: 2026-08-11T00:40:00Z
---


Design (from the W2 route doc + WhiteheadLinkScaffold): prove
tendsto (2pi/N) log (whiteheadLinkMajorant N) -> 4*Cl2(pi/2), via the 2D
functional g(u,v) = clausen u + 2 clausen v - 2 clausen(u+v) on the
triangle {u,v>=0, u+v<=2pi}: unique interior critical point (pi, pi/2)
(sin((u+v)/2)=sin(v/2) => u+2v=2pi; then sin(v/2)=cos(v/2)), value 4G;
boundary edges give -clausen(u) <= Cl2(pi/3) < 4G (certified bounds).
Grid: log S_{n,k} = 2(s_{n+k}-s_k)-s_n deviation (3 E5c-4 instances),
n=0/k=0 rows direct; upper envelope N^2 * max; lower at (N/2, N/4).
Combined with VdVWhiteheadLemma4 (scaffold) this makes the b=1 W-link
volume limit conditional ONLY on vdV Lemma 4.

DONE (PR #4971): WhiteheadMajorantRate.lean sorry-free.
tendsto_two_pi_log_whiteheadLinkMajorant -> 4*clausen(pi/2); wrapper
tendsto_log_whiteheadLinkMajorant_vol (Vol_Borromean/2 form);
whiteheadLink_volume_of_lemma4 [VdVWhiteheadLemma4] — the b=1 W-link
volume limit is now conditional ONLY on vdV Lemma 4. 2D max done with
1D monotone-split bricks (no compactness), reusing #4532's
clausen_diff_le_shift; W4b deviation generic M-slot covered the whole
grid with zero slack.
