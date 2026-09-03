---
doc_id: arxiv-2406.05311v1
doc_title: "A QUANTUM MURNAGHAN\u2013NAKAYAMA RULE FOR THE FLAG MANIFOLD C. BENEDETTI, N. BERGERON, L. COLMENAREJO, F. SALIOLA, AND F. SOTTILE"
section_id: sec-002-a-murnaghan-nakayama-rule-for-quantum-cohomology
section_title: "A Murnaghan\u2013Nakayama rule for quantum cohomology"
section_number: 3
pages: 8-12
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
doc_brief: "A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD C. BENEDETTI, N. BERGERON, L. COLMENAREJO, F. SALIOLA, AND F. SOTTILE — 5 sections: Introduction; A Murnaghan–Nakayama rule for (cla; A Murnagha"
---
The (small) quantum cohomology ring qH ∗ Fℓn of the flag manifold is a deformation of the
ordinary cohomology ring H ∗ Fℓn whose product encodes the three-point Gromov–Witten
invariants of Fℓn . We describe this ring and extend the main objects from Section 2 to the
quantum setting.
3.1. Quantum cohomology ring of the flag manifold. As a Z-module, we have
qH ∗Fℓn = Z[q1 , . . . , qn−1 ] ⊗Z H ∗ Fℓn ,
where q1 , . . . , qn−1 are indeterminates. To simplify notation, write Z[q] for Z[q1 , . . . , qn−1 ],
αn−1
and use multiindex notation, for α ∈ Nn−1 , we have q α := q1α1 · · · qn−1
. The Schubert classes
{Sw }w∈Sn in H ∗ Fℓn form a Z[q]-basis of qH ∗ Fℓn . We write Su ∗ Sv for the product of Schubert classes Su and Sv in qH ∗ Fℓn to distinguish it from the product Su · Sv in H ∗ Fℓn .
The ring structure of qH ∗ Fℓn is determined by the quantum Monk formula [13]. For every
u ∈ Sn and 1 ≤ k < n we have,
X
X
Su ∗ S(k,k+1) =
Su(i,j) +
qi,j Su(i,j)
(3.1)
1≤i≤k<j≤n
ℓ(u)+1=ℓ(u(i,j))

1≤i≤k<j≤n
ℓ(u)+1=ℓ(u(i,j))+2(j−i)

where qi,j := qi qi+1 · · · qj−1 for i < j. The summand on the left above comes from the classical
Monk formula (2.4). For example, in qH ∗ Fℓ4 we have,
S1432 ∗ S(2,3) = S3412 + S2431 + q2 S1342 + q2,3 S1234 .

(3.2)

Givental and Kim [17] proved that qH ∗ Fℓn ≃ Z[q][x]/Inq for a certain ideal Inq , establishing
an analog to Borel’s presentation (2.1). Fomin, Gelfand, and Postnikov [13] defined quantum
Schubert polynomials Sqw (x) in Z[q][x] so that the quantum product of Schubert classes


QUANTUM MURNAGHAN–NAKAYAMA RULE

9

satisfies Su ∗ Sv 7→ (Squ (x) + Inq )(Sqv (x) + Inq ), for u, v ∈ Sn , under this isomorphism. To
simplify notation, for f (x) ∈ Z[q][x], we will write Su ∗ f (x) for Squ (x)f (x) + Inq .
As explained in Section 2.1, every Schur polynomial is a Schubert polynomial: more precisely, sλ (x1 , . . . , xk ) = Sv(λ,k) (x), where λ ⊆ Rk,n−k . Analogously, we define the quantum
Schur polynomial sqλ (x1 , . . . , xk ), for λ ⊆ Rk,n−k , to be sqλ (x1 , . . . , xk ) := Sqv(λ,k) (x). Following
Equation (2.8), the quantum power sum is defined to be
pqr (x1 , . . . , xk ) :=
sq(r) (x1 , . . . , xk ) − sq(r−1,1) (x1 , . . . , xk ) + · · · + (−1)r+1 sq(1r ) (x1 , . . . , xk ) .

