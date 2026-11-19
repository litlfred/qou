**Algorithm (Generic Dipper–James / Wenzl semisimplicity and GPMT modified-trace renormalization on $H_n(q)$).**
*Decompose the generic Iwahori–Hecke algebra $H_n(q)$ over $\mathbb{Q}(q)$ (or over $\mathbb{R}$ at any real $q > 0$, $q \neq 1$) into simple matrix blocks indexed by partitions $\lambda \vdash n$, compute the central full-twist eigenvalues $\Delta_n^2|_{S^\lambda} = q^{2c(\lambda)}$, and extract both the Convention-D Wenzl weights $w_\lambda(z_D)$ and the Geer–Patureau-Mirand–Turaev (GPMT) modified dimensions $d_{\mathrm{mod}}(\lambda)$ for higher-row strata.*

### Input

- *Strand count $n \in \mathbb{N}_{\ge 1}$ and generic deformation parameter $q \in (0, \infty) \setminus \{1\}$ (or formal indeterminate $q$).*
- *Convention-D Markov parameter $z_D = \frac{q^3}{q^2 + 1}$.*

### Output

- *Indexed family $\bigl\{\bigl(\lambda,\; d_\lambda,\; c(\lambda),\; w_\lambda(z_D),\; m_\lambda,\; d_{\mathrm{mod}}(\lambda)\bigr)\bigr\}_{\lambda \vdash n}$, where:*
  - *$d_\lambda \in \mathbb{N}_{\ge 1}$ is the Specht/Hoefsmit block dimension satisfying $\sum_{\lambda \vdash n} d_\lambda^2 = n!$;*
  - *$c(\lambda) = \sum_{(i,j) \in \lambda} (j - i) \in \mathbb{Z}$ is the total Young content sum fixing $\Delta_n^2|_{S^\lambda} = q^{2c(\lambda)}$;*
  - *$w_\lambda(z_D) \in \mathbb{Q}(q)$ is the Convention-D Wenzl–Markov weight;*
  - *$m_\lambda = \mathrm{ord}_{z = z_D} w_\lambda(z) \in \mathbb{N}$ is the vanishing multiplicity at $z_D$, and $d_{\mathrm{mod}}(\lambda) = \lim_{z \to z_D} \frac{w_\lambda(z)}{(z - z_D)^{m_\lambda}} \in \mathbb{Q}(q)^\times$ is the non-zero GPMT modified dimension.*

### Algorithm

1. **Certify generic semisimplicity:** Verify $[m]_q = \frac{q^m - q^{-m}}{q - q^{-1}} = \sum_{j=0}^{m-1} q^{m - 1 - 2j} > 0$ for every $1 \le m \le n$ on $q \in (0, \infty)$, ensuring $[n]_q! = \prod_{m=1}^n [m]_q \neq 0$ so $H_n(q) \cong \bigoplus_{\lambda \vdash n} M_{d_\lambda}(\mathbb{Q}(q))$ is split semisimple.
2. **Enumerate partitions and exact discrete invariants:** For each partition $\lambda = (\lambda_1 \ge \cdots \ge \lambda_r > 0) \vdash n$:
   - Compute $d_\lambda = \frac{n!}{\prod_{(i,j) \in \lambda} h_\lambda(i, j)}$ by the Frame–Robinson–Thrall hook-length formula in exact integer arithmetic.
   - Compute the content sum $c(\lambda) = \sum_{(i,j) \in \lambda} (j - i)$ and central full-twist scalar $\Delta_n^2|_{S^\lambda} = q^{2c(\lambda)}$ (for instance, on $H_4(q)$, $c(\lambda) \in \{+6, +2, 0, -2, -6\}$ and $\Delta_4^2|_{S^\lambda} \in \{q^{12}, q^4, 1, q^{-4}, q^{-12}\}$).
3. **Evaluate two-row Convention-D Wenzl weights:** Construct the rational Schur–Wenzl weight $w_\lambda(z) \in \mathbb{Q}(q)(z)$ as a product over cells $(i, j) \in \lambda$ divided by the quantum hook product $\prod_{(i,j) \in \lambda} [h_\lambda(i, j)]_q$. For $\ell(\lambda) \le 2$, $m_\lambda = 0$ and $w_\lambda(z_D) \neq 0$ (e.g. $w_{(3)}(z_D) = \frac{q^4 + 1}{(q^2 + 1)^2}$ and $w_{(2,1)}(z_D) = \frac{q^2}{(q^2 + 1)^2}$ on $H_3(q)$).
4. **Extract GPMT modified dimensions on $\ell(\lambda) \ge 3$:** Whenever $\ell(\lambda) \ge 3$, factor out the exact power $(z - z_D)^{m_\lambda}$ in $\mathbb{Q}(q)[z]$ from the numerator of $w_\lambda(z)$ (each cell in row $3$ with content $c(\square) = j - 3$ contributing the Convention-D zero at $j = 1$) and evaluate the cancelled quotient at $z = z_D$:
   $$
     d_{\mathrm{mod}}(\lambda)
     \;=\;
     \left.\frac{w_\lambda(z)}{(z - z_D)^{m_\lambda}}\right|_{z = z_D}
     \;\in\; \mathbb{Q}(q)^\times.
   $$

### Termination and Complexity

Partition enumeration visits $p(n)$ Young diagrams ($p(3) = 3$, $p(4) = 5$, $p(9) = 30$), and for each $\lambda \vdash n$ the hook product, content sum, and polynomial division in $\mathbb{Q}(q)[z]$ require $O(n^2)$ arithmetic operations, giving total complexity $O(p(n)\,n^2)$.

### Mathematical Justification

1. **Wedderburn–Wenzl decomposition:** Split semisimplicity and the trace decomposition $\mathrm{tr}_M = \sum_{\lambda \vdash n} w_\lambda(z)\,\chi^\lambda$ follow from [the Wedderburn trace identity](#prop:wedderburn-trace-identity), [Wenzl-bridge applicability](#prop:wenzl-bridge-applicability-qou), and [the non-commutative Fourier decomposition](#prop:wedderburn-as-noncomm-fourier).
2. **Modified-trace desingularisation:** By [Convention-D uniqueness](#prop:convention-d-kills-antisymmetriser), $z = z_D$ annihilates $\ell(\lambda) \ge 3$ in the bare trace with finite algebraic multiplicity $m_\lambda \ge 1$; dividing by $(z - z_D)^{m_\lambda}$ before setting $z = z_D$ yields a non-degenerate $Z(H_n(q))$-equivariant trace on the three-row and four-row ideals (such as $(1^3)$ in $H_3(q)$ and $(2,1^2), (1^4)$ in $H_4(q)$), supplying the three-body and four-body nuclear Mayer cumulants of [Step 9b](#alg:per-isotope-binding).
