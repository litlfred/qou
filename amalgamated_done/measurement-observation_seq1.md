<!-- FILE_START: bundle-observation-intro.md -->
The knot-particle dictionary assigns a particle to each knot composite but leaves the carrier untouched. We now make the carrier explicit. A bundle initial condition fixes the data over the brane, the observation map factors through a braid, and the resulting sorting deposits energy $q + q^{-1}$ per crossing in the colour fibre.

The argument proceeds from the physical reading of the Borromean composite to the bundle initial data it fixes over the brane, and then to observation itself. The load-bearing step proves that sorting deposits energy in the colour fibre—observation is an open braid map whose internal crossings each pay the Hecke-eigenvalue cost. From there the picture acquires dynamics: isotopic bundle data as the same physical state, torsion-driven flow through configuration space, and its categorical home as finite bundles over $\mathbb{P}(V)$.
<!-- FILE_END: bundle-observation-intro.md -->

<!-- FILE_START: quarks-borromean-picture.md -->
We reassign quarks from individual knot types to Borromean-linked unknots. With this identification, a baryon's mass arises almost entirely from the Borromean linking volume, matching the QCD result that ${\sim}99\%$ of proton mass is binding energy.

The original dictionary assigned individual knot types to quarks. The revised picture identifies quarks as unknots (neutrinos) Borromean-linked in the exceptional divisor of Bring's surface. A baryon is the Borromean link $\mathcal{B}_3(\nu_r, \nu_g, \nu_b)$ bound by the Hopf link $\mathcal{L}_H$:

- **Proton**: $\mathcal{B}_3(\nu_r, \nu_g, \nu_b) \oplus \mathcal{L}_H$ with the $2 + 1$ crossing-orientation partition (two up, one down).
- **Neutron**: $\mathcal{B}_3(\nu_r, \nu_g, \nu_b) \oplus \mathcal{L}_H$ with the $1 + 2$ partition (one up, two down).

Up/down flavour arises from the crossing orientation of each unknot within $\mathcal{B}_3$, not from distinct knot types. The baryon mass comes almost entirely from the Borromean linking volume $\mathrm{Vol}(S^3 \setminus \mathcal{B}_3) = 7.328\ldots$.

The mass of each hadron is determined by the terminal resolution, matching CODATA values to sub-keV precision.
<!-- FILE_END: quarks-borromean-picture.md -->

<!-- FILE_START: bundle-initial-conditions.md -->
A measurement records where each constituent sits on the fibre while leaving its momentum entirely free. A **bundle initial condition** is the object that encodes exactly this position-only data. Over the projective line $\mathbb{P}(V)$ at a reference point in an affine chart, it is a formal sum of localized hadrons and photons at base points:

$$
  \mathcal{S}_0 = \sum_{i \in I} (p_i, H_i)
$$

where each $(p_i, H_i)$ is a localized hadron or a photon. The photon identity $\mathbf{1}_{B_4}$ is knot-trivial under Markov closure yet carries four internal polarisation/chirality components on the exceptional divisor. The index set $I$ may be infinite, and multiple constituents may share the same base point.

Equivalently, $\mathcal{S}_0$ is a section of the free commutative monoid on the hadron sheaf $\mathcal{H}$:

$$
  \mathcal{S}_0 \in \Gamma\!\bigl(\mathbb{P}(V), \mathrm{Free}_{\mathrm{CMon}}(\mathcal{H})\bigr).
$$

This specifies the fibre data of the bundle—which constituent sits in which fibre—without any information about the horizontal transport connecting neighbouring fibres.

Subsequent configurations $\mathcal{S}_1, \mathcal{S}_2, \ldots$ represent the forward light cone from $\mathcal{S}_0$. Each step applies one iteration of the Reeb flow, adding horizontal transport and accumulating interaction relations. The backward sequence represents the past light cone.
<!-- FILE_END: bundle-initial-conditions.md -->

<!-- FILE_START: observation-braid.md -->
An observation injects genuinely new information. Its outcome is not necessarily determined by the initial conditions $\mathcal{S}_0$. This is the open-map property: observation maps open sets in the state space to open sets, creating new open neighbourhoods not present in $\mathcal{S}_0$.

In the braid picture, an observation inserts a new crossing into the braid word. The crossing type is not forced by the existing braid. Each observation is one crossing injected at a discrete Planck step, supplying one bit of information. 

The Toffoli gate requires three crossings. An observer performing one Toffoli computation injects three crossings into the braid, corresponding to three Planck steps of intentional interaction with the state bundle.
<!-- FILE_END: observation-braid.md -->

