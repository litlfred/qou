---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-015-51-classical-teichmüller-theory-of-the-four-hole
section_title: "Classical Teichmüller theory of the four-holed sphere"
section_number: 5.1
pages: 13-14
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.978
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
To be
specific, let us restrict attention to four-holed spheres $C_{0,4}$.
The holes are assumed to be represented by geodesics
with lengths $L=(l_1, \dots,l_4)$.
There are three simple closed curves $\ga_s$, $\ga_t$, and $\ga_u$
encircling pairs of points $(z_1,z_2)$, $(z_2,z_3)$ and $(z_1,z_3)$,
respectively. A set of useful coordinate functions are defined
in terms of the hyperbolic cosines
$L_\si=2\cosh\frac{l_\si}{2}$, $\si\in\{s,t,u\}$, 
of the geodesic length functions
$l_\si$ on $\CT_{0,4}\equiv \CT(C_{0,4})$. $l_\si$ is defined
as the length of the geodesic $\ga_\si$, defined
by means of the constant negative
curvature metric on $C_{0,4}$. 

The well-known relations
between Teichm\"uller spaces $\CT(C)$ 
and the moduli spaces $\CM_G(C)$ of 
flat $G=SL(2,\BR)$-connections on Riemann surfaces imply 
that the geodesic length functions $L_\si$ are related to the 
holonomies $g_\si$ along $\ga_\si$ as $L_{\si}=-{\rm Tr}(g_\si)$.
This allows us to use the description given in \cite{NRS}, 
which may be briefly summarized as follows. The structure of
$\CM_G(C_{0,4})$ as an algebraic variety is expressed by the fact
that the three
coordinate functions $L_s$, $L_t$ and $L_u$ satisfy one algebraic
relation of the form $\CP_L(L_s,L_t,L_t)=0$. 
The Poisson bracket $\{L_{\si_1},L_{\si_2}\}$ defined
by the Weil-Petersson symplectic form is also algebraic in 
the length variables $L_\si$, and
can be written elegantly in the form 
\begin{equation}\label{loopPB}
\{\,L_s\,,L_t\,\}\,=\,\frac{\pa}{\pa L_u}\CP_L(L_s,L_t,L_t)\,.
\end{equation}
As shown in \cite{NRS} one may represent $L_s$, $L_t$ and $L_u$ 
in terms of Darboux-coordinates $l_s$ and $k_s$ which have
Poisson bracket $\{l_s,k_s\}=2$. The expressions for $L_s$ and $L_t$
are, in particular,
\begin{align}\label{FN-FK}
& L_s\,=\,2\cosh(l_s/2)\,,\\
& L_t(L_s^2-4)\,=\,
2({L}_2L_3+L_1L_4)+L_s(L_1L_3+L_2L_4) 

+2\cosh(k_s)
\sqrt{c_{12}(L_s)c_{34}(L_s)}\,,
\notag\end{align}
where $L_i=2\cosh\frac{l_i}{2}$, and $c_{ij}(L_s)$ is defined as
\begin{align}\label{cijdef}
c_{ij}(L_s) & \,=\,L_s^2+L_i^2+L_j^2+L_sL_iL_j-4\ \\ \nonumber & = 
2 \cosh \fr{l_s+l_i+l_j}{4} 2 \cosh \fr{l_s+l_i-l_j}{4} 
2 \cosh \fr{l_s-l_i+l_j}{4} 2 \cosh \fr{l_s-l_i-l_j}{4}.
\end{align}
Together with a similar formula for $L_u$, these expressions
ensure that both the algebraic relation $\CP_L(L_s,L_t,L_t)=0$ and 
the Poisson structure \rf{loopPB} are satisfied.
These Darboux coordinates
are identical to the Fenchel-Nielsen length-twist coordinates
well-known in hyperbolic geometry.\footnote{This can be
inferred from \cite{ALPS}. We thank T. Dimofte for 
pointing this reference out to us}

Similar Darboux coordinates $(l_t,k_t)$ and  $(l_u,k_u)$
can be associated to the 
curves $\ga_t$ and $\ga_u$, respectively.  
The change of coordinates between the Darboux-coordinates 
$(l_s,k_s)$ and  $(l_t,k_t)$
is represented by a generating function $\CS^{st}_L(l_s,l_t)$ 
such that 
\begin{equation}\label{cantrsf}
\frac{\pa}{\pa l_s}\CS^{st}_L(l_s,l_t)\,=\,-k_s\,,\qquad 
\frac{\pa}{\pa l_t}\CS^{st}_L(l_s,l_t)\,=\,k_t\,. 
\end{equation}

Other natural sets of 
Darboux-coordinates $(l_\si,k_\si')$ can be obtained by means of 
canonical transformations $k_\si'=k_\si+f(l_\si)$. By a suitable 
choice of $f(\si)$, one gets Darboux coordinates $(l_s,k_s')$
in which 
the expression for $L_t$ in \rf{FN-FK} is replaced by 
\begin{align}\label{FN-FK'}
L_t(L_s^2-4)\,=\,&
\;2({L}_2L_3+L_1L_4)+L_s(L_1L_3+L_2L_4) \\
& +
2 \cosh \fr{l_s+l_1-l_2}{4} 2 \cosh \fr{l_s+l_2-l_1}{4} 
2 \cosh \fr{l_s+l_3-l_4}{4} 2 \cosh \fr{l_s+l_4-l_3}{4} \;e^{+k_s'}\notag  \\
& +
2 \cosh \fr{l_s+l_1+l_2}{4} 2 \cosh \fr{l_s-l_1-l_2}{4} 
2 \cosh \fr{l_s+l_3+l_4}{4} 2 \cosh \fr{l_s-l_3-l_4}{4} \;e^{-k_s'}
\,. \notag
\end{align}
The Darboux coordinates $(l_s,k_s')$ are equally good to 
represent the Poisson structure of $\CM_G(C_{0,4})$, but they 
have the advantage that the expressions for $L_\si$ do not 
contain square-roots. This will later turn out to be important.
