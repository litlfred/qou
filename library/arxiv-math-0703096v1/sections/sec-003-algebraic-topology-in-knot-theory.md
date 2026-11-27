---
doc_id: arxiv-math-0703096v1
doc_title: "KNOTS From combinatorics of knot diagrams to combinatorial topology based on knots"
section_id: sec-003-algebraic-topology-in-knot-theory
section_title: "Algebraic topology in Knot Theory"
section_number: null
pages: 24-28
source_pdf: arxiv-math-0703096v1.pdf
source_sha256: 337c26b7164ff942
toc_source: outline
doc_brief: "History of knot theory (Przytycki, arXiv:math/0703096, chapter of KNOTS) — from Gauss and Listing through Kelvin, Tait, Kirkman and Little to the twentieth century"
---
Algebraic topology in Knot Theory
The fundamental problem in knot theory is to be able to distinguish non-
equivalent knots. It was not achieved (even in the simple case of the unknot
and the trefoil knot) until Jules Henri Poincar´e (1854-1912) in his “Analy-
sis Situs” paper ([Po-1] 1895) laid foundations for algebraic topology. Poul
Heegaard (1871-1948) in his Copenhagen Dissertation of 1898 ([Heeg]) con-
structed the 2-fold branch cover of a trefoil knot and showed that it is the
lens space, L(3, 1), in modern terminology. He also showed that the anal-
ogous branch cover of the unknot is S3. He distinguished L(3, 1) from S3
II.3. ALGEBRAIC TOPOLOGY IN KNOT THEORY
25
using the Betti numbers (more precisely he showed that the ﬁrst homology
group is nontrivial and he clearly understood that it is a 3-torsion group). He
didn’t state however that it can be used to distinguish the trefoil knot from
the unknot; see [Stil] p.226.32 Heinrich Tietze (1880-1964) used in 1908 the
fundamental group of the exterior of a knot in R3, called the knot group, to
distinguish the unknot from the trefoil knot [Ti-1]. The fundamental group
was ﬁrst33 introduced by Poincar´e in his 1895 paper [Po-1].
Wilhelm Wirtinger (1865-1945) in his lecture delivered at a meeting of
the German Mathematical Society in 1905 outlined a method of ﬁnding a
knot group presentation (it is called now the Wirtinger presentation of a
knot group) [Wir]. Max Dehn (1878-1952), in his 1910 paper [De-1] reﬁned
the notion of the knot group and in 1914 was able to distinguish the right
handed trefoil knot (
) from its mirror image, the left handed trefoil
knot (
); that is Dehn showed that the trefoil knot is not amphicheiral
[De-2] 34.
Tait was the ﬁrst to notice the relation between knots and planar graphs.
He colored the regions of the knot diagram alternately white and black
(following Listing) and constructed the graph by placing a vertex inside
each white region, and then connecting vertices by edges going through the
crossing points of the diagram (see Figure 4.1)[D-H].
32For the English translation of the topological part of the Heegaard thesis see the
appendix to [P-22].
33According to [Ch-M] Hurwitz’ paper of 1891 [Hur] “may very well be interpreted as
giving the ﬁrst approach to the idea of a fundamental group of a space of arbitrarily many
dimensions.”
34In 1978, W.Magnus wrote [Mag]: Today, it appears to be a hopeless task to assign
priorities for the deﬁnition and the use of fundamental groups in the study of knots, par-
ticularly since Dehn had announced [De-0] one of the important results of his 1910 paper
(the construction of Poincar´e spaces with the help of knots) already in 1907.
26
CHAPTER II. HISTORY OF KNOT THEORY
.
.
.
.
.
.
Figure 4.1
In 1912, George David Birkhoﬀ(1884-1944) when trying to prove the
four-color problem (formulated in 1852 by Francis Guthrie (1831-1899)),
introduced the chromatic polynomial of a graph [Birk-1].
The breakthrough, from the point of view which focuses on the Jones
type link invariants, was the invention by James Waddell Alexander (1888-
1971) of a Laurent polynomial invariant of links ([Al-3], 1928)35. Alexander
was a colleague of Birkhoﬀand we can conjecture that he knew about the
chromatic polynomial.36 We know for sure that when W. T. Tutte was gen-
eralizing the chromatic polynomial in 1947 [Tut-1], he was motivated by the
35 Alexander described the numerical precursor to his polynomial, for the ﬁrst time, in
the letter to Oswald Veblen, 1919 [A-V].
36Birkhoﬀwrites in [Birk-3] : “...Alexander, then [1911] a graduate student [at Prince-
ton], began to be especially interested in the subject [analysis situs].
His well known
“duality theorem,” his contributions to the theory of knots, and various other results,
have made him a particularly important worker in the ﬁeld”. We can also mention that in
the fall of 1909 Birkhoﬀbecame a member of the faculty at Princeton and left for Harvard
in 1912. His 1912 paper [Birk-1] ends with “Princeton University, May 4, 1912.”
II.3. ALGEBRAIC TOPOLOGY IN KNOT THEORY
27
knot polynomial of Alexander. The Alexander polynomial can be derived
from the group of the knot (or link). This point of view has been extensively
developed since Alexander’s discovery. More generally, the study of the fun-
damental group of a knot complement and the knot complement alone was
the main topic of research in knot theory for the next ﬁfty years, culminating
in 1988 in the proof of Tietze [Ti-1] conjecture (that a knot is determined by
its complement) by Gordon and Luecke [G-Lu]. We can refer to the survey
articles by Ralph Hartzler Fox (1913 -1973) [F-1] and Gordon [Gor] or books
[Bi-1, B-Z, K-3, Re-2, Ro-1] in this respect. However, Alexander observed
also that if three oriented links, L+, L−and L0, have diagrams which are
identical except near one crossing where they look as in Figure 4.2, then their
polynomials are linearly related [Al-3]. An analogous discovery about the
chromatic polynomial of graphs was made by Ronald M. Foster in 1932 (see
[Whit-1]; compare also [Birk-2] Formula (10)). In early 1960’s, J. Conway
rediscovered Alexander’s formula and normalized the Alexander polynomial,
∆L(t) ∈Z[t±1/2], deﬁning it recursively as follows ([Co-1]):
(i) ∆o(t) = 1, where o denotes a knot isotopic to a simple circle
(ii)
∆L+ −∆L−= (
√
t −1
√
t)∆L0
+
L
-
L
L 0
Figure 4.2
28
CHAPTER II. HISTORY OF KNOT THEORY
