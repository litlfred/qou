---
doc_id: arxiv-1408.3518v3
doc_title: "On Augmentation Algorithms for Linear and Integer-Linear Programming:"
section_id: sec-002-2-proofs
section_title: "Proofs"
section_number: 2
pages: 8-13
source_pdf: 1408.3518v3.pdf
source_sha256: cf18585b886587c7
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.992
doc_brief: "On Augmentation Algorithms for Linear and Integer-Linear Programming: — 4 sections: Introduction.; Our Contributions; Proofs"
---
We present the proofs to the above results in separate subsections. We will use the following  lemma (a slight variation from Theorem 3.1 in \cite{Ahuja+Magnanti+Orlin}) which  establishes the bounds we claim once we can guarantee sufficient improvement at each iteration:
\begin{lemma}
\label{Lemma: Sufficient improvement leads to polynomial algorithm}

Let $\epsilon>0$ be given. Moreover, let $H$ denote the difference between maximum and minimum objective-function values of the LP/ILP problem in $n$ variables.
Suppose that $f^k=\vecc^\T \vex_k$ is the objective-function value of the solution $\vex_k$ at the $k$-th iteration of an algorithm and that $f^*=\vecc^\T \vex_{\min}$ is the minimum objective-function value. Furthermore, suppose that the algorithm guarantees that for every augmentation $k$,
\[
(f^k-f^{k+1})\geq\beta(f^k-f^*)
\]
(i.e., the improvement at augmentation $k+1$ is at least $\beta$ times the maximum possible improvement). Then the algorithm reaches a solution with $f^k-f^*<\epsilon$ in no more than $2 \log{(H/\epsilon)}/\beta$ augmentations.
\end{lemma}

\proof{Proof:} Without loss of generality, we assume that $\vecc$ is an integer vector. (Thus for the ILP version the values $f^k$ are decreasing successive integer values.) The biggest necessary change of value of the objective function occurs when we start the augmentation at an maximum point $\vex_{\max}$ and end with some minimum optimal point $\vex_{\min}$. Thus, we have $H=f^{\max}-f^{\min}$.

If we had at every augmentation an improvement of at least $\beta (f^{\max}-f^{\min})/2$, then
in no more than $2/\beta$ augmentations we would have reached the optimum. But if this improvement is not achieved at each augmentation, say at the $q$-th augmentation we have $f^q-f^{q+1} \leq \beta (f^{\max}-f^{\min})/2$ then, together with the hypothesis $(f^q-f^{q+1})\geq\beta(f^q-f^{\min})$, we get that
\[
  f^q-f^{\min} \leq (f^{\max}-f^{\min})/2=H/2.
\]
In other words, the overall improvement reached so far is at least half of the maximum possible improvement $H$.
In conclusion, after $2/\beta$ augmentations, we have either reached the optimum or have at least divided the possible gap by $2$. Therefore in no more than $2/\beta \log_2{(H/\epsilon)}$ augmentations we reach a solution with $f^k-f^*<\epsilon$. \Halmos
\endproof

It is important to note that in the ILP case $f^k$ is integer, and we can apply Lemma \ref{Lemma: Sufficient improvement leads to polynomial algorithm} with $\epsilon=1$ and conclude that we can reach the optimum in $O(\log{(H)}/\beta)$ augmentations. In the LP case, let $\delta$ denote the least common multiple of all subdeterminants of $A$. Observe that once we find a feasible solution $\vex_k$ with objective value $f^k$ satisfying $f^k-f^*<\epsilon=1/\delta$, then any vertex with an objective value of at most $f^k$ must be optimal. As explained above (right before the statement of Theorem \ref{theorem:main, ILP case}), such a vertex can be found from $\vex_k$ in at most $n$ additional augmentations. This leads to extra factors of $n$ and of $\log(\delta)$ in the bounds for the LP cases compared to the ILP cases.


\subsection{Proof of Lemma \ref{ILP-greedy} and Theorem \ref{theorem:main, ILP case}}

