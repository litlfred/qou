---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-015-71-a-black-box-algorithm
section_title: "A black box algorithm"
section_number: 7.1
pages: 25-26
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.988
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
\label{sec:black-box}
The LP feasibility and optimization algorithms in \cite{DadushNV20} rely on a black-box subroutine for approximate LP solutions, and use their outputs to find exact primal (and dual) optimal solutions in time $\poly(m,n,\log (\bar \Le_A+n))$. For the black-box, one can use the fast interior-point algorithms cited above.

More precisely, we require  the following approximately feasible and optimal solution $\tilde x$ to \ref{LP-subspace-f} in time $\mathrm{poly}(n,m)\log((\bar\kappa_A + n)/\varepsilon)\big)$.
Here $\operatorname{OPT}_{\mathrm{LP}}$ denotes the objective value of \ref{LP-subspace-f}.
\begin{equation}
  \label{sys:near_feas_near_opt}
  \tag{\texttt{APX-LP}}
  \begin{aligned}
  \pr{c}{\tilde x} &\le \operatorname{OPT}_{\mathrm{LP}}+ \varepsilon \|c\|\cdot\|d\| \\ 
  \tilde x &\in W + d \\
  \|\tilde x^-\| &\le \varepsilon \|d\|\,\\
  \tilde x &\in \R^n 
  \end{aligned}
\end{equation}
The feasibility algorithm makes $O(m)$ calls, and the optimization algorithm makes $O(nm)$ calls to such a subroutine for $\varepsilon=1/(\bar\kappa_A + n)^{O(1)}$.

We now give a high-level outline of the feasibility algorithm in \cite{DadushNV20} for the system $x\in W+d$, $x\ge 0$. For the description, let us assume this system is feasible; in case of infeasibility, the algorithm recovers a Farkas-certificate.
The main progress step in the algorithm is reducing the dimension $m$ of the linear space $W$ by one,
based on information obtained form  an approximate solution  $\tilde x$  to \eqref{sys:near_feas_near_opt}. We can make such an inference using the proximity result Lemma~\ref{lem:feas}. 

If $\tilde x\ge 0$ for the solution returned by the solver, we can terminate with $x=\tilde x$. 
Otherwise, let $I \subseteq [n]$ denote the set of `large' coordinates of $\tilde x$, i.e., where $\tilde x_i>\kappa_W\|\tilde x^-\|_1$. By Lemma~\ref{lem:feas}, there must exist a feasible solution $x\in W+d$, $x\ge 0$ such that $x_i$ is still sufficiently large for $i\in I$.
Therefore,
 one can drop the sign-constraint on $I$, as non-negativity can be enforced automatically. We recurse on $\pi_J(W)$ for $J=[n]\setminus I$, i.e. project out the variables in $I$.

Each recursive call decreases the dimension of the subspace, until a feasible vector is found. The feasible solution on the remaining variables now has to be \emph{lifted} to the variables we projected out, to get a feasible solution to the original problem $x\in W + d$, $x\ge 0$. We use the \emph{lifting operator} $L_J^W(p)$ introduced in Section~\ref{subsec:lifting_operator}: for $p\in \pi_J(W)$, $z=L_J^W(p)$ is the minimum-norm vector in $W$ such that $z_J=p$.
According to Proposition~\ref{lem:kappa-lift}, $\|z\|_\infty\le \kappa_W\|p\|_1$; this bound can be used to guarantee that the lifted solution is nonnegative on $I$.

Algorithm~\ref{alg:feas} gives a simplified description of the 
feasibility algorithm of \cite{DadushNV20}. For simplicity, we ignore the infeasibility case and the details of the $\texttt{Adjust}(d)$ that may replace $d$ by it projection to $W^\perp$ in certain cases. This is needed to ensure $I\neq\emptyset$. Further, we omit an additional proximity condition from the approximate system \ref{sys:near_feas_near_opt}.

\begin{algorithm}[htb!]
  \caption{\texttt{Feasibility-Simplified}}
  \label{alg:feas}
  \SetKwInOut{Input}{Input}
  \SetKwInOut{Output}{Output}
  \SetKwComment{Comment}{$\triangleright$\ }{}
  \SetKw{And}{\textbf{and}}
  \Input{Instance of \ref{LP-subspace-f}, $\eps > 0$, with $c = 0_n$.}
  \Output{Feasible solution to the system in Lemma~\ref{lem:feas}}
   $d \gets \texttt{Adjust}(d)$ \Comment*{Occasionally applies a projection}
    \lIf{$d \in W$}{
      \Return{ $0_n$}
    }
    $\tilde x \gets \ref{sys:near_feas_near_opt}(W,d,0_n, \eps)$  \Comment*{Provided by Black box solver}
    $I \gets \{i : \tilde x_i \ge \kappa_W \|\tilde x^-\| \}, J \gets [n] \setminus I$,\;
    $z \gets \texttt{Feasibility-Simplified}(\pi_J(W), d_J, \eps)$\;
    \Return{$\begin{bmatrix} \tilde x_I + [L_J^W(z - \tilde x_J)]_I \\ z \end{bmatrix}$} \label{line:return}
\end{algorithm}

As stated here, the computation complexity is dominated by the at most $m$ recursive calls to the solver for the system \eqref{sys:near_feas_near_opt}.

In  \cite{DadushNV20}, these techniques are also extended to solve the minimum-cost problem \ref{LP-subspace-f} for arbitrary cost vector $c \in \R^n$. The  optimization algorithm  makes $O(m)$ recursive calls to the approximate solver to identify a variable $x_i$ that must be 0 in every optimal solution; this is deduced 
 using Theorem~\ref{cor:dual-fix-weak}.
