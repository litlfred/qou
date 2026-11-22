---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-032-74-rises-in-random-permutations
section_title: "Rises in random permutations"
section_number: 7.4
pages: 58-61
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.96
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\label{subsec:rises}
As illustrated in the previous section,
the methods of singularity analysis and the \emph{transfer theorems} between the singularities of a generating series and the asymptotic behavior of its coefficients (see \emph{e.g.} \cite[Chapter VI]{FSe09})
can be use to prove mod-$\phi$ convergence
(this is not surprising as they can be used to establish the related concept of {\em quasi-powers},
see Section~\ref{Subsect:QP}).
We examine here another example where we do not have strictly speaking mod-$\phi$ convergence 
since the reference law is not infinitely divisible,
but where our methods can nevertheless be used.

If $\sigma \in \sym(n)$ is a permutation, a \emph{rise} of $\sigma$ is an integer $i \in \lle 1,n-1\rre$ such that $\sigma(i)<\sigma(i+1)$. The number of rises $R(\sigma)$ is thus a quantity between $0$ and $n-1$, the two extremal values corresponding to the permutations $n(n-1)\ldots 2 1$ and $12\ldots (n-1)n$. We denote $R_n=R(\sigma_n)$ the random variable which counts the number of rises of a random permutation $\sigma_n \in \sym(n)$ chosen under the uniform measure. The double generating series
$$R(z,t) = \sum_{n=0}^\infty \esper[\E^{z R_n}]\,t^n$$
is computed in \cite[III.7, p. 209]{FSe09}:
$$R(z,t)=\frac{\E^{z}-1}{\E^z-\E^{t(\E^z-1)}}.$$
If $\Re (z)\leq \log 2$, then $|\E^{z}|\leq 2$ and the smallest (in modulus) root of the denominator is 
$$t=\rho(z)=\frac{z}{\E^z-1}.$$
We then have $R(z,t) = \frac{1}{\rho(z)-t} + (\E^z-1)\,S(z,t)$ with $S(z,t)=\frac{1}{\E^z - \E^{t(\E^z-1)}}-\frac{1}{z-t(\E^z-1)}$ analytic in $t$ and on the band $z \in \mathcal{S}_{(-\infty,\log 2)}$. This implies:

