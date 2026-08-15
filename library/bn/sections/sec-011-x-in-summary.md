---
doc_id: bn
doc_title: "Braid groups and Hodge theory Curtis T. McMullen 25 April, 2009"
section_id: sec-011-x-in-summary
section_title: "In summary:"
section_number: X
pages: 16-18
source_pdf: bn.pdf
source_sha256: 95ed0908ceb54a1c
doc_brief: "Braid groups and Hodge theory Curtis T. McMullen 25 April, 2009 — This paper gives an account of the unitary representations of the braid group that arise via the Hodge theory of cyclic branched cove"
---
Theorem 3.1 We have
dimH 1(X)jk = dimH 1, 0(X)jk = 1 if 0<j/n<k/d< 1, and
dimH 1(X)jk = dimH 0, 1(X)jk = 1 if 0<k/d<j/n< 1.
The remaining eigenspaces are zero.
The case of a degree d = 6 covering branched over n = 9 points (and inﬁnity)
is shown in Figure 6.
Corollary 3.2 When q = ζ −k
d , the signature of the intersection form on
H 1(X, C)q is given by (r,s ) = ( ⌈n(k/d) − 1⌉, ⌈n(1 −k/d) − 1⌉).
Indeed, the signature (r,s ) just counts the number of terms of type (1 , 0) and
(0, 1) in the expression H 1(X)q =⨁
jH 1(X)jk , or equivalently the number
of terms above and below (but not on) the diagonal in the kth row of Figure
6.
Corollary 3.3 The eigenspace H 1(X)q has dimension n − 2 if qn = 1, and
dimension n − 1 otherwise.
Genus zero quotients. We note that the Riemann surfaces X/⟨R⟩,X/⟨T ⟩
andX/⟨RT ⟩ all have genus zero. This provides another explanation for t he
vanishing of eigenspaces — any R, T or RT -invariant cohomology class
descends to the sphere, and H 1(ˆC) = 0.
Remark: Lefschetz formulas. The eigenspace decomposition of H 1(X)
shown in Figure 6 can be determined, alternatively, by apply ing the Lef-
schetz formulas
Tr(g|H 1(X)) = 2 −
∑
g(z)=z
1 and Tr( g|H 0, 1) = 1 −
∑
g(z)=z
(1 −g′(z))−1
to compute the characters of G = ⟨R,T ⟩ acting on H 1(X) and H 0, 1(X).
The Chevalley-Weil formula similarly gives the characters of G|H 1, 0(X) for
general Galois coverings [ChW]; see also [Hu].
15
Figure 7. A model for the branched covering X.
Remark: the hexagon model. Here is an explicit model for H 1(X, Z) as
a symplectic lattice equipped with the action of G = Z/n × Z/d = ⟨R,T ⟩.
The proof will also provide a global topological model for G acting on X.
LetS = {(1, 0), (0, 1), (−1, −1)} ⊂ G. Deﬁne an alternating form on the
standard basis of the group ring Z[G] ∼
= Znd by
[g,h ] =





1 if g −h ∈S,
−1 if h −g ∈S, and
0 otherwise ,
(3.3)
and extend it by linearity to Z[G]. Let R ⊂ Z[G] denote the radical of this
form (the set of elements x such that [x,y ] = 0 for all y).
Theorem 3.4 The spaceH1(X, Z) is isomorphic to Z[G]/R as a symplectic
Z[G]-module.
Sketch of the proof. Let A and B be a pair of 2-disks, colored white
and black respectively. Construct a surface Y0 from (A ⊔B) ×G by joining
A × {g} to B × {g +s} with a band whenever s ∈ S (see Figure 7). The
group G acts by deck transformations on Y0, with quotient a surface Y0/G
of genus 1 with 1 boundary component.
Now put a half-twist in each band of Y0 (as in Figure 5), to obtain a new
surface Y1. Then Y1/G has genus 0 and 3 boundary components. By ﬁlling
in the boundary components of Y1 and Y1/G with disks, we obtain closed
surfaces Y and Z ∼
=S2 and a degree nd branched covering
π :Y →S2
with deck group G.
16
LetC ⊂Y be the core curve of one of the hexagons appearing in Figure 7.
It is then straightforward to check that the intersection nu mber (gC ) · (hC)
in H1(Y, Z) is given by (3.3). By comparing the rank of this form with the
ﬁrst Betti number of Y , we ﬁnd the inclusion Z[G]/R → H 1(Y, Z) is an
isomorphism.
Now one can also regard Y/G as an orbifold with signature ( n,d,nd/e ),
where e = gcd(d,n ). The generators of G correspond loops around the
points of orders n andd. Similarly, the map p :X →ˆC given byp(x,y ) = xn
presentsX/⟨R,T ⟩ as a covering of the same orbifold, with singular points at
0, 1, ∞. The proof is completed by identifying p :X →ˆC withπ :Y →S2.
