# Pre-registration: chirality and CPT through B₃ → PSL(2,ℤ)

Written before any computation. Issue #9096, branch
`claude/helon-battery-chirality-2026-11-22`.

## 0. Source and its availability

Chester, Arsiwalla, Kauffman, *Preons, Braid Topology, and Representations
of Fundamental Particles*, arXiv:2501.03260v1 (2025).

**The paper is not in `library/`.** No `library/arxiv-2501.03260v1/`
directory exists, and `grep -ai arsiwalla` over `library/*/sections`,
`library/*/ocr` and `uploads/` is empty (checked 2026-11-22). The
quotations below come from the arXiv HTML rendering
(`https://arxiv.org/html/2501.03260v1`), read with a fetch tool that
summarises long pages. **They are cited by section only. The HTML has no
page numbers and I did not read the PDF, so no page is given.** Where a
quotation was summarised rather than copied, I say so. Ingesting the paper
into `library/` is follow-up work. It is not done here.

## 1. What the paper states

### 1.1 The map (§4, "CPT Invariance and Braid Topology")

> "the homomorphism from 𝓑₃ to the modular group PSL(2,ℤ)" … "the generators
> of 𝓑₃ are realized in PSL(2,ℤ) via the identification σ₁ → t and σ₂ → rtr"

with t = [[1,1],[0,1]]. The HTML prints both matrices with the label `t`,
which is a typesetting slip. The second matrix is [[0,−1],[1,0]], and I
read it as r. The same paragraph gives the chain (Eq. 14)

> B₃ → SL(2,ℤ) ↪ SL(2,ℝ) ↪ SL(2,ℂ) ↪ Pin(1,3)

and says it gives "indirect evidence that the proposed topological analogues
of C, P, and T transformations may correspond to the algebraic C, P, and T
transformations associated with Pin(1,3)."

**Correction to the task brief.** The brief says the authors read chirality
*through* B₃ → B₃/Z(B₃) ≅ PSL(2,ℤ). As far as the fetched text shows, they
do not. Z(B₃), the quotient B₃/Z and the kernel are never mentioned. The map
is used only for the embedding-chain argument (Eq. 14). Chirality and CPT are
defined and checked directly on braid words. So the PSL(2,ℤ) chirality test
below is **ours**. It reads their objects through their map, but it is not
their test.

### 1.2 Chirality (definitions as given)

- §4: "Recall that the chirality of fermions is determined by braid group
  generators in 𝓑₃."
- §6: "The position σ₁^{±1} signifies whether the particle is left- or
  right-chiral."

No formal definition is given.

### 1.3 C, P, T on braids (§4, Eqs. 8–11)

- C: "acts on any word … via switching of the braid crossings", together
  with reversing the twists.
- P: "via a reflection across the vertical axis".
- T: "via a reflection across the horizontal axis", together with reversing
  the twists.
- Eq. 8, C: σ₁⁻¹σ₂ → σ₁σ₂⁻¹
- Eq. 9, P: σ₁⁻¹σ₂ → σ₂σ₁⁻¹
- Eq. 10, T: σ₁⁻¹σ₂ → σ₂⁻¹σ₁
- Eq. 11: σ₁⁻¹σ₂ →C σ₁σ₂⁻¹ →P σ₂⁻¹σ₁ →T σ₁⁻¹σ₂
- Their negative example: σ₁σ₂ →C σ₁⁻¹σ₂⁻¹ →P σ₂σ₁ →T σ₁⁻¹σ₂⁻¹

**Letter rules these equations force (my reading, stated before computing):**

- C(σᵢ^ε) = σᵢ^{−ε}, word order kept. This is the mirror automorphism.
- P(σᵢ^ε) = σ_{3−i}^{−ε}, word order kept. Their σ₁σ₂ example rules out the
  other candidate for P (reverse the word, keep the letters): that rule sends
  σ₁⁻¹σ₂⁻¹ to σ₂⁻¹σ₁⁻¹, not to σ₂σ₁.
