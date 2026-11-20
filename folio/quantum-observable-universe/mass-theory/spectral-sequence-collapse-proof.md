*Proof.*
A separable algebra has $\mathrm{HH}^k(A, M) = 0$ for $k \geq 1$ and
every bimodule $M$ (Hochschild 1945; this is the associative analogue
of Whitehead's lemma, not Whitehead's lemma itself).  A semisimple
algebra over a field of characteristic zero is separable.  The
spectral sequence $E_r^{p, q} \Rightarrow \mathrm{HH}^{p+q}$ then has
$E_\infty^{p,q} = 0$ for $p + q \geq 1$, and $E_\infty^{0, 0} =
\mathrm{HH}^0 = Z(A)$. Nothing here forces the differentials $d_r$ to
vanish. $\square$

**Corollary (mass functional is a q-deformed Wedderburn-weighted centre projection).**
*The categorical mass functional pairs the Frobenius integral
$\int_A : A \to R$ with the centre via the Wedderburn decomposition
([categorical mass, Markov](#prop:categorical-mass-markov)):*

$$
  \mathfrak{m}_{q,\mathcal{K}}
  \;=\; \sum_{\lambda \,\vdash\, n} w_\lambda(q) \cdot \frac{\chi_\lambda(\rho(\beta_\mathcal{K}))}{\dim_q V_\lambda},
  \qquad w_\lambda(q) = \frac{\dim_q^2 V_\lambda}{[n]_q!},
$$

*The $q$-deformed Wedderburn weights $w_\lambda(q)$ are bounded, but
$\sum w_\lambda(q) \neq 1$ at $q \neq 1$ in general (cf.
[Plancherel weights define a probability distribution: $\sum_\lambda w_\lambda = 1$, $0 \leq w_\lambda \leq 1$](#prop:plancherel-weight-boundedness)
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

> **Refuted on the centre, scope (b).** The sentence above
> transports the annihilator duality from $A$ to the *strata*, and the
> paragraph below reads those strata off the central idempotents
> $e_\lambda$. On that basis the pairing is **diagonal**, not
> anti-diagonal, so distinct strata pair to **zero**: for any linear
> functional $\varphi$,
> $\varphi(e_\lambda e_\mu) = \varphi(\delta_{\lambda\mu} e_\lambda)$.
> Measured exactly in $\mathbb{Q}(q)$ at $n = 3$ on the corpus's own
> idempotents — all six off-diagonal entries identically $0$, diagonal
> $\mathrm{diag}(\tau(e_\lambda))$ nonzero, completeness self-test
> $\sum_\lambda \tau(e_\lambda) = 1$
> ([`centre_frobenius_pairing_is_diagonal_probe.py`](../../../computations/probes/centre_frobenius_pairing_is_diagonal_probe.py)).
> So each stratum is **self**-dual and the annihilator of a stratum
> within $Z$ is the span of the *complementary* idempotents — a set
> complement, not a rank-reindexed stratum. The asserted pairing is
> identically zero exactly where it claims to be perfect, whenever
> $\ell \neq N - \ell$.
>
> **Scope (b)** rests on a proved invariant — mutual annihilation of
> distinct central primitive idempotents — which holds for *every*
> linear functional and every $n$. So no choice of filtration and no
> choice of Frobenius form restores a cross-stratum pairing here, and
> **supplying the missing $J^\bullet$ bridge would not repair it**:
> this defect is independent of the Gap note below.
>
> **Not refuted:** $(J^\ell)^\perp = J^{N - \ell}$ as a statement about
> the filtration of $A$ itself, which is a different claim and is
> untouched here; and the *Practical consequence* below, which uses the
> Wedderburn sum and not this duality. Same defect as
> [Partial argument for the stratified quantum dilogarithm](#rem:quantum-dilogarithm-stratified-partial-argument)
> Step 1.

**Practical consequence.**
*categorical derivation steps need only enumerate central idempotents $e_\lambda$,
compute their GB-depth, evaluate $\chi_\lambda$ via Hoefsmit seminormal
form ([Hoefsmit pipeline](#conj:hoefsmit-scattering-pipeline)), and
sum $\sum_\lambda w_\lambda \cdot \chi_\lambda(\beta) / \dim_q V_\lambda$
binning by $\mathrm{depth}(\lambda)$.  This uses only the centre
$Z(A) = E_\infty^{0,0}$, so no page of the spectral sequence is
needed. That is not because the differentials $d_r$ vanish, which
is not shown.*

> **Gap.** The step above reads a grading of the **centre** by
> *partition* depth off a proposition that stratifies $H_n(R,q)$ by the
> curvature rank of **words**. That identification is not stated in the cited
> proposition, and the three readings of $J^\bullet$ present in the corpus are
> each excluded: the ideal-power reading is provably $\bot$ above degree $0$
>; the Coxeter-length reading
> fails a dimension count at $n \leq 3$; and the rewrite-depth reading is
> identically zero once `def:hecke-normal-form` fixes $T_w$ as the unique
> normal-form basis indexed by $S_n$.
> **Not claimed:** that this block's conclusion is false — only that the step
> it rests on is unestablished, and that the obvious ways to establish it do
> not work.
