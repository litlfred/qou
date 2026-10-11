---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-004-15-second-main-result-polynomiality-of-structure
section_title: "Second main result: polynomiality of structure constants of Jack characters"
section_number: 1.5
pages: 10-12
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.994
---
[]{#subsect:Second_Main_Result label="subsect:Second_Main_Result"} It follows from the work of Lassalle -- see Proposition [\[prop:Jack-characters-basis\]](#prop:Jack-characters-basis){reference-type="ref" reference="prop:Jack-characters-basis"} -- that the functions $\mathop{\mathrm{Ch}}_{\mu}^{(\alpha)}$ span linearly the algebra of $\alpha$-polynomial functions denoted by $\Lambda_\star^{(\alpha)}$ (when $\mu$ runs over integer partitions of all sizes). Hence, there exist some rational numbers $g^{(\alpha)}_{\mu,\nu;\pi}$, depending on $\alpha$ such that $$\label{eq:definition-structure-constants}
    \mathop{\mathrm{Ch}}^{(\alpha)}_\mu \cdot \mathop{\mathrm{Ch}}^{(\alpha)}_\nu =\sum_{\substack{\pi \text{ partition} \\ \text{of any size}}} 
    g^{(\alpha)}_{\mu,\nu;\pi} \mathop{\mathrm{Ch}}^{(\alpha)}_\pi.$$ These numbers are often called *structure constants* of the basis $(\mathop{\mathrm{Ch}}_{\mu}^{(\alpha)})$. It is a worthy goal to understand them, because they describe the multiplicative structure of the algebra.

Our second main result is a polynomiality result for these structure constants with precise bounds on the degree: let $$\begin{aligned}
    n_1(\mu) &= |\mu|+\ell(\mu), \\
    n_2(\mu) &= |\mu|-\ell(\mu), \\
    n_3(\mu) &= |\mu|-\ell(\mu)+m_1(\mu).
\end{aligned}$$ Then we have:

::: theorem
[]{#theo:struct-const label="theo:struct-const"} Fix three partitions $\mu$, $\nu$ and $\pi$. The structure constant $g^{(\alpha)}_{\mu,\nu;\pi}$ is a polynomial in $\gamma={\sqrt{\alpha}}^{-1}-\sqrt{\alpha}$ with rational coefficients and of degree at most $$\min_{i=1,2,3} n_i(\mu) + n_i(\nu) - n_i(\pi).$$ Moreover, if $n_1(\mu) + n_1(\nu) - n_1(\pi)$ is even (respectively, odd), it is an even (respectively, odd) polynomial.
:::

### Other applications of the second main result {#subsect:other_applications}

In addition of the main purpose of this paper, Theorem [\[theo:struct-const\]](#theo:struct-const){reference-type="ref" reference="theo:struct-const"} can be applied to several different problems from the literature.

-   It contains a fifty-year old result from Farahat and Higman, stating that the structure constants of the center of the symmetric group algebra behave polynomially in $n$ [@FarahatHigmanCentreQSn].

-   A natural analog of the center of the symmetric group algebra is the Hecke algebra of the pair $(S_{2n},H_n)$, see *e.g.* [@Macdonald1995 Section 7.2] for an introduction to it. Theorem [\[theo:struct-const\]](#theo:struct-const){reference-type="ref" reference="theo:struct-const"} implies also an analog of Farahat and Higman's result in this context: up to some explicit normalization factor, structure constants also behave polynomially in $n$[^1]. The same result has been proved independently by Tout [@Tout-Structure-constant-S2n-Hn].

-   Goulden and Jackson [@GouldenJacksonMatchingJack], have defined, using Jack polynomials, an interpolation between the structure constants of both algebras. By construction, these quantities are rational functions in $\alpha$ but they were conjectured to be in fact polynomials in $\alpha-1$ with non-negative integer coefficients having some combinatorial interpretation [@GouldenJacksonMatchingJack Section 4]. Here, we prove that they are *polynomials* in $\alpha$ (or equivalently in $\alpha-1$) with rational coefficients. Unfortunately, we are not able to prove either the integrity or the positivity of the coefficients.

-   We are also able to prove two conjectures of Matsumoto [@MatsumotoOddJM Section 9], arising in the context of matrix integrals (Section [\[SubsectMatsumoto\]](#SubsectMatsumoto){reference-type="ref" reference="SubsectMatsumoto"}).

-   We can give a short proof of a recent result of Vassilieva [@VassilievaJack] which generalizes a famous result of Dénes [@Denes1959] for the number of *minimal* factorizations of a cycle in the symmetric group.

The link between our main result and the first two items is presented in Section [\[SectSpecialValues\]](#SectSpecialValues){reference-type="ref" reference="SectSpecialValues"}, while the connection with the last three items is explained in Appendix [\[app:Matching-Jack_And_Matsumoto\]](#app:Matching-Jack_And_Matsumoto){reference-type="ref" reference="app:Matching-Jack_And_Matsumoto"}.

### Tool: Kerov's polynomial for Jack characters

Let us now say a word about the proof of our second main result.

The algebra $\Lambda_\star^{(\alpha)}$, linearly spanned by the functions $\mathop{\mathrm{Ch}}_\mu^{(\alpha)}$, admits also some interesting algebraic basis: for example the basis of *free cumulants* $(R_k^{(\alpha)})_{k \ge 2}$ -- see Section [\[SectDefKerov\]](#SectDefKerov){reference-type="ref" reference="SectDefKerov"}. Thus $\mathop{\mathrm{Ch}}_\mu^{(\alpha)}$ writes uniquely as a polynomial in free cumulants. As it was first considered by Kerov in the case $\alpha=1$, it is usually termed *Kerov's polynomial* (or *Kerov's expansion* to avoid repetition of the word polynomial).

In [@Lassalle2009], Lassalle has described an inductive algorithm to compute the coefficients of this expansion. In this paper, by a careful analysis of Lassalle's algorithm, we obtain some polynomiality results (with several bounds on the degree) for these coefficients: see Propositions [\[PropBound1\]](#PropBound1){reference-type="ref" reference="PropBound1"}, [\[PropBound2\]](#PropBound2){reference-type="ref" reference="PropBound2"} and [\[PropBound3\]](#PropBound3){reference-type="ref" reference="PropBound3"}.

Clearly, writing some functions in a multiplicative basis may help to understand how to multiply them and we can deduce Theorem [\[theo:struct-const\]](#theo:struct-const){reference-type="ref" reference="theo:struct-const"} from these results on Kerov's polynomials.

While inappropriate to obtain close formulas, this way of studying structure constants is, as far as we know, original. Usually, results of structure constants are obtained using their combinatorial description of *via* representation theory tools [@FarahatHigmanCentreQSn; @GouldenJacksonMapsZonal; @IvanovKerovPartialPermutations; @GoupilSchaefferStructureCoef; @Tout-Structure-constant-S2n-Hn].

To finish this paragraph, let us mention that there is an appealing positivity conjecture on Kerov's polynomials for Jack characters [@Lassalle2009 Conjecture 1.2]. While we can not solve this conjecture, our analysis of Lassalle's algorithm gives some partial results: we prove in general the polynomiality of the coefficients and we compute a few specific values that were conjectured by Lassalle (see Appendix [\[app:Kerov_polynomials\]](#app:Kerov_polynomials){reference-type="ref" reference="app:Kerov_polynomials"}).

Another interesting application of our result on Kerov's polynomials is a new proof of the polynomial dependence of Jack polynomials in term of Jack parameter $\alpha$, which was an important open problem in the early nineties. This is presented in Section [\[SubsectCoefJackPoly\]](#SubsectCoefJackPoly){reference-type="ref" reference="SubsectCoefJackPoly"}.

## An open problem: edge fluctuations of Jack measure

Another natural question on asymptotics of Jack measure is the behavior of the first few rows of the Young diagrams. This kind of results, orthogonal to the ones in this paper, is called *edge fluctuations*. Our law of large number on the bulk on Young diagrams implies that, for any fixed positive integer $k$ and real number $C<1$, $$\mathbb{P}\left[ \frac{(\lambda_{(n)})_k}{\sqrt{n}} \leq \frac{2\, C}{\sqrt{\alpha}} \right] \to 0,$$ while Lemma [\[lem:FiniteSupport\]](#lem:FiniteSupport){reference-type="ref" reference="lem:FiniteSupport"} tells us that $(\lambda_{(n)})_k/\sqrt{n}$ exceeds $(2e)/\sqrt{\alpha}$ with exponentially small probability.

A natural conjecture, considering the case $\alpha=1$ where the edge fluctuations are well described (see [@Okounkov2000; @BorodinOkounkovOlshanski2000] and references therein) and the link with $\beta$-ensemble, would be the following: for each integer $k \ge 1$, the quantity $(\lambda_{(n)})_k/\sqrt{n}$ converges in probability towards $2/\sqrt{\alpha}$ and the joint vector $$\left[ n^{1/3} \left( \frac{(\lambda_{(n)})_j}{\sqrt{n}} - \frac{2}{\sqrt{\alpha}} \right) \right]_{1 \le j \le k}$$ converges in law towards the $\beta$-Tracy-Widom distribution, which has been introduced and studied in [@BetaEdgeFluctuations] to study edge fluctuations of $\beta$-ensemble. Naturally, a similar conjecture can be formulated for the lengths of the first columns of the Young diagram $\lambda_{(n)}$.

These conjectures hold true for the first row/column in the case $\alpha=1/2$ and $\alpha=2$. The proof uses the combinatorial interpretation of Jack measure at these particular values of $\alpha$, using Robinson-Schensted on random fixed point free involutions: see [@BaikRainsMonotomeSubsequenceInvolutions].

We have not made computer experiments to confirm this conjecture and let this problem wide open for future research.

[^1]: Let us also mention the work of Aker and Can [@AkerCanFarahatHecke] in this direction. Unfortunately, a factor $2^n n!$ is missing in the main result and the authors are not able to correct this [@CanMistake]
