The Hecke-algebra GNS data
([algebraic GNS embedding](#prop:algebraic-gns-embedding))
forms a non-commutative probability space in Voiculescu's sense
[`biane1998`]: a unital $*$-algebra equipped with a tracial state.
Under this reading, every QOU-internal computation involving the
Markov trace has a probabilistic translation.

**The dictionary.**

| Classical probability | QOU non-commutative analogue |
|---|---|
| Sample space $(\Omega, \mathcal{F}, P)$ | $(H_\infty(q), \mathrm{tr}_M)$ — type II$_1$ factor with faithful trace |
| Random variable $X \colon \Omega \to \mathbb{R}$ | Braid transfer matrix $\sigma_i \in H_\infty(q)$ |
| Expectation $\mathbb{E}[X] = \int X\, dP$ | $\mathrm{tr}_M(\sigma_i)$ |
| Moment $\mathbb{E}[X^k]$ | $\mathrm{tr}_M(\sigma_i^k)$ |
| Joint moment $\mathbb{E}[X_1 X_2 \cdots X_k]$ | $\mathrm{tr}_M(\sigma_{i_1} \sigma_{i_2} \cdots \sigma_{i_k}) = J_K(q)$ — Jones polynomial of the closed braid $K$ |
| Independence | Voiculescu freeness (Jucys–Murphy elements at $q = 1$) |
| Distribution / CDF | Linear functional $p \mapsto \mathrm{tr}_M(p(\sigma_i))$ on polynomials |
| Cumulants | Free cumulants on the lattice of non-crossing partitions (Speicher) |
| Gaussian attractor of the CLT | q-Gaussian attractor of the q-CLT [`marsh2006`] |
| Variance | Second free cumulant $\kappa_2$; bounded by Féray–Méliot $O(1/\sqrt{n-3})$ for q-Plancherel |
| Free entropy $\chi$ (Voiculescu) | $\log$-asymptotic of moments — same form as Kashaev hyperbolic volume $\mathrm{Vol}(K) = 2\pi \lim_{N \to \infty} \log\lvert J_N(K)\rvert / N$ |

**Three structural facts that follow.**

1. **Knot theory is the moment theory of QOU's non-commutative
   probability space.** Every closed-braid knot invariant
   ($J_K(q)$, colored Jones, HOMFLY, Khovanov categorifications) is
   a specific joint moment of transfer matrices under $\mathrm{tr}_M$.
   Knot tables are joint-moment tables; the Kashaev volume conjecture
   is a free-entropy-style log-asymptotic of moments.

2. **Wedderburn idempotents are events.** The central projectors
   $e_\lambda$ satisfy $1 = \sum_\lambda e_\lambda$ and
   $e_\lambda^2 = e_\lambda$, $e_\lambda e_\mu = 0$ for $\lambda \neq \mu$
   — they partition the unit into a non-commutative analogue of
   measurable events. The Plancherel measure $\tilde w_\lambda =
   \mathrm{tr}_M(e_\lambda)$ assigns probability mass to each event:
   $\mathrm{tr}_M(x) = \sum_\lambda \tilde w_\lambda \cdot \chi_\lambda(x)$
   is the **law of total probability** in this space.

3. **Jucys–Murphy elements are commuting random variables.** The
   elements
   $J_k = \sigma_{k-1} \sigma_{k-2} \cdots \sigma_1 \sigma_1 \cdots \sigma_{k-2} \sigma_{k-1}$
   commute pairwise and generate the maximal abelian subalgebra
   (Gelfand–Tsetlin). Biane proved that in the large-$n$ limit at
   $q = 1$, suitably normalised $J_k$'s become *free random
   variables* with semicircle distribution
   [`biane1998`]; the q-deformed version (Féray–Méliot 2010, q-CLT
   below) replaces semicircle with the q-Gaussian
   [`marsh2006`].

**This reading is not metaphor.** It is the precise statement that
the Hecke algebra under the Markov trace is a non-commutative
$(W^*, \mathrm{tr})$ probability space in the sense of Voiculescu,
and every theorem about such spaces applies directly to QOU. The
q-CLT below
([q-CLT for Hecke transfer matrices](#conj:q-clt-non-commutative))
makes this explicit by stating the central limit theorem in the
QOU setting.

**Why this is useful regardless of CFS.** Even if the
$\mu_{\mathrm{arch}}$ Lagrangian-match conjecture fails, the non-comm
probability framework supplies QOU with:
- A rigorous bridge from discrete algebra to macroscopic continuity
  via the q-CLT (the substrate explains why measurements register
  smooth distributions).
- A justified locality / non-locality reconciliation
  ([trace locality vs GS non-locality](#prop:trace-locality-meets-gs-non-locality)).
- A finite, convergent integration over the brane tower
  ([brane-tower q-Laplacian decay](#prop:brane-tower-q-laplacian-decay)).
- A direct knot-invariant ↔ free-probability dictionary unlocking
  results from random matrix theory, free probability, and
  asymptotic representation theory.

These are positive QOU results that do not depend on whether any
Finster-style continuum lift exists.
