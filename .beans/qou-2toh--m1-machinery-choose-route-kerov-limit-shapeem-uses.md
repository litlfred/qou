---
# qou-2toh
title: 'M1 machinery: choose route — Kerov limit-shape+EM (uses CompositeEulerMaclaurin) vs discrete Bessel-J asymptotics'
status: completed
type: task
priority: normal
created_at: 2026-08-29T01:34:20Z
updated_at: 2026-08-29T01:36:09Z
---

DECIDED: Route 1 (Kerov limit-shape + CompositeEulerMaclaurin). Rationale in
docs/audits/2026-08-29-covariance-kernel-M1-machinery-inventory-and-route.md: kink cancels => smooth
integrand => existing order-2 EM remainder applies; Route 2 (Bessel-J asymptotics) is a larger new build.
