---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-045-11-open-questions-and-problems
section_title: "Open questions and problems"
section_number: 11
pages: 34-36
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.97
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:question}

We conclude this survey paper with a list of open questions and problems.

\begin{enumerate}
\item Using elementary ideals one can define the twisted $k$--th Alexander polynomial, generalizing the $k$--th Alexander polynomial of a knot $K\subset S^3$.
What information do these invariants contain?
\item  Let $K\subset S^3$ a knot and let $\gamma:\pi_1(S^3\setminus \nu K)\to \mbox{SL}(k,R)$ be a representation, where $R$ is a Noetherian UFD with possibly trivial involution.
Does it follow that $\Delta_K^\gamma$ is reciprocal, i.e. does it hold that $\Delta_K^\gamma \doteq \overline{\Delta_K^\gamma}$?
Note that this holds for unitary representations (cf. Section \ref{section:duality}, \cite{Ki96}, \cite{KL99a}) and for all calculations known to the authors. \\
Added in proof: This question was answered in the negative by Hillman, Silver and Williams \cite{HSW09}, cf. also the remark after Proposition \ref{prop:dualitytau}.
\item Can any two knots or links be distinguished using twisted Alexander polynomials?
\item If $(N,\phi)$ is non--fibered, does there exist a representation $\gamma:\pi_1(N)\to \mbox{GL}(k,R)$ such that
$\Delta_{N}^{\gamma \otimes \phi}$ is not monic?
\item If $(N,\phi)$ is non--fibered, does there exist a representation $\gamma:\pi_1(N)\to \mbox{SL}(2,\mathbb{C})$ such that
$\tau(N,{\gamma\otimes \phi})$ is not monic? (cf. e.g. \cite[Problem~1.1]{GM03}).

\item If $(N,\phi)$ is non--fibered, does there exist a representation $\gamma:\pi_1(N)\to \mbox{GL}(k,R)$ such that
$\Delta_{N}^{\gamma \otimes \phi}$ is zero?


\item Let $K\subset S^3$ be any knot, does the twisted Reidemeister torsion of \cite{GKM05} corresponding to a generic faithful representation detect fiberedness? (cf. \cite[p.~452]{Mo08} for some calculations).
\item Let $N$ be a 3--manifold with empty or toroidal boundary, $N\ne S^1\times D^2, S^1\times S^2$, let $\phi \in H^1(N;\mathbb{Z})$ and let $\gamma:\pi_1(N)\to \mbox{GL}(k,R)$ be a  representation such that $\Delta_{N}^{{\gamma\otimes \phi}}\ne 0$. Does it follow that
\[\deg(\tau(N,{\gamma\otimes \phi}))= \deg(\Delta_{N,1}^{\gamma\otimes \phi})-\deg(\Delta_{N,0}^{\gamma\otimes \phi})-\deg(\Delta_{N,2}^{\gamma\otimes \phi})  \]
has the parity of $k||\phi||_T$? Note that this holds for fibered $(N,\phi)$ and for the untwisted Alexander polynomials of a knot.\\
Added in proof: this also holds for hyperbolic knots and the canonical $SL(2,\C)$ representation. 
\item Does the twisted Alexander polynomial detect the Thurston norm of a given $\phi \in H^1(N;\mathbb{Z})$?
\item Let $K$ be a hyperbolic knot and $\rho:\pi_1(S^3\setminus \nu K)\to \mbox{SL}(2,\mathbb{C})$ the unique discrete faithful representation.
\begin{enumerate}
\item  Is $\Delta_K^\rho$ non--trivial?
\item Does $\deg(\Delta_K^\rho)$ determine the genus of $K$?
\item Is $K$ fibered if $\tau(K,\rho)$ is monic?
\end{enumerate}
Note that the unique discrete representation is over a number field which for many knots can be obtained explicitly with Snappea.
These questions can therefore be answered for small crossing knots.\\
Added in proof: the answer to all three questions is yes, if $K$ has at most 13 crossings (\cite{DFJ10}).
\item Does there exist a knot $K\subset S^3$ and a nonabelian representation  $\gamma$ such that $\Delta_K^\gamma$ is trivial?
\item Are there knots for which Kitayama's lower bounds on the free genus of a knot (cf. \cite{Kiy08a})
are larger than the bound on the ordinary genus obtained in \cite{FK06}?

\item Find a practical algorithm for computing higher order Alexander polynomials.
\item Do higher order Alexander polynomials detect mutation?
\item Does there exist a twisted version of Turaev's torsion function?
\item Use twisted Alexander polynomials to determine which knots with up to twelve crossings are doubly slice.
\item Can the results of \cite{HK79} and \cite{Hat80} regarding Alexander polynomials of amphichiral knots be generalized to twisted Alexander polynomials?
\end{enumerate}
