---
doc_id: arxiv-1101.3374v1
doc_title: "Pontryagin invariants and integral formulas for Milnor's triple linking number"
section_id: sec-005-6-proof-of-theorem
section_title: "Proof of Theorem ??"
section_number: 6
pages: 41-43
source_pdf: 1101.3374v1.pdf
source_sha256: 01d76c1d259c1d51
toc_source: outline
doc_brief: "Pontryagin invariants and integral formulas for Milnor's triple linking number — To each three-component link in the 3-sphere, we associate a geometrically natural characteristic map from the 3-torus"
---
Let L be a three-component link in the 3-sphere with characteristic map gL : T 3 →S2.
Theorem A asserts that the degrees of gL on the coordinate 2-tori of T 3 are equal to the
pairwise linking numbers p, q and r of the components of L, and that Pontryagin’s absolute
ν-invariant of gL is equal to twice Milnor’s triple linking number µ(L) mod 2 gcd(p, q, r).
The ﬁrst statement was proved easily at the end of Section 4. We now prove the second
statement by an inductive argument, relying heavily on the techniques and results of the
last section. Throughout, we will use the asymmetric characteristic map hL : T 3 →S2 in
place of gL, since these two maps are homotopic.
Proof of the base case of Theorem A
In Example 2.1 we introduced the “base links” Lpqr with pairwise linking numbers p, q
and r and µ(Lpqr) = 0. See Figure 3. We will show that Theorem A holds for these links.
To accomplish this, we must show that for each p, q and r, the associated characteristic
map hLpqr is homotopic to the base map fpqr : T 3 →S2 used in Section 3 to convert the
relative Pontryagin ν-invariant to an absolute ν-invariant. In other words, we must show
that ν(hLpqr) = 0.
First move Lpqr by a link homotopy into generic position, and let L = X ∪Y ∪Z be the
resulting link. Then Z coincides with the binding K of the standard open book, while X
and Y wind around Z in a generic fashion, q and p times respectively, linking each other
41
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
r times along the way. In fact this winding can be made monotonic, to appear as shown
in Figure 28 for the case (p, q, r) = (5, 3, −2).
q
p
r
X
Y
Z
Figure 28. A generic link L representing Lpqr
Observe that one need not actually construct a link homotopy carrying Lpqr to L, but
need only check that the pairwise and triple linking numbers of Lpqr and L coincide,
and then appeal to Milnor’s classiﬁcation. The veriﬁcation that µ(L) = 0 is completely
analogous to the calculation for µ(Lpqr), using the obvious stacked disks, joined by half
twisted bands, as Seifert surfaces for X and Y , and a hemispherical page in the open book
on S3 as a Seifert surface for Z.
Now the bicycles in L are easily identiﬁed. There are d = gcd(p, q) of them, all of
longitudinal degree ℓ= lcm(p, q), and all but one of meridional degree 0, the remaining
one being of degree r. The parametrizing icycles are all parallel to a (p/d, q/d) torus knot
in the 2-torus, with vertical winding numbers all equal to zero, except one equal to r. By
the bicycle theorem, these icyles form a diagram for the Pontryagin link of hL, with global
framing −(pq + r). This is exactly the situation described in Example 3.2, and so
ν(hLpqr) = ν(hL) = 0 ∈Z2 gcd(p,q,r)
as asserted.
Proof of the inductive step of Theorem A
First recall from Example 2.2 that any three-component link L with pairwise linking
numbers p, q and r is link homotopic to a link obtained from Lpqr by a sequence of delta
moves of the type shown in Figure 4 (or its inverse), by a result of Murakami and Nakanishi
[1989]. It was shown in that example that each such move increases µ(L) by 1.
Now observe that such a delta move ∆: L →bL can be viewed as a double crossing
change D, of the kind shown in Figure 25, composed with an isotopy, as indicated in
Figure 29. By Corollary 5.2, this double crossing change increases ν(L) by 2, and so ∆
does the same.
42
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
isotopy
D
∆
L
X
Y
bL
bL
Figure 29. Another view of the delta move
Since this argument applies to an arbitrary delta move, it follows that ν(L) = 2µ(L)
for all three component links L. This completes the proof of Theorem A.
