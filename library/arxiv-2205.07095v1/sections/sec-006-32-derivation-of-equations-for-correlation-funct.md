---
doc_id: arxiv-2205.07095v1
doc_title: "Virial Expansions for Correlation Functions in Canonical Ensemble"
section_id: sec-006-32-derivation-of-equations-for-correlation-funct
section_title: "Derivation of equations for correlation functions."
section_number: 3.2
pages: 6-8
source_pdf: 2205.07095v1.pdf
source_sha256: 2ec6916399150e2d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.961
doc_brief: "Virial Expansions for Correlation Functions in Canonical Ensemble — The inﬁnite set of coupled integral nonlinear equations for correlation func- tions in the case of classical canonical ensemble is"
---
The correlation functions of the canonical ensemble of the system $N$ of particles in some limited volume $\Lambda$ in configuration $\eta=\{x_1,\ldots, x_m\}$ are determined by the sequence

$$\begin{aligned}
\label{corfCA-2}
\rho^{(N)}_{\Lambda}(\eta)\;:=\;\begin{cases}
 & 1,\;\;\text{at}\; \eta = \emptyset,\\
 & \varrho=\frac{N}{V}\;\;\text{at}\;\; |\eta|=1, V=\sigma(\Lambda),\\
 & 0,\;\text{at};|\eta|=m\;>\; N,
  \end{cases}
\end{aligned}$$ and for $2\leq m\leq N$, $$\label{corfCA-3}
\rho^{(N)}_{\Lambda}(\eta)\;:=\;\frac{1}{Z_\Lambda(\beta, N)}\int_{\Gamma^{(N-m)}_\Lambda}\frac{d\gamma}{(N-m)!}
 e^{-\beta U(\eta\cup\gamma)},$$

where $$\label{SSCA}
Z_{\Lambda}(\beta, N)\;=\;\frac{1}{N!}\int_{\Gamma^{(N)}_\Lambda}
e^{-\beta U(\gamma)}d\gamma,$$ and $\varrho$ is the density of the particles in the system.

