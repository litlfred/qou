---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-013-41-speed-of-convergence
section_title: "Speed of convergence"
section_number: 4.1
pages: 24-30
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.956
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
\label{subsec:speedofconv}
Getting back to our special case of the Curie-Weiss model, we denote $X_n=\frac{1}{n^{1/4}}\sum_{i=1}^n B_i$ a scaled sum of $\pm 1$ independent Bernoulli random variables; $Y_n$ the random variable with modified law 
$$\qproba_n[dy]=\frac{\E^{\frac{y^2}{2n^{1/2}}}\,\proba_n[dy]}{\esper\!\left[\E^{\frac{(X_n)^2}{2n^{1/2}}}\right]};$$
$G_n$ an independent Gaussian random variable of variance $\frac{1}{n^{1/2}}$; and $W_n=\frac{Y_n}{n^{1/2}} + G_n$. It follows from the previous results that the law of $W_n$ has density
$$\frac{\psi_n(x)}{I_n}=\frac{1}{I_n}\,\E^{-\frac{n^{1/2}x^2}{2}}\,\left( \cosh \frac{x}{n^{1/4}}\right)^n,$$
which converges in $\leb^1$ towards the law $\frac{\psi(x)}{I_\infty}=\frac{1}{I_\infty}\,\E^{-\frac{x^4}{12}}$. We hence wish for an upper bound for the Kolmogorov distance between $\frac{Y_n}{n^{1/2}}$ and $W_\infty$. For this we shall need the following general lemmas.
\bigskip

\begin{lemma}\label{lem:kolmogorov}
Consider the two distributions $W_n = \frac{\psi_n(x)\,dx}{I_n}$ and $W_\infty = \frac{\psi(x)\,dx}{I_\infty}$. The Kolmogorov distance between them is smaller than
$$\frac{\|\psi-\psi_n\|_{\mathrm{L}^1}}{I_\infty}\,(1+o(1)).$$
\end{lemma}

\begin{proof}
Fix  $a \in \R$, and suppose for instance that $\int_\R \psi(x)\,dx \geq \int_{\R} \psi_n(x)\,dx$. We have
\begin{align*}
F_{W_n}(a)-F_{W_{\infty}}(a) &= \left(\frac{\int_{-\infty}^a \psi_n(x)\,dx }{I_n}-\frac{\int_{-\infty}^a \psi(x)\,dx }{I_n}\right) \!+\! \left(\frac{\int_{-\infty}^a \psi(x)\,dx }{I_n}-\frac{\int_{-\infty}^a \psi(x)\,dx }{I_\infty}\right) \\
&= \frac{\int_{-\infty}^a (\psi_n(x)-\psi(x))\,dx}{I_n} + \left(\int_{-\infty}^a \psi(x)\,dx\right) \frac{\int_{-\infty}^\infty (\psi(x)-\psi_n(x))\,dx}{I_\infty I_n}\\
&\leq -\frac{\int_{-\infty}^a (\psi(x)-\psi_n(x))\,dx}{I_n}+\frac{\int_{-\infty}^\infty (\psi(x)-\psi_n(x))\,dx}{I_n}\\
&\leq \frac{\int_{a}^\infty (\psi(x)-\psi_n(x))\,dx}{I_n} \leq \frac{\|\psi-\psi_n\|_{\mathrm{L}^1}}{I_n}.
\end{align*}
Writing $F_{W_{\infty}}(a)-F_{W_n}(a) = (1-F_{W_n}(a)) - (1-F_{W_\infty}(a))$, one sees that the inequality is in fact valid with an absolute value on the left-hand side. Since $I_n=I_{\infty} (1+o(1))$, this shows the claim. If $\int_{\R} \psi_n(x)\,dx \geq \int_{\R} \psi(x)\,dx$, it suffices to exchange the roles played by $\psi_n$ and $\psi$ to get the inequality.
\end{proof}\bigskip


