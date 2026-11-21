---
doc_id: arxiv-2202.06733v1
doc_title: "Received <day> <Month>, <year>"
section_id: sec-007-24-the-characteristic-polynomial-and-cayley-hami
section_title: "The characteristic polynomial and Cayley-Hamilton theorem for SU(3)"
section_number: 2.4
pages: 5-6
source_pdf: 2202.06733v1.pdf
source_sha256: e670632090447f14
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 1.0
doc_brief: "Received <day> <Month>, <year> — Diﬀerent ways of representing the group 푆푈(3) within a Geometric Algebra approach are explored."
---
We can now employ these results to look at the characteristic polynomial and Cayley-Hamilton theorem. For the characteristic polynomial

\be
C_f(\lambda)=\sum_{s=0}^{m} (-\lambda)^{m-s} \, \partial_{(s)} \!\ast\! f_{(s)}
\ee

then taking the scalar parts of the above results for $f(a)=B\dt a$, we find

\be
C_f(\lambda)=\textstyle{\frac{1}{64}}\det^2(M) + \textstyle{\frac{1}{16}}|B|^4 \lambda^2 +\half|B|^2\lambda^4+\lambda^6
\ee


For the Cayley-Hamilton theorem, i.e.\ that a linear function satisfies its own characteristic equation, we should find

\be
\sum_{s=0}^{m} (-1)^{m-s} \, \partial_{(s)} \!\ast\! f_{(s)} f^{m-s}(a)=0
\ee

for any input vector $a$. Here this means that $f$ itself should satisfy:

\be
\textstyle{\frac{1}{64}}\det^2(M) a + \textstyle{\frac{1}{16}}|B|^4 f^2(a) +\half|B|^2 f^4(a) + f^6(a)=0
\ee

where we remember $f(a)=B\dt a$ and $f^0(a)=a$.

For $B$ of the completely general $SU(3)$ form given in equation (\ref{eqn:gen-su3-B}), we can explicitly evaluate this equation, and we find that the l.h.s.\ vanishes, and so the Cayley-Hamilton theorem is indeed satisfied.

At this point we can start comparing with the treatment of $SU(3)$ in the Roelfs \alert{`Geometric invariant decomposition of SU(3)'} paper\cite{roelfs2021geometric}, where he is finding the decomposition of a general $SU(3)$ traceless skew-Hermitian matrix $\mathbf{B}$ into three commuting matrices $\mathbf{b}_i$, $i=1,2,3$.

A key equation there, his equation (13) is

\be
0= \frac{1}{64}\left( \det(\mathbf{B})\right)^2-\frac{1}{64}\left({\rm tr}[\mathbf{B}^2]\right)^2\lambda+\frac{1}{4}{\rm tr}[\mathbf{B}^2]\lambda^2-\lambda^3
\label{eqn:roelfs-char-poly}
\ee

from which three roots, $\lambda_i$ can be found, and which will satisfy $\mathbf{b}_i^2=\lambda_i$.

We can compare this with our

\be
C_f(\lambda)=\textstyle{\frac{1}{64}}\det^2(M) + \textstyle{\frac{1}{16}}|B|^4 \lambda^2 +\half|B|^2\lambda^4+\lambda^6
\ee


Modulo some differences in the definition of {\sl length} of $B$, and some signs (arising from Hermitian versus anti-Hermitian matrix choices), we can see that the Cayley-Hamilton theorem applied to $f(a)=a \dt B$ is yielding an equation in which the eigenvalues are {\em squared} compared to the form got via the abstract matrix approach.

We can understand this as follows. Consider the function $f^2$. Writing out this function explicitly as acting on $a$ we get
\be
f^2(a) = \left( a \dt B \right) \dt B
\ee

and this is symmetric because its \alert{curl} vanishes, indeed

\be
\da f^2(a) = \da \left( a \dt B \right) \dt B = -|B|^2
\ee

so that $\da \wdg f^2(a) =0$.

Now in the book by Hestenes \& Sobczyk\cite{hestenessobczyk}, page 82, it says that if we wish to decompose a bivector $B$ into commuting blades, then the {\em squares} of these blades can be found since they satisfy the characteristic polynomial for the function $f(a)= a\dt B$. What is not immediately clear from this statement, is that actually the characteristic polynomial is for the {\em squared} function we have just described. This is why in forming the decomposition using the roots of (\ref{eqn:roelfs-char-poly})
we find a polynomial in the \alert{squares} of our $\lambda$ quantities, and these are the coefficients needed in the decomposition of the bivector $B$.

This also shows us why the {\em square} of the matrix determinant appears in the top level characteristic multivector for this case, since again we are effectively (referring it to the abstract matrix-type approach) working with the function $f^2$ rather than $f(a)=a\dt B$. 

All these considerations will presumably apply more generally when dealing with other groups in which we want to carry out a commuting bivector decomposition of the generators, and to compare this with what one finds via looking at the characteristic multivectors, the full power of which has probably not yet been tapped.

Before moving onto a more detailed study of $SU(3)$ in the context of a GA approach to the strong force, we note that decomposition of $SU(3)$ elements into commuting blades will come up in the perhaps surprising context of Octonions towards the end of the paper, and we will return there to an interpretation of the decomposition found in \cite{roelfs2021geometric}.
