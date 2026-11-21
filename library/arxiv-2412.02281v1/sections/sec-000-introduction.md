---
doc_id: arxiv-2412.02281v1
doc_title: "Explicit evaluation of the q -Stokes matrices for certain conﬂuent hypergeometric q -diﬀerence equations"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 2412.02281v1.pdf
source_sha256: ac4127cf4994b2ba
toc_source: outline
text_source: latex
latex_prose_ratio: 0.808
latex_coverage_ratio: 0.979
doc_brief: "Explicit evaluation of the q -Stokes matrices for certain conﬂuent hypergeometric q -diﬀerence equations — We prove a connection formula for the basic hypergeomtric function nϕn−1 (a1, ..., an−1, 0"
---
Set $q\in\mathbb{R}$ with $0<q<1$.    Take the Lie algebra ${\mathfrak {gl}_n}$ over the field of complex numbers with a positive integer $n$. Consider the confluent hypergeometric $q$-difference  system
\begin{equation}\label{u+A/z}
	D_qF_q(z):=\frac{\sigma_qF_q(z)-F_q(z)}{qz-z}=\left(u+\frac{A}{z}\right)F_q(z),
\end{equation}
where $\sigma_q F(z)=F(q z)$, $u=\mathrm{diag}\left(u_1,...,u_{n-1},u_n\right)$ and $A=(a_{ij})\in {\mathfrak {gl}_n}$.  The infinity $z=\infty$ is a  Fuchsian singularity  of    \eqref{u+A/z} if the diagonal matrix $u$ is invertible. One can use the method of isomonodromy deformation to study the connection problem of the equation \eqref{u+A/z} (see e.g., \cite{jimbo1996q, MR2652472, MR2642627, ohyama2021q, MR4245859}). It is parallel to the corresponding differential system case studied in \cite{MR688949, MR533348, TX, Xu}. In this method,    the monodromy data of the system \eqref{u+A/z} with $u=\mathrm{diag}(0,...,0,1)$  are needed.  

In this paper, we focus on the irregular      case of the form
\begin{equation}\label{qdes}
    D_qF_q(z)=\left(E_{n n}+\frac{A}{z}\right)F_q(z),
\end{equation}
with  $E_{n n}=\mathrm{diag}(0,...,0,1)$.    
Denote by $A^{\left(k\right)}$ the upper left $k\times k$ submatrix of $A=\left(a_{i j}\right)\in \mathfrak{gl}_n$, and by $\lambda^{\left(k\right)}_1,...,\lambda^{\left(k\right)}_{k}$ the $k$ eigenvalues of $A^{\left(k\right)}$.   Set  the complex numbers
    \begin{align*}
	&\mu_i:=\mathrm{log}_q\left(1-(1-q)\lambda_i^{(n)}\right),\quad 1\leq i\leq n,\\
&\nu_i:=\mathrm{log}_q\left(1-(1-q)\lambda_i^{(n-1)}\right),\quad 1\leq i\leq n-1,
	\end{align*}
where we take the principal branch of the logarithmic function. 

 

Under the following assumption
\begin{equation}
    \nu_i- \nu_j\notin \mathbb{Z}, \ \text{for all} \ 1\leq i \neq j \leq n-1, \label{eq:vivj}
\end{equation}
 the system \eqref{qdes}  has   a unique formal fundamental solution $\hat{F}_q$ around $z=\infty$. The theory of $q$-Borel resummation states that for  $\lambda\in \mathbb{C}^{*}\backslash -\frac{1-q}{q^{\nu_j}}q^{\mathbb{Z}}$,  $1\leq j \leq n-1$,    there exists a meromorphic fundamental solution $F^{(\infty)}_q(z,\lambda)$ which is  asymptotic to  $\hat{F}_q$  of  $q$-Gevrey order  $1$ along the direction $\lambda$.  For different directions, these solutions are in general different
