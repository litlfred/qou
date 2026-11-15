---
doc_id: arxiv-1804.10084v1
doc_title: "Concentration of Lipschitz Functions of Negatively Dependent Variables"
section_id: sec-003-3-concentration-under-negative-regression
section_title: "Concentration under negative regression"
section_number: 3
pages: 3-4
source_pdf: 1804.10084v1.pdf
source_sha256: 716da9708f06d930
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 1.0
doc_brief: "Concentration of Lipschitz Functions of Negatively Dependent Variables — We explore the question whether Lipschitz functions of random variables under various forms of negative correlation satisfy"
---
[]{#sec:neg-reg-result label="sec:neg-reg-result"}

We provide here what (we claim) is a correct proof of a previously claimed result [@DubhashiRanjan98 Proposition 31], namely a concentration bound for Lipschitz functions of random variables under the property of negative regression. In fact we improve their theorem in the sense that we do not require the assumption of monotonicity of $f$. For simplicity, we focus on the case of $1$-Lipschitz functions.

::: theorem
[]{#thm:Lipschitz-R label="thm:Lipschitz-R"} Let $X_1,\ldots,X_n$ be $\{0,1\}$ random variables satisfying the condition of negative regression. Let $f:\{0,1\}^n \rightarrow {\mathbb R}$ be a $1$-Lipschitz function, and $\mu = {\mathbb E}[f(X_1,\ldots,X_n)]$. Then for any $t > 0$, $$\Pr[f(X_1,\ldots,X_n) \geq \mu + t] \leq e^{-t^2/2n},$$ $$\Pr[f(X_1,\ldots,X_n) \leq \mu - t] \leq e^{-t^2/2n}.$$ If $f$ is monotone, then the bound can be improved to $e^{-2 t^2 / n}$.
:::

We remark that in the case of monotone $f$, our bound coincides with that of McDiarmid's inequality for independent random variables [@McDiarmid89], in which case the constant in the exponent is known to be tight. In the non-monotone case, it is known that the same constant cannot be achieved [@PemPeres14], but it might be possible to prove a bound of $e^{-t^2/n}$; i.e., our constant could be off by a factor of $2$.

Negative regression is weaker than stochastic covering, or the strong Rayleigh property, and hence qualitatively our bound subsumes that of [@PemPeres14]. In terms of applications, it is fair to say that most of the known examples satisfying negative regression in fact satisfy the strong Rayleigh property and are hence covered by [@PemPeres14].

Quantitatively speaking, the constants in the exponent proved by Pemantle and Peres [@PemPeres14] are somewhat worse than ours, but their bounds are functions of $\mu = {\mathbb E}[\sum X_i]$ rather than $n$, so are not directly comparable to ours.

In terms of techniques, our proof is more elementary than that of [@PemPeres14], which relies on the (beautiful) theory of stable polynomials. We follow the classical martingale paradigm, with one new twist --- an adaptive ordering of the variables.
