---
doc_id: arxiv-1408.3518v3
doc_title: "On Augmentation Algorithms for Linear and Integer-Linear Programming:"
section_id: sec-000-1-introduction
section_title: "Introduction."
section_number: 1
pages: 1-4
source_pdf: 1408.3518v3.pdf
source_sha256: cf18585b886587c7
text_source: latex
latex_prose_ratio: 0.643
latex_coverage_ratio: 0.998
doc_brief: "On Augmentation Algorithms for Linear and Integer-Linear Programming: — 4 sections: Introduction.; Our Contributions; Proofs"
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



\subsection{Our Contributions}

The main contribution of this paper is an extension of Bland's theorem beyond LP to ILP.
Our main results and proofs extend what Bland did for circuits to Graver bases. We look at several  augmentation rules.  
Although they are very similar, our results here are naturally divided into the LP and ILP cases, with small but important 
technical changes. Also, depending on whether variables are restricted to be integers or not, we rely on different sets as the set 
of allowable augmentation directions, which we denote by $\cal T (A)$. The set $\cal T(A)$ will change depending on the case.

In what follows, we will employ $\cal T(A)$ in augmentation algorithms that iteratively replace a feasible (either continuous or integer)
solution $\vex_k$ to $A\vex=\veb$, $\ve 0\leq\vex\leq\veu$, by a better feasible solution $\vex_{k+1}:=\vex_k+\alpha\vez$, where
 $\vecc^\T\vez<0$ and $\alpha>0$. We consider three specific augmentation rules.

\medskip
  \begin{definition}[Discrete Deepest Descent]
    With respect to a feasible solution $\vex_k$, we choose  $\vez$ such that $-\alpha\vecc^\T\vez$ is maximized among all $\vez\in{\cal T}(A)$ and $\alpha>0$ such that $\vex_{k+1} :=\vex_k + \alpha \vez$ is feasible (note that for ILP this means that $\alpha\in\Z$).
  \end{definition}

\medskip

  \begin{definition}[Discrete Dantzig Descent]
    With respect to a feasible solution $\vex_k$, we choose  $\vez$ such that $-\vecc^\T\vez$ is maximized among all $\vez\in\cal T(A)$ such that $\vex_k + \epsilon\vez$ is feasible for some $\epsilon>0$ (note that for LP this means for all sufficiently small $\epsilon>0$, and for ILP this means for $\epsilon=1$). Then we take a maximum augmentation in such a direction. That is, we let $\vex_{k+1} := \vex_k + \alpha \vez$, where $\alpha$ is the largest value for which $\vex_k + \alpha \vez$ is feasible (note that for ILP this means that $\alpha\in\Z$).
  \end{definition}

\medskip

  \begin{definition}[Discrete Steepest Descent]
    With respect to a feasible solution $\vex_k$, we choose  $\vez$ such that $-\vecc^\T\vez/\|\vez\|_1$  is maximized among all $\vez\in\cal T(A)$ such that $\vex_k + \epsilon \vez$ is feasible for some $\epsilon>0$ (note that for LP this means for all sufficiently small $\epsilon>0$, and for ILP this means for $\epsilon=1$). Then we take a maximum augmentation  in such a direction. That is, we let $\vex_{k+1} := \vex_k + \alpha \vez$, where $\alpha$ is the largest value for which $\vex_k + \alpha \vez$ is feasible  (note that for ILP this means that $\alpha\in\Z$).
  \end{definition}

\medskip

Note that all three augmentation rules produce maximal augmentations. Practically speaking, there are more situations in which discrete steepest descent and 
discrete Dantzig descent can be practically implemented, as compared to discrete deepest descent. Still, it is interesting to analyze and contrast these augmentation rules.
We derive the following main results concerning these augmentation rules for the ILP and the LP cases. In some structured situations, these bounds will provide very 
good guarantees of performance. Our ILP theorem is new, while our LP results extend what Bland started early on, and greatly extends the applicability of the 
bounds of Kitahara and Mizuno. 

Next we state the results. Note that in what follows the base of all logarithms is two.

For the discrete deepest-descent rule, in the ILP case a polynomial time bound was first proved, but not explicitly stated as a proposition, in \cite{Hemmecke+Onn+Weismantel:oracle} and in \cite{onn:nonlinear-discrete-monograph} (see top of page 47 (end of proof of Lemma 3.10)).  Here we make it very explicit:

\begin{lemma}[(see also \cite{Hemmecke+Onn+Weismantel:oracle})] \label{ILP-greedy}
The number of discrete deepest-descent augmentations needed to reach an optimal solution from $\vex_0$ is bounded by $(4n-4)\,\log(\vecc^\T (\vex_0-\vex_{\min})).$
\end{lemma}

