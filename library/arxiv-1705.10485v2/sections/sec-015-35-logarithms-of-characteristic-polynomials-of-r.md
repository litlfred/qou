---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-015-35-logarithms-of-characteristic-polynomials-of-r
section_title: "Logarithms of characteristic polynomials of random matrices"
section_number: 3.5
pages: 26-28
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.946
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
In [@KN12 Sections 3 and 4] and [@FMN16 Section 7.5], the mod-Gaussian convergence of the following random variables was proven:

::: center
         random matrix $M_n$                             random variable $X_n$                       parameters $t_n$                 residue $\theta(\xi)$
  ---------------------------------- ------------------------------------------------------------- -------------------- -------------------------------------------------
    $\mathrm{Haar}(\mathrm{U}(n))$                 $\mathrm{Re}(\log \det(I_n-M_n))$                $\frac{\log n}{2}$   $\frac{(G(1+\frac{\I \xi}{2}))^2}{G(1+\I \xi)}$
   $\mathrm{Haar}(\mathrm{USp}(n))$   $\log \det(I_{2n}-M_n) - \frac{1}{2} \log \frac{\pi n}{2}$    $\log \frac{n}{2}$    $\frac{G(\frac{3}{2})}{G(\frac{3}{2}+\I\xi)}$
   $\mathrm{Haar}(\mathrm{SO}(2n))$   $\log \det(I_{2n}-M_{n}) - \frac{1}{2} \log \frac{8\pi}{n}$   $\log \frac{n}{2}$    $\frac{G(\frac{1}{2})}{G(\frac{1}{2}+\I\xi)}$

  : Mod-Gaussian convergence of the characteristic polynomials of Haar-distributed random matrices in compact Lie groups.
:::

Here, $G$ is Barnes' function, which is the unique entire solution of the equations $G(1)=1$ and $G(z+1)=G(z)\,\Gamma(z)$. Moreover, the mod-Gaussian convergence holds in fact on an half-plane $H =\{z \in \mathbb{C}\,|\,\mathrm{Re}(z)>-\alpha\}$. In the sequel, we denote $X_n^{\mathrm{A}}$, $X_n^{\mathrm{C}}$ and $X_n^{\mathrm{D}}$ the mod-Gaussian convergent random variables, according to the type of the classical group ($\mathrm{A}$ for unitary groups, $\mathrm{C}$ for compact symplectic groups and $\mathrm{D}$ for even orthogonal groups). Before computing zones of control for these variables, let us make the following essential remark:

