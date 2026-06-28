**Proposition (categorical $\Phi_q$ truncation depth).**

*Let $\mathfrak{H}$ be a confined particle with Hecke NF $T_w \in H_n(R, q)$
([Hecke normal form](#def:hecke-normal-form)). Let
$\mathrm{supp}(T_w) = \{\lambda \vdash k : \langle T_w, e_\lambda \rangle \neq 0\}$
be the set of central idempotents on which $T_w$ has nonzero
projection, and define*

$$
  k_\star(T_w) \;:=\; \max_{\lambda \in \mathrm{supp}(T_w)} \mathrm{depth}_{\mathrm{GB}}(\lambda),
$$

*the **NF-support depth** in the GB-curvature-rank stratification
([curvature-rank stratification](#prop:curvature-rank-gb-stratification)).
Then the categorical brane-tower contribution to the mass functional
is the finite sum*

$$
  \mathfrak{m}^{\mathrm{tower}}_{q,\mathcal{K}}(T_w)
  \;=\;
  \sum_{k=0}^{k_\star(T_w)}
    \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}(T_w),
$$

*where $\mathfrak{m}^{(k)}_{q,\mathcal{K}}$ is the depth-$k$ centre
projection and $\alpha_k$ are the curvature-rank coefficients
([unified mass formula](#prop:unified-curvature-rank-mass-formula)).
Equivalently, expressed via the analytic dilogarithm,*

$$
  \mathfrak{m}^{\mathrm{tower}}_{q,\mathcal{K}}(T_w)
  \;=\;
  \sum_{i} \Phi_q^{[\leq k_\star(T_w)]}(z_i)
  \;=\;
  \sum_i \prod_{j=1}^{k_\star(T_w)} (1 - q^{-j} z_i)^{-1},
$$

*with the truncation depth $k_\star(T_w)$ structurally determined by
$T_w$'s NF support — not chosen externally.*

**Corollary (any deeper truncation is categorically equivalent).**
*For any $k \geq k_\star(T_w)$,*

$$
  \sum_i \Phi_q^{[\leq k]}(z_i)
  \;=\;
  \sum_i \Phi_q^{[\leq k_\star(T_w)]}(z_i) \mod E_\infty^{\geq 1, *},
$$

*and the right-hand side already vanishes on $E_\infty^{\geq 1, *}$ by
prop:spectral-sequence-collapse. Therefore truncation at any
$k \geq k_\star(T_w)$ gives the same categorical answer; the
analytic divergence at $|\hat{V}|\approx 1$ is a spurious side-effect
of representing the finite centre-projection sum by an infinite
product.*
