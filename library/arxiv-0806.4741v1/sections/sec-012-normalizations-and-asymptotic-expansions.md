---
doc_id: arxiv-0806.4741v1
doc_title: "The deformation quantizations of the hyperbolic plane"
section_id: sec-012-normalizations-and-asymptotic-expansions
section_title: "Normalizations and asymptotic expansions"
section_number: null
pages: 17-19
source_pdf: 0806.4741v1.pdf
source_sha256: 5e7ad85a99fb3552
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.961
doc_brief: "The deformation quantizations of the hyperbolic plane — We describe the space of (all) invariant deformation quantizations on the hyperbolic plane D as solutions of the evolution of a second order"
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
