---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-018-46-signs
section_title: "Signs"
section_number: 4.6
pages: 52-54
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.983
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
[]{#sec:signs label="sec:signs"}

In order to determine the signs appearing in the counts of triangles, we need to specify the brane structures on the Lagrangians $L(d)$. Since $L(d)$ fibers over a curve in the base, and its intersection with each fiber is a curve, the tangent bundle of $L(d)$ is trivial, and we can define a framing of $TL(d)$ using the vertical and horizontal tangent vectors at each point. Using this framing, we can give $L(d)$ a trivial $\Spin(2)$ structure, which is induced by product of the trivial $\Spin(1)$ structures on the horizontal an vertical tangent bundles.

Although we have not said much about it up until now, strictly speaking the generators of $CF^*(L(d_1),L(d_2))$ are not canonically identified with intersection points $q \in L(d_1)\cap L(d_2)$. Rather, each intersection point $q$ gives rise to an abstract $1$-dimensional $\R$--vector space, the orientation line $o(q)$. Following [@seidel-book Ch. 11], this line is canonically isomorphic up to multiplication by a positive number with the determinant line of a certain Fredholm operator $D_q$. The moduli space of pseudo-holomorphic curves is canonically oriented relative to these lines.

In the case $d_1 \leq d_2$, where all the intersections have degree $0$, there is a preferred choice of trivialization for $o(q)$. Let $q
\in L(d_1)\cap L(d_2)$. Then we have horizontal-vertical splittings $$T_qL(d_i) = (T_qL(d_i))^h \oplus (T_qL(d_i))^v$$ The intersection point $q$ has degree $0$ as a morphism from $L(d_1)$ to $L(d_2)$, and moreover both $(T_qL(d_i))^h$ and $(T_qL(d_i))^v$ tilt clockwise by a small amount as we pass from $L(d_1)$ to $L(d_2)$.

Let $H$ denote the half-plane with a negative puncture. We define the orientation operator $D_q = D_q^h \oplus D_q^v$, acting on the product bundle $\C\times \C \to H$, where the boundary condition in the first factor is the short path $(T_qL(d_1))^h\to (T_qL(d_2))^h$, while that in the second factor is the short path $(T_qL(d_1))^v \to
(T_qL(d_2))^v$. By [@seidel-book Eq. (11.39)], there is a canonical isomorphism $$\det(D_q) \cong o(q)$$ which for our purposes we take as the definition of $o(q)$. On the other hand, $D_q$ is the direct sum of the operators $D_q^h$ and $D_q^v$, which have vanishing kernel and cokernel. Hence $$\det(D_q) \cong \det(D_q^h)\otimes \det(D_q^v) \cong \R \otimes \R
  \cong \R$$ where all isomorphisms are canonical. This gives us a preferred choice of isomorphism $o(q) \cong \R$.

::: proposition
[]{#prop:signs label="prop:signs"} Taking the preferred isomorphisms $o(q) \cong \det(D_q)\cong \R$ for all generators $q \in CF^0(L(d_1),L(d_2))$ for $d_1 \leq d_2$, all of the holomorphic triangles found above have the same sign. Hence, after possibly reversing all off the preferred isomorphisms $o(q) \cong \R$, all of them have a positive sign.
:::

::: proof
*Proof.* Let $u: S \to X(B)$ be a triangle with positive punctures at $q_1
  \in CF^0(L(d_1),L(d_2))$ and $q_2 \in CF^0(L(d_2),L(d_3))$ and negative puncture at $q_0 \in CF^0(L(d_1),L(d_3))$. Let $D_u$ denote the linearized operator at $u$. Gluing onto $D_u$ the chosen orientation operators $D_{q_2}$ and $D_{q_1}$ in that order gives another orientation operator $D_{q_0}'$ for the point $q_0$, and we want to compare the two orientations for the line $o(q_0)$.

The linearized operator $D_u$ is an operator in the pulled back tangent bundle $u^*TX(B)$. The bundle $TX(B)$ has a splitting into horizontal and vertical subspaces $TX(B) = TX(B)^h \oplus TX(B)^v$ given by the symplectic connection. Over the boundaries of $S$, the Lagrangian boundary condition also splits. Recall from the discussion on gradings in Section [\[sec:gradings\]](#sec:gradings){reference-type="ref" reference="sec:gradings"} that we have phase maps on horizontal and vertical subspaces, which measure rotation with respect to the foliations by circles on the base and fiber respectively. These serve to give us preferred trivializations of $u^*TX(B)^h$ and $u^*TX(B)^v$. With respect to these trivializations, the Lagrangian boundary conditions move only by a small amount: in the horizontal space, $TL^h$ has essentially constant phase, while in the vertical space, $TL^v$ moves in such a way that it never crosses the the line corresponding to the circle foliation on the fibers.

The next step is to observe that the boundary conditions for the operator $D_u$ are essentially the same independent of the map $u$ and of the chosen degree zero generators $q_0, q_1, q_2$, and that hence all of the maps $u$ must contribute with the same sign. In all cases we have an operator in a trivial rank two vector bundle, with split Lagrangian boundary conditions, each factor of which is trivial. Additionally, each pair of Lagrangians at a puncture has the same local form, namely they are related by a small clockwise rotation in both the horizontal and vertical directions. The orientation operators $D_{q_i}$ used to define the orientation lines are also essentially the same for every point $q_i$. Hence the relative sign between the determinant of $D_{q_0}'$ and $o(q_0)$ must be the same for each map $u$.

If the signs are all positive, we are done. Otherwise by reversing our choice of generator for every line $o(q)$ we obtain bases for the groups $CF^0(L(d_1),L(d_2))$ in which all curves contribute positively. ◻
:::

::: remark
The preceding proposition is another example of the phenomenon observed by Abouzaid [@abouzaid06 Lemma 3.21]. A similar argument is found in [@seidel-book (13c)].
:::