(3.3)

3.2. Quantum k-Bruhat order. The terms appearing in the quantum Monk formula (3.1)
define a ranked partial order on the (infinite) set

Sn [q] := q α u | u ∈ Sn and α ∈ Nn−1 .

The quantum k-Bruhat order ≤qk on Sn [q] is defined by the following cover relations:

(1) u ⋖qk u(i, j) if i ≤ k < j and ℓ(u) + 1 = ℓ(u(i, j)), so that u ⋖k u(i, j);
(2) u ⋖qk qi,j u(i, j) if i ≤ k < j and ℓ(u) + 1 = ℓ(u(i, j)) + 2(j−i) ; and
(3) extend q-multiplicatively: u ≤qk q β w if and only if q α u ≤qk q α+β w for u, w ∈ Sn [q] and
any α, β ∈ Nn−1 .
We will say that covers of type (1) and their extensions by (3) are classical, and covers of
type (2) and their extensions by (3) are quantum. The rank function ℓ on Sn [q] is given by
ℓ(q α u) := 2 deg q α +ℓ(u), where deg q α is the usual degree of the monomial q α in Z[q]. Figure 4
shows two levels of the quantum 2-Bruhat order on S4 [q] starting at the permutation 14 32.
We draw the classical covers in green and the quantum covers in red. Compare the first level
to the example in (3.2).
34 21

q2,3 21 34

❍❍
❍❍

q2 23 41

✟✟ ❅
✟
✟
❅

24 31

q2 14 32
✁
✁

q2 13 42

PP
PP
PP

q2 31 42
✁
✁

34 12

✏✏✥✥✥✥✥
✏✥
✥
✏
✥
✏✥
✏✥

q2,3 13 24
✁
✁

q2,3 12 34

14 32
Figure 4. Two levels of the quantum 2-Bruhat order on S4 [q] above 14 32.
As with the k-Bruhat order (see Proposition 2.1), there is an intrinsic formulation of the
cover relations for the quantum k-Bruhat order.
Proposition 3.1. Let u ∈ Sn and q α w ∈ Sn [q]. Then u ⋖qk q α w if and only if
(1) α = 0 and q α w = w = u(i, j) for some i ≤ k < j such that u(i) < u(j), and
there does not exist l such that i < l < j and u(i) < u(l) < u(j); or
(2) q α w = qi,j u(i, j) for some i ≤ k < j such that u(i) > u(j), and
for every l such that i < l < j, we have u(j) < u(l) < u(i).


QUANTUM MURNAGHAN–NAKAYAMA RULE

10

3.3. Minimal intervals. As far as we know, there is no analog of the Grassmannian–Bruhat
order related to the quantum k-Bruhat order, and so rather than speak of minimal permutations (as we did in the classical case; see Section 2.4), we work instead with certain intervals
in the quantum k-Bruhat order. This lack of an analog of the Grassmannian–Bruhat order
necessitates the significant work we do in Section 5.
Let u, w ∈ Sn and suppose that u ≤qk q α w in the quantum k-Bruhat order on Sn [q]. We say
that the interval [u, q α w]qk is minimal if its rank ℓ(q α w)−ℓ(u) equals # supp(wu−1 )−s(wu−1).
When q α = 1, the interval [u, w]qk = [u, w]k is minimal if and only if wu−1 is a minimal
permutation. In the proof of Theorem 3.2 we will show that if [u, q αw]qk is minimal, then
wu−1 is a minimal permutation in the sense of Section 2.4.
The interval on the left in Figure 1 is a minimal interval in the quantum 5-Bruhat order in
S8 . Figure 5 displays two minimal intervals in quantum k-Bruhat order on S5 [q] for k = 2, 3.
q1,5 q2,4 12 354
q2,5 52 314 q1,5 15 324

