---
doc_id: arxiv-hep-th-9211141v1
doc_title: "arXiv:hep-th/9211141v1 1 Dec 1992"
section_id: sec-007-22-hamiltonian-structure
section_title: "Hamiltonian Structure"
section_number: 2.2
pages: 14-16
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.686
latex_coverage_ratio: 0.948
doc_brief: "arXiv:hep-th/9211141v1 1 Dec 1992 — 17 sections: Front matter; INTRODUCTION AND SUMMARY OF RESULT; The System of Partial Differential"
---
[]{#subsec:hamiltonian label="subsec:hamiltonian"} The partial differential equations ([\[airy_1\]](#airy_1){reference-type="ref" reference="airy_1"})--([\[airy_6\]](#airy_6){reference-type="ref" reference="airy_6"}) can be rewritten in a compact form that reveals a symplectic structure with ([\[airy_7\]](#airy_7){reference-type="ref" reference="airy_7"}) defining a family of commuting Hamiltonians. To see this we first change the notation slightly $$\begin{aligned}
q_{2j}&=& -{i\over 2} x_{2j},\ \ \ \ p_{2j}=-i y_{2j}, \\
q_{2j-1}&=& {1\over 2} x_{2j-1},\ \ \ \ p_{2j-1}=y_{2j-1},
\end{aligned}$$ for $j=1,2,\ldots,m$, and $$v={1\over 2} x_0,  \ \ \ \ u=y_0,$$ and introduce the canonical symplectic structure $$\lbrace x_j,x_k\rbrace = \lbrace y_j,y_k\rbrace  = 0, \ \ \
\lbrace x_j,y_k\rbrace = \delta_{jk} ,$$ for $j,k=0,1,\ldots,m$. Then equations ([\[airy_1\]](#airy_1){reference-type="ref" reference="airy_1"})--([\[airy_6\]](#airy_6){reference-type="ref" reference="airy_6"}) become $$d_a x_j = \lbrace x_j,\omega(a)\rbrace \ \ \  {\rm and} \ \ \
d_a y_j=\lbrace y_j,\omega(a)\rbrace \ \ \ (j=0,1,\ldots,m)
\label{hamilton_eqn}$$ where $$\begin{aligned}
\omega(a) &=&  d_a \log {\rm det}\left(I-K\right) \nonumber \\
&=& \sum_{j=1}^{2m} G_j(x,y)\, da_j
\label{hamiltonian}
\end{aligned}$$ and $$G_j(x,y) = y_j^2 - {1\over 4} a_j x_j^2 - x_j y_j y_0 +{1\over 4} x_j^2 x_0
-{1\over 4}\sum_{k=1\atop k\neq j}^{2m}
{\left(x_j y_k - x_k y_j\right)^2\over a_j - a_k} \> .$$ Furthermore, the $G_j$'s are in involution $$\left\lbrace G_j,G_k \right\rbrace =0  \, .$$ This last result can be verified by a direct calculation, but as we discuss below, there is a better way to understand why such Hamiltonians are in involution. We can summarize the system of equations by saying, in words, that to find the $a_k$-flow of the coordinates $x_j$ and $y_j$, one flows according to Hamilton's equation with Hamiltonian $G_k$. The consistency of these equations (i.e. mixed partials are equal) follows immediately from this Hamiltonian formulation (see, e.g. [@tw1]).

When equations ([\[airy_1\]](#airy_1){reference-type="ref" reference="airy_1"})--([\[airy_6\]](#airy_6){reference-type="ref" reference="airy_6"}) are expressed in the Hamiltonian form ([\[hamilton_eqn\]](#hamilton_eqn){reference-type="ref" reference="hamilton_eqn"}), the equations are exactly analogous to the case of the sine kernel [@jmms] and in both cases the Hamiltonians are defined via ([\[hamiltonian\]](#hamiltonian){reference-type="ref" reference="hamiltonian"}). For the JMMS equations (see, e.g. [@tw1]) this Hamiltonian system is closely related to the Hamiltonian system studied by Moser [@moser]. In fact in both cases the systems of partial differential equations can be formulated in terms of the classical $R$-matrix approach to completely integrable systems. Such an approach identitfies the Lax operator and hence the commuting flow result above follows without any calculations. We refer the reader to [@htw] for a discussion of this classical $R$-matrix formulation of these systems of partial differential equations.

# THE ORDINARY DIFFERENTIAL EQUATIONS {#sec:ode}

In this section we specialize to the case $J=(s,\infty)$ and derive the differential equations ([\[p2\]](#p2){reference-type="ref" reference="p2"}), ([\[rDE\]](#rDE){reference-type="ref" reference="rDE"}) and ([\[Rq_relation\]](#Rq_relation){reference-type="ref" reference="Rq_relation"}). In the notation of the last section $m=1$, $a_1=s$, $a_2=\infty$. All terms in the formulas we derived which contain $a_2$ vanish because of the decay of the Airy kernel at $+\infty$. Recall that we now denote the quantity $q$ corresponding to the endpoint $a_1=s$ by $q(s)$, and write $R(s)$ for $R(s,s)$.

First, equation ([\[Rq_relation\]](#Rq_relation){reference-type="ref" reference="Rq_relation"}) is immediate from ([\[uv_5\]](#uv_5){reference-type="ref" reference="uv_5"}), which now says that $R=u$, and ([\[airy_5\]](#airy_5){reference-type="ref" reference="airy_5"}).

For ([\[rDE\]](#rDE){reference-type="ref" reference="rDE"}) we observe that ([\[airy_3\]](#airy_3){reference-type="ref" reference="airy_3"}) and ([\[airy_4\]](#airy_4){reference-type="ref" reference="airy_4"}) in the present case read $$\begin{aligned}
q^\prime &=& p-q u\, ,\label{q_prime}\\
p^\prime &=& s q +p u - 2 q v\, , \label{p_prime}
\end{aligned}$$ whereas ([\[airy_7\]](#airy_7){reference-type="ref" reference="airy_7"}) reads $$R=p q^\prime - q p^\prime \, .$$ Thus, by ([\[Rq_relation\]](#Rq_relation){reference-type="ref" reference="Rq_relation"}), $${R\over R^\prime} = \left({p\over q}\right)^\prime\, .
\label{Rprime}$$ Taking the logarithmic derivative of both sides of ([\[Rq_relation\]](#Rq_relation){reference-type="ref" reference="Rq_relation"}) gives $${1\over 2}{R^{\prime\prime}\over R^\prime} = {q^\prime\over q}$$ and by ([\[q_prime\]](#q_prime){reference-type="ref" reference="q_prime"}) this equals $${p\over q}-u={p\over q} - R \, .$$ Thus $${1\over 2} \left({R^{\prime\prime}\over R^\prime}\right)^\prime
= \left( p\over q \right)^\prime - R^\prime \, .$$ By ([\[Rprime\]](#Rprime){reference-type="ref" reference="Rprime"}) this is just ([\[rDE\]](#rDE){reference-type="ref" reference="rDE"}).

Finally, to obtain ([\[p2\]](#p2){reference-type="ref" reference="p2"}) we differentiate ([\[q_prime\]](#q_prime){reference-type="ref" reference="q_prime"}) and use ([\[q_prime\]](#q_prime){reference-type="ref" reference="q_prime"}), ([\[p_prime\]](#p_prime){reference-type="ref" reference="p_prime"}), ([\[airy_5\]](#airy_5){reference-type="ref" reference="airy_5"}) and ([\[airy_6\]](#airy_6){reference-type="ref" reference="airy_6"}). We find by an easy computation that $$q^{\prime\prime} = s q +q^3 +q(u^2-2v)\, .$$ Conveniently, we have ([\[uv_1\]](#uv_1){reference-type="ref" reference="uv_1"}), which says in this case that $u^2-2v=q^2$. Thus ([\[p2\]](#p2){reference-type="ref" reference="p2"}) is established.
