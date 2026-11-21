---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-007-32-the-residue-of-mod-gaussian-convergence-as-a
section_title: "The residue of mod-Gaussian convergence as a limiting law"
section_number: 3.2
pages: 13-15
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.928
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
We can now state and prove the main result of this Section. We assume the hypotheses \eqref{hyp:laplacemod} and \eqref{hyp:l1mod}, and keep the same notation as before.

\begin{theorem}\label{thm:mainl1}
The following assertions are equivalent:\vspace{2mm}
\begin{enumerate}[(i)]
\item The sequence $(\frac{Y_n}{t_n})_{n \in \N}$ is tight.\label{l1i}\vspace{1mm}
\item The sequence $(\frac{Y_n}{t_n})_{n \in \N}$ converges in law to a variable with density $\psi(x)/\int_{\R}\psi(x)\,dx$.\label{l1ii}\vspace{1mm}
\item The convergence $\psi_n \to \psi$, which is supposed locally uniform on $\R$, also occurs in $\mathrm{L}^1(\R)$.\label{l1iii}\vspace{1mm}
\end{enumerate}
We shall then say that $(X_n)_{n \in \N}$ converges in the $\mathrm{L}^1$-mod-Gaussian sense with parameters $t_n$ and limiting function $\psi$. In this setting, the residue $\psi$ can be interpreted as the limiting law of $(X_n)_{n \in \N}$ after an appropriate change of measure.
\end{theorem}

\begin{proof}
Since the Gaussian variable $G_n$ of variance $\frac{1}{t_n}$ converges in probability to $0$, $(\frac{Y_n}{t_n})_{n \in \N}$ converges to a law $\mu$ if and only if $(W_n)_{n \in \N}$ converges to the law $\mu$. If \eqref{l1iii} is satisfied, then by Proposition \ref{prop:enlemma},
$$\lim_{n \to \infty} \proba[W_n \leq w] = \frac{\int_{-\infty}^w \psi(x)\,dx}{\int_{-\infty}^\infty \psi(x)\,dx},$$
so the cumulative distribution functions of the variables $W_n$ converge to the cumulative distribution function of the law $\psi(x)/\int_{\R}\psi(x)\,dx$, and \eqref{l1ii} is established. Obviously, one  also has \eqref{l1ii}$\,\Rightarrow\,$\eqref{l1i}. Finally, if \eqref{l1iii} is not satisfied, then by Scheffe's lemma one  also has
$$\int_{\R}\psi_n(x)\,dx\not\to  \int_{\R}\psi(x)\,dx.$$
However, by Fatou's lemma, $\int_{\R} \psi(x)\,dx \leq \liminf_{n \to \infty} \int_{\R}\psi_n(x)\,dx$. Therefore, the non-convergence in $\mathrm{L}^1$ is only possible if $\int_{\R} \psi(x)\,dx < \limsup_{n \to \infty} \int_{\R}\psi_n(x)\,dx$. Thus, there is an $\eps>0$ and a subsequence $(n_k)_{k \in \N}$ such that
$$\forall k \in \N,\,\,\int_{\R} \psi_{n_k}(x)\,dx \geq \eps + \int_\R \psi(x)\,dx.$$
Then, for all $a,b \in \R$,
\begin{align*}\limsup_{k \to \infty} \,\proba[a \leq W_{n_k} \leq b] &= \limsup_{k \to \infty}\left(\frac{\int_a^b \psi_{n_k}(x)\,dx}{\int_{\R} \psi_{n_k}(x)\,dx} \right) = \frac{\int_a^b \psi(x)\,dx}{\liminf_{k \to \infty} \int_\R \psi_{n_k}(x)\,dx}\\
& \leq \frac{\int_{\R} \psi(x)\,dx}{\eps+\int_{\R} \psi(x)\,dx}<1
\end{align*}
which amounts to saying that $(W_n)_{n \in \N}$ (and therefore $(\frac{Y_n}{t_n})_{n \in \N}$) is not tight; hence, \eqref{l1i} implies \eqref{l1iii}.
\end{proof}
\bigskip

