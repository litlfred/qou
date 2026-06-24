By definition $\delta_q(T_{2,k}) = q^{k} - q^{-k}$ and
$[k]_q = (q^{k} - q^{-k})/(q - q^{-1})$. Since $q - q^{-1} \neq 0$ in the
substrate ring $R$, multiplying $[k]_q$ by $h = q - q^{-1}$ cancels the
denominator:
$$
  h\,[k]_q
  = (q - q^{-1}) \cdot \frac{q^{k} - q^{-k}}{q - q^{-1}}
  = q^{k} - q^{-k}
  = \delta_q(T_{2,k}).
$$
The cancellation is the only step, and it is valid precisely because
$q - q^{-1} \neq 0$. The identity is purely algebraic in
$R = \mathbb{Z}[q^{\pm 1/2}, h^{-1}]$ — pre-archimedean, no $\pi$. The Lean
witness `QOU.AlphaBasisKnot.deltaQ_eq_h_qbracket` discharges it sorry-free
via `div_mul_cancel₀`. $\qquad\blacksquare$
