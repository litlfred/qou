# Per-Wedderburn-block χ_λ(β_n − β_p) closed forms verified, LO coefficients reveal Hopf-Jones pattern

**Date:** 2026-05-19
**Branch:** `claude/track-a-b-per-isotope-and-rho-xi`
**Context:** user direction "also check paper" — and indeed the paper already has the per-block closed forms in `content/quantum-observable-universe/braids-and-knots/chi-per-irrep-cyclotomic-closed-forms.md`.

## Verified closed forms

The paper's per-Wedderburn-block character differences for typed-B_3 β_n − β_p:

$$
\begin{aligned}
\chi_{(3)}(\beta_n - \beta_p) &= -\frac{(q^2 + 1)^2 (q^2 - 1)}{4q} \\
\chi_{(2,1)}(\beta_n - \beta_p) &= -\frac{(q^4 + 1)(q^2 - 1)}{4q^3} \\
\chi_{(1,1,1)}(\beta_n - \beta_p) &= -\frac{(q^2 + 1)^2 (q^2 - 1)}{4q^5}
\end{aligned}
$$

Cyclotomic factorisation:

| irrep | numerator | cyclotomic |
|-------|-----------|------------|
| V_(3) | −(q²−1)(q²+1)² | Φ_4² · Φ_2 · Φ_1 |
| V_(2,1) | −(q²−1)(q⁴+1) | Φ_8 · Φ_2 · Φ_1 |
| V_(1,1,1) | −(q²−1)(q²+1)² | Φ_4² · Φ_2 · Φ_1 |

**Verification**: τ_M(β_n − β_p) via Σ y_λ · χ_λ at q_0 = −0.14207 matches direct compute to 1.4e-9 ✓ (both assertions pass in `qbeta_per_block_paper_closed_forms.py`).

## Cleaner ℏ_q-linear form

Factoring out ℏ_q = (q-1)/q (since q²-1 = q(q+1)·ℏ_q):

$$
\boxed{
\chi_\lambda(\beta_n - \beta_p) = -\frac{(\text{cyclotomic factor})(q+1) \cdot \hbar_q}{4 q^{2(\ell_\lambda - 1)}}
}
$$

where $\ell_\lambda$ = 0, 1, 2 for $V_{(3)}, V_{(2,1)}, V_{(1,1,1)}$ (the depth in the Wedderburn-block hierarchy):

| irrep | clean form |
|-------|------------|
| V_(3) | −(q²+1)²(q+1) · ℏ_q / 4 |
| V_(2,1) | −(q⁴+1)(q+1) · ℏ_q / (4q²) |
| V_(1,1,1) | −(q²+1)²(q+1) · ℏ_q / (4q⁴) |

**Each block is LINEAR in ℏ_q at leading order.** This is the structural reason the global precision ladder has ε^(2k) factors — each rung corresponds to a higher-order PRODUCT or CONVOLUTION of these per-block linear contributions.

## Leading-order ε^1 coefficients per block

Taylor-expanding around q=1 in ε = q−1:

| irrep | ε^1 coefficient | Interpretation |
|-------|---------------:|----------------|
| **V_(3)** | **−2** | **= J_Hopf(q=1) — pure Hopf-Jones value** |
| V_(2,1) | −1 | = J_Hopf(q=1) / 2 — half-Hopf |
| **V_(1,1,1)** | **−2** | **= J_Hopf(q=1)** (same as V_(3)) |

Both 1D reps (trivial V_(3) and sign V_(1,1,1)) see the **full Hopf-Jones value −2** at LO. The 2D standard rep V_(2,1) sees **half** of that.

This is a structurally clean statement of the framework's Fact 3 ("2-strand sub-braid → Hopf link Jones at q=1"): the Hopf-Jones value enters at LO in the per-block decomposition, with the 1D reps absorbing the full value and the 2D rep absorbing half (consistent with character-formula scaling by the rep dimension).

## Implication for c_k^(λ) extraction

The framework's hypothesis `c_k = Σ_λ dim_q²(V_λ) · c_k^(λ)` (per `per-wedderburn-block-c5-c6.md` scaffolding) can now be tested per rung:

- c_3 = −2 = J_Hopf(q=1): consistent with V_(3) + V_(1,1,1) each contributing −2 at LO, with V_(2,1) contributing −1·2 = −2 (its character × dimension), summing to −2 in the Wenzl-weighted average.
- Higher c_k: come from PRODUCTS of the per-block linear-in-ℏ_q forms, generating ℏ_q^k powers at order k.

This is the foundation for first-principles per-block c_k^(λ) extraction. The closed forms in the paper ARE the per-block contributions to the Markov-trace difference; the precision-ladder c_k come from convolutions of these at higher orders.

## Open question: c_k^(λ) extraction rule

The per-block ladder factor `F^(λ)(q)` such that

$$
\tau_M(\beta_n - \beta_p) \cdot E_0 \;=\; Q_A \cdot \cos(\alpha - b\hbar_q^2/2) \cdot \prod_\lambda F^{(\lambda)}(q)^{?weight}
$$

needs to be specified. Candidates:

1. **Sequential per-block ladders**: each block has its own (1 + c_k^(λ)·b^k·ℏ_q^(2k)) factor; the global ladder is a sum/product.
2. **Convolution via y_λ weights**: c_k = Σ_λ y_λ(q_0) · c_k^(λ), with c_k^(λ) extracted from the per-block Taylor expansion of χ_λ(T_β)(q).
3. **Cyclotomic decomposition**: the Φ_n cyclotomic factors in the closed forms suggest a decomposition by roots of unity.

This audit verifies the paper's foundational closed forms and identifies the LO Hopf-Jones pattern; the c_k^(λ) extraction RULE is the remaining categorical work.

## Cross-references

- [`content/quantum-observable-universe/braids-and-knots/chi-per-irrep-cyclotomic-closed-forms.md`](../../content/quantum-observable-universe/braids-and-knots/chi-per-irrep-cyclotomic-closed-forms.md) — paper's closed forms (verified)
- [`content/quantum-observable-universe/braids-and-knots/chi-v3-closed-form-proof.md`](../../content/quantum-observable-universe/braids-and-knots/chi-v3-closed-form-proof.md) — Lean proof for V_(3)
- [`content/quantum-observable-universe/braids-and-knots/q-beta-c3-hopf-three-fold-markov.md`](../../content/quantum-observable-universe/braids-and-knots/q-beta-c3-hopf-three-fold-markov.md) — Fact 3 for c_3
- [`content/quantum-observable-universe/braids-and-knots/per-wedderburn-block-c5-c6.md`](../../content/quantum-observable-universe/braids-and-knots/per-wedderburn-block-c5-c6.md) — per-block c_5, c_6 scaffolding
- [`computations/qbeta/qbeta_per_block_paper_closed_forms.py`](../../computations/qbeta/qbeta_per_block_paper_closed_forms.py) — verification script
- [`computations/qbeta/qbeta-per-block-paper-closed-forms.witness.json`](../../computations/qbeta/qbeta-per-block-paper-closed-forms.witness.json) — verification witness