(which reflects the $q$-Stokes phenomenon), and the transition between them can be measured  by  a  $q$-Stokes
matrix (see e.g.,  \cite{marotte2000multisommabilite, ramis1992growth, ramis2013local, MR1952546, zhang1999developpements, zhang2002sommation, zhang2005remarks} for the detailed study of $q$-Borel resummation, $q$-Gevrey order and so on).   The main result of this paper is the following theorem, which gives the
$q$-Stokes matrix   of the system  \eqref{qdes}  explicitly. See Section \ref{sec:qdes} for a proof.

\begin{thm}\label{intro: qstokes}
   If the following condition holds for the matrix $A$:
\begin{equation*}
\begin{aligned}
    &   \mu_i-\mu_j\notin \mathbb{Z}, \  &&\text{for all}  \  1\leq i \neq j \leq  n,   \\
    & \nu_i-\nu_j\notin  \mathbb{Z},  \  &&\text{for all}  \  1\leq i\neq  j \leq  n-1,   \\
    &\lambda^{\left(n-1\right)}_j   \neq   \lambda^{\left(n-2\right)}_l,  \  &&\text{for all}  \  1\leq j \leq  n-1, 1\leq l \leq n-2,
\end{aligned}
\end{equation*}
and the following condition holds for   $z,\lambda,\mu$:
\begin{equation*}
     \lambda,\mu  \in \mathbb{C}^*,  \  \mu\notin \lambda q^{\mathbb{Z}},   \ \lambda,\mu  \notin -\frac{1-q}{q^{\nu_l}}q^{\mathbb{Z}}, \  \text{for} \   1\leq l \leq n-1,       \  \text{and} \  z\in \mathbb{C}^*, \  z\notin - \frac{1}{\mu}q^{\mathbb{Z}}, \  z\notin  - \frac{1}{\lambda}q^{\mathbb{Z}},
\end{equation*}
    then the $q$-Stokes matrix $S_q\left(z,\lambda,\mu;E_{nn}, A\right)$ of the system \eqref{qdes} takes the block matrix form
\begin{equation*}
S_q\left(z,\lambda,\mu;E_{nn}, A\right)=\left(\begin{array}{cc}
    \mathrm{Id}_{n-1} & 0  \\
    b_q & 1
  \end{array}\right),
  \end{equation*}
where $b_{q}=\left(\left(b_q\right)_1,...,\left(b_{q}\right)_{n-1}\right)$ with
\begin{align*}
\left(b_{q}\right)_k=&\sum_{j=1}^{n-1} \text{ \scriptsize $ \frac{(-1)^{n+k}\Delta_{1,...,n-1}^{1,..., n-2,n}\left(A-\lambda_j^{\left(n-1\right)}\cdot \mathrm{Id}_n\right) \Delta^{1,...,\hat{k},...,n-1}_{1,...,n-2}   \left(A-\lambda^{\left(n-1\right)}_j\cdot \mathrm{Id}_n\right)}{{\prod_{l=1,l\ne j}^{n-1}\left(\lambda^{\left(n-1\right)}_l-\lambda^{\left(n-1\right)}_j\right)\prod_{l=1}^{n-2}\left(\lambda^{\left(n-2\right)}_l-\lambda^{\left(n-1\right)}_j\right)} } $ }  \\
    &  \sum_{s=1}^n
    \frac{  \prod_{l=1}^{n-1} ( q^{1+\mu_{s}-\nu_{l}}  ;q)_\infty}{\prod_{l=1,l\neq   s}^{n}   (q^{1+\mu_{s}-\mu_{l}}   ;q)_\infty}   \frac{\prod_{l=1,l\neq s}^{n}\theta_q((1-q)q^{1-\mu_l}/\lambda)}{\prod_{l=1}^{n-1}\theta_q((1-q)q^{1-\nu_l}/\lambda)}   
 \frac{\theta_q\left(  q^{ \mu_s-\nu_n  }  \lambda z\right)}{\theta_q(\lambda  z )}     \\
  &\times   \frac{ \prod_{ l=1,l\neq  s  }^n  ( q^{1+\mu_l-{\nu}_j} ;q )_{\infty} \prod_{l=1,l\neq  j}^{n-1}  ( q^{ \nu_l-\mu_s  }  ;q)_{\infty} }{ \prod_{l=1,l\neq  j}^{n-1} ( q^{ 1+\nu_l-\nu_j  } ;q)_{\infty}\prod_{l=1,l\neq  s}^n ( q^{\mu_{ l }-\mu_s} ;q)_{\infty} }        \frac{ \theta_q\left( q^{ \nu_j-\mu_s-1  }    {  \mu z }  \right)  }{ \theta_q\left(  \mu z   \right)   }  \frac{ \theta_q \left(  {{ q^{ \mu_s       } \mu   }}/{(1-q)} \right)  }{ \theta_q\left(   {{  q^{    \nu_j  -1  } \mu  }}/({1-q})  \right)  }    \frac{z^{\nu_j}}{z^{\nu_n+1}} .
