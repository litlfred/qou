# Octonion colour strand: result

Pre-registration: [`PREREG.md`](PREREG.md), including Addendum A, written before any compute.
Arithmetic is exact throughout:
- Laurent polynomials in a formal q with `Fraction` coefficients (`lalg.py`);
- sympy rationals;
- for nonvanishing proofs only, residues mod the prime p = 67108859. A nonzero residue proves the rational identity fails.

No q₀ is read anywhere.

**Question asked (owner).** Is there a strand that naturally interacts with the octonions and carries su(3) colour, the way the photon's strand carries the EM charge? And do Bring's handles correspond to the directions i, j, k?

**What this probe does and does not do.** The gluon is open, and this probe does not select one. It lists the candidate strands, says which structural tests each passes, and says what forces or excludes each one. The coideal / quantum-symmetric-pair route is another agent's and is not touched here.

## Summary table

| strand | braid / Hecke at substrate q | one colour su(3) moves with the strand | colour singlet sits in | verdict |
|---|---|---|---|---|
| **S2** Furey ideal ℂ⁸ = 1⊕3⊕3̄⊕1′, Jimbo gl₈ | Hecke ✓, braid ✓ | **only as two independent gl₃'s** (one on 3, one on 3̄). One U_q(sl₃) on 3⊕3̄ fails at generic q (passes only at q = 1). | — | scope (a) negative for a single colour group |
| **S5** oriented strand V = ℂ³, V* = 3̄ as the reversed strand (quantised walled Brauer) | mixed Yang–Baxter ✓ | **✓ at generic q** | the monodromy singlet; the octet is the eigenvalue-1 channel | passes every test in PREREG |
| **S1** G₂ strand V₇ = Im 𝕆, U_q(g₂) | the only two-eigenvalue equivariant braiding is x = 1 + s·P₁, which is Temperley–Lieb, **Hecke at q′ with q′ + 1/q′ = ±dim_q V₇, not at q** | ✓ classically, but **trivially**: the cup-cap is O(7)-invariant, so every subalgebra of so(7) commutes with it and the octonions play no role in the braid. At q ≠ 1 no colour su(3) inside U_q(g₂) exists as a Hopf subalgebra (`2026-11-15-colour-stabilizer-bridge.md` §8) | **the one-row channel** of H₃(q′), which convention D keeps | passes, at the cost of a second Hecke parameter |
| **S4** Bring handles → ℍ or 𝕆 | — | — | — | **no equivariant unit and no equivariant i, j, k triad**: scope (b) |

## S2: Furey ideal with Jimbo braiding ([`furey_oriented_probe.py`](furey_oriented_probe.py), [`furey-oriented.witness.json`](furey-oriented.witness.json))

Two block orders were checked, [1, 3, 3̄, 1′] and [3, 1, 3̄, 1′]. Both give the same result.

- **Q2a.** The Hecke relation (Ř − q)(Ř + q⁻¹) = 0 holds on ℂ⁸⊗ℂ⁸. The braid relation holds on (ℂ⁸)^⊗3.
- **Q2b.** The U_q(sl₃) relations hold on ℂ⁸. The weights are:
  - on 3: (1,0), (−1,1), (0,−1);
  - on 3̄: (0,1), (1,−1), (−1,0).
- **Q2c-Levi (control). Passes.** Take gl₃ acting on the 3 block and a separate gl₃ acting on the 3̄ block, each with the gl₈ coproduct. Both commute with Ř.
- **Q2c-diag (the real test). Fails.** Take one U_q(sl₃) acting on 3 ⊕ 3̄, coupled through its own coproduct. It does not commute with the Jimbo Ř in any of the four coproduct conventions.
  - The commutator entries are ±(q − 1), ±(1 − q⁻¹), ±(q² − 1) and ±(q − q⁻¹).
  - They vanish at q = 1 and not at q = −1.
  - This is the octonionic form of the corpus result `primitive_commute_rCheckN_iff` (`docs/audits/2026-11-15-colour-stabilizer-bridge.md`): a single colour group and a Hecke braiding on 3 ⊕ 3̄ coexist only classically.
  - Scope (a): this strand and this braiding, alone.
- **Q2e. Convention-D twists.**
  - A twist supported on a union of r basis lines is a Markov twist with z = q^r/[r]_q, as in PR #9059.
  - A twist that splits a colour block is not colour-invariant.
  - With colour-invariance imposed, the only twist giving z_D = q³/(q² + 1) (that is, r = 2) is the one supported on the two colour singlets {1, 1′}, which are Furey's lepton lines.
  - So on the Furey ideal, convention D lives on the lepton lines. This is a structural observation; nothing is selected by it.
- **Q2f. Passes.** σ₀, σ₁ and the chiral vertex σ₀σ₁⁻¹ (photon letters; photon = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹) commute with Levi colour on (ℂ⁸)^⊗3.
  - So every braid word is colour-neutral.
  - Consequence: **a colour octet cannot be a braid word in H_n(q)** on this strand. The gluon would have to be something other than a word.

