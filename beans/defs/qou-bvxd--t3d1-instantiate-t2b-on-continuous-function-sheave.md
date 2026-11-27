---
# qou-bvxd
title: 'T3/D1: instantiate T2b on continuous-function sheaves + Čech first Chern class infrastructure'
status: todo
type: task
priority: high
created_at: 2026-10-12T20:38:54Z
updated_at: 2026-11-28T00:30:00Z
parent: qou-533l
---

Owner: try all T3 designs. Front D1+Chern (owner also asked: add needed infra like Chern classes).

1. Instantiate the T2b PresheafCentralExtension on presheaves of continuous functions: Z -> R -> U(1) and mu_n -> U(1) -> U(1).
2. Define the Čech first Chern class of a U(1)-cocycle as its lifting obstruction along Z -> R -> U(1).
3. Prove: additivity, naturality, and that the mu_n obstruction is c_1 mod n (so an n-th root exists iff c_1 is n-divisible at cochain level).
4. Bean the gaps that need the topology of surfaces (degree, Poincaré–Hopf).

## 2026-10-12 — d1-chern subagent: cochain-level Chern class + Kummer, sorry-free

New file `folio/quantum-observable-universe/lean/QOU/MathlibExt/CechChernClass.lean`. Checked with lean-direct `-DautoImplicit=false -s 65536`: exit 0, 0 warnings, 0 sorry. Axioms on 12 key declarations: propext, Classical.choice, Quot.sound only.

Done (items 1-3):
- Generic results: `obstruction_map` (naturality under morphisms of extensions) and `obstruction_mul` (exact multiplicativity for commutative 𝓔 and 𝒢).
- `expExtension` (ℤ →2π ℝ →exp U(1)) and `kummerExtension` (μₙ → U(1) →ⁿ U(1)) on `Opens X`. Both have sectionwise exactness proved; surjectivity of exp on sections is not claimed.
- `chernClass` with the formula 2π·c₁ = ξij+ξjk−ξik. Also proved: cocycle, lift-independence up to integer coboundary, refinement naturality, exact additivity (`chernClass_mul`), additivity up to coboundary for any lift (`chernClass_mul_lift`), and `exists_realCocycle_iff`.
- `kummer_obstruction`: obsₙ = κ∘c₁ (c₁ mod n), at cochain level, via `obstruction_map`.
- `exists_nthRoot_iff`: γ has an n-th root cocycle ⇔ c₁ = δβ + nθ. Proved in both directions, using `kappa_surjective`, the facts that μₙ is finite and discrete, and the lift of μₙ-cochains to ℤ-cochains.

Still open (item 4; detail in docs/audits/2026-10-12-t3-d1-chern.md):
- (a) Existence of local real lifts. `IsRealLift` is a hypothesis; it needs good covers or local logarithms on simply connected overlaps.
- (b) Ȟ² groups, refinement colimit, and comparison with H²(X;ℤ). Mathlib's NonabelianCohomology has degree 1 only.
- (c) Principal U(1)-bundles ↔ U(1)-cocycles. FiberBundleCore has transition functions but no classification.
- (d) c₁ = e = χ, degree pairing, Poincaré–Hopf. Mathlib has no surface topology.

thm:qu-to-qou item 2's "= χ" and item 3's "χ mod n" are NOT formalised. Only the cochain relation obsₙ = c₁ mod n is formalised, and it holds for any c₁. Status stays in-progress (the open identifications are its subject).


**2026-11-20T08:32:31Z — owner-approved status change (coordinator session_01VQDpPdnjTBLBcPi6D5gj61, PR #8542 batch C):** in-progress → todo. Open conjecture: stale claim released; never to be completed while the conjecture is open (AGENTS rule 13a).

## 2026-11-21 (bean-drain sibling bring-gerbe-ns, session_01Qmmkt6JCxoNkQcgaG1tFNF, issue #8808)

Superseded-premise check (owner, 2026-11-21: photon L±, virtual photons, old γγ letters, T(2,n_s), convention C, single-term trace, trefoil electron, c_2 = −1, χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean; its subject is surface topology / gerbes / NS and touches none of them.
Item 4 progress on main: (b) Ȟ² and the refinement colimit now exist (CechColimit, CechColimitConverse), and for S² the comparison with the coefficient group is proved (PR #7969). Still open: (a) local real lifts (IsRealLift hypothesis; on S² the box covers have convex-cone pieces, so a lift through exp exists on each piece, which is a feasible next Lean step), (c) bundles ↔ cocycles, (d) c_1 = χ / Poincaré–Hopf.

## 2026-11-22 applicability review (wave-2 sibling bring-riemann-gerbes, session_01Qmmkt7Jw9nSDCzSdsd8hLX)

APPLIES. Premises checked against owner-rulings.md on origin/main (all rows to 2026-11-22: photon with fixed constant 1, γγ linking neutrality, derived quark charges, potential-energy sign, m_p = m_n at q = 1, gluon open, electron σ₀σ₁σ₀ with T(2,n) as backup, S₅ two-test rule, T(A) tangent algebra) and git log on the Lean/content paths since the last update. Unchanged; IsRealLift hypothesis (local real lifts) is still the open item.

## 2026-11-27 (thread "Build the brane-tower gerbes", PR #9735)

Item 4(a) partly done: MathlibExt/CechLocalLog.lean proves a local real lift exists when each transition function misses a point (Circle.localLog, AvoidsPoints, avoidsPoints_of_overlap, exists_isRealLift_of_avoids, chernClassOfAvoids). Sorry-free, standard axioms.
Still open: avoidance after refinement for an arbitrary cocycle (needs a fine-cover argument), then (b)–(d) as above.

## 2026-11-27 (thread "Build sheaves and Čech Chern class in Lean")

- PR #9842, MathlibExt/CechChernClassH2.lean: c₁ as a class in H2 U C(-,ℤ) and in the colimit Ȟ² over open covers. Lift independence, gauge invariance (Chern cochains of hγh⁻¹ and γ are equal for h = exp(is)), [c₁] = 1 iff a real-cocycle logarithm exists, additivity, Kummer with closed quotient θ (C(T,ℤ) has no n-torsion), open covers directed by pairwise intersection, and c₁ = 0 in Ȟ² iff a real-cocycle log exists on an open refinement.
- PR #9850, QOU/Transcendental/MathlibExt/ContSheafTorsor.lean: item 4(c) for sheaf torsors. C(-,G) is a sheaf on Opens X; C(-,G)-torsors trivialised on an open cover ↔ G-valued 1-cocycles (cocycleTorsor + descentIso); a trivialised U(1)-torsor with local real lifts reduces to a C(-,ℝ)-torsor iff its Chern cochain is an integer coboundary.
Still open: (a') real lifts after refinement for an arbitrary cocycle (needs paracompactness or a Lebesgue-number argument); Ȟ²(X; C(-,ℤ)) ≅ H²(X; ℤ); FiberBundle comparison; (d) c₁ = e = χ, Poincaré–Hopf.
