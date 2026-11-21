---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-013-6-hoffman-proximity-theorems
section_title: "Hoffman proximity theorems"
section_number: 6
pages: 22-24
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.988
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
\label{sec:hoffman}

Hoffman's seminal work \cite{Hoffman52} has analyzed proximity of LP solutions. Given $P=\{x\in \R^n:\, Ax\le b\}$, $x_0\in \R^n$, and norms $\|.\|_\alpha$ and $\|.\|_\beta$, we are interested in the minimum of 
$\|x-x_0\|_\alpha$ over $x\in P$.
Hoffman showed that this can be bounded as $H_{\alpha,\beta}(A)\|(Ax_0-b)^+\|_\beta$, where the Lipschitz-bound $H_{\alpha,\beta}(A)$ is a constant that only depends on $A$ and the norms. Such results are known as \emph{Hoffman proximity bounds} in the literature and have been extensively studied;  we refer the reader to \cite{Guler1995,Klatte1995,Pena2020} for references. In particular, they are related to  $\delta$ studied in Section~\ref{sec:delta}, see e.g. 
\cite{Guler1995}. 

In this section, we show a Hoffman-bound $H_{\infty,1}=\kappa_W$ for the system $x\in W+d,\, x\ge 0$, namely. Related bounds using $\bar\chi_A$ have been shown in \cite{ho2002}. We then extend it to proximity results on optimal LP solutions. These will be used in the black-box LP algorithms in Section~\ref{sec:black-box}, as well as for the improved analysis of the steepest descent circuit augmentation algorithm in Section~\ref{sec:steepest-improved}.

A central tool in this section are conformal decompositions into circuits as in Lemma~\ref{lem:sign-cons}. The next proof is similar to that of Proposition~\ref{lem:kappa-lift}.

\begin{lemma}\label{lem:feas}
 If the system $x\in W+d,\, x\ge 0$ 
   is feasible, then the system
  \begin{align*} 
  x&\in W+d\\
  \|x-d\|_\infty&\le \kappa_W \|d^-\|_1\\
  x&\ge 0,
  \end{align*}
  is also feasible.
  \end{lemma}
\begin{proof} 
Let $x$ be a solution to \ref{LP-subspace-f} such that $\|x-d\|_\infty$ is minimal, and subject to that, $\|x-d\|_1$ is minimal. Let $D=\{i\in [n]:\, d_i<0=x_i\}$.

  Take a conformal circuit decomposition of the  vector $x - d \in W$ as in Lemma~\ref{lem:sign-cons} in the form $x-d = \sum_{k = 1}^t g^k$ for some $t \in [n]$. We claim that $\supp(g^k)\cap D\neq \emptyset$ for all $k\in [t]$. Indeed, if $\supp(g^k)\cap D=\emptyset$, then $x'=x-\varepsilon g^k$ for some $\varepsilon>0$ is another solution with $\|x'-d\|_\infty\le \|x-d\|_\infty$ and $\|x'-d\|_1< \|x-d\|_1$.

Consider any index $i\notin D$. For every elementary vector $g^k$ with $i\in \supp(g^k)$, there exists an index $j\in D$ such that $|g^k_i|\le \Le_W |g_j^k|$. By conformity, 
\[
|x_i-d_i|=\left|\sum_{k=1}^t g^k_i\right|=\sum_{k=1}^t \left|g^k_i\right|\le\Le_W \sum_{j\in D} \sum_{k=1}^t\left|g^k_j\right|=\Le_W\sum_{j\in D} |d_j|\le \Le_W\|d^-\|_1\, ,
\]
completing the proof.
\end{proof}

We note that  \cite{DadushNV20} also provides a strongly polynomial algorithm that, for a given $z\in W+d$, and an estimate $\hat \Le$ on $\Le_W$, either finds a solution as in Lemma~\ref{lem:feas}, or finds an elementary vector that reveals $\hat \Le>\Le_W$.

