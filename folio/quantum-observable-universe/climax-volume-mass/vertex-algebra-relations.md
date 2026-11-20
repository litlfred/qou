The vertex operator algebra $(V, Y, |0\rangle)$ ([vertex operator](#def:vertex-operator)) inherits every QU and QUO axiom as a relation on the Hecke generators $\sigma_1, \ldots, \sigma_{n-1}$ of $H_n(R, q)$, translated into **knot coordinates**: braid words in $\sigma_i$, the affine coordinate $z$ on $\mathcal{S}_p$, the Markov trace $\mathrm{tr}_M$, and cup/cap morphisms $\cup\colon \mathbf{1} \to V^{\vee} \otimes V$, $\cap\colon V \otimes V^{\vee} \to \mathbf{1}$. The generators obey the Hecke relation

$$
  \sigma_i^2 = (q - q^{-1})\sigma_i + 1 \qquad (1 \leq i \leq n-1),
$$

and the vertex algebra of a QUO is the quotient of the free algebra on $\{\sigma_i, \cup, \cap, L_{-1}, \mathrm{tr}_M, d, d_q, \star\}$ by **25 relations** — 13 structural (the QU/QUO axioms QU-1 through QUO-4, with QUO-3a withdrawn) and 12 cohomological (C-1 through C-10) — catalogued in [Table 2](#tbl:vertex-algebra-relations-table2-data) and [Table 3](#tbl:vertex-algebra-relations-table3-data), coupled with the Hecke--Skein dictionary $\sigma_i \leftrightarrow L_+$, $\sigma_i^{-1} \leftrightarrow L_-$, $1 \leftrightarrow L_0$.

## Proof

Each axiom is translated into knot coordinates below.

***

## QU Axioms (Quantum Universe)

### QOU-1: Rigid braided monoidal structure (rigidity is a quantum-observable-universe condition; a quantum universe is braided but not rigid)

The braiding $c_{V,V}$ acts on $V^{\otimes n}$ via the Hecke representation $\rho_n\colon B_n \to H_n(R, q)$. Write $\sigma_i$ both for the braid generator in $B_n$ and for its image $\rho_n(\sigma_i)$ in $H_n(R, q)$. Three families of relations encode rigidity and braiding:

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

Equivalently, the Gram matrix $G_{ij} = \mathrm{tr}_M(T_{\beta_i} \cdot T_{\beta_j})$ over any normal-form basis $\{T_{\beta_i}\}$ of $H_n(R, q)$ is invertible (**convention D**: read on the quotient $H_n/\mathrm{rad}\,\mathrm{tr}_M \cong \mathrm{TL}_n$, where the induced pairing is non-degenerate; on $H_n$ itself $\det G = 0$ exactly, the $(1^3)$ block being the radical).

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

The second Chern class $c_2(\mathrm{Ad}(A)) = 0$ translates via the fibre functor to the relation QUO-3b below.

**(QUO-3a, withdrawn.)** An earlier version stated $c_1(\mathrm{Ad}(A)) = 0$ as $\sum_{i=1}^{n-1} \mathrm{tr}_M(\sigma_i - \sigma_i^{-1}) = 0$. That relation fails for every linear trace with $\mathrm{tr}_M(1) \neq 0$ when $q^2 \neq 1$. The Hecke relation QU-1a gives $\sigma_i^{-1} = \sigma_i - (q - q^{-1})$, so

$$
  \sum_{i=1}^{n-1}
  \mathrm{tr}_M\!\bigl(\sigma_i - \sigma_i^{-1}\bigr)
  = (n-1)(q - q^{-1})\,\mathrm{tr}_M(1).
$$

This is the skein relation $L_+ - L_- = (q - q^{-1}) L_0$ under the trace; it holds for every word and carries no information about $c_1$. A writhe-type functional that could express $c_1(\mathrm{Ad}(A))$ is not known in this framework.

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
$$

where $\mathrm{wr}(a)$ is the writhe of $\hat{\beta}_a$: the exponent sum of the braid word $\beta_a$, i.e. its image under the abelianisation $B_n \to \mathbb{Z}$, $\sigma_i^{\pm 1} \mapsto \pm 1$. It is not a trace: the trace of $\sum_i (\sigma_i - \sigma_i^{-1})$ is the constant $(n-1)(q - q^{-1})\mathrm{tr}_M(1)$ for every word.

The curvature 2-form $\omega_V$ is the Hecke Casimir:

$$
  \omega_V
  = 
  \sum_{i < j}
  (\sigma_i \sigma_j - \sigma_j \sigma_i) dz^i \wedge dz^j.
$$

Thus $d_q^2 = 0$ if and only if $q = 1$ (classical limit) or $\mathrm{wr}(\alpha) = 0$ (horizontal forms). For generic $q \neq 1$ and non-horizontal $\alpha$, $d_q^2 \neq 0$: the $q$-deformed complex is **not** a cochain complex. The obstruction evaluates to writhe $\times$ curvature.

### C-3: Hodge star and Poincaré duality

The categorical Hodge star ([categorical Hodge star](#def:categorical-hodge-star)) $\star\colon \Omega^k(A) \to \Omega^{n-k}(A)$ satisfies $\star^2 = \mathrm{id}$. In knot coordinates, $\star$ acts on modes via the antipode:

$$
  \star(a_m)
  = 
  S(a_m)^*
  = 
  (\sigma_i^{-1})_m^*
  \qquad\text{where } (\cdot)^* \text{ is Frobenius conjugation.}
$$

**Poincaré duality** in knot coordinates demands that for all braid words $\beta, \beta'$:

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
  \chi_{\mathrm{eu}}(M_0) =  -6
  \qquad\Longleftrightarrow\qquad
  \mathrm{tr}_M(\mathrm{id}) =  -6.
$$

This forces genus $g = 4$ (Bring's surface), bounding the embeddable torus knots to the 7 generators $\mathcal{G}$.

### C-5: obstruction classes

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

**Kummer persistence** (C-5a): When $\chi_{\mathrm{eu}}(M_0) = -6$, item 3 of the [QU-to-QOU theorem](#thm:qu-to-qou) gives

$$
  \kappa_n = 0 \iff n \mid 6,
  \qquad n \geq 1,
$$

for the Kummer obstruction $\chi(A) \bmod n$. This relation formerly asserted $\kappa_n \neq 0$ for all $n$, on the ground that jet corrections and the base obstruction occupy complementary subgroups; that argument is withdrawn. Whether the $R$-matrix class defined above coincides with the Kummer obstruction is open.

*Scope.* This restates item 3 of [QU-to-QOU](#thm:qu-to-qou) in its earlier, jet-tower form, which is retracted. Item 3 now states persistence in the Kummer tower (the obstruction $\chi(\mathcal{S}) \bmod n$ to an $n$-th root of the Reeb bundle), not at every level of the jet tower. For the bands used in this corpus the complementary-subgroup step is not established on a closed surface such as Bring's. There $H^2(\mathcal{S}, \mathcal{O}_{\mathcal{S}}) = 0$, so the jet corrections $\delta_n$ vanish. For the band $\mathbb{Z}$, the group $H^2(\mathcal{S}, \mathbb{Z}) \cong \mathbb{Z}$ has no non-trivial complement. For $\mathcal{O}^{\times}$ and $\mathbb{G}_m$, the obstruction group itself is zero. See the scope note in the [proof of QU-to-QOU](#prf:qu-to-qou).

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

These **25 relations** (13 structural + 12 cohomological), coupled with the Hecke--Skein dictionary $T \leftrightarrow L_+$, $T^{-1} \leftrightarrow L_-$, $1 \leftrightarrow L_0$, supply a complete presentation of the QOU vertex algebra in knot coordinates. They encode both algebraic structure and cohomological topology using the single language of braid words and the Markov trace.
