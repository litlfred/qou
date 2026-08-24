---
doc_id: bn
doc_title: "Braid groups and Hodge theory"
section_id: sec-029-10-similarly-for-n-5-we-can-rule-out-d-4
section_title: "Similarly, for n = 5 we can rule out d = 4"
section_number: 10
pages: 36-38
source_pdf: bn.pdf
source_sha256: 95ed0908ceb54a1c
doc_brief: "Braid groups and Hodge theory — This paper gives an account of the unitary representations of the braid group that arise via the Hodge theory of cyclic branched cove r- ings of P1, highlighting their"
---
by checking that r(A) > 1 at q = ζ4; and for n = 7 we can rule out d = 6
by checking that r(A) > 1 at q = ζ6. (Here we have used the fact that
the representations ρq at diﬀerent primitive dth roots of unity are all Galois
conjugate.)
Corollary 8.2 The image of the braid group ρq(Bn) is ﬁnite iﬀ U(Λ n,q ) is
ﬁnite.
35
Jacobians. Whenρq(Bn) is ﬁnite, the Hodge structure on the correspond-
ing part of the H 1(X) is rigid; equivalently, we have an isogeny
Jac(X) →J(X) ×A
where dimA> 0 and A is independent of X. We refer to A as a rigid factor
of the Jacobian of X.
Theorem 8.3 The Jacobian of the curve X deﬁned by
yd = (x −b1) · · · (x −bn)
(for n distinct points) has a rigid factor in the 8 cases shown in Tab le 10.
n d g(X) Factor of Jac(X)
3 3 1 C/Z[ζ3]
3 4 3 (C/Z[ζ4])2
3 6 4 (C/Z[ζ3])2
3 10 9 (C2/Z[ζ5])2
n d g(X) Factor of Jac(X)
4 4 3 (C/Z[ζ4])2
4 6 7 (C/Z[ζ3])3
5 6 10 (C/Z[ζ3])4
6 6 10 (C/Z[ζ3])4
Table 10. Rigid factors of the Jacobian.
In Table 10, g(X) indicates the genus of X, and the rigid factor listed
comes from ⨁ H 1(X)q over the primitive dth roots of unity.
The factor C2/Z[ζ5], which occurs for ( n,d ) = (3, 10), denotes quotient
of C2 by the image of Z[ζ5] under x ↦→(x,x ′), where x ↦→x′ is the Galois
automorphism satisfying ζ ′
5 =ζ 2
5 . The other factors listed are elliptic curves
with automorphisms of orders 4 or 6.
Note that the cases ( n,d ) = (3, 4) and (4, 4) yield the same set of curves
X, as do the cases (5 , 6) and (6 , 6). Note also that curves of type ( n,d ) =
(3, 6) cover curves of type (3 , 3), so they also have a second rigid factor
A′ ∼
= C/Z[ζ3].
Proof of Theorem 8.3. LetS =⨁ H 1(X)q, where the sum is taken over
the primitive dth roots of unity. This subspace is deﬁned over Q, so it meets
H 1(X, Z) in a lattice SZ of the same rank as dim CS.
For the 8 cases listed, the induced Hodge structure on S is given by
S =S1, 0 ⊕S0, 1 =

 ⨁
Im q>0
H 1(X)q

 ⊕

 ⨁
Im q<0
H 1(X)q

,
36
where again the sum is over the primitive dth roots of unity (see Corollary
3.2). That is, the Hodge structure is reﬁned by the eigenspac e decomposition
of T |S, which is independent of the complex structure on X; and hence the
complex torus A =S1, 0/SZ is a rigid factor of Jac( X). The dimension of A
is determined by Corollary 3.3, and the CM-type of the endomo rphismT |A
(see [Shi, §5.5A]) is determined by the condition Im q >0. This information
determines A itself, up to isogeny, yielding Table 10.
Genus 3 curves branched over 4 points. For added perspective we
describe some details in one of the simplest cases, namely ge nus 3 curves X
of the form
y4 = (x −b1)(x −b2)(x −b3).
