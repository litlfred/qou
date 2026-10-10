---
# qou-rdmr
title: 'Layer 3 candidate (parent: qnnq): braid word → cusp winding via the Rademacher symbol (Ghys modular knots). For geodesics on the modular orbifold, the cusp winding of the closed geodesic attached to a word in ⟨L,R⟩ (≅ B₃ up to center) IS the Rademacher function of the conjugacy class — an explicit combinatorial word→integer winding map, exactly the shape Layer 3 needs. Probe: compute Rademacher/linking data for the 4₁ and Borromean braid words and compare against the T4-inverted ϑ (does ϑ/(√3/2 ln q₀) track a Rademacher-type quasimorphism rather than an integer?). Lean: Rademacher symbol on words in two generators is finitary — formalizable.'
status: completed
type: task
priority: normal
created_at: 2026-07-31T19:30:00Z
updated_at: 2026-08-01T22:05:47Z
---

Literature anchors:
- Ghys, "Knots and dynamics" (ICM 2006) — B₃ = π₁(unit tangent bundle of modular orbifold); linking of modular knot with trefoil = Rademacher invariant.
- Duke–Imamoglu–Tóth, "Modular cocycles and linking numbers" (DMJ 2017).
- "Linking numbers of modular knots" (arXiv 2211.05957, Geom. Topol. 29, 2025) — cusp winding of a closed geodesic computed by the Rademacher symbol.

Why it fits: a quasimorphism (not a homomorphism) explains a braid-word-determined quantity that is nearly-but-not-exactly additive and lands OFF the integer lattice after conjugation-averaging — consistent with the observed non-integer ϑ. This is the only route that directly attacks the word → (m,ℓ) map rather than the geometry side.


---

## 2026-08-01 RESOLVED — scope-(a) refutation (PR #4513)

**Verdict: the Rademacher symbol is NOT the source of ϑ_K.**

Both corpus anchors are (σ₁σ₂⁻¹)ⁿ closures — 4₁ at n=2, Borromean 𝔹₃ at n=3 —
so their SL(2,ℤ) images are (RL)ⁿ. An RL-balanced word has Φ = n − n = 0.
Confirmed three independent ways (exact-Fraction Dedekind sums, RL-word count,
homogeneity). Φ vanishes for BOTH knots: predicts ϑ = 0 against 0.0589/0.2032,
and cannot even DISTINGUISH the anchors — the minimum any word→ϑ map must do.

Upgraded to an **A-free** refutation by the qou-qnnq constraint curve: at
ϑ_μ = 0 the curve forces ϑ_p = 0.23551, so Φ ≡ 0 is off it regardless of A_ω.

**Scope (a), not (b):** the Ghys word→winding programme is NOT refuted. The
braid word does carry independent information (the binary precondition passed —
the two anchors are two different words); Φ is simply not the functional that
extracts it. A different quasimorphism, or the full linking datum rather than
its Rademacher shadow, remains open.

**Two corrections to this bean as originally written:**
1. It said to "compare against the T4-inverted ϑ". Those are A_ω-conditioned;
   FITTING to them is circular (`circ-derived-used-as-input`). The probe
   predicts from the braid word alone, then compares.
2. The anchors are 4₁ (muon) and 𝔹₃ (proton), not both 4₁.

Probe: computations/probes/qbeta_rdmr_rademacher_winding_probe.py
Note:  docs/scope/2026-08-01-theta-independent-routes.md §1
