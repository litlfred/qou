---
doc_id: arxiv-hep-th-0001202v2
doc_title: "Towards cohomology of renormalization: bigrading the combinatorial Hopf algebra of rooted trees"
section_id: sec-005-51-general-inequalities
section_title: "General inequalities"
section_number: 5.1
pages: 8-9
source_pdf: 0001202v2.pdf
source_sha256: b2e3e22ea3d51c0b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.959
doc_brief: "Towards cohomology of renormalization: bigrading the combinatorial Hopf algebra of rooted trees — The renormalization of quantum ﬁeld theory twists the antipode of a non- cocommutative Hopf algebra"
---
Let ${\cal H}$ be a commutative graded Hopf algebra with unit $e$. Let ${\rm deg}$ be the grading, with ${\rm deg}(X)\in {\Nb}$ for all $X\in{\cal H}$ and ${\rm deg}(e)=0$. We assume that ${\cal H}$ is reduced to scalars by the counit $\bar{e}$.

Let ${\cal H}_k$ be the set of elements in the kernel of $U_k$ which are in the range of $U_{k-1}$, so that $U_k(X)=0$ and $U_{k-1}(X)\not=0$, for $X\in{\cal H}_k$. Then we call $k$ the degree of primitivity of $X$, writing ${\rm deg}_p(X)=k$. We let ${\cal H}_0$ be the set of elements in the kernel of $P=U_0$, i.e. the scalars. The augmentation ideal fulfills ${\cal H}_c={\cal H}/{\cal H}_0=
\sum_{k=1}^\infty {\cal H}_k$.

To show that ${\rm \deg}_p(X)\le{\rm deg}(X)$, suppose that $$\Delta^{{\rm deg}(X)-1}(X)
=\sum_i X^{(1)}_i\otimes\ldots\otimes X_i^{({\rm deg(X)})}
\label{major}$$ has nonscalar entries in ${\cal H}_c^{\otimes {\rm deg}(X)}$. Then they are all formed from 1-primitives, in ${\cal H}_1$, since the coproduct is homogenous in ${\rm deg}$ and any element $X$ with ${\rm deg}(X)=1$ also has ${\rm deg}_p(X)=1$. Hence ${\rm deg}_p$ is majorized by ${\rm deg}$ and is thus finite for each $X\in {\cal H}$.

We denote by $H_{n,k}$ the number of linearly inequivalent terms $X$ with weight ${\rm deg}(X)=n$ and primitivity ${\rm deg}_p(X)=k$. Then the generators $H_k(x):=\sum_{n\ge k}H_{n,k}x^n$ satisfy $$H_{j+k}(x)\le H_j(x)H_k(x),\quad j,k>0\,.
\label{leq}$$

**Proof**: It is sufficient to show that an element $X\in{\cal H}_{j+k}$ may be labelled by those terms in $\Delta(X)$ that are in ${\cal H}_j\otimes{\cal H}_k$. To prove this, suppose that $X_1$ and $X_2$ give the same terms in ${\cal H}_j\otimes{\cal H}_k$. Now observe that $U_{j,k}:=
U_{j-1}\otimes U_{k-1}$ projects onto ${\cal H}_j\otimes{\cal H}_k$, giving $U_{j,k}\circ\Delta(X_1-X_2)=0$. Finally, observe that coassociativity gives $$0=U_{j,k}\Delta(X_1-X_2)=P^{\otimes(j+k)}\circ\Delta^{j+k-1}(X_1-X_2)
:=U_{k+j-1}(X_1-X_2)
\label{done}$$ which shows that $X_1-X_2$ is $(j+k-1)$-primitive and hence that $X_1$ and $X_2$ are equivalent elements of ${\cal H}_{j+k}$. $\Box$

In consequence of ([\[leq\]](#leq){reference-type="ref" reference="leq"}) we obtain $$H_k(x)\le [H_1(x)]^k\,.
\label{weak}$$ This reflects the fact that the terms in $\Delta^{k-1}(X)$ which belong to ${\cal H}_1^{\otimes k}$ are sufficient to label elements $X\in{\cal H}_k$. The remarkable feature of the Hopf algebra of rooted trees, to be proved below, is that all the elements of ${\cal H}_1^{\otimes k}$ are necessary to label elements of ${\cal H}_k$.

As a further comment, we note that ([\[weak\]](#weak){reference-type="ref" reference="weak"}) may be strengthened if the Hopf algebra is cocommutative, since then the order of labels is immaterial. In the case of ${\cal H}_{\rm ladder}$, with $\overline{H}_1(x)=x/(1-x)$, one thus obtains $$\overline{H}_k(x)\le\prod_{j\le k}{x\over1-x^j}
\label{ladsat}$$ which is in fact saturated by Table 1.
