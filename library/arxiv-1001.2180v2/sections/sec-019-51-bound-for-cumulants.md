---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-019-51-bound-for-cumulants
section_title: "Bound for cumulants"
section_number: 5.1
pages: 18-21
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
character values) has already been stated by P. Śniady in the case where the characters are small and the
corresponding diagrams balanced. Here, we have to use diﬀer ent observables and a diﬀerent gradation,
but the ideas of the proof are the same, and the deﬁnitions of t he diﬀerent cumulants used here come
from [ Śni06]. In particular we shall use joint cumulants of random varia bles k(X1, . . . , Xr), which can be
deﬁned by induction 2 on r:
/BX [X1 X2 · · ·Xr] =
∑
π partition
of {1,2,...,r}
k
(
Xi∈π1
)
k
(
Xi∈π2
)
· · ·k
(
Xi∈πℓ
)
.
A centered gaussian vector (Y1, . . . , Yk) is characterized by the fact that all k(Yi1 , . . . , Yir ) are equal to
0 for r ⁄= 2 . Moreover, the values for r = 2 give then the covariance matrix. Therefore, the proof of
Proposition 16 consists in computing the limit of k(Wn,q,i1 , . . . , Wn,q,ir ). In fact, we will show a stronger
result than the convergence towards 0 for r ≥ 3:
Lemma 17 (Order of magnitude of cumulants) . For any x1, x2, . . . , xr ∈ O, one has:
k(x1, . . . , xr) = O
(
ndeg(x1)+···+deg(xr)−r+1
)
.
The end of this subsection is devoted to the proof of this lemm a. Thanks to the multi-linearity of
cumulants (for r ≥ 2) and some compatibility relation with respect to products ( see [ LS59] and [ Śni06,
Theorem 4.4]), it is enough to prove this lemma with the xi in any graded algebraic basis of O. A good
choice is the basis (Σk)k≥1; indeed, we have already computed the expectation of these o bservables under
the q-Plancherel measure. Unfortunately, we do not know their jo int moments /BX [Σi1 · · ·Σir ], which are
diﬀerent from what we have computed in the previous section, namely, /BX [Σi1,...,ir ].
5.1.1. Cumulants k•. This diﬃculty disappears if we use the algebra O •, because Σ i1 •· · ·• Σ ir = Σ i1,...,ir .
This algebra gives rise to a new kind of cumulant, the so-call ed disjoint cumulants, which we shall
denote by k•(X1, . . . , Xr). Their deﬁnition is the same as for k(X1, . . . , Xr), except that the product of
observables is now the disjoint product:
(10)
/BX [X1 • X2 • · · · • Xr] =
∑
π partition
of {1,2,...,r}
k•(
Xi∈π1
)
k•(
Xi∈π2
)
· · ·k•(
Xi∈πℓ
)
.
It is easy to prove the analog of Lemma 17 for these disjoint cumulants:
Lemma 18 (Order of magnitude of disjoint cumulants) . For any x1, x2, . . . , xr ∈ O, one has:
k•(x1, . . . , xr) = O
(
ndeg(x1)+···+deg(xr)−r+1
)
.
Proof. As for classical cumulants, it is enough to prove it for xj = Σij . In this case, the left-hand side of
(10) is simply
/BX [Σi1,...,ir ] = (q − 1)i1+···+ir
∏ (qij − 1) n↓(i1+···+ir ).
2It can also be deﬁned via generating functions.
ASYMPTOTICS OF q-PLANCHEREL MEASURES 19
Except for the factor n↓(i1+...+ir ), everything is multiplicative with respect to the parts of λ. More
formally, there exist numbers αi such that:
/BX [Σi1,...,ir ] =

∏
j
αij

 n↓(i1+···+ir );
=

∏
j
αij


/BX
[
Σ 1, . . . ,1/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
i1+···+ir times
]
.
An immediate induction implies that:
k•(Σi1 , . . . , Σin ) =

