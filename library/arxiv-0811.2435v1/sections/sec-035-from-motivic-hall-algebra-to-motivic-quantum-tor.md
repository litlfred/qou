---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-035-from-motivic-hall-algebra-to-motivic-quantum-tor
section_title: "From motivic Hall algebra to motivic quantum torus"
section_number: null
pages: 95-102
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.993
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
Assume that $\CC$ is an ind-constructible $3d$ Calabi-Yau category endowed with polarization and orientation data $\sqrt{\cal D}$. The Hall algebra of $\CC$ is graded by the corresponding lattice $\Gamma$: $H(\CC)=\oplus_{\gamma\in \Gamma}H(\CC)_{\gamma}$. Main result of this section is the following theorem.

::: thm
The map $\Phi: H(\CC)\to {\cal R}_{\Gamma}$ given by the formula $$\Phi(\nu)=(\nu,w)\hat{e}_{\gamma}, \,\,\,\nu\in H(\CC)_{\gamma}$$ is a homomorphism of $\Gamma$-graded $\Q$-algebras. Here $w$ is the motivic weight and $(\bullet,\bullet)$ is the pairing between motivic measures and functions.
:::

In other words, the homomorphism $H(\CC)\to {\cal R}_{\Gamma}$ can be written as $$[\pi: Y\to Ob(\CC)]\mapsto$$ $$\mapsto \int_{Y}(1-MF(\pi(y)))\,(1-MF_0(Q_{\pi(y)}))\,{\mathbb L}^{-{1\over{2}}\op{rk}Q_{\pi(y)}}\,{\mathbb L}^{{1\over{2}}(\pi(y),\pi(y))_{\le 1}}\,\hat{e}_{\op{cl}(\pi(y))}\,\,,$$ where $\int_Y$ is understood as the direct image functor (see Section 4.2).

The natural extension of the above homomorphism to the completion of $\widehat{H}(\CC_V)$ maps the element $A_V^{\op{Hall}}$ to the element $A_V^{mot}$ defined in Section 6.2.

*Proof.* For simplicity we will present the proof of the Theorem for $$\nu_E:=[\delta_E:pt\to Ob(\CC)]\,\,,$$ where $\delta_E(pt)=E\in Ob(\CC(\k))$ is the "delta-function\". The general proof for equivariant constructible families is similar. We will also assume that our category is minimal on the diagonal.

The proof will consists of several steps.

*Step 1.*

We have:

$$\nu_{E_1}\cdot\nu_{E_2}={\mathbb L}^{-(E_2,E_1)_{\le 0}}[\pi_{21}:\op{Ext}^1(E_2,E_1)\to Ob(\CC)]\,\,,$$ the map $\pi_{21}$ is the restriction of the cone map[^1] $$tot(\op{Ker}(m_1:{\cal HOM}^0\to{\cal HOM}^1))\to Ob(\CC)$$ to the fiber over the point $(E_2[-1],E_1)$. Under this map the element $\alpha\in \op{Ext}^1(E_2,E_1)$ is mapped to the object $$E_{\alpha}=Cone(\alpha: E_2[-1]\to E_1)\,\,.$$

Let us denote by $\gamma_i$ the class $\op{cl}(E_i)\in \Gamma, i=1,2$. Then we have: $$\Phi(\nu_{E_i})={\mathbb L}^{{1\over{2}}(E_i,E_i)_{\le 1}}(1-MF_0(W_{E_i}^{min}))\,\overline{I}(h(E_i))\,\hat{e}_{\gamma_i},\,\,\, i=1,2\,\,,$$ where $h(E_i)$ is the value at $E_i$ of the element $h\in J_2(\CC)$ (i.e. the image of the restriction map to $J_2(\CC)$) given by the super line bundle $\sqrt{{\cal D}}\otimes {\cal D}_{\le 1}^{-1}$ with trivialized tensor square.

We have:

