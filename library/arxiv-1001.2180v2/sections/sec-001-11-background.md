---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-001-11-background
section_title: "Background"
section_number: 1.1
pages: 1-2
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.82
latex_coverage_ratio: 0.949
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
[]{#subsect:background label="subsect:background"} Given a combinatorial family of planar objects, it is natural to ask if, with a good rescaling, there is a limiting continuous object when the size tends to infinity. In the case of Young diagrams endowed with Plancherel measure, this question has been solved in 1977 independently by A. Vershik and S. Kerov [@KV77] and B. Logan and L. Shepp [@LS77]. V. Ivanov and G. Olshanski [@IO02], using unpublished notes of S. Kerov, have been able to describe the fluctuations of diagrams around this limit shape.

The Plancherel measure is natural when we look at Young diagrams of a given size $n$ (the set of which will be denoted $\mathscr{Y}_{n}$), because it is related to the regular representation of $\mathfrak{S}_n$. But there are many other interesting measures on Young diagrams and we can look for a limiting continuous object in these cases as well. P. Biane has proven the existence of a limiting shape under some general conditions on the character values of the representation associated to the measure [@Bia01]. This includes some natural representations, like the one on $(\mathbb{C}^N)^{\otimes n}$ appearing in Schur-Weyl duality under some conditions on $n$ and $N$. In this context, the second-order asymptotics have been studied by P. Śniady [@Sniady06].

The results mentioned above give a limit shape for the Young diagrams rescaled by $1/\sqrt{n}$, where $n$ is the number of boxes of the diagram. In particular, the existence of a limit shape implies that the probability that a random diagram has a long row or column (of length $\gg \sqrt{n}$) tends to $0$. Therefore the same method can not be used directly to study the asymptotic behavior of non-balanced Young diagrams, such as diagrams under the $q$-Plancherel measure.

This measure is a natural $q$-analog of the Plancherel measure. It was first introduced by Kerov in [@KerovQHookWalk] *via* a deformed hook walk algorithm. The asymptotic behavior of diagrams under this measure has then been considered by a Strahov [@Stra08]. By generalizing Kerov's method of a differential growth model [@Kerov96], he has obtained a limit shape for a diagram under the $q$-Plancherel measure with a parameter $q$ depending of the size of the diagrams.

We have mentioned above that, if we fix $q$, there is no hope in finding a limit shape of diagrams rescaled by $1/\sqrt{n}$ as the first rows or columns are not of order $\Theta(\sqrt{n})$ . In this paper, we give the precise behavior (first- and second-order asymptotics) of the length of these first rows or columns (either rows or columns, depending on the value of $q$, are of order $\Theta(n)$). This is a good description of the shape of the diagram as a finite number of rows or columns contain an arbitrarily big proportion of the boxes of the Young diagram (outside a set of small probability). Our method is close to the one of the papers [@IO02; @Sniady06]. The first-order asymptotics actually follow from general results of harmonic analysis on the infinite symmetric group ([@Tho64; @KV81; @KOO97; @KOV04]); our computations are quite independent of these results, and they allow to tackle with the same formalism the second-order asymptotics.

A natural question arising after this result on $q$-Plancherel measure is the following: can our method be adapted to measures for which typical diagrams have rows of intermediate scaling $\Theta(n^\alpha)$ with $1/2 < \alpha < 1$: intermediate between the balanced case ($\alpha=1/2$) and the $q$-Plancherel case ($\alpha=1$)? The answer is yes and, as examples, we look at measures associated to Schur-Weyl duality. In these cases, the method gives results on the global shape of the diagram, but not the precise behavior of the first rows and columns. Indeed, as for balanced diagrams, the asymptotic behavior of the lengths of the first rows and columns is not a direct consequence of the existence of the limit shape. For instance, in the case of the Plancherel measure, a consequent amount of extra work is needed: see [@BDJ99firstrow; @BDJ99secondrow; @Okounkov99; @BOO00; @JohanssonPlancherel].
