---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-007-35-dimensions
section_title: "Dimensions"
section_number: 3.5
pages: 21-23
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Re p(St)."
---
dimension of indecomposable objects in Re p(ST ;K). Let us start by deﬁning the
hook length formula.
Deﬁnition 3.26. The hook length of a ﬁxed box in a Young diagram λ is the
number of boxes in λ which are either directly below or directly to the right of
the ﬁxed box, counting the ﬁxed box itself once. Given a Young diagram λ let Pλ
denote the unique polynomial such that
Pλ(d) = d!∏(hook lengths of λ(d))
for every integer d≥ 2|λ|.
Example 3.27. Let λ =
 and suppose d≥ 10 is an integer. In the following
picture each box of λ(d) is labeled by its hook length.
¶Deligne assumesd≥ 2|λ| in [Del07, Proposition 6.4]. If that assumption is removed, Deligne’s
proof will show Proposition 3.25.
22 JONATHAN COMES AND VICTOR OSTRIK
ThusPλ(d) = d!
24(d−3)(d−4)(d−6)(d−8)! = 1
24d(d− 1)(d− 2)(d− 5)(d− 7). 2
First, we show how Pλ is related to the indecomposable object in Re p(ST ;K)
corresponding to λ.
Proposition 3.28. dimRep(ST ;K)L(λ) =Pλ(T ) for any Young diagram λ.
Proof. Fix a Young diagram λ. Let K′ = F (T ) and suppose ε∈ K′P|λ|(T ) is a
primitive idempotent with L(λ) = ([|λ|],ε ) in Re p(ST ;K′). Applying Proposition
3.8 to the ﬁeld extension K′⊂K showsL(λ) = ([|λ|],ε ) in Rep(ST ;K) too. Thus
dimRep(ST ;K)L(λ) = tr (ε) is a rational function in T . Now, by Proposition 3.12(4)
and Proposition 3.25 we can ﬁnd an integer N so that Lift d(L(λ)) = L(λ) and
F : Rep(Sd;F )→ Rep(Sd;F ) hasF(L(λ)) = Lλ(d) for all integers d > N. Hence,
if d>N is an integer, we have
Pλ(d) = dimRep(Sd;F )Lλ(d) (see e.g. [FH91, 4.12])
= dimRep(Sd;F )L(λ) (since tensor functors preserve dimension)
= (dimRep(ST ;K)L(λ))|T =d (by Proposition 3.12(2))
Hence, dim Rep(ST ;K)L(λ) (a rational function in T ) agrees with Pλ(T ) (a polyno-
mial in T ) for inﬁnitely many values of T . Hence they must always agree. □
Next, we wish to determine the roots of Pλ. The following combinatorics will be
useful toward that endeavor.
Deﬁnition 3.29. Given a Young diagram λ and an integer d≥ 2|λ|, create the
(λ,d ) grid marking as follows: Start with a grid of (|λ| + 1)× (d−|λ|) black boxes.
Place the Young diagram λ(d) (with white boxes) atop the grid so that the upper
left corner of λ(d) is atop the upper left corner of the grid. Now place the numbers
0,...,d − 1 into the boxes of the grid using the following rules:
• Begin by placing the number 0 in the lower left box of the grid.
• If the number i is in a black box, place i + 1 into the box directly above i.
• If the number i is in a white box, place i + 1 into the box directly to the
right of i.
Label the rows of the grid 0 ,..., |λ| (from top to bottom) and the columns of the
grid 1,...,d −|λ| (from left to right).
Example 3.30. Set λ = (4, 3, 1, 1, 0,... ) and d = 25. Below is the λ-marking of
the 10× 16 grid.
2
ON BLOCKS OF DELIGNE’S CATEGORY Re p(St). 23
The following proposition records the properties of the (λ,d ) grid marking which
will be useful for determining the roots of Pλ.
Proposition 3.31. The (λ,d ) grid marking has the following properties:
(1) If
 appears in the ith row, then k =|λ| +λi−i.
(2) If
 appears in the ith column, then d−k is the hook length of the row 0,
columni box in λ(d).
Proof. (1) If
 appears in the ith row, then
 must be in column µi + 1. Hence
k is the number of up/right moves it takes to get from the lower left corner to the
upper right corner in a (|λ|− i)× (λi + 1) grid. The result follows.
(2) Let ci denote the number of boxes in the ith column of λ. Notice there are
ci boxes below, andd−|λ|−i boxes to the right of the row 0, column i box inλ(d).
Hence the hook length of that box is d−|λ|− i +ci + 1. On the other hand, if
appears in the ith column, then
 must be in row ci. Hence k is the number of
up/right moves it takes to get from the lower left corner to the upper right corner
in a (|λ|− ci)×i grid. Thus k =|λ|− ci +i− 1. □
Using Proposition 3.31, we can determine all the roots of the polynomial Pλ.
Proposition 3.32. Pλ is a degree |λ| polynomial with |λ| distinct, integer roots
given by|λ| +λi−i for each i = 1,..., |λ|.
Proof. Suppose d is an integer with d >2|λ|. It follows from Deﬁnition 3.26 that
the roots of Pλ are exactly the integers 0 ≤ k < dsuch that d−k is not a hook
length of a box in the top row of λ(d). By Proposition 3.31(2), those are exactly
the values of k for which
 appears in the ( λ,d ) grid marking. The result now
follows from Proposition 3.31(1). □
