**Conjecture (gluon-octet closed form for $1/\alpha_{EM}$, PSLQ-empirical).**
*Let $q$ denote the substrate parameter, $[k]_q := (q^k - q^{-k})/(q - q^{-1})$ the quantum integer, and $\hbar_q := (q-1)/q$ the reduced Planck constant. We conjecture the closed form*

$$
  \frac{1}{\alpha_{EM}}
  \;=\;
  45 \cdot [3]_q \cdot \bigl(1 + \delta_{CS} + 8q \cdot \delta_{CS}^2\bigr),
  \qquad
  \delta_{CS} \;:=\; \hbar_q^{4} \cdot [5]_q.
$$

> **Status: PSLQ-empirical, not derived.** The formula matches CODATA at $q_0$ to $6.7 \times 10^{-9}$ and is the unique short integer relation in the canonical 52-element basis at 1000 dps, but a structural derivation linking each factor to an upstream proposition is **incomplete**. See [open problems](#rem:alpha-em-derivation-open-problems) for a factor-by-factor audit:
>
> - **$45 = \binom{10}{2}$**: dimension confirmed via $\Lambda^2 V_{\text{nat}}^{10} = V_{(9,1)} \oplus V_{(8,1,1)}$, but the categorical link to $\alpha_{EM}$ is asserted, not proved (the "10" matches the [10]_q crossing count, not a strand count).
> - **$[3]_q$**: the claim "$\mathrm{tr}_\tau$ on singlet idempotent in gluon-octet sector $= [3]_q$" is **not supported** by direct computation: in $H_3(q)$, $\dim_q V_{(2,1)} = [2]_q$ (not $[3]_q$), and the $\mathfrak{sl}_3$ adjoint has classical dimension $8$, not $[3]_q$.
> - **$\delta_{CS} = \hbar_q^4 \cdot [5]_q$**: the κ-formula in [`gram-determinant-plancherel-ratio`](#prop:gram-determinant-plancherel-ratio) is structural, but the "leading non-trivial term at $n=10$" specialisation has not been carried out — the embedding $T_{2,9}, T_{3,5} \hookrightarrow H_{10}$ requires Markov-stabilization choices not specified.
> - **$8q$**: identified two ways (Lean: $8 = \dim\mathfrak{su}(3)$ gluon octet; .md: "genus-4 torus-knot two-step crossing pattern enumeration") with **no calculation** for either. The required order-3 coefficient to match CODATA exactly is $\approx -52$, which is not a clean q-rational, suggesting the formula is a 2-term truncation/fit rather than an exact closed form.
>
> Forms A (Chern-Simons) and B (this conjecture) **disagree at every $q \ne q_0$** — confirming they are not the same q-function and that this form is presently a single-point fit. See [`docs/alpha-fsc-audit.md`](#) for the full audit.

## Conjectured derivation (incomplete)

The closed form is assembled from four structural ingredients, each of which is independently established:

**(i) The integer $45$.** By [prop:exterior-square-borromean](#prop:exterior-square-borromean), $\binom{10}{2} = 45$ is the dimension of the strand-pair representation $\Lambda^2 V_\mathrm{nat}^{10}$ of $S_{10}$, decomposing as $V_{(9,1)} \oplus V_{(8,1,1)}$ with $\dim 9 + 36 = 45$.

**(ii) The quantum integer $[3]_q$ (claimed).** By [thm:em-spectral-completeness](#thm:em-spectral-completeness) and [cor:gauge-coupling-uniqueness](#cor:gauge-coupling-uniqueness), the two-strand braiding endomorphism algebra has rank 2 with central idempotents $e_+, e_-$ summing to identity, and any $R$-linear scalar coupling $A^{\otimes 2} \to \mathbf{1}$ is a unique multiple of $\mathrm{tr}_\tau(e_-) \cdot e_-$. The original ansatz *claimed* that the quantum trace $\mathrm{tr}_\tau$ on the singlet idempotent evaluates to $[3]_q$ in the gluon-octet sector (purportedly the quantum dimension of $\mathfrak{sl}_3$'s adjoint summand corresponding to the symmetric strand pair). **Audit: this claim is unsupported.** Direct computation of q-dimensions in $H_3(q)$ gives $\dim_q V_{(2,1)} = [2]_q$ (not $[3]_q$), and the $\mathfrak{sl}_3$ adjoint has classical dimension $8$, with q-dimension $\ne [3]_q$ in any standard convention. The structural origin of $[3]_q$ in this prefactor remains unidentified.

**(iii) The Chern--Simons correction $\delta_{CS} = \hbar_q^4 \cdot [5]_q$.** By [prop:gram-determinant-plancherel-ratio](#prop:gram-determinant-plancherel-ratio), the Gram-determinant ratio $\kappa$ has the closed-form Plancherel-weighted character expansion

$$
  \kappa \;=\; \prod_\lambda \Bigl[\frac{\dim V_\lambda}{\dim_q V_\lambda} \cdot \frac{[n]_q!}{n!}\Bigr]^{c_\lambda^{(s)} \cdot c_\lambda^{(w)}}
$$

over $S_n$ irreps, where $c_\lambda^{(\bullet)} = \chi_\lambda(\beta_\bullet)$ are central-idempotent character coefficients of the genus-$4$ torus knots $T_{2,9}$ (strong) and $T_{3,5}$ (weak). The leading non-trivial term of this expansion at $n = 10$ specialises to $\delta_{CS} = \hbar_q^4 \cdot [5]_q$.

**(iv) The prefactor $8q$ on $\delta_{CS}^2$.** By [prop:force-carrier-bring-uniqueness](#prop:force-carrier-bring-uniqueness), the force-carrier sector consists of exactly $\{T_{2,9}, T_{3,5}\}$ (genus-4 torus knots embedded in Bring's curve). The second-order coefficient $8q$ in the Gram--Plancherel expansion is the genus-$4$ torus-knot enumeration count of distinct two-step crossing patterns, weighted by $q$ (the per-crossing quantum factor).

**Assembly (conjectural).** Combining (i)--(iv) is asserted to yield the closed form. **However, only step (i) admits a complete proof** (the dimension count $9 + 36 = 45$). Steps (ii), (iii), (iv) are sketches: (ii) misidentifies $\dim_q V_{(2,1)}$ in $H_3$ as $[3]_q$ (the correct value is $[2]_q$); (iii) does not carry out the leading-term computation in the Plancherel-character product; (iv) provides two mutually inconsistent stories for the integer $8$.

## Numerical validation

At $q_0 \approx 1.10998$ in 50 dps mpmath:

| Quantity | Value |
|----------|------:|
| $1/\alpha_{EM}$ (gluon-octet) | $137.035999998\,175\ldots$ |
| $1/\alpha_{EM}$ (CODATA 2018) | $137.035999084(21)$ |
| Residual | $+6.7 \times 10^{-9}$ (sub-ppb) |
| $q_0$ precision floor | $\approx 1.2 \times 10^{-9}$ |

The residual sits inside the $q_0$ uncertainty band (set by CODATA $m_\mu/m_e$ at $\sim 22$ ppb).

## PSLQ uniqueness

Run at $\mathrm{tol\_dps} \in \{50, 100, 200, 500, 1000\}$ over the canonical 52-element basis $\{1, \pi, \pi^2, \pi^4, \zeta(3), G, e, \gamma_E, \log 2, [k]_q\, (k=2..12), \hbar_q^k\, (k=1..6), (q;q)_n\, (n=2..6), q^k\}$:

> **No competing integer relation found at any tested precision.**

The gluon-octet form is the unique q-arithmetic relation in this basis matching CODATA $\alpha_{EM}$ at $> 10^{-9}$ precision. Witness: [`alpha-em-pslq-uniqueness.witness.json`](#).

## Status

This conjecture is **PSLQ-empirical**: it matches CODATA at $q_0$ to sub-ppb precision and is unique in the chosen 52-element basis, but a structural derivation linking each of $45$, $[3]_q$, $\hbar_q^4 [5]_q$, $8q$ to upstream propositions is **incomplete**. Only the integer $45$ is rigorously linked. Cross-validation at $q \ne q_0$ shows the formula disagrees with the alternative Chern-Simons form at every other $q$, indicating that the present statement is a single-point empirical fit, not a proven q-rational identity. Closing the derivation is an open problem.

## Witness

[`folio-assistant/computations/alpha_em_pslq_uniqueness.py`](#) — gluon-octet closed-form evaluation + PSLQ uniqueness probe at 1000 dps. Output: [`alpha-em-pslq-uniqueness.witness.json`](#).
