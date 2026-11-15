---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-008-32-lifting-objects
section_title: "Lifting objects"
section_number: 3.2
pages: 15-18
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
toc_source: outline
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Rep(St)."
---
is an indeterminate. In this section we use the process of lifting idempotents (see
appendix A) to lift objects in Rep(St; F) to objects in Rep(ST ; K). We then prove
some useful properties of these lifted objects. In the next section we will show
that Rep(ST ; K) is semisimple (see Corollary 3.17), and hence uncomplicated from
16
JONATHAN COMES AND VICTOR OSTRIK
our point of view. The process of lifting objects developed in this section will be
used later in the paper to compare the structure of Rep(St; F) with that of the
semisimple category Rep(ST ; K). The following theorem will be used to deﬁne the
notion of lifting objects.
Theorem 3.9. Suppose e is an idempotent in FPn(t). Then there exists an idempo-
tent ε ∈KPn(T) of the form ε = P
π∈Pn,n aππ with aπ ∈F[[T −t]] for all π ∈Pn,n
such that ε|T =t = e (we say ε is a lift of e). Moreover, if ([n1], e1) and ([n2], e2)
are isomorphic objects in Rep(St; F) and ε1, ε2 are lifts of e1, e2 respectively, then
([n1], ε1) and ([n2], ε2) are isomorphic in Rep(ST ; K).
Proof. The existence of a lift of e is guaranteed by the ﬁrst statement of Theorem
A.2. Now suppose ([n1], e1) ∼= ([n2], e2) in Rep(St; F). To prove the remainder of
the theorem we may assume n1 ≤n2. If n1 = 0 the theorem is easy to check, so
assume n1 > 0. Set
φ :=
 idn1
if n1 = n2
φn2 · · · φn1+1
if n1 < n2
and
φ′ :=
 idn1
if n1 = n2
φ′
n1+1 · · · φ′
n2
if n1 < n2
where φn and φ′
n are as in the proof of Lemma 3.6. Then ([n1], e1) ∼= ([n2], φe1φ′)
and φε1φ′ is a lift of φe1φ′. Hence it suﬃces to show the theorem is true when n1 =
n2. In this case the remainder of the theorem follows from the second statement of
Theorem A.2 along with Proposition 2.20(2).
□
Lifted idempotents satisfy the following property.
Proposition 3.10. If ([n], e) ∼= ([n1], e1)⊕([n2], e2) in Rep(St; F) and ε, ε1, ε2 are
lifts of e, e1, e2 respectively, then ([n], ε) ∼= ([n1], ε1) ⊕([n2], ε2) in Rep(ST ; K).
Proof. By the Krull-Schmidt property there exist ¯e1, ¯e2 ∈FPn(t) with the property
([ni], ei) ∼= ([n], ¯ei) for i = 1, 2 such that e = ¯e1 + ¯e2 is an orthogonal decomposition
of the idempotent e. Let ¯ε1, ¯ε2 ∈KPn(T) be lifts of ¯e1, ¯e2 respectively. Then ¯ε1+¯ε2
is a lift of e. Hence, by Theorem A.2 and Proposition 2.20(2) ([n], ε) ∼= ([n], ¯ε1 + ¯ε2)
in Rep(ST ; K). Since ¯ε1 and ¯ε2 are orthogonal idempotents (see Theorem A.2) we
have ([n], ¯ε1 + ¯ε2) ∼= ([n], ¯ε1) ⊕([n], ¯ε2) in Rep(ST ; K). The result now follows from
the last statement of Theorem 3.9.
□
By Proposition 2.20(2) any object in Rep(St; F) is a ﬁnite direct sum of objects
of the form ([n], e).
Hence, setting Liftt([n], e) := ([n], ε), where ε ∈KPn(T)
is a lift of e ∈FPn(t) and extending to all objects in Rep(St; F) by requiring
Liftt(A ⊕B) = Liftt(A) ⊕Liftt(B) gives the operation
Liftt :
 objects in Rep(St; F)
up to isomorphism

−→
 objects in Rep(ST ; K)
up to isomorphism

