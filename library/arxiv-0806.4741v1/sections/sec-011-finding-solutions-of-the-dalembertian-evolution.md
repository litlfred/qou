---
doc_id: arxiv-0806.4741v1
doc_title: "The deformation quantizations of the hyperbolic plane"
section_id: sec-011-finding-solutions-of-the-dalembertian-evolution
section_title: "Finding solutions of the Dalembertian evolution by variable separation"
section_number: null
pages: 15-17
source_pdf: 0806.4741v1.pdf
source_sha256: 5e7ad85a99fb3552
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.95
doc_brief: "The deformation quantizations of the hyperbolic plane — We describe the space of (all) invariant deformation quantizations on the hyperbolic plane D as solutions of the evolution of a second order"
---
\label{SectSL}
For convenience, we fix a particular choice of closed star product $\star$ on $\MM$ associated as above with
the function 
\begin{equation}
\cp(\zeta)\;=\;\cp^{\mbox{\tiny{\rm closed}}}(\zeta):=\sqrt{\cosh(\hbar \zeta)}\;.
\end{equation}
We denote the corresponding intertwiner by $T^{{\mbox{\tiny{\rm closed}}}}$. We then note that, from the above discussion,  the analogue of equation (\ref{ES}) for the direct operator $U$ in this case can be rewritten under the following form:
\begin{equation}\label{BoxBrutApp}
- \Box_{|\bar{{  z}}} W({  x},\bar{{  z}}) = F^\star_{{ (x)}}
W({ x},\bar{{  z}}) \quad ,
\end{equation}
with
\begin{equation}\label{DefWApp}
W({  x},\bar{{  z}}) = \left( (\phi_\hbar ^*)^{-1} \circ {\cal F}
\circ T^{{\mbox{\tiny{\rm closed}}}} \right)_{|{  z}} u({ z}^{-1}{  x}) \quad ,
\end{equation}
and where  the operator $\Box$ is given by (\ref{box1}). 
Observe that from  (\ref{DefWApp})
 the function $W({
x},\bar{{z}}) = W(a,n,b,r)$ takes the form 
\begin{equation}\label{FormeW}
W  (a,n,b,r) =   (1+ \hbar^2 \,r^2)^{1/4} \, q
\, e^{-i  r  n  q} \, F (q,r) \quad,
\end{equation}
with $q =  e^{2(a-b)}$ and
\begin{equation}\label{uF}
F (q,r) = \int\, e^{i\,  q\,r\, y} \, u
(\frac{1}{2} \ln  q,y) \, dy \quad,
\end{equation}
and where $ (a,n)$ are the coordinates of $x$, $(b,\ell)$ those of $z$, and, 
$(b,r)$ those of $\bar z$, $r$ being the variable conjugated to $\ell$ through the
Fourier transformation  ${\cal F}$ which only affect the second
$z$-coordinate.

