---
# qcz19
title: 'Front B (cycle exclusion): period-4 word-elimination + q-Steiner bound'
status: todo
type: task
priority: medium
created_at: 2026-07-31T20:00:00Z
updated_at: 2026-07-31T20:00:00Z
---

Period-1/2/3 cycle exclusion proved (word-elimination via linear_combination).
- B1 (tractable): extend to PERIOD 4 — each primitive parity word (EEEO, EEOO,
  EOOO, EOEO up to rotation) pins the cycle value to a non-unit coeff in Z[q^pm1].
  Mechanical linear_combination per word. Does NOT generalize (words explode).
- B2 (hard): the q-Steiner / Simons-de Weger height bound D_w ∤ n_w for ALL
  admissible w — the general result; needs a valuation/height invariant D_w
  carries that n_w cannot match. Formalize-first: find the invariant before scan.
Census (<=period 18) is negative evidence only. Anti-laundering: (a)/(b) scope.
