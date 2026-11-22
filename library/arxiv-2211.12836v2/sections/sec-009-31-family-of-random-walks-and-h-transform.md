---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY"
section_id: sec-009-31-family-of-random-walks-and-h-transform
section_title: "Family of random walks and h-transform"
section_number: 3.1
pages: 15-17
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.902
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY — We study a class of commuting Markov kernels whose simplest element describes the movement of k particles on a discrete circle of size n"
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