- T(w) = w⁻¹, the group inverse (reverse the word, invert each letter).

Consequence: P∘C is σᵢ ↦ σ_{3−i}, which is conjugation by the half twist
Δ = σ₁σ₂σ₁, an inner automorphism. So

    CPT(w) = Δ · w⁻¹ · Δ⁻¹     (an anti-automorphism of B₃).

### 1.4 Their claim (§4)

> "the braid diagrams of the helon model … are the only braid diagrams that
> turn out to be invariant under the these topological analogues of CPT
> transformations"

> "There are only four braid words that are invariant with respect to our
> proposed CPT transformation": σ₁σ₂⁻¹, σ₂σ₁⁻¹, σ₁⁻¹σ₂, σ₂⁻¹σ₁ (out of "16
> two-operator diagrams").

Their assignments (Table 2, as summarised by the fetch): e_L⁻ = σ₁⁻¹σ₂;
e_R and ν_R = σ₂σ₁⁻¹; d_{r,L} = σ₁⁻¹σ₂; ū_{b,L} = σ₁σ₂⁻¹. Photons and other
gauge bosons carry no braid ("the photons are identity operators").

## 2. Index convention

Our σ₀, σ₁ (0-indexed, owner rulings) are their σ₁, σ₂. Every computation is
done in their indexing, and the result is translated back.

## 3. Test objects

| object | word (ours) | word (theirs) |
|---|---|---|
| electron (ruling) | σ₀σ₁σ₀ | σ₁σ₂σ₁ = Δ |
| electron backup | σ₀³ ∈ B₂ ↪ B₃ | σ₁³ |
| photon terms | 1, σ₀, σ₁, σ₀σ₁⁻¹ | 1, σ₁, σ₂, σ₁σ₂⁻¹ |
| up quark | unknot strand: no crossings | identity braid e |

**Photon.** γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹ is an element of H₃(q), not of
B₃. A group homomorphism does not act on it. I will **not** force one. Only
two extensions are legitimate:

- (a) linear extension to the group ring, ℤ[B₃] → ℤ[PSL(2,ℤ)]. This applies
  to the formal sum *before* the Hecke quotient, term by term.
- (b) the SL(2,ℤ) lift, i.e. a 2×2 matrix representation of ℤ[B₃]. PSL
  elements are not matrices (±A), so a linear combination needs a lift to be
  summed at all.

Under neither extension is the photon itself "an element with a chirality".
I report the four terms one by one, and say whether the Hecke relation
survives.

## 4. What is computed (exact: sympy integer matrices, no floats)

1. **The map.** Check the braid relation for σ₁ ↦ t, σ₂ ↦ rtr in SL(2,ℤ) and
   in PSL(2,ℤ). Check that Δ² ↦ −I in SL(2,ℤ), i.e. ↦ 1 in PSL(2,ℤ).
2. **Images.** The PSL image (a normalised ± representative), its |trace|
   and its type (elliptic / parabolic / hyperbolic / identity), for each
   object.
3. **Chirality (ours).** C corresponds to conjugation by J = diag(1,−1),
   which is in GL(2,ℤ) but not in SL(2,ℤ). An image A is PSL-achiral iff A
   is conjugate in PSL(2,ℤ) to its mirror JAJ. Conjugacy invariant used: the
   Rademacher function Ψ. It is self-tested numerically for invariance
   before use. Ψ ≠ Ψ(mirror) certifies chirality. Achirality is claimed only
   when an explicit conjugator is exhibited, or when A = JAJ literally.
4. **CPT.** Compute CPT(w) = Δw⁻¹Δ⁻¹ for each object, and compare at three
   levels: as a word, as a B₃ element (via the faithful reduced Burau
   representation of B₃ with symbolic t), and as a PSL image.
