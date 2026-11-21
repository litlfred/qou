---
doc_id: arxiv-2505.00799v2
doc_title: "Quantum Modular Forms and Resurgence"
section_id: sec-010-33-discontinuity-calculations
section_title: "Discontinuity Calculations"
section_number: 3.3
pages: 24-27
source_pdf: 2505.00799v2.pdf
source_sha256: cc9d2ab4c6c79b50
toc_source: outline
text_source: latex
latex_prose_ratio: 0.748
latex_coverage_ratio: 0.86
doc_brief: "Quantum Modular Forms and Resurgence — In 2010, Zagier described a new phenomenon which he called quantum mod- ularity."
---
[]{#subsec: discontinuity label="subsec: discontinuity"} Here we compute the discontinuities of the Borel-Laplace sums of the functions of *Types 4* and *5* along the ray of angle $\pi/2$.

::: prop
[]{#prop: eichler discont label="prop: eichler discont"} If $g$ is of Type 4 with $2-k= \kappa$ or of Type 5 with $s = \kappa/2$, then for $\gamma = \begin{psmallmatrix} a & b \\ c & d \end{psmallmatrix} \in \Gamma_0(N)$, we have that $2g|_{\kappa}\gamma(z) = \emph{disc}_\kappa^{\pi/2}(\mathcal{B}_\kappa(\varphi_{-d/c}(z))$.
:::

::: proof
*Proof.* We begin with $g$ of *Type 4* and $\widehat{\varphi}_{-d/c}^{\ell}(z)$ as defined in Section [\[subsec: asymptotics\]](#subsec: asymptotics){reference-type="ref" reference="subsec: asymptotics"}. Note that $\mathcal{S}_1^{\pi/2 - \varepsilon}(\widehat{\varphi}_{-d/c}^{\ell})=\mathcal{S}_1^{\pi/2 + \varepsilon}(\widehat{\varphi}_{-d/c}^{\ell})$ for $0< \varepsilon< \pi/2$ since $\widehat{\varphi}_{-d/c}^{\ell}$ is a polynomial. Therefore, these terms cannot contribute to the discontinuity.

By the computations in Section [\[subsec: asymptotics\]](#subsec: asymptotics){reference-type="ref" reference="subsec: asymptotics"}, we also have that $\mathcal{B}_{2-k}(\varphi^\ell_{-d/c}(z))$ has simple poles at $\omega_m = \frac{2\pi i m}{c^2}$ with residues $-2 \frac{\varepsilon_d^{2k} \left( \frac{c}{d}\right)}{c^{2-k}}  a_m m^{1-k}\zeta_c^{am}\omega_m^{k-1}$. Then $$\begin{aligned}
\text{disc}_{2-k}^{\pi/2}(\mathcal{B}_{2-k}(\varphi_{-d/c}(z)) &= (z+d/c)^{k-2}\sum_{\omega \in \Omega_\theta} S_\omega \omega^{1-k} e^{-\omega/(z+d/c)}\\
    &= 2 \frac{\varepsilon_d^{2k} \left( \frac{c}{d}\right)}{c^{2-k}} (z+d/c)^{k-2}\sum_{n =1}^\infty    a_m m^{1-k}\zeta_c^{am} e^{-2\pi i m/(c^2(z+d/c))}\\
    &= 2(cz+d)^{k-2}\varepsilon_d^{2k} \left( \frac{c}{d}\right)\sum_{n =1}^\infty    a_m m^{1-k} e^{2\pi i m\left(\frac{az+b}{cz+d}\right)} \\
    &= 2g|_{2-k}\gamma(z),
\end{aligned}$$ where the second to last equality follows from the identity $\frac{1}{c^2(\tau+d/c)} = \frac{a}{c} - \frac{a\tau+ b}{c\tau +d}$. Turning to *Type 5*, we have in this case that $$\text{disc}_\kappa^{\pi/2}(\mathcal{B}_\kappa(\varphi_{0}(z)) = z^{-1}\sum_{\omega \in \Omega_\theta} S_\omega e^{-\omega/z} =2 z^{-1} \sum_{n=1}^\infty  A_n e^{-2\pi i n/z} = 2g|_{1}(S)(z). \qedhere$$ ◻
:::

Using the analogous result for the Eisenstein case given in Proposition [\[prop: eisenstein asymptotic\]](#prop: eisenstein asymptotic){reference-type="ref" reference="prop: eisenstein asymptotic"}, we can also prove the following.

::: prop
If $g$ is of Type 6, then for $\gamma = \begin{psmallmatrix} a & b \\ c & d \end{psmallmatrix} \in \Gamma_0(N)$, we have that $2g|_{1}\gamma(z) = \emph{disc}_1^{\pi/2}(\mathcal{B}_1(\varphi_{0}(z))$.
:::

Now we return to the cases that require a different approach.

::: prop
[]{#prop: modular slash label="prop: modular slash"} If $g$ is of Type 1 or 2 with $\kappa = k$ or Type 3 with $\kappa = 2-k$, then for $\gamma = \begin{psmallmatrix} a & b \\ c & d \end{psmallmatrix} \in \Gamma_0(N)$, we have that $$g|_{\kappa}\gamma(z) = \frac{1}{2\sqrt{z+d/c}} \int_{\Gamma}e^{-u/(z+d/c)}\hat{g}_{-d/c}^{odd}(u)\frac{du}{\sqrt{u}}.$$
:::

::: proof
*Proof.* In the cases where $g$ is of *Type 1* or *2*, since the asymptotic series $\varphi_{-d/c}(z)$ is zero, we have that $\mathcal{B}_{1/2}(\varphi_{-d/c}(z))=0$. So, it suffices to analyze $$\frac{1}{\sqrt{u}}\widehat{g}_{-d/c}^{odd}(u) = -\frac{1}{\sqrt{\pi }} \sum_{n=0}^\infty \frac{ L(g, \zeta_c^{-d};-n-1/2)}{\Gamma(2n+2)}(8\pi i)^{n+1/2}u^{n}.$$

We first consider $g$ of *Type 1* or *2*. We assume the notation and some of the techniques of Proposition [\[prop: med resum\]](#prop: med resum){reference-type="ref" reference="prop: med resum"}. We can write the above as

$$\begin{aligned}
\frac{1}{\sqrt{u}}\widehat{g}_{-d/c}^{odd}(u) &= - \sum_{n=0}^\infty \frac{ L(g, \zeta_c^{-d};-n-1/2)}{\Gamma(n+1)\Gamma(n+3/2)}(2\pi i)^{n+1/2}u^{n}\\
 &=C_{k, -d/c} \frac{i^{-k}}{\pi} \sum_{n=0}^\infty \Big\lbrack \left(\frac{c}{2\pi}\right)^{k+2n+1}\frac{\Gamma(n+k+1/2)}{\Gamma(n+1)}\\ & \quad \quad \quad \quad\quad \quad\quad \quad\cdot L(g, \zeta_c^{a}; n+k+1/2) (-1)^n(2\pi i)^{n+1/2}u^n\Big\rbrack,
\end{aligned}$$ where $C_{k, -d/c}=1$ when $k$ is an integer and equals $\varepsilon_d^{2k}\left(\frac{c}{d}\right)$ when $k$ is a half-integer.

If we define $$\Phi(z) =C_{k, -d/c}\frac{i^{-k}}{\pi} \sum_{n=0}^\infty \left(\frac{c}{2\pi}\right)^{k+2n+1} (-1)^n\Gamma(n+k+1/2)L(g, \zeta_c^{a}; n+k+1/2)(2\pi i)^{n+1/2}z^n,$$ then we see that $\mathcal{B}_1(\Phi(z)) = \frac{1}{\sqrt{u}}\widehat{g}_{-d/c}^{odd}(u)$. Instead consider $\mathcal{B}_{k+1/2}(\Phi(z))$, which equals $$i^{-k} C_{k, -d/c}\sum_{n=0}^\infty \left(\frac{c}{2\pi}\right)^{k+2n+1} (-1)^nL(g, \zeta_c^{a}; n+k+1/2)(2\pi i)^{n+1/2}u^n.$$ Writing $L(g, \zeta_c^{a}; n+k+1/2)$ as its Dirichlet series and using absolute convergence allows us to write this as $$\begin{aligned}
&\frac{-C_{k, -d/c}}{\pi i c^k} \sum_{m=1}^\infty \sum_{n=0}^\infty \frac{a(m)\zeta_c^{am}}{(2\pi i m/c^2)^{n+k+1/2}}u^n = \frac{C_{k, -d/c}}{\pi i c^k}\sum_{m=1}^\infty  \frac{a(m)\zeta_c^{am}}{u - 2\pi i m/c^2}\frac{1}{(2\pi i m/c^2)^{k-1/2}}.
\end{aligned}$$ We can argue along the same lines as in Proposition [\[prop: med resum\]](#prop: med resum){reference-type="ref" reference="prop: med resum"} in order to move between the Borel-Laplace sum of $\Phi$ with shift 1 and with shift $k+1/2$. We have that $$\begin{aligned}
&\frac{1}{2\sqrt{z+d/c}} \int_{\Gamma}e^{-u/(z+d/c)}\widehat{g}_{-d/c}^{odd}(u)\frac{du}{\sqrt{u}}\\
&= \frac{1}{2\sqrt{z+d/c}} \int_{\Gamma}e^{-u/(z+d/c)}\mathcal{B}_1(\Phi)\;du\\


&= \frac{1}{2}\sqrt{z+d/c}\left( \mathcal{L}_{1}^{\pi/2-\varepsilon}(\mathcal{B}_1(\Phi)) - \mathcal{L}_{1}^{\pi/2+\varepsilon}(\mathcal{B}_1(\Phi))\right) \\
&= \frac{1}{2}\sqrt{z+d/c}\left( \mathcal{L}_{k+1/2}^{\pi/2-\varepsilon}(\mathcal{B}_{k+1/2}(\Phi)) - \mathcal{L}_{k+1/2}^{\pi/2+\varepsilon}(\mathcal{B}_{k+1/2}(\Phi))\right)\\
&= \sqrt{z+d/c}\cdot c^{-k} (z+d/c)^{-k-1/2} \sum_{m=1}^\infty a(m)\zeta_c^{am}\frac{(2\pi i m/c^2)^{k-1/2}}{(2\pi i m/c^2)^{k-1/2}} e^{2\pi i m/c^2(z+d/c)}\\
&= (cz+d)^{-k}\sum_{m=1}^\infty a(m) e^{2\pi i m\left(\frac{az+b}{cz+d}\right)}.
\end{aligned}$$

In the case where $g$ is of *Type 3*, the argument is largely the same. We assume that $g$ is the Eichler integral of $f$. Turning our attention back to $$\frac{1}{\sqrt{u}}\widehat{g}_{-d/c}^{odd}(u) = -\frac{1}{\sqrt{\pi }} \sum_{n=0}^\infty \frac{ L(g, \zeta_c^{-d};-n-1/2)}{\Gamma(2n+2)}(8\pi i)^{n+1/2}u^{n},$$ we see that this equals $$\begin{aligned}
    &-\frac{1}{\sqrt{\pi}}\sum_{n=0}^\infty \frac{L(f, \zeta_c^{-d};-n+k-3/2)}{\Gamma(2n+2)}(8\pi i)^{n+1/2} u^{n} \\
    
    &= \frac{- c^{k-2} \varepsilon_d^{2k} \left( \frac{c}{d}\right)}{\pi i}\sum_{n=0}^\infty  \frac{\Gamma(n-k+5/2)}{\Gamma(n+1)} \frac{L(f, \zeta_c^{a}; n+3/2)}{(2\pi i/c^2)^{n+5/2-k}} u^n.\\
\end{aligned}$$ Again we define $$\Phi(z) := \frac{- c^{k-2} \varepsilon_d^{2k} \left( \frac{c}{d}\right)}{\pi i}\sum_{n=0}^\infty \Gamma(n-k+5/2) \frac{L(f, \zeta_c^{a}; n+3/2)}{(2\pi i/c^2)^{n+5/2-k}} z^n,$$ so that $\mathcal{B}_1(\Phi(z)) =\frac{1}{\sqrt{u}}\widehat{g}_{-d/c}^{odd}(u)$. After splitting off finitely many terms to ensure convergence of the Dirichlet series representation of $L(f, \zeta_c^{a}; n+3/2)$, we take the Borel transform of the remaining terms of $\Phi$ with shift $5/2-k$.

We proceed as before to realize the discontinuity after shifting as in Proposition [\[prop: eichler discont\]](#prop: eichler discont){reference-type="ref" reference="prop: eichler discont"}, deforming contours and relating Borel-Laplace sums as for *Types 1* and *2*. ◻
:::

# Proof of Theorem [\[thm: Main\]](#thm: Main){reference-type="ref" reference="thm: Main"} {#sec: main theorem}

We now prove our main theorem. We proceed by analyzing each case in order. For $g$ of *Type 1* or *2*, by Section [\[subsec: asymptotics\]](#subsec: asymptotics){reference-type="ref" reference="subsec: asymptotics"}, we know that the Borel--Laplace sum $$\frac{1}{\sqrt{z+d/c}} \int_{0}^{\infty}e^{-u/(z+d/c)} \mathcal{B}_{1/2}(\varphi_{-d/c}(z)) \frac{du}{\sqrt{\pi u}}$$ equals zero. Since in these cases $g$ is modular, this equals their obstruction to modularity. Moreover, we have that $$g(z) =  \frac{1}{2\sqrt{z+d/c}}\int_{\Gamma}e^{-u/(z+d/c)} \hat{g}_{-d/c}(u) \;\frac{du}{\sqrt{ u}} = \frac{1}{2\sqrt{z+d/c}} \int_{\Gamma}e^{-u/(z+d/c)}\hat{g}_{-d/c}^{odd}(u)\frac{du}{\sqrt{u}}.$$ Lastly, by Proposition [\[prop: modular slash\]](#prop: modular slash){reference-type="ref" reference="prop: modular slash"}, we have that $$g|_{\kappa}\gamma(z) = \frac{1}{2\sqrt{z+d/c}} \int_{\Gamma}e^{-u/(z+d/c)}\hat{g}_{-d/c}^{odd}(u)\frac{du}{\sqrt{u}}.$$ Thus we have that $g(z) = g|_{\kappa}\gamma(z)$.

When $g$ is of *Type 3*, the argument is essentially the same, except the integral $$\frac{1}{\sqrt{z+d/c}} \int_{0}^{\infty}e^{-u/(z+d/c)} \mathcal{B}_{1/2}(\varphi_{-d/c}(z)) \frac{du}{\sqrt{\pi u}}$$ is not zero. We note that this is precisely the Borel resummation of $\varphi_{d/c}$ with shift $1/2$, and so it is equal to the Borel resummation of $\varphi_{d/c}$ with shift $1$. We will show explicitly that this equals the expected period polynomial in Proposition prop: polynomial.

For $g$ of *Type 4* or *5*, we have already shown that $g(z)=\mathcal{S}_{med}^{\pi/2}(\varphi_{-d/c})(z)$ in Proposition [\[prop: med resum\]](#prop: med resum){reference-type="ref" reference="prop: med resum"}. From Section [\[subsec: resurgence\]](#subsec: resurgence){reference-type="ref" reference="subsec: resurgence"}, we have that $$\mathcal{S}_{med}^{\pi/2}(\varphi_{-d/c})=\mathcal{S}^{0}(\varphi_{-d/c}) + \frac{1}{2}\text{disc}_{\kappa}^{\pi/2}(\mathcal{B}_{\kappa}(\varphi_{-d/c}))$$ for $z+d/c$ in the first quadrant. By Proposition [\[prop: eichler discont\]](#prop: eichler discont){reference-type="ref" reference="prop: eichler discont"}, we have that $$\frac{1}{2}\text{disc}_{\kappa}^{\pi/2}(\mathcal{B}_{\kappa}(\varphi_{-d/c})) = g|_{\kappa}\gamma(z)$$ where $\gamma = \begin{psmallmatrix} a & b \\ c & d
 \end{psmallmatrix}$. This tells us that $g(z) - g|_\kappa\gamma(z) = \mathcal{S}^0(\varphi_{-d/c})$ in this region. By analytic continuation, we get the desired equality on $\mathbb{H}$. The analytic continuation of $\mathcal{S}^0(\varphi_{-d/c})$ to $\mathbb{C}_\gamma$ is guaranteed by the location of the Stokes rays for $\mathcal{B}_\kappa (\varphi_{-d/c})$. The case where $g$ is of *Type 6* is identical except for the addition of the integral $$\frac{1}{2\sqrt{z}}\int_\Gamma e^{-u/z} \left( \frac{-4+2\log(8\pi i u)}{2\pi i u} \right)\frac{du}{\sqrt{\pi u}},$$ which contributes to the obstruction to modularity.
