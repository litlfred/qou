---
doc_id: arxiv-0806.2317v1
doc_title: "Bounds for codes and designs in complex subspaces Aidan Roy ∗"
section_id: sec-009-association-schemes
section_title: "Association schemes"
section_number: null
pages: 27-32
source_pdf: 0806.2317v1.pdf
source_sha256: c54e80d460413a5e
doc_brief: "Bounds for codes and designs in complex subspaces Aidan Roy ∗ — We introduce the concepts of complex Grassmannian codes and designs."
---
As Theorem 9.6 indicates, sets of Grassmannian subspaces wh ich reach equality
in the Delsarte bounds have a great deal of structure. In this section, we show
that—much like spherical codes and spherical designs—thes e sets are often
endowed with the structure of an association scheme.
Let S be an f -code with a ﬁnite number of distinct sets of principal angle s
y = (y1, . . . , y m). Denote the set of y’s that occur by Y. For each y ∈ Y , deﬁne
a |S| × |S| matrix as follows:
Ay(a, b ) :=
{
1, a, b have principal angles y;
0, otherwise.
Each Ay is a symmetric {0, 1}-matrix. Furthermore, each pair ( a, b ) has some
principal angle y, so ∑
y∈Y Ay = J, where J is the all-ones matrix. If y0 :=
(1, . . . , 1) denotes the trivial principal angles set, then A0 := Ay0 is the identity
matrix. We will call the Ay matrices Schur idempotents, as they are idempotent
under Schur multiplication, deﬁned as follows:
(A ◦ B)ij := AijBij.
27
Under certain conditions, these Schur idempotents form an a ssociation scheme.
For each integer partition µ and corresponding zonal polynomial Zµ , deﬁne
an |S| × |S| matrix as follows:
Eµ (a, b ) := 1
|S| Zµ (a, b ).
Each Eµ is also symmetric and in the span of {Ay}y∈Y :
Eµ = 1
|S|
∑
y∈Y
Zµ (y)Ay.
In particular, E0 is a scalar multiple of J. When {Ay}y∈Y forms an association
scheme, the matrices Eµ are the scheme’s idempotents.
Lemma 10.1. If S is a 2t-design, then {Eµ }|µ |≤t, len(µ )≤m are a set of orthogonal
idempotents.
Proof. Suppose |µ | = i and |λ| = j, with i, j ≤ t. Then
(Eµ Eλ )a,b = 1
|S|2
∑
c∈S
Zµ (a, c )Zλ (c, b )
= 1
|S| ⟨Zµ,a , Z λ,b ⟩S .
Since Zµ,a and Zµ,b are in Ht, their product is in H2t. Now S is a 2 t-design, so
the average of Zµ,a Zλ,b over S is the same as the average over Gm,n . But
⟨Zµ,a , Z λ,b ⟩ = δλ,µ Zµ (a, b ),
and so we ﬁnd that Eµ Eλ = δλ,µ Eµ .
More generally, if |µ | = i and |λ| = j, and S is a ( i + j)-design, then Eµ and
Eλ are orthogonal.
Now suppose S is a 2 t-design. By the previous lemma {Eµ }|µ |≤t are linearly
independent, and clearly the matrices {Ay}y∈Y are also linearly independent. If
|Y| equals the number of partitions of at most t (into at most m parts), then the
span of {Ay}y∈Y and {Eµ }|µ |≤t are the same. Since {Eµ }|µ |≤t is closed under
multiplication, so too is the span of {Ay}y∈Y , and so we have an association
scheme.
Corollary 10.2. Let S be a 2t-design in Gm,n with principal angle set Y. If
|Y| is equal to the total number of partitions of 0, 1, . . . , t into at most m parts,
then {Ay}y∈Y is an association scheme.
28
Lemma 10.3. Let S be a 2t-design in Gm,n with principal angle set Y such
that |Y| is the total number of partitions of 0, 1, . . . , t into at most m parts.
Then {Eµ }|µ |≤t, len(µ )≤m are the idempotents of the scheme {Ay}y∈Y .
Proof. Since Eµ = 1
|S|
∑
y∈Y Zµ (y)Ay, we see that the matrix [ Zµ (y)] is
the transition matrix between the two bases of the associati on scheme and is
therefore invertible. It follows that for each yi in Y, some linear combination of
the rows Zµ forms a homogeneous degree- t polynomial gi such that gi(yj) = δij.
(Conversely, if such gi polynomials exist, then [ Zµ (y)] is invertible.) Then
(AiEµ )a,b = 1
|S|
∑
c:y(a,c )=yi
Zµ (c, b )
= ⟨gi,a , Z µ,b ⟩S
= ⟨gi,a , Z µ,b ⟩.
Now write gi =∑
|λ |≤t ci,λ Zλ , so that
⟨gi,a , Z µ,b ⟩ =
∑
|λ |≤t
ci,λ ⟨Zλ,a , Z µ,b ⟩ = ci,µ Zµ (a, b ).
Thus AiEµ = ci,µ Eµ for some ci,µ .
By way of example, let t = 1, and suppose S is a 2-design with only one
nontrivial principal angle set (and one trivial one, for a to tal of two). The
number of partitions of at most 1 is also two ( µ = 0 and µ = (1)), so by
Corollary 10.2 we have an association scheme. In this case th e scheme is the
trivial one, namely {I, J − I}.
As another example of an association scheme obtained from pr incipal angles,
consider the collection of subspaces in Gn/ 2,n from Theorem 8.1. This collection
has four distinct sets of principal angles:
y = (1, . . . , 1) (trivial principal angles) ,
y = (0, . . . , 0) (angles between a and a⊥),
y = (1, . . . , 1/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
n/ 4
, 0, . . . , 0/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
n/ 4
),
y = ( 1
2 , . . . , 1
2 ).
While |Y| = 4 is the number of partitions of at most 2 ( µ = 0, µ = (1),
µ = (1 , 1) and µ = (2)), the hypotheses of Corollary 10.2 are not satisﬁed
29
because the subspaces do not form a 4-design. Nevertheless, it is easy to verify
computationally that this collection does give a 3-class as sociation scheme.
We may deﬁne a coarser set of relations on an f -code S using the sums of
principal angles—the inner products of the projection matr ices—instead of the
principal angles themselves. Let A denote the set of nontrivial inner product
values that occur in S, so S is an A-code. For α ∈ A let A′
α be the |S| × | S|
matrix deﬁned as follows:
A′
α (a, b ) :=
{
1, tr(PaPb) = α,
0, otherwise.
Also deﬁne A′
m := I for the identity relation. Clearly each A′
α is in the span of
{Ay : y ∈ Y} ; in fact
A′
α =
∑
y∈Y: P yi=α
Ay.
In particular, A′
m = A0 = I, and if 0 is in A, then A′
0 = A(0,..., 0). As before, the
matrices are Schur idempotents and sum to J. Next we need the corresponding
idempotents. For each i ∈ {0, . . . , t }, deﬁne E′
i as follows:
E′
i :=
∑
|µ |=i
Eµ .
This implies that E′
0 = J/ |S| and E′
i(a, b ) = ( Zi(a, b ) − Zi−1(a, b ))/ |S| for
i > 0. As in Lemma 10.1, if S is a 2 t-design, then {E′
i : i ≤ t} is a set of
orthogonal idempotents, and if S is a (2 t − 1)-design, then {E′
i : i ≤ t} are
linearly independent.
Clearly E′
i is in the span of {Ay : y ∈ Y} , since each Eµ is in that span. But
suppose Zi(y) is the annihilator polynomial of some i-distance set, so it is a only
function of ∑
i yi: then in fact E′
i is in the span of {A′
α : α ∈ A}. If Zi(y) is an
annihilator for suﬃciently many i, then {E′
i : 0 ≤ i ≤ t} and {A′
α : α ∈ A∪{ m}}
span the same set, and that set is closed under multiplicatio n.
Corollary 10.4. Let S be a 2t-design that is also an A-code in Gm,n . If |A| ≤ t,
and Zi(y) is an annihilator polynomial for each i ≤ t, then {A′
α : α ∈ A ∪ {m}}
is an association scheme.
In fact, these hypotheses can be weakened.
Theorem 10.5. Let S be a (2t − 2)-design that is also an A-code in Gm,n . If
|A| = t, and Zi(y) is an annihilator for each 0 ≤ i ≤ t − 1, then {A′
α : α ∈
A ∪ {m}} is an association scheme.
30
Proof. Since S is a 2( t − 1)-design, the idempotents {E′
i : 0 ≤ i ≤ t − 1}
are linearly independent. We claim that I is also linearly independent from
{E′
i : 0 ≤ i ≤ t − 1}. For, if I =∑ t−1
i=0 ciE′
i, then the oﬀ-diagonal entries of I
are functions of a polynomial of degree at most t − 1 in ∑
j yj, namely
1
|S|
(
c0 +
t−1∑
i=1
ci(Zi(y) − Zi−1(y))
)
.
But all oﬀ-diagonal entries are 0, implying that the polynomi al has t roots in∑
i yi, a contradition. So {E′
i : 0 ≤ i ≤ t − 1} ∪ {I} is linearly independent and
therefore spans {A′
α : α ∈ A ∪ {m}}. Since it is closed under multiplication, we
have an association scheme.
By way of example, suppose t = 2 in Theorem 10.5. Note that Z0(y) and
Z1(y) are always annihilators. It follows that if S is a 2-design, and the inner
product set A = {tr(PaPb) : a ⁄= b ∈ S} contains exactly two distinct values,
then {A′
α : α ∈ A ∪ { m}} is a 2-class association scheme.
Corollary 10.6. Let S be a (2t − 2)-design and an A-code in Gm,n such that
|A| = t and Zi(y) is an annihilator for i ≤ t − 1. Then the idempotents of the
scheme {A′
α : α ∈ A ∪ { m}} are E′
0, . . . , E ′
t−1, and J −∑ t−1
i=0 E′
i.
Proof. Let fα denote the annihilator polynomial of A\{α 0, α }, normalized
so that fα (α ) = 1. Then fα is a polynomial of degree t − 1 in ∑
i yi, and the
corresponding zonal polynomial fα,a is in Ht−1(n). Writing Pi := Zi − Zi−1 =∑
|µ |=i Zµ , we have
(A′
α E′
i)a,b = 1
|S|
∑
tr(PaPc)=α
Pi(tr(PcPb))
= ⟨fα,a , P i,b ⟩S − fα (m)
|S| Pi(tr(PaPb))
= ⟨fα,a , P i,b ⟩ − fα (m)
|S| Pi(tr(PaPb)).
Now decomposing into its degrees as fα =∑
i cα,i Pi, we get
(A′
α E′
i)a,b = cα,i ⟨Pi,a , P i,b ⟩ − fα (m)
|S| Pi(tr(PaPb))
= cα,i Pi(tr(PaPb)) − fα (m)
|S| Pi(tr(PaPb))
= (cα,i |S| − fα (m))(E′
i)a,b .
Thus A′
α E′
i = λ α,i E′
i for some constant λ α,i .
31
