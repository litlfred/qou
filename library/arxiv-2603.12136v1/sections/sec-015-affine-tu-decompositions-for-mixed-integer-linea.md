---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-015-affine-tu-decompositions-for-mixed-integer-linea
section_title: "Affine TU decompositions for mixed-integer linear programs"
section_number: null
pages: 44-45
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
programs
We consider a mixed-integer linear program with variables(x,y,z,ω)∈ZW 1
×ZW 2
×
RW 3
×MI W 4
I, whereW 4
I ⊆W 4 are the integer variables inW 4. We useW I =
W 1∪W 2∪W 4
I to denote the integer variables andW=W 1∪W 2∪W 3∪W 4 to
denote all variables. The linear relaxation of the integer program is of the form:
P :={Ax+By+Cz=b, Dx+Ey+Fω=g, ℓ≤
x y z ω⊺
≤u},
whereA∈Z m1×W 1
,B∈Z m1×W 2
,C∈Z m1×W 3
,b∈Z m1,D∈Q m2×W 1
,E∈
Qm2×W 2
,F∈Q m2×W 4
andℓ≤uhold, whereℓanduare rational vectors where we
consider infinite entries to be integral. Any MILP can be brought into this form if we
allowm 1 = 0andm 2 = 0to hold.
Theorem 33Suppose that fork≤|W 2|, there exist matricesS∈Z m1×W 2
,U∈Z m1×k,
T∈Z k×W 2
andR∈Q m2×k such thatB=S+UT,E=RTand
S C
TO

is totally
unimodular and thatℓ,u∈MI WI∪W 3
holds. Then, for anyd= (dW 1,dT,dW 4
I
)∈Z W 1
×Zk×
ZW 4
I, the affine fiberHd :={(x,y,z,ω)∈P|x=d W 1, Ty=d T, ωW 4
I
=dW 4
I
}satisfies
Hd = conv(Hd∩MIWI ) = conv(Hd∩MIWI∪W 3
)and
conv(P∩MIWI ) = conv(P∩MIWI∪W 3
) = conv({(x,y,z,ω)∈P|x∈Z W 1
, Ty∈Z k, ω∈MI W 4
I})
holds.
ProofWe consider the affine fiberHd for any fixedd∈Z W 1
×Zk×ZW 4
I and rewrite it by
substitutingB=S+UTandD=RT.
Hd :={(x,y,z,ω)∈R W|Ax+By+Cz=b, Dx+Ey+Fω=g, x=d W 1, Ty=d T,
ωW 4
I
=dW 4
I
, ℓ≤

x y z ω
⊺≤u}
={(x,y,z,ω)∈R W|x=d W 1, Sy+Cz=b−Ad W 1−Ud T, Ty=d T,
Fω=g−Dd W 1−RdT, ωW 4
I
=dW 4
I
, ℓ≤

x y z ω
⊺≤u}
={x∈R W 1
|x=d W 1, ℓW 1≤x≤u W 1}×
{ω∈R W 4
|Fω=g−Dd W 1−RdT, ωW 4
I
=dW 4
I
, ℓW 4≤ω≤u W 4}×
{(y,z)∈R W 2∪W 3
|Sy+Cz=b−Ad W 1−Ud T, Ty=d T,ℓW 2∪W 3≤

y z
⊺≤uW 2∪W 3}
:=Hx
d×H ω
d×H y,z
d
In the third step, we use thatH d can be rewritten as the Cartesian product of the
three polyhedraH x
d ⊆R W 1
,H y,z
d ⊆R W 2∪W 3
andH ω
d ⊆R W 4
. Then since
S C
TO

is
totally unimodular and
b−Ad W 1−Ud T
dT

is integral by integrality ofb,U,Aandd, and
44
ℓW 2∪W 3 anduW 2∪W 3 are integral,Hy,z
d is an integral polyhedron by Hoffman and Kruskal’s
theorem [43]. Thus, we haveHy,z
d = conv(Hy,z
d ∩ZW 2∪W 3
) = conv(Hy,z
d ∩(ZW 2
×RW 3
)),
where the last equality follows sinceHy,z
d ∩ZW 2∪W 3
⊆H y,z
d ∩(ZW 2
×RW 3
)⊆H y,z
d holds.
This implies thatHd = conv(Hd∩MIWI ) = conv(Hd∩MIWI∪W 3
)holds.
Then, note thatCis totally unimodular since it is a submatrix of
S C
TO

. SinceA,Band
bare integral and the variable boundsℓW 3 andu W 3 ofzare integral we have by that the
equationconv(P∩MI WI ) = conv(P∩MI WI∪W 3
)holds by [29, Theorem 3]. Finally, using
bT=


IW 1 O O
OTO
O OI W 3
I

 as the matrix in Lemma 31 and the fact thatHd = conv(Hd∩MIWI )
holds, we derive thatconv(P∩MI WI )) = conv({(x,y,z,ω)∈P|x∈Z W 1
, Ty∈Z k, ω∈
MIW 4
I})holds. □
There are a few key differences between Proposition 30 and Theorem 33 that make
the latter more convenient to use. First of all, we do not require integrality of all of the
right-hand sides, and we only need to construct an affine TU decomposition of a block
in the constraint matrix rather than the complete matrix. Additionally, theE=RT
condition in Theorem 33 is new. This condition broadens the scope of the theorem,
as otherwise,D=Owould have to hold to guarantee implied integrality in the affine
fiberH d in the proof. Furthermore, during the detection we infer implied integrality
for the continuous variables and haveconv(P∩MIWI ) = conv(P∩MI WI∪W 3
).
Theorem 33 can be used directly to show that the condition (13) in Theorem 26
holds. For integer variablesWI ⊆Wand an equitable partition(P,Q)such that
eitherQ∩W I =∅orQ⊆W I holds, letQ 2 ={Q∈Q I||Q|>1}and letW 2 =
WB∪S
Q∈Q2Q. Then, if the conditions of Theorem 33 hold forT= (Π⊺
QΛ)Q′,⋆ for
some subsetQ ′ ⊆ Q2, this directly shows condition (13) in Theorem 26 by using
Theorem 32, and Theorem 32 shows that we can recover integral solutions for the
original model.
