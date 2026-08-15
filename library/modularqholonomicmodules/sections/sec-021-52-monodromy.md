---
doc_id: modularqholonomicmodules
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-021-52-monodromy
section_title: "Monodromy"
section_number: 5.2
pages: 40-43
source_pdf: modular.qholonomic.modules.pdf
source_sha256: 640303a68dd75453
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
---
and the associated monodromy. Using the modular transformation properties of the Jacobi
θ-function Equation (49) and the Dedekind η-function, it is easy to see that Equation (31)
implies (32).
Note that each of the functions
−→
M2,1,
−→
M2,1|−1T,
−→
M2,1|−1S has SL2(Z )-stabiliser⟨T 2,TST⟩,
⟨T 2,S⟩ and⟨ST 2S,T⟩, respectively, and that the second group is the θ-subgroup and the
last group is Γ0(2). The appearance of Γ 0(2) is a consequence of the (1/2)-q-Borel transform
below.
The rest of this section is devoted to the proof that the monodromy is given by Equa-
tion (31). To achieve this, we need to write f (−1) and f (1) as linear combinations of g(0,0)
and g(0,1), the coeﬃcients in these expressions give the entries of the monodromy matrix.
Firstly we determine the second column of the monodromy, using an adaption of an argu-
ment in [54]. Using the (−1)-q-Laplace transform or the Meinardus trick (see for example [51]
MODULAR q-HOLONOMIC MODULES 41
and [71, p.54]) and shifting the contour of
∮
:=
∫
|t|=ε we obtain that
ˆf (−1)(t,q ) = (q;q)2
∞
∮
0
θ(t/ξ;q)
(ξ;q)2∞
dξ
2πiξ =−(q;q)2
∞
∞∑
k=0
(
Resξ=q−k
)θ(t/ξ;q)
(ξ;q)2∞
dξ
2πiξ
=−(q;q)2
∞
∞∑
k=0
(Resε=0) θ(tqkeε;q)
(q−1e−ε;q−1)2
k(e−ε;q)2∞
−dε
2πi
=−(q;q)4
∞∑
k=0
(Resε=0) (−1)kq−k(k+1)/2t−ke−kεθ(teε;q)
θ(eε;q)2
(qeε;q)2
∞
q−k(k+1)e−2kε(qeε;q)2
k
−dε
2πi
= (q;q)6
∞Resε=0
θ(teε;q)
θ(eε;q)2
(qeε;q)2
∞
(q;q)2∞
∞∑
k=0
(−1)kqk(k+1)/2t−kekε
(qeε;q)2
k
dε
2πi
=−θ(t−1;q)
∞∑
k=0

 1
2E1(q)− 1
2 +
k∑
j=1
1 +qj
1−qj

 (−1)kqk(k+1)/2t−k−1
