---
doc_id: arxiv-2410.20973v1
doc_title: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-2
source_pdf: 2410.20973v1.pdf
source_sha256: 852b7bbc81a62883
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 1.0
doc_brief: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS — We prove conjectures of Garoufalidis-Gu-Mari˜no [9] that perturbative series associated with the hyperbolic knots 41 and 52 are resurgent and"
---
The volume of a hyperbolic knot $K\subset S^3$ has a natural perturbative deformation constructed from the quantum dilogarithm~\cite{Hikami:stateint}. This deformation is a formal power series
\be
  \Phi_{K}(\hbar)
  \=
  \exp\Big(\frac{\mathrm{Vol}(S^3\backslash K)}{\hbar}\Big)\frac{\hbar^{3/2}}{\sqrt{\delta}}(1+A_1\hbar+\cdots)
\ee
where $\delta$ and $A_k$ are elements in the trace field of $K$. This formal power series $\Phi_{K}$ is conjectured to agree to all orders with the asymptotic series of the Kashaev invariant of $K$---expected to exist as part of Kashaev's volume conjecture~\cite{Kashaev:VC}. Independent of Kashaev's volume conjecture, the series $\Phi_{K}$ can be explicitly described in terms of Neumann--Zagier data~\cite{DimGar:QC} and proved to be a topological invariant~\cite{GSW}. This paper is concerned with the analytic properties of $\Phi_{K}$.

\medskip

It was conjecture by Garoufalidis~\cite{Gar:resCS} that $\Phi_{K}$ is resurgent, which means that its Borel transform has endless analytic continuation~\cite{EcalleI}. The singularities of the Borel transform are expected to be located at the values of the Chern--Simons functional at parabolic $\SL_{2}(\BC)$-flat connections of the knot complement. While there have been many examples of resurgent series associated to non-hyperbolic knots~\cite{Zagier:Vas,CG:KZser}, there has been no proof of resurgence of the asymptotic series $\Phi_{K}$ of any hyperbolic knot.

\medskip

A step further in the study of the analytic properties of $\Phi_{K}$ is to address its summability. This requires the existence of analytic functions with prescribed asymptotics. By refining Hikami's original approach~\cite{Hikami:stateint}, Andersen--Kashaev~\cite{AK:I} defined a convergent integral of products of Faddeev's quantum dilogarithm associated to certain triangulations. These integrals are called state integrals as they give a continuous analogue of state sums. Combining ideas from quantum modularity~\cite{GZ:RQMOD} and numerical Borel--Padé--Laplace resummation, Garoufalidis--Gu--Mariño~\cite{GGM:I} gave precise conjectures for the Borel--Laplace resummation of $\Phi_{K}$ for the two simplest hyperbolic knots $4_1$ and $5_2$. The main result of this paper proves their conjectures for these examples, and it can be summarised in the following theorem.

\begin{theorem}\label{thm:4152}
The series $\Phi_{4_1}$ and $\Phi_{5_2}$ are Borel--Laplace summable and their resummations are equal to combinations of state integrals.
\end{theorem}





The method that we use to prove these conjectures seems easily generalisable and will likely lead to many resurgence and summability results for a wide class of asymptotic series associated to $q$-hypergeometric functions. This would have a variety of applications in a number of areas such as topological strings~\cite{GM:tsres}, quantum $K$-theory~\cite{GivLee:QK}, and complex Chern--Simons theory~\cite{GGM:I}. Hopefully, this can also lend insights to the infinite dimensional approach considered in~\cite{KS:floer}.
