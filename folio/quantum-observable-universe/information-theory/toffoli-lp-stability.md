Let $T_q \in H_3(q)$ be the $q$-Toffoli element, realized as the $3$-strand braid word with traced volume matrix $M(q)$. Let $G = (\mathrm{tr}_M(b_i \cdot b_j))_{i,j}$ be the Gram matrix of the normal-form basis. Express the $q$-Toffoli in normal-form coordinates as $T_q = \sum_{i=1}^{6} t_i(q) \, b_i$. Then:

1. **(Stability region.)** Under the canonical convention $z_D = q^3/(q^2+1)$ the amplitudes the Toffoli construction produces are
$$
  P_{6,6} = \frac{(q^4+1)(q^4+q^2+2)}{4q(q^2+1)^2},
  \qquad
  P_{7,7} = \frac{q^3(q^4+1)}{(q^2+1)^2},
$$
$$
  P_{7,6} = -\frac{(q-1)(q+1)(q^6+q^4+2q^2+1)}{2q(q^2+1)^2},
  \qquad
  P_{6,7} = \frac{(q-1)(q+1)(2q^6+q^4+q^2+1)}{2q(q^2+1)^2}.
$$
The two diagonal amplitudes are strictly positive on $q > 0$; each off-diagonal amplitude has exactly one zero there, at $q = 1$, since its sextic factor is positive for every real $q$. So the derived family has **one** operator zero on $(0,\infty)$, not three, and $P_{7,6} < 0$ for every $q > 1$ — including the aether parameter. Two values associated with alternative normalizations,
$$
  q_\star \,=\, 1/\varphi^2 \,=\, (3 - \sqrt{5})/2 \,\approx\, 0.3820,
  \qquad
  q_\Phi \,\approx\, 0.4656,
$$
are the roots of retired expressions: $q_\star$ is the root of the convention-$C$ diagonal $(q + \sqrt q - 1)/(q+1)$, and $q_\Phi$ is the root of the closed form $\Phi$, which does not lie in the image of the Toffoli construction under any indexing or convention ([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)).

