<!-- FILE_START: horizons-aeons-intro.md -->
The incompleteness horizon of the previous section remains local to a single resolution tree. We now globalise it. The brane tower $A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$ stratifies every affine chart by jet order. A horizon forms as a codimension-$1$ locus where the lowest floor $A_0$ vanishes, allowing higher floors to leak through. This section defines these horizons, organises their connected components into aeons, and links the resulting cyclic structure to Penrose's Conformal Cyclic Cosmology.

Definition: Jet horizon (degree-$0$ vanishing locus) establishes the horizon ideal $\mathfrak{h} \subset \Gamma(U, A_0)$. It dictates that photons remain blocked at the horizon, while degree $\geq 1$ Taylor coefficients escape. Definition: Big bang state (degree-$0$ trivial configuration) reframes this condition as an initial datum. Definition: CMB as boundary datum of a big bang state isolates the surviving degree-$1$ and degree-$2$ jet data. Remark: The CMB as photon color content surviving the horizon interprets this data as photon polarization and color content. Remark: Hawking radiation as degree $\geq 1$ leakage recovers the Bekenstein--Hawking entropy as the rank of $\Gamma(\mathcal{H}, A_1/A_0)$.

Categorical packaging follows. Definition: Observable subcategory $\mathrm{Bun}^{\circ}(\mathbb{P}(V))$ isolates the locus where $A_0$ does not vanish. Definition: Aeon identifies a connected component of that subcategory. Definition: Horizon functor and Definition: CMB functor map each aeon to its boundary and its surviving jet data. The Conjecture: Aeon recycling: $\Phi_1^q \circ \mathrm{CMB}$ lands in $\mathrm{Bun}^{\circ}$ posits that the boundary datum regenerates a chart under one Planck step of the torsion flow. Proposition: Conformal invariance at the jet horizon and Proposition: A QOU with aeons is a conformal cyclic cosmology align this structure with Penrose's framework. Remark: Relation to Penrose's Conformal Cyclic Cosmology supplies the required translation dictionary. The next section, **Quantum Geometry Variants**, applies the aeon boundary and degree-$0$ vanishing to model alternative Euler-characteristic scenarios for the descended universe. _(draft.)_
<!-- FILE_END: horizons-aeons-intro.md -->

<!-- FILE_START: jet-horizon.md -->
Let $U \subset M_0$ be an open subset of the descended universe carrying an affine chart. Let $A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$ be the brane tower .

A **jet horizon** in $U$ is a closed codimension-$1$ subset $\mathcal{H} \subset U$ such that every section of $A_0$ extending continuously across $\mathcal{H}$ vanishes on $\mathcal{H}$:

$$
  \mathcal{H}
  = 
  V\!\bigl(\mathfrak{h}\bigr),
  \qquad
  \mathfrak{h}
  = 
  \bigl\{
    s \in \Gamma(U, A_0)
     : 
    s|_{\mathcal{H}} = 0
  \bigr\}.
$$

The ideal $\mathfrak{h} \subset \Gamma(U, A_0)$ is the **horizon ideal**. At degree $0$, no fibre data crosses $\mathcal{H}$: photons ($K = \mathbf{1}_{B_4}$ 4-strand id, step $0$) cannot propagate across the horizon, and no zeroth-order observable distinguishes one side from the other.

**Higher-degree leakage.**
The horizon ideal lives strictly in $A_0$. The quotient algebras $A_k / A_0$ for $k \geq 1$ are not constrained by $\mathfrak{h}$. First-order (linear) and second-order (curvature) jet data can carry non-trivial sections across $\mathcal{H}$. 

| Jet degree | Data type | Crosses $\mathcal{H}$? |
|:---:|:---|:---:|
| $0$ | Fibre value (photon identity) | **No** |
| $1$ | Linear transport (winding number) | Yes |
| $2$ | Curvature (linking number) | Yes |
| $\geq 3$ | Higher-order topology | Yes |

The information that leaks through a jet horizon is exactly the degree $\geq 1$ jet data: the Taylor coefficients of the energy function beyond the constant term. This leakage is thermal in character. It carries no particle identity (degree $0$), only statistical correlations (degrees $1$ and $2$).
<!-- FILE_END: jet-horizon.md -->

<!-- FILE_START: big-bang-state.md -->
Let $U \subset M_0$ be an affine chart carrying a bundle initial condition $\mathcal{S}_0 = \sum_i (p_i, H_i)$ .

