---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action"
section_id: sec-036-3-aiajak
section_title: "AiAjAk"
section_number: 3
pages: 39-41
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
doc_brief: "Non-Abelian Stokes theorem in action — In this short review main issues related to the non-Abelian S tokes theorem have been addressed."
---
)
, (44)
where k ∈ Z±. The use of Eq.44 is not obligatory. One could as well choose the
action of the so-called BF -theory
SBF = k
4π
∫
S3
d3x εijkTr(BiFjk), (45)
where Bi = Ba
i (x)T a is an auxiliary gauge ﬁeld, and now k ∈ R±.
To encode the topology of a link L = {Ci} into a path integral we introduce
an auxiliary one-dimensional topological ﬁeld theory (topological qu antum me-
chanics) in an external gauge ﬁeld A, living on the corresponding loop Ci. The
39
classical action of this theory is chosen in the form (see, Eq.25)
SCi(A) = i
∮
Ci
dt ¯ziDtzi, (46)
where the multiplet of scalar ﬁelds ¯zi, zi transforms in a irreducible representa-
tion Ri. The partition function corresponding to 46 has the following stand ard
form
Zi(A) =
∫
D2zi exp [iSCi(A)] .
It is obvious that the observables SCi(A) are akin to the Wilson loops.
We deﬁne the topological invariant of the link L as the (normalized) expec-
tation value
⟨∏
i
Zi(A)
⟩
≡
[ ∫
dµ exp(iS)
] −1∫
dµ exp(iS)
∏
i
Zi(A), (47)
where S consists of SCS plus quantum terms, and the measure should also con-
tain the auxiliary ﬁelds. We can calculate 47 recursively, using the so- called
skein relations . Thus, our present task reduces to the derivation of the corre-
sponding skein relation. To this end, we consider a pair of loops, say C1 and
C2, where a part of C1, forming a small loop ℓ (ℓ = ∂N ), is wrapped round
C2. In other words, C2 pierces N at a point P . Such an arrangement can be
interpreted as a preliminary step towards ﬁnding the corresponding monodromy
matrix M. Having given the loop ℓ we can utilize the non-Abelian Stokes the-
orem (actually the Abelian Stokes theorem for 46) in its holomorphic v ersion,
obtaining Eq.32. In general position, N and C2 can intersect in a ﬁnite number
of points, and the contribution to the path-integral coming from t hese points
can be explicitly calculated. We replace the curvature in 32 by the fun ctional
derivative operator
F a
ij(x) − →4π
ik εijk
δ
δAa
k(x) .
This substitution yields an equivalent expression provided the order of terms in
47 is such that the functional derivative can act on SCS producing F . Using
formal translational invariance of the product measure DA, and functionally
integrating by parts in 47 with respect to A, we obtain, for each intersection
40
✻ ✻
C1 C2
N
Figure 10: C1 and C2, where a part of C1, forming a small loop ℓ (ℓ = ∂N ), is
wrapped round C2.
point P , the monodromy operator
M = exp
[ 4π
ik (¯z1T a
1 z1)(¯z2T a
2 z2)(P )
]
. (48)
To calculate the matrix elements of 48 one utilizes the following scalar product
(f, g) = 1
2πi
∫
f gexp(¯zz)d¯zdz.
This kind of the scalar product is implicit in our derivations of the path integral.
Expanding 48 in a power series, multiplying with respect to this scalar p roduct,
and re-summing, we get the monodromy matrix
M = (¯z1¯z2, M z2z1) = exp
(4π
ik T a
1 ⊗ T a
2
)
.
The square root of the monodromy matrix gives rise to the, so-calle d, braiding
matrix B resposible for a proper form of skein relations, yielding knot/link
invariants.
