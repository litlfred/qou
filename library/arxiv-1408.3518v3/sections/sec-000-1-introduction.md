---
doc_id: arxiv-1408.3518v3
doc_title: "On Augmentation Algorithms for Linear and Integer-Linear Programming: From Edmonds-Karp to Bland and Beyond"
section_id: sec-000-1-introduction
section_title: "Introduction."
section_number: 1
pages: 1-4
source_pdf: 1408.3518v3.pdf
source_sha256: cf18585b886587c7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.998
doc_brief: "On Augmentation Algorithms for Linear and Integer-Linear Programming: From Edmonds-Karp to Bland and Beyond — 13 sections: Front matter; Introduction.; Our Contributions"
---
We consider a general framework for solving linear programs (LPs) and integer-linear programs (ILPs) of the form
\begin{equation} \label{themilp}
  \min\set{\,\vecc^\T\vex\ :\ A\vex=\veb,\ \ve 0\leq\vex\leq\veu,\ \vex\in X\,},
\end{equation}
where $A\in\Z^{d\times n}$, $\veb\in\Z^d$, $\vecc\in\Z^n$, and where $X=\R^n$ (LP) or $X=\Z^n$ (ILP). We focus on solution algorithms that are based on an \emph{augmentation procedure}. At each iteration, we have a current feasible point $\vex_k$. An \emph{augmentation direction} $\vez$ has $\vex_k + \alpha\vez$ feasible for some $\alpha>0$ (which implies that
$\vez$ is in the kernel of $A$) and has $\vecc^\T \vez < 0$.
Together, the \emph{augmentation} is $\alpha\vez$, and we pass to the next
feasible solution  $\vex_{k+1}:=\vex_k + \alpha\vez$.
We note the trivial fact that $\vecc^\T \vex_{k+1} < \vecc^\T \vex_{k}$.
In this way, an augmentation procedure produces
a sequence of feasible solutions $\vex_1$, $\vex_2$, $\ldots$
that are successive improvements on the value of the objective function,
until an optimal solution is reached. Finally, an augmentation $\alpha\vez$ is \emph{maximal} if,
considering $\vex_k$ and $\vez$ to be fixed,
$\alpha$ is the largest value of $t>0$ for which  $\vex_{k+1}:=\vex_k + t\vez$ is feasible.
If the augmentation is maximal, $\vex_{k+1}$ is the best
point on the intersection of the feasible region with
the half-line $\{ \vex_k + t\vez ~:~ t >0\}$. In what follows, we give upper bounds on the number of maximal augmentations required to reached an optimum, for
both the LP and ILP cases.


Of course, augmentation algorithms are nothing new, and one of the best-known in the family is the classical  simplex algorithm. 
For the case of LP, the simplex method is indeed an augmentation algorithm, where
we start at a vertex of the polyhedron that is the feasible region,
and the augmentation used at each iteration corresponds to an available edge direction at the current vertex.
Of course, in the degenerate case, there can be considerable work to calculate an improving edge direction.
Nonetheless, by limiting augmentation directions to available edge directions at the current vertex, and always choosing maximal
augmentations, we insure that the next feasible solution is also a vertex, and so the simplex algorithm can continue.
Similarly, the idea of augmentation has played a very important historical role in the algorithmic theory of network flows; in particular, there is the seminal and very well-known work of  Edmonds and Karp (see \cite{edmondskarp}). They showed that for maximum-flow (essentially the same problem as maximizing the flow on a single arc of a flow-conservative network, subject to simple bounds on the other arcs), the number of augmentations (taken by the classic Ford-Fulkerson augmentation algorithm)
is bounded by the number of arcs times the number of vertices, or slightly more crudely by the number of arcs squared,
\emph{when augmentations are always chosen to have the fewest number of arcs, and the augmentation is maximal.}
In unpublished work, R. Bland (\cite{blandFlorida}) extended this, rather elegantly, to general LPs. Besides not being published
by Bland in the 1970's, it is not well known even today. The result was implicitly alluded to in print in 1987 (see \cite{BixMarTr}), and mentioned more concretely in J. Lee's 1986 dissertation \cite{LeeCornell} (see Proposition 3.1 in the follow-on publication \cite{LeeLAA}). Bland himself made a concrete statement of it (still without proof) in 1992  (see \cite{blandjensen}):



