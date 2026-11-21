---
doc_id: arxiv-2301.00125v3
doc_title: "Generating Function for Pinsky’s Combinatorial Second Moment Formula for the Generalized Ulam Problem"
section_id: sec-009-5-summary-and-outlook
section_title: "Summary and outlook"
section_number: 5
pages: 16-16
source_pdf: 2301.00125v3.pdf
source_sha256: 7ecd0cff7d6c2ec4
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.986
doc_brief: "Generating Function for Pinsky’s Combinatorial Second Moment Formula for the Generalized Ulam Problem — Given a uniform random permutation π ∈Sn, let Zn,k be equal to the number of increasing"
---
We have presented some explicit formula for the generating function of the combinatorial array $A(N,j)$.
This arrray was introduced by Ross Pinsky in his beautiful combinatorial formula for the 2nd moment
of $Z_{n,k}$ from the generalized Ulam problem.
Pinsky then obtained rigorous upper and lower bounds, sufficient for his purpose of determining when the sequence $Z_{n,{k_n}}$
satisfies a weak law of large numbers or does not satisfy such, depending on the behavior of the sequence $k_n$
as $n \to \infty$.
But for  reasons discussed in Appendix \ref{sec:SK} and in the introduction, we believe
that more precise asymptotics are desirable.

We presented several formulas for the generating function, but not for the precise asymptotics. Using the Chebyshev
inequality applied to 
\begin{equation}
\alpha(w,x^2)\, =\, \sum_{j,N=0}^{\infty} w^j x^{2N} A(N,j)\, ,
\end{equation}
since all the combinatorial terms $A(N,j)$ are nonnegative, we may obtain an upper bound
\begin{equation}
	A(N,j)\, \leq\, \min_{w>0} \min_{z>0} \frac{\alpha(w,x^2)}{w^j x^{2N}}\, =\,
\min_{w>0} \min_{z>0} \frac{\mathcal{A}_1(x,w)+\mathcal{A}_2(x,w)}{w^j x^{2N}}\, .
\end{equation}
We have not yet carried out this optimization problem.
We mention that the collaboration resulting in the present paper took place after one of the authors
worked on his own (with mentorship) for  precisely one summer, and then both coauthors collaborated
on the present paper after that work was carried out.
This paper represents the end product of a certain collaboration. 
Even if further results seem like they should naturally be contained herein, we have limited this paper to 
the products of that research experience.

So the above calculation represents our primary interest in future research in this area.
As we said before, a next natural question is to calculate $\mathbf{E}[Z_{n,k} Z_{n,\ell}]$ for $k$ and $\ell$
being allowed to differ.
We expect that is an important first step towards calculating all higher moments by iterating Pinsky's
procedure for the 2nd moment.
But as with the problem above, we have not carried that out yet.
Either we will return to this problem, possibly in collaboration with other researchers.
Or else perhaps some other researchers will resolve this, indepenent from ourselves.

\label{sec:Outlook}


\section{Acknowledgments}

S.S.~is grateful to Dongsheng Wu for a  helpful conversation. The work of S.S.~was partly supported by 
a Simons collaboration grant.
