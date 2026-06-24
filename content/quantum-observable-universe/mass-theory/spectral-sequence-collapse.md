**Proposition (cohomology vanishing collapses the GB spectral sequence).**
*Let $A = H_n(R, q)$ for $R$ a commutative ring with $q \in R$ such
that $A$ is semisimple
([three-parameters-wedderburn](#prop:three-parameters-wedderburn)).
Then Hochschild cohomology vanishes in positive degrees:*

$$
  \mathrm{HH}^k(A,\, A) \;=\; 0 \quad \text{for all } k \geq 1.
$$

*Consequently the GB filtration spectral sequence
([GB spectral sequence](#prop:gb-spectral-sequence)) collapses at
$E_1$, with all contributions concentrated in*

$$
  E_\infty^{0, *} \;=\; \mathrm{HH}^0(A) \;=\; Z(A) \;=\; \bigoplus_{\lambda \,\vdash\, n} R \cdot e_\lambda,
$$

*the centre, a direct sum of central idempotents indexed by partitions
of $n$.*

**Corollary (mass functional is a q-deformed Wedderburn-weighted centre projection).**
*The categorical mass functional pairs the Frobenius integral
$\int_A : A \to R$ with the centre via the Wedderburn decomposition
([categorical mass, Markov](#prop:categorical-mass-markov)):*

$$
  \mathfrak{m}_{q,\mathcal{K}}
  \;=\; \sum_{\lambda \,\vdash\, n} \tilde w_\lambda \cdot \frac{\chi_\lambda(\rho(\beta_\mathcal{K}))}{\dim_q V_\lambda},
  \qquad \tilde w_\lambda = \frac{\dim_q^2 V_\lambda}{[n]_q!},
$$

*q-deformed Wedderburn weights $\tilde w_\lambda$, bounded but
$\sum \tilde w_\lambda \neq 1$ at $q \neq 1$ in general (cf.
[`prop:plancherel-weight-boundedness`](#prop:plancherel-weight-boundedness)
for the classical Plancherel measure $w_\lambda = (\dim V_\lambda)^2/n!$
that does sum to $1$).  Binning by GB-depth
([curvature-rank stratification](#prop:curvature-rank-gb-stratification))
gives the curvature-rank decomposition
$\mathfrak{m}_{q,\mathcal{K}} = \sum_k \alpha_k \cdot
\mathfrak{m}^{(k)}_{q,\mathcal{K}}(1)$
([unified mass formula](#prop:unified-curvature-rank-mass-formula)).*

**Frobenius duality of strata.**
*The Frobenius pairing $\langle a, b \rangle = \int_A a \cdot b$ gives
a self-duality $A \cong A^{\vee}$
([Yekutieli rigidity](#prop:vol-through-tau)).
Under this duality the GB filtration
$J^0 \supset J^1 \supset \cdots \supset J^N$ maps to its annihilator
filtration*

$$
  (J^\ell)^\perp \;=\; \{a : {\textstyle\int_A}\, a \cdot J^\ell = 0\} \;=\; J^{N - \ell}.
$$

*This is **Poincaré duality of curvature-rank strata**: rank-$\ell$
contributions pair with rank-$(N - \ell)$ contributions under the
Frobenius integral.  The chirality stratum (S-anti-invariant rank
$\geq 2$) is self-dual under combined S-reversal and rank inversion.*

**Practical consequence.**
*Numerical pipelines need only enumerate central idempotents $e_\lambda$,
compute their GB-depth, evaluate $\chi_\lambda$ via Hoefsmit seminormal
form ([Hoefsmit pipeline](#conj:hoefsmit-scattering-pipeline)), and
sum $\sum_\lambda w_\lambda \cdot \chi_\lambda(\beta) / \dim_q V_\lambda$
binning by $\mathrm{depth}(\lambda)$.  No higher-page differentials
$d_r$ ($r \geq 1$) need ever be computed — they all vanish.*
