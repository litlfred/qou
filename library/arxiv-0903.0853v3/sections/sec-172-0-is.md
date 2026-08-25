---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-172-0-is
section_title: "Is"
section_number: 0
pages: 109-110
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
give the same privileged cocycle, which we shall now describe more precisely.
Remark 6.1.3 . — The construction in theorem 4.4.1 is not deterministic,
since it involves the choice of a good covering and of functio ns gi asymptotic
to ˆF. However, among the possible choices, there is the possibil ity to take the
sums deﬁned by theorems 5.5.7 and 6.1.2. Thus, among the poss ible cocycles
constructed in theorem 4.4.1, there is our privileged cocyc le.
If M0 is the pure module with matrix A0, recall from section 4.3 the sheaf
ΛI(M0) of automorphisms of A0 inﬁnitely tangent to the identity. We shall
also denote U the covering of Eq consisting of the Zariski open subsets Uc :=
Eq\{c} such that c⁄∈ΣA0 (thus, we drop the upper bar denoting classes
in Eq). For any c∈ Eq\ ΣA0 an authorized direction of summation, write
for short Fc := Sc ˆFA. Then Fc is holomorphic invertible over the preimage
p−1(Uc)⊂ C∗. If c,d∈ Eq\ΣA0,Fc,d :=F −1
c Fd is in G
(
O(p−1(Uc∩Ud))
)
and
it is an automorphism of A0 inﬁnitely tangent to the identity:
Fc,d∈ ΛI(M0)(Uc∩Ud).
The cocycle (Fc,d)∈ Z 1(U, ΛI(M0)) involves rectangular blocks ( Fc,d)i,j (for
1 ≤ i < j≤ k) belonging to the space Ei,j of solutions of the equation
(σqX)zµjAj =zµiAiX. For X∈Ei,j, it makes sense to speak of its poles on
Eq, and of their multiplicities. Forc,d∈ Eq\ΣA0 distinct, we writeEi,j,c,d the
space of those X∈Ei,j that have at worst poles in c,d and with multiplicities
µj−µi.
Lemma 6.1.4 . — The space Ei,j,c,d has dimension rirj(µj−µi).
Proof. — Writing again θq,a(z) := θq(z/a), any X ∈ Ei,j,c,d can be written
(θq,aθq,b)−(µj −µi)Y , where p(−a) = c, p(−b) =d and Y is holomorphic on C∗
and satisﬁes the equation:
σqY =
(z
ab
) µj −µi
AiYA −1
j .
Taking Y as a Laurent series, one sees that ( µj−µi) consecutive terms in
Matri,rj(C) can be chosen at will.
Deﬁnition 6.1.5 . — The cocycle ( Fc,d)∈Z 1(U, ΛI(M0)) is said to be priv-
ileged if (Fc,d)i,j∈Ei,j,c,d for all distinct c,d∈ Eq\ ΣA0 and all 1≤i<j ≤k.
The space of privileged cocycles is denoted Z 1
pr(U, ΛI(M0)).
104 CHAPTER 6. GEOMETRY OF THE SPACE OF CLASSES
It is not hard to see that, i,j being ﬁxed, the corresponding component
(c,d )↦→(Fc,d)i,j of a cocycle is totally determined by its value at any particular
choice of c,d . That is, ﬁxing distinct c,d∈ Eq\ ΣA0 gives an isomorphism:
Z 1
pr(U, ΛI(M0))→
⨁
1≤i<j≤k
Ei,j,c,d.
Thus, the space of privileged cocycles has the same dimensio n as F(M0).
Actually, one has two bijections:
Theorem 6.1.6. — The following natural maps are bijections:
F(M0)→Z 1
pr(U, ΛI(M0))→H 1(Eq, ΛI(M0)).
Proof. — See [ 50, prop. 3.17, th. 3.18]. The second map is the natural
one.
6.1.3. q-Gevrey interpolation. — The results found in section 3.4 can be
adapted here mutatis mutandis : the two classiﬁcation problems tackled there
lead to the following spaces of classes: ⨁
µj −µi<1/s
Ei,j,c,d and ⨁
µj −µi≥1/s
Ei,j,c,d,
which have exactly the desired dimensions. This can be most e asily checked
using the devissage arguments from section 6.2 below.
