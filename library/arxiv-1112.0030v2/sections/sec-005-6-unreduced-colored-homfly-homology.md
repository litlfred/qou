---
doc_id: arxiv-1112.0030v2
doc_title: "Homological Algebra of Knots and BPS States"
section_id: sec-005-6-unreduced-colored-homfly-homology
section_title: "Unreduced colored HOMFLY homology"
section_number: 6
pages: 30-36
source_pdf: 1112.0030v2.pdf
source_sha256: 745f143c2df4734b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.984
doc_brief: "Homological Algebra of Knots and BPS States — It is known that knot homologies admit a physical description as spaces of open BPS states. We study operators and algebras acting on these spaces."
---
\label{sec:unreduced}

Here we compute the unreduced colored superpolynomial and the colored HOMFLY polynomial
of the unknot and the Hopf link by using the refined topological vertex approach from \cite{GIKV}.
The formulas obtained there are partition functions, presented in the form of the quotient of two infinite series.
Below we find the explicit closed form expressions for the unreduced $S^r$-colored HOMFLY homology of the unknot and the Hopf link.
More precisely, we evaluate eq. (67) of \cite{GIKV}, according to which the unreduced superpolynomial
(= the Poincar\'e polynomial of the unreduced triply-graded colored homology)
of the Hopf link with components colored by partitions $\lambda$ and $\mu$ is given by:
\begin{equation}
\label{eq67}
\bar{\mathcal{P}}^{\lambda\mu}(\text{Hopf})=(-1)^{|\lambda|+|\mu|} \left(\frac{q_1}{q_2}\right)^{|\lambda||\mu|} \left(Q^{-1}\sqrt{\frac{q_1}{q_2}}\right)^{\frac{|\lambda|+|\mu|}{2}}\times\frac{Z_{\lambda\mu}}{Z_{\emptyset\emptyset}} \,,
\end{equation}
where
\[
Z_{\lambda\mu}=\sum_{\nu} (-Q)^{|\nu|} q_2^{\frac{||\nu||}{2}} q_1^{\frac{||\nu^t||}{2}} \tilde{Z}_{\nu}(q_1,q_2)\tilde{Z}_{\nu^t}(q_2,q_1) s_{\lambda}(q_2^{-\rho}q_1^{-\nu^t}) s_{\mu}(q_2^{-\rho}q_1^{-\nu^t}) \,.
\]
The unreduced superpolynomial of the unknot colored by $\lambda$ is obtained by setting $\mu=\emptyset$ in (\ref{eq67}).

The change of variables from topological strings variables $(Q,q_1,q_2)$ to knot theory variables $(\a,q,t)$ used in this paper is given by:
\begin{eqnarray}
\sqrt{q_2}&=&q, \\ \nonumber
\sqrt{q_1}&=&-tq, \\ \label{transf}
Q&=&-t\a^{-2}. \nonumber
\end{eqnarray}
In particular, the specialization $q_1=q_2$ corresponds to the specialization $t=-1$ in the homological knot invariants.

By expanding the product of the Schur functions as
\[
s_{\lambda}s_{\mu}=\sum_{\varphi} c_{\lambda,\mu}^{\varphi} s_{\varphi} \,,
\]
where $c_{\lambda,\mu}^{\varphi}$ is the Littlewood-Richardson coefficient, we obtain:
\[
Z_{\lambda\mu}=\sum_{\varphi} c_{\lambda,\mu}^{\varphi}  \sum_{\nu} (-Q)^{|\nu|} q_2^{\frac{||\nu||}{2}} q_1^{\frac{||\nu^t||}{2}} \tilde{Z}_{\nu}(q_1,q_2)\tilde{Z}_{\nu^t}(q_2,q_1) s_{\varphi}(q_2^{-\rho}q_1^{-\nu^t}) = \sum_{\varphi} c_{\lambda,\mu}^{\varphi} Z_{\varphi} \,.
\]
Replacing this in (\ref{eq67}) gives
\begin{eqnarray*}
\bar{\mathcal{P}}^{\lambda\mu}(\text{Hopf})&=&(-1)^{|\lambda|+|\mu|} \left(\frac{q_1}{q_2}\right)^{|\lambda||\mu|} \left(Q^{-1}\sqrt{\frac{q_1}{q_2}}\right)^{\frac{|\lambda|+|\mu|}{2}}\times\frac{Z_{\lambda\mu}}{Z_{\emptyset\emptyset}}=\\
&=&(-1)^{|\lambda|+|\mu|} \left(\frac{q_1}{q_2}\right)^{|\lambda||\mu|} \left(Q^{-1}\sqrt{\frac{q_1}{q_2}}\right)^{\frac{|\lambda|+|\mu|}{2}}\sum_{\varphi} c_{\lambda,\mu}^{\varphi}\frac{Z_{\varphi}}{Z_{\emptyset\emptyset}}=\\
&=& \left(\frac{q_1}{q_2}\right)^{|\lambda||\mu|} \sum_{\varphi} c_{\lambda,\mu}^{\varphi} (-1)^{|\varphi|} \left(Q^{-1}\sqrt{\frac{q_1}{q_2}}\right)^{\frac{|\varphi|}{2}} \frac{Z_{\varphi}}{Z_{\emptyset\emptyset}}=\\
&=&  \left(\frac{q_1}{q_2}\right)^{|\lambda||\mu|} \sum_{\varphi} c_{\lambda,\mu}^{\varphi} \bar{\mathcal{P}}^{\varphi}(\unknot) \,.
\end{eqnarray*}
Equivalently, in the knot theory variables $(\a,q,t)$ we found the following simple formula
for the superpolynomial of the Hopf link expressed in terms of that of the unknot:
\begin{equation}\label{hopfun}
\bar{\mathcal{P}}^{\lambda\mu}(\text{Hopf}) \; = \;
t^{2|\lambda||\mu|} \sum_{\varphi} c_{\lambda,\mu}^{\varphi} \bar{\mathcal{P}}^{\varphi}(\unknot) \,.
\end{equation}

Thus, in order to compute the unreduced superpolynomial of the Hopf link,
it suffices to compute the superpolynomial of the unknot from (\ref{eq67}).


\subsection{Unreduced colored HOMFLYPT polynomial and homology of the unknot}

Below we give the results for the unknot derived from (\ref{eq67}). The notations and computations are summarized in Appendix \ref{compun}.

The quantum $sl(N)$ invariant (that is, $\a=q^N$ specialization of the colored HOMFLY polynomial) is given by:
\begin{eqnarray*}
\bar{{P}}^{\lambda}(\unknot)(\a=q^N,q)&=&q^{-2\sum_{x\in\lambda} c(x)}\left[\!\!\!\begin{array}{c} N\\\lambda^t \end{array}\!\!\! \right]=\\
&=&q^{-2(n(\lambda^t )-n(\lambda ) )} \left[\!\!\!\begin{array}{c} N\\\lambda^t \end{array} \!\!\!\right]= q^{-\kappa(\lambda)} \left[\!\!\!\begin{array}{c} N\\\lambda^t \end{array}\!\!\! \right] \,.
\end{eqnarray*}
In particular, for the $r$-th symmetric representation $S^r$ we find
\be
\label{polsim}
\bar{{P}}^{S^r}(\unknot)(\a=q^N,q) \; = \; q^{-r(r-1)} \left[\!\!\begin{array}{c} N+r-1\\ r \end{array}\!\!\right] \,,
\ee
whereas for the anti-symmetric representation $R = \Lambda^r$ we have
\be
\bar{{P}}^{\Lambda^r}(\unknot)(\a=q^N,q) \; = \; q^{r(r-1)} \left[\!\!\begin{array}{c} N\\ r \end{array}\!\!\right] \,.
\ee

The two-variable polynomial $\bar{{P}}^{\lambda}(\unknot)(\a,q)$ can be obtained from the above expressions
by replacing $q^N$ with $\a$ and the $q$-binomial coefficients by two-variable polynomials in the following way:
\begin{equation}\label{pom1}
 \!\!\!\!\!\! \left[\!\!\begin{array}{c}N \\ r-j \end{array}\!\!\right]  \leftrightarrow  \frac{(-1)^{r-j} \a^{r-j} q^{r-j}}{(1-q^2)(1-q^4)\ldots(1-q^{2r})} \sum_{l=0}^r { (-1)^l \a^{-2l} q^{l(r-j-1)} \left[\!\!\begin{array}{c}r-j \\l\end{array}\!\!\right]  (1-q^{2(r-j+1)})\cdots (1-q^{2r})   } \,,
\end{equation}
where the left hand side is the $\a=q^N$ specialization of the right hand side.
This last formula follows from
\[
\prod_{i=0}^{n-1} {(1+q^{2i}z)} \; = \; \sum_{j=0}^n { q^{j(n-1)}  \left[\!\!\begin{array}{c} n \\ j \end{array}\!\!\right]  z^j   } \,.
\]

In particular, for the symmetric representation we have:
\begin{equation}\label{sim1}
\bar{P}^{S^r}(\unknot)(\a,q)=\frac{(-1)^r\a^rq^r}{(1-q^2)(1-q^4)\ldots(1-q^{2r})} q^{-2r(r-1)}\sum_{l=0}^r { (-1)^l \a^{-2l} q^{l(r-1)} \left[\!\!\begin{array}{c}r \\l\end{array}\!\!\right]  q^{2(r-l)(r-1)}    } .
\end{equation}

Now, the formula for the $\a=q^N$ specialization of the $S^r$-colored superpolynomial
for the unknot is obtained by using the following quantum binomial coefficients formula:
\begin{equation}
\left[\!\!\begin{array}{c} N+r-1 \\ r \end{array}\!\!\right] \; = \; q^{r(r-1)} \sum_{j=0}^{r-1} q^{-j(N+r-1)} \left[\!\!\begin{array}{c} r-1 \\ j \end{array}\!\!\right] \left[\!\!\begin{array}{c} N \\ r-j \end{array}\!\!\right] \,.
\end{equation}
Then, the Poincar\'e polynomial of the $S^r$-colored $sl(N)$ homology of the unknot
is obtained by adding a factor $t^{-2j}$ in every summand in the above expression for the quantum
binomial coefficient in (\ref{polsim}):
\begin{eqnarray}
\bar{\mathcal{P}}^{sl(N),S^r}(\unknot)(q,t) & = &
\bar{\mathcal{P}}^{S^r}(\unknot)(\a=q^N,q,t) = \label{simgl} \\
& = & \sum_{j=0}^{r-1} q^{-j(N+r-1)} \left[\!\!\begin{array}{c} r-1 \\ j \end{array}\!\!\right]
\left[\!\!\begin{array}{c} N \\ r-j \end{array}\!\!\right]t^{-2j} \,. \nonumber
\end{eqnarray}
Note that the corresponding homology $\bar{\mathcal{\CH}}^{sl(N),S^r}(\unknot)$ is finite-dimensional.

We list some particular instances of (\ref{simgl}) for small $r$:
\begin{eqnarray}
\bar{\mathcal{P}}^{sl(N),S^1}(\unknot)&=& [N] \,,\\
\bar{\mathcal{P}}^{sl(N),S^2}(\unknot)&=& \left[\!\!\begin{array}{c} N \\ 2 \end{array}\!\!\right] + q^{-(N+1)}[N]t^{-2} \,,\\
\bar{\mathcal{P}}^{sl(N),S^3}(\unknot)&=&  \left[\!\!\begin{array}{c} N \\ 3 \end{array}\!\!\right] + q^{-(N+2)}[2] \left[\!\!\begin{array}{c} N \\ 2 \end{array}\!\!\right]t^{-2} + q^{-2(N+2)}[N]t^{-4} \,.
\end{eqnarray}
Specifying further the value of $N$, one finds the following expressions:
\begin{eqnarray*}
\bar{\mathcal{P}}^{sl(2),S^2}(\unknot)&=&1+q^{-2}t^{-2}+q^{-4}t^{-2},\\
\bar{\mathcal{P}}^{sl(3),S^2}(\unknot)&=&q^2+1+q^{-2}+q^{-2}t^{-2}+q^{-4}t^{-2}+q^{-6}t^{-2},\\
\bar{\mathcal{P}}^{sl(3),S^3}(\unknot)&=&1+q^{-2}t^{-2}+2q^{-4}t^{-2}+2q^{-6}t^{-2}+q^{-8}t^{-2}+q^{-8}t^{-4}+q^{-10}t^{-4}+q^{-12}t^{-4},\\
\bar{\mathcal{P}}^{sl(4),S^2}(\unknot)&=&q^4+q^2+2+q^{-2}+q^{-4}+q^{-2}t^{-2}+q^{-4}t^{-2}+q^{-6}t^{-2}+q^{-8}t^{-2}.
\end{eqnarray*}
The expression for the whole triply-graded superpolynomial is obtained from (\ref{simgl}) by using (\ref{pom1}).\\

In the case of anti-symmetric representations, the entire homology of the unknot is concentrated
in the homological degree zero, and thus the $\Lambda^r$ superpolynomial of the unknot coincides
with its $\Lambda^r$-colored HOMFLY polynomial:
\begin{equation}
\bar{\mathcal{P}}^{sl(N),\Lambda^r}(\unknot) \; = \; q^{r(r-1)}  \left[\!\!\begin{array}{c} N \\ r \end{array}\!\!\right] \,.
\end{equation}




\subsection{Comparison with other approaches}
\label{sec:comparison}

Much of the present paper is devoted to exploring the structure --- motivated from physics --- of the colored knot homology,
namely its reduced version. A combinatorial or group theoretic definition of such theory is still waiting to be discovered.
However, in the case of the unreduced theory, which we sketched in this section, there have been several attempts
to define the colored knot homology, especially in low rank.
Therefore, we conclude this section with a brief comparison to other approaches.

Unfortunately, the structure of the colored differentials becomes more obscure (alternatively, more interesting!) in the unreduced version of
the colored knot homology.\footnote{This is familiar from the ordinary, non-colored knot homology \cite{DGR,GWalcher}.}
This, in part, is the reason why we kept our discussion here very brief, relegating a more thorough analysis to future work.
Another reason, which will become clear in a moment, is that even a quick look at the unknot
exposes a number of questions that need to be understood in order to relate and unify different formulations:

\begin{itemize}

\item
singularities in moduli spaces (of BPS configurations):
$\dim \CH_{\text{BPS}} < \infty$ versus $\dim \CH_{\text{BPS}} = \infty$

\item
framing dependence in the colored knot homology

\item
colored homological invariants versus cabling

\item
analog of wall crossing phenomena in mathematical formulations of colored knot homologies

\item
the role of the ``preferred direction'' in the combinatorial formulation based on 3d partitions

\item
proper interpretation of formal expressions, or
\be
\frac{1-q^2}{1-q^2} = (1-q^2)(1 + q^2 + q^4 + q^6 + \ldots) \qquad \text{versus} \qquad \frac{1-q^2}{1-q^2}=1
\label{susyratio}
\ee

\end{itemize}

\noindent
In addition, each formulation typically involves individual choices and subtleties, which may also affect the form of the answer.
In fact, even the total dimension of the colored homology may depend on some (or, perhaps, all)
of these choices.\footnote{We hope that at least some of these delicate aspects are washed away when one passes
to the reduced theory, as it happens in the non-colored case. This is one of the reasons why in the present paper
we mainly consider the reduced homology.}

While good understanding of these aspects is still lacking, many approaches to colored knot homology seem to agree
on one general feature: the unreduced $sl(N)$ homology has finite support only for certain sufficiently small representations.
For example, in \cite[eq. (67)]{GIKV} this corresponds to the fact that for general representations
there is no way to clear the denominators.
This should be compared with the fundamental representation of $sl(N)$,
where every existent approach leads to a homology with finite support.
The simplest example that belongs to the ``grey territory'' is the second symmetric representation $R=S^2$ of $sl(N)$.
For $N=2$, this corresponds to the adjoint representation of $sl(2)$ and, as we saw in \eqref{HHunknot3dim},
physics realizations \cite{GSV,fiveknots} lead to a 3-dimensional knot homology
$\bar{\CH}^{sl(2), \tableau{2}} (\unknot)$ categorifying the colored Jones polynomial of the unknot,
\be
\bar P^{\tableau{2}}_2 (\unknot) \; = \; [3] \; = \; q^{-2} + 1 + q^2 \,.
\label{coloredJunknot}
\ee
On the other hand, some mathematical formulations lead to a theory with infinite support
(which can be attributed to several gaps in the present understanding and the above-listed questions).
For example, fixing\footnote{We thank E.~Gorsky for pointing this out.} a typo in \cite[Proposition 3.4]{Webster},
one finds the following candidate for the Poincar\'e polynomial of the colored unknot homology:
\be
\bar \CP^{\tableau{2}}_2 (\unknot) \; = \; q^{-2} t^2 + 1 + q^2 t^{-2} + \frac{q^{-2} + q^{-2} t}{1-t^2 q^{-4}} \,.
\label{PWebster}
\ee
The structure of the corresponding homology theory is clear: the first three terms reproduce (upon specializing to $t=-1$)
the colored Jones polynomial \eqref{coloredJunknot} and the quotient in the last term corresponds to
the infinite-dimensional contribution to the homology, all of which disappears upon taking the Euler characteristic.

Similar structure emerges in other frameworks,
in particular in approaches based on categorification of the Jones-Wenzl projectors.
The Jones-Wenzl projectors appear in decomposing the finite dimensional representations
of the quantum group $U_q (\frak{sl}_2)$ and, as such, play a key role in the definition
and computation of quantum group invariants of knots and 3-manifolds.
Several ways to categorify the Jones-Wenzl projectors have been proposed in the literature,
{\it e.g.} the topological categorification \cite{CKrushkal}
and the Lie theoretic categorification \cite{Stroppel} which agree (up to Koszul duality).
In particular, the latter approach leads to a theory that categorifies \eqref{coloredJunknot}
by replacing the middle term with infinite-dimensional homology whose Poincar\'e polynomial equals
\be
\bar \CP^{\tableau{2}}_2 (\unknot) \; = \; q^{-2} + \frac{1}{[2] [2]} (q+q^{-1})^2 + q^2 \,,
\label{PStroppel}
\ee
where $[2] = q+q^{-1}$ and the authors of \cite{Stroppel} instruct us to interpret $\frac{1}{[2]}$
as a power series $q - q^3 + q^5 - q^7 + \ldots$. This power series is familiar to physicists as
a trace (``partition function'') over the infinite-dimensional Hilbert space
$\CH_{\text{Bose}} = H^* (\cp^{\infty}) = \C [x]$
of a harmonic oscillator / single boson,
\be
P_{\text{Bose}} \; = \; \frac{1}{1-q^2} = 1 + q^2 + q^4 + q^6 + \ldots \,.
\label{ZBose}
\ee
Partition function of a single fermion has a similar form, except that fermions contribute to
the numerator instead of the denominator. Indeed, the trace over a two-dimensional Hilbert space
of a single fermion looks like
\be
P_{\text{Fermi}} \; = \; 1-q^2 \,,
\label{ZFermi}
\ee
in agreement with a well-known fact that contributions of bosons and fermions cancel each other, {\it cf.} \eqref{susyratio}.
Therefore, instead of canceling the ratio in the middle term of \eqref{PStroppel},
the authors of \cite{Stroppel} instruct us to interpret it as a Hilbert space of two bosons and two fermions.
Note, due to the presence of bosonic states this Hilbert space is infinite-dimensional,
as opposed to a much smaller, finite-dimensional space that one might infer by simplifying the ratio.
Similarly, \eqref{PWebster} contains one boson
(due to the factor $\frac{1}{1-t^2 q^{-4}}$ in the last term), {\it etc.}

If this, however, is the proper interpretation of \eqref{PStroppel}, then one immediately runs into
a general question of how to interpret formal expressions like \eqref{susyratio} and when to clear denominators.
The answer to this question will certainly affect many calculations of Poincar\'e polynomials,
in particular calculations based on \cite[eq. (67)]{GIKV} that has non-trivial numerators and denominators,
as well as similar calculations in other frameworks.

A novel physical framework that appears to be closely related to knot homology
is the so-called ``refined Chern-Simons theory.''
Although Lagrangian definition of this theory is not known at present,
its partition function was conjectured \cite{AShakirov} to compute topological invariants
of knots and 3-manifolds that preserve an extra rotation symmetry.
This includes torus knots and Seifert 3-manifolds.
The rotation symmetry gives rise to an extra quantum number, so that for torus knots
and Seifert 3-manifolds the refined Chern-Simons theory leads to a striking prediction:
the space \eqref{HHBPS} is quadruply-graded rather than triply-graded in these cases.

In simple examples, the fourth grading (coming from the extra rotation symmetry of a 3-manifold)
is determined by the other three gradings \eqref{aqtgradings}.
It would be interesting to study under which conditions this happens; when it does, the partition function
of the $SU(N)$ refined Chern-Simons theory computes the specialization of the superpolynomial to $\a = q^N$.
Assuming this is the case for the unknot colored by the second symmetric representation,
the $SU(2)$ refined Chern-Simons theory gives:
\be
\bar \CP^{\tableau{2}}_2 (\unknot) \; = \;
- \frac{(q^2 t + q^{-2})}{(q - q^{-1})} \frac{(q^4 t^2 + q^{-2} t^{-1})}{(q^3 t^2 - q^{-1})} \,.
\label{PrefinedCS}
\ee
The corresponding Hilbert space contains at least two ``bosons'' (due to two factors in the denominator of \eqref{PrefinedCS})
and, therefore, leads to a version of colored homology with infinite support.

In our quick tour through different ways of categorifying the colored Jones polynomial of the unknot \eqref{coloredJunknot}
we saw theories with finite support as well as theories with infinite support, in fact, of different kind
(with different number of ``bosons'' / factors in the denominator).
One would hope that all these theories correspond to different choices (of framing, chamber, regularization, ... )
and with a proper understanding of the above-mentioned issues could be unified in a single framework.
One piece of evidence that it might be possible
comes from the fact that all physical and geometrical approaches agree when
the corresponding moduli spaces are non-singular, as {\it e.g.} for minuscule representations.
Therefore, we hope to see a much bigger story, only small elements of which have been revealed so far.



\bigskip
{\it Acknowledgments~}
We would like to thank S.~Cautis, M.~Marino, K.~Schaeffer,
Y.~Soibelman, C.~Stroppel, C.~Vafa, J.~Walcher, and E.~Witten
for valuable discussions.

The work of SG is supported in part by DOE Grant DE-FG03-92-ER40701
and in part by NSF Grant PHY-0757647.
Opinions and conclusions expressed here are those of the authors
and do not necessarily reflect the views of funding agencies.

MS was partially supported by the Funda\c c\~ao para a Ci\^encia e Tecnologia (ISR/IST plurianual funding)
through the programme Programa Operacional Ci\^encia, Tecnologia, Inova\c c\~ao (POCTI) and the POS Conhecimento programme,
co-financed by the European Community fund FEDER.
MS was also partially supported by the Ministry of Science of Serbia, project no. 174012.
