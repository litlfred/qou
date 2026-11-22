---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-009-32-integral-transformations
section_title: "Integral transformations"
section_number: 3.2
pages: 19-22
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.967
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:QDilog:Int}
Here we describe several properties of the quantum dilogarithm involving integrations.

\begin{Lem}\label{FT} \cite[(3.31), (3.32)]{BT} We have the following Fourier transformation formula:
\Eq{\int_{\R+i0} e^{2\pi i t r}\frac{e^{-\pi i t^2}}{G_b(Q+i
t)}dt=\frac{\bar{\ze_b}}{G_b(\frac{Q}{2}-ir)}=g_b(e^{2\pi b r}), }
\Eq{\int_{\R+i0} e^{2\pi i t r}\frac{e^{-\pi Qt}}{G_b(Q+i
t)}dt=\ze_b G_b(\frac{Q}{2}-ir)=\frac{1}{g_b(e^{2\pi br})}=g_b^*(e^{2\pi br}) ,} where the contour goes above the pole
at $t=0$.

Using the reflection properties, we also obtain \Eq{\int_{\R+i0} 
e^{2\pi i t r}e^{\pi Q t}G_b(-i
t)dt=\frac{\bar{\ze_b}}{G_b(\frac{Q}{2}-ir)},}
\Eq{\int_{\R+i0} 
e^{2\pi i t r}e^{\pi it^2}G_b(-it)dt=\ze_b G_b(\frac{Q}{2}-ir),}
where again the contour goes above the pole at $t=0$.
\end{Lem}




\begin{Lem} \label{qbi}\cite[B.4]{BT} $q$-Binomial Theorem:
For positive self-adjoint variables $u,v$ with $uv=q^2vu$, we have:
\Eq{(u+v)^{ib\inv t}=\int_{C}\veca{it\\i\t}_b u^{ib\inv (t-\t)}v^{ib\inv \t}d\t ,}
where the $q$-beta function (or $q$-binomial coefficient) is given by
\Eq{\veca{t\\\t}_b=\frac{G_b(-\t)G_b(\t-t)}{G_b(-t)},}
and $C$ is the contour along $\R$ that goes above the pole at $\t=0$
and below the pole at $\t=t$.
\end{Lem}

\begin{Lem}\label{tau} \cite[Lem 15]{PT2} We have the Tau-Beta Theorem:
\Eq{\int_C e^{-2\pi \t \b}
\frac{G_b(\a+i\t)}{G_b(Q+i\t)}d\t =\frac{G_b(\a)G_b(\b)}{G_b(\a+\b)},}
where the contour $C$ goes along $\R$ and goes above the poles of
$G_b(Q+i\t)$ and below those of $G_b(\a+i\t)$. By the asymptotic properties of $G_b$, the integral converges for $Re(\b)>0, Re(\a+\b)<Q$.
\end{Lem}

\begin{Lem}\label{45}Rewriting the integral transform in \cite{Vo} in terms of $G_b$, we obtain the 4-5 relation given by:
\Eq{\int_C d\t e^{-2\pi \c\t}\frac{G_b(\a+i\t)G_b(\b+i\t)}{G_b(\a+\b+\c+i\t)G_b(Q+i\t)}=\frac{G_b(\a)G_b(\b)G_b(\c)}{G_b(\a+\c)G_b(\b+\c)},}
where the contour $C$ goes along $\R$ and goes above the poles of the denominator, and below the poles of the numerator. By the asymptotic properties of $G_b$, the integral converges for $Re(\c)>0$.
\end{Lem}

An important corollary of Lemma \ref{tau} is the following:
\begin{Cor} \label{delta} Let $f(z)\in \cW$ (cf. Definition \ref{WDef}), then we have
\Eq{\lim_{\e\to 0}\int_C\frac{G_b(Q-\e)G_b(iz)}{G_b(Q+iz-\e)} f(z)dz = f(0),}
where the contour go above the poles of the denominator and below the poles of the numerator. Alternatively, we can shift the poles so that the expression is an integration over $\R$:
\Eq{\lim_{\e\to 0}\int_\R\frac{G_b(Q-2\e)G_b(iz+\e)}{G_b(Q+iz-\e)} f(z)dz = f(0).}
Formally as distribution,
\Eq{\frac{G_b(Q)G_b(ix)}{G_b(Q+ix)}=\d(x),\tab x\in\R.}
\end{Cor}