<!-- FILE_START: observation-intent-energy.md -->
Choosing to sort a sequence of items inserts crossings that increase local order (decreasing classical entropy) at the cost of quantum energy ($\delta q > 0$ per crossing). Every observation costs at least one crossing's worth of $\hbar_q$.

An observation is done with intent. Physically, intent increases the quantum energy of the system. The substrate perturbation $\delta q > 0$ shifts $q$ upward, increasing the quantum Planck constant $\hbar_q = 1 - q^{-1}$. The crossing energy of the injected crossing is the energetic cost of the observation.

The intent can either increase or decrease the classical energy of the system provided the change is continuous. It cannot leave the quantum energy unchanged.
<!-- FILE_END: observation-intent-energy.md -->

<!-- FILE_START: observation-braid-not-predetermined.md -->
The initial conditions $\mathcal{S}_0$ specify fibre data without horizontal transport. The braid that unfolds from $\mathcal{S}_0$ encodes the horizontal transport. Observations modify this braid in real time. The full braid word of the universe interleaves two sources:

1. **The flow**: Crossings generated by the autonomous Reeb dynamics of the state bundle, determined by $\mathcal{S}_0$ and the variational equations.
2. **Observations**: Crossings injected by observers via the adjoint action on the colour fibre, determined by open-map contributions, not by $\mathcal{S}_0$.

Suppose the flow winds three colour fibres into $\sigma_1\sigma_2$. An observer measuring the first and third strands injects a single inverse crossing $\sigma_1^{-1}$, completing the word to $\sigma_1\sigma_2\sigma_1^{-1}$. No autonomous continuation of $\mathcal{S}_0$ would have produced this finite braid. The observation does not perturb the flow; it appends a crossing the flow could not.

The open map structure of observation implies that the set of reachable sections is larger than the set determined by the initial conditions alone. Observers expand the computable fragment of the universe.
<!-- FILE_END: observation-braid-not-predetermined.md -->

<!-- FILE_START: sorting-color-energy.md -->
Observation sorts colour. Swapping two adjacent items into their correct order is a projection between the two eigenspaces of the R-matrix. Each swap deposits a fixed quantum of energy in the colour fibre.

**Proposition.**
*Let $\sigma_i$ be the Hecke generator acting on $V \otimes V$, where $V$ is the fundamental representation. Then:*

1. **(Eigenspace decomposition.)** *The R-matrix decomposes $V \otimes V$ into two eigenspaces:*

   $$
     V \otimes V = \mathrm{Sym}^2(V) \oplus \textstyle\bigwedge^2(V)
   $$

   *with eigenvalues $q$ (symmetric, ordered) and $-q^{-1}$ (antisymmetric, disordered) respectively.*

2. **(Sorting is projection.)** *A sorting operation is the projection from $\bigwedge^2(V)$ to $\mathrm{Sym}^2(V)$ at the generator $\sigma_i$. This projection acts on the colour fibre by rotating the gauge degrees of freedom from the disordered to the ordered eigenspace.*

3. **(Energy per crossing.)** *The energy deposited in the colour fibre by one sorting operation is the eigenvalue gap:*

   $$
     \Delta E_{\mathrm{colour}} = q - (-q^{-1}) = q + q^{-1}
   $$

   *At $q = q_0$, $\Delta E = 2.011$ action units per crossing.*

4. **(Total sorting energy.)** *Let $\pi \in S_n$ be a permutation representing the disordered state of $n$ items. The minimum number of adjacent transpositions needed to sort $\pi$ is the inversion count $\mathrm{inv}(\pi)$. The total energy deposited is:*

   $$
     E_{\mathrm{colour}}(\pi) = \mathrm{inv}(\pi) \cdot (q + q^{-1})
   $$
<!-- FILE_END: sorting-color-energy.md -->

<!-- FILE_START: bundle-isotopy-equivalence.md -->
The physical content of a bundle initial condition depends only on which hadron types are placed where, not on the index labels or the particular representative of each ambient isotopy class. Two bundle initial conditions are **isotopy equivalent** if they are related by a permutation of indices and an ambient isotopy within each fibre:

