---
doc_id: arxiv-2412.02281v1
doc_title: "Explicit evaluation of the q -Stokes matrices for certain conﬂuent hypergeometric q -diﬀerence equations"
section_id: sec-014-behavior-of-the-connection-formula-as-q1
section_title: "Behavior of the Connection Formula as q1"
section_number: null
pages: 18-22
source_pdf: 2412.02281v1.pdf
source_sha256: ac4127cf4994b2ba
toc_source: outline
text_source: latex
latex_prose_ratio: 0.8
latex_coverage_ratio: 0.968
doc_brief: "Explicit evaluation of the q -Stokes matrices for certain conﬂuent hypergeometric q -diﬀerence equations — We prove a connection formula for the basic hypergeomtric function nϕn−1 (a1, ..., an−1, 0"
---
\label{subsec:eqlim}
We focus on the  behavior of  the connection formula   as $q\rightarrow 1$ of the equation
 \begin{equation}\label{sec:qconf eq}
    \prod_{l=1}^{n-1}\left(zD_q+\alpha_{l} \right)y(z)=D_q\prod_{l=1}^{n-1}\left(zD_q+\beta_{l}-1 \right)y(z),
\end{equation}
which takes the general  form of the equation \eqref{Fnj eq}.  See \cite{morita2013connection} for more discussion of  $n=2$ case.  If
    the   complex numbers    $\alpha_l\neq  \frac{1}{q-1}  $, $\beta_l\neq  \frac{q}{q-1} $,  for $1\leq l \leq  n-1$,  
we take the  parameters   $a_1,...,a_{n-1},b_1,...,b_{n-1}$           as  
\begin{align}
    &{a}_l=\frac{1}{1+(1-q)\alpha_l}, \  \text{for all}  \    1\leq l \leq   n-1,   \label{al change}  \\
     &{b}_l=\frac{q}{1+(1-q)(\beta_l-1)}, \  \text{for all}  \    1\leq l \leq   n-1.  \label{bl change}
\end{align}

Similar to the   case  of  \eqref{Fnj eq},   we have 
\begin{prop}
Given $a_l,b_l$, for $1\leq l \leq n-1$,   in \eqref{al change}, \eqref{bl change},    the solutions and the    connection formula of  \eqref{sec:qconf eq} are:
   \begin{itemize}
    \item   The  equation \eqref{sec:qconf eq}  admits the convergent solution:
    \begin{equation}
        \tilde{f}^{(0)}_q(z):={}_n\varphi_{n-1}\left(  \begin{array}{c}  a_1,...,a_{n-1},0\\
 b_1,...,b_{n-1}  \end{array};q,\frac{(1-q)z\prod_{l=1}^{n-1}{b_l}}{\prod_{l=1}^{n-1}{q}a_l}   \right).\label{tildef0qz}  
    \end{equation}
 \item  The equation \eqref{sec:qconf eq}  admits  the   fundamental system of meromorphic    solutions  around infinity:
 \begin{align}\label{tildefinfeq}
     \tilde{f}^{(\infty)}_q(z,\lambda)&=  \left(  \tilde{f}^{(\infty)}_q(z,\lambda)_1,...,\tilde{f}^{(\infty)}_q(z,\lambda)_{n-1},\tilde{f}^{(\infty)}_q(z)_n   \right) \nonumber  \\
    &:= \left(
 \frac{\tilde{h}^{(\infty)}_q(z,\lambda)_{1}}{z^{ \log_qa_1  }}  ,
...  ,
   \frac{\tilde{h}^{(\infty)}_q(z,\lambda)_{n-1}}{z^{ \log_qa_{n-1}  }},
\tilde{h}^{(\infty)}_q(z)_{n}  \frac{z^{\sum_{l=1}^{n-1}\log_qa_l}}{  z^{ \sum_{l=1}^{n-1}\log_qb_l   }  } e_q\left( \frac{z\prod_{l=1}^{n-1}{b_l}}{\prod_{l=1}^{n-1}{q}a_l}  \right)
\right)       ,
 \end{align}  
 with
 \begin{equation*}
     \tilde{h}^{(\infty)}_q(z,\lambda)_{i}={}_nf_{n-2}\left(\begin{array}{c}
			a_i, a_i q/b_1,...,a_i q/b_{n-1}\\
			a_i q/a_1,...,\widehat{a_i q/a_{{i}} },...,a_i q/a_{n-1}
		\end{array};  q,\frac{q^{n-1}\lambda}{(1-q)a_i}, \frac{q^{n-1}}{a_i(1-q)z}\right), \   \text{for} \  i=1,...,n-1,   
 \end{equation*}
