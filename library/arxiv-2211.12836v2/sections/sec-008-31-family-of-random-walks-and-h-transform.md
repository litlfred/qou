---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-008-31-family-of-random-walks-and-h-transform
section_title: "Family of random walks and h-transform"
section_number: 3.1
pages: 15-18
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.892
---
Given a PM-graph with distinguished vertex $v_0$, one can construct a family of commuting Markov kernels as follows. For sake of simplicity we assume here that $A$ is irreducible, although the same reasoning apply beyond irreducibility. Let $h^r$ (resp. $h^l$) be the right (resp. left) Perron-Frobenius vector of $A$, normalized so that $h^l(v_0)=1$ and $\langle h^l,h^r\rangle_{L^2(V)}=1$. By irreducibility of $A$, $h^l(v)>0$ and $h^r(v)>0$ for all $v\in V$. In the case where we are considering an adjacency matrix $M$ which is not necessarily irreducible, we say that $v$ is a positive eigenvector of $M$ if $v$ is an eigenvector of $M$ which has positive coefficients in its expansion in the canonical basis.

::: lemma
[]{#lem:Perron_sv label="lem:Perron_sv"} For all $v\in V$, $h^l$ and $h^r$ are respectively left and right eigenvectors of $s_v$ with eigenvalue $h^l(v)$.
:::

::: proof
*Proof.* The fact that $h^l$ and $h^r$ are eigenvectors of $s_v$ is deduced from the fact that both vectors are eigenvectors of $A$ and $s_v$ commutes with $A$. Hence, they are left and right positive eigenvectors of $s_v$, and thus correspond to the same eigenvalue we denote temporarily by $\lambda$. On the one hand, we have by definition of $s_v$ $$\langle h^l,s_v e_{v_0}\rangle=\langle h^l,e_v\rangle=h^l(v),$$ and on the other hand, $$\langle  h^l,s_v e_{v_0}\rangle=\langle s_v^*h^l,e_{v_0}\rangle=\lambda\langle h^l,e_{v_0}\rangle=\lambda.$$ We conclude that $$\lambda=h^l_v.$$ ◻
:::

It will be convenient to introduce the Hadamard product on vectors $x,y\in L^2(V)\mapsto x\cdot y\in L^2(V)$ defined by $$(x\cdot y)(v)=x(v)y(v).$$ If $x$ has nonzero entries, we write $\frac{1}{x}$ for the vector having entry $\frac{1}{x(v)}$ at $v$.

::: definition
[]{#def:h_transform label="def:h_transform"} The $h$-space $L^2_h(V)$ is the vector space $L^2(V)$ endowed with the Hilbert product $$\langle x,y\rangle_h=\langle h^l\cdot x,h^r\cdot y\rangle=\sum_{v\in V}\mu^h(v)\overline{x(v)}y(v),$$ with $\mu^h=h^l\cdot h^r$ called the invariant probability measure of $A$.

The $h$-transform of an operator $B\in End(L^2(V))$ is the operator $B^h$ given by $$B^h(x)=\frac{1}{h^r}\cdot B(h^r\cdot x).$$
:::

The space $L^2_h(V)$ can be also seen as the Hilbert space of $L^2$-functions on $V$ with respect to the probability measure $\mu^h$.

Since $h^r$ has positive entries, the map $B\mapsto B^h$ is well-defined. Its is actually an algebra isomorphism of $End(L^2(V))$ which amounts to a conjugation by a diagonal matrix; we denote by $\mathcal{A}^h$ the algebra $\{B^h, B\in \mathcal{A}\}$, which is isomorphic to $\mathcal{A}$. It is readily seen that $$(B^h)^*(x)=h^r\cdot B^*\left(\frac{1}{h^r}\cdot x\right),$$ while taking the adjoint $(\cdot)^{h,*}$ of $B$ with respect to $\langle \cdot,\cdot\rangle_h$ yields $$B^{h,*}(x)=\frac{1}{\mu^h}\cdot B^*\left(\mu^h\cdot x\right).$$ For $v\in V$, let us write $$P^v=\frac{s_v^h}{h^l(v)}\in \mathcal{A}^h.$$

::: proposition
The set $\left\{P^v, v\in V\right\}$ is a family of commuting Markov kernels on $L^2(V)$ with common invariant measure $\mu_h$.
:::

::: proof
*Proof.* Let $v\in V$ and denote by $\mathbf{1}\in V$ the vector with $\mathbf{1}(v)=1$ for all $v\in V$. Remark first that by Lemma [\[lem:Perron_sv\]](#lem:Perron_sv){reference-type="ref" reference="lem:Perron_sv"}, $$P^v(\mathbf{1}_V)=\frac{1}{h^l(v)}\frac{1}{h^r}\cdot s_v(h^r)=\frac{1}{h^r}\cdot h^r=\mathbf{1}.$$ Then, writing $s_{v}s_{v'}=\sum_{v''\in V}c_{vv'}^{v''}s_{v''}$ with $c_{vv'}^{v''}\geq 0$ for all $v,v',v''\in V$, we have $$P^v(e_{v'})=h^r(v')\frac{1}{h^r}\cdot s_v(s_{v'}e_{v_0})=\sum_{v''\in V}h^r(v')c_{vv'}^{v''}\left(\frac{1}{h^r}\cdot s_{v''}(e_{v_0})\right)=\sum_{v''\in V}\frac{h^r(v')}{h^r(v'')}c_{vv'}^{v''}e_{v''}.$$ Since $\frac{h^r_{v'}}{h^r_{v''}}c_{vv'}^{v''}\geq 0$ for all $v,v',v''\in V$, $P^v$ is an adjacency matrix and thus a Markov kernel on $L^2_h(V)$. Since by Lemma [\[lem:Perron_sv\]](#lem:Perron_sv){reference-type="ref" reference="lem:Perron_sv"} $$(s_v^h)^*[\mu^h]=h^r\cdot s_v^*\left(\frac{1}{h^r}\cdot \mu^h\right)=h^r\cdot s_v^*(h^l)=h^l(v)h^r\cdot h^l=h^l(v)\mu^h,$$ the vector $\mu_h$ is a positive eigenvector of $P^v$ with eigenvalue $1$. Hence, $\mu_h$ is an invariant measure of $P^v$. ◻
:::

Remark that we can similarly view the set $\left\{P^v, v\in V\right\}$ as a family of commuting Markov kernels on $L^2_h(V)$ with common invariant measure having density $\mathbf{1}$ with respect to $\mu^h$. We have indeed similarly $$(P^v)^{h,*}[\mathbf{1}]=\frac{1}{\mu^h}h^r\cdot \frac{s_v^*}{h^l(v)}\left(\frac{1}{h^r}\cdot \mu^h\cdot \mathbf{1}\right)=\frac{1}{h^l}\cdot \frac{s_v^*}{h^l(v)}(h^l)=\frac{1}{h^l}\cdot h^l=\mathbf{1}.$$

## Convolution product on $L^2_h(V)$

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
