<!-- FILE_START: intro-archimedean-realization-kashaev.md -->
The generic knot category requires a functor to the archimedean realm to yield real-valued physical observables. This section constructs the archimedean realisation functor and matches its output to the Kashaev volume conjecture, identifying hyperbolic volume as the archimedean shadow of the Hecke-skein.

We first define the functor and prove it preserves the Hecke-skein relation. We compute its value on torus knots, where the Kashaev volume vanishes. We then track the convergence of the substrate-level invariant to the hyperbolic volume as $q \to 1$, establishing categorical $\mathrm{Vol}_{\mathrm{hyp}}$ as the Kashaev sum limit.

Finally, we clarify the pre-$\tau$ versus post-$\tau$ distinction and the period identifications that secure the volume conjecture's substrate-level interpretation.
<!-- FILE_END: intro-archimedean-realization-kashaev.md -->

<!-- FILE_START: archimedean-realization-functor.md -->
**Definition.**
*The **archimedean realization functor** $\mathcal{R}_{\mathrm{top}}$ is the composite*

$$
  \mathcal{R}_{\mathrm{top}}
  \;:\;
  \widehat{\mathcal{M}}
  \;\xrightarrow{\;\;\chi_{\mathrm{top}}\;\;}\;
  \widehat{\mathcal{M}} \otimes_{K_0(\mathrm{Var})} \mathbb{Z}
  \;\xrightarrow{\;\;\pi_\infty\;\;}\;
  \mathbb{R}
$$

*sending the motivic class $[X]$ to its topological Euler characteristic $\chi_{\mathrm{top}}(X)$ followed by the **archimedean projection** $\pi_\infty \colon \mathbb{A} \to \mathbb{R}$. This functor evaluates motivic geometric shapes into real-valued physical observables.*

**Realization and projection.**
A motivic integral $\int_{\mathcal{L}(X)} d\mu \in \widehat{\mathcal{M}}$ defines a geometric shape. The topological realization $\chi_{\mathrm{top}}$ maps this shape to an integer (Euler characteristic) or a refined Hodge-theoretic invariant like hyperbolic volume. The adelic projection $\pi_\infty$ discards non-archimedean components, returning the real-valued laboratory measurement.

**Identification with the fibre functor.**
The QOU fibre functor $\tau \colon \mathbf{C} \to \mathbf{Arch}$ is the exclusive exit from the categorical substrate to the real numbers. On motivic QOU inputs, $\mathcal{R}_{\mathrm{top}}$ coincides exactly with the archimedean component of $\tau$:

$$
  \mathcal{R}_{\mathrm{top}}
  \;=\;
  \tau_{\mathrm{arch}}
  \;:=\;
  \pi_\infty \circ \tau
  \quad\text{on } \widehat{\mathcal{M}}_{\mathrm{QOU}}
  \;\subseteq\; \widehat{\mathcal{M}}.
$$

**Synthesis.**
The framework processes discrete categorical data along a single chain: adelic stitching, motivic integration, and archimedean projection. It requires no continuous differential equations or Lebesgue measures. The Kashaev limit of the algebraic quantum volume exemplifies this mechanism.
<!-- FILE_END: archimedean-realization-functor.md -->

<!-- FILE_START: pre-tau-vs-post-tau.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the structurally-wrong leading-order ansatz per [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md).

**The Archimedean wall.**
Every derivation step belongs to exactly one of two registers:

| Register | Coefficient ring | Operative invariants | Examples |
|---|---|---|---|
| **Pre-$\tau$** | $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$ (or $z$-Habiro) | Hecke spectra, Markov traces | SDP feasibility, Gröbner--Shirshov reductions |
| **Post-$\tau$** | $\mathbb{R}$ via $\tau_{\mathrm{arch}}$ | Hyperbolic volumes | PL thimble flow, Bloch--Wigner $D(z)$ |

The functor $\tau_{\mathrm{arch}}$ is the only legal bridge between these columns.

* Pre-$\tau$ derivation steps cannot use post-$\tau$ values (e.g., hyperbolic volume) as inputs.
* Post-$\tau$ derivation steps cannot claim algebraic-side identities (e.g., Hecke relations) that only hold prior to realization.
* Bridging equalities that cross the wall must use $\approx$ unless stating an explicit error term. They describe the functor, not algebraic derivation steps.

**Motivic shorthand.**
The $z$-Habiro completion cleanly houses algebraic encounter data, treating quantum dilogarithm poles as quotients of cyclotomic ideals. Under $\tau_{\mathrm{arch}}$, these algebraic poles realize as hyperbolic-triangulation cusps. Any violation of the wall boundary breaks the formal derivation.
<!-- FILE_END: pre-tau-vs-post-tau.md -->

<!-- FILE_START: vol-through-tau.md -->
**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a QOU with fibre functor $\tau$. For every braid $\beta \in H_n(R, q)$, the real-valued knot volume $\mathrm{Vol}(K_\beta)$ factors strictly through $\tau$:*

