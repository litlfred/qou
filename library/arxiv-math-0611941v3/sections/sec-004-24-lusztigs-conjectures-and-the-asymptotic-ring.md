---
doc_id: arxiv-math-0611941v3
doc_title: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR"
section_id: sec-004-24-lusztigs-conjectures-and-the-asymptotic-ring
section_title: "Lusztig's conjectures and the asymptotic ring J"
section_number: 2.4
pages: 4-5
source_pdf: 0611941v3.pdf
source_sha256: bf6f2d55c7adee51
toc_source: outline
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.935
doc_brief: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR — Let H be the one-parameter Hecke algebra associated to a ﬁnite Weyl group W, deﬁned over a ground ring in which “bad” primes for W are invertible."
---
[]{#sub24 label="sub24"}

In the sequel, we assume that the following hypotheses are satisfied.

::: center
:::

(Actually, for our purposes, instead of **(P15)** it is enough to require the somewhat weaker statement [@Lusztig03 18.9(b)], which we called **(P15')** in [@mylaus §5].) By [@Lusztig03 Chap. 15], these conjectures are known to hold when $L$ is a positive multiple of the length function ("equal parameter case"), thanks to a deep geometric interpretation of the basis $\{c_w\}$. They are also known for a certain class of non-trivial weight functions in type $B_n$; see [@GeIa06], [@myert06].

Assuming the above hypotheses, we can perform the following constructions. Following Lusztig [@Lusztig03 Chap. 18], let $J$ be a free ${{\mathbb{Z}}}$-module with basis $\{t_w\mid w\in W\}$. We define a multiplication on $J$ by $$t_xt_y=\sum_{z\in W} \gamma_{x,y,z^{-1}}\, t_z,$$ where $\gamma_{x,y,z^{-1}} \in {\mathbb{Z}}$ is the constant term of $v^{{\mathbf{a}}(z)}
h_{x,y,z} \in {{\mathbb{Z}}}[v]$. Then it turns out that this multiplication is associative and we have an identity element given by $1_J=\sum_{d\in {\mathcal{D}}} 
n_dt_d$. Furthermore, we have a homomorphism of $A$-algebras $\phi \colon 
{\mathcal{H}}\rightarrow J_A=A \otimes_{{\mathbb{Z}}} J$ such that $$\phi(c_w^\dagger)=\sum_{\genfrac{}{}{0pt}{}{z\in W,d\in {\mathcal{D}}}{{\mathbf{a}}(z)={\mathbf{a}}(d)}}
h_{w,d,z} \hat{n}_z\, t_z \qquad (w\in W),$$ where $\hat{n}_z$ is defined as follows. Given $z\in W$, let $d$ be the unique element of ${\mathcal{D}}$ such that $d\sim_{{\mathcal{L}}} z^{-1}$; then $\hat{n}_z=n_d=\pm 1$. (See properties **(P5)**, **(P13)** in Lusztig's conjectures [@Lusztig03 14.2].) Note that the function $z \mapsto \hat{n}_z$ is constant on the right cells of $W$.
