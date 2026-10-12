# γγ products to first order in h: results

Recipe: `preregistration.md` (`bca743c8b98`), with K3 amended before any number was computed. Producer: `gg_quark_letters_h1_probe.py`. Witness: `gg-quark-letters-h1.witness.json`. Exact integer-polynomial arithmetic over ℤ[h]; no floats. **4/4 checks pass:** K1 Hecke and braid relations, both in the table and in the representations; K2 h⁰ is a single permutation; K3 χ_(2,1)(V³) − 2 = −h⁴(3 + h²); K4 φ(V^k) = V^{−k}. Issue #7754, bean `qou-ales`. Nothing adopted, nothing compared with data.

## 1. The γγ core, expanded

With V = σ₀σ₁⁻¹ and T_w the standard basis of H₃:

    V   = T_{s₀s₁} − h·T_{s₀}
    V³  = 1 + h²(T_{s₀s₁} − T_{s₁s₀}) + h³(T_{s₁} − T_{s₀}) + O(h⁴)

with exact coefficients c_e = −(h−1)(h+1)(h²+1) = 1 − h⁴, c_{s₀s₁} = h²(1 + h²), c_{s₁s₀} = −h², c_{s₁} = h³, c_{s₀} = −h³(1 + h²), and c_{w₀} = 0.

**Three facts, all exact:**

1. **The core has no h¹ term at all.** V³ − 1 = O(h²), as the h-tower table states. So the confined core supplies **no** first-order content. If flavour sits at order h¹, as #7718 measured for the template, it does not come from V³.
2. **Every deviation of the core up to order h³ is odd under the flip φ: σ₀ ↔ σ₁.** At h² it is T_{s₀s₁} − T_{s₁s₀}, and at h³ it is T_{s₁} − T_{s₀}. The φ-even part starts only at h⁴. This is forced: φ(V) = V⁻¹ (K4), so the odd part of V³ is ½(V³ − V⁻³). It measures the **orientation** of the vertex.
3. **The first single letters are at order h³, and they are antisymmetric: +σ₁, −σ₀.** Reversing the vertex orientation (V → V⁻¹) swaps them. V⁶ has the same pattern at h³, doubled: −2σ₀ + 2σ₁.

## 2. Single-letter content per word (first order at which T_{s₀} or T_{s₁} appears)

| word | h⁰ permutation | first order | c_{s₀} | c_{s₁} | φ-symmetric? |
|---|---|---|---|---|---|
| V, V⁴ | s₀s₁ | h¹ | −1 | 0 | no |
| V², V⁵ | s₁s₀ | h¹ | 0 | −1 | no |
| **V³** | e | **h³** | **−1** | **+1** | **no** |
| V⁶ | e | h³ | −2 | +2 | no |
| U³ = (σ₀σ₁)³ | e | h¹ | +1 | +1 | **yes** |
| U⁴, U⁵ | s₀s₁, s₁s₀ | h¹ | +1 | +1 | yes |
| U⁶ | e | h¹ | +2 | +2 | yes |
| V^{−k} | — | as V^k with σ₀ ↔ σ₁ | | | no |

(U¹ and U² carry no single letter at any order.)

## 3. What this says

- **Outcome (A) for the γγ reading V = σ_iσ_{i+1}⁻¹.** Its products carry generator-asymmetric single letters. A lone vertex has one negative letter on the generator of its positive crossing. The confined core has the antisymmetric pair +σ₁ − σ₀, first at h³.
- **Outcome (B) for the bare product U = σ_iσ_{i+1}.** Its single letters are φ-symmetric at every k, so U cannot separate the two generators and cannot supply a placement.
- **Outcome (C) is not met.** The core is not flavour-blind at all orders, but it is blind at h¹ and h².
- The asymmetry is **the vertex's orientation**, nothing more: V and V⁻¹ = φ(V) give mirror-image answers. So any (generator, sign) read off the core is fixed exactly up to the choice of γγ̄ versus γ̄γ. The corpus fixes that choice as σ₀σ₁⁻¹ (`gamma_gamma_pair_production_decomposition.py`).

## 4. What it does not do, and the comparison with the template

- **No dictionary to flavour is derived.** The template assigns signs to *flavours* (u, d). This probe yields signs on *generators*. Turning one into the other needs a rule saying which quark sits on which strand pair, and that rule is the placement question itself. So this does not yet produce a sign map. It shows the γγ core already carries an orientation-odd, generator-asymmetric structure at h², h³, which is where such a rule would have to come from.
- **A coincidence, reported and not used.** #7718 found the template verdict decided at t¹, "or at t³ when the t¹ term cancels". The core's first single letters are at h³. Whether that is the same h³ is not tested here.
- Not done: strand counts above 3, the Jones pair closure (pre-registered on #7733), or inserting letters into the nucleon element.
