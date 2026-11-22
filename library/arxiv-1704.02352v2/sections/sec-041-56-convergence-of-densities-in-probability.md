---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-041-56-convergence-of-densities-in-probability
section_title: "Convergence of densities, in probability."
section_number: 5.6
pages: 39-40
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.897
latex_coverage_ratio: 0.94
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
We have proved that the sequence of random variables $(S_k^{[n]})_n$ converges (as $n\to\infty$) to $s_k$ in probability; in other words for each $\epsilon>0$ and each integer $k\geq 0$ $$\label{eq:moments-convergence}
\lim_{n\to\infty} \mathbb{P}\left( \left| \int u^{k} \dif P_{\Lambda_n}(u)
-  
\int u^{k} \dif P_{\Lambda_\infty}(u)
\right| >
\epsilon \right) =0;$$ in other words the sequence of random probability measures $P_{\Lambda_n}$ converges to the measure $P_{\Lambda_\infty}$ *in moments, in probability*.

The weak topology of probability measures can be metrized, for example by Lévy--Prokhorov distance $\pi$. Since the measure $P_{\Lambda_\infty}$ is uniquely determined by its moments, convergence to $P_{\Lambda_\infty}$ *in moments* implies convergence to the same limit *in the weak topology of probability measures*. With the help of the distances $d$ (cf. [\[sec:limit-measure-Plambdainfty\]](#sec:limit-measure-Plambdainfty){reference-type="ref" reference="sec:limit-measure-Plambdainfty"}) and $\pi$, the latter statement can be rephrased as follows: for each $\varepsilon>0$ there exists $\delta>0$ such that for any probability measure $\mu$ $$d(\mu, P_{\Lambda_\infty}) < \delta \implies 
\pi(\mu, P_{\Lambda_\infty}) < \varepsilon.$$ It follows that the sequence of random probability measures $P_{\Lambda_n}$ converges to the measure $P_{\Lambda_\infty}$ *in the weak topology of probability measures, in probability*, i.e. for each $\varepsilon>0$ $$\label{eq:Levy}
\lim_{n\to\infty} \mathbb{P}\left( \pi(P_{\Lambda_n}, P_{\Lambda_\infty})  >
\varepsilon \right) =0.$$

Let $\epsilon>0$; by adapting the proof of [\[eq:Lipschitz-is-good\]](#eq:Lipschitz-is-good){reference-type="eqref" reference="eq:Lipschitz-is-good"}, we get that $$\label{eq:weak-conv-implications1}
\left| f_{\Lambda_n}(u_0) - \int\ \phi_\epsilon(u)\ \dif  P_{\Lambda_n}(u) \right| 
\leq \epsilon.$$ Lévy--Prokhorov distance $\pi$ metrizes the weak convergence of probability measures; it follows that we can choose sufficiently small $\varepsilon>0$ with the property that for any probability measure $\mu$ on $\mathbb{R}$ $$\label{eq:weak-conv-implications2}
\pi(\mu, P_{\Lambda_\infty})\leq \varepsilon \implies 
\left| \int \phi_\epsilon(u) \dif \mu(u)-  \int \phi_\epsilon(u) \dif P_{\Lambda_\infty}(u) \right| <\epsilon.$$ Equation [\[eq:Levy\]](#eq:Levy){reference-type="eqref" reference="eq:Levy"} combined with [\[eq:weak-conv-implications2\]](#eq:weak-conv-implications2){reference-type="eqref" reference="eq:weak-conv-implications2"} as well as [\[eq:weak-conv-implications1\]](#eq:weak-conv-implications1){reference-type="eqref" reference="eq:weak-conv-implications1"} imply therefore that $$\lim_{n\to\infty} 
\mathbb{P} \left( \left| f_{\Lambda_n}(u_0) - \int \phi_\epsilon(u) \dif P_{\Lambda_\infty}(u) \right| > 2\epsilon
\right) = 0.$$ As $\epsilon\searrow 0$, the integral $\int \phi_\epsilon(u) \dif P_{\Lambda_\infty}(u)$ converges to the density $f_{\Lambda_\infty}(u_0)$ by an analogue of [\[eq:Lipschitz-is-good\]](#eq:Lipschitz-is-good){reference-type="eqref" reference="eq:Lipschitz-is-good"}. In this way we proved that *for each $u_0$ the sequence $f_{\Lambda_n}(u_0)$ converges to $f_{\Lambda_\infty}(u_0)$ in probability*.

By the same type of argument as in [\[eq:sup-bound\]](#eq:sup-bound){reference-type="eqref" reference="eq:sup-bound"} it follows that *the sequence of functions $f_{\Lambda_n}$ converges uniformly to $f_{\Lambda_\infty}$ in probability*, i.e. for each $\epsilon>0$ $$\lim_{n\to\infty} \mathbb{P} \left( \left\| f_{\Lambda_n} - f_{\Lambda_\infty} \right\|_{\infty} > \epsilon \right) = 0$$ with respect to the supremum norm.
