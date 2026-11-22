---
doc_id: arxiv-1404.2541v1
doc_title: "The Stokes phenomenon for the Ramanujan’s q -diﬀerence equation and its higher order extension"
section_id: sec-005-6-the-q-borel-laplace-transformations
section_title: "The q-Borel-Laplace transformations"
section_number: 6
pages: 13-15
source_pdf: 1404.2541v1.pdf
source_sha256: edb7c9b2b1561ac3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.985
doc_brief: "The Stokes phenomenon for the Ramanujan’s q -diﬀerence equation and its higher order extension — We show connection formulae of local solutions of the Ramanu- jan equation between the origin and the"
---
In this section, we show a connection formula of the divergent series ${}_2\varphi_0$. This series appears in the second solution of the Ramanujan equation [\[ram\]](#ram){reference-type="eqref" reference="ram"}. At first, we define two types of the $q$-Borel-Laplace transformations.

**Definition.** *We assume that $f(x)$ is a formal power series $f(x)=\sum_{n\ge 0}a_nx^n$, $a_0=1$.*

1.  The $q$-Borel transformation of the first kind is $$\left(\mathcal{B}_q^+f\right)(\xi ):=\sum_{n\ge 0}a_nq^{\frac{n(n-1)}{2}}\xi^n\left(=:\varphi (\xi )\right).$$

2.  The $q$-Laplace transformation of the first kind is $$\left(\mathcal{L}_{q, \lambda}^+\varphi\right)(x):=
    \frac{1}{1-q}\int_0^{\lambda\infty}\frac{\varphi (\xi )}{\theta_q\left(\frac{\xi}{x}\right)}\frac{d_q\xi}{\xi}=\sum_{n\in\mathbb{Z}}\frac{\varphi (\lambda q^n)}{\theta_q\left(\frac{\lambda q^n}{x}\right)},$$ here, this transformation is given by Jackson's $q$-integral [@GR].

We also define the $q$-Borel-Laplace transformations of the second kind as follows:

1.  The $q$-Borel transformation of the second kind is $$(\mathcal{B}_q^-f)(\xi ):=\sum_{n\ge 0}a_nq^{-\frac{n(n-1)}{2}}\xi^n\left(=:g(\xi )\right).$$

2.  The $q$-Laplace transformation of the second kind is $$\left(\mathcal{L}_q^-g\right)(x):=\frac{1}{2\pi i}\int_{|\xi |=r}g(\xi )\theta_q\left(\frac{x}{\xi }\right)\frac{d\xi}{\xi},$$ where $r>0$ is enough small number.

We remark that the $q$-Borel transformation $\mathcal{B}_q^+$ is formal inverse of the $q$-Laplace transformation $\mathcal{L}_{q,\lambda }^+$ as follows;

::: lmm
For any entire function $f(x)$, we have $$\mathcal{L}_{q, \lambda}^+\circ\mathcal{B}_q^+f=f.$$
:::

The $q$-Borel transformation $\mathcal{B}_q^-$ also can be considered as a formal inverse of the $q$-Laplace transformation.

::: lmm
We assume that the function $f$ can be $q$-Borel transformed to the analytic function $g(\xi )$ around $\xi =0$. Then, we have $$\mathcal{L}^-_q\circ\mathcal{B}^-_qf=f.$$
:::

::: proof
*Proof.* We can prove this lemma calculating residues of the $q$-Laplace transformation around the origin. ◻
:::

The $q$-Borel transformation $\mathcal{B}_q^-$ has following operational relation.

::: lmm
[]{#orqb label="orqb"} For any $l,m\in\mathbb{Z}_{\ge 0}$, $$\mathcal{B}_q^-(t^m\sigma_q^l)=q^{-\frac{m(m-1)}{2}}\tau^m\sigma_q^{l-m}\mathcal{B}_q^-.$$
:::

In the following subsection, we apply these resummation methods to deal with the connection problem.
