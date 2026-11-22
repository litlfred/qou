---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-012-32-winding-number-of-a-planar-brownian-motion
section_title: "Winding number of a planar Brownian motion"
section_number: 3.2
pages: 20-21
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.988
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
[]{#Sect:Winding label="Sect:Winding"} In this section, we consider a standard planar Brownian motion $(Z_t)_{t \in \mathbb{R}_+}$ starting from $z=1$. It is well known that, a.s., $Z_t$ never touches the origin. One can thus write $Z_t=R_t\,\E^{\I\varphi_t}$, for continuous functions $t\mapsto R_t$ and $t\mapsto \varphi_t$, where $\varphi_0=0$, see Figure [1](#fig:winding){reference-type="ref" reference="fig:winding"}.

<figure id="fig:winding">
<div class="center">
<embed src="winding.pdf" />
</div>
<figcaption>Planar Brownian motion and its winding number; we will see that the latter is asymptotically mod-Cauchy.<span id="fig:winding" label="fig:winding"></span></figcaption>
</figure>

The Fourier transform of the *winding number* $\varphi_t$ was computed by Spitzer in [@Spi58]: $$\mathbb{E}[\E^{\I\xi \varphi_t}]=\sqrt{\frac{\pi}{8t}}\,\,\E^{-\frac{1}{4t}}\,\left(I_{\frac{|\xi|-1}{2}}\left(\frac{1}{4t}\right)+I_{\frac{|\xi|+1}{2}}\left(\frac{1}{4t}\right)\right),$$ where $I_{\nu}(z)=\sum_{k=0}^\infty \frac{1}{k!\,\Gamma(\nu+k+1)}\,\left(\frac{z}{2}\right)^{\nu+2k}$ is the modified Bessel function of the first kind. As a consequence, and as was noticed in [@DKN11 §3.2], $(\varphi_t)_{t \in \mathbb{R}_+}$ converges mod-Cauchy with parameters $\tfrac{\log 8t}{2}$ and limiting function $\theta(\xi)=\sqrt{\pi} \ \Gamma\big(\tfrac{|\xi|+1}{2}\big)^{-1}$. Indeed, $$\begin{aligned}
&\mathbb{E}[\E^{\I\xi \varphi_t}] \exp\left(|\xi|\,\frac{\log 8t}{2}\right) \\
&= \sqrt{\pi}\,\E^{-\frac{1}{4t}} \,
\left(\sum_{k=0}^\infty \frac{1}{k!}\left(\frac{1}{8t}\right)^{\!2k} \left(\frac{1}{\Gamma(k+\frac{|\xi|+1}{2})} + \frac{1}{8t\,\Gamma(k+\frac{|\xi|+3}{2})}\right)\right),
\end{aligned}$$ and the limit of the power series as $t$ goes to infinity is its constant term $\frac{1}{\Gamma(\frac{|\xi|+1}{2})}$.

Here, $|\theta(\xi)-1|$ is of order $O(|\xi|)$ around $0$, since the first derivative of $\Gamma$ is not zero at $\frac{1}{2}$. Therefore, if the mod-convergence can be given a zone of control, then the index of this control will be $v=1$, which forces for Berry--Esseen estimates $\gamma\leq 0$ since $\gamma\leq \min(\frac{v-1}{\alpha},\frac{1}{w-\alpha})$. Conversely, for any $\xi$, notice that the function $x \mapsto \frac{1}{\Gamma(x+\frac{1}{2})}$ has derivative bounded on $\mathbb{R}_+$ by $$-\frac{\Gamma'(\frac{1}{2})}{\left(\Gamma(\frac{1}{2})\right)^2}=1.11_- < \frac{2}{\sqrt{\pi}},$$ and therefore that $$\begin{aligned}
|\theta_t(\xi)-1| &\leq 2\,\E^{-\frac{1}{4t}} \sum_{k=0}^\infty \frac{1}{k!}\left(\frac{1}{8t}\right)^{2k} \left(1+\frac{1}{8t}\right) \frac{|\xi|}{2} \\
&\leq \E^{\left(\frac{1}{8t}\right)^2-\frac{1}{4t}}\,\left(1+\frac{1}{8t}\right)\,|\xi| \leq |\xi|
\end{aligned}$$ for $t$ large enough. So, in particular, one has mod-Cauchy convergence with index of control $(1,1)$, zone of control $[-K,K]$ with $K$ as large as wanted, and constants $K_1=1$ and $K_2=0$. It follows then from Theorem [\[thm:kolmogorov\]](#thm:kolmogorov){reference-type="ref" reference="thm:kolmogorov"} that if $\mathcal{C}$ follows a standard Cauchy law, then $$d_\mathrm{Kol}\left(\frac{2\varphi_t}{\log 8t},\,\mathcal{C}\right)\leq \frac{4}{\log 8t}$$ for $t$ large enough. As far as we know, this estimate is new.