\noindent The right-hand side of eq. (\ref{BoxBrutApp}) is simpler  :
\begin{eqnarray}\label{BoxBox}
F^\star_{ x}W(x,\bar z)= e^{2\,a}q\left(2\,q\,n\,\partial_q-(k'+n^2)\partial_n\right) W(q,n,r)\quad 
\end{eqnarray}
$k'$ being for the operator $F^\star_{x}$ the corresponding of $k$ for the  operator $F$ in $\rho_\hbar ^1(F)_{|{  z}}$  (see eqs (\ref{fundamental})), so finally eq. (\ref{BoxBrutApp}) simplifies to the following equation for $F  (q,
r)$ :
\begin{equation}\label{BoxFqr}
\left(-r\,  \hbar^2 q^2\,(1+\hbar^2  r^2  ) \partial_q^2 - r\,(1+\hbar^2 r^2)^2 \partial_r^2  + 2\,q\,(1+\hbar^2 r^2)^2 \partial_r
\partial_q   - 2\,\hbar^2\,r^2\,(1+\hbar^2 r^2)  \partial_r +
V\right) F (q,r) = 0 \ ,
\end{equation}
with 
\begin{equation}
V\;=\;V(q,r)\;:=\;r\,(-\frac{\hbar^2}4 (2+\hbar^2 r^2 ) + (1+\hbar^2 r^2) (k - k' q^2))\;.
\end{equation}

\noindent The problem  amounts thus to solve the corresponding equation for $F_\hbar (q,
r)$, from which we could find $u_\hbar$ by
inverting (\ref{uF}). We set 
\begin{equation}
G(q,r)  = q^{1/2} (1+ r^2\hbar^2)^{1/4}\,F(q,r)\;,
\end{equation}
\noindent and use the variables:
\begin{equation}\label{UVqr}
U = q^{\frac{1}{2}}\sinh(\frac{\hbar}{2}\zeta) \quad, \quad V =
q^{\frac{1}{2}}\cosh(\frac{\hbar}{2}\zeta)  \quad,
\end{equation}
with
\begin{equation}\label{rzeta}
r\;=:\;\frac{1}{\hbar}\sinh(\hbar\zeta)\;.
\end{equation}
\noindent The equation then becomes
\begin{equation}\label{wave}
\left[\partial_U \partial_V + \tilde{Q}(U,V)\right] G(U,V) = 0
\quad,
\end{equation}
with
\begin{equation}
\tilde{Q}(U,V) = -\frac{4}{\hbar^2} \frac{UV}{(U^2 - V^2)^2}
(\frac{\hbar^2}{4} - k + k'(U^2 - V^2)^2) \quad.
\end{equation}
Note that here : $U^2 - V^2 = -q$, hence $U^2 - V^2<0$. Setting  $U^2=\frac{1}{2}(t-x)$,
$V^2=\frac{1}{2}(t+x)$ and $G(q,r)=H(t,x)$, one then gets
\begin{equation}
\left\{x^2(\partial^2_t-\partial^2_x)-\frac
1{\hbar^2}[\frac{\hbar^2}{4} -k+k'x^2]\right\}H(t,x)=0\;.
\end{equation}
Applying a method of separation of variables to the latter yields solutions  as  superpositions of 
the following modes:
\begin{equation}
F_{\hbar,s} (q,r) =  h_s(q) (1+\hbar^2
\, r^2)^{-1/4} e^{i s q\sqrt{1+\hbar^2\,r^2} }\quad,
\end{equation}
with
\begin{equation}\label{hs}
h_s(x)= A\, J_{\frac
{\sqrt{k}}{\hbar}}[\sqrt{s^2+ {k'} /{\hbar^2}}\,\,
x] + B\, Y_{\frac{\sqrt{k}}{\hbar}}[\sqrt{s^2+  {k'}/ {\hbar^2}}\,\, x]\quad,
\end{equation}
where $J_\m$ and $Y_\mu$ denote  Bessel functions of the first and second kinds (see ref. \cite{Wa}).
From (\ref{uF})
\begin{equation}\label{Ftou}
u(a,l) = \frac{e^{2a}}{2 \pi}\int\, e^{-i \,r\, l\, e^{2a}} F(
e^{2a},r) \, dr \quad,
\end{equation}
thus (up to constant factors)
\begin{equation}\label{uGen}
u_{\hbar,s}(a,l) =  e^{2a} \, h_s(  e^{2a})\, \int \, {\cal
H}_s(a,b) \, e^{i  b  l e^{2a}} \, db \quad,
\end{equation}
with
\begin{equation}\label{uGenbis}
{\cal H}_s(a,b) = (1+ \hbar^2r^2)^{-1/4} e^{  i s
\sqrt{1+\hbar^2r^2} e^{2a}} \quad.
\end{equation}
We may use a similar technique to determine the kernel of the inverse operator $U^{-1}$. By writing
\begin{equation}
 [U^{-1}f]({x})=\int \, v({z}^{-1}{x}) \, f({z}) d{z} \quad,
 \end{equation}
one finds:
\begin{equation}\label{BoxBrutAppInv}
 \Box_{\bar{{x}}} M(\bar{{x}},{z}) = - F^\star_{{z}} M(\bar{{x}},{z}) \quad
 \end{equation}
with
\begin{equation}\label{M}
M(\bar{{  x}},{z}) = \left( (\phi_\hbar^*)^{-1} \circ {\cal F}
\circ T^{{\cal P}} \right)_{|{ x}} v^{{\cal P}}({z}^{-1}{x}) \quad .
\end{equation}
Solutions to (\ref{BoxBrutAppInv}) can be deduced by using a slight generalization of what we have done here above. We finally get,
\begin{equation}\label{vGen2}
v_{\hbar,s}(a,l) = e^{-2a} \, h_s(  e^{-2a})\, \int
\, (1+ \hbar^2r^2)^{-1/4} e^{  i s \sqrt{1+\hbar^2r^2} e^{-2a}} \, e^{-i b l} \, db \quad.
\end{equation}
