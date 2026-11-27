# Result: chirality and CPT through B₃ → PSL(2,ℤ)

Pre-registration: [`PREREG.md`](PREREG.md), committed and pushed before any
computation. Producer: `chirality_psl2z_probe.py`. Witness:
`chirality-psl2z.witness.json`. All arithmetic is exact: sympy integer
matrices, `Fraction` Dedekind sums, and the reduced Burau representation of
B₃ over ℚ(t), which is faithful, used to decide equality in B₃.

Source: Chester–Arsiwalla–Kauffman, arXiv:2501.03260v1, **§4**. The paper is
**not in `library/`**. Quotations are from the arXiv HTML; no page numbers
(see PREREG §0).

## Verdicts per object

Words are written in our indexing. "CPT inv." is reported at three levels:
the word, the element of B₃, and its image in PSL(2,ℤ).

| object | PSL image (± rep.) | type | Ψ | PSL chirality | CPT(w) | CPT inv. word / B₃ / PSL |
|---|---|---|---|---|---|---|
| electron σ₀σ₁σ₀ = Δ (ruling) | [[0,−1],[1,0]] | elliptic, order 2 | 0 | achiral (image = mirror image) | σ₁⁻¹σ₀⁻¹σ₁⁻¹ = Δ⁻¹ | no / **no** / **yes** |
| electron backup σ₀³ | [[1,3],[0,1]] | parabolic | 3 | **chiral** (Ψ 3 vs −3) | σ₁⁻³ | no / no / no |
| photon term 1 | I | identity | 0 | achiral | 1 | yes / yes / yes |
| photon term σ₀ | [[1,1],[0,1]] | parabolic | 1 | chiral (Ψ 1 vs −1) | σ₁⁻¹ | no / no / no |
| photon term σ₁ | [[1,0],[−1,1]] | parabolic | −1 | chiral | σ₀⁻¹ | no / no / no |
| photon vertex σ₀σ₁⁻¹ | [[2,1],[1,1]] | hyperbolic, \|tr\| = 3 | 0 | **achiral** (conjugator [[−3,−2],[2,1]]) | σ₀σ₁⁻¹ | **yes / yes / yes** |
| up quark (unknot strand) | I | identity | 0 | achiral | 1 | yes / yes / yes |
| *reference: their e_L⁻ = σ₀⁻¹σ₁* | [[−2,1],[1,−1]] | hyperbolic, \|tr\| = 3 | 0 | achiral | itself | yes / yes / yes |

**What "PSL chirality" means here.** This is our test, not the paper's. The
mirror C (σᵢ ↦ σᵢ⁻¹) acts on the images as conjugation by J = diag(1,−1),
which is in GL(2,ℤ) but not in SL(2,ℤ); checked on both generators. An image
is chiral if it is not PSL-conjugate to its mirror image. The certificate
used is the Rademacher function Ψ, a class invariant. Before use it was
checked on 300 random conjugations, and checked to be even under −I.
"Achiral" is claimed only with an explicit conjugator, or when the image is
literally equal to its mirror image.

## Pre-registered expectations

- **E1, electron: confirmed exactly.** C(Δ) = P(Δ) = T(Δ) = Δ⁻¹ in B₃, all
  three checked by Burau. So CPT(Δ) = Δ⁻¹ ≠ Δ. Δ⁻¹ = Δ·Δ⁻², and Δ² generates
  the centre (its image in SL is −I), so the PSL image is CPT-invariant. Its
  image is S, the order-2 elliptic element, which is achiral. The electron is
  **CPT-invariant only modulo the centre Z(B₃)**: exactly in PSL(2,ℤ) = B₃/Z,
  and not in B₃. Closure: 2 components (the Hopf link, consistent with the
  ruling; the Hopf link is achiral, which also agrees).
- **E2, trefoil: confirmed.** Chiral, Ψ = 3 against −3, which matches the
  known chirality of T(2,3). Not CPT-invariant at any level.
- **E3, photon: confirmed term by term.** The ruled chiral vertex σ₀σ₁⁻¹ is
  CPT-invariant at all three levels. **It is literally one of their four
  helon words** (their σ₁σ₂⁻¹, which they assign to ū_{b,L} and, in §4, to
  e_L⁺). Its image is the hyperbolic "cat map" [[2,1],[1,1]], which is
  PSL-achiral. The single generators σ₀ and σ₁ are chiral, and CPT exchanges
  them, inverted: CPT(σ₀) = σ₁⁻¹. Termwise,
  CPT(γ) = 1 + φ₀σ₁⁻¹ + φ₁σ₀⁻¹ + φ₀₁σ₀σ₁⁻¹ as a formal sum. **No verdict is
  given for γ as a whole.** See the Hecke section for why it does not live in
  H₃(q).
- **E4, up quark: confirmed.** Trivially invariant and achiral.
- **E5, their claim: confirmed inside its stated scope, and false outside
  it.** See the next section.
- **E6, Hecke: confirmed.** See below.

## Their claim, tested

Paper (§4): of the 16 two-letter words, "only four braid words … are
invariant", namely the helon words, and these "are the only braid diagrams"
invariant under CPT.

