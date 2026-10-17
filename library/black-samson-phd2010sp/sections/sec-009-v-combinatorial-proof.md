---
doc_id: black-samson-phd2010sp
doc_title: "REPRESENTATIONS OF HECKE"
section_id: sec-009-v-combinatorial-proof
section_title: "COMBINATORIAL PROOF"
section_number: V
pages: 49-58
source_pdf: Black_Samson_phd2010sp.pdf
source_sha256: c16799b0bd54ff29
toc_source: inferred
---
In this chapter we prove Theorem IV.2.2 directly from formulas (IV.lO) and (IV.ll). Since
the function A is defined on the set of words in the braid generators, we must show that A is well-
defined on the braid group.
V.l.
Braid Group Invariance
For a permutation diagram x, let 7r(x) E Sd denote the underlying permutation.
Let
pT,(a) = {x permutation diagram satisfying (PI) /7r(x) = 7r}.
Notice that P1(a) = P(a), the
admissible diagrams. 'vVe have immediately:
P(afJ)
IT {xy I x E P,,(a) and y E P,,-l (fJ)}
"ESd
IT P,,(a) x P,,-1(fJ)
"ESd
(V.l)
\iVith signs attached to the strands in the diagrams, we have the analogous definition of S,,(a) and
the decomposition:
S(afJ) ~ IT S,,(a) x S,,-1 (fJ)·
"ESd
(V.2)
\iVe prove a Lemma now that shows that the function A is invariant under concatenation
for certain pairs of braid words. For 7r E Sd, define
A,,(a) =
I.: (c:)M(a,x,c:)
(x,c)ES,,(ex)
(V.3)
Lemma V.l.l. Suppose that fJ, fJl E ~j satisfy A,,(fJ) = A,,(fJ') faT' all 7r E Sd.
Then, A(afJ) =
A(afJ') and A(fJa) = A(fJ'o:) for any 0: E ~j.
42
P7'Oof. Let Srr(a,f3) = S7T(a) x SCI ({3).
L (cv)M(a{3, xy, EV)
S, (ex,(3)
1
A(a(3) = 1dJ L
7TE S d
1
= 1dJ L
L
(E)M(a, x, E) L
(v)M({3, y, v)
7TES" (x.E)ES,,(a)
(Y,l/)ES,,-I ((3)
1
= [d] L
L
(E)l\1(a, x, E) A 7T-I ({3)
7TES" (x,E)ES,,(a)
(VA)
(V.5)
(V.6)
This last expression is equal to A(a{3'), using the fact that A7T ((3)
A({3a) = A({3'a) is completely analogous and is omitted.
A7T ({3').
The proof that
o
Proposition V.1.2. If a, (3 E I:d represent the same group element in 3 d , then A(a) = A({3).
Proof. Identity. A(1a) = A(a) = A(a1).
This is clear since A is defined by resolving crossings in the braid diagram. For the remainder of
the proof, we use Lemma V.l.1, checking cases according to permutations 7f.
Inverse.
A((J;!=I(J~I) = A(0).
Let (x,c) E S7T((J,.(J,~I), where 7r = 7r(x). We must show that A7T ((Jr(J;I) = 1 when 7r = 1 and 0
otherwise.
(Case 7r = 1). If the signs on strands rand r + 1 match, then the only available diagrams
have the crossings (Jr(J;1 resolved straight through. If (cr,Er+d = (+,+), then M((Jr(J;I,X,c) =
v· V-I = 1. And with (-, -),
M((Jr(J,~l,x,E) = (_V-I). (-V) = 1. If Er i- Er+l, then there are
two possible resolutions that form states, as illustrated.
I \
+ -
or Q
+ -
With (cr, cr+d = (+, -), we calculate the contribution of the two states is
_v- r
-v r
[r+1]
[r-1]
--.-+--.--
IT]
[r]
[r]
[r]'
which equals 1, using Lemma V.2.3.
With (cr' Er+d = (-, +), a similar calculation establishes
equality.
43
then there are two possible resolutions that form states, as illustrated.
~
+ -
or ><
+ -
'With (cTlcr+Jl = (+, -), we calculate the contribution from the two states is
[1'-1]
-vr
v r
[1'-1]
--·-+-·--=0.
[1']
[1']
[1']
[1']
The calculation with (cr,cr+Jl = (+, -) is analogous and is omitted.
Braid relations. A((Jr(Js) = A((Js(Jr) when IT - sl > 1. This is a simple calculation only
using the commutativity of the ring C(v).
A((Jr(Jr+)tJr)
=
A((Jr+l(Jr(Jr+l).
Let x (resp., y) denote a permutation diagram for
(Jr(Jr+l(Jr (resp., (Jr+l(Jr(Jr+l)'
Again, we organize by cases -rr = -rr(x) = -rr(y).
In Figure V.2,
the possible permutation diagrams are shown with labels suggesting the possible signs on those
strands.
For example, the label (a, b, b) indicates that possible signs are (+, +, -), (+, -, +),
(-, +, -), or (-, -, +). Permutations are named by how they act on strands 1', l' + 1, and l' + 2.
Notice that for -rr = (3 2 1), there are no ways to assign signs, as each pair of strands crosses.
,Ve illustrate one calculation (of twenty):
-rr = 1 and (cr' Cr+l, Cr+2) = (-, -, +). These
signs match each of the patterns except (a, a, c), so it suffices to verify that the following equation
holds:
This is equivalent to showing that vr~l[T + 1] = ~_v2r+l + Vr[T + 2], which follows from Lemma
V.2.3.
0
V.2.
Markov Moves
Now that we have established that A
!3
--'> q v) is well-defined, we check that A is
invariant under the Markov moves.
Lemma V.2.1.
The state-sum fOTm'ula in (IV.ii) descends to a well-defined link invaTiant:
A(a) = A(,6) if a and,6 aTe Telated by the MaTkov moves.
PTOOf. In order to show invariance under the cyclic move (II.2), note that there is a bijection
44
n=l
abc
a
a
C
abc
a
b
b
n=(12)
aaC
aa
C
a a
C
~ ~ (2 3)
~
a
b
b
a
b
b
a
b
b
n = (1 23)
a
a a
a
a a
n = (1 32)
a
a a
a a a
n=(32l)
Figure V.l: Possible states x and y, organized according to n.
between states for a{3 and {3a, defined as follows.
Any admissible permutation diagram of a{3looks like the concatenation xy, where x (resp.,
y) is a permutation diagram for a (resp., (3). The diagrams x and y may not be admissible, but
n(x)n(y) = n(xy) = 1.
So, yx is admissible, as well, since left- and right-inverses agree in a
group. For any state (xy,e) E S(a{3) , (yx,n(y).e) is a state for (3a, where n(y).e denotes the
signs permuted by n(y).
Beginning with a state for (3a, and repeating the procedure, only this time, twisting
the signs by n(x), we construct an inverse.
Now, since M(a{3,xy,e) = M({3a,yx,n(y).e) and
; ...~...
+ + -
~
...~.
:
~ .
+ -
+
45
Figure V.2: A state (xy,E) for 0:{3 and the corresponding state ({3o:,7l"(y).E) for (30:.
(E) = (7l"(y).E) for each state of 0:{3, we obtain the equality A(o:{3) = A({3o:).
To prove invariance under the stabilization move (II.3), observe that the crossing ad must
be resolved straight through in order to form an admissible permutation diagram. Assume that
Ed-l = + (the other case is similar). Then, for each state (X,E) for 0:, either sign on strand d forms
a state for o:ad. Call them (y,E±), respectively.
Calculate the contribution to the state-sum for each such pair of states:
(E+)M(o:ad, y, E+) + (E-) M(o:ad ,y, E-)
(v __~~n) (E)M(o:,X,E)
[d+ 1J
[dj(E)M(o:, x, c)
Now, A(o:ad) = A(o:) follows once the global normalizations are included.
(V.7)
o
.I....:.:..:....I..~
..:
0:
:
·I···············I··~;
.. .
"
;.1..:.:.:..1..1.
:
x
:
:'T"~::'r'I";
+ +
i··I··:·:·~···.l.J1
or
;. 'I'~':':"" '1''1":
+ -
Figure V.3: The states (y,E+) and (y,E_) for o:an associated to the state (X,E) for 0:.
Theorem V.2.2. For any link L and any choice of braid word w whose closure is L,
A(w) = t::.(L).
Proof. By Lemma V.2.1, the function A is a link invariant, so it suffices to show that it agrees
with the Alexander-Conway polynomial. There are two things to show: the skein relation and the
Conway normalization.
I '" j I .., I
..........................-
I,LL: J
I ",,-;11"
... r,'"
L_
..I::'.J..J··:.I..
·1........\......[
·..·\..
.. -
.
Lo
46
Figure V.4: The Conway skein relation on links:
~(L+) -
~(L_) = (v -
v-1)~(Lo)
For the skein relation, it suffices to show that
(V.8)
Let x be any permutation diagram for a, and let y + and y _ be permutation diagrams for aO'r and
aO';1, respectively. Now, consider the permutation 7r = 7r(x). If 7r = 1, so x is admissible, then
Y± must be resolved straight through to form states. For any such state with sign sequences with
(Cr' Cr+1) equal to (+, +) or (-, -), we verify that
When the signs on strands rand r + 1 are different, we calculate
(vr. v-r)
M(aO'nY+,c) - M(aO';l,y_,c) =
[r] - [;:r
M(a,x,c)
= (v - v- 1)M(a,x, c).
(V.g)
(V.lO)
Finally, consider the case where 7r = (r r + 1), so x is not admissible. There are no states
for a with such a permutation diagram.
Any state for aO'; 1 must have y ± with a crossing of
strands rand r + 1. The contribution to the sum when (cr, cr+d = (+, -) is
-1
([r+1]
[r+1])
M(aO'r,Y+,c) - M(aO'r
,y_,c) =
~ - ~
M(a,x,c) = O.
The case (cn cr+ 1) = (-, +) gives 0 as well.
The Conway normalization for the Alexander polynomial has \l(unknot) = 1. A braid
representative is the trivial braid on one strand. There is only one state available, carrying the
sign +. The weight involves the empty product, hence gives value 1.
D
47
Lemma V.2.3. The following identities hold for quantum integers:
min(r,s)
[r][sJ
=
L
[r + s + 1 - 2k]
k=l
[r + s][r - sJ
[rJ2 - [sf
[r + s]
r, s 2: 0
(V.l1)
(V.12)
(V.13)
Proof The proofs are elementary and follow from the definition of quantum integers.
0
48
REFERENCES
[1] J. W. Alexander, Topological invariants of knots and links, Trans. ArneI'. Math. Soc. 30 (2)
(1928) 275-306.
[2] J. W. Alexander II, A lemma on systems of knotted curves, Nat. Acad. Proc. 9 (1923) 93-95.
[3] E. Artin, Theory of braids, Ann. of Math. (2) 48 (1947) 101-126.
[4] G.
Benkart,
S.-J. Kang,
M. Kashiwara,
Crystal bases for the quantum superalgebra
Uq(gl(mln)), J. Amer. Math. Soc. 13 (2) (2000) 295-331.
[5] A. Berele, A. Regev, Hook Young diagrams, combinatorics and representations of Lie super-
algebras, Bull. Amer. Math. Soc. (N.S.) 8 (2) (1983) 337-339.
[6] J. S. Birman, Braids, links, and mapping class groups, Princeton University Press, Princeton,
N.J., 1974, annals of Mathematics Studies, No. 82.
[7] J. S. Birman, T. E. Brendle, Braids: a survey, in: Handbook of knot theory, Elsevier B. V.,
Amsterdam, 2005, pp. 19-103.
[8] J. Brundan, A. Kleshchev, Blocks of cyclotomic Hecke algebras and Khovanov-Lauda algebras,
Invent. Math. 178 (3) (2009) 451-484.
[9] J. H. Conway, An enumeration of knots and links, and some of their algebraic properties,
in:
Computational Problems in Abstract Algebra (Proc. Conf., Oxford, 1967), Pergamon,
Oxford, 1970, pp. 329-358.
[10] P. R. Cromwell, Knots and links, Cambridge University Press, Cambridge, 2004.
[11] C. W. Curtis, 1. Reiner, Methods ofrepresentation theory. Vol. I, II, Pure and Applied Math-
ematics (New York), John Wiley & Sons Inc., New York, 1987, with applications to finite
groups and orders, A Wiley-Interscience Publication.
[12] R. Dipper, G. James, Representations of Hecke algebras of general linear groups, Proc. London
Math. Soc. (3) 52 (1) (1986) 20-52.
[13] R. Dipper, G. James, Blocks and idempotents of Hecke algebras of general linear groups, Proc.
London Math. Soc. (3) 54 (1) (1987) 57-82.
[14] P. Freyd, D. Yetter, J. Hoste, W. B. R. Lickorish, K. Millett, A. Ocneanu, A new polynomial
invariant of knots and links, Bull. Amer. Math. Soc. (N.S.) 12 (2) (1985) 239-246.
[15J W. Fulton, Young tableaux, vol. 35 of London Mathematical Society Student Texts, Cam-
bridge University Press, Cambridge, 1997, with applications to representation theory and
geometry.
[16] M. Geck, The character table of the Iwahori-Hecke algebra of the symmetric group: Starkey's
rule, C. R. Acad. Sci. Paris Ser. I Math. 329 (5) (1999) 361-366.
49
[17] M. Geck, N. Jacon, Ocneanu's trace and Starkey's rule, J. Knot Theory Ramifications 12 (7)
(2003) 899-904.
[18] A. Gyoja, A q-analogue of Young symmetrizer, Osaka J. Math. 23 (4) (1986) 841-852.
[19] P. N. Hoefsmit, Representations of hecke algebras of finite groups with bn-pairs of classical
type, PhD in Mathematics, University of British Columbia (1974).
[20) J. C. Jantzen, Introduction to quantum groups, in: Representations ofreductive groups, Publ.
Newton Inst., Cambridge Univ. Press, Cambridge, 1998, pp. 105-127.
[21] M. Jimbo, A q-difference analogue of U(g) and the Yang-Baxter equation, Lett. Math. Phys.
10 (1) (1985) 63-69.
[22] M. Jimbo, Quantum R matrix related to the generalized Toda system: an algebraic approach,
in: Field theory, quantum gravity and strings (Meudon/Paris, 1984/1985), vol. 246 of Lecture
Notes in Phys., Springer, Berlin, 1986, pp. 335-361.
[23] V. F. R. Jones, A polynomial invariant for knots via von neumann algebras, Bull. Am. Math.
Soc., New Ser. 12 (1985) 103-111.
[24] V. F. R. Jones, Hecke algebra representations of braid groups and link polynomials, Ann. of
Math. (2) 126 (2) (1987) 335-388.
[25] C. Kassel, V. Turaev, Braid groups, vol. 247 of Graduate Texts in Mathematics, Springer,
New York, 2008, with the graphical assistance of Olivier Dodane.
[26] L. H. Kauffman, State models and the Jones polynomial, Topology 26 (3) (1987) 395-407.
[27J L. H. Kauffman, D. Radford, Bi-oriented quantum algebras, and a generalized Alexander
polynomial for virtual links, in: Diagrammatic morphisms and applications (San Francisco,
CA, 2000), vol. 318 of Contemp. Math., Amer. Math. Soc., Providence, RI, 2003, pp. 113-140.
[28] L. H. Kauffman, H. Saleur, Free fermions and the Alexander-Conway polynomial, Comm.
Math. Phys. 141 (2) (1991) 293-327.
[29] D. Kazhdan, G. Lusztig, Representations ofCoxeter groups and Hecke algebras, Invent. Math.
53 (2) (1979) 165-184.
[30] M. Khovanov, A categorification of the Jones polynomial, Duke Math. J. 101 (3) (2000)
359-426.
[31] A. Markoff, Uber die freie Aquivalenz der geschlossenen zopfe, Rec. Math. Moscou, n. Ser. 1
(1936) 73-78.
[32] H. Mitsuhashi, Schur-Weyl reciprocity between the quantum superalgebra and the Iwahori-
Hecke algebra, Algebr. Represent. Theory 9 (3) (2006) 309-322.
[33] J. Murakami, A state model for the multivariable Alexander polynomial, Pacific J. Math.
157 (1) (1993) 109-135.
[34] J. H. Przytycki, P. Traczyk, Invariants of links of Conway type, Kobe J. Math. 4 (2) (1988)
115-139.
[35] A. Ram, Seminormal representations of Weyl groups and Iwahori-Hecke algebras, Proc. Lon-
don Math. Soc. (3) 75 (1) (1997) 99-133.
50
[36] N. Y. Reshetikhin, V. G. Turaev, Ribbon graphs and their invariants derived from quantum
groups, Comm. Math. Phys. 127 (1) (1990) 1-26.
[37] L. Rozansky, H. Saleur, Quantum field theory for the multi-variable Alexander-Conway poly-
nomial, Nuclear Phys. B 376 (3) (1992) 461-509.
[38] 1. Schur, Uber die rationalen Darstellungen der allgemeinen linearen Gruppe., Sitzungsberichte
Akad. Berlin 1927 (1927) 58-75.
[39] W. Soergel, Kazhdan-Lusztig polynomials and a combinatoric[s] for tilting modules, Repre-
sent. Theory 1 (1997) 83-114 (electronic).
[40] O. Y. Viro, Quantum relatives of the Alexander polynomial, Algebra i Analiz 18 (3) (2006)
63-157.
[41] H. Weyl, The Classical Groups. Their Invariants and Representations, Princeton University
Press, Princeton, N.J., 1939.
