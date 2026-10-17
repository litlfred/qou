---
doc_id: arxiv-math-0611941v3
doc_title: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR"
section_id: sec-001-2-kazhdanlusztig-theory-and-the-asymptotic-ring
section_title: "Kazhdan–Lusztig theory and the asymptotic ring"
section_number: 2
pages: 2-2
source_pdf: 0611941v3.pdf
source_sha256: bf6f2d55c7adee51
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.976
doc_brief: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR — Let H be the one-parameter Hecke algebra associated to a ﬁnite Weyl group W, deﬁned over a ground ring in which “bad” primes for W are invertible."
---
[]{#sec2 label="sec2"} References for this section are the books [@GePf] and [@Lusztig03]. Let $W$ be a finite Weyl group, with generating set $S$. Let $L \colon 
W \rightarrow {\mathbb{Z}}$ be a weight function. Thus, we have $L(ww')=L(w)+L(w')$ whenever $l(ww')=l(w)+l(w')$ for $w,w'\in W$; here $l(w)$ denotes the length of $w \in W$. Note that $L(s)=L(t)$ whenever $s,t \in S$ are conjugate in $W$.

We will assume throughout that $L(s)\geqslant 0$ for all $s \in S$.

Let $R \subseteq {\mathbb{C}}$ be a subring and $A=R[v,v^{-1}]$ be the ring of Laurent polynomials in an indeterminate $v$. Let ${\mathcal{H}}={\mathcal{H}}_A(W,L)$ be the corresponding generic *Iwahori--Hecke algebra*. This is an associative algebra, free over $A$ with a basis $\{T_w \mid w \in W\}$ and multiplication given as follows. $$T_sT_w=\left\{\begin{array}{cl} T_{sw} & \quad \mbox{if $l(sw)>l(w)$},\\
T_{sw}+(v^{L(s)}-v^{-L(s)})T_w & \quad \mbox{if $l(sw)<l(w)$},\end{array}
\right.$$ where $s\in S$ and $w\in W$.