- **Word level, length 2: PASS.** Exactly σ₁σ₂⁻¹, σ₁⁻¹σ₂, σ₂σ₁⁻¹, σ₂⁻¹σ₁ (in
  their indexing). This is the reading their Eqs. 8–11 require: C mirrors, P
  is σᵢ ↦ σ_{3−i}^{−ε}, T is the group inverse. The other candidate for P
  (reverse the word) contradicts their own σ₁σ₂ example. With these rules,
  CPT(w) = Δw⁻¹Δ⁻¹.
- **Group level, length 2:** the same four, plus the four cancelling words
  σᵢ^{±}σᵢ^{∓}, which equal the identity. That is harmless.
- **Beyond length 2: FAIL as a general statement.** Among freely reduced
  words of length 4, **12 are CPT-invariant in B₃**. Examples:
  σ₁²σ₂⁻², σ₁σ₂σ₁⁻¹σ₂⁻¹, and (σ₁σ₂⁻¹)². The powers are invariant
  automatically, because CPT is an anti-automorphism. At length 3, four words
  are invariant in PSL(2,ℤ) but not in B₃: σ₁σ₂σ₁ and σ₂σ₁σ₂ (both equal to Δ)
  and their inverses (both equal to Δ⁻¹). That set includes our electron.
  So "the helon braids are the only CPT-invariant braids" holds only among
  two-crossing words, which is the population the paper actually enumerated.
  It is not a property of B₃.

## The map itself: a defect in Eq. 14

With σ₂ ↦ rtr, r = [[0,−1],[1,0]], the image of σ₂ is −[[1,0],[−1,1]]. Then:

- **The braid relation fails in SL(2,ℤ)** (tst ≠ sts as matrices). It holds
  only up to sign, i.e. in PSL(2,ℤ).
- So the paper's identification is a homomorphism **B₃ → PSL(2,ℤ)**, as its
  text says, but **not B₃ → SL(2,ℤ)**, which is how Eq. 14 begins. The chain
  SL(2,ℤ) ↪ SL(2,ℝ) ↪ SL(2,ℂ) ↪ Pin(1,3) therefore needs the standard lift
  σ₂ ↦ [[1,0],[−1,1]], which does satisfy the braid relation in SL and sends
  Δ² to −I and Δ⁴ to I. Their rtr gives the same PSL map but no SL map.
- **Caveat.** The HTML prints r with the label `t`. If the intended r differs
  from [[0,−1],[1,0]], this finding moves with it.

The paper does **not** use PSL(2,ℤ) to define chirality or CPT (correcting
the task brief; see PREREG §1.1). Its CPT check is on words.

## Hecke compatibility

- The SL(2,ℤ) image of σ is unipotent, with minimal polynomial (x−1)². The
  residual t² − (q−q⁻¹)t − I has entries −q+q⁻¹ and −q+2+q⁻¹. **No q makes
  all of them zero.** So the map does not factor through H₃(q) for any q, and
  it is not an algebra map from H₃(q). It is a map of the group algebra
  ℤ[B₃] only.
- So the photon γ ∈ H₃(q) has **no image** under this map. One can map the
  pre-quotient formal sum termwise in ℤ[B₃], but that answer depends on which
  word represents each Hecke element, and the Hecke relation does not
  survive.
- CPT contains σ ↦ σ⁻¹ (via C, P and T separately). In H₃(q), σ⁻¹ = σ − h
  satisfies the Hecke relation with **h ↦ −h** (checked symbolically). So CPT
  is **not a linear map of H₃(q) at fixed q₀**. It is semilinear, conjugating
  q to −q or to q⁻¹. A "CPT-invariant photon" in H₃(q₀) is not even
  well-posed without choosing that extension. The two reversal-type pieces,
  T∘C (word reversal), are linear anti-automorphisms. This is standard and
  was not computed here.

## Agreements and conflicts with our rulings

- **Agreement.** The ruled photon vertex σ₀σ₁⁻¹ is a CPT-invariant helon word.
  This is the one place where their invariance criterion and our photon
  ruling coincide exactly.
- **Conflict: electron.** Their e_L⁻ is σ₀⁻¹σ₁ (2 crossings, mixed signs,
  closure 1 component). Ours is Δ = σ₀σ₁σ₀ (positive, closure Hopf link).
  Ours is not CPT-invariant in B₃, only mod centre, and their §6 chirality
  rule (the sign of the σ₁ letter) gives it no handedness at all. Under their
  criterion, our electron is **not** a helon braid.
- **Conflict: trefoil backup.** Chiral, and not CPT-invariant at any level.
  Under their criterion it is excluded outright.
- **Conflict: up quark.** In their table every quark carries a two-crossing
  braid word; only gauge bosons are braid-free. Our up quark is braid-free.
  The ruling is untouched; the frameworks simply disagree.
- **Their photon is the identity operator**, carrying twists only. Ours is a
  four-term Hecke element.

## Scope

- **Scope (a) throughout.** These are statements about one map
  (σ₁ ↦ t, σ₂ ↦ rtr) and one reading of C, P and T, the reading forced by
  their Eqs. 8–11.
- **What is proved by a computed invariant:**
  - the trefoil's PSL chirality (Ψ);
  - the electron's non-invariance in B₃ (faithful Burau);
  - the failure of the SL braid relation;
  - the non-factorisation through H₃(q) (minimal polynomial).
- Twists (their B₂ factor) are not modelled. Their C and T also reverse the
  twists, so a full CPT verdict on a twisted helon is outside this probe.
- No parameter, no fit, no selection. Nothing is ruled on.
