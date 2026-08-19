---
# qou-ph2s
title: 'L4-1c(ii): smooth Riemann defect for phi(x)=log(2 sin x/x) — Lipschitz across the removable singularity at 0'
status: completed
type: task
priority: normal
created_at: 2026-08-11T10:45:00Z
updated_at: 2026-08-11T11:40:00Z
---

Last genuinely-new estimate in L4-1 (epic qou-u1b5). After L4-1c(i)
(`log_cell_telescope`, exact) and L4-1b (Stirling), the whole remaining
content of the second-order log-sine expansion is the `C¹` Riemann-sum
defect of the SMOOTH function

    phi(x) := log(2 sin x / x) = log(2 sin x) - log x,   phi(0+) = log 2,

namely `sum_j int_{cell_j} (phi(x_j) - phi(u)) du`, whose `(N/pi)`-scaled
limit is `(1/2)(phi(r*pi) - phi(0)) = (1/2) log(sin(r pi)/(r pi))` — vdV's
`+/- (1/2)(log r pi - log sin r pi)` term.

Only hard point: a Lipschitz / derivative bound valid ACROSS the removable
singularity at 0, needed because the first cell is `[0, h]`. Note
`phi'(x) = cot x - 1/x`: each term blows up at 0, the difference is
regular (`phi'(0) = 0`, `phi` even about 0). Candidate routes:
  (a) bound `|cot x - 1/x| <= C*x` on `(0, 5pi/6]` directly;
  (b) go through a `sinc`-style analytic representation if Mathlib has one;
  (c) handle the first cell separately with an `O(h^2)` variation bound and
      the remaining cells with the plain `(0, pi)` derivative bound.

Route (c) is probably cheapest but still needs (a) on `(0, h]`.

PROGRESS (LogSineSmoothPart.lean, all sorry-free): the predicted obstacle
DISSOLVED. The cell defects need a SIGN, not a derivative bound, and phi is
strictly antitone on (0,pi) — so no Lipschitz estimate across the removable
singularity is required, and none of the three candidate routes (a)/(b)/(c)
was needed. Landed: sin_sub_mul_cos_pos (x cos x < sin x, via psi = sin - x cos
with psi(0)=0, psi' = x sin x > 0), hasDerivAt_phi, strictAntiOn_phi,
phi_le_log_two (the first-cell ceiling standing in for the unused value at 0).
REMAINING: assemble the telescoping two-sided bound
h(phi(nh) - log 2) <= sum_j int_cell (phi(x_j) - phi(u)) du <= 0
(needs intervalIntegral.integral_mono_ae_restrict for the first cell's single
bad point at u=0).

DONE (assembled): smooth_defect_squeeze sorry-free —
h(phiExt n - log 2) <= sum_{i<n} int_cell (phi(x_{i+1}) - phi u) du <= 0.
Per-cell bounds via intervalIntegral.integral_mono_ae_restrict (the first
cell's single bad point at u=0 is null); telescoped with
Finset.sum_range_sub against the ceiling phiExt (log 2 at j=0, phi(jh)
after). Integrability from intervalIntegrable_log' (unconditional) +
intervalIntegrable_log_two_sin. NO derivative estimate anywhere.
L4-1's ingredient list is now complete: L4-1a (defect repr) + L4-1c(i)
(exact singular telescope) + L4-1b (Stirling) + this.

REDUNDANT (2026-08-19) -- L4-1's target was ALREADY PROVED ON MAIN, stronger,
since 2026-08-10 19:24 UTC, one day BEFORE the L4-1 feasibility pass that
opened this bean.

  QOU/Knot/KashaevAsymptotic.lean :: kashaev_log_sum_asymptotic
    | sum_{j=1}^{k} log(2 sin(j pi/N))
        - ( -(N/pi) Lob(k pi/N) + (1/2) log(2N sin(k pi/N))
            + (pi/(12N)) cot(k pi/N) ) |
      <= 1/(144 k^2) + (7/12)(pi/N)^2 + (pi/N)^2/(12 sin^2(k pi/N))

Verified: 17-module cone ok=17, axioms [propext, Classical.choice, Quot.sound],
no sorryAx.  It is STRICTLY STRONGER than the L4-1 target: it identifies the
O(1/N) term as (pi/12N)cot, and its error is effective (explicit constants).
The two (1/2)log terms differ by exactly (1/2)log(2pi) -- the Stirling constant
the L4-1 route was going to produce.

Nothing is deleted; the work here is correct and sorry-free.  Downstream
consumers should cite kashaev_log_sum_asymptotic instead.
Audit: docs/audits/2026-08-19-l41-was-already-proved-on-main.md
