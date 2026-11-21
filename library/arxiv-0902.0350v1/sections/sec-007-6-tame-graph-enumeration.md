---
doc_id: arxiv-0902.0350v1
doc_title: "A REVISION OF THE PROOF OF THE KEPLER CONJECTURE"
section_id: sec-007-6-tame-graph-enumeration
section_title: "Tame graph enumeration"
section_number: 6
pages: 16-19
source_pdf: 0902.0350v1.pdf
source_sha256: 4591687132c93973
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.978
doc_brief: "A REVISION OF THE PROOF OF THE KEPLER CONJECTURE — The Kepler conjecture asserts that no packing of congruent balls in three-dimensional Euclidean space has density greater than that of the"
---
\label{sec:graph}

Tame graphs are particular plane graphs that represent potential
counterexamples to the Kepler conjecture. The \emph{Archive} is a list of over 5000 plane
graphs.  The original proof generates the Archive with the help of a Java program that
enumerates all plane graphs. Tameness is defined
in Section~18 and the enumeration is sketched in Section~19 of
\cite{Hales:2006:DCG}.
This section sketches the formally machine-checked proof of Claim~3.13 and
Theorem 19.1 in the original proof~\cite{Hales:2006:DCG}:
\begin{thm}\label{Archive:complete}
Any tame plane graph is isomorphic to a graph in the Archive.
\end{thm}
There are two potential reasons why an error in the original proof of this theorem might have gone undetected:
the publications only sketch the details of the enumeration, and the
referees only made a passing glance at the implementation, consisting of more than 2000
lines of Java.

 

We recast the Java program for the enumeration of all tame graphs in
logic, proved its completeness with the help of an interactive theorem prover,
ran it, and compared the output to the
Archive.  It turns out that the original proof was right, the Archive is complete,
although redundant (there are at most 2771 tame graphs).
Doing all this inside a logic and a theorem prover requires two things:
\begin{itemize}
\item The logic must contain a programming language.
We used Church's \emph{higher-order logic} (HOL) based on $\lambda$-calculus,
the foundation of functional programming. Programs in HOL are simply
sets of recursion equations, i.e.\ pure logic.
\item The programming language contained in the logic must be efficiently
executable and such executions must count as proofs. The theorem prover that we used, Isabelle/HOL~\cite{LNCS2283} fulfills this criterion. If all functions
that appear in a term are either data, e.g.\ numbers, or functions defined
by recursion equations, Isabelle/HOL offers the possibility to evaluate this term $t$ in one big and relatively efficient step to a value $v$, giving rise to the theorem $t = v$.
\end{itemize}
The enumeration of all tame graphs generates 23 million plane graphs ---
hence the need to perform massive computations in reasonable time.

Now we give a top-level overview of the formalization and proof of
completeness of the enumeration of tame graphs in HOL. For details
see~\cite{NipkowBS-IJCAR06}. The the complete machine-checked proof, over
17000 lines, is available online in the Archive of Formal Proofs at
\url{afp.sf.net}~\cite{BauerN-AFP06}.


\subsection{Plane graphs}

Following the original proof, we represent finite, undirected, plane graphs as lists
(= finite sets) of faces and faces as lists of vertices. Note that by
representing faces as lists they have an orientation. The enumeration of
plane graphs requires an additional distinction between \emph{final}
and \emph{non-final} faces. Hence a face is really a pair of a list
of vertices and a Boolean.
A plane graph is \emph{final} iff each of its faces is.
In final graphs we can ignore the Boolean component of the faces.


\subsection{Enumeration of plane graphs}

The original proof characterizes plane graphs by an executable enumeration and sketches a
proof of completeness of this enumeration. We have followed the original proof and taken
this enumeration as the definition of planarity.  The enumeration of plane
graphs in the original proof proceeds inductively: you start with a seed graph with two faces, the
final outer one and the (reverse) non-final inner one. If a graph contains a
non-final face, it can be subdivided into a final face and any number of
non-final ones.  Because a face can be subdivided in many ways, this process
defines a tree of graphs. By construction the leaves must be final graphs,
and they are the plane graphs we are interested in: any plane graph of $n$
faces can be generated in $n-1$ steps by this process, adding one (final)
face at a time. For details see~\cite{Hales:2006:DCG} or
\cite{NipkowBS-IJCAR06}.

The enumeration is parameterized by a natural number $p$ which controls the
maximal size of final faces in the generated graphs. The seed graph
\textit{Seed$_p$} contains two $(p+3)$-gons and the final
face created in each step may at most be a $(p+3)$-gon. As a result,
different parameters lead to disjoint sets of graphs.

