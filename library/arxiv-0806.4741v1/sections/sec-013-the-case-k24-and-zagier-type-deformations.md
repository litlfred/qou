---
doc_id: arxiv-0806.4741v1
doc_title: "The deformation quantizations of the hyperbolic plane"
section_id: sec-013-the-case-k24-and-zagier-type-deformations
section_title: "The case k=24 and Zagier type deformations"
section_number: null
pages: 19-20
source_pdf: 0806.4741v1.pdf
source_sha256: 5e7ad85a99fb3552
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.99
doc_brief: "The deformation quantizations of the hyperbolic plane — We describe the space of (all) invariant deformation quantizations on the hyperbolic plane D as solutions of the evolution of a second order"
---
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