**Definition.** A **big bang state** is a bundle initial condition with a trivial degree-$0$ algebra:
$$
  \mathcal{S}_0 \text{ is a big bang state}
  \quad\Longleftrightarrow\quad
  \Gamma\!\bigl(U, A_0|_{\mathcal{S}_0}\bigr) = 0.
$$

Equivalently, every constituent satisfies $H_i = \varnothing$ (a photon with zero fibre data), and the section $s_0 \in \Gamma(U, A_0)$ encoding their identity vanishes. There are no degree-$0$ observables at $\mathcal{S}_0$. The remaining higher-jet data—sections of $A_1/A_0$ (linear transport) and $A_2/A_0$ (curvature)—provides the seed for the forward light cone $\mathcal{S}_1, \mathcal{S}_2, \ldots$

**Relation to the jet horizon.**
A big bang state is algebraically identical to the data on one side of a jet horizon . Both are characterised by the vanishing of $A_0$. The difference is purely contextual:

| Concept | Algebraic condition | Role |
|:--------|:---:|:---|
| Jet horizon | $A_0\vert_{\mathcal{H}} = 0$ | Boundary within an affine chart |
| Big bang state | $A_0\vert_{\mathcal{S}_0} = 0$ | Reference configuration of an affine chart |

A jet horizon is a boundary. A big bang state is an initial condition. The same vanishing ideal $\mathfrak{h}$ describes both.

**Existence is not assumed.**
Whether any affine chart in the descended universe admits a big bang state is a dynamical question, not an axiom. The framework accommodates three consistent scenarios:
- Every affine chart has a big bang state (global initial singularity).
- Only some charts have a big bang state.
- No chart has a big bang state (the backward light cone extends indefinitely).
<!-- FILE_END: big-bang-state.md -->

<!-- FILE_START: cmb-boundary-datum.md -->
The cosmic microwave background records the initial state of an aeon. We model this as the boundary jet data surviving at a big bang state.

Let $\mathcal{S}_0$ be a big bang state  in an affine chart $U$. Let $A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$ be the associated brane tower . The **cosmic microwave background** (CMB) of $\mathcal{S}_0$ is the boundary datum

$$
  \mathrm{CMB}(\mathcal{S}_0)
  = 
  \bigl(
    \Gamma(U, A_1/A_0)|_{\mathcal{S}_0}, 
    \Gamma(U, A_2/A_0)|_{\mathcal{S}_0}
  \bigr).
$$

This pair isolates the degree-$1$ (linear transport) and degree-$2$ (curvature) jet data at $\mathcal{S}_0$. Because $A_0|_{\mathcal{S}_0} = 0$, we can equivalently restrict $A_1 \oplus A_2$:

$$
  \mathrm{CMB}(\mathcal{S}_0)
   \cong 
  \bigl(A_1 \oplus A_2\bigr)\big|_{\mathcal{S}_0}.
$$

The jet degrees dictate the physical content.

| Degree | Jet data | Physical content |
|:---:|:---|:---|
| $1$ | $A_1/A_0$: linear transport | Photon polarization modes ($\sigma_0, \sigma_1$), winding numbers, first-order correlations |
| $2$ | $A_2/A_0$: curvature | Hopf-link cross-terms ($L_{\pm}$), linking numbers, power spectrum |

Because degree-$0$ data ($A_0$) vanishes at the boundary, the CMB lacks photon identity $\mathbf{1}$, particle labels, and knot types. It is strictly thermal. It carries only the **color content** $(\varphi_0, \varphi_1)$ of the boundary photons .

When $\mathcal{S}_0$ bounds the past of an aeon $\mathcal{A}$ , the CMB seeds the forward light cone. The initial Planck step $\mathcal{S}_0 \to \mathcal{S}_1$ generates particles. It applies the Reeb flow $f_q$ to the degree-$1$ transport data, regenerating non-trivial degree-$0$ data. 

When $\mathcal{S}_0$ also bounds the future of a preceding aeon $\mathcal{A}'$, the datum inherits from the terminal horizon of $\mathcal{A}'$ . The thermal remnant of one aeon becomes the initial condition of the next.
<!-- FILE_END: cmb-boundary-datum.md -->

<!-- FILE_START: cmb-photon-color-content.md -->
We decompose a photon into identity and color components. The photon color content model  writes a photon as:

$$
  \gamma
  = 
  \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
  + \varphi_{01}\sigma_0\sigma_1,
  \qquad \varphi_0, \varphi_1, \varphi_{01} \in R.
