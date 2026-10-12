# γγ products to first order in h: where single letters appear (pre-registration)

Written and committed **before any number in this directory was computed**. Issue #7754. Bean `qou-ales`.

**Owner ruling, 2026-10-12** (#7718, option 4): the quark sign map and the letter placement must be **outputs** of the γγ construction plus reading 3 at every strand count, not a template choice. This is step 1. It measures; it adopts nothing. Nothing here is compared with Q_β, CODATA, AME or any mass.

## 0. Why order h¹, stated from the corpus before computing

- σ⁻¹ = σ − h (h = q − q⁻¹), so every quark letter of the template equals σ at h⁰. Flavour first appears at h¹ (`computations/probes/quark_template/results.md` §1). In the template, the h¹ term of a letter σ^ε is −h(1−ε)/2 times the identity: a d-type letter "drops its crossing" at first order and a u-type letter does not.
- In H₃ every γγ word is a power V^k of V = σ₀σ₁⁻¹ (`QOU/Mass/GammaGammaSelectorH3.lean`). Expanding once, V = σ₀σ₁ − hσ₀, so a single vertex also drops one crossing at h¹, and which one it drops is fixed by the vertex.
- The flip φ: σ₀ ↔ σ₁ is an automorphism of H₃ (conjugation by T_{w₀}), and φ(V) = σ₁σ₀⁻¹ = V⁻¹.

So the measurable question is: **in the products V^k, which single-crossing terms appear at the first order where any appear, and are they symmetric under φ?** A φ-symmetric answer cannot tell σ₀ from σ₁, and so cannot supply a placement.

## 1. What is computed (fixed)

H₃ over ℤ[h] in the standard basis {T_e, T_{s₀}, T_{s₁}, T_{s₀s₁}, T_{s₁s₀}, T_{w₀}}, with T_{s_i}T_w = T_{s_i w} when the length goes up, and T_{s_i w} + h·T_w when it goes down. σ_i = T_{s_i}, σ_i⁻¹ = T_{s_i} − h.

**Elements (primary):** V^k for k = 1, …, 6.
**Elements (secondary, separate column):** U^k with U = σ₀σ₁ (the bare product), k = 1, …, 6; and V^{−k} = (φV)^k, k = 1, …, 6.

For each element, report:
1. every coefficient c_w(h) ∈ ℤ[h], exactly;
2. the **first order** n ≥ 1 at which a single-letter coefficient c_{s₀} or c_{s₁} is nonzero, and both values at that order;
3. **flip symmetry**: whether c_{s₀}(h) = c_{s₁}(h) as polynomials;
4. the characters χ_(3), χ_(2,1) of the element as exact rational functions of q, and their values at q = 1. Reading 3 on H₃ (level 3, the only level) is reported.

## 2. Checks (pass/fail fixed in advance)

- **K1.** The multiplication table satisfies σ_i² = hσ_i + 1 and the braid relation σ₀σ₁σ₀ = σ₁σ₀σ₁, exactly.
- **K2.** At h = 0 each element's coefficients are those of the permutation it maps to (a single T_w with coefficient 1).
- **K3.** χ_(2,1)(V³) − 2 = −h⁴(3 + h²) exactly. This is the same-strand identity of the h-tower table, also #7733's check C4.
- **K4.** φ acts as an automorphism on the computed elements: φ(V^k) computed by swapping generators equals V^{−k} computed directly.

## 3. Outcomes (stated before computing)

- **(A) Asymmetric single-letter content at the first order:** V^k supplies a derived (generator, sign) for a single crossing. Reported per k, with no adoption. Comparing it to the template's S± and its 8 placements (#7718) is reported as a comparison, not used to choose.
- **(B) Symmetric, or none at all at every order up to the top:** a scope-(a) negative for this route. Flavour does not come from the h-expansion of γγ words in H₃ alone.
- **(C)** The core V³ carries no single-letter content at all, at any order. Reported separately, because it would mean the core is flavour-blind and the letters must come from structure outside V^k (for example the Jones pair closure, pre-registered on #7733).

## 4. Not done

No strand count above 3, no quark letters inserted, no gluons. Exact integer polynomial arithmetic; no floats.

## Amendment (before any number was computed)

K3 originally compared against #7733's witness. That PR is not on `main`, so the first run stopped at an import, before computing anything. K3 now checks the identity that #7733's own C4 checks. The characters come from a self-contained exact 2×2 seminormal representation, whose braid and Hecke relations are checked as part of K1.
