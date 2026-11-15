---
doc_id: arxiv-1604.01247v2
doc_title: "Exceptional quantum geometry and particle physics"
section_id: sec-022-55-differential-calculi-as-a-algebras
section_title: "Differential calculi as A-algebras"
section_number: 5.5
pages: 28-30
source_pdf: 1604.01247v2.pdf
source_sha256: 5a402405aadf5d54
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Exceptional quantum geometry and particle physics — Based on an interpretation of the quark-lepton symmetry in terms of the unimodularity of the color group SU(3) and on the existence of 3"
---
Let ${\cal A}$ be a complex unital $\ast$-algebra and let $\Omega_u({\cal A})=\oplus_{n\geq 0}\Omega^n_u({\cal A})$ be the universal differential calculus over ${\cal A}$, [@kar:1983]. It is shown in [@wor:1989] (see also in [@mdv:2001]) that there is a unique involution on $\Omega_u({\cal A})$ which extends the involution of ${\cal A}$ for which it is a differential graded $\ast$-algebra. This means that one has $$\left\{
 \begin{array}{l}
 (\alpha\beta)^\ast=(-1)^{ab}\beta^\ast \alpha^\ast\\
 d(\gamma^\ast)=(d\gamma)^\ast
 \end{array}
 \right.
 \label{stardga}$$ for any $\alpha\in\Omega^a_u({\cal A}),\beta\in\Omega^b_u({\cal A})$ and $\gamma\in\Omega_u({\cal A})$. The cohomology of $\Omega_u({\cal A})$ is trivial, i.e. $H^n(\Omega_u({\cal A}))=0$ for $n\geq 1$ and $H^0(\Omega_u({\cal A}))=\mathbb C$, and in fact by using a linear form $\omega$ on ${\cal A}$ such that $\omega(\mbox{\rm 1\hspace {-.6em} l})=1$, one constructs a linear mapping $K$ of degree -1 on $\Omega_u({\cal A})$ such that $$dK+Kd=I
 \label{coho}$$ on $\oplus_{n\geq 1}\Omega^n_u({\cal A})$ (see in [@mdv:2001]). By replacing $K$ by $\frac{1}{2}(K+K^\ast)$ one can assume that $K(\alpha^\ast)=K(\alpha)^\ast$ for any $\alpha\in\Omega_u({\cal A})$.\
Let $J={\cal H}({\cal A})$ be the real Jordan algebra of the hermitian elements of ${\cal A}$, i.e. $J=\{h\in {\cal A}\vert h^\ast=h\}$ endowed with the product $$h\circ h'=\frac{1}{2}(hh'+h'h)$$ for $h,h'\in J$. Then the real graded subspace $\Omega(J)$ of $\Omega_u({\cal A})$ of hermitian elements is a real differential graded Jordan algebra, that is a differential calculus over $J$ for the graded Jordan product defined by $$\alpha\circ \beta=\frac{1}{2}(\alpha\beta+(-1)^{ab}\beta\alpha)
 \label{grJ}$$ for $\alpha\in\Omega^a(J),\beta\in\Omega^b(J)$.\
The contracting homotopy $K$ restricts to $\Omega(J)$. By using $K$, one constructs by induction on $n$ a sequence of product $m_n(\alpha_1,\cdots,\alpha_n)$ of respective degrees $2-n$ on $\Omega(J)$ starting with $m_1(\alpha)=d\alpha$ and $m_2(\alpha,\beta)=\alpha\circ \beta$ such that, endowed with these products, $\Omega(J)$ is an $A_\infty$-algebra [@kel:2001]. This implies in particular that the graded Jordan product $\alpha\circ \beta$ of $\Omega(J)$ is associative up to homotopy. In fact, by taking $$m_3(\alpha,\beta,\gamma)=K((\alpha\circ\beta)\circ \gamma-\alpha\circ(\beta\circ \gamma))
 \label{m3}$$ for $\alpha\in\Omega^a(J), \beta\in\Omega^b(J),\gamma\in\Omega^c(J)$ with $a+b+c\geq 1$, one gets $$(\alpha\circ\beta)\circ \gamma-\alpha\circ (\beta\circ \gamma)=d(m_3) (\alpha,\beta,\gamma)$$ i.e. the associativity up to homotopy of the graded Jordan product.\
The occurrence of $A_\infty$-structures in the present context is not accidental. For instance it will be shown in another paper that, for the simple finite dimensional Euclidean Jordan algebras of Theorem 2, the derivation-based differential calculus admits such $A_\infty$-structures with $m_1$ given by the differential and $m_2$ given by the graded Jordan product.