The asymptotics of the $\leb^1$-norm $\|\psi-\psi_n\|_{\leb^1}$ in the Curie-Weiss model are computed as follows. Noting that one always has $\psi_n(x) \geq \psi(x)$, it suffices to compute
$$\int_{\R} \psi_n(x)\,dx = \int_{\R} \E^{-\frac{n^{1/2}\,x^2}{2}}\,\left(\cosh(x\,n^{-1/4})\right)^{n}\,dx=n^{1/4}  \int_{\R} \left(\E^{-\frac{u^2}{2}}\,\cosh(u)\right)^{n}\,du.$$
By the Laplace method (see \cite[Formula (19.17), p. 624-625]{Zor04}), the asymptotics of the integral is
$$n^{-\frac{1}{4}}\left(\frac{{12}^{1/4}\,\Gamma(\frac{1}{4})}{2}\right)+n^{-\frac{3}{4}}\left(\frac{12^{3/4}\,\Gamma(\frac{3}{4})}{10}\right)+\text{smaller terms}.$$
The first term corresponds to $I_\infty=\int_{\R} \psi(x)\,dx = \int_{\R}\E^{-x^4/12}\,dx$. As a consequence, 
$$\frac{\|\psi-\psi_n\|_{\mathrm{L}^1}}{I_\infty}=\frac{1}{n^{1/2}}\,\frac{\sqrt{12}\,\Gamma(\frac{3}{4})}{5\,\Gamma(\frac{1}{4})}\,(1+o(1)) .$$
\bigskip

The main work now consists in computing $d_{\mathrm{Kol}}(\frac{Y_n}{n^{1/2}},W_n)$. We start by a Lemma which is a variation of arguments used for i.i.d. random variables in \cite[p. 87]{Tao12}. In the following, given a function $f \in \mathrm{L}^1(\R)$, we write its Fourier transform $\widehat{f}(\xi)=\int_{\R}f(x)\,\E^{\I \xi x}\,dx$. Recall that the function
$$\upsilon(\xi)=\begin{cases}\E^{-\frac{1}{1-4\xi^2}} &\text{if }|\xi|<\frac{1}{2},\\
0&\text{otherwise}.
\end{cases}$$
is even, of class $\mathcal{C}^\infty$ and with compact support $[-\frac{1}{2},\frac{1}{2}]$. We set $\widehat{\rho_\star}=\upsilon$, so that $$\rho_\star(x)=\frac{1}{2\pi}\int_{-\frac{1}{2}}^{\frac{1}{2}} \upsilon(\xi)\,\E^{-\I x \xi}\, d\xi$$
by the Fourier inversion theorem. By construction, the Fourier transform of $\rho_\star$ has support equal to $[-\frac{1}{2},\frac{1}{2}]$. Set now 
$$\rho(x)=\frac{(\rho_\star(x))^2}{\int_{\R} (\rho_*(y))^2\,dy}.$$ 
By construction, $\rho$ is smooth, even, non-negative and with integral equal to $1$. Moreover, $\widehat{\rho}$ is up to a constant equal to $\nu*\nu(\xi)$, so it has support included into $[-1,1]$. The convolution of $\rho$ with characteristic functions of intervals will allow us to transform estimates on test functions into estimates on cumulative distribution functions. More precisely, for $a \in \R$ and $\eps >0$, set
$\rho_\eps(x)=\frac{1}{\eps}\,\rho(\frac{x}{\eps})$, and $\phi_{a,\eps}(x)=\phi_\eps(x-a)$, where $\phi_\eps$ is the function $1_{(-\infty,0]}*\rho_\eps$. One sees $\phi_{a,\eps}$ as a smooth approximation of the characteristic function $1_{(-\infty,a]}$.\bigskip

For all $a,\eps$, $\phi_{a,\eps}$ has Fourier transform compactly supported on $\left[-\frac{1}{\eps},\frac{1}{\eps}\right]$. Moreover, it has negative derivative, and decreases from $1$ to $0$. Later, we will use the identity
$$\phi_\eps(\eps x)=\phi_1(x)=\phi(x).$$
On the other hand, we have the following estimates for $K>0$ (we used \textsc{Sage} for numerical computations):
\begin{align*}
 |\rho_*(K)| &= \frac{1}{2\pi K^2}\left|\int_{-\frac{1}{2}}^{\frac{1}{2}} \upsilon''(\xi)\,\E^{-\I K \xi}\, d\xi\right| \leq \frac{1}{2\pi K^2} \int_{0}^{\frac{1}{2}} |\upsilon''(\xi)|\,d\xi = \frac{1.0166_-}{K^2};\\
