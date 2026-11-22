---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-018-41-convergence-of-power-sums
section_title: "Convergence of power sums"
section_number: 4.1
pages: 14-15
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.981
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
The $q$-Plancherel measure is a measure on Young diagrams, so the functions on Young diagrams and in particular the elements of $\mathscr{O}$ are in this context random variables. In particular we will denote by $\mathbb{E}$ their expectation. Thanks to the characterization of the $q$-Plancherel measure with the normalized trace (paragraph [\[subsect:qPlancherel_trace\]](#subsect:qPlancherel_trace){reference-type="ref" reference="subsect:qPlancherel_trace"}), one has immediately: $$\mathbb{E}[\varSigma_{\rho,q}] = \begin{cases}
                                n^{\downarrow k} & \text{if }\rho = 1^k ;\\
                0 & \text{else.}
                               \end{cases}$$ By using the triangular relation between the $\varSigma_{\rho}$ and the $\varSigma_{\nu,q}$, we obtain: $$\begin{aligned}
\mathbb{E}[\varSigma_{\rho}] &= \frac{1}{q^\rho-1}\,\sum_{\nu \in \mathscr{Y}_k} (q-1)^{\ell(\nu)}\,\left\langle m_\nu\vphantom{p_\rho}\,\right |\left.p_\rho \vphantom{m_\nu}\right\rangle\,\mathbb{E}[\varSigma_{\nu,q}]=\frac{(q-1)^{|\rho|}}{q^\rho-1}\,n^{\downarrow |\rho|}\,\left\langle m_{1^{|\nu|}}\vphantom{p_\rho}\,\right |\left.p_\rho \vphantom{m_{1^{|\nu|}}}\right\rangle \nonumber\\
\label{eq:esp_sigma} &=\frac{(1-q)^{|\rho|}}{1-q^\rho}\,n^{\downarrow|\rho|}
\end{aligned}$$

This gives in particular the asymptotic order of magnitude: $$\mathbb{E}[\varSigma_{\rho}] = O\big(n^{|\rho|}\big) = O\big(n^{\deg(\varSigma_{\rho})}\big)$$ In fact, this is true for any measure on Young diagrams, but is not always precise enough (for example, to study the usual Plancherel measure, one has to use the fact that it is $O(n^{(|\rho|+\ell(\rho))/2})$). In this context, the exact computation above shows that we could not find a better bound. As $(\varSigma_{\rho})_{\rho \in \mathscr{Y}}$ is a linear basis of $\mathscr{O}$, the previous estimate remains true for any element of $\mathscr{O}$.

::: lemma
[]{#lem:major_Ex_deg label="lem:major_Ex_deg"} For any $x \in \mathscr{O}$, one has $\mathbb{E}[x] = O(n^{\deg(x)})$.
:::

This lemma allows us to forget terms of lower degree when we want to look at the asymptotic behavior of the expectation of some observable. In particular, one can obtain the following result for the power sums of the Frobenius coordinates:

::: lemma
[]{#lem:cv_powersums label="lem:cv_powersums"} Under the $q$-Plancherel measures, we have convergence in probability of the renormalized power sums $p_k(\lambda)$: $$\forall k \geq 1,\,\,\frac{p_k(\lambda)}{|\lambda|^k} \longrightarrow_{M_{n,q}} \frac{(1-q)^k}{1-q^k}.$$
:::

::: proof
*Proof.* An immediate consequence of equation ([\[eq:esp_sigma\]](#eq:esp_sigma){reference-type="ref" reference="eq:esp_sigma"}) is that $\mathbb{E}[\varSigma_\rho]/n^{|\rho|} \to(1-q)^{|\rho|}/(1-q^\rho)$ when $n$ goes to infinity. But $\varSigma_\rho-p_\rho$ is an observable of degree less than $|\rho|-1$, so the same holds for $p_\rho$: $$\label{EqEquivPRho}
\lim_{n \to \infty} \frac{\mathbb{E}[p_\rho]}{n^{|\rho|}} = \frac{(1-q)^{|\rho|}}{1-q^\rho}$$ Fix $\varepsilon>0$ and $k \geq 1$. The Bienaymé-Chebyshev inequality ensures that $$\begin{aligned}
M_{n,q}\left[\left|\frac{p_k}{n^k} - \frac{(1-q)^k}{1-q^k}\right|\geq \varepsilon\right] &\leq\frac{1}{\varepsilon^2}\,\mathbb{E}\left[\left(\frac{p_k}{n^k} - \frac{(1-q)^k}{1-q^k}\right)^2\right]\\
&\leq\frac{1}{\varepsilon^2}\,\left(\frac{\mathbb{E}[p_{k,k}]}{n^{2k}} - 2 \,\frac{\mathbb{E}[p_k]}{n^k}\,\frac{(1-q)^k}{1-q^k} +\frac{(1-q)^{2k}}{1-q^{k,k}}\right).
\end{aligned}$$ But the right-hand side tends to $0$ (which is easily seen using equation [\[EqEquivPRho\]](#EqEquivPRho){reference-type="eqref" reference="EqEquivPRho"} for $\rho=(k)$ and $\rho=(k,k)$) and the proof is over. ◻
:::

::: corollary
[]{#corol:concentration_q-characters label="corol:concentration_q-characters"} Under the $q$-Plancherel measures, in probability,o ne has: $$\begin{aligned}
 &\forall \rho \in \mathscr{Y}, \,\, \frac{\varSigma_\rho}{n^{|\rho|}}  \longrightarrow_{M_{n,q}} \frac{(1-q)^{|\rho|}}{1-q^\rho}\quad   \text{  i.e. } \chi^\lambda(\rho)  \longrightarrow_{M_{n,q}} \frac{(1-q)^{|\rho|}}{1-q^\rho};\\ 
& \forall \rho \in \mathscr{Y},  \,\, \frac{\varSigma_{\rho,q}}{n^{|\rho|}}  \longrightarrow_{M_{n,q}} \delta_{\rho=1^{|\rho|}}\quad \quad  \text{ i.e. } \chi^\lambda(\rho,q)  \longrightarrow_{M_{n,q}}\delta_{\rho=1^{|\rho|}}.
\end{aligned}$$
:::

::: proof
*Proof.* It is a direct consequence of Proposition [\[prop:sigma_pk\]](#prop:sigma_pk){reference-type="ref" reference="prop:sigma_pk"} and Lemma [\[lem:cv_powersums\]](#lem:cv_powersums){reference-type="ref" reference="lem:cv_powersums"}. ◻
:::
