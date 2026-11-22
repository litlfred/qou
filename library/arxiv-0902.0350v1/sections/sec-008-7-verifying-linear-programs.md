---
doc_id: arxiv-0902.0350v1
doc_title: "A REVISION OF THE PROOF OF THE KEPLER CONJECTURE"
section_id: sec-008-7-verifying-linear-programs
section_title: "Verifying linear programs"
section_number: 7
pages: 19-22
source_pdf: 0902.0350v1.pdf
source_sha256: 4591687132c93973
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.975
doc_brief: "A REVISION OF THE PROOF OF THE KEPLER CONJECTURE — The Kepler conjecture asserts that no packing of congruent balls in three-dimensional Euclidean space has density greater than that of the"
---
\label{sec:lp}

This section reports on the current state of the formal verification of
the linear programming part of the proof of the Kepler conjecture.
The results of the linear programming in the original proof are recorded
in several gigabytes of log files.
This section presents the formalization of the generation and bounding of these linear programs 
in the mechanical proof assistant Isabelle~\cite{LNCS2283}. 
A more detailed version of the material presented here can be found in S. Obua's thesis~\cite{obua:phd}.

This formalization relies on the archive of tame graphs. Each tame graph (except the graphs associated with the face-centered cubic and hexagonal close packings) represents a potential counterexample to the Kepler conjecture. 
Each potential counterexample  obeys certain constraints.  The original
proof refutes each potential counterexample by building a linear program
from the constraints and showing that these linear programs are infeasible.

A structure, which we call a \emph{graph system}, makes this precise
in a formal environment.
An instance of a graph system is a tame graph which obeys the constraints listed in the definition of a graph system.
The current formalization does not use all of the constraints of the original proof but only those that do not require branch and bound strategies. Our current notion of graph system can be viewed
as a detailed formalization of what is called \emph{basic linear programs} in~\cite[\S 23.3]{Hales:2006:DCG}. 
Because the current formalization does not capture not all constraints of the original proof, we cannot hope to refute all potential counterexamples. Nevertheless we manage to refute most of them.

We represent tame graphs as \emph{hypermaps}~\cite{gonthier:2008:formal}, \cite{hales:2008:blueprint}. As mentioned in Section~\ref{sec:blueprint}, 
a hypermap is just a finite set $D$ of \emph{darts} together
with three permutations on $D$: the edge, the face, and the node permutation that compose to the identity $e\circ n\circ f = I$.   See Figure~\ref{fig:hypermap}.
This representation greatly simplifies
the axiomatization of a graph system. For a detailed description of how we represent 
hypermaps and for a complete list of all of the axioms of a graph system see~\cite[\S4]{obua:phd}.

\begin{figure}
\begin{center}
\includegraphics[width=12cm]{hyper.pdf}
\end{center}
\caption{A hypermap is a combinatorial structure attached to a planar graph.  A  dart, represented as a small triangle, is place at each face angle of the graph.  In the second frame, the face permutation $f$ cycles through the darts in each face.  In the third frame, the node permutation $n$ cycles through the darts at each node.  The edge permutation $e$ (not shown) is an involution exchanging darts from opposite ends of the edge of a graph. (This figure has ben reproduced from~\cite{Hales:2008:Dodec}.)}
\label{fig:hypermap}
\end{figure}

Figure~\ref{fig:lpapproach} summarizes how we generate and solve the linear programs.
We apply the axioms of a graph system to each tame graph. This results in a large Isabelle theorem which is a conjunction of
linear equalities and inequalities. We then normalize this conjunction
to bring it into the form of a matrix inequality
\begin{equation}
A  x \leq b.
\end{equation}
The entries of $A$ and $b$ are symbolic expressions which contain various real constants (such as $\pi$) that are needed to
define the axioms of a graph system. In order to apply linear programming, 
we need to replace $A$ and $b$ with numerical approximations. We achieve this via a formalization of 
interval arithmetic in Isabelle, and arrive at numerical matrices $A'$, $A''$ and $b'$ for which we have the formally proven 
Isabelle theorems 
\begin{equation}
A' \leq  A  \leq A'', \quad b \leq b'.
\end{equation}
We then apply a simple preprocessing step which gives us formally proven a-priori bounds $x'$ and $x''$ for $x$ such
that 
\begin{equation}
x' \leq x \leq x''.
\end{equation}
It is then possible to obtain a certificate from an external linear programming solver like GLPK (Gnu Linear Programming Kit) that allows us to formally reach a contradiction from $A x \leq b$. The beauty of a certificate is 
that we can use results obtained from an untrusted source (in our case this untrusted source is a 
heavily optimized linear program solver programmed in C) in a trusted and completely mechanically verifiable way.

In this way, we proved the inconsistency of 2565 of the graph systems but failed to prove the inconsistency of the remaining 206. 
This yields a success rate of about $92.5\%$. Future work will extend the notion of graph system and  generate linear programs
that take all the constraints of the original proof into account.


\begin{figure}
\begin{center}
\includegraphics[width=10cm]{lpapproach.pdf}
\end{center}
\caption{Refuting a potential counterexample to the Kepler conjecture}
\label{fig:lpapproach}
\end{figure}

\part{Addendum to and Errata in the Original Proof}
