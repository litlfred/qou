---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-169-61-privileged-cocycles-101
section_title: "PRIVILEGED COCYCLES 101"
section_number: 6.1
pages: 107-108
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
where we have introduced the Laurent series expansions g = ∑
n∈Z
gnzn and
uθq,c = ∑
n∈Z
[uθq,c]nzn. If c⁄∈qZ, we get the solution:
fc := 1
θq,c
∑
n∈Z
[uθq,c]n
cqn− 1zn.
This is clearly the unique solution of zσqf−f = u with only simple poles
on [−c;q], a condition that depends on c only and justiﬁes the notation fc.
We consider it as the summation of the formal solution ˆf in the “authorized
direction of summation ”c∈ Eq. Accordingly, we write it Sc ˆf. The sum Sc ˆf
is asymptotic to ˆf (see further below). Note that the “directions of summa-
tion” are elements of Eq = C∗/qZ which plays here the role of the circle of
directions S1 := C∗/R∗
+ of the classical theory. Also note that all “directions
of summations”
c∈ Eq are authorized, except for one.
Returning to the general equationF[A0] =A⇔σqF =AFA −1
0 , we want to
look for solutions F that are meromorphic on some punctured neighborhood
of 0 in C∗, and we want to have unicity by imposing conditions on the hal f
q-spirals of poles: position and multiplicity. Thus, for f∈M (C∗, 0), and for
a ﬁnite family (ai) of points of C∗ and (ni) of integers, we shall translate the
condition: “The germ f at 0 has all its poles on ⋃ [ai;q], the poles on [ ai;q]
having at most multiplicity ni” by an inequality of divisors on Eq:
divEq(f)≥−
∑
ni[ai].
We introduce a ﬁnite subset of Eq deﬁned by resonancy conditions:
ΣA0 :=
⋃
1≤i<j≤k
Si,j, where Si,j :={p(−a)∈ Eq|qZaµiSp(Ai)∩qZaµjSp(Aj)⁄=∅}.
Here, Sp denotes the spectrum of a matrix.
Theorem 6.1.2 (“Algebraic summation”) . — For any matrix A in form
(3.2), and for any “authorized direction of summation ”
c∈ Eq\ ΣA0, there
exists a unique meromorphic gauge transform F∈ GA0
(
M(C∗, 0)
)
satisfying:
F[A0] =A and div Eq(Fi,j)≥− (µj−µi)[−c] for 1≤i<j ≤k.
Proof. — See [ 50, theorem 3.7].
Of course, div Eq(Fi,j)≥− (µj−µi)[−c] means that all coeﬃcients f of the
rectangular block Fi,j are such that div Eq(f)≥− (µj−µi)[−c]. The matrix
F of the theorem is considered as the summation of ˆFA in the authorized
102 CHAPTER 6. GEOMETRY OF THE SPACE OF CLASSES
direction of summation c∈ Eq and we write it Sc ˆFA.
It is actually the very same sum as that obtained in theorem 5. 5.3. Indeed,
using notations from subsection 5.5.1, if one requires the d ivisors Λ i to be
supported by a single point c∈ Eq, the genericity condition of deﬁnition 5.5.1
translates here to: c∈ Eq\ΣA0, as one sees by using the dictionary provided in
remark 5.5.2. Then, from the same dictionary, one draws that the conditions
on the sum guaranteed by the conclusion of theorem 5.5.3 imme diately imply
the conditions on Sc ˆFA guaranteed by the above theorem, and the unicity in
the above theorem allows one to conclude. As a consequence of subsection
5.5.1, the sum Sc ˆFA is asymptotic to ˆFA.
The algorithm to compute F := Sc ˆFA is the following. We introduce the
gauge transform:
TA0,c :=







θq,c−µ1Ir1 ... ... ... ...
... ... ... 0 ...
0 ... ... ... ...
... 0 ... ... ...
0 ... 0 ... θ q,c−µkIrk







. (Recall that θq,c(z) =θq(z/c).)
Then F[A0] = A , is equivalent to G[B0] = B, where B = TA0,c[A], B0 =
TA0,c[A0], andG =TA0,cFT −1
A0,c. Now, B0 is block-diagonal with blockscµiAi∈
GLri(C), and we can solve for G[B0] = B with G∈ GA0
(
O(C∗, 0)
)
, because
this boils down to a system of matricial equations:
(σqX)cµjAj−cµiAiX = some r.h.s. Y.
Expanding in Laurent series X =∑ Xpzp, Y =∑ Ypzp, we are led to:
qpXpcµjAj−cµiAiXp =Yp.
Since the spectra ofcµiAi andcµiAi are non resonant moduloqZ, the spectra of
qpcµiAi andcµiAi are disjoint and the endomorphismV ↦→qpVc µjAj−cµiAiV
of Matri,rj(C) is actually an automorphism. There is therefore a unique formal
solution X, and convergence in ( C∗, 0) is not hard to prove, so we indeed get
G with the required properties. Last, putting F :=T −1
A0,cGTA0,c givesS
c ˆFA in
the desired form.
