---
doc_id: arxiv-1303.6444v3
doc_title: "VIRIAL EXPANSION BOUNDS"
section_id: sec-006-52-morais-procacci-bound
section_title: "Morais-Procacci Bound"
section_number: 5.2
pages: 7-8
source_pdf: 1303.6444v3.pdf
source_sha256: 4f12ace2197f70ca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.906
latex_coverage_ratio: 0.975
doc_brief: "VIRIAL EXPANSION BOUNDS — In the 1960s, the technique of using cluster expansion bounds in order to achieve bounds on the virial expansion was developed by Lebowitz and Penrose (1964) and Ruelle"
---
This is an alternative derivation of the Morais-Procacci bounds using the method outlined in Section [\[sec: general\]](#sec: general){reference-type="ref" reference="sec: general"}.

In the recent paper [@MP13], Morais and Procacci obtain a bound for the virial coefficients via the Canonical Ensemble, using polymer expansion methods and the bounds for cluster coefficients, in the form: $$|nb_n| \leq \frac{n^{n-1}}{n!}e^{2\beta B(n-2)}C(\beta)^{-1}$$

The values $a=C(\beta)^{-1}e^{-4\beta B}$; $b=e^{2 \beta B}C{\beta}$; and thus $ab=e^{-2\beta B}$ are substituted into [\[reqn\]](#reqn){reference-type="eqref" reference="reqn"}, so that we get: $$r(s)=s(e^{-s}(1+e^{- 2\beta B})C(\beta)^{-1}e^{-2 \beta B}-C(\beta)^{-1}e^{-4\beta B}) \label{proceqn}$$ If we let $u=e^{2\beta B}$, then our equation becomes: $$r(s)=C(\beta)^{-1}\frac{1}{u}s(e^{-s}(1+\frac{1}{u})-\frac{1}{u}) \label{uform}$$ We reiterate the remark that $s \in (0, \ln (1+u))$ so that we change variables (monotonically) to $s = \ln (1+u(1-e^{-\alpha}))$, so that:

$$\begin{aligned}
\tilde{r}(\alpha)&=\frac{1}{C(\beta)u}\left(\ln(1+u(1-e^{-\alpha}))\left(\frac{u+1}{u(1+u(1-e^{-\alpha}))}-\frac{1}{u}\right)\right) \label{tildeeqn} \\
&=  \frac{1}{C(\beta)u} \frac{\ln(1+u(1-e^{-\alpha}))}{e^{\alpha}(1+u(1-e^{-\alpha}))}
\end{aligned}$$ This then gives us the bound for $|\rho|$ as: $$|\rho| \geq C(\beta)^{-1}\max_{\alpha \in (0, \infty)} \frac{\ln(1+u(1-e^{-\alpha}))}{ue^{\alpha}(1+u(1-e^{-\alpha}))} \label{alphabeta}$$ If we then follow the same argument before, we get the bound for the virial coefficient as: $$|c_n| \leq \frac{\beta^{-1}}{n}C(\beta)^{n-1} (\mathcal{F}(u))^{-(n-1)}$$ where $\mathcal{F}(u)=\max_{a \in (0, \infty)} \frac{\ln(1+u(1-e^{-\alpha}))}{ue^{\alpha}(1+u(1-e^{-\alpha}))}$.

The main improvement in the paper comes from better techniques of approximating virial coefficients. Using techniques involving Canonical Ensemble calculations for free energy and its relationship as the Legendre transform of pressure, they obtain slightly better bounds on the virial coefficients, although still under the proviso that $|\rho| \leq \rho^*$, where $\rho^*$ is the radius of convergence in [\[firstbound\]](#firstbound){reference-type="eqref" reference="firstbound"}. The improved estimates for the coefficients seem to imply that there may be a way of extending the radius of convergence, at least for temperatures for which the bound on the coefficient is an improvement. They obtain bounds on the coefficient of $\rho^{k+1}$ in the free energy as: $$\left( \frac{1}{k+1}+(e^{\alpha^*_{\beta}}-1)e^{\alpha^*_{\beta}k}\right)e^{2\beta B(k-1)}\frac{(k+1)^k}{k!}C(\beta)^k$$ where $\alpha^*_{\beta}$ is the optimal $\alpha$ from [\[alphabeta\]](#alphabeta){reference-type="eqref" reference="alphabeta"}. This leads to the (better) asymptotic bound for the virial coefficients as: $$K\left(\frac{e^{2\beta B}C(\beta)}{0.24026}\right)^k$$where $K$ is a constant.
