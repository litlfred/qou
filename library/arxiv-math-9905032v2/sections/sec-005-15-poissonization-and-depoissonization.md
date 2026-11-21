---
doc_id: arxiv-math-9905032v2
doc_title: "Asymptotics of Plancherel measures for symmetric groups"
section_id: sec-005-15-poissonization-and-depoissonization
section_title: "Poissonization and depoissonization"
section_number: 1.5
pages: 10-11
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.993
doc_brief: "Asymptotics of Plancherel measures for symmetric groups — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
[]{#s15 label="s15"}

We obtain Theorems [\[t2\]](#t2){reference-type="ref" reference="t2"} and [\[t3\]](#t3){reference-type="ref" reference="t3"} from Theorem [\[t1\]](#t1){reference-type="ref" reference="t1"} using the so-called depoissonization techniques. We recall that the fundamental idea of depoissonization is the following.

Given a sequence $b_1,b_2,b_3,\dots$ its *poissonization* is, by definition, the function

$$\label{e18}
B(\theta)=e^{-\theta} \sum_{k=1}^\infty \frac{\theta^k}{k!}\, b_k \,.$$

Provided the $b_k$'s grow not too rapidly this is an entire function of $\theta$. In combinatorics, it is usually called the exponential generating function of the sequence $\{b_k\}$. Various methods of extracting asymptotics of sequences from their generating functions are classically known and widely used, see for example [@V] where such methods are used to obtain the limit shape of a typical partition under various measures on the set of partitions.

A probabilistic way to look at the generating function [\[e18\]](#e18){reference-type="eqref" reference="e18"} is the following. If $\theta\ge 0$ then $B(\theta)$ is the expectation of $b_\eta$ where $\eta\in\{0,1,2,\dots\}$ is a Poisson random variable with parameter $\theta$. Because $\eta$ has mean $\theta$ and standard deviation $\sqrt\theta$, one expects that

$$\label{e19}
B(n) \approx b_n\,, \quad n\to\infty \,,$$

provided the variations of $b_k$ for $|k-n|\le \operatorname{const}\sqrt n$ are small. One possible regularity condition on $b_n$ which implies [\[e19\]](#e19){reference-type="eqref" reference="e19"} is monotonicity. In a very general and very convenient form, a depoissonization lemma for nonincreasing nonnegative $b_n$ was established by K. Johansson in [@J]. We use this lemma in Section [\[s4\]](#s4){reference-type="ref" reference="s4"} to prove Theorem [\[t3\]](#t3){reference-type="ref" reference="t3"}.

Another approach to depoissonization is to use a contour integral

$$\label{e110}
b_n = \frac{n!}{2\pi i} \int_C \frac{B(z)\, e^{z}}{z^n} \,  \frac{dz}{z} \,,$$

where $C$ is any contour around $z=0$. Suppose, for a moment, that $b_n$ is constant $b=b_n=B(z)$. The function $e^z/z^n=e^{z-n\ln z}$ has a unique critical point $z=n$. If we choose $|z|=n$ as the contour $C$, then only neighborhoods of size $|z-n|\le \operatorname{const}\sqrt{n}$ contribute to the asymptotics of [\[e110\]](#e110){reference-type="eqref" reference="e110"}. Therefore, for general $\{b_n\}$, we still expect that provided the overall growth of $B(z)$ is under control and the variations of $B(z)$ for $|z-n| \le \operatorname{const}\sqrt n$ are small, the asymptotically significant contribution to [\[e110\]](#e110){reference-type="eqref" reference="e110"} will come from $z=n$. That is, we still expect [\[e19\]](#e19){reference-type="eqref" reference="e19"} to be valid. See, for example, [@JS] for a comprehensive discussion and survey of this approach.

We use this approach to prove Theorem [\[t2\]](#t2){reference-type="ref" reference="t2"} in Section [\[s3\]](#s3){reference-type="ref" reference="s3"}. The growth conditions on $B(z)$ which are suitable in our situation are spelled out in Lemma [\[l31\]](#l31){reference-type="ref" reference="l31"}.

In our case, the functions $B(\theta)$ are combinations of the Bessel functions. Their asymptotic behavior as $\theta\approx n \to\infty$ can be obtained directly from the classical results on asymptotics of Bessel functions which are discussed, for example, in the fundamental Watson's treatise [@W]. These asymptotic formulas for Bessel functions are derived using the integral representations of Bessel functions and the steepest descent method. The different behavior of the asymptotics in the bulk $(-2,2)$ of the spectrum, near the edges $\pm 2$ of the spectrum, and outside of $[-2,2]$ is produced by the different location of the saddle point in these three cases.
