---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-074-233-some-special-cases
section_title: "Some special cases"
section_number: 23.3
pages: 122-124
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.921
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:specialcases label="subsection:specialcases"}

Taking $a := b := q^{-1}$ yields: $$\hat{f} = \sum_{n \geq 0} (q^{-1};q^{-1})_{n} q^{n(n+1)/2} z^{n}.$$ The recurrence relation $\dfrac{u_{n+1}}{u_{n}} = q^{n+1} - 1$ immediately gives the non homogeneous equation $q z \sigma_qf - (1+z) f = -1$. This, in turn, boils down to the straight $q$-Euler equation by setting $g := \dfrac{z}{(-q^{-1} z;q^{-1})_{\infty}} f$, so that $z \sigma_qg - g = \dfrac{- z}{(-z;q^{-1})_{\infty}} \cdot$\
Taking $a := b := 0$ yields: $$\hat{f} = \sum_{n \geq 0} \dfrac{1}{(q^{-1};q^{-1})_{n}} q^{n(n+1)/2} z^{n}.$$ The recurrence relation $\dfrac{u_{n+1}}{u_{n}} = \dfrac{q^{2n+2}}{q^{n+1} - 1}$ gives the homogeneous equation $q^{2} z \sigma_q^{2} f - \sigma_qf + f = 0$. The convergent solution is $f_{0} := \dfrac{1}{z {\theta_{q}}} g_{0}$, where $g_{0} = \sum \gamma_{n} z^{n} \in 1 + z {{\mathbf C}\{z\}}$ is solution of the equation $(\sigma_q^{2} - \sigma_q+ q z) g = 0$. The corresponding recurrence relation $(q^{2 n} - q^{n}) \gamma_{n} + q \gamma_{n-1} = 0$ can be solved exactly and entails: $$g_{0} = \sum_{n \geq 0} \dfrac{(-1)^{n} q^{-n^{2}}}{(q^{-1};q^{-1})_{n}} z^{n}.$$ The corresponding factorisation is $L = \left(\sigma_q- \dfrac{g_{0}}{\sigma_qg_{0}}\right)
\left(q z \sigma_q- \dfrac{\sigma_qg_{0}}{g_{0}}\right)$. Following [@CZCBHG][^1], one can prove the following formula for the Stokes operators: $$S_{\lambda} \hat{f} - S_{\mu} \hat{f} = (q^{-1};q^{-1})_{\infty}^{2}
\dfrac{{\theta_{q}}(-\lambda/\mu) {\theta_{q}}(z/\lambda\mu)}
{{\theta_{q}}(-1/\lambda) {\theta_{q}}(-1/\mu) {\theta_{q}}(\lambda/z) {\theta_{q}}(z/\mu)}
\sum_{n \in {\mathbf Z}} \dfrac{(-1)^{n} q^{-n^{2}}}{(q^{-1};q^{-1})_{n}} z^{n}.$$ We shall not attempt to prove this, but a similar formula is checked in the next case.\
Taking $a := 0, b := q^{-1}$ yields: $$\hat{f} = \sum_{n \geq 0} q^{n(n+1)/2} z^{n} = \text{\tencyr\cyracc Ch}(q z),$$ which is solution of the $q$-Euler equation $(q z \sigma_q- 1) f = -1$. A solution of the associated homogeneous equation is $\dfrac{1}{{\theta_{q}}(qz)} = \dfrac{1}{{\theta_{q}}(1/z)}$, so that, for any two $\lambda,\mu \not\in [1;q]$ (authorized directions of summation): $$S_{\lambda} \hat{f} - S_{\mu} \hat{f} = \dfrac{K(\lambda,\mu,z)}{{\theta_{q}}(1/z)},$$ where $K$ is $q$-invariant in each of the three arguments. We assume $\overline{\lambda} \neq \overline{\mu}$; then, as a function of $z$, the numerator $K$ is elliptic with simple zeroes over $[-1;q]$ and at most simple poles over $[-\lambda;q]$ and $[-\mu;q]$; thus: $$\label{not104}
K(\lambda,\mu,z) = K'(\lambda,\mu) ~
\dfrac{{\theta_{q}}(1/z) {\theta_{q}}(z/\lambda \mu)}{{\theta_{q}}(\lambda/z) {\theta_{q}}(z\mu)},$$ where $K'(\lambda,\mu)$ is independent of $z$ and, as a function of $\lambda$, has at most simple poles over $[1;q]$ and $[\mu;q]$; thus: $$K'(\lambda,\mu) \dfrac{{\theta_{q}}(z/\lambda \mu)}{{\theta_{q}}(\lambda/z)} = 
K'' \dfrac{{\theta_{q}}(z/\lambda \mu) {\theta_{q}}(-\lambda/\mu)}
{{\theta_{q}}(\lambda/z) {\theta_{q}}(-1/\lambda)},$$ where $K''$ is independent of $\lambda,\mu,z$. Last, we get: $$S_{\lambda} \hat{f} - S_{\mu} \hat{f} = C
\dfrac{{\theta_{q}}(-\lambda/\mu) {\theta_{q}}(z/\lambda\mu)}
{{\theta_{q}}(-1/\lambda) {\theta_{q}}(-1/\mu) {\theta_{q}}(\lambda/z) {\theta_{q}}(z/\mu)} \cdot$$ We shall now see that $C = -{\theta_{q}}'(-1) = (q^{-1};q^{-1})_{\infty}^{3}$. The second equality follows immediately from Jacobi Triple Product Formula. Note that, by simple singularity analysis, one may write: $$S_{\lambda} \hat{f} = 
\sum_{n \in {\mathbf Z}} \dfrac{\alpha_{n}}{z + \lambda q^{n}} \cdot$$ Since $S_{\lambda} \hat{f}(0) = 1$, we have $\sum \alpha_{n} q^{-n} = \lambda$. On the other hand, from the functional equation, taking residues yields the recurrence relation: $\alpha_{n-1}  = - \lambda \alpha_{n} q^{n-1}$, then $\alpha_{n} = (-1/\lambda)^{n} q^{-n(n-1)/2} \alpha_{0}$ and in the end: $$\lambda = \alpha_{0} \sum_{n \in {\mathbf Z}} (-1/\lambda)^{n} q^{-n(n-1)/2} = 
\alpha_{0} {\theta_{q}}(-1/\lambda) \Longrightarrow 
\alpha_{0} = \dfrac{\lambda}{{\theta_{q}}(-1/\lambda)} \cdot$$ On the other hand: $$\begin{aligned}
\alpha_{0} &= 
\lim_{z \to -\lambda} (z + \lambda) (S_{\lambda} \hat{f} - S_{\mu} \hat{f}) \\
&= 
\lim_{z \to -\lambda} (z + \lambda) C
\dfrac{{\theta_{q}}(-\lambda/\mu) {\theta_{q}}(z/\lambda\mu)}
{{\theta_{q}}(-1/\lambda) {\theta_{q}}(-1/\mu) {\theta_{q}}(\lambda/z) {\theta_{q}}(z/\mu)} \\
&=
C \dfrac{1}{{\theta_{q}}(-1/\lambda)} \dfrac{-\lambda}{{\theta_{q}}'(-1)},
\end{aligned}$$ whence the desired conclusion.

[^1]: Note that [@LuZ] contains similar formulas.
