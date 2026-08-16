---
doc_id: s40687-023-00400-3
doc_title: "bonn.mpg.de/stavros 2MaxPlanckInstitutefor Mathematics,Bonn,Germany Fulllistofauthorinformationis availableattheendofthearticle DedicatedtoWalterNeumann andDonZagier,withadmiration"
section_id: sec-005-13-neumannzagier-matrices-and-their-twisted-vers
section_title: "Neumann–Zagier matrices and their twisted version"
section_number: 1.3
pages: 4-7
source_pdf: s40687-023-00400-3.pdf
source_sha256: fd7638a8cf512a99
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
duplicate_of: "arxiv-2109.00379v1"
---
Having already discussed the torsion and twisted torsion, we now recall some basic facts
from ideal triangulations of 3-manifolds and their gluing equations, following [22,26].
Let M be an oriented hyperbolic 3-manifold with a torus boundary component (often
called a one-cusped hyperbolic 3-manifold) equipped with an ideal triangulationT .A n
Eulercharacteristicargumentshowsthatthenumber N oftetrahedrain T isequaltothe
number of edges. We order the edgesei and the tetrahedra/Delta1j of T for 1≤ i, j ≤ N.A
quad type of a tetrahedron is a pair of opposite edges; hence each tetrahedron has three
quad types. We ﬁx an orientation and a quad type of each tetrahedron/Delta1
j so that each
edgeof /Delta1j admitsashapeparameteramong
zj ,z ′
j = 1
1 − zj
, or z′′
j = 1 − 1
zj
∈ C \{0,1}
with opposite edges having same parameters (see Fig.1). We denote by□ the three pairs
ofoppositeedgesofatetrahedron,sothattheedgesof □ areassignedtheedgeparameter
z□ .
A complete hyperbolic structure ofM can be described by a special solution of the
gluing equations. The latter describe the holonomy of the hyperbolic structure around
eachedge e
i of T ,andhavethe(logarithmic)form
N∑
j=1
(
Gij log zj + G′
ij log z′
j + G′′
ij log z′′
j
)
= 2π
√
−1. (5)
Here G, G′and G′′arethegluingequationmatriceswhoserowsandcolumnsareindexed
by the edges and by the tetrahedra ofT , respectively, such that the (i, j)-entry of G□ is
the number of edges of/Delta1j with parameter z□
j is incident to the edgeei in T .I tw i l lb e
convenienttointroduce ζ-variables
ζ = dlog z
dz = 1
z , ζ′= dlog z′
dz = 1
1 − z , ζ′′= dlog z′′
dz = 1
z(z −1) (6)
following[25]. Note thatthe three shape parameters ineach tetrahedronsatisfy the rela-
tion zz′z′′=− 1, and this implies the linear relationζ + ζ′+ ζ′′= 0. Thus one can
eliminate the variableζ′from any expression given in terms ofζ ,ζ′,a n dζ′′, arriving at
the Neumann–Zagier matrices
A := G − G′, B := G′′− G′. (7)
Notethat
Gdiag(ζ) + G′diag(ζ′) + G′′diag(ζ′′) = Adiag(ζ) + Bdiag(ζ′′)( 8 )
S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37 Page 5 of 23 37
wherediag( ζ□ )denotesthediagonalmatrixwithdiagonalentries ζ□
1 ,... ,ζ□
N .
TheNZmatriceshaveremarkablepropertiesdiscoveredin[ 22]whichisastartingpoint
forthequantizationofthegluingequationsandforpassingfromhyperbolicgeometryto
quantumtopology.ThesymplecticpropertyoftheNZmatricesimpliesthat
AB
T = BAT . (9)
Therearetwoenhancementsofthegluingequationsandoftheircorrespondingmatri-
ces.Theﬁrstisobtainedbylookingatthecusp,i.e.,theperipheral(alsocalledboundary)
torusofthe3-manifold.Bya peripheral curve,wemeananoriented,homotopicallynon-
trivial,simpleclosedcurveintheperipheraltorusof M.Aperipheralcurve γ givesatriple
(C
γ , C′
γ , C′′
γ)ofrowvectorsin ZN thatdescribethecompletenessequationas
N∑
j=1
(
Cγ j log zj + C′
γ j log z′
j + C′′
γ j log z′′
j
)
= 0. (10)
Fixingaperipheralcurve γ,let G□
γ denotethematrixobtainedfrom G□ byreplacingthe
lastrowby C□
γ ,andlikewisefor Aγ and Bγ.
The second enhancement is acombinatorial ﬂattening of T ,t h a ti sat r i p l e(f, f ′,f ′′)o f
columnvectorsin ZN suchthat
Gf + G′f ′+ G′′f ′′= (2,... ,2)T , (11)
f + f ′+ f ′′= (1,... ,1)T , (12)
Cγ f + C′
γ f ′+ C′′
γ f ′′= 0 (13)
for any peripheral curveγ. This term was introduced in [6, Sec.4.4] as a necessary ingre-
dient to deﬁne the 1-loop invariant (and there, it was called a combinatorial ﬂattening
compatible with any peripheral curve). Every ideal triangulation has combinatorial ﬂat-
tenings[21,Thm.4.5].
ThisconcludesourdiscussionoftheNZmatrices.Wenowintroduceatwistedversion
oftheNZmatricesofanidealtriangulation
T ofa3-manifold M asabove.Wewillﬁxan
epimorphism α : π1(M) → Zand aperipheral curveμsatisfying α(μ) = 1.For instance,
if M is a knot complement inS3, thenα is the abelianization map andμ is a meridian
of the knot. Let~M and M(n) denote the cyclic covers ofM corresponding toα−1(0) and
α−1(nZ), respectively. The ideal triangulation~T of the inﬁnite cyclic cover~M induced
from T isequippedwithanactionofthedecktransformationgroup Z(generatedbythe
μ-action),andinducesanidealtriangulation T (n) ofthe n-foldcycliccover M(n).
We choose lifts~ei and ~/Delta1j of ei and /Delta1j to ~T , respectively, and fork ∈ Z let G□
k be the
N × N matrix whose (i, j)-entry is the number of edges ofμk · ~/Delta1j with parameter z□
j
is incident to the edge~ei in ~T . Note thatG□
k is a zero matrix for all but ﬁnitely many
k, as there are ﬁnitely many tetrahedra around~ei. We deﬁne thetwisted gluing equation
matrices G□ (t)of T by
G□ (t): =
∑
k∈Z
G□
k tk (14)
andthe twisted Neumann–Zagier matrices by
A(t): = G(t) − G′(t), B(t): = G′′(t) − G′(t). (15)
37 Page 6 of 23 S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37
(Moregenerally,if X(t)isamatrixwithentriesin Z[t±1],wedenoteby Xk thecoeﬃcient
of tk in X(t).)Notethattherowsandcolumnsofthesematricesareindexedbytheedges
and tetrahedra ofT , respectively, and that their entries are in the ringZ[t±1]. Since the
above matrices are well deﬁned after ﬁxing lifts of each edge and tetrahedron ofT ,a
diﬀerent choice of lifts changesG□ (t), A(t)a n dB(t) by multiplication from the left or
right by the same diagonal matrix diag(tc1 ,t c2 ,... ,t cN ) for integersc1,c2,... ,c N. This
ambiguitypropagatestoanyinvariantconstructedusingthesematrices.
AﬁrstpropertyofthetwistedNZmatrices A(t)and B(t)isthattheydeterminetheNZ
matrices A(n) and B(n) of the cyclic coversT (n) of T , and moreover they do so via block
circulant matrices, i.e., square matrices such that each row is obtained by its predecessor
by a cyclic shift. We refer to [4]a n d[24] for details on the properties of block circulant
matrices.
Theorem 1.1 We have
X
(n) =
⎛
⎜⎜⎜
⎜⎝
∑
r≡0 Xr
∑
r≡1 Xr ··· ∑
r≡n−1 Xr∑
r≡n−1 Xr
∑
r≡0 Xr ··· ∑
r≡n−2 Xr
..
.
..
. . . . ..
.∑
r≡1 Xr
∑
r≡2 Xr ··· ∑
r≡0 Xr
⎞
⎟⎟⎟
⎟⎠
(16)
for X = G
□ , A or B.
The twisted NZ matrices satisfy a twisted version of the symplectic property of Equa-
tion(9).
Theorem 1.2 We have
A(t)B(1/t)T = B(t)A(1/t)T . (17)
In other words,A(t)B(1/t)T is symmetric under tranposition followed byt ↦→ 1/t.I n
particular, A(ω)B(ω)∗ is Hermitian forω ∈ Cwith |ω|= 1a n ds oi sB(ω)−1A(ω)i fB(ω)
is non-singular. HereX∗ is the complex conjugate of the transpose of a matrixX.N o t e
that given any ideal triangulation, we can choose quads so thatB (hence alsoB(t), since
B(1) = B)isinvertible;see[ 6,App.A].
Remark 1.3 OnecancheckthatEquation( 17)(orequivalently,itsrestrictionto n-throots
ofunity t)isequivalenttothat A(n)(B(n))T = B(n)(A(n))T forall n ≥ 1.
We now come to a conjectural property of the twisted NZ matrices, which we have
checkedinnumerousexamples.
Conjecture 1.4 The Laurent polynomials det(A(t)) and det(B(t)) are palindromic, i.e.,
satisfy p(t) = εtr p(1/t)forsome ε =± 1andaninteger r.
We next discuss the behavior of the twisted NZ matrices under a 2–3 Pachner move
relatinganidealtriangulation T with N tetrahedratoanotherone T with N+1tetrahedra.
Recallthatsuchamoveisdeterminedbytwotetrahedrawithacommonfacein T ,which
becomethreetetrahedrawithacommonedgein T asshowninFig. 2below.Letuswrite
thetwistedNZmatrices A(t)and B(t)ofthetriangulation T schematicallyincolumnsas
A(t) = (a1,a 2,a i), B(t) = (b1,b 2,b i), (18)
S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37 Page 7 of 23 37
with ai meaning (a3,a4, ..., aN) and similarly forbi.L e tA(t)a n dB(t) denote the corre-
spondingtwistedNZmatricesof T .
Theorem 1.5 With the above notation, there exists a lower triangular matrix P with 1’s
on the diagonal such that
P A(t) =
(
−1 −1 −10
b1 + b2 a1 a2 ai
)
,P B(t) =
(
−1 −1 −10
0 a2 + b1 a1 + b2 bi
)
. (19)
Thiscorrectstheomissionof P in[6,Eqn.(3.27)],whichdoesnotaﬀectthevalidityofthe
proofsin[ 6].
