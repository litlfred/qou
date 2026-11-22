---
doc_id: arxiv-2412.02281v1
doc_title: "Explicit evaluation of the q -Stokes matrices for certain conﬂuent hypergeometric q -diﬀerence equations"
section_id: sec-003-basic-hypergeometric-series
section_title: "Basic Hypergeometric Series"
section_number: null
pages: 4-5
source_pdf: 2412.02281v1.pdf
source_sha256: ac4127cf4994b2ba
toc_source: outline
text_source: latex
latex_prose_ratio: 0.862
latex_coverage_ratio: 0.948
doc_brief: "Explicit evaluation of the q -Stokes matrices for certain conﬂuent hypergeometric q -diﬀerence equations — We prove a connection formula for the basic hypergeomtric function nϕn−1 (a1, ..., an−1, 0"
---
\label{hyper series}
\begin{defn}\label{def:basic f}
    A basic hypergeometric series associated to   $\boldsymbol{a}=(a_1,a_2,...,a_n)$ and  $\boldsymbol{b}=(b_1,b_2,...,b_m)$ is
\begin{equation*}
    {}_n\varphi_m\left(\begin{array}{c}
a_1, a_2, ..., a_n \\
b_1, ..., b_m
\end{array} ; q, z\right)
:=
\sum_{k=0}^{\infty} \frac{ \prod_{l=1}^n    \left(a_l ; q\right)_k}{(q ; q)_k\prod_{l=1}^m \left(b_l ; q\right)_k }\left[(-1)^k q^{\frac{k(k-1)}{2}}\right]^{1+m-n} z^k,
\end{equation*}
for  $b_1,...,b_m\notin q^{-\mathbb{N}  }$.
{ We also denote it by ${}_n\varphi_m(a_1, a_2, ..., a_n ;b_1, ..., b_m;q,z)$, or simply ${}_n\varphi_m(\boldsymbol{a};\boldsymbol{b};q,z)$.}
\end{defn}
 The  basic hypergeometric series   is a $q$-analog of the generalized hypergeometric series defined as follows. 
\begin{defn}
 A   generalized hypergeometric series  for    $\boldsymbol{\alpha}=(\alpha_1,...,\alpha_n)$ and  $\boldsymbol{\beta}=(\beta_1,...,\beta_m)$   is  defined as  
{\begin{equation*}
    {}_nF_m\left(\begin{array}{c}
\alpha_1, \alpha_2, ..., \alpha_n \\
\beta_1, ..., \beta_m
\end{array} ;  z\right)
:=
\sum_{k=0}^{\infty}\frac{\prod_{l=1}^n\left(\alpha_l\right)_k}{\prod_{l=1}^m\left(\beta_l\right)_k }\frac{z^k}{k!},
\end{equation*}}
where $\left(\alpha\right)_0=1$ and $\left(\alpha\right)_k=\alpha \left(\alpha+1\right) \cdots \left(\alpha+k-1\right)$, for $k\geq 1$  and  $\beta_l\notin {\mathbb{Z}_{\leq 0}}$,  for $1\leq l \leq m$. We also denote it by ${}_nF_m(\alpha_1, \alpha_2, ..., \alpha_n ;\beta_1, ..., \beta_m;z)$, or simply ${}_nF_m(\boldsymbol{\alpha};\boldsymbol{\beta};z)$. 
 \end{defn}

 \begin{prop}[see e.g., {\cite[Chapter 16, Chapter 17]{OLBC}}]
    The radius of convergence  { of}  ${}_n\varphi_m\left(
\boldsymbol{a};
 \boldsymbol{b}
 ; q, z\right)$ and ${}_{n}F_{m}\left(\boldsymbol{\alpha};\boldsymbol{\beta};z\right)$  is $0$, $1$ and $\infty$, {for} $n\ge m+2$, $n=m+1$ and $n\leq m$ respectively.  




\end{prop}
The equation  \eqref{intro:conflu hyper eq}  is  a   special case of the  hypergeometric $q$-difference equation: 
\begin{equation}\label{intro: qhyper eq}
      z\prod_{l=1}^{n}(1-a_l \sigma_q)y(z)=(1-\sigma_q)\prod_{l=1}^{n-1}\left(1-\frac{b_l}{q}\sigma_q\right)y(z),
 \end{equation}
 and we have 
\begin{prop}[\cite{birkhoff1913generalized}]\label{pre:connection prob}
   {If}      the  following    condition holds for  $a_1,...,a_n,b_1,...,b_{n-1}$:
\begin{equation*}
    a_i\neq 0,\  a_i/a_j\notin q^{\mathbb{Z}\backslash \{ 0 \} },\  \text{for} \   1\leq i, j \leq n, \ \text{and} \ b_l\neq   0, \ \text{for} \ 1\leq l\leq n-1,
