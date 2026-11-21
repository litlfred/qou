---
doc_id: arxiv-1908.07065v3
doc_title: "Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-009-41-review-of-instanton-calculus
section_title: "Review of instanton calculus"
section_number: 4.1
pages: 21-25
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.992
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve of N = 2, SU(2) super Yang–Mills"
---
\label{ic}

Let us first review some basic ingredients of instanton calculus in
the 4d $N=2$ SYM with gauge group $G=SU(N)$ \cite{n,no2,ns,
  Flume:2002az, bfmt}.

We denote a partition (or  Young tableaux) by
\be Y=(y_1, y_2, \cdots),\ee 
 its transposed by
\be Y^t=(y_1^t, y_2^t, \cdots),\ee
and a vector of Young tableaux as
\begin{equation}
  \label{Y-vec}
  \boldsymbol{Y}=(Y_1, \cdots, Y_N). 
\end{equation}

It is useful to  define

\begin{equation}
  h_Y(s)=y_i-j, \qquad v_Y(s)= y^t_j-i, 
\end{equation}
where $ s=(i,j) $ is a  box (not necessarily in the
partition $Y$). We will also use 


\begin{equation}\label{ly}
  \ell( \boldsymbol{Y})= \sum_{I=1}^N \ell(Y_I) \ ,
\end{equation}
whith
\begin{equation}
  \ell(Y)= \sum_i y_i \ .
\end{equation}

The four dimensional   $SU(N)$ Nekrasov partition function is \cite{n, Flume:2002az}
\be
\label{z4d}
Z (\bs{a}; \epsilon_1, \epsilon_2)=\sum_{\boldsymbol{Y}}  \left((-1)^N
  \Lambda^{2N} \right)^{\ell (\boldsymbol{Y})}  \CZ_{\boldsymbol{Y}},  
\ee

where 

\be
\ba
\label{zdef}\CZ_{\bs{Y}}&=\prod_{I,J=1}^N \prod_{s \in Y_I} {1\over \alpha_I -\alpha_J -\epsilon_1 v_{Y_J}(s) +\epsilon_2 \left( h_{Y_I}(s)+1 \right)} \\
&\qquad \qquad \times  \prod_{s\in Y_J}
{1\over \alpha_I -\alpha_J +\epsilon_1 \left(v_{Y_I}(s)+1\right){-} \epsilon_2 h_{Y_J}(s)},
\ea
\ee
with
\be  \sum_{i=1}^N \alpha_i=0, \ee
and 
\be a_i=\alpha_{i}-\alpha_{i+1} , \quad i=1,\cdots, N-1.\ee

The  four dimensional   $SU(N)$ Nekrasov-Shatashvili (NS) free energy is then defined by \cite{ns}

\begin{equation}
\label{fns4d}
F_{\rm NS}^{\rm inst}(\bs{a}, \hbar) =\ri \hbar \, \lim_{\epsilon_2
  \rightarrow 0} \, \epsilon_2 \log Z(\bs{a}; \ri \hbar , \epsilon_2).
\end{equation}

An important property of this free energy is that it is given as a
power series in $\Lambda$ which is expected to have a non-vanishing
radius of convergence in a certain range of values of $a$ and $\hbar$
around the semiclassical region $|\Lambda/a| \ll 1$\footnote{Recall
  that for $\hbar = 0$, in the electric frame both $a(u)$ and $a_D(u)$
  are convergent series of $\Lambda^2/u$ up to the monopole and dyon
  points.  The prepotential, which is related to $a,a_D$ by the
  special geometry relation, is thus also convergent series of
  $\Lambda/a$ up to these points.  The NS free energy is its smooth
  deformation which tends to enlarge the domain of convergence.}.
 
In order to make contact with the (modified) Mathieu equation, the relevant
gauge theory is $\CN=2$, $SU(2)$ SYM theory, hence we
have to consider \eqref{fns4d} with $N=2$. In this case the first few
terms read

\begin{equation}
  \label{inst} \ba F_{\rm NS}^{\rm inst}(a, \hbar)=-\frac{2 \Lambda
    ^4}{a^2+\hbar ^2}+ \frac{\Lambda ^8 \left(7 \hbar ^2-5
      a^2\right)}{\left(a^2+\hbar ^2\right)^3 \left(a^2+4 \hbar
      ^2\right)}+\CO\left(\Lambda ^{16}\right).\ea
\end{equation}