## S5: oriented strand ([same script and witness](furey_oriented_probe.py))

V = ℂ³ is the fundamental of U_q(gl₃). V* is the same strand with reversed orientation. This reads the corpus's charge-conjugation bit (su3(e) = su3(−e)) as the orientation bit.

The mixed crossings are:
- c_{V*,V} = P (t⊗id)(R⁻¹);
- c_{V,V*} = (K_{2ρ}⁻¹⊗1) P (id⊗t)(R⁻¹) (1⊗K_{2ρ}), with K_{2ρ} = diag(q², 1, q⁻²).

These left-dual forms were identified by a search over candidate forms, and only these intertwine.

Results:
- **Q5a. Passes.** All mixed crossings intertwine the genuine U_q(gl₃) coproduct at generic q. Colour moves with the strand.
- **Q5b. Passes.** Mixed Yang–Baxter holds on VV*V, V*VV and VVV*.
- **Q5c. Passes.** The monodromy c_{V*,V}·c_{V,V*} on V⊗V* has two eigenvalues:
  - q⁻⁶ with multiplicity 1, the singlet;
  - 1 with multiplicity 8, the octet.

  So the octet projector P₈ lies in span(1, e), where e is the cup-cap. P₈ is a channel, not a gluon selection.

This is the quantised walled Brauer algebra, the standard home of a quark/antiquark strand pair. It meets the owner's "strand that interacts with colour" as a strand. What it does **not** supply is a reason for the octonions: V = ℂ³ with its dual is U_q(gl₃) data, and 𝕆 enters only through the Furey reading 3 ⊕ 3̄ ⊂ ℂ⁸.

## S1: G₂ strand ([`g2_hecke_search_probe.py`](g2_hecke_search_probe.py), [`g2-hecke-search.witness.json`](g2-hecke-search.witness.json); [`octonion_norm_tl_probe.py`](octonion_norm_tl_probe.py), [`octonion-norm-tl.witness.json`](octonion-norm-tl.witness.json))

**Setup.**
- The commutant End_{U_q(g₂)}(V₇⊗V₇) has dimension 4 at q = 2 and q = 3, computed exactly over ℚ.
- Its idempotents have ranks 1, 7, 14, 27.

**Search.**
- Every two-eigenvalue element of the commutant is, up to a scalar, x(t) = P_S + t·P_{Sᶜ}.
- For each of the 7 splits {S, Sᶜ}, the braid defect is a cubic in t.
- For 6 of the 7 splits, the entrywise gcd of the defect has degree 1. Its only root is t = 1, the trivial braiding.
- Only the split S = {1} (the invariant-form channel) has a degree-3 gcd. Its nontrivial roots satisfy s² + δ²s + δ² = 0, where s = t − 1 and δ = ±(q¹⁰ + q⁸ + q² + 1 + q⁻² + q⁻⁸ + q⁻¹⁰) = ±dim_q V₇. This was checked exactly at q = 2 and q = 3.
- At q = 3 the roots are 33759284 and 23418954 mod p. At q = 2 they lie in an extension of F_p.

**So the only U_q(g₂)-equivariant two-eigenvalue braidings on V₇ are the Temperley–Lieb (Jones) braidings of the q-octonion norm.** They are Hecke at a parameter q′ with q′ + 1/q′ = ±δ, which is not the substrate q.

**Classical check at q = 1, exact.**
- 𝕆 is built from the Fano triples. It is alternative and not associative.
- The norm cup-cap satisfies e² = 7e, e₁e₂e₁ = e₁ and e₂e₁e₂ = e₂.
- The braid defect of 1 + u·e is u(u² + 7u + 1)(e₁ − e₂).
- So q′ = (7 ± 3√5)/2 = φ^{±4}.
- Colour su(3)_e = {D ∈ Der 𝕆 : D e₇ = 0} has dimension 8. Its coproduct commutes with e, so colour moves with this strand. L_{e₇}² = −1 on e₇⊥ gives the 3 ⊕ 3̄ complex structure.
- The colour-singlet baryon tensor φ_{ijk} = ⟨e_i e_j, e_k⟩ satisfies e₁φ = e₂φ = 0. So σ₁φ = σ₂φ = φ, and φ spans the **one-row** (trivial) character of H₃(q′).
- Contrast with PR #9059: in the Jimbo (ℂ³)^⊗n tower the colour singlet ε_{abc} is the (1³) block, which lies in convention D's radical. On the G₂ strand the colour singlet sits in a channel that convention D keeps.
- 11 of 11 checks pass.

**On φ⁴.** That q′ = φ⁴ classically and that the icosian group (S4 below) involves φ is an exact algebraic coincidence of two quadratic fields. It is **not** evidence linking them, and no claim rests on it.