In addition, for the other two augmentation rules we prove:

\begin{theorem}[ILP case]\label{theorem:main, ILP case}
Let $A\in\Z^{d\times n}$, $\veb\in\Z^d$ and $\vecc\in\Z^n$ define the ILP
\[
\min\set{\,\vecc^\T\vex\ :\ A\vex=\veb,\ \ve 0\leq\vex\leq\veu,\ \vex\in\Z^n\,}.
\]
Let $\vex_0$ be an initial feasible solution, let $\vex_{\min}$ be an optimal solution, and let $\gamma$ be the maximum non-zero 
entry (in absolute value) in any feasible solution. Then we have the following bounds on the number of augmentations to reach an optimal solution from $\vex_0$.
\begin{enumerate}
\medskip
\item[(a)] The number of discrete Dantzig-descent augmentations needed to reach an optimal solution of the ILP is bounded by 
$(4n-4)\gamma \, \log(\vecc^\T (\vex_0-\vex_{\min})).$

\item[(b)] Any discrete steepest-descent direction (which by definition belongs to $\Graver(A)$) is an overall steepest-descent direction (which could be any applicable direction from $\Z^n$). Moreover, the number of discrete steepest-descent augmentations to reach an optimal solution of the given ILP is bounded by $|\Graver(A)|$.
\end{enumerate}
\end{theorem}

Next we present our results for augmentation algorithms in linear programming.
The results for \emph{integer} augmentations arguments in \cite{Hemmecke+Onn+Weismantel:oracle} and in \cite{onn:nonlinear-discrete-monograph} (see top of page 47 (end of proof of Lemma 3.10)) could be adapted to obtain an LP bound too, but the bound one obtains from  \cite{Hemmecke+Onn+Weismantel:oracle}  leads directly to an extra factor of $n$ in the number of augmentations due to the strategy presented there to ensure termination. Our contribution is that we manage to get rid of this factor of $n$:

\begin{lemma} \label{LP-greedy}
 The number of discrete deepest-descent augmentations needed to reach an optimal solution from $\vex_0$ is bounded by $2n\log(\delta\,\vecc^\T (\vex_0-\vex_{\min})).$ 
\end{lemma}

Moreover we prove the following extensions to the other augmentation rules for LPs:

\begin{theorem}[LP case]\label{theorem:main, LP case}
Let $A\in\Z^{d\times n}$, $\veb\in\Z^d$ and $\vecc\in\Z^n$ define the LP
\[
\min\set{\,\vecc^\T\vex\ :\ A\vex=\veb,\ \ve 0\leq\vex\leq\veu,\ \vex\in\R^n\,}.
\]
Let $\vex_0$ be an initial feasible solution, let $\vex_{\min}$ be an optimal solution, let $\gamma$ be the maximum non-zero entry (in absolute value) in any feasible solution, and let $\delta$ denote the least common multiple of all subdeterminants of $A$. Then we have the following bounds on the number of augmentations to 
reach an optimal solution from $\vex_0$.
\begin{enumerate}
\medskip
\item[(a)] The number of discrete Dantzig-descent augmentations needed to reach an optimal solution from $\vex_0$ is no more than
$2n^2\delta\gamma\,\log(\delta\,\vecc^\T (\vex_0-\vex_{\min})).$

\item[(b)] Any discrete steepest-descent direction (which by definition belongs to ${\cal C}(A)$) is an overall steepest-descent direction (which could be any applicable direction from $\R^n$). Moreover, the number of discrete steepest-descent augmentations to reach an optimal solution of the given LP is bounded by $|{\cal C}(A)|$.
\end{enumerate}
\end{theorem}


While by nature LP augmentation algorithms cannot have cycling, as can happen for the simplex method, it should be noted that the LP case of the discrete deepest-descent and the discrete Dantzig-descent augmentation algorithms only guarantee that we reach a feasible solution $\vex_k$ with objective value ``close enough'' to the optimal value. Whether any given feasible solution is ``close enough'' can be checked by generating a vertex of the feasible region with objective value that is at least as good as $\vecc^\T\vex_k$. Finding such a vertex can be done by augmenting $\vex_k$ only along such (discrete deepest-/Dantzig-descent) circuit directions that lead to a better feasible solution with an additional component reaching its lower or upper bound. Geometrically, this corresponds to (iterative) augmentation within the smallest face of the polyhedron $\set{\,\vex\ :\ A\vex=\veb,\ \ve 0\leq\vex\leq\veu,\ \vex\in\R^n\,}$ that contains $\vex_k$. (The circuits of the problem matrix $A$ provide such a restricted optimality certificate). We recommend  the example in \cite{Hemmecke:PSP}. Finally, again using the circuits of $A$, it can be checked whether the vertex found is optimal. The overall closeness-test requires at most $n$ augmentations.