$$\Phi(\nu_{E_1})\Phi(\nu_{E_2})={\mathbb L}^{{1\over{2}}((E_1,E_1)_{\le 1}+(E_2,E_2)_{\le 1})}\times$$ $$\times\,{\mathbb L}^{{1\over{2}}((E_1,E_2)_{\le 1}-(E_2,E_1)_{\le 1})}(1-MF_0(W_{E_1}^{min}\oplus W_{E_2}^{min}))\overline{I}(h(E_1))\overline{I}(h(E_2))\,\hat{e}_{\gamma_1+\gamma_2}\,\,.$$ In order to obtain this formula we used the Calabi-Yau property, which implies that $$\begin{array}{rcl}
\langle \gamma_1,\gamma_2\rangle&=&\sum_{j\in \Z}(-1)^j(E_1,E_2)_j=(E_1,E_2)_{\le 1}+(E_1,E_2)_{\geqslant 2}=\\
&=&(E_1,E_2)_{\le 1}-(E_2,E_1)_{\le 1}\,\,,
\end{array}$$ where we employ the notation $(E_1,E_2)_{\geqslant m}=\sum_{j\geqslant m}(-1)^j(E_1,E_2)_j$. Also we used the motivic Thom-Sebastiani theorem for the Milnor fibers and the product formula for the basis elements in the motivic quantum torus ${\cal R}_{\Gamma}$.

On the other hand, we can apply $\Phi$ to the product $\nu_{E_1}\cdot \nu_{E_2}$ and obtain: $$\begin{array}{l}
\Phi(\nu_{E_1}\cdot \nu_{E_2})=\\
={\mathbb L}^{-(E_2,E_1)_{\le 0}}\int_{\alpha\in
\op{Ext}^1(E_2,E_1)}{\mathbb L}^{{1\over{2}}(E_{\alpha},E_{\alpha})_{\le
1}}(1-MF_0(W_{E_{\alpha}}^{min}))\overline{I}(h(E_{\alpha}))\hat{e}_{\gamma_1+\gamma_2}\,\,.
\end{array}$$

Using the identity $(E_2,E_1)_{\le 0}=(E_2,E_1)_{\le 1}+(E_2,E_1)_1$ (and also recall that $(E_2,E_1)_1=\dim \op{Ext}^1(E_2,E_1)$) and observing that $$(E_1\oplus E_2,E_1\oplus E_2)_{\le 1}=(E_1,E_1)_{\le 1}+(E_2,E_2)_{\le 1}+(E_1,E_2)_{\le 1}+(E_2,E_1)_{\le 1}$$ we arrive to the following equality which is equivalent to $$\Phi(\nu_{E_1}\cdot \nu_{E_2})=\Phi(\nu_{E_1})\Phi(\nu_{E_2})$$ and hence implies the Theorem:

$${\mathbb L}^{(E_2,E_1)_1}(1-MF_0(W_{E_1}^{min}\oplus W_{E_2}^{min}))\overline{I}(h(E_1))\overline{I}(h(E_2))=$$ $$=\int_{\alpha\in \op{Ext}^1(E_2,E_1)}{\mathbb L}^{{1\over{2}}((E_{\alpha},E_{\alpha})_{\le
1}-(E_1\oplus E_2,E_1\oplus E_2)_{\le 1})}(1-MF_0(W_{E_{\alpha}}^{min}))\overline{I}(h(E_{\alpha}))\,\,.$$

*Step 2.*

Now we would like to express the difference

$$(E_{\alpha},E_{\alpha})_{\le 1}-(E_1\oplus E_2,E_1\oplus E_2)_{\le 1}$$ as the rank of a certain linear operator. Recall that the object $E_{\alpha}$ can be thought of as a deformation of the object $E_0:=E_1\oplus E_2$. Therefore, there is a spectral sequence which starts at $\op{Ext}^{\bullet}(E_1\oplus E_2,E_1\oplus E_2)$ and converges to $\op{Ext}^{\bullet}(E_{\alpha},E_{\alpha})$. Using the $\A$-structure one can make it very explicit. Namely, let us denote by $d_{\alpha}:\op{Ext}^{\bullet}(E_1\oplus E_2,E_1\oplus E_2)\to \op{Ext}^{\bullet}(E_1\oplus E_2,E_1\oplus E_2)$ the differential of degree $+1$ given by the formula $$d_{\alpha}=m_2(\alpha,\bullet)+m_2(\bullet,\alpha)+m_3(\alpha,\bullet,\alpha)\,\,.$$ Then the graded vector space $\op{Ext}^{\bullet}(E_{\alpha},E_{\alpha})$ is isomorphic to the cohomology of $d_{\alpha}$ (cf. e.g. [@KoSo3], Remark 10.1.5).