## S4: Bring handles and i, j, k ([`furey_oriented_probe.py`](furey_oriented_probe.py))

The owner's sub-question: do Bring's handles correspond to i, j, k?

**Data.**
- Bring's surface has genus 4, Aut = S₅, signature (2,4,5). Riemann–Hurwitz confirms the genus.
- Lefschetz characters of H¹(ℂ) by cycle type: 1 → 8, (2) → −4, (3) → 2, (2,2) → 0, (4) → 0, (3,2) → 2, (5) → −2.
- Decomposition:
  - over S₅, H¹ = 2·(std₄ ⊗ sgn), the corpus's "2W";
  - over A₅, H¹ = 2·**4**.

**Tests.**
- **No equivariant unit.** The trivial multiplicity is 0, so no handle direction is fixed by the symmetry group. An equivariant map onto ℍ or 𝕆 that sends something to 1 is impossible.
- **No equivariant i, j, k triad.** m(**3**) + m(**3′**) = 0, so H¹ has no 3-dimensional A₅ summand to carry Im ℍ.
- This is scope (b). The invariants are the trivial multiplicity and the 3-summand multiplicity of the Lefschetz character, both exact.

**What does exist, at module level only.** Over A₅ ≅ 2I/±1, the 4-dimensional irrep is **4** = **2** ⊗ **2′**, the product of the two Galois-conjugate spinors of the binary icosahedral group. Its characters: 0 on involutions, (−1)(−1) = 1 on order 3, (φ − 1)(−φ) = −1 on order 5.

So W ≅ ℍ as an **icosian bimodule** (x ↦ g·x·σ(g)⁻¹), and H¹ ≅ ℂ ⊗ ℍ **as a module**. This is not an equivariant algebra structure:
- no unit is fixed;
- i, j, k are permuted together with 1;
- there is no octonionic structure.

The fact that the two dimensions are both 8 = dim 𝕆 is a dimension count only, and is not evidence of anything.

## The open question (owner call, nothing selected)

A single colour group acting on 3 ⊕ 3̄ and braiding at the substrate q is not available from the octonions alone. Exactly one of the following has to give, and the probe cannot choose:

1. **Orientation (S5).** 3̄ is the reversed strand: quark/antiquark in a quantised walled Brauer category at the substrate q. Colour is exact at generic q, and the octet appears as a monodromy channel. This costs a second strand type, a V* alongside V. The octonions then enter only as the Furey reading of 3 ⊕ 3̄ and are not needed.
2. **Second Hecke parameter (S1).** The colour strand is Im 𝕆 with the norm-TL braiding at q′, where q′ + 1/q′ = dim_q V₇ (q′ = φ⁴ at q = 1). This is the "strand that naturally interacts with the octonions". Colour is exact, and the baryon singlet is D-compatible. This costs a braid algebra H(q′) separate from the photon's H₃(q), and how the two interact is unknown.
3. **Two colour groups (S2 Levi).** Keep the Hecke braiding on Furey ℂ⁸ and accept independent gl₃'s on 3 and on 3̄. This is not one su(3).

For any of these the gluon is **not a braid word**. It is a channel or projector (S5's P₈) or an algebra action, never a word in σ. That holds on S2 by Q2f and on S5 by construction.

**My judgement, not a finding:** option 1 needs the fewest new ingredients and is already the standard knot-theoretic home of quarks. In option 2 the octonions do work only through the trivalent vertex (the 3-form φ, the q-cross-product); the braiding itself sees only the norm.

> **Correction (2026-11-22, same session).** This section first said option 2 is "the only one in which the octonions do real work" and that colour moves with the S1 strand. Both overstated it. The TL braiding 1 + u·e is built from the norm alone, so it commutes with all of O(7), not just with g₂ or su(3). Colour commuting with it is therefore automatic and is no evidence for octonions. The G₂ content enters only through invariant theory: φ is the unique G₂-invariant in V₇^⊗3, but it is one vector in the trivial-channel space of dimension at least 343 − 14 = 329. The same overstatement was repeated in `docs/audits/2026-11-22-colour-viewpoints-synthesis.md` §3 and D2, corrected in the same commit, and in a chat message. Which of the two is meant is the owner's question.

**Default if nothing is decided:** nothing changes. This probe adds no content block and wires nothing.

## Not tested (per PREREG)

- q-octonions as an algebra;
- U_q(g₂) on 1 ⊕ 7;
- so₇ / so₈ braidings (BMW);
- the coideal route (another agent);
- spin;
- any evaluation at q₀.

## Reproduce

```
cd computations/probes/qcd_octonion_colour_strand
python3 furey_oriented_probe.py     # S2, S5, S4  (~0.5 s)
python3 g2_hecke_search_probe.py    # S1 search  (< 1 min)
python3 octonion_norm_tl_probe.py   # S1 classical TL check
```

Expected FAIL lines are results, not bugs: the two Q2c-diag lines and the two S4 lines. All other checks pass.