and $\tilde{h}^{(\infty)}_q(z)_{n}$ is  a  convergent  power
series  whose coefficients can be uniquely determined recursively.
 \item  The solutions  $\tilde{f}^{(0)}_q(z)$  and   $\tilde{f}_q^{(\infty)}(z,\lambda)$   of \eqref{sec:qconf eq}  are related by the following connection formula
 \begin{equation}
     \tilde{f}^{(0)}_q(z)= \sum_{i=1}^{n-1} \tilde{f}^{(\infty)}_q(z,\lambda)_{i}  \tilde{C}_i(z)+\tilde{f}^{(\infty)}_q(z)_{n}  \tilde{C}_n(z,\lambda),\label{eq: qconnefomu}
 \end{equation}
 with for  $1\leq  i\leq n-1$,
 \begin{align*}
    & \tilde{C}_i(z):=\frac{(a_1,...,\widehat{a_{i} },...,a_{n-1},b_1/a_i,...,b_{n-1}/a_i;q)_\infty}{(b_1,...,b_{n-1},a_1/a_i,...,\widehat{a_{i}/a_i},...,a_{n-1}/a_i;q)_\infty}\frac{\theta_q\left(-a_i {(1-q)z\prod_{l=1}^{n-1}{b_l}}\big/{\prod_{l=1}^{n-1}{q}a_l}\right)}{ \theta_q\left(-{(1-q)z\prod_{l=1}^{n-1}{b_l}}\big/{\prod_{l=1}^{n-1}{q}a_l}\right) }z^{ \log_q a_i  },\\
    &\tilde{C}_n(z,\lambda)
  
		
  :=\frac{(a_1,...,a_{n-1};q)_\infty}{(b_1,...,b_{n-1};q)_\infty}  \frac{\prod_{l=1}^{n-1}\theta_q\left( {b_l (1-q)}\big/{ (q^{n-1}  \lambda) }   \right)}{\prod_{l=1}^{n-1}\theta_q\left( {  a_l(1-q) }\big/{ (q^{n-1} \lambda )}     \right)} \frac{\theta_q\left(   {  { \lambda  }  z\prod_{l=1}^{n-1}{b_l}}\big/{\prod_{l=1}^{n-1}a_l}     \right)}{\theta_q\left( \lambda z   \right)}  
		\frac{z^{\sum_{l=1}^{n-1}\log_qb_l  }}{ z^{ \sum_{l=1}^{n-1}\log_qa_l }  }. 
 \end{align*}
   \end{itemize}
   \end{prop}






 The  equation     \eqref{sec:qconf eq} converges  in the form  to  the  confluent hypergeometric differential equation  
\begin{equation}\label{c h eq}
    \prod_{l=1}^{n-1}\left(z\frac{\mathrm{d}}{\mathrm{d}z}+\alpha_{l} \right)y(z)=\frac{\mathrm{d}}{\mathrm{d}z}\prod_{l=1}^{n-1}\left(z\frac{\mathrm{d}}{\mathrm{d}z}+\beta_{l}-1 \right)y(z).
\end{equation}
It is well known that  there is a fundamental system of formal solutions around infinity  of  \eqref{c h eq}  (see  e.g., \cite{balser2008formal, turrittin1955convergent}):
\begin{equation*}
        \hat{f}(z):=\left(
 \hat{h}_{1}(z) z^{-\alpha_1},
...  ,
 \hat{h}_{n-1}(z) z^{-\alpha_{n-1}  } ,
\hat{h}_{n}(z)  \mathrm{e}^z z^{  \sum_{l=1}^{n-1}\left(\alpha_l-\beta_l\right)  }
\right),
   \end{equation*}
   with