It is clear that for any cohomological complex $(C^{\bullet},d)$ of finite-dimensional vector spaces we have the equality $$\sum_{i\le 1}(-1)^i\dim H^i(C)-\sum_{i\le 1}(-1)^i\dim C^i
=\op{rk}d^{(1)},$$ where $d^{(1)}: C^1\to C^2$ is the component of $d$. Applying this observation to our complex we obtain that $$(E_{\alpha},E_{\alpha})_{\le 1}-(E_1\oplus E_2,E_1\oplus E_2)_{\le 1}=\op{rk}d^{(1)}_{\alpha}.$$

*Step 3.*

Let us introduce a $\kk$-vector space $${\cal M}_{E_1,E_2}=\op{Ext}^1(E_1\oplus E_2, E_1\oplus E_2)=$$ $$=\op{Ext}^1(E_1,E_1)\oplus \op{Ext}^1(E_2,E_1)\oplus \op{Ext}^1(E_1,E_2)\oplus \op{Ext}^1(E_2,E_2)\,\,.$$ It can be interpreted as the tangent space to the moduli space of formal deformations of the object $E_1\oplus E_2$. We choose coordinates $(x,\alpha,\beta,y)$ on this space in such a way that $x$ denotes the coordinates on $\op{Ext}^1(E_1,E_1)$, $\alpha$ denotes the coordinates on $\op{Ext}^1(E_2,E_1)$, $\beta$ denotes the coordinates on $\op{Ext}^1(E_1,E_2)$ and $y$ denotes the coordinates on $\op{Ext}^1(E_2,E_2)$. Then the point $(0,\alpha,0,0)$ corresponds (by abuse of notation) to the isomorphism class $\alpha\in \op{Ext}^1(E_2,E_1)$ of an exact triangle $E_1\to E_{\alpha}\to E_2$. Later we are going to use the integral identity from Section 4.4 applying it to the formal neighborhood of the subspace consisting of the points $(0,\alpha,0,0)$. In order to do that we will relate the potential of the object $E_{\alpha}$ with a certain formal function on ${\cal M}_{E_1,E_2}$.

We may assume that the full subcategory $\CC(E_1,E_2)$ consisting of the pair of objects $E_1,E_2$ is minimal. As in the case of one object the potential of $\CC$ induces a formal power series $W_{E_1,E_2}=W(x,\alpha,\beta, y)$ on ${\cal M}_{E_1,E_2}$. It is defined as the abelianization of a series $\sum_{n\geqslant 3} W_n/n$ in cyclic paths in the quiver $Q_{E_1,E_2}$ with the vertices $E_1$ and $E_2$ and $(E_i,E_j)_1$ edges between vertices $E_i$ and $E_j$ for $i,j\in \{1,2\}$. Since any cyclic path has the same number of edges in the direction $E_1\to E_2$ as in the direction $E_2\to E_1$ we conclude that the potential $W_{E_1,E_2}$ is ${\bf G}_m$-invariants with respect to the ${\bf G}_m$-action on the graded vector space ${\cal M}_{E_1,E_2}$ with the weights $wt\, x=wt\, y=0$ and $wt\, \alpha=-wt\, \beta=1$. The potential $W_{E_1,E_2}$ is obtained from the potential $W_{E_1\oplus E_2}$ by a formal change of variables.

It follows from ${\bf G}_m$-invariance of $W_{E_1,E_2}$ that it belongs to $\kk[\alpha][[x,\beta,\gamma]]$. Therefore it defines a function on the formal neighborhood of the affine subspace $\{(0,\alpha,0,0)\}\subset {\cal M}_{E_1,E_2}$. In particular, for any $\alpha\in \op{Ext}^1(E_2,E_1)$ we obtain a formal power series $W_{E_1,E_2,\alpha}$ on ${\cal M}_{E_1,E_2}$ which is the Taylor expansion of $W_{E_1,E_2}$ at the point $(0,\alpha,0,0)$. Similarly to the Proposition 7 from Section 3.3 the series $W_{E_1,E_2,\alpha}$ becomes (after a formal change of coordinates) a direct sum $W_{E_{\alpha}}^{min}\oplus Q_{E_{\alpha}}\oplus N_{E_{\alpha}}$, where $Q_{E_{\alpha}}$ is a non-degenerate quadratic form, $N_{E_{\alpha}}$ is the zero function on a vector subspace, and $W_{E_{\alpha}}^{min}$ does not contain terms of degree less than $3$ in its Taylor expansion. By the motivic Thom-Sebastiani theorem we have $$(1-MF_0(W_{E_1,E_2,\alpha}))=(1-MF(E_{\alpha}))(1-MF_0(Q_{E_{\alpha}}))\,\,.$$ Let us consider the quadratic form $((W_{E_1,E_2})^{\prime\prime})_{|(0,\alpha,0,0)}$ on ${\cal M}_{E_1,E_2}$, where $(W_{E_1,E_2})^{{\prime\prime}}$ denotes the second derivative of the potential with respect to the affine coordinates. It follows from the above discussion that this quadratic form is equal to the direct sum of $Q_{E_{\alpha}}$ and the zero quadratic form.

