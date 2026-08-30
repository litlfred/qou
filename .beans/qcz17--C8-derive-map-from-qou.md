---
# qcz17
title: 'C8: derive the Skein-Collatz map FROM the QOU (substrate -> q-arithmetic -> map)'
status: completed
type: task
priority: medium
created_at: 2026-07-25T03:30:00Z
updated_at: 2026-08-29T16:26:27Z
parent: qcz15
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

BRICK 1 DONE: structure SkeinCollatzArith (R) bundling the substrate q; qi2/qi3 defs; skein_divisibility, contraction_gap, coprime, fundamental_odd_step all PROVED by construction (simp+ring/linear_combination). Shows the whole q-arithmetic + fundamental cycle descends from the single substrate parameter q. mathlib-only, sorry-free (lean-direct exit 0). BRICK 2 (QuantumObservableUniverse import) + BRICK 3 (Reeb Skein module) remain — heavy, may hit sandbox import wall.

BRICK 2 DONE (2026-07-31): collatz_substrate_link.lean — SubstrateParameter.toSkeinCollatzArith derives SkeinCollatzArith (brick 1) from an ACTUAL QOU SubstrateParameter (field: M->R, q(p)>=1>0, not root of unity). skein_divisibility_at + fundamental_odd_step_at: the map's arithmetic + fundamental cycle hold FOR the substrate value q(p), the cycle honest via field_pos (q invertible). GENUINE derivation, no axiomatization — consumes the real SubstrateParameter structure. Unblocked by from-source build of the QOU library (CategoricalFoundations/SubstrateParameter are Mathlib-only, buildable against restored Mathlib oleans). sorry-free, lean-direct exit 0. Remaining: BRICK 3 (Reeb-bundle Skein module S(q)=Z[q^pm1] link, prop:skein-generation).

BRICK 3 DONE (2026-07-31): collatz_substrate_link.lean — skeinModuleArith : SkeinCollatzArith (LaurentPolynomial ℤ) with q = T (the Reeb-bundle Skein module S(q)≅Z[q^pm1] = R_q, prop:skein-generation). skeinModuleArith_qi2 ([2]_q=T+1), skeinModuleArith_fundamental_odd_step (q=T a unit via qcollatz_laurent_qunit; fundamental cycle realised in S(q)). Exhibits the TWO levels of q: fibre q=T in S(q)=Z[q^pm1] (brick 3) vs archimedean q(p) in R (brick 2). C8 COMPLETE (bricks 1+2+3). sorry-free, exit 0.

STALE-REFRESH 2026-08-29. All three C8 bricks landed:
- BRICK 1: QCollatz.SkeinCollatzArith with proved (not axiomatised) fields -- skein_divisibility ([3]=q[2]+1), contraction_gap ([2]^2-[3]=q), coprime, fundamental_odd_step.
- BRICK 2: collatz_substrate_link.ArchimedeanSubstrateField.toSkeinCollatzArith + skein_divisibility_at + fundamental_odd_step_at -- the arithmetic IS the QOU substrate parameter.
- BRICK 3: collatz_substrate_link.skeinModuleArith on S(q)=Z[q^{pm 1}] with skeinModuleArith_qi2 and skeinModuleArith_fundamental_odd_step.
C8 -- the conceptually central 'on a QOU' derivation gap -- is closed. Marking completed.
