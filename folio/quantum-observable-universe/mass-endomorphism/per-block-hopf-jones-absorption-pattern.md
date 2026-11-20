# Per-Wedderburn-block leading-order pattern: dimension-scaled Hopf-Jones absorption

Expanding the per-block character closed forms (from [All three $V_\lambda$ per-irrep character difference closed forms with **cyclotomic factor pattern**](#rem:chi-per-irrep-cyclotomic-closed-forms)) around $q = 1$ in $\varepsilon = q - 1$ exposes a structural pattern in the $\varepsilon^1$ leading-order coefficients.

| Irrep $\lambda$ | $\chi_\lambda(\mathcal{B}_n - \mathcal{B}_p)$ closed form | LO $\varepsilon^1$ coeff | Hopf-Jones absorption |
|:---:|:---:|:---:|:---|
| $V_{(3)}$ | $-\dfrac{(q^2+1)^2(q^2-1)}{4q}$ | $\mathbf{-2}$ | Full ($= J_{\text{Hopf}}(q{=}1)$) |
| $V_{(2,1)}$ | $-\dfrac{(q^4+1)(q^2-1)}{4q^3}$ | $-1$ | Half ($= J_{\text{Hopf}}(q{=}1)/2$) |
| $V_{(1,1,1)}$ | $-\dfrac{(q^2+1)^2(q^2-1)}{4q^5}$ | $\mathbf{-2}$ | Full ($= J_{\text{Hopf}}(q{=}1)$) |

## Structural interpretation

Each block is linear in $\hbar_q = (q-1)/q$ at leading order. Factoring out the common $(q^2-1) = q(q+1)\hbar_q$ gives:

$$
\begin{aligned}
\chi_{(3)}(\mathcal{B}_n - \mathcal{B}_p)     &= -\tfrac{1}{4}(q^2+1)^2 (q+1) \cdot \hbar_q, \\[4pt]
\chi_{(2,1)}(\mathcal{B}_n - \mathcal{B}_p)   &= -\tfrac{1}{4q^2}(q^4+1) (q+1) \cdot \hbar_q, \\[4pt]
\chi_{(1,1,1)}(\mathcal{B}_n - \mathcal{B}_p) &= -\tfrac{1}{4q^4}(q^2+1)^2 (q+1) \cdot \hbar_q.
\end{aligned}
$$

One extracts the leading-order $\varepsilon^1 = 2\hbar_q\big|_{q=1}$ coefficients by setting $q = 1$ in the cyclotomic factor:

- $V_{(3)}$: $-\tfrac{1}{4}(2)^2 \cdot 2 = -2 = J_{\text{Hopf}}(q{=}1)$.
- $V_{(2,1)}$: $-\tfrac{1}{4}(2) \cdot 2 = -1 = J_{\text{Hopf}}(q{=}1)/2$.
- $V_{(1,1,1)}$: $-\tfrac{1}{4}(2)^2 \cdot 2 = -2 = J_{\text{Hopf}}(q{=}1)$.

The one-dimensional representations ($V_{(3)}$ trivial, $V_{(1,1,1)}$ sign) absorb the full Hopf-Jones value $-2$. The two-dimensional standard representation $V_{(2,1)}$ absorbs half, $-1$. The character-formula scaling by $\dim(V_\lambda)$ accounts for this halving.

## Connection to $c_3 = -2$

The global precision-ladder coefficient $c_3 = J_{\text{Hopf}}(q{=}1) = -2$ emerges via the two-strand sub-braid argument ([`prop:q-beta-c3-hopf-three-fold-markov`](#prop:q-beta-c3-hopf-three-fold-markov)). The per-block decomposition shows that this Hopf-Jones value arises structurally per Wedderburn block. 

Both one-dimensional representations absorb $-2$ in full. The two-dimensional representation absorbs $-1$, but carries a character-formula multiplicity $\dim V_{(2,1)} = 2$ in the Wedderburn sum. The dimension-weighted sum reproduces the global $c_3$ before Wenzl-bridge re-weighting via $y_\lambda$:

$$
\dim_q^2(V_{(3)}) (-2) + \dim_q^2(V_{(2,1)}) (-1/2) + \dim_q^2(V_{(1,1,1)}) (-2)
$$

Evaluating at $q = 1$ yields $1 (-2) + 4 (-1/2) + 1 (-2) = -6$. 

Under the Markov-bridge $y_\lambda$ weighting, $y_\lambda$ at $q=1$ satisfies $\mathrm{tr}_M(1)=1$, $\mathrm{tr}_M(\sigma)=z=1/2$, and $\mathrm{tr}_M(\sigma_1\sigma_2)=z^2=1/4$. This yields $y_{(3)}(1)=1/2$, $y_{(2,1)}(1)=1/4$, and $y_{(1,1,1)}(1)=0$. The sum evaluates to:

$$
y_{(3)}(1) (-2) + y_{(2,1)}(1) (-1) + y_{(1,1,1)}(1) (-2) = -\tfrac{5}{4}.
$$

This provides the Markov-trace leading-order coefficient $\mathrm{tr}_M(\mathcal{B}_n - \mathcal{B}_p) \approx -\tfrac{5}{4}\varepsilon + O(\varepsilon^2)$. At the substrate parameter $q_0$, the $y_\lambda$ values constitute $q$-dependent rational functions rather than a probability measure. A direct computation gives $\mathrm{tr}_M(\mathcal{B}_n - \mathcal{B}_p) \approx -0.142$, consistent with the $y_\lambda(q_0) \chi_\lambda(q_0)$ sum.

## Significance

This per-block absorption pattern establishes the foundation for extending the coefficient sequence beyond $c_3$. Higher precision-ladder coefficients $c_k$ for $k \geq 4$ arise from products of the per-block linear-in-$\hbar_q$ factors, producing $\hbar_q^k$ at order $k$. Each block's contribution carries the leading-order Hopf-Jones absorption, modulated by the block's cyclotomic-factor structure ($\Phi_4^2$ for one-dimensional representations; $\Phi_8$ for two-dimensional representations).
