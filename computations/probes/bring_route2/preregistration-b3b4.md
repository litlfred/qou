# Route 2, Part B options B4 and B3: pre-registration (written before any B3 number was computed)

Owner request, 2026-10-11: "explore b4 b3" (options of `preregistration-pure.md` Part B). The selection rule stays open (bean `qou-99qc`). Nothing here ranks, selects, or compares to Q_β, CODATA or any mass. Every fork below has a default fixed before computing. A result obtained under a default the owner later overrules is reported as POST-HOC.

The elements, as `pyhecke.atom.build_nucleon_nf` builds them (verified term by term in `signed_candidates_probe.py`, check `expansion_reproduces_builder_*`), are

    proton  P = (σ₀σ₁⁻¹)³ · σ₀ · ½(σ₀+σ₀⁻¹) · ½(σ₁+σ₁⁻¹) · σ₀σ₀
    neutron N = (σ₀σ₁⁻¹)³ · ½(σ₀+σ₀⁻¹) · ½(σ₀+σ₀⁻¹) · σ₁⁻¹ · σ₀σ₀

Each is a weighted sum of braids: four of weight ¼ each for P; for N, three distinct braids of weight ¼, ½, ¼.

## B4: no energy for sums (descriptive, nothing new computed)

Under B4, route 2 assigns each nucleon only the **weighted multiset** of the Bring loops of its terms (`results_signed.md` §2), and no single number:

- P ↦ {¼ · 9.2064, ¼ · 15.9431, ¼ · 6.3677, ¼ · 20.4442}
- N ↦ {¼ · 15.9431, ½ · 20.4442, ¼ · (no loop)}

What B4 commits to is that route 2 is a *diagnostic of the terms*, not a functional on the element. Any selection of the nucleon element must then come from elsewhere: the γγ construction plus the confinement SDP (bean `qou-ales`). The B4 write-up records this multiset, plus the facts already measured: route 2 identifies non-conjugate braids (`results_core_sameloop.md`), and P and N share two braids.

## B3: evaluate the element in a linear representation

### 1. Which representation (fixed)

H₃(q) has three irreducibles: the two characters σ ↦ q and σ ↦ −q⁻¹, and one of dimension 2, ρ₂ (partition (2,1)). Only ρ₂ gives a matrix that acts on the hyperbolic plane, so B3 uses ρ₂.

Reduced Burau, `S₀(t) = [[−t,1],[0,1]]` and `S₁(t) = [[1,0],[t,−t]]`, has eigenvalues −t and 1. Hecke σ has eigenvalues q and −q⁻¹. They match **only** after a scalar: σ_H = −q⁻¹·S(t) with t = q². (The other choice, q·S(t) with t = q⁻², is the same representation up to equivalence.) The scalar does not change the length of a single braid, but it does change a **sum** of braids. In ½(σ + σ⁻¹), the two terms are scaled by c and c⁻¹, not by a common factor.

### 2. Two normalisations, both computed, neither chosen by its numbers

- **N-H (Hecke at q₀).** ρ₂(σ_i) = −q₀⁻¹·S_i(q₀²). This is the algebra the element is actually built in (`hm_mp`, with σ⁻¹ = σ − h and h = q₀ − q₀⁻¹).
- **N-B (the ruled R-q point).** ρ(σ_i) = S_i(−q₀), unscaled. This is the owner's 2026-10-11 ruling for single braid words (`preregistration-qdeformed.md` §2). The element is read as an element of the braid group algebra, with σ⁻¹ ↦ S⁻¹. Note: t = −q₀ corresponds to Hecke at q² = −q₀, i.e. at imaginary q, **not** to H₃(q₀). So N-B is not a representation of the algebra the element lives in, and the element's Hecke normal form does not determine ρ_{N-B}(element). This is stated now, before computing.

**Default:** neither is "the" B3. Both are reported in separate columns. Choosing one is an owner decision, and B4 remains the status of selection until then.

### 3. The length (fixed, same as R-q §3)

For M = ρ(element) with d = det M:

- d = 0 gives no length (degenerate);
- otherwise x = |tr M| / √|d|;
- d < 0 is a glide reflection, ℓ = 2·asinh(x/2);
- d > 0 and |x − 2| < 10⁻²⁵ is parabolic, ℓ = 0;
- d > 0 and x > 2 is hyperbolic, ℓ = 2·arccosh(x/2);
- otherwise elliptic, with the rotation angle reported.

A sum is generally **not** a scalar multiple of an SL(2) element. Scaling to |det| = 1 is a convention, and ℓ is the translation length of the projective action, nothing more. This is **not** a Bring length: there is no fold onto Bring's surface at q₀ (R-q §0), and ℓ must not be compared with route 2's L.

### 4. What is computed

For P and N, under N-H and N-B: tr, det, x, type and ℓ of ρ(element). For context, the same for each term (single braids) and for the γγ core. mpmath at 60 dps, q₀ = `Q_50_DIGIT_STR` (proton pin).

### 5. Checks (pass/fail fixed in advance)

1. ρ₂ under N-H satisfies the Hecke relation σ_i² = hσ_i + 1 and the braid relation, to 10⁻⁴⁰.
2. Under N-H, ρ₂(element) computed as the weighted term sum equals Σ_w c_w ρ₂(T_w), using the builder's normal-form coefficients c_w. The basis is [1, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀] (`gram.hm`). This ties B3 to the canonical element and does not rely on my expansion.
3. tr ρ₂ under N-H equals χ_(2,1)(element) from the builder's normal form, via χ_(2,1) on the basis.
4. At q₀ → 1, N-B single-braid traces agree with the SL(2,ℤ) traces of `results_signed.json` (t = −1).

### 6. What would make B3 uninformative (stated in advance)

- If det ρ(element) is 0, or x lies within 10⁻²⁰ of 2, the length is reported as undefined or degenerate. It is not regularised.
- If N-H and N-B disagree in type for the same element, that is reported as showing that B3 depends on the normalisation. It is not resolved by picking one.