\begin{proof} By Lemma \ref{tau}, we have
\begin{eqnarray*}
&&\lim_{\e\to 0}\int_\R\frac{G_b(Q-2\e)G_b(iz+\e)}{G_b(Q+iz-\e)} f(z)dz\\
&=&\lim_{\e\to 0}\int_\R \int_C e^{-2\pi\t(iz+\e)}\frac{G_b(Q-2\e+i\t)}{G_b(Q+i\t)}f(z)d\t dz,\\
\end{eqnarray*}
where the contour $C$ goes above the pole at $\t=0$.

Now by Corollary \ref{asymp}, the integrand in $\t$ has asymptotics
$$\left|e^{-2\pi\t\e}\frac{G_b(Q-2\e+i\t)}{G_b(Q+i\t)}\right|\sim\left\{\begin{array}{cc}e^{-2\pi \t\e}& \t\to\oo\\ e^{2\pi \t\e}&\t\to-\oo\end{array}.\right.$$
Hence the integrand is absolutely convergent in both $\t$ and $z$. Hence we can interchange the integration order of $\t$ and $z$,
\begin{eqnarray*}
&=&\lim_{\e\to 0}\int_C \int_\R e^{-2\pi\t(iz+\e)}\frac{G_b(Q-2\e+i\t)}{G_b(Q+i\t)}f(z)dz d\t \\
&=&\lim_{\e\to 0}\int_C e^{-2\pi\t\e}\frac{G_b(Q-2\e+i\t)}{G_b(Q+i\t)}(\cF f)(\t)d\t ,\\
\end{eqnarray*}
where $\cF$ is the Fourier transform. Since $f\in \cW, \cF f\in \cW$ as well, hence the integrand is absolutely convergent independent of $\e$. Hence we can interchange the limit and finally obtain
\begin{eqnarray*}
&=&\int_\R \lim_{\e\to 0}e^{-2\pi\t(iz+\e)}\frac{G_b(Q-2\e+i\t)}{G_b(Q+i\t)}(\cF f)(\t)d\t  \\
&=&\int_\R(\cF f)(\t)d\t \\
&=&f(0),
\end{eqnarray*}
where the last line follows from the properties of Fourier transform.
\end{proof}
\begin{Rem}
This is just the analogue of the delta function as a hyperfunction. Since the integrand is $0$ unless $z$ is close to 0, it suffices to notice that near $z=0$, from the analytic properties for $G_b$  we have $G_b(z) \sim \frac{1}{G_b(Q-z)}\sim\frac{1}{2\pi z}$, so that
\begin{eqnarray*}
&&\lim_{\e\to0}\frac{G_b(Q-2\e)G_b(iz+\e)}{G_b(Q+iz-\e)}\\
&\sim&\lim_{\e\to0} \frac{2\e}{2\pi i(iz-\e)(iz+\e)}\\
&=&\lim_{\e\to0}\frac{1}{2\pi i}\left(\frac{1}{z-i\e}-\frac{1}{z+i\e}\right)\\
&=&\d(z).
\end{eqnarray*}

Intuitively, restricting to $x\in\R$, $\frac{G_b(Q)G_b(ix)}{G_b(Q+ix)}$ is always 0 unless $x=0$, in which case it is $\oo$. The properties of $G_b$ say that it gives the right normalization to be a delta function.
\end{Rem}

The other variants which we will also use include:
\begin{Cor} For $f(x)\in\cW$, we have
\begin{eqnarray}
\lim_{\e\to0}\int_\R \frac{G_b(\e-ix)G_b(\e+ix)}{G_b(2\e)}f(x)dx &=& f(0),\\
\lim_{\e\to0}\int_\R \frac{G_b(\e+ix-b)G_b(Q+b-2\e)}{G_b(Q+ix-\e)}f(x)dx &=& -q^2 f(0)+f(-ib),
\end{eqnarray}
or formally
\begin{eqnarray}
\frac{G_b(-ix)G_b(ix)}{G_b(0)}&=&\d(x),\\
\frac{G_b(ix-b)G_b(Q+b)}{G_b(Q+ix)}&=&-q^2\d(x)+\d(x+ib),
\end{eqnarray}
which follows from the functional properties of $G_b(x)$ and similar arguments as above.
\end{Cor}

A particular important case in the study of modular double (see the next section) is proved in \cite[Lem 3]{BT} and \cite{Vo} which can also be obtained from the above arguments:
\begin{Cor}\label{u+v} Let $u,v$ be positive self-adjoint operators satisfying $uv=q^2vu$. By taking $t\to -ib\inv$ in Lemma \ref{qbi} we obtain
\Eq{(u+v)^{1/b^2} = u^{1/b^2}+v^{1/b^2}.}
\end{Cor}
