---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-024-84-an-improved-bound-for-steepest-descent-augmen
section_title: "An improved bound for steepest-descent augmentation"
section_number: 8.4
pages: 33-36
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.995
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
\label{sec:steepest-improved}
We now prove Theorem~\ref{thm:steepest-main}.
The proof follows the same lines as that of the Goldberg--Tarjan algorithm; see also \cite[Section 10.5]{amo} for the analysis. A factor $\log n$ improvement over the original bound was given in \cite{Radzik-Goldberg}. A key property in the original analysis is that for a flow around a cycle (i.e., an elementary vector), every edge carries at least $1/|V|$ fraction of the $\ell_1$-norm of the flow. This can be naturally replaced by the argument that for every elementary flow $g$, the minimum nonzero value of $|g_i|$ is at least $\|g\|_1/(1+(m-1)\kappa_A)$. 

The Goldberg--Tarjan algorithm has been generalized to separable convex minimization with linear constraints by Karzanov and McCormick \cite{Karzanov97}. Instead of $\Le_W$, they use the maximum entry in a Graver basis (see Section~\ref{sec:graver} below). Lemma 10.1 in their paper proves a weakly polynomial bound similar to Lemma~\ref{lem:weakly-poly} for the separable convex setting. However, no strongly polynomial analysis is given (which is in general not possible for the nonlinear setting).

\medskip

Our arguments will be based on the dual of \ref{LP-augment}:
\begin{equation}
\label{LP-augment-dual}
  \begin{aligned}
  \max \;  \pr{y}{b}-&\pr{u}{t} \\
  A^\top y + s-t &= c \\
  s,t & \geq 0\,. \\
  \end{aligned}
\end{equation}
Recall the primal-dual slackness conditions from Section~\ref{sec:hoffman}: if  $x$ is feasible to \ref{LP-augment} and $y\in\R^m$, they  are primal and dual optimal solutions if and only if $\pr{a_i}{y}\le c_i$ if $x_i<u_i$ and $\pr{a_i}{y}\ge c_i$ if $x_i>0$.

Let us start by formulating the steepest-descent direction as an LP. 
Let ${\bar A}=(A|-A)\in \R^{m\times (2n)}$ and $\bar c=\binom{c}{-c}\in \R^{2n}$. Clearly, $\Le_{\bar A}=\Le_A$.
For a feasible solution $x=x^{(t)}$ to \ref{LP-augment}, we define 
\emph{residual variable set} 
\[
N(x)=\{i\in [n]: x_i<u_i\}\cup \{n+j: j\in [n]: x_j>0\}\subseteq [2n]\, ,
\]
and consider  the system
\begin{equation}
\label{eq:minratio-primal}
\begin{aligned}
\min \; & \pr{\bar c}{z} \\ 
\bar A z&=0 \\
\pr{\1_{2n}}{z}&=1\\
z_{[2n] \setminus N(x)} &= 0\\
z&\ge 0\,.\\
\end{aligned}
\end{equation}
We can map a solution $z\in \R^{2n}$ to $g\in \R^n$ by setting $g_i=z_i-z_{n+i}$.
We will assume that $z$ is chosen as a basic optimal solution.
Observe that every basic feasible solution to this program maps to an elementary vector in $\ker(\bar A)$.
The dual program can be equivalently written as 
\begin{equation}
\label{eq:minratio-dual}
\begin{aligned}
\min \; & \varepsilon \\ 
\pr{\bar a_i}{y}&\le \bar c_i +\varepsilon \quad\forall i\in N(x)\,.
\end{aligned}
\end{equation}

For the solution $x$, we let $\varepsilon(x)$ denote the optimal solution to this dual problem; thus, the optimal solution to the primal is $-\varepsilon(x)$. 
If $\varepsilon=0$, then $x$ and $y$ are complementary primal and dual optimal solutions to \ref{LP-augment}. We first show that this quantity is monotone (a key step also in the analysis in \cite{DHL15}).

\begin{lemma}\label{lem:epsilon-mon} At every iteration of the circuit augmentation algorithm, $\varepsilon(x^{(t+1)})\le \varepsilon(x^{(t)})$.
\end{lemma}
\begin{proof}
Let $\varepsilon=\varepsilon(x^{(t)})$ and let $y$ be an optimal solution to \eqref{eq:minratio-dual} for $N(x^{(t)})$. We show that the same $y$ is also feasible for $N(x^{(t+1)})$; the claim follows immediately.  There is nothing to prove if $N(x^{(t+1)})\subseteq N(x^{(t)})$, so let $i\in N(x^{(t+1)})\setminus  N(x^{(t)})$.