Once the NS free energy is known, the quantum
$A$ period $a(u,\hbar)$ can be obtained by inverting the quantum
Matone relation \cite{acdkv,lmn,francisco,bk,bkk,fm-wilson,sciarappa1} 

\begin{equation}
  \label{mmap}u= {a^2\over 8}-{\Lambda \over 8}
  \partial_{\Lambda}F_{\rm NS}^{\rm inst}(a, \hbar, \Lambda).
\end{equation}

This leads to a series expansion for $a(u, \hbar)$ in powers of
$\Lambda^{4}$ which is expected to converge in an appropriate range of the parameters $\Lambda$, $E$, $\hbar$ around the semiclassical region $|\Lambda^2/E| \ll 1$.  The quantum
$B$ period $a_D(u,\hbar)$ is then obtained from the quantum special geometry relation

\begin{equation}
  \ba a_D(a, \hbar)=\partial_{a}F_{\rm NS}(a, \hbar, \Lambda)=& 2
  \gamma (a,\hbar,\Lambda )+\partial_{a}F_{\rm NS}^{\rm inst}(a,
  \hbar, \Lambda)\\ 




  \ea
\end{equation}

where \cite{hm}

\begin{equation}
  \label{gammadef}
  \gamma (a,\hbar )=\frac{a}{2}  \log \left({\hbar ^2\over
        \Lambda^2}\right)-\frac{\pi \hbar }{4}-\frac{\ri
  \hbar }{2}  \left(\log \Gamma\left(1+\frac{\ri a}{\hbar }\right)-\log
    \Gamma\left(1-\frac{\ri a}{\hbar }\right)\right) \ ,
\end{equation}

and we replace $a$ by $a(u,\hbar)$.


We also note that it is possible to express the NS free energy via a
TBA system \cite{ns,kt2} (different from the one discussed in
section~\ref{sc:SW-TBA}). This TBA system however has a range of
validity/convergence which is smaller than the one of the instanton
calculus. For instance, the TBA breaks down if ${\rm Re}(a)\neq 0$,
while the instanton counting expression for $F_{\rm NS}^{\rm inst}$
\eqref{fns4d} is still well defined.


 
It was found in \cite{mirmor} that by expanding \eqref{inst},
\eqref{mmap} at small values of $\hbar$, it is possible to recover the
WKB periods \eqref{QP}. More precisely, at order $\hbar^{2n}$, one
finds an expansion in $\Lambda$ which agrees with the expansion of
$\Pi^{(n)}(E)$ at large $E$: 



\begin{equation}
  \label{limit}
  \ba
  &2 \pi \, a(u,\hbar)\longrightarrow \sum_{n=0}^\infty \hbar^{2n}
    \Pi_A^{(n)} (E=2u), \\ 
  & 2 \ri \, a_D(a(u,\hbar), \hbar)= 2 \ri \partial_a( F_{\rm NS}(a,
  \hbar))\Big|_{a= a(u,\hbar)}\longrightarrow 
\sum_{n=0}^\infty \hbar^{2n} \Pi_B^{(n)} (E=2u).
  \ea
\end{equation}

Therefore, the Bethe/gauge correspondence provides an analytic way to
resum the WKB periods period into well defined functions which are
exact in $\hbar$. We will denote these functions by
$\Pi_{A, B}^{\rm ex}(E, \hbar)$, and we will refer to them as ``exact"
quantum periods. In terms of the quantities that we have introduced,
they are given by

\be\label{abpe}  
\ba
\Pi^{\rm ex}_A(E, \hbar)&=2 \pi a(E,\hbar), \\
\Pi_B^{\rm ex}(E, \hbar) &={ 2 \ri }\partial_{a}F_{\rm NS}(a (E, \hbar),\hbar),
\ea
\ee

where we use the notation $a(E,\hbar):=a(u=E/2,\hbar)$.

It turns out that one can find the series expansion for $a(u, \hbar)$
by using elementary methods.  To do this, we use the WKB method, but we solve the Riccati
equation \eqref{riccati} perturbatively in $\Lambda$, i.e.\ we solve

\be
 Y^2(x)-\ri \hbar\frac{\rd Y(x)}{\rd x}=E- 2\Lambda^2 \cosh(x) 
\end{equation}

with an ansatz

\be
Y(x) = \sum_{n \ge 0} Y_n (x, \hbar, E) \Lambda^{2n}. 
\ee

Clearly, we should set 

