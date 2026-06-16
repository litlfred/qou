# λ_scale substrate-derivation search (Borromean baryon formula)

**Date:** 2026-05-18
**Branch:** `claude/canonical-chi-rust` (PR #683)
**Status:** Open R&D — candidate substrate form at 5.6 ppm; full closure deferred.

## Context

The Borromean baryon mass formula
([`conj:borromean-baryon-mass-formula`](../../content/quantum-observable-universe/braids-and-knots/borromean-baryon-mass-formula.md))
gives

$$
  m_p = m_e \cdot \biggl[\frac{\mathrm{Vol}(\mathcal{B}_3)}{\hbar_q^2} \cdot \lambda_{\mathrm{scale}} + S(p)\biggr]
$$

with empirical closure (at MPFR-50dps, S(p) ≈ 0):

| Quantity | Value |
|----------|-------|
| Vol(B_3) | 7.32772290646480718089... |
| ℏ_q² (q_0) | 0.00981718851... |
| Vol(B_3)/ℏ_q² | 746.4176633... |
| **λ_p target (from CODATA)** | **2.4599534044** |
| λ_n target (from CODATA) | 2.4633442516 |
| Δλ_pn | 3.391 × 10⁻³ |

The substrate-derivation R&D: find a function of q₀ alone (and
topological invariants of B_3) equal to λ_p.

## Comparison with the FSC derivation pattern

The fine-structure constant derivation
([`alpha-em-categorical-trace`](../../content/quantum-observable-universe/braids-and-knots/alpha-em-categorical-trace.md))
followed the pattern:

  1/α_EM = q · [9]_q · [10]_q   (bare ansatz, 9, 10 from substrate)
  → matches CODATA to 6.7 × 10⁻⁹

The substrate-form: q-integer products × small-integer prefactor.

## Search for λ_scale substrate-form

### Direct q-integer products

| Form | Value | Δ to target |
|------|-------|-------------|
| [4]_q | 4.110 | −67% |
| [2]_q² | 4.044 | −64% |
| (1+h)·[2]_q | 2.431 | −2.5% |
| 1/2 · [4]_q · z | 1.025 | −58% |
| 5/2 | 2.500 | +1.63% |
| **5/2 − h²·G** | **2.459967** | **+5.6 ppm** |

None of the pure q-integer products land within < 1%. The **5/2 −
h²·G** form (where G = Catalan's constant) is the **best match**
at 5.6 ppm.

### The 5/2 − h²·G hypothesis

```
target            = 2.4599534044
5/2 − h²·G        = 2.4599666078
difference        = +1.32 × 10⁻⁵ (5.6 ppm)
```

Equivalently:

```
λ_p = 5/2 - h² · X
where X = 0.91627769 (target)
     G = 0.91596559 (Catalan)
     X - G = 3.02 × 10⁻⁴
```

The residual X − G ≈ 3 × 10⁻⁴ is roughly the same order as h²·(small)
— suggesting a sub-leading correction.

### Two-term ansatz fit

```
λ_p = 5/2 - h²·G·(1 + α·h²)
α   ≈ 0.00790  (small dimensionless residual)
```

The coefficient α ≈ 0.008 doesn't immediately match a simple
substrate constant. Could be:
- Higher-order Catalan-G expansion
- Skein polynomial Q(B_3) correction
- The Vol(B_3) literature value vs 8·G identification needs
  refining (they differ at the 7th digit — see below)

### The Vol(B_3) = 8·G near-identity

Numerically:
- 8·G = 7.327724753...
- Vol(B_3) literature = 7.327722906...
- Difference = 1.85 × 10⁻⁶

These are close but **not exactly equal**. The standard identity
is Vol(B_3) = 2 · V_oct where V_oct is the ideal regular octahedron
volume; and V_oct = 8·Λ(π/4), with Λ the Lobachevsky function.
Several sources give Λ(π/4) = G but the literature volume value
suggests the identification is approximate.

If Vol(B_3) = 8·G exactly were taken as the substrate definition,
then `5/2 - h²·Vol(B_3)/8 = 5/2 - h²·G` would be the structural
form. The 5.6 ppm gap could trace to:
1. Vol(B_3) literature value precision
2. Higher-order quantum corrections
3. S(p) ≠ 0 in the conjecture's Skein contribution

## What this is and isn't

**This is:** a strong structural candidate for the substrate form
of λ_scale — connecting it to **Catalan's constant G** and the
substrate parameter h = q − q⁻¹. The form `5/2 − h²·G` is
**mathematically natural** (rational + topological-invariant term)
and matches CODATA m_p to within 5.6 ppm.

**This isn't:** a closed proof. The 5.6 ppm residual must come
from either:
- the Vol(B_3) literature value vs 8·G discrepancy (a definitional
  question — what's the "right" Vol(B_3)?)
- a higher-order substrate term
- the S(p) Skein contribution

## Open R&D path

1. **Determine the exact relationship Vol(B_3) vs 8·G.** If
   they're exactly equal (the literature value's last digits are
   computed numerically, not from a closed formula), then
   `5/2 − h²·G` becomes the exact substrate form modulo S(p)
   and the higher-order terms.

2. **Compute S(p) from the Kauffman bracket of the canonical
   11-crossing Borromean braid.** If S(p) is non-trivial, the
   formula refines.

3. **Compute the Jones polynomial V_{B_3}(q_0).** From the
   standard Borromean Jones poly
   V(t) = -t^{-3} + 3t^{-2} - 2t^{-1} + 4 - 2t + 3t² - t³,
   evaluated at q₀:
   - V_{B_3}(q) ≈ 4.011
   - V_{B_3}(q²) ≈ 4.038
   - √V_{B_3}(q²) ≈ 2.009 (close to [2]_q but not λ_scale)

   So V(B_3) at substrate point gives **4.04 ≈ 4 + small**, not 2.46.
   The Jones polynomial of B_3 is NOT directly λ_scale.

4. **Try graded-Hecke-energy weight** (the 2nd of three open
   candidates per the conjecture's Status #2).

5. **Verify the neutron** λ_n = 2.4633442516 fits the same
   form with a substrate-derivable Δλ_pn.

## Status

The 5/2 − h²·G candidate is the **closest substrate-only match
yet found** for λ_scale and represents real structural progress
toward closing the m_p chain — but the remaining 5.6 ppm residual
is not yet attributable. Further R&D needed.

Witness: planned at
`computations/lambda-scale-substrate-search.witness.json`
(deferred to follow-up commit).

## Where could `5/2 − h²·G` come from?

Structural sketch (informal):

### The "5/2" term

The natural integer-half candidates at Hecke-algebra level n:
- **n = 4: 5 partitions** of 4 = {(4), (3,1), (2,2), (2,1,1), (1,1,1,1)}
- The proton in QOU is the canonical 3-strand braid (A=1, n_strands = 3·A = 3),
  but its **categorical "weight" at the n=4 level** (one Markov-stabilisation
  step up) lives in H_4(q), where there are 5 Wedderburn blocks.

If λ_scale is the **Markov-stabilised Wedderburn block count / 2** at the
proton's natural Hecke level:
- 5/2 = (# partitions of 4) / 2

At q = 1, dim_q = dim (classical), and the "5/2" is the leading-order
classical projection.

### The "h²·G" correction

- **h² = (q − q⁻¹)²** is the leading deformation away from q = 1.
- **G = Vol(B_3) / 8** is the per-cell hyperbolic volume of the Borromean
  rings complement (8 ideal octahedra share the cell; G is the
  Lobachevsky volume of one octahedral cell).

The natural appearance of h²·G:
- At Hecke level n, [n]_q = n + n(n²−1)/6 · h²·(...) + O(h⁴) (q-integer
  expansion). The leading correction is proportional to h².
- The hyperbolic structure on B_3 contributes G (the per-cell volume)
  via the **Yekutieli categorical Stokes**
  ([prop:yekutieli-stokes-mass](#prop:yekutieli-stokes-mass))
  applied to the Borromean ribbon surface.

Combined: the **first quantum correction** to the classical 5/2 is
h²·(per-cell hyperbolic volume) = h²·G — the substrate deformation
× topological invariant.

### Schematic categorical formula

If this hypothesis is right:

$$
  \lambda_{\mathrm{scale}}
  = \underbrace{\frac{p(4)}{2}}_{\text{partition count}/2}
    - h^2 \cdot \underbrace{\frac{\mathrm{Vol}(\mathcal{B}_3)}{8}}_{\text{per-cell hyperbolic volume}}
    + O(h^4)
$$

where p(4) = 5 = # partitions of 4.

This is a **quantum perturbation of the classical Wedderburn block
count**, with the leading correction tied to the Borromean
hyperbolic structure. The form is structurally natural —
a leading rational × half-integer plus h²-Vol-correction —
matching the patterns seen in other QOU substrate derivations.

### Open numerical questions

1. **Is the residual 5.6 ppm explained by the next correction?**
   The h^4 coefficient should be derivable from the partition algebra
   at level n=4. Compute the next-order Wedderburn weight and check.

2. **Does p(5)/2 = 7/2 work for the Σ baryon or higher generations?**
   Test: m_Σ / m_e = Vol(B_3)/ℏ_q² · (7/2 − h²·G·...) at CODATA precision.

3. **Is the formula generation-dependent?**
   First-generation: p(4)/2 = 5/2.
   Second-generation: p(5)/2 = 7/2, p(6)/2 = 11/2, etc.

### Status (this section)

This is **structural speculation**, not a proof. The match at 5.6 ppm
is suggestive but not conclusive — distinguishing "natural quantum
correction" from "PSLQ coincidence" requires either:
- Deriving the exact h^4 (and higher) coefficient from the partition
  algebra
- Independently verifying the formula at the neutron / muon / higher
  baryons

Both are concrete next R&D items.

## §13 Honest distinction: derivation vs justification

**The user asked: "derivation or justification?"** Critical question.
Honest classification of each finding:

### What we ACTUALLY derived

| Result | Status | Why |
|--------|--------|-----|
| `Vol(B_3) = 8·G` | **DERIVATION** | Standard topology: B_3 complement = 2 ideal regular octahedra (Adams 1985); V(oct) = 8·Λ(π/4); Λ(π/4) = G/2. Composition gives `Vol(B_3) = 16·Λ(π/4) = 8G` exactly. The 0.25 ppm literature offset is numerical precision. |

### What we numerically OBSERVED (justification, not derivation)

| Result | Status | What's missing |
|--------|--------|----------------|
| `λ_p ≈ 5/2 − h²·G` (5.4 ppm) | **JUSTIFICATION** | No proof that λ_scale equals the H_4 partition half-symmetric count. WHY the proton's natural Hecke level is n=4 (proton is a 3-strand braid). WHY h²·G is the correct leading correction (not some other h²·X form). |
| `5/2 = (2 conj pairs + 1 self-conj)/2 at H_4` | **NUMERICAL OBSERVATION** | The count is exact. But no categorical theorem yet links λ_scale to this count. |
| `Σ/Λ ratio ≈ √2 (0.08%)` | **JUSTIFICATION** | √2 is suggestive of isospin Clebsch-Gordan, but no proof yet links the strange-baryon λ extension to the isospin-multiplet structure. |

### What we TAUTOLOGICALLY confirmed

| Result | Status | Why |
|--------|--------|-----|
| `Δm_pn = ΔS_pn · m_e ≈ 1.293 MeV` | **TAUTOLOGY** | This is just rearrangement of the conjecture's formula m = m_e·(Vol/ℏ²·λ + S). Computing ΔS = Δm/m_e then verifying ΔS·m_e = Δm is circular. Doesn't prove λ_p = λ_n (we ASSUMED that to extract ΔS). |

### What this means for the m_p closure

To go from **justification at 5.4 ppm** → **derivation**, we need:

1. **A theorem linking λ_scale to H_4 partition data.** Currently we only have a numerical match. The categorical statement should be:

   > **Conjecture (to prove):** For the canonical (u,d)-Borromean baryon at H_4, the substrate λ_scale equals the conjugate-pair half-symmetric partition count, minus the leading h² correction proportional to Vol(B_3)/8 = G.

   This is not yet proved — it's a **bold structural hypothesis** with 5.4 ppm numerical support.

2. **A categorical derivation of the h²·G correction term** from the q-deformation of the H_4 Markov trace. The h²·G should come from EXPANDING the q-trace around q=1, with the topological invariant Vol(B_3)/8 entering via the Borromean braid's hyperbolic structure.

3. **A proof of the 5.4 ppm residual structure** — either as a calculable h^4 correction or as the S(p) Skein term that we currently assume is zero.

4. **Independent verification at the neutron** under the SAME λ_common = 5/2 − h²·G (already shown to be self-consistent with the 1.293 MeV split via Skein).

5. **An SU(3) extension** for strange baryons explaining why the Σ/Λ ratio approaches √2.

### Summary

**Currently:** 5/2 − h²·G is a substrate-form **PSLQ candidate** matching m_p to 5.4 ppm, with a plausible structural interpretation but no rigorous derivation.

**Required to claim "derived":** items 1-5 above, particularly items 1 and 2 (theorem + h²-correction proof).

**Status:** the m_p chain is now structurally **justified** to 5.4 ppm, but **not derived** in the strict QOU sense. The remaining gap to full derivation is well-defined: 5 concrete R&D items, each in principle tractable.
