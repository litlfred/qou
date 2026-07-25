---
# qcz17
title: 'C8: derive the Skein-Collatz map FROM the QOU (substrate -> q-arithmetic -> map)'
status: in-progress
type: task
priority: medium
parent: qcz15
created_at: 2026-07-25T03:30:00Z
updated_at: 2026-07-25T03:30:00Z
---

The conceptually central "on a QOU" gap. Full chain: QuantumObservableUniverse
-> substrate parameter q -> Skein module S(q)=Z[q^pm1] -> Skein-Collatz map.
Bricks:
- BRICK 1 (start, mathlib-only, verifiable): formalize that the map's q-arithmetic
  (qi2=q+1, qi3=q^2+q+1, Skein divisibility, contraction gap, fundamental cycle)
  is DETERMINED by the single substrate parameter q — a structure/def
  SkeinCollatzArith with proved (not axiomatized) identity fields. Shows the
  categorical data descends from q.
- BRICK 2 (heavy): link q to an actual QUomega QuantumObservableUniverse's
  substrate parameter (needs the heavy QOU library import; QuantumObservableUniverse.olean
  not in the lake cache -> build-from-source friction). Mirror sibling q-ns
  "concrete Descartes QOU" grounding (qou-4xqa).
- BRICK 3: connect to the Reeb-bundle Skein module def (prop:skein-generation,
  S(q)=Z[q^pm1]).
Anti-laundering: BRICK 2/3 must DERIVE, not axiomatize. If the QOU import is
infeasible in-sandbox, do BRICK 1 + honestly document the import wall.
