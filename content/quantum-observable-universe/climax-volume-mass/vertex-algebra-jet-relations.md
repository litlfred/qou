Every relation in the QU/QUO presentation ([vertex algebra relations](#prop:vertex-algebra-relations)) lifts to the jet bundle $J^n(A) = A_n$ via the brane tower ([recursive brane tower](#def:recursive-brane-tower)). The jet prolongation $L_{-1}\colon A_n \to A_{n+1}$ promotes each level-$n$ Iwahori--Hecke algebra $H^{(n)}(q)$ to a level-$(n{+}1)$ Hecke algebra $H^{(n+1)}(q)$. Write $\sigma_i^{(n)}$ for the Hecke generators, $\mathrm{tr}_M^{(n)}$ for the level-$n$ Markov trace, and $\check{R}^{(n)}$ for the level-$n$ $R$-matrix; the jet embedding $\ell_n$ and the descent $\mathfrak{d}_{n+1}$ satisfy

$$
  \ell_n(\sigma_i^{(n)}) = \sigma_i^{(n+1)}, \qquad
  \mathfrak{d}_{n+1}\colon H^{(n+1)}(q) \to H^{(n)}(q), \qquad
  \mathfrak{d}_{n+1} \circ \ell_n = \mathrm{id}.
$$

The :refterm[descent]{#descent} involution $\hat{\tau}_n = \ell_n \circ \mathfrak{d}_{n+1}$ splits the level-$(n{+}1)$ relations into **descended** (inherited from level $n$) and **transient** (genuinely new at level $n{+}1$). The presentation on $J^n(A)$ comprises 34 relations — 11 structural (level-$n$ lifts of QU/QUO), 4 :refterm[descent]{#descent}, and 9 cohomological, plus the 2 inter-level relations J-3c and J-4a — catalogued in [Table 1](#tbl:vertex-algebra-jet-relations-table1-data), [Table 2](#tbl:vertex-algebra-jet-relations-table2-data), and [Table 3](#tbl:vertex-algebra-jet-relations-table3-data).

## Proof

The relations are exhibited level by level.

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

Non-degeneracy requires $\det G^{(n)}_{ij} \neq 0$ at every brane level.

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

### JC-4: obstruction at level $n$

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

The obstruction persists: $\kappa_n \neq 0$ at every level, so the $R$-matrix possesses a nonzero transient component. Braiding at level $n{+}1$ is **not** exclusively determined by level $n$.

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

Every structural and cohomological relation holds precisely in $\mathcal{A}_\infty$. The global gluing condition requires locally defined braid words to patch into a well-defined element of the direct limit.

***

## IV. Summary: relations on $J^n(A)$

**Structural (level-$n$ lifts of QU/QUO)**:

See [Table 1](#tbl:vertex-algebra-jet-relations-table1-data).

**:refterm[Descent]{#descent} decomposition**:

See [Table 2](#tbl:vertex-algebra-jet-relations-table2-data).

**Cohomological (level-$n$ lifts)**:

See [Table 3](#tbl:vertex-algebra-jet-relations-table3-data).

The total presentation on $J^n(A)$ comprises **34 relations**: 11 structural (level-$n$ QU/QUO), 4 :refterm[descent]{#descent}, 9 cohomological, plus the 2 inter-level relations J-3c and J-4a that bind adjacent brane levels. Each is expressed entirely in the level-$n$ Hecke generators $\sigma_i^{(n)}$, the level-$n$ Markov trace $\mathrm{tr}_M^{(n)}$, and the :refterm[descent]{#descent} involution $\hat{\tau}_n$.
