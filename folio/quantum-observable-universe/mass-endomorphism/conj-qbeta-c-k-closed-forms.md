**Conjecture (higher-order $\mathfrak{Q}_\beta$ ladder coefficients $c_k$ for $k \ge 4$).**

*In the infinite-product expansion $\Pi_{\mathrm{op}}(u) = \prod_{k=2}^\infty (1 + c_k u^k) = 1 + \sum_{n=2}^\infty p_n u^n$ of the neutron $\beta$-decay observable in the Habiro–Hoefsmit coordinate $u(q) = b(q)\,\hbar_q^2$ ($b(q) = \sqrt{q^4 + q^2 + 1}/(q^2 + 1)$, $\hbar_q = 1 - q^{-1}$), each higher-order coefficient $c_k$ ($k \ge 4$) is uniquely determined by a single canonical Markov-trace operator projection on $H_3(q)$.*

## Proved Convention-D structure vs retired Convention-C pattern guesses

Under canonical Convention D ($z_D = q^3/(q^2 + 1)$), three foundational components of the ladder are established unconditionally:

1. **All-order generating function, critical radius, and distinct-partition extraction:** Every bar-even building block of the Convention-D + GPMT + Two-Term Borromean $V^3$ operator is a rational function or polynomial in $H = (q - q^{-1})^2$. The squared ladder coordinate $u_{\mathrm{bar}}^2(H) = H^2(H + 3)/(16(H + 4))$ is strictly increasing on $H \ge 0$ and has its nearest complex critical point at $H_* = (-15 + \sqrt{33})/4 \in (-3, -2)$, fixing the Lagrange–Bürmann radius of convergence $R_u = \sqrt{u_{\mathrm{bar}}^2(H_*)} \approx 0.36900873$. Over any commutative ring, $(c_2, \ldots, c_{10})$ and the Taylor coefficients $(p_2, \ldots, p_{10})$ stand in division-free polynomial bijection via partitions into distinct parts $\ge 2$, and the contraction ratio $u(q_0)/R_u \approx 0.02308 < 1/40$ bounds the $N = 9$ Cauchy tail strictly below $10^{-16}$ ($< 1\,\mathrm{ppQ}$).
2. **Operator-level $c_2$ and $c_3$ closure:** Rewriting the mirror-projected Convention-D phase in the bar-even Habiro variable $y = (q + q^{-1}) - 2 = q\,\hbar_q^2$ eliminates the $\sqrt{u}$ branch point and yields the exact algebraic Taylor jet $(1, -\sqrt{3}/12, 47/96, -2069\sqrt{3}/5760)$ through $u_{\mathrm{Hab}}^3$ alongside the $N = 3$ Kashiwara–Hopf product seeds $c_2 = -1$ and $c_3 = -2$.
3. **Quartic rung $u(q)^4 \in \mathbb{Q}(q)$ and structural $c_4$ candidates:** Every even rung power $u(q)^{2m} = ((h^2 + 3)/(h^2 + 4))^m \hbar_q^{4m}$ lies in $\mathbb{Q}(q)$ without radicals, with $u(q_0)^4 \approx 5.263 \times 10^{-9} < 6 \times 10^{-9}$. At $q = 1$, both the $m = 2$ divided-power Kashiwara crystal cosine coefficient $[2]_q / ([3]_q [4]_q)$ and the variance-matched Convention-D Jucys–Murphy content kurtosis rung $\frac{1}{2} + \gamma_2^D(1)/6$ ($\gamma_2^D(1) = -2$) evaluate to $+1/6$, whereas the three-block GPMT+ kurtosis evaluates to $+101/288$. Because $u(q_0)^4 < 6 \times 10^{-9}$, every order-unity choice of $c_4$ shifts $m_n$ by less than $10^{-4}\,\sigma_{\mathrm{exp}}(m_n)$.

In contrast, [the categorical precision ladder](#prop:q-beta-categorical-precision-ladder) historically recorded four empirical Convention-C ($z_C = \sqrt{q}/(q + 1)$, $z = 1$) pattern guesses:
$$
  c_4^{\mathrm{hist}} = c_3 b^4 = -2 b^4, \qquad
  c_5^{\mathrm{hist}} = -\bigl(b^2 + \tfrac{1}{2}\bigr), \qquad
  c_6^{\mathrm{hist}} = c_3^2 b^2 = 4 b^2, \qquad
  c_7^{\mathrm{hist}} = c_3^3 = -8.
$$
Those four expressions were calibrated against CODATA residuals on the retired Convention-C cell and remain unproved; downstream statements referencing them take that closed-form assumption as an explicit uninhabited hypothesis. What remains genuinely open under Convention D is selecting a single canonical operator projection distinguishing the $+1/6$ Kashiwara/Wedderburn quartic rung from the $+101/288$ GPMT+ kurtosis rung at $k = 4$, and deriving explicit closed forms for $c_k$ ($k \ge 5$) via finite-$q$ Khovanov–Rozansky or KLR canonical-basis traces ([companion derivation remark](conj-qbeta-c-k-closed-forms-derivation.md)).