Let us assume that $\vex_k$ is a non-optimal feasible solution, and let $\vex_{\min}$ be an optimal solution to the ILP. Then there exists a (sign-compatible) representation
\[
  \vex_{\min} -  \vex_k =\sum\alpha_i\veg_i,
\]
with $\alpha_i>0$, $\alpha_i\in\Z$ and with $\alpha_i\veg_i\red \vex_{\min} - \vex_k$. Moreover, due to Seb\"o's result \cite{Sebo90}, at most $2n-2$ summands are needed.

Note that sign-compatibility of the representation $\vex_{\min}-\vex_k =\sum\alpha_i\veg_i$ implies that for all $i$ the vectors $\vex_{k}+\alpha_i\veg_i$ and $\vex_{\min}-\alpha_i\veg_i$ are all feasible solutions, since their components lie between the components of $\vex_k$ and of $\vex_{\min}$. Moreover, we can observe that for all such sign-compatible representations $\vex_{\min}-\vex_k =\sum\alpha_i\veg_i$ we must have $\vecc^\T\veg_i\leq 0$ for all $i$, as otherwise $\vex_{\min}-\alpha_i\veg_i$ would be a feasible solution with $\vecc^\T (\vex_{\min}-\alpha_i\veg_i)=\vecc^\T\vex_{\min}-\alpha_i\vecc^\T\veg_i<\vecc^\T\vex_{\min}$, contradicting the minimality of $\vex_{\min}$.

Next, we analyze what happens for each choice of augmentation rule:

\subsubsection{Proof of Lemma \ref{ILP-greedy}: Discrete deepest descent.} We observe that
\[
  0>\vecc^\T (\vex_{\min}-\vex_k)
   =\vecc^\T \sum\alpha_i\veg_i
   = \sum\alpha_i\vecc^\T\veg_i
   \geq -(2n-2)\Delta
\]
where $\Delta>0$ is the largest value of $-\alpha\vecc^\T\vez$ over all $\vez\in\Graver(A)$ and integer $\alpha>0$ for which $\vex_k+\alpha\vez$ is feasible. Rewriting this, we get
\[
  \Delta\geq\frac{\vecc^\T (\vex_k-\vex_{\min})}{2n-2}.

\]
Now let $\alpha\vez$ be the discrete deepest-descent augmentation applied to $\vex_k$, leading to $\vex_{k+1}:=\vex_k+\alpha\vez$. Then we get $\Delta=-\alpha\vecc^\T\vez$ and
\[
  \vecc^\T (\vex_k-\vex_{k+1})=-\alpha\vecc^\T\vez=\Delta
  \geq\frac{\vecc^\T (\vex_k-\vex_{\min})}{2n-2}.
\]
Thus, we have a factor of $\beta=1/(2n-2)$ of objective-function decrease at each augmentation, leading to the desired polynomial number of augmentations via Lemma \ref{Lemma: Sufficient improvement leads to polynomial algorithm} taking $\epsilon=1$.
In this case, we get the number of augmentations bounded by $(4n-4)\,\,\log(\vecc^\T (\vex_0-\vex_{\min})))$.

\subsubsection{Proof of part (a) of Theorem \ref{theorem:main, ILP case}: Discrete Dantzig descent.} We observe that
\[
  0>\vecc^\T (\vex_{\min}-\vex_k)
   =\vecc^\T \sum\alpha_i\veg_i
   = \sum\alpha_i\vecc^\T\veg_i
   \geq - \Delta_0 \sum\alpha_i
   \geq -(2n-2)\Delta_0 \alpha_{\max},
\]
where this time $\Delta_0>0$ denotes the greatest value of $-\vecc^\T\vez$ over all $\vez\in\Graver(A)$ for which $\vex_k+\vez$ is still feasible and where $\alpha_{\max}=\max\set{\, \alpha_i\, }$. Rewriting this, we get
\[
  \Delta_0 \geq\frac{\vecc^\T (\vex_k-\vex_{\min})}{(2n-2) \alpha_{\max}}.
\]
Now let $\alpha\vez$ be the discrete Dantzig-descent augmentation  applied to $\vex_k$, leading to $\vex_{k+1}:=\vex_k+\alpha\vez$. Then we get
\[
  \vecc^\T (\vex_k-\vex_{k+1})=-\alpha\vecc^\T\vez=\alpha\Delta_0\geq\Delta_0
  \geq\frac{\vecc^\T (\vex_k-\vex_{\min})}{(2n-2) \alpha_{\max}}
  \geq \frac{\vecc^\T (\vex_0-\vex_{\min})}{(2n-2)\gamma},
\]
where $\gamma$ is the maximum entry in any feasible integer solution (or, equivalently, in any vertex of $P_I$). Thus, we have a factor of $\beta=1/((2n-2) \gamma)$ of objective-function decrease at each augmentation leading to the desired polynomial number of augmentations via Lemma \ref{Lemma: Sufficient improvement leads to polynomial algorithm} taking $\epsilon=1$. In this case we get the number of augmentations bounded by  $(4n-4)\,\gamma \, \log(\vecc^\T (\vex_0-\vex_{\min})))$



