It is easy to check that $\left(((W_{E_1,E_2})^{\prime\prime})_{|(0,\alpha,0,0)}\right)(v)$ is equal to $(d_{\alpha}^{(1)}v,v)$ for any $v\in {\cal M}_{E_1,E_2}$. Hence $Q_{E_{\alpha}}$ can be identified with the quadratic form on $\op{I
m}(d_{\alpha}^{(1)})$ given by $(u, (d_{\alpha}^{(1)})^{-1}u)$.

*Step 4.*

Recall (see Section 5.2) that for any exact triangle $E_1\to E_{\alpha}\to E_2$ we have a super line bundle $L$ with a canonically trivialized square:

$$L_{E_1\to E_{\alpha}\to E_2}=({\cal D}_{{\le 1},E_{\alpha}}\otimes {\cal D}_{{\le 1},E_1}^{-1}\otimes {\cal D}_{{\le 1},E_2}^{-1})\otimes (\op{sdet}(\op{Ext}^{\bullet}(E_1,E_2)))^{-1}.$$ For a split triangle $E_{\alpha}\simeq E_1\oplus E_2$ (i.e. $\alpha=0$) this line bundle is canonically trivialized since

-   by definition, for $E_{\alpha}\simeq E_1\oplus E_2$ we have $${\cal D}_{\le 1,E_{\alpha}}\simeq {\cal D}_{\le 1,E_{1}}\otimes {\cal D}_{\le 1,E_{2}}\otimes$$ $$\otimes\op{sdet}(\op{Ext}^{\le 1}(E_1,E_2))\otimes \op{sdet}(\op{Ext}^{\le 1}(E_2,E_1))\,\,,$$

-   by the Calabi-Yau property we have $$\op{sdet}(\op{Ext}^{\le 1}(E_2,E_1))\simeq \op{sdet}(\op{Ext}^{\geqslant 2}(E_1,E_2))\,\,.$$

Therefore, for any exact triangle $E_1\to E_{\alpha}\to E_2$ we have an isomorphism $$L_{E_1\to E_{\alpha}\to E_2}\simeq {\cal D}_{\le 1,E_{\alpha}}\otimes {\cal D}_{\le 1,E_{1}\oplus E_2}^{-1}\,\,.$$ On the other hand, considerations similar to those in Step 2 give rise to a canonical isomorphism $${\cal D}_{\le 1,E_{\alpha}}\otimes {\cal D}_{\le 1,E_{1}\oplus E_2}^{-1}\simeq \op{sdet}(\op{Im}(d_{\alpha}^{(1)}))\,\,.$$ One can see that the trivialization $(\op{sdet}(\op{Im}(d_{\alpha}^{(1)})))^{\otimes 2}\simeq {\bf 1}$ comes exactly from the non-degenerate quadratic form $Q_{E_{\alpha}}$. Therefore, for an arbitrary exact triangle $E_1\to E_{\alpha}\to E_2$ we have an isomorphism of super lines compatible with the trivializations of squares: $$L_{E_1\to E_{\alpha}\to E_2}\simeq \op{sdet}(\op{Im}(d_{\alpha}^{(1)}))\,\,.$$ This implies that $$\overline{I}(Q_{E_{\alpha}})=\overline{I}(l(E_1\to E_{\alpha}\to E_2))\,\,,$$ where $l\in J_2(Funct({\CC}_3, \CC))$ was defined in Section 5.2.

*Step 5.*

