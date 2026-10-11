---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-022-56-convergence-of-densities-in-probability
section_title: "Convergence of densities, in probability."
section_number: 5.6
pages: 39-41
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Y oung diagrams which can be regarded as a natural one-parameter deformation of so me classi- cal Y"
text_source: latex
latex_prose_ratio: 0.892
latex_coverage_ratio: 0.967
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

## Back to Young diagrams.

The function $\omega_{\Lambda_\infty}$ which was promised in the formulation of [\[theo:lln\]](#theo:lln){reference-type="ref" reference="theo:lln"} is simply given by the relationship [\[eq:density\]](#eq:density){reference-type="eqref" reference="eq:density"} for the specific choice of $f_{\Lambda}:=f_{\Lambda_\infty}$, namely $$\omega_{\Lambda_\infty}(u):= 2 f_{\Lambda_\infty}(u) + |u|.$$

We just finished the proof of the fact that $\omega_{\Lambda_n}$ converges to $\omega_{\Lambda_\infty}$ in the supremum norm as $n
\to \infty$, in probability, thus the proof of [\[theo:lln\]](#theo:lln){reference-type="ref" reference="theo:lln"} is completed.

# Central Limit Theorem. Proof of [\[theo:clt\]](#theo:clt){reference-type="ref" reference="theo:clt"} {#sec:proof-of-CLTCLT}

::: proof
*Proof of [\[theo:clt\]](#theo:clt){reference-type="ref" reference="theo:clt"}.* In the light of [\[remark:theo:clt\]](#remark:theo:clt){reference-type="ref" reference="remark:theo:clt"} we shall investigate the cumulants of the form $$\kappa_\ell \left(Y_{i_1}, \dots, Y_{i_\ell}  \right)$$ for the random variables $(Y_k)$ given by [\[eq:my-random-variables-2\]](#eq:my-random-variables-2){reference-type="eqref" reference="eq:my-random-variables-2"}.

We start with the case $\ell\geq 2$. By [\[eq:fluctuations-around-infty\]](#eq:fluctuations-around-infty){reference-type="eqref" reference="eq:fluctuations-around-infty"}, each $Y_k$ is equal (up to a deterministic shift) to the random variable $$X_k:= 
    
    \sqrt{n}\ \frac{k-1}{2} \int  u^{k-2} \ \omega_{\Lambda_n}(u) \dif u =
    n^{-\frac{k-1}{2}} \mathcal{S}_k(\lambda_n).$$

For $\ell\geq 2$ the cumulant $\kappa_\ell$ is translation-invariant; it follows therefore that $$\label{eq:cumulant-concrete}
    \kappa_\ell \left( Y_{i_1},\dots, Y_{i_\ell} \right)=
    \kappa_\ell \left( X_{i_1},\dots, X_{i_\ell} \right)=
    \kappa_\ell \left( {{n}^{-\frac{i_1-1}{2}}}\ \mathcal{S}_{i_1}, \dots, 
    {{n}^{-\frac{i_\ell-1}{2}}}\ \mathcal{S}_{i_\ell}    \right).$$

By [\[def:approx-factorization-charactersB\]](#def:approx-factorization-charactersB){reference-type="ref" reference="def:approx-factorization-charactersB"}[\[item:afp2\]](#item:afp2){reference-type="ref" reference="item:afp2"} the approximate factorization property of $(\chi_n)$ is equivalent to condition [\[item:cumulants-classic-polynomial\]](#item:cumulants-classic-polynomial){reference-type="ref" reference="item:cumulants-classic-polynomial"} which we apply in the special case when $(x_1,\dots,x_{\ell}):=(\mathcal{S}_{i_1},\dots,\mathcal{S}_{i_\ell})$. The latter implies that the right-hand side of [\[eq:cumulant-concrete\]](#eq:cumulant-concrete){reference-type="eqref" reference="eq:cumulant-concrete"} is of order

$O\left( {n}^{\frac{2-\ell}{2}} \right)$. This implies that for each $\ell\geq 3$ $$\lim_{n\to\infty} \kappa_\ell \left( Y_{i_1},\dots, Y_{i_\ell} \right) = 0.$$

Consider now the case $\ell=2$. If we adapt the above reasoning, we get that

the limit $$\lim_{n\to\infty} \kappa_2\left( Y_{i_1}, Y_{i_2} \right)$$ exists and is finite.

We consider now the case $\ell=1$. By [\[def:approx-factorization-charactersB\]](#def:approx-factorization-charactersB){reference-type="ref" reference="def:approx-factorization-charactersB"}[\[item:equivalent-enhanced\]](#item:equivalent-enhanced){reference-type="ref" reference="item:equivalent-enhanced"}, enhanced approximate factorization property implies that for each $k\geq 2$ there exist constants $a_k'', b_k''$ such that $${n^{- \frac{k}{2}}}\ 
    \mathbb{E}\mathcal{S}_k(\lambda_n) = a_k'' +
    \frac{b_k''+o(1)}{\sqrt{n}}$$ as $n\to\infty$.

It follows that the cumulant

$$\kappa_1(Y_k)=
    \mathbb{E}Y_k
    =
    
    
    
    \sqrt{n} \left({n^{- \frac{k}{2}}}\ \mathbb{E}
    \mathcal{S}_k(\lambda_n) - \lim_{m\to\infty} {m^{- \frac{k}{2}}}\ \mathbb{E}\mathcal{S}_k(\lambda_m) 
    \right)$$

converges as $n\to\infty$ to $b_k''$ (given explicitly by [\[eq:what-is-b-bis\]](#eq:what-is-b-bis){reference-type="eqref" reference="eq:what-is-b-bis"}).

Let us summarize the above discussion. We have proved that the limit $$\lim_{n\to\infty} \kappa_\ell \left( Y_{i_1},\dots, Y_{i_\ell} \right)$$ exists and is finite for any choice of $\ell \geq 1$ and $i_1,\dots,i_\ell \geq 2$. In other words: the joint distribution of the random variables $(Y_i)$ converges in moments as $n\to\infty$ to the joint distribution of an abstract family of random variables $(Z_i)$ with the property that all cumulants vanish: $\kappa_\ell \left( Z_{i_1},\dots, Z_{i_\ell} \right)=0$, except for $\ell\leq 2$. The latter is the defining property of the Gaussian distribution. Since the Gaussian distribution is uniquely determined by its moments, it follows that $(Y_i)$ converges to $(Z_i)$ not only in moments but also in the weak topology of probability measures, as required. ◻
:::