\subsubsection{Proof of part (b) of of Theorem \ref{theorem:main, ILP case}: Discrete steepest descent.}

We begin with a series of lemmas. Note that the proof for the LP case follows exactly the same lines, since we do not use integrality of the components in our arguments.

\begin{lemma}\label{Lemma: Steepest descent direction is in G(A)}
  Let $\vex_k$ be a feasible solution, and let $\vez$ be an associated  steepest \-descent direction. Then there is some augmentation direction $\veg\in\Graver(A)$ from $\vex_k$, with $-\vecc^\T\veg / \|\veg\|_1 \geq -\vecc^\T\vez/\|\vez\|_1$.
\end{lemma}

\proof{Proof.}
  There is a sign-compatible representation $\vez=\sum\alpha_i\veg_i$  via elements $\veg_i\in\Graver(A)$. Observe that due to the sign-compatible representation, $\vex_k+\alpha_i\veg_i$ is also feasible for all $i$. (The components of $\vex_k+\alpha_i\veg_i$ lie between those of $\vex_k$ and $\vex_k+\vez$, implying that $\ve 0\leq\vex_k+\alpha_i\veg_i\leq\veu$.) In other words, all $\alpha_i\veg_i$ are applicable augmentations at $\vex_k$.

  It remains for us to show that there exists some index $i$ with $-\vecc^\T\veg_i/\|\veg_i\|_1\geq-\vecc^\T\vez/\|\vez\|_1$. Assume to the contrary that we have $-\vecc^\T\veg_i/\|\veg_i\|_1 < -\vecc^\T\vez/\|\vez\|_1$ for all $i$. This yields
  \begin{eqnarray*}
    -\vecc^\T\vez & = &- \sum\alpha_i\vecc^\T\veg_i\\
    & = & \sum\alpha_i\|\veg_i\|_1\frac{-\vecc^\T\veg_i}{\|\veg_i\|_1}\\[5pt]
    & < & \sum\alpha_i\|\veg_i\|_1\frac{-\vecc^\T\vez}{\|\vez\|_1}\\[5pt]
    & = & \frac{-\vecc^\T\vez}{\|\vez\|_1}\ \sum\alpha_i\|\veg_i\|_1\\[5pt]
    & = & \frac{-\vecc^\T\vez}{\|\vez\|_1}\ \|\vez\|_1\\[5pt]
    & = & -\vecc^\T\vez,
  \end{eqnarray*}
  a contradiction.
 \Halmos
\endproof

Lemma \ref{Lemma: Steepest descent direction is in G(A)} states that among all steepest-descent directions applicable at a feasible solution $\vex_k$, there is always one in $\Graver(A)$. Or in other words, the discrete steepest-descent rule is a steepest descent rule as claimed in Theorems \ref{theorem:main, ILP case} and \ref{theorem:main, LP case}, parts(c).


\begin{lemma}\label{Lemma: monotonicity}
  Let $\vex_k$ be a feasible solution, let $\alpha\ves$ be a steepest-descent augmentation relative to $\vex_k$, and let $\vex_{k+1}:=\vex_k + \alpha\ves$.
  Let  $\beta\vet$ be a steepest-descent augmentation relative to $\vex_{k+1}$.
  Then we have $-\vecc^\T\ves/\|\ves\|_1\geq -\vecc^\T\vet/\|\vet\|_1$.
\end{lemma}

