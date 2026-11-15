---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-001-11-irreducible-representations-of-large-symmetri
section_title: "Irreducible representations of large symmetric groups"
section_number: 1.1
pages: 1-2
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.99
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
[]{#subsec:need label="subsec:need"}

Irreducible representations of symmetric groups are in the one-to-one correspondence with Young diagrams and due to algorithms such as Murnaghan--Nakayama rule or Robinson--Littlewood rule the essential questions concerning representations and characters of symmetric groups can be answered by a combinatorial study of the corresponding Young diagrams [@FultonYoungtableaux]. However, when one studies the asymptotic properties of large symmetric groups, the work with Young tableaux becomes cumbersome and one is in the need to find another object which would encode the same information in a more convenient way. Alternatively, one can state the above problem as follows: a typical partition of a large number $q$ (or equivalently, a Young diagram with $q$ boxes) is a collection of at least $\sqrt{q}$ numbers, hence it contains a lot of information. Nevertheless, we can expect that one does not need to know all this information to extract (with a reasonable accuracy) the properties of characters and representations. Therefore the question arises how to compress the information about the Young diagrams in the most efficient way.

It turns out that the right tool for development of the above program is the notion of the transition measure of a Young diagram which was introduced by Kerov [@Kerov1993transition; @Kerov1999differential].

The transition measure of a Young diagram is a probability measure on the real line---therefore it has a much more analytic nature than a combinatorial notion of a Young diagram and for this reason it is very appealing for our purposes. Yet another advantage of this object is that it is possible to characterize it in many ways [@Biane1998; @Okounkov2000randompermutations].

Of course, a question arises how to relate the transition measure of a Young diagram with the values of the corresponding characters.

In this article we find the appropriate formula in a form of an asymptotic series the terms of which correspond to two-dimensional surfaces with a prescribed genus.

The first result in this direction was obtained by Biane [@Biane1998]: he showed that if the sequence of Young diagrams (after appropriate scaling) converges to some limit shape then the leading term corresponds to surfaces with genus zero and therefore this leading term can be computed by the means of Voiculescu's free probability theory [@VoiculescuDykemaNica; @HiaiPetz2000]. Okounkov [@Okounkov2000randompermutations] was studying the distribution of the length of the first rows of a large random Young diagram sampled according to the Plancherel measure; he showed that the limit distribution coincides with the limit distribution of the biggest eigenvalues of a random matrix in the Gaussian Unitary Ensemble (GUE). The main idea of his proof was the observation that the both the formula for the moments of a GUE random matrix and the formula for the moments of the transition measure of a random Young diagram can be viewed as series the terms of which correspond to two-dimensional surfaces with prescribed genus. One can view results of this article as an attempt to simplify some of the arguments of Biane [@Biane1998] and simultaneously to provide better asymptotic expansion. Our results are closely related to those of Okounkov [@Okounkov2000randompermutations] with the difference that we do not study the connection with random matrices but on the bright side we do not restrict ourselves to the case of the Plancherel measure.

In the remaining part of the introduction we will present a more detailed view of the methods and the results of this article.
