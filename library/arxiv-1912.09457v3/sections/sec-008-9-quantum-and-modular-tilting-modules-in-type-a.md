---
doc_id: arxiv-1912.09457v3
doc_title: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS"
section_id: sec-008-9-quantum-and-modular-tilting-modules-in-type-a
section_title: "Quantum and modular tilting modules in type A"
section_number: 9
pages: 27-34
source_pdf: 1912.09457v3.pdf
source_sha256: c00b3801060fc3cc
doc_brief: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS — We introduce a generalization of the notion of a negligible morphism and study the associated tensor ideals and thick id eals."
---
ForUq(sln) two-sided cells of the aﬃne Weyl group are parametrized by
Young diagrams λ of size n. We show that the thick ideal I(F0(λ)) agrees
with the thick ideal attached to the two-sided cell by work of Shi and Ostrik.
This also connects the nullity with the values of Lusztig’s a-function. We
propose a geometric description of the thick ideals for Uq(sln) and for SL(n).
We assume throughout that ℓ and p are bigger than the Coxeter number h,
which is equal to n in our case.
9.1. Description of I(F )s. We would like to get an elementary geometric
description of the region in which the dominant integral wei ghts λ lie for
which T (λ) is in I(F ), for a given minimal facet. For rank 2 these can
be found in [ L]. It turns out that the regions corresponding to cells in the
dominant Weyl chamber given by Lusztig coincide with the reg ions described
in Proposition 8.8. We expect that the regions described in Proposition 8.8
would also describe cells beyond rank 2. We will illustrate t his below for
some cases.
28 THORSTEN HEIDERSDORF AND HANS WENZL
The cells for the aﬃne Weyl groups of type A have been determined by
Shi in [ Shi]. Using Ostrik’s results, this implies that the thick ideal s in type
An−1 are labeled by the partitions λ of the set {1, 2, ..., n}. As usual,
we write partitions λ = [λ1,λ 2, ... λr] where the λi are integers satisfying
λ1 ≥ λ2 ≥ ... λr > 0. We identify them with Young diagrams, where λi
indicates the number of boxes in the i-th row. We denote weights of sln by
the projections of n-tuples of integers into the plane of Rn given by vectors
whose coordinate sum is equal to 0. We will usually only write the n-tuple
of integers for simplicity of notation. We will also use the n otation ⃗l for
λ +ρ.
Deﬁnition 9.1. Letℓ be a positive integer, ℓ>n , and let s be the number
of columns of λ. Then we write the expression ( i − 1)ℓ +xj−1 into the
box of λ in the i-th row and j-th column, where we have the convention
0 = x0 < x1 < ... < xs−1 < ℓ. The standard facet F0(λ) consists of all
n-tuples whose coordinates consist of all possible arrangem ents of numbers
in the boxes of λ, written in descending order.
Deﬁnition 9.2. We call a facet F strongly minimal if F ′ ⁄< F for any F ′
withW (F ′) ∼
=W (F ). Here all facets are assumed to be in the interior of C.
Deﬁnition 9.3. Let F be a facet. We call α a root of the stabilizer W (F )
if there exists an integer nα such that ( α,x ) = nαℓ for every x ∈ F . We
call a root α positive if (α,x )> 0 for all x ∈F . Finally, we call a collection
R+
F = {αi} of positive roots of W (F ) a set of simple roots of F if every
positive root of W (F ) can be uniquely written as a linear combination of
the αis with nonnegative integer coeﬃcients.
Remark 9.4. The simple roots of W (F ) allow us an easy description of
the region C+(F ): If ( α,y ) = nαℓ for all y ∈F , then C+(F ) consists of all
pointsx ∈ h∗ such that (α,x ) ≥nαℓ for all simple α ∈W (F ). It is tempting
to speculate whether a description of the tensor ideal I(F ) can be given via
the region
D(F ) =
⋃
W (F ′)=W (F )
C+(F ′),
where it would be enough to only consider strongly minimal fa cets F ′ on
the right hand side. We study this question in more detail for typeA in the
following sections.
9.2. More facets. Let y be a point in the interior or lower closure of a
given alcove. The following deﬁnition will be useful for Shi ’s algorithm for
identifying cells which will be used later.
Deﬁnition 9.5. Let y be a point in the interior or lower closure of a given
alcove. We call a subset {yi,i ∈ I} of the coordinates of y a y-chain if
|yi −yj| ≥ ℓ for all i,j ∈I. We call it an ℓ-strict (or just strict) y-chain if
its elements are of the form yi −rℓ for 0 ≤r< |I| − 1.
GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS 2 9
Observe that if y is a point in the standard facet F0(λ), the coordinates of
y can be written as a disjoint union ⋃
j Γ j of strict chains where |Γ j| =λT
j .
Namely Γ j consists of all the coordinates of y which are congruent to xj−1
mod ℓ, where x0 = 0.
There is a more general procedure to produce facets from any s tandard
tableau of shape λ, i.e. for any ﬁlling of the boxes of λ such that the numbers
increase along the rows and down the columns. Let i(r,c ) be the number in
the box in the r-th row and c-th column. Then we deﬁne the facet Ft by
the points y satisfying the equalities
yi(r,c) −yi(r+1,c) =ℓ
for any pair of boxes ( r,c ) and ( r + 1,c ) of our tableau. In general, these
equations may describe a collection of facets. In this case, we pick the lowest
one. It can be obtained by adding the additional inequalitie s yi −yi+1 <ℓ ,
1 ≤i<n . We now say that
(2) F ∼F0(λ)
if F = Ft for some standard tableau of shape λ. We now also deﬁne the
region D(λ) by
(3) D(λ) =
⋃
F ∼F0(λ)
C+(F ).
Remark 9.6. 1. Not every minimal facet is of the form Ft for a standard
tableau. E.g. for sl3 the facet given by y2 −y3 =ℓ andy1−y2<ℓ is minimal,
but can not be deﬁned via a standard tableau t. However, we will see that
any strongly minimal facet can be obtained from a standard ta bleau.
2. If 1 ≤i ≤n, we deﬁne ¯i =n+1−i. If a root α is given byα(y) = yi−yj,
we deﬁne the root ¯α by ¯α(y) = y¯j −y¯i. If F is a facet deﬁned by α(y) = ℓ
for certain roots α, we analogously deﬁne the facet ¯F by the same equalities
replacing each α by ¯α. We leave it to the reader to check that F0(λ) = ¯Ft,
where t is the standard tableau obtained by ﬁlling the boxes of λ row by
row.
9.3. Identifying minimal facets and their cells. Shi has given several
algorithms how to identify the 2-sided cell to which a given a lcove belongs.
We review one of the here, and another one in the next section, following
the presentation in [
Co08], [ Co10].
Given a point y in the interior of the dominant Weyl chamber, deﬁne
a Young diagram µ = µ(y) as follows: µ1 is the maximum of |Γ 1|, for all
possibley-chains Γ 1. Assuming we know µ1 up to µi we then deﬁne µi+1 by
the condition
(4)
i+1∑
j=1
µj = max{
i+1∑
j=1
|Γ j| },
where the Γ js are mutually disjoint y-chains, and the maximum is taken
over all possible collection of i + 1 disjoint y-chains.
30 THORSTEN HEIDERSDORF AND HANS WENZL
Proposition 9.7. If y is a point on a facet F ∼ F0(λ) for the Young
diagramλ, we have µ(y) = λT . Moreover, F0(λ) is a minimal facet.
Proof. Let y be a point on the facet F . Let Γ i be the chain consisting of
all the entries yi which are congruent to i − 1 mod ℓ; by construction it
has λT
i elements. The claim would follow if we can show that for any ot her
collection of mutually disjoint y-chains ˜Γ j we have
i+1∑
j=1
|˜Γ j| ≤
i+1∑
j=1
|Γ j|, for 0 ≤i<n.
Let I(m) be the number of indices k for which mℓ ≤yk < (m + 1)ℓ. Then
obviously the number of such indices in a disjoint union of i chains is less
or equal to the minimum of i and I(m). Summing over all m from 0 to n
shows that the largest possible number we can get is the numbe r of boxes of
λ in its ﬁrst i columns. As by induction assumption µj =λT
j for 1 ≤j ≤i,
it follows that µ(y) = λT .
To prove the second claim, let y be the point on F0(λ) with xj = j − 1.
Observe that any point ˜y ∈W.y ∪C with ˜y ≤y needs to have the same L1
norm, it needs to have the same number of coordinates congrue nti modℓ as
y for each i, and its coordinates need to be positive and strictly decrea sing.
By construction, the coordinates of y are the smallest possible numbers
subject to these constraints. Hence if ˜ y ⁄= y, we could ﬁnd an i such that∑ i
j=1 ˜yj > ∑ i
j=1yj, contradicting ˜y ≤y. □
9.4. Description of D(λ). We now describe a second way how to determine
the two-sided cell to which a given alcove in the dominant Wey l chamber
belongs. It is also due to Shi. Given a point y in the dominant Weyl chamber,
we construct a standard tableau ty as follows: We start with putting the
number 1 into the top-left box. We then add the box with the num ber 2 on
the right if y1 −y2 < ℓ, and we add it below the ﬁrst box if y1 −y2 ≥ ℓ.
Having placed boxes with the numbers 1 until i, we add the box containing
i + 1 at the bottom of the left-most column such that yr −yi+1 ≥ℓ, where
r is the number in the lowest box of that column. Then one can sho w (see
e.g. [
Co08], Section 3.2 and 3.2):
Proposition 9.8. Ify is a dominant integral weight, the procedure above
constructs a standard tableau ty. If λ is the associated Young diagram, and
y is in the lower closure of the alcove A, then A is in the two-sided cell
labeled by λT .
Theorem 9.9. The indecomposable moduleT (ν) is in the ideal I(λ) gen-
erated by the facet F0(λ) if and only if ν +ρ is in the region D(λ) as deﬁned
in 3.
Proof. It follows from Proposition 9.7 that whenever ν +ρ ∈ F with F ∼
F0(λ), then T (ν) ∈ I (λ). Hence T (ν) ∈ I (λ) whenever ν +ρ ∈ D(λ) by
Proposition 8.8. To prove the other inclusion, let T (ν) be an indecomposable
GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS 3 1
tilting module with highest weight ν such thatν +ρ is in an alcove belonging
to the two-sided cell labeled by λT . Then we obtain a tableau ty of shape λ,
where y =ν +ρ. Let i(r,c ) be the number in the box in the r-th row and
c-th column. Then by construction yi(r,c) −yi(r+1,c) ≥ℓ. Deﬁne F as the set
of points x such that xi(r,c) −xi(r+1,c) =ℓ. This is exactly the facet obtained
from ty, see the discussion above 2. Then obviously y ∈C+(F ). □
9.5. Examples. In the following we list the strongly minimal facetsF con-
jugate (as deﬁned in 2) to F0(λ) for sln, n ≤ 5, for each Young diagram λ
with n boxes. We use the convention that 0 < x1 < x2 < ... < ℓ. The
region C+(F ) is then given by all points y satisfying (y,α ) ≥ℓ for all roots
α listed under simple roots. We start with sl3, where all strongly minimal
facets are standard facets:
λ facet nullity simple roots
[3] (x2,x 1, 0) 0 ∅
[2, 1] (ℓ,x 1, 0) 1 ǫ1 −ǫ3
[13] (2ℓ,ℓ, 0) 3 ǫ1 −ǫ2,ǫ 2 −ǫ3
In the following, we list all strongly minimal facets for sl4. Observe that
we also have a strongly minimal facet which is not a standard f acet for the
diagram [2, 12].
λ facet nullity simple roots
[4] (x3,x 2,x 1, 0) 0 ∅
[3, 1] (ℓ,x 2,x 1, 0) 1 ǫ1 −ǫ4
[22] (ℓ +x1,ℓ,x 1, 0) 2 ǫ1 −ǫ3,ǫ 2 −ǫ4
[2, 12] (2ℓ,ℓ,x 1, 0) 3 ǫ1 −ǫ2,ǫ 2 −ǫ4
(2ℓ,ℓ +x1,ℓ, 0) 3 ǫ1 −ǫ3,ǫ 3 −ǫ4
[14] (3ℓ, 2ℓ,ℓ, 0) 6 ǫ1 −ǫ2,ǫ 2 −ǫ3,ǫ 3 −ǫ4
For sl5, we will omit the facets corresponding to [5] (the fundament al alcove),
to [4, 1] (the wall of the fundamental alcove which is not in a reﬂect ion plane
of the ﬁnite Weyl group) and [1 5], which consists of the point (4 ℓ, 3ℓ, 2ℓ,ℓ, 0)
corresponding to the Steinberg module. The remaining facet s then consist
of
λ facet nullity
[3, 2] (ℓ +x1,ℓ,x 2,x 1, 0) 2 ǫ1 −ǫ4,ǫ 2 −ǫ5
[3, 1, 1] (2ℓ,ℓ,x 2,x 1, 0) 3 ǫ1 −ǫ2,ǫ 2 −ǫ5
(2ℓ,ℓ +x1,ℓ,x 2, 0) 3 ǫ1 −ǫ3,ǫ 3 −ǫ5
(2ℓ,ℓ +x2,ℓ +x1,ℓ, 0) 3 ǫ1 −ǫ4,ǫ 4 −ǫ5
[22, 1] (2ℓ,ℓ +x1,ℓ,x 1, 0) 4 ǫ1 −ǫ3,ǫ 3 −ǫ5,ǫ 2 −ǫ4
[2, 13] (3ℓ, 2ℓ,ℓ,x 1, 0) 6 ǫ1 −ǫ2,ǫ 2 −ǫ3,ǫ 3 −ǫ5
(3ℓ, 2ℓ,ℓ +x1,ℓ, 0) 6 ǫ1 −ǫ2,ǫ 2 −ǫ4,ǫ 4 −ǫ5
(3ℓ, 2ℓ +x1, 2ℓ,ℓ, 0) 6 ǫ1 −ǫ3,ǫ 3 −ǫ4,ǫ 4 −ǫ5
32 THORSTEN HEIDERSDORF AND HANS WENZL
9.6. The a-function. Recall from the introduction that Lusztig deﬁned
an integer valued function on two-sided cells. In type A there is an easy
description of the a-function [
EH17, Section 4.2, 5.2]. By [ Shi] the two-
sided cells of the aﬃne Weyl group W are parametrized by partitions of n.
It is well-known that it is suﬃcient (in type A) to compute the value of the
a-function in the ﬁnite case Wn =Sn. By [ EH17]
a(λT ) = r(λ)
where r(λ) is the row number of λ, the sum over the row numbers of the
boxes in the Young diagram where the row number of a box in the i-th row
is i − 1 (note that we use λT for the partition labeled by λ in [ EH17]).
Example 9.10. For n = 8 consider the partition λ = (4, 3, 1). Its row
number is 0 + 0 + 0 + 0 + 1 + 1 + 1 + 2 = 5. Hence the value of thea-function
on the two-sided cell associated to λ is 5.
Theorem 9.11. The thick ideal I(λ) = I(F0(λ)) generated by the tilting
modules T (ν) for which ν +ρ ∈ F0(λ) coincides with the thick ideal con-
structed by Ostrik for the cell in the dominant Weyl chamber c orresponding
to the two-sided cell labeled by the Young diagram λT . In particular, the
nullity of any generating module T (ν) of that ideal is equal to the a-function
of that cell. Moreover, that thick ideal contains all tiltin g modules T (ν) for
which ν +ρ ∈D(λ), as deﬁned below ( 2).
Proof. Let T (ν) be a tilting module for which y =ν +ρ ∈F0(λ). As F0(λ)
is a minimal facet by Proposition 9.7,T (λ) = V (λ). Hence its nullity can be
determined from its dimension, see Corollary 7.5. By construction of F0(λ)
yi is congruent yj modℓ ifyi andyj are in the same column of λ. Hence the
nullity is given by ∑
i
( λT
i −1
2
)
, which is equal to the row number r(λ). This
shows that the nullity of F0(λ) coincides with the a-function.
We have seen in Proposition
9.7 that if y ∈ F with F ∼ F0(λ) then
µ(y) = λT . Hence any module T (ν) with ν +ρ ∈F is also in I(λ). The last
statement now follows from Proposition 8.8. □
Remark 9.12. It was shown by Ostrik for ℓ a large enough prime (see [ O01]
[O98]) that the dimension of any tilting module corresponding to a two-sided
cellA is divisible by ℓa(A) and for any cell there exists a tilting module such
that its dimension is not divisible by ℓa(A)+1. Hence the relationship between
nullity and a-function in Theorem 9.11 would hold whenever one can show
that the nullity of such a module is given by its dimension. So it would
seem reasonable to expect this to be true in general. But see t he example
in Section 7.5.2 where the nullity of a modular tilting module is not given
by its dimension.
Remark 9.13. We were able to give a fairly explicit description of the
tensor ideals thanks to the work of Shi [
Shi]. In the formulation as D(F ),
see Remark 9.4, our approach might also be useful to characterize tensor
GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS 3 3
ideals for other Lie types. E.g. this formulation works for a ll rank 2 cases,
but not for all ideals for type D4, see Remark 8.13.
Remark 9.14. The thick ideal Nk is the sum of the I(λ) (λ partition of n)
for which the nullity is ≥k.
9.7. Regions for the modular case. We can use the results from the
previous subsection also for the modular case; to conform wi th the usual
notations, we replace ℓ by the primep. In addition, we can use the “telescop-
ing eﬀect” in Lemma 8.7 (b) and Proposition 8.8 (b) to construct inﬁnitely
many thick ideals. We will also extend our conjectural descr iption of these
ideals and the related cells to this case. We use the same nota tion as in the
previous subsection. Let F0(λ) be the standard minimal facet associated to
the Young diagram λ, and let r be an integer, r ≥ 1. Then we construct the
region Dr(λ) by D1(λ) = D(λ) and
Dr(λ) =
⋃
F ∼F0(λ)
(
⋃
λ∈F
λ(r) +X +), r> 1
whereλ(r) is as in Lemma 8.7 (andλ is interpreted as a weight), and the ﬁrst
union goes over all strongly minimal facets F which are equivalent to F0(λ).
The following proposition again follows from Lemma 8.7 and Proposition
8.8.
Proposition 9.15. If µ +ρ is in Dr(λ) its nullity is at least equal to
r|R+| +k(F0(λ)).
Question 9.16. Is every thick ideal in type A a sum of ideals of the form
Dr(λ)?
An aﬃrmative answer would give a geometric description of th e right
p-cells in the aﬃne Weyl group.
Remark 9.17. 1. It is easy to see for r ≥ 1 that Dr(∅) = Dr−1([1k]). We
will identify these regions in the following.
2. For type A1 the thick ideals are generated by the Steinberg modules.
It is easy to see that our regions do describe the thick ideals in this case.
An explicit description of the tensor ideals has also been gi ven for type A2,
see section 9.7.1. One checks easily that this is compatible with our regions.
9.7.1. The modular A2-case. By [An04, Example 15] [ Je17, Chapter 10] the
thick ideals are given by the the Steinberg cells <St r >=T (≤cr
1) and the
tilting modules associated to the weight cell
c
r
2 =Yr \ (Yr+1 ∪c
r
1) .
A beautiful picture illustrating the p = 5-case can be found in [
An04] .
In the sl2-case we have < Str >= Nr|R+|, so in order to determine the
k-negligible ideals it suﬃces to ﬁnd one weight λ in each cr
2 such that the
associated tilting module is a Weyl module and compute its nu llity with the
dimension formula. All in all we obtain
34 THORSTEN HEIDERSDORF AND HANS WENZL
(1) The Steinberg ideals with nullity 3 s for s = 0, 1, 2,... and
(2) for s = 0, 1, 2,... the ideals generated by the T (λ) with
(λ +ρ,ρ ) = ps+1, (λ +ρ,α 1) = rps, 1 ≤r<p
of nullity 3s + 1.