2. **(The operator threshold.)** The derived family has a single threshold on $(0,\infty)$:
See [the zero-locus comparison table](#tbl:toffoli-lp-stability-table1-data).
At $q = 1$ both off-diagonal amplitudes vanish through their common factor $(q-1)$: the classical reversible Toffoli has trivial off-diagonal amplitude. Neither diagonal amplitude vanishes anywhere on $q > 0$, and neither off-diagonal sextic factor has a positive real root, so $q = 1$ is the only threshold. By contrast, $q_\star$ marks where the convention-$C$ diagonal $(q + \sqrt q - 1)/(q+1)$ vanishes, and $q_\Phi$ is a root of $\Phi$.

3. **(Dual shadow prices.)** On a non-degenerate subspace of $G(q)$ for $q > 1$, LP duality bounds the shadow prices $y_i^*(q)$ by
$$
  |y_i^*(q)| \leq \kappa(\mathrm{G}(q)) \cdot \|t(q)\|,
$$
where $\kappa(\mathrm{G}(q)) = \lambda_{\max}(G)/|\lambda_{\min}(G)|$. Under the canonical convention $z_D = q^3/(q^2+1)$, however, the Markov–Gram form is **singular** on the full six-dimensional normal-form span, so $\lambda_{\max}/|\lambda_{\min}|$ is infinite on the ambient space and a finite condition-number bound requires descending to the Temperley–Lieb quotient modulo the trace radical. (An earlier finite estimate $\kappa(G(q_0)) \approx 3.03$ arose from an unreduced naive length-rule trace $\mathrm{tr}_M(T_w) = z^{\ell(w)}$ under convention $C$ and does not apply to the canonical Markov trace.)

4. **(Physical-aether stability — the uniform positivity does not hold as stated.)** At $q_0 \approx 1.110$, under convention $D$:
$$
  P_{7,7}(q_0) \,\approx\, 0.6912,
  \qquad
  P_{7,6}(q_0) \,\approx\, -0.1438.
$$
The diagonal is strictly positive; the target-flip amplitude is **negative**, and remains negative throughout $q > 1$ (whereas convention $C$ and $\Phi$ gave $0.5514$ and $+0.0495$, respectively).

An argument running through simultaneous positivity of *both* amplitudes therefore does not close on the derived family. Reducing feasibility of $G\vec t(q) \geq 0$ to positivity of $P_{7,7}(q)\,W_{\mathrm{std}}(q)$ multiplied by a sign factor from the flip amplitude leaves that sign relation unproved, <!-- literal-source: closed-form rational evaluation (q_0^7 + q_0^3)/(q_0^4 + 4*q_0^2 + 1) = 0.4624 --> though the first factor itself satisfies $P_{7,7}(q_0)\,W_{\mathrm{std}}(q_0) \approx 0.4624 > 0$.

**Direct evaluation of the cone condition.** Rather than relying on that reduction, one can construct $T_q$ and evaluate $G\vec t(q_0) \geq 0$ directly. Since the crossing coefficients satisfy $C_{ij} = c_j\sigma_i + d_j$ and the chain recursion reduces $(a\sigma+b)(c\sigma+d)$ via $\sigma^2 = \hbar_\times\sigma + 1$, the all-proton ordering yields
$$
  T_q \;=\; \sigma_1 \;+\; \hbar_\times\,\sigma_0\sigma_1,
  \qquad \hbar_\times = q - q^{-1}.
$$
Against the canonical Markov–Gram matrix, every component of $G\vec t(q_0)$ is strictly positive across all eight strand-type orderings. Thus the aether parameter satisfies the stated LP condition.

**Two structural qualifications.** First, the Gram matrix is entrywise non-negative, as is $\vec t$ for the all-proton ordering, so for $2$ of the $8$ orderings positivity is forced by entry signs alone while the remaining $6$ involve genuine sign interplay. Second, and more consequentially, $\vec t$ acquires a negative component precisely when $\hbar_\times < 0$, namely on $0 < q < 1$ — the *opposite* side of $q = 1$ from where $P_{7,6}$ is negative. The amplitude sign and the cone condition therefore select opposite regimes.

**Structural sign inversion.** Since $\hbar_\times = (q-1)(q+1)/q$, the flip amplitude factors as
$$
  P_{7,6}(q) \;=\; -\,\hbar_\times\,\cdot\,\frac{S(q)}{2(q^2+1)^2},
  \qquad S(q) = q^6+q^4+2q^2+1,
$$
where $S$ has no real root and $(q^2+1)^2 > 0$, so the cofactor is strictly positive on all of $\mathbb{R}$. The flip amplitude is therefore $-\hbar_\times$ times a positive rational function, whereas the cone coordinate is $+\hbar_\times$, giving $P_{7,6}(q)\,\hbar_\times(q) \leq 0$ for every $q > 0$.

Consequently, no reduction in which the cone condition *inherits* the sign of $P_{7,6}$ can hold at any anchor, because the two carry opposite signs of the same factor $(q - 1)$. Only a relation involving $-P_{7,6}$ could align their signs on $(0,\infty) \setminus \{1\}$.

Since $G\vec t(q_0) > 0$ holds directly, no LP-instability arises at $q_0$, and the downstream statement that $\{q\text{-Toffoli}, H\}$ generates universal reversible computation on the Reeb bundles remains unobstructed.

**Global sign and zero structure on $(0,\infty)$.** None of these properties depends on evaluating at a single numerical anchor:

| Property | Domain / algebraic mechanism |
|---|---|
| $P_{7,7} > 0$, no positive root | $q > 0$, numerator $q^3(q^4+1) > 0$ |
| $P_{6,6} > 0$, no positive root | $q > 0$, numerator $(q^4+1)(q^4+q^2+2) > 0$ |
| $P_{7,6}$'s only positive zero is $q = 1$ | $q > 0$, sextic factor $S(q) > 0$ |
| $P_{7,6} < 0$ on the aether side | $q > 1$ |
| $P_{7,6} > 0$ | $0 < q < 1$ |
| $P_{6,7} + P_{7,6} = q(q-1)^2(q+1)^2/2(q^2+1)$ | all $q \neq 0$ (antisymmetry defect) |
| the flip channel is **not** antisymmetric | $q > 0,\ q \neq 1$ |
| $W_{\mathrm{std}} > 0$ and $P_{7,7}W_{\mathrm{std}} > 0$ | $q > 0$ |
| $\mathrm{sign}\,P_{7,6} = -\mathrm{sign}\,\hbar_\times$ | $q > 0$, $P_{7,6}\,\hbar_\times \leq 0$ |

The antisymmetry defect is exact and vanishes on $(0,\infty)$ only at $q = 1$, so reversing the crossing negates the amplitude only in the classical limit.

**Zero-set obstruction to monomial reduction.** Any reduction of the cone condition to a monomial product in $P_{7,7}W_{\mathrm{std}}$ and $P_{7,6}$ forces the cone condition's zero locus into the union of the factors' zero loci. With the symbolic Markov--Gram matrix, the cone condition reduces to a **single** nontrivial constraint, indexed by the longest word $\sigma_0\sigma_1\sigma_0$:

$$
  (G\vec t)_5 \;=\; \frac{q^{10}+q^{6}-q^{4}+q^{2}-1}{(q^2+1)^2}
$$

| quantity | zeros on $q > 0$ |
|---|---|
| the cone constraint $(G\vec t)_5$ <!-- literal-source: unique positive real root of polynomial cone constraint (G*t)_5(q) = 0 --> | one, at $q_c \approx 0.8944802929$ |
| $P_{7,7}W_{\mathrm{std}} = (q^7+q^3)/(q^4+4q^2+1)$ | **none** — strictly positive |
| $P_{7,6}$ | one, at $q = 1$ |

Since $q_c \neq 1$, neither factor accounts for the cone's zero, ruling out any single-product reduction. The numerator is irreducible over $\mathbb{Q}$ and has a unique positive real root; even purely rationally, across $[1/2, 9/10]$ the cone constraint changes sign while both candidate factors remain strictly positive at each endpoint.

**Quadratic relation in the amplitude subring.** The eight amplitudes generate the full rational function field $\mathbb{Q}(q)$ — four already reconstruct $q$ via $M_{33}/M_{44} = q^4$ and $P_{7,7}/M_{00} = q^6$ — so unrestricted rational dependence is automatic, whereas polynomial dependence at bounded degree is restrictive. Over the common denominator $q^6(q^2+1)^4$ the ambient space of numerators is $21$-dimensional, and the degree-$2$ span of the amplitudes has rank $15$, a proper subspace of **codimension $6$**. The cone constraint lies in this subspace, and four amplitudes already suffice:

$$
  (G\vec t)_5 \;=\; -\tfrac{4}{9}
  \;+\; \tfrac{5}{36}M_{00}^2 \;-\; \tfrac{20}{3}M_{00}M_{33} \;-\; \tfrac{10}{9}M_{00}M_{44} \;+\; \tfrac{5}{18}M_{00}P_{7,7}
  \;-\; \tfrac{28}{9}M_{33}^2 \;+\; \tfrac{20}{3}M_{33}M_{44} \;+\; \tfrac{38}{9}M_{33}P_{7,7} \;+\; \tfrac{20}{9}M_{44}^2 \;+\; \tfrac{5}{36}P_{7,7}^2
$$

With the positive common denominator carrying the sign directly from the numerator to the constraint, only addition and multiplication appear, with no division by an amplitude. The *cross* terms are essential: the span of the amplitudes and their pure squares has rank $14$ and does **not** contain the constraint.

Whereas a monomial vanishes only where a factor vanishes, a degree-$2$ polynomial can vanish by cancellation between products where none of its terms vanishes, which is the exact mechanism producing the root at $q_c$. Whether any member of the resulting one-parameter quadratic family admits a direct Hecke-algebraic interpretation is unresolved.

**Canonical polynomial form in Markov and Hecke parameters.** Writing $z = q^3/(q^2+1)$ for the Markov parameter and $\hbar_\times = q - 1/q$ for the Hecke deformation parameter of $\sigma^2 = \hbar_\times\sigma + 1$,

$$
  (G\vec t)_5 \;=\; z^2 \;+\; 2\hbar_\times z \;+\; 3\hbar_\times^2 z^2 \;+\; \hbar_\times^3 z \;+\; \hbar_\times^4 z^2 ,
$$

with integer coefficients $(1,2,3,1,1)$ and no denominators. **Degree $6$ is minimal** — no polynomial in $(z,\hbar_\times)$ of total degree $\leq 5$ represents $(G\vec t)_5$.

The two parameters satisfy the irreducible degree-$4$ algebraic relation

$$
  \hbar_\times^3 z - \hbar_\times^2 z^2 + 4\hbar_\times z - 4z^2 + 1 \;=\; 0 ,
$$

so $\mathbb{Q}[z,\hbar_\times]$ is the coordinate ring of an affine rational curve, and polynomial representatives are unique only modulo this relation. The degree-$6$ representatives form a **six-parameter family**: for instance, $-1 + 4z^2 - 3\hbar_\times z + 4z^4 + \hbar_\times^2 z^4$ is an equally integral representative differing by $(\hbar_\times z + z^2 + 1)$ times the defining relation, while the graded reverse lexicographic normal form is $\hbar_\times^5 z + 4\hbar_\times^3 z + \hbar_\times^2 - 2\hbar_\times z + 5z^2 - 1$. This algebraic relation is intrinsic to $H_n(q)$ and its Markov trace.

Integrality in $\mathbb{Z}[z,\hbar_\times]$ follows structurally before explicit evaluation: the Markov property $\mathrm{tr}(x\sigma_{\mathrm{last}}) = z\,\mathrm{tr}(x)$ eliminates the highest generator and the Hecke quadratic relation reduces higher powers, giving in particular $\mathrm{tr}(\sigma_0\sigma_1\sigma_0) = \hbar_\times z^2 + z$. Since $T_q = \sigma_1 + \hbar_\times\sigma_0\sigma_1$ has normal-form coordinates $\vec t = (0,0,1,\hbar_\times,0,0)$, the constraint $(G\vec t)_5 = \mathrm{tr}(W\sigma_1) + \hbar_\times\mathrm{tr}(W\sigma_0\sigma_1)$ necessarily lies in $\mathbb{Z}[z,\hbar_\times]$.

Both parameters are genuinely required: the minimal polynomial of the constraint has degree $3$ over $\mathbb{Q}(z)$ and degree $2$ over $\mathbb{Q}(\hbar_\times)$, so it belongs to neither subfield alone (and by coprimality $\mathbb{Q}(z,\hbar_\times) = \mathbb{Q}(q)$). Moreover, the numerator $q^{10}+q^6-q^4+q^2-1$ is neither reciprocal nor anti-reciprocal, so it cannot be the Alexander polynomial of any knot.

**Aether stability table:**
See [the sign-regime table](#tbl:toffoli-lp-stability-table2-data).
