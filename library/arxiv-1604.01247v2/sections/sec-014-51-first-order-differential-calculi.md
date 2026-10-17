---
doc_id: arxiv-1604.01247v2
doc_title: "EXCEPTIONAL QUANTUM GEOMETRY"
section_id: sec-014-51-first-order-differential-calculi
section_title: "First order differential calculi"
section_number: 5.1
pages: 24-26
source_pdf: 1604.01247v2.pdf
source_sha256: 5a402405aadf5d54
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "EXCEPTIONAL QUANTUM GEOMETRY — Based on an interpretation of the quark-lepton symmetry in terms of the unimodularity of the color group SU(3) and on the existence of 3 generations, we develop an"
---
Given a category $\mathbf C$ of algebras over some field $\mathbb K$ and an algebra ${\cal A}$ in $\mathbf C$, a pair $(\Omega^1,d)$ of an ${\cal A}$-bimodule $\Omega^1$ for $\mathbf C$ [@mdv:2001] and a derivation $d$ of ${\cal A}$ into $\Omega^1$, that is a $\mathbb K$-linear mapping satisfying (the Leibniz rule) $$d(xy)=d(x)y+xd(y)$$ for any $x,y\in {\cal A}$, will be refered to as a *first order differential calculus over ${\cal A}$* for $\mathbf C$ or simply a first order calculus over ${\cal A}$ when no confusion arises. There is an obvious notion of homomorphism of first order differential calculi over ${\cal A}$. This terminology as well as the one for higher order differential calculi was introduced in [@wor:1989] for the case of the category of associative algebras on a field $\mathbb K$.

In the following we shall be concerned with the category of real unital Jordan algebras so, if $J$ is such a unital Jordan algebra, a $J$-bimodule is a unital $J$-module which will be simply refered to as a $J$-module when no confusion arises.\
Let $J$ be a unital Jordan algebra and let us define *its center* $Z(J)$ by $$Z(J)=\{z\in J \vert [x,y,z]=[x,z,y]=0, \forall x,y\in J\}
  \label{center}$$ where $[x,y,z]=(xy)z-x(yz)$ denotes the associator of $x,y,z\in J$. The center $Z(J)$ is a unital associative subalgebra of $J$. The Lie algebra ${\mbox{Der}}(J)$ of all derivations of $J$ into itself is also a $Z(J)$-module and we denote by $\Omega^1_{{\mbox{\tiny Der}}}(J)$ the $J$-module of all the $Z(J)$-homomorphisms of ${\mbox{Der}}(J)$ into $J$. One defines a derivation $$d_{{\mbox{\tiny Der}}}:J\rightarrow \Omega^1_{{\mbox{\tiny Der}}}(J)$$ by setting $$d_{{\mbox{\tiny Der}}}(x)(X)=X(x)
  \label{dDer}$$ for any $x\in J$ and $X\in{\mbox{Der}}(J)$.\
This first-order differential calculus $(\Omega^1_{{\mbox{\tiny Der}}}(J),d_{{\mbox{\tiny Der}}})$ will be referred to as the *derivation-based first order differential calculus* over $J$.

## First order differential calculi over $J^8_3$

The Lie algebra ${\mbox{Der}}(J^8_3)$ of all derivations of the exceptional Jordan algebra $J^8_3$ is the exceptional compact simple Lie algebra $\mathfrak f_4$. Since $J^8_3$ is simple $Z(J^8_3)=\mathbb R$ so the unital $J^8_3$-module $\Omega^1_{{\mbox{\tiny Der}}}(J^8_3)$ is the vector space of all linear mappings of ${\mbox{Der}}(J^8_3)$ into $J^8_3$ that is $$\Omega^1_{{\mbox{\tiny Der}}}(J^8_3)=J^8_3\otimes {\mbox{Der}}(J^8_3)^\ast
  \label{omegad}$$ where ${\mbox{Der}}(J^8_3)^\ast=\mathfrak f_4^\ast$ denotes the dual vector space of ${\mbox{Der}}(J^8_3)$.\
One defines as before the derivation $d_{{\mbox{\tiny Der}}}:J^8_3\rightarrow \Omega_{{\mbox{\tiny Der}}}(J^8_3)$ by setting $d_{{\mbox{\tiny Der}}}(x)(X)=X(x)$ for any $x\in J^8_3$ and $X\in {\mbox{Der}}(J^8_3)$. The first order differential calculus $(\Omega_{{\mbox{\tiny Der}}}(J^8_3),d_{{\mbox{\tiny Der}}})$ over $J^8_3$ is characterized by the following universal property.

::: proposition
[]{#univ label="univ"} For any first order calculus $(\Omega^1,d)$ over $J^8_3$, there is a unique (unital) Jordan module homomorphism $i_d:\Omega^1_{{\mbox{\tiny Der}}}(J^8_3)\rightarrow \Omega^1$ such that one has $d=i_d\circ d_{{\mbox{\tiny Der}}}$.
:::

[Proof]{.underline}. From the general structure of the $J^8_3$-modules, $\Omega^1$ is of the form $\Omega^1=J^8_3\otimes E$ for some vector space $E$. Let $(e^\alpha)$ be a basis of $E$ then $d(x)=X_\alpha(x)\otimes e^\alpha$ with $X_\alpha\in {\mbox{Der}}(J^8_3)$ for any $\alpha$. Let $(\partial_k)$ be a basis of ${\mbox{Der}}(J^8_3)$ with dual basis $\theta^k$ then one has $d(x)=\partial_k(x)\otimes C^k_\alpha e^\alpha$ with the $C^k_\alpha\in \mathbb R$. Define $i_d$ by $i_d(x\otimes \theta^k)=x\otimes C^k_\alpha e^\alpha$, then $i_d$ is a $J^8_3$-module homomorphism satisfying $d=i_d\circ d_{{\mbox{\tiny Der}}}$ which is clearly unique. $\square$\
[Remark]{.underline}. Proposition [\[univ\]](#univ){reference-type="ref" reference="univ"} is very specific to the exceptional Jordan algebra $J^8_3$ and is a direct consequence of the fact that $J^8_3$ is, as $J^8_3$-module, the only irreducible module. For instance if $J$ is a finite-dimensional simple Euclidean Jordan algebras of Theorem 2 which is distinct of $\mathbb R$ and of $J^8_3$, the first order differential calculus $(\Omega^1_{{\mbox{\tiny Der}}}(J), d_{{\mbox{\tiny Der}}})$ is not universal since then there several inequivalent irreducible $J$-modules and not only $J$ itself. In all these cases one has $\Omega^1_{{\mbox{\tiny Der}}}(J)=J\otimes {\mbox{Der}}(J)^\ast$ and ${\mbox{Der}}(J)$ is a real compact form of a classical simple Lie algebra. Furthermore all the classical simple Lie algebras are realized in this way as Lie algebras of derivations of the finite-dimensional simple special Euclidean Jordan algebras.