q3,5 521 34
524 31 q3,5 421 35

q2,5 51 324 q1,5 14 325

514 32 523 41

425 31

54 321 q1,5 13 425

513 42 423 51

415 32

53 421

413 52

Figure 5. Two minimal quantum intervals. Note that q1,5 q2,4 = q1,4 q2,5 = q1 q22 q32 q4 .
3.4. The Murnaghan–Nakayama rule for qH ∗ Fℓn . As for Corollary 2.6, we derive the
quantum Murnaghan–Nakayama formula from an intermediate result describing the quantum
product of a Schubert class Su by a quantum hook Schur polynomial sq(b,1a−1 ) (x1 , . . . , xk ).
Theorem 3.2. Let u ∈ Sn , a ≤ k and b ≤ n − k. Then
X  s(wu−1 )−1 
q α Sw ,
Su ∗ sq(b,1a−1 ) (x1 , . . . , xk ) =
ht(wu−1 )−a

the sum over all minimal intervals [u, q α w]qk such that ℓ(q α w) − ℓ(u) = a+b−1.
The proof depends on Theorem 5.1 and Lemma 4.4, which will be proved in subsequent
sections.
Proof. For u, w ∈ Sn , a partition λ, αk ∈ N with 1 ≤ k and α ∈ Nn−1 , define quantum
q w
Littlewood–Richardson coefficients Cu,v(λ,k)
∈ q α N by
X
qα w
Cu,v(λ,k)
Su ∗ sqλ (x1 , . . . , xk ) =
Sw .
(3.4)
q α w∈Sn [q]

We must prove that
qα w

Cu,v((b,1a−1 ),k) =

 

s(wu−1 )−1
α

q ht(wu−1 )−a ,

0,

if [u, q α w]qk is minimal and
ℓ(q α w) − ℓ(u) = a+b−1,
otherwise.


QUANTUM MURNAGHAN–NAKAYAMA RULE

11

Suppose that [u, q αw]qk is a minimal interval with ℓ(q α w) −ℓ(u) = a+b−1. By Theorem 5.1,
qα w
there exists a hook partition γ with |γ| = ℓ(q α w) − ℓ(u) and Cu,v(γ,k)
6= 0. By Lemma 4.4,
there exist permutations y, z ∈ Sn satisfying
y ≤k z,

ℓ(z) − ℓ(y) = ℓ(q α w) − ℓ(u) = a+b−1,

zy −1 = wu−1,

(3.5)

and such that
α

q w
Cu,v(µ,k)
= q α czy,v(µ,k)

for all partitions µ with |µ| = a+b−1 .

(3.6)

This implies that zy −1 is a minimal permutation, since
ℓ(z) − ℓ(y) = ℓ(q α w) − ℓ(u) = # supp(wu−1) − s(wu−1) = # supp(zy −1 ) − s(zy −1 ),
where the middle equality follows from the assumption that [u, q α w]qk is minimal. Then




s(wu−1 )−1
s(zy −1 )−1
qα w
α
α z
α
,
(3.7)
=
q
Cu,v((b,1
−1
−1
a−1 ),k) = q cy,v((b,1a−1 ),k) = q
ht(wu )−a
ht(zy )−a
where the first equality follows from (3.6) and the second equality follows from Proposition 2.5
and that zy −1 is a minimal
permutation.
qα w
Conversely, suppose Cu,v((b,1a−1 ),k) 6= 0. By Lemma 4.4, there exist y, z ∈ Sn satisfying (3.5)
and (3.6). Setting µ = (b, 1a−1 ) in (3.6) gives
α

q w
α z
Cu,v((b,1
a−1 ),k) = q cy,v((b,1a−1 ),k) .

(3.8)