\begin{quotation}
\it
``It was prompted by another result in the same Edmonds-Karp paper \cite{edmondskarp}, that if one always augments on a shortest augmenting
path, the number of augmentations in the Ford-Fulkerson maximum flow algorithm
is less than the product of the numbers of nodes and edges. Fulkerson \cite{fulk}  had
investigated the extent to which fundamental properties of networks generalize to
broader classes of linear programming problems, where elementary vectors in the
appropriate subspaces play the roles of circuits and cocircuits (minimal cutsets).
Bland's dissertation \cite{blandthesis} carried this further, and in later work he showed how the
Edmonds-Karp result generalizes to arbitrary linear programming problems of the
form
{\rm
\begin{eqnarray}
&&\mbox{maximize }  x_0 \nonumber \\
&&\mbox{subject to } A\vex =\ve 0, \label{blandlp}\\
&&\vel\leq \vex \leq \veu. \nonumber
\end{eqnarray}
}
Here the bound on the number of augmentations is the number of variables times
the number of different lengths of normalized elementary vectors; in particular if
$A$ is totally unimodular the bound is the product of the dimensions of $A$, as in the
max flow result of Edmonds and Karp, where $A$ is the (totally unimodular) node-edge
matrix of a directed graph. This seemed to be amusing, but without any obvious
use, until late in 1978 when Paul Seymour \cite{seymour} proved his remarkable decomposition
theorem for unimodular matroids. Bland and Edmonds \cite{blandedmonds} used Seymour's theorem
to show how shortest augmentations could be computed in polynomial time when
the constraint matrix $A$ is totally unimodular. Cost scaling was used to extend the
approach to a polynomial-time primal algorithm for totally unimodular linear programming problems
{\rm
\begin{eqnarray*}
&&\mbox{maximize }  \vea^\T\vex  \\
&&\mbox{subject to } A\vex =\veb, \\
&&\vel\leq \vex \leq \veu.
\end{eqnarray*}
}
which are solved as a sequence of subproblems of the form (\ref{blandlp}). More recently
Tardos \cite{Tardos} has given strongly polynomial algorithms for totally unimodular linear
programming problems, and still more general classes of combinatorial optimization
problems, using cost scaling in a far more clever way.''
\end{quotation}


Today, progress on the augmentation approach to LP continues: new families of augmentation algorithms for
LP include those proposed in \cite{cardosoclimaco} (and rediscovered in \cite{baraszvempala}). Very recently, 
the work of Kern, Faigle, and Peis \cite{peis} rekindled our interest in Bland's result as they, among other things, rediscovered it. Additionally,  Kitahara and Mizuno  \cite{kitaharamizuno} gave an upper bound for  the number of different basic-feasible solutions generated by the simplex method. Their results are direct generalizations of Y. Ye's work \cite{yye}.




On the other hand, the study of augmentation algorithms for ILPs goes back at least to the 1970's and was part of the study of 
``test sets'' (see \cite{Graver:75,Scarf:97, SchulzWeismantel99} and the references therein).  More recently 
there have been important developments. In \cite{SW2002} the authors show that one can solve every integer-linear programming problem in polynomial time provided one can efficiently solve a  special \emph{directed-augmentation problem} (the directed-augmentation problem differs from the ordinary augmentation problem by splitting each direction into its positive and negative parts and considering linear objectives on each of these parts). These authors showed that if one can solve the directed-augmentation problem in polynomial time, then the original problem can be solved by a polynomial-time algorithm. Their main application is to specific combinatorial-optimization problems, such as the min-cost flow problem. Later \cite{Hemmecke+Onn+Weismantel:oracle} showed that if a ``best-improving'' augmentation $\vez$ in the ``Graver basis'' of the constraint matrix is chosen (the authors of \cite{Hemmecke+Onn+Weismantel:oracle} called this augmentation rule  ``greedy improvement''; here we will call this ``deepest descent''), only polynomially-many augmentations (in the binary encoding length of the input data) must be performed in order to reach the optimal value. The paper \cite{Hemmecke+Onn+Weismantel:oracle} shows how to efficiently use an augmentation algorithm for separable convex objective functions and implicitly provided bounds like those presented here.




