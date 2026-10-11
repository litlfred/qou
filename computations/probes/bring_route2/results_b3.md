# Route 2, Part B: options B4 and B3, results

Recipe: `preregistration-b3b4.md`, committed (132dd4894f) before any B3 number was computed. Producer: `b3_linear_probe.py`, mpmath at 60 dps, proton pin q₀. **4/4 checks pass.** Nothing is ranked or selected, and nothing is compared with Q_β, CODATA or any mass. The selection rule stays open (bean `qou-99qc`).

## B4: what route 2 says about the element when sums get no energy

Route 2 gives each nucleon only a weighted list of Bring loops, one per braid in its expansion:

- proton: ¼·9.2064, ¼·15.9431, ¼·6.3677, ¼·20.4442
- neutron: ¼·15.9431, ½·20.4442, ¼·(no loop)

Two of the three neutron braids are also proton braids (`results_signed.md` §2). Route 2 also identifies braids that are not conjugate (`results_core_sameloop.md`). So under B4, route 2 describes the terms but cannot select the element, and selection has to come from elsewhere: the γγ construction plus the confinement SDP (bean `qou-ales`).

## B3: the whole element as a 2×2 matrix

The element is a sum of braids. Under B3 it is evaluated in a 2×2 representation and the resulting matrix is classified. Here x = |tr M| / √|det M|, and ℓ is the translation length of the projective action. **ℓ is not a Bring length** and is not comparable with route 2's L.

| | N-H: Hecke H₃(q₀), 2-dim irreducible | N-B: Burau at t = −q₀ (the ruled R-q point) |
|---|---|---|
| proton element | det −1.02197, x = 0.27756, glide reflection, ℓ = 0.27668 | det 1.38249, x = 40.919, hyperbolic, ℓ = 7.42198 |
| neutron element | det −1.02197, x = 0.36794, glide reflection, ℓ = 0.36589 | det 1.12211, x = 57.154, hyperbolic, ℓ = 8.09087 |
| γγ core (σ₀σ₁⁻¹)³ | det 1, x = 1.99419, **elliptic** | det 1, x = 18.263, hyperbolic, ℓ = 5.80369 |

Per-term values are in `results_b3.json`.

**Checks**
1. N-H satisfies the Hecke relation σ² = hσ + 1 and the braid relation, to 10⁻⁴⁰.
2. The N-H matrix of the element, built as the ¼-weighted sum of braids, equals Σ_w c_w ρ₂(T_w) built from the coefficients of `build_nucleon_nf_mp`. So B3 is evaluated on the canonical element itself, not only on my expansion of it.
3. tr ρ₂ equals the character χ_(2,1) of the builder's element. The character values on the basis [1, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀] are 2, h, h, −1, −1, 0.
4. N-B at t = −1 reproduces the SL(2,ℤ) traces of `results_signed.json`.

## What the numbers turn out to be (POST-HOC, not pre-registered, but derived exactly)

The determinants carry no new information. Each nucleon is a **product** of factors, and each factor is a polynomial f in a single generator. det is multiplicative, and for a single generator, det f(ρ(σ)) is the product of f over the generator's two eigenvalues:

- **N-H** (eigenvalues q and −q⁻¹): det = χ_(3)(X) · χ_(1³)(X), the product of the two one-dimensional characters. The values are 1.38249 × (−0.73922) for the proton and 1.12211 × (−0.91076) for the neutron. Both nucleons give exactly **−([2]_q/2)⁴ = −((q₀+q₀⁻¹)/2)⁴ = −1.0219724938…**, because σ and σ⁻¹ each contribute −1 and each averaged ud letter contributes −([2]_q/2)². This is the same −1.02197249381 that AGENTS.md records as the (2,1)-block value in the reading-1 PSD table; the agreement is an independent cross-check of check 2.
- **N-B** (eigenvalues q₀ and 1): det = χ_(3)(X) exactly (1.38249 for the proton, 1.12211 for the neutron), since every factor contributes f(1) = 1.

So:

1. **Under N-H, B3 is a function of the three Wedderburn characters**: x = |χ_(2,1)| / √|χ_(3)·χ_(1³)|. It adds no structure beyond what the Markov-trace machinery already has. The one twist is that χ_(1³) enters, even though under convention D its Markov weight y_(1³) is 0.
2. **N-H and route 2 sit at opposite ends.** N-H is Burau at t = q₀² ≈ 1.23, close to t = +1, which is the finite permutation representation. That is why the γγ core is elliptic there (x within 0.006 of 2), whereas at route 2's t = −1 it is hyperbolic with trace 18. Every odd-length braid, including every nucleon term (11 letters), has det −1 under N-H, so every element comes out as a glide reflection. That is a feature of the normalisation, not of the nucleon.
3. **N-B is not a representation of the algebra the element lives in.** It corresponds to Hecke at q² = −q₀. The two normalisations disagree in type for every row (§6 of the recipe), so B3 depends on the normalisation and does not resolve it.

## Status

B3 is computed and fully diagnostic. Neither normalisation is adopted, and the default stays B4: no energy for sums. Whether either normalisation should define "the" B3 is an owner decision.
