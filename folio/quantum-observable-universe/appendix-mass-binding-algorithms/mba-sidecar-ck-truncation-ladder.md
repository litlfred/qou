**Algorithm (All-order Convention-D $c_k^{(D)}$ generating function, Lagrange–Bürmann inversion, and cumulant extraction).**
*Construct the all-order Convention-D $\beta$-decay generating function $\mathcal{G}_D(u; q) = \prod_{k=2}^{\infty} \bigl(1 + c_k^{(D)}\,u^k\bigr)$, extract the closed-form Convention-D rungs $c_2^{(D)}$, $c_3^{(D)}(q)$, and $c_4^{(D)}(q)$ together with all higher $c_k^{(D)}$ by division-free distinct-partition recursion, and certify geometric tail convergence inside $R_u$.*

### Input

- *Deformation parameter $q > 1$ (symbolic or evaluated at $q_{2t}$) with Convention-D parameter $z_D = \frac{q^3}{q^2 + 1}$, quadratic discriminant $h = q - q^{-1}$, bar-even variable $H = h^2 = (q - q^{-1})^2$, and quantum Planck step $\hbar_q = 1 - q^{-1}$.*
- *Maximum extraction order $K_{\max} \ge 4$ and target tail tolerance $\varepsilon > 0$.*

### Output

- *Exact critical branch point $H_* = \frac{-15 + \sqrt{33}}{4}$ and convergence radius $R_u = \sqrt{\bar{u}^2(H_*)} \approx 0.369009$.*
- *Derived Convention-D coefficients $\bigl\{c_k^{(D)}\bigr\}_{k=2}^{K_{\max}}$ and certified truncation order $N(\varepsilon)$.*

### Algorithm

1. **Assemble bar-even $H = (q - q^{-1})^2$ rational operator blocks:** Express every Convention-D + GPMT + Two-Term Borromean $V^3$ trace component as an exact rational function of $H$:
   $$
     w_{(2,1)}(z_D) = \frac{1}{H + 4},
     \quad
     w_{(3)}(z_D) = \frac{H + 2}{H + 4},
     \quad
     \bigl|d_{\mathrm{mod}}(1^3)\bigr|^2 = \frac{1}{(H + 4)(H + 3)^2},
     \quad
     \Delta\mathrm{tr}_{\mathrm{QED,conn}}(V^3) = \frac{H^2(4H + 9)}{27},
   $$
   together with the squared mirror-projected phase $\bigl(\alpha_D^{\mathrm{proj}}(q)\bigr)^2 = \frac{y(y + 4)(y^2 + 2y - 2)^2}{16(y + 2)^2}$ in $y = q + q^{-1} - 2 = q\,\hbar_q^2$.
2. **Invert the ladder coordinate via Lagrange–Bürmann:** The squared bar-even ladder coordinate
   $$
     \bar{u}^2(H) \;=\; \frac{H^2(H + 3)}{16(H + 4)}
   $$
   has derivative numerator $H\,(2H^2 + 15H + 24)$ ($8(2H^2 + 15H + 24) = (4H + 15)^2 - 33$), proving strict monotonicity on $H \ge 0$ and locating the nearest complex singularity at $H_* = \frac{-15 + \sqrt{33}}{4} \in (-3, -2)$ (strictly closer to $H = 0$ than the $[3]_q = 0$ zero at $H = -3$ and $[2]_q = 0$ pole at $H = -4$). Set $R_u = \frac{15 - \sqrt{33}}{16}\sqrt{\frac{\sqrt{33} - 3}{\sqrt{33} + 1}} \approx 0.36900873$ and invert $H(\bar{u}) = \sum_{m=1}^{K_{\max}} \beta_m\,\bar{u}^m$ over $\mathbb{Q}(\sqrt{3})$.
