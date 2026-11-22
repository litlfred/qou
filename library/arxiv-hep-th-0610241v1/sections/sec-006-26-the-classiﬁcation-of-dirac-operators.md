---
doc_id: arxiv-hep-th-0610241v1
doc_title: "Gravity and the standard model with neutrino mixing"
section_id: sec-006-26-the-classiﬁcation-of-dirac-operators
section_title: "The classiﬁcation of Dirac operators"
section_number: 2.6
pages: 12-15
source_pdf: hep-th-0610241.pdf
source_sha256: 6a71ab6f6459c070
toc_source: inferred
doc_brief: "Gravity and the standard model with neutrino mixing — We present an eﬀective uniﬁed theory based on noncommutative geometry for the standard model with neutrino mixing, minimally coupled to gravity."
---
We now characterize all operators DF which qualify as Dirac operators and moreover com-
mute with the subalgebra
CF ⊂AF ,
CF = {(λ, λ, 0) , λ ∈C}
(2.30)
Remark 2.19. The physical meaning of the commutation relation of the Dirac operator
with the subalgebra of (2.30) is to ensure that the photon will remain massless.
We have the following general notion of Dirac operator for the ﬁnite noncommutative geom-
etry with algebra AF and Hilbert space HF.
Deﬁnition 2.20. A Dirac operator is a self-adjoint operator D in HF commuting with JF ,
CF, anticommuting with γF and fulﬁlling the order one condition [[D, a], b0] = 0 for any
a, b ∈AF.
In order to state the classiﬁcation of such Dirac operators we introduce the following notation.
Let Y(↓1), Y(↑1), Y(↓3), Y(↑3) and YR be 3 × 3 matrices. We then let D(Y ) be the operator in
HF given by
D(Y ) =

S
T ∗
T
¯S

(2.31)
where
S = S1 ⊕(S3 ⊗13).
(2.32)
In the decomposition (↑R, ↓R, ↑L, ↓L) we have
S1 =


0
0
Y ∗
(↑1)
0
0
0
0
Y ∗
(↓1)
Y(↑1)
0
0
0
0
Y(↓1)
0
0


S3 =


0
0
Y ∗
(↑3)
0
0
0
0
Y ∗
(↓3)
Y(↑3)
0
0
0
0
Y(↓3)
0
0

.
(2.33)
The operator T maps the subspace ER =↑R ⊗10 ⊂HF to the conjugate JF ER by the matrix
YR, and is zero elsewhere. Namely,
T|ER : ER →JF ER,
T|ERf = YR JF f
T|HF ⊖ER = 0.
(2.34)
We then obtain the classiﬁcation of Dirac operators as follows.
Theorem 2.21.
1. Let D be a Dirac operator. There exist 3 × 3 matrices Y(↓1), Y(↑1),
Y(↓3), Y(↑3) and YR, with YR symmetric, such that D = D(Y ).
2. All operators D(Y ) (with YR symmetric) are Dirac operators.
GRAVITY AND THE STANDARD MODEL WITH NEUTRINO MIXING
13
3. The operators D(Y ) and D(Y ′) are conjugate by a unitary operator commuting with
AF, γF and JF iﬀthere exists unitary matrices Vj and Wj such that
Y ′
(↓1) = V1 Y(↓1)V ∗
3 , Y ′
(↑1) = V2 Y(↑1) V ∗
3 ,
Y ′
(↓3) = W1 Y(↓3) W ∗
3 , Y ′
(↑3) = W2 Y(↑3) W ∗
3 , Y ′
R = V2 YR ¯V ∗
2
Proof. The proof relies on the following lemma, which determines the commutant A′
F of AF
in HF .
Lemma 2.22. Let P =

P11
P12
P21
P22

