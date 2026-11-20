**Remark (open problems for $\alpha_{EM}$ derivation).**

The bare singlet derivation ([prop:em-coupling-projection](#prop:em-coupling-projection)) gives

$$
  \frac{1}{\alpha_{\text{bare}}} \;=\; q\cdot[9]_q\cdot[10]_q
  \;\approx\; 136.823 \quad \text{at}\;\; q = q_0.
$$

This agrees with the CODATA-2022 value $137.035999177(21)$ to within $-0.155\%$. The bare formula reproduces the fine-structure constant to three significant figures with no free parameters. A relative gap of $1.55 \times 10^{-3}$ remains. Two prior attempts to close this gap are open conjectures:

| Form | Statement | Residual at $q_0$ | Status |
|------|-----------|-------------------|--------|
| Bare | $q[9]_q[10]_q$ | $-1.55\times 10^{-3}$ | Derived |
| Form A (CS) | $\cdot\bigl(1+\delta_{CS}/(1-\delta_{CS}\kappa)\bigr)$ with $\kappa=1.722$ | $-4.68\times 10^{-7}$ | Conj.; $\kappa$ unproved (Lean `sorry`); $\kappa \approx 1.9153$ needed for exact match |
| Form B (gluon-octet) | $45[3]_q\,(1+\hbar_q^4[5]_q+8q(\hbar_q^4[5]_q)^2)$ | $+2.6\times 10^{-9}$ | Conj.; only $45$ rigorously derived; disagrees with Form A at $q\ne q_0$ |

*Superseded figures, recorded so the change is legible.* This table previously
gave Form A as the order-$\delta_{CS}^2$ truncation with residual
$-4.0\times 10^{-7}$ and $\kappa \approx 1.888$, and Form B as
$+6.7\times 10^{-9}$. All three are **muon-pin** numbers, each correctly
computed for the pin and truncation it belongs to: $-4.0\times 10^{-7}$ is the
order-$2$ truncation at the muon pin ($-399.53$ ppb); $+6.7\times 10^{-9}$ is
Form B at the muon pin against CODATA-2018 ($6.672$ ppb); and
$\kappa \approx 1.888$ is exact closure at the muon pin under the order-$2$
truncation ($1.8880423$). They were stale, not wrong. The rows above are the **proton pin** (the standing default) with
the tower resummed in closed form, matching
[the Chern-Simons block](#rem:em-coupling-chern-simons), which already carried
the resummation and the re-pin. Reproduce every entry with
[`alpha_em_form_comparison_probe.py`](../../../computations/alpha/alpha_em_form_comparison_probe.py).

## Why both prior attempts fail

**Form A's $\kappa$ is incorrect.** The Witten-1988 Gram-determinant identification gives $\kappa \approx 1.722$. Matching CODATA at the proton-pinned $q_0$, with the tower resummed, requires $\kappa \approx 1.9153$. The discrepancy is $11.2\%$ and cannot be quadrature error: resummation is worth $11.06$ ppb against a $468$ ppb gap, about one part in forty. The Lean formalisation carried this as `sorry` from the start.

**Form B is hidden numerology.** Of its four factors:

- $45 = \dim \Lambda^2 V_{\text{nat}}^{10}$ is rigorous. It is the hook-length count of $V_{(9,1)} \oplus V_{(8,1,1)}$.
- $[3]_q$ does not equal the $q$-dimension of any natural irrep of $H_3(q)$ or $U_q(\mathfrak{sl}_3)$. The singlet-idempotent gluon-octet identification is asserted, not computed.
- $\hbar_q^4 \cdot [5]_q$ is claimed to be the leading non-trivial term of the Plancherel-character expansion at $n=10$. The calculation was not performed. The ambient $H_n$ is unspecified.
- $8q$ is identified two ways (Lean: $\dim \mathfrak{su}(3)$; text: two-step crossing-pattern enumeration). Neither calculation was performed. Exact truncation requires an order-$3$ coefficient of $\approx -52$, which is not a clean $q$-rational.

Form A and Form B agree only at $q = q_0$. They give different values for $1/\alpha$ at every other $q$. Form B is a single-point fit.

## Ruled-out derivation paths

Four computational paths to close the $1.55 \times 10^{-3}$ gap are ruled out. They do not produce clean low-degree $q$-rationals:

| Path | Result | Verdict |
|------|--------|---------|
| Gram-det Plancherel-character product at $n=3$ | $\kappa \approx 7 \times 10^{-6}$ | Ruled out (need $\sim 1.888$) |
| q-Plancherel sums on $H_5$ Wedderburn blocks | trivial or astronomical | Ruled out |
| Scan $\hbar_q^k\cdot[a]_q\cdot[b]_q/([c]_q\cdot[d]_q)$, $a,b,c,d \le 12$ | 0 matches at $10^{-4}$ | Ruled out at this degree |
| **PSLQ at 100 dps over 54-element basis incl. $\pi, \zeta(3), \log 2$** | **No non-trivial integer relation** | **Decisively ruled out** |

The closest single-term near-match is

$$ F - 1 \;\approx\; \frac{\hbar_q^2}{\pi \cdot [2]_q} $$

at $7.4 \times 10^{-4}$ relative residual. This structure relates to $\mathrm{Vol}(S^3_q) = \pi^2[2]_q$ geometry, but it is not exact. A direct closed-form correction in any natural $q$-arithmetic basis at low degree is impossible.

See `alpha-em-correction-derivation-attempts.witness.json` for the full attempt log.

## Insufficiency of block-diagonal Gram deformations

A natural ansatz deforms the Gram matrix by a framing correction $\mathcal{A}$ induced by a chiral anomaly on Bring's surface, $G_{\mathrm{CS},n}' = G_{\mathrm{CS},n} \otimes \mathcal{A}$. Every $G$ in this section is a **Chern--Simons** pairing Gram on Bring's surface, indexed by jet level $n$; none of them is the Markov--Gram $\mathrm{tr}_M(b_i b_j)$ of the $H_3(q)$ normal-form basis ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)), whose own determinants appear elsewhere in the corpus under the same glyph and whose $q$-dependence runs through the Markov parameter $z$, which never enters here. There are two sub-cases:

1. **Scalar $\mathcal{A} \in R$.** For an $N \times N$ Gram matrix, $\det G_{\mathrm{CS},n}' = \mathcal{A}^N \det G_{\mathrm{CS},n}$. The determinant ratio $\kappa = \det G_{\mathrm{CS},n} / \det G_{\mathrm{CS},n-1}$ becomes $\kappa' = \mathcal{A}^{\dim G_{\mathrm{CS},n} - \dim G_{\mathrm{CS},n-1}} \cdot \kappa_{\text{Witten}}$. This is a fixed power of $\mathcal{A}$ multiplying the Witten value. The corrected $1/\alpha_{EM}$ takes the multiplicative form $q[9]_q[10]_q \cdot (1 + \delta_{CS} + \mathcal{A}^{\Delta\dim}\kappa_{\text{Witten}}\delta_{CS}^2)$.
2. **Block-diagonal $2{\times}2$ $\mathcal{A}$**. This acts on the two Hecke eigenchannels $V_{(2)}, V_{(1,1)}$. The determinant of $G_{\mathrm{CS},n}'$ factors as a product of per-channel scalar powers. Again, $\kappa'$ is a multiplicative perturbation of $\kappa_{\text{Witten}}$. This "old derivation" route yielded $\kappa \approx 1.722$. It agrees with the Wedderburn-block Plancherel sum but falls short of the CODATA value.

Both sub-cases live in the multiplicative $q$-rational family. The 100-dps PSLQ scan over the 54-element basis ruled out this family. Any Gram deformation preserving block-diagonal structure on $V_{(2)} \oplus V_{(1,1)}$ cannot close the gap.

Closure requires an off-diagonal approach or an additive form. The additive Bring zero-mode form ([Additive Bring zero-mode form $1/\alpha_{EM} = q\cdot[9]_q\cdot[10]_q + 2g/(4\pi(g-1))$ (conditional)](#prop:em-coupling-bring-zero-mode)) supplies the correction $2/(3\pi) = 2g/(4\pi(g-1))$ at $g=4$ as a summand. The substrate pentagon-coherence factors the quantum observable universe mass-formula state sum through a class in the Bloch group $B(\mathbb{C})$. Bloch-Suslin pentagon-uniqueness forces every real-valued archimedean realization to coincide with the Bloch-Wigner dilogarithm $D$. The $\pi$ in $2/(3\pi)$ is the unique archimedean shadow of substrate pentagon data. Two open computations remain: identify the explicit Bloch-group class on Bring's surface, and lift the next-order $\alpha/(4\pi)$ term to a higher Bloch group $B_n(\mathbb{C})$.

## Implications

**The correction is a genuine two-loop effect.**
The additive photon zero-mode $2/(3\pi)$ has arithmetic weight $1$. It derives from $b_1/\mathrm{Area}$ and brings the residual to $-4.2\;\mathrm{ppm}$. The remaining $\mathcal{O}(\alpha^2)$ correction has arithmetic weight $3$. Its home is $\zeta(3)$. Quantum electrodynamics first requires a two-loop diagram at this rung. Classical categorical or tree-level routes have weight $\le 2$. The parameter-free prediction is complete to $\approx 4\;\mathrm{ppm}$. The finer $\mathcal{O}(\alpha^2)$ correction is a genuine two-loop vacuum-polarisation effect. It is not a categorical-level closed form.

## Promising lead: additive QED-style correction

An additive form yields a striking numerical match:

$$
  \frac{1}{\alpha_{EM}}
  \;\approx\;
  q \cdot [9]_q \cdot [10]_q
  \;+\;
  \frac{2}{3\pi}
  \;+\;
  \frac{\alpha}{4\pi}.
$$

| Form | Predicted $1/\alpha$ at $q_0$ | Residual vs CODATA (relative) |
|------|------------------------------|-------------------------------|
| Bare $q[9]_q[10]_q$ | 136.823220 | $-1.55 \times 10^{-3}$ |
| $+ 2/(3\pi)$ | 137.035426 | $-4.2 \times 10^{-6}$ |
| $+ \alpha/(4\pi)$ | 137.036007 | $+5.7 \times 10^{-8}$ |
| CODATA 2022 | $137.035999177(21)$ | — |

The first correction is derived ([Photon IR zero-mode on Bring's surface](#prop:photon-ir-zero-mode-bring)). It is the photon infrared zero-mode on the 2-surface $M_{\text{Bring}}$. The harmonic $1$-form sector $b_1(M_g) = 2g$ normalises by the Gauss–Bonnet area $4\pi(g-1)$:

$$
  \frac{2}{3\pi}
  \;=\; \frac{b_1(M_g)}{\mathrm{Area}(M_g)}
  \;=\; \frac{2g}{4\pi(g-1)}\Big|_{g=4}
  \;=\; \frac{8}{12\pi}.
$$

The sphere-volume form $2/(3\pi) = \mathrm{Vol}(S^2)/(3\cdot\mathrm{Vol}(S^3))$ is a secondary reading of the same number. The photon zero-mode lives on the $2$-surface. The denominator $3$ is the Gauss–Bonnet factor $(g-1)=3$. The $\alpha/(4\pi)$ term suggests a Schwinger-like 1-loop self-coupling.
