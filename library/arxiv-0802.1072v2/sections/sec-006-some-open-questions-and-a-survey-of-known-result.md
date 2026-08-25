---
doc_id: arxiv-0802.1072v2
doc_title: "A note on closed 3-braids ∗"
section_id: sec-006-some-open-questions-and-a-survey-of-known-result
section_title: "Some open questions and a survey of known results about links of braid index 3"
section_number: null
pages: 9-14
source_pdf: 0802.1072v2 (1).pdf
source_sha256: 6f4d93f0b7ba5cd7
doc_brief: "A note on closed 3-braids ∗ — This is a review article about knots and links of braid index 3."
---
of braid index 3
In this section we survey the literature and discuss some unk nown properties of knots and links of
braid index 3. Our choices are guided by what we know best, and by our wish to illustrate ways in
which Theorems 1,2 and 3 have been and might be useful.
1. We made inquiries, but were unable to ﬁnd a computer progra m that implements Xu’s solution
to the conjugacy problem in B3. If anyone is interested, it would be useful to have such a
program, if it is freely available to researchers.
2. In our judgment, the most striking feature of closed 3-bra ids that has not been used in any
substantial way in the literature is that we know precisely w hich links of braid index 3 are
invertible, and which are not. In the early history of knot th eory it was not known whether
non-invertible knots exist. The ﬁrst proof that they do exis t is due to H. Trotter [37], who
showed that if|p|,|q|,|r|≥ 2 are distinct, then the assumption that the pretzel knots K(p, q, r)
are invertible leads to a contradiction about the structure of their groups. His indirect proof
characterizes all the work that we know which treats non-inv ertibility. We do not know of
any computable numerical invariant that detects non-inver tible knots. Therefore, if anyone
has a candidate for an invariant that detetcts non-invertib ility, three-braids are an excellent
source of examples, because ‘most’ of them are non-invertib le. Note that all knots that admit
a ﬂype, degenerate or not, are invertible. Theorem 2 and Tabl es I and II tell us precisely how
to ﬁnd all non-invertible 3-braid examples.
3. A knot − →K is strongly invertible if there is a representative − →K ⊂ S3 and an involution ι :
(S3,− →K )→ (S3,← −K ). In the course of writing this note we observed the followin g:
Proposition 4. In the special case of 3-braids, if a knot type − →K is invertible, then it is
strongly invertible.
Question: Is it possible that this is the case for arbitrary k nots?
9
4. We discuss next a problem which turns out to be closely rela ted to problem 2 above, although
initially it does not seem to be. A knot is transversal if it is everywhere transverse to the stan-
dard contact structure in R3. The transversal knot type of a transversal knot is its equivalence
class under isotopies through transversal knots. Known inv ariants of transversal knot types
are their topological knot type and their Bennequin number a nd (a recent development at
the time of this writing) certain invariants based upon Knot Floer Homology and Khovanov
Homology [28, 26, 30, 31, 39, 14]. The ﬁrst examples of pairs o f knots which have the same
topological knot type and the same Bennequin invariant, but are transversally distinct, were
discovered via 3-braids [6]. The proof in [6] is indirect, an d at this writing nobody has found
an invariant which distinguishes even one of those pairs, ho wever caution is needed: Each
pair is an example of a pair of knots which are topologically i nvertible but not transversally
invertible. In view of Problem 1 above they are bound to be ext remely subtle to detect.
5. We discuss a diﬀerent set of questions about 3-braids which has received much attention and
which, like Problem 2 above, seems very diﬃcult. When the Jon es and HOMFLY polynomials
were discovered [16] it was not known whether they were or wer e not injective on topological
link types, but examples taken from 3-braids [2] quickly sho wed that the answer is ‘no’.
However, at this writing we know very little about how good a j ob the Jones polynomial
does. It is therefore a natural question to ask whether one ca n arrive at some understanding
of the kernel of the Jones polynomial in the special case of br aid index 3. This is especially
tempting because when the braid index is 3 the Jones polynomi al depends on just one small
calculation: the trace of a certain 2 × 2 matrix. Nevertheless, the prohibitively complicated
formulas in [36] tell us that this is simply not a good questio n, and that simpliﬁcations are
needed before we can hope for a start in understanding the ker nel of the Jones polynomial of
links that are closed 3-braids.
An example is enlightening, even though it does not have much to do with 3-braids. In the
class of torus links, two integers r, s are all that is needed to distinguish one torus link from
another. On the other hand, if one wishes to distinguish the J ones polynomial of one torus
link from that of another, the matter is considerably more co mplicated. One has the following
very complicated formula [17]:
Vr,s(t) = t
1
2 (r−1)(s−1)
1− t2
n∑
l=0
( n
l
)
t
r
n (n−l)(1+ s
n l)(t(n−l) s
n− t1+l s
n ), where n = gcd(r, s). (5)
It isn’t even obvious that it gives a polynomial (although of course it does). The reader will
notice that, knowing the general form of (5), Vr,s(t) is completely determined by the two
integers r and s.
6. Concluding this note, we point the reader, in no particula r order, to some of the published
work that has come to our attention about links of braid index 3:
(a) K. Murasugi’s monograph [24] was pioneering, in the sens e that it was the ﬁrst study that
isolated knots and links of braid index 3 as a special class wo rthy of study. It is ﬁlled with
detailed information and the author’s tireless, error-fre e and very useful calculations.
Murasugi used Schreier’s solution to the conjugacy problem [33], but carried things a
step further by partitioning Schreier’s conjugacy classes into groups which were later
realized to coincide with pseudo-Anosov, ﬁnite order and re ducible braids. In this sense
it was prescient, because it forsaw the Nielsen-Thurston tr ichotemy that has played such
a major role in understanding mapping class groups of surfac es, in the special case of
10
3-braids. This seemed so striking that many people tried to c arry generalize Murasugi’s
work to Bn, but alas the generalizations did not seem to work. One may al so ﬁnd, in
[24], an example of the ﬂypes which play such an important rol e in Theorems 1,2 and 3.
(b) Two algorithmic solutions to the shortest word problem f or 3-braids appeared in the
literature essentially simultaneously. They were due to P. J.Xu [40] and M. Berger [1],
and they used the band and classical presentations respecti vely. A year later R.D.Keever
[19] gave yet another solution, duplicating both of the prec eding. (His paper appeared
in the same journal as Xu’s paper, a year later, and neither Ke ever nor anyone else
seems to have realized the duplication!). Of these three, on ly Xu’s paper does more, as
it not only also gives the pleasant solution to the conjugacy problem that we discussed in
§2.3 but also proves that the shortest word problem implies an algorithm for computing
link genus. Very recently Usman Ali [38] posted a paper on the arXiv that chooses
a unique representative in SS( W ) algorithmically when W is a 3-braid, but using the
classical presentation rather than the band presentation o f Xu. All these results are of
interest because it has been proved by Paterson and Razborov [29] that the shortest
word problem in Bn, using the classical presentation, is NP complete.
(c) In a separate paper [41] Xu uses her earlier work to comput e the growth functions for
the positive braid semigroup. Neither [1] nor [19] consider that problem.
(d) In a diﬀerent direction S. Orevkov [27] discovered an algo rithm for deciding whether
links of braid index 3 are quasi-positive, a question which i s of interest in the study of
the topology of plane real algebraic curves.
(e) In [25] Y. Ni used knot Floer homology to determine which l inks of braid index 3 are
ﬁbered. He introduced there the interesting concept of ‘alm ost ﬁbered’. The question of
when 3-braids are ﬁbered was also studied by A. Stoimenow in [ 34].
(f) M.T. Lozano and J. Przytycki [22] classiﬁed horizontal i ncompressible surfaces in the
complement of a link of braid index 3. Using a diﬀerent set of te chniques, E. Finkelstein
obtained related results in [12].
(g) D. Erle has computed the signature of links of braid index 3 in [9].
(h) A. Stoimenow gives a classiﬁcation of alternating links of braid index 3 in [35].
(i) W. Menasco and X. Zhang prove, in [23], that knots which ar e closed 3-braids have
Property P.
(j) In [20] E. Kin uses 3-braids to study a problem in dynamics .
Acknowledgment: We thank Sang-Jin Lee, Lenny Ng, Peter Ozsvath and Dylan Thur ston for
useful comments on the precurser of this manuscript, the pre print [4]. We thank Usman Ali for
pointing out errors in Table I.
References
[1] M. Berger, Minimum crossing numbers for 3-braids , J. Phys. A 27 (1994), no. 18, 6205-
6213.
11
[2] J. S. Birman, On the Jones polynomial of closed 3-braids , Inventiones mathematicae 81
(1985), 287-294.
[3] Birman, K.H.Ko and S.J. Lee, A new approach to the word and conjugacy problems in the
braid groups, Adv. Math. 139 (1998), no. 2, 322–353.
[4] J.S. Birman and W.W.Menasco, A note on transversal knots which are closed 3-braids ,
preprint, arXiv math/0703669.
[5] J. S. Birman and W. W. Menasco, Studying links via closed braids III: Classifying links
which are closed 3-braids , Paciﬁc Journal of Mathematics 161 (1993), 25-113.
[6] J. S. Birman and W. W Menasco, Stabilization in the braid groups II: Transversal simplicity
of knots , Geometry and Topology 10 (2006), 1425-1452.
[7] P. Dehornoy, Groupes de Garside , Ann. Sci. cole Norm. Sup. (4) 35 (2002), no. 2, 267–306.
[8] P. Dehornoy and L. Paris, Gaussian groups and Garside groups, two generalisations of
Artin groups, Proc. London Math. Soc. (3) 79 (1999), no. 3, 569–604.
[9] D. Erle, Calculation of the signature of a 3-braid link , Kobe J. Math. 16, (1999), no. 2,
161–175.
[10] J. Etnyre and K. Honda, Cabling and transverse simplicity , Annals of Math.(2) 162 (2005),
No. 3, 1305-1333.
[11] E. El-Rifai and H. Morton, Algorithms for positive braids , Quart. J. Math. Oxford Ser. (2)
45, (1994), 479–497.
[12] E. Finkelstein, Closed incompressible surfaces in closed braid complements , J. Knot Theory
Ramiﬁcations 7, (1998), no. 3, 335–379.
[13] F. A. Garside, The braid group and other groups , Quart. J. Math. Oxford Ser. (2) 20 (1969)
235–254.
[14] S. Harvey, K. Kawamuro and O. Plamenevskaya, Transverse knots, branched double covers
and Heegaard Floer contact invariants , preprint arXiv 0712.1557.
[15] J. Hoste and M. Thistlethwaite (with help from Bruce Ewi ng, Ken
Millett, Ken Stephenson and Jeﬀ Weeks), Knotscape 1.01 4-1-99 ,
http://www.math.utk.edu/∼morwen/knotscape.html.
[16] V.F.R.Jones, Hecke algebra representations of braid groups and link poly nomials, Ann. of
Math. (2) 126, (1987), no. 2, 335–388.
[17] Private communication from Vaughan Jones.
[18] E.S. Kang, K.H. Ko and S.J.Lee, Band-generator presentation for the 4-braid group, Topol-
ogy Appl. 78, (1997), no. 1-2, 39–60.
12
[19] R.D. Keever, Minimal 3-braid representations , J. Knot Theory Ramiﬁcations 3, no. 2
(1994), 163-177.
[20] E. Kin, The forcing partial order on a family of braids forced by pseud o-Anosov 3-braids ,
preprint, arXiv:0711.4398.
[21] K.H. Ko and S.J. Lee Flypes of closed 3-braids in the standard contact space , Journal of
the Korean Mathematical Society, 36 (1999), No. 1, 51 -71.
[22] M.T.Lozano and J. Przytycki, Incompressible surfaces in the exterior of a closed 3-braid.
I. Surfaces with horizontal boundary components , Math. Proc. Cambridge Philos. Soc. 98,
(1985), no. 2, 275–299.
[23] W. Menasco and X. Zhang, Positive Knots And Knots With Braid Index Three Have
Property-P, J. Knot Theory Ramiﬁcations 12, (2003), no. 4, 427–444.
[24] K. Murasugi, On closed 3-braids , Memoirs of the AMS 151, 1974.
[25] Y. Ni, Closed 3-braids are nearly ﬁbered , preprint arXiv:math.GT/0510243.
[26] L. Ng, P. Ozsv´ath and D. Thurston, Transverse knots distinguished by knot Floer homology ,
preprint arXiv math.GT/0703446.
[27] S. Orevkov, Quasipositivity problem for 3-braids , Turkish J. Math. 28. (2004), no. 1, 89-93.
[28] P. Ozsv´ath, Z. Szab´o, and D. Thurston, Legendrian knots, transverse knots and combina-
torial Floer homology , preprint, arXiv math.GT/0611841.
[29] M. S. Paterson and A. A. Razborov, The set of minimal braids is co-NP-complete , J.
Algorithms 12, (1991), no. 3, 393–408.
[30] O. Plamenevskaya, Transverse knots, double branched double covers and Heegaa rd Floer
Knot Homology, J. Symplectic Geometry, 4 (2006), No. 2, 149-170
[31] O. Plamenevskaya, Transverse knots and Khovanov homology , Math Research Letters 13
(2006), No. 4, 571-586.
[32] D. Rolfsen, Knots and Links , Publish or Perish 1976 and 1990.
[33] O. Schreier, Uber die Gruppen AaBb = 1, Abh. Math. Sem. Univ. Hamburg, 3 (1924),
167-169.
[34] A. Stoimenow, Properties of closed 3-braids and other link braid represen tations, preprint,
arXiv:math/0606435v2.
[35] A. Stoimenow, The skein polynomial of closed 3-braids , J. Reine Angew. Math. 564 (2003),
167-180.
[36] M. Takahashi, Explicit formulas for the Jones polynomials of closed 3-bra ids, Comment.
Math. Univ. St. Paul 38, (1989), no. 2, 129-167.
13
[37] H. Trotter, Non-invertible knots exist , Topology 2 (1963) 275–280.
[38] A. Usman, Conjugacy classes of 3-braid group B3, preprint arXiv:0801.4443.
[39] H. Wu, Braids, transversal links and the Khovanov-Rozansky theor y, Trans. Amer. Math.
Soc. 360 (2008), 3365-3389.
[40] P.J. Xu, The genus of closed 3-braids , J. of Knot Theory and its Ramiﬁcations 1 (1992),
303-326.
[41] P.J.Xu, Growth of the positive braid semigroups , J. Pure Appl. Algebra 80 (1992), no. 2,
197–215.
14
