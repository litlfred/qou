**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
with $G = \mathrm{Aut}^{\otimes}(\tau)$
([Tannaka–Krein](#rem:tannaka-krein-overview)).  In the following,
$\tau_1, \tau_2$ denote arbitrary fibre functors on $\mathbf{C}$
(not the canonical $\tau$).  Then:*

1. **(Charts.)** *Each fibre functor
   $\tau_1 \colon \mathbf{C} \to \mathbf{Vect}_R$ is an
   affine chart: a concrete realisation of the abstract
   categorical data as linear algebra over $R$.  The contact
   affine chart on $\mathbb{P}(V)$
   ([contact affine chart](#def:contact-affine-chart)) is the
   chart associated to the canonical fibre functor $\tau$.*

2. **(Transitions.)** *For any two fibre functors
   $\tau_1, \tau_2$, the set of monoidal natural isomorphisms
   $\tau_1 \xrightarrow{\sim} \tau_2$ is a $G$-torsor.  Each
   such isomorphism is a transition function: a change of
   affine coordinates relating the two observers' descriptions
   of the same categorical data.*

3. **(Cocycle condition.)** *Given three fibre functors
   $\tau_1, \tau_2, \tau_3$ with transition isomorphisms
   $g_{01}, g_{12}, g_{02}$, functoriality of composition
   forces $g_{02} = g_{12} \circ g_{01}$.  The cocycle
   condition is not imposed — it is automatic.*

4. **(Atlas.)** *The category of all fibre functors on
   $\mathbf{C}$, with monoidal natural isomorphisms as
   morphisms, is a $G$-gerbe: a connected groupoid on which
   $G$ acts simply transitively.  This is the **affine atlas**
   of the quantum observable universe.*

*Proof.*
(1) A fibre functor $\tau_1$ assigns to each object $X$ in
$\mathbf{C}$ a vector space $\tau_1(X)$ and to each morphism
$f$ a linear map $\tau_1(f)$, preserving the tensor product.
This is a concrete coordinate system for the abstract
category — an affine chart.

(2) By the Tannaka–Krein theorem
([SU(2) emergence](#thm:su2-emergence)), any monoidal natural
isomorphism $\eta \colon \tau_1 \xrightarrow{\sim} \tau_2$
is determined by an element $g \in G = \mathrm{Aut}^{\otimes}(\tau)$
acting on the fibre.  The set of all such isomorphisms is a
principal homogeneous space for $G$ — a $G$-torsor.

(3) If $\eta_{01} \colon \tau_1 \to \tau_2$ and
$\eta_{12} \colon \tau_2 \to \tau_3$ are monoidal natural
isomorphisms, their composition $\eta_{12} \circ \eta_{01}$
is the unique monoidal natural isomorphism $\tau_1 \to \tau_3$
corresponding to the group product $g_{12} \cdot g_{01}$.
The cocycle identity $g_{02} = g_{12} \cdot g_{01}$ is
the associativity of composition in the functor category.

(4) Connectedness: any two fibre functors are isomorphic
(Tannaka–Krein).  Simple transitivity: the isomorphism is
unique up to $G$.  $\square$
