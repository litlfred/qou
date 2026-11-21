---
doc_id: arxiv-math-9905032v2
doc_title: "Asymptotics of Plancherel measures for symmetric groups"
section_id: sec-015-41-results-and-strategy-of-proof
section_title: "Results and strategy of proof"
section_number: 4.1
pages: 24-26
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.886
latex_coverage_ratio: 0.973
doc_brief: "Asymptotics of Plancherel measures for symmetric groups — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
[]{#s41 label="s41"}

In this section we prove Theorem [\[t3\]](#t3){reference-type="ref" reference="t3"} which was stated in Section [\[s14\]](#s14){reference-type="ref" reference="s14"} of the Introduction. We refer the reader to Section [\[s14\]](#s14){reference-type="ref" reference="s14"} for a discussion of the relation between Theorem [\[t3\]](#t3){reference-type="ref" reference="t3"} and the results obtained in [@BDJ1; @BDJ2; @O].

Recall that the Airy kernel was defined as follows

$$\mathsf{A}(x,y)=\frac{A(x)A'(y)-A'(x)A(y)}{x-y}.$$

where $A(x)$ is the Airy function [\[e17\]](#e17){reference-type="eqref" reference="e17"}. The *Airy ensemble* is, by definition, a random point process on $\mathbb{R}$, whose correlation functions are given by

$$\rho^{\textup{Airy}}_k(x_1,\dots,x_k)= \det \Big[\,\mathsf{A}(x_i,x_j)
\Big]_{1\le i,j \le k}\,.$$

This ensemble was studied in [@TW]. We denote by $\zeta_1 > \zeta_2 > \dots$ a random configuration of the Airy ensemble. Theorem [\[t3\]](#t3){reference-type="ref" reference="t3"} says that after a proper scaling and normalization, the rows $\lambda_1,\lambda_2,\dots$ of a Plancherel random partition $\lambda$ converge in joint distribution to the Airy ensemble. Namely, the following random variables $\widetilde{\lambda}$

$$\widetilde{\lambda}=
\left(\widetilde{\lambda}_1 \ge \widetilde{\lambda}_2 \ge \dots
\right)\,,
\quad 
\widetilde{\lambda}_i =
n^{1/3} \, \left(
\frac{\lambda_i}{n^{1/2}}-2 \right) \,,$$

converge, in joint distribution, to the Airy ensemble as $n\to\infty$.

In the proof of Theorem [\[t3\]](#t3){reference-type="ref" reference="t3"}, we shall follow the strategy explained in Section [\[s15\]](#s15){reference-type="ref" reference="s15"} of the Introduction. First, we shall prove that under the poissonized measure $M^\theta$ on the set of partitions $\lambda$, the random variables $\widetilde{\lambda}$ converge, in joint distribution, to the Airy ensemble as $\theta\approx n\to\infty$. This result is stated below as Theorem [\[t4\]](#t4){reference-type="ref" reference="t4"}. From this, using certain monotonicity and Lemma [\[l48\]](#l48){reference-type="ref" reference="l48"} which is due to K. Johansson, we shall conclude that the same is true for the measures $M_n$ as $n\to\infty$.

The proof of Theorem [\[t4\]](#t4){reference-type="ref" reference="t4"} will be based on the analysis of the behavior of the correlation functions of $M^\theta$, $\theta\approx n \to \infty$, near the point $2\sqrt{n}$. From the expression for correlation functions of $M^\theta$ given in Theorem [\[t1\]](#t1){reference-type="ref" reference="t1"} it is clear that this amounts to the study of the asymptotics of $J_{2\sqrt{n}}(2\sqrt\theta)$ when $\theta\approx n \to \infty$. This asymptotics is classically known and from it we shall derive the following

::: proposition
[]{#p41 label="p41"} Set $r=\sqrt\theta$. We have

$$r^{\frac 13}\mathsf{J}\left(2r+xr^{\frac 13},2r+yr^{\frac 13},{r^2} \right)\to \mathsf{A}(x,y), 
\quad r\to+\infty\,,$$

uniformly in $x$ and $y$ on compact sets of $\mathbb{R}$.
:::

The prefactor $r^{\frac 13}$ corresponds to the fact that we change the local scale near $2r$ to get non-vanishing limit correlations.

Using this and verifying certain tail estimates we obtain the following

::: theorem
[]{#t4 label="t4"} For any fixed $m=1,2,\dots$ and any $a_1,\dots,a_m\in\mathbb{R}$ we have

$$\begin{gathered}
\label{e401} 
\lim_{\theta\to+\infty}
M^\theta\left(\left\{\lambda\,\left|\,
\frac{\lambda_i-2\sqrt{\theta}}{\theta^{\frac 16}}\,< a_i\,, \  1\le i\le 
m\right.\right\}\right)=\\
\operatorname{Prob}\{\zeta_i< a_i\,,\  1\le i\le m\}\,,
\end{gathered}$$

where $\zeta_1>\zeta_2>\dots$ is the Airy ensemble.
:::

Observe that the limit behavior of $\widetilde{\lambda}$ is, obviously, identical with the limit behavior of similarly scaled $1$st, $2$nd, an so on maximal Frobenius coordinates.

Proofs of Proposition [\[p41\]](#p41){reference-type="ref" reference="p41"} and Theorem [\[t4\]](#t4){reference-type="ref" reference="t4"} are given Section [\[s42\]](#s42){reference-type="ref" reference="s42"}. In Section [\[s43\]](#s43){reference-type="ref" reference="s43"}, using a depoissonization argument based on Lemma [\[l48\]](#l48){reference-type="ref" reference="l48"} we deduce Theorem [\[t3\]](#t3){reference-type="ref" reference="t3"}.

::: remark
We consider the behavior of any number of initial rows of $\lambda$, where $\lambda$ is a Plancherel random partition. By symmetry, same results describe the behavior of any number of initial columns of $\lambda$.
:::
