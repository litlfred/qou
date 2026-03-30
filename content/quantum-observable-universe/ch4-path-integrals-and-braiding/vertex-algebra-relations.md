The vertex operator algebra $(V, Y, |0\rangle)$
([vertex operator](#def:vertex-operator)) inherits every QU and QUO
axiom as a relation on the Hecke generators $T_1, \ldots, T_{n-1}$
of $H_n(q)$.  Below we list each axiom and its explicit
translation into **formal knot coordinates** — i.e.\ braid words
in $T_i$, the formal variable $z$ on $\mathcal{S}_p$, the Markov
trace $\mathrm{tr}_M$, and cup/cap morphisms
$\cup\colon \mathbf{1} \to V^{\vee} \otimes V$,
$\cap\colon V \otimes V^{\vee} \to \mathbf{1}$.

---

## QU Axioms (Quantum Universe)

### QU-1: Rigid braided monoidal structure

The braiding $c_{V,V}$ acts on $V^{\otimes n}$ via the Hecke
representation $\rho_n\colon B_n \to H_n(q)$ with
$T_i = \rho_n(\sigma_i)$.  Rigidity and braiding are encoded by
three families of relations:

**(QU-1a) Hecke relation** (quadratic):

$$
  T_i^2 \;=\; (q - q^{-1})\,T_i + 1
  \qquad (1 \leq i \leq n-1).
$$

Equivalently $(T_i - q)(T_i + q^{-1}) = 0$: the eigenvalues $q$
(symmetric/bosonic channel) and $-q^{-1}$ (antisymmetric/fermionic
channel) correspond to the two OPE channels of the vertex algebra.

**(QU-1b) Yang--Baxter relation** (braid relation):

$$
  T_i\, T_{i+1}\, T_i
  \;=\;
  T_{i+1}\, T_i\, T_{i+1}
  \qquad (1 \leq i \leq n-2).
$$

This is the hexagon axiom of the braided monoidal category,
expressed in the Hecke basis.

**(QU-1c) Far-commutativity**:

$$
  T_i\, T_j \;=\; T_j\, T_i
  \qquad (|i - j| \geq 2).
$$

Strands that do not share a crossing commute: locality of the
vertex algebra OPE.

**(QU-1d) Snake identities** (rigidity):

The cup $\cup\colon \mathbf{1} \to V^{\vee} \otimes V$ and
cap $\cap\colon V \otimes V^{\vee} \to \mathbf{1}$ satisfy:

$$
  (\cap \otimes \mathrm{id}_V) \circ
  (\mathrm{id}_V \otimes \cup)
  \;=\; \mathrm{id}_V,
$$

$$
  (\mathrm{id}_{V^{\vee}} \otimes \cap) \circ
  (\cup \otimes \mathrm{id}_{V^{\vee}})
  \;=\; \mathrm{id}_{V^{\vee}}.
$$

In the graphical calculus these are the zig-zag straightenings.
In knot coordinates, $\cup$ and $\cap$ are the Markov-trace
cup/cap insertions: the contour-integral endpoints of $Y(a, z)$
around the Reeb fibre.

### QU-2: Frobenius--Hopf relations

The multiplication $\mu$, comultiplication $\Delta$, unit $\eta$,
counit $\varepsilon$, antipode $S$, and Frobenius form $\int_A$
become operations on braid closures:

**(QU-2a) Associativity**:

$$
  \mu \circ (\mu \otimes \mathrm{id})
  \;=\;
  \mu \circ (\mathrm{id} \otimes \mu)
  \colon A^{\otimes 3} \to A.
$$

In knot coordinates: merging three strands is independent of
grouping.  For braid words $\beta_1, \beta_2, \beta_3$:

$$
  \mathrm{tr}_M\!\bigl(
    \rho(\beta_1 \cdot \beta_2) \cdot \rho(\beta_3)
  \bigr)
  \;=\;
  \mathrm{tr}_M\!\bigl(
    \rho(\beta_1) \cdot \rho(\beta_2 \cdot \beta_3)
  \bigr).
$$

**(QU-2b) Frobenius relation** (sliding):

$$
  (\mu \otimes \mathrm{id}) \circ
  (\mathrm{id} \otimes \Delta)
  \;=\;
  \Delta \circ \mu
  \;=\;
  (\mathrm{id} \otimes \mu) \circ
  (\Delta \otimes \mathrm{id}).
$$

In knot coordinates this is the **saddle-point relation**: a
strand merge followed by a split equals a split followed by a
merge.  Graphically, this is the genus-$0$ cobordism identity —
a pair of pants composed either way gives the same surface.

**(QU-2c) Non-degenerate Frobenius pairing** ($A \cong A^{\vee}$):

The Frobenius pairing $\int_A \circ \mu\colon A \otimes A \to
\mathbf{1}$ is the **Markov trace of the product**:

$$
  \langle a, b \rangle_F
  \;=\;
  \int_A \mu(a \otimes b)
  \;=\;
  \mathrm{tr}_M\!\bigl(\rho(\hat{\beta}_a \cdot \hat{\beta}_b)\bigr),
$$

where $\hat{\beta}_a$ is the braid word representing state $a$.
Non-degeneracy means: for every nonzero braid word $\beta$, there
exists $\beta'$ such that
$\mathrm{tr}_M(\rho(\beta \cdot \beta')) \neq 0$.

**(QU-2d) Hopf (antipode) relation**:

$$
  \mu \circ (S \otimes \mathrm{id}) \circ \Delta
  \;=\;
  \eta \circ \varepsilon
  \;=\;
  \mu \circ (\mathrm{id} \otimes S) \circ \Delta.
$$

In knot coordinates, the antipode $S$ is the **braid reversal**
(orientation reversal of all crossings):

$$
  S(T_i) \;=\; T_i^{-1}
  \;=\; T_i - (q - q^{-1})
  \qquad\text{(from the Hecke relation)}.
$$

The Hopf relation then reads: closing a braid word against its
reverse yields the unknot (vacuum):

$$
  \mathrm{tr}_M\!\bigl(
    \rho(\beta) \cdot \rho(\beta^{-1})
  \bigr)
  \;=\;
  \mathrm{tr}_M(1)
  \;=\;
  J_{0_1}(q).
$$

**(QU-2e) Coassociativity and counit**:

$$
  (\Delta \otimes \mathrm{id}) \circ \Delta
  \;=\;
  (\mathrm{id} \otimes \Delta) \circ \Delta,
  \qquad
  (\varepsilon \otimes \mathrm{id}) \circ \Delta
  \;=\;
  \mathrm{id}
  \;=\;
  (\mathrm{id} \otimes \varepsilon) \circ \Delta.
$$

In knot coordinates: splitting a strand into three is independent
of grouping, and the counit (trace evaluation at the unknot)
acts as a unit for splitting.

### QU-3: Fibre functor (Markov trace)

The fibre functor $\tau\colon \mathbf{C} \to R\text{-Mod}$
realises as the Jones--Markov trace
([Jones--Markov trace](#thm:jones-markov-trace)).  Its defining
relation on Hecke generators is:

**(QU-3a) Markov property I** (conjugation invariance):

$$
  \mathrm{tr}_M\!\bigl(T_i \cdot w\bigr)
  \;=\;
  \mathrm{tr}_M\!\bigl(w \cdot T_i\bigr)
  \qquad \forall\, w \in H_n(q).
$$

**(QU-3b) Markov property II** (stabilisation):

$$
  \mathrm{tr}_M\!\bigl(w \cdot T_n^{\pm 1}\bigr)
  \;=\;
  \frac{1}{\delta}\;\mathrm{tr}_M(w)
  \qquad \text{for } w \in H_n(q) \subset H_{n+1}(q),
$$

where $\delta = -(q + q^{-1})$ is the writhe normalisation.

**(QU-3c) Faithfulness**:

$$
  \mathrm{tr}_M\!\bigl(\rho(\beta)\bigr) = 0
  \;\;\forall\, \beta \in B_n
  \quad\Longrightarrow\quad
  \rho(\beta) = 0 \;\text{in } H_n(q).
$$

The fibre functor detects every nonzero morphism — equivalently,
the Jones polynomial separates knots (modulo the open Jones
conjecture for the full category; for torus knots this is a
theorem \cite{jones1987}).

### QU-4: Differential calculus (translation operator)

The Kähler differentials $\Omega^1(A)$ in the vertex algebra
are generated by the **translation operator** $L_{-1} = j$
(jet prolongation):

**(QU-4a) Translation relation**:

$$
  [L_{-1},\, Y(a, z)]
  \;=\;
  \partial_z Y(a, z)
  \;=\;
  Y(L_{-1}\, a,\, z).
$$

In Hecke generators, the mode expansion gives:

$$
  [L_{-1},\, a_m] \;=\; -m\, a_{m-1},
$$

where $a_m = \mathrm{tr}_M(\check{R}_{(a)}\, z^m)$ is the
$m$-th mode of the vertex operator.

**(QU-4b) Vacuum axiom**:

$$
  Y(|0\rangle, z) \;=\; \mathrm{id}_V, \qquad
  L_{-1}\,|0\rangle \;=\; 0.
$$

The unknot ($|0\rangle = 1 \in A_0$) produces the identity
operator; translation annihilates the vacuum.

---

## QUO Axioms (Observable Universe)

### QUO-1: Non-degenerate integration

The Frobenius form $\int_A$ induces $A \cong A^{\vee}$.  In
knot coordinates this sharpens QU-2c:

$$
  \mathrm{tr}_M\!\bigl(\rho(\beta) \cdot \rho(\beta')\bigr)
  \;=\; 0
  \;\;\forall\, \beta'
  \quad\Longrightarrow\quad
  \beta = \varnothing \;\text{(empty braid)}.
$$

Equivalently, the Gram matrix
$G_{ij} = \mathrm{tr}_M(T_{\beta_i} \cdot T_{\beta_j})$
over any normal-form basis $\{T_{\beta_i}\}$ of $H_n(q)$ is
invertible.

### QUO-2: Observability ($\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$)

There is no braid word invariant under the adjoint (conjugation)
action.  In Hecke generators:

$$
  T_i\, w\, T_i^{-1} \;=\; w
  \quad \forall\, i
  \quad\Longrightarrow\quad
  w \in R \cdot 1
  \;\text{(scalar multiple of the identity)}.
$$

Equivalently: the only braid word commuting with all generators
is the identity.  In the vertex algebra, this means there is no
nontrivial state $a \in V$ with $Y(a, z) = \lambda\,\mathrm{id}$
for all $z$ — every state produces a genuinely $z$-dependent
operator.

### QUO-3: Measurability (anomaly freedom)

The Chern classes $c_1(\mathrm{Ad}(A)) = c_2(\mathrm{Ad}(A)) = 0$
translate via the fibre functor to:

**(QUO-3a) First Chern class vanishing** ($c_1 = 0$):

$$
  \sum_{i=1}^{n-1}
  \mathrm{tr}_M\!\bigl(
    T_i - T_i^{-1}
  \bigr)
  \;=\; 0.
$$

This is the total writhe of the adjoint representation being
zero — the adjoint bundle is orientable.

**(QUO-3b) Second Chern class vanishing** ($c_2 = 0$):

$$
  \sum_{i < j}
  \mathrm{tr}_M\!\bigl(
    [T_i, T_j]\,[T_i, T_j]^{\dagger}
  \bigr)
  \;=\; 0,
$$

where $[T_i, T_j] = T_i T_j - T_j T_i$ and $\dagger$ is the
anti-involution $T_i^{\dagger} = T_i^{-1}$.  This ensures no
topological phases accumulate under transport around the adjoint
bundle.

### QUO-4: Categorical volume constraint

The exterior power $\Lambda^2 V$ maps onto $\mathbf{1}$ via a
non-degenerate epimorphism $\epsilon$ preserved by gauge
automorphisms.  The antisymmetriser in $H_2(q)$ is:

$$
  \mathrm{Alt}_2
  \;=\;
  \frac{1}{[2]_q}\bigl(\mathrm{id} - q^{-1}\, T_1\bigr),
  \qquad
  [2]_q = q + q^{-1}.
$$

The volume constraint is:

$$
  \epsilon \circ \mathrm{Alt}_2
  \;=\;
  \epsilon
  \colon V^{\otimes 2} \to \mathbf{1},
$$

and for every gauge automorphism
$g \in \mathrm{Aut}^{\otimes}(\tau)$:

$$
  \epsilon \circ (\Lambda^2 g_V) \;=\; \epsilon.
$$

In Hecke generators, this becomes: the antisymmetric contraction
$\epsilon$ satisfies

$$
  \epsilon\!\bigl(v \otimes w - q^{-1}\,(T_1 \cdot v \otimes w)\bigr)
  \;=\;
  [2]_q\;\epsilon(v \otimes w)
$$

and is gauge-invariant, fixing the $q$-deformed volume element.

---

## Summary: complete presentation

The vertex operator algebra of a QUO is the quotient of the free
algebra on generators $\{T_i, \cup, \cap, L_{-1},
\mathrm{tr}_M\}$ by the relations:

| Label | Relation | Axiom |
|-------|----------|-------|
| QU-1a | $T_i^2 = (q - q^{-1})T_i + 1$ | Hecke (braiding) |
| QU-1b | $T_i T_{i+1} T_i = T_{i+1} T_i T_{i+1}$ | Yang--Baxter |
| QU-1c | $T_i T_j = T_j T_i$ ($\lvert i-j\rvert \geq 2$) | Locality |
| QU-1d | $(\cap \otimes 1)(1 \otimes \cup) = \mathrm{id}$ | Rigidity |
| QU-2b | $(\mu \otimes 1)(1 \otimes \Delta) = \Delta \circ \mu$ | Frobenius |
| QU-2d | $\mu(S \otimes 1)\Delta = \eta\varepsilon$ | Antipode |
| QU-3a | $\mathrm{tr}_M(T_i w) = \mathrm{tr}_M(w T_i)$ | Markov I |
| QU-3b | $\mathrm{tr}_M(w T_n^{\pm 1}) = \delta^{-1}\mathrm{tr}_M(w)$ | Markov II |
| QU-4a | $[L_{-1}, a_m] = -m\,a_{m-1}$ | Translation |
| QUO-1 | $\det G_{ij} \neq 0$ | Non-degeneracy |
| QUO-2 | $T_i w T_i^{-1} = w\;\forall i \Rightarrow w \in R$ | Observability |
| QUO-3a | $\sum_i \mathrm{tr}_M(T_i - T_i^{-1}) = 0$ | $c_1 = 0$ |
| QUO-3b | $\sum_{i<j} \mathrm{tr}_M([T_i,T_j][T_i,T_j]^{\dagger}) = 0$ | $c_2 = 0$ |
| QUO-4 | $\epsilon \circ \Lambda^2 g_V = \epsilon$ | Volume |

These $14$ relations, together with the Hecke--Skein dictionary
$T \leftrightarrow L_+$, $T^{-1} \leftrightarrow L_-$,
$1 \leftrightarrow L_0$, constitute a complete presentation of
the QOU vertex algebra in formal knot coordinates.
