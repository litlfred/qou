---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-013-43-the-haar-functional
section_title: "The Haar functional"
section_number: 4.3
pages: 27-28
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.952
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:QPlane:Haar}
Recall from Definition \ref{leftinv} that a linear functional on $\cA$ is called a left invariant Haar functional if it satisfies
\Eq{(1\ox h)(\D x) = h(x)\cdot 1_{M(\cA)},}
and a right invariant Haar functional if it satisfies
\Eq{(h\ox 1)(\D x)=h(x)\cdot 1_{M(\cA)},}
where $1_{M(\cA)}$ is the unital element in the multiplier algebra $M(\cA)$.

\begin{Thm}\label{Haar} There exists a left invariant Haar functional on $\cA$, given by
\Eq{h\left(\int_{\R+i0}\int_\R f(s,t)A^{ib\inv s}B^{ib\inv t}dsdt \right) = f(0,iQ).}
\end{Thm}
\begin{proof} From Proposition \ref{coprod}, the coproduct is given by
\begin{eqnarray*}
&&\D\left(\int_{\R+i0}\int_\R f(s,t)A^{ib\inv s}B^{ib\inv t}dsdt \right) \\
&=&\int_{\R+i0}\int_\R\int _C f(s,t)\frac{G_b(-i\t)G_b(i\t-it)}{G_b(-it)}A^{ib\inv s}B^{ib\inv (t-\t)}\ox A^{ib\inv (s+t-\t)}B^{ib\inv \t} d\t dsdt \\
&=&\int_\R\int_{\R-i0}\int _C f(s,t+\t-s)\frac{G_b(-i\t)G_b(is-it)}{G_b(is-it-i\t)}A^{ib\inv s}B^{ib\inv (t-s)}\ox A^{ib\inv t}B^{ib\inv \t} d\t dsdt. \\
\end{eqnarray*}
In the last step, we push the contour of $t$ back to the real line, and the contour of $\t$ to be the real line that goes above the pole at $\t=0$ only. This will force the contour of $s$ to move below the pole at $s=t$.

Now as a function of $\t$ the integrand is well-defined for $0<Im(\t)<Q$. Therefore to apply the Haar functional, we take the analytic continuation to $\t=iQ$ by $$\dis\t=\lim_{\e\to 0}iQ-i\e.$$ Using Corollary \ref{delta}, we have
\begin{eqnarray*}
&=&\lim_{\e\to 0}\int_{\R-i0} f(s,iQ-s-i\e)\frac{G_b(Q-\e)G_b(is)}{G_b(Q+is-\e)}A^{ib\inv s} B^{ib\inv (-s)}ds\\
&=&f(0,iQ)
\end{eqnarray*}
as desired.
\end{proof}

Using exactly the same technique, we can derive the counit for $\cA$:
\begin{Cor} The counit is given by
\Eq{\e(f) = \lim_{t\to 0} G_b(Q+it)\int_\R f(s,t)ds}
and satisfies
\Eq{(1\ox \e)\D = Id_\cA = (\e\ox 1)\D.}
\end{Cor}
