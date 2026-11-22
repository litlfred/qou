---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY"
section_id: sec-010-32-convolution-product-on-l2hv
section_title: "Convolution product on L2h(V)"
section_number: 3.2
pages: 17-18
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.939
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY — We study a class of commuting Markov kernels whose simplest element describes the movement of k particles on a discrete circle of size n"
---
Similarly to [\[eq:isomor_L2_CA\]](#eq:isomor_L2_CA){reference-type="eqref" reference="eq:isomor_L2_CA"} there is an isomorphism from $L^2_h(V)$ to $\mathcal{A}^h$ given by $$\label{eq:isomor_L2h_CA}
M^h:\left\lbrace \begin{aligned} L^2(V)&\rightarrow &\mathcal{A}^h\\ e_v&\mapsto &\mu^h(v)P^v\end{aligned}\right..$$ We can then transpose the multiplicative structure on $\mathcal{A}^h$ to a multiplication on $L^2_h(V)$. This motivates the following definition.

::: definition
[]{#def:convolution label="def:convolution"} The convolution of $x,y\in L^2_h(V)$ is the vector $x*y$ defined by $$x*y=\sum_{v\in V}\mu^h(v)x(v)P^v(y)=\sum_{v\in V}h^r(v)x(v)s_v^h(y).$$ A vector $u\in L^2_h(V)$ with nonnegative real entries is called a $h$-probability measure if $$\langle \mathbf{1},u\rangle_h=1.$$
:::

We denote by $\mathcal{M}_1(V)$ the set of $h$-probability measures. We have then the following results analogous to the usual convolution on classical groups.

::: proposition
[]{#prop:structure_conv label="prop:structure_conv"} The convolution product turns $L^2_h(V)$ into an algebra isomorphic to $\mathcal{A}$ through the map $M^h$. Moreover, the set $\mathcal{M}_1(V)$ is stable by convolution.
:::

::: proof
*Proof.* To prove the first statement, it is enough to prove that $M^h$ intertwines $*$ and the operator product on $\mathcal{A}^h$. By linearity, it is enough to prove it on $\frac{e_v}{h^r(v)},\frac{e_{v'}}{h^r(v')}$ for $v,v'\in V$. Let $v,v'\in V$. Then, using that $\mu^h=h^l\cdot h^r$ and $P^v=\frac{s^h_v}{h^l(v)}$, $$\begin{aligned}
\frac{e_v}{h^r(v)}*\frac{e_{v'}}{h^r(v')}=\sum_{v''\in V}\left(h^r\cdot \frac{e_v}{h^r(v)}\right)(v'')s_{v''}^h\left(\frac{e_{v'}}{h^r(v')}\right)=s_v^h\left(\frac{e_{v'}}{h^r(v')}\right)=&\frac{1}{h_r}\cdot s_v(e_{v'}).
\end{aligned}$$ Since $e_{v'}=s_{v'}e_{v_0}$, writing $s_{v}s_{v'}=\sum_{v''\in V}c_{vv'}^{v''}s_{v''}$ we get $$s_{v}(e_v)=\sum_{v''\in V}c_{vv'}^{v''}e_{v''}.$$ Hence, $$\frac{e_v}{h^r(v)}*\frac{e_{v'}}{h^r(v')}=\sum_{v''\in V}c_{vv'}^{v''}\frac{e_{v''}}{h^r(v'')}.$$ Since we have $M^h\left(\frac{e_v}{h^r(v)}\right)=s_v^h$, we deduce that $$M^h\left(\frac{e_v}{h^r(v)}*\frac{e_{v'}}{h^r(v')}\right)=M^h\left(\frac{e_v}{h^r(v)}\right)M^h\left(\frac{e_{v'}}{h^r(v')}\right).$$ Hence, $(L^2_h(V),+,*)$ is an algebra which is isomorphic to $\mathcal{A}^h$ (and thus to $\mathcal{A}$).

Suppose that $x,y\in \mathcal{M}_1(V)$. Then, $$\begin{aligned}
\langle \mathbf{1},x\ast y\rangle_h=&\sum_{v\in V}\mu^h(v)x(v)\langle \mathbf{1},P^v(y)\rangle_h\\
=&\sum_{v\in V}\mu^h(v)x(v)\left\langle h^l,h^r\cdot \frac{1}{h^r}\cdot \frac{s_v(h^r\cdot y)}{h^l(v)}\right\rangle=\sum_{v\in V}h^r(v)x(v)\left\langle h^l,s_v(h^r\cdot y)\right\rangle.
\end{aligned}$$ By Lemma [\[lem:Perron_sv\]](#lem:Perron_sv){reference-type="ref" reference="lem:Perron_sv"}, $h^l$ is an eigenvector of $s_v^*$ with eigenvalue $h^l(v)$ for all $v\in V$, thus, using the fact that $x,y\in\mathcal{M}_{1}(V)$, $$\begin{aligned}
\langle \mathbf{1},x\ast y\rangle_h=&\sum_{v\in V}h^r(v)x(v)\left\langle s_v^*h^l,h^r\cdot y\right\rangle\\
=&\sum_{v\in V}\mu^h(v)x(v)\left\langle h^l,h^r\cdot y\right\rangle=\sum_{v\in V}\mu^h(v)x(v)\left\langle \mathbf{1},y\right\rangle_{h}=\langle \mathbf{1},x\rangle_{h}=1.
\end{aligned}$$ ◻
:::