\be
Y_0(x, \hbar, E)= {\sqrt{E}}, 
\ee
The equation for $Y_1(x, \hbar, E)$ is 

\be
2 Y_0 Y_1 -{\ri \hbar} {\rd Y_1 \over \rd x}= - 2 \cosh(x). 
\ee

The general solution to this equation is of the form 

\be
Y_1(x, \hbar, E)= -{4 {\sqrt{E}} \cosh(x) + 2 \ri \hbar \sinh(x) \over 4 E+ \hbar^2} + c \re^{-{2 \ri {\sqrt{E}} x\over \hbar}}. 
\ee

We note that the term involving the unknown coefficient leads to a
non-perturbative effect in $\hbar$. We will set it to zero to recover
the perturbative series.  The general term $Y_n$ satisfies

\be
2 {\sqrt{E}} Y_n(x, \hbar, E) -\ri \hbar {\rd Y_n \over \rd x}+\sum_{k=1}^{n-1} Y_k(x, \hbar, E) Y_{n-k}(x, \hbar, E)=0. 
\ee

This can be integrated order by order, setting to zero non-perturbative terms. We find in this way, 

\be
Y_2(x, \hbar, E)= -\frac{4 E^2+5 E \hbar ^2+\ri {\sqrt{E}}  \hbar  \left(8 E-\hbar ^2\right)
   \sinh (2 x)+E \left(4 E-5 \hbar ^2\right) \cosh (2 x)+\hbar ^4}{{\sqrt{E}}
    \left(E+\hbar ^2\right) \left(4 E+\hbar ^2\right)^2}. 
    \ee
    
    The functions $Y_n(x, \hbar, E)$ are complicated, but their integrals are slightly
    simpler. As it follows from (\ref{eq:PiA0}), we have to calculate
    
    \be
  \CI_n (E, \hbar)=  {1\over 2 \pi} \int_{-\pi}^\pi Y_n (\ri x, \hbar, E) \rd x. 
    \ee
    
As expected, only even terms contribute. We find, for example, 
 
 \be
   \ba
   \CI_2(E, \hbar)&=  -\frac{1}{4 E^{3/2}+{\sqrt{E}}  \hbar ^2}, \\
   \CI_4(E, \hbar)&=-\frac{60 E^2+35 E \hbar ^2+2 \hbar ^4}{4 E^{3/2} \left(E+\hbar
   ^2\right) \left(4 E+\hbar ^2\right)^3}, \\
   \CI_6(E, \hbar)&=-\frac{6720 E^5+18480E^4 \hbar ^2+15260 E^3 \hbar ^4+4705 E^2
   \hbar ^6+413 E \hbar ^8+18 \hbar ^{10}}{4 E^{5/2} \left(E+\hbar
   ^2\right)^2 \left(4 E+\hbar ^2\right)^5 \left(4 E+9 \hbar
   ^2\right)},
   \ea
   \ee
   
   and so on. Then, one finds
   
   \be
   \label{aseries}
  a(E, \hbar)= 2\left(\sqrt{E} + \sum_{m=1}^{\infty} \CI_{2m}(E, \hbar) \Lambda^{4m}\right).
   \ee
   
When $\hbar=0$, we recover the standard SW period \eqref{eq:PiA0}: 
   
   \be
2 \pi a (E, 0)=4 \pi{\sqrt{2+E}} ~_2 F_1\left( -{1\over 2}, {1\over 2}, 1; {4 \over 2+E}\right)={8} {\sqrt{2\Lambda^2+E}~} {\bf E}\left( {4\Lambda^2 \over {2\Lambda^2+E}} \right). 
   \ee
   
  At finite $\hbar, \Lambda$ we also find perfect agreement between \eqref{aseries} and the standard result of instanton calculus. 
  
  
  We note that the integrals above can be calculated as residues, since 
  
  \be
  \CI_n (E, \hbar)=\oint_{|X|=1} Y_n(X, \hbar, E) {\rd X \over  X} ={\rm Res}_{X=0} { Y_n(X, \hbar, E) \over X}, 
  \ee
  
  where
  
  \be
  X=\re^x. 
  \ee
  
  In fact, it is more convenient to solve the differential equation
  directly in the $X$ variable, since everything is algebraic, i.e.\ it
  is better to solve
  
  \be 2 \sqrt{E} Y_n(X, \hbar, E) -\ri \hbar X {\rd Y_n \over \rd X
  }(X, \hbar, E)+\sum_{k=1}^{n-1} Y_k(X, \hbar, E) Y_{n-k}(X, \hbar,
  E)=0.  \ee