$$

Here $\mathbf{1}$ is the degree-$0$ photon identity, $\sigma_0, \sigma_1$ are the Hecke generators, and $\sigma_0\sigma_1$ is the Hopf link dressing . Each generator maps to a polarization mode on the exceptional divisor $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$. The generator $\sigma_0$ provides horizontal polarization; $\sigma_1$ provides vertical.

## Decomposition by jet degree

The four summands distribute across jet degrees.

| Summand | Jet degree | Role | Survives horizon? |
|:---:|:---:|:---|:---:|
| $\mathbf{1}$ | $0$ | Photon identity (fibre value) | **No** |
| $\varphi_0\sigma_0$ | $1$ | Horizontal polarization (linear transport) | **Yes** |
| $\varphi_1\sigma_1$ | $1$ | Vertical polarization (linear transport) | **Yes** |
| $\varphi_{01}\sigma_0\sigma_1$ | $2$ | Hopf link dressing (quadratic transport) | **Yes** |

At a jet horizon $\mathcal{H}$ , the degree-$0$ ideal $\mathfrak{h}$ annihilates $A_0$, removing the photon identity $\mathbf{1}$. Because the higher-degree quotients $A_1/A_0$ and $A_2/A_1$ are unconstrained, the color content $(\varphi_0, \varphi_1, \varphi_{01})$ survives the horizon.

## Surviving color content

The CMB boundary datum  at a big bang state $\mathcal{S}_0$ collects the degree $\geq 1$ jet data surviving the horizon. As a collection of photons $\{\gamma_k\}$ approaches the boundary, their degree-$0$ identities $\mathbf{1}_k$ vanish. Their color weights $(\varphi_{0,k}, \varphi_{1,k})$ persist as sections of $A_1/A_0$.

The CMB aggregates the color content of the boundary photons:

$$
  \mathrm{CMB}(\mathcal{S}_0)\big|_{\text{degree }1}
   \sim 
  \sum_k
  \bigl(\varphi_{0,k}\sigma_0 + \varphi_{1,k}\sigma_1\bigr).
$$

The components $\sigma_0$ and $\sigma_1$ determine the independent polarization modes of the CMB.

| CMB observable | Photon color content | Jet data |
|:---|:---|:---|
| Temperature anisotropy | $\varphi_{0,k} + \varphi_{1,k}$ (total color weight) | Trace of $A_1/A_0$ |
| $E$-mode polarization | $\varphi_{0,k} - \varphi_{1,k}$ (polarization asymmetry) | Difference of $\sigma_0, \sigma_1$ modes |
| $B$-mode polarization | Cross-terms $\varphi_{0,k}\varphi_{1,j}$ ($k \neq j$) | Degree-$2$ Hopf-link contributions ($L_{\pm}$) |

The degree-$2$ data ($A_2/A_0$) detects linking between photons. It isolates the Hopf-link terms $L_{\pm} = \sigma_0\sigma_1$ and $\sigma_1\sigma_0$ from the product formula . These pairwise correlations generate the CMB power spectrum.

## Condensation

The initial Planck step condenses the CMB back into particles. When the Reeb flow $f_q$ acts on the boundary datum , the degree-$1$ color content $(\varphi_0, \varphi_1)$ reconstitutes degree-$0$ identities via the Hecke relation:

$$
  \sigma_i^2
  = 
  (q - q^{-1})\sigma_i + \mathbf{1}.
$$

Each color mode iterates to generate a photon identity $\mathbf{1}$ (the constant term) alongside a residual color mode $\sigma_i$ (the linear term). The Hecke self-energy algebraically converts surviving polarization data into particle states.
<!-- FILE_END: cmb-photon-color-content.md -->

<!-- FILE_START: hawking-radiation.md -->
The jet horizon  provides an algebraic model of a black hole event horizon.

Hawking radiation \cite{hawking1975} predicts that black holes emit thermal radiation at temperature $T_H = \hbar c^3 / (8\pi G M k_B)$. This radiation carries no internal information. It exhibits a Planck spectrum determined entirely by the mass $M$.

The jet-horizon framework translates this into a direct algebraic interpretation:

1. **Degree-$0$ data is trapped.** The horizon ideal $\mathfrak{h} \subset A_0$ blocks all zeroth-order sections. No particle identity (knot type or crossing structure) crosses the horizon. This states the information paradox algebraically: the full fibre data of $A_0$ remains inaccessible from the outside.