5. **Their claim.** Enumerate the 16 two-letter words and confirm their four
   at both word level and group level. Then extend to all freely reduced
   words of length ≤ 4. That tests whether "only the helon braids" survives
   outside length 2.
6. **Hecke compatibility.** Decide whether any q makes the SL(2,ℤ) image
   satisfy σ² = (q − q⁻¹)σ + 1, and whether CPT extends to a linear map of
   H₃(q) at fixed q.

## 5. Expectations, stated before computing

- **E1 (electron, Δ).** Δ² generates Z(B₃), so Δ maps to an element of order
  2 in PSL(2,ℤ) (conjugate to S = [[0,−1],[1,0]]: elliptic, trace 0). Expect
  C(Δ) = P(Δ) = T(Δ) = Δ⁻¹ in B₃, so CPT(Δ) = Δ⁻¹ ≠ Δ in B₃. Δ⁻¹ = Δ·Δ⁻²
  differs from Δ by a central element, so in PSL(2,ℤ) CPT(Δ) = Δ. Expect
  "**not CPT-invariant in B₃, CPT-invariant mod centre**", and PSL-achiral.
  Under their §6 rule (position of σ₁^{±1}) the electron has no chirality at
  all, because Δ has no inverse letters. Their electron σ₁⁻¹σ₂ is a different
  word from ours; conflict expected.
- **E2 (trefoil σ₁³).** Parabolic t³. Expect chiral: Ψ(t³) = 3 against
  Ψ(t⁻³) = −3. Expect not CPT-invariant, either in B₃ or in PSL:
  CPT(σ₁³) = σ₂⁻³.
- **E3 (photon terms).** 1: invariant, achiral. σ₁: CPT ↦ σ₂⁻¹, not
  invariant. σ₂: CPT ↦ σ₁⁻¹, not invariant. σ₁σ₂⁻¹ (our σ₀σ₁⁻¹, the ruled
  chiral vertex): **expect CPT-invariant**. It is one of their four helon
  words, their ū_{b,L} / e_L⁺. Expect a hyperbolic image, trace 3 (the cat
  map), and probably PSL-achiral, since the mirror word σ₁⁻¹σ₂ is conjugate
  to it by Δ. Check. The photon as a whole: no verdict beyond term by term.
- **E4 (up quark, e).** Identity image, CPT-invariant, achiral. Their quarks
  carry braids, ours does not. Conflict expected.
- **E5 (their claim).** At word level among the 16 length-2 words, exactly
  their four. At group level the trivial word σ₁σ₁⁻¹ = e is also invariant.
  At length ≤ 4, expect more invariant elements, for example powers of the
  four (CPT is an anti-automorphism, so CPT(w^k) = CPT(w)^k). So "only the
  helon braids" holds only inside length 2.
- **E6 (Hecke).** The SL(2,ℤ) image of σ₁ is unipotent, with minimal
  polynomial (x−1)². The Hecke polynomial (x−q)(x+q⁻¹) has roots q and −q⁻¹,
  which cannot both be 1. So no q makes the image a Hecke quotient. Expect
  the map not to factor through H₃(q). And CPT, which contains a σ ↦ σ⁻¹,
  should not be a linear map of H₃(q) at fixed q: it should exchange h and
  −h.

## 6. Pass/fail criteria

- **Agreement with their claim**: their four words are CPT-invariant, and
  are the only invariant length-2 words at word level. PASS/FAIL per level.
- **Electron**: E1 confirmed or refuted as stated. Any refutation is
  reported, not explained away.
- Each object gets one verdict per column: PSL image type,
  chiral/achiral/undetermined, CPT-invariant (word / B₃ / PSL).
- **Scope.** This is a scope-(a) probe of one map and one reading of C, P, T.
  Nothing here is a structural exclusion unless it rests on a computed
  invariant (Ψ, the centre, the minimal polynomial), and then that invariant
  is cited.
- **No fitting.** Nothing is selected against a target; there are no free
  parameters.
