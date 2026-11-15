---
doc_id: arxiv-2509.20302v1
doc_title: "Universality in the resurgence of generalized Tracy-Widom distributions"
section_id: sec-004-32-generic-relations
section_title: "Generic relations"
section_number: 3.2
pages: 4-5
source_pdf: 2509.20302v1.pdf
source_sha256: 59837f5b511c9e07
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.977
doc_brief: "Universality in the resurgence of generalized Tracy-Widom distributions — We analyze determinants associated with Bessel kernels and generic symbol functions, which govern a class of ob- servables"
---
For generic $\{x_{j}\}$ the non-perturbative corrections of order $e^{-8\pi gx_{j}}$ satisfy the same equations as for $x_{1}$, merely $x_{1}$ is replaced with $x_{j}$. Thus we can conclude that ${\cal D}^{\{j\}}\equiv{\cal D}^{\{0,\dots,0,1,0,\dots,\}}$ has the same form as ${\cal D}^{\{\}}$ but with $I_{n}^{\{j\}}=I_{n}^{\{\}}+\frac{2(-1)^{n}}{(2\pi x_{j})^{2n-1}}$. The corresponding Stokes constant is $$\begin{aligned}
S^{\{j\}} & =\frac{e^{i\pi\ell_{\beta}}}{4\pi x_{j}}\frac{\Phi(2i\pi x_{j})}{\Phi'(-2i\pi x_{j})}\\
 & =-ie^{i\pi\ell_{\beta}}\prod_{m\neq j}\frac{(x_{j}+x_{m})}{(x_{j}-x_{m})}\prod_{m}\frac{(x_{j}-y_{m})}{(x_{j}+y_{m})}
\end{aligned}$$ and the alien derivatives are $$\Delta_{j}{\cal D}^{\{\}}=-2S^{\{j\}}{\cal D}^{\{j\}}\ ;\quad\Delta_{j}^{2}{\cal D}^{\{\}}=0$$ We can think of ${\cal D}^{\{j\}}$ as the perturbative part corresponding to $\Phi^{\{j\}}$. Since $\Phi^{\{j\}}$ has no zero at $x_{j}$ (rather a pole there) we do not expect any singularity on the Borel plane at $x_{j}$ neither a non-perturbative correction at order $e^{-8\pi x_{j}g}$ or any higher multiple of them. Indeed, this is what we found by analysing the asymptotic behaviour of ${\cal D}_{k}^{\{j\}}$ as well as the analytic structure of ${\cal B}[{\cal D}^{\{j\}}](s)$ in many cases.

However, the non-perturbative corrections ${\cal D}^{\{j\}}$ will still have Borel singularities related to $x_{k}$ and its asymptotic behaviour indicates corrections of the form $e^{-8\pi x_{k}g}$. Since our argumentations work for generic $\{x_{1},\dots,x_{j},\dots\vert y_{1},y_{2},\dots\}$ it will also work for $\{x_{1},\dots,\hat{x}_{j},\dots\vert x_{j,}y_{1},y_{2},\dots\}$, where with the hat we indicated that $x_{j}$ is absent. Thus, following from the resurgence relations ([\[eq:asymrel\]](#eq:asymrel){reference-type="ref" reference="eq:asymrel"}), we can say that ${\cal D}^{\{j,k\}}\equiv{\cal D}^{\{0,\dots0,1,0,\dots,0,1,0,\dots\}}$ must have the same expansion as the perturbative part but with the replacements $I_{n}\to I_{n}^{\{j,k\}}$, where $$\begin{aligned}
I_{n}^{\{j,k\}} & =I_{n}^{\{j\}}+\frac{2(-1)^{n}}{(2\pi x_{k})^{2n-1}}=I_{n}^{\{k\}}+\frac{2(-1)^{n}}{(2\pi x_{j})^{2n-1}}
\end{aligned}$$ The corresponding Stokes constants are $$\begin{aligned}
S^{\{j,k\}} & =S^{\{j\}}S^{\{k\}}\frac{(x_{j}-x_{k})^{2}}{(x_{j}+x_{k})^{2}}
\end{aligned}$$ where the extra factor is due to the fact that we need to take $\frac{e^{i\pi\ell_{\beta}}}{4\pi x_{k}}\frac{\Phi^{\{j\}}(2i\pi x_{k})}{\Phi^{\{j\}\prime}(-2i\pi x_{k})}$ rather than the same expression with $\Phi$, which defines $S^{\{k\}}$. Observe that the result does not depend on which order we take the non-perturbative corrections. Stating in a different manner $$\Delta_{j}\Delta_{k}{\cal D}^{\{\}}=\Delta_{k}\Delta_{j}{\cal D}^{\{\}}$$

Repeating the same procedure further we can see that ${\cal D}^{\{j_{1},\dots,j_{n}\}}$ has exactly the same expansion as ${\cal D}^{\{\}}$, but we have to replace $I_{n}$ with $I_{n}^{\{j_{1},\dots,j_{n}\}}$, which is obtained from $I_{n}$ by flipping the signs of $x_{j_{k}}$s $$I_{n}^{\{j_{1},\dots,j_{l}\}}=I_{n}+\sum_{k=1}^{l}\frac{2(-1)^{n}}{(2\pi x_{j_{k}})^{2n-1}}$$ Similarly, the Stokes constants are $$S^{\{j_{1},\dots,j_{l}\}}=\prod_{m}S^{\{j_{m}\}}\prod_{m<n}\frac{(x_{j_{m}}-x_{j_{n}})^{2}}{(x_{j_{m}}+x_{j_{n}})^{2}}$$ and the alien derivatives read as $$\Delta_{k}{\cal D}^{\{j_{1},\dots,j_{l}\}}=-2\frac{S^{\{k,j_{1},\dots,j_{l}\}}}{S^{\{j_{1},\dots,j_{l}\}}}{\cal D}^{\{k,j_{1},\dots,j_{l}\}}$$ from which it follows that different alien derivatives commute $\Delta_{j}\Delta_{k}{\cal D}^{\{j_{1},\dots,j_{l}\}}=\Delta_{k}\Delta_{j}{\cal D}^{\{j_{1},\dots,j_{l}\}}$. It is also true that $\Delta_{k}^{2}{\cal D}^{\{j_{1},\dots,j_{l}\}}=0$.

By slightly changing the normalization of the expansion function $$S^{\{\delta_{j}\}}{\cal D}^{\{\delta_{j}\}}(g)=\prod_{j}(S^{\{j\}})^{\delta_{j}}\bar{{\cal D}}^{\{\delta_{j}\}}$$ the determinant can be formulated as an infinite parameter trans-series $$\begin{aligned}
{\cal D}(g,\{\sigma\})=A & e^{4\pi g\sum_{i}(x_{i}-y_{i})}g^{\frac{\beta^{2}+2\ell\beta}{2}}\times\\
 & \quad\sum_{\{\delta_{i}=0,1\}}e^{-8\pi g\sum_{i}\delta_{i}x_{i}}(\prod_{i}\sigma_{i}^{\delta_{i}})\bar{{\cal D}}^{\{\delta_{i}\}}(g)\nonumber 
\end{aligned}$$ Since the alien derivaties are proportional to derivatives wrt. the trans-series parameters $\Delta_{j}{\cal D}(g,\{\sigma\})=-2\partial_{\sigma_{j}}{\cal D}(g,\{\sigma\})$ the Stokes automorphism, which connects the two lateral resummations, shifts the trans-series parameters as $\sigma_{j}\to\sigma_{j}+2S^{\{j\}}$, and the median resummation provides the physical answer: $\sigma_{j}=S^{\{j\}}$.