\end{equation*}
     {then} the equation \eqref{intro: qhyper eq} has a fundamental system of    meromorphic  solutions around infinity:
 \begin{equation}\label{qhyper fsol}
    {}_n\varphi_{n-1}\left(\begin{array}{c}
			a_i, a_i q/{b_1},...,a_i q/{b_{n-1}  }\\
			a_i q/{{a}_{1}},...,\widehat{a_i q/{{a}_{i}} },...,a_i q/{{a}_{n}}
\end{array}		; q, \frac{q\prod_{l=1}^{n-1} b_l}{z\prod_{l=1}^{n}a_l }\right)z^{-\log_qa_i}, \  \text{for} \    i=1,...,n. 
 \end{equation}
Here     $\widehat{a_i q/{{a}_{i}} }$ means the $i$-th item  ${a_i q/{{a}_{i}} }$ is skipped.
\end{prop}
When           $a_n=0$,     ${}_n\varphi_{n-1}\left(\begin{array}{c}
a_1, a_2, ..., a_{n-1},0 \\
b_1, ..., b_{n-1}
\end{array} ; q, z\right)$ is   known as  a   confluent   type basic hypergeometric series, and satisfies the    confluent hypergeometric $q$-difference equation  \eqref{intro:conflu hyper eq}. 
 The equation  \eqref{intro:conflu hyper eq}  also  has a solution of the form 
 \begin{equation*} 
     \left(1+ c_1 z^{-1}+c_2 z^{-2}+...\right)\frac{z^{\sum_{l=1}^{n-1}\log_q\left(a_l/b_l\right)    }   }{(z;q)_\infty},   
 \end{equation*}
where  $c_k$  can be uniquely determined  recursively 
and  $1+\sum_{k=1}^{\infty}c_k z^{-k}$ is convergent  on some  neighbourhood of  infinity (see e.g.,  \cite{adams1928linear}).      Then we get
\begin{prop}\label{n=m+1an=0}
    Suppose the following condition holds  for  $a_1,...,a_{n-1},b_1,...,b_{n-1}$:
    \begin{equation*}
    a_i\neq 0,\  a_i/a_j\notin q^{\mathbb{Z}\backslash \{ 0 \} },\  \text{for} \   1\leq i , j \leq n-1, \ \text{and} \ b_l\neq   0, \ \text{for} \ 1\leq l \leq n-1,
\end{equation*}
then the equation \eqref{intro:conflu hyper eq} has a fundamental system of   formal  solutions around infinity:
\begin{align}
    \hat{f}_q(z)=&\left(
 \hat{f}_q(z)_{1} ,
...  ,
 \hat{f}_q(z)_{n-1}  ,
{f}_q(z)_{n}
\right)     \nonumber   \\
:=&
    \left(
 \hat{h}_q(z)_{1}\cdot z^{-\log_q a_1},
...  ,
 \hat{h}_q(z)_{n-1}\cdot   z^{-\log_q a_{n-1}  },
{h}_q(z)_{n} \cdot   \frac{z^{\sum_{l=1}^{n-1}\log_q\left(a_l/b_l\right)}}{(z;q)_\infty}
\right),    \label{eq:fqinfn}
\end{align}
with  
\begin{align}
   & \hat{h}_q(z)_{i}=  {}_n\varphi_{n-2}\left(\begin{array}{c}
			a_i, a_i q/b_1,...,a_i q/b_{n-1}\\
			a_i q/a_1,...,\widehat{a_i q/a_{{i}} },...,a_i q/a_{n-1}
		\end{array};  q, {\frac{\prod_{l=1}^{n-1} b_l}{ {a_i}z\prod_{l=1}^{n-1}a_l }}\right)  , \  \text{for} \ i=1,...,n-1,  \nonumber   \\
  &{h}_q(z)_{n}=1+ c_1 z^{-1}+c_2 z^{-2}+...,   \label{eq:qformalsol}
\end{align} 
with  $c_k$  uniquely determined  in a recursive way. 
The equation \eqref{intro:conflu hyper eq} also has a fundamental system of meromorphic solutions around the origin:
\begin{equation*}
    {f}^{(0)}_q(z)=\left(
 {f}^{(0)}_q(z)_{1} ,
...  ,
 {f}^{(0)}_q(z)_{n-1}  ,
{f}^{(0)}_q(z)_{n}
\right),
\end{equation*}
with  
\begin{align*}
&{f}^{(0)}_q(z)_{i}:={}_n\varphi_{n-1}\left( \begin{array}{c}
   qa_1/b_i,...,qa_{n-1}/b_i,0   \\
q^2/b_i,qb_1/b_i,...,\widehat{qb_i/b_i},...,qb_{n-1}/b_i  
\end{array}; q,z \right)z^{1-\log_qb_i},\  \text{for}\  i=1,...,n-1,\\
&{f}^{(0)}_q(z)_{n}:={}_n\varphi_{n-1}\left(\begin{array}{c}
a_1, a_2, ..., a_{n-1},0 \\
b_1, ..., b_{n-1}
\end{array} ; q, z\right).
\end{align*}
\end{prop}
