---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-022-52-precise-deviations-for-random-variables-with
section_title: "Precise deviations for random variables with control on cumulants"
section_number: 5.2
pages: 39-43
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.928
latex_coverage_ratio: 0.965
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\label{subsec:deviationscumulant}
We use the same hypotheses as in the previous subsection, and without loss of generality, we suppose that $v=3$. Then, the sequence of random variables
$$X_n=\frac{S_{n}}{\betan\,(\alphan)^{1/3}}$$ 
conver\-ges mod-Gaussian with parameters $(\alphan)^{1/3}\,\sigma^{2}$ and limiting function $\psi(z)=\exp(Lz^{3}/6)$ (here, we may have $L=0$). So, one can apply the previous theorems to estimate the tail of the distribution of $S_n$.
In particular, $X_n/\sqrt{t_n} = S_n/(\betan \sigma \sqrt{\alphan})$ satisfies a central limit theorem
with a normality zone of size $o(\sqrt{t_n}) = o \big( \alphan^{1/6} \big)$ (as for the sum of $\alpha_n$ i.i.d. variables)
and one can describe the deviation probabilties at the edge of the normality zone 
--- see Proposition \ref{prop:normalityzone}.















We shall see now that, with stronger assumptions on the speed of convergence than Equation \eqref{eq:cv_sndthrd_cumulants},
we can extend these results to a larger scale.
More precisely, we will assume:
\begin{align}\kappa^{(2)}(S_{n})&= \sigma^{2}\,\alphan\,(\betan)^{2}\,(1+O((\alphan)^{-1/2})); \nonumber\\ 
\kappa^{(3)}(S_{n}) &= L \,\alphan\,(\betan)^{3}\,(1+O((\alphan)^{-1/4})).\label{eq:limitcumulant}
\end{align}
We then have the following result:
\begin{proposition}\label{prop:largedeviationscumulants}
Let $(S_{n})_{n \in \N}$ be a sequence of centered real-valued random variables.
Assume that the bound on cumulants \eqref{eq:superbound} and the asymptotics of second and third cumulants given by Equation \eqref{eq:limitcumulant} hold.
If $x_n$ is a positive sequence, bounded away from $0$ with $x_n=o\big(\alphan^{1/12} \big)$, then



\begin{align*}
    \proba\!\left[S_{n} \geq \betan \sigma^2 \alphan^{2/3} x_n \right]=
\proba[X_n \ge t_n x_n] =
\frac{\E^{-\frac{(x_n)^2(\alphan)^{1/3}\sigma^2}{2}}}{x_n(\alphan)^{1/6}\sigma \sqrt{2\pi}}\,\E^{\frac{L(x_n)^3}{6}}\,(1+o(1)).\\
    \proba\!\left[S_{n} \geq \betan \sigma^2 \alphan^{2/3} x_n \right]=
\proba[X_n \le - t_n x_n] =
\frac{\E^{-\frac{(x_n)^2(\alphan)^{1/3}\sigma^2}{2}}}{x_n(\alphan)^{1/6}\sigma \sqrt{2\pi}}\,\E^{\frac{-L(x_n)^3}{6}}\,(1+o(1)).
\end{align*}
\end{proposition}

\begin{remark}
The case where $x_n$ is a constant sequence equal to $x$ corresponds to Equations \eqref{eq:PosDev} and \eqref{eq:NegDev}, 
which gives an equivalent for the deviation probability at the edge of the normality zone.
Hence, the proposition asserts that, with appropriate assumptions on cumulants,
this result is valid at a larger scale.
Namely, we give an equivalent for the deviation probability of $X_n$ of order up to $o\big( t_n^{5/4}\big)$,
instead of the usual $O(t_n)$.
\end{remark}