3. **Evaluate the closed-form low-order Convention-D rungs ($k = 2, 3, 4$):**
   - *Quadratic Kashiwara rung ($k = 2$):* $c_2^{(D)} = -1$ on the explicit $(1 - u^2)$ factor, with rational square $u(q)^2 = \frac{H + 3}{H + 4}\hbar_q^4 \in \mathbb{Q}(q)$ (for the unseparated cosine-included series, $\tilde{c}_2^{(D)} = -1 - \tfrac{1}{8} = -\tfrac{9}{8}$).
   - *Cubic Convention-D rung ($k = 3$):* evaluate the exact rational Convention-D odd-channel function
     $$
       c_3^{(D)}(q) \;=\; -\frac{3q^2 - 1}{2q(q^2 + 1)}
     $$
     and the branch-free Habiro $u_{\mathrm{Hab}} = q\,u = b(q)\,y$ cubic jet of $\cos\alpha_D^{\mathrm{proj}}(q)$.
   - *Quartic cumulant rung ($k = 4$):* all even ladder powers $u(q)^{2m} = \bigl(\frac{H + 3}{H + 4}\bigr)^m \hbar_q^{4m} \in \mathbb{Q}(q)$ are radical-free ($u^4 = \frac{9}{16}\hbar_q^8 + O(\hbar_q^{10})$); evaluate $c_4^{(D)}(q)$ from the $m = 2$ divided-power Kashiwara crystal coefficient $\frac{[2]_q}{[3]_q[4]_q}$ ($\to +\tfrac{1}{6}$ at $q = 1$) and the fourth Jucys–Murphy content cumulant (kurtosis $\kappa_4^{(D)} = \mu_4 - 3\mu_2^2$, $\kappa_4^{(D)}(1) = -\tfrac{1}{8}$, excess kurtosis $\gamma_2^{(D)}(1) = -2$) on $H_3(q)$ and its GPMT 3-block completion.
4. **Extract all higher $c_n^{(D)}$ ($2 \le n \le K_{\max}$) by division-free distinct-partition recursion:** Substitute $H(\bar{u})$ into the normalised Convention-D operator ratio to obtain $\mathcal{G}_D(u; q) = 1 + \sum_{n=2}^{K_{\max}} p_n^{(D)}\,u^n$. Because each factor $(1 + c_k^{(D)} u^k)$ is linear in $u^k$, $[u^n]\prod_{k \ge 2}(1 + c_k^{(D)} u^k)$ ranges over partitions of $n$ into distinct parts $\ge 2$, yielding the exact division-free triangular recursion
   $$
     c_n^{(D)}
     \;=\;
     p_n^{(D)}
     \;-\;
     \sum_{\substack{\lambda \vdash n,\; \ell(\lambda) \ge 2 \\ \lambda_1 > \lambda_2 > \cdots > \lambda_{\ell} \ge 2}}
       \prod_{j=1}^{\ell(\lambda)} c_{\lambda_j}^{(D)}
     \qquad (2 \le n \le K_{\max}).
   $$
5. **Certify the geometric Cauchy tail:** Bound the relative remainder above order $N$ using $r = u(q)/R_u < \tfrac{1}{40}$ via $\frac{r^{N+1}}{1 - r}$ ($< 4 \times 10^{-15}$ at $N = 8$ and $< 10^{-16}$ at $N = 9$).

### Termination and Complexity

Series composition up to degree $K_{\max}$ over $\mathbb{Q}(\sqrt{3})$ takes $O(K_{\max}^2)$ ring operations, and enumerating strict partitions of $n \le K_{\max}$ into parts $\ge 2$ takes $O(q_{\mathrm{strict}}(K_{\max}))$ multiplications ($10$ strict partitions at $n = 10$).

### Mathematical Justification

The convergent product structure and truncation inequality follow [the categorical precision-ladder proposition](#prop:q-beta-categorical-precision-ladder), the structural $k = 2$ coefficient follows [the $c_2 = -1$ structural proposition](#prop:q-beta-c-2-eq-neg-one-structural), and the Convention-D eigenphase transfer structure follows [Convention-D cosine resummation](#prop:q-beta-cos-resummation), replacing the retired Convention-C empirical cache throughout [Step 11](#alg:q-beta-truncation).
