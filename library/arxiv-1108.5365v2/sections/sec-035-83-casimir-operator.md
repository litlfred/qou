---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-035-83-casimir-operator
section_title: "Casimir operator"
section_number: 8.3
pages: 79-82
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.976
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:regular:Casimir}
Next we will study the action induced from the pairing with the multiplicative unitary $\bW$. It turns out that the technical difficulty comes from the analysis of the following positive operator:
\Eq{\bC=e^{2\pi bx}+e^{-2\pi bx}+e^{-2\pi bp},}
which is studied in detail in \cite{Ka4} in a different context. This expression comes from the Casimir operator defined by 
\Eq{C=FE+\frac{qK^2+q\inv K^{-2}-2}{(q-q\inv)^2}.}
More precisely, under the pairing given in the next section, the Casimir operator is given by
\Eq{C=\left(\frac{i}{q-q\inv}\right)^2 (e^{2\pi bx}+e^{-2\pi bx}+e^{-2\pi bp}+2).}
\begin{Prop} For $\l \in \R^+$, 
\Eq{\Phi_\l(s_2):=S_b(-ix+i\l)S_b(-ix-i\l)}
is an eigenfunction for the operator $\bC$ with eigenvalue $e^{2\pi b\l}+e^{-2\pi b\l}$.
\end{Prop}
\begin{proof} We need to solve
\Eq{\bC\Phi_\l(x) = (e^{2\pi b\l}+e^{-2\pi b\l}) \Phi_\l(x).}

We consider $$\bC- (e^{2\pi b\l}+e^{-2\pi b\l}) = \bC-2\cos(2\pi ib\l)=2\cos(2\pi ib x)-2\cos(2\pi ib\l)+e^{2\pi b p_{s_2}}.$$

From the angle sum formula, we have
\begin{eqnarray*}
&&2\cos(2\pi ib x)-2\cos(2\pi ib\l)\\
&=&-4\sin(\pi ib(x-\l))\sin(\pi ib(x+\l)),\\
\end{eqnarray*}
and from the functional equation \eqref{funceq} $$S_b(x+b)=2\sin(\pi bx)S_b(x),$$ we immediately see that
\begin{eqnarray*}
&&e^{2\pi bp_{x}}\cdot S_b(-ix+i\l)S_b(-ix-i\l)\\
&=&S_b(-ix+i\l+b)S_b(-ix-i\l+b)\\
&=&4\sin(\pi ib(-x+\l))\sin(\pi ib(-x-\l))S_b(-ix+i\l)S_b(-ix-i\l)\\
&=&4\sin(\pi ib(x-\l))\sin(\pi ib(x+\l))S_b(-ix+i\l)S_b(-ix-i\l).
\end{eqnarray*}
Hence $\Phi_\l(x) =S_b(-ix+i\l)S_b(-ix-i\l)$ satisfies the above eigenvalue equation.
\end{proof}

Therefore we introduce the following transformation
\begin{Def} We define the integral transformation
$$\Phi\inv: L^2(\R^+, d\mu(\l))\to L^2(\R)$$
\Eq{F(\l)\mapsto f(x):=\lim_{\e\to 0}\int_0^\oo \Phi_\l(x+i\e)e^{-2\pi x\e} F(\l) d\mu(\l)}
where $d\mu(\l)=|S_b(Q+2i\l)|^2d\l$.
\end{Def}

