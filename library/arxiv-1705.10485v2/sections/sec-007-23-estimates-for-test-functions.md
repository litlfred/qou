---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-007-23-estimates-for-test-functions
section_title: "Estimates for test functions"
section_number: 2.3
pages: 12-14
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.928
latex_coverage_ratio: 0.887
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
We now give an estimate of $\mathbb{E}[f_n(Y_n)]-\mathbb{E}[f_n(Y)]$, where $(f_n)_{n \in \mathbb{N}}$ is a sequence of test functions in $\mathscr{T}_0(\mathbb{R})$ or $\mathscr{T}_1(\mathbb{R})$, and $(Y_n)_{n\in\mathbb{N}}$ is a sequence of random variables associated to a sequence $(X_n)_{n\in \mathbb{N}}$ which has a zone of control.

::: proposition
[]{#prop:zonedistribution label="prop:zonedistribution"} Let $(X_n)_{n \in \mathbb{N}}$ be a sequence of random variables, $\phi_{c,\alpha,\beta}$ a reference stable law, $Y$ with law $\phi_{c,\alpha,\beta}$ and $Y_n$ as in Proposition [\[prop:clt\]](#prop:clt){reference-type="ref" reference="prop:clt"}. We assume that:

1.  $(X_n)_{n\in \mathbb{N}}$ has a zone of control $[-K(t_n)^\gamma,K(t_n)^\gamma]$ with index $(v,w)$;

2.  $(f_n)_{n \in \mathbb{N}}$ is a sequence of smooth test functions in $\mathscr{T}_0(\mathbb{R})$, such that the support of $\widehat{f}_n$ is included into $[-K(t_n)^{\gamma+1/\alpha},K(t_n)^{\gamma+1/\alpha}]$.

Then, $$|\mathbb{E}[f_n(Y_n)] - \mathbb{E}[f_n(Y)]|\leq C_0(c,\alpha,v)\,K_1\,\frac{\|f_n\|_{\mathrm{L}^1}}{(t_n)^{v/\alpha}},$$ where $C_0(c,\alpha,v)=\frac{2^{\frac{v+1}{\alpha}}\,\Gamma((v+1)/\alpha)}{\pi\alpha\,c^{v+1}}$.

If instead of (2) we assume:

1.  $(f_n)_{n \in \mathbb{N}}$ is a sequence of smooth test distributions in $\mathscr{T}_1(\mathbb{R})$ such that if $\phi_n = \partial f_n$ is the derivative of the distribution $f_n$, then the support of $\widehat{\phi}_n$ is included into $[-K(t_n)^{\gamma+1/\alpha},K(t_n)^{\gamma+1/\alpha}]$.

Then $$|\mathbb{E}[f_n(Y_n)] - \mathbb{E}[f_n(Y)]|\leq C_1(c,\alpha,v)\,K_1\,\frac{\|\phi_n\|_{\mathrm{L}^1}}{(t_n)^{v/\alpha}},$$ where $C_1(c,\alpha,v)=\frac{2^{v/\alpha}\,\Gamma(v/\alpha)}{\pi\alpha\,c^{v}}$.
:::

::: proof
*Proof.* Consider first a sequence $(f_n)_{n \in \mathbb{N}}$ of test functions in $\mathscr{T}_0(\mathbb{R})$, which satisfies (2). Using Parseval formula and the zone of control assumption, we have $$\begin{aligned}
\mathbb{E}[f_n(Y_n)]-\mathbb{E}[f_n(Y)] &= \frac{1}{2\pi} \!\int_{-K(t_n)^{\gamma+\frac{1}{\alpha}}}^{K(t_n)^{\gamma+\frac{1}{\alpha}}} \!\!\widehat{f}_n(\xi)\,\E^{\eta(-\I\xi)}\left(\theta_n\!\left(-\xi/(t_n)^{\frac{1}{\alpha}}\right)-1\right)\!\,d\hspace*{-0.3mm}{\xi};\\
|\mathbb{E}[f_n(Y_n)]-\mathbb{E}[f_n(Y)]| &\leq \frac{K_1\|\widehat{f}_n\|_\infty}{2\pi (t_n)^{v/\alpha}} \int_{-K(t_n)^{\gamma+\frac{1}{\alpha}}}^{K(t_n)^{\gamma+\frac{1}{\alpha}}} |\xi|^v\,\E^{-|c\xi|^\alpha + K_2 \left(\frac{|\xi|}{(t_n)^{1/\alpha}}\right)^w} \,d\hspace*{-0.3mm}{\xi}.
\end{aligned}$$ For $\xi$ in $[-K(t_n)^{\gamma+1/\alpha},K(t_n)^{\gamma+1/\alpha}]$, since $(t_n)^{\gamma-1/(w-\alpha)}\leq 1$, the second term in the exponent can be bounded as follows: $$\begin{aligned}
K_2 \left(\frac{|\xi|}{(t_n)^{1/\alpha}}\right)^w = K_2 |\xi|^{\alpha} \left(\frac{|\xi|}{(t_n)^{\frac{1}{\alpha}+\frac{1}{w-\alpha}}}\right)^{w-\alpha} &\leq K_2 |\xi|^{\alpha} \left(K (t_n)^{\gamma-\frac{1}{w-\alpha}}\right)^{w-\alpha} \\
&\leq \frac{|c\xi|^\alpha}{2}.
\end{aligned}$$ This is compensated by the term $-|c\xi|^\alpha$ and, therefore, $$\begin{aligned}
|\mathbb{E}[f_n(Y_n)]-\mathbb{E}[f_n(Y)]| &\leq \frac{K_1\|\widehat{f}_n\|_\infty}{2\pi (t_n)^{v/\alpha}}\int_{\mathbb{R}} |\xi|^v \E^{-\frac{|c\xi|^\alpha}{2}}\,d\hspace*{-0.3mm}{\xi} \\
&\leq \frac{2^{\frac{v+1}{\alpha}}\,K_1}{\pi\alpha\,c^{v+1} (t_n)^{v/\alpha}}\,\,\Gamma\!\left(\frac{v+1}{\alpha}\right)\,\|f_n\|_{\mathrm{L}^1}.
\end{aligned}$$ This ends the proof of the first case. For test distributions $f_n \in \mathscr{T}_1(\mathbb{R})$ which satisfies the condition $(2')$, let us introduce the signed measure $\mu = \mathbb{P}_{Y_n}-\mathbb{P}_Y$. One has $\widehat{\mu}(0)=0$, and by hypothesis, $$\left|\frac{\widehat{\mu}(\xi)}{\xi}\right| \leq \frac{K_1\,|\xi|^{v-1}}{(t_n)^{v/\alpha}}\,\E^{-|c\xi|^\alpha+K_2\left(\frac{|\xi|}{(t_n)^{1/\alpha}}\right)^w}.$$ Remark [\[rmk:parsevaldistribution\]](#rmk:parsevaldistribution){reference-type="ref" reference="rmk:parsevaldistribution"} applies, and thus, $$|\mathbb{E}[f_n(Y_n)]-\mathbb{E}[f_n(Y)]|=\left|\left\langle \mu\vphantom{f_n}\,\right |\left.f_n \vphantom{\mu}\right\rangle\right| = \frac{1}{2\pi}\left|\left\langle  \widehat{f_n}\vphantom{\overline{\widehat{\mu}}}\,\right |\left.\overline{\widehat{\mu}} \vphantom{ \widehat{f_n}}\right\rangle\right| = \frac{1}{2\pi}\left|\int_{\mathbb{R}} \widehat{\phi_n}(\xi)\,\frac{\widehat{\mu}(-\xi)}{\xi}\,d\hspace*{-0.3mm}{\xi}\right| .$$ From there, the computations are exacly the same as before, with an index $v-1$ instead of $v$.0◻ ◻
:::
