---
doc_id: arxiv-1604.01247v2
doc_title: "Exceptional quantum geometry and particle physics"
section_id: sec-020-53-differential-graded-jordan-algebras
section_title: "Differential graded Jordan algebras"
section_number: 5.3
pages: 26-27
source_pdf: 1604.01247v2.pdf
source_sha256: 5a402405aadf5d54
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Exceptional quantum geometry and particle physics — Based on an interpretation of the quark-lepton symmetry in terms of the unimodularity of the color group SU(3) and on the existence of 3"
---
Let us define a *differential graded Jordan algebra* to be a $\mathbb N$-graded algebra $$\Omega=\oplus_{n\in \mathbb N}\Omega^n$$ which is a *Jordan superalgebra*, (see e.g. in [@kac:1977], [@mar-zel:2010]), for the induced $\mathbb Z/2\mathbb Z$ degree and which is equipped with a *differential*, that is with an antiderivation $d$ of degree 1 and of square 0.\
Thus $\Omega$ is a graded-commutative algebra, that is one has $$ab=(-1)^{\vert a\parallel b\vert} ba \in \Omega^{\vert a\vert+\vert b\vert}
\label{grcom}$$ for $a\in \Omega^{\vert a\vert}$, $b\in \Omega^{\vert b\vert}$, and one has the *graded Jordan identity* $$(-1)^{\vert a\parallel c\vert}[L_{ab},L_c]_{\mathrm{gr}}+(-1)^{\vert b\parallel a\vert}[L_{bc},L_a]_{\mathrm{gr}}+(-1)^{\vert c\parallel b\vert}[L_{ca},L_b]_\mathrm{gr}=0
\label{grJ}$$ for $a\in \Omega^{\vert a\vert},b\in\Omega^{\vert b\vert}, c\in \Omega^{\vert c\vert}$ where $L_a$ is the left-multiplication operator by $a\in \Omega$ defined by $L_a(x)=ax$ for any $x\in \Omega$ and where $[\bullet, \bullet]_{\mathrm{gr}}$ denotes the graded commutator $$[A,B]_{\mathrm{gr}}=AB-(-1)^{\vert a \parallel b\vert}BA$$ for $A$ of degree $\vert a\vert$ and $B$ of degree $\vert b\vert$. The differential $d$ satisfies $$d^2=0$$ $$d\Omega^n\subset \Omega^{n+1}$$ for any $n\in \mathbb N$, and the graded Leibniz rule $$d(ab)=d(a)b+(-1)^{\vert a\vert} ad(b)$$ for $a\in \Omega^{\vert a\vert}$, $b\in \Omega$.\
In the following the real unital differential graded Jordan algebras will be our models for the "algebras of differential forms\" on "quantum spaces\".\
Let $J$ be a Jordan algebra. A differential graded Jordan algebra $\Omega=\oplus_{n\geq 0}\Omega^n$ such that $\Omega^0=J$ will be called a *differential calculus over* $J$.\
