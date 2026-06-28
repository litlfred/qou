**Remark on Yekutieli's "max_grade".**
*The witness data
[`joint-tower-sdp-h6-h9.witness.json`](https://github.com/litlfred/qou/blob/claude/brane-tower-regularization-xTt8V/computations/joint-tower-sdp-h6-h9.witness.json)
records a per-atom `max_grade` field labelled* $k_{\max}$. *This number
is the maximal $k$ such that $T_w$ has nonzero $\lambda$-projection with
$\dim_q V_\lambda \geq 2$, which is **distinct** from $k_\star(T_w)$
defined above:*

| Symbol | Definition | Source |
|:---|:---|:---|
| $k_{\max}(K, q)$ (witness) | smallest $k$ s.t. $T_w$ uses no $\lambda \vdash k' > k$ with $d_\lambda \geq 2$ | $T_w$'s strand structure |
| $k_\star(T_w)$ (this prop) | max GB-depth of $\lambda \in \mathrm{supp}(T_w)$ | curvature-rank stratification |

*The two coincide whenever the GB-depth filtration is induced by the
strand-size filtration on partitions, but they **can differ** when a
small-$k$ partition $\lambda$ sits at large GB-depth or vice versa.*

**Computed for tritium.** A direct YSN/Hoefsmit
character computation
([`probe_tritium_k_star.py`](https://github.com/litlfred/qou/blob/claude/brane-tower-regularization-xTt8V/computations/probe_tritium_k_star.py))
gives $\chi_\lambda(\rho(\mathrm{T_w})) \neq 0$ for **every**
$\lambda \vdash 5$, so $\mathrm{supp}(\mathrm{T_w}) = \{\lambda : \lambda \vdash 5\}$
and $k_\star(\mathrm{T_w}) = \max_{\lambda \vdash 5} \mathrm{maxhook}(\lambda) = 5$.

**Three distinct "depths" — disambiguation.**
The literature and witness data conflate three structurally
different depth invariants of $T_w$:

| Depth | Formal definition | Tritium value |
|:---|:---|:---:|
| Coxeter length $\ell_{\max}(T_w)$ | longest reduced NF word in $S_{n_0}$ supporting $T_w$ | $9$ |
| q-Habiro depth $m_{\max}(T_w)$ | termination depth of cyclotomic expansion in $q$, $\leq \lceil\sqrt{2 \deg p}\rceil$ ([atomic Habiro expansion](#cor:habiro-expansion-atomic)) | $\approx 9$ |
| Partition GB-depth $k_\star(T_w)$ | $\max_\lambda \mathrm{maxhook}(\lambda)$ over $\mathrm{supp}(T_w)$ (this proposition) | $5$ |

The witness's $\mathtt{max\_grade} = 9$ matches both $\ell_{\max}$
and $m_{\max}$ for tritium (an accidental alignment of independent bounds:
$\deg p \approx 40$ and $\binom{5}{2} = 10$, not a structural relationship), but it does **not**
match $k_\star = 5$. This proposition's truncation depth is
$k_\star$, not $\ell_{\max}$ or $m_{\max}$ — these are independent
structural quantities, all bounded but not equal.

**Structural upper bound.** For any $T_w \in H_{n_0}(q)$,
$k_\star(T_w) \leq n_0$ because every partition $\lambda \vdash n_0$
has $\mathrm{maxhook}(\lambda) \leq n_0$. The witness's $k_{\max}$ is
**not** so bounded — it is the Coxeter-length filtration, which can
reach $\binom{n_0}{2}$ (the longest element in $S_{n_0}$). Identifying
the two is the strand-padding artifact: padding $T_w$'s NF to longer
Coxeter words does not change partition support, but does inflate
$k_{\max}$ in the witness.

**Empirical implication.**
*Under this proposition, the structural truncation depth for tritium
is $k_\star(\mathrm{T_w}) = 5$ (computed; full partition support of
$\lambda \vdash 5$), and for D and ${}^3\mathrm{He}$ at most
$k_\star \leq 3$ (since they live in $H_3$). The uniform-$k$ probe
([`probe_phiq_uniform_k.py`](https://github.com/litlfred/qou/blob/claude/brane-tower-regularization-xTt8V/computations/probe_phiq_uniform_k.py))
shows the Frobenius-paired truncation is far from numerically closed:
at $k = 2$ subtractive form, D errs $-22\%$, T errs $-39\%$,
${}^3\mathrm{He}$ overshoots $+134\%$; at $k = 5$ (the
structural truncation for tritium), the absolute formula errs by
$\sim 70000\%$. The Frobenius-paired equality
$\mathrm{tr}_M(\Phi_q \cdot T_w) = \mathrm{tr}_M(\Phi_q^{[\leq k_\star]} \cdot T_w)$
is a **categorical identity**, not a real-valued numerical identity;
the real-valued mass at $|\hat V|\approx 1$ requires the open
$z$-Habiro uniform bound to convert categorical equality into
numerical equality
([brane tower in $z$-Habiro](#conj:brane-tower-z-habiro)).*
