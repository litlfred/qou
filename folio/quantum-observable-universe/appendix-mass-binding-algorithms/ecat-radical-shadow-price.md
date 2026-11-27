**Prior-art reduction.** Certifying primal bounds via linear-programming resolving multipliers and kernel annihilators follows **Gyula Farkas** \cite{farkas1902} and **Leonid Vitaliyevich Kantorovich** \cite{kantorovich1939}, combined with **Hans Wenzl**'s \cite{wenzl1988} three-strand idempotent annihilator on $H_3(q)$ ([Markov--Gram star positivity](#prop:markov-gram-star-positive), [Operator selection LP](#prop:operator-selection-lp)).

- **Input:** Six-component geometric cost vector $t_{\mathrm{geom}} = (c_0, c_1, c_1', c_2, c_2', c_3) \in \mathbb{Q}(q)^6$ indexed by the ordered Coxeter basis $(1, \sigma_0, \sigma_1, \sigma_0\sigma_1, \sigma_1\sigma_0, \sigma_0\sigma_1\sigma_0)$ of $H_3(q)$ at $q > 0$, $q \neq 1$.
- **Output:** Exact closed-form net-normalization shadow price $y_0^\ast(q) \in \mathbb{Q}(q)$ and reduced-cost vector $\bar{t}(q) = t_{\mathrm{geom}} - y_0^\ast(q)\,\mathbf{1}$ on the five-dimensional quotient $TL_3(q)$, evaluated without invoking an interior-point solver.
- **QOU delta (algebraic radical pairing on singular $H_3(q)$):** Under $z = q^3/(q^2+1)$, the six-dimensional Gram operator $S$ on $H_3(q)$ has one-dimensional kernel spanned by $r_{[1^3]}(q) = (1, -q^{-1}, -q^{-1}, q^{-2}, q^{-2}, -q^{-3})$, which makes unreduced numerical interior-point factorizations singular. Contracting the dual stationarity equation $S^\mathsf{T} y + y_0\,\mathbf{1} = t_{\mathrm{geom}}$ against $r_{[1^3]}(q)$ annihilates $S^\mathsf{T} y$ identically and pins the net shadow price in closed rational form:

$$
  y_0^\ast(q) \;=\; \frac{\langle t_{\mathrm{geom}}, r_{[1^3]}(q)\rangle}{\langle \mathbf{1}, r_{[1^3]}(q)\rangle},
  \qquad
  \langle \mathbf{1}, r_{[1^3]}(q)\rangle \;=\; (1 - q^{-1})(1 + q^{-1} - q^{-2}) \neq 0.
$$

  For any Coxeter-length-symmetric cost $(c_0, c_1, c_1, c_2, c_2, c_3)$, the numerator reduces to $(c_0 - c_3 q^{-3}) - q^{-1}(1 - q^{-1})(c_1 + c_2)$, deciding non-vanishing of the radical shadow price by a six-term polynomial check in $\mathbb{Q}(q)$.
- **Complexity and precision:** $\mathcal{O}(1)$ exact field operations in $\mathbb{Q}(q)$ ($6$ multiplications), evaluated at $q_0$ to 80 decimal places with zero floating-point matrix inversions.
