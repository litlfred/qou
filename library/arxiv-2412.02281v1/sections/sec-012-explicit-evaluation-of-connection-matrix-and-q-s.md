---
doc_id: arxiv-2412.02281v1
doc_title: "Explicit evaluation of the q -Stokes matrices for certain conﬂuent hypergeometric q -diﬀerence equations"
section_id: sec-012-explicit-evaluation-of-connection-matrix-and-q-s
section_title: "Explicit Evaluation of Connection Matrix and q-Stokes Matrix of (2)"
section_number: null
pages: 17-18
source_pdf: 2412.02281v1.pdf
source_sha256: ac4127cf4994b2ba
toc_source: outline
text_source: latex
latex_prose_ratio: 0.61
latex_coverage_ratio: 0.957
doc_brief: "Explicit evaluation of the q -Stokes matrices for certain conﬂuent hypergeometric q -diﬀerence equations — We prove a connection formula for the basic hypergeomtric function nϕn−1 (a1, ..., an−1, 0"
---
\label{sec:qdes}


Since the matrices $E_{n n}$ and $\operatorname{diag}\left({P}_{n-1},1\right)$ commute with each other, we get
\begin{prop}\label{conjugation}
Under the  condition \eqref{eq:vivj} (with   the   condition \eqref{ineq1} included), the nonresonant condition \eqref{qnreso},    and  condition \eqref{ineq2},   for       $\lambda\in \mathbb{C}^{*}\backslash \cup_{1\leq l \leq n-1} [-{(1-q)}/{q^{\nu_l}};q]$,     we  have
\begin{align*}
&     {F}_q^{(\infty)}(z,\lambda;E_{nn},A)=\operatorname{diag}\left({P}_{n-1},1\right) {F}_q\left(z,\lambda;E_{nn},A_{n-1}\right)\operatorname{diag}\left({P}_{n-1}^{-1},1\right),  \\
&    {F}^{(0)}_q(z;E_{nn},A)=\operatorname{diag}\left({P}_{n-1},1\right) {F}^{(0)}_q\left(z;E_{nn},A_{n-1}\right)  .
\end{align*}
   Moreover, the  connection matrix and  $q$-Stokes matrices   of the systems \eqref{qdes} and \eqref{diagqdes} are related by
\begin{align*}
&S_q\left(z,\lambda,\mu;E_{nn}, A\right)=\operatorname{diag}\left({P}_{n-1},1\right)S_{q}\left(z,\lambda,\mu;E_n, A_{n-1}\right)\operatorname{diag}\left({P}_{n-1}^{-1},1\right),\\
&U_q\left(z,\lambda;E_{nn},A   \right)=\operatorname{diag}\left({P}_{n-1},1\right) U_q\left(z,\lambda;E_{nn},A_{n-1}   \right).
\end{align*}
\end{prop}
Following Proposition \ref{conjugation}, the explicit expression of the $q$-Stokes matrix of \eqref{qdes} is given below and the connection matrix of \eqref{qdes}  can be determined in a similar manner.
\begin{thm}\label{main q-stokes}
Under the condition \eqref{cond:uiujvivj},    and  for  $z,\lambda,\mu$  such that
\begin{equation*}
     \lambda,\mu  \in \mathbb{C}^*,\ \lambda,\mu  \notin -\frac{1-q}{q^{\nu_l}}q^{\mathbb{Z}}, \  \text{for} \   1\leq l \leq n-1, \  \mu\notin \lambda q^{\mathbb{Z}},      \  \text{and} \  z\in \mathbb{C}^*, \  z\notin - \frac{1}{\mu}q^{\mathbb{Z}}, \  z\notin  - \frac{1}{\lambda}q^{\mathbb{Z}},
\end{equation*}
 the $q$-Stokes matrix $S_q\left(z,\lambda,\mu;E_{nn}, A\right)$ of the system \eqref{qdes} takes the block matrix form
\begin{equation*}
S_q\left(z,\lambda,\mu;E_{nn}, A\right)=\left(\begin{array}{cc}
    \mathrm{Id}_{n-1} & 0  \\
    b_q & 1
  \end{array}\right),
  \end{equation*}