::: remark
[]{#rem:clever label="rem:clever"} Let $(X_n)_{n \in \mathbb{N}}$ be a sequence of random variables that is mod-Gaussian convergent on a domain $D \subset \mathbb{C}$ which contains a neighborhood of $0$ (this ensures that $\theta_n$ and all its derivatives converge towards those of $\theta$). We denote $(t_n)_{n\in \mathbb{N}}$ the parameters of mod-Gaussian convergence of $(X_n)_{n \in \mathbb{N}}$. Then, without generality, one can assume $\theta_n'(0)=\theta_n''(0) = 0$ and $\theta'(0)=\theta''(0)=0$. Indeed, set $$\widetilde{X}_n = X_n + \I \theta_n'(0) \qquad;\qquad \widetilde{t}_n = t_n - \theta_n''(0).$$ We then have $$\begin{aligned}
\widetilde{\theta}_n(\xi):=\mathbb{E}[\E^{\I \xi \widetilde{X}_n}]\, \E^{\widetilde{t}_n\frac{\xi^2}{2}} = \theta_n(\xi)\,\E^{-\theta_n'(0) \xi - \theta_n''(0) \frac{\xi^2}{2}}
\end{aligned}$$ and this new residue satisfies $\widetilde{\theta}_n'(0) = \widetilde{\theta}_n''(0) = 0$. For the construction of zones of control, it allows us to force $v=3$, up to a translation of $X_n$ and of the parameter $t_n$.
:::

In the following, we only treat the case of unitary groups, the two other cases being totally similar (one could also look at the imaginary part of the log-characteristic polynomial). There is an exact formula for the Fourier transform of $X_n^\mathrm{A}$ [@KS2000 Formula (71)]: $$\mathbb{E}[\E^{\I \xi X_n^{\mathrm{A}}}] = \prod_{k=1}^n \frac{\Gamma(k)\Gamma(k+\I \xi)}{\left(\Gamma(k+\frac{\I\xi}{2})\right)^2}.$$ We have $\mathbb{E}[X_n^{\mathrm{A}}]=0$, and $$\widetilde{t}_n=\mathbb{E}[(X_n^{\mathrm{A}})^2]=\frac{1}{2}\sum_{k=1}^n \frac{\Gamma''(k)}{\Gamma(k)} - \left(\frac{\Gamma'(k)}{\Gamma(k)}\right)^2 = \frac{1}{2}\sum_{k=1}^n \psi_1(k),$$ where $\psi_1(z)$ is the trigamma function $\frac{d^2}{dz^2}(\log\Gamma(z))$, and is given on integers by the remainder of the series $\zeta(2)$: $$\psi_1(k) = \sum_{m=k}^\infty \frac{1}{m^2}.$$ Therefore, $\widetilde{t}_n = \frac{1}{2}\sum_{m=1}^\infty \frac{\min(n,m)}{m^2} = \frac{1}{2}(\log n + \gamma + 1 + O(n^{-1}))$. So, $(X_n^\mathrm{A})_{n \in \mathbb{N}}$ is mod-Gaussian convergent with parameters $(\widetilde{t}_n)_{n \in \mathbb{N}}$ and limit $$\widetilde{\theta}(\xi) = \frac{\left(G(1+\frac{\I \xi}{2})\right)^2}{G(1+\I \xi)}\,\E^{\frac{(\gamma+1)\xi^2}{4}},$$ which satisfies $\widetilde{\theta}'(0)=\widetilde{\theta}''(0)=0$. With these conventions, we can write the residues $\widetilde{\theta}_n(\xi)$ as $$\widetilde{\theta}_n(\xi)= \left(\prod_{k=1}^n \frac{\Gamma(k)\Gamma(k+\I \xi)}{\left(\Gamma(k+\frac{\I\xi}{2})\right)^2}\right)\,\E^{\frac{\widetilde{t}_n\xi^2}{2}} = \prod_{k=1}^n \left(\frac{\Gamma(k)\Gamma(k+\I \xi)}{\left(\Gamma(k+\frac{\I\xi}{2})\right)^2}\,\E^{\frac{\psi_1(k)\xi^2}{4}}\right).$$ Denote $\vartheta_k(\xi)$ the terms of the product on the right-hand side; we use a similar strategy as in Section [\[subsec:independent\]](#subsec:independent){reference-type="ref" reference="subsec:independent"} for computing a zone of control. The function $\varphi_k(\xi) = \log \vartheta_k(\xi)$ vanishes at $0$, has its two first derivatives that also vanish at $0$, and therefore writes as $$\varphi_k(\xi) = \left(\int_0^1 \varphi_k'''(t\xi)\, (1-t)^2\,d\hspace*{-0.3mm}{t}\right)\frac{\xi^3}{2}.$$ The third derivative of $\varphi_k(\xi)$ is given by $$\varphi_k'''(\xi) = -\I \,\psi_2(k+\I\xi) + \frac{\I}{2}\,\psi_2\left(k+\frac{\I\xi}{2}\right),$$ with $\psi_2(z) = -2\sum_{j=0}^\infty \frac{1}{(j+z)^3}$. As a consequence, $\varphi_k'''(\xi)$ is *uniformly bounded* on $\mathbb{R}$ by $$3\,\sum_{j=0}^\infty \frac{1}{(j+k)^3} \leq \frac{3\,\zeta(3)}{k^2}.$$ Therefore, $$\begin{aligned}
|\varphi_k(\xi)| &\leq \frac{\zeta(3)\, |\xi|^3}{2k^2};\\
|\vartheta_k(\xi)| &\leq \E^{\frac{\zeta(3)\, |\xi|^3}{2k^2}};\\
|\vartheta_k(\xi)-1| &\leq \frac{\zeta(3)\, |\xi|^3}{2k^2}\,\E^{\frac{\zeta(3)\, |\xi|^3}{2k^2}}.
\end{aligned}$$ It follows that for any $n$ and any $\xi \in \mathbb{R}$, $|\widetilde{\theta}_n(\xi)-1| \leq S\exp S$ with $S = \sum_{k=1}^\infty \frac{\zeta(3)\, |\xi|^3}{2k^2} = \frac{3\,\zeta(3)\,|\xi|^3}{\pi^2}$. Set $K_1=K_2 = \frac{3\,\zeta(3)}{\pi^2}$, and $K=\frac{1}{4K_2} = \frac{\pi^2}{12\,\zeta(3)}$. We have a zone of control $[-Kt_n,Kt_n]$ of index $(3,3)$, with constants $K_1$ and $K_2$. We conclude with Theorem [\[thm:kolmogorov\]](#thm:kolmogorov){reference-type="ref" reference="thm:kolmogorov"}:

::: proposition
Let $M_n$ be a random unitary matrix taken according to the Haar measure. For $n$ large enough, $$d_\mathrm{Kol}\left(\frac{\mathrm{Re}(\log \det(I_n-M_n))}{\sqrt{\mathrm{Var}(\mathrm{Re}(\log \det(I_n-M_n)))}}\,,\,\mathcal{N}_{\mathbb{R}}(0,1)\right) \leq \frac{C}{(\log n)^{3/2}}$$ with a constant $C \leq 18$. Up to a change of the constant, the same result holds if one replaces $\mathrm{Re}(\log \det(I_n-M_n))$ by $\mathrm{Im}(\log \det(I_n-M_n))$, or by $$\log \det(I_{2n}-P_n) - \mathbb{E}[\det(I_{2n}-P_n)],$$ with $P_n$ Haar distributed in the unitary compact symplectic group $\mathrm{USp}(n)$ or in the even special orthogonal group $\mathrm{SO}(2n)$.
:::
