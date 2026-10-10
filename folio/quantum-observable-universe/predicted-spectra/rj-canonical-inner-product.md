The Markov trace on the Iwahori–Hecke algebra $H_r(q)$ induces a canonical bilinear form on the representation ring $R(H_r(q))$ via Schur orthogonality. The form is degenerate, and it is an inner product on the span of the two-row classes.

## Statement

**Proposition.**
*Let $H_r(q)$ be the Iwahori–Hecke algebra on $r$ strands with parameter $q \neq 0, 1$. Let $R(H_r(q)) = \bigoplus_{\lambda \vdash r} \mathbb{Z} \cdot [\lambda]$ be its representation ring.*

**(i)** *The Markov trace $\mathrm{tr}_M \colon H_r(q) \to \mathbb{Q}(q)$ uses the canonical Markov parameter $z = q^3/(q^2+1) = q^2/[2]_q$. It descends to a bilinear form on $R(H_r(q))$:*

$$
  \langle [\lambda], [\mu] \rangle_{\mathrm{RJ}}
  = 
  d_\lambda(q) \cdot \delta_{\lambda\mu},
$$

*where $d_\lambda(q) = \prod_{\Box \in \lambda} \frac{[2 + c(\Box)]_q}{[h(\Box)]_q}$ is the $U_q(\mathfrak{sl}_2)$ quantum dimension of $V_\lambda$. Here $c(\Box)$ is the content and $h(\Box)$ the hook length (arm $+$ leg $+ 1$) of cell $\Box$ in the Young diagram $\lambda$, and $[n]_q = (q^n - q^{-n})/(q - q^{-1})$. The Markov block weights are $w_\lambda = \mathrm{tr}_M(p_\lambda) = d_\lambda(q)/[2]_q^{\,r}$ for a minimal idempotent $p_\lambda$. Because $d_\lambda = 0$ whenever $\lambda$ has more than two rows, the form is degenerate: its radical is spanned by the classes $[\lambda]$ with more than two rows, and it is non-degenerate on the span of the two-row classes.*

**(ii)** *The form is the one induced by the Markov trace on minimal idempotents:*

$$
  \langle [\lambda], [\mu] \rangle_{\mathrm{RJ}}
  =
  [2]_q^{\,r} \, \mathrm{tr}_M\!\bigl(p_\lambda \, p_\mu\bigr)
  =
  d_\lambda(q) \cdot \delta_{\lambda\mu},
$$

*which does not depend on the choice of minimal idempotents, since conjugate idempotents have equal trace and $p_\lambda p_\mu = 0$ for $\lambda \neq \mu$. Equivalently $[2]_q^{\,r}\,\mathrm{tr}_M(x) = \sum_{\lambda \vdash r} d_\lambda(q)\, \chi_\lambda(x)$ for $x \in H_r(q)$. The Markov trace with $\mathrm{tr}_M(1) = 1$ is unique for a given $z$, so the form is determined by $z$ alone. Diagonality in the irrep basis does not by itself determine the form: a diagonal form has one free entry for each two-row class, and the normalisation $\mathrm{tr}_M(1) = 1$ fixes only one combination of them.*

**(iii)** *Let $\gamma = \sigma_1 \cdots \sigma_{r-1}$, so that $\gamma^r = \Delta^2$ is the full twist, which acts on $V_\lambda$ by $\theta_\lambda = q^{2 c_\lambda}$, where $c_\lambda$ is the content sum of $\lambda$. For $\gcd(r,s) = 1$ the torus knot $\tau(r,s)$ is the closure of $\gamma^s$, and its trace is given by the Rosso–Jones formula:*

$$
  [2]_q^{\,r} \, \mathrm{tr}_M\!\bigl(\gamma^{s}\bigr)
  =
  \sum_{j=0}^{r-1} (-1)^{j} \, d_{(r-j,1^j)}(q) \, \theta_{(r-j,1^j)}^{\,s/r}
  =
  [r+1]_q \, q^{s(r-1)} - [r-1]_q \, q^{s(r-3)}.
$$

*The sum runs over the hooks $(r-j, 1^j)$, and the signs $(-1)^j$ are the coefficients of the Adams operation $\psi^r$ applied to the fundamental representation. Since $c_{(r-j,1^j)} = r(r-1-2j)/2$, each exponent $2 s c_\lambda / r = s(r-1-2j)$ is an integer. Only $j = 0, 1$ contribute, because $d_\lambda = 0$ for every hook with more than two rows. The unknot-normalised invariant $[2]_q^{\,r-1} \, q^{-2s(r-1)} \, \mathrm{tr}_M(\gamma^s)$ is the Jones polynomial of $\tau(r,s)$ at $t = q^{-2}$.*
