---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-030-a2-a-sign-term
section_title: "A sign term"
section_number: A.2
pages: 26-29
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
toc_source: inferred
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — We study a computational method of the hyperbolic Reidemeister torsion (also called in the literature"
---
the sense that they are given by Poincar´e duality. In the case of link exteriors, using
such homology orientations we will ﬁx numbers of sign indeterminacy in our formulas.
However, to be exhaustive it remains to us to explicitly compute the Reidemeister torsion
of the long exact sequence in homology associated to the pair (EL, ∂EL). This torsion is
a new sign term, given in the following proposition, which will give us the sign–term in
the symmetry formula for the polynomial torsion (see Section 8, in particular Theorem 14
and Equation (32)).
Proposition 16. The torsion of the long exact sequence in homology associated to the
pair (EL, ∂EL), in which homology groups are endowed with the distinguished bases given
in Equation (39), is equal to (−1)b(b−1)/2.
Proof. Let H∗denotes the long exact sequence in homology associated to the pair
(EL, ∂EL). Counting dimensions, it is easy to observe that H∗is decomposed into the
following three short exact sequences:
(40)
H(i)
∗
: 0 →Hi+1(EL, ∂EL; R)
δ(i)
−−→Hi(∂EL; R)
−j(i)
∗
−−−→Hi(EL; R) →0
for i = 0, 1, 2. Here δ(i) denotes the connecting homomorphism and j(i)
∗
is induced by the
usual inclusion ∂EL֒ →EL. Thus, the torsion of H∗is equal to the alternative product
of the three torsions of the above short exact sequences (40).
The torsions are computed with respect to the bases given in Equation (39) and we
have:
Claim 17. The Reidemeister torsions of the short exact sequences H(i)
∗
are given by:
Tor(H(2)
∗, {h∗
EL, h∗
∂EL, h∗
(EL,∂EL)}, ∅) = (−1)b−1,
Tor(H(1)
∗, {h∗
EL, h∗
∂EL, h∗
(EL,∂EL)}, ∅) = (−1)b(b−1)/2,
Tor(H(0)
∗, {h∗
EL, h∗
∂EL, h∗
(EL,∂EL)}, ∅) = (−1)b−1.
Proof of the claim. Each torsion of the short exact sequences H(i)
∗
can be calculated as
follows.
• Computation of Tor(H(2)
∗, {h∗
EL, h∗
∂EL, h∗
(EL,∂EL)}, ∅).
The connecting homomorphism δ(2) maps [[EL, ∂EL]] to [[T 2
1 ]] + · · · + [[T 2
b ]].
Moreover one has
j(2)
∗([[T 2
ℓ]]) = [[T 2
ℓ]] for ℓ= 1, . . . , b −1.
Thus the set {[[T 2
1 ]], . . . , [[T 2
b−1]]} of vectors in H2(∂EL; R) can be chosen as lifts of
the distinguished basis of H2(EL; R). As a result, the torsion of this short exact
26
sequence H(2)
∗
is given by the following base change determinant:
Tor(H(2)
∗, {h∗
EL, h∗
∂EL, h∗
(EL,∂EL)}, ∅)
=

{δ([[EL, ∂EL]]), [[T 2
1 ]], . . . , [[T 2
b−1]]}/{[[T 2
1 ]], [[T 2
2 ]], . . . , [[T 2
b ]]}

=

1
1
...
...
1
1
1

= (−1)b−1.
• Computation of Tor(H(1)
∗, {h∗
EL, h∗
∂EL, h∗
(EL,∂EL)}, ∅).
The connecting homomorphism δ(1) maps [[Sℓ]] to [[λℓ]]+P
k̸=ℓℓk(Kℓ, Kk)[[µk]]
where ℓk denotes the linking number.
Moreover, j(1)
∗([[µℓ]]) = [[µℓ]], for ℓ=
1, . . . , b. Thus, the set {[[µ1]], . . . , [[µb]]} of vectors in H1(∂EL; R) can be chosen
as lifts of the distinguished basis of H1(EL; R). It follows that the torsion of the
short exact sequence H(1)
∗
is given by the ratio of the following two determinants
of bases change matrices:
Tor(H(1)
∗, {h∗
EL, h∗
∂EL, h∗
(EL,∂EL)}, ∅)
= [{δ([[S1]]), . . . , δ([[Sb]]), [[µ1]], . . . , [[µb]]}/{[[λ1]], [[µ1]], . . . , [[λb]], [[µb]]}] .
(41)
Observe that the determinant in the right-hand side of Equation (41) can be
written again as the product of the following two base change determinants:
D1 = [{δ([[S1]]), . . . , δ([[Sb]]), [[µ1]], . . . , [[µb]]}/{[[λb]], . . . , [[λ1]], [[µ1]], . . . , [[µb]]}] ,
D2 = [{[[λb]], . . . , [[λ1]], [[µ1]], . . . , [[µb]]}/{[[λ1]], [[µ1]], . . . , [[λb]], [[µb]]}] .
It is easy to observe that
D1 = [{[[λ1]], . . . , [[λb]], [[µ1]] . . . , [[µb]]}/{[[λb]], . . . , [[λ1]], [[µ1]], . . . , [[µb]]}]
=

0
· · ·
1
...
. . .
...
1
· · ·
0

= (−1)b(b−1)/2,
and that D2 = 1, because it is the signature of a product of even permutations.
As a conclusion, we have that
Tor(H(1)
∗, {h∗
EL, h∗
∂EL, h∗
(EL,∂EL)}, ∅) = (−1)b(b−1)/2.
• Computation of Tor(H(0)
∗, {h∗
EL, h∗
∂EL, h∗
(EL,∂EL)}, ∅).
The connecting homomorphism δ(0) maps [[γℓ]] to [[pb]] −[[pℓ]], for all ℓ=
1, . . . , b −1. Also observe that j(0)
∗([[pb]]) = [[pb]]. Thus, the torsion of the short
exact sequence H(0)
∗
is given by the following base change determinant:
Tor(H(0)
∗, {h∗
EL, h∗
∂EL, h∗
(EL,∂EL)}, ∅) = [{δ([[γ1]]), . . . , δ([[γb−1]]), [[p1]]}/{[[p1]], . . . , [[pb]]}]
=


−1
...
...
−1
1
· · ·
1
1

= (−1)b−1.
□
Using this result, we conclude that the torsion Tor(H∗, {h∗
EL, h∗
∂EL, h∗
(EL,∂EL)}, ∅) of
H∗is given by Q2
i=0 Tor(H(i)
∗, {h∗
EL, h∗
∂EL, h∗
(EL,∂EL)}, ∅)
(−1)i
= (−1)b(b−1)/2.
□
27
References
[CS83]
M. Culler and P. B. Shalen, Varieties of group representations and splittings of 3-manifolds,
Ann. of Math. 117 (1983), 109–146.
[DHY09]
J. Dubois, V. Huynh, and Y. Yamaguchi, Non-abelian Reidemeister trosion for twist knots,
J. Knot Theory Ramiﬁcations 18 (2009), 303–341.
[Dub05]
J. Dubois, Non abelian Reidemeister torsion and volume form on the SU(2)-representation
space of knot groups, Ann. Institut Fourier 55 (2005), 1685–1734.
[FK06]
S. Friedl and T. Kim, The Thurston norm, ﬁbered manifolds and twisted Alexander polyno-
mials, Topology 45 (2006), 929–953.
[FKK]
S. Friedl, T. Kim, and T. Kitayama, Poincar´e duality and degrees of twisted Alexander
polynomials, in preparation.
[FT00]
M. Farber and V. Turaev, Poincar´e-Reidemeister metric, Euler structures, and torsion, J.
Reine Angew. Math. 520 (2000), 195–225.
[FV09]
S. Friedl and S. Vidussi, A survey of twisted Alexander polynomials, arXiv:0905.0591, 2009.
[HLMA92] H. M. Hilden, M. T. Lozano, and J. M. Montesinos-Amilibia, A characterization of arithmetic
subgroups of SL(2, R) and SL(2, C), Math. Nachr. 159 (1992), 245–270.
[HSW]
J. Hillman, D. Silver, and S. Williams, On reciprocality of twisted Alexander invariants,
arXiv:0905.2574.
[Joh]
D. Johnson, A geometric form of Casson invariant and its connection to Reidemeister tor-
sion, Unpublished Lecture Notes.
[JW93]
Lisa Jeﬀrey and Jonathan Weitsman, Half density quantization of the moduli space of ﬂat
connections and witten’s semiclassical manifold invariants, Topology 32 (1993), 509–529.
[Kit96]
T. Kitano, Twisted Alexander polynomial and Reidemeister torsion, Paciﬁc J. Math. 174
(1996), 431–442.
[KK90]
P. Kirk and E. Klassen, Chern–Simons invariants of 3-manifolds and representation spaces
of knot groups, Math. Ann. 287 (1990), 343–367.
[KL99]
P. Kirk and C. Livingston, Twisted Alexander Invariants, Reidemeister torsion, and Casson-
Gordon invariants, Topology 38 (1999), 635–661.
[KM05]
T. Kitano and T. Morifuji, Divisibility of twisted Alexander polynomials and ﬁbered knots,
Ann. Sc. Norm. Super. Pisa Cl. Sci. 4 (2005), 179–186.
[LM85]
A. Lubotzky and A. R. Magid, Varieties of representations of ﬁnitely groups, Mem. Amer.
Math. Soc. 58 (1985), no. 336, xi+117.
[Mil62]
J. Milnor, A Duality theorem for Reidemeister Torsion, Ann. of Math. 76 (1962), 134–147.
[Mil66]
, Whitehead torsion, Bull. Amer. Math. Soc. 72 (1966), 358–426.
[Mil68]
, Inﬁnite cyclic coverings, Conference on the Topology of Manifolds (Michigan State
Univ., E. Lansing, Mich., 1967) (1968), 115–133.
[Par97]
J. Park, Half–density volumes of representation spaces of some 3–manifolds and their appli-
cation, Duke Math. J. 86 (1997), 493–515.
[Por97]
J. Porti, Torsion de Reidemeister pour les vari´et´es hyperboliques, Mem. Amer. Math. Soc.
128 (1997), no. 612, x+139.
[Rol90]
D. Rolfsen, Knots and links, Publish or Perish Inc., 1990.
[Sei34]
H. Seifert, ¨Uber das Geschlecht von Knoten, Math. Ann. 110 (1934), 571–592.
[Thu02]
W. Thurston, The Geometry and Topology of Three-Manifolds, Electronic Notes available
at http://www.msri.org/publications/books/gt3m/, 2002.
[Tur]
V. Turaev, A homological estimate for the thurston norm, arXiv:math/0207267.
[Tur86]
, Reidemeister torsion in knot theory, Uspekhi Mat. Nauk 247 (1986), 97–147.
[Tur01]
, Introduction to combinatorial torsions, Lectures in Mathematics, Birkh¨auser, 2001.
[Tur02]
, Torsions of 3-dimensional manifolds, Progress in Mathematics, vol. 208, Birkh¨auser,
2002.
[Wad94]
M. Wada, Twisted Alexander polynomial for ﬁnitely presentable groups, Topology 33 (1994),
241–256.
[Wit91]
E. Witten, On Quantum Gauge Theories in Two Dimensions, Commun. Math. Phys. 141
(1991), 153–209.
[Yam08]
Y. Yamaguchi, A relationship between the non-acyclic Reidemeister torsion and a zero of
the acyclic Reidemeister torsion, Ann. Inst. Fourier (Grenoble) 58 (2008), 337–362.
Institut de Math´ematiques de Jussieu, Universit´e Paris Diderot–Paris 7, UFR de Math´ematiques,
Case 7012, Bˆatiment Chevaleret, 75205 Paris Cedex 13 France
E-mail address: dubois@math.jussieu.fr
28
Department of Mathematics, Tokyo Institute of Technology, 2-12-1 Ookayama Meguro-ku,
Tokyo 152-8551, Japan
E-mail address: shouji@math.titech.ac.jp
29