be an operator in HF = Hf ⊕H ¯f. Then P ∈A′
F iﬀthe
following holds
• P11 is block diagonal with three blocks in M12(C), M12(C), and 12 ⊗M12(C) correspond-
ing to the subspaces where the action of (λ, q, m) is by λ, ¯λ and q.
• P12 has support in 1 ⊗20
L ⊕1 ⊗20
R and range in ↑R ⊗10⊕↑R ⊗30.
• P21 has support in ↑R ⊗10⊕↑R ⊗30 and range in 1 ⊗20
L ⊕1 ⊗20
R.
• P22 is of the form
P22 = T1 ⊕(T2 ⊗13)
(2.35)
Proof. The action of AF on HF = Hf ⊕H ¯f is of the form

π(λ, q, m)
0
0
π′(λ, q, m)

(2.36)
On the subspace Hf and in the decomposition (↑R, ↓R, ↑L, ↓L) one has
π(λ, q, m) =


λ
0
0
0
0
λ
0
0
0
0
α
β
0
0
−β
α

⊗112
(2.37)
where the 12 corresponds to (10 ⊕30) × 3. Since (2.36) is diagonal the condition P ∈A′
F is
expressed independently on the matrix elements Pij.
Let us consider ﬁrst the case of the element P11. This must commute with operators of the
form π(λ, q, m) ⊗112 with π as in (2.37), and 112 the unit matrix in a twelve dimensional
space. This means that the matrix of P11 is block diagonal with three blocks in M12(C),
M12(C), and 12 ⊗M12(C), corresponding to the subspaces where the action of (λ, q, m) is by
λ, ¯λ and q.
We consider next the case of P22. The action of (λ, q, m) ∈AF in the subspace H ¯f is given
by multiplication by λ or by m thus the only condition on P22 is that it is an operator of the
form (2.35).
The oﬀdiagonal terms P12 and P21 must intertwine the actions of (λ, q, m) ∈AF in Hf and
H ¯f. However, the actions of q or m are disjoint in these two spaces, while only the action by
λ occurs in both. The subspace of Hf on which (λ, q, m) acts by λ is ↑R ⊗10⊕↑R ⊗30. The
subspace of H ¯f on which (λ, q, m) acts by λ is 1 ⊗20
L ⊕1 ⊗20
R. Thus the conclusion follows
from the intertwining condition.
Let us now continue with the proof of Theorem 2.21.
1) Let us ﬁrst consider the oﬀdiagonal part of D(Y ) in (2.31), which is of the form

0
Y ∗
R
YR
0

.
Anticommutation with γF holds since the operator γF restricted to ER ⊕JF ER is of the form
14
CHAMSEDDINE, CONNES, AND MARCOLLI

−1
0
0
1

. Moreover the oﬀdiagonal part of D(Y ) commutes with JF iﬀ(YRξ) = Y ∗
R ¯ξ for all
ξ i.e. iﬀYR is a symmetric matrix. The order one condition is automatic since in fact the
commutator with elements of AF vanishes exactly.
We can now consider the diagonal part

S
0
0
¯S

of D(Y ). It commutes with J and anticom-
mutes with γF by construction. It is enough to check the commutation with CF ⊂AF and
the order one condition on the subspace Hf. Since S exactly commutes with the action of A0
F
the order one condition follows. In fact for any b ∈AF, the action of b0 commutes with any
operator of the form (2.35) and this makes it possible to check the order one condition since
P = [S, π(a)] is of this form. The action of AF on the subspace HF is given by (2.37) and
one checks that π(λ, λ, 0) commutes with S since the matrix of S has no non-zero element
between the ↑and ↓subspaces.
2) Let D be a Dirac operator. Since D is self-adjoint and commutes with JF it is of the form
D =

S
T ∗
T
¯S

where T = T t is symmetric.
Let v = (−1, 1, 1) ∈AF. One has
γF ξ = v ξ ,
∀ξ ∈Hf.
(2.38)
Notice that this equality fails on H ¯f.
The anticommutation of D with γF implies that D = −1
2 γF [D, γF ]. Notice that γF is given
by a diagonal matrix of the form
γF =

g
0
0
−¯g