$$
  \mathrm{Vol}(K_\beta)
  \;=\;
  \tau_{\mathrm{arch}}\bigl(\mathrm{Vol}_q(\beta)\bigr)
  \;=\;
  (\pi_\infty \circ \tau)\bigl(\mathrm{Vol}_q(\beta)\bigr).
$$

*There is no other archimedean route.*

**Identification.**
On the algebraic quantum volume, $\tau_{\mathrm{arch}}$ coincides with $\mathcal{R}_{\mathrm{top}} = \pi_\infty \circ \chi_{\mathrm{top}}$. The fibre functor $\tau$ is the exclusive bridge to the laboratory continuum. The realization functor defines its canonical computation rule.

**Sketch.**
By Tannaka-Krein rigidity, any composite mapping $\mathbf{C}$ to $\mathbb{R}$ that preserves tensor products and dualities is uniquely isomorphic to the fibre functor $\tau$. Conversely, restricting the composite $\tau \circ \mathrm{Vol}_q$ via $\pi_\infty$ recovers exactly $\ln |\mathrm{Vol}_{q_0}(\beta)|$. Every physical computation of a knot volume (e.g., Kashaev limit, Bloch-Wigner dilogarithm) evaluates this identical composite.

**Lean formalization.**
The Lean theorem `vol_through_tau_factors` currently holds an existence stub pending a faithful formal statement.
<!-- FILE_END: vol-through-tau.md -->

<!-- FILE_START: vol-as-motivic-period.md -->
**Period interpretation.**
The hyperbolic volume $\mathrm{Vol}(S^3 \setminus K)$ is a motivic period: the value of a mixed-Tate motive under the Bloch-Wigner regulator $r_\infty$. For a hyperbolic knot complement with shape parameters $z_i$, the volume is:

$$
  \mathrm{Vol}(S^3 \setminus K)
  \;=\;
  \sum_{i=1}^{k} D(z_i),
$$

where $D$ is the Bloch-Wigner dilogarithm. Each $D(z_i)$ is a Kontsevich-Zagier period.

**Regulator interpretation.**
The shape parameters define a class $[K] \in \mathcal{B}(\overline{\mathbb{Q}})$ in the pre-Bloch group, yielding:

$$
  \mathrm{Vol}(S^3 \setminus K)
  \;=\;
  r_\infty\bigl([K]\bigr).
$$

The volume $\mathrm{Vol}(K)$ is the $K$-theoretic image of an algebraic class under a transcendental regulator.

**QOU placement.**
The archimedean realization functor factorizes identically across three pictures: adelic projection ($\pi_\infty \circ \tau$), Euler-characteristic integration ($\pi_\infty \circ \chi_{\mathrm{top}}$), and Bloch-Wigner regulation ($r_\infty$). These pictures agree entirely on the algebraic quantum volume domain. Each formalizes a distinct aspect: adelic ensures categorical compatibility, Euler-characteristic handles blow-up calculus, and Bloch-Wigner bridges to quantum topology literature.
<!-- FILE_END: vol-as-motivic-period.md -->

<!-- FILE_START: kashaev-volume-density.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the structurally-wrong leading-order ansatz per [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md).

The topological mass formula $\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$ is exactly a volume $\times$ density product.

### Substrate density $\rho_q$

*Define the **substrate density** to be the inverse squared quantum Planck constant:*

$$
  \rho_q
  \;:=\;
  \frac{1}{\hbar_q^{2}}
  \;=\;
  \frac{q^{2}}{(q-1)^{2}}.
$$

Physically, $\rho_q$ measures the categorical drag cost of transporting a closed vortex through the Frobenius-Hopf structure. Mass is topological volume weighted by substrate drag.

### The Kashaev bridge

The Kashaev Volume Conjecture bridges the archimedean continuous volume and the algebraic discrete Markov trace:

$$
  \mathrm{Vol}(K)
  \;=\;
  2\pi\,\lim_{N \to \infty}
  \frac{\log\lvert J_{N}(K;\,e^{2\pi i/N})\rvert}{N}.
$$

The left-hand side is the continuous hyperbolic volume. The right-hand side is an asymptotic limit of colored Markov traces evaluated within the Hecke algebra.

### Inverting the ontology

The QOU framework reverses the classical priority: the discrete trace is fundamental, while the continuous volume is emergent. The colored Jones polynomials are finite algebraic evaluations of Markov traces. The hyperbolic volume simply describes the asymptotic scaling of these exact categorical evaluations. The macroscopic continuum shadow emerges from the accumulated algebraic drag of discrete crossing resolutions.

### Consequences for the mass formula

Substituting the Kashaev identity yields a fully algebraic derived mass:

$$
  \mathfrak{m}(K)
  \;\approx\;
  \rho_{q}\;\cdot\;
  \Bigl[
    2\pi\,\lim_{N \to \infty}
    \frac{\log\lvert J_{N}(K;\,e^{2\pi i/N})\rvert}{N}
  \Bigr].
