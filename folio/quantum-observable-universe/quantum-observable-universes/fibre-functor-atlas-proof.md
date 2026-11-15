*Proof.*
(1) A fibre functor $\tau'$ assigns to each object $X$ in
$\mathbf{C}$ an $R$-module $\tau'(X)$ and to each morphism
$f$ a linear map $\tau'(f)$, preserving the tensor product.
This is a concrete coordinate system for the abstract
category — an affine chart.

(2) By the Tannaka–Krein theorem
([$\mathrm{SU}(2)$ emergence](#thm:su2-emergence)), any monoidal natural
isomorphism $\eta \colon \tau' \xrightarrow{\sim} \tau''$
is determined by an element $g \in G = \mathrm{Aut}^{\otimes}(\tau)$
acting on the fibre. The set of all such isomorphisms is a
principal homogeneous space for $G$ — a $G$-torsor.

(3) If $\eta_{01} \colon \tau' \to \tau''$ and
$\eta_{12} \colon \tau'' \to \tau'''$ are monoidal natural
isomorphisms, their composition $\eta_{12} \circ \eta_{01}$
is the unique monoidal natural isomorphism $\tau' \to \tau'''$
corresponding to the group product $g_{12} \cdot g_{01}$.
The cocycle identity $g_{02} = g_{12} \cdot g_{01}$ is
the associativity of composition in the functor category.

(4) Connectedness: any two fibre functors are isomorphic
(Tannaka–Krein). Simple transitivity: the isomorphism is
unique up to $G$. $\square$