\begin{proof}
Set $X_{n}=(\alphan)^{-1/3}\,S_{n}$; up to a renormalization of the random variables, one can suppose $\beta_n=1$, and also $\sigma^{2}=1$. Let $z_n$ be a sequence of complex numbers with $|z_{n}|=O((\alphan)^{1/12})$; we set $\eta_n = |z_n| \,(\alphan)^{-1/12}$. Then, following the computation of Section \ref{subsec:modgaussfromcumulants} with $v=3$, we get:
\begin{align*}
\log \varphi_{X_n}(z_n)&=\frac{\kappa^{(2)}(S_{n})}{2\,(\alphan)^{\frac{2}{3}}}\,(z_n)^{2}+\frac{\kappa^{(3)}(S_{n})}{6\,\alphan }\,(z_n)^{3}+\sum_{r=4}^{\infty} \frac{\kappa^{(r)}(S_{n})}{r!\,(\alphan)^{\frac{r}{3}}}\,(z_n)^{r}\\
&=\frac{1}{2}\,(\alphan)^{\frac{1}{3}}\,(z_n)^{2}+\frac{L}{6}\,(z_n)^{3}+ O((\eta_n)^2 + (\eta_n)^3+(\eta_n)^4).
\end{align*}
If $|z_{n}|=o((\alphan)^{1/12})$, then $\eta_n \to 0$, so the remainder above is $o(1)$ and we have:
\begin{equation}
\varphi_{X_{n}}(z_{n})=\exp\left((\alphan)^{\frac{1}{3}}\frac{(z_{n})^{2}}{2}+\frac{L(z_{n})^{3}}{6}\right)\big(1+o(1)\big).
\label{EqPhiXn}
\end{equation}
We make the change of probability measure 
$$\proba[Y_{n} \in dy]=\frac{\E^{x_ny}}{\varphi_{X_{n}}(x_n)}\,\proba[X_{n} \in dy]$$ 
with $x_n=o((\alphan)^{1/12})$; the generating function of $Y_{n}$ is $\varphi_{Y_{n}}(z)= \frac{\varphi_{X_{n}}(x_n+z)}{\varphi_{X_{n}}(x_n)}$. So, using the inequality
$$|(z+x_n)^r - (x_n)^r| \leq 2^r\,|z|\,\max(|z|,|x_n|)^{r-1},$$
we get, setting $\eta_n^z = |z|\,(\alphan)^{-1/12}$ and $\eta_n^{x,z} = \max(|x_n|,|z|)\,(\alphan)^{-1/12}$,
\begin{align}
\log \varphi_{Y_{n}}(z)&=(\alphan)^{1/3}\frac{(z+x_{n})^{2}-(x_n)^2}{2}+\frac{L((z+x_{n})^{3}-(x_n)^3)}{6}\nonumber\\
&\quad+O(\eta_{n}^z(\eta_n^{x,z} + (\eta_n^{x,z})^2+(\eta_n^{x,z})^3))\nonumber\\
&=\left((\alphan)^{1/3}\,x_{n} +\frac{L\,(x_{n})^{2}}{2}\right)z+\left(\frac{(\alphan)^{1/3}+L\,x_{n}}{2}\right)z^{2}+\frac{L}{6}\,z^{3}\nonumber\\
&\quad+O(\eta_{n}^z(\eta_n^{x,z} + (\eta_n^{x,z})^2+(\eta_n^{x,z})^3))\label{eq:push}
\end{align}
Thus, if 
$$Z_{n}=Y_{n}-(\alphan)^{1/3}\,x_{n} -\frac{L\,(x_{n})^{2}}{2},$$
then the sequence $(Z_{n})_{n \in \N}$ converges in the mod-Gaussian sense, with parameters $t_n=(\alphan)^{1/3}+L\,x_{n}$ and limiting function $\exp(\frac{L\,z^{3}}{6})$. Moreover, in Equation \eqref{eq:push}, the approximation is valid for any $z$ such that $|z|\leq \Delta(\alphan)^{1/12}$, for some constant $\Delta$ depending only on the constant $C$ in the bound \eqref{eq:superbound}.\bigskip

Besides, for $x_n=o((\alphan)^{1/12})$, one has
\begin{align*}
\proba&\!\left[S_{n} \geq x_{n}\,(\alphan)^{\frac{2}{3}}\right]=\proba\!\left[X_{n} \geq x_n\,(\alphan)^{\frac{1}{3}}\right]=\varphi_{X_{n}}(x_n)\int_{y=x_n\,(\alphan)^{1/3}}^{\infty}\E^{-x_ny}\,\,\proba[Y_{n} \in dy]\\
&=\varphi_{X_{n}}(x_n)\,\E^{-\left((\alphan)^{1/3}\,(x_{n})^{2}+\frac{L\,(x_{n})^{3}}{2}\right)}\!\!\int_{z=-\frac{L\,(x_{n})^{2}}{2}}^{\infty} \E^{-x_n z}\, \,\proba[Z_{n} \in dz]\\
&=\exp\left(-\frac{(\alphan)^{1/3}\,(x_n)^{2}}{2}-\frac{L(x_n)^3}{3}\right)\,R_{n}\,(1+o(1)),
\end{align*}
by replacing $\varphi_{X_n}(x_n)$ by its estimate \eqref{EqPhiXn}, which holds since $x_n=o((\alphan)^{1/12})$; $R_n$ is the integral of the second line.\bigskip