\proof{Proof.}
  Suppose on the contrary that $-\vecc^\T\ves/\|\ves\|_1 < -\vecc^\T\vet/\|\vet\|_1$.
  First observe that $\alpha\ves+\beta\vet$ is an applicable augmentation at $\vex_k$. Moreover, we have
  \begin{eqnarray*}
    -\vecc^\T(\alpha\ves+\beta\vet) & = & \alpha\|\ves\|_1\frac{-\vecc^\T\ves}{\|\ves\|_1}+\beta\|\vet\|_1\frac{-\vecc^\T\vet}{\|\vet\|_1}\\[5pt]
    & > & \alpha\|\ves\|_1\frac{-\vecc^\T\ves}{\|\ves\|_1}+\beta\|\vet\|_1\frac{-\vecc^\T\ves}{\|\ves\|_1}\\[5pt]
    & = & (\alpha\|\ves\|_1+\beta\|\vet\|_1)\frac{-\vecc^\T\ves}{\|\ves\|_1},\\[5pt]
    & \geq & (\|\alpha\ves+\beta\vet\|_1)\frac{-\vecc^\T\ves}{\|\ves\|_1},
  \end{eqnarray*}
  and therefore
  \[
    \frac{-\vecc^\T(\alpha\ves+\beta\vet)}{\|\alpha\ves+\beta\vet\|_1}>\frac{-\vecc^\T\ves}{\|\ves\|_1}.
  \]
  This contradicts the fact that $\ves$ was a steepest descent direction for $\vex_k$.
 \Halmos
\endproof

Lemma \ref{Lemma: monotonicity} states that the steepness of steepest-descent augmentations never  increases.

\begin{lemma}\label{Lemma: chance of sign-pattern leads to change in slope}
  Let $\vex_k$ be a feasible solution and let $\alpha_1\vez_1,\ldots,\alpha_j\vez_j$ be the following steepest-descent augmentations applied to $\vex_k$. If $\vez_1$ and $\vez_j$ do not have the same sign-pattern from $\set{\,\leq 0,\geq 0\,}^n$, then we have $-\vecc^\T\vez_1/\|\vez_1\|_1>-\vecc^\T\vez_j/\|\vez_j\|_1$.
\end{lemma}

\proof{Proof.}
  Assume on the contrary that $-\vecc^\T\vez_1/\|\vez_1\|_1 \leq -\vecc^\T\vez_j/\|\vez_j\|_1$. By monotonicity, Lemma \ref{Lemma: monotonicity}, we must have $\frac{-\vecc^\T\vez_1}{\|\vez_1\|_1}=\frac{-\vecc^\T\vez_2}{\|\vez_2\|_1}=\dots=\frac{-\vecc^\T\vez_j}{\|\vez_j\|_1}$. We conclude that
  \begin{eqnarray*}
    -\vecc^\T\textstyle\left(\sum_{i=1}^j\alpha_i\vez_i\right) & = & \textstyle\sum_{i=1}^j\alpha_i\|\vez_i\|_1\frac{-\vecc^\T\vez_i}{\|\vez_i\|_1}\\
    & = & \textstyle\sum_{i=1}^j\alpha_i\|\vez_i\|_1\frac{-\vecc^\T\vez_1}{\|\vez_1\|_1}\\
    & = & \textstyle\left(\sum_{i=1}^j\alpha_i\|\vez_i\|_1\right)\frac{-\vecc^\T\vez_1}{\|\vez_1\|_1}\\
    & > & \textstyle\left\|\sum_{i=1}^j\alpha_i\vez_i\right\|_1\frac{-\vecc^\T\vez_1}{\|\vez_1\|_1},
  \end{eqnarray*}
  since $\vez_1$ and $\vez_j$ do not have the same sign-pattern. This implies that
  \[
    \frac{-\vecc^\T\textstyle\left(\sum_{i=1}^j\alpha_i\vez_i\right)}{\|\sum_{i=1}^j\alpha_i\vez_i\|_1}>\frac{-\vecc^\T\vez_1}{\|\vez_1\|_1}.
  \]
  As by assumption $\sum_{i=1}^j\alpha_i\vez_i$ is an applicable augmentation at $\vex_k$. This contradicts the fact that $\vez_1$ was a steepest-descent augmentation for $\vex_k$.
 \Halmos
