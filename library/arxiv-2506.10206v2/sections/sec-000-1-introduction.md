---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.993
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
Higher logarithm functions are of fundamental importance in many areas of both physics and mathematics, and the dilogarithm function $\operatorname{Li}_{2}$ may be seen as the most basic and fundamental function of this form. Polylogarithms arise in deep areas of number theory and quantum theory, and the study of higher logarithm functions in its own right provides one of the core topics concerning special functions. Zagier [@Zagier2007] built on the pioneering work of Nahm et al. [@Nahm1995; @Nahm2007; @Nahm1994; @NahmRecknagelTerhoeven1993] in ways that relate the use of higher $K$-groups and higher Bloch groups to the behavior of the $\operatorname{Li}_{2}$-function, and the seminal nature of the monographs by Lewin on the dilogarithm and polylogarithm functions [@Lewin1958; @Lewin1981; @Lewin1991text] further motivates the techniques and $\operatorname{Li}_{2}$-identities introduced in this paper, in which we solve open problems given by both Bytsko [@Bytsko1999] and Campbell [@Campbell2025].

The problem of evaluating inverse binomial series in terms of polylogarithms and related special functions often leads to rich areas of research within computational and experimental mathematics [@BorweinBaileyGirgensohn2004 §1.7]. For hypergeometric series of this form with half-integer parameters, the evaluation of such series is fairly well understood, and our work is inspired by a known evaluation of this form introduced by D'Aurizio and subsequently explored by D'Aurizio and Di Trani [@DAurizioDiTrani2018]. By letting the *Pochhammer symbol* be such that $(x)_{n} = x(x+1) \cdots (x + n - 1)$ for $n \in \mathbb{N}_{0}$, and by letting *generalized hypergeometric series* be denoted and defined so that $${}_{p}F_{q}\!\!\left[ \begin{matrix} a_{1}, a_{2}, \ldots, a_{p} \vspace{1mm}\\ b_{1}, b_{2}, \ldots, b_{q} \end{matrix} \ \Bigg| \ x 
 \right] = \sum_{n=0}^{\infty} \frac{ \left( a_{1} \right)_{n} \left( a_{2} \right)_{n} \cdots \left( a_{p} \right)_{n} }{ \left( b_{1} \right)_{n} 
 \left( b_{2} \right)_{n} \cdots \left( b_{q} \right)_{n} } \frac{x^{n}}{n!},$$ the above referenced D'Aurizio evaluation is such that $${}_{4}F_{3}\!\!\left[ \begin{matrix} 1, 1, 1, \frac{3}{2} \vspace{1mm}\\ \frac{5}{2}, \frac{5}{2}, \frac{5}{2} \end{matrix} \ \Bigg| \ 1 \right] = 
 27 \sum_{n\geq 0}\frac{16^n}{(2n+3)^3 (2n+1)^2 \binom{2n}{n}^2} = {\frac{27}{2}\left(7\,\zeta(3)+(3 - 
 2 G)\,\pi-12\right)}$$ for Apéry's constant $\zeta(3) = \frac{1}{1^3} + \frac{1}{2^3} + \cdots$ and Catalan's constant $G = \frac{1}{1^2} - \frac{1}{3^2} + 
 \frac{1}{5^2} - \cdots$. Relatively little is known when it comes to the evaluation of inverse binomial series that have third-integer or quarter-integer or sixth-integer values as lower parameters, in contrast to the half-integer parameter values involved in D'Aurizio's ${}_{4}F_{3}(1)$-series, but evaluations for ${}_{4}F_{3}$-series of the form $$\label{4F3thirdinteger} 
 {}_{4}F_{3}\!\!\left[ \begin{matrix} 1, 1, 1, \frac{3}{2} \vspace{1mm}\\ 
 \frac{4}{3}, \frac{5}{3}, 2 \end{matrix} \ \Bigg| \ z \right] 
 = \frac{4}{9 z} \sum_{n=1}^{\infty} \left( \frac{27z}{4} \right)^{n} \frac{1}{n^2 \binom{3 n}{n}}$$ and for equivalent or related series have been considered by a number of authors [@AdegokeFrontczakGoy2024; @Batir2005; @CampbellLevrie2024; @Chu2022; @ChudnovskyChudnovsky1998; @DAurizioDiTrani2018], with [\[4F3thirdinteger\]](#4F3thirdinteger){reference-type="eqref" reference="4F3thirdinteger"} admitting an analytic evaluation. Similar inverse binomial series related to the quarter-integer and sixth-integer cases have been investigated, respectively, by Rathie and Shpot [@RathieShpot2025] and by Sun et al. [@Sun2024; @SunZhoupreprint].

The evaluation techniques introduced in this paper are related to those in the above references on inverse binomial series, but may be seen as providing a more comprehensive treatment of dilogarithm identities. Our beta integral-based series evaluation methods build on our past work [@Hakimoglupreprint] and appear to be original. For background material on computational approaches toward the evaluation of series, we refer to the monograph due to Sofo [@SOFO2003].
