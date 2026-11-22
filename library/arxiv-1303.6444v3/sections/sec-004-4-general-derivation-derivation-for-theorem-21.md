---
doc_id: arxiv-1303.6444v3
doc_title: "VIRIAL EXPANSION BOUNDS"
section_id: sec-004-4-general-derivation-derivation-for-theorem-21
section_title: "General Derivation: Derivation for Theorem 2.1"
section_number: 4
pages: 5-7
source_pdf: 1303.6444v3.pdf
source_sha256: 4f12ace2197f70ca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.985
doc_brief: "VIRIAL EXPANSION BOUNDS — In the 1960s, the technique of using cluster expansion bounds in order to achieve bounds on the virial expansion was developed by Lebowitz and Penrose (1964) and Ruelle"
---
[]{#sec: general label="sec: general"} We wish to obtain bounds on virial coefficients using those which come from cluster coefficients, in order to gain an estimate of the lower bound for the radius of convergence of the virial expansion. The derivation loosely follows the method used by Ruelle in [@R69] and that of Lebowitz and Penrose in [@LPen64]. The starting point is the cluster expansion bound, which is given in the form: $$|nb_n| \leq a \frac{n^{n-1}}{n!}b^n \label{generalcluster}$$ Where $a$ and $b$ are positive functions of temperature defined by the particular bound we use.

The starting point is the relationship in [\[contourrep\]](#contourrep){reference-type="eqref" reference="contourrep"}, (implicitly) defining virial coefficients in terms of cluster coefficients: $$c_n=\frac{\beta^{-1}}{2 \pi i} \oint_C \frac{\mathrm{d}z}{nz\rho^{n-1}} \label{integralforvirial}$$ In order to get an upper bound on $|c_n|$, we need to bound $|\rho|$ from below. To do this we use the bound: $$|\rho-z| \leq \sum\limits_{n=2}^{\infty} |nb_n||z|^n \label{r-zbound}$$ We then substitute in for the upper bounds we have on the cluster coefficients: $$|\rho-z| \leq a \sum\limits_{n=2}^{\infty}\frac{n^{n-1}}{n!}(b|z|)^n \label{r-zbound2}$$ We define the function: $f(x):=\sum\limits_{n=1}^{\infty}\frac{n^{n-1}}{n!}x^n$ and write [\[r-zbound2\]](#r-zbound2){reference-type="eqref" reference="r-zbound2"} conveniently as: $$|\rho-z| \leq a(f(b|z|)-b|z|) \label{simplebound}$$ Using the reverse triangle inequality, we obtain: $$|\rho| \geq |z|(1+ab)-a f(b|z|) \label{rbound}$$ Let $b|z|=se^{-s}$ and observe that, from the assumed generic bound on the cluster expansion, $b|z| \leq e^{-1}$ in order for $\sum\limits_{n=1}^{\infty}nb_nz^n$ to converge. $se^{-s}$ is an increasing function on $(0,1)$ and it takes values in $(0,e^{-1})$ as required. We then have the bound in terms of $s$: $$|\rho|\geq b^{-1}se^{-s}(1+ab)-af(se^{-s}) \label{sfunction1}$$ We have chosen the function $se^{-s}$ since it is the inverse function of $f$. This can be understood from Lagrange Inversion (shown in appendix) and is a result in [@CJK97] . We thus have the expression: $$|\rho| \geq b^{-1}se^{-s}(1+ab)-as \label{sfunction2}$$ We thus seek to maximise the right hand side to get the best possible bound. We notice that in the range $s \in (0,1)$ we have a zero at $s=0$ and another when $b^{-1}e^{-s}(1+ab)-a=0$ i.e. when $e^{s}=1+\frac{1}{ab}$, so at $s=\ln\left(1+\frac{1}{ab}\right)$. It is positive for $s \in (0,\ln\left(1+\frac{1}{ab}\right))$. We seek the value of $s$ to maximise this function in this range.

::: remark
This approach to estimating a lower bound for the radius of convergence for the virial expansion, takes a value of $|z|$ some distance away from its maximal value for convergent cluster expansions. We expect density to increase with fugacity and so the maximal density for which the cluster expansions remain convergent appears to be greater than that for the virial expansion. This is not true in general and is a weakness of this approach.
:::

If we define: $$r(s):=s(e^{-s}(1+ab)b^{-1}-a) \label{reqn}$$ and take the derivative to search for an extremum in this range. $$r'(s) = (e^{-s}(1+ab)b^{-1}-a)-se^{-s}(1+ab)b^{-1} \label{r'eqn}$$ if we find when $r'(s)=0$ in [\[r\'eqn\]](#r'eqn){reference-type="eqref" reference="r'eqn"}, then we solve: $$(1-s)e^{-s}=\frac{ab}{1+ab}$$ Substituting $\gamma=1-s$, we get the equation for $\gamma$: $$\gamma e^{\gamma}=\frac{eab}{1+ab} \label{lambertfunction}$$ The Lambert $W$-function, as is explained in [@CJK97], is the inverse of $\gamma e^{\gamma}$ and so we can write [\[reqn\]](#reqn){reference-type="eqref" reference="reqn"} in terms of $\gamma$ and substitute $\gamma$ for $W(\mu)$, where $\mu := \frac{eab}{1+ab}$. If we write $\tilde{r}(\gamma(s)):=r(s)$. We thus get: $$\begin{aligned}
 \tilde{r}(\gamma)&=(1-\gamma)(e^{\gamma}\frac{1+ab}{eb}-a) \notag \\
 &= a(e^{\gamma}\frac{1+ab}{eab}-\gamma e^{\gamma} \frac{1+ab}{eab}-1+\gamma) \notag \\
 &=a(\frac{1}{\gamma}-2+\gamma) \notag \\
 &=a\frac{(W(\mu)-1)^2}{W(\mu)} \label{finalreqn}
\end{aligned}$$ Where we use [\[lambertfunction\]](#lambertfunction){reference-type="eqref" reference="lambertfunction"} to cancel: $\gamma e^{\gamma} \frac{1+ab}{eab}=1$ and $e^{\gamma} \frac{1+ab}{eab}=\frac{1}{\gamma}$.

We evaluate the integral [\[integralforvirial\]](#integralforvirial){reference-type="eqref" reference="integralforvirial"} along the contour described by the circle $|z|=$ constant, where the constant is determined by the manipulations above. This leaves us with the integral: $$|c_n| \leq \frac{\beta^{-1}}{2n\pi} \oint_C \frac{\mathrm{d}z}{|z||\rho|^{n-1}}$$ This gives us bounds on the coefficients $c_n$ as: $$|c_n| \leq \frac{\beta^{-1}}{n} \left(a^{-1}\frac{W(\mu)}{(W(\mu)-1)^2}\right)^{n-1} \label{cbounds}$$

This gives us the radius of convergence of the virial expansion satisfying: $$\mathcal{R}_{\text{Vir}} \geq a \frac{(W(\mu)-1)^2}{W(\mu)}$$
