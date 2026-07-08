<!-- FILE_START: cosimplicial-intro.md -->
The recursive brane tower carries a higher-categorical structure organising the transitions between levels into a cosimplicial crossed groupoid. Yekutieli's framework for central extensions of gerbes \cite{yekutieli2010} supplies exactly the triples $(x, g, a)$ required to define the face and degeneracy maps.

We proceed in three stages. First, we fix the cosimplicial crossed groupoid structure on the brane tower by verifying the cosimplicial identities. Second, we translate these identities into the Yekutieli cocycle conditions, providing the obstruction theory for lifting morphisms from $A_n$ to $A_{n+1}$. Third, we assemble the cocycle data into the central-extension class governing the tower. This class reappears in fluid dynamics as the obstruction class $\kappa_n$ controlling the $q$-Navier–Stokes degeneration.

Scope note: The cosimplicial structure naturally hosts the descent involution. Readers comfortable with the explicit level-by-level arguments may treat this section as an abstract reformulation, extracting the explicit cocycle conditions only when required downstream.
<!-- FILE_END: cosimplicial-intro.md -->

<!-- FILE_START: yekutieli-triple.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with recursive brane tower $\{A_n\}_{n \geq 0}$ ([recursive brane tower](#def:recursive-brane-tower)) and substrate parameter $q$. Let $\{U_i\}$ be a covering of the underlying site $\mathcal{S}$ trivialising every level of the tower. The **Yekutieli triple** at level $n$ over an intersection $U_i \cap U_j$ is the datum $(x_{ij}^{(n)}, g_{ij}^{(n)}, a_{ij}^{(n)})$, where:

1. **Objects.** $x_i^{(n)} \in \mathrm{Ob}(\mathfrak{G}_n|_{U_i})$ are local trivialisations of the Frobenius--Hopf object $A_n$.
2. **$1$-morphisms.** $g_{ij}^{(n)} \colon x_i^{(n)} \to x_j^{(n)}$ are the transition automorphisms in $\mathrm{Aut}_{\mathbf{C}}(A_n|_{U_i \cap U_j})$. They encode the patching data of the comultiplication $\Delta_n$.
3. **$2$-morphisms.** $a_{ij}^{(n)} \colon g_{ij}^{(n)} \Rightarrow g_{ij}^{(n+1)}$ are the deformation parameters living in the band $\mathcal{B}$. They implement the lift of transition automorphisms from level $n$ to level $n{+}1$.

The assignment $n \mapsto (x^{(n)}, g^{(n)}, a^{(n)})$ is functorial. The jet prolongation ([jet prolongation](#prop:jet-prolongation)) sends the triple at level $n$ to the triple at level $n{+}1$. The :refterm[descent]{#descent} homomorphism $\mathfrak{d}_{n+1}$ ([:refterm[descent]{#descent}](#lem:descent)) reverses this assignment. In the archimedean realisation, $g_{ij}^{(n)} \in \Gamma(U_i \cap U_j, \mathrm{SU}_{q_n}(2))$ are gauge transition functions and $a_{ij}^{(n)} \in \mathcal{O}_M^{\times}$.
<!-- FILE_END: yekutieli-triple.md -->

<!-- FILE_START: cosimplicial-crossed-groupoid.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with recursive brane tower $\{A_n\}_{n \geq 0}$ ([recursive brane tower](#def:recursive-brane-tower)) and substrate parameter $q$. Equipped with the Yekutieli triples $(x^{(n)}, g^{(n)}, a^{(n)})$ ([Yekutieli triple](#def:yekutieli-triple)), the assignment

$$
  [n]  \longmapsto  \mathfrak{G}_n
$$

from the simplex category $\Delta$ to the $2$-category of gerbes on $M$ extends to a *cosimplicial crossed groupoid*. In this cosimplicial object:

1. The coface maps $\delta^i \colon \mathfrak{G}_{n} \to \mathfrak{G}_{n+1}$ are given by jet prolongation acting on objects (inserting the $i$-th degeneracy in the Cech nerve).
2. The codegeneracy maps $\sigma^j \colon \mathfrak{G}_{n+1} \to \mathfrak{G}_{n}$ are given by the :refterm[descent]{#descent} homomorphism $\mathfrak{d}_{n+1}$ (collapsing the $j$-th face).
3. The crossed structure is furnished by the conjugation action of the $1$-morphisms $g_{ij}^{(n)}$ on the $2$-morphisms $a_{ij}^{(n)}$ via the adjoint representation of $\mathrm{SU}_{q_n}(2)$.
<!-- FILE_END: cosimplicial-crossed-groupoid.md -->

<!-- FILE_START: ccg-cosimplicial-identities.md -->
**Definition.** *The coface maps $\delta^i$ (composites of jet prolongation with Cech face maps) and codegeneracy maps $\sigma^j$ (composites of :refterm[descent]{#descent} with Cech degeneracy maps) satisfy the cosimplicial identities:*

$$
  \delta^j \circ \delta^i = \delta^i \circ \delta^{j-1} \;(i < j),
  \quad
  \sigma^j \circ \sigma^i = \sigma^i \circ \sigma^{j+1} \;(i \leq j).
$$

*They also satisfy the mixed identities. Each case reduces either to disjoint-support commutation or to the retraction $\mathfrak{d}_{n+1} \circ \ell_n = \mathrm{id}$.*
<!-- FILE_END: ccg-cosimplicial-identities.md -->

<!-- FILE_START: ccg-crossed-module-structure.md -->
*At each level $n$, the pair $(\mathrm{SU}_{q_n}(2), \mathcal{O}_M^{\times})$ is a crossed module \cite{yekutieli2010}, with boundary $\partial(a) = a \cdot \mathbf{1}$ and conjugation action $g \cdot a = g a g^{-1}$.*
<!-- FILE_END: ccg-crossed-module-structure.md -->

<!-- FILE_START: jet-as-descent.md -->
In the cosimplicial crossed groupoid of [cosimplicial crossed groupoid](#prop:cosimplicial-crossed-groupoid), the coface map $\delta^0 \colon \mathfrak{G}_n \to \mathfrak{G}_{n+1}$ applied to a local section $x_i^{(n)}$ produces the jet-prolonged section $x_i^{(n+1)} = J^1(x_i^{(n)})$. This is precisely the content of [jet prolongation](#prop:jet-prolongation): the jet prolongation acts as a formal :refterm[descent]{#descent} of information from the higher categorical level $\mathfrak{G}_{n+1}$ to the lower level $\mathfrak{G}_n$, packaged as a coface map. The retraction property $\sigma^0 \circ \delta^0 = \mathrm{id}$ shows that the codegeneracy $\sigma^0 = \mathfrak{d}_{n+1}$ inverts this map, underpinning the :refterm[descent]{#descent} involution ([:refterm[descent]{#descent} involution](#def:descent-involution)).
<!-- FILE_END: jet-as-descent.md -->

<!-- FILE_START: descent-condition.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with recursive brane tower $\{A_n\}_{n \geq 0}$ and substrate parameter $q$. Given Yekutieli triples $(x^{(n)}, g^{(n)}, a^{(n)})$ ([Yekutieli triple](#def:yekutieli-triple)) and the distributional connection $A_\infty = \sum_{n,i} c_{n,i} \alpha_{n,i}$ ([distributional connection](#rem:distributional-connection)), the global consistency of $A_\infty$ is equivalent to the *twisted $2$-cocycle condition*: for every triple intersection $U_i \cap U_j \cap U_k$,

```tex
\begin{equation}\label{eq:twisted-2-cocycle}
  d\!\left(g_{ijk}^{(n)}\right)
  = 
  a_{ij}^{(n)} \cdot g_{ijk}^{(n)} \cdot \left(a_{jk}^{(n)}\right)^{-1},
\end{equation}
```

where $g_{ijk}^{(n)} = g_{ij}^{(n)} \cdot g_{jk}^{(n)} \cdot (g_{ik}^{(n)})^{-1}$ is the Cech $1$-cocycle deviation at level $n$, $d(g_{ijk}^{(n)})$ is the Cech coboundary (measuring failure of the $1$-cocycle condition), and $a_{ij}^{(n)}, a_{jk}^{(n)} \in \mathcal{O}_M^{\times}$ are the $2$-morphisms (quantum deformation feedback from $\mathrm{SU}_{q_n}(2)$).

Equivalently, the obstruction class $\kappa_n$ ([quantum characteristic classes](#def:quantum-characteristic-classes)) is the cohomology class of the twisted $2$-cocycle $[a_{ij}^{(n)} \cdot (\cdot) \cdot (a_{jk}^{(n)})^{-1}]$ in $H^2(M, \mathcal{O}_M^{\times})$.
<!-- FILE_END: descent-condition.md -->

<!-- FILE_START: descent-cocycle-deviation.md -->
*Under the central extension $\mathfrak{G}_{n+1} \to \mathfrak{G}_n$ with local lift data $a_{ij}^{(n)} \in \mathcal{O}_M^{\times}$, the cocycle deviation at level $n+1$ is:*

$$
  g_{ijk}^{(n+1)}
  =
  a_{ij}^{(n)} \cdot a_{jk}^{(n)} \cdot (a_{ik}^{(n)})^{-1}
  \cdot g_{ijk}^{(n)}.
$$

*Thus, the twisted Cech $2$-cocycle equation*

$$
  d(g_{ijk}^{(n)})
  =
  a_{ij}^{(n)} \cdot g_{ijk}^{(n)} \cdot (a_{jk}^{(n)})^{-1}
$$

*holds and possesses a cohomology class in $H^2(M, \mathcal{O}_M^{\times})$.*
<!-- FILE_END: descent-cocycle-deviation.md -->

<!-- FILE_START: weak-equiv-invariance.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with recursive brane tower $\{A_n\}_{n \geq 0}$, cosimplicial crossed groupoid structure ([cosimplicial crossed groupoid](#prop:cosimplicial-crossed-groupoid)), and substrate parameter $q$. Let $\tau \colon \mathcal{A}_\infty \to \mathbb{C}$ be the vacuum state ([vacuum state](#prop:vacuum-state)). A *weak equivalence* between brane levels $n$ and $m$ is a zigzag of coface and codegeneracy maps:

$$
  \mathfrak{G}_n
  \xleftarrow{\sigma}
  \mathfrak{G}_{k_1}
  \xrightarrow{\delta}
  \cdots
  \xrightarrow{\delta}
  \mathfrak{G}_m.
$$

For every observable $a \in \mathcal{A}_\infty$, the expectation value is invariant under weak equivalence:

$$
  \tau\!\bigl(\iota_n(a|_n)\bigr)
  = 
  \tau\!\bigl(\iota_m(a|_m)\bigr),
$$

where $\iota_n \colon \Gamma(J^1 \mathcal{S}_n, \mathrm{SU}_{q_n}(2)) \hookrightarrow \mathcal{A}_\infty$ is the canonical embedding and $a|_n$ restricts $a$ to level $n$. In particular, physical states (the GNS vectors of $\tau$) remain invariant under fluctuations of the substrate parameter $q(p)$ across brane levels.
<!-- FILE_END: weak-equiv-invariance.md -->