\begin{align*}
  & \hat{h}_i(z):= {}_{n}F_{n-2}\left(\alpha_i,1+\alpha_i-\boldsymbol{\beta};1+\alpha_i-\boldsymbol{\alpha_{\hat{i}}};-z^{-1} \right), \  \text{for} \  i=1,...,n-1,\\
  &  \hat{h}_n(z):= 1+ \sum_{m=1}^{\infty}\kappa_m z^{-m},
\end{align*}







where   $\kappa_m$  can be uniquely determined recursively.  Here we use  index notations 
\begin{align*}
    &1+\alpha_i-\boldsymbol{\beta}:=( 1+\alpha_i-\beta_1,..., 1+\alpha_i-\beta_{n-1} ),\\
    &1+\alpha_i-\boldsymbol{\alpha_{\hat{i}}}:=\Big( 1+\alpha_i-\alpha_1,...,\widehat{1+\alpha_i-\alpha_i},...,1+\alpha_i-\alpha_{n-1} \Big),
\end{align*}
and  $\widehat{1+\alpha_i-\alpha_i}$ means that this term is skipped.

The standard theory of Borel resummation (see e.g., \cite{balser2008formal, loday2016divergent, Wasow})  states that   
\begin{prop}
     On $\mathrm{Sect}_{+}:=S\left(-\pi/2,3\pi/2 \right)$ and $\mathrm{Sect}_-:=S\left(-3\pi/2,\pi/2 \right)$ (recall the notation  $S\left(a,b\right)$ in Section \ref{sec:q-borel sum}),     there exist a  fundamental system of  meromorphic   solutions around infinity of  \eqref{c h eq}
    \begin{equation}\label{eqfinfpm}
    {f}^{(\infty)}_{\pm}(z):=\left(
 {h}^{(\infty)}_{\pm,1} z^{-\alpha_1},
...  ,
 {h}^{(\infty)}_{\pm,n-1} z^{-\alpha_{n-1}  } ,
{h}^{(\infty)}_{\pm,n}  \mathrm{e}^z z^{  \sum_{l=1}^{n-1}\left(\alpha_l-\beta_l\right)  }
\right),
\end{equation}
    such that the  asymptotic expansions hold
\begin{align*}
    &{h}^{(\infty)}_{\pm,i} \sim {}_{n}F_{n-2}\left(\alpha_i,1+\alpha_i-\boldsymbol{\beta};1+\alpha_i-\boldsymbol{\alpha}_{\hat{i}};-z^{-1} \right),\ \text{as} \ z \rightarrow \infty \ \text{on}\ \mathrm{Sect}_{\pm}, \  \text{for} \ i=1,...,n-1,  \\
    
     &{h}^{(\infty)}_{\pm,n} \sim 1+\sum_{m=1}^{\infty}\kappa_m z^{-m},\ \text{as} \ z \rightarrow \infty \ \text{on}\ \mathrm{Sect}_{\pm}.
\end{align*}
\end{prop}
\begin{defn}\label{def:hi}
For  $1\leq i \leq n-1$,        the  analytic continuation of the    function   ${h}^{(\infty)}_{+,i}(z)$  defined on  $\mathrm{Sect}_{+}$  to   $\widetilde{C^*}$  is denoted as ${h}^{(\infty)}_{i}$.
\end{defn}
Moreover, there is a convergent   solution around the origin of \eqref{c h eq} of the form (see e.g., \cite{OLBC})
\begin{equation*}
    f^{(0)}(z):= {}_{n-1}F_{n-1}\left(\alpha_1,...,\alpha_{n-1};\beta_1,...,\beta_{n-1};z\right).