\endproof
Lemma \ref{Lemma: chance of sign-pattern leads to change in slope} states that once the sign pattern
of a steepest-descent augmentation strictly changes, the steepness must decrease.
This lemma has a surprising consequence if we only apply steepest-descent directions from $\Graver(A)$:

\begin{corollary}\label{Corollary: number of augmentations bounded by size of Graver basis}
For discrete steepest descent, no direction from $\Graver(A)$ is chosen twice as an augmenting direction. Therefore, the number of steepest-descent augmentations needed to reach an optimal solution is bounded by $|\Graver(A)|$ and thus is independent of $\veb$, $\vecc$ and the initial solution $\vez_0$.
\end{corollary}

\proof{Proof.}
  Let $\vex_k$ be a feasible solution and let $\alpha_1\vez_1,\ldots,\alpha_j\vez_j$, with $\vez_1,\ldots,\vez_j\in\Graver(A)$, be the following steepest-descent augmentations applied to $\vex_k$ with $\alpha_i$ chosen maximally in each augmentation. Moreover assume that $\vez_j=\vez_1$. Then, by Lemma \ref{Lemma: chance of sign-pattern leads to change in slope}, all intermediate augmentations must have the same sign-pattern as $\vez_1$, as otherwise the steepness of the augmentations would have dropped. As all vectors $\alpha_1\vez_1,\ldots,\alpha_j\vez_j$ have the same sign-pattern, the components of $\vex_k+\alpha_1\vez_1+\alpha_j\vez_j$ lie between the components of $\vex_k$ and $\vex_k+\sum_{i=1}^j\alpha_i\vez_i$ and therefore also between $\ve 0$ and $\veu$. Thus, $\vex_k+\alpha_1\vez_1+\alpha_k\vez_j=\vex_k+(\alpha_1+\alpha_j)\vez_1$ is a feasible solution. This contradicts the fact that $\alpha_1$ was chosen maximally.
 \Halmos
\endproof



\subsection{Proof of Lemma \ref{LP-greedy} and Theorem \ref{theorem:main, LP case}}

Let us assume that $\vex_k$ is a non-optimal feasible solution, and let $\vex_{\min}$ be an optimal solution to the LP. Then there exists a (sign-compatible) representation
\[
  \vex_{\min} -  \vex_k =\sum\alpha_i\veg_i,
\]
with $\alpha_i>0$ and with $\alpha_i\veg_i\red \vex_{\min} - \vex_k$. Moreover, due to Carath\'eodory theorem, at most $n$ summands are needed in such a representation.
Again, sign-compatibility of the representation $\vex_{\min}-\vex_k =\sum\alpha_i\veg_i$ implies that for all $i$ the vectors $\vex_{k}+\alpha_i\veg_i$ and $\vex_{\min}-\alpha_i\veg_i$ are all feasible solutions.

Let us now analyze what happens for each choice of augmentation rule:

\subsubsection{Proof of Lemma \ref{LP-greedy} for Discrete deepest descent.} We observe that
\[
  0>\vecc^\T (\vex_{\min}-\vex_k)
   =\vecc^\T \sum\alpha_i\veg_i
   = \sum\alpha_i\vecc^\T\veg_i
   \geq -n\Delta
\]
where $\Delta>0$ is the largest value of $-\alpha\vecc^\T\vez$ over all $\vez\in\Circuits(A)$ and $\alpha>0$ for which $\vex_k+\alpha\vez$ is feasible. Rewriting this, we get
\[
  \Delta\geq\frac{\vecc^\T (\vex_k-\vex_{\min})}n.
\]
Now let $\alpha\vez$ be the discrete deepest-descent augmentation applied to $\vex_k$, leading to $\vex_{k+1}:=\vex_k+\alpha\vez$. Then we get $\Delta=-\alpha\vecc^\T\vez$ and
\[
  \vecc^\T (\vex_k-\vex_{k+1})=-\alpha\vecc^\T\vez=\Delta
  \geq\frac{\vecc^\T (\vex_k-\vex_{\min})}n.
\]
Thus, we have a factor of $\beta=1/n$ of objective-function value decrease at each augmentation. Applying Lemma \ref{Lemma: Sufficient improvement leads to polynomial algorithm} with $\epsilon=1/\delta$ then yields a solution $\bar\vex$ with $|\vecc^\T(\bar\vex-\vex_{\min})|<1/\delta$ within $2n\,\log(\delta\,\vecc^\T (\vex_0-\vex_{\min})))$ many augmentations. Due to the definition of $\delta$ as the least common multiple of all subdeterminants of $A$, any vertex with an objective value of at most $\vecc^\T\bar\vex$ must be optimal. As explained right before the statement of Theorem \ref{theorem:main, ILP case}, such a vertex can be found from $\bar\vex$ in at most $n$ additional augmentations. Finally, note that once the discrete deepest-descent augmentation makes progress in objective value less than $\epsilon/(2n-2)$, we have
\[
  |\vecc^\T(\vex_k-\vex_{\min})|=\sum|\alpha_i\vecc^\T\veg_i| <(2n-2)\cdot\epsilon/(2n-2)=\epsilon.
\]
Hence, we can decide effectively when we should stop making discrete deepest-descent augmentations and should rather find a nearby vertex.



