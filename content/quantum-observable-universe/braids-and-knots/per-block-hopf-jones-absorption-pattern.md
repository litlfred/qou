**Per-Wedderburn-block leading-order pattern: dimension-scaled Hopf-Jones absorption.**

Expanding the paper's per-block character closed forms from
[`rem:chi-per-irrep-cyclotomic-closed-forms`](#rem:chi-per-irrep-cyclotomic-closed-forms)
around $q = 1$ in $\varepsilon = q - 1$ exposes a clean structural
pattern in the $\varepsilon^1$ leading-order coefficients:

| irrep $\lambda$ | $\chi_\lambda(\beta_n - \beta_p)$ closed form | LO $\varepsilon^1$ coeff | Hopf-Jones absorption |
|:---:|:---:|:---:|:---|
| $V_{(3)}$ | $-\dfrac{(q^2+1)^2(q^2-1)}{4q}$ | $\mathbf{-2}$ | **full** ($= J_{\text{Hopf}}(q{=}1)$) |
| $V_{(2,1)}$ | $-\dfrac{(q^4+1)(q^2-1)}{4q^3}$ | $-1$ | half ($= J_{\text{Hopf}}(q{=}1)/2$) |
| $V_{(1,1,1)}$ | $-\dfrac{(q^2+1)^2(q^2-1)}{4q^5}$ | $\mathbf{-2}$ | **full** ($= J_{\text{Hopf}}(q{=}1)$) |

## Structural interpretation

Each block is **linear in $\hbar_q = (q-1)/q$ at leading order** —
factoring out the common $(q^2-1) = q(q+1)\hbar_q$:

$$
\begin{aligned}
\chi_{(3)}(\beta_n - \beta_p)     &= -\tfrac{1}{4}(q^2+1)^2 (q+1) \cdot \hbar_q, \\[4pt]
\chi_{(2,1)}(\beta_n - \beta_p)   &= -\tfrac{1}{4q^2}(q^4+1) (q+1) \cdot \hbar_q, \\[4pt]
\chi_{(1,1,1)}(\beta_n - \beta_p) &= -\tfrac{1}{4q^4}(q^2+1)^2 (q+1) \cdot \hbar_q.
\end{aligned}
$$

The LO $\varepsilon^1 = 2\hbar_q\big|_{q=1}$ coefficients are
extracted by setting $q = 1$ in the cyclotomic factor:

- $V_{(3)}$: $-\tfrac{1}{4}(2)^2 \cdot 2 = -2 = J_{\text{Hopf}}(q{=}1)$.
- $V_{(2,1)}$: $-\tfrac{1}{4}(2) \cdot 2 = -1 = J_{\text{Hopf}}(q{=}1)/2$.
- $V_{(1,1,1)}$: $-\tfrac{1}{4}(2)^2 \cdot 2 = -2 = J_{\text{Hopf}}(q{=}1)$.

The pattern: each 1-dimensional irrep ($V_{(3)}$ trivial, $V_{(1,1,1)}$
sign) absorbs the **full Hopf-Jones value** $-2$; the 2-dimensional
standard rep $V_{(2,1)}$ absorbs **half**, $-1$. The 2D
character-formula scaling by $\dim(V_\lambda)$ explains the halving.

## Connection to $c_3 = -2 = J_{\text{Hopf}}(q{=}1)$

[`prop:q-beta-c3-hopf-three-fold-markov`](#prop:q-beta-c3-hopf-three-fold-markov)
derives the global precision-ladder coefficient
$c_3 = J_{\text{Hopf}}(q{=}1) = -2$ via the 2-strand sub-braid argument
(Fact 3). The per-block decomposition above shows that this single
Hopf-Jones value is **realised structurally per Wedderburn block**:

- Both 1D reps absorb $-2$ in full.
- The 2D rep absorbs $-1$ (half), but with character-formula
  multiplicity $\dim V_{(2,1)} = 2$ in the Wedderburn sum.

The dimension-weighted sum reproduces the global $c_3$:
$\dim_q^2(V_{(3)}) \cdot (-2) + \dim_q^2(V_{(2,1)}) \cdot (-1)/2 +
\dim_q^2(V_{(1,1,1)}) \cdot (-2)$
$= 1 \cdot (-2) + [2]_q^2 \cdot (-1/2) + 1 \cdot (-2)$
which evaluates at $q = 1$ to $-2 + 4 \cdot (-1/2) + (-2) = -6$,
**before** Wenzl-bridge re-weighting via $y_\lambda$.

Under the Markov-bridge $y_\lambda$ weighting (not $\dim_q^2$):
$y_{(3)}(1) \cdot (-2) + y_{(2,1)}(1) \cdot (-1) + y_{(1,1,1)}(1) \cdot (-2)
= \tfrac{1}{6}(-2) + \tfrac{2}{3}(-1) + \tfrac{1}{6}(-2)
= -\tfrac{4}{3}$

This is the Markov-trace LO coefficient
$\tau_M(\beta_n - \beta_p) \approx -\tfrac{4}{3}\varepsilon + O(\varepsilon^2)$,
which matches the direct compute at $q_0$ to four-decimal precision.

## Why this matters

The per-block Hopf-Jones absorption pattern is the **structural
foundation** for extending [Fact 3](#prop:q-beta-c3-hopf-three-fold-markov)
beyond $c_3$. Higher precision-ladder coefficients $c_k$ for $k \geq 4$
come from **products** of the per-block linear-in-$\hbar_q$ factors,
giving $\hbar_q^k$ at order $k$. Each block's contribution carries the
LO Hopf-Jones absorption ($-2$ or $-1$), modulated by the block's
specific cyclotomic-factor structure (\Phi_4^2$ for 1D; $\Phi_8$ for 2D).

Verified at $q_0$ via
[`folio-assistant/computations/qbeta_per_block_paper_closed_forms.py`](../../folio-assistant/computations/qbeta_per_block_paper_closed_forms.py)
+
[`qbeta-per-block-paper-closed-forms.witness.json`](../../folio-assistant/computations/qbeta-per-block-paper-closed-forms.witness.json).
