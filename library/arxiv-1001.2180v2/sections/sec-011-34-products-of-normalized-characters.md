---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-011-34-products-of-normalized-characters
section_title: "Products of normalized characters"
section_number: 3.4
pages: 10-11
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
the point-wise multiplication of functions over Young diag rams of size n corresponds to the product in
the center of the symmetric group algebra. But, in Z(/BV Sn), one has
Σµ · Σν =
∑
∀i, A i∈A(n, µi)
∀i⁄=j, A i∩Aj =∅
∑
∀i, B i∈A(n, νi)
∀i⁄=j, B i∩Bj =∅
C(A1) C(A2) · · · C(Ar) C(B1) C(B2) · · · C(Br).
As the Ai’s and the Bj’s may have elements in common, this is not equal to Σµ∪ν. Let us split this double
summation over ai,j and bk,l in the following way. To each indexing sequence ai,j, bk,l, we associate the
partial matching between the sets IA = (i, j)1≤j≤µi (indices of the a’s) and IB = (k, l)1≤k≤νl , which links
(i, j) and (k, l) if and only if ai,j = bk,l. When we sum the quantity
(4) C(A1) C(A2) · · · C(Ar) C(B1) C(B2) · · · C(Br)
over indexing sequences with a given partial matching, we ob tain Σ ρ for some ρ depending on the
matching. Indeed, if we know which of the ai,j’s are equal to which of the bk,l’s, the product ( 4) can be
rewritten as a product of cycles with disjoint supports in a w ay which does not depend of the values of
the a’s and of the b’s. Finally,
Σµ · Σν =
∑
Σρ(M),
where the sum runs over partial matchings M of the set of indices of the a’s with the set of indices of the
b’s.
Example 2. Let us compute Σ2 · Σ3. The set of indices of the a’s (resp. the b’s) is {1, 2} (resp. {1, 2, 3}).
• If A and B have no common element, the product C(A) C(B) is a 3-cycle multiplied by a 2-cycle
with disjoint supports and the corresponding sum is Σ3,2.
ASYMPTOTICS OF q-PLANCHEREL MEASURES 11
• If a1 = b1, but all other elements are diﬀerent, then (a1 a2 a3) · (a1 b2) = ( a1 b2 a2 a3). When
we sum on all possible values of a1, b2, a2, a3 (all diﬀerent), one obtains Σ4.
The result is the same for any of the 6 matchings of size 1.
• If a1 = b1 and a2 = b2, then (a1, a2, a3) · (a1, a2) = ( a1, a3)(a2). When we sum on all possible
values of a1, a2, a3, we obtain Σ2,1 (note that here it is important to remember that we have to
sum over indices a2 even if its value does not change the permutation).
Once again, the result is the same for any of the 6 matchings of size 2.
Thus, Σ2 · Σ3 = Σ2,3 + 6Σ4 + 6Σ2,1.
In general, one has the following properties:
(1) The size of ρ(M ) is simply |µ| + |ν| − |M | where |M | is the size of the matching.
(2) The term corresponding to the empty matching is Σν∪µ. Thus,
Σν · Σµ = Σν∪µ +
∑
|ρ|<|µ|+|ν|
cρ
ν,µ Σρ.
By induction, one obtains that, if k1 ≥ k2 ≥ . . . ≥ kr:
Σk1 · Σk2 · · ·Σkr = Σk1,...,kr +
∑
|ρ|<k1+···+kr
cρ
k1,...,kr Σρ.
This triangular relation can be inverted, so the Σρ are in the algebra O and span it linearly.
Moreover, Σρ is a non-homogeneous element of degree |ρ| and its homogeneous component of
maximal degree is pρ.
(3) If µ = ( l) and ν = ( m), all matchings of size 1 give a term Σl+m−1. As there are ml such
matchings, one has
Σl Σm = Σl,m + ml Σl+m−1 + (terms of degree at most l + m − 2).