2. **Degree $\geq 1$ data leaks.** The quotients $A_1/A_0$ and $A_2/A_0$ carry non-trivial sections across $\mathcal{H}$. These constitute the first and second Taylor coefficients of the energy function (linear transport as winding number, curvature as linking number). This data is thermal. It depends on statistical properties (temperature $\sim \eta_q$, operational entropy ) rather than individual particle states.

3. **The Bekenstein--Hawking entropy** \cite{bekenstein1973} $S = A / (4\ell_P^2)$ counts the independent degree $\geq 1$ sections on the horizon surface $\mathcal{H}$. In the QOU framework, the area $A$ is the rank of $\Gamma(\mathcal{H}, A_1/A_0)$. This rank measures the dimension of the first-order jet data that the horizon can support.

4. **No photons escape.** Photons are degree-$0$ objects ($K = \varnothing$, step $0$ in the jet-Planck correspondence ). The horizon ideal blocks them alongside all other degree-$0$ data. What an external observer detects as "thermal photons" are actually degree-$1$ winding modes lacking knot identity. These are the Hawking quanta.
<!-- FILE_END: hawking-radiation.md -->

<!-- FILE_START: observable-subcategory.md -->
Let $\mathrm{Bun}(\mathbb{P}(V))$ be the category of finite bundles over the projective line  and its morphisms are permutation-isotopy pairs.

The **observable subcategory** $\mathrm{Bun}^{\circ}(\mathbb{P}(V))$ is the full subcategory on objects where the degree-$0$ algebra is non-trivial:

$$
  \mathrm{Bun}^{\circ}(\mathbb{P}(V)) = \bigl\{ \mathcal{S} \in \mathrm{Bun}(\mathbb{P}(V)) : \Gamma(\mathcal{S}, A_0) \neq 0 \bigr\}.
$$

**Observability.**
We require a non-degenerate Frobenius pairing to define degree-$0$ measurements . When $A_0|_{\mathcal{S}} = 0$, the pairing degenerates on the lowest floor of the brane tower and no degree-$0$ observable is well-defined. The subcategory $\mathrm{Bun}^{\circ}$ defines the regime where the full observational apparatus functions.

**Complement.**
The complement $\mathrm{Bun}(\mathbb{P}(V)) \setminus \mathrm{Bun}^{\circ}(\mathbb{P}(V))$ consists of configurations with $A_0 = 0$. These are the jet horizons  and big bang states .

**Connected components.**
The connected components $\pi_0(\mathrm{Bun}^{\circ})$ are the aeons . Each aeon is a maximal connected full subcategory of $\mathrm{Bun}^{\circ}$. It encompasses all light cones accessible without crossing a jet horizon.
<!-- FILE_END: observable-subcategory.md -->

<!-- FILE_START: aeon.md -->
Let $\mathrm{Bun}^{\circ}(\mathbb{P}(V))$ be the observable subcategory of the category of finite bundles over the projective line .

**Definition.** An **aeon** is a connected component of $\mathrm{Bun}^{\circ}(\mathbb{P}(V))$.

An aeon $\mathcal{A}$ is a maximal full subcategory of $\mathrm{Bun}^{\circ}$ such that a zigzag of morphisms (flow maps, inclusions, or their inverses) connects any two objects $\mathcal{S}$ and $\mathcal{S}'$ without leaving $\mathrm{Bun}^{\circ}$. Every light cone forms a directed diagram within the aeon. The aeon unions all light cones that connect without crossing a jet horizon .

**Maximality.**
The connected-component definition guarantees maximality automatically. No larger subcategory of $\mathrm{Bun}^{\circ}$ containing $\mathcal{A}$ is connected. We avoid defining an explicit interval $(a, b) \subset \mathbb{Z}$. Instead, we define the aeon over the full categorical structure, naturally encompassing all intersecting light cones.
<!-- FILE_END: aeon.md -->

<!-- FILE_START: aeon-boundary.md -->
Let $\mathcal{A}$ be an aeon —a connected component of $\mathrm{Bun}^{\circ}(\mathbb{P}(V))$.

**Definition.** The **boundary** $\partial\mathcal{A}$ of an aeon is the set of objects $\mathcal{S} \in \mathrm{Bun}(\mathbb{P}(V))$ that are limits of diagrams in $\mathcal{A}$ but do not themselves lie in $\mathrm{Bun}^{\circ}$:
$$
  \partial\mathcal{A}
  = 
  \overline{\mathcal{A}} \setminus \mathcal{A}^{\circ}
  \subset
  \bigl\{
    \mathcal{S} : \Gamma(\mathcal{S}, A_0) = 0
  \bigr\}.
