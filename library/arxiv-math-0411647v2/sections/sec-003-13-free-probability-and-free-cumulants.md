---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-003-13-free-probability-and-free-cumulants
section_title: "Free probability and free cumulants"
section_number: 1.3
pages: 4-6
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.987
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
[]{#subsec:freeproba label="subsec:freeproba"}

In this paper we study free cumulants of the transition measure of a given Young diagram. The notion of free cumulants plays a fundamental role in the free probability, a theory which was initiated by Voiculescu in order to answer some old questions in the theory of operator algebras but it soon evolved into an exciting self--standing theory with many links to other fields, see [@HiaiPetz2000; @VoiculescuDykemaNica; @VoiculescuPlenar; @VoiculescuLectures].

This theory can be viewed as a highly non--commutative probability theory in which the notion of independence of random variables was replaced by a non--commutative notion of freeness. For the purpose of this article we shall concentrate on the combinatorial aspect of this theory connected with non--crossing partitions [@Kreweras] and mentioned above free cumulants, which were introduced by Speicher [@Speicher1994; @Speicher1997; @Speicher1998].

### Free convolution and free cumulants {#subsec:convolution}

For probability measures $\mu$, $\nu$ on the real line one can define their free convolution $\mu\boxplus\nu$ which is also a probability measure on the real line. One of the first problems of free probability was to study this convolution. The simplest approach is to consider the sequence of moments $$M_i(\mu)=\int_{{\mathbb{R}}} x^i \ d\mu(x) \label{eq:momenty}$$ of a given measure $\mu$ and ask what is the relation between the moments of $\mu\boxplus\nu$ and the moments of $\mu$ and $\nu$. Unfortunately, in turns out that the answer is given by a sequence of quite complicated polynomials.

The solution to the above problem of finding a nice description of the free convolution is given by free cumulants. To the measure $\mu$ we assign a sequence of its free cumulants $R_1(\mu),R_2(\mu),\dots$;

every free cumulant $R_i(\mu)$ is a certain polynomial in the moments of $\mu$, and conversely, every moment of $\mu$ can be expressed as a certain polynomial in free cumulants; therefore the sequence of moments and the sequence of free cumulants carry the same information. The advantage of the notion of free cumulants over the notion of moments is the simplicity of the relation between free cumulants: $R_n(\mu\boxplus\nu)=R_n(\mu)+R_n(\nu)$. In this article we are not interested in the study of free convolution; our point is that free cumulants have a miraculous property of simplifying certain complicated non--commutative relations.

### Free cumulants of the transition measure {#subsec:kerov}

In this article we study the relation between the transition measure $\mu^{\lambda}$ of a Young diagram $\lambda$ and the characters of the corresponding irreducible representation. The simplest idea would be to describe the transition measure in terms of its moments $M_i(\mu^{\lambda})$, however---as we already mentioned---the relation between these moments and characters turns out to be quite complicated. Similarly as in the example from the above Section [0.0.1](#subsec:convolution){reference-type="ref" reference="subsec:convolution"}, free cumulants can simplify dramatically the complexity of the formulas: it was shown by Biane [@Biane1998] that for each $n$ the value $\Sigma_n$ of the normalized character on the $n$--cycle

can be expressed as a certain polynomial in free cumulants $R_2,R_3,\dots$ of the transition measure of the corresponding Young diagram. Furthermore, the leading term is particularly simple, namely $$\label{eq:asymptotyka0}

\Sigma_{n}=

R_{n+1} + \text{lower degree terms}.$$

The fundamental property of this polynomial, called Kerov polynomial, is that it is universal for all Young diagrams.

Kerov polynomials seem to have very interesting combinatorial properties but not too much about them is known [@BianeCharacters; @StanleyRectangularCharacters; @StanleySlajdyKerov]. Kerov conjectured that all coefficients of Kerov polynomials are non--negative integers; this conjecture seems to be quite difficult. Unfortunately, Kerov's conjecture does not seem to have interesting applications, but on the other hand its proof might be much more interesting than the conjecture itself: Biane [@BianeCharacters] suggested that the coefficients of Kerov polynomials might be interpreted as the number of certain intervals in the decomposition of the Cayley graph of the symmetric group and it would be very interesting to state Biane's conjecture in a more concrete form.

### The second main result: second-order expansion for Kerov polynomials

One of the main results of this paper is a more precise asymptotic expansion of characters $$\begin{gathered}
\Sigma_{n}=
  R_{n+1}+ \\  \sum_{\substack{m_2,m_3,\dots\geq 0 \\
                  2m_2+3 m_3+4 m_4+\cdots=n-1}}\!\!
            \frac{1}{4} \binom{n+1}{3} \binom{m_2+m_3+\cdots}{m_2,m_3,\dots}
                    \prod_{s\geq 2} \big( (s-1) R_s \big)^{m_s} +\\ \text{lower degree terms},
\label{eq:asymptotyka1}
 
\end{gathered}$$

which was conjectured by Biane [@BianeCharacters]. In other words: we calculate explicitly the coefficients of Kerov polynomials corresponding to the two highest--degree terms. We also outline an algorithm which can provide such an expansion of any order.

After the first version of this article was made public [@Sniady2003HigherOrder; @Sniady2003pushing] Goulden and Rattan [@GouldenRattan05] using different methods found an explicit formula for all coefficients of Kerov polynomials. The Kerov's positivity conjecture remains open until now.