\int_{\R} (\rho_*(y))^2\,dy&=\frac{1}{2\pi} \int_0^{\frac{1}{2}} |\upsilon(\xi)|^2\,d\xi = 0.01059_+.\end{align*}
Therefore, for any $K>0$,
\begin{align*}
\rho(K) &= \rho(-K)=\frac{(\rho_*(K))^2}{\int_{\R} (\rho_*(y))^2\,dy} \leq \frac{99}{K^4};\\
\phi(K)&=1-\phi(-K)=\int_{0}^\infty \rho(K+y)\,dy \leq \frac{33}{K^3}.
\end{align*}
\medskip

\begin{lemma}\label{lem:tao}
Let $V$ and $W$ be two random variables with cumulative distribution functions $F_V$ and $F_W$. Assume that for some $\eps>0$
$$|\esper[\phi_{a,\eps}(V)]-\esper[\phi_{a,\eps}(W)] | \leq B\eps,$$
where the positive constant $B$ is independent of $a$. We also suppose that $W$ has a density w.r.t. Lebesgue measure that is bounded by $m$. Then, 
$$\sup_{a \in \R} |F_V(a)-F_W(a)| \leq 2(B+10m)\,\eps.$$ 
\end{lemma}

\begin{proof}
Fix a positive constant $K$, and denote $\delta=\sup_{a \in \R}|F_V(a)-F_W(a)|$ the Kolmo\-go\-rov distance between $V$ and $W$. One has
\begin{align*}F_V(a) = \esper[1_{V \leq a}] &\leq \esper[\phi_{a+K\eps,\eps}(V)] + \esper[(1-\phi_{a+K\eps,\eps}(V))\,1_{V \leq a}]\\
&\leq \esper[\phi_{a+K\eps,\eps}(W)] + \esper[(1-\phi_{a+K\eps,\eps}(V))\,1_{V \leq a}] + B\eps.
\end{align*}
The second expectation writes as
\begin{align*}
\esper[(1-&\phi_{a+K\eps,\eps}(V))\,1_{V \leq a}]=\int_{\R} (1-\phi_{a+K\eps,\eps}(x))\,1_{(-\infty,a]}(x)\, f_V(x)\,dx\\
&=-\int_{\R} ((1-\phi_{a+K\eps,\eps}(x))\,1_{(-\infty,a]}(x))'\, F_V(x)\,dx\\
&=\int_{\R} \phi_{a+K\eps,\eps}'(x)\,1_{(-\infty,a]}(x)\, F_V(x)\,dx+\int_{\R} (1-\phi_{a+K\eps,\eps}(x))\,1_a(x)\, F_V(x)\,dx.
\end{align*}
For the first integral, since $F_V(x)\geq F_W(x)-\delta$ and the derivative of $\phi_{a+K\eps,\eps}$ is negative, an upper bound on $I_1$ is
\begin{align*}& \int_{\R} \phi_{a+K\eps,\eps}'(x)\,1_{(-\infty,a]}(x)\, F_W(x)\,dx - \delta\int_{\R}\phi_{a+K\eps,\eps}'(x)\,1_{V \leq a}(x) \\
&= \int_{\R} \phi_{a+K\eps,\eps}'(x)\,1_{(-\infty,a]}(x)\, F_W(x)\,dx +  (1-\phi_{a+K\eps,\eps}(a))\,\delta\\
&=\int_{\R} \phi_{a+K\eps,\eps}'(x)\,1_{(-\infty,a]}(x)\, F_W(x)\,dx + (1-\phi(-K))\,\delta.
\end{align*}
As for the second integral, it is simply $(1-\phi_{a+K_\eps,\eps}(a)) F_V(a)$, and by writing $F_V(a) \leq F_W(a)+\delta$, one gets the upper bound on $I_2$
\begin{align*}
&\int_{\R} (1-\phi_{a+K\eps,\eps}(x))\,1_a(x)\, F_W(x)\,dx + (1-\phi_{a+K\eps,\eps}(a))\,\delta \\
&=\int_{\R} (1-\phi_{a+K\eps,\eps}(x))\,1_a(x)\, F_W(x)\,dx + (1-\phi(-K))\,\delta .
\end{align*}
One concludes that 
$$\esper[(1-\phi_{a+K\eps,\eps}(V))\,1_{V \leq a}]\leq \esper[(1-\phi_{a+K\eps,\eps}(W))\,1_{W \leq a}]+2 (1-\phi(-K))\delta.$$
On the other hand, if $m$ is a bound on the density $f_W$ of $W$, then
\begin{align*}\esper[\phi_{a+K\eps,\eps}(W)\,1_{W \geq a}] &= \int_a^{\infty} \phi_{a+K\eps,\eps}(y)\,f_W(y)\,dy\\
&\leq m\int_{a}^\infty \phi_{\eps}(y-a-K\eps)\,dy = m\int_0^\infty \phi_\eps(y-K\eps)\,dy\\
&\leq m\eps \int_0^\infty \phi(u-K)\,du \leq m \eps \left(K+4.82\right),
\end{align*}
by using on the last line the bound $\phi(x) \leq \frac{33}{x^3}$. As a consequence,
\begin{align*}
\esper[\phi_{a+K\eps,\eps}(W)] &\leq \esper[\phi_{a+K\eps,\eps}(W)\,1_{W \leq a}] + m\left(K+4.82\right)\eps\\
F_V(a)&\leq F_W(a) + \left(B+m\left(K+4.82\right)\right) \eps + 2\,\frac{33}{K^3}\,\delta.
\end{align*}
Similarly, $F_V(a)\geq F_W(a) - (B+m(K+4.82)) \eps - 2\,\frac{33}{K^3}\,\delta$, so in the end
$$\delta = \sup_{a \in \R}|F_V(a)-F_W(a)| \leq \left(B+m\left(K+4.82\right)\right)\eps + \frac{66}{K^3}\,\delta.$$\bigskip
As this is true for every $K$, one can for instance take $K=\sqrt[3]{132}$, which gives 
$$\delta \leq \frac{1}{1-\frac{1}{2}}\left(B+m\left(\sqrt[3]{132}+4.82\right)\right)\eps \leq  2(B + 10m)\,\eps.$$
\end{proof}
\bigskip

