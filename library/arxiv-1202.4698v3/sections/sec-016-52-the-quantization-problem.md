---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-016-52-the-quantization-problem
section_title: "The quantization problem"
section_number: 5.2
pages: 14-15
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 1.0
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
The quantum Teichm\"uller theory \cite{Fo97,Ka97,CF99,CF00}
constructs a non-commutative
algebra $\CA_b$ 
deforming the Poisson-algebra of geodesic length functions
on Teichm\"uller space. In the so-called 
length representation \cite{Teschner:2003at,T05} one may construct 
natural representations of this algebra associated to pants 
decompositions of the Riemann surface under consideration. 

For the case under consideration, the aim is to construct a 
one-parameter family
of non-commutative deformations $\CA_b$ 
of the Poisson-algebra
of functions on $\CT_{0,4}\equiv\CT(C_{0,4})$ which has generators
$\CL_s$, $\CL_t$, $\CL_u$ corresponding to the 
functions 
$L_\si$, $\si\in\{s,t,u\}$, respectively. There is one algebraic
relation that should be satisfied
among the three generators $\CL_s$, $\CL_t$, $\CL_u$.

Natural representations $\pi_\si$, $\si\in\{s,t,u\}$, 
of $\CA_b$ by operators on suitable spaces of functions 
$\psi_\si(l_\si)$ can be constructed in terms of the quantum counterparts of
the Darboux variables $l_\si$, $k_\si$, now represented by the
operators
$\sll_\si$, $\sk_\si$ defined as
\begin{equation}
\sll_\si\,\psi_\si(l_\si):=\,l_\si\,
\psi_\si(l_\si)\,,\qquad 
\sk_s\,\psi_\si(l_\si):=4\pi b^2
\frac{1}{\textup{i}}\frac{\pa}{\pa l_s}\psi_\si(l_\si)\,.
\end{equation}
The operator $\pi_\si(\CL_\si)$ acts as 
operator of multiplication in the representation $\pi_\si$,

$\pi_\si(\CL_\si)\equiv 2\cosh(\sll_\si)/2$.

The remaining two generators of $\CA_b$ are then represented 
as difference operators. Considering the representation
$\pi_s$, for example, we will find that $\pi_s(\CL_t)$
can be represented in the form
\begin{equation}\label{Diffop}
\pi_s(\CL_t)\psi_s(l_s)\,=\,\big[ 
D_+(l_s)e^{+\sk_s}+D_0(l_s)+D_-(l_s)e^{-\sk_s}\big]\psi_s(l_s)\,.
\end{equation}
This formula should of course reproduce \rf{FN-FK} or \rf{FN-FK'}  
in the classical 
limit, but due to ordering issues and other
possible quantum corrections it is a priori far from obvious how 
to define the coefficients $D_\ep(l_s)$, $\ep=-,0,+$. 

Note, in particular, that the 
requirement that $\pi_s(\CL_s)$ acts as multiplication 
operator leaves a large freedom. 
A gauge transformation 
\begin{equation}\label{gauge}
\psi_s(l_s)\,=\,e^{\textup{i}\chi(l_s)}\psi_s'(l_s)\,,
\end{equation}
would lead to a representation $\pi_s'$ of the form \rf{Diffop}
with $\sk_s$ replaced by
\begin{equation}\label{q-can}
\sk'_s:=\,\sk_s+4\pi b^2\,\pa_{l_s}\chi(l_s)\,.
\end{equation}
This is nothing but the quantum version of a
canonical transformation $(l_s,k_s)\ra (l_s,k_s+f(l_s))$. 
The representation 
$\pi_s'(\CL_t)$ may then be obtained from \rf{Diffop}
by replacing 
$D_\ep(l_s)\ra E_\ep(l_s)$ with 
$E_\ep(l_s)$ equal to $e^{\textup{i}(\chi(l_s-4\ep \textup{i} \pi b^2)-\chi(l_s))}
D_\ep(l_s)$ for $\ep=-1,0,1$. Fixing a particular set of Darboux coordinates
corresponds to fixing a particular choice of the
coefficients $D_\ep(l_s)$ in \rf{Diffop}.
