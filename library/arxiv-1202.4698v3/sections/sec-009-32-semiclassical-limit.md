---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-009-32-semiclassical-limit
section_title: "Semiclassical limit"
section_number: 3.2
pages: 9-10
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.921
latex_coverage_ratio: 0.983
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
In the
following we will assume that $\al_k\in\BR$,
$0<\al_k<Q/2$.
In order to 
study the quasi-classical limit of (\ref{6j3}) let us write the 
right hand side
 of \rf{6j3} in the form 
\begin{equation}\label{Int}
I:=E(\underline{\al})\int_{\CC}du \,\CI(a,b;u)\,.
\end{equation}
The integrand $\CI(a,b;u)$ may be written as
\begin{equation}\label{int}
\CI(a,b;u)=
\frac{\prod_{i=1}^4 S_b(a_i+u)}{S_b(-Q+u) \prod_{i=1}^3 S_b(Q-b_i+u)} du,
\end{equation}
where
\begin{align}
& a\equiv[ a_1,a_2,a_3,a_4 ] \ = \ [-\alpha_s-\alpha_1-\alpha_2, -\alpha_s-\alpha_3-\alpha_4, -\alpha_t-\alpha_1-\alpha_4, -\alpha_t-\alpha_2-\alpha_3], \nonumber \\ & 
b\equiv[ b_1,b_2,b_3 ] \ = \ [ \alpha_s+\alpha_t+\alpha_1+\alpha_3, \alpha_s+\alpha_t+\alpha_2+\alpha_4, \alpha_1+\alpha_2+\alpha_3+\alpha_4 ].
\end{align}
The quasi-classical limit of $\CI(a,b;u)$ is easily determined with the help
of formula \rf{Sbscl} in Appendix \ref{Qdil}. In order to write
the result in an convenient form
let us reparameterize variables
$$e^{-2 \pi \textup{i} b  \alpha_k+\pi \textup{i}} \equiv A_k\,,\qquad k\in\{1,2,3,4,s,t\}\,.
$$
Introducing the integration variables $v:=2\pi b(u-Q/2)$ 
we get an integral of the form 
\begin{equation}\label{Int'}
I=D(\underline{\al})\int_{\CC-Q/2}
\frac{dv}{2\pi b} 
\,\CJ(a,b;v)
\end{equation} 
whose integrand $\CJ(a,b;v)$ 
has quasi-classical asymptotics
\begin{equation}
\CJ(a,b;v)\,=\,\exp\bigg(\frac{1}{2\pi b^2}\,U(e^{\textup{i}v},\underline{{A}})\bigg)
\Big(1+\CO(b^2)\Big)\,,
\end{equation}
with $U(e^{\textup{i}v},\underline{{A}})$ given by the formula \rf{Udef}.
The quasiclassical asymptotics of the prefactor in \rf{Int'} is
\beqa
&& D_{\rm cl}(\underline{{A}}) = \exp \left( \frac{1}{2 \pi \textup{i} b^2} 
\Big( \Delta(\underline{{A}}) - \frac53 \pi^2 \Big) \right)\,,
\eeqa
where $\Delta(\underline{{A}})$ was defined in \rf{Deltadef} above.


Now we are ready to perform the saddle-point approximation for 
the integral (\ref{Int}). 
The saddle points are the solutions of the equation \rf{eq}.
The values of the b-$6j$ at these points are
$$
\exp \bigg( \frac{1}{2 \pi \textup{i} b^2} 
W_{\pm}(\underline{{A}}) \bigg),\quad{\rm where}
\quad
W_{\pm}(\underline{{A}}) = U(z_{\pm},\underline{{A}}) + 
\Delta(\underline{{A}}) - \frac53 \pi^2 + 2 \pi \textup{i} \log u_{\pm}.
$$
Since $u_{\pm}=e^{\pm \pi \textup{i} \phi}$, $\phi\in\BR$ as noted
above,  we find that
\beq \label{quasclas}
W_{\pm}(\underline{{A}}) = U(z_{\pm},\underline{{A}}) + 
\Delta(\underline{{A}}) - \frac53 \pi^2 \mp 2 \pi^2 \phi.
\eeq
Taking the imaginary part of (\ref{quasclas}) one sees 
that we are  getting the volume 
of a hyperbolic tetrahedron \rf{volume}.
