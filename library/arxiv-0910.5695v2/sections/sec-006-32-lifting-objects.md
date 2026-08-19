---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-006-32-lifting-objects
section_title: "Lifting objects"
section_number: 3.2
pages: 15-21
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Re p(St)."
---
is an indeterminate. In this section we use the process of lifting idempotents (see
appendix A) to lift objects in Re p(St;F ) to objects in Re p(ST ;K). We then prove
some useful properties of these lifted objects. In the next section we will show
that Rep(ST ;K) is semisimple (see Corollary 3.17), and hence uncomplicated from
16 JONATHAN COMES AND VICTOR OSTRIK
our point of view. The process of lifting objects developed in this section will be
used later in the paper to compare the structure of Re p(St;F ) with that of the
semisimple category Rep(ST ;K). The following theorem will be used to deﬁne the
notion of lifting objects.
Theorem 3.9. Supposee is an idempotent inFPn(t). Then there exists an idempo-
tentε∈KPn(T ) of the form ε =∑
π∈Pn,naππ withaπ∈F [[T−t]] for all π∈Pn,n
such that ε|T =t = e (we say ε is a lift of e). Moreover, if ([n1],e 1) and ([n2],e 2)
are isomorphic objects in Rep(St;F ) and ε1,ε 2 are lifts of e1,e 2 respectively, then
([n1],ε 1) and ([n2],ε 2) are isomorphic in Rep(ST ;K).
Proof. The existence of a lift of e is guaranteed by the ﬁrst statement of Theorem
A.2. Now suppose ([ n1],e 1)∼= ([n2],e 2) in Re p(St;F ). To prove the remainder of
the theorem we may assume n1≤ n2. If n1 = 0 the theorem is easy to check, so
assume n1 > 0. Set
φ :=
{ idn1 if n1 =n2
φn2··· φn1+1 if n1 <n 2
and φ′ :=
{ idn1 if n1 =n2
φ′
n1+1··· φ′
n2 if n1 <n 2
where φn and φ′
n are as in the proof of Lemma 3.6. Then ([ n1],e 1)∼= ([n2],φe 1φ′)
andφε1φ′ is a lift ofφe1φ′. Hence it suﬃces to show the theorem is true when n1 =
n2. In this case the remainder of the theorem follows from the second statement of
Theorem A.2 along with Proposition 2.20(2). □
Lifted idempotents satisfy the following property.
Proposition 3.10. If ([n],e )∼= ([n1],e 1)⊕ ([n2],e 2) in Rep(St;F ) andε,ε 1,ε 2 are
lifts of e,e 1,e 2 respectively, then ([n],ε )∼= ([n1],ε 1)⊕ ([n2],ε 2) in Rep(ST ;K).
Proof. By the Krull-Schmidt property there exist ¯e1, ¯e2∈FPn(t) with the property
([ni],ei)∼= ([n], ¯ei) fori = 1, 2 such thate = ¯e1 + ¯e2 is an orthogonal decomposition
of the idempotente. Let ¯ε1, ¯ε2∈KPn(T ) be lifts of ¯e1, ¯e2 respectively. Then ¯ε1+ ¯ε2
is a lift ofe. Hence, by Theorem A.2 and Proposition 2.20(2) ([n],ε )∼= ([n], ¯ε1 + ¯ε2)
in Rep(ST ;K). Since ¯ε1 and ¯ε2 are orthogonal idempotents (see Theorem A.2) we
have ([n], ¯ε1 + ¯ε2)∼= ([n], ¯ε1)⊕ ([n], ¯ε2) in Rep(ST ;K). The result now follows from
the last statement of Theorem 3.9. □
By Proposition 2.20(2) any object in Re p(St;F ) is a ﬁnite direct sum of objects
of the form ([ n],e ). Hence, setting Lift t([n],e ) := ([ n],ε ), where ε ∈ KPn(T )
is a lift of e ∈ FPn(t) and extending to all objects in Re p(St;F ) by requiring
Liftt(A⊕B) = Liftt(A)⊕ Liftt(B) gives the operation
Liftt :
{ objects in Re p(St;F )
up to isomorphism
}
−→
{ objects in Re p(ST ;K)
up to isomorphism
}
Theorem 3.9 along with Proposition 3.10 show that Lift t is well deﬁned.
Example 3.11. (0) Liftt(L(∅)) = Liftt(([0], id0)) = ([0], id0) =L(∅) for all t∈F .
(1) Notice Lift t(([1], id1)) = ([1] , id1) = L(2)⊕ L(∅) in Re p(ST ;K) for all
t∈ F . If t⁄= 0, then ([1] , id1) = L(2)⊕L(∅). Hence (using part (0) and the
additivity of Lift t) we have Lift t(L(2)) = L(2) whenever t⁄= 0. On the other
hand, ([1], id1)∼=L(2) in Rep(S0;F ). Hence Lift 0(L(2)) =L(2)⊕L(∅).
The following proposition lists some useful properties of Lift t.
ON BLOCKS OF DELIGNE’S CATEGORY Re p(St). 17
Proposition 3.12. For this proposition supposeA andB are objects in Rep(St;F ).
(1) Liftt(A⊗B) = Liftt(A)⊗ Liftt(B) for all t∈F .
(2) (dimRep(ST ;K) Liftt(A))|T =t = dimRep(St;F )A for all t∈F .
(3) Suppose t∈ F and λ,λ (1),...,λ (m) are Young diagrams with the property
Liftt(L(λ)) = L(λ(1))⊕···⊕ L(λ(m)) in Rep(ST ;K). Then there exists a unique
j∈{ 1,...,m } with λ(j) = λ. Moreover, |λ(i)| <|λ| for all i⁄= j. In particular,
Liftt is injective.
(4) Fix a Young diagram λ. Liftt(L(λ)) =L(λ) for all but ﬁnitely many t∈F .
(5) dimK HomRep(ST ;K)(Liftt(A), Liftt(B)) = dim F HomRep(St;F )(A,B ) for all
t∈F .
Proof. (1) It suﬃces to prove the statement when A andB are objects of the form
A = ([n],e ),B = ([n′],e′). Suppose ε,ε′ are lifts of e,e′ respectively. Then ε⊗ε′ is
a lift of e⊗e′, hence
Liftt(A⊗B) = Liftt([n +n′],e⊗e′) = ([n +n′],ε⊗ε′) = Liftt(A)⊗ Liftt(B).
(2) Again, we may assume A is of the form A = ([n],e ). Let ε denote a lift of e.
Then dimRep(ST ;K) Liftt(A) = tr (ε), and dim Rep(St;F )A = tr (e) = tr (ε)|T =t.
(3) It is easy to show Lift t(L(∅)) = L(∅) for all t∈ F , Liftt(L(2)) = L(2)
for all nonzero t∈ F , and Lift 0(L(2)) = L(∅)⊕L(2). Hence, we can assume
n :=|λ| > 1. Suppose e∈ FPn(t) is an idempotent and ε∈ KPn(T ) is a lift
of e. Let ˜e (resp. ˜ε) denote the image of e (resp. ε) under the quotient map
FPn(t)→ FPn(t)/(ζ)∼= FSn (resp. KPn(T )→ KPn(T )/(ζ)∼= KSn) where ζ
is as in Lemma 3.1. Then ˜ ε∈ KSn is a lift of ˜e∈ FSn. However, ˜e (viewed as
an element of KSn) is also a lift of ˜e (viewed as an element of FSn). Thus (by
Theorem A.2) ˜ε is conjugate to ˜e in KSn. Now suppose L(λ)∼= ([n],e ). Then ˜e is
a primitive idempotent in FSn corresponding to λ (see Remark 3.5). Thus ˜e (and
hence ˜ε) is also a primitive idempotent in KSn corresponding to λ. Therefore, any
orthogonal decomposition of ε into primitive idempotents must contain exactly one
primitive idempotent corresponding to λ and all other idempotents corresponding
to Young diagrams with smaller size than λ (see Remark 3.5). The result follows.
(4) Set K′ :=F (T ) (ﬁeld of fractions of the polynomial ring F [T ]) viewed as a
subﬁeld of K. Now suppose ε∈K′Pn(T ) is a primitive idempotent corresponding
to λ. Then by Proposition 3.8, ε is also primitive when viewed as an element
of KPn(T ). Now write ε = ∑
π∈Pn,naππ where aπ ∈ K′. Let Q⊂ F denote
the ﬁnite set consisting of all roots of all denominators of the aπ’s. If t⁄∈Q, then
aπ∈F [[T−t]] for allπ∈Pn,n. Thus, if t⁄∈Q thenε is a lift ofe :=ε|T =t∈FPn(t).
It is easy to show that e is primitive in FPn(t). Hence ([ n],e )∼= L(µ) for some
Young diagram µ (see Theorem 3.7). Thus Lift t(L(µ)) = L(λ) for all t⁄∈ Q. By
part (3) we have µ =λ and we are done.
(5) SetA = ([n],e 1),B = ([n′],e′
1),e2 = 1−e1∈FPn(t),e′
2 = 1−e′
1∈FPn′(t),
and supposeεi∈KPn(T ) (resp. ε′
i∈KPn′(T )) is a lift ofei (resp. e′
i) fori∈{ 1, 2}.
Then
(3.4) dim Kε′
iKPn,n′εj≥ dimFe′
iFPn,n′ej
for all i,j ∈{ 1, 2} since evaluating T =t certainly cannot increase dimension. On
the other hand,
KPn,n′ =
⨁
1≤i,j≤2
ε′
iKPn,n′εj and FPn,n′ =
⨁
1≤i,j≤2
e′
iFPn,n′ej.
18 JONATHAN COMES AND VICTOR OSTRIK
Comparing dimensions we get
|Pn,n′| =
∑
1≤i,j≤2
dimKε′
iKPn,n′εj≥
∑
1≤i,j≤2
dimFe′
iFPn,n′ej =|Pn,n′|.
Hence equality must hold in (3.4) for all i,j ∈{ 1, 2}. In particular, equality holds
in (3.4) when i =j = 1 which gives the desired statement. □
3.3. On Rep(St;F ) for generic t. In this section we will show that Re p(St;F )
is semisimple for “generic” values of t. Deligne showed that Re p(St;F ) is not
semisimple if and only if t is a nonnegative integer (see [Del07]). That result will
follow from our description of the blocks in Re p(St;F ) (see Corollary 5.23). For
now we conﬁne ourselves to prove a weaker result (see Theorem 3.15) which allows
us to conclude that Re p(ST ;K) is semisimple (see Corollary 3.17).
The following well-known lemma will be useful in showing that Re p(St;F ) is
generically semisimple.
Lemma 3.13. Suppose A is a ﬁnite dimensional F -algebra. For a∈ A, let φa
denote the F -linear map A→A given by x↦→ax. Deﬁne the trace form on A by
(a,b ) := tr (φaφb). Then A is a semisimple algebra if and only if the trace form on
A is non-degenerate.
Proof. Let S :={a∈ A| (a,b ) = 0 for all b∈ A}. We will show that S is equal
to J(A) (the Jacobson radical of A). Suppose a∈J(A). Since J(A) is a nilpotent
ideal,ab is nilpotent for everyb∈A. Hence (a,b ) = 0 for allb∈A, soJ(A)⊂S. To
showS⊂J(A) it suﬃces to show that every element ofS is nilpotent. If a∈S then
tr (φn
a) = 0 for all integers n> 0. If we let x1,...,x r∈F denote the eigenvalues of
φa, then we have ∑r
i=1xn
i = 0 for all n >0. Hence, any non-constant symmetric
polynomial in x1,...,x r is zero (see for example [Mac95]). Thus the characteristic
polynomial of φa must be χ(X) =Xr. Therefore φa, and thus a, is nilpotent. □
Before showing Rep(St;F ) is generically semisimple we give two examples illus-
trating the usefulness of Lemma 3.13. The reader may ﬁnd these examples helpful
when reading the proof of Theorem 3.15.
Example 3.14. (1) Consider the partition algebra FP 1(t). Let π be as in the
proof of Theorem 3.4 and ﬁx the ordered basis P1,1 ={id1,π} for FP 1(t). Under
this ordered basis the matrix with entries ( x,y ) for x,y∈P1,1 is
( 2 t
t t 2
)
Since the determinant of the matrix above is t2, we conclude (by Lemma 3.13) that
FP 1(t) is semisimple if and only if t⁄= 0.
(2) Consider the partition algebra FP 2(t). Using the ordered basis
ON BLOCKS OF DELIGNE’S CATEGORY Re p(St). 19
the matrix with entries (π,µ ) for π,µ∈P2,2 is


2t4 2t3 2t3 2t3 2t3 2t3 2t3 2t2 2t2 2t2 2t2 2t2 2t2 2t2 2t
2t3 5t2 2t2 2t2 2t2 2t2 2t2 5t 2t 2t 2t 5t 5t 2t 5
2t3 2t2 5t2 2t2 2t2 2t2 2t2 5t 2t 2t 5t 2t 2t 5t 5
2t3 2t2 2t2 2t2 2t3 2t2 2t2 2t 2t2 2t 2t2 2t2 2t 2t 2t
2t3 2t2 2t2 2t3 2t2 2t2 2t2 2t 2t2 2t 2t 2t 2t2 2t2 2t
2t3 2t2 2t2 2t2 2t2 2t2 5t2 2t 2t 5t 5t 2t 5t 2t 5
2t3 2t2 2t2 2t2 2t2 5t2 2t2 2t 2t 5t 2t 5t 2t 5t 5
2t2 5t 5t 2t 2t 2t 2t 15 2 t 7 5 5 5 5 5
2t2 2t 2t 2t2 2t2 2t 2t 2t 2t2 2t 2t 2t 2t 2t 2t
2t2 2t 2t 2t 2t 5t 5t 7 2 t 15 5 5 5 5 5
2t2 2t 5t 2t2 2t 5t 2t 5 2 t 5 5 5 2 t 5t 5
2t2 5t 2t 2t2 2t 2t 5t 5 2 t 5 5 5 5 t 2t 5
2t2 5t 2t 2t 2t2 5t 2t 5 2 t 5 2 t 5t 5 5 5
2t2 2t 5t 2t 2t2 2t 5t 5 2 t 5 5 t 2t 5 5 5
2t 5 5 2 t 2t 5 5 5 2 t 5 5 5 5 5 5


The determinant of the matrix above is 1259712t14(t−1)4(t−2)6. Hence, by Lemma
3.13, FP 2(t) is semisimple if and only if t⁄= 0, 1, 2. 2
Now to prove that Re p(St;F ) is generically semisimple.
Theorem 3.15. Rep(St;F ) is semisimple for all but countably many values of t.
Moreover, if Rep(St;F ) is not semisimple, then t is an algebraic integer.
Proof. We may assume t⁄= 0. Suppose L1 and L2 are two indecomposable objects
in Rep(St;F ). By Proposition 2.20(2) along with Lemma 3.6(1)(2) we can ﬁnd a
nonnegative integer n and idempotents e1,e 2∈ FPn(t) so that L1∼= ([n],e 1) and
L2 ∼= ([n],e 2). Whence Hom Rep(St;F )(L1,L 2) = e2FPn(t)e1. Thus, in order to
show Hom Rep(St;F )(L1,L 2) is either zero or a ﬁnite dimensional division algebra
over F , it suﬃces to show FPn(t) is a semisimple algebra. Therefore, for a ﬁxed
t∈F , Rep(St;F ) is semisimple whenever FPn(t) are semisimple for all n≥ 0.
Let Mn(t) denote the matrix whose rows and columns are labelled by the ele-
ments of Pn,n (in some ﬁxed order) with the x,y -entry equal to ( x,y ) (the trace
form on FPn(t), see Lemma 3.13). Then the entries of Mn(t) are in Z[t]. Hence
detMn(t)∈ Z[t]. It follows from Lemma 3.13 that FPn(t) is semisimple if and
only if detMn(t)⁄= 0. However, from Theorem 2.6, we know that FPn(d) is semi-
simple for integers d≥ 2n. Hence, det Mn(t) is a polynomial in t which is not
identically zero. Thus, for each n≥ 0 there are only ﬁnitely many values of t for
which detMn(t) = 0. Therefore there are only countably many values oft for which
FPn(t) is not semisimple for all n≥ 0. □
Remark 3.16. Ift∈F is not an algebraic integer, then by Theorem 3.15 we know
Rep(St;F ) is semisimple. However, given an arbitrary t∈F , neither Theorem 3.15
nor its proof allow us to determine if Re p(St;F ) is semisimple. As mentioned at
the beginning of this section, we will eventually show that Rep(St;F ) is semisimple
if and only if t is not a nonnegative integer.
We close this section with one ﬁnal observation.
Corollary 3.17. Rep(ST ;K) is semisimple.
Proof. This follows from Theorem 3.15 as T is not an algebraic integer. □
3.4. The interpolation functor Rep(Sd;F )→ Rep(Sd;F ). Throughout this sec-
tion we assumed is a nonnegative integer. In this section we will describe following
[Del07,§6] how Rep(Sd;F ) “interpolates” the category Rep(Sd;F ). More precisely,
20 JONATHAN COMES AND VICTOR OSTRIK
we will show Rep(Sd;F ) is equivalent to the quotient of Rep(St;F ) by the so-called
“negligible morphisms.” To start, let us deﬁne the interpolation functor.
Deﬁnition 3.18.F : Rep(Sd;F )→ Rep(Sd;F ) is the functor deﬁned on indecom-
posable objects byF([n],e ) =f(e)(V⊗n
d ), and on morphisms α : ([n],e )→ ([n′],e′)
byF(α) =f(α). Here f and Vd are as in section 2.1.
Notice thatF is clearly a tensor functor. From the discussion in section 2.1 we
have the following.
Proposition 3.19. F is surjective on objects and morphisms.
Proof. This follows from Proposition 2.1 and Theorem 2.6(1). □
However, by Theorem 2.6(2) we know thatF does not induce an equivalence of
categories. To illustrate the amount by which F fails to induce an equivalence of
categories we need the following deﬁnition.
Deﬁnition 3.20. A morphism f :X→Y in a tensor category is called negligible
if tr (fg ) = 0 for all g :Y →X. Set N (X,Y ) :={f :X→Y | f is negligible}.
Example 3.21. (1) The only morphisms in Re p0(S0;F ) which are not negligible
are nonzero scalar multiples of id 0 (see Example 2.22(1)).
(2) Let π : [1] → [1] be as in the proof of Theorem 3.4. Then xπ : [1] → [1],
deﬁned by equation (2.1), is given by xπ =π− id1. Since tr (π) = t = tr (id1), we
have tr (xπ) = 0. Moreover, xππ = (t−1)π so that tr (xππ) =t(t−1). We conclude
that xπ is negligible if and only if t = 0, 1.
(3) Consider the morphism π∈ HomRep0(St;F )([1], [2]) given by
From equation (2.1) we get xπ =π−µ1−µ2−µ3 + 2µ4 where
If we set
then one can compute tr (xπν0) =t(t− 1)(t− 2), and tr (xπνi) = 0 for i = 1, 2, 3, 4.
Thusxπ is negligible if and only if t = 0, 1, 2. 2
Remark 3.22. Each of the examples 3.21 follow from the following fact: In
Rep0(St;F )
N ([n], [m]) =
{ SpanF{xπ| π∈Pn,m has more than t parts}, if t∈Z≥0
0, otherwise.
ON BLOCKS OF DELIGNE’S CATEGORY Re p(St). 21
Fort∈ Z≥0 this fact follows from Theorem 2.6(2), Remark 2.17, along with the
following Proposition 3.23(2). For t⁄∈Z≥0 we will eventually show that the larger
category Rep(St;F ) is semisimple (see Corollary 5.23). It is well-known that there
are no nonzero negligible morphisms in a semisimple category.
Proposition 3.23. The following statements hold in any tensor category.
(1)N is a tensor ideal.
(2) The image under a full tensor functor of a morphism f is negligible if and
only if f is negligible.
Proof. Suppose f : A→ B, g : B→ A, and h : B⊗C→ A⊗C are morphisms
in a tensor category. Observe that tr ( f◦g) = tr (g◦f). Moreover, one can show
tr ((f⊗ idC)◦h) = tr (f◦ (idA⊗evC)◦ (h⊗ idC)◦ (idB⊗coevC)). Statement
(1) follows. Statement (2) follows from the fact that a tensor functor preserves the
trace of a morphism. □
Since there are no nonzero negligible morphisms in Rep( Sd;F ), by Proposition
3.23(2) we conclude the functor F : Rep(Sd;F )→ Rep(Sd;F ) sends all negligible
morphisms to zero. Thus F induces a functorF : Rep(Sd;F )/N→ Rep(Sd;F ).
Theorem 3.24.F induces an equivalence of categoriesRep(Sd;F )/N∼= Rep(Sd;F ).
Proof. This follows from Proposition 3.19 and Proposition 3.23(2). □
We ﬁnish this section with the following proposition concerning the functor F.
For proof of the proposition we refer the reader to [Del07, Proposition 6.4] ¶.
Proposition 3.25. Suppose d is a nonnegative integer and λ = (λ1,λ 2,... ) is a
Young diagram. If d−|λ|≥ λ1, then F(L(λ)) = Lλ(d). If d−|λ| < λ1, then
F(L(λ)) = 0.
