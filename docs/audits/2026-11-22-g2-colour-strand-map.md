# The G₂ colour strand: what is proved, what it gives, what would change (2026-11-22)

Owner question (verbatim): *"Explore this option.... What can we prove and derive. What does it give us?
G₂ strand (Im 𝕆, 7-dim). Colour. What would we need to change in the corpus if anything? Or is it just
identifying the bits that are there?"*

This is a map. It records no new computation, selects no gluon and changes no ruling.

Rulings in force:
- The photon is `γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹`, on the H₃(q) strand.
- The up quark is an unknot strand.
- Convention D is canonical for the decay channel.

## 1. Already in the corpus (identification only)

### Classical layer: Lean, sorry-free, over ℚ

| fact | declaration |
|---|---|
| The octonion product on ℚ⁸ (Fano table) | `QOU.MathlibExt.OctonionDerivations.octMul` |
| **dim Der 𝕆 = 14**, so Der 𝕆 is g₂ | `octonion_derivation_dim` (`OctonionDerivationsUpperBound.lean`) |
| **Colour su(3) = stabiliser of one imaginary unit e, dimension 8**; the orbit is S⁶ = G₂/SU(3) | `finrank_su3_e1`, `OctonionSU3RankSix.lean` |
| su(3)_e is closed under bracket | `bracketDer_mem_su3` |
| L_e² = −1 on e⊥, and L_e commutes with su(3)_e; this gives the complex structure that splits 3 from 3̄ | `Le_sq_eq_neg_id`, `su3_comp_Le_eq_Le_comp` (`OctonionComplexStructure.lean`) |
| Im 𝕆 = 1 ⊕ (3 ⊕ 3̄) as complementary idempotent projectors | `OctonionColourTripletSplitting.lean` |
| A Lie-algebra colour action meeting the Jimbo Ř forces q = 1 | `ColourBridge.q_eq_one_of_e01_mem` |

### Quantum layer: probes, not Lean (`2026-11-15-colour-stabilizer-bridge.md` §8, §8.1)

- **The module V₇ of U_q(g₂) still splits as 1 ⊕ 3 ⊕ 3̄**, because the weights force it. The colour Cartan then acts through the long-root parameter **q³**, not through q.
- **The octonion product deforms to a unique U_q(g₂)-equivariant q-cross-product** V₇⊗V₇ → V₇, which is 1-dimensional. Left and right multiplication now differ by powers of q.
- **No colour su(3) Hopf subalgebra of U_q(g₂) exists.** su(3) ⊂ g₂ is not a Levi subalgebra, and S⁶ is not a symmetric space.
- **No U_q(g₂) braiding restricts to a Hecke operator on 3⊗3.** This is scope (b), over ℚ(q).

### New this session (`qcd_octonion_colour_strand`, PR #9097)

- The only U_q(g₂)-equivariant braiding on V₇ with two eigenvalues is the Temperley–Lieb (TL) braiding of the norm, 1 + u·e.
- It is Hecke at a parameter q′ with q′ + 1/q′ = ±dim_q V₇.
- At q = 1 this gives q′ = φ^{±4}.
- The baryon tensor φ_{ijk} = ⟨e_i e_j, e_k⟩ lies in the trivial TL channel.

**Caveat, corrected the same day.** The norm TL braiding is O(7)-invariant. So colour commuting with it is automatic and says nothing octonionic. The octonions enter only through the trivalent vertex: the 3-form φ, or at q ≠ 1 the q-cross-product. φ is the unique G₂-invariant in V₇^⊗3, but it sits inside a trivial-channel space of dimension at least 329.

## 2. What can be proved next (cheap, generic, sorry-free targets)

1. **TL braid identity, in any commutative ring.** Suppose e₁, e₂ satisfy eᵢ² = δeᵢ and eᵢeⱼeᵢ = eᵢ. Then σᵢ = 1 + u·eᵢ satisfies
   σ₁σ₂σ₁ − σ₂σ₁σ₂ = u(u² + δu + 1)(e₁ − e₂).
   So σ is a braid exactly when u² + δu + 1 = 0. This gives q′ + 1/q′ = δ as a derived consequence, not a choice.
2. **The norm cup-cap on Im 𝕆 satisfies TL with δ = 7.** This is a statement about any nondegenerate symmetric form on a 7-dimensional space.
3. **Every D in Der 𝕆 preserves the norm and annihilates φ.** This follows from the existing `Der𝕆` API. Hence G₂ commutes with the cup-cap, and φ is G₂-invariant.
4. **φ is killed by both cup-caps on V₇^⊗3.** Equivalently, φ lies in the trivial TL channel.

Items 3 and 4 are the only places where the octonions enter. None of the four needs q₀ or an empirical input.

## 3. What it gives

- **One self-dual strand carries quark, antiquark and a colour singlet**: Im 𝕆 = 3 ⊕ 3̄ ⊕ 1. The 1 is Furey's lepton direction. So, unlike the oriented strand, no second strand type is needed.
- **The baryon singlet is the trivalent vertex** (the 3-form φ, the Kuperberg G₂ spider vertex). It sits in the channel that convention D keeps. **This is the one route on which acceptance test (d), "colour singlets carry the D trace", can be kept**, though at q′ rather than at q. That changes the D1 framing in `2026-11-22-colour-viewpoints-synthesis.md` §5.
- **q′ is a function of q, so it is not a new calibration.** Two choices remain open: which normalisation of dim_q V₇ to use (short root q or long root q³), and the sign ±. These are conventions the corpus does not yet fix.

## 4. What it costs, and what would have to change

| item | kind | needs owner? |
|---|---|---|
| **Classical statistics.** At q = 1 the strand braid is Jones at δ = 7 (q′ = φ⁴), not the permutation, so colour strands stay anyonic in the classical limit. | physics cost | yes, if adopted |
| **Coupling to the photon.** The photon lives on Jimbo H₃(q) strands. A mixed crossing between a V₇ strand and a photon strand needs a braided category that holds both, and §8 shows U_q(g₂) and the Jimbo U_q(gl₃) share no Hopf subalgebra carrying colour. | open mathematics; the main obstacle | no (research) |
| **Colour at q ≠ 1.** It survives only as a weight decomposition at q³, not as an su(3) action. | open mathematics | no |
| **The up-quark ruling** ("unknot strand"). It would have to say on which strand type the unknot lives. | ruling | yes |
| **Content block `eightfold-way/color-su3-from-g2.md`.** It currently carries the PSL(2,7) / Klein-quartic route, which is excluded. A G₂-strand statement would be a new block or section. | content change | yes |

**Answer to "or is it just identifying the bits that are there?"** The algebra layer is identification: everything in §1 is already proved. The strand layer is new mathematics: §2 is cheap; the photon coupling in §4 is not.

## Not established

- Any q ≠ 1 colour action on the G₂ strand.
- Any mixed G₂ / Jimbo crossing.
- Which dim_q normalisation fixes q′.
- Lean for §2: not yet written.
