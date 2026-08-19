*Proof.*
Whitehead's lemma for semisimple algebras over a field of
characteristic zero: every Hochschild cocycle in degree $k \geq 1$ is
a coboundary, so $\mathrm{HH}^k = 0$.  Over a commutative ring $R$ the
same conclusion holds whenever $A$ is separable / semisimple.  The
spectral sequence $E_r^{p, q} \Rightarrow \mathrm{HH}^{p+q}$ then has
only $E_\infty^{p, 0}$ surviving with $p + 0 = 0$, giving
$E_\infty^{0, 0} = \mathrm{HH}^0 = Z(A)$. $\square$

**Corollary (mass functional is a q-deformed Wedderburn-weighted centre projection).**
*The categorical mass functional pairs the Frobenius integral
$\int_A : A \to R$ with the centre via the Wedderburn decomposition
([categorical mass, Markov](#prop:categorical-mass-markov)):*

$$
  \mathfrak{m}_{q,\mathcal{K}}
  \;=\; \sum_{\lambda \,\vdash\, n} w_\lambda(q) \cdot \frac{\chi_\lambda(\rho(\beta_\mathcal{K}))}{\dim_q V_\lambda},
  \qquad w_\lambda(q) = \frac{\dim_q^2 V_\lambda}{[n]_q!},
$$

*q-deformed Wedderburn weights $w_\lambda(q)$, bounded but
$\sum w_\lambda(q) \neq 1$ at $q \neq 1$ in general (cf.
[`prop:plancherel-weight-boundedness`](#prop:plancherel-weight-boundedness)
for the classical Plancherel measure $w_\lambda(1) = (\dim V_\lambda)^2/n!$
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
*categorical derivation steps need only enumerate central idempotents $e_\lambda$,
compute their GB-depth, evaluate $\chi_\lambda$ via Hoefsmit seminormal
form ([Hoefsmit pipeline](#conj:hoefsmit-scattering-pipeline)), and
sum $\sum_\lambda w_\lambda \cdot \chi_\lambda(\beta) / \dim_q V_\lambda$
binning by $\mathrm{depth}(\lambda)$.  No higher-page differentials
$d_r$ ($r \geq 1$) need ever be computed — they all vanish.*

> **Gap (2026-08-16).** The step above reads a grading of the **centre** by
> *partition* depth off a proposition that stratifies $H_n(R,q)$ by the
> curvature rank of **words**. That identification is not stated in the cited
> proposition, and the three readings of $J^\bullet$ present in the corpus are
> each excluded: the ideal-power reading is provably $\bot$ above degree $0$
> (`QOU.BraidKnot.WordFiltration.map_pow_eq_bot`); the Coxeter-length reading
> fails a dimension count at $n \leq 3$; and the rewrite-depth reading is
> identically zero once `def:hecke-normal-form` fixes $T_w$ as the unique
> normal-form basis indexed by $S_n$. Analysis:
> [`docs/audits/2026-08-16-three-gb-filtrations-one-name.md`](../../../docs/audits/2026-08-16-three-gb-filtrations-one-name.md).
> **Not claimed:** that this block's conclusion is false — only that the step
> it rests on is unestablished, and that the obvious ways to establish it do
> not work.
