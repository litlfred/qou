---
doc_id: arxiv-math-9905032v2
doc_title: "Asymptotics of Plancherel measures for symmetric groups"
section_id: sec-002-12-poissonization-and-correlation-functions
section_title: "Poissonization and correlation functions"
section_number: 1.2
pages: 4-6
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.97
doc_brief: "Asymptotics of Plancherel measures for symmetric groups — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
[]{#s12 label="s12"}

For $\theta>0$, consider the *poissonization* $M^\theta$ of the measures $M_n$

$$M^\theta(\lambda) = e^{-\theta}\sum_n \frac{\theta^n}{n!}\, M_n(\lambda) =
e^{-\theta} \theta^{|\lambda|} \,
\left(\frac{\dim\lambda}{|\lambda|!}
\right)^2 \,.$$

This is a probability measure on the set of all partitions. Our first result is the computation of the correlation functions of the measures $M^\theta$.

By correlation functions we mean the following. By definition, set $$\mathcal{D}(\lambda)=\{\lambda_i-i\}\subset\mathbb{Z}\,.$$ Also, following [@VK3], define the *modified Frobenius coordinates* $\operatorname{Fr}(\lambda)$ of a partition $\lambda$ by

$$\begin{gathered}
\label{e0009}

\operatorname{Fr}(\lambda)=\left(\mathcal{D}(\lambda)+{\textstyle \frac 12}\right)\triangle \left(\mathbb{Z}_{\le 0} -{\textstyle \frac 12}\right)\\
=
\left\{p_1+{\textstyle \frac 12},\dots,p_d+{\textstyle \frac 12},-q_1-{\textstyle \frac 12},\dots,-q_d-{\textstyle \frac 12}
\right\} \subset \mathbb{Z}+{\textstyle \frac 12}\,,
\end{gathered}$$

where $\triangle$ stands for the symmetric difference of two sets, $d$ is the number of squares on the diagonal of $\lambda$, and $p_i$'s and $q_i$'s are the usual Frobenius coordinates of $\lambda$. Recall that $p_i$ is the number of squares in the $i$th row to the right of the diagonal, and $q_i$ is number of squares in the $i$th column below the diagonal. The equality [\[e0009\]](#e0009){reference-type="eqref" reference="e0009"} is a well known combinatorial fact discovered by Frobenius, see Ex. I.1.15(a) in [@M]. Note that, in contrast to $\operatorname{Fr}(\lambda)$, the set $\mathcal{D}(\lambda)$ is infinite and, moreover, it contains all but finitely many negative integers.

The sets $\mathcal{D}(\lambda)$ and $\operatorname{Fr}(\lambda)$ have the following nice geometric interpretation. Let the diagram $\lambda$ be flipped and rotated $135^\circ$ as in Figure [\[fig1\]](#fig1){reference-type="ref" reference="fig1"}, but not scaled. Denote by $\omega_\lambda$ a piecewise linear function with $\omega'_\lambda=\pm 1$ whose graph if given by the upper boundary of $\lambda$ completed by the lines $$v=|u|\,, \quad u\notin[-\lambda'_1,\lambda_1] \,.$$ Then $$k\in\mathcal{D}(\lambda) \Leftrightarrow \omega'_\lambda\Big|_{[k,k+1]}=-1 \,.$$ In other words, if we consider $\omega_\lambda$ as a history of a walk on $\mathbb{Z}$ then $\mathcal{D}(\lambda)$ are those moments when a step is made in the negative direction. It is therefore natural to call $\mathcal{D}(\lambda)$ the *descent set* of $\lambda$. As we shall see, the correspondence $\lambda\mapsto\mathcal{D}(\lambda)$ is a very convenient way to encode the local structure of the boundary of $\lambda$.

The halves in the definition of $\operatorname{Fr}(\lambda)$ have the following interpretation: one splits the diagonal squares in half and gives half to the rows and half to the columns.

::: definition
The correlation functions of $M^\theta$ are the probabilities that the sets $\operatorname{Fr}(\lambda)$ or, similarly, $\mathcal{D}(\lambda)$ contain a fixed subset $X$. More precisely, we set

$$\begin{aligned}
{2}
\rho^\theta(X)&= M^\theta\left(\left\{\lambda\,|\, X\subset \operatorname{Fr}(\lambda)\right\} 
\right)\,,\quad &&X\in\mathbb{Z}+{\textstyle \frac 12}\,,\label{e11a}\\
\boldsymbol{\varrho}^\theta(X)&= M^\theta\left(\left\{\lambda\,|\, X\subset \mathcal{D}(\lambda)\right\} 
\right)\,,\quad &&X\in\mathbb{Z}\,. \label{e0006}
\end{aligned}$$
:::

::: theorem
[]{#t1 label="t1"} For any $X=\{x_1,\dots,x_s\}\subset \mathbb{Z}+{\textstyle \frac 12}$ we have

$$\rho^\theta(X)=
\det \Big[\mathsf{K}(x_i,x_j)\Big]_{1\le i,j \le s}\,,$$

where the kernel $\mathsf{K}$ is given by the following formula

$$\label{e12a}
\mathsf{K}(x,y)=\left\{
\begin{array}{ll}
\displaystyle
\sqrt{\theta}\,\,\frac{\mathsf{k}_+(|x|,|y|)}{|x|-|y|}\,, & xy >0 \,,\\[10pt]
\displaystyle \sqrt{\theta}\,\,\frac{\mathsf{k}_-(|x|,|y|)}{x-y} \,, & xy<0 \,.
\end{array}
\right.$$

The functions $\mathsf{k}_\pm$ are defined by

$$\begin{aligned}
\label{e12} 
\mathsf{k}_+(x,y)&= 
J_{x-\frac 12}\, J_{y+\frac 12}  - J_{x+\frac 12} \, J_{y-\frac 12} \,, \\ 
\mathsf{k}_-(x,y)&= J_{x-\frac 12}\, J_{y-\frac 12}  + J_{x+\frac 12} \, J_{y+\frac 12} \label{e13}\,,
\end{aligned}$$

where $J_x=J_x(2\sqrt{\theta})$ is the Bessel function of order $x$ and argument $2\sqrt{\theta}$.
:::

This theorem is established in Section [\[s21\]](#s21){reference-type="ref" reference="s21"}, see also Remark [\[r11\]](#r11){reference-type="ref" reference="r11"} below. By the complementation principle, see Sections [\[sA3\]](#sA3){reference-type="ref" reference="sA3"} and [\[s21b\]](#s21b){reference-type="ref" reference="s21b"}, Theorem [\[t1\]](#t1){reference-type="ref" reference="t1"} is equivalent to the following

::: theorem
[]{#t1b label="t1b"} For any $X=\{x_1,\dots,x_s\}\subset \mathbb{Z}$ we have

$$\label{e0005}
\boldsymbol{\varrho}^\theta(X)=
\det \Big[\mathsf{J}(x_i,x_j)\Big]_{1\le i,j \le s}\,,$$

Here the kernel $\mathsf{J}$ is given by the following formula

$$\label{e212}
\mathsf{J}(x,y)=\mathsf{J}(x,y;\theta)=\sqrt{\theta}\,\, \frac{J_x\, J_{y+1} - J_{x+1} \, J_{y}}
{x-y} \,,$$

where $J_x=J_x(2\sqrt\theta)$.
:::

::: remark
[]{#r11 label="r11"} Theorem [\[t1\]](#t1){reference-type="ref" reference="t1"} is a limit case of Theorem 3.3 of [@BO]. For the reader's convenience a direct proof of it is given in Section [\[s2\]](#s2){reference-type="ref" reference="s2"}. Another proof of the results of [@BO] will appear in [@BO2]. Various limit cases of the results of [@BO] are discussed in [@BO3]. By different methods, the formula [\[e0005\]](#e0005){reference-type="eqref" reference="e0005"} was obtained by K. Johansson [@J2].

A representation--theoretic proof of a more general formula than Theorem 3.3 of [@BO] has been subsequently given in [@O2].
:::

::: remark
Observe that all Bessel functions involved in the above formulas are of integer order. Also note that the ratios like $\mathsf{J}(x,y)$ are entire functions of $x$ and $y$ because $J_x$ is an entire function of $x$. In particular, the values $\mathsf{J}(x,x)$ are well defined. Various denominator--free formulas for the kernel $\mathsf{J}$ are given in Section [\[s21\]](#s21){reference-type="ref" reference="s21"}.
:::
