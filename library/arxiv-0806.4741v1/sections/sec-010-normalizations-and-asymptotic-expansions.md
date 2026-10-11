---
doc_id: arxiv-0806.4741v1
doc_title: "The deformation quantizations of the hyperbolic plane"
section_id: sec-010-normalizations-and-asymptotic-expansions
section_title: "Normalizations and asymptotic expansions"
section_number: null
pages: 17-22
source_pdf: 0806.4741v1.pdf
source_sha256: 5e7ad85a99fb3552
doc_brief: "The deformation quantizations of the hyperbolic plane — We describe the space of (all) invariant deformation quantizations on the hyperbolic plane D as solutions of the evolution of a second order"
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.928
---
\label{Norasympt}
\noindent Observe that the   change of variables (\ref{UVqr}) becomes singular when $\hbar$ vanishes, while the  equation (\ref{BoxFqr}) degenenrates into
\begin{equation}\label{BoxFqrdeg}
(-r\,\partial_r^2+2\,q\,\partial_r\partial_q+r\,(k-k'q^2))F(q,r)=0\qquad .
\end{equation}
The general solution of this equation can be expressed as a superposition of modes
\begin{equation}
F_{0,\sigma}=C\,\frac 1{\sqrt q}\,e^{i\frac{\sigma\,q\,r^2}2}\,e^{-\frac i{2\,\sigma}\left(\frac k q +k'q\right)}\qquad.
\end{equation}
Let us notice that these modes can be obtained from special combinations of modes (\ref{hs}) and a rescaling of the wave-number $s$ into $s=\sigma/\hbar^2$.
This rescaling is dictated by the necessity of maintaining a $r$ dependence in the limit $\hbar \rightarrow 0$ of the modes (\ref{hs}):
\begin{equation}
s\,\sqrt{1+\hbar^2r^2}\approx s + s\,\hbar^2r^2=\frac \sigma{\hbar^2}+\sigma \,r^2
\end{equation}
while the oscillating factor can be controlled by considering the asymptotic behavior of the  Hankel functions (\cite{Wa}, sec. {\bf 8.41})
\begin{equation}
H^{(2)}_{\frac{\sqrt k}{\hbar}}(\sqrt{\frac{\sigma^2}{\hbar^4}+\frac{k'}{\hbar^2}}q)\approx \hbar \sqrt{\frac 2{\pi\,\sigma\,q}}\,e^{-i\frac{\sigma\,q}{\hbar^2}}
e^{i\frac{\sqrt k\,\pi}{2\,\hbar}}\,e^{-\frac i{2\,\sigma}\left(\frac k q +k'q\right)}\qquad .
\end{equation}
Thus by choosing in the coefficients $A$ and $B$ in the linear combination (\ref{hs}) as :
\begin{equation}
A=-i\,B=C\,\frac 1 \hbar\,\sqrt{\frac{\pi\,\sigma}2}\,e^{-i\frac {\sqrt{k}\,\pi}{2\,\hbar}}
\end{equation}
we obtain   modes whose limit for $\hbar =0$ is well defined. This explain the results of our computations below.
 Note that, given an operator $U$, it is not straightforward to extract the inverse operator $U^{-1}$ since one has to determine how to superpose these different modes. In section \ref{Unterberger} however, we will discuss a particular example where the superposition is known.

\noindent The operators $U$ we consider hereafter will correspond  to \re{uGen}, \re{hs} with $B=0$. This special choice is motivated by the bad behavior of the $Y$-Bessel function near the origin. We have :
\begin{eqnarray}\label{USF}
 (U_s f)(a,l) =  C_\hbar (s) \int_{\R^2\times\R_+} \, dr \, dn\, dx\, J_{\frac{\sqrt{k}}{\hbar}}(\sqrt{s^2 + k'/\hbar^2}\, \,x) (1+\hbar^2 \,r^2)^{-\frac{1}{4}} \nonumber\\
  e^{i \,s\, x \sqrt{1+\hbar^2\, r^2}} \, e^{i \,r\, l x} \, e^{-i\, r\, n} \, f(a-\frac{1}{2}\ln x,n)\qquad.
\end{eqnarray}
A necessary condition for $U_s$ to define a star product is that $(U_s 1) = 1$. This leads to the condition\footnote{A useful relation in this derivation (see ref.\cite{Wa}, sec. 13.2, eq.[8]) is :
$
\int_0^\infty e^{(i\kappa-\epsilon)\zeta}J_\lambda (\beta\,\zeta)\,d\zeta=\frac{\beta^{-\lambda }[\sqrt{\beta^2-\kappa^2}+i\kappa]^{\lambda }}{\sqrt{\beta^2-\kappa^2}}
$}
\begin{equation}\label{Cnorm}
  C_\hbar(s) = \frac{ \sqrt{k'}}{2\,\pi\,\hbar}\left[ \frac{\sqrt{k'} - i \,\hbar\,s[\hbar]}{\sqrt{k'} + i \,\  \hbar\,s[\hbar]} \right]^{\frac{\sqrt{k'}}{2\,\hbar}}.
\end{equation}
Let us notice that we allow a $\hbar$ dependence in  $s$; we don't assume it a priori to be constant but  leave it as a free (regular) function of the deformation parameter.

\noindent On the other hand, the requirement 
\begin{equation}
   U_s f \underset{\hbar \ra 0}{\lra} f
\end{equation}
to get the right classical limit further imposes
\begin{equation}\label{kmu}
 k = k' \qquad .
\end{equation}
Let us now turn to the asymptotic expansion of the operator  \re{USF}. To this end we introduce the following Fourier-like transforms:
\begin{eqnarray}
 \tilde{f}_- (k,p) &=& \frac{1}{2\pi^2} \int f(a,l) e^{-i k e^{-2a}} e^{-ipl} e^{-2a} da\, dl \label{Fouriermoins}\\
  f(a,l) &=& \phantom{\frac{1}{2\pi^2}}\int \tilde{f}_- (k,p) e^{i k e^{-2a}} e^{i p l} dk dp\qquad ,
\end{eqnarray}
from which one obtains
\begin{eqnarray}\label{UsDev}
 (U_s f) (a,l) =\sqrt{k}\int \frac{(1+\hbar^2\, p^2)^{-1/4}}{(k + \hbar^2\,(s^2(\hbar) - \kappa^2))^{1/2}} \left[\frac{\sqrt{k + \hbar^2 \,(s^2(\hbar) - \kappa^2)} + i \,\hbar\,\kappa }{\sqrt{k} +  i \, \hbar\, s(\hbar)} \right]^{\frac{\sqrt{k}}{ \hbar}}  \tilde{f}_- (r,p)\,dp\,dr
\end{eqnarray}
where 
\begin{eqnarray}
 \kappa = r\, e^{-2a} + p\, l  + s(\hbar)\, \sqrt{1+\hbar^2\,r^2}.
\end{eqnarray}
Setting $X = r\, e^{-2a} + p\, l$, the integrand can be Taylor expanded around $\hbar = 0$ as 
\begin{equation}\label{TaylorU}
 \sqrt{k}  \frac{(1+\hbar^2\, p^2)^{-1/4}}{(k + \hbar^2\,(s^2(\hbar) - \kappa^2))^{1/2}} \left[\frac{\sqrt{k + \hbar^2 \,(s^2(\hbar) - \kappa^2)} + i \,\hbar\,\kappa }{\sqrt{k} +  i \,\hbar\, s(\hbar)} \right]^{\frac{\sqrt{k}}{ \hbar}}= {\rm e}^{i X} P(X,p^2)
\end{equation}
where \re{TaylorU} defines the $\hbar$ power series  $P(X,p^2)$,  which, at first (non-trivial) order\footnote{If we assume $s$ to be constant, instead of a function of $\hbar$, this expansion involves only even power of $\hbar$.}, reads as :
\begin{equation}\label{P}
 P(X,p^2) = 1 + \hbar^2 \left(-p^2\frac{ (1-2\,i\, s)}4 + \frac{ s}{k} X +  \frac{(1+ i\, s)}{2\,k} X^2 +  \frac{i}{6\, k}X^3\right) + O(\hbar^4) 
\end{equation}
The important point in the previous expression is the structure of the expansion, and in particular the occurrence of the factor $ {\rm e}^{i X}$. Using this result, the expansion of the operator $U$ follows:
\begin{eqnarray}
 (U_s f)(a,l) &\approx& \int P(X,p^2) e^{i X} \tilde{f}_- (r,p)\,dp\,dr \nonumber \\
              &=& \int   P[-i \p_\sigma,-\p^2_\alpha]\, e^{i \sigma X} e^{i\alpha p}\left . \tilde{f} (k,p)_- \right \vert_{\sigma=1, \alpha=0} \,dp\,dr  \nonumber \\
              &=& P[-i \p_\sigma,-\p^2_\alpha]\left. f(a-\frac{1}{2} \ln \sigma, \sigma l + \alpha)\right\vert_{\sigma=1, \alpha=0}\quad .
\end{eqnarray}
It therefore appears appears that the product so-defined deforms the pointwise product on the hyperbolic plane in the direction of the $\SL$-invariant Poisson bracket.

\noindent A similar computation can be performed starting from the inverse operator. One has (with $x= e^{2(b-a)}$)
\begin{eqnarray}
 (V_s f)(a,l) 
  =\frac{D_\hbar (s)}{2}\int_{\R^2\times\R_+} \, dr \, dn\, dx\, J_{\frac{\sqrt{k}}{\hbar}}(\sqrt{s^2 + k'/\hbar^2} \,x) (1+\hbar^2 \,r^2)^{-\frac{1}{4}} \nonumber\\
  e^{i \,s\, x \sqrt{1+\hbar^2\, r^2}} \, e^{ i r ({n\,x} -l)} \,   f(a+\frac{1}{2}\ln x,n)\qquad.\label{Vsf}
\end{eqnarray}
The requirement $V_s 1 = 1$, imposes
\begin{equation}\label{Dnorm}
 D_\hbar (s)=\frac{\sqrt{k}}{ \pi\,\hbar}\left(\frac{\sqrt{k'}-i\,\hbar\,s(\hbar)}{\sqrt{k'}+i\,\hbar\,s(\hbar)}\right)^\frac {\sqrt{k}} {2\,\hbar} 
 \end{equation}
while the right classical limit implies \footnote{A useful relation in that case is (see ref.\cite{Wa}, sec. 13.2, eq.(7)) : $
\int_0^\infty \frac{e^{(i\kappa-\epsilon)\zeta}} \zeta J_\lambda (\beta\,\zeta)\,d\zeta=\frac{[\sqrt{\beta^2-\kappa^2}+i\kappa]^{\lambda }}{\lambda \,\beta^{\lambda }}$}
\begin{equation}\label{kmu2}
  k =  k',
\end{equation}
in accordance with eq. \re{kmu}. 

\noindent Using again the expression of the Fourier transform of the Bessel function but   the Fourier transform
\begin{eqnarray}
 \tilde{f}_+ (k,p) &=& \frac{1}{2\pi^2} \int f(a,l) e^{-i k e^{2a}} e^{-ipl} e^{2a} da\, dl \label{Fourierplus}\\
  f(a,l) &=& \phantom{\frac{1}{2\pi^2}}\int \tilde{f}_+ (k,p) e^{i k e^{+2a}} e^{i p l} dk dp.
\end{eqnarray}
 one is led to
\begin{eqnarray}\label{VsDev}
 (V_s f)(a,l)  =\frac{\sqrt{k}}{2\,\pi}\int \frac{(1+\hbar^2\, p^2)^{-1/4}\,e^{i p l}\, e^{i \,q\, n}}{(k +   \hbar^2\,(s^2(\hbar) - \rho^2))^{1/2}} \left[\frac{\sqrt{k +  \hbar^2 \,(s^2(\hbar) - \rho^2)} + i  \,\hbar\,\rho }{\sqrt{k} +  i \, \hbar\, s(\hbar)} \right]^{\frac{\sqrt{k}}{ \hbar}}  \tilde{f}_+ (r,q)\,dp\,dr\,dn\,dq
\end{eqnarray}
where
\begin{equation}
 \rho =  {r\, e^{2a} - p\, n}  + s(\hbar)\, \sqrt{1+\hbar^2 \,p^2}\qquad.
\end{equation}
Setting $Y = r\, e^{2a} - p\, n$, we may write
\begin{equation}
\sqrt{k} \frac{(1+\hbar^2\, p^2)^{-1/4} }{(k +  \hbar^2\,(s^2(\hbar) - \rho^2))^{1/2}} \left[\frac{\sqrt{k +  \hbar^2 \,(s^2(\hbar) - \rho^2)} + i \, \hbar\,\rho }{\sqrt{k} +  i \,\hbar\, s(\hbar)} \right]^{\frac{\sqrt{k}}{ \hbar}} = e^{i Y} P(Y,p^2),
\end{equation}
where $P$ has the same expression as in \re{TaylorU} (Let us remark that this holds only  because we use the strongly closed $\SS$-invariant star product).
One successively gets
\begin{eqnarray}
 (V_s f)(a,l)  &=& \frac{1}{2\pi} \int dp \, dr\, dn \,dq \, e^{i \,p\, l} \,e^{i\,q\,n} P(Y,p^2) e^{iY} \tilde{f} _+(r,q) \nonumber \\
               &=&   \frac{1}{2\pi} \int dp \, dr\, dn \,dq \,  P[-i \p_\sigma,-\p^2_l] e^{i \sigma Y} \, e^{i \,p\, l} \,e^{i\,q\,n}\left . \tilde{f}_+ (k,q)\right\vert_{\sigma=1} \nonumber\\
               &=& \frac{1}{2\pi} \int dp \,dn \;  P[-i \p_\sigma,-\p^2_l]\left. f(a+\frac{1}{2} \ln\sigma,n) e^{i\,p\,(l-n\,\sigma)} \right\vert_{\sigma=1}\nonumber\\
               &=& P[-i \p_\sigma,-\p^2_l] \frac{1}{\sigma}\left. f(a+\frac{1}{2} \ln\sigma,\frac{l}{\sigma})\right\vert_{\sigma=1} \qquad .
\end{eqnarray}

\subsection{The case $k\;=\;\frac{\hbar^2}{4}$ and Zagier type deformations}
We now consider the case of our closed star product $\star:=T^{\mbox{\tiny{\rm closed}}}(\star^0_\hbar)$
together with a particular derivation $D_\hbar\in\mathfrak{Der}(\star)$ defined as setting $k=\frac{\hbar^2}{4}$ in the
expression (\ref{lambdaF}) and then intertwining by $T^{\mbox{\tiny{\rm closed}}}$ following (\ref{DERIV}).
We then proceed as in the subsection \ref{SectSL}, but use the following variables rather than (\ref{UVqr}):
\begin{equation}\label{UVqrbis}
\xi = q^{\frac{1}{2}}\frac{2}{\hbar}\sinh(\frac{\hbar}{2}\zeta) \quad, \quad \eta =
q^{\frac{1}{2}}\cosh(\frac{\hbar}{2}\zeta)  \quad
\end{equation}
Note that in contrast with the coordinates (\ref{UVqr}), the above one are not singular in the limit $\hbar\to 0$. Indeed, they become $\xi_0=q^{\frac{1}{2}}\zeta$ and $\eta_0=q^{\frac{1}{2}}$ in the limit.

\noindent Within these normalisations, the equation (\ref{wave})  then becomes:
\begin{equation}\label{wave-bis}
\partial_\xi\partial_\eta G\;=\;4k'\,\eta\xi\,G\;;
\end{equation}
with, as before,
\begin{equation}
G(q,r)  = q^{1/2} (1+ r^2\hbar^2)^{1/4}\,F(q,r)\;.
\end{equation}
Note that from (\ref{uF}), the classical  limit $\hbar\to0$ of the latter is prescribed to equal
\begin{equation}
F_{\mbox{\rm cl}}\;:=\;\delta_0(a)\otimes{\bf 1}_r\;.
\end{equation}
One way to achieve this requirement is to allow $k'$ to depend on $\hbar$ in such a way that the condition (\ref{kmu}) remains satisfied
\begin{equation}
\lim_{\hbar\to0}k'(\hbar)\;=\;0\;.
\end{equation}
More naturally, this corresponds to considering the $\hbar$-independent wave equation in the case $k'=0$:
\begin{equation}\label{wave-ter}
\partial_\xi\partial_\eta G\;=\;0\;,
\end{equation}
which trivially admits the $\xi$-independent solution:
\begin{equation}
G\;=\;G(\eta)\;=\:G\left(e^a\frac{\sqrt2}{2}\left(1+\sqrt{1+\hbar^2r^2}\right)^{\frac{1}{2}}\right)\;;
\end{equation}
with
\begin{equation}
G(e^a)\;:=\;e^{a}\,\delta_0(a)\;.
\end{equation}
The above discussion leads us to the particular solution:
\begin{equation}
u_\hbar(a,\ell)\;:=\;\frac{\sqrt2e^{2a}}{4\pi}\int_{-\infty}^\infty\,e^{ir\ell e^{2a}}\left(\frac{1+\sqrt{1+\hbar^2r^2}}{\sqrt{1+\hbar^2r^2}}\right)^{\frac{1}{2}}\,\delta_0\left(\,a\,+\,\frac{1}{2}\log
(\frac{1}{2}(1+\sqrt{1+\hbar^2r^2})\,)\right)\,{\rm d}r\;;
\end{equation}
that admits the correct limit:
\begin{equation}
u_0(a,\ell)\;=\;\delta_{e}(a,\ell)\;.
\end{equation}
The associated convolution operator $U$ produces a deformation
quantization that is invariant under the infinitesimal action of ${\mathfrak{sl}}_2(\R)$ on an open $\SS$-orbit
in $\R^2$ (the group $\SS$ acting by special linear transformations). The corresponding underlying geometry 
here being flat ($k'=0$). In particular, this class of solutions reproduces star products of the same type as the one considered by Connes and Moscovici in \cite{CM}, primarily constructed by Zagier as a $\mathfrak(sl)_2(\R)$-invariant deformation of the algebra of modular forms \cite{Za}.


\subsection{Unterberger type solutions and Weinstein's asymptotics}\label{Unterberger}
In \cite{Unt,Unt2} an associative $\SL$ invariant composition law, though not a star product, has been derived  in a totally different context by A.
and J. Unterberger, for the composition of symbols in the so-called Bessel calculus. We are going to show that a slight modification of their formula yields one of the simplest products in the family we have found.

\noindent As a prealable, let us notice, that in their works, these authors also make use of an interwiner operator linking an $\SL$- invariant composition law with an $AN$-invariant star product, but not the strongly closed one we have adopted. Instead of this one, the star product they use may be expressed in our framework as the one  obtained from (\ref{OpT}) with special weight function  ${\cal P}(\hbar \xi)=\cosh (\hbar \xi)$, as proven in \cite{BielMassar2}. 
\par\noindent The
convolution kernel of an intertwiner between an $\SL$-invariant star product $\#$ and a general
$AN\,$-invariant product, itself built from the Moyal star product twisted by an operator $T_{\cal P}$ is obtained from the operator $U$ we constructed in section \ref{SectSL} by:
\begin{equation}\label{fromone}
 U_{\cal P} = U  \circ (T^{{\mbox{\tiny{\rm closed}}}})^{-1} \circ T_{\cal P} \quad .
 \end{equation}
In particular, if $T_{\cal P}$ is of the form of eq. (\ref{OpT}), the kernel of $U_{\cal P}$ is then given as a superposition of modes,
\begin{equation}\label{ugenkernel}
 u_{\cal P} (a,l) = \int \, \phi(s') u^{\cal P}_{\hbar,s'}(a,l) \, ds' \quad , 
\end{equation}
with 
 \begin{equation}\label{uGenP}
u^{\cal P}_{\hbar,s}(a,l) =  e^{2a} \, h_s( e^{2a})\, \int \,
(1+\hbar^2 r^2)^{-\frac{1}{2}}\,{\cal P}({\rm arcsinh}(\hbar r))\, e^{ i s \sqrt{1+
\hbar^2 r^2} e^{2a}} \, e^{i r l e^{2a}} \, dr \quad,
\end{equation}
where $h_s(x)\propto  J_{
{\sqrt{k}}/{\hbar}}[\sqrt{s^2+ {k} /{\hbar^2}}\,\,
x] $.
 
\noindent An analog computation yields the kernel of the inverse operator $U^{-1}_{\cal P}$ 
again as a superposition of modes, each of them being given by 
\begin{equation} 
v^{\cal P}_{\hbar,s}(a,l) = e^{-2a} \, h_s( e^{-2a})\, \int
\, {\cal P}^{-1}({\rm arcsinh}(\hbar\,r)) e^{ i s \sqrt{1+\hbar^2
r^2} e^{-2a}} \, e^{-i r l} \, dr \quad .
\end{equation}

\noindent Let us plug  $B=0$ in \re{hs}, and normalize the modes accordingly to eqs (\ref{Cnorm}, \ref{Dnorm}) with $k=k'$ (see eqs (\ref{kmu}, \ref{kmu2}). The operator $U$ considered in  \cite{Unt,Unt2} then  corresponds to the value $s=0$  in \re{uGen}. This obviously amounts to pick up $\phi(s') = \delta (s')$ in eq. (\ref{ugenkernel}). By taking ${\cal P}(\hbar\,\xi)=\cosh (\hbar\,\xi)$, and denoting by $U_U$ the corresponding operator, one finds
\begin{equation}
 (U_{U} f) (a,l) = \frac{\sqrt{k}}{ \hbar} \int dx \; J_{\frac{\sqrt{k}}{\hbar}} ( {\sqrt{k}}\,x/\hbar) \, f(a-\frac{1}{2} \ln x,l\,x ).
\end{equation}
The inverse operator, $U^{-1}_U$ corresponds to the kernel resulting from the superposition
\begin{equation}
  v_{\hbar,s} (a,l) = \int \psi(s) \Psi_{\hbar,s}^{U}(a,l) ds
\end{equation}
of modes
\begin{equation}
 \Psi_{\hbar,s}^{U}(a,l) =\frac{\sqrt{k}}{ 2\,\pi\,\hbar}\left(\frac{\sqrt{k'}-i\,\hbar\,s(\hbar)}{\sqrt{k'}+i\,\hbar\,s(\hbar)}\right)^\frac {\sqrt{k}} {2\,\hbar}\, J_{\frac{\sqrt{k}}{\hbar}}(\sqrt{s^2 + k'/\hbar^2} \,x) \int    
 \frac{ e^{i \,s\, x \sqrt{1+\hbar^2\, r^2}} \, e^{- i r l}}{\sqrt{ (1+\hbar^2 \,r^2)}}\, dr 
 \end{equation}
that is obtained by using 
\begin{equation}
\psi(s)=(i-s)\,\delta'(s)
\end{equation}
in the superposition of modes like those appearing in eq. (\ref{Vsf}), normalized according to eq. (\ref{Dnorm}).
Explicitly,   one gets
\begin{equation}
 (U^{-1}_U f)(a,l) = \frac{\sqrt{k}}{ \hbar} \int dx \; J_{\frac{\sqrt{k}}{\hbar}} ({\sqrt{k}}\,x/\hbar) \, f(a+\frac{1}{2} \ln x ,\frac{  l}{x}).
\end{equation}
Apart from the $\hbar$-dependent pre-factors, these operators are exactly the ones found in \cite{Unt}, see equations (4.16) and (4.7).

\noindent Of course, the asymptotic expansions allows to build $U^{-1}$ perturbatively, as an expansion in $\hbar$. For illustrative purpose let us mention, that for a fixed value of $s$ we obtain at fourth order: 
\begin{eqnarray}
U^{-1}_s&=&\left(V_r -\frac i{4\,\pi}\,\left[1- i\,\hbar^2 r\,(\frac14+ i\,r)\right]\,\partial_r\,V_r\right)_{r=-s}+ O(\hbar^5)\nonumber \\
&=&\int \left[(1+\frac {\hbar^2}{16\,\pi}+i\frac{\hbar^2}2\,r) \delta[r+s]+\frac i{4\,\pi}(1-i\,\frac{\hbar^2}4\,r+ \pi\,\hbar^2\,r^2)\delta'(r+s)\right]\,V_r\, dr + O(\hbar^5)\nonumber\\
&&
\end{eqnarray}
\noindent By a long but straightforward computation, the above explicit expressions of $U_U$ and $U_U^{-1}$ yield
(for $k=1$) the following integral formula for the invariant star product on the hyperbolic plane $\DD$:
\begin{equation*}
u\,\sharp_\hbar \,v\,(x)\;=\;\frac{1}{16 \pi^3 \hbar^4}\, \int_{\DD\times\DD}\,K_\hbar\left(S_{\mbox{\rm can}}(x,y,z)\right)\,u(y)\,v(z)\,{\rm d}y\,{\rm d}z\;;
\end{equation*}
where ${\rm d}y$ denotes the Liouville measure on $\DD$ and where 
\begin{equation}\label{noyauK}
K_\hbar (\varpi)\;:=\; \int_0^\infty \, s^2 J_{\frac{1}{\hbar}} (s/\hbar)\,
 e^{\frac{i}{\hbar} s \varpi} \,{\rm d}s\;.
\end{equation}


\noindent Using tabulated Laplace transforms, one first computes
\begin{equation}
{\mathcal F}_\m(p)=\int_0^\infty \, e^{-pt} J_\mu (t) dt =
\frac{1}{p^{\mu +1}}
\frac{[1+(1+\frac{1}{p^2})^{1/2}]^{-\mu}}{\sqrt{1+\frac{1}{p^2}}}
\quad ,
\end{equation}
with $p=\varepsilon - i \varpi$, $\varepsilon \ll$ being a small
real part necessary to ensure convergence.
Using the following relations
\begin{equation} 1 + \frac{1}{p^2}  = \left\{ \bearlll
  1- \varpi^{-2} &\;& {\rm if}\ \varpi^2 >1 ,  \\[.3em]
  (\varpi^{-2} -1) \,{e}^{i \,\rm{sign}(\varpi)\pi} &\;& {\rm if}\ \varpi^2 < 1 ,  \eear\right .
\end{equation}
and 
\begin{equation} 1 + \sqrt{1 + \frac{1}{p^2}}  = \left\{ \bearlll
 1+ (1- \varpi^{-2})^{1/2} \in \R &\;& {\rm if}\ \varpi^2 >1 ,  \\[.3em]
 1+  (\varpi^{-2} -1)^{1/2} \,{e}^{i \,\rm{sign}(\varpi)\pi/2} &\;& {\rm if}\ \varpi^2 < 1 \;,  \eear\right .
\end{equation}
one finally gets
\begin{equation}
 {\mathcal F}_\m(-i \varpi)  = \left\{ \bearlll
 \frac{1}{\sqrt{1-\varpi^2}}\,\, e^{i \, \frac{\mu}{2}
f_W(\varpi)} &\;& {\rm if}\ \varpi^2 < 1 ,  \\[.3em]
  |\varpi|^{-(\m+2)} (\varpi^2 - 1)^{-1/2} [1+ (1- \varpi^{-2})^{1/2}]^{-\m} \,{e}^{i\, \frac{\pi}{2} (\m + 1) \rm{sign}(\varpi)} &\;& {\rm if}\ \varpi^2 > 1 \;;  \eear\right .
\end{equation}
where $f_W$ is the odd function  (\ref{fW}) defined by $f_W(S_{\mbox{\rm can}}):=S_W$.
Note that, when $\varpi^2 < 1$, the phase of ${\mathcal F}_\m$ is precisely given by $f_W(\varpi)$, while when $\varpi^2 > 1$, it is pure phase. The kernel $K_\mu$ is now simply described  by
\beq \label{KMU}
  K_\mu (\varpi) = -\frac{d^2}{d\varpi^2}{\mathcal F}_\m(-i \varpi).
\eeq
\noindent The phase $S_\mu$ of the kernel $K_\m$ can then be determined from \re{KMU}. For $\varpi^2 <1$, one gets
\begin{equation}\label{PhaseK}
S_\mu(\varpi) = \mu \frac{f_W(\varpi)}{2} - \arctan [\frac{ 3
 \mu \sin f_W(\varpi)}{\mu^2 -4 + (\mu^2+2) \cos
 f_W(\varpi)}] \quad .
\end{equation}
\noindent In other words, for $\varpi^2 <1$, which corresponds to triples of points in $\DD$ for which Weinstein's $S_W$
is well defined,  the above kernel $K_\hbar$ can be expressed under the WKB oscillatory form. The expression
of the corresponding phase is then the following:
\begin{equation}
S\;= \; \frac{S_W}{2} - \hbar\arctan [\frac{ 3
\hbar\sin S_W}{ 1 -4\hbar^2 + (1+2\hbar^2) \cos
S_W}] \quad .
\end{equation}
In particular, one has the following asymptotics:
\begin{equation*}
S\;\sim\;\frac{S_W}{2} \;,
\end{equation*}
agreeing with  A. Weinstein's picture in \cite{WeinsteinTr}.


\section{Acknowledgments}
P.B. and Ph.S. acknowledge partial support from the IISN-Belgium (convention 4.4511.06). 
 P.B. acknowledges partial support from the IAP grant `NOSY' delivered by the Belgian Federal Government. S.D. and Ph.S.  warmly thank the IHES for its hospitality and the exceptional working conditions provided to its guests.
