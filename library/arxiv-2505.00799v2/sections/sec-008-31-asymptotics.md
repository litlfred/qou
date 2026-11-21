---
doc_id: arxiv-2505.00799v2
doc_title: "Quantum Modular Forms and Resurgence"
section_id: sec-008-31-asymptotics
section_title: "Asymptotics"
section_number: 3.1
pages: 15-19
source_pdf: 2505.00799v2.pdf
source_sha256: cc9d2ab4c6c79b50
toc_source: outline
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 0.956
doc_brief: "Quantum Modular Forms and Resurgence — In 2010, Zagier described a new phenomenon which he called quantum mod- ularity."
---
[]{#subsec: asymptotics label="subsec: asymptotics"}

Throughout this paper, we will regularly leverage the relationship between the coefficients of an asymptotic expansion of an exponential series and the analytic continuation of an associated Dirichlet series. For a more thorough discussion, we direct the reader to [@zagier-appendix], but for most of our applications, the following result will suffice:

::: prop
Let $L(\rho)$ be a Dirichlet series convergent in some right half-plane $$L(\rho) = \sum_{m=1}^\infty \frac{a_m}{m^\rho}, \quad \quad \Re(\rho) \gg 0.$$ Suppose that the function $\phi(t) = \sum_{m=1}^\infty a_me^{-mt}$ has an asymptotic expansion of the form $$\phi(t) \sim \sum_{n=0}^\infty c_n t^n, \quad \quad (t \to 0).$$ Then $L(\rho)$ has an analytic continuation to all $\rho$, and its values at non-positive integers are given by $$L(-n) = (-1)^n n! c_n.$$ Conversely, if one assumes $L(\rho)$ analytically continues to $\mathbb{C}$, then $\phi(t)$ admits an asymptotic expansion with coefficients given by $$c_n  = (-1)^n \frac{L(-n)}{n!}.$$
:::

Now we compute the Borel transforms of the asymptotic series attached to cusp forms, their Eichler integrals, and periodic functions of Maass forms. In what follows, we assume $\gamma = \begin{psmallmatrix} a & b \\ c & d\end{psmallmatrix} \in \Gamma_0(N)$, and that the asymptotics are taken along geodesics in the upper half-plane.

When $g$ is of *Type 1* or *2*, the above proposition tells us that as $z \to -d/c$ along a geodesic,

$$\tilde{g}(z) \sim \varphi_{-d/c}(z) := \sum_{n=0}^\infty \frac{L(g, -d/c; -n)}{\Gamma(n+1)} (2\pi i)^n (z+d/c)^n.$$ Using the fact that $\Lambda(g, -d/c; \rho)$ is entire and $\Gamma(\rho)$ has poles at non-positive integers, $L(g, -d/c; \rho)$ is forced to have zeros at these locations. Therefore each term equals zero. This is to be expected since $g$ is a cusp form.

When $g$ is of *Type 3*, as $z \to -d/c$, we have $$g(z) \sim \varphi_{-d/c}(z) := \sum_{n=0}^\infty \frac{L(f, -d/c; -n-1+k)}{\Gamma(n+1)} (2\pi i)^n (z+d/c)^n,$$ where $f$ is the cusp form associated to $g$. When $-n-1+k$ is a non-positive integer, we again have that $L(f, -d/c; -n-1+k)=0$. Then only the first $k-2$ terms are nonzero. Using the functional equation of $L(f, -d/c; \rho)$, this equals $$\sum_{n=0}^{k-2} i^{-k} \left(\frac{c}{2\pi}\right)^{2n+2-k} \frac{L(f, a/c; n+1)}{\Gamma(-n-1+k)} (2\pi i)^n (z+d/c)^n.$$

We now consider when $g$ is of *Type 4*. Again we have that as $z \to -d/c$,

$$g(z) \sim \varphi_{-d/c}(z) := \sum_{n=0}^\infty \frac{L(f, -d/c; -n-1+k)}{\Gamma(n+1)} (2\pi i)^n (z+d/c)^n,$$ where $f$ is the cusp form associated to $g$. By the functional equation of $L(f, -d/c;\rho)$, we have that this equals $$\sum_{n=0}^\infty i^{-k} \varepsilon_d^{2k} \left( \frac{c}{d}\right) \left(\frac{c}{2\pi}\right)^{2n+2-k} \frac{L(f, a/c; n+1)}{\Gamma(-n-1+k)} (2\pi i)^n (z+d/c)^n.$$ Using that $$\frac{1}{\Gamma(-n-1+k)} = \frac{\sin(\pi(n+2-k))}{\pi} \Gamma(n+2-k),$$ and that $\sin(m\pi + \pi/2)= (-1)^m$, after rearranging we have $$\frac{1}{\pi i}  \frac{\varepsilon_d^{2k} \left( \frac{c}{d}\right) }{c^{2-k}}\sum_{n=0}^\infty \Gamma(n+2-k) \frac{L(f, a/c; n+1)}{(2\pi i /c^2)^{n+2-k}} (z+d/c)^n.$$ The fact that the above asymptotic series is Gevrey-1 is clear. Now we split the sum along $n=\ell$ for $\ell$ sufficiently large so that we can both leverage our Dirichlet series representation for $L(f, a/c; \rho)$ and ensure the convergence of a Laplace transform we will apply later. We write $$\begin{aligned}
\frac{1}{\pi i}  \frac{\varepsilon_d^{2k} \left( \frac{c}{d}\right) }{c^{2-k}} &\sum_{n=0}^{\ell-1}\Gamma(n+2-k) \frac{L(f, a/c; n+1)}{(2\pi i /c^2)^{n+2-k}} u^n \\&+ \frac{1}{\pi i} \frac{\varepsilon_d^{2k} \left( \frac{c}{d}\right)}{c^{2-k}}\sum_{n=\ell}^{\infty} \Gamma(n+2-k)\frac{L(f, a/c; n+1)}{(2\pi i /c^2)^{n+2-k}} u^n.
\end{aligned}$$

We will deal with the finitely many leading terms separately. For future use, we will call the first sum $\widehat{\varphi}_{-d/c}^{\ell}(z)$ second sum $\varphi_{-d/c}^\ell(z)$. For now, taking the Borel transform with shift $2-k$ with respect to $z+d/c$ of $\varphi_{-d/c}^\ell$ gives $$\frac{1}{\pi i}  \frac{\varepsilon_d^{2k} \left( \frac{c}{d}\right)}{c^{2-k}}\sum_{n=\ell}^\infty \frac{L(f, a/c; n+1)}{(2\pi i /c^2)^{n+2-k}} u^n.$$ This can be rewritten as $$\begin{aligned}
\frac{1}{\pi i}  \frac{\varepsilon_d^{2k} \left( \frac{c}{d}\right) }{c^{2-k}}\sum_{n=\ell}^{\infty} \sum_{m=1}^\infty \frac{a_m m^{1-k}\zeta_c^{am}}{\left(\frac{2\pi i m}{c^2}\right)^{n+2-k}} u^n 
= \frac{1}{\pi i}  \frac{\varepsilon_d^{2k} \left( \frac{c}{d}\right) }{c^{2-k}} \sum_{m=1}^\infty \frac{a_m m^{1-k}\zeta_c^{am}}{\left(\frac{2\pi i m}{c^2}\right)^{2-k}}\sum_{n=\ell}^{\infty}  \left(\frac{u}{\left(\frac{2\pi i m}{c^2}\right)}\right)^n
\end{aligned}$$ where we used absolute convergence to switch the order of summation. From here, summing the geometric series gives $$\frac{-1}{\pi i}  \frac{\varepsilon_d^{2k} \left( \frac{c}{d}\right) }{c^{2-k}}  \sum_{m=1}^\infty \frac{a_m m^{1-k}\zeta_c^{am} }{u-\left(\frac{2\pi i m}{c^2}\right)}\frac{u^{\ell}}{\left(\frac{2\pi i m}{c^2}\right)^{\ell+1-k}},$$ which has simple poles at $\omega_m = \frac{2\pi i m}{c^2}$ with residues $-2  \frac{\varepsilon_d^{2k} \left( \frac{c}{d}\right)}{c^{2-k}}  a_m m^{1-k}\zeta_c^{am}\omega_m^{k-1}$. The sum $\widehat{\varphi}_{-d/c}^{\ell}(z)$ will be resummed separately.

Turning to $g$ of *Type 5*, we appeal to the following result which is a corollary of Proposition 4.1 of [@fantini-rella]:

::: prop
[]{#prop: maass discont label="prop: maass discont"} Let $g$ be of Type 5 and let $\varphi_0(z)$ denote the asymptotic expansion of $g(z)$ as $z \to 0^+$ along a geodesic. Then we have $$\varphi_0(z)= \frac{1}{\pi i}\sum_{n =0}^\infty \Gamma(n+1) \sum_{m \neq 0}\frac{A_m}{(2\pi i m)^{n+1}}z^n.$$
:::

Taking a Borel transform of $\varphi(z)$, we have $$\begin{aligned}
\mathcal{B}_1(\varphi_0(z))= \frac{1}{\pi i}\sum_{n =0}^\infty  \sum_{m \neq 0}\frac{A_m}{(2\pi i m)^{n+1}}u^n=  \frac{1}{\pi i} \sum_{m \neq 0}\frac{A_m}{2\pi i m} \sum_{n =0}^\infty  \frac{u^n}{(2\pi i m)^{n}}=  \frac{-1}{\pi i} \sum_{m \neq 0} \frac{A_m}{u-2\pi i m}.    
\end{aligned}$$ This ultimately tells us that $\mathcal{B}_1(\varphi_0(z))$ has a meromorphic continuation to $\mathbb{C}$ with simple poles at $2\pi i m$ for $m \in \mathbb{Z}_{\neq 0}$ with residues $-2A_m$.

In the case where $g$ is of *Type 6*, the asymptotics require slightly more care.

::: prop
[]{#prop: eisenstein asymptotic label="prop: eisenstein asymptotic"} Let $g$ be of Type 6 and let $\varphi^*_0(z)$ denote the asymptotic expansion of $g(z)$ as $z \to 0^+$ along a geodesic. Then we have $$\varphi^*_0(z)= -8\frac{\log(-2\pi i z)-\gamma}{2\pi i z} -\frac{8}{\pi i} \sum_{\substack{n=1 \\ n \text{ odd}}}^\infty \Gamma(n+1) \sum_{m=1}^\infty \frac{d(m)}{(2\pi im)^{n+1}} z^n.$$
:::

::: proof
*Proof.* One considers the Mellin transform of $\sum_{n=1}^\infty d(n) q^n$ and moves the contour over the pole at $s=1$ to compute its contribution. We have $$g(z) = 1-4\sum_{n=1}^\infty d(n) q^n \sim -8\frac{\log(-2\pi i z)-\gamma}{2\pi i z} - 4 \sum_{n=1}^\infty \frac{\zeta^2(-n)}{n!}(2\pi i z)^n,$$ where $\gamma$ is the Euler-Mascheroni constant. From this point, we analyze the latter sum, which we call $\varphi_0(z)$. Using the functional equation for $\zeta^2$ and identities for the $\Gamma$-function, as formal power series we have $$- 4 \sum_{n=1}^\infty \frac{\zeta^2(-n)}{n!}(2\pi i z)^n = -4\sum_{\substack{n=1 \\ n \text{ odd}}}^\infty \Gamma(n+1) \frac{i^n}{2^n\pi^{n+2}} \zeta^2(n+1) z^n.$$ Now we are in the range where the Dirichlet series representation of $\zeta^2$ converges, and so we may expand and rearrange to arrive at

$$\frac{-8}{\pi i} \sum_{\substack{n=1 \\ n \text{ odd}}}^\infty \Gamma(n+1) \sum_{m=1}^\infty \frac{d(m)}{(2\pi im)^{n+1}} z^n. \qedhere$$ ◻
:::

Now considering the Borel transform of $\varphi_0$ and evaluating the geometric series, we have that $$\begin{aligned}
\mathcal{B}_1(\varphi_0(z)) &= \frac{-8}{\pi i} \sum_{\substack{n=1 \\ n \text{ odd}}}^\infty \sum_{m=1}^\infty \frac{d(m)}{(2\pi im)^{n+1}} u^n 


=  \frac{-8}{\pi i} \sum_{m=1}^\infty \frac{d(m)u}{(2\pi im)^{2} -u^2}.
\end{aligned}$$ Using the same strategy as in the proof of Proposition 4.1 of [@fantini-rella], this becomes $$\frac{4}{\pi i} \sum_{m\neq 0} \frac{d(|m|)}{z-2\pi i m}.$$ Then $\mathcal{B}_1(\varphi_0(z))$ has meromorphic continuation to $\mathbb{C}$ with simple poles at $2\pi i m$ for $m \in \mathbb{Z}_{\neq 0}$ with residues $8d(|m|)$.
