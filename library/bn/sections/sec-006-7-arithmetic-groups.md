---
doc_id: bn
doc_title: "Braid groups and Hodge theory"
section_id: sec-006-7-arithmetic-groups
section_title: "Arithmetic groups"
section_number: 7
pages: 32-36
source_pdf: bn.pdf
source_sha256: 95ed0908ceb54a1c
toc_source: inferred
doc_brief: "Braid groups and Hodge theory — This paper gives an account of the unitary representations of the braid group that arise via the Hodge theory of cyclic branched cover- ings of P1, highlighting their"
---
Arithmetic groups
We now turn to arithmetic constraints on the image of the braid group.
Consider the Z[q]-module
Λn,q = H1(X, Z[q])q ⊂H1(X)q.
The unitary automorphisms preserving this module form a countable sub-
group
U(Λn,q) ⊂U(H1(X)q) ∼= U(r, s).
Since our representation of the braid group preserves H1(X, Z[q]), it also
preserves Λn,q, and hence it factors as:
ρq : Bn →U(Λn,q) ⊂U(r, s).
In this section we will show:
Theorem 7.1 The values of n ≥3 and q̸ = 1 such that U(Λn,q) is a discrete
subgroup of U(H1(X)q) ∼= U(r, s) are those given in table Table 9 and their
complex conjugates. In these cases, either:
1. U(Λn,q) is an arithmetic lattice in U(r, s), or
2. We have q = −1, and U(Λn,q) ∼= Sp2g(Z) is a lattice in Sp2g(R) ⊂
U(g, g).
Corollary 7.2 The image of the braid group ρq(Bn) is discrete in the cases
appearing in Table 9.
Table of arithmetic groups. In Table 9, p gives the order of ρq(τi) in
U(Λn,q). Note that the values k/d = 1/6, 1/4, 1/3 and 1/2 occur for every
n ≥3. These are exactly the cases where Z[q] is a discrete subring of C, and
they account for all cases of discreteness when n > 12.
For the entries with n = 3, U(Λn,q) is an arithmetic triangle group of
signature (2, 3, p) (or its ﬁnite image in U(1), when p = 6). The complete list
of arithmetic triangle groups can be found in [Tak]. Note that the (2, 3, 5)
31
n
k/d
(r, s)
p
3
1/6
(0,2)
3
3
1/4
(0,2)
4
3
1/10
(0,2)
5
3
3/10
(0,2)
5
3
1/3
(0,1)
6
3
5/14
(1,1)
7
3
3/8
(1,1)
8
3
7/18
(1,1)
9
3
2/5
(1,1)
10
3
9/22
(1,1)
11
3
5/12
(1,1)
12
3
3/7
(1,1)
14
3
7/16
(1,1)
16
3
4/9
(1,1)
18
3
11/24
(1,1)
24
3
7/15
(1,1)
30
3
1/2
(1,1)
∞
4
1/6
(0,3)
3
4
1/4
(0,2)
4
4
3/10
(1,2)
5
4
1/3
(1,2)
6
4
5/14
(1,2)
7
4
3/8
(1,2)
8
4
2/5
(1,2)
10
4
5/12
(1,2)
12
4
4/9
(1,2)
18
4
1/2
(1,1)
∞
n
k/d
(r, s)
p
5
1/6
(0,4)
3
5
1/4
(1,3)
4
5
3/10
(1,3)
5
5
1/3
(1,3)
6
5
3/8
(1,3)
8
5
2/5
(1,2)
10
5
5/12
(2,2)
12
5
1/2
(2,2)
∞
6
1/6
(0,4)
3
6
1/4
(1,4)
4
6
3/10
(1,4)
5
6
1/3
(1,3)
6
6
3/8
(2,3)
8
6
5/12
(2,3)
12
6
1/2
(2,2)
∞
7
1/6
(1,5)
3
7
1/4
(1,5)
4
7
3/10
(2,4)
5
7
1/3
(2,4)
6
7
3/8
(2,4)
8
7
5/12
(2,4)
12
7
1/2
(3,3)
∞
8
1/6
(1,6)
3
8
1/4
(1,5)
4
8
3/10
(2,5)
5
8
1/3
(2,5)
6
8
3/8
(2,4)
8
8
5/12
(3,4)
12
8
1/2
(3,3)
∞
n
k/d
(r, s)
p
9
1/6
(1,7)
3
9
1/4
(2,6)
4
9
3/10
(2,6)
5
9
1/3
(2,5)
6
9
5/12
(3,5)
12
9
1/2
(4,4)
∞
10
1/6
(1,8)
3
10
1/4
(2,7)
4
10
3/10
(2,6)
5
10
1/3
(3,6)
6
10
5/12
(4,5)
12
10
1/2
(4,4)
∞
11
1/6
(1,9)
3
11
1/4
(2,8)
4
11
1/3
(3,7)
6
11
5/12
(4,6)
12
11
1/2
(5,5)
∞
12
1/6
(1,9)
3
12
1/4
(2,8)
4
12
1/3
(3,7)
6
12
5/12
(4,6)
12
12
1/2
(5,5)
∞
n
k/d
(r, s)
p
n > 12
1/6
(⌈n/6 −1⌉, ⌈5n/6 −1⌉)
3
1/4
(⌈n/4 −1⌉, ⌈3n/4 −1⌉)
4
1/3
(⌈n/3 −1⌉, ⌈2n/3 −1⌉)
6
1/2
(⌈n/2 −1⌉, ⌈n/2 −1⌉)
∞
Table 9.
For q = ζ−k
d
above, the braid group maps into an arithmetic lattice
U(Λn,q) ⊂U(r, s).
32
triangle group occurs twice in our table, once for each complex place of Q(ζ5).
In all other cases (including those with n > 3), we have 1/p + k/d = 1/2.
Arithmetic perspectives. To establish Theorem 7.1, we will relate the
group U(Λn,q) to the full Q-algebraic group G ∼= Sp2g(R)T of automorphisms
of H1(X) commuting with T and respecting the symplectic structure.
1. We ﬁrst note that the real points of the centralizer factor as follows:
G(R)
∼=
Sp2g(R)T
∼=
Sp(H1(X, R)−1) ×
Y
Im q>0
U(H1(X)q).
There are ⌊(d −1)/2⌋terms in the second factor, one for each d-th
root of unity q in the upper halfplane.
This factorization of G(R)
is obtained from the splitting of H1(X, R) into eigenspaces Vq+q of
T + T −1|H1(X, R). We have also used the fact that for q̸ = ±1, T
determines a complex structure on Vq+q which yields an isomorphism
Sp(Vq+q)T ∼= U(H1(X)q).
2. A fundamental result of Borel and Harish-Chandra then implies that
G(Z) ∼= Sp2g(Z)T is a lattice in G(R) ∼= Sp2g(R)T .
Indeed, the real characters of the symplectic and unitary factors of
G(R) satisfy XR(Sp2h(R)) = XR(U(r, s)) = 0, and hence XQ(G) ⊂
XR(G) = 0 as well. By [BH, Thm. 9.4], this implies vol(G(R)/G(Z)) <
∞.
3. Let Φe(x) denote the cyclotomic polynomial for the primitive e-th
roots of unity, and let Ge = G| Ker(Φe(T ∗)) We then have a similar
factorization of Q-algebraic groups, namely G = Q
e|d Ge. Note that
G1 is trivial, G2 is the symplectic group of Ker(T ∗+ I), and for e ≥3
we have
Ge(R) ∼=
Y
Φe(q)=0,Im q>0
U(H1(X)q).
Let Ge(Z) ⊂Ge(R) denote the stabilizer of the lattice Le = Ker(Φe(T ∗))∩
H1(X, Z). Then G(Z) is commensurable to Q
e|d Ge(Z), and as above
we ﬁnd:
Ge(Z) is a lattice in Ge(R).
33
4. Now suppose q is a primitive d-th root of unity. Then:
The projection of Gd(Z) to U(H1(X)q) is commensurable to
U(Λn,q) .
This comes from the fact that the Z[T]-module Le projects orthogo-
nally to a Z[q]-module commensurable to Λn,q in H1(X)q. Clear G(Z)
preserves Λn,q, so we also ﬁnd:
The group G(Z) projects to a subgroup of ﬁnite index in
U(Λn,q).
5. The lattice property of Gd(Z) then implies:
U(Λn,q) is a discrete, arithmetic subgroup of U(H1(X)q) iﬀ
the other factors of Gd(R) are compact.
6. Suppose q = ζk
d with 0 < k < d/2 and gcd(k, d) = 1. Using Corollary
3.2 to compute the signature (r′, s′) of H1(X)q′ for the other primitive
d-th roots of unity, we deduce:
U(Λn,q) ⊂U(H1(X)q) is a lattice ⇐⇒
Every k′̸ = k in the range 0 < k′ < d/2 with gcd(k′, d) = 1
satisﬁes k′ ≤d/n.
Table 9 is now readily veriﬁed by applying the criterion above, completing
the proof of Theorem 7.1.
Notes and references. More generally, one can show that if T ∈Sp2g(Q)
is semisimple, then Sp2g(Z)T is a lattice in Sp2g(R)T iﬀthe irreducible factors
of det(xI−T) are reciprocal polynomials (their roots are invariant under z 7→
1/z). (In particular, Sp2g(Z)T is a lattice in Sp2g(R)T whenever det(xI −T)
is irreducible.)
The pseudo-Anosov mapping in genus 3 studied in [AY] and [Ar] gives an
interesting example where the centralizer Sp6(Z)T is not a lattice in Sp6(R)T .
In this example, the reciprocal sextic polynomial det(xI −T) factors as a
product (x3 + x2 + x −1)(x3 −x2 −x −1) of two non-reciprocal cubics, and
Sp6(Z)T is commensurable to T Z in Sp6(R)T ∼= R∗× C∗.
For background on arithmetic and algebraic groups, see e.g. [BH], [Bor2,
§23], [Bor1], [Mg, Ch. I]. More on centralizers and conjugacy classes can be
found in [SS], [Re] and [Gr].
34
