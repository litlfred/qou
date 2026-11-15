---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action"
section_id: sec-007-212-ordering
section_title: "Ordering"
section_number: 2.1.2
pages: 10-11
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.976
doc_brief: "Non-Abelian Stokes theorem in action — In this short review main issues related to the non-Abelian Stokes theorem have been addressed."
---
There are a lot of different ordering operators in our formulas which have been collected in this section.

#### Dyson series

We know from quantum theory that the path-ordered exponent of an operator $\hat{A}$ can be expressed by the power series called the Dyson series, $$\begin{aligned}
        \lefteqn{{\rm P}\,\exp\left[i\int_{t'}^{t''}\!\hat{A}(t)\;dt\right]}   \nonumber \\
    &=& {\rm P}\left[1+\sum_{n=1}^{\infty}\frac{i^n}{n!}
    \int_{t'}^{t''}\!dt_1\int_{t'}^{t''}\!dt_2\ldots
    \int_{t'}^{t''}\!dt_n\,\hat{A}(t_1)\hat{A}(t_2)\ldots
    \hat{A}(t_n)\right]   \nonumber \\
    &=&1+\sum_{n=1}^{\infty}\frac{i^n}{n!}
    \int_{t'}^{t''}\!dt_1\int_{t'}^{t''}\!dt_2\ldots
    \int_{t'}^{t''}\!dt_n\,
    {\rm P}\left[\hat{A}(t_1)\hat{A}(t_2)\ldots
    \hat{A}(t_n)\right]   \nonumber \\
    &=&1+\sum_{n=1}^{\infty}i^n
    \int_{t'}^{t''}\!dt_1\int_{t'}^{t_1}\!dt_2\ldots
    \int_{t'}^{t_{n-1}}\!dt_n\,
    \hat{A}(t_1)\hat{A}(t_2)\ldots\hat{A}(t_n),
    \nonumber
\end{aligned}$$ where $${\rm P}\left[\hat{A}_1(t_1)\ldots\hat{A}_n(t_n)\right]
\stackrel{\rm def}{=}
\hat{A}_{\sigma(1)}\left(t_{\sigma(1)}\right)\ldots
\hat{A}_{\sigma(n)}\left(t_{\sigma(n)}\right)),
\qquad
t_{\sigma(1)}\geq\ldots\geq t_{\sigma(n)}.$$ For example, for two operators $${\rm P}\left[\hat{A}_1(t_1)\hat{A}_2(t_2)\right]
    \equiv \theta\left(t_1-t_2\right)\hat{A}_1(t_1)\hat{A}_2(t_2)
    +\theta\left(t_2-t_1\right)\hat{A}_2(t_2)\hat{A}_1(t_1),$$ where $\theta$ is the step function.

#### Conventions

Since the operators/matrices appearing in our considerations are, in general, non-commutative, we assume the following conventions: $$\prod_{n=1}^N X_n
    \stackrel{\rm def}{=}
    X_N X_{N-1} \ldots X_2 X_1,
    \nonumber$$ $${\rm P}_t \left(X_1 X_2 \ldots X_{N-1} X_N\right)
    \stackrel{\rm def}{=}
    X_N X_{N-1} \ldots X_2 X_1,
    \nonumber$$ whereas for two parameters $$\begin{aligned}
    \lefteqn{{\rm P}_{s,t}\prod_{m,n=1}^N X_{m,n}}   \nonumber \\
&\stackrel{\rm def}{=}&
    \prod_{n=1}^N \prod_{m=1}^N X_{m,n}\nonumber\\  
    &\equiv&
    X_{N,N} X_{N-1,N} \ldots X_{1,N} X_{N,N-1} \ldots X_{1,2} X_{N,1} \ldots X_{2,1} X_{1,1}.    \nonumber
\end{aligned}$$