We are going to apply Lemma \ref{lem:tao} with $V=\frac{Y_n}{n^{1/2}}$ and $W=W_n$. First, notice that a bound on the density of $W_n$ is
$$\frac{|\psi_n(x)|}{I_n}\leq \frac{1}{I_\infty}=\frac{2}{12^{1/4}\,\Gamma(\frac{1}{4})}=m.$$
On the other hand, using the Fourier transform of the Heaviside function
$$
\widehat{1}_{(-\infty,a]}(\xi)=\E^{\I a \xi}\,\left(\pi\delta_0(\xi)+\frac{\I}{\xi}\right),
$$
we get
\begin{align*}
\esper\left[\phi_{a,\eps}\!\left(\frac{Y_n}{n^{1/2}}\right)\right]-\esper[\phi_{a,\eps}(W_n)] &= \frac{1}{2\pi I_n} \int_{-\frac{1}{\eps}}^{\frac{1}{\eps}} \widehat{\phi_{a,\eps}}(\xi)\,\widehat{\psi_n}(\xi) \left(\E^{\frac{\xi^2}{2n^{1/2}}}-1\right)\,d\xi\\
&=\frac{1}{2\pi I_n} \int_{-\frac{1}{\eps}}^{\frac{1}{\eps}} \widehat{\rho_{\eps}}(\xi)\,\E^{\I a\xi}\,\left(\frac{\I}{\xi}\right)\,\widehat{\psi_n}(\xi) \left(\E^{\frac{\xi^2}{2n^{1/2}}}-1\right)\,d\xi ;\\
\left| \esper\!\left[\phi_{a,\eps}\!\left(\frac{Y_n}{n^{1/2}}\right)\right]-\esper[\phi_{a,\eps}(W_n)]\right| &\leq \frac{1}{2\pi I_n\,n^{1/2}} \int_{-\frac{1}{\eps}}^{\frac{1}{\eps}} |\widehat{\rho}(\eps\xi)|\, |\widehat{\psi_n}(\xi)|\,\E^{\frac{\xi^2}{2n^{1/2}}}\,d\xi
\end{align*}
by controlling $\E^{\frac{\xi^2}{2n^{1/2}}}-1$ by its first derivative (notice that we used the vanishing of this quantity at $\xi=0$ in order to compensate the singularity of the Fourier transform of the Heavyside distribution). Since $\|\widehat{\rho}\|_{\mathrm{L}^\infty}=\|\rho\|_{\mathrm{L}^1}=1$, the previous bound can be rewritten as
$$
\left| \esper\!\left[\phi_{a,\eps}\!\left(\frac{Y_n}{n^{1/2}}\right)\right]-\esper[\phi_{a,\eps}(W_n)]\right| \leq \frac{1}{2\pi I_n\,n^{1/2}} \int_{-\frac{1}{\eps}}^{\frac{1}{\eps}} |\widehat{\psi_n}(\xi)|\,\E^{\frac{\xi^2}{2n^{1/2}}}\,d\xi.
$$\bigskip

