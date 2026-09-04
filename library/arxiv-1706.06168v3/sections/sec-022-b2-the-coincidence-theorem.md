---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-022-b2-the-coincidence-theorem
section_title: "B.2 The Coincidence Theorem"
section_number: null
pages: 35-36
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨ and´ en characterized all linear oper ators on multivariate polynomials which preserve the"
---
The Grace-Walsh-Szeg˝ o coincidence theorem has strong ties to Grace’s theorem, and most books and surveys
on the subject state the two results side by side. Some books (e.g., [RS02]) even go so far as to demonstrate
their equivalence, perhaps with other results involving typical polyn omial convolutions. Here, we will state
and prove the general multivariate version of the theorem in terms of homogeneous polynomials, making use
of evaluation symbols and Grace’s theorem (Theorem 5.1).
First though, consider the following corollary to the symbol lemma (L emma 3.7) which is similar in spirit
to the evaluation symbol lemma (Lemma 5.10). Note that when applied to p ∈V (n) with m = 1, this result
has the following intuitive statement as a corollary: Dn(q ⊗p) is equal to the evaluation of Π ↑
np at the roots
of q.
Lemma B.4. Fix λ ∈ Nm
0 , p ∈V (λ), and any (a :b) ∈ (CP1)|λ|, more explicitly deﬁned as follows:
(a :b) ≡
(
(a1,1 :b1,1),..., (a1,λ1 :b1,λ1),..., (am,1 :bm,1),..., (am,λm :bm,λm)
)
∈ (CP1)λ1+···+λm
35
We have the following:
(Π ↑
λp)(a,b ) = Dλ
(
Π ↓
λ
(
Symb(ev(a,b))
)
⊗p
)
=Dλ


m∏
k=1
λk∏
j=1
(bk,jxk −ak,jyk) ⊗p


Proof. We ﬁrst prove the case of m = 1 and p ∈V (n), given as follows:
(Π ↑
np)(a,b ) = Dn (
Π ↓
n
(
Symb(ev(a,b))
)
⊗p
)
=Dn


n∏
j=1
(bjx −ajy) ⊗p


The second equality follows immediately from the deﬁnition of Π ↓
n and of ev (a,b) (Deﬁnition 5.9). For the
ﬁrst equality, Lemma B.2 implies:
Dn (
Π ↓
n
(
Symb(ev(a,b))
)
⊗p
)
=D(1n) (
Π ↑
n ◦ Π ↓
n
(
Symb(ev(a,b))
)
⊗ Π ↑
np
)
By deﬁnition of Π ↑
n, both Π ↑
n ◦ Π ↓
n
(
Symb(ev(a,b))
)
and Π ↑
np are symmetric in pairs of variables. Further, we
can explicitly compute:
Π ↑
n ◦ Π ↓
n
(
Symb(ev(a,b))
)
= 1
n!
∑
σ∈Sn
n∏
j=1
(bjxσ(j) −ajyσ(j))
This expression and the fact that Π ↑
np is symmetric then imply:
D(1n) (
Π ↑
n ◦ Π ↓
n
(
Symb(ev(a,b))
)
⊗ Π ↑
np
)
= 1
n!
∑
σ∈Sn
D(1n)


n∏
j=1
(bjxσ(j) −ajyσ(j)) ⊗ Π ↑
np


=D(1n)


n∏
j=1
(bjxj −ajyj) ⊗ Π ↑
np


The last expression is then equal to (Π ↑
np)(a,b ) by the evaluation symbol lemma (Lemma 5.10).
For the general case of p ∈V (λ), the same argument applies with a few tweaks. The key change is th at
Π ↑
λ ◦ Π ↓
λ
(
Symb(ev(a,b))
)
and Π ↑
λp are no longer fully symmetric in pairs of variables, but instead invarian t
under the action of Sλ1 × · · · ×Sλm on the |λ| pairs of variables.
Generally speaking, the above lemma demonstrates the strong con nection between the apolarity form
and the polarization map. We now utilize this to prove the coincidence t heorem.
Corollary B.5 (Grace-Walsh-Szeg˝ o). Fix λ ∈ Nm
0 , p ∈ V (λ), and any disjoint Grace pair (C1 × · · · ×
Cm,B 1 × · · · ×Bm). If p is (C1 × · · · ×Cm)-stable, then Π ↑
λp is (Cλ1
1 × · · · ×Cλm
m )-stable.
Proof. So as to prove the contrapositive, suppose Π ↑
λp is not ( Cλ1
1 × · · · × Cλm
m )-stable. That is, suppose
(Π ↑
λp)(a,b ) = 0 for some ( a,b ) = (a1,b 1,...,a m,λm,b m,λm) ∈ C2|λ| such that (aj,k :bj,k) ∈Cj for all j ∈ [m]
and k ∈ [λj]. By the previous lemma, this implies:
Dλ
(
Π ↓
λ
(
Symb(ev(a,b))
)
⊗p
)
= 0
By disjointness of Cj and Bj for all j ∈ [m], we then have that ( aj,k : bj,k) ⁄∈Bj for all j,k . Therefore
Symb(ev(a,b)) is ( Bλ1
1 × · · · × Bλm
m )-stable (see Deﬁnition 5.9). This implies Π ↓
λ
(
Symb(ev(a,b))
)
is (B1 ×
· · · ×Bm)-stable. Since Dλ
(
Π ↓
λ
(
Symb(ev(a,b))
)
⊗p
)
= 0, the deﬁnition of Grace pair (Deﬁnition 5.2) then
implies p must not be ( C1 × · · · ×Cm)-stable.
By Theorem 5.7, this implies the coincidence theorem for circular regions when m > 1 and for any
projectively convex regions when m = 1. Notice that there is no reference made to degree or convexity
restrictions (compare this to Theorems 1.1 and 1.2 in [ BB09b]). As discussed above, this is one of the main
beneﬁts of using homogeneous polynomials and interpreting zeros a s lying in CP1 and ( CP1)m.
36
