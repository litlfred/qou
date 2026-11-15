---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-031-78-the-local-asymptotics-for-the-weighted-bianal
section_title: "The local asymptotics for the weighted bianalytic Bergman kernel: the corrective algorithm II"
section_number: 7.8
pages: 28-31
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.949
---
[]{#subsec-II label="subsec-II"}

Here, we show how to combine the given criteria involving ${\mathbf S}$ and ${\mathbf S}'$ in a single criterion for $\Lfun_j^2$, which we explain for $j=0,1$.

We first observe first that [\[eq-4.13\'\]](#eq-4.13'){reference-type="eqref" reference="eq-4.13'"} and [\[eq-4.16.3\]](#eq-4.16.3){reference-type="eqref" reference="eq-4.16.3"} may be united in a single condition:

$${\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}+\frac{4}{\pi}
\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\in{\mathbf M}_{z-w}^2{\mathfrak R}_2.
\label{eq-2.05}$$ Second, we observe that [\[eq-4.14\]](#eq-4.14){reference-type="eqref" reference="eq-4.14"} and [\[eq-4.16.5\]](#eq-4.16.5){reference-type="eqref" reference="eq-4.16.5"} may be united in a single condition too: $$\begin{gathered}
{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{1}
+{\pmb{\partial}}_w{\pmb{\partial}}_\theta\bigg\{\frac12{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}+
\frac{2}{\pi}\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg\}
-\frac{4}{\pi}+\frac{2}{\pi}(\bar z-\bar w){\pmb{\partial}}_\theta\frac{1}{{\pmb{\partial}}_\theta\bar w}
\\
+{\mathbf M}_{z-w}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}^{-1}{\boldsymbol{\Big\lfloor}}
{\pmb{\partial}}_w{\pmb{\partial}}_\theta\boldsymbol{,}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}{\boldsymbol{\Big\rfloor}}
{\mathbf N}\bigg[\frac12{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}+\frac{2}{\pi}
\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg]\in{\mathbf M}_{z-w}^2{\mathfrak R}_2.
\label{eq-2.06}
\end{gathered}$$ Similar but more complicated statements apply for $j=2,3,4,\ldots$ as well. Finally, we observe that by Lemma [\[lem-uniq1\]](#lem-uniq1){reference-type="ref" reference="lem-uniq1"}, the condition [\[eq-2.05\]](#eq-2.05){reference-type="eqref" reference="eq-2.05"} determines $\Lfun^2_{0}$ uniquely, and as a consequence, the condition [\[eq-2.06\]](#eq-2.06){reference-type="eqref" reference="eq-2.06"} determines $\Lfun^2_{1}$ uniquely. Although in principle we are now set to obtain the concrete expressions for $\Lfun_j^2$, the computation is quite messy. For this reason, we show below how to proceed.

## The local asymptotics for the weighted bianalytic Bergman kernel: the corrective algorithm III {#subsec-III}

We continue the analysis of the corrective algorithm, with the aim to obtain concrete expressions for $\Lfun_j^2$, for $j=0,1,2$.

To simplify the notation, we shall at times write $$\lambda(z,w)=\lambda_Q(z,w):=\partial_z\bar\partial_w Q(z,w),
\label{eq-beta1}$$ and sometimes we abbreviate $\lambda=\lambda(z,w)$. The function $\lambda(z,w)$ has the interpretation of the polarization of $\varDelta Q$, which defines in a natural fashion a Riemannian metric wherever $\varDelta Q>0$ (see, e.g., [@ahm1]).

We recall that $1/{\pmb{\partial}}_\theta\bar w=\bar\partial_w\theta$,

and observe that $${\pmb{\partial}}_\theta\frac{1}{{\pmb{\partial}}_\theta\bar w}=
[\bar\partial_w\theta]^{-1}\bar\partial_w^2\theta
=\frac{\bar\partial_w^2\theta}{\bar\partial_w\theta}=
\bar\partial_w\log(\bar\partial_w\theta),
\label{eq-4.20.1}$$ and that by [\[eq-4.19.1\]](#eq-4.19.1){reference-type="eqref" reference="eq-4.19.1"}, $$\begin{gathered}
\frac{|z-w|^2}{{\pmb{\partial}}_\theta\bar w}=|z-w|^2\bar\partial_w\theta
=\sum_{i=0}^{+\infty}\frac{1}{(i+1)!}(\bar w-\bar z)(w-z)^{i+1}
\partial_z^{i+1}\bar\partial_w Q(z,w)
\\
=\sum_{i=0}^{+\infty}\frac{1}{(i+1)!}(\bar w-\bar z)(w-z)^{i+1}
\partial_z^{i}\lambda(z,w).
\label{eq-4.30}
\end{gathered}$$ By [\[eq-4.19.3\]](#eq-4.19.3){reference-type="eqref" reference="eq-4.19.3"} combined with Taylor expansion, we see that $$\log(\bar\partial_w\theta)=
\log(\partial_z\bar\partial_w Q(z,w))+
\sum_{n=1}^{+\infty}\frac{(-1)^{n-1}}{n}
\bigg\{\sum_{i=1}^{+\infty}\frac{1}{(i+1)!}(w-z)^{i}
\frac{\partial_z^{i+1}\bar\partial_w Q(z,w)}{\partial_z\bar\partial_w Q(z,w)}
\bigg\}^n,
\label{eq-4.19.4}$$ so that in view of [\[eq-4.20.1\]](#eq-4.20.1){reference-type="eqref" reference="eq-4.20.1"}, using standard coset notation, $${\pmb{\partial}}_\theta\frac{1}{{\pmb{\partial}}_\theta\bar w}
\in \bar\partial_w\log\lambda(z,w)
+\frac{1}{2}(w-z)\partial_z\bar\partial_w\log\lambda(z,w)





+{\mathbf M}_{z-w}^2{\mathfrak R}_1.
\label{eq-4.22}$$

From the expansion [\[eq-4.30\]](#eq-4.30){reference-type="eqref" reference="eq-4.30"}, we get that $$\frac{|z-w|^2}{{\pmb{\partial}}_\theta\bar w}
\in |z-w|^2\lambda(z,w)+\frac12|z-w|^2(w-z)\partial_z\lambda(z,w)+
{\mathbf M}_{z-w}^3{\mathfrak R}_2,
\label{eq-4.21}$$

Next, we put $$\Lfun^2_{0}(z,w):=-\frac{4}{\pi}|z-w|^2[\lambda(z,w)]^2
=-\frac{4}{\pi}|z-w|^2[\partial_z\bar\partial_w Q(z,w)]^2,
\label{eq-4.24}$$ which is biholomorphic in each of the variables $(z,\bar w)$. We quickly check that the condition [\[eq-2.05\]](#eq-2.05){reference-type="eqref" reference="eq-2.05"} is met. By Lemma [\[lem-uniq1\]](#lem-uniq1){reference-type="ref" reference="lem-uniq1"}, this is the only possible choice of $\Lfun^2_{0}$. A more precise calculation shows that

$${\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}+
\frac{4}{\pi}\frac{|z-w|^2}{{\pmb{\partial}}_\theta\bar w}
+\frac{4}{\pi}(z-w)|z-w|^2\partial_z\lambda(z,w)\in{\mathbf M}_{z-w}^3{\mathfrak R}_2, 
\label{eq-4.25}$$ from which we may conclude that $${\mathbf N}\bigg[\frac12{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}+
\frac{2}{\pi}\frac{|z-w|^2}{{\pmb{\partial}}_\theta\bar w}\bigg]
+\frac{2}{\pi}|z-w|^2\partial_z\lambda(z,w)
\in{\mathbf M}_{z-w}^2{\mathfrak R}_2, 
\label{eq-4.25.0}$$ and that $${\pmb{\partial}}_w{\pmb{\partial}}_\theta\bigg\{{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}+
\frac{4}{\pi}\frac{|z-w|^2}{{\pmb{\partial}}_\theta\bar w}
+\frac{4}{\pi}(z-w)|z-w|^2\partial_z\lambda(z,w)\bigg\}
\in{\mathbf M}_{z-w}^2{\mathfrak R}_2. 
\label{eq-4.25:1}$$ If we recall [\[eq-coordch1\]](#eq-coordch1){reference-type="eqref" reference="eq-coordch1"} and [\[eq-4.19-ratio\]](#eq-4.19-ratio){reference-type="eqref" reference="eq-4.19-ratio"}, we see that $$\begin{gathered}
{\pmb{\partial}}_\theta{\pmb{\partial}}_w\Big\{(z-w)|z-w|^2\partial_z\lambda(z,w)\Big\}
=\frac{1}{\bar\partial_w\theta}\bar\partial_w\bigg(\partial_w-
\frac{\partial_w\theta}{\bar\partial_w\theta}\bar\partial_w\bigg)
\Big\{(z-w)|z-w|^2\partial_z\lambda(z,w)\Big\}
\\
\in\frac{1}{\bar\partial_w\theta}\bar\partial_w\big\{-2|z-w|^2\partial_z\lambda(z,w)
\big\}+
{\mathbf M}_{z-w}^2{\mathfrak R}_2
=2(z-w)\frac{\partial_z\lambda(z,w)}{\lambda(z,w)}
-2|z-w|^2\frac{\partial_z\bar\partial_w\lambda(z,w)}{\lambda(z,w)}+
{\mathbf M}_{z-w}^2{\mathfrak R}_2.
\label{eq-4.25:2}
\end{gathered}$$ By combining this calculation with [\[eq-4.25:1\]](#eq-4.25:1){reference-type="eqref" reference="eq-4.25:1"}, we see that $${\pmb{\partial}}_\theta{\pmb{\partial}}_w\bigg\{\frac12{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}+
\frac{2}{\pi}\frac{|z-w|^2}{{\pmb{\partial}}_\theta\bar w}\bigg\}
+\frac{4}{\pi}(z-w)\frac{\partial_z\lambda(z,w)}{\lambda(z,w)}
-\frac{4}{\pi}|z-w|^2\frac{\partial_z\bar\partial_w\lambda(z,w)}{\lambda(z,w)} 
\in{\mathbf M}_{z-w}^2{\mathfrak R}_2.
\label{eq-4.25:3}$$

In view of [\[eq-4.22\]](#eq-4.22){reference-type="eqref" reference="eq-4.22"}, [\[eq-4.25:3\]](#eq-4.25:3){reference-type="eqref" reference="eq-4.25:3"}, we see that [\[eq-2.06\]](#eq-2.06){reference-type="eqref" reference="eq-2.06"} taken modulo ${\mathbf M}_{z-w}{\mathfrak R}_2$ (see [\[eq-4.14\]](#eq-4.14){reference-type="eqref" reference="eq-4.14"}) gives $$\frac{\Lfun^2_{1}}{\bar\partial_w\theta}-\frac{4}{\pi}+\frac{2}{\pi}(\bar z-\bar w)
\frac{\bar\partial_w\lambda(z,w)}{\lambda(z,w)}
\in{\mathbf M}_{z-w}{\mathfrak R}_2,$$ which suggests that we should look for $\Lfun^2_{1}$ of the form $$\Lfun^2_{1}(z,w):=\frac{4}{\pi}\lambda(z,w)
-\frac{2}{\pi}(\bar z-\bar w)\bar\partial_w\lambda(z,w)
+\frac{2}{\pi}(z-w)\partial_z\lambda(z,w)+|z-w|^2\Xi_1(z,w),
\label{eq-4.40}$$ where $\Xi_1(z,w)$ is holomorphic in $(z,\bar w)$. We find that $$\begin{gathered}
{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{1}=\frac{\Lfun^2_{1}}{\bar\partial_w\theta}
\in \frac{4}{\pi}-\frac{2}{\pi}(\bar z-\bar w)
\frac{\bar\partial_w\lambda(z,w)}{\lambda(z,w)}
-\frac{4}{\pi}(w-z)\frac{\partial_z\lambda(z,w)}{\lambda(z,w)}
\\
-\frac{1}{\pi}
|z-w|^2\frac{[\partial_z\lambda(z,w)][\bar\partial_w\lambda(z,w)]}
{[\lambda(z,w)]^2}+|z-w|^2\frac{\Xi_1(z,w)}{\lambda(z,w)}+{\mathbf M}_{z-w}^2{\mathfrak R}_2.
\label{eq-4.38:2}
\end{gathered}$$ As we add up the relations [\[eq-4.22\]](#eq-4.22){reference-type="eqref" reference="eq-4.22"}, [\[eq-4.25:3\]](#eq-4.25:3){reference-type="eqref" reference="eq-4.25:3"}, and [\[eq-4.38:2\]](#eq-4.38:2){reference-type="eqref" reference="eq-4.38:2"}, the result is

$$\begin{gathered}
{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{1}+{\pmb{\partial}}_\theta{\pmb{\partial}}_w
\bigg\{\frac12{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}+\frac{2}{\pi}
\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg\}
-\frac{4}{\pi}+\frac{2}{\pi}(\bar z-\bar w){\pmb{\partial}}_\theta\frac{1}{{\pmb{\partial}}_\theta\bar w}
\\
\in \frac{4}{\pi}-\frac{2}{\pi}(\bar z-\bar w)
\frac{\bar\partial_w\lambda(z,w)}{\lambda(z,w)}
-\frac{4}{\pi}(w-z)\frac{\partial_z\lambda(z,w)}{\lambda(z,w)}
-\frac{1}{\pi}
|z-w|^2\frac{[\partial_z\lambda(z,w)][\bar\partial_w\lambda(z,w)]}
{[\lambda(z,w)]^2}
\\
+|z-w|^2\frac{\Xi_1(z,w)}{\lambda(z,w)}
-\frac{4}{\pi}(z-w)\frac{\partial_z\lambda(z,w)}{\lambda(z,w)}
+\frac{4}{\pi}
|z-w|^2\frac{\partial_z\bar\partial_w\lambda(z,w)}{\lambda(z,w)}
-\frac{4}{\pi}
\\
+\frac{2}{\pi}(\bar z-\bar w)\big\{\bar\partial_w\log\lambda(z,w)
+\frac12(w-z)\partial_z\bar\partial_w\log\lambda(z,w)\big\}
+{\mathbf M}_{z-w}^2{\mathfrak R}_2, 
\label{eq-4.41}
\end{gathered}$$ which we simplify to $$\begin{gathered}
{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{1}+{\pmb{\partial}}_w{\pmb{\partial}}_\theta
\bigg\{\frac12{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}+
\frac{2}{\pi}\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg\}
-\frac{4}{\pi}+\frac{2}{\pi}(\bar z-\bar w){\pmb{\partial}}_\theta\frac{1}{{\pmb{\partial}}_\theta\bar w}
\\
\in |z-w|^2\bigg\{\frac{3}{\pi}\frac{\partial_z\bar\partial_w\lambda(z,w)}{\lambda(z,w)}
+\frac{\Xi_1(z,w)}{\lambda(z,w)}\bigg\}+{\mathbf M}_{z-w}^2{\mathfrak R}_2.
\label{eq-4.42}
\end{gathered}$$

We want to implement this information into [\[eq-2.06\]](#eq-2.06){reference-type="eqref" reference="eq-2.06"}. Then we need the commutator calculation $$\boldsymbol{\big\lfloor}{\pmb{\partial}}_w{\pmb{\partial}}_\theta\boldsymbol{,}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}
\boldsymbol{\big\rfloor}=
{\mathbf M}_{{\pmb{\partial}}_w{\pmb{\partial}}_\theta^2\bar w}+{\mathbf M}_{{\pmb{\partial}}_\theta^2\bar w}{\pmb{\partial}}_w+
{\mathbf M}_{{\pmb{\partial}}_w{\pmb{\partial}}_\theta\bar w}{\pmb{\partial}}_\theta,$$ which together with [\[eq-4.25.0\]](#eq-4.25.0){reference-type="eqref" reference="eq-4.25.0"} leads to $$\begin{gathered}
{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}^{-1}
\boldsymbol{\big\lfloor}{\pmb{\partial}}_\theta{\pmb{\partial}}_w\boldsymbol{,}
{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\boldsymbol{\big\rfloor}\,
{\mathbf N}\bigg[\frac12{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}+\frac{2}{\pi}
\frac{|z-w|^2}{{\pmb{\partial}}_\theta\bar w}\bigg]
\\
\in-\frac{2}{\pi}(\bar z-\bar w)
\frac{[\partial_z\lambda(z,w)][\bar\partial_w\lambda(z,w)]}
{[\lambda(z,w)]^2}
+{\mathbf M}_{z-w}{\mathfrak R}_2.
\label{eq-4.42.1}
\end{gathered}$$ Putting [\[eq-4.42\]](#eq-4.42){reference-type="eqref" reference="eq-4.42"} and [\[eq-4.42.1\]](#eq-4.42.1){reference-type="eqref" reference="eq-4.42.1"} together, we find that $$\begin{gathered}
{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{1}+{\pmb{\partial}}_w{\pmb{\partial}}_\theta
\bigg\{\frac12{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}
+\frac{2}{\pi}\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg\}
-\frac{4}{\pi}+\frac{2}{\pi}
(\bar z-\bar w){\pmb{\partial}}_\theta\frac{1}{{\pmb{\partial}}_\theta\bar w}
\\
+
{\mathbf M}_{z-w}{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}^{-1}\boldsymbol{\big\lfloor}
{\pmb{\partial}}_w{\pmb{\partial}}_\theta,{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\boldsymbol{\big\rfloor}\,
{\mathbf N}\bigg[\frac12{\mathbf M}_{{\pmb{\partial}}_\theta\bar w}\Lfun^2_{0}+\frac{2}{\pi}
\frac{|z-w|^2}{{\pmb{\partial}}_\theta \bar w}\bigg]
\\
\in |z-w|^2
\bigg\{\frac{3}{\pi}\frac{\partial_z\bar\partial_w\lambda(z,w)}{\lambda(z,w)}
+\frac{\Xi_1(z,w)}{\lambda(z,w)}
-\frac{2}{\pi}\frac{[\partial_z\lambda(z,w)][\bar\partial_w\lambda(z,w)]}
{[\lambda(z,w)]^2} 
\bigg\} +{\mathbf M}_{z-w}^2{\mathfrak R}_2








\label{eq-4.44}
\end{gathered}$$ By Lemma [\[lem-uniq1\]](#lem-uniq1){reference-type="ref" reference="lem-uniq1"}, we may conclude from [\[eq-4.44\]](#eq-4.44){reference-type="eqref" reference="eq-4.44"} that $$\Xi_1(z,w)=-\frac{3}{\pi}\partial_z\bar\partial_w\lambda(z,w)+\frac{2}{\pi}
\frac{[\partial_z\lambda(z,w)][\bar\partial_w\lambda(z,w)]}
{\lambda(z,w)}.$$ In conclusion, we obtain that $\Lfun_1^2$ has the form $$\begin{gathered}
\label{eq-7.9.21}
\Lfun^2_{1}(z,w)=\frac{4}{\pi}\lambda(z,w)
-\frac{2}{\pi}(\bar z-\bar w)\bar\partial_w\lambda(z,w)
+\frac{2}{\pi}(z-w)\partial_z\lambda(z,w)
\\
-\frac{3}{\pi}|z-w|^2\partial_z\bar\partial_w\lambda(z,w)+\frac{2}{\pi}|z-w|^2
\frac{[\partial_z\lambda(z,w)][\bar\partial_w\lambda(z,w)]}
{\lambda(z,w)}.
\end{gathered}$$ We have also obtained an explicit expression for the third term $\Lfun^2_{2}$, but we omit the rather long computation.

The result is $$\label{eq-7.9.22}
\Lfun^2_{2}(z,w)=\frac{2}{\pi}\partial_z\bar\partial_w \log\lambda+ 
\frac{1}{\pi}(\bar w-\bar z)\partial_z\bar\partial_w^2\log\lambda
+\frac{1}{\pi}(z-w)\partial_z^2\bar\partial_w\log\lambda
+|z-w|^2 \Xi_2(z,w),$$ where $$\begin{gathered}
\Xi_2(z,w)= 
\frac3{2\pi}\frac{[\partial_z\bar\partial_w^2\lambda][\partial_z\lambda]}
{[\lambda]^2} 
-\frac{13}{2\pi} 
\frac{[\partial_z b][\partial_z\bar\partial_w\lambda][\bar\partial_w\lambda]}
{[\lambda]^3}+\frac{3}{2\pi}\frac{[\partial_z\bar\partial_w\lambda]^2}{[\lambda]^2}
\\
-\frac{1}{\pi}\frac{[\partial_z\lambda]^2[\bar\partial_w^2\lambda]}{[\lambda]^3}
+ \frac{17}{4\pi} \frac{[\partial_z\lambda]^2[\bar\partial_w\lambda]^2}{[\lambda]^4}
-\frac{2}{3\pi} \frac{\partial_z^2 \bar \partial_w^2\lambda}{\lambda}
+\frac{3}{2\pi}\frac{[\partial_z^2\bar\partial_w\lambda][\bar\partial_w\lambda]}
{[\lambda]^2} 
\\
-\frac{1}{\pi}\frac{[\partial_z^2\lambda][\bar\partial_w \lambda]^2}{[\lambda]^3}
+\frac{1}{3\pi}\frac{[\partial_z^2\lambda][\bar \partial_w^2\lambda]}{[\lambda]^2}. 
\end{gathered}$$

::: rem
[]{#rem-AA label="rem-AA"} The formula for $\Lfun_0^2$ is given by [\[eq-4.24\]](#eq-4.24){reference-type="eqref" reference="eq-4.24"}, the formula for $\Lfun_1^2$ is given by [\[eq-7.9.21\]](#eq-7.9.21){reference-type="eqref" reference="eq-7.9.21"}, while $\Lfun_2^2$ is expressed by [\[eq-7.9.22\]](#eq-7.9.22){reference-type="eqref" reference="eq-7.9.22"}.
:::
