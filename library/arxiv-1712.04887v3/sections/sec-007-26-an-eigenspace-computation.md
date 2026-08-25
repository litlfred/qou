---
doc_id: arxiv-1712.04887v3
doc_title: "Bloch groups, algebraic K-theory, units, and Nahm's conjecture"
section_id: sec-007-26-an-eigenspace-computation
section_title: "An eigenspace computation"
section_number: 2.6
pages: 16-17
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
doc_brief: "Bloch groups, algebraic K-theory, units, and Nahm's conjecture — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn = F"
---
with a subgroup of ( Z/nZ)× via the map χ of Equation (4). Since F×
n/F×n
n is an n-torsion
G-module, the χ−1 eigenspace makes sense and is given by
(
F×
n/F×n
n
)χ−1
={x∈F×
n/F×n
n |σx =xχ(σ−1), for allσ∈G},
where xχ(σ−1) is computed using any lift of χ(σ−1)∈ (Z/nZ)× to Z.
In characteristic zero, one can also consider the action of G on M⊗Z R, where R is a
Z[G] module that contains the eigenvalues of σ∈ G. For example, one can take M =O×
n
and R = C. If n = p is prime, then one can take R = Zp, which contains the ( p− 1)th
roots of unity. In particular, if n = p, then one can deﬁne ( M⊗Z Zp)χ−1
, which will have
the property that
(M⊗Z Zp)χ−1
⊗ Z/pZ = (M/pM )χ−1
.
Proposition 2.12. Suppose that F is disjoint from Q(ζn).
(a) There exists an isomorphism of G-modules
(
O×
n⊗ C
)χ−1
= Cr2(F ). (26)
(b) If n =p is prime, so that χ :G→ (Z/pZ)× admits a Teichm¨ uller lift toZ×
p , then
rankZp
(
O×
n⊗ Zp
)χ−1
=r2(F ).
If in addition χ and χ−1 are distinct characters of G, then
(
O×
p/O×p
p
)χ−1
= (Z/pZ)r2(F ) .
Proof. Part (b) follows easily from part (a) and the above discussion, together with the fact
that if χ⁄= χ−1 then the torsion in the unit group (which just comprises roots of unity) is
in the χ-eigenspace and not the χ−1-eigenspace.
For (a), let ~F be the Galois closure of F over Q and let Γ = Gal(~F/Q). By assumption,
with ~Fn = ~F (ζn), we have Gal(~Fn/Q) = Γ×G = Γ×(Z/nZ)×. From the proof of Dirichlet’s
unit theorem, the unit group of ~Fn, tensored with C, decomposes equivariantly as
⨁
W
W dim(W|c=1),
where W runs over all the non-trivial irreducible representations of Γ ×G and c∈ Γ is
any complex conjugation, which we may take to be ( c,−1)∈ G× (Z/nZ)× for a complex
conjugationc∈ Γ. The irreducible representations of W are of the formU⊗V for irreducible
representationsU of Γ and V of G = (Z/nZ)×. Note that
dim(U⊗V|(c,−1) = 1) = dim(U|c = 1) dim(V|c = 1) + dim(U|c =−1) dim(V|c =−1).
If we take the χ−1-eigenspace under the action of the second factor, the only representation
V of G which occurs is χ−1, on which−1 acts by−1, and hence we are left with
(
O×
~Fn
⊗ C
)χ−1
=
⨁
V
V dim(V|c=−1),
BLOCH GROUPS, ALGEBRAIC K-THEORY, UNITS, AND NAHM’S CONJECTURE 17
where the sum runs over all representations V of Γ. In particular, there is an isomorphism
in the Grothendieck group of G-modules
[(
O×
~Fn
⊗ C
)χ−1]
+
[
O×
~F⊗ C
]
+
[
C
]
=
[
C[G]
]
.
Now take the ∆ = Gal( ~F/F ) = Gal(~Fn/Fn)-invariant part and take dimensions, we obtain
the equality
dimC
((
O×
Fn⊗ C
)χ−1)
+ (r1 +r2− 1) + 1 = r1 + 2r2,
where (r1,r 2) is the signature of F . The result follows. □
