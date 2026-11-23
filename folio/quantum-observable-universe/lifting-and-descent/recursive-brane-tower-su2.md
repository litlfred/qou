Continuing the [jet prolongation for SU(2)](#ex:jet-prolongation-su2), one constructs the explicit brane tower for $G = \mathrm{SU}(2)$.

**Level 0.** $A_0 = \mathcal{O}(\mathrm{SU}(2))$, the coordinate ring of polynomial functions on $\mathrm{SU}(2)$. As an $\mathrm{SU}(2)$ representation, it decomposes via Peter–Weyl as $A_0 \cong \bigoplus_{j \geq 0} V_j \otimes V_j^*$, where $V_j$ denotes the spin-$j$ representation of dimension $2j + 1$.

**Level 1.** $A_1 = J^1(A_0) = A_0 \otimes \Omega^1(A_0)$. Because $\Omega^1(A_0) \cong A_0 \otimes \mathfrak{su}(2)^*$ and $\mathfrak{su}(2)^* \cong V_1$, one strictly obtains:
$$
  A_1 \cong \Gamma\bigl(F(\mathrm{SU}(2))\bigr),
$$
the sections of the frame bundle. Each Peter–Weyl summand $V_j \otimes V_j^*$ in $A_0$ explicitly contributes $(V_j \otimes V_1) \otimes V_j^*$ in $A_1$, dictating a $3$-fold multiplicity increase.

**Level 2.** $A_2 = J^1(A_1) \cong \Gamma(J^2(\mathrm{SU}(2)))$, the sections of the second jet bundle. Each representation factor gains another tensor with $V_1$, yielding summands of the form $(V_j \otimes V_1 \otimes V_1) \otimes V_j^*$. The Clebsch–Gordan decomposition $V_1 \otimes V_1 \cong V_0 \oplus V_1 \oplus V_2$ explicitly caps the growth: no irreducible representation of spin $> j + 2$ appears at level $2$ unless the tensor product strictly forces it.

**Stabilization.** Because $\dim \mathrm{SU}(2) = 3$, the jet bundle $J^k(\mathrm{SU}(2))$ has a polynomially growing fibre dimension $\binom{k + 3}{3}$. However, the *tower of gerbes* $\mathfrak{G}_0 \to \mathfrak{G}_1 \to \mathfrak{G}_2 \to \cdots$ physically stabilizes at level $n = 3$. For $n \geq 3$, the obstruction classes $\kappa_n$ strictly repeat the pattern set by $\kappa_0, \kappa_1, \kappa_2$ because a single class identically generates $H^2(\mathbb{CP}^1, \mathcal{O}^{\times}) \cong \mathbb{Z}$.

**The tower.** The complete brane tower for $\mathrm{SU}(2)$ is:
$$
  A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots
$$
where each embedding acts as the unit section of the jet prolongation. Each $A_n$ forms a $(3^n \cdot \dim A_0)$-dimensional object in $\mathrm{Rep}(\mathrm{SU}(2))$.
