---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-062-127-conjugacy-class-invariant
section_title: "Conjugacy class invariant"
section_number: 12.7
pages: 71-72
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
i1····· σǫℓ
iℓ of length
ℓ of generators of the braid group Brn complexes Cσǫ1
i1 ,...,σ
ǫℓ
iℓ
∈ MFsc
Bℓ×G(Xℓ,f c, 0). The group ˆG acts only
on the ﬁrst and last factors in Xℓ,f c there is a ˆG-equivariant projection pri : Xℓ,f c→ g2×V :
pri(X,g 1,Y 1,...,g ℓ,Y ℓ,u ) = (X, Adgi(Yi),u ).
The image of the map pr1 restricted to X crit
ℓ,f c consists of stable triples ( X,Y,u ), [X,Y ] = 0, C[X,Y ]u =V .
Thus we have a well-deﬁned map pr1 : St ℓ→ Hilbn.
SinceCσǫ1
i1 ,...,σ
ǫℓ
iℓ
∈ MFsc,crit
Bℓ×G(Xℓ,f c, 0) we can apply the above constructions to obtain a complex of shea ves
on Hilb n
Sσǫ1
i1 ,...,σ
ǫℓ
iℓ
:=pr1
∗(HB(Cσǫ1
i1 ,...,σ
ǫℓ
iℓ
))
ˆG.
Theorem 12.4. The sheafSσǫ1
i1 ,...,σ
ǫℓ
iℓ
depends only on conjugacy class of β =σǫ1
i1····· σǫℓ
iℓ :
(12.55) Sσǫ1
i1 ,...,1,...,σ
ǫℓ
iℓ
∼S σǫ1
i1 ,...,σ
ǫℓ
iℓ
(12.56) Sσǫ1
i1 ,...,σ
ǫℓ
iℓ
=Sσǫ2
i2 ,...,σ
ǫℓ
iℓ
,σǫ1
i1
(12.57) Sσk,σ−1
k ,σǫ1
i1 ...∼S σǫ1
i1 ,..., Sσk,σk+1,σk,... =Sσk+1,σk,σk+1,...
where∼ stands for the homotopy equivalence.
71
Proof. The conjugacy invariance (12.56) follows almost immediately from the construction. Indeed, the
deﬁnition of pri implies that
Sσǫ2
i2 ,...,σ
ǫℓ
iℓ
,σǫ1
i1
=pr2
∗(HB(Cσǫ1
i1 ,...,σ
ǫℓ
iℓ
)).
On the other hand pr1|X crit
ℓ,f c
=pr2|X crit
ℓ,f c
and hence the equality.
To prove the rest of the theorem we introduce slightly more genera l deﬁnition:
Sβ1,...,βm :=pr1
∗(HB(Xm,f c, fgt∗(cl∗(π∗
12(Cβ1)⊗···⊗ π∗
m,m+1(Cβm)))))
ˆG
Now let us observe that pr1 =pr1◦ ˆπ2 where ˆπ2 : Xm,f c→ Xm−1,f c is the projection along the second
factor. Hence we have
Sβ1,β2,...,βm =Sβ1·β2,...,βm
It implies the desired equations.
✷
For an element β∈ Brn we denote by [ β] its conjugacy class. Thus for any element of the braid group
β∈ Brn we have a quasi-coherent sheaf S[β] on Hilb n.
It is not obvious to us how one could attach sheaf on the ﬂag Hilbert s cheme to a conjugacy class
in the braid group. There are well-deﬁned maps pri : St ℓ→ HilbL
1,n that send ( X,g 1,Y 1,...,g ℓ,Y ℓ,u ) to
(Ad−1
gi (X),Y i),g −1(u)). Naively one could hope that the push-forwards pri∗(H∗
B(X2,f c,C σǫ1
i1 ,...,σ
ǫℓ
iℓ
)) for some
i is a such sheaf but it is unclear why it would satisfy the properties fro m the theorem. However, as we will
see later, the push-forwards on the ﬂag Hilbert schemes are usef ul for understanding Markov moves, since
there are natural maps between the ﬂag Hilbert schemes of diﬀere nt ranks. It is also clear from the argument
of the previous theorem that for any β =σǫ1
i1····· σǫℓ
iℓ there is a well-deﬁned complex:
Sβ :=pr1,∗(H∗
B(X2,f c,C σǫ1
i1 ,...,σ
ǫℓ
iℓ
))∈Dper
Tsc (HilbL
1,n).
