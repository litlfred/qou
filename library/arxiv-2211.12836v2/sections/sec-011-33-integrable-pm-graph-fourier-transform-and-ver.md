---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY"
section_id: sec-011-33-integrable-pm-graph-fourier-transform-and-ver
section_title: "Integrable PM-graph, Fourier transform and Verlinde formula"
section_number: 3.3
pages: 18-21
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.921
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY — We study a class of commuting Markov kernels whose simplest element describes the movement of k particles on a discrete circle of size n"
---
[]{#sec:integrable_graph label="sec:integrable_graph"} In this section, we assume that $A$ is diagonalizable over $\mathbb{C}$. As a direct consequence of commutativity, all $s_v, \, v\in V$ are diagonalizable. We denote by $\{u^{(i)},i=0,\ldots,|V|-1\}$ a basis of right eigenvectors and $\{w^{(i)},i=0,\ldots,|V|-1\}$ the dual basis of left eigenvectors normalized so that $w^{(i)}(v_0)=1$ (as we will see in the next lemma, any eigenvector has a nonzero coordinate along $e_{v_0}$). We suppose that $u^{(0)}=h^r$ (and thus $w^{(0)}=h^l$). Finally, we denote by $\theta_v(i)$ the eigenvalue of $s_v$ on $u^{(i)}$, so that $\overline{\theta_v(i)}$ is the eigenvalue of $s_v$ on $w^{(i)}$). As in Lemma [\[lem:Perron_sv\]](#lem:Perron_sv){reference-type="ref" reference="lem:Perron_sv"}, the coordinates of $w^{(i)}$ along $\mathcal{B}_0$ are actually given by the eigenvalues of the family $s_v$.

::: lemma
[]{#lem:eigenvalue_eigenvector_relation label="lem:eigenvalue_eigenvector_relation"} For all $i\in \{0,\ldots,|V|-1\}$, $$w^{(i)}(v)=\overline{\theta_v(i)}.$$
:::

::: proof
*Proof.* Let $y$ be a left eigenvector with eigenvalue $\theta_v(i)$. Then, since $s_v(e_{v_0})=e_v$, $$\langle y,e_v\rangle=\langle s_v^*y,e_{v_0}\rangle=\theta_v(i)\langle y,e_{v_0}\rangle.$$ In particular, $\langle y,e_{v_0}\rangle\not=0$ for otherwise we would have $y=0$. Specifying to $y=w^{(i)}$ yields then $$w^{(i)}(v)=\overline{\theta_v(i)}.$$ ◻
:::

Remark that $s_{v}^h$ is also diagonalizable on $L^2_h(V)$ with same eigenvalues $\theta_v(i),\overline{\theta_v(i)}$ and left and right eigenvectors $$\tilde{u}^{(i)}=\frac{1}{h^r}\cdot u^{(i)},\, \tilde{w}^{(i)}=\frac{1}{h^l}\cdot w^{(i)}.$$ (beware that left eigenvectors are taken with respect to the adjoint $(\cdot)^{h,*})$).

::: definition
[]{#def:Fourier_transform label="def:Fourier_transform"} The Fourier transform $\Phi_V$ on $L^2_h(V)$ is the morphism from $L^2_h(V)$ to $\mathbb{C}^{|V|}$ defined by $$\Phi_V[x](i)=\left\langle \tilde{w}^{(i)},x\right\rangle_h.$$
:::

. With this definition, a vector $u\in L^2_h(V)$ is a $h$-probability measure if and only if $\Phi_V[u](0)=1$.

::: proposition
[]{#prop:diagonalization_Fourier label="prop:diagonalization_Fourier"} For any $x,y\in L^2_h(V)$, $$\Phi_V[x\ast y](i)=\Phi_V[x](i)\Phi_V[y](i).$$ Moreover, $\Phi_V$ is an isomorphism with inverse $$\Phi_V^{-1}(e_{i})=\tilde{u}^{(i)},$$ where $\{e_i\}_{1\leq i\leq \vert V\vert}$ is the canonical basis of $\mathbb{C}^{\vert V\vert}$.
:::

::: proof
*Proof.* Let $x,y\in L^2_h(V)$ and $0\leq i\leq \vert V\vert-1$. Then, using the definition of the convolution product and the fact that $\tilde{w}^{(i)}$ is an eigenvector of $(s_v^h)^{h,*}$ with eigenvalue $\overline{\theta_v^i}$, $$\begin{aligned}
\Phi_V[x\ast y](i)=&\langle \tilde{w}^{(i)},x\ast y\rangle_h\\
=&\sum_{v\in V}(h^r\cdot x)(v)\left\langle \tilde{w}^{(i)},s_v^h(y)\right\rangle_h\\
=&\sum_{v\in V}(h^r\cdot x)(v)\left\langle (s_v^h)^{h,*}(\tilde{w}^{(i)}),y\right\rangle_h\\
=&\sum_{v\in V}(h^r\cdot x)(v)\theta_v(i)\Phi_V[y](i).
\end{aligned}$$ Then, by Lemma [\[lem:eigenvalue_eigenvector_relation\]](#lem:eigenvalue_eigenvector_relation){reference-type="ref" reference="lem:eigenvalue_eigenvector_relation"}, $$\begin{aligned}
\Phi_V[x\ast y](i)=\Phi_V[y](i)\sum_{v\in V}(h^r\cdot x)(v)\overline{w^{(i)}(v)}=&\Phi_V[y](i)\sum_{v\in V}(h^r\cdot x)(v) \overline{(h^l\cdot \tilde{w}^{(i)})(v)}\\
=&\Phi_V[y](i)\left\langle \tilde{w}^{(i)},x\right\rangle_h=\Phi_V[y](i)\Phi_V[x](i),
\end{aligned}$$ which proves the first assertion. Then, for $0\leq i,j\leq \vert V\vert-1$, $$\Phi_V\left[\tilde{u}^{(i)}\right](j)=\left\langle \tilde{w}^{(j)},\tilde{u}^{(i)}\right\rangle_h=\delta_{ij},$$ so $\Phi_V$ is an isomorphism with inverse $$\Phi_V^{-1}(e_i)=\tilde{u}^{(i)}.$$ ◻
:::

The latter proposition amounts to say that $\Phi_V$ diagonalizes the convolution product on $L^2_h(V)$. We can deduce from the above construction a general formula to compute arbitrary convolutions in $L^2_h(V)$.

::: proposition
[]{#prop:Verlinde_formula_general label="prop:Verlinde_formula_general"} Let $n\geq 2$. Then, for $v\in V$ and $x_1,\ldots,x_n\in L^2_h(V)$ $$\left[x_1*\dots *x_n\right](v)=\sum_{i=0}^{|V|-1}\prod_{j=1}^n\Phi_V[x_j](i)\tilde{u}^i(v),$$ and for $v_1,\ldots,v_n\in V$, $$s_{v_1}\dots s_{v_n}=\sum_{v\in V}c_{v_1,\ldots,v_n}^vs_v$$ with $$\label{eq:Verlinde_formula_general}
c_{v_1,\ldots,v_n}^v=\sum_{i=0}^{|V|-1}\prod_{j=1}^n\theta_{v_j}(i)u^{(i)}(v).$$
:::

::: proof
*Proof.* Since $(\tilde{w}^{(i)})_{0\leq i\leq |V|-1}$ is the dual basis of $(\tilde{u}^{(i)})_{0\leq i\leq |V|-1}$ with respect to $\langle \cdot,\cdot\rangle_h$, we have $$x_1*\dots *x_n=\sum_{i=1}^{|V|-1}\langle \tilde{w}^{(i)},x_1*\dots *x_n\rangle_h \tilde{u}^{(i)}=\sum_{i=1^{|V|-1}}\Phi_V[x_1*\dots *x_n](i) \tilde{u}^{(i)}.$$ By Proposition [\[prop:diagonalization_Fourier\]](#prop:diagonalization_Fourier){reference-type="ref" reference="prop:diagonalization_Fourier"}, we then have $$x_1*\dots *x_n=\sum_{i=1}^{|V|-1}\prod_{j=1}^n\Phi_V[x_j](i)\tilde{u}^{(i)},$$ and the first statement is deduced. For the second statement, remark that we also have $$s_{v_1}^h\dots s_{v_n}^h=\sum_{v\in V}c_{v_1,\ldots,v_n}^vs_v^h$$ with the same coefficients (see Definition [\[def:h_transform\]](#def:h_transform){reference-type="ref" reference="def:h_transform"} and the remark afterwards). By Proposition [\[prop:structure_conv\]](#prop:structure_conv){reference-type="ref" reference="prop:structure_conv"} and the first statement, $$\begin{aligned}
s_{v_1}^h\dots s_{v_n}^h=&M^h\left(\frac{1}{h^r(v_1)}e_{v_1}*\dots *\frac{1}{h^r(v_n)}e_{v_n}\right)\\
=&\frac{1}{\prod_{j=1}^nh^r(v_j)}\sum_{i=1}^{|V|-1}\prod_{j=1}^n\Phi_V[e_{v_j}](i)M^h(\tilde{u}^i).
\end{aligned}$$ On the one hand, for $1\leq j\leq n$, we have $$\Phi_V[e_{v_j}](i)=\langle \tilde{w}^{(i)},e_{v_j}\rangle_h=\mu^h(v_j)\overline{\tilde{w}^{(i)}(v_j)}=h^r(v_j)\overline{w^{(i)}(v_j)}=h^r(v_j)\theta_{v_j}(i)$$ by Lemma [\[lem:eigenvalue_eigenvector_relation\]](#lem:eigenvalue_eigenvector_relation){reference-type="ref" reference="lem:eigenvalue_eigenvector_relation"}. On the other hand, $$M^h(\tilde{u}^{(i)})=\sum_{v\in V}h^r(v)\tilde{u}^{(i)}(v)s^h_{v}=\sum_{v\in V}u^{(i)}(v)s^h_{v}.$$ Hence, $$s_{v_1}^h\dots s_{v_n}^h=\sum_{v\in V}\left(\sum_{i=1}^{|V|-1}\prod_{j=1}^n\theta_{v_j}(i)u^{(i)}(v)\right) s_{v}^h,$$ and we thus get $$c_{v_1,\ldots,v_n}^v=\sum_{i=0}^{|V|-1}\left(\prod_{j=1}^n\theta_{v_j}(i)\right)u^{(i)}(v).$$ ◻
:::

::: remark
The formula [\[eq:Verlinde_formula_general\]](#eq:Verlinde_formula_general){reference-type="eqref" reference="eq:Verlinde_formula_general"} is called the Verlinde formula, since it is exactly the same formula that appears in the special case where the graph comes from the fusion ring in conformal field theory, see [@Beauv]. Let $\{v_j\}_{0\leq j\leq |V|-1}$ be an enumeration of the vertices of $V$, with $v_0$ the root of the PM graph as before, and write $S=\left(\theta_{v_i}(j)\right)_{0\leq i,j\leq |V|-1}$. Then, by Lemma [\[lem:eigenvalue_eigenvector_relation\]](#lem:eigenvalue_eigenvector_relation){reference-type="ref" reference="lem:eigenvalue_eigenvector_relation"} and the definition of the dual basis $u^{(i)}$ $$\left(S^{-1}\right)_{ij}=u^{(i)}(v_j).$$ Hence, [\[eq:Verlinde_formula_general\]](#eq:Verlinde_formula_general){reference-type="eqref" reference="eq:Verlinde_formula_general"} specializes in the more common formula $s_{v_i}s_{v_j}=\sum_{k=0}^{|V|-1}N_{ij}^ks_{v_k}$ with $$N_{ij}^k=\sum_{l=0}^{|V|-1}S_{il}S_{jl}\left(S^{-1}\right)_{lk}.$$ Note that a term $\frac{1}{S_{0l}}$ often appearing in the literature disappears in our case due to our normalization of the vectors $w^{(i)}$, $0\leq i\leq |V|-1$. In the special case of the quantum cohomology of the Grassmannian which is the subject of the present paper, this formula is known as Vafa and Intriligator's formula, see [@B].
:::

When $A$ is normal with respect to $\langle \cdot,\cdot\rangle$, then $A$ is diagonalizable in an orthogonal basis and, with our convention, we can choose $$\label{eq:normal_adjacency}
u^{(i)}=\frac{1}{\Vert w^{(i)}\Vert^2}w^{(i)}$$ for $0\leq i\leq |V|-1$. In particular, $h^r=\frac{1}{\Vert h^l\Vert^2}h^l$ and thus $$\mu^h=\frac{1}{\Vert h^l\Vert^2}h^l\cdot h^l.$$ In this case, $\lbrace \tilde{u}_i, 1\leq i\leq \vert V\vert\rbrace$ is an orthogonal basis of $L^2_h(V)$ with $\Vert \tilde{u}_i\Vert_{h}^2=\frac{\Vert h^l\Vert^2}{\Vert w^{(i)}\Vert^2}$ and then $\Phi_V$ is an isometry from $L^2_h(V)$ to $\mathbb{C}^{\vert V\vert}$ endowed with the Hilbert space structure $\langle e_i,e_j\rangle=\delta_{ij}\frac{\Vert h^l\Vert^2}{\Vert w^{(i)}\Vert^2}$.