\begin{theorem}[\cite{FSe09}, p. 658]\label{thm:flajoletrises}
For $z \in \mathcal{S}_{(-\infty,\log 2)}$, one has locally uniformly
$$\esper[\E^{zR_n}] = \tau(z)^{n+1} + O(|z|\,2^{-n}),$$
where $\tau(z) = \frac{\E^z-1}{z}$.
\end{theorem}
\noindent Notice that $\tau(z) = \frac{\E^z-1}{z} = \int_0^1 \E^{zu}\,du$ is the Laplace transform of a uniform random variable $U$ in the interval $[0,1]$. 
Informally, the previous should be thought as follows: $(R_n)_{n \in \N}$ converges mod-$U$ on $\mathcal{S}_{(-\infty,\log 2)}$ with parameters $t_n=n+1$ and limit $\psi(z)=1$.
However, the uniform law $U$ is not infinitely divisible, and $\tau(z)$ vanishes on any $z \in 2\I \pi\Z$,
therefore the error term $O(|z|\,2^{-n})$ cannot be rewritten as a multiplicative error term,
as we did before.
Still, every computation of Section \ref{sec:nonlattice} can be performed in this case. 
Let us stress out the necessary adjustments:
\begin{itemize}
    \item Berry-Esseen estimates. Set $F_n(x) = \proba[R_n - \frac{n+1}{2}\geq \sqrt{\frac{n+1}{12}}\,x]$ and $G_n(x)=\int_{-\infty}^x g(y)\,dy$. We have by Feller's lemma
    \begin{align*}
    |F_n(x)-G_n(x)| &\leq \frac{24m}{\Delta\pi\sqrt{t_n}} + \frac{1}{\pi\sqrt{t_n}} \int_{[\pm\delta \sqrt{t_n}]} \left|\frac{f_n^*(\xi)-\E^{-\frac{\xi^2}{2}}}{\xi}\right|\,d\xi  \\
    &\quad+ \frac{1}{\pi\delta\sqrt{t_n}} \int_{[\pm \Delta \sqrt{t_n}]\setminus [\pm \delta \sqrt{t_n}]} \left|f_n^*(\xi)-\E^{-\frac{\xi^2}{2}}\right|\,d\xi,
    \end{align*}
    where as in the proof of Proposition \ref{prop:berryesseen}, $f_n^*(\xi)$ is the Fourier transform of $\frac{R_n-\frac{t_n}{2}}{\sqrt{\frac{t_n}{12}}}$.
    From Theorem \ref{thm:flajoletrises} and a Taylor expansion of $\tau(\I \xi)$, one has 
    $$f_n^*(\xi) = \E^{-\frac{\xi^2}{2}\left(1+O\!\left(\frac{\xi^2}{t_n}\right)\right)} + O(|\xi|\,2^{-t_n}).$$
    In the first integral of Feller's bound, we are integrating 
    $$\left|\frac{f_n^*(\xi)-g^*(\xi)}{\xi}\right| = O\left(\delta^2\,\E^{-\frac{\xi^2}{2}}\right)+O(2^{-t_n}),$$
    so we get a $o(\frac{1}{\sqrt{t_n}})$ as $\delta$ goes to zero. Then, regarding the second integral, we are integrating a $O((q_\delta)^{t_n})$ for some $q_\delta\in [\frac{1}{2},1)$, so it does not contribute to the asymptotics. Thus, we get the uniform estimate $|F_n(x)-G_n(x)|=o(\frac{1}{\sqrt{t_n}})$ as in Proposition \ref{prop:berryesseen}.\vspace{2mm}
    \item Tilting method and large deviation estimates. When tilting by $h > 0$, the new random variable $R_n^h$ with law $\proba[R_n^h \in dy]=\frac{\E^{hy}}{\esper[\E^{hR_n}]}\,\proba[R_n \in dy]$ has its Fourier transform that has asymptotics
    $$\frac{\tau(h+\I\xi)^{n+1}+O(2^{-n})}{\tau(h)^{n+1}+O(2^{-n})} = \left(\frac{\tau(h+\I \xi)}{\tau(h)}\right)^{n+1} (1+o(1))$$ 
    the second formula holding if $h$ and $\xi$ are small enough (more precisely, we want $0<h<\log 2$ and then $\xi$ small enough with bounds depending on $h$).
    Notice that the new exponent $\frac{\tau(h+\I \xi)}{\tau(h)}$ does not vanish anymore, so we can now use the same argument as in Theorem \ref{thm:mainnonlattice}. Thus, if $F$ is the Legendre-Fenchel transform of the uniform law on $[0,1]$ (not really explicit), and if $h$ is the solution of $\frac{1+\eps}{2}=\eta'(h)$ with $\eta(h) = \log\left(\frac{\E^h-1}{h}\right)$, then for 
    $$\eps \in(2\eta'(0)-1,2\eta'(\log 2)-1) = \left(0,\,3-\frac{2}{\log 2}\right)\supseteq (0,0.114),$$
     we obtain the large deviation estimate:
    $$\proba\!\left[R_n \geq \frac{(1+\eps)(n+1)}{2}\right] = \frac{\E^{-t_n\,F(\frac{1+\eps}{2})}}{h\sqrt{2\pi t_n\,\eta''(h)}} (1+o(1))$$
    since we have mod-$U$ convergence of $(R_n)_{n \in \N}$ with parameters $t_n=\frac{n+1}{2}$ and residue $\psi(x)=1$. Similarly, for the negative deviations, the estimate of the Fourier transform of the tilted random variable $R^h_n$ can be used if $h>h_0$, where $h_0 \approx -1.594$ is the solution of the equation $\tau(h)=\frac{1}{2}$. Therefore, for
    $$\eps \in \left(0,\,\frac{2}{h_0}-1\right) \supseteq (0,0.254),$$
    we have
    $$\proba\!\left[R_n \leq \frac{(1-\eps)(n+1)}{2}\right] = \frac{\E^{-t_n\,F(\frac{1-\eps}{2})}}{|h|\sqrt{2\pi t_n\,\eta''(h)}} (1+o(1)),$$
    where $h$ is the solution of $\frac{1-\eps}{2}=\eta'(h)$.\vspace{2mm}
    \item Extended central limit theorem. The result of Lemma \ref{lem:technicqdelta_nonlattice} holds, because
\begin{align*}
\left|\frac{\tau(h+\I u)}{\tau(h)}\right|^2 &= \left|\frac{\E^{h+\I u}-1}{\E^{h}-1}\,\frac{h}{h+\I u}\right|^2 \\
&=\left(1+\frac{2\E^h\,(1-\cos u)}{(\E^h-1)^2}\right) \,\frac{h^2}{h^2+u^2} = \frac{h^2+2t(h)\,(1-\cos(u))}{h^2+u^2},
\end{align*}
where $t(h) = \frac{h^2\E^h}{(\E^h-1)^2} \leq 1$ for any $h$. From this inequality, one deduces that
$$q_\delta = \max_{u \in \R\setminus [-\delta,\delta]} \left|\frac{\tau(h+\I u)}{\tau(h)}\right| \leq 1-D\delta^2 $$
for some constant $D>0$ and any $h \in (-\eps,\eps)$, with $\eps$ small enough.\medskip

Since $\eta(x)=\log (\tau(x))$ has Taylor expansion $\frac{x}{2}+\frac{x^2}{24}-\frac{x^4}{2880}+o(x^5)$, we thus get from Equation \eqref{EqCramerOrdreMNL}:
$$\proba\!\left[R_n \geq \frac{n+1}{2} + \sqrt{\frac{n+1}{12}}\,y\right] =\frac{(1+o(1))}{y\sqrt{2\pi}}\,\exp\left(-\frac{y^2}{2} + \frac{y^4}{240t_n}\right)$$
for any positive $y$ with $y = o((t_n)^{\frac{1}{2}-\frac{1}{6}}) = o((t_n)^{\frac{5}{12}})$. 
\end{itemize}
\bigskip