\end{align*} 
Here  the definitions of the $q$-Pochhammer symbol $(a;q)_{\infty}$  and the $q$-theta function $\theta_q(z)$ are given in Section \ref{notation}   and    $\Delta_{1,...,n-1}^{1,..., n-2,n}\left(A-\lambda_j^{\left(n-1\right)}\cdot \mathrm{Id}_n\right)$  is  {a}  minor of the matrix $A-\lambda^{\left(n-1\right)}_j\cdot \mathrm{Id}_n$  introduced in Section \ref{sec:diag}.
\end{thm}

Under the nonresonant condition
\begin{equation}\label{qnreso}
    \mu_i-\mu_j\notin \mathbb{Z}_{>0}, \ \text{for all} \ 1\leq i,j \leq n,
\end{equation}
the system \eqref{qdes}  has  a convergent fundamental solution $F^{(0)}_q(z)$  around $z=0$.  The transition between  $F^{(0)}_q(z)$  and  $F^{(\infty)}_q(z,\lambda)$   is measured by some  connection  matrix given   explicitly in Theorem  \ref{qstokes matrix}.  

The computation of the $q$-Stokes matrix and the  connection  matrix
  mainly relies on the following   connection formula of  the   confluent hypergeometric $q$-difference   equation of the form
\begin{equation}\label{intro:conflu hyper eq}
      z\prod_{l=1}^{n-1}(1-a_l \sigma_q)y(z)=(1-\sigma_q)\prod_{l=1}^{n-1}\left(1-\frac{b_l}{q}\sigma_q\right)y(z),
 \end{equation}
 which   expresses  
the solutions  of  \eqref{intro:conflu hyper eq}  around the origin      as a sum of the solutions  of  \eqref{intro:conflu hyper eq}  around infinity         with     pseudo-constant  coefficients (see Definition \ref{def:pseudo}). Here   $\sigma_q$ is the $q$-shift operator defined by $\sigma_q y(z)=y(q z)$.
See Section \ref{seclab conne formu eq} for a proof of the following theorem.

 \begin{thm}\label{intro:our connection formula}
For $a_1,a_2,...,a_{n-1},b_1,b_2,...,b_{n-1}$ such that         
\begin{equation*}
    a_i\neq 0, \ a_i/a_j\notin q^{\mathbb{Z}}, \ \text{for}\ 1\leq i\neq j \leq n-1, \  \text{and} \ b_l\notin \{0\}\cup q^{-\mathbb{N}}, \  \text{for}  \ 1\leq l \leq n-1,
\end{equation*}
and  for  $\lambda,z$  such that     
\begin{equation*}
    \lambda\in \mathbb{C}^*,\ \lambda\notin -a_i q^{\mathbb{Z}}, \  \text{for} \   1\leq i \leq n-1, \  \text{and} \  z\in \mathbb{C}^*, \  z\notin q^{\mathbb{Z}}, \  z\notin  -\frac{\prod_{l=1}^{n-1} b_l}{ \lambda \prod_{l=1}^{n-1} a_l}q^{\mathbb{Z}},