where $b_{q}=\left(\left(b_q\right)_1,...,\left(b_{q}\right)_{n-1}\right)$ with
\begin{align*}
\left(b_{q}\right)_k=&\sum_{j=1}^{n-1} \text{  \scriptsize $\frac{(-1)^{n+k}\Delta_{1,...,n-1}^{1,..., n-2,n}\left(A-\lambda_j^{\left(n-1\right)}\cdot \mathrm{Id}_n\right) \Delta^{1,...,\hat{k},...,n-1}_{1,...,n-2}   \left(A-\lambda^{\left(n-1\right)}_j\cdot \mathrm{Id}_n\right)}{{\prod_{l=1,l\ne j}^{n-1}\left(\lambda^{\left(n-1\right)}_l-\lambda^{\left(n-1\right)}_j\right)\prod_{l=1}^{n-2}\left(\lambda^{\left(n-2\right)}_l-\lambda^{\left(n-1\right)}_j\right)} }$  } \\
    &  \sum_{s=1}^n
    \frac{  \prod_{l=1}^{n-1} ( q^{1+\mu_{s}-\nu_{l}}  ;q)_\infty}{\prod_{l=1,l\neq   s}^{n}   (q^{1+\mu_{s}-\mu_{l}}   ;q)_\infty}   \frac{\prod_{l=1,l\neq s}^{n}\theta_q((1-q)q^{1-\mu_l}/\lambda)}{\prod_{l=1}^{n-1}\theta_q((1-q)q^{1-\nu_l}/\lambda)}   
 \frac{\theta_q\left(  q^{ \mu_s-\nu_n  }  \lambda z\right)}{\theta_q(\lambda  z )}     \\
  &\times   \frac{ \prod_{ l=1,l\neq  s  }^n  ( q^{1+\mu_l-{\nu}_j} ;q )_{\infty} \prod_{l=1,l\neq  j}^{n-1}  ( q^{ \nu_l-\mu_s  }  ;q)_{\infty} }{ \prod_{l=1,l\neq  j}^{n-1} ( q^{ 1+\nu_l-\nu_j  } ;q)_{\infty}\prod_{l=1,l\neq  s}^n ( q^{\mu_{ l }-\mu_s} ;q)_{\infty} }        \frac{ \theta_q\left( { q^{  \nu_j-\mu_s-1  } \mu z }       \right)  }{ \theta_q\left(  \mu z   \right)   }  \frac{ \theta_q \left(  {{\mu q^{ \mu_s       }}}/{(1-q)} \right)  }{ \theta_q\left(   {{\mu q^{    \nu_j  -1  }}}/{(1-q)}  \right)  }    \frac{z^{\nu_j}}{z^{\nu_n+1}} .
\end{align*}
\end{thm}
\begin{proof}
The  expression of $\operatorname{diag}\left({P}_{n-1},1\right)S_{q}\left(z,\lambda,\mu;E_n, A_{n-1}\right)\operatorname{diag}\left({P}_{n-1}^{-1},1\right)$ tells us that
\begin{align}
    \left(b_{q}\right)_k=&-\sum_{j=1}^{n-1}   {b_j^{(n-1)}\left({P}^{-1}_{n-1}\right)_{jk}}  \sum_{s=1}^n
    \frac{  \prod_{l=1}^{n-1} ( q^{1+\mu_{s}-\nu_{l}}  ;q)_\infty}{\prod_{l=1,l\neq   s}^{n}   (q^{1+\mu_{s}-\mu_{l}}   ;q)_\infty}   \frac{\prod_{l=1,l\neq s}^{n}\theta_q((1-q)q^{1-\mu_l}/\lambda)}{\prod_{l=1}^{n-1}\theta_q((1-q)q^{1-\nu_l}/\lambda)}   
 \frac{\theta_q\left(  q^{ \mu_s-\nu_n  }  \lambda z\right)}{\theta_q(\lambda  z )}   \nonumber   \\
  &\times   \frac{ \prod_{ l=1,l\neq  s  }^n  ( q^{1+\mu_l-{\nu}_j} ;q )_{\infty} \prod_{l=1,l\neq  j}^{n-1}  ( q^{ \nu_l-\mu_s  }  ;q)_{\infty} }{ \prod_{l=1,l\neq  j}^{n-1} ( q^{ 1+\nu_l-\nu_j  } ;q)_{\infty}\prod_{l=1,l\neq  s}^n ( q^{\mu_{ l }-\mu_s} ;q)_{\infty} }        \frac{ \theta_q\left( { q^{  \nu_j-\mu_s-1  } \mu z }  \right)  }{ \theta_q\left(  \mu z   \right)   }  \frac{ \theta_q \left(  {{\mu q^{ \mu_s       }}}/{(1-q)} \right)  }{ \theta_q\left(   {{\mu q^{    \nu_j  -1  }}}/{(1-q)}  \right)  }    \frac{z^{\nu_j}}{z^{\nu_n+1}}
       . \label{b+k}
\end{align}
Using Proposition \ref{An-1Pn-1}, the identity \eqref{b+k} can be rewritten as the form in this theorem. 
\end{proof}
Like Remark \ref{rmkres:nvaphin}, we have
\begin{rmk}
    We can use the connection formula of ${}_n\varphi_n(a_1,...,a_n;b_1,...,b_n;z)$ to derive the $q$-Stokes matrix of the system
    \begin{equation*}
    D_qF_q(z)=\left(E_{n n}\sigma_q+\frac{A}{z}\right)F_q(z).
\end{equation*}
\end{rmk}


\section{Behavior of the Equation \eqref{intro:conflu hyper eq} and the System \eqref{qdes} as $q\rightarrow 1$}\label{qlimit}
In this section, we study the behavior of the connection formula for the equation \eqref{intro:conflu hyper eq} (see Section \ref{subsec:eqlim}),   as well as the connection matrix and the $q$-Stokes matrix of the system \eqref{qdes} (see Section \ref{sec:syslim}) as $q\rightarrow 1$.   See  \cite{sauloy2000systemes}  for   more  discussions in   the Fuchsian case  and  \cite{dreyfus2015confluence} in the irregular case.
