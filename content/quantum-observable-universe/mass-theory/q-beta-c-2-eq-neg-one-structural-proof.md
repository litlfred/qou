## Proof (algebraic identity)

The operator-valued $N{=}2$ correction to $\mathfrak{Q}_\beta$ (per the brane-tower
truncation of [`probe_q_beta_operator_valued_N3.py`](https://github.com/litlfred/qou/blob/main/computations/probe_q_beta_operator_valued_N3.py))
is the factor $(1 - b^2 \cdot \hbar_q^4)$. With $u_{\text{ladder}} = b \cdot \hbar_q^2$,
direct expansion gives

$$
1 - b^2 \cdot \hbar_q^4
\;=\; 1 - (b \cdot \hbar_q^2)^2
\;=\; 1 - u_{\text{ladder}}^2.
$$

This is a one-line `ring` identity in any commutative ring containing
$b$ and $\hbar_q$. Comparing to the ladder ansatz
$1 + c_2 \cdot u_{\text{ladder}}^2 + O(u_{\text{ladder}}^3)$ at order $u_{\text{ladder}}^2$
forces $c_2 = -1$. $\blacksquare$