∏
j
αij

 k•(Σ1, . . . ,1/bracehtipupleft
/bracehtipdownright/bracehtipdownleft/bracehtipupright
i1 times
, . . . , Σ1, . . . ,1/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
ir times
).
But χλ(Σ1i) = n↓i for any λ, so the corresponding cumulants do not depend on the measure considered
on Young diagrams, and we can use the result of P. Śniady who pr oved ([Śni06, Lemma 4.8]) that:
k•(Σ1, . . . ,1/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
i1 times
, . . . , Σ1, . . . ,1/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
ir times
) = O(ni1+···+ir−(r−1)).
This ends the proof of this lemma. □
5.1.2. Cumulants kid. The last problem is to link classical and disjoint cumulants . Thanks to the com-
mutativity of the diagram below
O O •
/BV
/d31/d31/d63/d63/d63/d63/d63
/BX =Mn,q
/d47/d47
/BX
id
/d127/d127/d127/d127/d127/d127/d127
/BX =Mn,q
this can be done by using a result of Brillinger [ Bri69]. One obtains the following formula, see [ Śni06,
Proposition 4.1]:
(11) k(X1, X2, . . . , Xn) =
∑
π⊢n
k•(kid(Xi∈π1), kid(Xi∈π2 ), . . . , kid(Xi∈πr )),
where kid is the cumulant corresponding to the identity map
/BX
id of the diagram (note that kid takes value
in O), that is to say that it is deﬁned by
X1X2 · · · Xr =
∑
π partition
of {1,2,...,r}
kid(
Xi∈π1
)
• kid(
Xi∈π2
)
• · · · • kid(
Xi∈πℓ
)
.
We will prove the following bound on the degree of identity cu mulants. For any i1, . . . , ir, one has:
(12) deg
(
kid(Σ i1 , . . . ,Σ ir )
)
≤ i1 + · · · + ir − (r − 1).
Note that it is not the same as [ Śni06, Theorem 4.3]; indeed, we use a diﬀerent gradation on the alg ebra
of observables.
Let us begin by looking at kid(Σi1 , . . . , Σin ) for small values of n. For n = 1, by deﬁnition kid(Σi) = Σi.
For n = 2, one has:
kid(Σi1 , Σi2 ) = Σi1 · Σi2 − Σi1,i2 .
20 V ALENTIN FÉRAY AND PIERRE-LOÏC MÉLIOT
But one also has
Σi1 · Σi2 =
∑
A1∈A(n,i1), A2∈A(n,i2)
C(A1) C(A2);
Σi1,i2 =
∑
A1∈A(n,i1), A2∈A(n,i2)
A1∩A2=∅
C(A1) C(A2).
so the diﬀerence kid is equal to the same expression with the sum restricted to pai rs of arrangements
which have a non-empty intersection:
kid(Σi1 , Σi2 ) =
∑
A1∈A(n,i1), A2∈A(n,i2)
A1∩A2⁄=∅
C(A1) C(A2).
It turns out that the identity cumulants satisfy a similar id entity in the general case, and the intersections
between the Aj play once again a signiﬁcant role. First, note that:
Σi1 · · · Σir =
∑
∀j, A j ∈A(n,ij )
C(A1) · · · C(Ar)
Given a family A1, . . . , Ar of arrangements, we consider the relation ∼1 deﬁned by k ∼1 l ⇔ Ak ∩ Al ⁄= ∅.
Its transitive closure is an equivalence relation; let us de note by π(A1, . . . , Ar) the corresponding partition
of [ [1, r] ]. Obviously, this partition depends only on which indices ar e equal and not on the values they
take, so the sum of C(A1) · · ·C(Ar) over arrangements corresponding to a given partition is of t he form
X G
i1,...,ir (notation of paragraph 3.5) and we can use Lemma 8 on this kind of expression.
Lemma 19. For any i1, . . . , ir, one has:
kid(Σi1 , . . . , Σir ) =
∑
∀j, A j ∈A(n,ij )
π(A1,...,Ar)={[ [1,r] ]}
C(A1) · · · C(Ar).
Proof. We will prove this statement by induction on r. As explained above, it is true for r = 1 , 2. Let
us suppose that it is true for all s ≤ r − 1. Because of the deﬁnition of the disjoint product •, for every
non-trivial set partition π, one has:
kid(
Σi∈π1
)
• kid(
Σi∈π2
)
• · · · • kid(
Σi∈πℓ
)
=
∑
∀j, A j ∈A(n,ij )
π(A1,...,Ar)=π
C(A1) · · · C(Ar).
Indeed, the induction hypothesis applies for each part πi, so we only keep terms corresponding to sequences
of arrangements for which two numbers in the same part of π are in the same part of π(A1, . . . , Ar).
Besides, when we form the product •, we take only disjoint set of indices (using Lemma 8), so two
numbers in diﬀerent parts of π cannot be in the same part of π(A1, . . . , Ar).
We use now the inductive deﬁnition of kid:
kid(Σi1 , . . . , Σir ) = Σi1 · · ·Σir −
∑
π⁄={[ [1,r] ]}
kid(
Σi∈π1
)
• kid(
Σi∈π2
)
• · · · • kid(
Σi∈πℓ
)
=
∑
∀j, A j ∈A(n,ij )
C(A1) · · ·C(Ar) −
∑
π⁄={[ [1,r] ]}




∑
∀j, A j ∈A(n,ij )
π(A1,...,Ar)=π
C(A1) · · · C(Ar)




=
∑
∀j, A j ∈A(n,ij )
π(A1,...,Ar)={[ [1,r] ]}
C(A1) · · ·C(Ar),
which is exactly the equality we wanted at rank r. □
ASYMPTOTICS OF q-PLANCHEREL MEASURES 21
Now, for every sequence of arrangements A1, . . . , Ar such that π(A1, . . . , Ar) is the trivial partition
{[ [1, r] ]}, the cardinality of |A1 ∪ · · · ∪ Ar| is smaller than i1 + · · · + ir − (r − 1), because one has at least
r − 1 equalities between diﬀerent elements of these arrangement s. So, kid(Σi1 , . . . , Σir ) can be written as
a linear combination of Σλ with |λ| ≤ i1 + · · · + ir − (r − 1), which ends the proof of equation ( 12).
Finally, equations ( 11) and ( 12), together with Lemma 18, complete the proof of Lemma 17.
