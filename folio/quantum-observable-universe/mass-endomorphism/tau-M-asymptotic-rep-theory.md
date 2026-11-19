**$\mathrm{tr}_M$ ladder — representation-theoretic structure.**

**Proposition (conditional on the open recursion kernel of [the Habiro $q$-difference recursion for $c_k$](#prop:q-beta-c-k-recursion-from-habiro-q-difference); "$\mathrm{tr}_M$ ladder").**

For a typed braid $\beta$ and a Hecke irreducible representation $V_\lambda$ of $H_n(q)$, the Markov-traced character at single wrap admits a canonical factorisation in the substrate ladder variable $u_\lambda = b_\lambda\,\hbar_q^2$ (where $\hbar_q = (q-1)/q$):

$$
\boxed{
  \mathrm{tr}_M^{V_\lambda}(\beta)
   \;=\;
   \mathrm{Tr}\,\rho_\lambda(\beta) \cdot
   \cos\!\Bigl(\alpha_\lambda - \tfrac{b_\lambda \hbar_q^2}{2}\Bigr) \cdot
   \prod_{k \geq 2}\bigl(1 + c_k^{(\lambda)}\, u_\lambda^{\,k}\bigr),
}
$$

This matches the canonical $\mathfrak{Q}_\beta$ precision ladder ([categorical precision ladder](#prop:q-beta-categorical-precision-ladder)), where:

- $\rho_\lambda$ is the Hoefsmit seminormal representation of $H_n(q)$ on $V_\lambda$.
- $b_\lambda$ is the off-diagonal coupling of $\rho_\lambda(\sigma_i)$ in the standard-tableau basis. For $V_{(2,1)}$ of $H_3$, the scalar $b = \sqrt{q^4+q^2+1}/(q^2+1) = \sqrt{d_1 d_2 + 1}$ from [`prop:hoefsmit-V21-cos-symmetrization`](#prop:hoefsmit-V21-cos-symmetrization).
- $\alpha_\lambda$ is the single-wrap eigenphase on $V_\lambda$. The $\cos(\alpha_\lambda - b_\lambda\hbar_q^2/2)$ envelope carries the $N=1$ coupling $b_\lambda$.
- $c_k^{(\lambda)}$ are the rung coefficients of the ladder, representing the higher Ohtsuki invariants of the correction factor.

The factorisation defines the correction factor $F_\lambda := \mathrm{tr}_M^{V_\lambda}(\beta) / \mathrm{Tr}\,\rho_\lambda(\beta)$, which is valid wherever $\mathrm{Tr}\,\rho_\lambda(\beta) \neq 0$. The right-hand side depends on $\hbar_q$ only through $\hbar_q^2$, so the factorisation is even in $\hbar_q$ by construction. This evenness is a property of the ansatz, not a consequence of the bar involution: under $q \mapsto q^{-1}$ one has $\hbar_q \mapsto 1 - q = -q\,\hbar_q$, not $-\hbar_q$.

The rung coefficients are conjectured to be determined by the proved second-order $q$-difference (Hahn–Exton $q$-Bessel) recursion of [the Habiro $q$-difference recursion for $c_k$](#prop:q-beta-c-k-recursion-from-habiro-q-difference). The entire product forms the Taylor expansion of the exact finite Habiro sum, which the production system evaluates without truncation ([Habiro precision-ladder equivalence](#prop:habiro-precision-ladder-equivalence)).

| order | datum | status |
|------:|:---:|:---|
| $q = 1$ | $F_\lambda = 1$ | proved (permutation-matrix limit) |
| 1-d irreps | $F_\lambda \equiv 1$ | proved ($V_{(n)}, V_{(1^n)}$: $b_\lambda = 0$) |
| $N=1$ envelope | $\cos(\alpha - b\hbar_q^2/2)$, coupling $b$ | proved (Hoefsmit $\tilde f_1$ matrix element) |
| $k = 2$ | $c_2 = -1$, factor $(1 - b^2\hbar_q^4)$ | structural: the $N=2$ factor rewritten as $1 + c_2 u^2$; the factor itself is not derived |
| $k = 3$ | $c_3$ | open (recursion kernel open) |
| $k \geq 4$ | $c_k^{(\lambda)}$ | recursion-generated; kernel open |

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs, including real-valued physical observables, real-analytic bounds, transcendental constants, and numerical evaluation at the substrate parameter $q_0$. Any generic categorical or $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