.
Thus, we get
S = −1
2 g [S, g] = −1
2 v [S, v]
using (2.38).
The action of v in HF is given by a diagonal matrix (2.36), hence v [S, v] coincides with the
A11 block of the matrix of A = v[D, v].
Thus, the order one condition implies that S commutes with all operators b0, hence that it
is of the form (2.32).
The anticommutation with γF and the commutation with CF then imply that the self-adjoint
matrix S can be written in the form (2.33).
It remains to determine the form of the matrix T. The conditions on the oﬀdiagonal elements
of a matrix
P =

P11
P12
P21
P22

,
which ensure that P belongs to the commutant of A0
F = JF AF JF , are
• P12 has support in 1 ⊗↑0
R ⊕3 ⊗↑0
R and range in 2L ⊗10 ⊕2R ⊗10.
• P21 has support in 2L ⊗10 ⊕2R ⊗10 and range in 1 ⊗↑0
R ⊕3 ⊗↑0
R.
This follows from Lemma 2.22, using JF .
Let then e = (0, 1, 0). One has π′(e) = 0 and π(e) is the projection on the eigenspace γF = 1
in HF. Thus, since [D, e] belongs to the commutant of A0
F = JF AF JF by the order one
GRAVITY AND THE STANDARD MODEL WITH NEUTRINO MIXING
15
condition, one gets that π′(e)T −Tπ(e) = −Tπ(e) has support in 2L ⊗10 ⊕2R ⊗10 and
range in 1 ⊗↑0
R ⊕3 ⊗↑0
R. In particular γF = 1 on the range.
Thus, the anticommutation with γF shows that the support of Tπ(e) is in the eigenspace
γF = −1, so that Tπ(e) = 0.
Let e3 = (0, 0, 1) ∈AF. Let us show that T e0
3 = 0. By Deﬁnition 2.20, T commutes with
the actions of v(λ) = (λ, λ, 0) ∈AF and of Jv(λ)J−1 = v(λ)0. Thus, it commutes with e0
3.
The action of e0
3 on Hf is the projection on the subspace • ⊗30. The action of e0
3 on H ¯f is
zero. Thus, [T, e0
3] = T e0
3 is the restriction of T to the subspace • ⊗30. Since [T, e0
3] = 0
we get T e0
3 = 0. We have shown that the support of T is contained in 2R ⊗10. Since T is
symmetric i.e. T = ¯T ∗the range of T is contained in 1 ⊗20
R.
The left and right actions of (λ, q, m) on these two subspaces coincide with the left and right
actions of v(λ). Thus, we get that T commutes with AF and A0
F. Thus, by Lemma 2.22, it
has support in ↑R ⊗10 and range in 1⊗↑0
R.
This means that T is given by a symmetric 3 × 3 matrix YR and the operator D is of the
form D = D(Y ).
3) By Lemma 2.22, the commutant of the algebra generated by AF and A0
F is the algebra of
matrices
P =

P11
P12
P21
P22

such that
• P12 has support in 1⊗↑0
R and range in ↑R ⊗10.
• P21 has support in ↑R ⊗10 and range in 1⊗↑0
R.
• Pjj is of the form
Pjj = P 1
jj ⊕(P 3
jj ⊗13)
where
P a
jj =


P a
j (1)
0
0
0
P a
j (2)
0
0
0
12 ⊗P a
j (3)


a = 1, 3 ,
j = 1, 2.
A unitary operator U acting in HF commuting with AF and J is in the commutant of the
algebra generated by AF and A0
F. If it commutes with γF, then the oﬀdiagonal elements
Uij vanish, since γF = −1 on ↑R ⊗10 and γF = 1 on 1⊗↑0
R. Thus U is determined by the
six 3 × 3 matrices Ua
1 (k) since it commutes with J so that Ua
2 (k) = ¯Ua
1 (k) . One checks that
conjugating by U gives the relation 3) of Theorem 2.21.
Remark 2.23. It is a consequence of the classiﬁcation of Dirac operators obtained in this
section that color is unbroken in our model, as is physically expected. In fact, this follows
from the fact that Dirac operators are of the form (2.31), with the S term of the form (2.32).
