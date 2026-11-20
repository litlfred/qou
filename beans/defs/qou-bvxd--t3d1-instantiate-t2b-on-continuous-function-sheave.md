---
# qou-bvxd
title: 'T3/D1: instantiate T2b on continuous-function sheaves + Čech first Chern class infrastructure'
status: todo
type: task
priority: high
created_at: 2026-10-12T20:38:54Z
updated_at: 2026-11-20T08:32:31Z
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