\end{equation*}
From \cite{ichinobe2001borel, OLBC},  one knows  that  
\begin{prop}[{\cite[Theorem 2.1]{ichinobe2001borel}}]\label{prop:hpm}
 For $1\leq i \leq n-1$,   



     ${h}^{(\infty)}_{\pm,i}$  is given by  (here for convenience, we denote $\beta_n=1$) 
\begin{align*}
{h}^{(\infty)}_{\pm,i}










=&\sum_{k=1}^{n}   \frac{\prod_{l=1,l\neq i}^{n-1}\Gamma(1+\alpha_i-\alpha_l)  \prod_{l=1  ,l\neq  k }^{n}\Gamma(\beta_k -\beta_l )}{\prod_{l=1,l\neq  k}^{n}\Gamma( 1+\alpha_i-\beta_l  )  \prod_{l=1,l\neq i}^{n-1}\Gamma(\beta_k -\alpha_l )}    z^{1+\alpha_i-\beta_k} \\
&\times {}_{n-1}F_{n-1} \left(\begin{array}{c}
  1+\alpha_1 -\beta_k ,...,  1+\alpha_{n-1} -\beta_k    \\
1+\beta_1-\beta_k   ,...,\widehat{{1+\beta_k -\beta_k }},..., {1+\beta_n-\beta_k   }
 \end{array};{z}\right),
\end{align*}
as  $z\in \mathrm{Sect}_{\pm}$.
As a result,  for $1\leq i \leq  n-1$,  we  have
\begin{equation*}
        {h}^{(\infty)}_{+,i}={h}^{(\infty)}_{-,i}, \  \text{as} \  z\in S(-\pi/2,\pi/2  ),
    \end{equation*}
    and  ${h}^{(\infty)}_{i}$ is also the analytic continuation of   ${h}^{(\infty)}_{-,i}$.
\end{prop}
\begin{prop}[see e.g., {\cite[Chapter 16]{OLBC}}]
    For  $z\in \mathrm{Sect}_{\pm}$,   the solutions  ${f}^{(0)}(z)$  and  ${f}^{(\infty)}_{\pm}(z)$    of \eqref{c h eq}  are related by the following connection formula:
 \begin{equation}\label{olbcconne}
f^{(0)}(z)=\sum_{i=1}^{n-1} \frac{\prod_{l=1}^{n-1}\Gamma\left(\beta_l\right)}{\prod_{l=1,l\neq i}^{n-1}\Gamma\left(\alpha_l\right)}  \frac{\prod_{l=1,l\neq i}^{n-1}\Gamma\left(\alpha_l-\alpha_i\right)}{\prod_{l=1}^{n-1}\Gamma\left(\beta_l-\alpha_i\right)}{ \mathrm{e}^{\pm\pi \mathrm{i} \alpha_i}  } {h}^{(\infty)}_{\pm,i} z^{-\alpha_i}+\frac{\prod_{l=1}^{n}\Gamma\left(\beta_l\right)}{\prod_{l=1}^{n}\Gamma\left(\alpha_l\right)}     {h}^{(\infty)}_{\pm,n}  \mathrm{e}^z z^{  \sum_{l=1}^{n-1}\left(\alpha_l-\beta_l\right)  }.
\end{equation}
\end{prop}





The  connection formula \eqref{eq: qconnefomu}    recovers the    connection formula \eqref{olbcconne} in the following sense.  That  is,
\begin{prop}\label{prop:lim eq}
 As  $q\rightarrow 1$,  it follows that  
 \begin{itemize}
\item[(1)]       The  convergent  solution  $\tilde{f}^{(0)}_q(z)$ (see \eqref{tildef0qz})  of  \eqref{sec:qconf eq}  converges to         the convergent  solution $f^{(0)}(z)$  of  \eqref{c h eq}:
\begin{equation}
 \lim_{q\rightarrow 1} \tilde{f}^{(0)}_q(z)= f^{(0)}(z).\label{lim:zero}