We next provide proximity results for optimization.
For vectors $d,c\in \R^n$, let us define the set
\begin{equation}\label{theta-def}
\Lambda(d,c):=\supp(d^-)\cup \supp(c^+)\, .
\end{equation}
 Note that for $c\ge 0$,
$\left\|d_{\Lambda(d,c)}\right\|_1=\left\|d^-\right\|_1 +\left\|d_{\supp(c)}^+\right\|_1$.
Consequently, if $c\ge 0$ and $d_{\Lambda(d,c)}=0$, then $x=d$ and $s=c$ are optimal primal and dual solutions to \ref{LP-subspace-f}.

\begin{lemma}\label{lem:opt}
  If the system \ref{LP-subspace-f} is feasible, bounded and $c\ge 0$, then there is an optimal solution such that 
  \[
  \left\|x-d\right\|_\infty\le \Le_W \left\|d_{\Lambda(d,c)}\right\|_1. \]
  \end{lemma}
  \begin{proof}
Similarly to the proof of Lemma~\ref{lem:feas}, let $x$ be an optimal solution to \ref{LP-subspace-f} chosen such  that $\|x-d\|_\infty$ is minimal, and subject to that, $\|x-d\|_1$ is minimal; let $D=\{i\in [n]:\, d_i<0=x_i\}$. Take a conformal circuit decomposition $x-d = \sum_{i = 1}^t g^k$ for some $t \in [n]$. 
    With a similar argument as in the proof of Lemma~\ref{lem:feas}, we can show that for each $g^k$, either $\supp(g^k)\cap D\neq\emptyset$, or $g^k$ is an objective-reducing circuit, i.e. $\pr{g^k}{c} < 0$. Since $c\ge 0$, the latter requires that for some $i\in\supp(g^k)$, $g^k_i<0$ and $c_i>0$, implying $i\in d_{\supp(c)}^+$. A similar bound as in the proof of Lemma~\ref{lem:feas} completes the proof.
      \end{proof}
  

\begin{lemma}\label{lem:primal_prox}
  Let $W\subseteq \R^n$ be a subspace and $c, d \in \R^n$.
  Let $(\tilde x, s)$ be an optimal solution to
   LP$(W,\tilde x,c)$. Then there exists an optimal solution $(x^*, s^*)$ to LP$(W,d,c)$ such that
  \[
      \|x^* - \tilde x\|_\infty \le (\kappa_W + 1)\left\|\proj_{W^\perp}(d-\tilde x)\right\|_1 \, .
   \]
  \end{lemma}
  \begin{proof}
  Let $x=\tilde x + \proj_{W^\perp}(d - \tilde x)$. Note that $W+x=W+d$, and also $W^\perp+s=W^\perp+c$. Thus, the systems
    LP$(W,d,c)$ and LP$(W,x,s)$ define the same problem.
  
    We apply Lemma~\ref{lem:opt} to $(W,x,s)$. This guarantees the existence of an optimal $(x^*,s^*)$
   to  LP$(W,x,s)$  such that 
   \[
   \|x^*-x\|_\infty\le \kappa_W\|x_{\Lambda(x,s)}\|_1=\kappa_W\left( \left\|x^-\right\|_1+\left\|x_{\supp(s)}^+\right\|_1\right)\ .
   \]
   
   Since $\tilde x\ge 0$, we get that $\|x^-\|_1\le \|x_{\supp(x^-)}-\tilde x_{\supp(x^-)}\|_1$. Second, by the optimality of $(\tilde x, s)$, we have $\tilde x_{\supp(s^+)}=0$, and thus $x_{\supp(s^+)} = x_{\supp(s^+)}-\tilde x_{\supp(s^+)}$. These together imply that
   \[
   \begin{aligned}
   \|x^* - \tilde x\|_\infty &\le \|x^* - x\|_\infty + \|x - \tilde x\|_\infty \le (\kappa_W+1) \|x - \tilde x\|_1\\
   &= (\kappa_W + 1)\|\proj_{W^\perp}(d-\tilde x)\|_1\, . 
   \end{aligned}
   \]
  \end{proof}

    We can immediately use Lemma~\ref{lem:primal_prox} to derive a conclusion on the support of the optimal dual solutions to LP$(W,d,c)$, using  the optimal solution to LP$(W,\tilde d,c)$. 
    \begin{theorem}\label{cor:dual-fix-weak}
        Let $W\subseteq \R^n$ be a subspace and $c, d \in \R^n$.
         Let $(\tilde x, s)$ be an optimal solution to
         LP$(W,\tilde x, c)$ and 
        \[
        R:=\{i\in [n]:\,  \tilde x_i> (\kappa_W + 1)\|\proj_{W^\perp}(\tilde x-d)\|_1\}\, .
        \]
         Then for every dual optimal solution $s^*$ to \ref{LP-subspace-f}, we have $s^*_R=0$.
    \end{theorem}
    \begin{proof}
        By Lemma~\ref{lem:primal_prox} there exists an optimal solution $(x', s')$ to LP$(W,d,c)$ such that $\|x' - \tilde x\|_\infty \le (\kappa_W + 1)\|\proj_{W^\perp}(d - \tilde x)\|_1$.
        Consequently, $x'_R>0$, implying $s^*_R=0$ for every dual optimal $s^*$ by complementary slackness.
    \end{proof}