$$

Each boundary object represents a jet horizon or a big bang state . We define the boundary datum at $\mathcal{S} \in \partial\mathcal{A}$ as the colimit of the degree $\geq 1$ data over all diagrams in $\mathcal{A}$ approaching $\mathcal{S}$. This is the CMB boundary datum $\mathrm{CMB}(\partial\mathcal{A})$ .
<!-- FILE_END: aeon-boundary.md -->

<!-- FILE_START: aeon-adjacency.md -->
Let $\mathcal{A}$ and $\mathcal{A}'$ be aeons  with boundaries $\partial\mathcal{A}$ and $\partial\mathcal{A}'$ .

**Definition.** Two aeons $\mathcal{A}$ and $\mathcal{A}'$ are **adjacent** if their boundaries share a common object:
$$
  \partial\mathcal{A} \cap \partial\mathcal{A}' \neq \varnothing.
$$

The shared boundary object simultaneously represents the terminal horizon of one aeon and the initial configuration of the next. It categorically realises one cosmological cycle handing off to the next.
<!-- FILE_END: aeon-adjacency.md -->

<!-- FILE_START: observable-beable-correspondence.md -->
't Hooft's :defterm[Cellular Automaton Interpretation]{#cai} of
quantum mechanics \cite{thooft2016} introduces the notion of a
**beable algebra** $\mathcal{A}_{\mathrm{beable}}$ — a maximal
commuting subalgebra of observables whose simultaneous eigenstates
constitute the ontological basis of the underlying deterministic
substrate. The framework's observable subcategory
$\mathrm{Bun}^{\circ}(\mathbb{P}(V))$
 realises
this notion structurally, with the following dictionary:

| 't Hooft (:refterm[CAI]{#cai}) | QOU (this framework) |
|---|---|
| beable algebra $\mathcal{A}_{\mathrm{beable}}$ | degree-$0$ algebra $\Gamma(\mathcal{S}, A_0)$ |
| ontological basis | simultaneous eigenstates of the algebra $\Gamma(\mathcal{S}, A_0)$ |
| "elements of reality" | degree-$0$ observables  |
| beable axiom (maximal commuting) | non-degeneracy of the Frobenius pairing on $A_0$ |
| epistemological / templated states | degree-$> 0$ floors of the brane tower |

**Structural vs. axiomatic.**
't Hooft posits the beable algebra as an additional axiom — one
must specify, separately from the dynamics, which subalgebra of
operators is ontological. The QOU observable subcategory removes
this axiomatic freedom: the degree-$0$ algebra
$\Gamma(\mathcal{S}, A_0)$ is **determined** by the bundle data
$\mathcal{S}$, and the non-triviality condition
$\Gamma(\mathcal{S}, A_0) \neq 0$ is a property of the bundle, not
a choice. The ontological basis is therefore not an input to the
theory but a derived feature of the categorical structure.

**Maximality.**
't Hooft's beable algebra is by construction maximal commuting
(elements outside it fail to commute with some beable). In QOU
the corresponding maximality is the statement that the degree-$0$
algebra is the **maximal** floor of the brane tower on which the
Frobenius pairing is non-degenerate; higher floors ($A_n$ for
$n \geq 1$) carry richer braided structure and fail the
commutativity required for simultaneous measurement. The
filtration $A_0 \subset A_1 \subset \cdots$ ordered by Frobenius
non-degeneracy is the categorical analogue of the beable / epistemic
split.

**Epistemic states as higher floors.**
The states 't Hooft calls *epistemological* (templated
superpositions used by the observer to encode partial knowledge)
correspond in QOU to elements of the higher brane-tower floors
restricted to $\mathcal{S}$ for $n \geq 1$ — well-defined as
categorical data, but not directly measurable since the Frobenius
pairing is degenerate or absent at those floors. Projection to
$A_0$ is the QOU realisation of 't Hooft's
"epistemic-to-ontological" projector.

**Consequence: no superselection axiom.**
't Hooft requires a separate superselection postulate to forbid
coherent superpositions across beable sectors. In QOU this
follows automatically from the categorical structure: the
connected components $\pi_0(\mathrm{Bun}^{\circ})$ — the **aeons**
 — are precisely the superselection sectors,