\end{equation} 
\item[(2)]  The coefficients  $\tilde{C}_1(z),...,\tilde{C}_{n-1}(z),\tilde{C}_n(z,\lambda)$ have limits:
\begin{align}
     &\lim_{q\rightarrow 1}\tilde{C}_i(z)=\frac{\prod_{l=1}^{n-1}  \Gamma(\beta_l) \prod_{l=1,l\neq  i}^{n-1} \Gamma( \alpha_l -\alpha_i )  }{\prod_{l=1,l\neq  i}^{n-1}  \Gamma( \alpha_l )  \prod_{l=1}^{n-1} \Gamma( \beta_l-\alpha_i  )}  \cdot       \mathrm{e}^{ \pm \mathrm{i}  \pi  \alpha_i },   \  \text{for}  \   1\leq  i\leq  n-1,  \label{tildeCi} \\
     &\lim_{q\rightarrow 1}\tilde{C}_n(z,\lambda)     =\frac{ \prod_{ l=1 }^{n-1}\Gamma(   \beta_l   )  }{ \prod_{ l=1 }^{n-1}\Gamma(   \alpha_l   )  }.  \label{tildeCn}
\end{align}
In \eqref{tildeCi},  \eqref{tildeCn} we take  $ \mathrm{arg}(\lambda)\in(-\pi,\pi)$  and  $\mathrm{arg}(z)\in  (-\mathrm{arg}(\lambda)-\pi,-\mathrm{arg}(\lambda)+\pi)$.  The  positive    or   negative  sign in \eqref{tildeCi}  is   chosen based on whether    $\mathrm{arg}(z)\in (0,-\mathrm{arg}(\lambda)+\pi  )$  or  $\mathrm{arg}(z)\in (-\mathrm{arg}(\lambda)-\pi, 0  )$.  
\item[(3)]     The fundamental system of meromorphic solutions  $ \tilde{f}_q^{(\infty)}(z,\lambda)$  (see  \eqref{tildefinfeq})   of  \eqref{sec:qconf eq}  converges to the fundamental system of meromorphic solutions  ${f}^{(\infty)}_{ \pm }(z)$   (see \eqref{eqfinfpm})  of  \eqref{c h eq}:
\begin{align}
 &\lim_{q\rightarrow 1}   \tilde{f}_q^{(\infty)}(z,\lambda)_i=h^{(\infty)}_i(z)  z^{-\alpha_i },   \  \text{as} \  \mathrm{arg}(z)\in  (-\mathrm{arg}(\lambda)-\pi,-\mathrm{arg}(\lambda)+\pi  ),   \  \text{for}  \  i=1,...,n-1,  \label{tildeflim} \\
 &\lim_{q\rightarrow 1} \tilde{f}^{(\infty)}_q(z)_n =\left\{
          \begin{array}{lr}
          {h}^{(\infty)}_{+,n}  \mathrm{e}^z z^{  \sum_{l=1}^{n-1}\left(\alpha_l-\beta_l\right)  },   & \text{if} \ \  \mathrm{arg}(z)\in (0,-\mathrm{arg}(\lambda)+\pi  ), \\
             {h}^{(\infty)}_{-,n}  \mathrm{e}^z z^{  \sum_{l=1}^{n-1}\left(\alpha_l-\beta_l\right)  }    , & \text{if} \ \ \mathrm{arg}(z)\in (-\mathrm{arg}(\lambda)-\pi, 0  ).
             \end{array}
\right.\label{tildeflim2eq}
\end{align}
\item[(4)]  If $\mathrm{arg}(z)\in (0,-\mathrm{arg}(\lambda)+\pi  )$,  the connection formula \eqref{eq: qconnefomu}  recovers \eqref{olbcconne} with the positive sign chosen in \eqref{olbcconne}, and if $\mathrm{arg}(z)\in (  -\mathrm{arg}(\lambda)-\pi ,0  )$,  the connection formula \eqref{eq: qconnefomu}  recovers \eqref{olbcconne} with the negative sign chosen in \eqref{olbcconne}.   
 \end{itemize}

 
\end{prop}
  To prove Proposition \ref{prop:lim eq},  we  need the following lemmas.
\begin{lemma}[see e.g., {\cite[Section 5]{askey1978q}, \cite[Section 1.10]{ gasper2004basic}}]\label{basic lim}
As  $q\rightarrow 1$,  we  have
\begin{align*}
  &  \lim_{q\rightarrow 1}  \log_q(1+(1-q)\alpha)=-\alpha, \ \text{for}  \   \alpha\neq 1/(q-1),\\
  &\lim _{q \rightarrow 1} e_q(z)=\mathrm{e}^z,\\
  &  \lim _{  
    q  \rightarrow 1
	  }  \Gamma_q(z)=\Gamma(z),                  \\
  &  \lim_{q\rightarrow 1}  \frac{\theta_q( q^{\beta} z )}{ \theta_q( q^{\alpha} z )  } =z^{\alpha-\beta},  \  \text{for} \  z\in  \mathbb{C}^*\backslash \mathbb{R}_{<0}.  
\end{align*}
Here  we  take  $-\pi<\mathrm{arg}(z)<\pi$  in the the power function  $z^{\alpha-\beta}$.
\end{lemma}










\begin{lemma}\label{lem:limf}
For $i=1,...,n-1$,    as $q\rightarrow 1$, we have the limit:
    \begin{equation}\label{expre:qlimf}
        \lim_{q\rightarrow 1}  {}_n f_{n-2}\left(\begin{array}{c}
          a_i, a_i q/b_1,...,a_i q/b_{n-1}\\
			a_i q/a_1,..., \widehat{ a_i q/a_{{i}} },...,a_i q/a_{n-1}
        \end{array}  ;\frac{q^{n-1}\lambda}{(1-q)a_i}; q, {\frac{ q^{n-1} }{ {a_i}{(1-q)z  }  }} \right)= {h}^{(\infty)}_{i}(z). 
    \end{equation}
  Here  in  the left side of \eqref{expre:qlimf} (a single-valued function), the variable  $z\in \mathbb{C}^*\backslash  - \lambda \mathbb{R}_{>0}$,   and  in the right side,  we   take the branch   of the multi-valued function    ${h}^{(\infty)}_{i}(z)$ (given in Definition \ref{def:hi})  with   $\mathrm{arg}(z)\in  (-\mathrm{arg}(\lambda)-\pi,-\mathrm{arg}(\lambda)+\pi  )$.  Here   we take $\mathrm{arg}(\lambda)\in (-\pi,\pi)$.
\end{lemma}
\begin{proof}
    From  Lemma \ref{Adachi}  and    Lemma \ref{basic lim},  we have  (here for convenience, we denote $b_n=q,\beta_n=1$) 
   
   
   
   
   
   
   
   
   
   
   
    \begin{align*}
     &   \lim_{q\rightarrow 1}   {}_n f_{n-2} \left(\begin{array}{c}
           a_i, a_i q/b_1,...,a_i q/b_{n-1}\\
			a_i q/a_1,..., \widehat{ a_i q/a_{{i}} },...,a_i q/a_{n-1} 
        \end{array}  ;  \frac{q^{n-1}\lambda}{(1-q)a_i}; q, {\frac{ q^{n-1} }{ {a_i}{(1-q)z  }  }}  \right)\\
        =&\lim_{q\rightarrow 1} \sum_{k=1}^n \frac{ \prod_{l=1,l\neq i}^{n-1}  \Gamma_q( \log_q( a_iq/a_l ) )  \prod_{l=1,l\neq  k}^n  \Gamma_q(\log_q( a_iq/b_l ) -\log_q( a_iq/b_k ) ) }{  \prod_{l=1,l\neq k}^n  \Gamma_q(    \log_q(a_iq/b_l  ) ) \prod_{l=1,l\neq i}^{n-1}\Gamma_q( \log_q( a_iq/a_l )-\log_q( a_i q/b_k ) )  } 
        \frac{\left( {z\lambda}  \right)^{\log_q( a_iq/b_k  )}}{ (1-q)^{ \log_q( a_iq/b_k  ) }  }      \\
        &\times \left(\frac{q^{n-1}\lambda}{(1-q)a_i}\right)^{-\log_q a_i  }     { }_n\varphi_{n-1}\left(\begin{array}{c}
   a_iq/b_k,a_1q/b_k,...,\widehat{a_iq/b_k},...,a_{n-1}q/b_k , {0} \\
 b_1q/b_k,...,\widehat{b_kq/b_k},...,b_nq/b_k
  \end{array} ;q, \frac{(1-q)z\prod_{l=1}^n b_l}{q^n\prod_{l=1}^{n-1}a_l}\right)   \\
        =&  \sum_{k=1}^n   \frac{ \prod_{l=1,l\neq i}^{n-1}  \Gamma( 1+\alpha_i-\alpha_l )  \prod_{l=1,l\neq  k}^n  \Gamma(   \beta_k-\beta_l   ) }{  \prod_{l=1,l\neq k}^n  \Gamma( 1+\alpha_i-\beta_l ) \prod_{l=1,l\neq  i}^{n-1}\Gamma( \beta_k -\alpha_l     )  }   \\
    &\times   z ^{1+\alpha_i-\beta_k}    {}_{n-1}F_{n-1}\left( \begin{array}{c}
        1+\alpha_1-\beta_k,...,1+\alpha_{n-1}-\beta_k  \\
         1+\beta_1-\beta_k,...,\widehat{1+\beta_k-\beta_k},...,1+\beta_n-\beta_k
        \end{array}       ;{z} \right)  , 
    \end{align*}
    where  we  take    $\mathrm{arg}{(\lambda)}\in  (-\pi,\pi)$  and   $\mathrm{arg}(z)\in  (-\mathrm{arg}(\lambda)-\pi,-\mathrm{arg}(\lambda)+\pi  )$.     Comparing the above formula and  Proposition    \ref{prop:hpm},  we obtain this proposition.
\end{proof}




\begin{proof}[Proof of Proposition \ref{prop:lim eq}]
The proof contains the following parts    ($a_1,...,a_{n-1},b_1,...,b_{n-1}$    given in  \eqref{al change}, \eqref{bl change}):
\begin{itemize}
    \item The formula \eqref{lim:zero}  is  derived from direct computations.
    \item      The  formula \eqref{tildeCi}    is  derived from    Lemma \ref{basic lim}  and   the following two formulas:
    \begin{equation*}
      \frac{\prod_{l=1,l\neq  i}^{n-1}(a_l;q)_{\infty}\prod_{l=1}^{n-1}(b_l/a_i;q)_\infty}{\prod_{l=1}^{n-1}(b_l;q)_{\infty}\prod_{l=1,l\neq  i}^{n-1}(a_l/a_i;q)_\infty} = (1-q)^{\log_q  a_i} \frac{\prod_{l=1}^{n-1}  \Gamma_q(\log_qb_l) \prod_{l=1,l\neq  i}^{n-1} \Gamma_q( \log_qa_l -\log_q a_i )  }{\prod_{l=1,l\neq  i}^{n-1}  \Gamma_q( \log_qa_l )  \prod_{l=1}^{n-1} \Gamma_q( \log_q b_l-\log_q a_i  )} , 
      \end{equation*}
    and
      \begin{align}
        
        & \lim_{q\rightarrow 1} (1-q)^{ \log_q a_i }   \frac{\theta_q\left( -  {   (1-q)a_i  z\prod_{l=1}^{n-1}{b_l}}\big/{\prod_{l=1}^{n-1}{q}a_l} \right)}{  \theta_q\left( -{(1-q)z\prod_{l=1}^{n-1}{b_l}}\big/{\prod_{l=1}^{n-1}{q}a_l} \right)    }  z^{ \log_q a_i  }   \nonumber \\
         =& \lim_{q\rightarrow 1}  \frac{(1-q)^{\log_q a_i }  z^{\log_q a_i  } }  {\left(-  {   (1-q)z\prod_{l=1}^{n-1}{b_l}}\big/{\prod_{l=1}^{n-1}{q}a_l} \right)^{ \log_q a_i }}  \nonumber  \\
            =&  \mathrm{e}^{ \pm \mathrm{i}  \pi  \alpha_i }  \label{pf:lim1}.
    \end{align}
    The  positive    or   negative  sign in \eqref{pf:lim1}  is   chosen based on whether    $\mathrm{arg}(z)\in (0, -\mathrm{arg}(\lambda)+\pi  )$  or  $\mathrm{arg}(z)\in ( -\mathrm{arg}(\lambda)-\pi, 0  )$.     And   the  formula \eqref{tildeCn}    is  derived from Lemma \ref{basic lim}  and the following two formulas:
    \begin{align}
     &   \frac{(a_1,...,a_{n-1};q)_\infty}{(b_1,...,b_{n-1};q)_\infty}  = \frac{ (1-q)^{ \sum_{l=1}^{n-1}\log_q b_l } }{  (1-q)^{ \sum_{l=1}^{n-1}\log_q a_l  } }  \frac{ \prod_{ l=1 }^{n-1}\Gamma_q( \log_qb_l   )  }{ \prod_{ l=1 }^{n-1}\Gamma_q( \log_qa_l   )  } ,\nonumber  \\
     
     & \lim_{q\rightarrow 1} \frac{ (1-q)^{ \sum_{l=1}^{n-1}\log_q b_l } }{  (1-q)^{ \sum_{l=1}^{n-1}\log_q a_l  } }\frac{\prod_{l=1}^{n-1}\theta_q\left( {b_l (1-q)  }\big/{ (q^{n-1}  \lambda )}   \right)}{\prod_{l=1}^{n-1}\theta_q\left( {  a_l(1-q) }\big/{ (q^{n-1} \lambda) }     \right)}  \frac{\theta_q\left(   { \lambda  z\prod_{l=1}^{n-1}{b_l}}\big/{\prod_{l=1}^{n-1}a_l}     \right)}{\theta_q\left( { \lambda  }  {z}       \right)}   \frac{{ z}^{\sum_{l=1}^{n-1}\log_qb_l  }}{ {  z }^{ \sum_{l=1}^{n-1}\log_qa_l }  } \nonumber \\
     =&\lim_{q\rightarrow 1}  \frac{ (1-q)^{ \sum_{l=1}^{n-1}\log_q b_l } }{  (1-q)^{ \sum_{l=1}^{n-1}\log_q a_l  } } \frac{\left({ ( 1-q) }/{  \lambda }\right)^{\sum_{l=1}^{n-1}\log_q \left(a_l\right)} }{\left({ ( 1-q) }/{  \lambda }\right)^{\sum_{l=1}^{n-1}\log_q \left(b_l\right)}} \frac{\left( \lambda z \right)^{\sum_{l=1}^{n-1}\log_q a_l}}{\left( \lambda z \right)^{\sum_{l=1}^{n-1}\log_q b_l}}    \frac{{ z}^{\sum_{l=1}^{n-1}\log_qb_l  }}{ {  z }^{ \sum_{l=1}^{n-1}\log_qa_l }  }   \nonumber  \\
     =&1.  \label{pf:lim2}
    \end{align}
      In \eqref{pf:lim2}  we take  $ \mathrm{arg}(\lambda)\in(-\pi,\pi)$  and  $\mathrm{arg}(z)\in  (-\mathrm{arg}(\lambda)-\pi,-\mathrm{arg}(\lambda)+\pi)$.
      \item  The formula \eqref{tildeflim} is derived from Lemma  \ref{lem:limf}, and  the formula \eqref{tildeflim2eq} is derived from \eqref{olbcconne},   \eqref{lim:zero}-\eqref{tildeflim}.
      \item  From \eqref{lim:zero}-\eqref{tildeflim2eq}, it follows that \eqref{eq: qconnefomu} recovers \eqref{olbcconne} as stated in this proposition.
\end{itemize}
\end{proof}
