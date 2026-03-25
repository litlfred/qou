Before stating the definition of a quantum observable universe, we
fix two pieces of notation that will appear throughout.

**The fundamental object $V$.**
In a rigid monoidal category $\mathbf{C}$, the *fundamental object*
$V$ is the unique (up to isomorphism) simple object of categorical
dimension $2$. Its dimension is not an independent assumption but is
*forced* by the volume constraint (Axiom 4 below): the existence of a
non-degenerate epimorphism $\epsilon \colon \Lambda^2 V \to \mathbf{1}$
requires $\Lambda^2 V$ to have rank $1$, which holds if and only if
$\operatorname{rank}(V) = 2$. (If $\operatorname{rank}(V) = 1$ then
$\Lambda^2 V = 0$ and no such epimorphism exists; if
$\operatorname{rank}(V) \geq 3$ then
$\operatorname{rank}(\Lambda^2 V) \geq 3$ and the non-degenerate
epimorphism to the rank-$1$ unit object $\mathbf{1}$ cannot exist.)
In the SU(2) example
([Example](#ex:rigid-monoidal-vect)), $V = V_{1/2} \cong \mathbb{C}^2$
is the defining (spin-$\tfrac{1}{2}$) representation. Every other
simple object $V_j$ is an exterior or symmetric power of $V$, so $V$
generates $\mathbf{C}$ as a tensor category.

**The emergent gauge group $G = \mathrm{Aut}^{\otimes}(\tau)$.**
Let $\tau \colon \mathbf{C} \to R\text{-}\mathrm{Mod}$ be the
forgetful functor. The *tensor automorphism group*
$G = \mathrm{Aut}^{\otimes}(\tau)$ consists of all monoidal natural
automorphisms of $\tau$: families of $R$-module automorphisms
$\{g_X \colon \tau(X) \xrightarrow{\sim} \tau(X)\}_{X \in \mathbf{C}}$
compatible with the tensor product. By Tannaka--Krein duality, $G$ is
an affine group scheme over $R$, and $\tau$ establishes a monoidal
equivalence $\mathbf{C} \simeq \mathrm{Rep}(G)$. No group is
postulated *a priori*; it *emerges* from $(\mathbf{C}, \tau)$.