Assume first $i\in [n+1,2n]$; let $i=n+j$. This means that $x^{(t)}_j=0<x_j^{(t+1)}$; therefore,  the augmenting direction $g$ has $g_{j}>0$. Thus, for the optimal solution $z$ to  \eqref{eq:minratio-primal}, we must have $z_j>0$. By primal-dual slackness, $\pr{a_j}{y}=c_j+\varepsilon$; thus, 
\[
\pr{\bar a_i}{y}=\pr{-a_j}{y}=-c_j-\varepsilon<-c_j=\bar c_j\, .
\]
The case $i\in [n]$ is analogous.
\end{proof}

The next lemma shows that within every $n$ iterations, $\varepsilon(x^{(t)})$ decreases by a factor depending on $\kappa_A$.
\begin{lemma}\label{lem:weakly-poly} For every iteration $t$, $\varepsilon(x^{(t+n)})\le \left(1-\frac{1}{1+(m-1)\kappa_A}\right) \varepsilon(x^{(t)})$.
\end{lemma}
\begin{proof}
Let us set $N=N(x^{(t)})$, $\varepsilon=\varepsilon(x^{(t)})$, and let $y=y^{(t)}$ be an optimal dual solution to \eqref{eq:minratio-dual} for $x^{(t)}$.
 Let 
 \[
 T := \{i \in N: \pr{\bar a_i}{y} > \bar c_i \} \subseteq [2n]\, ;
 \]
  that is, if $i\in [n]$ then $\pr{a_i}{y}>c_i$, and if $i\in [n+1,2n]$, $i=n+j$, then  $\pr{a_j}{y}<c_j$.  In particular, $|T\cap\{i,i+n\}|\le 1$ for every $i\in [n]$.
 Let $z^{(t)}$ be the basic optimal solution to \eqref{eq:minratio-primal} for $x^{(t)}$.
By complementary slackness, every $i\in \supp(z^{(t)})$ must have   $\pr{\bar a_i}{y}=\bar c_i+\varepsilon$, and thus,
 $\supp(z^{(t)})\subseteq T$.

\begin{claim}
Let us pick $k>t$ as the first iteration when for the basic optimal solution  $z^{(k)}$ to \eqref{eq:minratio-primal}, we have $\supp(z^{(k)})\setminus T\neq \emptyset$.
Then $k\le t+n$, and 
the solution $(y,\varepsilon)$ is still feasible for \eqref{eq:minratio-dual} for $x^{(k)}$.
\end{claim}
\begin{proof}
For $r\in[t,k-1]$, 
let  $T^{(r)}=T\cap N(x^{(r)})$. We show that $T^{(r+1)}\subsetneq T^{(r)}$. Since $|T|\le n$, this implies $k\le t+n$.
Let $z^{(r)}$ be the basic optimal solution  for \eqref{eq:minratio-primal}; recall that the augmenting direction is computed with $g_j=z^{(r)}_j-z^{(r)}_{n+j}$. By the choice of $k$, $\supp(z^{(r)})\subseteq T^{(r)}$. Thus, 
 we may only increase $x_i$ for $i\in T\cap [n]$ and decrease it for $i=j-n$ for $j\in T\cap [n+1,2n]$. Consequently, every index $i$ entering $N(x^{(r+1)})$ has $\pr{\bar a_i}{y}<\bar c_i$, and therefore $(y,\varepsilon)$ remains feasible throughout.

We now turn to the proof of $T^{(r+1)}\subsetneq T^{(r)}$.
Since we use a maximal augmentation, at least one index leaves $T^{(r)}$ at each iteration. We claim that $T^{(r+1)}\setminus T^{(r)}=\emptyset$. For a contradiction, assume  there exists $i\in T^{(r+1)}\setminus T^{(r)}$. If $i\in [n]$, then
$i+n$ must be in the support of $z^{(r)}$; in particular, $i+n\in T^{(r)}$. But this would mean that $\{i,i+n\}\subseteq T$, in contradiction with the definition of $T$. Similarly, for $i\in [n+1,2n]$.
\end{proof}

Let us now consider the optimal solution  $z=z^{(k)}$ to \eqref{eq:minratio-primal} at iteration $k$; by the above claim, $(y,\varepsilon)$ is still a feasible dual solution. Select an index  $j\in \supp(z)\setminus T$.
\[
\pr{-\bar c}{z}=\pr{\bar A^\top y - \bar c} z \le \varepsilon \sum_{i\in \supp(z)\setminus \{j\}} z_i = (1-z_j)  \varepsilon \le 
\left(1-\frac{1}{1+(m-1)\kappa_A}\right) \varepsilon\, .
\]
In the first inequality, we use that $\pr{\bar a_i}{y} - \bar c_i \le \varepsilon$ by the feasibility of $(y,\varepsilon)$, and $\pr{\bar a_j}{y} - \bar c_j \le 0$ by the choice of $j\notin T$. In the second equality, we use 
the constraint $\sum_i z_i=1$. The final inequality uses that
 $z$ is a basic solution, and therefore, an elementary vector in $\ker(\bar A)$. In particular $|\supp(z)|\le m$, and $z_i\le \kappa_{\bar A} z_j= \kappa_{A} z_j$. Consequently, $z_j\ge 1/(1+(m-1)\kappa_A)$.
