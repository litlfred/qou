---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-004-23-the-automorphism-group
section_title: "The Automorphism Group"
section_number: 2.3
pages: 10-12
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.989
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
[]{#subsec: automorphism group label="subsec: automorphism group"}

As previously noted, the $\mathbb{P}^4$-model of Bring's curve shows that the automorphism group $\mathop{\mathrm{Aut}}(\mathcal{B})$ contains $S_5$. Hurwitz's theorem on the automorphism group $G=\mathop{\mathrm{Aut}}(\mathcal{C})$ of a curve of genus $g\ge2$ yields that $|G|\in\{84(g-1), 48(g-1), 40(g-1),\ldots \}$ and that if $p$ is a prime where $p\big| |G|$, then $p\in\{2,\ldots,g, g+1,2g+1\}$.

For genus $4$ this means $p\in\{2,3,5\}$ and so the maximal automorphism group of a genus $4$ curve has order strictly less than $84(g-1)$. In 1895 Wiman showed[^1]

::: prop
$\mathop{\mathrm{Aut}}(\mathcal{B}) = S_5$. This is the maximal possible automorphism group for a genus-4 surface, and Bring's curve is the only curve to achieve it.
:::

Wiman's proof was enumerative and produced equations for the curves with a given automorphism group. He had previously dealt with the hyperelliptic curves and their automorphism groups and for non-hyperelliptic curves $\mathcal{C}$ of genus 4 he began with the canonical embedding of the curve in $\mathbb{P}^3$ which meant that their automorphisms could be taken to be collineations, and so forming a subgroup of $PGL_4(\mathbb{C})$. Wiman's approach then used the fact (see [@Hartshorne1977 IV.5.2.2]) that the canonical embedding of a non-hyperelliptic curve of genus 4 is the complete intersection of an irreducible cubic surface and a unique quadric surface (which is either irreducible, or a cone). The uniqueness of the quadric $Q$ means that automorphisms of the curve become automorphisms of $Q$. In the case where $Q$ is of full rank we have that it is isomorphic to $\mathbb{P}^1 \times \mathbb{P}^1$, hence we know $\mathop{\mathrm{Aut}}(\mathcal{C})$ is isomorphic to a finite subgroup of $\mathop{\mathrm{Aut}}(\mathbb{P}^1 \times \mathbb{P}^1) = C_2 \ltimes (PGL_2(\mathbb{C}) \times PGL_2(\mathbb{C}))$ and that using the coordinates of $\mathbb{P}^1 \times \mathbb{P}^1$ Wiman could express the curve $\mathcal{C}$ as an equation of bidegree $(3,3)$ in terms of these. In the singular case $Q$ is a quadric cone and by projecting from a point of the cone meant that $\mathcal{C}$ could be expressed as a plane sextic. In both cases Wiman could write equations for possible genus $4$ curves and his strategy was to look at the restrictions on these imposed by symmetries of orders $2$, $3$ and $5$. For curves without an order $5$ element the maximal order of symmetry group was $72$ for $Q$ either a smooth quadric or cone. Including an order $5$ element yielded a maximal symmetry group of order $120$ only in the case of the smooth quadric with the resulting curve being Bring's. In the case of Bring's curve the quadric $Q$ is the quadric $\mathcal{Q}$ we determined earlier. Different proofs of Wiman's result may be found in [@Kuribayashi1990; @Magaard2002].

It is clear from the $\mathbb{P}^4$-model that $\mathop{\mathrm{Aut}}(\mathcal{B})$ may be realised as projective transforms via the permutation representation of $S_5$ acting on the subspace $\sum_i x_i = 0$; it is also clear that it may be be realised as a subgroup of $PGL_4(\mathbb{C})$ via the induced action on the differentials or equivalently the $L_a$'s. What is non-trivial is the following fact.

::: theorem
[]{#autA5 label="autA5"} The $A_5$ subgroup of $\mathop{\mathrm{Aut}}(\mathcal{B})$ can be realised as a group of collineations in the HC-model, that is, can be realised as a subgroup of $PGL_3(\mathbb{C})$.
:::

::: proof
*Proof.* We will be explicit about the construction here as this will be profitable later; [@Braden2012] explains how this representation follows from [@Dye1995]. The group $A_5$ has two inequivalent irreducible three-dimensional representations, one of which is given by $\left\langle R, S \right\rangle$ where $$R:=\frac1{\sqrt5}\begin{pmatrix}
    1 & 2                 & 2 \\
    1 & \zeta^2+\zeta^{-2}&\zeta+\zeta^{-1}  \\
    1 & \zeta+\zeta^{-1}  & \zeta^2+\zeta^{-2}
  \end{pmatrix}, \, {R}^2=I , \,  
  S:=\begin{pmatrix}1&&\\ &\zeta&\\ &&\zeta^{-1}\end{pmatrix},\  {S}^5=I, \,  (RS)^3=I  .$$ Note the other inequivalent irreducibel 3-dimensional representation comes from replacing $\zeta$ in the above with $\zeta^2$ or $\zeta^3$. The invariants of the representation $\left\langle R, S \right\rangle$ (when acting on $(X,Y,Z)^T$ via left multiplication) are $$\begin{aligned}
i_2 &=\left( \frac{X}{2} \right)^2+\sum_{k=0}\sp4\left(\frac{\frac{X}{2}+Y\zeta^k+Z\zeta^{-k}}{\sqrt{5}}\right)^2=\frac{1}{2}X^2+2YZ,\\
i_6 &=\left( \frac{X}{2} \right)^6+\sum_{k=0}\sp4\left(\frac{\frac{X}{2}+Y\zeta^k+Z\zeta^{-k}}{\sqrt{5}}\right)^6,\\
i_{10} &=\left( \frac{X}{2} \right)^{10}+\sum_{k=0}\sp4\left(\frac{\frac{X}{2}+Y\zeta^k+Z\zeta^{-k}}{\sqrt{5}}\right)^{10},\\
i_{15} &= \left \lvert\frac{\partial\{ i_2,i_{6},i_{10}\} }{\partial \{X,Y,Z\}} \right \rvert.
\end{aligned}$$ There is a polynomial relation between $i_{15}\sp{ 2}$ and $i_2$, $i_6$, $i_{10}$. In particular the vanishing of $i_6-\lambda i_2^3$ gives us Dye's one-parameter family of $A_5$-invariant sextics in $\mathbb{P}\sp2$; this pencil appears to have first been studied by Winger [@Winger1925]. This pencil yields genus-10 curves for generic $\lambda$ [@Dye1995].[^2] The special value of $\lambda=13/100$[^3] yields a genus-4 curve, namely Bring's curve, as we have that $$\frac1{12}\left(100 i_6-13 i_2\sp{ 3} \right)= X(Y^5+Z^5)+(XYZ)^2-X^4 YZ-2(YZ)^3 = F(X,Y,Z)  .$$ ◻
:::

To complete our picture, we use the following result.

::: prop
[]{#prop: U is an automorphism label="prop: U is an automorphism"} The map $$U:\left( x,y \right) \mapsto \left( -\frac{y^5 + x^3y - 3xy^2 + 1}{(y-x^2)(y^3-x)}, - \frac{y^2x-1}{y^3-x} \right)$$ is an automorphism of the HC-model, and together with $R$ and $S$ generates the entire automorphism group $S_5$.
:::

::: proof
*Proof.* The proof that $U$ is an automorphism is simple algebraic verification. In order to find this map, we adapted the methods of [@Bruin2019]. To see that $\left\langle R,S,U \right\rangle \cong S_5$, note that $U$ is of order $4$, for example by checking that it has the orbit $a \mapsto c \mapsto b \mapsto d \mapsto a$. As such, $U$ corresponds to an odd permutation under the isomorphism $\mathop{\mathrm{Aut}}(\mathcal{B}) \cong S_5$, and a single odd permutation and all of $A_5$ together generate $S_5$. ◻
:::

By fixing a map from the HC-model to the $\mathbb{P}^4$-model as we did in the proof of Proposition [\[prop: HC valid model for Bring\]](#prop: HC valid model for Bring){reference-type="ref" reference="prop: HC valid model for Bring"}, we have fixed an isomorphism from the automorphism group of the curve (in the HC-model) to $S_5$, which we shall denote $\psi : \left\langle R,S,U \right\rangle \to S_5$. For example, it is simple to verify that we have $U^2([X:Y:Z]) = [X:Z:Y]$. We see $U^2([L_1: L_2: L_3: L_4]) = [L_2 : L_1 : L_4 : L_3]$, and so $U^2([x_1: x_2 : x_3 : x_4 : x_5]) = [x_2 : x_1 : x_4 : x_3 : x_5]$, that is $(12)(34)$. Through similar calculation we can find $$\begin{aligned}
    \psi(R) &= (13)(24), \quad
    \psi(S) = (1 3 4 2 5),\quad
    \psi(U) = (1 3 2 4).
\end{aligned}$$There are myriad choices that can be made in constructing the birational transformation (such as the labelling of the coordinates in $\mathbb{P}^3$ and the ordering of the rows of $A$, or indeed composing with any automorphism of the $\mathbb{P}^4$-model), and changing these would give different isomorphisms to $S_5$.

As we have previously described, the uniqueness of the quadric $Q$ whose intersection with a cubic yields the canonical model of the curve leads to an isomorphism of the automorphism group of the curve and a subgroup of $\mathop{\mathrm{Aut}}(Q)$. For Bring's curve $\mathcal{Q} \cong\mathbb{P}^1 \times \mathbb{P}^1$ and we obtain an isomorphism from $S_5$ to a subgroup of $\mathop{\mathrm{Aut}}(\mathbb{P}^1 \times \mathbb{P}^1) = \mathbb{Z}_2 \ltimes (PGL_2(\mathbb{C}) \times PGL_2(\mathbb{C}))$ which we now write down. Let $([u:v], [z:w])$ be the coordinates on $\mathbb{P}^1 \times \mathbb{P}^1$, then using the birational map constructed in Proposition [\[prop: HC valid model for Bring\]](#prop: HC valid model for Bring){reference-type="ref" reference="prop: HC valid model for Bring"} one can conjugate the standard irreducible 4-dimensional representation of $S_5$ on $[x_1: x_2 : x_3 : x_4]$ to an action on $[v_1 : v_2 : v_3 : v_4]$. The resulting action of $(12)$ is (projectively) $$\begin{aligned}
\label{can12}
    \begin{pmatrix}
    v \\ u
    \end{pmatrix} &\mapsto \begin{pmatrix}
    j & -1 \\ -1 & -j
    \end{pmatrix} \begin{pmatrix}
    w \\ z
    \end{pmatrix}:=A \begin{pmatrix}
    w \\ z
    \end{pmatrix}, \quad
    \begin{pmatrix}
    w \\ z
    \end{pmatrix} \mapsto \begin{pmatrix}
    -1 & j-1 \\ j-1 & 1
    \end{pmatrix}\begin{pmatrix}
    v \\ u
    \end{pmatrix}:=B\begin{pmatrix}
    v \\ u
    \end{pmatrix}, 
\end{aligned}$$ where $j = - \zeta^3 - \zeta^2$ satisfies $j^2-j-1=0$; that is it is the $j$ defined by Dye. One can show that $(34)$ has the same action, where the other root $j^\prime = \zeta^3+\zeta^2+1$ is taken. One can check that $AB = 1 \in PGL_2(\mathbb{C})$, consistent with the fact that $(12)^2=1 \in S_5$. Note the transposition interchanges the two copies of $\mathbb{P}^1$, which is the action of the semi-direct product with $\mathbb{Z}_2$. Combining the two transforms one gets that $(12)(34)$ acts as $$[u:v] \mapsto [-v:u] \, , \quad [z:w] \mapsto [-w:z]  .$$ This fixes each copy of $\mathbb{P}^1$ and is the antipodal map on each. Moreover, we can calculate the action of $(145)$ on the copies to be $$\begin{aligned}
\label{can145}
    \begin{pmatrix}
    v \\ u
    \end{pmatrix} &\mapsto \begin{pmatrix}
    \zeta & -\zeta^3-\zeta \\ -\zeta^2-1 & -\zeta^2
    \end{pmatrix} \begin{pmatrix}
    v \\ u
    \end{pmatrix}, \quad
    \begin{pmatrix}
    w \\ z
    \end{pmatrix} \mapsto \begin{pmatrix}
    \zeta^3+1 & \zeta^2 \\ \zeta^4 & -\zeta^3-\zeta
    \end{pmatrix}\begin{pmatrix}
    w \\ z
    \end{pmatrix} . 
\end{aligned}$$ As $\left\langle (12)(34), (145) \right\rangle \cong A_5$, we discover that the action of $A_5$ does not interchange the two copies of $\mathbb{P}^1$, but odd-parity elements in $S_5$ do. Here $A_5$ is given by the diagonal embedding in $PGL_2(\mathbb{C}) \times PGL_2( \mathbb{C})$.

[^1]: An English translation of Wiman's paper has been produced [@DisneyHogg2022].

[^2]: A variation on this pencil has been used to explain why Bring's curve is uniquely defined as an $A_5$-invariant curve of genus 4, but there is a 1-parameter family of dimension-4 $A_5$-invariant principally polarised abelian varieties, deforming $\mathop{\mathrm{Jac}}\mathcal{B}$ [@Zi2021; @Looijenga2021]. The paper [@Melliez2003] gives further interesting representation theoretic perspectives on Bring's curve.

[^3]: For $\lambda=17/180$ the curve is of genus 0; for $\lambda=1/10$ the curve is reducible.
