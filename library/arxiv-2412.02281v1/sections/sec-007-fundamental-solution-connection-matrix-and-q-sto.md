---
doc_id: arxiv-2412.02281v1
doc_title: "Explicit evaluation of the q -Stokes matrices for certain conﬂuent hypergeometric q -diﬀerence equations"
section_id: sec-007-fundamental-solution-connection-matrix-and-q-sto
section_title: "Fundamental Solution, Connection Matrix and q-Stokes Matrix"
section_number: null
pages: 10-11
source_pdf: 2412.02281v1.pdf
source_sha256: ac4127cf4994b2ba
toc_source: outline
text_source: latex
latex_prose_ratio: 0.825
latex_coverage_ratio: 0.914
doc_brief: "Explicit evaluation of the q -Stokes matrices for certain conﬂuent hypergeometric q -diﬀerence equations — We prove a connection formula for the basic hypergeomtric function nϕn−1 (a1, ..., an−1, 0"
---
\label{sec:sol zero inf}
 The fundamental solution of \eqref{u+A/z} is studied in \cite{birkhoff1913generalized} (especially when $u$ is invertible).  If $u$ is not invertible, there is     a slightly different formal  fundamental solution   (see e.g.,  \cite{dreyfus2015confluence}). Particularly,  the system \eqref{qdes} has a  formal fundamental solution around infinity as follows
 \begin{equation*}
    \hat{F}_q(z;E_{n n},A)=\hat{H}_q(z;E_{nn},A)  z^{\delta^{(n-1)}_{q}(A)}   e_q\left( E_{n n} q^{ -\delta_{q}^{(n-1)}(A) } z \right),
\end{equation*}
where $\hat{H}_q(z;E_{nn},A)=\mathrm{Id}_n+\sum_{m=1}^{\infty} H^{(\infty)}_{m}  z^{-m}$ and 
\begin{equation}\label{deltan-1}
    \delta^{(n-1)}_{q}\left(A\right)_{ij}=\left\{
          \begin{array}{lr}
             \log_q(1-(1-q)A^{(n-1)})_{i j},   & \text{if} \ \ 1\le i, j\le n-1,  \\
     \sum_{l=1}^{n} \mu_l-\sum_{l=1}^{n-1}\nu_l        , & \text{if} \ \ i=j=n,\\
           0, & \text{otherwise},
             \end{array}
\right.
\end{equation}
with  $A^{\left(n-1\right)}$ being  the upper left $(n-1)\times (n-1)$ submatrix of $A=\left(a_{i j}\right)$    and \[e_q\big( E_{n n} q^{ -\delta_{q}^{(n-1)}(A) } z \big)=\mathrm{diag}\Big(0,...,0,e_q\Big(q^{-\delta^{(n-1)}_{q}\left(A\right)_{n n}}z  \Big)\Big).\]  
\begin{prop}[see e.g.,  \cite{adams1928linear}]\label{convergent column}
    The entries in the last column of $\hat{F}_q(z;E_{n n},A)$  are convergent, while the  other entries of $\hat{F}_q(z;E_{n n},A)$  are   in general divergent.
\end{prop}
 But still, the entries of (the first $n-1$ columns of) the formal fundamental solution $\hat{F}_q(z;E_{nn},A)$ (or equivalently $\hat{H}_q(z;E_{n n},A)$) of the equation \eqref{qdes} are $[\lambda;q]$-summable for any $\lambda\in \mathbb{C}^{*}\backslash \cup_{1\leq j \leq n-1}[-{(1-q)}/{q^{\nu_j}};q]$ (see \cite{adachi2019q, dreyfus2015confluence}). That is,
\begin{prop}[\cite{adachi2019q, dreyfus2015confluence}]
For any $\lambda\in \mathbb{C}^{*}\backslash \cup_{1\leq j \leq n-1} [-{(1-q)}/{q^{\nu_j}};q]$,    there is a  fundamental solution $F_q^{(\infty)}(z,\lambda;E_{nn},A)$ of the equation \eqref{qdes} obtained from  the  $q$-Borel resummation as follows
  \begin{equation*}
      F_q^{(\infty)}(z,\lambda;E_{nn},A):={H}^{(\infty)}_q(z,\lambda;E_{n n},A)z^{\delta^{(n-1)}_{q}(A)}   e_q\left( E_{n n} q^{ -\delta_{q}^{(n-1)}(A) } z \right), 
  \end{equation*}
  with the $n\times n$ matrix ${H}^{(\infty)}_q(z,\lambda;E_{n n},A)$ given by
  \begin{equation*}
   {H}^{(\infty)}_q(z,\lambda;E_{n n},A)_{ij}:=   \mathcal{L}_{q ; 1}^{[\lambda;q]} \circ \hat{\mathcal{B}}_{q ; 1} (\hat{H}_q(z;E_{n n},A)_{ij}),\  \text{for} \ i,j=1,...,n.
  \end{equation*}
\end{prop}
Moreover, there is a convergent  fundamental solution around the origin of the form (see \cite{birkhoff1913generalized})
\begin{equation*}
    F_q^{(0)}(z;E_{n n},A)={H}^{(0)}_q(z;E_{nn},A)z^{\log_q(1-(1-q) A_n ) }, \  \text{with} \  {H}^{(0)}_q(z;E_{nn},A)= H^{(0)}_{0}+\sum_{m=1}^{\infty}H^{(0)}_{m}z^m  ,
\end{equation*}
where  $A_n:=\left(\lambda^{(n)}_1,...,\lambda^{(n)}_n  \right)$,   $\log_q(1-(1-q) A_n )=\operatorname{diag}(\mu_1,...,\mu_{n})$, and $H_0^{(0)}$  satisfies $A=H^{(0)}_0 A_n \left(H_0^{(0)}\right)^{-1}$. 

\begin{defn}\label{UqSq}
For any $\lambda\in \mathbb{C}^{*}\backslash \cup_{1\leq j \leq n-1} [-{(1-q)}/{q^{\nu_j}};q]$,       
the connection matrix $U_q(z,\lambda;E_{nn},A)$ of \eqref{qdes}   is  defined   by
\begin{equation*}
   F_q^{(\infty)}(z,\lambda;E_{nn},A) U_q(z,\lambda;E_{nn},A)=F_q^{(0)}(z;E_{nn},A).
\end{equation*}
For another $\mu \in \mathbb{C}^{*}$    satisfying    $\mu\notin   [\lambda;q]  $  and     $\mu\notin [-{(1-q)}/{q^{\nu_j}};q]$,  $1\leq j \leq n-1$,       the  $q$-Stokes matrix   $S_q(z,\lambda,\mu;E_{nn},A)$ of \eqref{qdes}  is defined   by
\begin{equation*}
    F_q^{(\infty)}(z,\mu;E_{nn},A)=F_q^{(\infty)}(z,\lambda;E_{nn},A) S_q(z,\lambda,\mu;E_{nn},A).
\end{equation*}
\end{defn}