\begin{Thm}\label{Casimir} $\Phi\inv$ is a unitary transformation that intertwines $e^{2\pi b\l}+e^{-2\pi b\l}$ and $\bC$.
\end{Thm}
\begin{proof} We compute the inner product for $f,g\in \cW^+$ where $\cW^+$ is the dense subspace
$$\cW^+:=\{f(x)\in C_\oo(\R^+): F(y):=f(e^y)\in \cW\}.$$
Note that
$$\over[\Phi_\l(x)]=\frac{1}{S_b(Q-ix-i\l)S_b(Q-ix+i\l)}.$$ We have
\begin{eqnarray*}
&&\<\Phi\inv f, \Phi\inv g\>\\
&=&\lim_{\e\to 0}\int_\R \int_0^\oo \int_0^\oo \frac{S_b(\e-ix-i\l)S_b(\e-ix+i\l)e^{-4\pi x\e}}{S_b(Q-\e-ix-i\b)S_b(Q-\e-ix+i\b)}f(\l)\over[g(\b)]d\mu(\l) d\mu(\b) dx\\
&=&\lim_{\e\to 0}\int_\R \int_0^\oo \int_0^\oo \frac{G_b(\e+ix-i\l)G_b(\e+ix+i\l)e^{\pi i\l^2-\pi i\b^2}e^{-2\pi x(Q-4\e)}}{G_b(Q-\e+ix-i\b)G_b(Q-\e+ix+i\b)}f(\l)\over[g(\b)]d\mu(\l) d\mu(\b) dx\\
\end{eqnarray*}
which means the contour for $x$ separates the poles of the numerator and denominator.

Now by Corollary \ref{asymp} the integrand has asymptotics in $x$
$$\left|\frac{G_b(\e+ix-i\l)G_b(\e+ix+i\l)e^{\pi i\l^2-\pi i\b^2}e^{-2\pi x(Q-4\e)}}{G_b(Q-\e+ix-i\b)G_b(Q-\e+ix+i\b)}\right|=\left\{\begin{array}{cc}e^{-2\pi x(Q-4\e)}&x\to\oo\\e^{2\pi Qx}&x\to-\oo\end{array}.\right.$$
Hence the integral is absolutely convergent in $x,\l,\b$ and we can interchange the order of integration to bring integration over $x$ inside.

Shifting $x\mapsto x+\b$, and using the 4-5 relation (Lemma \ref{45}), we obtain
\begin{eqnarray*}
&=&\lim_{\e\to 0}\int_0^\oo \int_0^\oo \frac{G_b(Q-4\e)G_b(2\e+i\b-i\l)G_b(2\e+i\b+i\l)}{G_b(Q-2\e+i\b-i\l)G_b(Q-2\e+i\b+i\l)}\cdot\\
&&e^{\pi i\l^2-\pi i\b^2}e^{-2\pi Q\b+8\pi\b\e} f(\l)\over[g(\b)]|S_b(Q+2i\l)|^2|S_b(Q+2i\b)|^2d\l d\b.
\end{eqnarray*}
Note that the integration for $\b$ separates the poles of the numerator and denominator as well, and also since $\l,\b>0$, the case $\b=-\l$ can be ignored, hence we obtain $\d(\l-\b)$ using Lemma \ref{delta}:
\begin{eqnarray*}
&=&\int_0^{\oo}\frac{G_b(2i\l)e^{-2\pi Q\l}}{G_b(Q+2i\l)} f(\l)\over[g(\l)]|S_b(Q+2i\l)|^4d\l\\
&=&\int_0^{\oo} f(\l)\over[g(\l)]|S_b(2i\l)|^2 |S_b(Q+2i\l)|^4d\l\\
&=&\int_0^{\oo} f(\l)\over[g(\l)]|S_b(Q+2i\l)|^2d\l.\\
\end{eqnarray*}
This shows that the map is an isometry. The converse showing the eigenfunctions are also complete is more difficult, and can be found in \cite{Ka4}. The technique involves writing the measure $$|S_b(Q+2i\l)|^2=4\sinh(\pi b\l)\sinh(\pi b^{-1}\l)$$ as linear combinations of 4 exponentials, and calculate the integral directly using hints from hyperfunctions.

From the proof we therefore deduce the inverse map of the unitary transformation to be the complex conjugate
$$\Phi: L^2(\R)\to L^2(\R^+, d\mu(\l))$$
$$f(x)\mapsto F(\l):= \int_{\R-i0} \frac{f(x)}{S_b(Q-ix-i\l)S_b(Q-ix+i\l)} dx,$$
where the contour goes below the poles.

Since $\Phi_\l(x)$ are the eigenfunctions satisfying $\bC\Phi_\l(x) = (e^{2\pi b\l}+e^{-2\pi b\l})\Phi_\l(x)$, formally the integral transformation with $\Phi_\l(x)$ as kernel will intertwine the action.
\end{proof}
