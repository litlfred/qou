---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-018-311-reﬁned-braid-operators-and-gamma-factors
section_title: "Reﬁned braid operators and gamma factors"
section_number: 3.1.1
pages: 15-21
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
A physical framework for knot homologies was ﬁrst proposed i n [28] and later studied from
various viewpoints and in a number of closely related system s in [32, 33, 34, 26]. Regardless
– 14 –
of the details and duality frames used, the basic idea is that a graded vector space HR(K)
associated to a knot K colored by a representation R is identiﬁed with the space of reﬁned
BPS invariants that carry information not only about the cha rge of the BPS state but also
about the spin content:
HR(K) = Href
BPS. (3.28)
This interpretation can be used for performing concrete com putations [35, 26, 36] (see also
[37, 38, 39] and [40, 41, 42]) as well as for studying the struc ture of Hg,R
i,j (K) for various g
and R [43, 44]. In this section, we will use both methods – based on c oncrete formulas for
torus knots and on structural properties for arbitrary knot s – to compute colored HOMFLY
homology and colored superpolynomials of (2, 2p + 1) torus knots. Furthermore, the physical
interpretation of the homological knot invariants in terms of the reﬁned (a.k.a. motivic) BPS
invariants is what will ultimately allow us to treat the latt er in more general systems on the
same footing, cf. section 4.
First, let us recall the ﬁve-brane conﬁguration relevant to the physical description of the
sl(N) knot homologies [28, 32, 33]:
space-time : R ×T ∗S3 ×M4
N M5-branes : R × S3 × D (3.29)
|R| M5-branes : R × LK × D
whereLK is the total space of the conormal bundle to K ⊂ S3 in the Calabi-Yau spaceT ∗S3,
and in most of applications one usually takes D ∼
= R2 and M4 ∼
= R4. See e.g. [44] for further
details, references, and the outline of the relation betwee n diﬀerent ways of looking at this
physical system.
The precise form of the 4-manifold M4 and the surface D ⊂ M4 is not important, as
long as they enjoy U(1)F ×U(1)P symmetry action, where the ﬁrst (resp. second) factor is
a rotation symmetry of the normal (resp. tangent) bundle of D ⊂ M4. Following [33], let
us denote the corresponding quantum numbers by F and P . These quantum numbers were
denoted, respectively, by 2S1 and 2(S1 −S2) in [26] and by 2j3 and n in [44].
Something special happens when K =T m,n is a torus knot. Then, as pointed out in [26],
the ﬁve-brane theory in (3.29) has an extra R-symmetry U(1)R that acts on S3 leaving the
knot K = T p,q and, hence, the Lagrangian LK ⊂T ∗S3 invariant. Following [26], we denote
the quantum number corresponding to this symmetry bySR, and also introduce the partition
function
Z ref
SU (N )(S3,T m,n
R ;q,t ) := Tr Href
BPS
(−1)SRqPtF −SR (3.30)
that “counts” reﬁned BPS states in the setup (3.29). A priori , this partition function is
diﬀerent from the Poincar´ e polynomial of thesl(N) knot homology, which in these notations
reads
P sl(N ),R(K;q,t ) = Tr Href
BPS
qPtF. (3.31)
– 15 –
However, it was argued in [26] that for some torus knots all re ﬁned BPS states (3.28) have
SR = 0 and the two expressions actually agree.
Similarly, in a dual description after the geometric transi tion the setup (3.29) turns into
a system
space-time : R ×X ×M4 (3.32)
M5-branes : R ×LK ×D
where X is the total space of the O(−1) ⊕ O(−1) bundle over CP1, and BPS states carry a
new quantum number which becomes the a-grading of Href
BPS = HR
i,j,k(K). One of the main
results in [26] is that this space has four gradings: in addition to the a-,q- andt-grading that
in the physics setup correspond to the “winding number” β ∈ H2(X,L K) ∼
= Z, and to the
quantum numbersP andF, the space HBP S = HR
i,j,k(K) has the fourth grading, by SR ∈ Z.
Therefore, one of the interesting features of the reﬁned Chern-Simons theory is that it pre-
dicts a new grading on the homology of torus knots and links, thereby upgrading Hsl(N ),R
i,j (K)
to a triply-graded theory (labeled by g andR) and similarly upgrading HR
i,j,k(K) to a homol-
ogy theory with as much as four gradings! It would be very interesting to study these new
extra gradings in other formulations of knot homologies. So me hints for the extra gradings
of torus knot homologies seem to appear in [45].
After the geometric transition, the partition function analogous to (3.30) “counts” reﬁned
BPS states in the setup (3.32):
Z ref(S3,T m,n
R ;a,q,t ) = Tr Href
BPS
(−1)SRaβqPtF −SR. (3.33)
When all reﬁned BPS states have SR = 0 – which, following [26], will be our working as-
sumption here – this expression coincides with the colored s uperpolynomial (3.7), which in
these notations reads P R(K;a,q,t ) = Tr Href
BPS
aβqPtF . This will be our strategy for obtain-
ing the colored superpolynomials of (2 , 2p + 1) torus knots. In fact, via the relation with
reﬁned BPS invariants, we will essentially do the computati on twice: ﬁrst, via direct calcu-
lation of the reﬁned Chern-Simons partition function (3.30 ) and its large N version (3.33),
and then, in section 3.1.3, by using the structural properties of (3.28) that follow from physics.
Although reﬁned Chern-Simons theory is not a gauge theory,2 its partition function can
be evaluated by mimicking the steps in the ordinary Chern-Si mons theory. In particular, one
can deﬁne “reﬁned analogs” of the S and T modular matrices and the braid operator BR1R2
used in (3.26). In addition to these ingredients, we will als o need a modiﬁcation of the reﬁned
braid operator by the so-called gamma factor proposed in [46, 47, 48, 49, 50]). Modulo this
modiﬁcation, the physical meaning of which is still unclear at present, we need the reﬁned
variants of
1. the partition function of the unknot Z CS
SU (N )(S3,
R;q) in order to determine the coef-
ﬁcientµQ, and
2At least, such formulation is not known at present.
– 16 –
2. the quadratic Casimir factor qCR in the monodromy by the action of the braid operator.
The former, viz. the reﬁned partition function of the unknot, is given by the partition function
of the reﬁned BPS invariants of the conifold with a D-brane in serted at the appropriate leg
of the toric diagram [36]. The resulting partition function is the reﬁned analogue of (3.18)
and is given simply by the Macdonald polynomial MR(x;q1,q 2):
Z ref
SU (N )(S3, R;q1,q 2)
Z ref
SU (N )(S3;q1,q 2) = MR(q̺
2;q1,q 2), (3.34)
see also appendix (A1). The combinatorial expression for th e Macdonald polynomial is
MR(q̺
2;q1,q 2) =
∏
(i,j)∈R
q
N−i+1
2
2 q
j−1
2
1 −q
− N−i+1
2
2 q
− j−1
2
1
q
Rt
j −i+1
2
2 q
Ri−j
2
1 −q
−
Rt
j −i+1
2
2 q
− Ri−j
2
1
, (3.35)
where Rt denotes the transposition of the Young diagram R. Furthermore, the Macdonald
polynomial satisﬁes the analogue of (3.20):
MR1(x;q1,q 2)MR2(x;q1,q 2) =
∑
Q∈R1⊗R2
N Q
R1R2MQ(x;q1,q 2), (3.36)
where N Q
R1R2 is a certain rational function of q1 and q2, namely the Littlewood-Richardson
coeﬃcient [51]. Therefore, as in (3.21), we can use these rel ations to determine the reﬁned
analogue of the coeﬃcient µQ
R1R2 that enters the expression (3.15) for the 3-ball partition
function: (
µQ
R1R2
) 2
= N Q
R1R2 ·MQ(q̺
2;q1,q 2) ·Z ref
SU (N )(S3;q1,q 2). (3.37)
Here, following [26], we tacitly assumed that generating fu nctions of the reﬁned BPS invari-
ants, such as (3.30) and (3.33), can be expressed in the form ( 3.12), as in a local quantum
ﬁeld theory, with a Hilbert space whose states are labeled by conformal blocks. It would
be interesting to understand better the physical basis for t his assumption and to study the
unitary structure on the “Hilbert space” of the reﬁned Chern -Simons theory. In particular,
in the case of Σ ≃ T2, one would hope to understand better the identiﬁcation of th e basis of
orthonormal states with integrable representations.
As for the second ingredient, the quadratic Casimir factorqC2(R) =e2πihR, it is related to
the modular transformation T =
(
1 1
0 1
)
which acts in the standard way on the homology cy-
cles of Σ = T2 in the WZW model. The modular matrix for the action of theT -transformation
on the characters of ˆsu(N)k is
TRQ = T∅∅ ·qC2(R) ·δRQ. (3.38)
– 17 –
In [26] the T -matrix for the reﬁned Chern-Simons theory is proposed:
T ref
RQ = T∅∅ · q
1
2 ||R||2
1
q
1
2 ||Rt||2
2
q
N
2 |R|
2
q
1
2N |R|2
1
·δRQ, (3.39)
where ||R||2 :=∑
iR2
i . Hence, we adopt a reﬁnement (3.27) and the eigenvalue λ(+)
Q (R,R ) of
the braid operator BRR for the reﬁned theory:
λ(+)
Q (R,R ) = ǫQ
RR
q||R||2
1
q||Rt||2
2
qN |R|
2
q
1
N |R|2
1
q
− 1
4 ||Q||2
1
q
− 1
4 ||Q2||2
2
q
− N
4 |Q|
2
q
− 1
4N |Q|2
1
. (3.40)
Similar framing factors were considered in [46] and also ded uced from the physics of reﬁned
BPS invariants in [36]. Here we use slightly modiﬁed express ions to match (3.25) in the
unreﬁned limit q1 =q2.
Using these ingredients, we ﬁnd the partition function Z ref
SU (N )(S3,T 2,2p+1
R ;q1,q 2) for the
T 2,2p+1 torus knot:
Z ref
SU (N )(S3,T 2,2p+1
R ;q1,q 2)
= Z ref
SU (N )(S3;q1,q 2)
∑
Q∈R⊗R
γQ
RR ·λ(+)
Q (R,R )2p+1 ·N Q
RR ·MQ(q̺
2;q1,q 2), (3.41)
where, following [46], we introduced a gamma factor γQ
RR. This factor is needed to make the
partition function for the torus knot invariant under the ob vious symmetry T n,m ↔T m,n:
Z ref
SU (N )(S3,T n,m
R ;q1,q 2) = Z ref
SU (N )(S3,T m,n
R ;q1,q 2). (3.42)
While the proper physical understanding of the gamma factor s is lacking, it does not prevent
one from doing calculations. Indeed, the gamma factors can b e determined by recursively
solving the consistency conditions (3.42) for m = 1, · · ·,n − 1 (m < n). In particular, for
torus knots T 2,2p+1, the gamma factors can be found from a single consistency con dition for
p = 0, i.e. for T 2,1 ≃
:
Z ref
SU (N )(S3,T 2,1
R ;q1,q 2)
Z ref
SU (N )(S3;q1,q 2) =
Z ref
SU (N )(S3, R;q1,q 2)
Z ref
SU (N )(S3;q1,q 2) (3.43)
=
∑
Q∈R⊗R
γQ
RR ·λ(+)
Q (R,R ) ·N Q
RR ·MQ(q̺
2;q1,q 2) =MR(q̺
2;q1,q 2).
The gamma factors for symmetric and anti-symmetric representations
In order to determine the gamma factors from the consistency condition (3.43), one needs the
explicit form of the Littlewood-Richardson coeﬃcients N Q
RR. For the symmetric representa-
tion R = Sr and the anti-symmetric representation R = Λ r, the explicit expression for the
– 18 –
Littlewood-Richardson coeﬃcients can be obtained from the Pieri formula:
N Sr+ℓ,r−ℓ
SrSr =
r−ℓ∏
j=1
1 −qj−1
1 q2
1 −qj
1
·
r+ℓ∏
j=2ℓ+1
1 −qj−1
1 q2
2
1 −qj
1q2
·
r∏
j=ℓ+1
(
1 −qj
1
1 −qj−1
1 q2
) 2
, (3.44)
N Λ r+ℓ,r−ℓ
Λ rΛ r =
ℓ∏
i=1
1 −q1qi−1
2
1 −qi
2
·
2ℓ∏
i=ℓ+1
1 −qi
2
1 −q1qi−1
2
. (3.45)
⊗ =
Sr Sr Sr+ℓ,r−ℓ
⊗ =
Λr Λr Λn+ℓ,r−ℓ
r
ℓ = 0
⊕
⊕
r
ℓ = 0
r +ℓ
r −ℓ
r +ℓ
r −ℓ
r
r
Figure 6: Young diagrams for tensor products of symmetric and anti-symme tric representations.
For the symmetric and anti-symmetric representations, the sign factorsǫQ
RR inλ(+)
Q (R,R )
look like [30, 52]:
ǫSr+ℓ,r−ℓ
SrSr = (−1)r−ℓ, ǫ Λ r+ℓ,r−ℓ
Λ rΛ r = (−1)ℓ. (3.46)
With the explicit expression for the Macdonald polynomials MR(q̺
2;q1,q 2) given in (3.35),
we can solve the constraint (3.43) and ﬁnd the following gamm a factors (see Appendix B for
details):
γSr+ℓ,r−ℓ
SrSr =
r−ℓ∏
i=1
q
r−i
2
1 q
1
2
2 −q
− r−i
2
1 q
− 1
2
2
q
r−i+1
2
1 −q
− r−i+1
2
1
, (3.47)
γΛ r+ℓ,r−ℓ
Λ rΛ r =
ℓ∏
i=1
q
i
2
2 −q
− i
2
2
q
i−1
2
2 q
1
2
1 −q
− i−1
2
2 q
− 1
2
1
. (3.48)
It would be very interesting to understand the physical meaning / origin of the gamma factors.
Collecting all the ingredients, (3.35), (3.40), and (3.44) –(3.48), we obtain a ﬁnal expres-
– 19 –
sion for the partition function (3.41) with R =Sr and R = Λr:
R =Sr : Z ref
SU (N )(S3,T 2,2p+1
Sr ;q1,q 2)/Zref
SU (N )(S3;q1,q 2)
=
r∑
ℓ=0
(q2;q1)ℓ(q1;q1)r(A;q1)r+ℓ(q−1
