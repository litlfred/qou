---
# qou-k7rb
title: 'GAP: vacuous carriers part B — residuals after PR #8690'
status: todo
type: task
priority: normal
created_at: 2026-11-20T21:28:46Z
updated_at: 2026-11-20T21:28:46Z
parent: qou-dx7g
---

PR #8690 tied part-B carriers to corpus definitions where they exist. Open:

1. **HyperbolicVolumeBridge** — no manifold side: M is a bare type. Needs a combinatorial
   knot-complement type with canonical triangulations (4₁, 5₂ first).
2. **Kashaev.VolumeConjecture** — invariant and volume pinned only on 4₁ and 𝓑₃; needs a
   Kashaev-invariant definition from the R-matrix state sum.
3. **Topological mass terms** (TopologicalMassDecomposition, ArchimedeanMassFormula) — totalMass,
   baseline, exceptional are free reals; need trace norms on End(A_{n+1}) with the vortex γ as data.
   Norm equality itself open (qou-27ys).
4. **InstantonConnection** — needs Ad(P)-valued 2-forms on H, Webster Hodge star on Λ²H, YM
   integral minimised over the gauge orbit.
5. **TrefoilElectronMassConj** — T not tied to σ₀³ (HeckeElement 2 has no generators); port to
   OcneanuTrace.MarkovTrace.
6. Smaller: VacuumState (G_q not constructed), NonSelfIntersection (ambientDist not a metric),
   ObservationEnergy (𝔖_q undefined as a function of q).
7. **DiscreteVortexSpectrumContext** — main's #8180 repair (qou-klr1) leaves qInt a free field and
   classical_limit vacuous for q ≠ 1. Replace qInt with QInteger.qIntBalCl, require q > 1.
8. docs/audits/lean-vacuity-review-ledger.json entries for the changed files are sha-stale.

## 2026-11-21T04:33:19Z — which trace (owner prompt, PR #8726)

Items 3 and 5 were worded around a single trace. The corpus's mass functional is the two-term
Lagrangian trace tau(L) = tau(D^2) + tau(psi* D psi) (qou-7xl8), with tau the Jimbo quantum
trace = convention-D Markov trace. A real repair of TopologicalMassDecomposition and
TrefoilElectronMassConj must state both terms; the matter term for the electron is not formalised.