In Section~\ref{sec:steepest-improved}, we use a dual version of this theorem, also including upper bound constraints in the primal side. We now adapt the required proximity result to the following primal and dual LPs, and formulate it in matrix language to conform to the algorithm in Section~\ref{sec:steepest-improved}.
\begin{equation}
  \label{LP_upper}
  \begin{aligned}
\min \; & \pr{c}{x} \\ 
Ax&=b\,, \\
0\leq x&\leq u\,.\\
  \end{aligned}
  \quad\quad\quad
  \begin{aligned}
  \max \;  \pr{y}{b}-&\pr{u}{t} \\
  A^\top y + s-t &= c\,, \\
  s,t & \geq 0\,. \\
  \end{aligned}
\end{equation}
Note that any $y\in\R^m$ induces a feasible dual solution with $s_i=(c_i-\pr{a_i}{y})^+$ and $t_i=(\pr{a_i}{y}-c_i)^+$ for $i\in [n]$.
A primal feasible solution  $x$  and $y\in\R^m$ are optimal solutions if and only if $\pr{a_i}{y}\le c_i$ if $x_i<u_i$ and $\pr{a_i}{y}\ge c_i$ if $x_i>0$.

        \begin{theorem}\label{thm:primal-fixing-upper}
        Let $(x',y')$ be optimal primal and dual solutions to \eqref{LP_upper} for input $(b,u,c')$, and $(x'',y'')$ for input $(b,u,c'')$. Let
        \[
        \begin{aligned}
                R_0&:=\{i\in [n]:\,  \pr{a_i}{y'}< c'_i- (\kappa_W + 1)\|c'-c''\|_1\}\, ,\\
        R_u&:=\{i\in [n]:\,  \pr{a_i}{y'}> c'_i+ (\kappa_W + 1)\|c'-c''\|_1\}\, .
        \end{aligned}
        \]
         Then $x''_i=0$ for every $i\in R_0$ and $x''_i=u_i$ for every $i\in R_u$.
    \end{theorem}
    \begin{proof}
    Let $\bar A=\begin{pmatrix}A & 0\\ I_n & I_n\end{pmatrix}$. It is easy to see that $\kappa_{\bar A}=\kappa_A$. 
Let $\bar d\in \R^{2n}$ such that $\bar A\bar d=\begin{pmatrix} b\\ u\end{pmatrix}$.
    With $\bar c=(c,0_n)$,
    the primal system can be equivalently written as 
    $\min \pr{\bar c}{\bar x}$, $\bar x\in \ker(\bar A)+\bar d$, $\bar x\ge 0$. The statement follows by Theorem~\ref{cor:dual-fix-weak} applied for $W=(\ker(\bar A))^\perp=\operatorname{im}(\bar A^\top)$.
    \end{proof}
