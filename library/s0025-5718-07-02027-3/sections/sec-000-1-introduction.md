---
doc_id: s0025-5718-07-02027-3
doc_title: "Li(p)-service? An algorithm for computing p-adic polylogarithms"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: S0025-5718-07-02027-3.pdf
source_sha256: 080b5ac8542ff19c
doc_brief: "Li(p)-service? An algorithm for computing p-adic polylogarithms — We describe an algorithm for computing Coleman’s p-adic poly- logarithms up to a given precision."
---
It is well known that, for a number ﬁeld k with ring of integers Ok,t h e r ei sa
relation between the regulator of the group of units of Ok, O∗
k, and the residue of
ζk(s)a t s =1 . I nt e r m so fK-theory, O∗
k ∼= K1(Ok), and Borel in [6] showed that
this relation generalizes, for n =2 , 3,... , to a similar relation between a suitably
deﬁned regulator of the higherK-group K2n−1(Ok) and the value ofζk(s)a t s = n.
However, it is far more diﬃcult to ﬁnd explicit non-trivial elements in those
higher K-groups than in O∗
k.B u t K2n−1(Ok) ∼= K2n−1(k)f o r n ≥ 2a n dZ a -
gier in [17] gave a conjectural description of the latter groups tensored with Q.
His construction always gives a Q-subspace (see, e.g., [9]), and gives the whole of
K3(k) ⊗Z Q and K5(k) ⊗Z Q for all number ﬁelds k,a sw e l la so fK2n−1(k) ⊗Z Q
for all n ≥ 2i f k is cyclotomic (see loc. cit. where this is deduced from results by
Suslin, Goncharov and Zagier respectively).
The regulator for O∗
k is deﬁned as the determinant of a matrix with its entries
the logarithm of the absolute value of certain elements of O∗
k embedded into C.I n
Zagier’s conjecture the Borel regulator for K2n−1(k) ∼= K2n−1(Ok) is obtained as
the determinant of a matrix with its entries suitable Q-linear combinations of the
values at certain elements of k embedded into C of the n-th (real) polylogarithm.
This n-th real polylogarithm is obtained from the complex polylogarithm Lin(z),
which is deﬁned by the power series
(1.1) Li n(z)=
∞∑
k=1
zk
kn (n ≥ 1)
on the open unit disc in C. It can be continued analytically to a multi-valued func-
tion on C \{ 0, 1}. The real-valued modiﬁcation is easily computed from this. For
the numerical veriﬁcation of the conjectures in the context of Zagier’s conjecture,
it is important to have an eﬃcient implementation of the complex polylogarithm,
as in, for example, PARI-GP.
Received by the editor June 19, 2006 and, in revised form, December 18, 2006.
2000 Mathematics Subject Classiﬁcation. Primary 11Y16, 11G55; Secondary 11S80.
Key words and phrases. Computational number theory, Coleman integration, p-adic
polylogarithm.
c©2007 American Mathematical Society
Reverts to public domain 28 years from publication
1105
1106 AMNON BESSER AND ROB DE JEU
There is a conjectural p-adic analogue of Borel’s theorem which ﬁts into the
general context of relations between regulators of K-groups and special values of
L-functions as conjectured by Beilinson (see [1] or [13]). Its predictions are rather
similar, but somewhat more involved, using the syntomic regulator [2] rather than
the Beilinson regulator. In the case of totally real number ﬁelds it follows from [5]
that the p-adic regulator on the part of theK-groups given by Zagier’s conjecture
1
is given by a determinant as before, but with the complex polylogarithm replaced
