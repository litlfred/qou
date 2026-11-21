*Let $R$ be the categorical coefficient ring with $q \in R$ generic, and let $\{b_i\}$ be the [normal-form basis](#def:hecke-normal-form) of the Iwahori-Hecke algebra $H_n(q)$. The data of the statement are:*

- *a finite family $\mathcal{O}$ of knot operators $o = T_{m,m'}$, each carrying a braid word $\beta(o) \in B_n$, which acts in $H_n(q)$ through $\sigma_i \mapsto \sigma_i$;*
- *a cost $t_o \in R$ for each operator $o \in \mathcal{O}$;*
- *a confinement target $T \in H_n(q)$ with normal form $\mathrm{NF}(T) = \sum_i c_i \, b_i$.*

*From these data define:*

- *the [Frobenius Gram matrix](#prop:frobenius-gram-matrix) $G_{ij} = \mathrm{tr}_M(b_i \, b_j)$ and its Moore–Penrose pseudo-inverse $G^{+}$, the inverse of the trace form on the quotient $H_n(q)/\mathrm{rad}$ by its radical; when $G$ is non-degenerate, $G^{+} = G^{-1}$;*
- *the supply matrix $S$, whose column $o$ is the coefficient vector of $\beta(o)$ in the normal-form basis, $S_{i,o} = [b_i]\,\mathrm{NF}(\beta(o))$;*
- *the demand vector $n_T$, with $n_T^{i} = \max(0, -c_i)$, the magnitudes of the negative normal-form coefficients of $T$ ([demand profile](#def:demand-profile)).*

*The selection of knot operators producing $T$ is the linear program*

$$
  \min_{\substack{x \in R^{\mathcal{O}},\; x \geq 0 \\ G^{+} S x \;\geq\; n_T}}
  \;\;\sum_{o \in \mathcal{O}} t_o \, x_o .
$$

*Given a primal optimum and a dual optimum with equal objective values (strong duality, assumed here), complementary slackness holds, and the LP dual variables $y^* \geq 0$ supply the shadow prices of the demand constraints and the active set $\{o : x_o^* > 0\}$ identifying which knot operators contribute to the bound state. A target with no negative normal-form coefficient has $n_T = 0$ and is met by the empty selection $x = 0$.*

The statement holds for every choice of the family $\mathcal{O}$, its braid words and the cost $t$; these enter only through $S$ and the objective. The LP is feasible if and only if $n_T$ is dominated componentwise by some non-negative combination of the columns of $G^{+} S$. The dual solution isolates the minimum-cost generators.
