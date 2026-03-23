Before stating the definition of a quantum observable universe, we
fix two pieces of notation that will appear throughout.

**The fundamental object $V$.**
In a rigid monoidal category $\mathcal{C}$, the *fundamental object*
$V$ is the unique (up to isomorphism) simple object of categorical
dimension $2$. In the SU(2) example
([Example](#ex:rigid-monoidal-vect)), $V = V_{1/2} \cong \mathbb{C}^2$
is the defining (spin-$\tfrac{1}{2}$) representation. Every other
simple object $V_j$ is an exterior or symmetric power of $V$, so $V$
generates $\mathcal{C}$ as a tensor category.

**The emergent gauge group $G = \mathrm{Aut}^{\otimes}(\tau)$.**
Let $\tau \colon \mathcal{C} \to R\text{-}\mathrm{Mod}$ be the
forgetful functor. The *tensor automorphism group*
$G = \mathrm{Aut}^{\otimes}(\tau)$ consists of all monoidal natural
automorphisms of $\tau$: families of $R$-module automorphisms
$\{g_X \colon \tau(X) \xrightarrow{\sim} \tau(X)\}_{X \in \mathcal{C}}$
compatible with the tensor product. By Tannaka--Krein duality, $G$ is
an affine group scheme over $R$, and $\tau$ establishes a monoidal
equivalence $\mathcal{C} \simeq \mathrm{Rep}(G)$. No group is
postulated *a priori*; it *emerges* from $(\mathcal{C}, \tau)$.
