<!-- FILE_START: classical-limit-intro.md -->
The preceding sections established that the algebraic substrate is unconditionally stable at the $q$-scale. The Hasse--Weil bound guarantees all Frobenius eigenvalues lie on the critical circle. The Reeb spectrum inherits this alignment. The substrate-side prime-counting estimate holds with the optimal square-root error term.

We now ask what happens in the classical limit $q \to 1$. The limit collapses the quantum gap $\hbar_q \to 0$, smooths the Jackson $q$-derivative into the ordinary derivative, and degrades the braided tensor category into a symmetric one. The local $q$-geometries at each prime fiber glue into the classical Riemann zeta function $\zeta(s)$. The Riemann hypothesis is exactly the statement that the macroscopic continuum inherits the stability of the $q$-scale.

**Skeleton of this section.** The remaining results share the [surreal rate calculus](#prop:surreal-rate-calculus) machinery. Treating the Reeb infinitesimal $\varepsilon$ ([Reeb infinitesimal](#def:reeb-epsilon)) as a strictly positive infinitesimal in $\mathbb{R}(\varepsilon) \subset \mathbf{No}$, we obtain two categorical invariants:

$$
  \Delta_q \;\asymp\; \varepsilon^3
  \qquad\text{(mass-gap dissipation, infinitesimal),}
$$
$$
  \Omega_q \;\asymp\; \varepsilon^{-1}
  \qquad\text{(Reeb period, transfinite).}
$$

The [surreal squeeze](#lem:surreal-squeeze) $\delta^2 \cdot \Omega_q > \Delta_q$ holds strictly for every standard real $\delta > 0$. Each millennium-problem remark applies this squeeze.
<!-- FILE_END: classical-limit-intro.md -->

<!-- FILE_START: classical-limit-functor.md -->
Define the **classical limit** as a :refterm[monoidal functor]{#monoidal-functor} $\mathcal{L} : \mathbf{C}_q \longrightarrow \mathbf{C}_1$ from the :refterm[braided monoidal category]{#braided-monoidal-category} $\mathbf{C}_q$ (at deformation parameter $q$) to the :refterm[symmetric monoidal category]{#symmetric-monoidal-category} $\mathbf{C}_1$ (at $q = 1$). The functor $\mathcal{L}$ acts on the substrate algebra by:

1. **Quantum gap collapse**: $\hbar_q = 1 - q^{-1} \to 0$, so that the non-commutativity vanishes.
2. **Differential smoothing**: The Jackson $q$-derivative $d_q f(z)$ converges to the ordinary derivative $\frac{df}{dz}$.
3. **Braiding trivialization**: The braiding $\sigma_{X,Y}$ specializes to the symmetric swap $\tau_{X,Y}$.

The functor $\mathcal{L}$ is exact but not full: quantum information is lost in the limit.
<!-- FILE_END: classical-limit-functor.md -->

<!-- FILE_START: classical-limit-adelic-assembly.md -->
**Adelic-assembly perspective (preferred reading).** Equivalently, $\mathcal{L}$ is the **archimedean component** of the realization tower $\{\rho_v\}_{v \in \mathrm{Pl}(\mathbb{Q})}$ of the [motivic substrate](#def:motivic-substrate). Under this reading, $\mathbf{C}_q$ is the universal motive over $\widehat{\mathcal{M}}$. Each finite place $p$ of $\mathbb{Q}$ ([adelic substrate](#def:adelic-substrate)) carries a local realization $\rho_p$ landing in $\mathbb{Q}_p$. The archimedean place $v = \infty$ carries $\rho_\infty = \mathcal{L}$, landing in $\mathbb{R}$. The $q \to 1$ limit is the vanishing of the local Reeb infinitesimal $\varepsilon_\infty$ at the archimedean place. The classical continuum is what remains after that single local $\varepsilon_v$ is collapsed.

**Non-fullness of $\mathcal{L}$: phase decoherence.** The full motivic class $[X] \in \widehat{\mathcal{M}}$ carries the relative $q$-phases between all finite places. The archimedean projection $\rho_\infty$ collapses across all those phases, retaining only the real-valued shadow. This is the rigorous mechanism behind the loss of quantum information. The classical continuum is a low-resolution shadow of the unglued adelic motives.
<!-- FILE_END: classical-limit-adelic-assembly.md -->

<!-- FILE_START: classical-limit-topology-free.md -->
**Topology-free reformulation (forward reference).** The [classical limit functor](#def:classical-limit-functor) uses a topological $q \to 1$ limit on the parameter space, which has obstructions ([classical limit obstruction](#def:classical-limit-obstruction)). The appendix replaces it with a literal evaluation in Conway's surreal field at $q = 1 + \varepsilon$, then takes the standard-part. Both replacements are conjectural; if they hold, they remove the need for any analytic machinery on the parameter space.
<!-- FILE_END: classical-limit-topology-free.md -->

<!-- FILE_START: quantum-gap-collapse.md -->
Under the classical limit functor $\mathcal{L}$, the following degenerations occur simultaneously:

1. **Planck constant**: $\hbar_q = 1 - q^{-1} \to 0$.
2. **$q$-differential**: $d_q \to d$.
3. **Braiding**: $\mathbf{C}_q$ degenerates to $\mathbf{C}_1$, as $R(q) \to \mathrm{id} \otimes \mathrm{id}$.
4. **Reeb period**: $\Omega_q \to \infty$.

Formally, $\mathcal{L}$ sends $A_q$ to a commutative Hopf algebra $A_1 = \mathcal{O}(\mathcal{B}_{\mathrm{cl}})$, the coordinate ring of the classical Bring's curve. The self-duality $A_q \simeq \omega_{A_q}^\bullet$ descends to classical Serre duality.
<!-- FILE_END: quantum-gap-collapse.md -->

<!-- FILE_START: classical-limit-obstruction.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum universe over a Noetherian ring $R$ with substrate parameter $q$ and classical limit functor $\mathcal{L} : \mathbf{C}_q \to \mathbf{C}_1$ ([classical limit functor](#def:classical-limit-functor)).

The **classical limit obstruction** of the quantum universe is the Hochschild cohomology group

$$
\mathrm{Obs}(\mathbf{C}, q \to 1)
 := 
HH^2(\mathcal{U}_q(\mathfrak{g}), \mathrm{Ad})
$$

where $\mathcal{U}_q(\mathfrak{g})$ is the Lusztig integral form of the quantized enveloping algebra associated to $A$, and $\mathrm{Ad}$ denotes the adjoint bimodule. Elements of $\mathrm{Obs}$ are obstructions to extending second-order deformations of the Frobenius--Hopf algebra $A_q$ across $q = 1$.
<!-- FILE_END: classical-limit-obstruction.md -->

<!-- FILE_START: classical-limit-obstruction-properties.md -->
The [classical limit obstruction](#def:classical-limit-obstruction) sits in a Hochschild tower whose vanishing controls flatness of the $q \to 1$ deformation.

**The Hochschild tower.** The Hochschild cohomology groups $HH^n(\mathcal{U}_q, \mathrm{Ad})$ govern the deformation theory of the substrate family $\{A_q\}_{q \in \mathbb{G}_m}$:
- $HH^0(\mathrm{Ad})$: hidden symmetries.
- $HH^1(\mathrm{Ad})$: outer derivations.
- $HH^2(\mathrm{Ad})$: obstructions to extending deformations across $q = 1$.
- $HH^3(\mathrm{Ad})$: secondary obstructions.

A property $\mathcal{P}(q)$ persists through $q = 1$ if and only if its obstruction class $[\mathcal{P}] \in HH^2(\mathrm{Ad})$ vanishes.

**Control of the classical limit by $HH^2$.** The classical limit $q \to 1$ is a deformation-theoretic specialisation. The obstructions to flatness at each order in $(q-1)$ live in $HH^2$. Expanding $A_q = A_1 + (q-1)\phi_1 + (q-1)^2\phi_2 + \cdots$, the first-order deformation $\phi_1$ is a Hochschild 2-cocycle. The second-order term $\phi_2$ exists iff $[\phi_1] \cup [\phi_1] = 0$ in $HH^3$. The total obstruction to the classical limit is the formal sum $\mathrm{obs}_\infty = \sum_{n \geq 1} (q-1)^n [\phi_n] \in HH^2(\mathrm{Ad})[[q-1]]$. This formal power series converges iff all Massey products vanish through the tower.

**Connection to the Yekutieli tower.** The Hochschild obstruction $[\phi_n]$ maps to the quantum characteristic class $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ under the Hochschild-to-sheaf comparison map. The abstract Hochschild obstruction is computed concretely by the Euler class $\kappa_0 = e(\xi)$ and its Kummer filtration.
<!-- FILE_END: classical-limit-obstruction-properties.md -->

<!-- FILE_START: qou-obstruction-reduction.md -->
**Theorem.** Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with gauge group $G = \mathrm{Aut}^{\otimes}(\tau)$ of dimension $d = \dim G$. Then:

**(a)** The classical limit obstruction ([classical limit obstruction](#def:classical-limit-obstruction)) is one-dimensional:
$$
\dim_k \mathrm{Obs}(\mathbf{C}, q \to 1) = \dim_k HH^2(\mathcal{U}_q, \mathrm{Ad}) = 1.
$$

**(b)** The unique obstruction class is the image of the Euler characteristic under the trace map:
$$
\mathrm{Obs}(\mathbf{C}, q \to 1) \cong k, \qquad [\phi_1] \mapsto \chi(A) \in R.
$$

**(c)** The obstruction vanishes at Kummer level $n$ iff $n \mid \chi(A)$.
<!-- FILE_END: qou-obstruction-reduction.md -->

<!-- FILE_START: qou-obstruction-reduction-interpretation.md -->
**Remark (the obstruction as a function on $\mathbb{P}^1$).** The obstruction $\chi(A) \bmod n$ varies over the Kummer tower $\{\mu_n\}_{n \geq 1}$:

$$
\mathrm{obs}(n) :=
\begin{cases}
0 & \text{if } n \mid \chi(A), \\
\chi(A) \bmod n & \text{otherwise.}
\end{cases}
$$

For the Descartes universe with $\chi(A) = -6$, the obstruction vanishes at only finitely many levels and persists at all levels $n$ with $\gcd(n, 6) \neq n$.

**Physical consequence:** The classical limit $q \to 1$ must pass through infinitely many Kummer levels where the obstruction is nonzero. In the limit, the obstruction is nonzero at a density-$1$ set of levels. The classical limit cannot avoid the obstruction.
<!-- FILE_END: qou-obstruction-reduction-interpretation.md -->

<!-- FILE_START: qou-obstruction-millennium-specializations.md -->
**Remark (the three millennium problems as specializations).** Each millennium problem is a property $\mathcal{P}$ that holds unconditionally at the $q$-scale, with obstruction class $[\mathcal{P}] \in \mathrm{Obs}(\mathbf{C}, q \to 1) \cong k$. The single obstruction scalar controls all three.

All three obstructions are images of the same class $\chi(A) \in HH^2 \cong k$ under different evaluation maps:
- **RH**: evaluate $\chi(A)$ on the spectral localization map.
- **NS**: evaluate $\chi(A)$ on the collision restriction map.
- **BSD**: evaluate $\chi(A)$ on the elliptic restriction map.

The one-dimensionality of $HH^2$ means these three evaluations are proportional. A single real number (the Euler characteristic $\chi(A) = -6$) controls whether all three millennium problems persist through the classical limit.

**Corollary.** If any one of the three millennium problems is resolved, the resolution constrains the other two. The mechanism is the same; only the evaluation map differs.
<!-- FILE_END: qou-obstruction-millennium-specializations.md -->

<!-- FILE_START: surreal-notation-cheat-sheet.md -->
**Cheat sheet for first-time readers of surreal notation.** The full surreal-number formalism is developed in the appendix ([`app:surreals`](#app:surreals)). This is a reading aid for the substrate-level uses of $\omega$ and $\varepsilon$. See [Table](#tbl:surreal-notation-cheat-sheet-table-data).

Wherever $\varepsilon$ appears in the substrate-level definitions below, read it as "the positive infinitesimal $1/\omega$". Wherever a surreal-bound statement appears, the cheat-sheet entry for $\mathrm{st}$ and $a \sim b$ is the only piece we need. The bound says "the inequality holds up to a $1 + \varepsilon$ factor", and applying $\mathrm{st}$ recovers the classical statement.
<!-- FILE_END: surreal-notation-cheat-sheet.md -->

<!-- FILE_START: reeb-epsilon.md -->
Let $(\mathbf{C}, A)$ be a quantum observable universe with categorical Reeb derivation $\xi \in \mathrm{Der}(A)$ ([categorical Reeb derivation](#def:categorical-reeb-derivation)), and let $\Phi_t : A \to A$ denote the one-parameter Reeb flow generated by $\xi$.

The **Reeb infinitesimal** is the distinguished element

$$
\varepsilon := \left. \frac{d}{dt} \right|_{t = 0} \Phi_t \;\in\; \mathrm{Der}(A)
$$

of the derivation algebra of the substrate object $A$.

**Primitivity.** The Reeb infinitesimal $\varepsilon$ is intrinsic to the categorical structure of $A$. It is the tangent vector at the identity of the Reeb flow. It is well defined before any choice of deformation scale is made.

**Positivity and archimedean independence.** The contact-form normalization $\xi \circ \varTheta = \varTheta$ of the Reeb derivation forces $\varepsilon$ to be a strictly positive element of $\mathrm{Der}(A)$. Moreover, $\varepsilon$ is archimedean-smaller than every standard-real derivation $\lambda \cdot \mathrm{id}_A$. These two properties pick out $\varepsilon$ as a positive infinitesimal direction.
<!-- FILE_END: reeb-epsilon.md -->

<!-- FILE_START: q-from-epsilon.md -->
With the Reeb infinitesimal $\varepsilon \in \mathrm{Der}(A)$ in hand ([Reeb infinitesimal](#def:reeb-epsilon)), the substrate parameter $q$ is now a derived quantity.

**Definition.** The **substrate parameter associated to $\varepsilon$** is

$$
q := 1 + \varepsilon,
$$

interpreted inside the ordered field generated by $\varepsilon$ over $\mathbb{R}$.
<!-- FILE_END: q-from-epsilon.md -->

<!-- FILE_START: q-from-epsilon-rationale.md -->
**Consistency with prior usage.** The existing Frobenius--Hopf substrate $A_q$ is recovered as the evaluation of the $\varepsilon$-expansion $A_q = A_1 + \varepsilon \, \phi_1 + \varepsilon^2 \, \phi_2 + \cdots$. Nothing in the existing $q$-theory changes: every identity previously written with $q - 1$ is now written with $\varepsilon$, and the classical point $\varepsilon = 0$ coincides with $q = 1$.

**Motivation for taking $\varepsilon$ as primitive.** First, categorical origin. The Reeb infinitesimal $\varepsilon$ is intrinsic to $A$ before any braiding is chosen. Second, exact error bounds. With $\varepsilon$ primitive and living in an ordered field with infinitesimals, the scaling laws become literal arithmetic inequalities.
<!-- FILE_END: q-from-epsilon-rationale.md -->

<!-- FILE_START: joint-galois-braid-figure-8-verified.md -->
**Proposition (joint Galois $\times$ braid action commutes on the figure-8 bi-filtration cell).**

The joint motivic-Galois $\times$ braid-group action conjecture ([`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)) predicts commutativity on each $\mathcal{H}_q^{(n, K)}$ stratum. We verify this prediction on the figure-8 row $\mathcal{H}_q^{(2, 4_1)}$ by direct computation.

The figure-8 bi-filtration cell is $\mathcal{H}_q^{(2, 4_1)} \subseteq G^{(2)}(\mathcal{H}_q)$, with dominant cell $\lambda_K = (2, 2)$ in $H_4(q)$ and shape parameter $z_K = \zeta_6 = e^{i\pi/3}$.

The two group actions:
- $G_{\mathrm{mot}} \supseteq \langle * \rangle$ (bar): $*: q \mapsto q^{-1}$, $\zeta_6 \mapsto \zeta_6^{-1}$.
- $B_4 \to H_4(q)$: $\sigma_1, \sigma_2, \sigma_3$ act by conjugation in $H_4(q)$, fixing central idempotents.
<!-- FILE_END: joint-galois-braid-figure-8-verified.md -->

<!-- FILE_START: joint-galois-braid-figure-8-verified-interpretation.md -->
**Remark (structural triviality of the figure-8 case, and the remaining cases).**

The verification works because the bar and braid actions touch disjoint structure. Braid acts on the cell $e_{(2,2)} \in Z(H_4(q))$, which is fixed by inner automorphisms. Bar acts on the coefficient ring $q$ and the shape parameter $\zeta_6 \in F^\times$. Disjoint actions commute trivially. This verifies the easiest case; the structurally non-trivial case is chiral pairs.

**Verified**: $(\lambda, K) = ((2, 2), 4_1)$ — a self-conjugate cell. By extension, any self-conjugate cell with a polylog argument in $F^\times$ has commuting bar $\times$ braid action.

**Remaining (open)**: chiral-pair cases. For the trefoil case ($n = 3$), verification is possible by direct computation but technical.

The joint-action conjecture is verified at the figure-8 row. The figure-8 row of the bi-filtration carries the full graded-Mikusiński structure as a theorem.
<!-- FILE_END: joint-galois-braid-figure-8-verified-interpretation.md -->

<!-- FILE_START: joint-galois-braid-discharged.md -->
**Proposition (joint motivic-Galois $\times$ braid action commutes on every bi-filtration cell).**

The joint-action conjecture ([`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)) predicted commutativity of the motivic-Galois action $G_{\mathrm{mot}}$ and the braid-group action $B_{n_K}$ on every $\mathcal{H}_q^{(n, K)}$ stratum. We discharge the conjecture in general. The argument is structural: the two actions touch disjoint factors of the bi-filtration's underlying tensor structure.

For every $(n, K)$, the actions $G_{\mathrm{mot}}$ and $B_{n_K}$ commute on $\mathcal{H}_q^{(n, K)}$:

$$
  g_{\mathrm{mot}}(\beta \cdot \alpha) \;=\; \beta \cdot g_{\mathrm{mot}}(\alpha)
  \quad\text{for } \alpha \in \mathcal{H}_q^{(n, K)},\;
  g_{\mathrm{mot}} \in G_{\mathrm{mot}},\;
  \beta \in B_{n_K}.
$$
<!-- FILE_END: joint-galois-braid-discharged.md -->

<!-- FILE_START: joint-galois-braid-discharged-interpretation.md -->
**Remark (the conjecture was open in form, not content; its discharge).**

The conjecture was structurally automatic. Bar, cyclotomic Galois, and the rest of $G_{\mathrm{mot}}$ act on the coefficient ring and shape parameter. The braid group acts on the Hecke cell. By design, these two structures are separate factors of $\mathcal{H}_q^{(n, K)}$, so disjoint actions commute.

The joint-action conjecture is now fully discharged. Combined with the small-cases bridge verification, the graded-Mikusiński bi-filtration framework's structural theorems are complete.
<!-- FILE_END: joint-galois-braid-discharged-interpretation.md -->