\end{equation*}
we have
\begin{align*}
    &{}_n\varphi_{n-1}\left(
			a_1,...,a_{n-1},0;
			b_1,...,b_{n-1}
		; q, z\right)\\
  =&\sum_{i=1}^{n-1}
		\frac{(a_1,...,\widehat{a_{{i}} },...,a_{n-1},b_1/a_i,...,b_{n-1}/a_i;q)_\infty}{(b_1,...,b_{n-1},a_1/a_i,...,\widehat{a_{{i}}/a_i},...,a_{n-1}/a_i;q)_\infty}\frac{\theta_q(-a_i z)}{ \theta_q(-z) } z^{\log_qa_i}  \cdot {f}^{(\infty)}_q(z,\lambda)_{i}\\
  &+\frac{(a_1,...,a_{n-1};q)_\infty}{(b_1,...,b_{n-1};q)_\infty}
		\frac{\prod_{s=1}^{n-1}\theta_q\big( {\prod_{l=1}^{n-1}a_l} \big / \big(  {\lambda \prod_{l=1,l\neq s}^{n-1}b_l}  \big)    \big)}{\prod_{s=1}^{n-1}\theta_q\left({a_s\prod_{l=1}^{n-1}a_l  }\big /\big({\lambda \prod_{l=1}^{n-1}b_l  } \big)  \right)}
		\frac{\theta_q\left( {\lambda z\prod_{l=1}^{n-1}b_l   }\big /{\prod_{l=1}^{n-1}a_l}\right)}{\theta_q\left( \lambda z \right)}
\frac{\prod_{l=1}^{n-1}z^{\log_qb_l}   }{ \prod_{l=1}^{n-1}z^{\log_qa_l}  }	{f}^{(\infty)}_q(z)_{n}	,
\end{align*}
 where the  basic hypergeometric series ${}_n\varphi_{n-1}\left(
			a_1,...,a_{n-1},0;
			b_1,...,b_{n-1}
		; q, z\right)$ (see Definition \ref{def:basic f})   is  a  solution  of \eqref{intro:conflu hyper eq} around the origin,   and  $
 {f}_q^{(\infty)}(z,\lambda)_{1} ,
...  ,
 {f}_q^{(\infty)}(z,\lambda)_{n-1}  ,
{f}_q^{(\infty)}(z)_{n}$ is a fundamental system  of meromorphic  solutions of \eqref{intro:conflu hyper eq}      around infinity   (see Proposition \ref{fqlambda}).  Here    $\widehat{a_{i}}$   and   $\widehat{a_{{i}}/a_i}$   mean the corresponding $i$-th terms  $a_i$  and  $a_{{i}}/a_i$  are skipped. 
\end{thm}

At the end of this article, we show that Theorem \ref{intro: qstokes} and Theorem \ref{intro:our connection formula}  recover the   corresponding   Stokes matrices  and   connection formula   in the differential case  as $q\rightarrow 1$.  See Section \ref{qlimit}.


The connection problem of the basic hypergeometric series ${}_n\varphi_m(a_1, a_2, ..., a_n ;b_1, ..., b_m;q,z)$  (see Definition \ref{def:basic f})  can be traced back to Heine (see e.g., \cite{Heine1846, Heine1847, MR204726}), and after that
\begin{itemize}
    \item  Thomae (see \cite{thomae1869beitrage}) and  Watson (see \cite{watson1910continuation})     gave the connection formula  of ${}_2\varphi_1(a_1,a_2;b_1;q,z)$ if   $a_1,a_2,b_1\neq 0$.
    \item  The connection formula of ${}_n\varphi_{n-1}(a_1,...,a_n;b_1,...,b_{n-1};q,z)$ was shown by Thomae   (see  \cite{thomae1870series})  when $a_i,b_j\neq 0$, for $1\leq i \leq n$,  $1\leq j \leq n-1$,  and  equivalent versions can be found in \cite{gasper2004basic, MR201688}.