It turns out that the function $Y(\ri x, \hbar, E)$ can be calculated exactly in terms of Mathieu functions. To see this, we note that $\CY(x, \hbar, E)=Y(\ri x, \hbar, E)$ satisfies the 
Riccati equation 

\be
\CY^2(x, \hbar, E) -\hbar {\rd \CY \over \rd x}(x, \hbar, E)= E- 2 \Lambda^2 \cos(x), 
\ee

which is the Mathieu equation with imaginary Planck constant. The solution to this equation is 

\be
\CY(x, \hbar, E)= -\hbar {\rd \over \rd x} \log \left\{ S \left(-{4 E \over \hbar^2}, -{4 \Lambda^2 \over\hbar^2}, {x\over 2}\right)+c C \left(-{4 E \over \hbar^2}, -{4 \Lambda^2 \over\hbar^2}, {x\over 2}\right)\right\}, 
\ee

where $c$ is an integration constant and $S(\alpha, q, x)$, $C(\alpha,q,x)$ are the odd (even) Mathieu functions, respectively. Since we want 

\be
\CY(x, \hbar, E) \approx {\sqrt{E}}
\ee

as $\Lambda \rightarrow 0$, we find that this leads to 

\be
c=\pm \ri
\ee

 (where the sign depends on the branch cut of the square root). We eventually find 

\be
\label{inta}
\Pi^{\rm ex}_A (E, \hbar) =  {2 }\int_{-\pi}^{\pi} \CY(x) \rd x = -{2 \hbar } \log {S \left(-{4 E \over \hbar^2}, -{4 \Lambda^2 \over\hbar^2}, {\pi\over 2}\right)+c C \left(-{4 E \over \hbar^2}, -{4 \Lambda^2 \over\hbar^2}, {\pi\over 2}\right) \over -S \left(-{4 E \over \hbar^2}, -{4 \Lambda^2 \over\hbar^2}, {\pi\over 2}\right)+c C \left(-{4 E \over \hbar^2}, -{4 \Lambda^2 \over\hbar^2}, {\pi\over 2}\right)}. 
\ee

Note that 

\be
\label{a-char}
\Pi^{\rm ex}_A(E, \hbar) =2 \pi  {\ri \hbar } \,\nu\left( -{4 E \over \hbar^2}, -{4 \Lambda^2 \over\hbar^2} \right), 
\ee

where $\nu$ is the characteristic exponent of the Mathieu equation (this relation has been noted in the context of the Mathieu equation in e.g. \cite{he-miao, kpt}). 
The advantage of the expressions \eqref{inta}, (\ref{a-char}) is that they make sense for values of $E$ for which the $\Lambda$ expansion \eqref{aseries} does not converge, so they extend 
(\ref{aseries}) to a larger domain. 

Let us consider some numerical examples. When $E=100$, $\hbar=3 \pi$ and $\Lambda=1$, we can evaluate the series (\ref{aseries}) by truncating it up to order $\Lambda^{28}$, and we find:

\be
{1\over 4 \pi } \Pi^{\rm ex}_A(100, 3 \pi)=-9.9997954179096157891757...
\ee

This is precisely what is also obtained from (\ref{inta}) and (\ref{a-char}). At the same time, by using (\ref{inta}) we can go all the way to $E=0$, where (\ref{aseries}) cannot be used. We find, for example, 

\be
 {1\over  4 \pi }\Pi^{\rm ex}_A(0, 3 \pi)=0.1501122164563802133431995... \ri. 
\ee

This procedure for evaluating the value of $\Pi^{\rm ex}_A$ at $E=0$ seems to be well-defined for sufficiently large $\hbar \Lambda^{-2}$ (e.g. $\hbar \Lambda^{-2} \ge 1$ works). 

We conclude that the ``exact" quantum $A$ period can be computed either
by the expression given by instanton calculus (or equivalently, by the
closely related series (\ref{aseries})), or by the expression
(\ref{a-char}) involving the Mathieu characteristic exponent
(\ref{a-char}). When these two expressions are both well-defined, they
agree, but (\ref{a-char}) has a larger range of validity. In the case
of the quantum $B$ period, it might be possible to obtain an alternative
expression to the one in (\ref{abpe}), in terms of infinite Hill
determinants, by using results in \cite{gutz1}.
