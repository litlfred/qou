# Pre-registration: route 2, braid word → closed curve on Bring's surface

Written 2026-10-10, **before any Δ(2,4,5) trace, Bring length or energy of a
candidate was computed.** Owner, 2026-10-10: *"work route 2 in foreground"*. This is
route 2 of the energy / O'Hara selection question (beans `qou-99qc`, `qou-pzsi`).
Route 1 is `../ohara_link_energy/`.

No Q_β, CODATA value or mass number enters any computation, ordering or table here.
Anything added after this file is first committed is marked **POST-HOC**.

## 0. What was known before writing this file

Under the corpus's convention σ₀ ↦ T = [[1,1],[0,1]] and σ₁ ↦ L = [[1,0],[−1,1]],
the following were computed exactly (integer arithmetic) **before** this file:

| word | SL(2,ℤ) image | trace | PSL(2,ℤ) type |
|---|---|---|---|
| nuc9 | [[1,−2],[1,−1]] | 0 | elliptic, order 2 |
| nuc11_interleaved = gluon_s0_s0 | [[1,0],[1,1]] | 2 | parabolic |
| gluon_s0_s1 | [[2,−1],[1,0]] | 2 | parabolic |
| gluon_s1_s0 | [[3,1],[2,1]] | 4 | hyperbolic |
| gluon_s1_s1 | [[5,−2],[3,−1]] | 4 | hyperbolic |
| nuc11_gen_grouped | [[−27,7],[−4,1]] | −26 | hyperbolic |

Two further facts were also known. The γγ core Δ² = (σ₀σ₁)³ maps to −I, so it is invisible in PSL(2,ℤ). The two conjugate pairs of route 1 (§0 there) get equal traces, as they must.

## 1. Construction (every choice fixed here)

1. **Representation.** B₃ → SL(2,ℤ) → PSL(2,ℤ), with σ₀ ↦ T and σ₁ ↦ L as above. This is the
   reduced Burau representation at t = −1, i.e. the classical specialisation. Its kernel is ⟨Δ⁴⟩.
2. **Bring as a quotient of the Hecke group H₄** (Kattan–Singerman, `library/arxiv-2402.08782v1`,
   Thm 3.2). H₄ = ⟨S: z↦−1/z, U: z↦z+√2⟩ ≅ Δ(2,4,∞). H₄(5) is normal of index 120, and the
   compactification of H/H₄(5) is Bring's surface.
3. **Commensurability, not a homomorphism.** Conjugating by D: z ↦ z/√2 carries H₄ onto
   Γ₀(2)⁺ = ⟨T, W₂⟩ with W₂: z ↦ −1/(2z). Γ₀(2) has index 2 in it. A homomorphism B₃ → H₄
   cannot be used: B₃ = ⟨x, y | x² = y³⟩ and H₄ ≅ ℤ/2 * ℤ/4 has no element of order 3, so any
   such map has abelian image. It would then factor through the exponent sum, which
   `LetterSumBlindness` already excludes. This is to be proved, not assumed (§3).
4. **Which subgroup.** Γ₀(2) is the stabiliser of the point ∞ of P¹(F₂). The reduction
   PSL(2,ℤ) → PSL(2,F₂) ≅ S₃ is the strand permutation, up to the canonical bijection of
   strands with P¹(F₂) induced by the generator convention.
   - **If the permutation fixes exactly one point p** (every candidate does: permutation (1 2)), conjugate by any h ∈ PSL(2,ℤ) with
     h·p = ∞. The Γ₀(2)-conjugacy class of hgh⁻¹ does not depend on h.
   - **Otherwise** use g^k, with k the order of the permutation. Words with identity permutation
     give three classes, and are out of scope for this study.
5. **Into H₄.** Apply D⁻¹(·)D, then write the element as a word in S and U by exact Hecke
   (Rosen, λ = √2) reduction over ℤ[√2].
6. **Filling the punctures.** H₄ → Δ(2,4,5) sends U to an elliptic element of order 5, keeping
   S² = 1 and (SU)⁴ = 1. The kernel of Δ(2,4,5) → S₅ is π₁(Bring).
   - Realise Δ(2,4,5) in PSL(2,ℝ) with tr S = 0, tr U = 2cos(π/5) and tr SU = 2cos(π/4) (the hyperbolic triangle
     group is rigid, so this is unique up to conjugacy).
   - Let r be the order of the image in S₅. This is the smallest r with g^r ∈ π₁(Bring).
7. **Outputs per candidate, in this order, all exact or ≥ 50 dps:**
   - (i) the image type in Δ(2,4,5): elliptic, or hyperbolic with trace;
   - (ii) r;
   - (iii) the Bring geodesic length L = r · 2 arccosh(|tr|/2) when hyperbolic, otherwise "no closed geodesic".

## 2. What is NOT pre-registered, and is therefore not claimed

- **An O'Hara/Möbius energy of the Bring geodesic.** An intrinsic regularised Möbius energy on a
  hyperbolic surface needs a choice of distance kernel and self-energy subtraction (cf. bean
  `qou-uh5f`). None is fixed here, so **this study reports lengths only**. A length is not an
  energy, and no word is "selected" by it.
- **Elliptic and parabolic words** (nuc9, class B) get **no** value. Their landing on
  finite-order elements is a domain fact, not evidence for or against them.
- **Comparison with route 1.** This study makes none.

## 3. Formalize-first targets (Lean, before or alongside the probe)

- (L1) The matrix identities: D U D⁻¹ = T, D S D⁻¹ = W₂, W₂ T W₂⁻¹ = [[1,0],[−2,1]] (projectively).
  These are over ℝ with √2, by `ring`/`norm_num` plus `Real.sq_sqrt`.
- (L2) (σ₀σ₁)³ ↦ −I under the representation of §1.1, over ℤ.
- (L3) No homomorphism from ⟨x, y | x² = y³⟩ to ℤ/2 * ℤ/4 has non-abelian image. This one may be
  out of reach: Mathlib's free products are thin. If so, it is recorded as a gap bean and **not**
  replaced by an axiom.

## 4. Pre-registered method checks

- **Conjugate pairs.** The conjugate pairs of route 1 (gluon_s0_s1 ~ gluon_s0_s0; gluon_s1_s0 ~
  gluon_s1_s1) must give identical outputs. Any difference means a bug.
- **Rigidity.** The S₅ images of S, U and SU must have orders 2, 5 and 4, and must generate S₅.
- **Round trip.** The Rosen reduction of §1.5 must reproduce the input matrix exactly.
