---
doc_id: arxiv-1712.04887v3
doc_title: "Bloch groups, algebraic K-theory, units, and Nahm's conjecture"
section_id: sec-002-12-algebraic-k-groups-and-associated-units
section_title: "Algebraic K-groups and associated units"
section_number: 1.2
pages: 4-6
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
doc_brief: "Bloch groups, algebraic K-theory, units, and Nahm's conjecture — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn = F"
---
concerns the relation to the algebraic K-theory of ﬁelds. The group B(F ) was introduced
by Bloch as a concrete model for the abstract K-group K3(F ). It was proved by Suslin [30]
that, ifF is a number ﬁeld, then (up to 2-torsion)K3(F ) is an extension ofB(F ) by the roots
of unity in F , and in this case one also knows by results of Borel and Suslin–Merkurjev [29],
[21], [35] that K3(F ) has the structure
K3(F ) ∼= Zr2(F ) ⊕
{
Z/w2(F )Z if r1(F ) = 0,
Z/2w2(F )Z⊕ (Z/2Z)r1(F )−1 if r1(F )≥ 1, (9)
where (r1(F ),r 2(F )) is the signature of F and w2(F ) is the integer
w2(F ) = 2
∏
p
pνp, ν p := max
{
ν∈ Z|ζpν +ζ−1
pν ∈F
}
. (10)
For a detailed introduction to the algebraic K-theory of number ﬁelds, see [35].
Theorem 1.2 is then a companion of the following result expressed in terms of K3(F )
rather than the Bloch group B(F ):
Theorem 1.5. LetF be a number ﬁeld. Then there is a canonical map
cζ : K3(F )/nK3(F ) −→
(
O×
S,n/O×n
S,n
)χ−1
⊂
(
F×
n/F×n
n
)χ−1
(11)
deﬁned using the theory of Chern classes for some ﬁnite set S of primes depending only
on F . If n is prime to a certain integer MF depending on F , then the map cζ is injective
and its image is contained in
(
O×
n/O×n
n
)χ−1
, and equal to this if n is prime.
We note that the proof of Theorem 1.2 relies upon the precise computation of K3(F ) and
the properties ofcζ given above. Finally, in view of the near isomorphism betweenB(F ) and
K3(F ), one might guess that the two maps Pζ and cζ are the same, at least up to a simple
scalar. This is the content of our next theorem.
Theorem 1.6. Forn prime to MF , the map Rζ equalscγ
ζ for some γ∈ (Z/nZ)×.
The constant γ does not depend on the underlying ﬁeld; both our construction and the
Chern class map are well behaved in ﬁnite extensions, so we can compare the maps over
any two ﬁelds with the maps in their compositum. We conjecture that the constant γ is, up
to sign, a power of 2 that is independent of both F and n. More optimistically, one might
further guess that γ is exactly 2. To motivate our conjecture, and to determine γ, it suﬃces
to compute the image under both maps Rζ and cζ of some element of K3(F )/nK3(F ) of
exact order n. For each root of unity ζ of order n, there is a speciﬁc element ηζ (eq. (34)) of
the ﬁnite Bloch group B(Q(ζ +ζ−1)) that is of exact order n. Using the relation of the map
Rζ to the radial asymptotics of certain q-series called Nahm sums discussed in Section 7, we
will prove
Rζ(ηζ) = ζ2 (12)
BLOCH GROUPS, ALGEBRAIC K-THEORY, UNITS, AND NAHM’S CONJECTURE 5
(Theorem 7.4). On the other hand, certain expected functorial properties of the map cζ,
discussed in Section 5.3 indicate that up to sign and a small power of 2, we have:
cζ(ηζ)
?
= ζ, (13)
and in combination with (12) this justiﬁes our conjecture concerning γ.
The above-mentioned relation between our modn regulator map on Bloch groups and the
asymptotics of Nahm sums near roots of unity is also an ingredient of our proof of Nahm’s
conjecture (under some restrictions) relating the modularity of his sums to torsion in the
Bloch group. The argument, described in Section 7.3, uses the full strength of Theorem 1.2
and gives a nice demonstration of the usefulness, despite its somewhat abstract statement,
of that theorem.
Theorem 1.2 also motivates a mod n (or ´ etale) version of the Bloch group of a number
ﬁeld F , deﬁned by
B(F ; Z/nZ) = A(F ; Z/nZ)/(nZ(F ) +C(F )), (14)
where A(F ; Z/nZ) is the kernel of the map d :Z(F )→∧ 2(F×/F×n) induced by d. This is
studied in Section 6, where we establish the following relation to K2(F ).
Theorem 1.7. The ´ etale Bloch group is related to the original Bloch group by an exact
sequence
0 −→ B(F )/nB(F ) −→ B(F ; Z/nZ) −→ K2(F )[n] −→ 0, (15)
whereK2(F )[n] is the n-torsion in the K-groupK2(F ).
There is a corresponding exact sequence (Equation (38)) withB(F )/nB(F ) andB(F ; Z/nZ)
replaced by Galois cohomology groups, and these sequences coincide for n = pm prime to
the number wF of roots of unity of F . A large part of the story that we have told here
for the Bloch group B(F ) and the third K-groupK3(F ) can be generalized to higher Bloch
groups Bm(F ) and K2m−1(F ) with m≥ 2, and here the ´ etale version really comes into its
own, because the higher Bloch groups as originally introduced in [36] have several alternative
deﬁnitions that are only conjecturally isomorphic and are diﬃcult or impossible to compute
rigorously, whereas their ´ etale versions turn out to have a canonical deﬁnition and be more
amenable to numerical computations. The study of the higher cases has many points in
common with the m = 2 case studied here, but there are also many new aspects, and the
discussion will therefore be left to a future time.
1.3. Nahm’s Conjecture. TheS-unit constructed in Section 1.1 also appears in connection
with the asymptotics near roots of unity of certainq-hypergeometric series called Nahm sums.
These series are deﬁned by
fA,B,C(q) =
∑
m∈Zr
≥0
q
1
2mtAm+Bm+C
(q)m1··· (q)mr
,
where (q)r = ∏r
k=1(1−qk) is the quantum r-factorial, A∈ Mr(Q) is a positive deﬁnite
symmetric matrix, B an element of Qr, and C a rational number. Based on ideas coming
from characters of rational conformal ﬁeld theories, Nahm conjectured a relation between the
modularity of the associated holomorphic function ~fA,B,C(τ) = fA,B,C(e2πiτ ) in the complex
6 FRANK CALEGARI, STA VROS GAROUF ALIDIS, AND DON ZAGIER
upper half-plane and the vanishing of a certain element or elements in the Bloch group
of Q. (See [24], [37], and Section 7 for more details.) This relation conjecturally goes in
both directions, but with the implication from the vanishing of the Bloch elements to the
modularity of certain Nahm sums not yet having a suﬃciently precise formulation to be
studied. The conjectural implication from modularity to vanishing of Bloch elements, on
the other hand, had a completely precise formulation, as follows. Let A be as above and
(X1,...,X r) the unique solution in (0, 1)r of Nahm’s equation
1− Xi =
r∏
j=1
X
aij
j (i = 1,...,r ).
Then Nahm shows that the element ξA =∑r
i=1[Xi] belongs to B(R∩ Q), and his assertion
is the following theorem, which we will prove as a consequence of the injectivity statement
in Theorem 1.2.
Theorem 1.8 (Nahm’s Conjecture). If the function ~fA,B,C(τ) is modular for some A, B
and C as above, then ξA vanishes in the Bloch group of Q.
We remark that the vanishing condition can be (and often is) stated by saying that ξA is
a torsion element in the Bloch group of the smallest real (but in general not totally real)
number ﬁeld containing all the Xi, but when we take the image of this Bloch group in the
Bloch group of Q or C, then the torsion vanishes, because B(Q) and B(C) are uniquely
divisible [28, Theorem 6.3] and so in particular are torsion free.
