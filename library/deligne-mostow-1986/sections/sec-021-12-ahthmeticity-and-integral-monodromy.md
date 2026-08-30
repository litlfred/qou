---
doc_id: deligne-mostow-1986
doc_title: "Monodromy of hypergeometric functions and non-lattice integral monodromy"
section_id: sec-021-12-ahthmeticity-and-integral-monodromy
section_title: "AHthmeticity and Integral Monodromy"
section_number: 12
pages: 64-76
source_pdf: deligne-mostow-1986.pdf
source_sha256: d9850f70ab2fecbd
doc_brief: "Monodromy of hypergeometric functions and non-lattice integral monodromy — 27 sections: P. DELIGNE AND G. D. MOSTOW; P. DELIGNE AND G. D. MOSTOW; Cohomology of a rank one local sys"
---
(12.1) Assume that for each s e S, pi, is a rational number and let d denote the
least common denominator of {(JiJjeS}. Set F == Q^(^T), 0 the ring of integers
in F, and V == H^P,, Lo) where P, = P — o(S) as in (3.1). Then the vector
space V can be defined over the ring O. To see this, let L(F) (resp. L(^)) denote a
local subsystem ofL on P^ (suitably chosen using a base point on Po) with fiber the sub-
field F (resp. subring 0) of C. The pairing of L with its complex conjugate induces an
^P-valued pairing on L^). Then one can define cohomology combinatorially as in (2.2)
with coefficients in L(^); one can also define the skew-hermitian cup product
^: ir(P,, LW OOH^P,, LW ->H^, 0) w (9
combinatorially; set
V(^)==Hi(P^LTO, V(F)==HI(P,,L(F),).
Define
(12.1.1) M^v) ==j<p(M,y),
where j = b — ~b for some b e 0 — 0 n R. This ^ is a hermitian form on V defined
over 0 and may be identified with the form defined in (2.i8), up to a real scalar factor.
We lift the map 6 : 7Ti(%, o) -> PU(V) of (3. lo. 2) via a local system L on M{c)
to 6': ^(M^), o) -^ U(V) by (3.14). The image of 6' is in U(V) {0). Set
(12.1.2) I\=Ime, r^==Im6'
where a =={exp 2mpiJ s e S}. Then
(12.1.3) r^ stabilizes V(^).
(12.2) We collect here some remarks and definitions pertaining to arithmeticity of
lattices.
Let r be a Zariski-dense subgroup ofG(^), for G an adjoint connected semi-simple
algebraic group G over k, a field of characteristic o. Set E = %[TrAd F], the field
spanned over % by {Tr Ad y | Y e r}.
Proposition (12.2.1)
(i) The group G has a faithful matrix representation p such that p(F) C GI^(E) {and
hence G has E as a field of definition).
(ii) E remains unchanged when F is replaced by a commensurable subgroup of G.
Proof. — Let T denote the function g }-> Tr Ad g on G, and let W denote the C-linear
span of the left G-translates of T (we define (xj) {y) ==/(jw) for any function/: G->C,
x andj? in G). Inasmuch as T is a sum of matrix coefficients, W is finite dimensional.
Since F is Zariski dense in G, there is a finite set of elements x^ ..., ^ in F such that
67
68 P.DELIGNEANDG.D.MOSTOW
(B == {^.T, ..., yT} is a base of W. Let p^ : G -> Aut W be the representation
given by x \-> x .f for x e G, / e W. It is well known that the representation p^ is
faithful ([ioj, Theorem (2. i), p. 123). Let p(^) denote the matrix ofp^(^) with respect
to the base (B. Then p(A:) has all its entries in the field E for all x e F.
To prove (ii) it clearly suffices to consider the case that 1^ is a subgroup of F of
finite index. Replacing F^ by d xFx~1^ we can suppose moreover that 1^ is normal
in P. Then Fg is also Zariski-dense in G. Set Eo == Q,[Tr Ad FJ and select the base
(B =={^.T,..., A^.T} with Xi e FQ {i == i, ..., n). Let a : E -> C be a mono"
morphism which is the identity on Eo. To prove (ii), it suffices to prove that a leaves
each element of E fixed. For any y e F and x e FQ, we have yxy~1 e FQ. Hence,
by (12.2.1),
PCW)-1 = °P(W1) == °P(jO W °P(^-1,
that is pOOpWpOO-1^0?^)?^)0?^)--1. Hence for all y e FQ, p(j0-10 p(j0
centralizes p(ro) and therefore p(G) since Fg is Zariski-dense in G. The center of p(G)
is i and consequently °p(^) = p(j^) for all y e G. Therefore a fixes each element ofE.
(12.2.2) Take p as in (12.2.1). The Zariski closure of p(F) in GL^(E) is an
algebraic group over E. Because taking Zariski closure commutes with field extensions
it is a form of G over E. This provides the group G with an E-structure, called the
natural E-structure of G. If p' is another faithful matrix representation of G with
p'(r) C GL^(E), it leads to the same E-structure. To check this, one compares p to p'
via p <9 p'.
If F is a subfield ofk and Gp an F-structure on G for which FC Gp(F), the field
of traces E is contained in F and, by the above construction applied to Gp over F, the
given F-structure on G is deduced from the natural E-structure.
(12.2.3) Let A be a semi-simple algebraic linear group defined over the field Q,
of rational numbers, let V be a finite dimensional vector space defined over Q, and
p:A -> GL(V) a faithful rational representation defined over Q,. By a theorem of
Borel-Harish-Chandra [3], the subgroup F == p'^GL^z)) is a lattice in A(R) for any
lattice Vz in VQ; that is, F is a discrete subgroup ofA(R) and A(R)/F has finite measure.
(12.2.4) Let G be an adjoint connected semi-simple real Lie group. It is the
topological connected component G(R)° ofG(R), for G an adjoint connected semi-simple
algebraic group over R. By definition, a subgroup F of G is arithmetic in G if and only
if there exists an algebraic group A over %, a compact group K and an analytic iso-
morphism 6 ofA(R)° onto G X K such that 8(A(Z) n A(R)°) has its projection into G
commensurable to F. The group A is necessarily reductive. It can be assumed
connected adjoint semi-simple; namely, replace A by A°/center (A°). The group A is
then a product of Q^-simple groups A» (cf. [23], p. 46 (3. i .2)). If G is a simple non-
€8
MONODROMY OF HYPERGEOMETRIC FUNCTIONS 69
compact Lie group, it follows from the definition that all A, but one, A^, are such that
A^(R) is compact. Replacing A by A^, one can then assume that A is Q^-simple, i.e. of
the form (cf. [23], p. 46 (3.1.2))
A == Restrp/Q B
for B an absolutely simple group over a finite extension F of Q^. One has F ® R == II F,,v
(product of the completions of Fat the infinite places v) and A(R) == B(F®R) == nB(FJ.v
The existence of 6 as in (12.2.4) amounts to saying that for all v but one, ^, B(FJ is
compact (hence if v 4= Vi the place v is a real place) and that B(F^,)° ^ G, the isomor-
phism carrying B(<5) to a subgroup of G commensurable to F. If G is an absolutely
simple Lie group, the place v^ is a real place, F is totally real, and B is an F-form of G,
F being identified with a subfield of R via ^.
(12.2.5) Assume that G is absolutely simple non compact. In our application,
it is PU(i, N — 3). By the Borel density theorem, any arithmetic T in G is Zariski
dense. If A == Restrp/Q B is as above, with F C R, B an F-form of G, and F a sub-
group commensurable to B(^p), then by (12.2. i), (12.2.2) FDE and the F-form B is
deduced from the natural E-structure of G defined by F. For all the real places v of F
above the identity embedding of E, the G(FJ are isomorphic, hence non compact.
There can hence be only one such v. Hence F = E. We conclude:
(12.2.6) Assume G is an adjoint connected absolutely simple non compact Lie
group. Then a subgroup F C G is arithmetic if and only if
a) the field of traces E is totally real;
b) for each embedding <rofEinR distinct from the identity embedding (°G) (R)
is a compact group (i.e. the real group G ®^ o ®- deduced from the natural E-structure
ofG is compact). G being as in (12.2.4);
c) r is commensurable with G(^g).
(12.2.7) Let G be an adjoint connected absolutely simple non compact Lie group,
and let F be a lattice in G. Assume a totally real number field F C R, and a form Gp
of G over F are given, such that a subgroup of finite index of F is contained in G(^p).
Then the field E == (^[TrAd F] is contained in F by (12.2.1).
Corollary (12.2.8). — A lattice FC G is arithmetic in G if and only if ^ for each embed-
ding a ofF in R, not inducing the identity embedding of E in R, the real group Gp ®p g R is
compact [i.e. °G(R) is a compact group).
Proof. — Since E C F, a) of (12.2.6) is implied by the assumption that F is totally
real. By (12.2.2), the given F-structure ofG is deduced from the natural E-structure
and rcG(E). The condition in (12.2.8) amounts to b) of (12.2.6). Assume it
69
7° P. DELIGNE AND G. D. MOSTOW
holds. Then, G(^) is an arithmetic lattice in G(R). A subgroup of finite index in F
lies in G(E) n G(^p) and hence G(^) contains a subgroup F of finite index in I\
Both F and G(^), being lattices in G(R), have finite covolume; hence the index of F'
in G{0^) is finite. Condition c) of (12.2.6) follows.
The criterion (12.2.8) will be applied to test the arithmeticity of I\ in PU(V, ^)-
(12.3) We shall need more explicit information about monodromy than given
in (9.2) in order to compute %[Trr^ where 1^ is as in (12. i .2). The result
needed is (12.5. i). Actually, by consulting the explicit lists in § 14, one can obtain the
required information in a case-by-case inspection except in three of the cases.
For the remainder of § 12, we assume o < ^ < i and ^ e % for all s e S.
Let S == Si u 82 with card 82 == i, let T^, Tg be trees as in (2.5) with the
vertices ofT, in S, (i = i, 2), and let (3 : Ti u Tg -> P be an embedding with (3 | S == o,
the base point of M.
Without loss of generality, we can assume that Ti is homeomorphic to the interval
o <_ x < i.
Fix an orientation on T^, let ^i, . . ., JN-I denote the vertices of T^ taken in order,
and let a, denote the oriented edge from s, to ^ (i <_ i <^ N — 2). Let T denote the
cone over T^ u T^ with apex A and denote by (B also an extension of (B to an embedding
of T in P. Since T — {s^, ..., s^} is simply connected, the pull-back p" L may be
identified with the constant system C on it, and we can choose /^) e H°(a,, (3* L) for
each i so that
(12.3.1) f{a,)^\a,w -i.(B[^.+ i.(3|^, i^<N-2
where ?, is the arc from A to s, and w denotes homology. Let w, denote the element
in H?(P,, L(fl?)) determined by ^).(B | ^; then as in (2.5) {^, . . ., w^_^} is a basis.
Let ^ denote the monodromy effected on H^P,, L) by moving o(^.) along a path
close to (B(Ti) disjoint from (B(t) u D, except at its initial point, where D, is a small
disc centered at o(j,), then making one positive turn around 8 D,, and then retracing the
path to o{s.).
Lemma (12.3.2). — Set ^ = yi,2 ^ and w^ == y, 3 ^,^ = i, ..., N - 2.
TA^z
^=^002^,
^ ==^2(1 —ai) Wi + ^2,
^= ^ ^> 2,
^^ Z^l == 003 Wi + 02(03 — i) W^
^2 == a2 03(001 - i) ^ + (003 a^ - 003 + i) w^
^3 = «2 003(1 — aj Wi + 003(1 — a^) ^2+^3, if N — 3 > i,
w^ == w^ k >, 3.
^
MONODROMY OF HYPERGEOMETRIC FUNCTIONS 7i
Proof. — Let c denote the unique element in the Sg. Introduce the local system 'L{c)
of (3.15) on P^). Without loss of generality, we can assume that our base point
o eM(^) i.e. o{c) == oo.
Set d == (3 (A). Without loss of generality we can choose the embedding a of T so
that inf | d — o{s) | > 3 diam o(S^) (here we are identifying P with P via a coordinate z
as in (3.15)).
The effect of horizontal transport of{z</i, •••5^-2} ^md^ variation ofembeddings
ofSinP is given by an isotopy ofP (cf. (3.6)). In particular, Y».j arises from an iso-
topy {"y]^j; o<^^i}ofP which twists o(^) one positive turn around o(s^ along the
path described above; here T)^. === identity and T)^ | o(S) === identity. The isotopy^
can be performed so that the only points which move lie in a disc containing o(Sj) of
diameter less than 2 diam o(Si). Since under the isotopy no point ofo(Si). turns around d,
one sees by inspection of the definition of L(c) that the restriction of the dual local
system lL{c) to the subset {{d X ^j o(S^)); o < ^ <^ 1} ofP^ has a trivializing non-
zero section ?, i <^ i,j' <^_ N — i. Consequently, for each t,j^N — i, e'(d) returns
to its initial value after horizontal transport via T]^-, o <^ ^ i.
Set ^ = ?.(3 | ?^ and ^ == r^^(v^, i <_ z,j, k <^ N — i. In view of (12.3. i),
w^w — ^ + ^+i when the section ? is taken to have the same value on d as the section
denoted / in (12.3.1); we choose ? in this way. The argument above shows that the
initial segment of the L valued singular chain ^ is unchanged by the map T]^.,
i<zJ,A^N-i.
^
0(83) ois^)
b)
72 P, DELIGNE AND G. D. MOSTOW
The effect of the isotopy T) corresponding to y^ 3 is pictured in diagrams a) and ^.
Let " ^ 9' denote (< homotopic in Po". Then
V[ ^ V^ + QL2{1 — ^3) ^2 — ^2 ^ ^3 ^1
cf
^S- ^2
^3 ^ ^3 — a;^ - ^3 — a3 ^2 — a^ 03 w^ + ai a^ 03 w^ + ag a^ 04 03 ^
^ ^ Vjc for A ^ 4.
Consequently
W[^ — V[ + ^ W 03 Wi + 02(03 —- l) W^,
w^ —v^+v^ —v^+v^+^ 003(0^ — i) w^ + (ai 003 — 03) Wg
» 002003(001 — i) ^ + (i — 03 + 0^03) w^,
^3 " — ^3 + ^4 ^ — ^3 + ^4 + ag 003(1 — a^ Wi + (003 — 04 003) M/a
w 003003(1 — ai) w^ + 003(1 — ai) w^ + !X/3.
The second part of (12.3.2) follows at once. The proof for y^ 2 ls similar.
(12.4) For N == 4, calculations as above yield for matrices with respect to the
basis [w^ w^}
/04002 ^(l -00^ )\ /I 0 \
p T2.3= - - - p
/ \i — 03 cog a3/
i o
Yl.2=== I - - - - », Y2.3= I - _ „
\ o I / \i — 03 ag 03
( »3 ^^l^1)}
W^— i) 001003— 003 + I ]
Yl,3===
and we easily verify that
(I2.4.I) Yl,2-T2,3-Tl3= ala2a3•
This shows that our lift 6': ^(M(^), o) -> U(V) of 6 : TCi(%, o) -> PU(V) cannot be
factored through TCi(M, o) -> U(V) if ^4+1/2, since the center of TCi(M) is
^(PGL(2)) == Z,.
^
MONODROMY OF HYPERGEOMETRIG FUNCTIONS 73
Lemma (12.5). — As in (12.1), set F == Q^T) and 1^ = Im 6'. Then
(".5.1) %[Trr,]==F
(12.5.2) QJTr Ad r^] == F n R if card S > 4.
Proof of (13.5.1). — By (12.1.2), %[Tr F,] C F. By (9.2) %[Tr P,] con-
tains a, a,,, for each distinct pair s, s' e S. It follows that %(Tr F^) D Q,(^/T) where n
is the least common denominator of {^ + ^ | j, j' e S, s = s'}. For any 3 distinct
elements ^,^3, ^ of S, we have
^ - ^, = (^ + ^.) - (^. + ^.).
Hence for any distinct j, j' in S, QJTr 1^] contains a,, a^^
We choose a basis {^, ..., w^_^} in H?(P,, L) as in (12.3). Then Yi.3-Ti,2 has
as matrix with respect to this basis the upper 2X2 diagonal of
( 03 ^^(oci — i) ai 003(1 — ai)\ /agOCi a^i — a^) o\
^(^—i) ^ai—003+1 003(1— ai) ) ( 0 i o|.
0 o i / \ o o i/
The diagonal terms of the product are
0030201, . . . — (ai — l)(a3 — i) + 003001 —003+1,1, . . .,
therefore, for any s^yS^.s^eS^ we get
^Yi.sYi^ = ^^2^ + a! + N — 4 == 001(002003 + i) modQ^.
Hence ai e %[Tr ry, provided that 02 03 + — i for some s^,s^eS^— {j,}. This
proviso fails only if ^ == 1/4 for all j in Si; in this case, replace Si by a partition T^
with card TI == card S^ (cf. (6.2.1)), and in the corresponding subgroup of 1^, the
proviso holds. It follows that a, e %[Tr 1^] for all s e S. This proves (12.5.1).
Proof of (12.5.2). —Set E = QJTr Ad r;] and ^ = C[Int r^]: the C-linear
span of the automorphisms Int y : ^ -^ y^T"1 with y e F^, where m eHom^V, V)
and V is as in (12. i). Let GeGal(F/E). Inasmuch as Tr Int^ = i + Tr Adg
for any g e GL(V), it follows by definition of E that for any y e r'a
("s.S-S) Tr(Int°Y) = °Tr(IntY) - Tr(Inty).
It follows from this that
(12.5.4) Inty -^Inty extends to a C-linear map 9 ofj^.
For S^ Y = o with ^ e C, y ^ Int F^ implies that for any {^} with ^ e C,
Tr(2^ °y) (2^ °y) = Tr 2^ ^ ^Yy')
=Tr^^(YY')
-(Tr2^y)(2^Y)=o.
73
10
74 P. DELIGNE AND G. D. MOSTOW
The group Int 1^ is Zariski-dense in Int GL(V). Consequently ^ coincides with
the C-linear span of Int GL(V); thus ^ is an associative algebra acting irreducibly on the
subspace y of trace o elements in Homc(V, V) and stabilizing the line C.I. Since a
field automorphism preserves Zariski-density, the C-linear span of °Int 1^ is also ^.
Therefore
; Tr((S^°y).m) = o for all m e ^.
Since Tr is non-degenerate on ^ it follows that 2^°y = °- This implies (12.5.4).
Clearly 9 preserves products and is an algebra isomorphism. Since
^ w Hornet, y}, ^ is a simple associative algebra. The map 9 is an algebra iso-
morphism and therefore 9 maps IntGL(V) isomorphically onto the Zariski closure
of Int °r^ which is also Int GL(V) That is, 9 stabilizes Int GL(V). Consequently,
there is an S e GL(V) such that for all g e GL(V) either
(i) ^(Intg) =IntS-lgS, or
(ii) 9(Int^) == IntS-1^-^.
For any ^eGL(V), Intgwg®^-1, where w denotes equivalence of repre-
sentations, and for any g e U(V, ^), the unitary group of some hermitian form ^ in V,
^-1^.
Consequently, for any y e ^ ^d a e Gal(F/E),
^®°(Y) = °(Y®T) - y(IntY) » (IntY := T0Y9
[ Int Y = Y ® Y-
It follows at once that
o^^(T)T in Case (i)
[X(Y) Y m Case (ii)
for all Y e fa where X(y) e C. Composing a with complex conjugation, one can
assume that we are in Case (i). Then there is an element S e GL(V) such that for
all yeF,,
^-S-^Y.^S.
From °(Yi ^) = ^1.^2 = S-1 yi Y2 ^(Yi) ^(Y2) S, we infer that X : F^ C is a
multiplicative homomorphism. For any y such that y — ! has rank i, °y has
the same property and therefore X(y) == i if dimV> 2. Since I\ is generated by
pseudo-reflections ((10.19.4), (11.2.1)), X(r^) == i and °Tr y = Tr y for all yel^,
i.e. a == i. This proves (12.5.2).
We close this section with a description of the field E = %[Tr Ad 1^] in the case
N==4, with a satisfying o<^< i for all s e S, S(JL, == 2, and condition (INT).
In this case, set A, = (i — p., — ^.)-1, i <; z'4=J^ 3. Assume k^> o (cf. § 14.3).
74
MONODROMY OF HYPERGEOMETRIC FUNCTIONS 75
Proposition (12.5.5).
T? rfc 2 7r 9 n o n n 7r ^1L == Ql cos2 —, cos2 —, cos2 —, cos — cos .—cos — .
L ^IZ ^23 ^31 ^12 ^23 ^31 J
Proof. — We have r,CPU(i,i). Thas Ad F, = Ad I\C S0(2, i,R). Let
A == A(^ ^23? ^3i) denote the group generated by reflections in the sides of the geodesic
triangle in the real hyperbolic 2-space Rh2 whose vertices are fixed by the monodromy
transformations y^ Y235 Y3i (cf. (12.3) and (12.4. i)), and let \ denote the subgroup of
orientation preserving elements in A. Then Ad I\CAo, card(A/Ao) == 2, and Ad I\
is of finite index in A.
Let <M, y> denote the Killing form on the Lie algebra JSf of PGL^C), and let
e, be an element in ^ with <<?„ <?,> == i such that (in the projective model ofRA2)
e{ contains a side of the above geodesic triangle {i == i, 2, 3), and <^., <?,> == — cos -7T
kij
if f+j. Let ^ denote the element of the dual space of ^ such that e^{v) == <y, ^,>
for all v e £C {i = i, 2, 3). Then the three generating reflections of A have the form
s, == i — 2^ ® ^ (i == z, 2, 3) and
^...^n^-^^)=^(-^ n^ ^,
J1<J'2.--<^
Tr^...^=.^(-2)^n^^ ^.^
where ^= -cos^ ^^^S,
T? ^' ==y.
From this it is clear that %[Tr A] is the field E' on the right side of (12.5.5). Suppose
now (T : E' -> C is a monomorphism fixing each element ofE. By the argument used in
(12.2.1) (ii) for any ye A and A:eAdI\, y-10^ is in the centralizer of S0(2, i, R).
Hence y~1 °y == ± i and °y = ±y. It follows that °detj^ = ± detj^. But y e 0(2, i)
has determinant db i and this value is fixed by CT. Therefore °y -== y and °Try = Try
i.e. or fixes each element of E. Consequently, E == E'.
(12.6) Assume card S > 4. Let {\L,\ s e S} be a family of numbers o < ^ < i
satisfying condition (INT). By Lemma (3.12), ^ is a rational number for each / By
Theorem (11.4)3 the group I\ is a discrete subgroup of finite covolume in PU(V, ipo)
where V == H^P,, L,). Set E=%[TrAdrj, F = Q(^T) as in (12.1).
Proposition (12.6.1). — I\ is arithmetic in PU(V) if and only if for each a e Gal F
whose restriction on E is not the identity, °^ is a definite Hermitian form on °V.
Proof. — Let G == PU(V, ^). Inasmuch as the complexification ofG is the simple
group PGL(V), (12.6. i) is essentially a restatement of the arithmeticity criterion (12.2.3).
75
76 P. DELIGNE AND G. D. MOSTOW
Proposition (12.6.2). — Assume card S > 4. Then I\ is arithmetic in PU(V) if and
only if for each a e Gal F with a =t= identity or complex conjugation, °^o is a definite Hermitian
form on °V.
Proof. — This follows at once from (12.6.1) and (12.5.2).
Proposition (12.6.3). — Assume card S == 4 and ^ satisfies condition (INT). Set
(i ^12 ^i\
8 == det«^, ^.» = det c^ i c^ [
^11 c^ i /^Sl ^S
wA^ c- == —cos-^-, i <^,7<3. 7^ I\ ^ non-arithmetic in PU(V) if and only if
3 k^
°8 < o for some a e Gal E with a 4= i on E.
Proof. — We have 8 == i — ^3 — 4$ ~ ^ji — ^12 ^23 c^ and thus 8 e E.
Moreover, °8> o implies that the matrix °<^, e^ is positive definite since all its prin-
cipal minors are positive. From this (12.6.3) follows.
Criterion (12.6.3) applies to the index 2 orientation preserving subgroup of a
group generated by reflections in the sides of a geodesic triangle in the real hyperbolic
2-space, a so-called cc triangle group ", cf. § 14.3. One can deduce from (12.6.3) that
at most a finite number of triangle groups are arithmetic. A complete list of these
groups was given by K. Takeuchi in [21].
Proposition (12.7). — For any b e Q, let < b > denote the fractional part ofb i.e. o <_ < b > < i
and b — <A > e Z. Let ^ == {(JiJ s e S} satisfy condition (INT) of (3.11) and let d denote
the least common denominator of [L. Then I\ is an arithmetic lattice in PU(V) if and only if
(12.7.1) for each integer A relatively prime to d with i < A < d — i,
S <A^> == i or card S — i.5
proof. — Let A be an integer relatively prime to d and let e be a primitive root
of unity of F = Q^(^T). Then c^ : s -> ^A is an automorphism of F which is non-
trivial on F n R if and only if A =(= ± i (mod rf). The automorphism o^ sends the
local system with monodromy a to the local system {exp 2ni <A^> | s e S}. By
Corollary (2.21), the hermitian form ^o has signature
(S<A^>-i,S(i-<A^»-i).5 8
The proposition now follows from (12.6.2) and (12.5.2).
76
MONODROMY OF HYPERGEOMETRIC FUNCTIONS 77
(12.8) Let r be a subgroup of GL(TZ, Z) and let G denote the Zariski closure
of r in GL(7z). Then G is an algebraic group defined over Q^with the property
(12.8.1) Any (^-character ^ of the connected component G0 of i in G is trivial.
(For ^(F n G°) is Zariski-dense in the connected subgroup ^(G^C) of C*, and it is
finite because it has bounded denominators; hence /(G6) = (i).)
By a well-known theorem of Borel-Harish Chandra, G(R)/G(R) n GL{n, Z) has
finite Haar volume [3]. Consequently F is an arithmetic subgroup in G(R) if and only
if r is commensurable with G(R) n GL(%, Z) or, equivalently, F is of finite covolume
in G(R).
(12.9) We consider now an algebraic family X defined over Q^ of curves of the
type described in (2.23). We describe an example.
Let [s., a, M be as above, let ^ == -J with d the least common denominator ford
{^ | s e S}. Fix a, b, c e S. Then for each m e M, there is a unique isomorphism
P ->P1 mapping m(a), m(b), m{c) respectively to o, i, oo. Let u: P x M x P1 be the
resulting map. Define
(12.9.1) X=={{v,u,m) ePxPxM\v-d= IT {u - m[s))^}. s+ c
Let 7^2, 7^3 denote the projections of X onto the second and third factors respec-
tively. Set X^ = TT^^w) and denote by TT^ the restriction ofn^ to X^ for any m e M.
More generally, let n: X —^ M be a fiber bundle over M (i.e., a topological
product over small open sets of M) satisfying
(12.9.2) For each m e M, Tr"1^) is an irreducible abelian cover of P, with
covering group G, ramified only at m(S) of orders dividing d.
Set X^ = TT'^w) for any m e M. Then {H^X^, Z) | m e M} is a local system on M
corresponding to a homomorphism S '' ^(M, o) -^AutH^Xp, Z).
Set r == ^(^(M, o)); we call F the H^monodromy group of the fibration. Moreover
the Galois group ^ acts fiber by fiber on X and commutes with horizontal transport
ofH^X^.Z). Consequently, ^ commutes elementwise with F. We thus obtain a
direct sum decomposition
(12.9.3) Hi(Xo, C) = © Hi(X,, C),
where ^ ranges over ^, the set of characters of ^. The group ^ is a quotient of
(Z/rf)^/^). In the case of (12.9.1), ^ = Z/rf.
Let gs^^ be the natural generator of the inertia (== decomposition) group
77
78 P.DELIGNEANDG.D.MOSTOW
at s (cf. (2.23)). Then there is a unique ^ e ^ with ^ (^) = o^ for each s eS and
by (2.23.1)
H^X^, C)^ == H^P^, 1^) for each w e M.
The vector space H^P^, L^) is defined over the field Q^y^i) and even over its ring
of integers by (12.1.3).
(ia.9.4) Set F = %(v^ V = HI(P,, L,), W = V ^ F = C °V where ., o G Gal F
is a primitive idempotent in G ®Q F, °V == ^W, and (i 0 r) €y == ^ for all (T, T e Gal F.
The space W is defined over Q^ and we have
w^)w ^p111^' ^^^
(12.9.5) Set W(Z) = © H^Po, L^ (fl?)) where (9 denotes the ring of integersoGGalF x
ofF. The monodromy group F of the fibration stabilizes H^Pp, L^(^)) for each cha-
racter % 6 ^ and in particular stabilizes W(Z).
Lemma (12.10). —Let n: X -> M 6^ an algebraic fiber bundle satisfying (12.9.2)
and with non-trivial ramification for each s e S. Let F denote the ly-monodromy group of the
fibering, let G be the ^ariski-closure of F in Aut H^Xo, C). If F is of finite covolume in G(R),
then in the euclidean topology 1^, the projection ofT on Aut V is dense in U(V, ^^, where ^ and V
are as in (12.9.4), ^ is as in (i 2.1. i), provided there is a a e Gal Q^(^T) w^A °^ indefinite
and CT ={= db i.
Proo/. — Suppose that G(R)/F has finite Haar volume. Then defining the integral
structure on H^X,,, C) as H^X^, Z), we infer that F is commensurable with
G(Z) == G n AutHl(Xo, Z) by (12.8). Inasmuch as W is a F-stable subspace defined
over Q^, it is also G-stable and the restriction of G(Z) to W is an arithmetic subgroup.
Consequently F^, the restriction of F to W, is arithmetic.
By (12. i .3)3 I\ C U(V, ^), and indeed the Zariski-closure of 1^ contains U(V)
and even SL(V)—this last fact can be verified by computing the Lie algebras of the
Zariski-closures of {y^ neZ,} where y ranges over the pseudo-reflections of 1^.
Set F = Q^(^T). We can regard U(V, ^) as the group of R-rational
points of an algebraic group U defined over F n R; namely as the subgroup
{ (x, x) [ x e U(V, ^o)} of Restr^jR GL(V). The subgroup 1^ then becomes a subgroup
of Aut H^Po, L^(fl?)) X Aut H^P^, LCT^)) and is thus commensurable with V{(P n R).
By hypothesis, the group U^V, °^) = °U(R) is not compact because the hermitian
form a^ff is indefinite. It remains to explain why U(^ n R) is topologically dense
in U(R) if i =f= or e Gal(F n R/QJ. This assertion is an immediate consequence of the
weak approximation theorem for algebraic groups over an algebraic number field,
which applies here since °U(R) is not compact (cf. [n], p. 192).
78
MONODROMY OF HYPERGEOMETRIC FUNCTIONS 79
Theorem (12.11). — Let X be the algebraic family (12.9. i) and let T be the H^mono-
dromy group of the fibering. Assume that ^ satisfies condition (INT) of (3.11). If F is of finite
covolume in its ^ariski-closure G(R) in Aut H^XQ , R), then I\ is an arithmetic lattice in U(V, ^).
Proof. — By Theorem (10.9.1), I\ is discrete in U(V, ^)- It follows at once
from the Lemma (12.10) that for all <r e Gal(Q^T)/%) with o+±i, °U(V, ^) is
compact. It follows from (12.2) that I\ is arithmetic in U(V, ^o).
(12.12) The foregoing results show that I\ is arithmetic in U(V, ^) if and only
if I\v is of finite covolume in its Zariski-closure in Aut W(R).
