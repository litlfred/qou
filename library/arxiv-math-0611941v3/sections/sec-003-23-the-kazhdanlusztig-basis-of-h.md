---
doc_id: arxiv-math-0611941v3
doc_title: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR"
section_id: sec-003-23-the-kazhdanlusztig-basis-of-h
section_title: "The Kazhdan–Lusztig basis of H"
section_number: 2.3
pages: 4-4
source_pdf: 0611941v3.pdf
source_sha256: bf6f2d55c7adee51
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.985
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
