---
doc_id: arxiv-2202.06733v1
doc_title: "Received <day> <Month>, <year>"
section_id: sec-005-22-the-characteristic-polynomial-and-the-cayley
section_title: "The characteristic polynomial and the Cayley-Hamilton theorem"
section_number: 2.2
pages: 3-3
source_pdf: 2202.06733v1.pdf
source_sha256: e670632090447f14
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 1.0
doc_brief: "Received <day> <Month>, <year> — Diﬀerent ways of representing the group 푆푈(3) within a Geometric Algebra approach are explored."
---
\label{sect:cay-ham}

We can now employ these definitions to look at the characteristic polynomial and {\em Cayley-Hamilton theorem}. These use just the scalar parts of the various simplicial derivatives. As shown in Hestenes \& Sobczyk\cite{hestenessobczyk} Section 3-2, the characteristic polynomial is

\be
C_f(\lambda)=\sum_{s=0}^{m} (-\lambda)^{m-s} \, \partial_{(s)} \!\ast\! f_{(s)}
\ee

where $\partial_{(0)} \!\ast\! f_{(0)}$ is interpreted as 1, $\lambda$ here is the scalar argument of the polynomial function, and the $\ast$ means `scalar part of' the geometric product.

If $\lambda$ is an eigenvalue of $f$, i.e.\ $f(a)=\lambda a$, then it should be a root of the characteristic polynomial, i.e.\ we will have $C_f(\lambda)=0$.
The Cayley-Hamilton theorem is then that a linear function satisfies its own characteristic equation, i.e.\ we should find

\be
\sum_{s=0}^{m} (-1)^{m-s} \, \partial_{(s)} \!\ast\! f_{(s)} f^{m-s}(a)=0
\ee

for any input vector $a$, where $f^0(a)$ is interpreted as $a$.
