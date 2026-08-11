---
# qou-ph2s
title: 'L4-1c(ii): smooth Riemann defect for phi(x)=log(2 sin x/x) — Lipschitz across the removable singularity at 0'
status: todo
type: task
priority: normal
created_at: 2026-08-11T10:45:00Z
updated_at: 2026-08-11T10:45:00Z
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