We then need estimates on the Fourier transform of $\widehat{\psi_n}$, and more precisely estimates of exponential decay. To this purpose, we use the following Lemma, which is related to \cite[Theorem IX.13, p. 18]{RS75}:

\begin{lemma}
Let $f$ be a function which is analytic on a band $\{z \in \CC\,\,|\,\,|\mathrm{Im}(z)|<c\}.$ 
For any $b \in (0,c)$,
$$|\widehat{f}(\xi) |\leq 2\left(\sup_{-b\leq a \leq b} \|f(\cdot + \I a)\|_{\leb^1}\right)\,\E^{-b|\xi|},$$
assuming that the supremum is finite.
\end{lemma}

\begin{proof}
Notice that the Fourier transform of $\tau_af(\cdot) =f(\cdot + \I a)$ is
$$\int_{\R} \tau_a f(x)\,\E^{\I x \xi}\,dx = \int_{\R} f(x+\I a)\,\E^{\I x \xi}\,dx = \left(\int_{\R} f(x+\I a)\,\E^{\I (x-\I a) \xi}\,dx\right)\E^{-a\xi}.$$
By analyticity of the function in the integral, using Cauchy's integral formula, one sees that the last term is also
$$\left(\int_{\R} f(x)\,\E^{\I x \xi}\,dx\right)\E^{a\xi} = \widehat{f}(\xi)\,\E^{-a\xi},$$
(see the details on page 132 of the book by Reed and Simon). It follows that
$$|\widehat{f}(\xi)|\,\E^{a|\xi|} \leq |\widehat{f}(\xi)|\,(\E^{a\xi}+\E^{-a\xi}) \leq |\widehat{\tau_af}(\xi)|+|\widehat{\tau_{-a}f}(\xi)| \leq \|\tau_af\|_{\leb^1}+\|\tau_{-a}f\|_{\leb^1}.$$
\end{proof}
\bigskip

Thus we need to compute for $a>0$ the $\leb^1$-norm of $\psi_n(\cdot+\I a)$. We write
\begin{align*}
|\psi_n(x+\I a)| &= \E^{-\frac{n^{1/2}(x^2-a^2)}{2}}\,\left|\cosh\left(\frac{x+\I a}{n^{1/4}}\right)\right|^n\\
&=|\psi_n(x)|\, \E^{\frac{n^{1/2}a^2}{2}}\, \left|\cos^2\left(\frac{a}{n^{1/4}}\right)+ \tanh^2\left(\frac{x}{n^{1/4}}\right) \,\sin^2\left(\frac{a}{n^{1/4}}\right)\right|^{\frac{n}{2}}\\
&=|\psi_n(x)|\, \E^{\frac{n^{1/2}a^2}{2}}\, \left|1-\left(1- \tanh^2\left(\frac{x}{n^{1/4}}\right) \right)\,\sin^2\left(\frac{a}{n^{1/4}}\right)\right|^{\frac{n}{2}}.
\end{align*}
For $n$ large enough, $\sin^2(\frac{a}{n^{1/4}}) \geq \frac{a^2}{n^{1/2}}-\frac{a^4}{3n}$, and on the other hand, $0\leq \tanh^2\left(\frac{x}{n^{1/4}}\right) \leq \frac{x^2}{n^{1/2}}$, so
\begin{align*}
\left|\frac{\psi_n(x+\I a)}{\psi_n(x)}\right| &\leq \E^{\frac{n^{1/2}a^2}{2}} \exp\left(-\frac{n^{1/2}a^2}{2}\left(1- \tanh^2\left(\frac{x}{n^{1/4}}\right)\right) \left(1-\frac{a^2}{3n^{1/2}}\right)\right)\leq \E^{\frac{a^4}{3}}\,\E^{\frac{a^2x^2}{2}}.
\end{align*}
Since $\psi_n(x)$ behaves as $\E^{-x^4/12}$, the previous Lemma can be applied, with an asymptotic bound
\begin{align*}
\|\psi_n(\cdot + \I a)\|_{\leb^1} &\lesssim \E^{\frac{a^4}{3}}\,\int_{\R} \E^{-\frac{x^4}{12}+\frac{a^2x^2}{2}}\,dx = \E^{\frac{13a^4}{12}} \int_{\R} \E^{-\frac{(x^2-3a^2)^2}{12}}\,dx \\
&\lesssim  \E^{\frac{13a^4}{12}}\left(2\sqrt{3}\,a+I_\infty\right)
\end{align*}
by cutting the integral in two parts according to the sign of $x^2-3a^2$. We have therefore proven:

