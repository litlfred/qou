---
doc_id: ant-v14-n7-s-p04
doc_title: "Elliptic curves over totally real cubic ﬁelds are modular"
section_id: sec-004-5-proof-of-theorem-6
section_title: "Proof of Theorem 6"
section_number: 5
pages: 4-5
source_pdf: ant-v14-n7-s-p04.pdf
source_sha256: 6abd838a4c933311
doc_brief: "Elliptic curves over totally real cubic fields are modular — 10 sections: Introduction; Images mod 3, 5, 7 and modularity; Modular curves"
---
Let X= X(b5, b7) (in standard notation denoted by X0(35)). It is known that X has four Q-points and
that these are cusps. Let K be a totally real cubic ﬁeld. For the proof of Theorem 6 it will be sufﬁcient
to show that X(K)= X(Q). Suppose P∈ X(K)\X(Q). Let P1, P2, P3 be the conjugates of P given
by the three embeddings of K in Q, and write D= P1+ P2+ P3. Then D is an irreducible Q-rational
divisor on X of degree 3. We shall determine all the irreducible Q-rational divisors of degree 3 on X and
show that none of them arise from totally real cubic points, giving a contradiction.
The arithmetic of X and its Jacobian are studied in [Freitas et al. 2015, Section 5.1]. The curve X is
hyperelliptic of genus 3. A model for X, derived by Galbraith [1996, Section 4.4], is given by
X: y2=(x2+ x− 1)(x6− 5x5− 9x3− 5x− 1). (2)
Write∞± for the two points at inﬁnity. Write J for J0(35) — the Jacobian of X. Then
J(Q)= Z
24Z·[∞−−∞+]+ Z
2Z·[ 3(0,−1)− 3∞+].
Elliptic curves over totally real cubic ﬁelds are modular 1795
Let D1,..., D48 be rational divisors of degree 0 on X representing the 48 classes in J(Q), and let
D′
i= Di+ 3∞+. Recall that D is an irreducible Q-rational divisor of degree 3. Then D∼ D′
i for some i.
We shall write L(D′
i) for the Riemann–Roch space corresponding to D′
i and|D′
i| for the corresponding
complete linear system. By Riemann–Roch and Clifford’s inequality, dim L(D′
i)= 1 or 2. Moreover, if
dim L(D′
i)= 2, then|D′
i| contains a base point (see [Arbarello et al. 1985, Chapter I, Exercise D.9]),
and therefore cannot contain an irreducible divisor. To sum up, D∼ D′
i for some 1≤ i≤ 48 such that
dim L(D′
i)= 1. We computed these spaces using Magma; for this Magma uses an algorithm of Hess [2002].
We found that dim L(D′
i)= 1 for precisely 44 of the 48 divisors D′
i. For these, letting fi be a Q-basis for
L(D′
i), gives D= D′
i+ div( fi) for some i. We found that precisely 28 of the effective degree 3 divisors
D′
i+ div( fi) are irreducible. However, all of these split over a cubic ﬁeld with a complex embedding
giving the required contradiction.
