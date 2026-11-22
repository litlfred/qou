---
doc_id: arxiv-1412.4711v1
doc_title: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT"
section_id: sec-017-41-a-variety
section_title: "A-variety"
section_number: 4.1
pages: 20-20
source_pdf: 1412.4711v1.pdf
source_sha256: 4fb1d6ee062cca8c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.986
doc_brief: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT — We give a description of several representation varieties of the fundamental group of the complement of the ﬁgure eight knot in PGL(3, C) or"
---
The study of these eigenvalues on each component of $\mathrm{Defor}(M,\mathcal T)$ can then be done by adding the following set $L_{\{l,m\}}$ of equations to the generators of, respectively, $I_{Y_{1}} ,I_{Y_{2}}$ and $I_{Y_{3}}$:
\begin{eqnarray*}
L_{\{ l,m \}} &= &\left\{ u_{34} v_{24} L-u_{12} u_{21}  , \quad v_{31} u_{42} v_{42} u_{24} M-u_{13} u_{31} v_{14} v_{23}  ,\right. \\
&&\left.  u_{34} L^{\ast} -v_{42} 
, \quad u_{42} v_{32}
u_{24} v_{41} M^{\ast} -u_{31} v_{13} u_{13} v_{24} \right\}.
\end{eqnarray*}

Eliminating all the variables but $\{ L,L^{\star} ,M,M^{\star} \}$ by means of
Gr{\"o}bner bases and similar factorization tricks as for the computation of
$\tmop{Defor} ( M, \mathcal{T} )$, we get that :
\begin{itemize}
  \item $( I_{Y_{2}} + \langle L_{l,m} \rangle ) \cap \mathbb{Q} [
  L,L^{\star} ,M,M^{\star} ] = \langle L^{3} -M,L^{\star 3} -M^{\star}
  \rangle$ or, equivalently, that over all the points of $D_{2}$, $L^{3} =M$
  and $L^{\star 3} =M^{\star}$
  
  \item $( I_{Y_{3}} + \langle L_{l,m} \rangle ) \cap \mathbb{Q} [
  L,L^{\star} ,M,M^{\star} ] = \langle L^{3} M-1,L^{\star 3} M^{\star} -1
  \rangle$ or, equivalently, that over all the points of $D_{3}$, $L^{3} =
  \frac{1}{M}$ and $L^{\star 3} = \frac{1}{M^{\star}}$
\end{itemize}
The eigenvalues over the component $D_{1}$ are more complicated to describe.
The Gr{\"o}bner basis of $( I_{Y_{1}} + \langle L_{l,m} \rangle ) \cap
\mathbb{Q} [ L,L^{\star} ,M,M^{\star} ]$, for the Degree Reverse
Lexicographic ordering is huge (made of 141 polynomials with up to 3462
terms). This might be due to the ordering itself or to the fact that the ideal
might have many complicated embedded components which can be viewed as an
artifact of the projection onto the coordinates $[L,L^{\star} ,M,M^{\star} ]$.

Using an elimination ordering with $M>L,L^{\star} ,M^{\star}$ one gets a
simpler description showing in particular that generically (say outside a
subvariety of dimension $1$), the points of that component of the $A$-variety
are in one-to-four correspondence with those of the hypersurface $H_{1}$ of
$\mathbb{C}^{3}$.