Finally we present the interesting consequences of the main theorems.
Note that the bounds in part (c) of Theorems \ref{theorem:main, ILP case} and \ref{theorem:main, LP case} only depend on $A$, but not on $\veb$, $\vecc$, and the particular initial feasible solution $\vex_0$ chosen. As a direct consequence of Part (b) of Theorem \ref{theorem:main, ILP case}, we obtain the following corollaries.

\begin{corollary} \label{01boxedcase}
  For the pure 0/1 ILP $\min\set{\,\vecc^\T\vex\ : A\vex=\veb,\ {\ve 0}\leq\vex\leq {\ve 1},\ \vex\in\Z^n\,}$ the number of discrete deepest-/Dantzig-/steepest-descent augmentations is bounded by $O(n \log(\|\vecc \|_1))$.
\end{corollary}

We note that in the LP case, the proof of Theorem \ref{theorem:main, LP case}, part (c), immediately gives Bland's
fundamental result:

\begin{corollary}[Bland's Theorem] \label{Corollary: Blands result}
  The number of discrete steepest-descent augmentations needed to solve   $\min\set{\,\vecc^\T\vex:A\vex=\veb, \ve 0\leq\vex\leq\veu, \vex\in\R^n\,}$ is bounded by the number of (different) positive values of $-\vecc^\T \vez/\|\vez\|_1$ over all (elementary vectors) $\vez\in{\cal C}(A)$ times the number $n$ of variables.
\end{corollary}

As for totally-unimodular matrices $A$, ${\cal C}(A)=\Graver(A)$, i.e., they coincide for the LP and ILP cases, the proof of Theorem \ref{theorem:main, LP case}, part (c), also implies:

\begin{corollary}\label{Corollary: TU matrix implies Blands result also for ILP}
  For totally-unimodular matrix $A$, the number of discrete steepest-descent augmentations needed to solve $\min\set{\,\vecc^\T\vex:A\vex=\veb, \ve 0\leq\vex\leq\veu, \vex\in\Z^n\,}$ is bounded by the number of (different) positive values of $-\vecc^\T \vez/\|\vez\|_1$ over all (elementary vectors) $\vez\in{\cal C}(A)$ times the number $n$ of variables.
\end{corollary}

For a totally-unimodular matrix $A$, $\Circuits(A)$ consists only of vectors with (at most $d+1$) entries in $\set{\,-1,0,1\,}$ Thus, for $\vez\in\Circuits(A)$ we have $|-\vecc^\T \vez|\leq\|\vecc\|_1$ and $\|\vez\|_1$ takes on at most $d+1$ different values. Plugging this into Corollary \ref{Corollary: TU matrix implies Blands result also for ILP} we get the following.

\begin{corollary} \label{tunumsteps}
  For totally-unimodular matrix $A$, the number of discrete steepest-descent augmentations needed to solve $\min\set{\,\vecc^\T\vex:A\vex=\veb, \ve 0\leq\vex\leq\veu, \vex\in\Z^n\,}$ is bounded by $n(d+1)\|\vecc\|_1$.
\end{corollary}

From this we immediately recover the complexity bound for the algorithm of Edmonds and Karp to find maximum flows in a network: let $A$ be the node/arc-incidence matrix of a connected directed graph. Note that one row of $A$ is linearly dependent on the other rows and thus can be removed from $A$. Then $n=|E|$ and $d=|V|-1$. As we maximize the flow on a specific (auxiliary) arc (from sink to source), we have $\|\vecc\|_1=1$. Thus, $n(d+1)\|\vecc\|_1=|E|\cdot|V|$ bounds the number of discrete steepest-descent augmentations to solve the max-flow problem. This observation is not  surprising, as the augmentation approach using Graver bases specializes to the algorithm by Edmonds and Karp in the setting of maximum flows.




It is  worth recalling that although the complexity statements in Corollary \ref{01boxedcase} and Corollary \ref{tunumsteps}
depend on the unary size of $\vecc$, these two results actually can be improved based on the results of Frank and Tardos \cite{andras+eva}.
Frank and Tardos used  Diophantine approximation to replace $\vecc$ with a new objective function $\vecc'$ where the integer
numbers occurring in the entries are small but define an equivalent problem with the same optima. Furthermore, the
new weight function $\vecc'$ can be found in strongly polynomial-time. In conclusion, if we are able to generate in polynomial time
the corresponding augmentation elements of the Graver basis according to one of the three rules, we  obtain strongly polynomial-time
algorithms. Of course, this is in general hard to do other than by computing the entire Graver basis, but for special matrices $A$, one can
do much better.

Our results on augmentations for totally-unimodular matrices provide another interesting geometric result. For years, researchers have been looking at the diameter
of the graph of polyhedra (i.e., the graph whose nodes are the vertices of the convex polyhedron $P=\{ \vex :  A\vex=\veb, \ve 0\leq\vex\leq\veu \}$). It has been shown in
\cite{determinants+diameters} that the diameter of the graph of totally-unimodular $d$-dimensional polytopes (i.e., the length of the longest shortest path between a pair of nodes) is bounded above by $d^{3.5}\log(d)$.  
We wish to stress that in our circuit augmentations, we do not always follow edges of the polyhedron $P$. Rather, we may cut through the interior of $P$ or the interior of some faces. This suggests the notion of \emph{circuit diameter}. The circuit distance from $v_1$ to $v_2$  is the smallest number of circuit augmentations needed to go from $v_1$ to $v_2$. We can then define the circuit diameter   as the maximum number of steps along circuit basis directions that are needed to go from any vertex of the polyhedron to any other vertex of the polyhedron. This notion was first introduced and investigated in the article \cite{circuitdiameter}. More recently other  generalizations of the notion of diameter 
using circuits were introduced in  \cite{manycircuitdiameters}. One can show that the circuit diameter of a polyhedron is bounded from above by the usual combinatorial diameter of polyhedra (this is because arcs are themselves  some of the possible augmentation directions, a subset of the circuits). In this context, our results show that one can bound the \emph{circuit diameter} for totally-unimodular polytopes in standard form as follows  


\begin{corollary}
  For a $d \times n$ totally-unimodular matrix $A$, the circuit diameter of the polyhedron $P:=\set{\,\vex :A\vex=\veb, \ve 0\leq\vex\leq\veu}$ is bounded above by $2(n(d+1)(n-d))$.
\end{corollary}

This corollary is a good general bound for totally-unimodular matrices, but we suspect it can be further improved, as we already know that for network-flow polytopes a better bound is possible. Indeed, Orlin \cite{orlin97-networkdiam} designed a polynomial-time primal network-simplex algorithm for the minimum-cost flow problem which gives a graph-diameter bound of $O(|E||V| \log(|V|))$, with $E,V$ equal to the sets of of arcs and nodes in the network. 


\proof{Proof:} To see this, take any vertex $v$ of $P$. Choose a cost vector specific to $v$: namely, let $c_i=1$ if $v_i=0$ and $c_i=-1$ if $v_i=u_i$. Otherwise, put $c_i=0$. Thus, this new objective function $\vecc$ has $n-d$ = $n-rank(A)$ many nonzero entries. Thus, by Corollary \ref{tunumsteps}, with the steepest-descent rule, any other vertex is connected to $v$ with no more than $n(d+1)(n-d)$ many augmentations. Hence,  the path between any pair of vertices of P is bounded by $2n(d+1)(n-d)$. \Halmos
\endproof


Finally, let us consider optimization problems for which the constraint matrix is structured. Recall that an $N$-fold matrix is a matrix of the form
\[
  [A,B]^{(N)}:=\begin{pmatrix}
    B & B & \cdots & B \\
    A & \maO  &   & \maO  \\
    \maO  & A &   & \maO  \\
       &   & \ddots &   \\
    \maO  & \maO  &   & A
  \end{pmatrix}.
\]
For fixed matrices $A$ and $B$, the size of the Graver basis of $[A,B]^{(N)}$ (and its binary encoding length) increases only polynomially with $N$. Combining this with Theorems \ref{theorem:main, ILP case} and \ref{theorem:main, LP case}, parts (c), we obtain the following result.

\begin{theorem}\label{Theorem: N-fold LPs and IPs are strongly poly-time solvable}
  For fixed matrices $A$ and $B$, the associated families of $N$-fold LPs and ILPs can be solved in strongly polynomial time.
\end{theorem}

This generalizes the results from \cite{hemmecke-onn-romanchuk:nfold-cubic,Hemmecke+Onn+Weismantel:oracle}, which showed that for fixed matrices $A$ and $B$, the corresponding $N$-fold ILPs could be solved in time polynomial in $N$, in fact in $O(N^3)$ steps. Theorem \ref {Theorem: N-fold LPs and IPs are strongly poly-time solvable} strengthens this to strong polynomiality. As a direct consequence we obtain the following results:

\begin{corollary} The following special cases of $N$-fold matrices can be solved in strongly polynomial time in the linear and integer case:
  \begin{itemize}
    \item All $2$-way transportation problems with a fixed number of rows or columns.
    \item All $3$-way transportation problems with two of the three dimensions fixed.
    \item All $d$-way transportation problems with $d-1$ dimensions of fixed constant value.
  \end{itemize}
\end{corollary}
