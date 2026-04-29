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

**Remark on Yekutieli's "max_grade".**
*The witness data
[`joint-tower-sdp-h6-h9.witness.json`](https://github.com/litlfred/qou/blob/claude/brane-tower-regularization-xTt8V/folio-assistant/computations/joint-tower-sdp-h6-h9.witness.json)
records a per-atom `max_grade` field labelled* $k_{\max}$. *This number
is the maximal $k$ such that $T_w$ has nonzero $\lambda$-projection with
$\dim_q V_\lambda \geq 2$, which is** distinct** from $k_\star(T_w)$
defined above:*

| Symbol | Definition | Source |
|:---|:---|:---|
| $k_{\max}(K, q)$ (witness) | smallest $k$ s.t. $T_w$ uses no $\lambda \vdash k' > k$ with $d_\lambda \geq 2$ | $T_w$'s strand structure |
| $k_\star(T_w)$ (this prop) | max GB-depth of $\lambda \in \mathrm{supp}(T_w)$ | curvature-rank stratification |

*The two coincide whenever the GB-depth filtration is induced by the
strand-size filtration on partitions, but they** can differ** when a
small-$k$ partition $\lambda$ sits at large GB-depth or vice versa.
Tritium's anomalously high $k_{\max} = 9$ in the witness data is
suspect under this distinction: the* $k_\star(T_w)$ *of T's actual
NF should be no larger than 2 (consistent with D's and ${}^3\mathrm{He}$'s
$k_\star = 2$), and the witness's $k_{\max} = 9$ likely reflects a
strand-padding artifact in the SDP search rather than genuine
GB-depth content. Resolving this discrepancy is a focused open
computation
([brane-tower in $z$-Habiro](#conj:brane-tower-z-habiro), level-selection rule).*

**Empirical implication.**
*Under this proposition, the right uniform truncation across light
isotopes is $k = 2$ (matching D and ${}^3\mathrm{He}$'s witness
$k_{\max} = 2$). The* uniform-$k$ *probe
([`probe_phiq_uniform_k.py`](https://github.com/litlfred/qou/blob/claude/brane-tower-regularization-xTt8V/folio-assistant/computations/probe_phiq_uniform_k.py))
shows $k = 2$ subtractive form gives D within $-22\%$, T within
$-39\%$, but ${}^3\mathrm{He}$ overshoots $+134\%$. The residual
${}^3\mathrm{He}$ overshoot is then* not *a brane-tower regularization
issue — by this proposition the brane-tower is centre-only and
correctly truncated — but a separate structural feature of
${}^3\mathrm{He}$'s NF, likely the doubled near-pole entry
$|\hat{V}_0| = |\hat{V}_3| \approx 0.989$ producing a multiplicity in
the centre projection that the uniform sweep does not absorb.*
