---
# qou-iyf6
title: 'LIT (qnnq): 1-loop = adjoint Reidemeister torsion — PROVED 2024 for 2-bridge knots (4₁,5₂ ARE 2-bridge). The torsion IS the geometric-connection density = candidate for QOU ρ_F. Two findings: (A) concrete cross-check ρ_F(4₁/5₂) =? adjoint torsion vs the existing conj:kashaev-density-equals-sdp-multiplicity; (B) TENSION — geometric cusp shape ϑ_K is a FIXED knot invariant (4₁→e^{iπ/3}, √-3), not a free per-particle DOF, so ''different particles = different ϑ same knot'' is suspect.'
status: completed
type: task
priority: high
created_at: 2026-08-01T19:00:51Z
updated_at: 2026-08-01T19:00:51Z
---

## Literature (verify authors before any references.ts registration — I mis-attributed twice today)

- **arXiv:2411.03801**, *1-loop equals torsion for two-bridge knots* (Nov 2024).
  Proves the Dimofte–Garoufalidis **1-loop conjecture** for **hyperbolic
  two-bridge knots**. Both **4₁ and 5₂ are two-bridge**, so the theorem covers
  exactly the QOU anchor knots.
- **Ohtsuki–Takata, Geom. Topol. 19 (2015) 853**, *On the Kashaev invariant
  and the twisted Reidemeister torsion of two-bridge knots*: the **second**
  coefficient of the Kashaev-invariant asymptotic expansion is a constant
  multiple of **√(twisted Reidemeister torsion)** at the holonomy
  representation of the hyperbolic structure (first coefficient = complex
  volume).
- **arXiv:2404.19155**, *Octahedral coordinates from the Wirtinger
  presentation* (2024): builds the hyperbolic shape/flat-connection data
  directly from a knot **diagram** (Wirtinger = crossing/braid presentation) —
  a braid→holonomy map, companion to the McPhail-Snyder route (`qou-t7az`).
- Context: Dimofte–Garoufalidis 1-loop invariant (from an ideal
  triangulation, CS perturbation theory); the adjoint Reidemeister torsion
  extends to a **rational function on the geometric component of the SL₂(ℂ)
  character variety**.

## Why this matters for qnnq / the Δ_λ chain

**Finding A — the torsion is a rigorous candidate for the QOU density ρ_F,
and gives a decisive cross-check.**
The corpus already conjectures (`conj:kashaev-density-equals-sdp-multiplicity`,
[`.md`](../content/quantum-observable-universe/mass-theory/kashaev-density-equals-sdp-multiplicity.md))
that the binding density prefactor `ρ_F` in
`B_pred(K_w) = ρ_F · m_e · Vol_hyp(K_w)` equals the joint-tower **SDP
Wedderburn multiplicity** `ν_SDP`. The literature says the *topological*
density selecting the geometric connection — the constant/second term of the
Kashaev asymptotics — **is the adjoint Reidemeister torsion**, now
**proved = the 1-loop invariant for 2-bridge knots (4₁, 5₂)**.
→ **Concrete, decisive test:** compute the adjoint Reidemeister torsion of
`4₁` and `5₂` (closed forms are in Ohtsuki–Takata / SnapPy) and compare to the
QOU `ρ_F = ν_SDP`. Agreement = a strong *independent* confirmation of the
density identity; disagreement = the SDP-multiplicity identification is in
tension with the topological density and must be re-scoped. Either outcome is
publishable signal. **This is the highest-value next step off this bean.**

**Finding B — adversarial: the geometric cusp shape ϑ_K is knot-FIXED, which
tensions the qnnq premise.**
The reframed qnnq gap treats `ϑ_K` as a "particle-specific" free DOF. But the
**geometric** cusp shape is a *fixed topological invariant* of the knot: the
corpus's own `cusp-shape-bar-parity`
([`.md`](../content/quantum-observable-universe/braids-and-knots/cusp-shape-bar-parity.md))
records `4₁ → ω = e^{iπ/3}` (Φ₆ root, trace field ℚ(√−3)), computable by
Neumann–Zagier / SnapPy. So if the proton and muon are **both** 4₁-based they
have the **same** geometric cusp shape — contradicting "different particles =
different ϑ." The probed off-lattice values (`ϑ_{4₁}(proton)=0.203`,
`ϑ_{4₁}(muon)=0.059`) are therefore **not** the geometric cusp shape; they can
only be a *deformed / incomplete-structure* (Dehn-filling) cusp datum, or the
particles are *different knots*. **The qnnq bean should state this fork
explicitly** — right now it silently assumes a same-knot per-particle ϑ, which
the geometric invariant forbids. (Consistent with the `meridian-holonomy-boost`
observation that at real q₀>1 the meridian turn is a *boost of rapidity ln q₀*,
not a compact spin — the incomplete-structure regime, not the complete one.)

## Next steps
1. **(A)** adjoint Reidemeister torsion of 4₁, 5₂ vs `ρ_F = ν_SDP` — the
   cross-check. Coordinate with `conj:kashaev-density-equals-sdp-multiplicity`.
2. **(B)** edit `qou-qnnq` to state the fork (geometric cusp shape is
   knot-fixed ⇒ per-particle same-knot ϑ is either deformed-structure or
   different-knot); do not leave the free-per-particle framing unqualified.
3. Verify authors + register the 3 refs in `references.ts` (deferred —
   burned twice today guessing author lists).
No fit, nothing wired.