To derive equation for correlation functions using lemma [\[lem2\]](#lem2){reference-type="ref" reference="lem2"} we write down the right hand part of [\[corfCA-3\]](#corfCA-3){reference-type="eqref" reference="corfCA-3"} by the integral [\[IL-P\]](#IL-P){reference-type="eqref" reference="IL-P"}: $$\label{corfCA1}
\rho^{(N)}_{\Lambda}(\eta)\;=\;\frac{1}{Z_{\Lambda}(\beta, N)}\int_{\Gamma_\Lambda}
e^{-\beta U(\eta\cup\gamma)}1\!\!1_{N-m}(\gamma)\lambda_\sigma(d\gamma), \;|\eta|\leq N,$$ where $$\begin{aligned}
\label{unit}
1\!\!1_{N-m}(\gamma)\;:=\;\begin{cases}
 &1,\; |\gamma|=N-m,\\
 & 0,\;|\gamma|\neq N-m.
  \end{cases}
\end{aligned}$$

Introduce a notation $\eta^{(\hat{x})}:=\eta\setminus\{x\}$. Let in configuration $\eta=\{x_1,..., x_m\}$ the coordinate $x_1$ such that, for which the following inequality is true: $$\label{St}
  W(x_1; \eta^{(\hat{x}_1)})=\sum_{k=2}^{m}\phi(|x_1-x_k|)\;\geq\;-B,\;B\geq 0 .$$ Then $$\label{SSCA}
  U(\eta\cup\gamma)=W(x_1; \eta^{(\hat{x}_1)})+W(x_1; \gamma)+U(\eta^{(\hat{x}_1)}\cup\gamma)$$ and $$\label{corf6}
 e^{-\beta W(x_1;\gamma)}=\prod_{y\in\gamma}\left[(e^{-\beta\phi(|x_1-y|)}-1)+1\right]=\sum_{\xi\subseteq\gamma}K(x_1;\xi),$$ where $$\begin{aligned}
\label{corf7}
K(x_1;\xi)\;:=\;\begin{cases}
 &\prod_{y\in\xi}(e^{-\beta\phi(|x_1-y|)}-1),|\xi|\geq 1,\\
 & 1,\;\xi=\emptyset.
  \end{cases}
\end{aligned}$$ Then $$\begin{aligned}
\label{corfCA12-1}
\rho^{(N)}_{\Lambda}(\eta)\;=\;&\frac{e^{-\beta W(x_1; \eta^{(\hat{x}_1)})}}{Z_{\Lambda}(\beta, N)}\int_{\Gamma_\Lambda}
e^{-\beta U(\eta^{(\hat{x}_1)}\cup\gamma)} \times\notag\\
&\times1\!\!1_{N-m}(\gamma)\sum_{\xi\subseteq\gamma}K(x_1;\xi)1\!\!1_{\Lambda}(\gamma\setminus\xi)\lambda_\sigma(d\gamma).
\end{aligned}$$ Apply to the integral in [\[corfCA12-1\]](#corfCA12-1){reference-type="eqref" reference="corfCA12-1"} the lemma [\[lem2\]](#lem2){reference-type="ref" reference="lem2"} with $$\label{GH1}
   G(\gamma)=e^{-\beta U(\eta^{(\hat{x}_1)}\cup\gamma)}1\!\!1_{N-m}(\gamma)\;\;\text{and}\;\;H(\xi;\gamma\setminus\xi)= K(x_1;\xi)1\!\!1_{\Lambda}(\gamma\setminus\xi).$$ Then $$\begin{aligned}
\label{corfCA14}
\rho^{(N)}_{\Lambda}(\eta)\;&=\;\frac{e^{-\beta W(x_1; \eta^{(\hat{x}_1)})}}{Z_{\Lambda}(\beta, N)}\int_{\Gamma_\Lambda}\int_{\Gamma_\Lambda}
e^{-\beta U(\eta^{(\hat{x}_1)}\cup\xi\cup\gamma)} \times\notag\\
&\times1\!\!1_{N-m}(\xi\cup\gamma)K(x_1;\xi)1\!\!1_{\Lambda}(\gamma)\lambda_\sigma(d\gamma)\lambda_\sigma(d\xi).
\end{aligned}$$ Rewrite the right hand side in the following way $$\begin{aligned}
\label{corfCA13}
&\rho^{(N)}_{\Lambda}(\eta)=e^{-\beta W(x_1; \eta^{(\hat{x}_1)})}\frac{Z_{\Lambda}(\beta, N-1)}{Z_{\Lambda}(\beta, N)}\int_{\Gamma_\Lambda}K(x_1;\xi)\times\\
&\times\left[\frac{1}{Z_{\Lambda}(\beta, N-1)}\int_{\Gamma_\Lambda}e^{-\beta U(\eta^{(\hat{x}_1)}\cup\xi\cup\gamma)} 1\!\!1_{N-m-|\xi|}(\gamma) \lambda_\sigma(d\gamma)\right]\lambda_\sigma(d\xi).\notag
\end{aligned}$$ Taking into account [\[corfCA1\]](#corfCA1){reference-type="eqref" reference="corfCA1"}($N-m-|\xi|= N-1-(m-1+|\xi|)$) we obtain: $$\label{corfCA123}
 \rho^{(N)}_{\Lambda}(\eta)= e^{-\beta W(x_1; \eta^{(\hat{x}_1)})} a_N^\Lambda
 \int_{\Gamma_\Lambda}K(x_1;\xi)\rho^{(N-1)}_{\Lambda}(\eta^{(\hat{x}_1)}\cup\xi)\lambda_\sigma(d\xi),$$ where $|\eta|=m$$\eta=\{x_1,..., x_m\}$, $1<m<N$, and $$\label{coef}
 a_N^\Lambda\;=\; \frac{Z_{\Lambda}(\beta, N-1)}{Z_{\Lambda}(\beta, N)}.$$

For $m=1$ $$\label{I-1}
 \rho^{(N)}_{\Lambda}(\{x_1\})=\frac{N}{V}=a_N^\Lambda
 \int_{\Gamma_\Lambda}K(x_1;\xi)\rho^{(N-1)}_{\Lambda}(\xi)\lambda_{\sigma}(d\xi),\;\;V=\sigma(\Lambda).$$

Note, also, that $$\label{I-2-3}
\rho^{(N)}_\Lambda(\eta)= 0, \;\;\text{if}\;\;  |\eta|\;\geq\;N.$$ In the thermodynamic limit $$\label{lim}
\Lambda\uparrow\Bbb R^d,\;\;\lim_{\substack{V\rightarrow\infty \\
N\rightarrow\infty}}\frac{V}{N}=v,\;\;\frac{1}{v}=\varrho,$$ existing of which was proved in [@BPH69] we have the following equation $$\label{limeq}
 \rho(\eta)\;=\;\varrho a(\varrho) e^{-\beta W(x_1; \eta^{(\hat{x}_1)})}
 \int_{\Gamma_0}K(x_1;\xi)\rho(\eta^{(\hat{x}_1)}\cup\xi)\lambda_{\sigma}(d\xi),$$ where $$\label{ratioPF}
\lim_{\substack{V=N/\varrho \\
N\rightarrow\infty}}\frac{Z_\Lambda(\beta, N-1)}{Z_\Lambda(\beta, N)}\;=\;\varrho a(\varrho),\;\;V=\sigma(\Lambda)$$ and $$\label{ratioPF1}
 a(\varrho)=\frac{1}{\widetilde{Q}(\rho)}, \;\widetilde{Q}(\rho)\;=\;\int_{\Gamma_0}K(x_1;\xi)\rho(\xi)\lambda_{\sigma}(d\xi).$$
