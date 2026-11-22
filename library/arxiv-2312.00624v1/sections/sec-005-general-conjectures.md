---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-005-general-conjectures
section_title: "General conjectures"
section_number: null
pages: 9-12
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.904
latex_coverage_ratio: 0.992
doc_brief: "On the structure of wave functions in complex Chern–Simons theory — We study the structure of wave functions in complex Chern–Simons theory on the complement of a hyperbolic knot, emphasizing the"
---
[]{#sec: conjectures label="sec: conjectures"} Our *first claim* is that the WKB expansion in Eq. [\[WKB\]](#WKB){reference-type="eqref" reference="WKB"} can be resummed at all orders in $\hbar$ and order by order in $X={\rm e}^{2 \pi {\mathsf{b}}u}$. Explicitly, for a fixed choice of $\alpha$, we have that

$$\label{WKB-conj}
\chi^{(\alpha), \rm{WKB}} (u; \hbar)=\exp \left(  {{\rm i}\over \hbar} s^{(\alpha)}_0(x) + s^{(\alpha)}_1(x) + \phi^{(\alpha), \rm{WKB}}(X;q) \right) \, ,$$

where $s^{(\alpha)}_{0,1}(x)$ are ${\mathbb R}$-polynomials in the variable[^1] $x= \log X$ and $$\label{phi-struc}
\phi^{(\alpha), \rm{WKB}}(X;q) = \sum_{n \ge 1} a^{(\alpha)}_n(q) X^n + a^{(\alpha)}_{-n}(q) X^{-n} \, .$$

The coefficient functions $a^{(\alpha)}_{\pm n}(q)$ can be written as $$\label{ahatf-def}
a^{(\alpha)}_{\pm n}(q)= {\hat{a}_{\pm n}^{(\alpha)} (q) \over n (q^n-1) q^{\sigma_{\alpha, \pm n}}} \, , \quad n \in {\mathbb Z}_{>0} \, ,$$ where $\hat{a}^{(\alpha)}_{\pm n} (q) \in {\mathbb Z}[q]$ such that $$\hat{a}^{(\rm{geom})}_{- n} (q) = 0 \, , \quad n \in {\mathbb Z}_{>0} \, ,$$ and $\sigma_{\alpha, m}$ is a function of $m \in {\mathbb Z}_{\ne 0}$ which takes values in ${\mathbb N}$, depends on the choice of classical branch $\alpha$, and satisfies $$\sigma_{{\rm geom}, m} = 0 \, ,  \quad \sigma_{\alpha, - |m|} = 0 \, \quad \forall \alpha \, .$$ Note that we use the same notation for the perturbative WKB series in Eq. [\[WKB\]](#WKB){reference-type="eqref" reference="WKB"} and its resummation in terms of $q$ in Eq. [\[WKB-conj\]](#WKB-conj){reference-type="eqref" reference="WKB-conj"}. However, in the rest of this paper, we will always refer to the resummed version of $\chi^{(\alpha), \rm{WKB}} (u; \hbar)$ as in Eq. [\[WKB-conj\]](#WKB-conj){reference-type="eqref" reference="WKB-conj"}.

In fact, there is additional structure in the resummed perturbative wave function. Our *second claim* is that $\phi^{(\alpha), \rm{WKB}}(X;q)$ has an integrality/multicovering-type structure. Namely, for a fixed choice of $\alpha$, we have that $$\label{multi-conj}
\phi^{(\alpha), \rm{WKB}}(X;q)= \sum_{k, s\ge 1}{D^{(\alpha)}_s(q^k) \over k (q^k-1) q^{k \sigma_{\alpha, s}}} X^{s k} + {D^{(\alpha)}_{-s}(q^k) \over k (q^k-1) q^{k \sigma_{\alpha, -s}}} X^{- s k} \, ,$$

where $D^{(\alpha)}_{\pm s}(q) \in {\mathbb Z}[q]$. Equivalently, we can write the coefficient functions from Eq. [\[phi-struc\]](#phi-struc){reference-type="eqref" reference="phi-struc"} as

$$\label{struc-an}
 a^{(\alpha)}_{\pm n}(q)= \sum_{k|n} {D^{(\alpha)}_{\pm {n \over k}}(q^k) \over k(q^k-1) q^{k \sigma_{\alpha, \pm {n \over k}}}} \, , \quad n \in {\mathbb Z}_{>0} \, ,$$

where the sum runs over all positive integer divisors of $n$.

Since the following discussion holds for all non-abelian choices of the classical branch, let us now drop the explicit dependence on $\alpha$ to simplify the notation and introduce

$$\label{Dtilde1}
{\tilde{D}}_{\pm s}(q)= {D_{\pm s}(q) \over (q-1) q^{\sigma_{\pm s}}} \, , \quad s \in {\mathbb Z}_{>0} \, .$$

As a consequence of Eq. [\[multi-conj\]](#multi-conj){reference-type="eqref" reference="multi-conj"}, we can write

$$\label{Exp}
\begin{aligned}
\exp \left( \phi^{\rm WKB}(X;q) \right)=& \exp\left( \sum_{k, s\ge 1} {1 \over k} {\tilde{D}}_s(q^k) X^{sk} \right) \exp\left( \sum_{k, s\ge 1} {1 \over k} {\tilde{D}}_{-s}(q^k) X^{-sk} \right) \\
=& {\rm Exp}_{X,q}\left( \sum_{s\ge 1} {\tilde{D}}_s(q) X^s \right) {\rm Exp}_{X,q}\left( \sum_{s\ge 1} {\tilde{D}}_{-s}(q) X^{-s} \right) \, , 
\end{aligned}$$

where ${\rm Exp}_{X,q}$ is the plethystic exponential in the variables $X, q$. See, *e.g.*, [@lm-pv]. It follows that we can extract the functions ${\tilde{D}}_{\pm s}(q)$ by applying the plethystic logarithm in the same two variables, which we denote by ${\rm Log}_{X,q}$, to both sides of Eq. [\[Exp\]](#Exp){reference-type="eqref" reference="Exp"}. Specifically, we find that

$$\sum_{s\ge 1} {\tilde{D}}_{\pm s}(q) X^{\pm s}={\rm Log}_{X,q} \left( \exp\left( \sum_{n \ge 1} a_{\pm n}(q) X^{\pm n}\right) \right)= \sum_{k, n\ge 1} {\mu(k) \over k} a_{\pm n} (q^k) X^{\pm n k} \, ,$$

where $\mu(k)$ is the Möbius function, which leads to the closed formula

$$\label{Dtilde2}
{\tilde{D}}_{\pm s}(q)= \sum_{k|s}  {\mu(k) \over k} a_{\pm {s\over k}} (q^k) \, , \quad s \in {\mathbb Z}_{>0} \, .$$ Note that this is the formal inverse of Eq. [\[struc-an\]](#struc-an){reference-type="eqref" reference="struc-an"}, which can be equivalently written as

$$\label{struc-an2}
a_{\pm n}(q)= \sum_{k|n} {1 \over k} {\tilde{D}}_{\pm {n\over k}}(q^k) \, , \quad n \in {\mathbb Z}_{>0} \, .$$

We comment that, in both examples of the figure-eight and the three-twist knots studied in Section [\[sec: examples\]](#sec: examples){reference-type="ref" reference="sec: examples"}, we have precise expressions for $\sigma_{\alpha, m}$ for all choices of $\alpha \ne \rm{geom}$, which are given in Eqs. [\[sigma41\]](#sigma41){reference-type="eqref" reference="sigma41"}, [\[sigma52\]](#sigma52){reference-type="eqref" reference="sigma52"}, and [\[sigma52self\]](#sigma52self){reference-type="eqref" reference="sigma52self"}. Moreover, our statements above simplify notably in the particular case of the geometric branch, whose function $\phi^{(\rm{geom}), \rm{WKB}}(X;q)$ has a series expansion including only the positive powers of $X$ and whose coefficients $a^{(\rm{geom})}_{n}(q)$ have a trivial factor of $q^{\sigma_{{\rm geom}, n}}=1$ in the denominator.

Let us explain how our conjectures originate from insights from the TS/ST correspondence. See [@mmrev] for a review and further references. In the context of the TS/ST correspondence, the analog of the AJ conjecture for the wave function in Eq. [\[AJ-eq\]](#AJ-eq){reference-type="eqref" reference="AJ-eq"} is given by the quantization of the mirror curve to a toric Calabi--Yau threefold, which defines a spectral problem. Its wave function can be computed in the WKB approximation as a formal power series in $\hbar$. It was noted in [@kpamir; @mz-wv] that this $\hbar$-expansion can be suitably resummed, producing the same picture that we have described in our claims above. This structure is similar to the one appearing in perturbative open topological string theory [@ov; @lmv], but it is slightly less constrained. Specifically, one has the structure of [@ov] but not the more detailed substructure found in [@lmv]. The integrality property in Eq. [\[multi-conj\]](#multi-conj){reference-type="eqref" reference="multi-conj"} defines what is called an *admissible series* in [@ks][^2] and is found in other examples like, *e.g.*, in [@as].

We can now ask how the resummed, perturbative partition functions in Eq. [\[WKB-conj\]](#WKB-conj){reference-type="eqref" reference="WKB-conj"} relate to the exact partition function $\chi(u;\hbar)$ described in Section [\[sec: theory\]](#sec: theory){reference-type="ref" reference="sec: theory"}. It follows both from physical arguments [@bdp] and from explicit calculations [@gk-qseries; @dimofte-levelk; @ggm2] that the exact wave function can be decomposed as

$$\label{exactconj}
\chi(u; \hbar)=\sum_{\alpha} \mathsf{C}_\alpha \, {\cal S}^{(\alpha)} (X; q){\cal S}^{(\alpha)} (X_D;q_D) \, ,$$

where the sum runs over the different branches of the classical $A$-polynomial labeled by $\alpha$, $\mathsf{C}_\alpha$ is an appropriate complex constant, and ${\cal S}^{(\alpha)} (X; q)$ is known as *holomorphic block*. Since the holomorphic block must reproduce the perturbative expansion of the wave function, it can be identified with the resummed WKB series in Eq. [\[WKB-conj\]](#WKB-conj){reference-type="eqref" reference="WKB-conj"}, that is,

$$\label{block-resummed}
{\cal S}^{(\alpha)} (X; q) = \exp \left(\frac{{\rm i}}{\hbar} s^{(\alpha)}_0(x) +  s^{(\alpha)}_1(x) + \phi^{(\alpha), \rm{WKB}}(X;q)\right) \, .$$

Therefore, our conjecture in Eq. [\[multi-conj\]](#multi-conj){reference-type="eqref" reference="multi-conj"} implies that holomorphic blocks in complex CS theory have the stated integrality/multicovering property, *i.e.*, they are admissible series in the Kontsevich--Soibelman sense. This could have been anticipated from the relation between holomorphic blocks and open topological string partition functions in some examples [@bdp]. Indeed, we will show in Section [\[sec: examples\]](#sec: examples){reference-type="ref" reference="sec: examples"} that, starting from the known closed expression for the holomorphic and antiholomorphic blocks, we can successfully verify the integrality structure of Eq. [\[multi-conj\]](#multi-conj){reference-type="eqref" reference="multi-conj"} in the examples of the figure-eight and the three-twist knots for all choices of the saddle connection $\alpha$.

Let us comment that the structure in Eqs. [\[exactconj\]](#exactconj){reference-type="eqref" reference="exactconj"}, [\[block-resummed\]](#block-resummed){reference-type="eqref" reference="block-resummed"} is again similar to what has been found in the open TS/ST correspondence [@kpamir; @mz-wv; @mz-wv2; @szabolcs; @fgrassi]: the exact wave functions are given by sums of products of the resummed WKB wave functions and their duals[^3].

As we mentioned in Section [\[sec: intro\]](#sec: intro){reference-type="ref" reference="sec: intro"}, a structure similar to the one in Eq. [\[phi-struc\]](#phi-struc){reference-type="eqref" reference="phi-struc"} has already been conjectured in [@ekholm], where the resummed WKB expansion is obtained by solving directly the quantized $A$-polynomial equation. The approach of [@ekholm] does not appeal to the decomposition into holomorphic blocks, and our explicit results for the resummation of the WKB expansion in the case of, *e.g.*, the figure-eight knot in Section [\[sec: examples\]](#sec: examples){reference-type="ref" reference="sec: examples"} appear to be different from those in [@ekholm][^4].

[^1]: The $S$-dual image of $x$ is $x_D = \log X_D = 2 \pi x /\hbar$.

[^2]: We thank Stavros Garoufalidis for pointing this out to us.

[^3]: In the TS/ST correspondence, one can also define *off-shell* wave functions, in which case the dual blocks differ from the original ones.

[^4]: One reason for this difference, which was pointed out to us by Sergei Gukov, is that the results of [@ekholm] involve the super $A$-polynomial, and they might lead to a different specialization for $\text{SL}(2,{\mathbb C})$.
