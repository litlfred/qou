---
doc_id: arxiv-0806.4741v1
doc_title: "The deformation quantizations of the hyperbolic plane"
section_id: sec-014-unterberger-type-solutions-and-weinsteins-asympt
section_title: "Unterberger type solutions and Weinstein's asymptotics"
section_number: null
pages: 20-22
source_pdf: 0806.4741v1.pdf
source_sha256: 5e7ad85a99fb3552
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.99
doc_brief: "The deformation quantizations of the hyperbolic plane — We describe the space of (all) invariant deformation quantizations on the hyperbolic plane D as solutions of the evolution of a second order"
---
\label{Unterberger}
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
