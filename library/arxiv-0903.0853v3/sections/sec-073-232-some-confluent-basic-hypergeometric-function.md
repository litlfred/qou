---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-073-232-some-confluent-basic-hypergeometric-function
section_title: "Some confluent basic hypergeometric functions"
section_number: 23.2
pages: 121-122
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.963
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:confluenthypergeom label="subsection:confluenthypergeom"}

Usual basic hypergeometrics series have the form: $$\label{not103}
{}_{2} \Phi_{1}(a,b;c;q,z) := \sum_{n \geq 0}
\dfrac{(a,b;q^{-1})_{n}}{(c,q^{-1};q^{-1})_{n}} z^{n}~,~
\text{~where~} a,b,c \in {\mathbf C}^{*}.$$ (Remember that here, $\left |q \right |> 1$.) Writing for short $F(z)$ this series, the rescaling $F(- q^{-1} z/c)$ degenerates, when $c \to \infty$, into a *confluent* basic hypergeometrics series: $$\phi(a,b;q,z) := \sum_{n \geq 0}
\dfrac{(a,b;q^{-1})_{n}}{(q^{-1};q^{-1})_{n}} q^{n(n+1)/2} z^{n}~,~
\text{~where~} a,b \in {\mathbf C}^{*}.$$ Writing $u_{n} := \dfrac{(a,b;q^{-1})_{n}}{(q^{-1};q^{-1})_{n}} q^{n(n+1)/2}$ the general coefficient, we have, for all $n \geq 0$: $$(q^{n+1} - 1) u_{n+1} = q^{2} (q^{n} - a) (q^{n} - b) u_{n},$$ whence, multiplying by $z^{n+1}$ and summing: $$(\sigma_q- 1) \hat{f} = q^{2} z (\sigma_q- a) (\sigma_q- b) \hat{f},$$ where we write for short $\hat{f}(z)$ the divergent series $\phi(a,b;q,z)$. We shall denote the corresponding $q$-difference operator as: $$L := q^{2} z (\sigma_q- a) (\sigma_q- b) - (\sigma_q- 1) =
q^{2} z \sigma_q^{2} - \bigl(1 + (a+b) q^{2} z)\bigr) \sigma_q+ (1 + ab q^{2} z).$$ We are interested in the equation $L f = 0$. Its Newton polygon (*i.e.* that of $L$) has slopes $0$ and $1$. The slope $0$ has exponent $1$ and gives rise to the divergent solution $\hat{f}$. To tackle the slope $1$, we compute: $$(z {\theta_{q}}) L (z {\theta_{q}})^{-1} = \dfrac{1}{q z}
\Bigl(\sigma_q^{2} - \bigl(1 + (a+b) q^{2} z)\bigr) \sigma_q+ 
q z (1 + ab q^{2} z)\Bigr),$$ which has slopes $0$ and $-1$, the latter having exponent $0$. According to Adams lemma (see the footnote in the introduction to this chapter), we thus get a unique solution $g_{0} \in 1 + z {{\mathbf C}\{z\}}$, whence the "convergent" solution $f_{0} := \dfrac{g_{0}}{z {\theta_{q}}}$ of equation $L f = 0$.

### Factoring $L$

To get $L = q^{2} z (\sigma_q- A)(\sigma_q- B)$, we first look for $B$ such that $(\sigma_q- B) f_{0} = 0$, that is, $B := \dfrac{\sigma_qf_{0}}{f_{0}} = 
\dfrac{1}{q z} ~ \dfrac{\sigma_qg_{0}}{g_{0}} \cdot$. Thus, $L = (\sigma_q- A)(q z \sigma_q- q z B) = (\sigma_q- A)
\left(q z \sigma_q- \dfrac{\sigma_qg_{0}}{g_{0}}\right)$ and, by identification of the constant terms: $A = \dfrac{(1 + a b q^{2} z) g_{0}}{\sigma_qg_{0}}$ and in the end: $$L = \left(\sigma_q- \dfrac{(1 + a b q^{2} z) g_{0}}{\sigma_qg_{0}}\right)
\left(q z \sigma_q- \dfrac{\sigma_qg_{0}}{g_{0}}\right).$$ The corresponding non homogeneous equation is $q z f \sigma_q- \dfrac{\sigma_qg_{0}}{g_{0}} f = v$, where $v$ is a non trivial solution of $\left(\sigma_q- \dfrac{(1 + a b q^{2} z) g_{0}}{\sigma_qg_{0}}\right) v = 0$. An obvious choice is: $$v := \dfrac{1}{g_{0}} \prod_{n \geq 1} (1 + a b q^{2-n} z) =
\dfrac{1}{g_{0}} (- a b q z;q^{-1})_{\infty}.$$ One checks easily that the above non homogeneous equation has indeed a unique solution in $1 + z {{\mathbf C}[[z]]}$, and this has to be $\hat{f}$. This equation is associated with the matrix $\begin{pmatrix} \dfrac{\sigma_qg_{0}}{g_{0}} & v \\ 0 & q z \end{pmatrix}$, which can be seen to be equivalent to the matrix $\begin{pmatrix} 1 & u \\ 0 & z \end{pmatrix}$ through the gauge transform $\begin{pmatrix} g_{0}^{-1} & 0 \\ 0 & z^{-1} \end{pmatrix}$.