To complete this result, it is important to compare the two notions of \emph{complex} mod-Gaussian convergence and of \emph{integral} $\mathrm{L}^1$-mod-Gaussian convergence. Though there are no direct implication between these two assumptions, the following Proposition shows that the latter notion is a stronger type of convergence:
\begin{proposition}\label{l1stronger}
Let $(X_n)_{n \in \N}$ be a sequence that converges in the $\mathrm{L}^1$-mod-Gaussian sense with parameters $t_n \to \infty$ and limiting function $\psi \in \mathrm{L}^1(\R)$. The estimate of precise large deviations \eqref{eq:upbound} is then satisfied.
\end{proposition}
\begin{proof}
Recall than $Z_n=\esper[\E^{(X_n)^2/2t_n}]=\sqrt{\frac{t_n}{2\pi}}\,\int_{\R}\psi_n(x)\,dx$. We want to compute
$$ \proba[X_n \geq t_n x] = \int_{t_n x}^\infty \proba_n[dy] = Z_n\,\int_{t_n x}^\infty \E^{-\frac{y^2}{2t_n}}\,\qproba_n[dy] =Z_n\,\int_{x}^\infty \E^{-\frac{t_n \,u^2}{2}}\,\proba_{\frac{Y_n}{t_n}}[du].
$$
Suppose for a moment that we can replace the law of $\frac{Y_n}{t_n}$ by the one of $W_n=G_n+\frac{Y_n}{t_n}$ in the previous computation. Then, one obtains from Proposition \ref{prop:enlemma}
$$
Z_n\,\int_{x}^\infty \E^{-\frac{t_n \,u^2}{2}}\,\proba_{W_n}[du]= \sqrt{\frac{t_n}{2\pi}}\,\int_{x}^\infty \E^{-\frac{t_n u^2}{2}}\psi_n(u)\,du.
$$
Fix $\eps>0$. Since $\psi_n$ converges locally uniformly to the continuous function $\psi$, there is an interval $[x,x+\eta]$ such that for $n$ large enough and $u \in [x,x+\eta]$, 
$$\psi(x)-\eps < \psi_n(u)<\psi(x) + \eps.$$
 Therefore, for $n$ large enough,
\begin{align*}
(\psi(x)- \eps)\,\int_{x}^{x+\eta} \E^{-\frac{t_n u^2}{2}}\,du &\leq \int_{x}^{x+\eta} \E^{-\frac{t_n u^2}{2}}\psi_n(u)\,du \leq (\psi(x)+ \eps)\,\int_{x}^{x+\eta} \E^{-\frac{t_n u^2}{2}}\,du\\
\downarrow \qquad& \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad \downarrow \\
(\psi(x)- \eps) \,\frac{\E^{-\frac{t_n x^2}{2}}}{t_n x} &\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad(\psi(x)+ \eps) \,\frac{\E^{-\frac{t_n x^2}{2}}}{t_n x}.
\end{align*}
Indeed, by integration by parts, $\int_x^{x+\eta} \E^{-\frac{t_n\,u^2}{2}}\,du$ is asymptotic to $\frac{\E^{-\frac{t_n\,x^2}{2}}}{t_n\,x}$. On the other hand, since $\psi_n \to_{\mathrm{L}^1} \psi$, for the remaining part of the integral,
$$\int_{x+\eta}^\infty \E^{-\frac{t_n u^2}{2}}\,\psi_n(u)\,du  \leq \E^{-\frac{t_n (x+\eta)^2}{2}}\left(\int_{x+\eta}^\infty \,\psi_n(u)\,du\right) \simeq \E^{-\frac{t_n (x+\eta)^2}{2}}\left(\int_{x+\eta}^\infty \,\psi(u)\,du\right) $$
which is much smaller than the previous quantities. Therefore, assuming that one can replace $\frac{Y_n}{t_n}$ by $W_n$, we obtain the asymptotics
$$\proba[X_n \geq t_n x] = \frac{\E^{-\frac{t_n\,x^2}{2}}}{\sqrt{2\pi t_n} \,x}\,\psi(x)\,(1+o(1))$$
for all $x>0$; this is what we wanted to prove. Finally, the replacement $\frac{Y_n}{t_n}\leftrightarrow W_n$ is indeed valid, because
\begin{align*}
\int_x^\infty \E^{-\frac{t_n\,u^2}{2}}\,\proba_{W_n}[du] &= \left[\E^{-\frac{t_n\,u^2}{2}}\,\proba[W_n \leq u]\right]_x^\infty +\int_x^\infty t_n u\,\E^{-\frac{t_n\,u^2}{2}}\,\proba[W_n \leq u]\,du \\
&\simeq \left[\E^{-\frac{t_n\,u^2}{2}}\,\proba[Y_n/t_n \leq u]\right]_x^\infty + \int_x^\infty t_n u\,\E^{-\frac{t_n\,u^2}{2}}\,\proba[Y_n/t_n \leq u]\,du\\
&\simeq \int_x^\infty \E^{-\frac{t_n\,u^2}{2}}\,\proba_{\frac{Y_n}{t_n}}[du] 
\end{align*}
by using on the second line the fact that both $\frac{Y_n}{t_n}$ and $W_n$ converge in law to the same limit, and therefore have equivalent cumulative distribution function on $\R_+$.
\end{proof}
\bigskip

In the same setting of $\mathrm{L}^1$-mod-Gaussian convergence, one has similarly the estimates on the negative part of the real line, and around $0$, as described on page \pageref{eq:upbound} in the setting of complex mod-Gaussian convergence.\medskip