\end{proof}

We say that the variable $j\in [2n]$ is \emph{frozen} at iteration $t$, if $j\notin N(x^{(t')})$ for any $t'\ge t$. Thus, for $j\in [n]$, $x_j=u_j$, and for $j\in [n+1,2n]$, $j=i+n$, $x_i=0$ for all subsequent iterations. We show that a new frozen variable can be found in every $O(nm\kappa_A\log(m\kappa_A))$ iterations; this implies
Theorem~\ref{thm:steepest-main}.

\begin{lemma}
For every iteration $t\ge 1$, there is a variable $j\in  N(x^{(t)})$ that is frozen at iteration $k$ for $k=t+O(nm\kappa_A\log(\kappa_A+n))$.
\end{lemma}
\begin{proof}
Let $\varepsilon=\varepsilon(x^{(t)})$. By Lemma~\ref{lem:weakly-poly}, we can choose $k=t+O(nm\kappa_A\log(n+\kappa_A))$ such that $\varepsilon'=\varepsilon(x^{(k)})<\varepsilon/(2n(\kappa_A+1))$.
Consider the primal and dual optimal solutions $(z,y,\varepsilon)$ to \eqref{eq:minratio-primal} and \eqref{eq:minratio-dual}  at iteration $t$ and $(z',y',\varepsilon')$ at iteration $k$. 

\begin{claim}\label{cl:largeindex} There exists a $j\in \supp(z)$ such that $\pr{\bar a_j}{y'}>\bar c_j + 2n(\kappa_A+1)\varepsilon'$. 
\end{claim}
\begin{proof}
For a contradiction, assume that $\pr{\bar a_j}{y'}-\bar c_j\le 2n(\kappa_A+1)\varepsilon'$ for every $j\in \supp(z)$.
 Then,
\[
\varepsilon= \pr{\bar c}{z}=\pr{\bar A^\top y -\bar c}{z} \le 2n(\kappa_A+1)\varepsilon'\sum_j z_j= 2n(\kappa_A+1)\varepsilon'\, , 
\]
contradicting the choice of $\varepsilon'$.
\end{proof}
We now show that all such indices are frozen at iteration $k$ by making use of Theorem~\ref{thm:primal-fixing-upper} on proximity. 
Let $x'=x^{(k)}$ and $x''=x^{(k'')}$ for any $k''>k$; let $(y'',\varepsilon'')$ be optimal to  \eqref{eq:minratio-dual} at iteration $k''$; we have $\varepsilon''\le\varepsilon'$ by Lemma~\ref{lem:epsilon-mon}.

Let us define the cost $c'\in\R^{n}$ by 
\[
c'_i:=\begin{cases}
\pr{\bar a_i}{y'}&\mbox{ if }0<x'_i<u_i\, \\
\max\{c_i, \pr{\bar a_i}{y'}\}&\mbox{ if }x'_i=u_i\, \\ 
\min\{c_i, \pr{\bar a_i}{y'}\}&\mbox{ if }x'_i=0\,.
\end{cases}
\]
If we replace the cost $c$ by $c'$, then  $x'$ and $y'$ satisfy complementary slackness, and hence are optimal to \ref{LP-augment} and \eqref{LP-augment-dual}. Moreover, the optimality of $(y',\varepsilon')$ to \eqref{eq:minratio-dual} guarantees that $\|c'-c\|_\infty\le \varepsilon'$.

We similarly construct $c''$ for $y''$, and note that $x''$ and $y''$ are primal and dual optimal solutions for the costs $c''$, $\|c''-c\|_\infty\le \varepsilon''$.  Further,
\[
\|c'-c''\|_1\le n\|c'-c''\|_\infty\le n\left(\|c'-c\|_\infty+\|c''-c\|_\infty\right)\le n(\varepsilon'+\varepsilon'')\le 2n\varepsilon'
\]
We thus apply Theorem~\ref{thm:primal-fixing-upper} for $(x',y')$ for $c'$ and $(x'',y'')$ for $c''$, showing that every variable $j$ as in Claim~\ref{cl:largeindex} must be frozen.
\end{proof}
