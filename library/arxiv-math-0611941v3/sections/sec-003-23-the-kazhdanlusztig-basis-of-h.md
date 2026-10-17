---
doc_id: arxiv-math-0611941v3
doc_title: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR"
section_id: sec-003-23-the-kazhdanlusztig-basis-of-h
section_title: "The Kazhdan–Lusztig basis of H"
section_number: 2.3
pages: 4-5
source_pdf: 0611941v3.pdf
source_sha256: bf6f2d55c7adee51
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.952
doc_brief: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR — Let H be the one-parameter Hecke algebra associated to a ﬁnite Weyl group W, deﬁned over a ground ring in which “bad” primes for W are invertible."
---
[]{#sub23 label="sub23"}

Let $\{c_w\mid w\in W\}$ be the "new" basis of ${\mathcal{H}}$ defined in [@Lusztig03 Theorem 5.2]. We have $c_w=T_w+ \sum_{y} p_{y,w}\, T_y$ where $p_{y,w} \in v^{-1}{{\mathbb{Z}}}[v^{-1}]$ and $p_{y,w}=0$ unless $y<w$ in the Bruhat--Chevalley order. Given $x,y\in W$, we write $$c_xc_y=\sum_{z\in W} h_{x,y,z}c_z\qquad\mbox{where $h_{x,y,z}\in A$}.$$ As in [@Lusztig03], we usually work with the elements $c_w^\dagger$ obtained by applying the unique $A$-algebra involution $H \rightarrow H$, $h \mapsto h^\dagger$ such that $T_s^\dagger=-T_s^{-1}$ for any $s\in S$; see [@Lusztig03 3.5]. We refer to [@Lusztig03 Chap. 8] for the definition of the preorders $\leqslant_{{\mathcal{L}}}$, $\leqslant_{{\mathcal{R}}}$, $\leqslant_{{\mathcal{L}}{\mathcal{R}}}$ and the corresponding equivalence relations $\sim_{{\mathcal{L}}}$, $\sim_{{\mathcal{R}}}$, $\sim_{{\mathcal{L}}{\mathcal{R}}}$ on $W$, induced by $L$. The equivalence classes with respect to these relations are called *left*, *right* and *two-sided cells* of $W$, respectively. If $L(s)=1$ for all $s \in S$, then $C_w=(-1)^{l(w)}c_w^\dagger$ where $\{C_w\}$ is the basis originally constructed in [@KaLu].

Let $z \in W$. Following Lusztig [@Lusztig03 13.6], we define ${\mathbf{a}}(z)\in {{\mathbb{Z}}}_{\geqslant 0}$ by the condition that $$\begin{aligned}
{2}
v^{{\mathbf{a}}(z)}h_{x,y,z} &\in {{\mathbb{Z}}}[v] &&\qquad \mbox{for all $x,y\in W$},\\
v^{{\mathbf{a}}(z)-1}h_{x,y,z} &\not\in {{\mathbb{Z}}}[v] &&\qquad \mbox{for some 
$x,y\in W$}.
\end{aligned}$$ Furthermore, if $p_{1,z}\neq 0$, we define $\Delta(z)\in {\mathbb{Z}}_{\geqslant 0}$ and $0\neq n_z\in {\mathbb{Z}}$ by the condition that $$p_{1,z}=n_zv^{-\Delta(z)}+\mbox{strictly smaller  powers of $v$};
\quad \mbox{see \cite[14.1]{Lusztig03}}.$$ Otherwise, we set $\Delta(z)=\infty$ and leave $n_z$ undefined. (This case can only occur when $L(s)=0$ for some $s \in S$.) We set $${\mathcal{D}}=\{z \in W \mid {\mathbf{a}}(z)=\Delta(z)\}.$$ (In what follows, the coefficients $n_z$ will only play a role when $z\in {\mathcal{D}}$.)

## Lusztig's conjectures and the asymptotic ring $J$ {#sub24}

In the sequel, we assume that the following hypotheses are satisfied.

::: center
:::

(Actually, for our purposes, instead of **(P15)** it is enough to require the somewhat weaker statement [@Lusztig03 18.9(b)], which we called **(P15')** in [@mylaus §5].) By [@Lusztig03 Chap. 15], these conjectures are known to hold when $L$ is a positive multiple of the length function ("equal parameter case"), thanks to a deep geometric interpretation of the basis $\{c_w\}$. They are also known for a certain class of non-trivial weight functions in type $B_n$; see [@GeIa06], [@myert06].

Assuming the above hypotheses, we can perform the following constructions. Following Lusztig [@Lusztig03 Chap. 18], let $J$ be a free ${{\mathbb{Z}}}$-module with basis $\{t_w\mid w\in W\}$. We define a multiplication on $J$ by $$t_xt_y=\sum_{z\in W} \gamma_{x,y,z^{-1}}\, t_z,$$ where $\gamma_{x,y,z^{-1}} \in {\mathbb{Z}}$ is the constant term of $v^{{\mathbf{a}}(z)}
h_{x,y,z} \in {{\mathbb{Z}}}[v]$. Then it turns out that this multiplication is associative and we have an identity element given by $1_J=\sum_{d\in {\mathcal{D}}} 
n_dt_d$. Furthermore, we have a homomorphism of $A$-algebras $\phi \colon 
{\mathcal{H}}\rightarrow J_A=A \otimes_{{\mathbb{Z}}} J$ such that $$\phi(c_w^\dagger)=\sum_{\genfrac{}{}{0pt}{}{z\in W,d\in {\mathcal{D}}}{{\mathbf{a}}(z)={\mathbf{a}}(d)}}
h_{w,d,z} \hat{n}_z\, t_z \qquad (w\in W),$$ where $\hat{n}_z$ is defined as follows. Given $z\in W$, let $d$ be the unique element of ${\mathcal{D}}$ such that $d\sim_{{\mathcal{L}}} z^{-1}$; then $\hat{n}_z=n_d=\pm 1$. (See properties **(P5)**, **(P13)** in Lusztig's conjectures [@Lusztig03 14.2].) Note that the function $z \mapsto \hat{n}_z$ is constant on the right cells of $W$.