(q;q)2
k
+θ′(t−1;q)
∞∑
k=0
(−1)kqk(k+1)/2t−k−1
(q;q)2
k
.
(210)
Therefore, we see that
f (−1)(t,q ) =g(0,1)(t,q ), (211)
which implies that
−→
M1,2 = 0 and
−→
M2,2 = 1. Lemma 5.4 below implies that det( M) =−1,
therefore
−→
M(t,λ,q ) =
(
−1 0
∗ 1
)
. (212)
To ﬁnish the proof we will show that the function
E2 :=f (1) +g(0,0)−m2,1g(0,1) (213)
vanishes identically, where m2,1 denotes the function given in Equation (31). The function
E2 is meromorphic of t∈ C × and has potential simple poles located at t∈± q−1/4− 1
2 Z λ−1
(coming fromf (1) and
−→
M2,1) and potential simple poles atqZ (coming fromg(0,1)). Lemma 5.3
below gives
Rest=±q−1/4−nλ−1f (1)(t,λ,q ) dt
2πit
= θ(±q3/4λ−1;q)θ(±q−1/4;q)θ(±q−3/4;q)θ(±q−3/4λ;q)
2(q;q)6
∞θ(q−1λ;q)θ(q−3/2λ;q) f (−1)(±q−1/4−nλ−1,q ).
(214)
On the other hand,
Rest=±q−1/4−nλ−1m2,1(t,λ,q ) dt
2πit
= Rest=±q−1/4−nλ−1θ(qt;q)θ(tλ;q)θ(tλq−1/2;q)θ(tλ2q−1/2;q)
θ(tλq1/4;q)θ(−tλq1/4;q)θ(tλq−1/4;q)θ(−tλq−1/4;q)θ(q−1λ;q)θ(q−3/2λ;q)
dt
2πit
= (−1)nqn(n−1)/2
(q;q)3
∞
θ(±q3/4−nλ−1;q)θ(±q−1/4−n;q)θ(±q−3/4−n;q)θ(±q−3/4−nλ;q)
θ(−q−n;q)θ(q−1/2−n;q)θ(−q−1/2−n;q)θ(q−1λ;q)θ(q−3/2λ;q)
= θ(±q3/4λ−1;q)θ(±q−1/4;q)θ(±q−3/4;q)θ(±q−3/4λ;q)
(q;q)3
∞θ(−1;q)θ(q−1/2;q)θ(−q−1/2;q)θ(q−1λ;q)θ(q−3/2λ;q)
= θ(±q3/4λ−1;q)θ(±q−1/4;q)θ(±q−3/4;q)θ(±q−3/4λ;q)
2(q;q)6
∞θ(q−1λ;q)θ(q−3/2λ;q) .
(215)
42 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
Therefore,
Rest=±q−1/4−nλ−1E2(t,λ,q ) dt
2πit = 0. (216)
A similar computation or the fact everything is elliptic in λ↦→q1/2λ also shows that
Rest=±q−3/4−nλ−1E2(t,λ,q ) dt
2πit = 0. (217)
Now notice that m2,1(qZ ,λ,q ) = 0 which implies m2,1g(0,1) is holomorphic at t∈ qZ . We
then see that E2(t,λ,q ) extends to a holomorphic function of t ∈ C ×. Therefore, from
Corollary 5.5 we see that E2(t,λ,q ) =C(q)g(0,0)(t,q ). Finally, we note that
−C(q)
(q;q)2
∞
= lim
r→∞
E2(qrt,λ,q )
θ(qrt;q) = 0 (218)
which follows from Lemma 5.1. Thus, Equation (31) follows from the residue equation (214)
and from a computation of the determinants of U and V . We discuss these in the next
sections.
Lemma 5.1. Fort in some compact set where the functions are holomorphic, we have
lim
r→∞
g(0,0)(qrt,q )
θ(qrt;q) = −1
(q;q)2
∞
lim
r→∞
f (−1)(qrt,q )
θ(qrt;q) = 0
lim
r→∞
g(0,1)(qrt,q )
θ(qrt;q) = 0 lim
r→∞
f (1)(qrt,q )
θ(qrt;q) = 1
(q;q)2
∞
.
(219)
Proof. We have
g(0,0)(qrt,q ) =
∞∑
k=0
(−1)kqk(k+1)/2−rk−r
(q;q)2
k
t−k−1
=q−r(r+1)/2
∞∑
k=0
(−1)kq(k−r)(k−r+1)/2
(q;q)2
k
t−k−1
= (−1)rq−r(r+1)/2t−r−1
∞∑
k=−r
(−1)kqk(k+1)/2
(q;q)2
k+r
t−k.
(220)
The ﬁrst equality then follows from
lim
r→∞
g(0,0)(qrt,q )
θ(qrt;q) = lim
r→∞
−1
θ(t−1;q)
∞∑
k=−r
(−1)kqk(k+1)/2
(q;q)2
k+r
t−k
= −1
θ(t−1;q)
∑
k∈Z
(−1)kqk(k+1)/2
(q;q)2
∞
t−k = −1
(q;q)2
∞
.
We can show similarly that
g(0,1)(qrt,q ) = (−1)rq−r(r+1)/2t−r−1
∞∑
k=−r

 1
2E1(q)−r− 1
2− θ′(t−1;q)
θ(t−1;q) +
k+r∑
j=1
1 +qj
1−qj

 (−1)kqk(k+1)/2
(q;q)2
k+r
t−k. (221)
MODULAR q-HOLONOMIC MODULES 43
Noting that E1(q)/2− 1/2 +∑k
j=1
1+qj
1−qj = k +O(qk) completes the proof of the limits of
g(0,0),g (0,1). The limits of f (±1) follow from Watson’s lemma for q-Borel resummation and
keeping track of the θ prefactors. □
