---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS"
section_id: sec-029-7-open-problems
section_title: "Open problems"
section_number: 7
pages: 123-128
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
doc_brief: "Stabilization in the braid groups I: MTWS — 30 sections: Introduction; The problem; Block-strand diagrams and template"
---
(1) As was pointed out in Section 1.1, Markov’s Theorem is just one example of a class
of theorems about 3–manifolds in which some form of stabilization and destabilization
play an important role. A very different and very important example is the Kirby
Calculus [21], relating two surgery representations of a 3–manifold. The stabilization
move is the addition of an unknot with standard framing to the link that is to be surgered.
In this setting, what should be the analogue of the MTWS? Presumably, the ﬁrst entry
in the complexity function should be the number of components in the surgery link. But
unfortunately, in this regard, we do not know of any tools that could be put to work, to
play the role that was played by the geometry of braid foliations and the group structure
of the braid group in the proof of the MTWS.
(2) There are many analogies between the study of knots via their closed braid
representatives and the study of 3–manifolds via their Heegaard diagrams (or equivalently
Geometry &Topology 10 (2006)
536 Joan S Birman and William W Menasco
via their ‘Heegaard gluing maps’ in the mapping class group of a closed orientable
surface of genus g). In the latter setting equivalence classes of Heegaard splittings are
in 1–1 correspondence with double cosets in the mapping class groupMg modulo the
mapping class groupHg of a handlebody. We pose as an open problem to ﬁnd moves
which (like the moves inT (m)) change the equivalence class of a Heegaard splitting of
a 3–manifold without increasing its Heegaard genus. A strategy for ﬁnding such moves
is given by the second author in [24], however (lacking an invariant) there is no proof
that this strategy actually produces inequivalent splittings. In his PhD thesis [33] Joel
Zablow made a relevant contribution in his study of waves in Heegaard diagrams. Is
there a tool which plays the role of braid foliations in the situation of Heegaard splittings
of 3–manifolds? This seems to be a very interesting area for future investigations.
(3) We pass to open questions about Theorem 2 of this paper. In principle the templates
inT (m) can be enumerated, but the actual enumeration is non-routine. We pose this
as an open problem for m = 4, 5 and any other cases which prove to be computable.
A very interesting special case are to classify the templates inT (m, m). In particular,
these relate any two closed braid representatives when both have minimum braid index.
There should be applications. For example, knowing that the only templates that we
need for braid index 3 are the ﬂype and destabilization templates, it is a simple matter to
classify links which are closed 3–braids (replacing the complicated argument we used
in [11]), and it is to be expected that ifT (4) is computed, then one would learn more
about the classiﬁcation of links of braid index 4. One could expect many applications,
if such an advance in knowledge could be achieved.
(4) Although actual enumeration of T (m) may not be routine, if we restrict our
attention to a single type of isotopy such enumeration or characterization may be
reasonably doable. Speciﬁcally, referring back to Section 5.7, the characterization of all
knot complements that admit a cyclic move predicated on the existence of an essentially
embedded standard annulus in its complement would be of interest. Moreover, such
knot complements could be divided into two classes: the ﬁrst class would have the
components of G++ and G−− being homeomorphic to [0, 1]; and, the second class
would have the components of G++ and G−− being homeomorphic to S1. The ﬁrst
class would use a positive stabilization and destabilization to begin and end the cyclic
move. The second class would use a negative stabilization and destabilization for the
cyclic move. The question is how to determine when a knot is not in both classes, since
the ﬁrst class corresponds to a transversal isotopy and the second class does not. (See
our article [6].)
(5) In the manuscript [ 7] the authors proved that an arbitrary closed braid representative
of a composite knot or link may be modiﬁed by the use of exchange moves to a prime
summand of the same braid index. We do not know whether the work in that paper can
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 537
be incorporated into the proof of the MTWS. The difﬁculty is that we do not know
whether the splitting 2–sphere which realizes the connect-sum operation can be modiﬁed
to one which intersects the clasp annulusCA in a ‘nice’ way.
(6) Some knots or links, for example the unlink [ 9] and most iterated torus links [25],
have unique closed braid representatives of minimum braid index. On the other hand,
there are links of braid index 3 which have more than one conjugacy class of 3–braid
representatives [11], and this pathology clearly persists as braid index is increased. We
pose the open problem: ﬁnd general conditions which sufﬁce for a knot or link type to
have a unique conjugacy class of closed braid representative of minimum braid index.
(7) Referring back to Remark 6.3.2, it would be of interest to understand exactly
how the structure of a minimal genus Seifert surface can restrict the ability of a given
link type having minimal braid index n to be carried by any template ofT (m, n). In
particular, if the Seifert surface has a foliation composed of aa tiles at minimal braid
index isT (m, n) necessarily empty for all values of m.
(8) There are special knots and links, for example the unlink [ 9] and most iterated
torus links [ 25], for which the MTWS is very simple: the moves are simply braid
isotopy and exchange moves. We say that such links are exchange-reducible. Are there
other examples of exchange-reducible links? Does the conclusion hold under weaker
hypotheses?
We remark that by the main result in Birman–Wrinkle [14], if a knot typeX is exchange-
reducible, then every transversal knot typeTX associated toX is transversally simple,
ie determined up to transversal isotopy byX and the Thurston–Bennequin invariant.
Since G–exchange moves and positive ﬂypes are realized by transversal isotopy, it
would be equally interesting if the condition ‘exchange-reducible’ was weakened to
‘exchange and positive ﬂype-reducible’.
(9) As noted in problem (4) above, the unlink is exchange-reducible. This fact proves
that there exists a monotonic and very rapid (perhaps even a quadratic) algorithm for
recognizing the unlink, through the use of exchange moves. Unfortunately, however,
the complexity function that would translate this existence theorem into a working
algorithm needs new techniques, as the complexity function is concealed in the invisible
family of discs which the unlink bounds. (One of these days the ﬁrst author will write a
short note to show that it is also concealed in the auxiliary ‘extended braid word’ of
Birman and Hirsch [ 5].) We note that the unknot recognition algorithms in [ 5] and
the ﬁnite unknot recognition algorithm in the very new paper by Ivan Dynnikov [17],
which is based upon related foliation techniques, are exponential. A vague (but we
feel realistic) problem is to ﬁnd an ‘energy functional’ (AKA complexity function)
which uses the monotonic reduction process that is guaranteed to exist because of
Geometry &Topology 10 (2006)
538 Joan S Birman and William W Menasco
exchange-reducibility. A wild guess is that it is encoded in notions based upon Ricci
curvature.
(10) The MTWS begins with a choice of a closed braid representative X−∈X which
has braid index b(X ), however at this writing we do not know how to compute b(X ).
The most useful tool that we know is the ‘Morton–Franks–Williams inequality’, however
the MFW inequality is doomed to fail in certain situations (see Kawamuro [20]). An
important open problem is to develop new techniques for computing the braid index of
a knot or link. As can be seen from [20], templates can be a very useful tool.
(11) Conjecture:
• Every block-strand diagram in a template inT (m) has at least one block.
We remark that our attempts to ﬁnd a counterexample have been unsuccessful, but
we lack a proof that it cannot happen. Note that the number of counterexamples is
necessarily ﬁnite.
(12) In a standard annulus, the graph G−,δ (resp. G+,δ ) is topologically equivalent to
a circle which cobounds with a component of X+ (resp. X−) an embedded annulus.
That annulus is foliated without singularities. From this is follows that, if we regard
G−,δ and G+,δ as deﬁning knots in R3, then they will have the same knot type as the
component in question ofX . But in fact more can be said. The graph G−,δ (resp. G+,δ )
is a union of arcs, each a branch in a singular leaf, which join up a string of negative
(resp. positive) vertices in a cycle. Each arc lies in a ﬁber of H and has its endpoints on
A, and so this representation of the component ofX has an ‘arc presentation’, in the
sense deﬁned by Cromwell [16] and Dynnikov [17]. Indeed, Ivan Dynnikov has been
engaged in a project which begins with the introduction of braid foliations, and goes
on to study the foliations of the associated Seifert surface bounded by G−,δ and G+,δ ,
adapting the braid foliation machinery in [7] and [9] to arc presentations. One expects
that there will be similar adaptations of the work in this paper to arc presentations,
although the adaptation is almost certainly non-trivial.
One reason why arc presentations are of interest is because they give a ﬁltration of
all knots and links, using the number of arcs as a measure of complexity, and with
that ﬁltration there are always ﬁnitely many arc presentations which represent a given
knot type and have complexity at most the complexity of a given example. This fact is
important if one wishes to use the braid foliation machinery to construct algorithmic
solutions to the knot and link problem.
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 539
References
[1] J W Alexander, A lemma on systems of knotted curves, Proc. Nat. Acad. Sci. USA 9
(1923) 93–95
[2] D Bennequin , Entrelacements et ´equations de Pfaff , from: “Third Schnepfenried
geometry conference, V ol. 1 (Schnepfenried, 1982)”, Ast´erisque 107, Soc. Math. France,
Paris (1983) 87–161 MR753131
[3] J S Birman, Braids, links, and mapping class groups , Princeton University Press,
Princeton, N.J. (1974) MR0375281
[4] J S Birman, E Finkelstein , Studying surfaces via closed braids , J. Knot Theory
Ramiﬁcations 7 (1998) 267–334 MR1625362
[5] J S Birman, M D Hirsch, A new algorithm for recognizing the unknot, Geom. Topol. 2
(1998) 175–220 MR1658024
[6] J S Birman, W W Menasco, Stabilization in the braid groups II: Applications to
transverse knots arXiv:math.GT/0310280
[7] J S Birman, W W Menasco, Studying links via closed braids IV: Composite links and
split links, Invent. Math. 102 (1990) 115–139 MR1069243
[8] J S Birman, W W Menasco, Studying links via closed braids I: A ﬁniteness theorem,
Paciﬁc J. Math. 154 (1992) 17–36 MR1154731
[9] J S Birman, W W Menasco, Studying links via closed braids V: The unlink , Trans.
Amer. Math. Soc. 329 (1992) 585–606 MR1030509
[10] J S Birman, W W Menasco, Studying links via closed braids VI: A nonﬁniteness
theorem, Paciﬁc J. Math. 156 (1992) 265–285 MR1186805
[11] J S Birman, W W Menasco, Studying links via closed braids III: Classifying links
which are closed 3–braids, Paciﬁc J. Math. 161 (1993) 25–113 MR1237139
[12] J S Birman, W W Menasco, On Markov’s theorem, J. Knot Theory Ramiﬁcations 11
(2002) 295–310 MR1905686
[13] J S Birman, M Rampichini, P Boldi, S Vigna, Towards an implementation of the B–H
algorithm for recognizing the unknot, J. Knot Theory Ramiﬁcations 11 (2002) 601–645
MR1915499
[14] J S Birman, N C Wrinkle, On transversally simple knots , J. Differential Geom. 55
(2000) 325–354 MR1847313
[15] G Burde, H Zieschang, Knots, de Gruyter Studies in Mathematics 5, Walter de Gruyter
& Co., Berlin (1985) MR808776
[16] P R Cromwell, Embedding knots and links in an open book I: Basic properties, Topology
Appl. 64 (1995) 37–58 MR1339757
[17] I Dynnikov , Arc presentations of links: monotonic simpliﬁcation arXiv:
math.GT/0208153
[18] T Fiedler, A small state sum for knots, Topology 32 (1993) 281–294 MR1217069
Geometry &Topology 10 (2006)
540 Joan S Birman and William W Menasco
[19] J Hempel, 3–Manifolds, Princeton University Press, Princeton, NJ (1976) MR0415619
[20] K Kawamuro , Failure of the Morton–Franks–Williams inequality arXiv:
math.GT/0509169
[21] R Kirby, A calculus for framed links in S3 , Invent. Math. 45 (1978) 35–56 MR0467753
[22] S Lambropoulou, C P Rourke, Markov’s theorem in 3–manifolds, Topology Appl. 78
(1997) 95–122 MR1465027
[23] A A Markov, Uber die freie Aquivalenz geschlossener Zopfe, Recueil Mathematique
Moscou 1 (1935) 73–78
[24] W W Menasco, Closed braids and Heegaard splittings , from: “Knots, braids, and
mapping class groups—papers dedicated to Joan S. Birman (New York, 1998)”, AMS/IP
Stud. Adv. Math. 24, Amer. Math. Soc., Providence, RI (2001) 131–141 MR1873114
[25] W W Menasco, On iterated torus knots and transversal knots, Geom. Topol. 5 (2001)
651–682 MR1857523
[26] H R Morton, Inﬁnitely many ﬁbred knots having the same Alexander polynomial ,
Topology 17 (1978) 101–104 MR486796
[27] H R Morton, An irreducible 4–string braid with unknotted closure , Math. Proc.
Cambridge Philos. Soc. 93 (1983) 259–261 MR691995
[28] H R Morton, Threading knot diagrams, Math. Proc. Cambridge Philos. Soc. 99 (1986)
247–260 MR817666
[29] M Scharlemann, A Thompson, Thin position and Heegaard splittings of the 3–sphere,
J. Differential Geom. 39 (1994) 343–357 MR1267894
[30] J Singer, Three-dimensional manifolds and their Heegaard diagrams, Trans. Amer.
Math. Soc. 35 (1933) 88–111 MR1501673
[31] P Traczyk, A new proof of Markov’s braid theorem, from: “Knot theory (Warsaw, 1995)”,
Banach Center Publ. 42, Polish Acad. Sci., Warsaw (1998) 409–419 MR1634469
[32] F Waldhausen, Heegaard–Zerlegungen der 3–Sph¨are, Topology 7 (1968) 195–203
MR0227992
[33] J Zablow, Loops, waves and an algebra for Heegaard splittings , PhD thesis, City
University of New York (1999)
Department of Mathematics, Barnard College, Columbia University
2990 Broadway, New York NY 10027, USA
Department of Mathematics, University at Buffalo, Buffalo NY 14260, USA
jb@math.columbia.edu, menasco@math.buffalo.edu
Proposed: Robion Kirby Received: 23 June 2005
Seconded: Benson Farb, David Gabai Accepted: 25 January 2006
Geometry &Topology 10 (2006)