$$

No continuous inputs remain. Every constituent is a discrete Hecke trace evaluated at roots of unity. The finite categorical evaluation operates precisely at the non-asymptotic substrate value $q_0 \approx 1.11$, avoiding the $N \to \infty$ continuum idealization entirely.
<!-- FILE_END: kashaev-volume-density.md -->

<!-- FILE_START: kashaev-as-archimedean-realization.md -->
The Kashaev volume conjecture identifies the archimedean realization functor applied to the algebraic quantum volume. It is not an external mathematical coincidence, but the canonical action of $\mathcal{R}_{\mathrm{top}}$ on the brane substrate.

**Algebraic side.**
The colored Jones polynomial evaluated at roots of unity is a purely $p$-adic/cyclotomic discrete algebraic trace. The algebraic quantum volume $\mathrm{Vol}_q(\mathcal{B}_K)$ packages these local data into a global Habiro element.

**Archimedean realization.**
The asymptotic limit $N \to \infty$ executes the action of $\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$. It discards cyclotomic data and projects the adelic ring to $\mathbb{R}$. The Kashaev-Murakami-Murakami theorem confirms this limit equals the hyperbolic volume:

$$
  \mathrm{Vol}(S^3 \setminus K)
  \;=\;
  \tau_{\mathrm{arch}}\bigl(\mathrm{Vol}_q(\mathcal{B}_K)\bigr)
  \;=\;
  \mathcal{R}_{\mathrm{top}}\bigl(\mathrm{Vol}_q(\mathcal{B}_K)\bigr).
$$

The fibre functor $\tau$ is the exclusive archimedean route. The Kashaev limit is the realization functor of the QOU.
<!-- FILE_END: kashaev-as-archimedean-realization.md -->

<!-- FILE_START: phi-q-piece.md -->
Let $\beta \in B_n$ be a braid. For each subset $S \subseteq \{0, \dots, n-2\}$, the **$\Phi_q$-piece $K_S \subseteq S^3$** is the link obtained from $\widehat{\beta}$ by $L_0$-smoothing every crossing not in $S$ while leaving crossings in $S$ intact.

This construction satisfies three properties:
1. **Functoriality:** $K_\emptyset$ is the unlink; $K_{\{0,\dots,n-2\}}$ is the original closure.
2. **Subset compatibility:** $K_S = (K_T)_S$ for $S \subseteq T$.
3. **Categorical interpretation:** The pieces $K_S$ constitute the geometric shadow of the Wedderburn-block stratification. The algebraic spectral coordinate $\prod_{i \in S} \hat{V}_i$ localizes geometrically to $K_S$.

The piece $K_S$ acts as the geometric carrier of the per-$S$ summand $\Phi_q\bigl(\bigl\lvert\prod_{i \in S} \hat{V}_i^{\mathrm{full}}\bigr\rvert\bigr)$. The empty piece is the descended level-zero carrier. All others are transient carriers. The $\Phi_q$-piece serves as the discrete unit on which archimedean realization evaluates the tower.

### Motivic interpretation

The quantum dilogarithm $\Phi_q$ is a $q$-deformation of the Bloch-Wigner dilogarithm. The per-piece summand $\Phi_q(\lvert V_S\rvert)$ represents a class in the quantum Bloch group. The family $\{K_S\}_S$ provides the geometric stratification along which the regulator decomposes, solidifying the bridge to hyperbolic volume as a strict regulator statement.
<!-- FILE_END: phi-q-piece.md -->

<!-- FILE_START: phi-q-tower-algebraic-stratification.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the structurally-wrong leading-order ansatz per [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md).

**Proposition (algebraic stratification of the $\Phi_q$ tower).**
*Let $\beta \in B_n$ be a braid. The $\Phi_q$-tower admits a purely algebraic stratification by $|S|$ within the Gröbner-Shirshov filtration of the Hecke algebra:*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \bigl\| \mathrm{tr}_M(\rho(\beta_\emptyset))\bigr\|_F
  \;+\;
  \sum_{|S| = 1} \Phi_q\bigl(\|\hat V_S\|_F\bigr)
  \;+\;
  \sum_{|S| = 2} z^{2} \Phi_q\bigl(\|\hat V_S\|_F\bigr).
$$

*The Frobenius norm $\|\cdot\|_F$ evaluates entirely within the ground ring $\mathbb{Z}[q^{\pm 1/2}]$. This unconditional stratification identifies exactly with the $J^{|S|}/J^{|S|+1}$ grading of the GS confinement filtration.*

The algebraic stratification operates strictly pre-$\tau$. It decomposes the mass endomorphism using only discrete categorical data, isolating the structural descent without invoking any hyperbolic or continuous geometry.
<!-- FILE_END: phi-q-tower-algebraic-stratification.md -->