Theorem 3.9 along with Proposition 3.10 show that Liftt is well deﬁned.
Example 3.11. (0) Liftt(L(∅)) = Liftt(([0], id0)) = ([0], id0) = L(∅) for all t ∈F.
(1) Notice Liftt(([1], id1)) = ([1], id1) = L(2) ⊕L(∅) in Rep(ST ; K) for all
t ∈F. If t̸ = 0, then ([1], id1) = L(2) ⊕L(∅). Hence (using part (0) and the
additivity of Liftt) we have Liftt(L(2)) = L(2) whenever t̸ = 0. On the other
hand, ([1], id1) ∼= L(2) in Rep(S0; F). Hence Lift0(L(2)) = L(2) ⊕L(∅).
The following proposition lists some useful properties of Liftt.
ON BLOCKS OF DELIGNE’S CATEGORY Rep(St).
17
Proposition 3.12. For this proposition suppose A and B are objects in Rep(St; F).
(1) Liftt(A ⊗B) = Liftt(A) ⊗Liftt(B) for all t ∈F.
(2) (dimRep(ST ;K) Liftt(A))|T =t = dimRep(St;F ) A for all t ∈F.
(3) Suppose t ∈F and λ, λ(1), . . . , λ(m) are Young diagrams with the property
Liftt(L(λ)) = L(λ(1)) ⊕· · · ⊕L(λ(m)) in Rep(ST ; K). Then there exists a unique
j ∈{1, . . . , m} with λ(j) = λ. Moreover, |λ(i)| < |λ| for all i̸ = j. In particular,
Liftt is injective.
(4) Fix a Young diagram λ. Liftt(L(λ)) = L(λ) for all but ﬁnitely many t ∈F.
(5) dimK HomRep(ST ;K)(Liftt(A), Liftt(B)) = dimF HomRep(St;F )(A, B) for all
t ∈F.
Proof. (1) It suﬃces to prove the statement when A and B are objects of the form
A = ([n], e), B = ([n′], e′). Suppose ε, ε′ are lifts of e, e′ respectively. Then ε ⊗ε′ is
a lift of e ⊗e′, hence
Liftt(A ⊗B) = Liftt([n + n′], e ⊗e′) = ([n + n′], ε ⊗ε′) = Liftt(A) ⊗Liftt(B).
(2) Again, we may assume A is of the form A = ([n], e). Let ε denote a lift of e.
Then dimRep(ST ;K) Liftt(A) = tr (ε), and dimRep(St;F ) A = tr (e) = tr (ε)|T =t.
(3) It is easy to show Liftt(L(∅)) = L(∅) for all t ∈F, Liftt(L(2)) = L(2)
for all nonzero t ∈F, and Lift0(L(2)) = L(∅) ⊕L(2). Hence, we can assume
n := |λ| > 1. Suppose e ∈FPn(t) is an idempotent and ε ∈KPn(T) is a lift
of e.
Let ˜e (resp.
˜ε) denote the image of e (resp.
ε) under the quotient map
FPn(t) →FPn(t)/(ζ) ∼= FSn (resp. KPn(T) →KPn(T)/(ζ) ∼= KSn) where ζ
is as in Lemma 3.1. Then ˜ε ∈KSn is a lift of ˜e ∈FSn. However, ˜e (viewed as
an element of KSn) is also a lift of ˜e (viewed as an element of FSn). Thus (by
Theorem A.2) ˜ε is conjugate to ˜e in KSn. Now suppose L(λ) ∼= ([n], e). Then ˜e is
a primitive idempotent in FSn corresponding to λ (see Remark 3.5). Thus ˜e (and
hence ˜ε) is also a primitive idempotent in KSn corresponding to λ. Therefore, any
orthogonal decomposition of ε into primitive idempotents must contain exactly one
primitive idempotent corresponding to λ and all other idempotents corresponding
to Young diagrams with smaller size than λ (see Remark 3.5). The result follows.
(4) Set K′ := F(T) (ﬁeld of fractions of the polynomial ring F[T]) viewed as a
subﬁeld of K. Now suppose ε ∈K′Pn(T) is a primitive idempotent corresponding
to λ.
Then by Proposition 3.8, ε is also primitive when viewed as an element
of KPn(T).
Now write ε = P
π∈Pn,n aππ where aπ ∈K′.
Let Q ⊂F denote
the ﬁnite set consisting of all roots of all denominators of the aπ’s. If t̸ ∈Q, then
aπ ∈F[[T −t]] for all π ∈Pn,n. Thus, if t̸ ∈Q then ε is a lift of e := ε|T =t ∈FPn(t).
It is easy to show that e is primitive in FPn(t). Hence ([n], e) ∼= L(µ) for some
Young diagram µ (see Theorem 3.7). Thus Liftt(L(µ)) = L(λ) for all t̸ ∈Q. By
part (3) we have µ = λ and we are done.
(5) Set A = ([n], e1), B = ([n′], e′
1), e2 = 1 −e1 ∈FPn(t), e′
2 = 1 −e′
1 ∈FPn′(t),
and suppose εi ∈KPn(T) (resp. ε′
i ∈KPn′(T)) is a lift of ei (resp. e′
i) for i ∈{1, 2}.
Then
(3.4)
dimK ε′
iKPn,n′εj ≥dimF e′
iFPn,n′ej
for all i, j ∈{1, 2} since evaluating T = t certainly cannot increase dimension. On
the other hand,
KPn,n′ =
M
1≤i,j≤2
ε′
iKPn,n′εj
and
FPn,n′ =
M
1≤i,j≤2
e′
iFPn,n′ej.
18
JONATHAN COMES AND VICTOR OSTRIK
Comparing dimensions we get
|Pn,n′| =
X
1≤i,j≤2
dimK ε′
iKPn,n′εj ≥
X
1≤i,j≤2
dimF e′
iFPn,n′ej = |Pn,n′|.
Hence equality must hold in (3.4) for all i, j ∈{1, 2}. In particular, equality holds
in (3.4) when i = j = 1 which gives the desired statement.
□