and morphisms between distinct aeons are forbidden by the
jet-horizon structure  rather
than by an additional axiom.
<!-- FILE_END: observable-beable-correspondence.md -->

<!-- FILE_START: horizon-functor.md -->
Let $\mathrm{Bun}^{\circ}(\mathbb{P}(V))$ denote the observable subcategory . Let $\pi_0(\mathrm{Bun}^{\circ})$ denote its set of connected components (the aeons, [aeon](#def:aeon)).

The **horizon functor** is the map

$$
  \partial \colon 
  \pi_0\!\bigl(\mathrm{Bun}^{\circ}(\mathbb{P}(V))\bigr)
  \longrightarrow 
  \mathcal{P}\!\bigl(
    \mathrm{Bun}(\mathbb{P}(V))
    \setminus
    \mathrm{Bun}^{\circ}(\mathbb{P}(V))
  \bigr).
$$

It sends each aeon $\mathcal{A}$ to its boundary. This boundary comprises configurations $\mathcal{S}$ that appear as limits of diagrams in $\mathcal{A}$ but have $A_0|_{\mathcal{S}} = 0$:

$$
  \partial(\mathcal{A})
  = 
  \bigl\{
    \mathcal{S} \in \mathrm{Bun} \setminus \mathrm{Bun}^{\circ}
    : 
    \mathcal{S} = \varinjlim D
    \text{ for some directed diagram } D \subset \mathcal{A}
  \bigr\}.
$$

Every element of $\partial(\mathcal{A})$ defines a jet horizon .

**Functoriality.**
If $\mathcal{A} \hookrightarrow \mathcal{A}'$ is an inclusion of connected components, then $\mathcal{A} = \mathcal{A}'$ by maximality, and $\partial$ acts as the identity. For adjacent aeons $\mathcal{A}$ and $\mathcal{A}'$ , the intersection $\partial(\mathcal{A}) \cap \partial(\mathcal{A}') \neq \varnothing$. These shared boundary objects specify the loci where the CCC transition occurs.

**Relation to the torsion flow.**
The torsion flow $\Phi_t^q$  provides an endofunctor of $\mathrm{Bun}(\mathbb{P}(V))$. Within an aeon, $\Phi_t^q$ restricts to an endofunctor of $\mathrm{Bun}^{\circ}$ (preserving $A_0 \neq 0$). The horizon $\partial(\mathcal{A})$ constitutes the set of fixed points of the limiting behaviour $\Phi_t^q \to \partial$ as $t$ approaches the aeon boundary.
<!-- FILE_END: horizon-functor.md -->

<!-- FILE_START: cmb-functor.md -->
To aggregate the cosmic microwave background across an entire boundary, we promote the pointwise boundary datum to a functor. 

Let $\partial$ be the horizon functor  and let $A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$ be the brane tower . The **CMB functor** maps each aeon $\mathcal{A}$ to the colimit of the degree $\geq 1$ jet quotients over its boundary. We define this as the composition:

$$
  \mathrm{CMB}
   \colon 
  \pi_0\!\bigl(\mathrm{Bun}^{\circ}\bigr)
  \xrightarrow{\partial}
  \mathcal{P}\!\bigl(\mathrm{Bun} \setminus \mathrm{Bun}^{\circ}\bigr)
  \xrightarrow{\varinjlim (A_1/A_0 \oplus A_2/A_0)}
  \mathbf{Mod}_R.
$$

Evaluated on an aeon $\mathcal{A}$, the functor yields:

$$
  \mathrm{CMB}(\mathcal{A})
  = 
  \varinjlim_{\mathcal{S} \in \partial(\mathcal{A})}
  \bigl(A_1/A_0 \oplus A_2/A_0\bigr)\big|_{\mathcal{S}}.
$$

The target category $\mathbf{Mod}_R$ consists of $R$-modules corresponding to sections of the jet quotient sheaves over the boundary.

| Factor | Jet degree | Content |
|:---|:---:|:---|
| $\varinjlim (A_1/A_0)\vert_{\partial\mathcal{A}}$ | $1$ | Linear transport: winding modes, first-order correlations |
| $\varinjlim (A_2/A_0)\vert_{\partial\mathcal{A}}$ | $2$ | Curvature: linking modes, power spectrum |

We take the colimit over the directed system of all diagrams in $\mathcal{A}$ converging to boundary objects. This aggregates the degree $\geq 1$ data from every light cone reaching the boundary, not just a single computation sequence.

For a single boundary object $\mathcal{S}_0 \in \partial(\mathcal{A})$, the pointwise CMB  $\mathrm{CMB}(\mathcal{S}_0) = (A_1/A_0, A_2/A_0)|_{\mathcal{S}_0}$ is the stalk of the CMB functor at $\mathcal{S}_0$. The full CMB functor is the sheafification over the entire boundary.

By conformal invariance , the CMB functor does not depend on the choice of generator for the horizon ideal $\mathfrak{h} \subset A_0$. It depends solely on the vanishing locus—the conformal class of $A_0$.
<!-- FILE_END: cmb-functor.md -->

<!-- FILE_START: aeon-boundary-generates-chart.md -->
**Conjecture (Aeon recycling).**
*Let $\mathrm{CMB}$ be the CMB functor . Let $\Phi_1^q$ denote the first Planck step of the torsion flow , and let $\nabla_q$ be the $q$-connection.*

*Assume the degree-$1$ component of $\mathrm{CMB}(\mathcal{A})$ satisfies the integrability condition of $\nabla_q$. The composition*
$$
  \Phi_1^q \circ \mathrm{CMB}
   \colon 
  \pi_0\!\bigl(\mathrm{Bun}^{\circ}\bigr)
   \longrightarrow 
  \mathrm{Bun}^{\circ}(\mathbb{P}(V))
$$
*is well-defined. Applying the first Planck step to the CMB of an aeon produces an object with $A_0 \neq 0$, landing back inside $\mathrm{Bun}^{\circ}$.*

**Content of the conjecture.**

1. **The CMB regenerates particles.** Iterating the degree-$1$ transport data (winding modes) in $\mathrm{CMB}(\mathcal{A})$ once by the Reeb flow $f_q$ produces non-trivial degree-$0$ fibre data. This formalises the "condensation" of thermal radiation into particle states.
2. **The recycling map lands in a new aeon.** The output $\Phi_1^q(\mathrm{CMB}(\mathcal{A}))$ lies in $\mathrm{Bun}^{\circ}$. It inhabits some connected component—a (possibly new) aeon $\mathcal{A}'$.
3. **Adjacent aeons connect via the recycling map.** If $\mathcal{A}$ and $\mathcal{A}'$ are adjacent , then $\Phi_1^q(\mathrm{CMB}(\mathcal{A})) \in \mathcal{A}'$.

**The integrability condition.**
The $q$-connection $\nabla_q$ defines parallel transport along the Reeb flow. The integrability condition is $\nabla_q^2 = F_{\nabla_q}$. The connection's curvature determines whether degree-$1$ data iterates coherently. When $F_{\nabla_q}$ aligns with the degree-$2$ component of the CMB, the transport data fits together globally. This ensures the recycling map is well-defined.

**Categorical formulation.**
If the conjecture holds for all aeons, $\Phi_1^q \circ \mathrm{CMB}$ extends to a functor:
$$
  \mathcal{R}
   \colon 
  \pi_0(\mathrm{Bun}^{\circ})
   \longrightarrow 
  \pi_0(\mathrm{Bun}^{\circ}).
$$
We call this the **recycling functor**. It maps each aeon to its successor. A fixed point of $\mathcal{R}$ represents a self-recycling aeon: one whose CMB regenerates itself.
<!-- FILE_END: aeon-boundary-generates-chart.md -->

<!-- FILE_START: horizon-conformal-invariance.md -->
*Let $\mathcal{H}$ be a jet horizon  in an affine chart $U$. Let $A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$ denote the brane tower.*

*The boundary datum $\partial\mathcal{A} = (A_1/A_0, A_2/A_0)|_{\mathcal{H}}$ that survives the horizon is invariant under rescaling of $A_0$. For any $\lambda \in \mathcal{O}(U)^{\times}$:*

$$
  (A_1 / \lambda A_0, A_2 / \lambda A_0)\big|_{\mathcal{H}}
  = 
  (A_1 / A_0, A_2 / A_0)\big|_{\mathcal{H}}.
$$

*Consequently, the boundary datum depends only on the conformal class of $A_0$ (its zero locus), and not on the specific generator of the horizon ideal $\mathfrak{h}$.*
<!-- FILE_END: horizon-conformal-invariance.md -->

<!-- FILE_START: horizon-conformal-invariance-interpretation.md -->
This provides the QOU analogue to conformal invariance in Penrose's CCC \cite{penrose2010}. In CCC, massless particles are conformally invariant; they do not see the conformal factor $\Omega$. Here, the degree $\geq 1$ jet data ignores the "size" of $A_0$. Only its vanishing locus matters.

The QOU observability axioms  require a non-degenerate Frobenius pairing to detect degree-$0$ data. At the horizon, $A_0 = 0$ and the Frobenius pairing degenerates on that component. The surviving observations act exclusively on $A_k/A_0$ — the higher-jet conformal data. Conformal invariance at the horizon emerges as a consequence of the observability axioms, rather than an additional assumption.
<!-- FILE_END: horizon-conformal-invariance-interpretation.md -->

<!-- FILE_START: qou-is-ccc.md -->
*Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a QOU. Let $U \subset M_0$ be an affine chart admitting a chain of adjacent aeons $\ldots, \mathcal{A}_{-1}, \mathcal{A}_0, \mathcal{A}_1, \ldots$ . This aeon chain satisfies the three defining properties of a conformal cyclic cosmology \cite{penrose2010}:*

**(CCC-1) Conformal invariance at boundaries.** *At each aeon boundary $\mathcal{S}_b$, the boundary datum $\partial\mathcal{A}|_b = (A_1/A_0, A_2/A_0)|_{\mathcal{S}_b}$ is invariant under rescaling of $A_0$ . The surviving data depends only on the conformal class of the horizon ideal $\mathfrak{h}$. It depends on the vanishing locus, not the specific generator.*

**(CCC-2) Boundary data inheritance.** *The CMB of aeon $\mathcal{A}_{k+1}$  precisely matches the terminal boundary datum of aeon $\mathcal{A}_k$:*

$$
  \mathrm{CMB}(\mathcal{S}_0^{(k+1)})
  = 
  \partial\mathcal{A}_k\big|_b.
$$

*The degree $\geq 1$ jet data that survives the terminal horizon of one aeon constitutes the seed of the next.*

**(CCC-3) Only conformally invariant data crosses.** *At each boundary, the degree-$0$ algebra vanishes ($A_0|_{\mathcal{S}_b} = 0$). By the observability axioms , the Frobenius pairing degenerates on $A_0$. Therefore, no degree-$0$ observable can detect a difference across the boundary. The only data that crosses is the degree $\geq 1$ quotient, which is exactly the conformal data.*
<!-- FILE_END: qou-is-ccc.md -->

<!-- FILE_START: penrose-ccc.md -->
The aeon structure  parallels Penrose's **Conformal Cyclic Cosmology** (CCC) \cite{penrose2010}. The underlying mechanism, however, differs.

**Penrose's CCC.**
In CCC, the infinite future of one aeon is conformally identified with the Big Bang of the next. At $t \to \infty$, all massive particles have decayed to massless radiation. Massless particles, such as photons and gravitons, are conformally invariant. The conformal structure at $t \to \infty$ is therefore compatible with the conformal structure at $t = 0$ of the successor aeon. The transition is a conformal rescaling $g \mapsto \Omega^2 g$ with $\Omega \to 0$.

**QOU translation.**
In the QOU framework, the aeon boundary is a **degree-$0$ vanishing**, not a conformal rescaling. The horizon ideal $\mathfrak{h} \subset A_0$ annihilates all zeroth-order sections.

See [Table](#tbl:penrose-ccc-table-data).

**Key differences.**

1. **No conformal rescaling.** The QOU aeon boundary is algebraic (ideal vanishing), not geometric (metric rescaling). The brane tower structure is preserved across the boundary. Only the lowest floor ($A_0$) is removed.

2. **The CMB is degree $\geq 1$ data.** In CCC, the CMB of one aeon carries imprints from the previous aeon's final state. In the QOU, this is the boundary datum $\partial\mathcal{A}|_b$. It consists of the first- and second-order jet data that survives the horizon.

3. **Local, not global.** CCC is a global cosmological model with a definite cyclic timeline. The QOU aeon structure is local to an affine chart. Different charts may have different numbers of aeons, or none at all.

4. **Reverse flow.** The backward iteration $f_q^{-1}$ of the Reeb dynamics may or may not reach a past boundary ($A_0 \to 0$). If it does, the affine chart acquires a past jet horizon, representing a big bang state, and the reverse flow terminates. If it does not, the aeon is past-complete and there is no cyclic structure in that chart. Cyclicity is a **consequence of dynamics**, not an axiom.
<!-- FILE_END: penrose-ccc.md -->