Since the left hand side is assumed to be nonzero, we have that czy,v((b,1a−1 ),k) is nonzero. It
now follows from Proposition 2.5 that zy −1 is a minimal permutation so that
ℓ(q α w) − ℓ(u) = ℓ(z) − ℓ(y) = # supp(zy −1 ) − s(zy −1 ) = # supp(wu−1) − s(wu−1),
where the first and last equalities follow from (3.5). Thus, [u, q α w]qk is a minimal interval such
that ℓ(q α w) − ℓ(u) = a+b−1.

The following was conjectured in [27]. It follows from Theorem 3.2 in the same way that
Corollary 2.6 follows from Proposition 2.5, and is the signature result in this paper.
Corollary 3.3 (Quantum Murnaghan–Nakayama Formula). Let u ∈ Sn . Then
X
−1
Su ∗ pqr (x1 , . . . , xk ) =
(−1)ht(wu )+1 q α Sw

the sum over all minimal intervals [u, q α w]qk of rank r such that wu−1 is a single cycle.
Example 3.4. In qH ∗ Fℓ8 , if u = 68235741, then the product Su ∗ pq4 (x1 , . . . , x5 ) is
S(2,3,5,7,4)u + S(2,4,3,5,7)u + S(3,5,6,7,4)u − S(2,3,5,6,7)u
+q5,7 S(2,3,4,7,5)u + q5,7 S(3,4,6,7,5)u + q5,8 S(1,6,7,3,5)u + q5,8 S(1,7,2,3,5)u
−q5,8 S(1,6,7,5,4)u − q5,8 S(1,7,5,3,4)u − q5,8 S(1,7,4,3,5)u − q2,6 S(2,3,5,7,8)u
+q2,8 S(1,7,3,5,8)u + q2,8 S(1,8,2,3,4)u + q2,8 S(1,6,7,5,8)u + q2,8 S(1,7,5,6,8)u − q2,8 q5,7 S(1,7,5,4,8)u .

Note that unlike in ordinary cohomology, this is not an identity among quantum Schubert
polynomials Sqw (x), but rather among their images in the quotient ring Z[q][x]/Inq .


QUANTUM MURNAGHAN–NAKAYAMA RULE

12

3.5. Remarks regarding [25, Thm. 15]. Proposition 2.5 may be deduced from a stronger
result of Mészáros, Panova, and Postnikov [25, Thm. 8]. There, they establish a formula for a
‘lift’ of the Schur polynomial s(b,1a−1 ) (x1 , . . . , xk ) to the Fomin–Kirillov [15] algebra En , which
is a subalgebra (generated by certain Dunkl elements θi ) of the quotient of a free associative
algebra with generators xi,j for 1 ≤ i < j ≤ n by certain relations, which include x2i,j = 0.
Their paper contains another result [25, Thm. 15] which is a quantum analog of [25, Thm. 8],
giving a formula for a ‘quantum lift’ of sq(b,1a−1 ) (x1 , . . . , xk ) to the quantum Fomin–Kirillov
algebra Enq [32]. This formula would imply Theorem 3.2. Unfortunately, as we now sketch,
there is a gap in the proof of [25, Thm. 15] (we have communicated this to the authors).
The result [25, Thm. 15] is deduced from the proof of [25, Thm. 8] using a technical
result [25, Lem. 13] which roughly asserts the following: If an identity involving positive
terms holds in En , and if no relations x2i,j = 0 were used to deduce the identity, then the
same identity holds in Enq . We are convinced this lemma is correct, but it unfortunately does
not apply in the case invoked to prove [25, Thm. 15]. The proof of [25, Thm. 8] uses in a
fundamental way [25, Cor. 10], that ea (θ1 , . . . , θa )hb (θ1 , . . . , θa ) = 0 in Ea+b (in their notation).
However, this identity can only be proven directly in Ea+b using the relations x2i,j = 0. For
example, when a = b = 1, as θ1 = x1,2 , it becomes 0 = e1 (x1,2 )h1 (x1,2 ) = x21,2 .