The set of possible augmentation directions we use depends on the type of problem:
for the LP case, we use as the set of possible augmentation directions the \emph{circuits} of $A$. $\Circuits(A)$ consists of the normalized \emph{elementary vectors} (or \emph{circuits}) associated with $\ker(A)\setminus\set{\,\ve 0\,}$ (see \cite{rocka}) --- that is, the vectors having (set-wise)  minimal support in $\ker(A)\setminus\set{\,\ve 0\,}$. The set of elementary vectors of $\ker(A)\setminus\set{\,\ve 0\,}$ is a finite set of lines through the origin, with the origin excluded. Usually, it is convenient to normalize in an arbitrary manner, so that $\Circuits(A)$ comprises a single point and its negative from each such line. In our context, Bland's normalization uses the objective function so that $\vecc^\T \vez=-1$ for every augmentation direction --- in his terms, such a $\vez$ is \emph{unit augmenting}. For the vectors in $\Circuits(A)$, we choose on each line the (nonzero) integer point closest to the origin and its negative as the normalized representatives.

For the IP case, the set of possible augmentation directions is  the \emph{Graver basis} of $A$, denoted by $\Graver(A)$. We obtain Graver's original finite set  of $\red$-minimal elements in $\ker(A)\cap\Z^n\setminus\set{\,\ve 0\,}$, where $\veu\red\vev$ if and only if $u^{(i)}v^{(i)}\geq 0$ and $|u^{(i)}|\leq|v^{(i)}|$ (see \cite{Graver:75}).
In general, $\Graver(A)$ has a nice sign-compatible representation property: every (integer vector) $\vez\in\ker(A)$ can be written as $\vez=\sum \alpha_i\veg_i$, with $\veg_i\in\Graver(A)$, $\alpha_i>0$, $\alpha_i\in\Z$, and $\alpha_i\veg_i\red\vez$, for all $i$, and the sum involves at most $2n-2$ terms.
 In fact, $\Graver(A)$ is an inclusion-minimal set with this property. It should be noted that due to the sign-compatible representation we have
\[
  \|\vez\|_1=\sum\alpha_i\|\veg_i\|_1,
\]
where $\|\cdot\|_1$ is the usual 1-norm.

We remark that the all circuits are members of the Graver basis. But they also provide an elegant sign-compatible representation 
\emph{over the reals} for all non-zero elements of $\ker(A)$. Specifically, every vector $\vez\in\ker(A)$ can be written as 
$\vez=\sum \alpha_i\veg_i$, with $\veg_i\in{\cal C}(A)$, $\alpha_i\geq0$, $\alpha_i\in\R$, and the sum involves at most $n$ terms. Note that the
(worst-case) number of summands is smaller than in the general Graver decomposition. It is worth remarking that Graver bases can also be defined 
for the general mixed-integer case (see \cite[Section 3.3]{Hemmecke:PSP}) --- but in the mixed-integer setting, the Graver basis is not generally finite, 
in sharp contrast to the LP and ILP cases; so we do not consider that situation here as, unlike the LP and ILP cases, it requires the existence of some 
kind of specialized oracle to generate the augmentations one by one. For an introduction to Graver bases and the latest on augmentation algorithms for integer
programming see the books \cite{DHKbook} and \cite{onn:nonlinear-discrete-monograph}.