The HOL formalization defines an executable function
\textit{next-plane$_p$} that maps a
graph to a list of graphs, the successor graphs reachable by subdividing one
non-final face.  The plane graphs are the final graphs reachable from
\textit{Seed$_p$} via \textit{next-plane$_p$} for some $p$.


\subsection{Enumeration of tame graphs}

The definition of tameness in the original proof is already quite close to a direct logical
formulation. Hence the HOL formalization is very close to this. Of course
pictures of graphs had to be translated into formulae, taking implicit
symmetries in pictures into account. We found one simplification: in the
definition of an admissible weight assignment one can drop condition 3
(a condition on the $4$-circuits in graphs)
without changing the set of tame graphs. What facilitated our work
considerably was that a number of the eight tameness conditions 
in the original proof are directly
executable. The details are described elsewhere~\cite{NipkowBS-IJCAR06}.

The enumeration of tame graphs is a modified enumeration of plane graphs
where we remove final graphs that are definitely not tame, and prune the
search tree at non-final graphs that cannot lead to tame graphs anymore.  
The published
description~\cite{Hales:2006:DCG} is deliberately sketchy, and 
the precise formulation of the pruning criteria is based on the
original Java programs.  This
is the most delicate part of the proof because we need to balance
effectiveness of pruning with simplicity of the completeness proof: weak
pruning criteria are easy to justify but lead to unacceptable run times of
the enumeration, sophisticated pruning techniques are difficult to justify
formally. Since computer-assisted proofs are still very laborious,
simplifying those proofs was of prime importance. In the end, the HOL
formalization defines a function \textit{next-tame$_p$}
from a graph to a graph list. It computes the list of plane successor graphs
\textit{next-plane$_p$ g} and post-processes it as follows:
\begin{enumerate}
\item Remove all graphs from the list that cannot lead to tame graphs
because of lower bound estimates for the total admissible weight of the final
graph.
\item Finalize all triangles in all of the graphs in the list
(because every 3-cycle in a tame graph must be a face).
\item Remove final graphs that are not tame from the list.
\end{enumerate}
A necessary but possibly not sufficient check for tameness is used in the last
step. Hence the enumeration may actually produce non-tame graphs. This is
unproblematic: in the worst case a fake counterexample to the Kepler
conjecture is produced, but we do not miss any real ones.

Although we have roughly followed the procedure of the original proof, we have simplified it in
many places. In particular we removed the special treatment of
\textit{Seed$_0$} and \textit{Seed$_1$}, which is a fairly intricate
optimization that turned out to be unnecessary.

The following completeness theorem is the key result:
\begin{thm}\label{thm:TameEnum_comp}
If a tame and final graph $g$ is reachable from
\textit{Seed$_p$} via \textit{next-plane$_p$}
then $g$ is also reachable from \textit{Seed$_p$} via \textit{next-tame$_p$}.
\end{thm}

Each step \textit{next-tame$_p$} is executable and an exhaustive enumeration
of all graphs reachable from a seed graph is easily defined on top of it. We
call this function \textit{tameEnum$_p$}. By definition, tame graphs may
contain only triangles up to octagons, which corresponds to the parameters $p
= 0,\dots,5$.


\subsection{Archive}

In order to build on the above enumeration of all tame graphs without having
to rerun the enumeration, the results of running \textit{tameEnum$_p$} with
$p = 0,\dots,5$ are put into an Archive and isomorphic graphs are
eliminated. This results in 2771 graphs, as opposed to 5128 in the original proof. The
reasons are twofold: there are many isomorphic copies of graphs in the
Archive and it contains a number of non-tame graphs, partly because, for
efficiency reasons, the original proof did not enforce all tameness conditions in its Java
program. The new reduced Archive is also available
online~\cite{BauerN-AFP06}.

Finally we can prove Theorem~\ref{Archive:complete}: if $g$ is tame plane
graph, Theorem~\ref{thm:TameEnum_comp} and the definition of
\textit{tameEnum} tell us that $g$ must be contained in \textit{tameEnum$_p$}
for some $p=0,\dots,5$. Hence it suffices to enumerate \textit{tameEnum$_p$},
$p=0,\dots,5$, and check that, modulo graph isomorphism, the result is the
same as the Archive. This is a proposition that can be proved by executing it
(because the HOL formalization also includes a verified executable test for
graph isomorphism which we do not discuss).
