---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-001-11-preliminaries
section_title: "Preliminaries"
section_number: 1.1
pages: 2-4
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.921
latex_coverage_ratio: 0.992
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
The *$\Gamma$-function* is among the most fundamental and ubiquitous special functions and may be defined via the Euler integral $\Gamma(x) := \int_{0}^{\infty} u^{x-1} e^{-u} \, du$ for $\Re(x) > 0$ [@Rainville1960 §2]. The *beta integral* is of basic importance as a special function, in much the same way as the $\Gamma$-function, and may be defined so that $$\label{betadefinition}
 B(p, q) := \int_{0}^{1} t^{p-1} (1-t)^{q-1} \, dt$$ for $\Re(p) > 0$ and $\Re(q) > 0$ [@Rainville1960 §2.16], so that $$\label{betaevaluate}
 B(p, q) = \frac{ \Gamma(p) \Gamma(q) }{ \Gamma(p + q)},$$ again for $\Re(p) > 0$ and $\Re(q) > 0$. Our main family of dilogarithm identities is derived, as below, using [\[betadefinition\]](#betadefinition){reference-type="eqref" reference="betadefinition"} together with the families of sextic integrals shown in Section [\[sectionsextic\]](#sectionsextic){reference-type="ref" reference="sectionsextic"} below.

The *dilogarithm function* is a central object of study in our work and is given by the $m = 2$ case of the *polylogarithm function* such that $\operatorname{Li}_{m}(x) := \sum_{n=1}^{\infty} \frac{x^{n}}{n^m}$ for complex $x$ such that $|x| \leq 1$. For a full review of background material on the dilogarithm, we again refer to the seminal monographs due to Lewin concerning this function [@Lewin1958; @Lewin1981; @Lewin1991text]. By writing $$\label{RogersLdefinition}
 L(x) := \frac{6}{\pi^2} \left( \operatorname{Li}_{2}(x) + \frac{1}{2} \ln x \ln(1-x) \right)$$ to denote the Rogers $L$-function, a version of the five-term (Abel) functional equation such that $$L(x) + L(y) = L(x y) + 
 L\left( \frac{x(1-y)}{1- x y} \right) + L\left( \frac{y(1-x)}{1-xy} \right)$$ is to be applied in our work. Other fundamental functional equations for the dilogarithm that are to arise in our work include the duplication formula such that $$\label{duplicationformula}
 2 \operatorname{Li}(x) + 2 \operatorname{Li}(-x) = \operatorname{Li}(x^{2}),$$ together with Euler's reflection identity such that $$\label{Eulerreflectionidentity}
 \operatorname{Li}_2(x) = -\operatorname{Li}_2(1 - x) + \frac{\pi^2}{6} - \ln(x) \ln(1 - x),$$ along with Landen's dilogarithm identity such that $$\label{Landenformula}
 \operatorname{Li}_{2}(-x) = -\operatorname{Li}_{2}\left( \frac{x}{1+x} \right) - \frac{1}{2} \ln^2(1+x).$$ In addition to the Rogers $L$-function defined in [\[RogersLdefinition\]](#RogersLdefinition){reference-type="eqref" reference="RogersLdefinition"}, there are a number of well known special functions that are closely related to $\operatorname{Li}_{2}$ and that are to be involved in our work. This includes the *inverse tangent integral* function $\text{Ti}_{2}$ [@Lewin1981 §2] such that $$\text{Ti}(x) = \frac{1}{2i} \left( \operatorname{Li}_{2}(i 
 x) - \operatorname{Li}_{2}(-ix) \right) = \int_{0}^{x} \frac{ \operatorname{arctan} \, t}{t} \, dt$$ for $|x| \leq 1$, together with the *Legendre chi-function* $\chi_2$ [@Lewin1981 §1.8] such that $$\chi_{2}(x) = \frac{1}{2} \operatorname{Li}_{2}(x) - 
 \frac{1}{2} \operatorname{Li}_{2}(-x) = \frac{1}{2} \int_{0}^{x} \ln\left( \frac{1+t}{1-t} \right) \frac{dt}{t}$$ for $|x| \leq 1$, along with the *Clausen function* $\text{Cl}_{2}$ [@Lewin1981 §4] such that $$\text{Cl}_{2}(x) = \sum_{n=1}^{\infty} \frac{\sin n 
 x}{n^2} = -\int_{0}^{x} \ln\left( 2 \sin \frac{t}{2} \right) \, dt$$ for $|x| \leq 1$.

Mathematical objects referred to as *dilogarithm ladders* are a main object to be explored in this paper, and our main results include new ladder relations, inspired by the recent work of Campbell [@Campbell2025] on dilogarithm ladders. As in this work by Campbell [@Campbell2025], we reproduce the standard definition of a polylogarithm *ladder* of a given weight $n$ and index $N$ and $\mathbb{Q}$-algebraic argument $u$, and this refers to an expression of the form $$\label{ladderdefinition}
 L_{n}(N, u) := \frac{\operatorname{Li}_{n}\left( u^{N} \right)}{N^{n - 1} } - \left( \sum_{r=0}^{N-1} \frac{A_{r} 
 \operatorname{Li}_{n}\left( u^{r} \right)}{r^{n-1}} + \frac{A_{0} \ln^{n}(u)}{n!} \right)$$ for rational values $A_{r}$ such that the right-hand side of [\[ladderdefinition\]](#ladderdefinition){reference-type="eqref" reference="ladderdefinition"} reduces to $$\label{Dscalar}
 L_{n} = \sum_{m=2}^{n} \frac{ D_{m} \ln^{n-m}(u) }{(n-m)!}$$ for scalar coefficients $D_{m}$ [@Lewin1991text p. 6]. If such scalars are rational, then the ladder relation given by $L_{n}(N, 
 u)$ reducing to [\[Dscalar\]](#Dscalar){reference-type="eqref" reference="Dscalar"} is said to be *valid*. The valid ladder relations that we introduce as main results appear to be inequivalent to previously known ladder relations, and we invite the interested reader to review past and notable references related to polylogarithm ladders [@AbouzahraLewinXiao1987; @CohenLewinZagier1992; @Gangl2013; @Lewin1993; @Lewin1986; @Lewin1991collection].