$$
  \{(p_i, H_i)\}_{i \in I} \sim \\{(p_{\sigma(i)}, H_{\sigma(i)}')\\}_{i \in I}
$$

where $\sigma$ is a bijection on $I$ and each $H_{\sigma(i)}'$ is ambient-isotopic to $H_{\sigma(i)}$ in the fibre $E_{p_{\sigma(i)}}$.
<!-- FILE_END: bundle-isotopy-equivalence.md -->

<!-- FILE_START: torsion-knot-flow.md -->
Given a bundle initial condition $\mathcal{S}_0 = \{(p_i, K_i)\}_{i=1}^{N}$, the **torsion-driven knot flow** is the one-parameter family of bundle states

$$
  \mathcal{S}_t = \bigl\{\bigl(\Phi_t^q(p_i), K_i\bigr)\bigr\}_{i=1}^{N} \qquad t \geq 0,
$$

where $\Phi_t^q$ is the flow on $\mathbb{P}(V)$ generated by the $q$-deformed Reeb vector field $\xi_q$.

The flow has two components:

1. **Intrinsic rotation.** Each knot type $K$ carries an intrinsic angular momentum proportional to its crossing number $c(K)$:

   $$
     \omega_K = c(K) \cdot \frac{2\pi}{[c(K)]_q!}
   $$

   This drives geodesic motion on $\mathbb{P}(V) \cong S^2$.

2. **Pairwise interaction.** When two localized knots $(p_i, K_i)$ and $(p_j, K_j)$ are within Planck-scale separation $d_{\mathbb{P}(V)}(p_i, p_j) < \ell_P$, they experience a short-range repulsive force

   $$
     F_{ij} = \frac{\Delta_q(K_i) \cdot \Delta_q(K_j)}{d(p_i, p_j)^2 + \ell_P^2}
   $$

   where $\Delta_q(K)$ is the $q$-Alexander polynomial of $K$ evaluated at $q = e^{-r}$.

The flow preserves the total knot content $\sum_i K_i$ but redistributes positions on $\mathbb{P}(V)$. Categorically, the flow is a natural transformation on the category $\mathrm{Bun}(\mathbb{P}(V))$ of finite bundles over the projective line.

**Archimedean specialisation.** The combinatorial knot data lives over the ground ring $R_q = \mathbb{Z}[q, q^{-1}]$. The angular-momentum normalisation, the round metric on $S^2$, and the evaluation $q = e^{-r}$ are the archimedean specialisation over $\mathbb{R}$.
<!-- FILE_END: torsion-knot-flow.md -->

<!-- FILE_START: bundle-category.md -->
This category serves as the categorical counterpart of the Feynman path integral. Rather than integrating over all field configurations, we follow a single deterministic flow on a finite bundle. A configuration is a fixed collection of knots pinned to base points in the projective fibres. The content of the theory is the trajectory that configuration traces as the torsion flow carries it forward.

The bundle initial conditions and the torsion-driven knot flow define a category $\mathrm{Bun}(\mathbb{P}(V))$:

- **Objects**: Bundle initial conditions $\mathcal{S}_0 = \{(p_i, K_i)\}$.
- **Morphisms**: Pairs $(\sigma, \{\phi_i\})$ consisting of a permutation $\sigma \in S_N$ and a family of ambient isotopies $\phi_i \colon K_{\sigma(i)} \simeq K_{\sigma(i)}'$ in the respective fibres. Morphisms preserve total knot content.
- **Identity**: The identity permutation with trivial isotopies.
- **Composition**: Permutation composition followed by isotopy concatenation.

The torsion flow $\Phi_t^q$ is an endofunctor $\Phi_t^q \colon \mathrm{Bun}(\mathbb{P}(V)) \to \mathrm{Bun}(\mathbb{P}(V))$ acting on objects by moving base points and on morphisms by conjugating isotopies with the flow. The family $\{\Phi_t^q\}_{t \geq 0}$ assembles into a continuous functor from $(\mathbb{R}_{\geq 0}, +)$ into the endofunctor category $\mathrm{End}(\mathrm{Bun}(\mathbb{P}(V)))$. The physics is the trajectory $t \mapsto \mathcal{S}_t$.
<!-- FILE_END: bundle-category.md -->

<!-- FILE_START: outro-measurement-observation.md -->
This closes the measurement-and-observation chapter. Quarks reside in a Borromean configuration. Bundle initial conditions fix the observable's pre-state, the observation braid sorts colour by energy, and the bundle-category-level isotopy equivalence pins the measurement classes. Together, these constitute the bundle-structure picture, identifying observation as a categorical torsion-knot flow on the state bundle $\mathcal{S}$.

The next chapter lifts these measurement constructions to the archimedean side and identifies the spacetime base—the Bring surface $\mathcal{E}_q$—on which the bundle category lives. The orbital symmetry and cohomological embedding from that chapter inherit the measurement structure recorded here.
<!-- FILE_END: outro-measurement-observation.md -->