To estimate the integral $R_n$, we shall adapt the proof of Proposition \ref{prop:berryesseen} to the special case of a sequence $(Z_n)_{n \in \N}$ that converges in the mod-Gaussian sense, with parameters $t_n$, limit function $\exp(Kz^3)$, and with the approximation
\begin{equation}
\log \varphi_{Z_n}(z) = \frac{t_n\,z^2}{2} + K\,z^3 + O\!\left(\frac{z}{(t_n)^{1/4}}\right)
\label{EqLogPhi}
\end{equation}
that is valid for every $|z| \leq \Delta (t_n)^{1/4}$ with $\Delta>0$. Notice that the sequence $(Z_n)_{n \in \N}$ previously constructed satisfies these hypotheses with $t_n = (\alphan)^{1/3} + Lx_n \simeq (\alphan)^{1/3}$. If one applies Proposition \ref{prop:berryesseen} to the case of mod-Gaussian convergence with a limit $\exp(Kz^3)$, then $\eta'''(0)=\psi'(0)=0$, so the approximation of the law $dF_n(w)$ of $Z_n/\sqrt{t_n}$ is simply the Gaussian law $dG(w) = (2\pi)^{-1/2}\,\E^{-w^2/2}\,dw$, and the Kolmogorov distance between $F_n$ and $G$ is a $o((t_n)^{-1/2})$. However, by using the validity of the approximation \eqref{EqLogPhi} on a larger scale than $z=O(1)$, it is possible to obtain a better Berry-Esseen bound, namely, $O((t_n)^{-3/4})$.\bigskip

Recall that for any $T>0$ and any $w \in \R$, the distance between cumulative distribution functions is smaller than
$$|F_n(w)-G(w)|\leq \frac{1}{\pi} \int_{-T}^{T} \left|\frac{f_n^{*}(\zeta)-g^{*}(\zeta)}{\zeta}\right|\, d\zeta +\frac{24m}{\pi T}.$$
However, for any $\zeta=O((t_n)^{3/4})$, one has
\begin{align*}
\left|\frac{f_n^{*}(\zeta)-g^{*}(\zeta)}{\zeta}\right| &= \E^{-\frac{\zeta^2}{2}} \,\left|\frac{\exp\left(\frac{K\,\zeta^3}{(t_n)^{3/2}} + O\!\left(\frac{\zeta}{(t_n)^{3/4}}\right)\right)-1}{\zeta}\right| \\
\E^{\frac{\zeta^2}{2}}\left|\frac{f_n^{*}(\zeta)-g^{*}(\zeta)}{\zeta}\right| &\leq \left|\E^{\frac{K\,\zeta^3}{(t_n)^{3/2}}}\right|\,\left|\frac{\exp\left(O\!\left(\frac{\zeta}{(t_n)^{3/4}}\right)\right)-1}{\zeta}\right| + \left|\frac{\exp\left(\frac{K\,\zeta^3}{(t_n)^{3/2}}\right)-1}{\zeta}\right|  \\
&\leq \E^{\frac{K\,|\zeta|^3}{(t_n)^{3/2}}} \,O\!\left(\frac{1}{(t_n)^{3/4}} + \frac{\zeta^2}{(t_n)^{3/2}}\right).
\end{align*}
In these inequalities, the constant hidden in the big $O$ can be chosen uniform if $\frac{\zeta}{(t_{n})^{3/4}}$ stays in a bounded, sufficiently small interval $[-\Delta,\Delta]$. As a consequence, setting $T=\Delta\,(t_n)^{3/4}$, one obtains from Feller's lemma:
$$|F_n(w)-G(w)|\leq O\left(\,\int_{-\Delta\,(t_n)^{3/4}}^{\Delta\,(t_n)^{3/4}} \left(\frac{1}{(t_n)^{3/4}} + \frac{\zeta^2}{(t_n)^{3/2}}\right)\, \E^{-\frac{\zeta^2}{2} + \frac{K\,|\zeta|^3}{(t_n)^{3/2}}}\,d\zeta +\frac{1}{\Delta\,(t_n)^{3/4}}\right)$$
uniformly in $w$.
Since $|\zeta|$ stays smaller than $\Delta\,(t_n)^{3/4}$, in this integral,
$$-\frac{\zeta^2}{2} + \frac{K\,|\zeta|^3}{(t_n)^{3/2}} \leq -\frac{\zeta^2}{2}\left(1-\frac{K\,\Delta}{(t_n)^{3/4}}\right) \leq -\frac{\zeta^2}{4}$$
for $t_n$ large enough. As claimed before, it follows that
$$\sup_{w \in \R} |F_n(w)-G(w)| = O\left(\frac{1}{(t_n)^{3/4}}\right).$$
\bigskip

We can now compute the asymptotics of the integral $R_n$. Set
$$\eps_n = -\frac{L(x_n)^2}{2\sqrt{(\alphan)^{1/3}+Lx_n}} = -\frac{L(x_n)^2}{2\sqrt{t_n}};$$
since $x_n = o((\alphan)^{1/12})$, $\eps_n \to 0$. Now,
\begin{align*}
R_n&=\int_{w=\eps_n}^\infty \exp\left(-w\,x_n\sqrt{t_n} \right)\,dF_n(w)\\
&=x_n\sqrt{t_n} \int_{\eps_n}^{\infty}\exp\left(-w\,x_n\sqrt{t_n} \right)\,(F_n(w)-F_n(\eps_n))\,dw \\
&=x_n\sqrt{t_n} \int_{\eps_n}^{\infty}\exp\left(-w\,x_n\sqrt{t_n} \right)\left(G_n(w)-G_n(\eps_n) + O\!\left(\frac{1}{(t_n)^{3/4}}\right)\right)\,dw \\
&=\frac{1}{\sqrt{2\pi}}\,\int_{\eps_n}^{\infty} \exp\left(-w\,x_n\sqrt{t_n}-\frac{w^2}{2} \right)\,dw + O\!\left(\frac{\E^{\frac{L\,(x_n)^3}{2}}}{(t_n)^{3/4}}\right).
\end{align*}
The last Gaussian integral is given by Lemma \ref{lem:gaussintegral}, \eqref{item:gausstail}:

\begin{align*}
\int_{\eps_n}^{\infty} \exp\left(-w\,x_n\sqrt{t_n}-\frac{w^2}{2} \right)\,dw &= \E^{\frac{t_n(x_n)^2}{2}}\int_{0}^{\infty} \exp\left(-\frac{(y+\eps_n+x_n\sqrt{t_n})^2}{2} \right)\,dy\\
&= \frac{\E^{\frac{L(x_n)^3}{2}}}{\eps_n+x_n\sqrt{t_n}}\, (1+o(1)) = \frac{\E^{\frac{L(x_n)^3}{2}}}{x_n\sqrt{t_n}} \,(1+o(1))
\end{align*}
since $\eps_n \to 0$. Since $x_n=o((\alphan)^{1/12}) = o((t_n)^{1/4})$, $\frac{1}{x_n\sqrt{t_n}}$ becomes much larger than $O(\frac{1}{(t_n)^{3/4}})$ as $t_n$ goes to infinity, so finally:
$$R_n = \frac{1}{\sqrt{2\pi}}\,\frac{\E^{\frac{L(x_n)^3}{2}}}{x_n(\alphan)^{1/6}} \,(1+o(1))$$
as $t_n\simeq (\alphan)^{1/3}$. Gathering everything, we get
$$\proba\!\left[S_{n} \geq x_{n}\,(\alphan)^{\frac{2}{3}}\right] = \frac{\E^{-\frac{(x_n)^2(\alphan)^{1/3}}{2}}}{x_n(\alphan)^{1/6}\sqrt{2\pi}}\,\E^{\frac{L(x_n)^3}{6}}\,(1+o(1)),$$
and this ends the proof if $\beta_n=\sigma^2=1$ (set $T=x_n\,(\alphan)^{2/3}$ in the statement of the Proposition). In the general case, it suffices to replace $S_n$ by $\frac{S_{n}}{\sigma\beta_n}$, which changes $L$ into $\frac{L}{\sigma^3}$ in the previous computations.
\end{proof}
\medskip

\begin{remark}
The argument which allows one to get a better Berry-Esseen estimate than in Proposition \ref{prop:berryesseen} can be used in a very general setting of mod-stable convergence, in order to get optimal bounds on the Kolmogorov distance. This will be the main topic of the forthcoming paper \cite{FMN14}.
\end{remark}
\bigskip
