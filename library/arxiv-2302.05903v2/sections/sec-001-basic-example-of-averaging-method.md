---
doc_id: arxiv-2302.05903v2
doc_title: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials"
section_id: sec-001-basic-example-of-averaging-method
section_title: "Basic example of averaging method"
section_number: null
pages: 3-4
source_pdf: 2302.05903v2.pdf
source_sha256: 9a17abd36cc8a317
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.934
doc_brief: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials — We elaborate on the recent suggestion to consider averaging of Cauchy identities"
---
Eq.([\[gendia\]](#gendia){reference-type="ref" reference="gendia"}) counts Young diagrams, or the ordered integer partitions, while ([\[Cauchy\]](#Cauchy){reference-type="ref" reference="Cauchy"}) is the Cauchy identity for the Schur functions, i.e. for the characters of linear groups $GL_N$. Technically, upon choosing $p_k=\bar p_k=\delta_{k,1}$ in ([\[Cauchy\]](#Cauchy){reference-type="ref" reference="Cauchy"}), the difference between the two formulas is in the power of $d_R:=S_R\{\delta_{k,1}\}$: they are the sums of $d_R^0$ and $d_R^2$, accordingly. Generally, $|R|!\cdot d_R={\rm dim}_R$ are *integer*-valued dimensions of representations of the symmetric group ${\cal S}_{|R|}$ [@Fulton], and the sum $$\begin{aligned}
\xi_m:=\sum_R q^{|R|} d_R^m = \sum_R q^{|R|}\frac{{\rm dim}_R^m}{(|R|!)^m}
\label{dimrep}
\end{aligned}$$ looks somewhat terrible. The first terms in ([\[dimrep\]](#dimrep){reference-type="ref" reference="dimrep"}) are $$\begin{aligned}
\xi_m = 1 + q + \frac{2}{(2!)^m} q^2
+ \frac{2^m+2}{(3!)^m} q^3
+ \frac{2\cdot 3^m+2^m+2}{(4!)^m} q^4
+ \frac{6^m+2\cdot 5^m +2\cdot 4^m+2}{(5!)^m} q^5 +
\nonumber\\
+ \frac{16^m+2\cdot 10^m+2\cdot 9^m+4\cdot 5^m+2}{(6!)^m} q^6
+ \frac{2\cdot 35^m+2\cdot 21^m + 20^m +2\cdot 15^m +4\cdot 14^m+2\cdot 6^m+2}{(7!)^m} q^7 +
\nonumber\\
+ \frac{90^m + 2\cdot 70^m+2\cdot 64^m+2\cdot 56^m+42^m + 2\cdot 35^m +2\cdot 28^m +2\cdot 21^m + 2\cdot 20^m
+ 2\cdot 14^m+2\cdot 7^m+2}{(8!)^m} q^8 +
\nonumber
\end{aligned}$$ $$\begin{aligned}
+ \ldots
\label{xim}
\end{aligned}$$ The more surprising is that, at some particular values of $m$, one gets sensible formulas.

The best known is the quadratic case, $m=2$, where the generic theory of finite groups implies that the sum of the squared dimensions is always a dimension of the group. In the case of ${\cal S}_r$, this gives $$\begin{aligned}
\sum_{R\vdash r}  {\rm dim}_R^2 = r!
\end{aligned}$$ and leads to the particular case of ([\[Cauchy\]](#Cauchy){reference-type="ref" reference="Cauchy"}) $$\begin{aligned}
\xi_2=
\sum_R q^{|R|} S_R\{\delta_{k,1}\}^2 = \sum_R q^{|R|} d_R^2 = e^{q}
\label{0powerdR}
\end{aligned}$$

For $m=0$, one gets a far more transcendental, still comprehensible formula ([\[gendia\]](#gendia){reference-type="ref" reference="gendia"}), which just counts the numbers of representations of ${\cal S}_{|R|}$.

Amusingly, the case of $m=1$ is also simple: $$\begin{aligned}
\Sigma_n=\sum_{R\vdash n}q^n {\rm dim}_R=n!\sum_{R\vdash n}q^n d_R
\end{aligned}$$ gives rise to sequence A000085 from [@seqs] which counts the numbers of Young *tableaux* of a given size $r$, and this is in perfect accordance with the fact that the dimension ${\rm dim}_R$ is equal to the number of Young *tableaux* associated with the diagram $R$. For the exponential generating function of this sequence, see [@seqs sequence A000085 and references therein], $$\begin{aligned}
\xi_1 =
\sum_R q^{|R|}d_R = \sum_{n=0}^\infty{\Sigma_n\over n!} = e^{q+\frac{q^2}{2}}
\label{1powerdR}
\end{aligned}$$ Moreover, this sum can be lifted to a sum of single(!) Schur functions $$\begin{aligned}
\boxed{
\sum_R q^{|R|}  S_R\{p\} =
\sum_R q^{|R|}  S_R\{p\} \underbrace{\left<S_R\{\bar p\}\right>^{\bf\!A}_{\!\bar p}}_{1}
\ \stackrel{(\ref{Cauchy})}{=}\
\left<\exp\left(\sum_{k=1}^\infty\frac{q^kp_k\bar p_k}{k}\right)\right>^{\bf\!A}_{\bar p}=
\exp\left\{\sum_{k=1}^\infty \left(q^{2k}\frac{p_k^2}{2k}
+ q^{2k-1}\frac{p_{2k-1}}{2k-1}\right)\right\}
}
\label{idlinSchur}
\end{aligned}$$ In the language of [@2212.04859], this follows from taking average of the Cauchy identity ([\[Cauchy\]](#Cauchy){reference-type="ref" reference="Cauchy"}) over the variables $\bar p_k$ with the measure $$\begin{aligned}
\label{Gm}
\text{\bf Measure A:} \ \ \ \ \ \ \ \ \
\Big<S_R\Big>^{\bf\!A}=1: && \ \ \ \ \ \ \
d\mu^{\bf A} \sim \prod_{k=1}^\infty dp_k\exp\left(-\frac{(p_{2k-1}-1)^2}{2(2k-1)} - \frac{p_{2k}^2}{4k}\right)
\end{aligned}$$ Hereafter, the average with a given measure $d\mu$ over variables $p_k$, $k=1,2,\ldots$ is defined as $$\begin{aligned}
\label{average}
\Big< f(\{p_k\})\Big>:=\int_{-\infty}^{\infty} d\mu f(\{p_k\})
\end{aligned}$$ and normalized in such a way that $\Big<1\Big>=1$.

Average ([\[Gm\]](#Gm){reference-type="ref" reference="Gm"}) converts the Schur polynomials into 1, $\left<\bar S_R\{\bar p\}\right>^{\bf\!A}=1$, and is Gaussian, so it is trivial to take averages of the r.h.s. of ([\[Cauchy\]](#Cauchy){reference-type="ref" reference="Cauchy"}), $$\begin{aligned}
\left<\exp\left(\sum_{k=1}^\infty\frac{q^k p_k\bar p_k}{k}\right)\right>^{\bf\!A}_{\!\bar p}
\sim \prod_{k=1}^\infty \left(\int e^{\frac{q^{2k-1} p_{2k-1}\bar p_{2k-1}}{2k-1}}
e^{-\frac{(\bar p_{2k-1}-1)^2}{2(2k-1)}} d\bar p_{2k-1}
\int e^{\frac{q^{2k} p_{2k}\bar p_{2k}}{2k}}
e^{-\frac{\bar p_{2k}^2}{4k}} d\bar p_{2k}
\right)
\end{aligned}$$ is just the r.h.s. of ([\[idlinSchur\]](#idlinSchur){reference-type="ref" reference="idlinSchur"}).

The sum ([\[1powerdR\]](#1powerdR){reference-type="ref" reference="1powerdR"}) can be also represented as $$\begin{aligned}
\sum_R q^{|R|}d_R = \sum_R q^{R} S_R\{\delta_{k,1}\}\underbrace{\left<S_R\{\bar p_k\}\right>^{\bf\!A}_{\bar p}}_{1}
\ \stackrel{(\ref{Cauchy})}{=} \
\left<e^{ q\bar p_1}\right>^{\bf\!A} = \sum_{r=0}^\infty \frac{q^r \!\left<\bar p_1^r\right>^{\bf\!A}}{r!}
\end{aligned}$$ i.e. $$\begin{aligned}
r!\cdot \sum_{R\vdash r}  d_R = \left< p_1^r\right>^{\bf\!A}
\end{aligned}$$

Note that while ([\[gendia\]](#gendia){reference-type="ref" reference="gendia"}) is a generating function for numbers of Young diagrams, ([\[1powerdR\]](#1powerdR){reference-type="ref" reference="1powerdR"}) is an *exponential* (i.e. weighted with additional factors $\frac{1}{r!}$) generating function for numbers of Young *tableaux*.

Another important difference between counting diagrams and tables is that the latter, being related to dimensions, admit a quantum deformation, see sec.[\[Mac\]](#Mac){reference-type="ref" reference="Mac"} below.

According to [@seqs], no interpretations for $\xi_m$ are yet known for $m\geq 3$.
