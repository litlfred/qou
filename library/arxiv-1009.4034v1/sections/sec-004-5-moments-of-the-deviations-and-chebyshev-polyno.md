---
doc_id: arxiv-1009.4034v1
doc_title: "KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES OF PARAMETER α = 1/2"
section_id: sec-004-5-moments-of-the-deviations-and-chebyshev-polyno
section_title: "Moments of the deviations and Chebyshev polynomials of the second kind"
section_number: 5
pages: 13-21
source_pdf: 1009.4034v1.pdf
source_sha256: 8f8d6d786b60c279
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.994
doc_brief: "KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES OF PARAMETER α = 1/2 — In this article, we show that Kerov’s central limit theorem related to the ﬂuctuations of Young diagrams under the"
---
[]{#core label="core"} To make appear the Chebyshev polynomials of the second type, we start by computing the moments of the deviation $\Delta_{\lambda,c}$ of a rescaled Young diagram from its limit shape. If $\lambda$ is a partition of size $n$, let us denote by $\tilq_{k,c}(\lambda)$ the following quantity: $$\widetilde{q}_{k,c}(\lambda)=\frac{\widetilde{p}_{k+1}(\lambda)}{(k+1)\,n^{k/2}}-\sum_{l=1}^{\lfloor\frac{k+1}{2}\rfloor} \frac{k^{\downarrow 2l-1}}{(k+1-l)\,l!\,l-1!}\,c^{k+1-2l}\,n^{1/2}$$ Because of the factors $n^{-k/2}$ and $n^{1/2}$, $\widetilde{q}_{k,c}$ is not contained in $\obs$, but is rather in the localized ring $\obs^{+}=\obs[{\varSigma_{1}}^{-1/2}]$. In [@IO02], all the computations are done in this ring of generalized observables, and using the so-called Kerov degree; as we shall see here, this complicated framework is not at all required for the asymptotic analysis of fluctuations of Plancherel ($c=0$) and Schur-Weyl ($c>0$) measures.

::: lemma
[]{#moment label="moment"} Let $\lambda$ be a partition of size $n$, and let us define the deviation $\Delta_{\lambda,c}$ by $\Delta_{\lambda,c}(s)=\lambda^{*}(s)-\Omega_{c}(s)$. Then, for any $k\geq 1$, $$\frac{\sqrt{n}}{2}\int_{\R}s^{k}\,\Delta_{\lambda,c}(s)\,ds=\frac{\tilq_{k+1,c}(\lambda)}{k+1}.$$
:::

::: proof
*Proof.* Notice that this lemma is the exact analogue of [@IO02 Proposition 7.2]. Besides, the proof is exactly the same. Hence, by using the second part of Proposition [\[obslimitshape\]](#obslimitshape){reference-type="ref" reference="obslimitshape"}, one gets: $$\widetilde{q}_{k,c}(\lambda)=\frac{\sqrt{n}}{k+1}\left(\frac{\tilp_{k+1}(\lambda)}{n^{\frac{k+1}{2}}}-\tilp_{k+1}(\Omega_{c})\right)=\sqrt{n}\left(\frac{{\tilp_{k+1}(\lambda^{*})}-\tilp_{k+1}(\Omega_{c})}{k+1}\right)$$ Then, $\Delta_{\lambda,c}(s)=\lambda^{*}(s)-\Omega_{c}(s)=(\lambda^{*}(s)-|s|)-(\Omega_{c}(s)-|s|)$, so: $$\begin{aligned}
\frac{\sqrt{n}}{2}\int_{\R}s^{k}\,\Delta_{\lambda,c}(s)\,ds&=\sqrt{n} \left(\int_{\R}s^{k}\,\sigma_{\lambda^{*}}(s)\,ds-\int_{\R}s^{k}\,\sigma_{\Omega_{c}}(s)\,ds\right)\\
&=\frac{\sqrt{n}}{(k+1)(k+2)}\left(\int_{\R}s^{k+2}\,\sigma_{\lambda^{*}}''(s)\,ds-\int_{\R}s^{k+2}\,\sigma_{\Omega_{c}}''(s)\,ds\right)\\
&=\frac{\sqrt{n}}{(k+1)(k+2)}\big(\tilp_{k+2}(\lambda^{*})-\tilp_{k+2}(\Omega_{c})\big)=\frac{\tilq_{k+1,c}(\lambda)}{k+1}
\end{aligned}$$ ◻
:::

::: proposition
[]{#linearfunctional label="linearfunctional"} Let $p(s)$ be a polynomial in $s$. One chooses $\lambda\in \Part_{n}$ randomly according to the Schur-Weyl measure with parameters $\alpha=1/2$ and $c>0$. Then, $$\sqrt{n}\scal{p(s)}{\Delta_{\lambda,c}(s)}=\sqrt{n}\int_{\R}p(s)\,\Delta_{\lambda,c}(s)\,ds$$ converges in law towards a centered (gaussian) random variable.
:::

::: proof
*Proof.* The important part of Proposition [\[linearfunctional\]](#linearfunctional){reference-type="ref" reference="linearfunctional"} is actually the fact that the limit random variable exists and is centered, see the proof of Theorem [\[almosttheorem\]](#almosttheorem){reference-type="ref" reference="almosttheorem"} hereafter. Because of Theorem [\[sniadytheo\]](#sniadytheo){reference-type="ref" reference="sniadytheo"}, for any $l\geq 2$, $$\sqrt{n}\left(\frac{R_{l}(\lambda)}{n^{\frac{l}{2}}}-c^{l-2}\right)=\sqrt{n}\left(R_{l}(\lambda^{*})-R_{l}(\Omega_{c})\right)$$ converges towards a centered gaussian variable, and the result is also true when $l=1$ (in this case the variables are null for all $n$). Now, if $\mu=(\mu_{1},\ldots,\mu_{r})$ is a partition, then $$\sqrt{n}\left(R_{\mu}(\lambda^{*})-R_{\mu}(\Omega_{c})\right)=\sum_{i=0}^{r-1}R_{\mu_{1}\ldots\mu_{r-i-1}}(\lambda^{*})\,\left[\sqrt{n}\,(R_{\mu_{r-i}}(\lambda^{*})-R_{\mu_{r-i}}(\Omega_{c}))\right]\,R_{\mu_{r-i+1}\ldots\mu_{r}}(\Omega_{c}).$$ Because of Theorem [\[firstasymptotic\]](#firstasymptotic){reference-type="ref" reference="firstasymptotic"}, each $R_{\mu_{1}\ldots\mu_{r-i-1}}(\lambda^{*})$ converges towards the constant variable $R_{\mu_{1}\ldots\mu_{r-i-1}}(\Omega_{c})$, and on the other hand, each difference $\left[\sqrt{n}\,(R_{\mu_{r-i}}(\lambda^{*})-R_{\mu_{r-i}}(\Omega_{c}))\right]$ converges towards a centered gaussian variable. Moreover, for these differences of free cumulants $\sqrt{n}\,(R_{l}(\lambda^{*})-R_{l}(\Omega_{c}))$, one has in fact joint convergence in finite-dimensional laws towards a centered gaussian process. Consequently, the limit of $\sqrt{n}(R_{\mu}(\lambda^{*})-R_{\mu}(\Omega_{c}))$ is an element of a gaussian space whose variables are all centered: $$\forall \mu,\,\,\,\Delta_{n,c} (R_{\mu})=\sqrt{n}\,(R_{\mu}(\lambda^{*})-R_{\mu}(\Omega_{c})) \quad\longrightarrow \quad\mathcal{N}(0,(\sigma_{\mu,c})^{2})$$ In fact, the same argument as before shows that given a vector $(\Delta_{n,c}(R_{\mu^{(1)}}), \ldots, \Delta_{n,c}(R_{\mu^{(s)}}))$ of such fluctuations, one has a joint convergence towards a gaussian vector. Since the $R_{\mu}$'s form a linear basis of $\obs$, the same result holds for any vector $(\Delta_{n,c}(f^{(1)}),\ldots,\Delta_{n,c}(f^{(s)}))$ of scaled fluctuations of observables of diagrams: it converges in law towards a centered gaussian vector. As Lemma [\[moment\]](#moment){reference-type="ref" reference="moment"} ensures that $$\frac{\sqrt{n}}{2}\scal{s^{k}}{\Delta_{\lambda,c}(s)}=\frac{\Delta_{n,c}(\tilp_{k+2})}{(k+1)(k+2)},$$ our claim is proved. ◻
:::

::: lemma
[]{#transmoment label="transmoment"} With the same notations as in Lemma [\[moment\]](#moment){reference-type="ref" reference="moment"}, $$\begin{aligned}
&\frac{\sqrt{n}}{2}\int_{\R}(s-c)^{k}\,\Delta_{\lambda,c}(s)\,ds=\\
&\frac{\sqrt{n}}{(k+1)(k+2)}\left(\sum_{2 \leq l \leq k+2}\!\! \binom{k+2}{l} (-c)^{k+2-l}\,\frac{\widetilde{p}_{l}(\lambda)}{n^{l/2}}-\sum_{2 \leq 2m \leq k+2}\!\! \binom{k+2}{m} (-c)^{k+2-2m}\right)
\end{aligned}$$
:::

::: proof
*Proof.* Of course, one applies Newton's binomial theorem in order to expand the power $(s-c)^{k}$: $$\begin{aligned}
\frac{\sqrt{n}}{2}\scal{(s-c)^{k}}{\Delta_{\lambda,c}(s)}&=\sum_{l=0}^{k}\binom{k}{l}(-c)^{k-l}\,\frac{\sqrt{n}}{2}\int_{\R}s^{l}\,\Delta_{\lambda,c}(s)\,ds=\frac{1}{k+1}\sum_{l=0}^{k}\binom{k+1}{l+1}(-c)^{k-l}\,\tilq_{l+1,c}(\lambda)\\
&=\frac{1}{k+1}\sum_{l=1}^{k+1}\binom{k+1}{l}(-c)^{k+1-l}\,\tilq_{l,c}(\lambda)\\
&=\left(\frac{\sqrt{n}}{(k+1)(k+2)}\sum_{l=2}^{k+2}\binom{k+2}{l}(-c)^{k+2-l}\,\frac{\tilp_{l}(\lambda)}{n^{l/2}}\right)-\sqrt{n}\,A(c)
\end{aligned}$$ where $A(c)$ is the following quantity (one just uses the definition of $\tilq_{l,c}(\lambda)$): $$\begin{aligned}
A(c)&=\sum_{m=1}^{\lfloor \frac{k}{2}\rfloor +1} \sum_{l=2m-1}^{k+1} \frac{k!}{k+1-l!\,l-2m+1!\,m!\,m-1!\, (l+1-m)}\,(-1)^{k+1-l}c^{k+2-2m} \\
&=\sum_{m=0}^{\lfloor \frac{k}{2}\rfloor} \frac{k!}{k-2m!\,m!\,m+1!}\left\{\sum_{u=0}^{k-2m} \binom{k-2m}{u}\,\frac{(-1)^{k-u-2m}}{u+m+1}\right\}c^{k-2m}
\end{aligned}$$ The term between brackets can be computed by writing $\frac{1}{u+m+1}=\int_{0}^{1} x^{u+m}\,dx$. So, $$\begin{aligned}
\sum_{u=0}^{k-2m} \binom{k-2m}{u}\,\frac{(-1)^{k-u-2m}}{u+m+1}&=\int_{0}^{1} \sum_{u=0}^{k-2m} \binom{k-2m}{u}\,(-1)^{k-u-2m}\,x^{u+m}\,dx\\
&=\int_{0}^{1}x^{m}\,(x-1)^{k-2m}\,dx=(-1)^{k-2m}\,\frac{k-2m!\,m!}{k-m+1!}
\end{aligned}$$ and consequently, $A(c)=\sum_{m=0}^{\lfloor \frac{k}{2}\rfloor} \frac{k!}{k-m+1!\,m+1!}\,(-c)^{k-2m}=\frac{1}{(k+1)(k+2)}\sum_{m=0}^{\lfloor \frac{k}{2}\rfloor} \binom{k+2}{m+1}\,(-c)^{k-2m}$, whence the formula announced. ◻
:::

In the following, we denote by $U_{k}(s)$ the Chebyshev polynomial of the second kind renormalized so that $U_{k}(2\cos\theta)=\frac{\sin (k+1)\theta}{\sin \theta}$. These polynomials satisfy the relation $$U_{k+2}(X)=X\,U_{k+1}(X)-U_{k}(X),$$ and the first values are $U_{0}(X)=0$, $U_{1}(X)=X$, $U_{2}(X)=X^{2}-1$, $U_{3}(X)=X^{3}-2X$ and $U_{4}(X)=X^{4}-3X^{2}+1$. The end of this paragraph is devoted to the proof of the following theorem:

::: theorem
[]{#almosttheorem label="almosttheorem"} For any non-negative integer $k$, $\frac{\sqrt{n}}{2}\scal{U_{k}(s-c)}{\Delta_{\lambda}(s)}$ is equal to $$\frac{1}{k+1}\sum_{l=0}^{k-1}\binom{k+1}{l}(-c)^{l}\,X_{k+1-l}(\lambda),$$ plus some observables that under Schur-Weyl measures of parameter $1/2$ converge towards $0$ when $n$ goes to infinity.
:::

::: examples
Since the proof is quite tricky, we have found useful to include in our paper the complete computations for $k=0,1,2,3,4$ (one has to go up to $k=4$ to see all the tricks). In particular, this will make Lemma [\[nasty\]](#nasty){reference-type="ref" reference="nasty"} much more natural. One will use the relations between the $\tilp$'s and the $\varSigma$'s presented at the end of §[\[obs\]](#obs){reference-type="ref" reference="obs"}.

1.  Since $\Delta_{\lambda,c}(s)$ is the difference between two normalized continuous Young diagrams, $$\scal{U_{0}(s-c)}{\Delta_{\lambda,c}(s)}=\scal{1}{\Delta_{\lambda,c}(s)}=0,$$ and this agrees with the formula of Theorem [\[almosttheorem\]](#almosttheorem){reference-type="ref" reference="almosttheorem"}.

2.  $\scal{U_{1}(s-c)}{\Delta_{\lambda,c}(s)}=\scal{s-c}{\Delta_{\lambda,c}(s)}=\scal{s}{\Delta_{\lambda,c}(s)}$ can be computed by using Lemma [\[moment\]](#moment){reference-type="ref" reference="moment"}. Thus, $$\frac{\sqrt{n}}{2}\scal{U_{1}(s-c)}{\Delta_{\lambda,c}(s)}=\frac{\widetilde{q}_{2}(\lambda)}{2}=\frac{\widetilde{p}_{3}(\lambda)}{6n}-\frac{c\sqrt{n} }{2}=\frac{\sqrt{n}}{2}\left(\frac{\varSigma_{2}(\lambda)}{n^{3/2}}-c\right)=\frac{X_{2}(\lambda)}{2}.$$

3.  $\scal{U_{2}(s-c)}{\Delta_{\lambda,c}(s)}=\scal{(s-c)^{2}-1}{\Delta_{\lambda,c}(s)}=\scal{(s-c)^{2}}{\Delta_{\lambda,c}(s)}$ is the second translated moment of the deviation, so it can be computed thanks to Lemma [\[transmoment\]](#transmoment){reference-type="ref" reference="transmoment"}. $$\begin{aligned}
    \frac{\sqrt{n}}{2}\scal{U_{2}(s-c)}{\Delta_{\lambda,c}(s)}&=\frac{\sqrt{n}}{12}\left(\frac{\tilp_{4}(\lambda)}{n^{2}}-4c\frac{\tilp_{3}(\lambda)}{n^{3/2}}+6c^{2}\frac{\tilp_{2}(\lambda)}{n}-6-4c^{2}\right)\\
    &=\frac{\sqrt{n}}{12}\left(\frac{4\varSigma_{3}(\lambda)}{n^{2}}+\frac{6\varSigma_{1,1}(\lambda)}{n}+\frac{2}{n}-\frac{12c\varSigma_{2}(\lambda)}{n^{3/2}}+12c^{2}-6-4c^{2}\right)\\
    &=\frac{\sqrt{n}}{3}\left(\frac{\varSigma_{3}(\lambda)}{n^{2}}-c^{2}\right)-c\sqrt{n}\left(\frac{\varSigma_{2}(\lambda)}{n^{3/2}}-c\right)-\frac{1}{3n^{1/2}}\\
    &=\frac{X_{3}(\lambda)}{3}-cX_{2}(\lambda)-\frac{1}{3\sqrt{n}}
    \end{aligned}$$ Here, we've used the relation[^1] $\varSigma_{1,1}=(\varSigma_{1})^{2}-\varSigma_{1}$, and in general we shall use extensively the factorization of symbols $\varSigma_{\mu}$ in top homogeneous component.

4.  $\scal{U_{3}(s-c)}{\Delta_{\lambda,c}(s)}=\scal{(s-c)^{3}-2(s-c)}{\Delta_{\lambda,c}(s)}$ is the difference of the third translated moment, minus two times the first translated moment; this latter term will bring a contribution of $-X_{2}$. Then, by using again Lemma [\[transmoment\]](#transmoment){reference-type="ref" reference="transmoment"}, one sees that $\frac{\sqrt{n}}{2}\scal{(s-c)^{3}}{\Delta_{\lambda,c}(s)}$ is equal to $$\begin{aligned}
    &\frac{\sqrt{n}}{20}\left(\frac{\tilp_{5}(\lambda)}{n^{5/2}}-5c\frac{\tilp_{4}(\lambda)}{n^{2}}+10c^{2}\frac{\tilp_{3}(\lambda)}{n^{3/2}}-10c^{3}\frac{\tilp_{2}(\lambda)}{n}+10c+5c^{3}\right)\\
    &=\frac{\sqrt{n}}{20}\left(\frac{5\varSigma_{4}(\lambda)}{n^{5/2}}+\frac{20\varSigma_{2}(\lambda)}{n^{3/2}}-\frac{25\varSigma_{2}(\lambda)}{n^{5/2}}-\frac{20c\varSigma_{3}(\lambda)}{n^{2}}+\frac{20c}{n}+\frac{30c^{2}\varSigma_{2}(\lambda)}{n^{3/2}}-20c-15c^{3}\right)\\
    &=\frac{\sqrt{n}}{4}\left(\frac{\varSigma_{4}(\lambda)}{n^{5/2}}-c^{3}\right)-c\sqrt{n}\left(\frac{\varSigma_{3}(\lambda)}{n^{2}}-c^{2}\right)+\left(\frac{3c^{2}\sqrt{n}}{2}+\sqrt{n}\right)\left(\frac{\varSigma_{2}(\lambda)}{n^{3/2}}-c\right)+\frac{c}{\sqrt{n}}-\frac{5\varSigma_{2}(\lambda)}{4n^{2}}\\
    &=\frac{X_{4}(\lambda)}{4}-cX_{3}(\lambda)+\frac{3c^{2}X_{2}(\lambda)}{2}+X_{2}(\lambda)+\frac{c}{\sqrt{n}}-\frac{5\varSigma_{2}(\lambda)}{4n^{2}}.
    \end{aligned}$$ Again, we have used the relation $\varSigma_{2,1}=\varSigma_{2}\,\varSigma_{1}-2\varSigma_{2}$. By adding the contribution $-X_{2}(\lambda)$, one recovers the formula of Proposition [\[almosttheorem\]](#almosttheorem){reference-type="ref" reference="almosttheorem"}, because $\varSigma_{2}(\lambda)=O(n^{3/2})$ under a Schur-Weyl measure, and as a consequence $-5\varSigma_{2}(\lambda)/4n^{2}=O(n^{-1/2}) \to 0$. In the general case, we shall use the weight filtration on observables to neglict some terms: indeed, for any observable $f$, the order of magnitude is a $O(n^{\wt(f)/2})$, so one can for instance neglict terms of the kind $f/n^{k/2}$ with $k>\wt(f)$. Notice that there are some other simplifications in the calculation of $\scal{(s-c)^{3}}{\Delta_{\lambda,c}(s)}$; essentially, they are due to Lemma [\[linearfunctional\]](#linearfunctional){reference-type="ref" reference="linearfunctional"} that ensures that the mean of a scaled fluctuation is asymptotically equal to zero.

5.  Finally, another kind of trick has to be used in order to compute $\scal{U_{4}(s-c)}{\Delta_{\lambda,c}(s)}$, and this is due to the appearance of a term $\varSigma_{2,2}$ in the expansion of $\tilp_{6}$ in the basis of central characters. Because of Lemma [\[transmoment\]](#transmoment){reference-type="ref" reference="transmoment"}, $\frac{\sqrt{n}}{2}\scal{(s-c)^{4}}{\Delta_{\lambda,c}(s)}$ is equal to $$\begin{aligned}
    &\frac{\sqrt{n}}{30}\left(\frac{\tilp_{6}(\lambda)}{n^{3}} - 6c\frac{\tilp_{5}(\lambda)}{n^{5/2}}+15c^{2}\frac{\tilp_{4}(\lambda)}{n^{2}}-20c^{3}\frac{\tilp_{3}(\lambda)}{n^{3/2}}+15c^{4}\frac{\tilp_{2}(\lambda)}{n}-20-15c^{2}-6c^{4}\right)\\
    &=\frac{\sqrt{n}}{30}\left(\frac{6\varSigma_{5}(\lambda)}{n^{3}}+\frac{30\varSigma_{3}(\lambda)}{n^{2}}-\frac{90\varSigma_{3}(\lambda)}{n^{3}}+\frac{15(\varSigma_{2}(\lambda))^{2}}{n^{3}}-\frac{60}{n}+\frac{42}{n^{2}}\right.\\
    &\left.-\frac{30c\varSigma_{4}(\lambda)}{n^{5/2}}-\frac{120c\varSigma_{2}(\lambda)}{n^{3/2}}+\frac{150c\varSigma_{2}(\lambda)}{n^{5/2}} +\frac{60c^{2}\varSigma_{3}(\lambda)}{n^{2}}-\frac{60c^{2}}{n}-\frac{60c^{3}\varSigma_{2}(\lambda)}{n^{3/2}}+75c^{2}+24c^{4}\right)
    \end{aligned}$$ In order to simplify the calculations, we have used the relations $\varSigma_{1,1,1}=(\varSigma_{1})^{3}-3(\varSigma_{1})^2+2\varSigma_{1}$, $\varSigma_{3,1}=\varSigma_{3}\,\varSigma_{1}-3\varSigma_{3}$ and $\varSigma_{2,2}=(\varSigma_{2})^{2}-4\varSigma_{3}-2(\varSigma_{1})^{2}+2\varSigma_{1}$. Now, the new trick consists in writing: $$\frac{(\varSigma_{2}(\lambda))^{2}}{n^{3}}=\left(\frac{\varSigma_{2}(\lambda)}{n^{3/2}}\right)^{2}=\left(\frac{\varSigma_{2}(\lambda)}{n^{3/2}}-c\right)^{2}+2c\left(\frac{\varSigma_{2}(\lambda)}{n^{3/2}}-c\right)+c^{2}=\frac{(X_{2}(\lambda))^{2}}{n}+2c\frac{X_{2}(\lambda)}{\sqrt{n}}+c^{2}$$ Multiplying by the factor $\sqrt{n}$, one sees that the term $(X_{2}(\lambda))^{2}/\sqrt{n}$ will disappear in the limit $n \to \infty$, because $X_{2}(\lambda)=O(1)$. So, the previous expression may be written as: $$\begin{aligned}
    &\frac{X_{5}(\lambda)}{5}-cX_{4}(\lambda)+\left(2c^{2}+1\right)X_{3}(\lambda)-(3c+2c^{3})X_{2}(\lambda)\\
    &+\frac{(X_{2}(\lambda))^{2}}{2\sqrt{n}}+\frac{5c\varSigma_{2}(\lambda)}{n^{2}}-\frac{3\varSigma_{3}(\lambda)}{n^{5/2}}-\frac{2+2c^{2}}{\sqrt{n}}+\frac{7}{5n^{3/2}}
    \end{aligned}$$ If one adds $\frac{\sqrt{n}}{2}\scal{-3(s-c)^{2}+1}{\Delta_{\lambda,c}(s)}$ in order to obtain $\frac{\sqrt{n}}{2}\scal{U_{4}(s-c)}{\Delta_{\lambda,c}(s)}$, one finally gets $$\begin{aligned}
    &\frac{X_{5}(\lambda)}{5}-cX_{4}(\lambda)+2c^{2}X_{3}(\lambda)-2c^{3}X_{2}(\lambda)\\
    &+\frac{(X_{2}(\lambda))^{2}}{2\sqrt{n}}+\frac{5c\varSigma_{2}(\lambda)}{n^{2}}-\frac{3\varSigma_{3}(\lambda)}{n^{5/2}}-\frac{1+2c^{2}}{\sqrt{n}}+\frac{7}{5n^{3/2}}
    \end{aligned}$$ and every term on the second line can be neglicted when $n$ goes to infinity; on the other hand, the first line is precisely the formula of Theorem [\[almosttheorem\]](#almosttheorem){reference-type="ref" reference="almosttheorem"}.

Now, we certainly have enough numerical evidences in order to believe in Theorem [\[almosttheorem\]](#almosttheorem){reference-type="ref" reference="almosttheorem"}, and on the other hand, we also have a precise idea of the technicities needed for a general proof.
:::

::: lemma
[]{#idenpart label="idenpart"} For any positive integers $s\geq l$, $$\sum_{\substack{|\mu|=s\\ \ell(\mu)=l}}\frac{1}{\prod_{i \geq 1}m_{i}(\mu)!}=\frac{1}{l!}\,\binom{s-1}{l-1}.$$ Similarly, given (random) variables $Y_{p\geq 1}$, one has $$\sum_{\substack{|\mu|=s\\ \ell(\mu)=l}}\frac{1}{\prod_{i \geq 1}m_{i}(\mu)!}\left(\sum_{p \in \mu}Y_{p}\right)=\frac{1}{l-1!}\,\sum_{u=0}^{s-l} \binom{l-2+u}{u}\,Y_{s-l+1-u}.$$
:::

::: proof
*Proof.* The first formula is equivalent to $$\sum_{\substack{|\mu|=s\\ \ell(\mu)=l}}\binom{l}{m_{1}(\mu),\ldots,m_{s}(\mu)}=\binom{s-1}{l-1},$$ and both sides of this equation correspond to the number of $l$-uplets of positive integers $(s_{1},\ldots,s_{l})$ such that $s_{1}+\cdots+s_{l}=s$, so this is indeed true. As for the second formula, one sees that: $$\begin{aligned}
S_{2}&=\sum_{\substack{|\mu|=s\\ \ell(\mu)=l}}\frac{1}{\prod_{i \geq 1}m_{i}(\mu)!}\left(\sum_{p \in \mu}Y_{p}\right)=\sum_{\substack{|\mu|=s\\ \ell(\mu)=l}}\frac{1}{\prod_{i \geq 1}m_{i}(\mu)!}\left(\sum_{i=1}^{s-l+1}m_{i}(\mu)\,Y_{i}\right)\\
&=\sum_{\substack{|\mu|=s\\ \ell(\mu)=l}}\sum_{i=1}^{s-l+1}\frac{1}{\left(\prod_{\substack{j \geq 1\\ j \neq i}}m_{j}(\mu)!\right)\,(\max(0,m_{i}(\mu)-1))!}\,Y_{i}
\end{aligned}$$ because the biggest possible part of a partition of length $l$ and size $s$ is $s-l+1$. Then, by reverting the order of summation, one obtains: $$S_{2}=\sum_{i=1}^{s-l+1}Y_{i}\left(\sum_{\substack{|\mu|=s-i\\\ell(\mu)=l-1}} \frac{1}{\prod_{i \geq 1}m_{i}(\mu)!}\right)=\frac{1}{l-1!}\sum_{i=1}^{s-l+1}\binom{s-i-1}{l-2}\,Y_{i},$$ and this is exactly the second formula up to the change of index $u=s-l+1-i$. ◻
:::

::: lemma
[]{#nasty label="nasty"} Fix a parameter $c>0$, and a positive integer $k$. The scaled observable $\tilp_{k}(\lambda)/n^{\frac{k-1}{2}}$ is equal to $$\sqrt{n}\left(\sum_{l=1}^{\lfloor \frac{k}{2}\rfloor} \frac{k!}{(k-l)\,k-2l!\,l-1!\,l!}\,c^{k-2l }\right)+\sum_{l=1}^{\lfloor \frac{k}{2}\rfloor}\frac{k!}{k-l!\,l-1!} \left( \sum_{u=0}^{k-2l} \binom{l-2+u}{u}c^{u}\,X_{1+k-2l-u} \right),$$ plus a random variable $V_{k}(c)$ that under the Schur-Weyl measures $\mathrm{SW}_{n,1/2,c}$ converges in probability towards a constant $L_{k}(c)$ as $n$ goes to infinity.
:::

::: proof
*Proof.* Because of Proposition [\[changeofbasis\]](#changeofbasis){reference-type="ref" reference="changeofbasis"}, one can write $$\tilp_{k}=\left(\sum_{|\mu|+\ell(\mu)=k}\frac{k^{\downarrow \ell(\mu)}}{\prod_{i \geq 1}m_{i}(\mu)!} \prod_{i \geq 1}(\varSigma_{i})^{m_{i}}\right)+D_{k-1},$$ where $D_{k-1}$ is an observable of weight $k-1$. Let us decompose $D_{k-1}$ in the basis of free cumulants: $$D_{k-1}=\sum_{\substack{|\mu| \leq k-1\\ m_{1}(\mu)=0}}d_{\mu,k}\,R_{\mu}$$ Then, one knows that $R_{\mu}/n^{|\mu|/2}$ converges in probability towards $c^{|\mu|-2\ell(\mu)}$, so $V_{k}(c)=D_{k-1}/n^{\frac{k-1}{2}}$ converges in probability to $$L_{k}(c)=\sum_{\substack{|\mu|=k-1  \\ m_{1}(\mu)=0}} d_{\mu,k}\,c^{|\mu|-2\ell(\mu)}.$$ We won't need the precise value of $L_{k}(c)$, so let us focus on the remaining part $\tilp_{k}-D_{k-1}$. One uses the same trick as for the term $(\varSigma_{2})^{2}$ in the expansion of $\widetilde{p}_{6}/n^{5/2}$: $$\begin{aligned}
\frac{\tilp_{k}-D_{k-1}}{n^{\frac{k-1}{2}}}&=\sqrt{n}\left(\sum_{|\mu|+\ell(\mu)=k}\frac{k^{\downarrow \ell(\mu)}}{\prod_{i \geq 1}m_{i}(\mu)!} \prod_{i \geq 1}\left(\frac{\varSigma_{i}}{n^{\frac{i+1}{2}}}\right)^{m_{i}(\mu)}\right)\\
&=\sqrt{n}\left(\sum_{|\mu|+\ell(\mu)=k}\frac{k^{\downarrow \ell(\mu)}}{\prod_{i \geq 1}m_{i}(\mu)!} \prod_{i \geq 1}\left(\frac{X_{i}}{\sqrt{n}}+c^{i-1}\right)^{m_{i}(\mu)}\right)
\end{aligned}$$ With $\mu$ fixed, one expands the product $\prod_{i\geq 1}\left(\frac{X_{i}}{\sqrt{n}}+c^{i-1}\right)^{m_{i}(\mu)}$ ; the two leading terms are $$A(\mu)+\frac{B(\mu)}{\sqrt{n}}=c^{|\mu|-\ell(\mu)}+\frac{1}{\sqrt{n}}\sum_{p \in \mu} X_{p} \,c^{|\mu|-\ell(\mu)-p+1},$$ and the remainder is a $O(n^{-1})$. So, $$\frac{\tilp_{k}-D_{k-1}}{n^{\frac{k-1}{2}}}=\sqrt{n}\left(\sum_{|\mu|+\ell(\mu)=k}\frac{k^{\downarrow \ell(\mu)}\,A(\mu)}{\prod_{i \geq 1}m_{i}(\mu)!}\right) + \left(\sum_{|\mu|+\ell(\mu)=k}\frac{k^{\downarrow \ell(\mu)}\,B(\mu) }{\prod_{i \geq 1}m_{i}(\mu)!}\right)+ O(n^{-1/2}).$$ The first part is equal to $$\sqrt{n}\left(\sum_{l=1}^{\lfloor \frac{k}{2}\rfloor}\sum_{\substack{\mu \in \Part_{k-l}\\ |\mu|=l}} \frac{k!}{k-l!}
\,\frac{c^{k-2l }}{\prod_{i \geq 1}m_{i}(\mu)!}\right)=\sqrt{n}\left(\sum_{l=1}^{\lfloor \frac{k}{2}\rfloor} \frac{k!}{(k-l)\,k-2l!\,l-1!\,l!}\,c^{k-2l }\right)$$ because of the first part of Lemma [\[idenpart\]](#idenpart){reference-type="ref" reference="idenpart"}. As for the second part, we set $Y_{p}=X_{p}/c^{p-1}$ and we apply the second part of Lemma [\[idenpart\]](#idenpart){reference-type="ref" reference="idenpart"}, so we obtain $$\sum_{l=1}^{\lfloor \frac{k}{2}\rfloor} \sum_{\substack{\mu \in \Part_{k-l}\\ \ell(\mu)=l}}\sum_{p \in \mu}\frac{k!}{k-l!}\,\frac{c^{k-2l}\,Y_{p}}{{\prod_{i \geq 1}m_{i}(\mu)!}}=\sum_{l=1}^{\lfloor \frac{k}{2}\rfloor}\frac{k!}{k-l!\,l-1!} \left( \sum_{u=0}^{k-2l} \binom{l-2+u}{u}Y_{1+k-2l-u} \right) c^{k-2l}.$$ Since $Y_{1+k-2l-u}\,c^{k-2l}=X_{1+k-2l-u}\,c^{u}$, the proof is achieved. ◻
:::

::: lemma
Up to a random variable that converges in probability to zero under the Schur-Weyl measures $\mathrm{SW}_{n,1/2,c}$, the translated $k$-th moment of the deviation $\frac{\sqrt{n}}{2}\int_{\R}(s-c)^{k}\,\Delta_{\lambda,c}(s)\,ds$ is equal to $$\frac{1}{k+1}\sum_{l=0}^{k-1}\left(\sum_{m=0}^{\lfloor \frac{l}{2} \rfloor} \binom{k+1}{m}\binom{k+1-2m}{l-2m}\,(-c)^{l-2m}\right)X_{k+1-l}(\lambda).$$
:::

::: proof
*Proof.* Because of Lemma [\[transmoment\]](#transmoment){reference-type="ref" reference="transmoment"} and Lemma [\[nasty\]](#nasty){reference-type="ref" reference="nasty"}, the translated $k$-th moment of the deviation is the combination of the following terms: $$\begin{aligned}
A&=\sqrt{n}\,\left(\sum_{2\leq l \leq k+2}\sum_{m=1}^{\lfloor \frac{l}{2}\rfloor } \frac{k!}{(l-m)\,k+2-l!\,l-2m!\,m-1!\,m!}\,(-1)^{k+2-l}\, c^{k+2-2m}\,\right)\\
B&=\sum_{2\leq l \leq k+2}\sum_{m=1}^{\lfloor \frac{l}{2}\rfloor }\sum_{u=0}^{l-2m} \frac{k!}{k+2-l!\,l-m!\,m-1!}\binom{m-2+u}{u}(-1)^{k+2-l}\,c^{k+2-l+u}\,X_{1+l-2m-u}\\
C&=\sum_{2\leq l \leq k+2} \frac{k!}{l!\,k+2-l!}\,(-c)^{k+2-l}\,V_{l}(c)\\
D&=-\sqrt{n}\,\left(\sum_{2\leq 2m \leq k+2}\frac{k!}{m!\,k+2-m!}\,(-c)^{k+2-2m}\right)
\end{aligned}$$ In $A$, we revert the order of summation: $$\frac{A}{\sqrt{n}}=\sum_{2\leq 2m \leq k+2}\frac{k!}{m!\,k+2-2m!\,m-1!}(-c)^{k+2-2m}\left\{\sum_{l=2m}^{k+2}(-1)^{l}\frac{k+2-2m!}{(l-m)\,k+2-l!\,l-2m!}\right\}$$ The sum between brackets can be written as: $$\begin{aligned}
\sum_{u=0}^{k+2-2m}\binom{k+2-2m}{u}\frac{(-1)^{u}}{u+m}&=\int_{0}^{1}\left(\sum_{u=0}^{k+2-2m}\binom{k+2-2m}{u}(-x)^{u}\right)x^{m-1}\,dx\\
&=\int_{0}^{1}(1-x)^{k+2-2m}\,x^{m-1}\,dx=\frac{k+2-2m!\,m-1!}{k+2-m!}
\end{aligned}$$ Hence, $A+D=0$. Then, $B$ is asymptotically a centered gaussian variable, and $C$ converges towards $\sum_{2\leq l \leq k+2} \frac{k!}{l!\,k+2-l!}\,(-c)^{k+2-l}\,L_{l}(c)$. But because of Proposition [\[linearfunctional\]](#linearfunctional){reference-type="ref" reference="linearfunctional"}, the translated $k$-th moment of the deviation converges in law towards a centered gaussian variable, so $$\sum_{2\leq l \leq k+2} \frac{k!}{l!\,k+2-l!}\,(-c)^{k+2-l}\,L_{l}(c)=0$$ (this is why we did not need the precise values of the $L_{l}(c)$'s). Finally, one can simplify $B$ as follows. The index $1+l-2m-u$ takes its values in the interval $\lle 1,k+1\rre$, so $B$ can be written as a linear combination $\sum_{v=1}^{k+1} f(v,c)\,X_{v}$. Since $X_{1}=0$, one can actually take $v$ in $\lle 2,k+1 \rre$, so let us make the change of index $1+l-2m-u=k+1-x$ with $x \in \lle 0,k-1\rre$. Then, $$\begin{aligned}
 B&=\sum_{x=0}^{k-1}X_{k+1-x}\left(\sum_{\substack{k+2\geq l \geq 2m \geq 2\\l-2m\geq k-x}} \frac{(-1)^{k+2-l}\,c^{x-2m+2}\,k!\,l-m-k+x-2!}{k+2-l!\,l-m!\,m-1!\,m-2!\,l-2m-k+x!}\right)\\
 &=\sum_{x=0}^{k-1}X_{k+1-x}\left(\sum_{y=0}^{\lfloor\frac{x}{2}\rfloor} \sum_{z=0}^{x-2y} \frac{(-1)^{x-2y-z}\,c^{x-2y}\,k!\,y+z-1!}{y!\,y-1!\,z!\,k+1-x+y+z!\,x-2y-z!}\right)
 
\end{aligned}$$ with $y=m-1$ and $z=l-2m-k+x$. Then we use another hypergeometric identity $$\sum_{z=0}^{Z} \frac{\alpha+z!}{\beta+z!}\binom{Z}{z} (-1)^{z}= \frac{\alpha!\,\beta-\alpha+Z-1!}{\beta-\alpha-1!\,\beta+Z!}$$ that holds for any $\beta> \alpha$, and that can again be shown by using methods *à la* Wilf-Zeilberger, see [@PWZ97]. It implies that: $$\begin{aligned}
B&=\sum_{x=0}^{k-1}X_{k+1-x}\left(\sum_{y=0}^{\lfloor \frac{x}{2} \rfloor}\frac{(-c)^{x-2y}\,k!}{y!\,y-1!\,x-2y!}\sum_{z=0}^{Z=x-2y} \frac{y-1+z!}{y+k+1-x+z!}\binom{Z}{z}(-1)^{z}\right)\\
&=\sum_{x=0}^{k-1}X_{k+1-x}\left(\sum_{y=0}^{\lfloor \frac{x}{2} \rfloor}\frac{(-c)^{x-2y}\,k!\,k+1-2y!}{y!\,x-2y!\,k+1-x!\,k+1-y!}\right)\\
&=\frac{1}{k+1}\sum_{x=0}^{k-1}X_{k+1-x}\left(\sum_{y=0}^{\lfloor \frac{x}{2} \rfloor} \binom{k+1}{y}\binom{k+1-2y}{x-2y}\,(-c)^{x-2y}\right)
\end{aligned}$$ Notice that a slight abuse of notation has been made when considering expressions such as $y-1!$ with $y=0$; nethertheless, it can be checked that in the end our formal computation does give the exact result. ◻
:::

::: proof
*Proof of Theorem [\[almosttheorem\]](#almosttheorem){reference-type="ref" reference="almosttheorem"}.* The explicit expansion of $U_{k}(X)$ is $$U_{k}(X)=\sum_{m=0}^{\lfloor \frac{k}{2}\rfloor} (-1)^{m}\binom{k-m}{m}\,X^{k-2m}$$ see [@IO02 p. 33]. Moreover, given two set of variables $a_{0},a_{1},\ldots$ and $b_{0},b_{1},\ldots$, the following set of relations are equivalent $$\left\{b_{k}=\sum_{m=0}^{\lfloor\frac{k}{2} \rfloor}\binom{k}{m} \,a_{k-2m}\right\}_{\!k \geq 0}\quad\iff\quad\left\{a_{k}=\sum_{m=0}^{\lfloor\frac{k}{2} \rfloor}(-1)^{m}\,\frac{k}{k-m}\binom{k-m}{m} \,b_{k-2m}\right\}_{\!k\geq 0}$$ see [@IO02 p. 36]. We denote by $\frac{B_{k+1}}{k+1}$ the random variable computed in the previous lemma. Then, the linear functional of the deviation associated to the translated Chebyshev polynomial $U_{k}(s-c)$ is: $$\frac{\sqrt{n}}{2}\scal{U_{k}(s-c)}{\Delta_{\lambda,c}(s)}=\sum_{m=0}^{\lfloor \frac{k}{2} \rfloor} (-1)^{m} \binom{k-m}{m}\,\frac{B_{k+1-2m}}{k+1-2m}=\sum_{m=0}^{\lfloor \frac{k}{2} \rfloor} (-1)^{m} \binom{k+1-m}{m}\,\frac{B_{k+1-2m}}{k+1-m}$$ Since $B_{0}=B_{1}=0$, the index $m$ can in fact be taken up to $\lfloor \frac{k+1}{2}\rfloor$, so the expression is exactly $\frac{A_{k+1}}{k+1}$, where the $A$'s and the $B$'s are related as mentioned before. Consequently, it is sufficient to identify the random variables $A_{k}$ such that: $$\forall k,\,\,\,\sum_{l=0}^{k-1}\left(\sum_{m=0}^{\lfloor \frac{l}{2} \rfloor} \binom{k+1}{m}\binom{k+1-2m}{l-2m}\,(-c)^{l-2m}\right)X_{k+1-l}=\sum_{m=0}^{\lfloor \frac{k+1}{2}\rfloor} \binom{k+1}{m}\,A_{k+1-2m}$$ In the left-hand side, we revert the order of summation and thus obtain: $$\begin{aligned}
B_{k+1}&=\sum_{m=0}^{\lfloor \frac{k-1}{2}\rfloor}\binom{k+1}{m}\left(\sum_{l=2m}^{k-1}\binom{k+1-2m}{l-2m}\,(-c)^{l-2m}\,X_{k+1-l}\right)\\ 
&=\sum_{m=0}^{\lfloor \frac{k-1}{2}\rfloor}\binom{k+1}{m}\left(\sum_{l=0}^{k-1-2m}\binom{k+1-2m}{l}\,(-c)^{l}\,X_{k+1-2m-l}\right)\\
&=\sum_{m=0}^{\lfloor \frac{k+1}{2}\rfloor}\binom{k+1}{m}\left(\sum_{l=0}^{k-1-2m}\binom{k+1-2m}{l}\,(-c)^{l}\,X_{k+1-2m-l}\right)\quad\text{because }X_{0}=X_{1}=0.
\end{aligned}$$ As a consequence, $$A_{k+1}=\sum_{l=0}^{k-1}\binom{k+1}{l}\,(-c)^{l}\,X_{k+1-l},$$ and since $\frac{A_{k+1}}{k+1}=\frac{\sqrt{n}}{2}\scal{U_{k}(s-c)}{\Delta_{\lambda,c}(s)}$, the proof of Theorem [\[almosttheorem\]](#almosttheorem){reference-type="ref" reference="almosttheorem"} is completed. ◻
:::

[^1]: Such a relation can be obtained if one considers the symbols $\varSigma_{\mu}$ as elements of the algebra of partial permutations, see [@IK99]. As a consequence, any product of terms $\varSigma_{\mu}$ is a sum over certain partial matchings $M$ of symbols $\varSigma_{\rho(M)}$, see [@FM10 §3.3] for a precise statement.