\begin{proposition}\label{prop:sizefourier}
For any $b \geq 0$, 
$$|\widehat{\psi}_n(\xi)| \lesssim K(b)\,\E^{-b|\xi|},$$
where $K(b) = 2\E^{\frac{13b^4}{12}}(2\sqrt{3}\,b+I_\infty)$ and where the symbol $\lesssim$ means that the inequality is true up to any multiplicative constant $1+\eps$, for $\eps>0$ and $n$ large enough.
\end{proposition}
\bigskip

We can now conclude. Fix $b>0$, and $D<2b$. On the interval $[-Dn^{1/2},Dn^{1/2}]$,  we have
$$\frac{\xi^2}{2n^{1/2}}-b|\xi| = -|\xi|\left(b-\frac{|\xi|}{2n^{1/2}}\right) \leq - |\xi|\left(b-\frac{D}{2}\right).$$
Therefore, with $\eps=\frac{1}{Dn^{1/2}}$,
\begin{align*}\left| \esper\!\left[\phi_{a,\eps}\!\left(\frac{Y_n}{n^{1/2}}\right)\right]-\esper[\phi_{a,\eps}(W_n)]\right| &\lesssim \frac{K(b)}{2\pi I_\infty\,n^{1/2}} \int_{\R} \E^{-\left(b-\frac{D}{2}\right)|\xi|}\,d\xi= \frac{K(b)}{\pi I_\infty\,n^{1/2}\,\left(b-\frac{D}{2}\right)}\\
&\lesssim \frac{K(b)\, D}{\pi I_\infty \,\left(b-\frac{D}{2}\right)}\,\eps.
\end{align*}
So, Lemma \ref{lem:tao} applies to $V=\frac{Y_n}{n^{1/2}}$ and $W=W_n$, with
$$d_{\mathrm{Kol}}\left(\frac{Y_n}{n^{1/2}},W_n\right)\lesssim 2\left(\frac{K(b)\,D}{\pi I_\infty \,\left(b-\frac{D}{2}\right)}+\frac{10}{I_\infty}\right)\,\eps=\frac{2}{I_\infty\,n^{1/2}}\left(\frac{K(b)}{\pi\,(b-\frac{D}{2})}+\frac{10}{D}\right).$$
Taking $b=D=0.77$, we get finally
\begin{align*}
d_{\mathrm{Kol}}\left(\frac{Y_n}{n^{1/2}},W_n\right)\lesssim \frac{2}{I_\infty\,n^{1/2}} \left( \frac{2\,K(b)}{\pi \,b}+\frac{10}{b}\right)\leq \frac{10.27}{n^{1/2}}.
\end{align*}
Adding the bound on $d_{\mathrm{Kol}}(W_n,W_\infty)$ yields then:

\begin{theorem}
For $n$ large enough, $$d_{\mathrm{Kol}}\left(\frac{Y_n}{n^{1/2}},W_\infty\right)\leq 11\,n^{-1/2}.$$
\end{theorem}
Notice that we have only used arguments of Fourier analysis and the language of mod-Gaussian convergence in order to get this bound.
\medskip