\end{itemize}
However, if one of the conditions: $m=n-1$  or  $a_i,b_j\neq 0$  for $1\leq i \leq n$,  $1\leq j \leq m$,  does not hold,  the connection problem involves  divergent series  and  the  $q$-Borel resummation is required.  In these cases,
\begin{itemize}
    \item     Zhang obtained the connection formula of  ${}_2f_0(a_1,a_2;-;\lambda;q,z)$ (see Definition \ref{def:nfn-2} for the notation)      in \cite{zhang2002sommation},    ${}_2\varphi_1(0,0;b_1;q,z)$,  ${}_0\varphi_1(-;b_1;q,z)$ in \cite{zhang2003fonctions},  ${}_1\varphi_1(a_1;b_1;q,z)$,       ${}_2\varphi_1(a_1,0;b_1;q,z)$  in       \cite{ zhang2005remarks}    and so on.
        \item Morita obtained the   connection formula of  ${}_1\varphi_1(0;b_1;q,z)$ in \cite{morita2011connection},  ${}_2\varphi_1(a_1,a_2;0;q,z)$ in \cite{morita2013connection},   ${}_2\varphi_0(0,0;-;q,z)  $, ${}_0\varphi_1(-;0;q,z)$ in \cite{morita2014stokes}, ${}_3\varphi_1(a_1,a_2,a_3;b_1;q,z)$ in \cite{morita2014stokes1} and so on.
        \item Ohyama obtained the connection formula of   ${}_1\varphi_1(0;b_1;q,z)$ in  \cite{ohyama2016q},    ${}_r\varphi_{r-1}(0,...,0;b_1,...,b_{r-1};q,z)$  in   \cite{ohyama2017connection},  ${}_n\varphi_m(a_1, a_2, ..., a_n ;b_1, ..., b_m;q,z)$  with   $a_l\neq 0$,  $1\leq l \leq n$, for $n\geq m+1$   in \cite{ohyama2021q} (with Zhang) and so on.
        \item Adachi obtained the connection formula of ${ }_n f_{m}(a_1,...,a_n ; b_1,...,b_m ; \lambda ; q, z)$  (see Definition \ref{def:nfn-2})   for $n\geq m+2$  in \cite{adachi2019q} and so on.

        \item 
This paper derives the connection formula of ${}_n\varphi_{n-1}(a_1,...,a_{n-1},0;b_1,...,b_{n-1};q,z)$ with $a_l,b_l\neq 0$, for $1\leq l \leq n-1$. For $n=2$, it recovers the connection formula of $_2\varphi_1(a_1,0;b_1;q,z)$ in Zhang \cite{ zhang2005remarks}. 
\end{itemize}
There may be other works missed in the above list. 

After 1990s, Ramis,  Sauloy  and Zhang   are constructing modern theory
on $q$-asymptotics (see \cite{ramis2013local})  and the application to global analysis on $q$-Painlev\'e equations  leads to   the Riemann-Hilbert correspondence in modern sense(see e.g., \cite{MR4245859, ohyama2021q}).



\vspace{2mm}
The organization of the paper is as follows. Section \ref{sec:equation case} recalls the basic knowledge of basic hypergeometric series,  the theory of $q$-Borel resummation and  derive the connection formula of the equation  \eqref{intro:conflu hyper eq}.  Section \ref{main section}  computes explicitly the $q$-Stokes matrix of the system \eqref{qdes}. Section \ref{qlimit} studies   the behavior of   the connection formula  and the $q$-Stokes matrix   as $q\rightarrow 1$.
 


\subsection{Acknowledgments}
\noindent
We would like to thank Qian Tang for the discussion and valuable feedback on the paper. The authors are supported by  the  National Key Research and Development Program of China (No. 2020YFE0204200),  by   the National Key Research and Development Program of China (No. 2021YFA1002000) and by the National Natural Science Foundation of China (No. 12171006).

















\section{Connection Formula of the Equation \eqref{intro:conflu hyper eq} }\label{sec:equation case}
This section derives explicitly the connection formula  of the equation  \eqref{intro:conflu hyper eq}. In particular, Section \ref{notation} gives the basic notations of $q$-calculus. Section \ref{hyper series} 
introduces the basic hypergeometric series. Section \ref{sec:q-borel sum} overviews the $q$-Borel resummation. Section \ref{seclab conne formu eq} then {gives} the explicit connection   formula  of the equation   \eqref{intro:conflu hyper eq} via the confluence method.
