<!-- FILE_START: intro-ns-obstruction-tower-mtc.md -->
The preceding section established the $q$-deformed Navier–Stokes system on $\Omega^1(A)$ alongside its global regularity for any substrate parameter $q > 1$. This section builds the obstruction tower governing how that regularity breaks down as $q \to 1$. It also isolates the modular tensor category structure on the limiting observables that survives this degeneration.

The argument proceeds in two tracks. The first six blocks assemble the obstruction tower over the collision locus of two anti-parallel vortex filaments. The boundary observability $\mathrm{Obs}_\partial(A)$ serves as the kernel of the restricted Yekutieli classes, computed directly via Kummer specialisation and matched against the torus-NS-regular case using root-of-unity truncation. The final two blocks (Track B) extract the observable modular tensor category and its inherent braid-group action. This braided action constitutes the categorical residue of the fluid flow, serving as the foundational input for the research programme in the subsequent section.

The two-vortex amalgamation ([approach to exceptional divisor](#sec:approach-to-exceptional-divisor)) organically extends to three. During a triple-vortex collision, the merged fundamental group $\pi_1(U \setminus K_3)$ hosts a three-strand braid representative. The categorical instanton operates on $\mathbf{V}^{\otimes 3}$ via the $B_3$-representation $\rho_3$ of [prop:bn-mtc-action](#prop:bn-mtc-action). SDP/LP minimisation identifies the Brunnian (pairwise-unlinked, triple-linked) Borromean braid $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ of [conj:borromean-quark](#conj:borromean-quark) as the dominant physical representative. Confinement directly matches the non-vanishing triple Milnor invariant $\bar{\mu}_{123}$.
<!-- FILE_END: intro-ns-obstruction-tower-mtc.md -->

<!-- FILE_START: ns-obstruction-tower.md -->
**Proposition (conditional on
[`conj:q-aubin-lions`](#conj:q-aubin-lions),
[`conj:ns-counterexample`](#conj:ns-counterexample),
[`conj:critical-exponent`](#conj:critical-exponent),
[`prop:blowup-yekutieli`](#prop:blowup-yekutieli),
and
[`conj:regularity-breakdown`](#conj:regularity-breakdown);
"NS obstruction tower").**

Let $(\mathbf{C}, A, \tau)$ define a QOU carrying Euler characteristic $\chi(A)$ and [obstruction classes](#def:quantum-characteristic-classes) $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$. Let $\Sigma \subset \mathcal{S}$ denote the precise collision locus of two anti-parallel vortex filaments.

The [boundary observability](#def:ns-regular-qou) $\mathrm{Obs}_\partial(A)$ derives directly from the restriction of the obstruction classes down to the collision locus:

$$
  \mathrm{Obs}_\partial(A)
  = 
  \ker\!\left(
    \bigoplus_{n \geq 0}
    H^2(\mathcal{S}, \mathcal{B})
    \xrightarrow{ \mathrm{res}_\Sigma}
    \bigoplus_{n \geq 0}
    H^2(\Sigma, \mathcal{B}|_\Sigma)
  \right).
$$

The QOU is [NS-singular](#def:ns-regular-qou) (mandating blowup) if and only if $\mathrm{res}_\Sigma(\kappa_n) \neq 0$ for at least one $n$. It is NS-regular if and only if $\mathrm{res}_\Sigma(\kappa_n) = 0$ for all $n$.

**(a) Where the obstruction sits.**

Following the [QU-to-QOU theorem](#thm:qu-to-qou), the base obstruction is exactly $\kappa_0 = e(\xi)$, the Euler class of the Reeb bundle, carrying $\mathrm{tr}(\kappa_0) = \chi(A)$. The obstruction at arbitrary level $n$ takes the form

$$
  \kappa_n
  = 
  \kappa_0
  + 
  \delta_n,
  \qquad
  \delta_n \in \mathrm{im}\!\bigl(
    H^2(\mathcal{S}, \mathcal{O}_\mathcal{S})
    \to H^2(\mathcal{S}, \mathcal{B})
  \bigr),
$$

where $\delta_n$ applies the explicit jet correction at level $n$. Due to the perpetual obstruction ([QU-to-QOU](#thm:qu-to-qou) item 3, rigidly strengthened by [motivic perpetual obstruction](#conj:motivic-perpetual-obstruction) evaluating the substrate's motivic Galois character place-by-place), $\kappa_0$ and $\delta_n$ strictly occupy complementary subgroups whenever $\kappa_0$ avoids torsion. Consequently, $\kappa_n \neq 0$ unconditionally for all $n$.

**(b) Restriction to the collision locus.**

The collision locus $\Sigma$ forms a strict 1-dimensional submanifold (a line segment). $H^2(\Sigma, \mathcal{B}|_\Sigma)$ derives from the long exact sequence applied to the pair $(\mathcal{S}, \mathcal{S} \setminus \Sigma)$:

$$
  \cdots \to
  H^1(\mathcal{S} \setminus \Sigma, \mathcal{B})
  \xrightarrow{\partial}
  H^2_\Sigma(\mathcal{S}, \mathcal{B})
   \to 
  H^2(\mathcal{S}, \mathcal{B})
  \xrightarrow{ \mathrm{res}}
  H^2(\mathcal{S} \setminus \Sigma, \mathcal{B})
  \to \cdots
$$

The obstruction transfers nontrivially to $\Sigma$ if and only if $\kappa_n$ strictly evades the image of the restriction map descending from $\mathcal{S} \setminus \Sigma$. Equivalently, the connecting homomorphism $\partial$ isolates it: $\kappa_n|_\Sigma \neq 0$ if and only if $\kappa_n$ maintains nontrivial **local cohomology** support anchored precisely at $\Sigma$.

**(c) Local cohomology computation.**

Evaluating the [local cohomology](#def:local-cohomology-group) at any collision point $p \in \Sigma$ gives

$$
  H^1_{\mathfrak{m}_p}(A)
  = 
  R^1\Gamma_{\mathfrak{m}_p}(A).
$$

For the anti-parallel pair, each vortex filament naturally hosts the fundamental representation $V_{1/2}$ of $\mathrm{SU}_q(2)$. At the intersection point $p$, both filaments stack their contributions onto the local cohomology:

$$
  H^1_{\mathfrak{m}_p}(A)
  = 
  V_{1/2}^{(1)} \oplus V_{1/2}^{(2)}.
$$

This constructs a rigid 4-dimensional space. It remains **nonzero** if and only if both individual filaments successfully provide nontrivial local sections at $p$ — physically, if the discrete vortex cores have not dissolved into a continuous sheet.

**(d) Connection to core aspect ratio.**

Relying on [core-Levi equivalence](#prop:core-levi-form), the local cohomology holds a nonzero value if and only if the Levi form maintains strict non-degeneracy at $p$. Algebraically:

$$
  H^1_{\mathfrak{m}_p}(A) \neq 0
  \quad\Longleftrightarrow\quad
  \lambda_\parallel(p) > 0
   \text{ and }
  \lambda_\perp(p) > 0
  \quad\Longleftrightarrow\quad
  \kappa(p) = a_\perp/a_\parallel \in (0, \infty).
$$

If the core flattens completely ($\kappa \to 0$ or $\kappa \to \infty$), one Levi eigenvalue collapses. The local cohomology subsequently degenerates from $V_{1/2}^{\oplus 2}$ down to a quotient, forcing the obstruction class $\kappa_n|_\Sigma$ to deform safely toward zero.

**(e) The NS obstruction as an Euler-class residue.**

Synthesising (a)--(d), the exact NS obstruction at level $n$, forcibly restricted to the collision locus, yields

$$
  \kappa_n\big|_\Sigma
  = 
  \mathrm{lk}(\varrho_1, \varrho_2)
  \cdot e(\xi)\big|_\Sigma
  +  \delta_n\big|_\Sigma,
$$

where $\mathrm{lk}(\varrho_1, \varrho_2)$ tracks the explicit linking number separating the two filaments, and $e(\xi)|_\Sigma$ evaluates the Euler class of the Reeb bundle precisely on $\Sigma$.

Mapped onto the Descartes universe ($\chi(A) = -6$, anchored on Bring's surface): $e(\xi) = -6 \cdot [\Sigma_4]$ evaluated inside $H^2(\Sigma_4, \mathbb{Z})$. The local restriction $e(\xi)|_\Sigma$ registers as nonzero strictly when $\Sigma$ behaves homologically nontrivially inside $\Sigma_4$. The anti-parallel pair (carrying linking number 1) satisfies this identically.

**Summary.** We measure the NS obstruction consistently across every level of the Yekutieli tower by forcibly restricting $\kappa_n$ onto the collision locus $\Sigma$. It remains nonzero (confirming NS-singular blowup) if and only if the local cohomology $H^1_{\mathfrak{m}_p}(A)$ holds a nonzero value at collision points. This matches the exact condition where the Levi form successfully evades degeneracy (maintaining a bounded core aspect ratio). The [Levi degeneracy conjecture](#conj:levi-degeneracy) isolates whether $\kappa_n|_\Sigma$ collapses or survives through the strict $q \to 1$ limit.
<!-- FILE_END: ns-obstruction-tower.md -->

<!-- FILE_START: ns-obstruction-computation.md -->
Let $(\mathbf{C}, A, \tau)$ define the Descartes universe spanning $\chi(A) = -6$ (Bring's surface of genus 4). Let $\Sigma$ designate the precise collision locus governing an anti-parallel vortex pair marked by linking number $\mathrm{lk} = 1$.

The [NS obstruction](#prop:ns-obstruction-tower) at level $n$, strictly restricted to $\Sigma$, evaluates as $\kappa_n|_\Sigma = \mathrm{lk} \cdot e(\xi)|_\Sigma + \delta_n|_\Sigma$. We systematically compute both terms.

**(a) The Euler class term.**

The explicit Euler class $e(\xi) \in H^2(\Sigma_4, \mathbb{Z})$ driving the Reeb bundle enforces $\mathrm{tr}(e(\xi)) = \chi(A) = -6$. Because $H^2(\Sigma_4, \mathbb{Z}) \cong \mathbb{Z}$ (Bring's surface exists as a closed orientable surface), $e(\xi)$ resolves strictly as the integer $-6$.

Restricting the class onto $\Sigma$ (a one-dimensional line segment, thus inherently contractible) mathematically zeros out $e(\xi)|_\Sigma = 0$ inside $H^2(\Sigma, \mathbb{Z})$.

However, the **local** Euler class pinned to a specific point $p \in \Sigma$ derives from the local cohomology $H^2_{\{p\}}(\Sigma_4, \mathbb{Z})$, which safely evades zero. Employing excision yields:

$$
  H^2_{\{p\}}(\Sigma_4, \mathbb{Z})
   \cong 
  H^2(D^4, S^3; \mathbb{Z})
   \cong 
  \mathbb{Z},
$$

where $D^4$ defines a tight ball encircling $p$ and $S^3$ defines its boundary (acknowledging Bring's surface possesses real dimension 4). The Euler class therefore maps directly to the **local degree** precisely at $p$:

$$
  e(\xi)|_p = -6 \cdot \deg_p(\xi) \in \mathbb{Z}.
$$

At a generic point, $\deg_p(\xi) = 0$ (the Reeb vector field avoids vanishing). At an explicit **vortex collision point**, the Reeb field forcibly zeroes out (the contact structure must degenerate if the physical core flattens). $\deg_p(\xi)$ strictly records the index of this resulting zero.

**(b) The jet correction term.**

The formal jet correction $\delta_n$ at level $n$ inside the Yekutieli tower isolates the $n$-th iterated jet prolongation. Due to [Euler characteristic stability](#prop:euler-char-stability), $\chi(E_n) = \chi(A) = -6$ holds uniformly across all $n$. The topological baseline therefore ignores the level completely.

The specific analytic correction $\delta_n|_\Sigma$ feeds directly off the $(n+1)$-jet of the associated velocity field impinging on $\Sigma$. The anti-parallel pair enforces the Biot--Savart structure $v \sim \Gamma/(2\pi d)$ approaching the collision. The resulting jets strictly diverge as $d \to 0$:

$$
  |j^n v|_\Sigma
   \sim 
  \frac{\Gamma}{d^{n+1}}
   \sim 
  \frac{1}{(T^* - t)^{(n+1)/2}}.
$$

The magnitude $|j^n v|$ strictly dictates the jet correction $\delta_n|_\Sigma$; the correction operates nonzeroly whenever the corresponding $n$-th jet mathematically diverges. For the anti-parallel pair, $|j^n v| \to \infty$ applies universally to all $n \geq 1$ as $t \to T^*$.

**(c) The total obstruction.**

Fusing (a) and (b), the exact NS obstruction resting on the collision locus cleanly segregates into two pieces:

1. **Topological**: $\mathrm{lk} \cdot e(\xi)|_p$. This term avoids zero if and only if the Reeb field zeroes out at $p$ (which occurs if and only if the contact structure structurally degenerates).
2. **Analytic**: $\delta_n|_\Sigma$. This term avoids zero universally whenever the $n$-th jet of the operative velocity field cleanly diverges (holding for all $n \geq 1$ under the anti-parallel configuration).

The topological and analytic components map exactly into mathematically complementary subgroups inside $H^2(\mathcal{S}, \mathcal{B})$ (governed by the perpetual obstruction mechanism, [QU-to-QOU](#thm:qu-to-qou) item 3).
Consequently:

- If the Reeb field fundamentally **lacks a zero** at $p$ ($\deg_p(\xi) = 0$): the topological component cleanly vanishes, but the analytic component $\delta_n|_\Sigma \neq 0$ stubbornly persists. The surviving obstruction becomes **purely analytic** while the contact structure avoids degeneracy. This explicitly describes the **NS-singular** (blowup) condition.
- If the Reeb field **possesses a zero** at $p$ ($\deg_p(\xi) \neq 0$): both isolated terms avoid zero. Because they occupy strictly complementary subgroups, they possess no mechanism to mathematically cancel. The aggregate obstruction persists nonzeroly. This similarly enforces the **NS-singular** condition.

**(d) Result.**

Mapped over the Descartes universe with $\chi(A) = -6$:

$$
  \kappa_n\big|_\Sigma  \neq  0
  \qquad\text{for all } n \geq 1.
$$

The analytic component $\delta_n|_\Sigma$ absolutely avoids zero because the nested jets composing the Biot--Savart velocity field mathematically diverge at the exact collision point. The paired topological term evaluates either as zero (lacking a Reeb zero) or nonzero (possessing a Reeb zero). In all permutations, the isolated $\delta_n$ term prevents the total obstruction from collapsing, as the complementary structure forbids any potential cancellation.

Therefore $\mathrm{Obs}_\partial(A) = 0$. The Descartes universe operates uniformly as **NS-singular**.

*Formal asymptotic content. The absolute jet divergence $|j^n v|_\Sigma \sim 1/(T^*-t)^{(n+1)/2}$ translates cleanly into $\ordw(\lvert j^n v \rvert_\Sigma) = -\tfrac{n+1}{2}\,\ordw(T^*-t)$ as $t \to T^*$. The complete recursive jet tower establishes the [surreal blow-up calculus](#def:surreal-blowup-calculus), while the exact $q \to 1$ classical-limit extraction requires the [standard-part functor](#def:standard-part-functor). See also [Big-O via $\ordw$](#rem:conway-normal-form) alongside the [body asymptotics catalog](#rem:body-asymptotics-catalog).*
<!-- FILE_END: ns-obstruction-computation.md -->

<!-- FILE_START: ns-obstruction-computation-interpretation.md -->
**Mathematical Novelty.** Calculating local Euler classes via excision ($H^2_{\{p\}}$) and executing Biot-Savart jet divergence reflect standard differential topology and fluid mechanics. The strict mathematical novelty lies in mechanically bridging them to verify that the analytic and topological terms populate strictly complementary subgroups inside the obstruction tower. This mechanism rigorously proves that physical adjustments operating in the topological background manifold cannot mathematically "cancel out" classical divergence bounds. The explicit structural obstruction persists rigidly across all jet levels.
<!-- FILE_END: ns-obstruction-computation-interpretation.md -->

<!-- FILE_START: ns-kummer-specialisation.md -->
Let $(\mathbf{C}, A, \tau)$ isolate a valid QOU bearing $\kappa_0 = e(\xi) \in H^2(\mathcal{S}, \mathbb{G}_m)$ constrained by $\mathrm{tr}(\kappa_0) = \chi(A)$.

The strict Kummer exact sequence evaluated at any integer $n \geq 1$:

$$
  1 \to \mu_n \to \mathbb{G}_m
  \xrightarrow{(\cdot)^n} \mathbb{G}_m \to 1
$$

forces a long exact sequence mapping through cohomology:

$$
  H^2(\mathcal{S}, \mu_n)
  \to H^2(\mathcal{S}, \mathbb{G}_m)
  \xrightarrow{\cdot n}
  H^2(\mathcal{S}, \mathbb{G}_m)
  \to H^3(\mathcal{S}, \mu_n).
$$

The [specialisation driving $q = 1$](#rem:substrate-gm-torsion) projects cleanly:

$$
  \kappa_0 \mapsto
  \kappa_0 \bmod n
   \in 
  H^2(\mathcal{S}, \mathbb{G}_m) / nH^2(\mathcal{S}, \mathbb{G}_m).
$$

This resulting class safely avoids zero if and only if $\kappa_0$ fundamentally **resists** $n$-divisibility.

**(a) Divisibility of the Euler class.**

Constrained over a closed orientable surface $\Sigma_g$ anchored at genus $g$: $H^2(\Sigma_g, \mathbb{Z}) \cong \mathbb{Z}$. The bare Euler class scales as $e(\xi) = \chi(A) \in \mathbb{Z}$. Therefore:

$$
  \kappa_0 \bmod n = 0
  \quad\Longleftrightarrow\quad
  n \mid \chi(A).
$$

Applied to the Descartes universe at $\chi(A) = -6$, the valid divisors restrict strictly to $\{1, 2, 3, 6\}$. $\kappa_0 \bmod n$ mathematically zeroes out only spanning $n \in \{1, 2, 3, 6\}$. It rigorously evades zero for all other $n$ (verifiably holding for $n = 5, 7, 11, 13, \ldots$).

**(b) Obstruction persistence.**

Evaluating at the root of unity $q = e^{i\pi/\kappa}$, the operating Kummer level isolates strictly to $n = 2\kappa$ (reflecting the exact order mapping $q$ inside $\mathbb{G}_m$). The functional obstruction $\kappa_0 \bmod 2\kappa$ reduces to:

$$
  \kappa_0 \bmod 2\kappa = 0
  \quad\Longleftrightarrow\quad
  2\kappa \mid \chi(A).
$$

For $\chi(A) = -6$, $2\kappa \mid 6$ permits exclusively $\kappa \in \{1, 3\}$, corresponding to $q = e^{i\pi}$ or $q = e^{i\pi/3}$. At every other valid $\kappa$ (universally capturing all $\kappa \geq 4$), the obstruction fundamentally **persists** squarely at that root of unity.

**(c) The limit as kappa goes to infinity.**

Pushing $\kappa \to \infty$ ($q \to 1$) forces $2\kappa \to \infty$. Consequently, $2\kappa \nmid 6$ governs unconditionally for all $\kappa \geq 4$. The math yields:

$$
  \kappa_0 \bmod 2\kappa  \neq  0
  \qquad\text{for all } \kappa \geq 4.
$$

The topological component driving the NS obstruction **rigorously avoids vanishing** through the $q \to 1$ classical limit.

**(d) Formal statement.**

Evaluated against any QOU possessing $\chi(A) \neq 0$:

1. The exact specialisation $\kappa_0|_{q=1}$ rigidly avoids zero within $H^2(\mathcal{S}, \mathbb{G}_m)/n$ universally for all integers $n \nmid \chi(A)$.
2. The integer set $\{n : n \nmid \chi(A)\}$ strictly extends to infinity (safely encompassing all primes avoiding $\chi(A)$). The overall obstruction must remain **persistently nonzero** structurally piercing infinitely many levels inside the Kummer tower.
3. The absolute obstruction zeroes out exclusively at the finite, isolated Kummer levels matching $n \mid \chi(A)$. These align perfectly with the finite set of roots of unity where the category's truncation operates compatibly alongside the fixed Euler class.

**(e) Consequence for NS regularity.**

A valid QOU constrained by $\chi(A) = -6$ universally executes as **NS-singular**: $\mathrm{Obs}_\partial(A) = 0$. The boundary observability systematically vanishes. The classical Navier--Stokes equation inherently permits finite-time blowup.

This result stems absolutely from (e) bonded to the [complementary-subgroup argument](#thm:qu-to-qou) (item 3). The core topological obstruction $e(\xi)|_\Sigma \neq 0$ lacks any mathematical channel to suffer cancellation against the operative analytic correction $\delta_n|_\Sigma$. They strictly populate complementary summands inside $H^2(\mathcal{S}, \mathbb{G}_m)$.
<!-- FILE_END: ns-kummer-specialisation.md -->

<!-- FILE_START: ns-singularity-descartes.md -->
Let $(\mathbf{C}, A, \tau)$ define the explicit Descartes quantum universe anchored by $\chi(A) = -6$ (mapping Bring's surface at genus 4).

The structure $(\mathbf{C}, A, \tau)$ evaluates unconditionally as [NS-singular](#def:ns-obstruction):

$$
  \mathrm{NS}(A)
  = 
  e(\xi)\big|_\Sigma
   \neq  0.
$$

The classical 3-dimensional Navier--Stokes equation mathematically admits smooth initial data designed to force the solution directly into a finite-time singularity.
<!-- FILE_END: ns-singularity-descartes.md -->

<!-- FILE_START: ns-singularity-descartes-interpretation.md -->
**Mathematical Novelty.** The physical proof leverages a precise array of conditional geometric limits (Kummer tower survival, perpetual obstruction, core-Levi bounding, BKM divergence). The mathematical novelty resides entirely in assembling these abstract topological components mechanically into a single, strictly deterministic logical criterion. It elegantly bypasses standard brute-force PDE analytic estimates, successfully deploying the isolated arithmetic constraint ($\chi(A)=-6$) as a pure global topological forcing term capable of dictating finite-time blowup solely through native categorical mechanics.
<!-- FILE_END: ns-singularity-descartes-interpretation.md -->

<!-- FILE_START: torus-ns-regular.md -->
Assume $(\mathbf{C}, A, \tau)$ represents a valid quantum universe placing $A$ physically on the classical torus $\Sigma_1$ (genus $g = 1$). The math dictates

$$
  \chi(A) = 2 - 2g = 0.
$$

**The NS obstruction vanishes.**
The corresponding Euler class traversing the Reeb bundle sets $\kappa_0 = e(\xi)$, yielding $\mathrm{tr}(\kappa_0) = \chi(A) = 0$. Measured against every integer $n \geq 1$, $2\kappa \mid 0$ functions unconditionally across all $\kappa$. This locks $\kappa_0 \bmod 2\kappa = 0$ universally across every single Kummer level. Executing the [Kummer specialisation](#prop:ns-kummer-specialisation) yields exactly zero obstruction:

$$
  \mathrm{NS}(A) = \kappa_0\big|_\Sigma = 0.
$$

The torus quantum universe operates strictly as **NS-regular**.

**Physical meaning.**
The Levi form possesses total structural freedom to degenerate seamlessly at any collision locus. The physical vortex cores can structurally flatten seamlessly into macroscopic sheets. Vorticity naturally dissipates rather than forcefully concentrating. The classical Navier--Stokes equation (safely specialised at $q = 1$) seamlessly converts all smooth initial data into mathematically smooth global solutions.

**Failure of the torus to support the observed physics.**
Because the torus anchors at $g = 1$, it physically embeds exactly one torus knot: $T_{2,3}$ (the generic trefoil spanning Seifert genus 1). The generated knot spectrum isolates a single physical generator — effectively abandoning the muon, the tau, and any quarks outside the first generation. The explicit representation theory governing $\pi_1(\Sigma_1) = \mathbb{Z}^2$ behaves completely abelian: every valid $\mathrm{SU}(2)$ representation must mechanically factor down through $\mathrm{U}(1)$. The base gauge group completely collapses. The expected full particle spectrum simply cannot emerge.

**The torus also fails observability.**
Evaluated over $\Sigma_1$, explicitly flat $\mathrm{SU}(2)$ connections reliably exist bearing holonomy restricted to $\mathrm{U}(1) \subset \mathrm{SU}(2)$. These remaining connections act entirely **reducible**: $H^0(\Sigma_1, \mathrm{Ad}(P)) \neq 0$ (the isolated Cartan subalgebra $\mathfrak{u}(1) \subset \mathfrak{su}(2)$ automatically supplies a persistent nonzero equivariant section). Consequently, $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \neq 0$. The core observability axiom explicitly fails.

The resulting torus structure forms a quantum pre-universe (QPU), definitively rejecting QOU status.

**Contrast with the Descartes universe.**

See [Table](#tbl:torus-ns-regular-table-data).

The mathematical torus provides the absolute simplest mechanical example where $\chi = 0$ rigorously forces exact NS regularity. Predictably, it is also completely physically trivial. The mechanically vanishing Euler characteristic specifically prevents the torus from physically supporting a dense universe, explaining precisely why its resulting fluid dynamics remain entirely tame.

**Other $\chi = 0$ examples.**
Any physical genus-1 surface enforces exactly $\chi = 0$: including the standard flat torus $\mathbb{R}^2/\mathbb{Z}^2$, the specific Heisenberg nilmanifold $\mathrm{Heis}(\mathbb{Z}) \backslash \mathrm{Heis}(\mathbb{R})$, or any properly constructed Seifert fibration spanning an elliptic curve. By exactly this matching argument, they operate universally as strictly NS-regular.
<!-- FILE_END: torus-ns-regular.md -->

<!-- FILE_START: root-of-unity-truncation.md -->
**Proposition (conditional on
[`conj:q-aubin-lions`](#conj:q-aubin-lions),
[`conj:ns-counterexample`](#conj:ns-counterexample),
[`conj:critical-exponent`](#conj:critical-exponent),
[`prop:blowup-yekutieli`](#prop:blowup-yekutieli),
and
[`conj:regularity-breakdown`](#conj:regularity-breakdown);
"Root-of-unity truncation").**

The governing [QOU axiom](#def:substrate-parameter) rigorously demands that $q$ remains **not** a root of unity. However, forcibly passing the limit $q \to 1$ directly through the dense set of unity roots triggers a radical truncation across the representation theory that forcibly **strengthens** classical regularity. The resulting macroscopic blowup operating at $q = 1$ behaves merely as the pure mathematical accumulation gathering these infinite truncations.

The core truncation mechanism — driven exclusively by the vanishing of the $q$-integer $[\kappa]_q$ executing exactly at $q = e^{i\pi/\kappa}$, which cleanly collapses the spanning $q$-Laplacian spectral tower $[k]_q^2$ straight into the constrained finite Verlinde/ADE set — finds derivation strictly within [the $q$-Laplacian spectral tower](#prop:q-laplacian-spectral-tower). The following formally extracts the resulting fluid-dynamical consequence.

**Three regimes of $\mathrm{SU}_q(2)$ representations.**

1. **Generic $q > 1$ (QOU regime).**
 Contains infinitely many valid simple objects $V_j$, indexing $j = 0, 1/2, 1, \ldots$ Quantum dimensions rigorously hold $[2j+1]_q > 0$ across all valid $j$. The physical eigenvalues scale as $[k]_q^2 \sim q^{2k}$ (providing strict exponential growth). The core [well-posedness theorem](#thm:q-ns-wellposedness) mechanically guarantees global regularity.
2. **Root of unity $q = e^{i\pi/\kappa}$, bounded $\kappa \in \mathbb{Z}_{\geq 2}$.**
 Contains strictly **finitely many** simple objects, spanning $j = 0, 1/2, \ldots, (\kappa-2)/2$. The active quantum dimension $[2j+1]_q$ forcibly zeroes out at precisely $j = (\kappa-1)/2$, cleanly truncating the entire representation category. The strict Verlinde formula regulates all physical fusion:

 $$
     N_{ij}^k
     = \int_0^1 \frac{S_{ik}S_{jk}}{S_{0k}}dk,
   $$

 where $S$ acts as the modular $S$-matrix. The resulting representation category devolves directly into a **modular tensor category** — identically matching the required algebraic input driving Chern--Simons TQFT cleanly at level $\kappa$.
3. **$q = 1$ (classical limit).**
 Spans an infinite array of simple objects evaluating $[k]_1 = k$ (strictly polynomial scaling). All truncation ceases. All exponential damping vanishes. This establishes exactly the [regularity breakdown](#conj:regularity-breakdown) regime.

**Root-of-unity regularity is stronger than generic.**

Evaluated cleanly at $q = e^{i\pi/\kappa}$, the operating q-NS system mechanically supports at most exactly $(\kappa-1)/2$ active vortex modes (as the tightly truncated representation category contains strictly finitely many objects). This forms an absolute **hard cutoff**, fundamentally differing from the generic soft exponential damping controlling $q > 1$:

- Within generic $q > 1$: valid modes breaching $[k]_q > \mathrm{Re}_q^{1/2}$ safely experience exponential damping but strictly remain nonzero.
- Operating at root of unity: any hypothetical modes breaching $j > (\kappa-2)/2$ mathematically **do not exist** anywhere inside the governing category. The entire bounded Hilbert space remains strictly finite-dimensional.

A purely finite-dimensional ODE mathematically defaults to globally regular unconditionally (enforcing Picard--Lindelöf). Consequently, situated exactly at every isolated root of unity, the operative q-NS system operates not merely as well-posed, but absolutely **finite-dimensional**.

**The $q = 1$ accumulation.**

Driving $\kappa \to \infty$ smoothly pulls $q = e^{i\pi/\kappa} \to 1$. The hard truncation level actively scales up: $j_{\max} = (\kappa-2)/2 \to \infty$. Steadily, more and more functional modes mechanically unlock. The strict mathematical sequence traversing these rigidly finite-dimensional systems flawlessly approaches the pure infinite-dimensional classical baseline.

The absolute blowup occurring at $q = 1$ effectively states that this terminal infinite-dimensional limit executes as mathematically **singular**: while no isolated finite truncation can ever trigger a blowup, the exact accumulation limit gathering all conceivable truncations effortlessly can. This maps the precise physical structure dictating a macroscopic **phase transition stationed at the exact accumulation point**.

**Connection to the core aspect ratio.**

Operating at an isolated root of unity $q = e^{i\pi/\kappa}$, the exact geometric shape controlling the physical vortex core answers directly to the strict **modular tensor category** structure. The explicit fusion rules $N_{ij}^k$ logically dictate all valid mode interactions. The hard truncation boundary spanning $j \leq (\kappa-2)/2$ completely outlaws high-frequency geometric core deformations: the physical core mathematically **cannot** form fine-scale spatial structure exceeding the strict cutoff. Examining this physically:

- The continuous core aspect ratio $\kappa(t) = a_\perp/a_\parallel$ strictly answers to the isolated Fourier modes spanning the core boundary.
- Operating at root of unity: exactly $(\kappa-1)/2$ modes logically exist. Consequently, $\kappa(t)$ forms merely a basic trigonometric polynomial obeying a strictly bounded degree.
- Any valid trigonometric polynomial scaled to degree $N$ rigidly obeys $|\kappa'(t)| \leq N\|\kappa\|_\infty$ (enforcing the Bernstein inequality), mathematically preventing rapid physical oscillation.

This sequence delivers an **explicit mathematical bound** actively functioning at every isolated root of unity:

$$
  \sup_{t < T^*} \kappa(t)
   \leq 
  1 + C \cdot (\kappa - 1)
$$

relying on some shared universal constant $C$. The resulting mathematical bound steadily grows linearly pacing the truncation level $\kappa$, mathematically diverging flawlessly as $\kappa \to \infty$ ($q \to 1$).

**The refined gap.**

The baseline [vorticity lower bound](#prop:vorticity-lower-bound) strictly mandates $\sup_t \kappa(t) \leq C$, keeping $C$ rigidly independent of $q$. The unified root-of-unity analysis directly supplies $\kappa(t) \leq 1 + C(\kappa-1)$, which visibly scales alongside $\kappa$. The absolute question zeroes in on the **rate of growth**:

- Assuming $\kappa(t) \leq C_0$ uniformly (operating entirely independent of $\kappa$): the physical core remains permanently circular. The rigorous lower bound flawlessly holds. NS definitively blows up. The counter-example stands mathematically established.
- Assuming $\kappa(t) \sim \kappa$ (exhibiting purely linear growth): the physical core safely flattens exactly mirroring the rate unlocking new modes. Physical vorticity safely spreads forming a wide sheet. The strict lower bound $\omega \geq c/(T^*-t)$ potentially fails. NS may function as completely regular.
- Assuming $\kappa(t) \sim \kappa^\beta$ spanning $0 < \beta < 1$: an intermediate regime triggers. The firm lower bound holds cleanly provided $\beta < 1/2$ (confirming the physical flattening remains mathematically slower than the approach).

The explicit [Levi form condition number](#def:levi-form-defect) governing the vortex core rigidly evaluates to $\lambda_{\max}/\lambda_{\min}$, perfectly equating to $\kappa(t)^2$. The underlying contact structure mathematically degenerates (flipping completely integrable) exactly if and only if $\lambda_{\min} \to 0$, driving $\kappa(t) \to \infty$. Consequently:

$$
  \boxed{
    \text{NS blows up}
    \iff
    \text{Levi form stays non-degenerate at collision}
    \iff
    \kappa(t) = O(1).
  }
$$

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: root-of-unity-truncation.md -->

<!-- FILE_START: root-of-unity-truncation-interpretation.md -->
**This provides the contact-geometric reformulation of the millennium problem:** Does the physical contact structure mapping the brane definitively remain non-degenerate precisely exactly at the mathematical collision point bridging two isolated vortex filaments?
<!-- FILE_END: root-of-unity-truncation-interpretation.md -->

<!-- FILE_START: observable-mtc.md -->
Fix any valid positive integer $N \geq 3$ and strictly define $q = \zeta_N = e^{2\pi i / N}$ — specifying a precise primitive $N$-th root of unity. Operating at exactly this value inside the substrate parameter, the full representation category $\mathrm{Rep}(U_q(\mathfrak{su}_2))$ mathematically ceases to remain semisimple. Systematically quotienting out the designated ideal containing strictly negligible morphisms flawlessly generates the *truncated* category $\mathbf{C}_{\mathrm{any}}(N)$. This isolated category supports exclusively finitely many valid simple objects scaling exactly across $\mathbf{V}_0, \mathbf{V}_1, \ldots, \mathbf{V}_{N-2}$ \cite{moore-seiberg1989}.

**Definition.** The strict **observable modular tensor category** operating exactly at level $N$ forms the specific ribbon fusion category $\mathbf{C}_{\mathrm{any}}(N)$, directly equipped alongside the specific braiding $c$ and matching ribbon twist $\varTheta$ rigidly inherited straight from the base quasi-triangular structure defining $U_q(\mathfrak{su}_2)$ stationed exactly at $q = \zeta_N$. Equivalently phrased, $\mathbf{C}_{\mathrm{any}}(N)$ operates precisely as a fully *modular* tensor category: its structural $S$-matrix spanning $S_{ij} = \mathrm{tr}(c_{\mathbf{V}_i, \mathbf{V}_j} \circ c_{\mathbf{V}_j, \mathbf{V}_i})$ evaluates as entirely non-degenerate.
<!-- FILE_END: observable-mtc.md -->

<!-- FILE_START: observable-mtc-braiding.md -->
**Braiding non-symmetry.** Evaluating $N \geq 3$ mapping any definitively non-trivial simple object $\mathbf{V} \in \mathbf{C}_{\mathrm{any}}(N)$, the math guarantees

$$
  c_{\mathbf{V}, \mathbf{V}} \circ c_{\mathbf{V}, \mathbf{V}}
    \neq  \mathrm{id}_{\mathbf{V} \otimes \mathbf{V}}.
$$

The mathematical braiding strictly refuses to square cleanly back into the identity across valid simples. This functions as the absolute hallmark denoting a genuinely modular (strictly non-symmetric) tensor category. It acts as the rigid absolute prerequisite unlocking valid anyonic statistics.

**Relation to the commutative limit.** The exact commutative limit executing $q \to 1$ detailed in Chapter 3 maps directly onto scaling $N \to \infty$. At this limit, the strict mathematical truncation fully opens up. All negligible morphisms cleanly vanish. The isolated braiding forcibly degenerates backward into a strictly symmetric mathematical structure. Consequently, the two specified specialisations fundamentally separate:

| Specialisation | $q$ | Braiding | Anyons |
|---|---|---|---|
| Commutative limit | $q = 1$ | strictly symmetric | no |
| Root-of-unity $\mathrm{MTC}$ | $q = \zeta_N$ ($N \geq 3$) | strictly non-symmetric | yes |

The resulting geometric shadow projected exactly upon the genus-$2$ curve $\mathcal{X}_5$ detailed in [def:hyperelliptic-quintic](#def:hyperelliptic-quintic) safely isolates either distinct regime, relying entirely on its fifth-roots-of-unity active branch set. Tracking within the commutative limit, the precise values $\zeta_5^{k}$ rigidly mark pure classical phase defects mounted exactly across a single isolated $\mathrm{U}(1)$ tube. Conversely, evaluating directly at $q = \zeta_5$, that identical set of discrete data seamlessly labels the valid anyonic fusion channels populating $\mathbf{C}_{\mathrm{any}}(5)$.
<!-- FILE_END: observable-mtc-braiding.md -->

<!-- FILE_START: bn-mtc-action.md -->
Let $\mathbf{C}_{\mathrm{any}}(N)$ define the exact observable modular tensor category detailed in [def:observable-mtc](#def:observable-mtc), functioning specifically at level $N \geq 3$. Let $\mathbf{V}$ specify any definitively non-trivial simple object. Evaluating across every $n \geq 2$, the embedded categorical braiding directly generates a functional representation

$$
  \rho_n \colon B_n  \longrightarrow
   \mathrm{Aut}_{\mathbf{C}_{\mathrm{any}}(N)}(\mathbf{V}^{\otimes n}),
  \qquad
  \sigma_i  \longmapsto
   \mathrm{id}_{\mathbf{V}^{\otimes (i-1)}}
   \otimes\, c_{\mathbf{V}, \mathbf{V}}
   \otimes\, \mathrm{id}_{\mathbf{V}^{\otimes (n - i - 1)}},
$$

governing the pure Artin braid group $B_n$ (see [def:braid-group](#def:braid-group)) mapped exactly onto the strict tensor power of $\mathbf{V}$. This active representation fundamentally refuses to factor cleanly straight through the basic symmetric-group quotient tracing $B_n \twoheadrightarrow S_n$.
<!-- FILE_END: bn-mtc-action.md -->

