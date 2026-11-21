---
doc_id: arxiv-0802.1072v2
doc_title: "A note on closed 3-braids ∗"
section_id: sec-006-some-open-questions-and-a-survey-of-known-result
section_title: "Some open questions and a survey of known results about links of braid index 3"
section_number: null
pages: 9-14
source_pdf: 0802.1072v2.pdf
source_sha256: 6f4d93f0b7ba5cd7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.998
latex_coverage_ratio: 0.791
doc_brief: "A note on closed 3-braids ∗ — This is a review article about knots and links of braid index 3."
---
[]{#S:known and unknown label="S:known and unknown"} In this section we survey the literature and discuss some unknown properties of knots and links of braid index 3. Our choices are guided by what we know best, and by our wish to illustrate ways in which Theorems 1,2 and 3 have been and might be useful.

1.  We made inquiries, but were unable to find a computer program that implements Xu's solution to the conjugacy problem in $B_3$. If anyone is interested, it would be useful to have such a program, if it is freely available to researchers.

2.  In our judgment, the most striking feature of closed 3-braids that has not been used in any substantial way in the literature is that we know precisely which links of braid index 3 are invertible, and which are not. In the early history of knot theory it was not known whether non-invertible knots exist. The first proof that they do exist is due to H. Trotter [@Tr], who showed that if $|p|,|q|,|r|\geq 2$ are distinct, then the assumption that the pretzel knots $K(p,q,r)$ are invertible leads to a contradiction about the structure of their groups. His indirect proof characterizes all the work that we know which treats non-invertibility. We do not know of any computable numerical invariant that detects non-invertible knots. Therefore, if anyone has a candidate for an invariant that detetcts non-invertibility, three-braids are an excellent source of examples, because 'most' of them are non-invertible. Note that all knots that admit a flype, degenerate or not, are invertible. Theorem 2 and Tables I and II tell us precisely how to find all non-invertible 3-braid examples.

3.  A knot $\overrightarrow{K}$ is *strongly invertible* if there is a representative $\overrightarrow{K}\subset S^3$ and an involution $\iota:(S^3,\overrightarrow{K}) \to (S^3,\overleftarrow{K})$. In the course of writing this note we observed the following:

    ::: proposition
    In the special case of 3-braids, if a knot type $\overrightarrow{\mathcal K}$ is invertible, then it is strongly invertible.
    :::

    Question: Is it possible that this is the case for arbitrary knots?

4.  We discuss next a problem which turns out to be closely related to problem 2 above, although initially it does not seem to be. A knot is *transversal* if it is everywhere transverse to the standard contact structure in $\mathbb R^3$. The *transversal knot type* of a transversal knot is its equivalence class under isotopies through transversal knots. Known invariants of transversal knot types are their topological knot type and their Bennequin number and (a recent development at the time of this writing) certain invariants based upon Knot Floer Homology and Khovanov Homology [@OST; @NOT; @Pl1; @Pl2; @Wu; @HKP]. The first examples of pairs of knots which have the same topological knot type and the same Bennequin invariant, but are transversally distinct, were discovered via 3-braids [@BM-stab-II]. The proof in [@BM-stab-II] is indirect, and at this writing nobody has found an invariant which distinguishes even one of those pairs, however caution is needed: Each pair is an example of a pair of knots which are topologically invertible but not transversally invertible. In view of Problem 1 above they are bound to be extremely subtle to detect.

5.  We discuss a different set of questions about 3-braids which has received much attention and which, like Problem 2 above, seems very difficult. When the Jones and HOMFLY polynomials were discovered [@Jones] it was not known whether they were or were not injective on topological link types, but examples taken from 3-braids [@Bir-Jones] quickly showed that the answer is 'no'. However, at this writing we know very little about how good a job the Jones polynomial does. It is therefore a natural question to ask whether one can arrive at some understanding of the kernel of the Jones polynomial in the special case of braid index 3. This is especially tempting because when the braid index is 3 the Jones polynomial depends on just one small calculation: the trace of a certain $2 \times 2$ matrix. Nevertheless, the prohibitively complicated formulas in [@Tak] tell us that this is simply not a good question, and that simplifications are needed before we can hope for a start in understanding the kernel of the Jones polynomial of links that are closed 3-braids.

    An example is enlightening, even though it does not have much to do with 3-braids. In the class of torus links, two integers $r,s$ are all that is needed to distinguish one torus link from another. On the other hand, if one wishes to distinguish the Jones polynomial of one torus link from that of another, the matter is considerably more complicated. One has the following very complicated formula [@Jones2]:

    $$\label{E:JP of torus link}
    V_{r,s}(t) = \frac{t^{\frac{1}{2}(r-1)(s-1)}}{1-t^2}\sum _{l=0}^{n}\left( n \over l \right)t^{\frac{r}{n}(n-l)(1+\frac{s}{n}l)}(t^{(n-l)\frac{s}{n}} - t^{1 + l\frac{s}{n}}), \ \  {\rm where} \ \   n = gcd(r,s).$$ It isn't even obvious that it gives a polynomial (although of course it does). The reader will notice that, knowing the general form of ([\[E:JP of torus link\]](#E:JP of torus link){reference-type="ref" reference="E:JP of torus link"}), $V_{r,s}(t)$ is completely determined by the two integers $r$ and $s$.

6.  Concluding this note, we point the reader, in no particular order, to some of the published work that has come to our attention about links of braid index 3:

    1.  K. Murasugi's monograph [@Mur] was pioneering, in the sense that it was the first study that isolated knots and links of braid index 3 as a special class worthy of study. It is filled with detailed information and the author's tireless, error-free and very useful calculations. Murasugi used Schreier's solution to the conjugacy problem [@Sc], but carried things a step further by partitioning Schreier's conjugacy classes into groups which were later realized to coincide with pseudo-Anosov, finite order and reducible braids. In this sense it was prescient, because it forsaw the Nielsen-Thurston trichotemy that has played such a major role in understanding mapping class groups of surfaces, in the special case of 3-braids. This seemed so striking that many people tried to carry generalize Murasugi's work to $B_n$, but alas the generalizations did not seem to work. One may also find, in [@Mur], an example of the flypes which play such an important role in Theorems 1,2 and 3.

    2.  Two algorithmic solutions to the shortest word problem for 3-braids appeared in the literature essentially simultaneously. They were due to P.J.Xu [@Xu] and M. Berger [@Berger], and they used the band and classical presentations respectively. A year later R.D.Keever [@Keev] gave yet another solution, duplicating both of the preceding. (His paper appeared in the same journal as Xu's paper, a year later, and neither Keever nor anyone else seems to have realized the duplication!). Of these three, only Xu's paper does more, as it not only also gives the pleasant solution to the conjugacy problem that we discussed in $\S$[\[SS:the conjugacy problem\]](#SS:the conjugacy problem){reference-type="ref" reference="SS:the conjugacy problem"} but also proves that the shortest word problem implies an algorithm for computing link genus. Very recently Usman Ali [@Us] posted a paper on the arXiv that chooses a unique representative in SS$(W)$ algorithmically when $W$ is a 3-braid, but using the classical presentation rather than the band presentation of Xu. All these results are of interest because it has been proved by Paterson and Razborov [@PR] that the shortest word problem in $B_n$, using the classical presentation, is NP complete.

    3.  In a separate paper [@Xu2] Xu uses her earlier work to compute the growth functions for the positive braid semigroup. Neither [@Berger] nor [@Keev] consider that problem.

    4.  In a different direction S. Orevkov [@Orev] discovered an algorithm for deciding whether links of braid index 3 are quasi-positive, a question which is of interest in the study of the topology of plane real algebraic curves.

    5.  In [@Ni] Y. Ni used knot Floer homology to determine which links of braid index 3 are fibered. He introduced there the interesting concept of 'almost fibered'. The question of when 3-braids are fibered was also studied by A. Stoimenow in [@St1].

    6.  M.T. Lozano and J. Przytycki [@LP] classified horizontal incompressible surfaces in the complement of a link of braid index 3. Using a different set of techniques, E. Finkelstein obtained related results in [@Fink].

    7.  D. Erle has computed the signature of links of braid index 3 in [@Erle].

    8.  A. Stoimenow gives a classification of alternating links of braid index 3 in [@St2].

    9.  W. Menasco and X. Zhang prove, in [@MZ], that knots which are closed 3-braids have Property P.

    10. In [@Kin] E. Kin uses 3-braids to study a problem in dynamics.

**Acknowledgment:** We thank Sang-Jin Lee, Lenny Ng, Peter Ozsvath and Dylan Thurston for useful comments on the precurser of this manuscript, the preprint [@BM-2006]. We thank Usman Ali for pointing out errors in Table I.