\subsubsection{Proof of part (a) of Theorem \ref{theorem:main, LP case}: Discrete Dantzig descent.}  In order to avoid zig-zagging (see example in Section 4 of \cite{Hemmecke:PSP} and the details of
how to avoid this), we must  augment to a vertex with lower objective-function value after each discrete Dantzig-descent augmentation. For this, we need at most $n$ discrete Dantzig-descent augmentations within smaller and smaller faces of $P$. Let $\vex_k$ be a vertex of the given polyhedron. Again we observe that
\[
  0>\vecc^\T (\vex_{\min}-\vex_k)
   =\vecc^\T \sum\alpha_i\veg_i
   = \sum\alpha_i\vecc^\T\veg_i
   \geq - \Delta_0 \sum\alpha_i
   \geq -n\Delta \alpha_{\max},
\]
where $\Delta_0>0$ is the greatest value of $-\vecc^\T\vez$ over all $\vez\in\Circuits(A)$ for which $\vex_k+\lambda\vez$ is feasible for sufficiently small $\lambda>0$ and where $\alpha_{\max}=\max\set{\, \alpha_i\, }$. Rewriting this, we get
\[
  \Delta_0 \geq\frac{\vecc^\T (\vex_k-\vex_{\min})}{n\alpha_{\max}}.
\]
Now, let $\alpha\vez$ be the discrete Dantzig-descent augmentation applied to $\vex_k$, leading to $\vex_{k+1}:=\vex_k+\alpha\vez$. As $\vex_k$ is a vertex and $\vez$ an edge direction, we have $\vex_k,\vez\in\frac{1}{\delta}\Z^n$. As $\vex_{k+1}$ is lies on the intersection of the half-line $\set{\,\vex=\vex_k+\lambda\vez:\lambda\geq 0\,}$ with some facet of the polyhedron, we get that $\vex_{k+1}\in\frac{1}{\delta^2}\Z^n$. Consequently, $\alpha\geq 1/\delta$.

Thus, we get
\[
  \vecc^\T (\vex_k-\vex_{k+1})=-\alpha\vecc^\T\vez=\alpha\Delta_0\geq\frac{1}{\delta}\Delta_0
  \geq\frac{\vecc^\T (\vex_k-\vex_{\min})}{n\delta \alpha_{\max}}
  \geq \frac{\vecc^\T (\vex_0-\vex_{\min})}{n\delta\gamma},
\]
where $\gamma$ is the maximum entry in any feasible solution (or, equivalently, in any vertex). Thus, we have a factor of $\beta=1/(n\delta\gamma)$ of objective-function decrease at each augmentation.
Applying Lemma \ref{Lemma: Sufficient improvement leads to polynomial algorithm} with $\epsilon=1/\delta$ then yields the desired bound on the number of augmentations $2n^2\delta\gamma\,\log(\delta\,\vecc^\T (\vex_0-\vex_{\min})))$ to reach a vertex $\bar\vex$ with $|\vecc^\T(\bar\vex-\vex_{\min})|<1/\delta$. This vertex must be optimal.


