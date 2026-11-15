---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05"
section_id: sec-016-61-background-on-association-schemes
section_title: "Background on association schemes"
section_number: 6.1
pages: 42-44
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.962
doc_brief: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05 — Stein’s method is used to prove limit theorems for random character ratios."
---
\label{rtassoc}

	This subsection gives preliminaries about association
	schemes, using notation from \cite{MS}. Another useful
	reference is \cite{BI}, and what we call association schemes
	some authors call symmetric association schemes.

	{\bf Definition}. An association scheme with $n$ classes
	consists of a finite set $X$ with $n+1$
	relations $R_0,\cdots,R_n$ defined on $X$ which satisfy:

\begin{enumerate}
\item Each $R_i$ is symmetric: $(x,y) \in R_i \Rightarrow (y,x) \in R_i$.
\item For every $x,y \in X$, one has that $(x,y) \in R_i$ for exactly one $i$.
\item $R_0=\{(x,x):x \in X\}$ is the identity relation.
\item If $(x,y) \in R_k$, the number of $z \in X$ such that $(x,z) \in R_i$ and $(y,z) \in R_j$ is a constant $c_{ijk}$ depending on $i,j,k$ but not on the particular choice of $x$ and $y$. 
\end{enumerate}

	The adjacency matrix $D_i$ corresponding to the relation $R_i$
	is the $|X| \times |X|$ matrix with rows and columns labeled
	by the points of $X$ defined by \[ (D_i)_{x,y} = \left\{
	\begin{array}{ll} 1 & \mbox{if $(x,y) \in R_i$}\\ 0 &
	\mbox{otherwise.} \end{array} \right.\] The Bose-Melner
	algebra is defined to be the vector space consisting of all
	matrices $\sum_{i=0}^n a_i D_i$ with $a_i$ real. Since the
	matrices in the Bose-Melner algebra are symmetric and commute
	with each other (by parts 1 and 4 of the definition of an
	association scheme), the Bose-Melner algebra is semisimple and
	has a distinguished basis of primitive idempotents
	$J_0,\cdots,J_n$ satisfying \begin{enumerate} \item
	$J_i^2=J_i$ \ \ \ $i=0,\cdots,n$.  \item $J_i J_k=0$ \ \ \ $i
	\neq k$.  \item $\sum_{i=0}^n J_i = I.$ \end{enumerate} Here I
	is the identity matrix.

 	The $D$'s are also a basis of the Bose-Melner algebra, so one
	can write \[ D_s = \sum_{i=0}^n \phi_s(i) J_i, \ \ \ s = 0,
	\cdots,n\] where the $\phi_s(i)$ are real numbers. Since $D_s
	J_i = \phi_s(i) J_i$, the $\phi_s(i)$ are the eigenvalues of
	$D_s$. For later use note that since $D_0$
	and $\sum_{i=0}^n J_i$ are both the identity matrix,
	$\phi_0(j)=1$ for all $j$.

	 Let $\mu_i$ be the rank of $J_i$. For all $s$, this is the
	multiplicity of the eigenvalue $\phi_s(i)$ of $D_s$. We define
	the Plancherel measure of the association scheme to be the
	probability measure on $\{0,\cdots,n \}$ which chooses $i$
	with probability $\frac{\mu_i}{|X|}$.
	
	Lemmas \ref{asorthog1} and \ref{asorthog2} are the
	orthogonality relations for eigenvalues of association
	schemes. To state them it is helpful to define
	$v_i=c_{ii0}$, so that for any $x$, one has that $v_i$ is the
	number of pairs $(x,y) \in R_i$. Clearly $\sum_{i=0}^n v_i =
	|X|$.


\begin{lemma}
 \label{asorthog1} (\cite{MS}, page 655) For $0 \leq k,l \leq n$, \[
 \sum_{r=0}^n \frac{\phi_r(k) \phi_r(l)}{v_r} = \frac{|X|}{\mu_k}
 \delta_{k,l}.\]
\end{lemma}

\begin{lemma} \label{asorthog2} (\cite{MS}, page 655)  For $0 \leq k,l \leq n$, \[ \sum_{i=0}^n \mu_i \phi_k(i) \phi_l(i) = |X| v_k \delta_{k,l}.\]
\end{lemma}

	Lemma \ref{ascountsol} will be crucial.

\begin{lemma}
 \label{ascountsol} The coefficient of $D_l$ in $D_{s_1} \cdots
 D_{s_m}$ is equal to \[ \frac{1}{v_l} \sum_{i=0}^n \frac{\mu_i}{|X|} \phi_{s_1}(i)
 \cdots \phi_{s_m}(i) \phi_l(i).\] In particular, the coefficient of $D_l$ in
 $(D_s)^m$ is \[ \frac{1}{v_l} \ee[ \phi_s(i)^m \phi_l(i)], \] where $s$ is
 random from Plancherel measure of the association scheme.
\end{lemma}

\begin{proof} Since $D_s = \sum_{i=0}^n \phi_s(i) J_i$, one knows that \[ D_{s_1} \cdots D_{s_m} = \sum_{i=0}^n \phi_{s_1}(i) \cdots \phi_{s_m}(i) J_i.\] By pages 654 and 655 of \cite{MS}, \[ J_i = \frac{1}{|X|} \sum_{l=0}^n \frac{\mu_i \phi_l(i)}{v_l} D_l.\] The result follows. \end{proof}

	Let $p_m(r)$ denote $\frac{v_r}{(v_s)^m}$ multiplied by the
	coefficient of $D_r$ in $(D_s)^m$. It follows from the
	definitions that $p_m(r)$ admits the following probabilistic
	interpretation. Start from some point $x_0 \in X$, move to a
	random $x_1 \in X$ such that $(x_0,x_1) \in R_s$, then to a
	random $x_2 \in X$ such that $(x_1,x_2) \in R_s$, and so on
	until one obtains $x_m$. Then $p_m(r)$ is the probability that
	$(x_0,x_m) \in R_r$.

	The following fact will be useful.

\begin{lemma} \label{asrel}
\begin{enumerate}
\item $p_4(0) = \sum_{r=0}^n \frac{p_2(r)^2}{v_r}$.
\item $p_3(s) = v_s  \sum_{r=0}^n \frac{p_2(r)^2}{v_r}$. 
\end{enumerate}
\end{lemma}

\begin{proof} The first assertion is clear from the probabilistic interpretation of
$p_m(r)$. For an analytic proof, note that by Lemma \ref{ascountsol} (in
the first and fourth equalities) and Lemma \ref{asorthog1} (in the
second and third equalities) \begin{eqnarray*} \sum_{r=0}^n
\frac{p_2(r)^2}{v_r} & = & \sum_{r=0}^n \frac{1}{v_r}
\left( \frac{1}{(v_s)^2} \sum_{i=0}^n \frac{\mu_i}{|X|} \phi_s(i)^2 \phi_r(i) \right)^2\\
& = & \frac{1}{(v_s)^4} \sum_{r=0}^n \frac{1}{v_r} \sum_{i=0}^n \frac{(\mu_i)^2}{|X|^2}
\phi_s(i)^4 \phi_r(i)^2\\ & = & \frac{1}{(v_s)^4} \sum_{i=0}^n \frac{\mu_i}{|X|}
\phi_s(i)^4 \\ & = & p_4(0). \end{eqnarray*}

	The second assertion follows from the first assertion since
$p_3(s)=v_s p_4(0)$, as can be seen either by the probabilistic
interpretation of $p_m(r)$ or by computing both sides of the equation
using Lemma \ref{ascountsol}. \end{proof}
