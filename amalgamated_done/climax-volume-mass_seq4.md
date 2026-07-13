<!-- FILE_START: braiding-relations-intro.md -->
The mass operator in the previous section is built from Hecke generators. We must now specify which Hecke relations the categorical axioms actually enforce. We read these relations off the rigid monoidal structure and apply them as a spectral filter on candidate braid configurations. 

This section pivots on Proposition: QU and QUO axioms as relations on Hecke generators, which translates the quantum-universe and quantum-universe-observation axioms into a finite list of polynomial relations on the generators. Its prolongation, Proposition: QU/QUO and cohomological relations on the jet bundle, lifts those relations along the brane-tower jet bundle. Remark: Skein relations as an archimedean shadow clarifies that the familiar Skein relations are the archimedean image of these categorical identities. Finally, Remark: Behaviour of $T_{2,11}$ on the jet bundle ideals demonstrates the filter in action, exhibiting the $(2,11)$ torus knot as the genus-bound test case that detects the ideal structure. 

The subsequent section, **Hadron Algebra and Knot Factorisation**, uses the filtered relation algebra to define the hadron composite and its factorisation into constituent knots.
<!-- FILE_END: braiding-relations-intro.md -->

<!-- FILE_START: skein-archimedean-shadow.md -->
In the archimedean realisation, the Markov trace on the braid-group representation yields the Jones polynomial. The Skein relation corresponds to the trace of the characteristic equation of the braiding $c_{V,V}$ ([R-matrix braiding](#rem:r-matrix-braiding)). Over $\mathbb{Q}_\mathfrak{p}$, the same characteristic equation holds (because the eigenvalues $q$ and $-q^{-1}$ are elements of the base ring), but no ambient $3$-manifold exists in which to interpret it as a knot invariant. The categorical formulation of the [braid action on tensor products](#prop:braid-action-tensor) therefore captures the algebraic content of braiding without presupposing an archimedean topology.
<!-- FILE_END: skein-archimedean-shadow.md -->

<!-- FILE_START: vertex-algebra-relations.md -->
The vertex operator algebra $(V, Y, |0\rangle)$ ([vertex operator](#def:vertex-operator)) inherits every QU and QUO axiom as a relation on the Hecke generators $\sigma_1, \ldots, \sigma_{n-1}$ of $H_n(R, q)$. Below we translate each axiom into **knot coordinates**: braid words in $\sigma_i$, the affine coordinate $z$ on $\mathcal{S}_p$, the Markov trace $\mathrm{tr}_M$, and cup/cap morphisms $\cup\colon \mathbf{1} \to V^{\vee} \otimes V$, $\cap\colon V \otimes V^{\vee} \to \mathbf{1}$.

***

## QU Axioms (Quantum Universe)

### QU-1: Rigid braided monoidal structure

The braiding $c_{V,V}$ acts on $V^{\otimes n}$ via the Hecke representation $\rho_n\colon B_n \to H_n(R, q)$. We write $\sigma_i$ both for the braid generator in $B_n$ and for its image $\rho_n(\sigma_i)$ in $H_n(R, q)$ (AGENTS.md §7a). Three families of relations encode rigidity and braiding:

**(QU-1a) Hecke relation** (quadratic):

$$
  \sigma_i^2 =  (q - q^{-1})\sigma_i + 1
  \qquad (1 \leq i \leq n-1).
$$

Equivalently, $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$. The eigenvalues $q$ (symmetric/bosonic channel) and $-q^{-1}$ (antisymmetric/fermionic channel) correspond to the two OPE channels of the vertex algebra.

**(QU-1b) Yang--Baxter relation** (braid relation):

$$
  \sigma_i \sigma_{i+1} \sigma_i
  = 
  \sigma_{i+1} \sigma_i \sigma_{i+1}
  \qquad (1 \leq i \leq n-2).
$$

This is the hexagon axiom of the :refterm[braided monoidal category]{#braided-monoidal-category}, expressed in the Hecke basis.

**(QU-1c) Far-commutativity**:

$$
  \sigma_i \sigma_j =  \sigma_j \sigma_i
  \qquad (|i - j| \geq 2).
$$

Strands that do not share a crossing commute. This encodes the locality of the vertex algebra OPE.

**(QU-1d) Snake identities** (rigidity):

The cup $\cup\colon \mathbf{1} \to V^{\vee} \otimes V$ and cap $\cap\colon V \otimes V^{\vee} \to \mathbf{1}$ satisfy:

$$
  (\cap \otimes \mathrm{id}_V) \circ
  (\mathrm{id}_V \otimes \cup)
  =  \mathrm{id}_V,
$$

$$
  (\mathrm{id}_{V^{\vee}} \otimes \cap) \circ
  (\cup \otimes \mathrm{id}_{V^{\vee}})
  =  \mathrm{id}_{V^{\vee}}.
$$

In the graphical calculus, these are the zig-zag straightenings. In knot coordinates, $\cup$ and $\cap$ are the Markov-trace cup/cap insertions: the contour-integral endpoints of $Y(a, z)$ around the Reeb fibre.

### QU-2: Frobenius--Hopf relations

The operations multiplication $\mu$, comultiplication $\Delta$, unit $\eta$, counit $\varepsilon$, antipode $S$, and Frobenius form $\int_A$ act on braid closures:

**(QU-2a) Associativity**:

$$
  \mu \circ (\mu \otimes \mathrm{id})
  = 
  \mu \circ (\mathrm{id} \otimes \mu)
  \colon A^{\otimes 3} \to A.
$$

In knot coordinates: merging three strands is independent of grouping. For braid words $\beta_1, \beta_2, \beta_3$:

$$
  \mathrm{tr}_M\!\bigl(
    \rho(\beta_1 \cdot \beta_2) \cdot \rho(\beta_3)
  \bigr)
  = 
  \mathrm{tr}_M\!\bigl(
    \rho(\beta_1) \cdot \rho(\beta_2 \cdot \beta_3)
  \bigr).
$$

**(QU-2b) Frobenius relation** (sliding):

$$
  (\mu \otimes \mathrm{id}) \circ
  (\mathrm{id} \otimes \Delta)
  = 
  \Delta \circ \mu
  = 
  (\mathrm{id} \otimes \mu) \circ
  (\Delta \otimes \mathrm{id}).
$$

In knot coordinates, this constitutes the **saddle-point relation**: a strand merge followed by a split equals a split followed by a merge. Graphically, this is the genus-$0$ cobordism identity: composing a pair of pants either way yields the same surface.

**(QU-2c) Non-degenerate Frobenius pairing** ($A \cong A^{\vee}$):

The Frobenius pairing $\int_A \circ \mu\colon A \otimes A \to \mathbf{1}$ defines the **Markov trace of the product**:

$$
  \langle a, b \rangle_F
  = 
  \int_A \mu(a \otimes b)
  = 
  \mathrm{tr}_M\!\bigl(\rho(\hat{\beta}_a \cdot \hat{\beta}_b)\bigr),
$$

where $\hat{\beta}_a$ is the braid word representing state $a$. Non-degeneracy requires that for every nonzero braid word $\beta$, there exists a $\beta'$ such that $\mathrm{tr}_M(\rho(\beta \cdot \beta')) \neq 0$.

**(QU-2d) Hopf (antipode) relation**:

$$
  \mu \circ (S \otimes \mathrm{id}) \circ \Delta
  = 
  \eta \circ \varepsilon
  = 
  \mu \circ (\mathrm{id} \otimes S) \circ \Delta.
$$

In knot coordinates, the antipode $S$ is the **braid reversal** (orientation reversal of all crossings):

$$
  S(\sigma_i) =  \sigma_i^{-1}
  =  \sigma_i - (q - q^{-1})
  \qquad\text{(from the Hecke relation)}.
$$

The Hopf relation states that closing a braid word against its reverse yields the unknot (vacuum):

$$
  \mathrm{tr}_M\!\bigl(
    \rho(\beta) \cdot \rho(\beta^{-1})
  \bigr)
  = 
  \mathrm{tr}_M(1)
  = 
  J_{0_1}(q).
$$

**(QU-2e) Coassociativity and counit**:

$$
  (\Delta \otimes \mathrm{id}) \circ \Delta
  = 
  (\mathrm{id} \otimes \Delta) \circ \Delta,
  \qquad
  (\varepsilon \otimes \mathrm{id}) \circ \Delta
  = 
  \mathrm{id}
  = 
  (\mathrm{id} \otimes \varepsilon) \circ \Delta.
$$

In knot coordinates: splitting a strand into three is independent of grouping. The counit (trace evaluation at the unknot) acts as the unit for splitting.

### QU-3: Fibre functor (Markov trace)

The fibre functor $\tau\colon \mathbf{C} \to R\text{-Mod}$ realises the Jones--Markov trace ([Jones--Markov trace](#thm:jones-markov-trace)). Its defining relation on Hecke generators is:

**(QU-3a) Markov property I** (conjugation invariance):

$$
  \mathrm{tr}_M\!\bigl(\sigma_i \cdot w\bigr)
  = 
  \mathrm{tr}_M\!\bigl(w \cdot \sigma_i\bigr)
  \qquad \forall w \in H_n(R, q).
$$

**(QU-3b) Markov property II** (stabilisation):

$$
  \mathrm{tr}_M\!\bigl(w \cdot \sigma_n^{\pm 1}\bigr)
  = 
  \frac{1}{\delta} \mathrm{tr}_M(w)
  \qquad \text{for } w \in H_n(R, q) \subset H_{n+1}(q),
$$

where $\delta = -(q + q^{-1})$ is the writhe normalisation.

**(QU-3c) Faithfulness**:

$$
  \mathrm{tr}_M\!\bigl(\rho(\beta)\bigr) = 0
   \forall \beta \in B_n
  \quad\Longrightarrow\quad
  \rho(\beta) = 0  \text{in } H_n(R, q).
$$

The fibre functor detects every nonzero morphism. Equivalently, the Jones polynomial separates knots (modulo the open Jones conjecture for the full category; for torus knots this is a theorem \cite{jones1987}).

### QU-4: Differential calculus (translation operator)

The Kähler differentials $\Omega^1(A)$ in the vertex algebra are generated by the **translation operator** $L_{-1} = j$ (jet prolongation):

**(QU-4a) Translation relation**:

$$
  [L_{-1}, Y(a, z)]
  = 
  \partial_z Y(a, z)
  = 
  Y(L_{-1} a, z).
$$

In Hecke generators, the mode expansion yields:

$$
  [L_{-1}, a_m] =  -m a_{m-1},
$$

where $a_m = \mathrm{tr}_M(\check{R}_{(a)} z^m)$ is the $m$-th mode of the vertex operator.

**(QU-4b) Vacuum axiom**:

$$
  Y(|0\rangle, z) =  \mathrm{id}_V, \qquad
  L_{-1}|0\rangle =  0.
$$

The unknot ($|0\rangle = 1 \in A_0$) produces the identity operator; translation annihilates the vacuum.

***

## QUO Axioms (Observable Universe)

### QUO-1: Non-degenerate integration

The Frobenius form $\int_A$ induces $A \cong A^{\vee}$. In knot coordinates, this sharpens QU-2c:

$$
  \mathrm{tr}_M\!\bigl(\rho(\beta) \cdot \rho(\beta')\bigr)
  =  0
   \forall \beta'
  \quad\Longrightarrow\quad
  \beta = \varnothing  \text{(empty braid)}.
$$

Equivalently, the Gram matrix $G_{ij} = \mathrm{tr}_M(T_{\beta_i} \cdot T_{\beta_j})$ over any normal-form basis $\{T_{\beta_i}\}$ of $H_n(R, q)$ is invertible.

### QUO-2: Observability ($\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$)

No braid word remains invariant under the adjoint (conjugation) action. In Hecke generators:

$$
  \sigma_i w \sigma_i^{-1} =  w
  \quad \forall i
  \quad\Longrightarrow\quad
  w \in R \cdot 1
   \text{(scalar multiple of the identity)}.
$$

Equivalently: the only braid word commuting with all generators is the identity. In the vertex algebra, no nontrivial state $a \in V$ satisfies $Y(a, z) = \lambda\mathrm{id}$ for all $z$. Every state produces a genuinely $z$-dependent operator.

### QUO-3: Measurability (anomaly freedom)

The Chern classes $c_1(\mathrm{Ad}(A)) = c_2(\mathrm{Ad}(A)) = 0$ translate via the fibre functor to:

**(QUO-3a) First Chern class vanishing** ($c_1 = 0$):

$$
  \sum_{i=1}^{n-1}
  \mathrm{tr}_M\!\bigl(
    \sigma_i - \sigma_i^{-1}
  \bigr)
  =  0.
$$

This indicates the total writhe of the adjoint representation is zero: the adjoint bundle is orientable.

**(QUO-3b) Second Chern class vanishing** ($c_2 = 0$):

$$
  \sum_{i < j}
  \mathrm{tr}_M\!\bigl(
    [\sigma_i, \sigma_j][\sigma_i, \sigma_j]^{\dagger}
  \bigr)
  =  0,
$$

where $[\sigma_i, \sigma_j] = \sigma_i \sigma_j - \sigma_j \sigma_i$ and $\dagger$ is the anti-involution $\sigma_i^{\dagger} = \sigma_i^{-1}$. This prevents topological phases from accumulating under transport around the adjoint bundle.

### QUO-4: Categorical volume constraint

The exterior power $\Lambda^2 V$ maps onto $\mathbf{1}$ via a non-degenerate epimorphism $\epsilon$ preserved by gauge automorphisms. The antisymmetriser in $H_2(R, q)$ is:

$$
  \mathrm{Alt}_2
  = 
  \frac{1}{[2]_q}\bigl(\mathrm{id} - q^{-1} \sigma_1\bigr),
  \qquad
  [2]_q = q + q^{-1}.
$$

The volume constraint reads:

$$
  \epsilon \circ \mathrm{Alt}_2
  = 
  \epsilon
  \colon V^{\otimes 2} \to \mathbf{1},
$$

and for every gauge automorphism $g \in \mathrm{Aut}^{\otimes}(\tau)$:

$$
  \epsilon \circ (\Lambda^2 g_V) =  \epsilon.
$$

In Hecke generators, the antisymmetric contraction $\epsilon$ satisfies:

$$
  \epsilon\!\bigl(v \otimes w - q^{-1}(\sigma_1 \cdot v \otimes w)\bigr)
  = 
  [2]_q\epsilon(v \otimes w)
$$

and is gauge-invariant, thereby fixing the $q$-deformed volume element.

***

## Cohomological Constraints in Knot Coordinates

The QU/QUO axioms imply a suite of cohomological constraints. Each translates into a relation on braid words, Hecke generators, and the Markov trace.

### C-1: De Rham complex ($d^2 = 0$ on horizontal forms)

The de Rham differential $d\colon \Omega^k(A) \to \Omega^{k+1}(A)$ acts on modes via $d(a_m z^{-m-1} dz) = a_{m-1} z^{-m} dz$. In knot coordinates, the nilpotence $d^2 = 0$ on the horizontal subcomplex $\Omega_H^k(A)$ becomes:

$$
  \mathrm{tr}_M\!\Bigl(
    \check{R}_{(a)} z^{m-2}
  \Bigr)
  - 
  2\mathrm{tr}_M\!\Bigl(
    \check{R}_{(a)} z^{m-1}
  \Bigr)
  + 
  \mathrm{tr}_M\!\Bigl(
    \check{R}_{(a)} z^{m}
  \Bigr)
  =  0
$$

for all $\xi$-invariant states $a$. These are the states annihilated by the weight operator ($[\xi, a] = 0$), which correspond to braid words in the centre of $H_n(R, q)$.

### C-2: $q$-Deformed obstruction to nilpotence ($d_q^2 \neq 0$)

The $q$-exterior derivative $d_q = q^{-1}d + (1 - q^{-1})\pi_V \circ d$ satisfies ([categorical $d_q^2$](#prop:categorical-dq-squared)):

$$
  d_q^2\alpha
  = 
  q^{-1}(1 - q^{-1})\omega_V \wedge_q [\xi, \alpha].
$$

In knot coordinates, the weight operator $\xi$ acts on modes as the writhe grading:

$$
  [\xi, a_m]
  = 
  \mathrm{wr}(a) a_m,
  \qquad
  \mathrm{wr}(a) = \sum_i \mathrm{tr}_M(\sigma_i - \sigma_i^{-1})
   \text{(writhe of $\hat{\beta}_a$)}.
$$

The curvature 2-form $\omega_V$ is the Hecke Casimir:

$$
  \omega_V
  = 
  \sum_{i < j}
  (\sigma_i \sigma_j - \sigma_j \sigma_i) dz^i \wedge dz^j.
$$

Thus $d_q^2 = 0$ if and only if $q = 1$ (classical limit) or $\mathrm{wr}(\alpha) = 0$ (horizontal forms). For generic $q \neq 1$ and non-horizontal $\alpha$, $d_q^2 \neq 0$: the $q$-deformed complex is **not** a cochain complex. The obstruction evaluates to writhe $\times$ curvature.

### C-3: Hodge star and Poincar'e duality

The categorical Hodge star ([categorical Hodge star](#def:categorical-hodge-star)) $\star\colon \Omega^k(A) \to \Omega^{n-k}(A)$ satisfies $\star^2 = \mathrm{id}$. In knot coordinates, $\star$ acts on modes via the antipode:

$$
  \star(a_m)
  = 
  S(a_m)^*
  = 
  (\sigma_i^{-1})_m^*
  \qquad\text{where } (\cdot)^* \text{ is Frobenius conjugation.}
$$

**Poincar'e duality** in knot coordinates demands that for all braid words $\beta, \beta'$:

$$
  \mathrm{tr}_M\!\bigl(
    \rho(\beta) \cdot \star\rho(\beta')
  \bigr)
  = 
  \mathrm{tr}_M\!\bigl(
    \rho(\beta) \cdot S(\rho(\beta'))^*
  \bigr)
  = 
  \delta_{\beta, \beta'} \mathrm{vol},
$$

where $\mathrm{vol} = \int_A(\mathrm{vol}) = 1$ normalises the top form. The pairing is non-degenerate by QUO-1.

### C-4: Euler characteristic constraint

The categorical Euler characteristic $\chi(A) = \mathrm{tr}(\mathrm{id}_A)$ provides the rigidity trace. In knot coordinates, this evaluates to the Jones polynomial of the unknot at strand count $n$:

$$
  \chi(A)
  = 
  \mathrm{tr}_M(\mathrm{id}_{H_n(R, q)})
  = 
  [n]_q!
  = 
  \prod_{k=1}^{n} \frac{q^k - q^{-k}}{q - q^{-1}}.
$$

**Stability under jet prolongation** (C-4a):

$$
  \mathrm{tr}_M\!\bigl(\mathrm{id}_{J^1 H_n(R, q)}\bigr)
  = 
  \mathrm{tr}_M\!\bigl(\mathrm{id}_{H_n(R, q)}\bigr).
$$

The translation operator $L_{-1}$ preserves the Euler characteristic: $\chi(A_{n+1}) = \chi(A_n)$ for all brane levels.

**Descartes constraint** (C-4b): For the physical universe,

$$
  \chi(A) =  -6
  \qquad\Longleftrightarrow\qquad
  \mathrm{tr}_M(\mathrm{id}) =  -6.
$$

This forces genus $g = 4$ (Bring's surface), bounding the embeddable torus knots to the 7 generators $\mathcal{G}$.

### C-5: Yekutieli obstruction classes

The quantum characteristic classes $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ ([quantum characteristic classes](#def:quantum-characteristic-classes)) obstruct lifting from brane level $n$ to $n+1$. In knot variables, the failure of Markov stabilisation at the jet level detects this obstruction:

$$
  \kappa_n
  = 
  \mathrm{tr}_M\!\bigl(
    \check{R}_{(n+1)} - L_{-1} \check{R}_{(n)}
  \bigr)
   \in 
  H^2(\mathcal{S}_p, \mathcal{B}),
$$

where $\check{R}_{(n)}$ is the $R$-matrix at brane level $n$. The class $\kappa_n = 0$ if and only if jet prolongation determines the level-$(n+1)$ braiding entirely from the level-$n$ braiding.

**Perpetual obstruction** (C-5a): When $\chi(A) = -6$,

$$
  \kappa_n  \neq  0
  \qquad \forall n \geq 0.
$$

In Hecke generators: at every brane level, there exist braid words $\beta_{n+1} \in H_{n+1}(q)$ that cannot be expressed as $L_{-1}(\mathcal{B}_n)$ for any $\mathcal{B}_n \in H_n(R, q)$. The jet corrections and the base obstruction occupy complementary subgroups; cancellation is impossible.

### C-6: Betti numbers and spectral sequence

The Leray--Serre spectral sequence controls the Betti numbers $b_k = \dim H^k(\mathcal{S}_n, \mathbb{R})$. In knot variables, $b_k$ counts linearly independent $k$-fold products of Hecke generators modulo the de Rham relation:

$$
  b_k(\mathcal{S}_n)
  = 
  \dim_R
  \frac{
    \ker\!\bigl(d\colon \Omega^k_{H_n(R, q)} \to \Omega^{k+1}_{H_n(R, q)}\bigr)
  }{
    \mathrm{im}\!\bigl(d\colon \Omega^{k-1}_{H_n(R, q)} \to \Omega^k_{H_n(R, q)}\bigr)
  },
$$

where $\Omega^k_{H_n(R, q)}$ is the space of degree-$k$ antisymmetric Hecke words:

$$
  \Omega^k_{H_n(R, q)}
  = 
  \mathrm{span}\!\bigl\{
    T_{i_1} T_{i_2} \cdots T_{i_k}
     \big| 
    i_1 < i_2 < \cdots < i_k
  \bigr\} \cdot \mathrm{Alt}_k,
$$

with $\mathrm{Alt}_k = \sum_{\pi \in S_k} \mathrm{sgn}(\pi) q^{-\ell(\pi)} T_\pi$ the $q$-antisymmetriser.

**Euler check**: $\chi = \sum_k (-1)^k b_k = -6$ reproduces C-4b.

### C-7: Instanton constraint (self-dual curvature)

The categorical instanton condition $\star_q F_\nabla = F_\nabla$ ([instanton on-shell](#rem:instanton-on-shell)) becomes a relation on the curvature 2-form in Hecke generators. The curvature $F_\nabla = \nabla^2$ has components:

$$
  (F_\nabla)_{ij}
  = 
  [\sigma_i, \sigma_j]
  + 
  \sum_k f^k_{ij} \sigma_k,
$$

where $f^k_{ij}$ are the structure constants of the Iwahori--Hecke algebra. The self-duality equation reads:

$$
  \star_q (F_\nabla)_{ij}
  = 
  (F_\nabla)_{ij}
  \qquad\Longleftrightarrow\qquad
  S\!\bigl([\sigma_i, \sigma_j]\bigr)^*
  = 
  [\sigma_i, \sigma_j].
$$

The curvature is invariant under the combined antipode-conjugation. It is **self-adjoint** in the Frobenius inner product.

**Bogomolny bound** (C-7a): The instanton number equals $c_2(A)$:

$$
  \lVert F_\nabla \rVert^2
  = 
  \sum_{i < j}
  \mathrm{tr}_M\!\bigl(
    [\sigma_i, \sigma_j] \cdot [\sigma_i, \sigma_j]^{\dagger}
  \bigr)
  = 
  c_2(A).
$$

By QUO-3b this vanishes for the adjoint. The adjoint bundle is flat. For the fundamental representation, $c_2(A)$ supplies the **topological charge** (knot crossing number modulo signs).

### C-8: Hodge--Laplacian and harmonic braid words

The $q$-Laplacian $\Delta_q = d_q \delta_q + \delta_q d_q$ ([Hodge--Laplacian](#rem:hodge-laplacian-relation)) is self-adjoint. In knot coordinates:

$$
  \Delta_q
  = 
  q^{-2}\Delta
  + 
  q^{-1}(1 - q^{-1})\bigl(
    \omega_V \wedge_q \iota_\xi
    + 
    \iota_\xi \omega_V \wedge_q
  \bigr),
$$

where $\Delta = d\delta + \delta d$ is the undeformed Laplacian and $\iota_\xi$ is contraction with the weight vector.

**Harmonic states** are braid words $\beta$ satisfying $\Delta_q \rho(\beta) = 0$. In Hecke generators:

$$
  \Delta_q \sigma_\beta = 0
  \quad\Longleftrightarrow\quad
  d_q\sigma_\beta = 0
   \text{and} 
  \delta_q \sigma_\beta = 0.
$$

The space $\ker \Delta_q$ constitutes the **particle state space**. Its dimension equals the number of linearly independent knot-particles at each brane level. Over $K = \mathbb{R}$, it acquires the Hilbert structure of $\ker \Delta_q \subset L^2(A)$; over a general field, it is a finite-dimensional vector space.

### C-9: Cohomological embedding (knot basis for $H^*$)

The cohomology of the moduli surface $\Sigma_g$ ([cohomological embedding](#prop:cohomological-embedding)) admits a knot basis. In knot coordinates, each cohomology generator corresponds to a specific Hecke word:

$$
  H^*(\Sigma_4)
  = 
  \mathrm{span}\!\bigl\{
    1,
    T_{(2,3)},
    T_{(2,5)},
    T_{(2,7)},
    T_{(3,5)},
    T_{(2,9)},
    T_{(3,4)},
    T_{(4_1)},
    T_{(4_1)}^*,
    \mathrm{vol}
  \bigr\},
$$

where $T_{(m,n)} = \mathrm{tr}_M(\rho(\sigma^{(m,n)}))$ evaluates the torus knot braid word $\sigma^{(m,n)} \in B_m$ via the Markov trace.

**Hodge decomposition in Hecke generators**:

See [Table 1](#tbl:vertex-algebra-relations-table1-data).

**Completeness**: the $6 \times 5$ character matrix $M_{ij} = \chi_{\lambda_j}(T_{(r_i, s_i)})$ over irreps $\lambda \vdash r$ of $H_2(R, q) \oplus H_3(R, q)$ has rank $5$. Every knot observable on $\Sigma_4$ forms a linear combination of evaluations of the $6$ torus-knot Hecke words.

### C-10: \v{C}ech--Yekutieli :refterm[descent]{#descent} cocycle

The cosimplicial crossed groupoid structure on the brane tower provides a \v{C}ech cocycle condition at each level. In knot variables, the twisted 2-cocycle is:

$$
  d\!\bigl(g^{(n)}_{ijk}\bigr)
  = 
  a^{(n)}_{ij} \cdot g^{(n)}_{ijk} \cdot
  \bigl(a^{(n)}_{jk}\bigr)^{-1},
$$

where $g^{(n)}_{ijk} \in H_n(R, q)$ is the transition braid word on triple overlaps and $a^{(n)}_{ij}$ are 2-morphism braid words. In Hecke generators, the cocycle condition translates to:

$$
  T_{g_{ijk}} \cdot T_{g_{jkl}}
  = 
  T_{a_{ij}} \cdot T_{g_{ikl}} \cdot T_{a_{kl}}^{-1}
  \qquad\text{(in $H_n(R, q)$)},
$$

where $T_g = \rho(g)$ denotes the Hecke image of a braid word. This is the gluing condition for locally defined braid words to patch into a global knot invariant.

***

## Summary: complete presentation

The vertex operator algebra of a QUO is the quotient of the free algebra on generators $\{\sigma_i, \cup, \cap, L_{-1}, \mathrm{tr}_M, d, d_q, \star\}$ by the following relations:

**Structural relations (QU/QUO axioms)**:

See [Table 2](#tbl:vertex-algebra-relations-table2-data).

**Cohomological relations**:

See [Table 3](#tbl:vertex-algebra-relations-table3-data).

These **26 relations** (14 structural + 12 cohomological), coupled with the Hecke--Skein dictionary $T \leftrightarrow L_+$, $T^{-1} \leftrightarrow L_-$, $1 \leftrightarrow L_0$, supply a complete presentation of the QOU vertex algebra in knot coordinates. They encode both algebraic structure and cohomological topology using the singular language of braid words and the Markov trace.
<!-- FILE_END: vertex-algebra-relations.md -->

<!-- FILE_START: vertex-algebra-jet-relations.md -->
Every relation in the QU/QUO presentation ([vertex algebra relations](#prop:vertex-algebra-relations)) lifts to the jet bundle $J^n(A) = A_n$ via the brane tower ([recursive brane tower](#def:recursive-brane-tower)). The jet prolongation $L_{-1}\colon A_n \to A_{n+1}$ promotes each level-$n$ Iwahori--Hecke algebra $H^{(n)}(q)$ to a level-$(n{+}1)$ Hecke algebra $H^{(n+1)}(q)$. The :refterm[descent]{#descent} involution $\hat{\tau}_n = \ell_n \circ \mathfrak{d}_{n+1}$ splits the level-$(n{+}1)$ relations into **descended** (inherited from level $n$) and **transient** (genuinely new at level $n{+}1$).

Let $\sigma_i^{(n)}$ denote the Hecke generators at brane level $n$, $\mathrm{tr}_M^{(n)}$ the level-$n$ Markov trace, and $\check{R}^{(n)}$ the $R$-matrix at level $n$. The jet embedding is $\ell_n\colon H^{(n)}(q) \hookrightarrow H^{(n+1)}(q)$ with $\ell_n(\sigma_i^{(n)}) = \sigma_i^{(n+1)}$. The :refterm[descent]{#descent} is $\mathfrak{d}_{n+1}\colon H^{(n+1)}(q) \to H^{(n)}(q)$ with $\mathfrak{d}_{n+1} \circ \ell_n = \mathrm{id}$.

***

## I. Structural relations on $J^n(A)$

### J-1: Hecke relations (level $n$)

The Hecke generators at every brane level satisfy the identical quadratic, braid, and locality relations:

**(J-1a)** $\sigma_i^{(n)2} =  (q - q^{-1})\sigma_i^{(n)} + 1$

**(J-1b)** $\sigma_i^{(n)} \sigma_{i+1}^{(n)} \sigma_i^{(n)} =  \sigma_{i+1}^{(n)} \sigma_i^{(n)} \sigma_{i+1}^{(n)}$

**(J-1c)** $\sigma_i^{(n)} \sigma_j^{(n)} =  \sigma_j^{(n)} \sigma_i^{(n)} \qquad (|i - j| \geq 2)$

The substrate parameter $q$ is the **same at every level**. This manifests the Euler characteristic stability $\chi(A_n) = \chi(A_0)$.

### J-2: Jet-prolonged Frobenius--Hopf relations

The multiplication $\mu_n$, comultiplication $\Delta_n$, and antipode $S_n$ on $A_n$ inherit from $A_0$ by jet prolongation. The Frobenius relation lifts level by level:

**(J-2a) Frobenius sliding at level $n$**:

$$
  (\mu_n \otimes \mathrm{id}) \circ
  (\mathrm{id} \otimes \Delta_n)
  = 
  \Delta_n \circ \mu_n.
$$

In knot coordinates:

$$
  \mathrm{tr}_M^{(n)}\!\bigl(
    \rho_n(\beta_1) \cdot \rho_n(\beta_2 \cdot \beta_3)
  \bigr)
  = 
  \mathrm{tr}_M^{(n)}\!\bigl(
    \rho_n(\beta_1 \cdot \beta_2) \cdot \rho_n(\beta_3)
  \bigr).
$$

**(J-2b) Antipode at level $n$**: $S_n(\sigma_i^{(n)}) = \sigma_i^{(n)-1} = \sigma_i^{(n)} - (q - q^{-1})$.

**(J-2c) Level-$n$ Frobenius pairing**:

$$
  \langle a, b \rangle_n
  = 
  \mathrm{tr}_M^{(n)}\!\bigl(
    \rho_n(\hat{\beta}_a \cdot \hat{\beta}_b)
  \bigr).
$$

Non-degeneracy demands $\det G^{(n)}_{ij} \neq 0$ at every brane level.

### J-3: Markov trace at level $n$

**(J-3a) Conjugation invariance**:

$$
  \mathrm{tr}_M^{(n)}(\sigma_i^{(n)} \cdot w)
  = 
  \mathrm{tr}_M^{(n)}(w \cdot \sigma_i^{(n)})
  \qquad \forall w \in H^{(n)}(q).
$$

**(J-3b) Stabilisation**:

$$
  \mathrm{tr}_M^{(n)}(w \cdot \sigma_m^{(n)\pm 1})
  = 
  \frac{1}{\delta} \mathrm{tr}_M^{(n)}(w),
  \qquad
  \delta = -(q + q^{-1}).
$$

**(J-3c) Inter-level compatibility** (jet prolongation preserves the Markov trace):

$$
  \mathrm{tr}_M^{(n+1)}\!\bigl(\ell_n(w)\bigr)
  = 
  \mathrm{tr}_M^{(n)}(w)
  \qquad \forall w \in H^{(n)}(q).
$$

This acts as the knot-variable form of Euler stability: the Jones polynomial of a knot remains independent of brane level.

### J-4: Translation operator between levels

**(J-4a) Mode relation across levels**:

$$
  [L_{-1}, a_m^{(n)}] =  -m a_{m-1}^{(n+1)},
$$

where $a_m^{(n)} = \mathrm{tr}_M^{(n)}(\check{R}^{(n)}_{(a)} z^m)$ represents the $m$-th mode at level $n$. The commutator maps level-$n$ modes to level-$(n{+}1)$ modes. The translation operator operates as the **inter-level ladder**.

**(J-4b) Vacuum stability across levels**:

$$
  |0\rangle^{(n)} =  \ell_{n-1} \circ \cdots \circ \ell_0(|0\rangle)
  =  1 \in A_n.
$$

The unknot embeds identically at every level.

### J-5: Observability at level $n$

$$
  \sigma_i^{(n)} w \sigma_i^{(n)-1} = w
   \forall i
  \quad\Longrightarrow\quad
  w \in R \cdot 1  \text{in } H^{(n)}(q).
$$

The vanishing of $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A_n))$ propagates from level $0$ via jet prolongation: any $\mathrm{Ad}$-invariant at level $n{+}1$ projects to one at level $n$, contradicting the base case.

### J-6: Volume constraint at level $n$

$$
  \epsilon_n \circ \mathrm{Alt}_2^{(n)} =  \epsilon_n,
  \qquad
  \epsilon_n \circ (\Lambda^2 g_V^{(n)}) = \epsilon_n.
$$

The $q$-antisymmetriser $\mathrm{Alt}_2^{(n)} = \frac{1}{[2]_q}(\mathrm{id} - q^{-1} \sigma_1^{(n)})$ adopts the same form at every level (same $q$). The volume constraint is thus **level-independent**.

***

## II. :refterm[Descent]{#descent} decomposition of relations

The :refterm[descent]{#descent} involution $\hat{\tau}_n = \ell_n \circ \mathfrak{d}_{n+1}$ operates idempotently on $H^{(n+1)}(q)$ and splits every relation into descended and transient parts.

### D-1: Descended Hecke generators

$$
  \hat{\tau}_n(\sigma_i^{(n+1)})
  = 
  \ell_n\!\bigl(\mathfrak{d}_{n+1}(\sigma_i^{(n+1)})\bigr)
  = 
  \ell_n(\sigma_i^{(n)})
  = 
  \sigma_i^{(n+1)}.
$$

For $i \leq n-1$: the base Hecke generators are **entirely descended**. They signify the exact same crossing at every level. The Hecke relation QU-1a is purely descended.

### D-2: Transient generators

At level $n{+}1$, the jet prolongation may produce new generators $\sigma^{(n+1)}_{\mathrm{new}}$ in the transient complement $\mathcal{A}^{\mathrm{trans}}_{n+1} = \ker\hat{\tau}_n$. These satisfy:

$$
  \hat{\tau}_n(\sigma^{(n+1)}_{\mathrm{new}}) =  0,
  \qquad
  \mathfrak{d}_{n+1}(\sigma^{(n+1)}_{\mathrm{new}}) =  0.
$$

Transient generators lack a pre-image at level $n$. They obey the Hecke relation (J-1a) at level $n{+}1$ but their Markov traces are **invisible at level $n$**:

$$
  \mathrm{tr}_M^{(n)}\!\bigl(
    \mathfrak{d}_{n+1}(\sigma^{(n+1)}_{\mathrm{new}})
  \bigr)
  =  0.
$$

### D-3: :refterm[Descent]{#descent} of the Frobenius relation

The Frobenius sliding relation (J-2a) decomposes as:

$$
  \Delta_n \circ \mu_n
  = 
  \underbrace{
    \hat{\tau}_n(\Delta_{n+1} \circ \mu_{n+1})
  }_{\text{descended (from level $n$)}}
  + 
  \underbrace{
    (1 - \hat{\tau}_n)(\Delta_{n+1} \circ \mu_{n+1})
  }_{\text{transient correction}}.
$$

The transient correction captures the **jet curvature**: the failure of the level-$(n{+}1)$ Frobenius relation to be entirely governed by level $n$.

### D-4: Bosonic vs fermionic modes

The :refterm[descent]{#descent} eigenspaces ([:refterm[descent]{#descent} eigenspaces](#prop:descent-eigenspaces)) partition modes by statistics:

* **Bosonic (longitudinal)**: $w \in \mathcal{A}^{\mathrm{desc}}_{n+1}$ obeys $\hat{\tau}_n(w) = w$. In knot coordinates: braid words whose Markov trace is fully fixed at level $n$:

$$
  \mathrm{tr}_M^{(n+1)}(w) =  \mathrm{tr}_M^{(n)}(\mathfrak{d}_{n+1}(w)).
$$

* **Fermionic (ladder)**: $w \in \mathcal{A}^{\mathrm{trans}}_{n+1}$ obeys $\hat{\tau}_n(w) = 0$. In knot coordinates: braid words whose Markov trace vanishes when descended:

$$
  \mathrm{tr}_M^{(n)}(\mathfrak{d}_{n+1}(w)) =  0.
$$

Fermionic modes are the jet-created braid words without an analogue at the prior level.

***

## III. Cohomological relations on $J^n(A)$

### JC-1: De Rham complex at level $n$

$$
  d_n^2 =  0
  \qquad\text{on } \Omega^k_H(A_n),
$$

where $\Omega^k_H(A_n)$ signifies the horizontal subcomplex at level $n$ (braid words with zero writhe at level $n$).

### JC-2: $q$-Obstruction at level $n$

$$
  d_{q,n}^2\alpha
  = 
  q^{-1}(1 - q^{-1})\omega_V^{(n)} \wedge_q [\xi_n, \alpha],
$$

where $\omega_V^{(n)} = \sum_{i<j}(\sigma_i^{(n)} \sigma_j^{(n)} - \sigma_j^{(n)} \sigma_i^{(n)})dz^i \wedge dz^j$ defines the level-$n$ Hecke Casimir. Because $q$ is level-independent, the obstruction to $d_q^2 = 0$ preserves the **same algebraic form** at every level while acting on a larger algebra.

### JC-3: Euler characteristic stability

$$
  \chi(A_n)
  = 
  \mathrm{tr}_M^{(n)}(\mathrm{id}_{H^{(n)}(q)})
  = 
  \mathrm{tr}_M^{(0)}(\mathrm{id}_{H^{(0)}(q)})
  = 
  \chi(A_0)
  =  -6.
$$

The rigidity trace of the identity remains level-invariant. In Hecke generators: the quantum factorial $[n]_q!$ at the base strand count persists through jet prolongation.

### JC-4: Yekutieli obstruction at level $n$

$$
  \kappa_n
  = 
  \mathrm{tr}_M^{(n+1)}\!\bigl(
    \check{R}^{(n+1)} - \ell_n(\check{R}^{(n)})
  \bigr)
   \in  H^2(\mathcal{S}, \mathcal{B}).
$$

In Hecke generators, this evaluates the **transient part of the $R$-matrix**:

$$
  \kappa_n
  = 
  \mathrm{tr}_M^{(n+1)}\!\bigl(
    (1 - \hat{\tau}_n) \check{R}^{(n+1)}
  \bigr).
$$

The perpetual obstruction $\kappa_n \neq 0$ confirms: at every level, the $R$-matrix possesses a nonzero transient component. Braiding at level $n{+}1$ is **not** exclusively determined by level $n$.

### JC-5: Betti numbers across levels

$$
  b_k(A_{n+1})
  = 
  b_k^{\mathrm{desc}}(A_{n+1}) + b_k^{\mathrm{trans}}(A_{n+1}),
$$

where

$$
  b_k^{\mathrm{desc}}
  = 
  \dim \frac{
    \ker(d_n) \cap \mathcal{A}^{\mathrm{desc}}_{n+1}
  }{
    \mathrm{im}(d_n) \cap \mathcal{A}^{\mathrm{desc}}_{n+1}
  }
  = 
  b_k(A_n)
$$

and $b_k^{\mathrm{trans}}$ enumerates genuinely new cohomology classes at level $n{+}1$. The Leray--Serre spectral sequence for $A_{n+1} \to A_n$ supplies the $E_2$-page:

$$
  E_2^{p,r}
  = 
  H^p\!\bigl(A_n, H^r(\Omega^1(A_n))\bigr)
  \Longrightarrow
  H^{p+r}(A_{n+1}),
$$

with differentials managed by $\kappa_n$.

### JC-6: Instanton constraint at level $n$

$$
  S_n\!\bigl([\sigma_i^{(n)}, \sigma_j^{(n)}]\bigr)^*
  = 
  [\sigma_i^{(n)}, \sigma_j^{(n)}].
$$

Self-duality of the curvature operates at every level by inheritance of the Frobenius-adjoint structure. The instanton number decouples:

$$
  c_2(A_n)
  = 
  c_2^{\mathrm{desc}}(A_n) + c_2^{\mathrm{trans}}(A_n),
$$

where $c_2^{\mathrm{desc}} = c_2(A_{n-1})$ is descended and $c_2^{\mathrm{trans}}$ constitutes the topological charge of the transient sector.

### JC-7: Harmonic braid words at level $n$

$$
  \Delta_{q,n} T_\beta^{(n)} = 0
  \quad\Longleftrightarrow\quad
  d_{q,n} T_\beta^{(n)} = 0
   \text{and} 
  \delta_{q,n} T_\beta^{(n)} = 0.
$$

The harmonic space resolves under :refterm[descent]{#descent}:

$$
  \ker \Delta_{q,n+1}
  = 
  \underbrace{
    \ell_n(\ker \Delta_{q,n})
  }_{\text{descended harmonics}}
   \oplus 
  \underbrace{
    \ker \Delta_{q,n+1} \cap \mathcal{A}^{\mathrm{trans}}_{n+1}
  }_{\text{new particles at level $n{+}1$}}.
$$

Descended harmonics represent the particles already populated at level $n$; transient harmonics are **new particle states** spawned by the jet prolongation.

### JC-8: \v{C}ech cocycle at level $n$

$$
  T_{g^{(n)}_{ijk}} \cdot T_{g^{(n)}_{jkl}}
  = 
  T_{a^{(n)}_{ij}} \cdot T_{g^{(n)}_{ikl}} \cdot
  T_{a^{(n)}_{kl}}^{-1}
  \qquad\text{in } H^{(n)}(q).
$$

The cosimplicial structure bridges adjacent levels: the coface map $\delta^i$ acts as jet prolongation $\ell_n$, and the codegeneracy $\sigma^j$ acts as :refterm[descent]{#descent} $\mathfrak{d}_{n+1}$. The cosimplicial identities in knot coordinates emerge as:

$$
  \ell_n(T_{g^{(n)}_{ijk}}) =  T_{g^{(n+1)}_{\delta^i(ijk)}},
  \qquad
  \mathfrak{d}_{n+1}(T_{g^{(n+1)}_{ijk}}) =  T_{g^{(n)}_{\sigma^j(ijk)}}.
$$

### JC-9: Global gluing (direct limit)

The direct limit $\mathcal{A}_\infty = \varinjlim H^{(n)}(q)$ defines the **infinite-level Iwahori--Hecke algebra**. A braid word $w_\infty \in \mathcal{A}_\infty$ embodies a compatible sequence $(w^{(0)}, w^{(1)}, w^{(2)}, \ldots)$ satisfying $\ell_n(w^{(n)}) = \hat{\tau}_n(w^{(n+1)})$ for all $n$. The global Markov trace reads:

$$
  \mathrm{tr}_M^{(\infty)}(w_\infty)
  = 
  \mathrm{tr}_M^{(0)}(w^{(0)})
  = 
  \mathrm{tr}_M^{(n)}(w^{(n)})
  \qquad\text{(level-independent)}.
$$

Every structural and cohomological relation holds precisely in $\mathcal{A}_\infty$. The global gluing condition compels locally defined braid words to patch seamlessly into a robust element of the direct limit.

***

## IV. Summary: relations on $J^n(A)$

**Structural (level-$n$ lifts of QU/QUO)**:

See [Table 1](#tbl:vertex-algebra-jet-relations-table1-data).

**:refterm[Descent]{#descent} decomposition**:

See [Table 2](#tbl:vertex-algebra-jet-relations-table2-data).

**Cohomological (level-$n$ lifts)**:

See [Table 3](#tbl:vertex-algebra-jet-relations-table3-data).

The total presentation on $J^n(A)$ demands **34 relations**: 11 structural (level-$n$ QU/QUO), 4 :refterm[descent]{#descent}, 9 cohomological, plus the 2 inter-level relations J-3c and J-4a that bind adjacent brane levels. Each is expressed entirely in the level-$n$ Hecke generators $\sigma_i^{(n)}$, the level-$n$ Markov trace $\mathrm{tr}_M^{(n)}$, and the :refterm[descent]{#descent} involution $\hat{\tau}_n$.
<!-- FILE_END: vertex-algebra-jet-relations.md -->

<!-- FILE_START: t211-ideal-annihilation.md -->
The torus knot $T_{2,11}$ claims Seifert genus $g = 5 > 4$ and represents the **first excluded generator** — the knot that would furnish a fourth lepton generation if embeddable. The algebraic mechanism originates in the Chebyshev overflow within the genus-filtration ideal $\mathfrak{I}_4 = (u^5)$ ([genus-filtration ideal](#prop:genus-filtration-ideal)). The Hecke coefficient $a_{11}(u) = u^5 + 9u^4 + \cdots$ asserts degree $5 > 4$, forcing $a_{11} \in (u^5)$.

This remark maps the **consequences** of that algebraic annihilation across the jet bundle, shell structure, and symmetry group.

***

## 1. Algebraic survival, physical death

The torus knot $T_{2,11}$ validates every structural relation; it behaves as a perfectly sound element of the Iwahori--Hecke algebra:

| Relation          | Status   | Detail                                               |
| ----------------- | -------- | ---------------------------------------------------- |
| Hecke (J-1)       | Survives | $T_1^{11} = a_{11}(u) T_1 + a_{10}(u) \in H_2(R, q)$ |
| Frobenius (J-2)   | Survives | $\mathrm{tr}_M(T_1^{11} \cdot T_\beta) \neq 0$       |
| Jones polynomial  | Survives | $J_{T_{2,11}}(q) \neq 0$                             |
| Translation (J-4) | Survives | Lifts to all brane levels                            |

Yet the cohomological constraints obliterate it:

| Constraint          | Status     | Detail                                   |
| ------------------- | ---------- | ---------------------------------------- |
| Chebyshev overflow  | **Killed** | $\deg_u a_{11} = 5 > 4 = g(\Sigma_4)$    |
| Mass functional     | **Killed** | $\mathcal{M}(T_{(2,11)}) = 0$            |
| Harmonic projection | **Killed** | $\Pi_{\mathrm{harm}} T_{(2,11)} = 0$     |
| Hodge dual          | **Killed** | $\star[T_{2,11}] = 0$ in $H^*(\Sigma_4)$ |

The bifurcation is severe: the Iwahori--Hecke algebra remains blind to the genus bound, leaving the Chebyshev degree ([genus-filtration ideal](#prop:genus-filtration-ideal)) as the sole polynomial certificate measuring membership within the spectral filter.

***

## 2. Behaviour on the jet bundle

At each brane level $n$, the jet embedding and :refterm[descent]{#descent} strictly preserve the level-$n$ spectral ideal $\mathcal{I}_4^{(n)} = \{w \in H^{(n)}(q) : g(\hat{w}) > 4\}$:

$$
  \ell_n(\mathcal{I}_4^{(n)}) \subseteq \mathcal{I}_4^{(n+1)},
  \qquad
  \mathfrak{d}_{n+1}(\mathcal{I}_4^{(n+1)}) \subseteq \mathcal{I}_4^{(n)}.
$$

The torus knot $T_{2,11}$ operates as **entirely descended** at every level:

$$
  \hat{\tau}_n(T_{(2,11)}^{(n+1)}) = T_{(2,11)}^{(n+1)},
  \qquad
  (1 - \hat{\tau}_n)(T_{(2,11)}^{(n+1)}) = 0.
$$

It retains no transient component, yields no input to the Yekutieli obstruction $\kappa_n$, and invokes no new physics at any level.

***

## 3. No :refterm[descent]{#descent} to shells

The transfer matrix eigenvalues $\lambda_\pm$ of $T_{\gamma e}(q)$ command the shell structure ([shell structure eigenvalues](#prop:shell-structure-eigenvalues)). The torus knot $T_{2,11}$ evaluates to:

$$
  \mathcal{T}_{T_{2,11}}(q) = \mathbf{I}_{2 \times 2},
  \qquad
  F(T_{2,11}, N) = 1  \forall N.
$$

* **No shell structure**: eigenvalues $(1, 1)$ yield the degenerate Chebyshev recurrence $\hat{V}(n) = 1$ for all $n$ — utterly flat, with no energy separation and no sub-shells.
* **No shell-transition levels**: it produces zero effective crossings on $\Sigma_4$, ensuring it cannot lift a spin-orbit level across a gap (shell-transition knot).
* **Null force operator**: the $(2,11)$ channel contributes only the identity factor to the spectral decomposition, rendering it a multiplicative ghost.

***

## 4. No $S_{11}$ symmetry — crystallographic obstruction

The symmetry group of $T_{2,11}$ is **not** $S_{11}$ but the dihedral group:

$$
  \mathrm{Sym}(T_{2,11})
  = \mathbb{Z}_{11} \rtimes \mathbb{Z}_2
  = D_{11}
  \qquad (\text{order } 22).
$$

* $\mathbb{Z}_{11}$: rotational symmetry (the winding number is $11$, independent of the strand count — $T_{2,11}$ is a 2-strand braid $\sigma_1^{11} \in B_2$).
* $\mathbb{Z}_2$: strand swap $S_2$ arising from $B_2 / \langle \sigma_1^2 = 1\rangle$.

**$\mathbb{Z}_{11}$ cannot embed in $S_5$.** The maximum element order in $S_5$ stands at $6$ (cycle type $(2,3)$), and $11 > 5$ means no element of order $11$ can exist:

$$
  \mathbb{Z}_{11} \not\hookrightarrow S_5
  = \mathrm{Aut}(\Sigma_4).
$$

This acts as a **crystallographic obstruction at the group level**: $11$-fold rotational symmetry proves incompatible with the $5$-sheet Bring surface, just as $5$-fold symmetry proves incompatible with a lattice ([fivefold symmetry](#rem:fivefold-symmetry)).

| Knot       |    Cyclic sym.    | Embeds in $S_5$? | Genus $\leq 4$? |        Status       |
| ---------- | :---------------: | :--------------: | :-------------: | :-----------------: |
| $T_{2,3}$  |   $\mathbb{Z}_3$  |        Yes       |   Yes ($g=1$)   |        Embeds       |
| $T_{2,5}$  |   $\mathbb{Z}_5$  |        Yes       |   Yes ($g=2$)   |        Embeds       |
| $T_{2,7}$  |   $\mathbb{Z}_7$  |        No        |   Yes ($g=3$)   | Embeds (sym broken) |
| $T_{2,9}$  |   $\mathbb{Z}_9$  |        No        |   Yes ($g=4$)   | Embeds (sym broken) |
| $T_{2,11}$ | $\mathbb{Z}_{11}$ |      **No**      |  **No** ($g=5$) | **Doubly excluded** |

For $T_{2,7}$ and $T_{2,9}$: the cyclic symmetry exceeds $S_5$ yet the genus fits — their symmetries simply *break* on $\Sigma_4$. For $T_{2,11}$: **both** criteria fail. It remains the ghost of the fourth generation — algebraically valid but topologically null, entirely bereft of shell action and compatible symmetry.

**Representation-theoretic refinement.** The privileged role of $T_{2,3}$ and $T_{2,5}$ atop the embedding table attains a representation-theoretic footing under the weight identification of [prop:x5-bring-weight-identification](#prop:x5-bring-weight-identification). Passing to the hyperelliptic quintic $\mathcal{X}_5$ of [thm:hyperelliptic-z5-classification](#thm:hyperelliptic-z5-classification), the non-trivial $\mathbb{Z}_5$-isotypical part of $H^1(\mathcal{X}_5, \mathbb{Q})$ manifests exactly as the 4-dim character sum $\chi_1 \oplus \chi_2 \oplus \chi_3 \oplus \chi_4$. The Seifert surface of $T_{2,5}$ fills this representation completely ($g(T_{2,5}) = 2 = \dim_{\mathbb{C}} J(\mathcal{X}_5)$), while $T_{2,3}$ occupies only a 2-dim sub-isotype. See [rem:weight-identification-consequences](#rem:weight-identification-consequences) for details.

***

## 5. Skein interaction: modified crossing relation

When $T_{2,11}$ surfaces as an $L_0$ intermediate in a Skein resolution of physical knots, the spectral filter projects it away. The physical Skein relation on $\Sigma_4$ reads:

$$
  q\mathcal{M}[L_+] = q^{-1}\mathcal{M}[L_-]
  \qquad\text{when } g(L_0) > 4,
$$

effectively fusing the two crossing channels. The $\mathbb{Z}_{11}$ symmetry of the intermediate term stays isolated within $\mathcal{I}_4$ and never penetrates the physical quotient.
<!-- FILE_END: t211-ideal-annihilation.md -->

<!-- FILE_START: outro-climax-volume-mass.md -->
This closes the climax chapter — the volume / mass duality operating at the substrate level. The braiding relations and spectral filter detailed in this closing section pinpoint exactly which categorical vertex-algebra relations survive the substrate-to-archimedean specialisation. The skein-archimedean shadow supplies the hyperbolic-volume aspect, the vertex-algebra jet relations provide the mass formulation, and the $T_{2,11}$ ideal annihilation seals the duality loop.

The subsequent mass theory chapter consolidates this derived mass content into the categorical mass formula, the Hoefsmit / Wenzl-bridge / Markov-trace stack, and the $\alpha_k$-coefficient table that underwrites every numerical prediction in the ensuing chapters.
<!-- FILE_END: outro-climax-volume-mass.md -->