\subsubsection{Proof of part (b) of Theorem \ref{theorem:main, LP case}: Discrete steepest descent.}

The proof here follows exactly the same lines of the proof to Theorem \ref{theorem:main, ILP case}, part (c).

\subsection{Proof of Theorem \ref{Theorem: N-fold LPs and IPs are strongly poly-time solvable}.}

If we keep $A$ and $B$ fixed and let $N$ vary, the binary encoding lengths of the Graver bases of $[A,B]^{(N)}$ are bounded by a polynomial in $N$, see \cite{DeLoera+Hemmecke+Onn+Weismantel:08}. More precisely, there is a constant $g(A,B)$, the so-called \emph{Graver complexity} of $A$ and $B$ (see \cite{Hosten+Sullivant,Santos+Sturmfels,Berstein+Onn:09}), given by
\[
  \max\set{\,\|\veg\|_1:\veg\in\Graver(B\Graver(A))\,},
\]
such that
\[ \left|\Graver\left([A,B]^{(N)}\right)\right|\leq\binom{N}{g(A,B)}\left|\Graver\left([A,B]^{(g(A,B))}\right)\right|\in O\left(N^{g(A,B)}\right).
\]
This means that we can find a steepest-descent direction in $\Graver\left([A,B]^{(N)}\right)$ in time polynomial in $N$ and by Theorems \ref{theorem:main, ILP case} and \ref{theorem:main, LP case}, parts (c), the number of steepest-descent augmentations to pass from any feasible solution $\vex_0$ to an optimal solution is bounded polynomially in $N$. As the input of an $N$-fold LP/ILP contains $\Theta(N)$ integer numbers (to encode $\veb$ and $\vecc$), we can augment $\vex_0$ to optimality in strongly polynomial-time. It remains for us to show how we can find such a feasible solution $\vex_0$ in strongly polynomial-time. Note that by a shift of coordinates, we may assume without loss of generality that $\vel=\ve 0$.

To find such a feasible solution $\vex_0$, consider the extended $N$-fold LP/ILP with problem matrix
{\small
  \[
    \left(\begin{array}{cccccccccccccccc}
      B & \maO    & \maO     & I_{d_B} & -I_{d_B} & B & \maO    & \maO     & I_{d_B} & -I_{d_B} & \cdots & B & \maO    & \maO     & I_{d_B} & -I_{d_B} \\
      A & I_{d_A} & -I_{d_A} & \maO    & \maO     &   &         &          &         &          &        &   &         &          &         &          \\
        &         &          &         &          & A & I_{d_A} & -I_{d_A} & \maO    & \maO     &        &   &         &          &         &          \\
        &         &          &         &          &   &         &          &         &          & \ddots &   &         &          &         &      \\
        &         &          &         &          &   &         &          &         &          &        & A & I_{d_A} & -I_{d_A} & \maO    & \maO
    \end{array}\right).
  \]
}

\noindent This is an $N$-fold matrix composed using the matrices $\bar{A}=\begin{pmatrix}A&I_{d_A}&-I_{d_A}&\maO&\maO\end{pmatrix}$ and $\bar{B}=\begin{pmatrix}B&\maO&\maO&I_{d_B}&-I_{d_B}\end{pmatrix}$. As the right-hand side of our LP/ILP, we choose the same right-hand side vector $\veb$, and as objective vector we use a $0/1$-vector with zeros in the original components and with ones in the auxiliary components. All variables get lower bounds of $0$, and the original variables get upper bounds specified by $\veu$. Due to the special form of the matrix, we can immediately write down a feasible solution to this problem. (Simply assign zeros to the original variables and set the auxiliary slack variables according to the positive and negative parts of the right-hand side values.)

  Optimizing this special linear objective function can now be done in strongly polynomial-time, since  $\bar{A}$ and $\bar{B}$ are constant the running time of this auxiliary $N$-fold LP/ILP is bounded polynomially in $N$, but does not depend on the right-hand side or the objective vector. If the optimal value of this auxiliary LP/ILP is $0$, a feasible solution to our original problem has been found (simply drop the auxiliary components). If the optimal value is positive, our original problem is infeasible.
\Halmos
\endproof