Let us apply the integral identity from Section 4.4 to the potential $W_{E_1,E_2}$. We put $$V_1:=\op{Ext}^1(E_2,E_1),\,V_2:=\op{Ext}^1(E_1,E_2),\,V_3:=\op{Ext}^1(E_1,E_1)\oplus\op{Ext}^1(E_2,E_2)\,.$$ We have: $$\int_{\alpha\in \op{Ext}^1(E_2,E_1)}(1-MF_{(0,\alpha,0,0)}(W_{E_1,E_2}))=$$ $$=
{\mathbb L}^{(E_2,E_1)_1}(1-MF_0((W_{E_1,E_2})_{|\op{Ext}^1(E_1,E_1)\oplus \op{Ext}^1(E_2,E_2)}))\,\,.$$

On the other hand the LHS of the integral identity is equal to $$\int_{\alpha\in \op{Ext}^1(E_2,E_1)}(1-MF_0(Q_{E_{\alpha}}))(1-MF(W^{min}_{E_{\alpha}})=$$ $$=\int_{\alpha\in \op{Ext}^1(E_2,E_1)}{\mathbb L}^{{1\over{2}}\op{rk}Q_{E_{\alpha}}}\overline{I}(Q_{E_{\alpha}})(1-MF(W^{min}_{E_{\alpha}}))\,\,.$$

Recall that $\op{rk} Q_{E_{\alpha}}=\op{rk}(d_{\alpha}^{(1)})=(E_{\alpha},E_{\alpha})_{\le 1}-(E_1\oplus E_2,E_1\oplus E_2)_{\le 1}$ by Steps 2 and 3. Then the integral identity becomes the following equality: $$\int_{\alpha\in \op{Ext}^1(E_2,E_1)}{\mathbb L}^{{1\over{2}}((E_{\alpha},E_{\alpha})_{\le 1}-(E_1\oplus E_2,E_1\oplus E_2)_{\le 1}) }\overline{I}(Q_{E_{\alpha}})(1-MF(W^{min}_{E_{\alpha}}))=$$ $$={\mathbb L}^{(E_2,E_1)_1}(1-MF_0(W^{min}_{E_1}\oplus W^{min}_{E_2}))\,\,.$$

Comparing this formula with the one we wanted to prove on Step 1 we see that they coincide if $$\overline{I}(Q_{E_{\alpha}})={{\overline{I}(h(E_{\alpha}))}\over{{\overline{I}(h(E_{1}))}{\overline{I}(h(E_{2}))}}}\,\,.$$ Now using Step 4 we observe that this cocycle condition is equivalent to the main property of the orientation data on exact triangles. This concludes the proof of the Theorem. $\blacksquare$

::: defn
Let $\CC$ be an ind-constructible $3$-dimensional Calabi-Yau category endowed with polarization, $\sigma\in Stab(\CC,\op{cl})$. We call the collection of elements $(A_V^{mot}\in {\cal R}_V)$ of the completed motivic quantum tori $({\cal R}_V)$ (for all strict sectors $V\subset \R^2$) the motivic Donaldson-Thomas invariant of $\CC$.
:::

Let us consider the following unital $\Q$-subalgebra of $\Q(q^{1/2})$: $$D_q:=\Z[q^{1/2},q^{-1/2},\left((q^n-1)^{-1}\right)_{n\geqslant 1}]\,.$$ There is a homomorphism of rings $\overline{D^{\mu}}\to D_q$ given by the twisted Serre polynomial. Namely, it maps ${\mathbb L}^{1/2}\mapsto q^{1/2}$, and on ${\cal M}^{\mu}$ it is the composition of the Serre polynomial with the involution $q^{1/2}\mapsto -q^{1/2}$. Therefore, we have a homomorphism of algebras ${\cal R}_{\Gamma}\to {\cal R}_{\Gamma,q}$, where ${\cal R}_{\Gamma,q}$ is a $D_q$-algebra generated by $\hat{e}_{\gamma}, \gamma\in \Gamma$, subject to the relations $$\hat{e}_{\gamma}\hat{e}_{\mu}=q^{{1\over{2}}{\langle\gamma,\mu\rangle}}\hat{e}_{\gamma+\mu}\,,\,\,\,\hat{e}_0=1\,.$$ Similarly to the motivic case, we have the algebra ${\cal R}_{V,q}$ associated with any strict sector $V$.

The motivic DT-invariants give rise to stability data on the graded Lie algebra associated with ${\cal R}_{\Gamma,q}$. We will denote by $A_{V,q}\in {\cal R}_{V,q}$ the element corresponding to $A_V^{mot}$.

[^1]: Recall that we pretend that such a map exists. In fact, it is defined only as a 1-morphism of stacks.
