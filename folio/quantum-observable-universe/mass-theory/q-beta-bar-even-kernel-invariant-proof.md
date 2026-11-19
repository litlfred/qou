## Proof (one-line ring identity)

The N=2 instance is the prototype. With $u = b \cdot \hbar_q^2$:

$$
1 \;-\; u^2
\;=\; 1 - (b \cdot \hbar_q^2)^2
\;=\; 1 - b^2 \cdot \hbar_q^4.
$$

This is a `ring` identity in any commutative ring containing $b$ and
$\hbar_q$. Both factors are bar-even at the Taylor level: $b^2(q)$ is a
manifest q-rational that satisfies $b^2(q^{-1}) = b^2(q)$ exactly
(verified in the canonical formalism
chain), and $\hbar_q^4$ is even in $t$ to leading order
($\hbar_q = t - t^2 + O(t^3)$, so $\hbar_q^2 = t^2 - 2t^3 + O(t^4)$ and
$\hbar_q^4 = t^4 + O(t^5)$ — the odd-in-$t$ content sits at orders $t^5$
and higher, which the bar-even ladder absorbs trivially). $\blacksquare$

## Contrast: α_EM template vs $\mathfrak{Q}_\beta$ trace-difference

| programme | kernel | bar-even? | scalar $c_k$ extraction |
|---|---|---|---|
| $\alpha_{\text{EM}}$ | $H(q) = [2]_q \cdot (1 - h^2 \alpha)$ | **yes** — $[2]_q = q + q^{-1}$ and $h^2 = (q - q^{-1})^2$ are manifest q-symmetric | **clean** |
| $\mathfrak{Q}_\beta$ | trace-difference $T_\beta$ on the operator level | **no** — archimedean trace mixes odd-in-$t$ content (closed operator-level framing) | **singular at $u = 0$** |

The bar-even discriminant explains the asymmetry structurally: $\alpha_{\text{EM}}$
admits a scalar Habiro element because its kernel is bar-even; $\mathfrak{Q}_\beta$ does
not, so generating an empirical integer-$u$ ladder at $k \ge 3$ (beyond the explicit Convention-D trace cumulants $c_2^{(D)}, c_3^{(D)}, c_4^{(D)}$) requires an **operator-level grading** that is conjectural.
