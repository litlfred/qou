---
doc_id: arxiv-math-0605242v1
doc_title: "N-Fold Integer Programming Jesús A. De Loera∗ Raymond Hemmecke † Shmuel Onn ‡ Robert Weismantel §"
section_id: sec-003-some-packing-problems
section_title: "Some packing problems"
section_number: null
pages: 6-8
source_pdf: 0605242v1.pdf
source_sha256: 65fac7285e4a77f4
doc_brief: "N-Fold Integer Programming Jesús A. De Loera∗ Raymond Hemmecke † Shmuel Onn ‡ Robert Weismantel § — In this article we study a broad class of integer programming problem s in variable dimension."
---
Minimum cost shipment
The minimum cost shipment problem concerns the shipment of a large stock of items of several types,
using various vessels, with minimum possible cost. More pre cisely, the data is as follows. There are t
types of items. The weight of each item of type j is wj and there are nj items of type j to be shipped.
There are v available vessels, where vessel k has maximum weight capacity uk. The cost of shipping
one item of type j on vessel k is pj,k. We now formulate this as an n-fold integer programming prob lem.
We set n := v, p := 1, q := t + 1. The deﬁning matrix is the row vector A = (Aj) := ( w1, w 2, . . . , w t, 1).
The variables vector is x = (x1, . . . , x n) with xk = (xk
1, . . . , x k
t , x k
q ), where xk
j represents the number of
items of type j to be shipped on vessel k for j = 1, . . . , t , and xk
q is an extra slack variable representing
the unused weight capacity in vessel k. The cost vector is c = ( c1, . . . , c n) with ck = ( ck
1, . . . , c k
t , c k
q ),
where ck
j := pj,k for j = 1 , . . . , t , and ck
q := 0. Finally, the demand vector is b = ( b0, b 1, . . . , b n)
with bk := uk for k = 1, . . . , n , and b0 := (n1, . . . , n t, ∑ v
k=1 uk − ∑ t
j=1 njwj). Then the resulting n-fold
integer programming problem, min {cx : A(n)x = b, x ∈ Nnq}, can be written in scalar form as follows:
min
q∑
j=1
n∑
k=1
ck
j xk
j =
t∑
j=1
v∑
k=1
pj,kxk
j
s.t.
n∑
k=1
xk
j = b0
j = nj , j = 1, . . . , t
n∑
k=1
xk
q = b0
q =
v∑
k=1
uk −
t∑
j=1
njwj
q∑
j=1
Aj xk
j =
t∑
j=1
wj xk
j + xk
q = bk = uk , k = 1, . . . , n
xk
j ∈ N , j = 1, . . . , q , k = 1, . . . , n .
6
Assume that the number t of types is ﬁxed, but the numbers nj of items of each type may be very
large: this is a reasonable assumption in applications (for instance, several types of automobiles to be
shipped overseas, or several types of appliances to be shipp ed on ground). Then we obtain the following
striking corollary of Theorem 1.1, showing that the problem is polynomial time solvable, where the
input size is v plus the bit size of the integer numbers nj, u k, p j,k constituting the data. Note that this
result is much stronger than the standard results on the pseudo-polynomial time solvability of this
kind of packing and knapsack-type problems using dynamic pr ogramming: our algorithm can handle
very large nj and uk, possibly exponential in the dimensional parameter v.
Corollary 2.5 For any ﬁxed number t of types and type weights wj, the minimum cost shipment
problem is solvable in time which is polynomial in the number v of vessels and in the bit size of the
integer numbers nj of items of each type to be shipped, vessel capacities uk, and shipment costs pj,k.
The cutting stock problem
This is a classical manufacturing problem, where the usual s etup is as follows: a manufacturer supplies
rolls of material (such as scotch-tape or band-aid) in one of t diﬀerent widths w1, . . . , w t. The rolls are
all cut out from standard rolls of common large width u, coming out of the production line. Given
orders by customers for nj rolls of width wj, the problem facing the manufacturer is to meet the
orders using the smallest possible number of standard rolls . This is almost a direct special case of
the minimum cost shipment problem discussed above, with suﬃ ciently many identical vessels, say
v := ∑ t
j=1⌈nj/ ⌊u/w j ⌋⌉, of capacity uk := u each, playing the role of the standard rolls, and with cost
pj,k := wj for each roll of width wj regardless of the standard roll from which it is being cut out . The
only correction needed is that each slack variable xk
q = xk
t+1, measuring the unused width of the kth
standard roll, has cost of one unit instead of zero, so that th e total cost becomes the number of standard
rolls used. Thus the formulation as an n-fold program is with n := ∑ t
j=1⌈nj/ ⌊u/w j ⌋⌉, p := 1, q := t+1,
A := ( w1, w 2, . . . , w t, 1), variables xk
j representing the number of rolls of width wj cut out of the kth
roll for j = 1, . . . , t and xk
q representing the unused width of the kth standard roll, costs ck
j := wj for
j = 1, . . . , t and ck
q := 1, and demands bk := u for k = 1, . . . , n and b0 := (n1, . . . , n t, nu − ∑ t
j=1 njwj).
Again, quite surprisingly, we get the following useful coro llary regarding this classical problem.
Corollary 2.6 For any ﬁxed t and widths w1, . . . , w t, the cutting stock problem is solvable in time
polynomial in ∑ t
j=1⌈nj/ ⌊u/w j ⌋⌉ and in the bit size of the numbers nj of orders and raw roll width u.
One common approach to the cutting stock problem makes use of so-called cutting patterns, which
are feasible solutions of the knapsack problem {y ∈ Nt : ∑ t
j=1 wjyj ≤ u}. This is useful when the
7
width u of the standard rolls is of the same order of magnitude as the d emand widths wj. However,
when u is much larger than the wj, the number of cutting patterns becomes prohibitively larg e to
handle. But then the values ⌊u/w j⌋ are large and hence n := ∑ t
j=1⌈nj/ ⌊u/w j ⌋⌉ is small, in which case
the result of Corollary 2.6 using n-fold integer programming becomes particularly appealing .
