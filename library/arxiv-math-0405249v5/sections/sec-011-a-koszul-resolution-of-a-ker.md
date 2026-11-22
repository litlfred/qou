---
doc_id: arxiv-math-0405249v5
doc_title: "Twisted homology of quantum SL (2)"
section_id: sec-011-a-koszul-resolution-of-a-ker
section_title: "a koszul resolution of A/ ker"
section_number: null
pages: 10-11
source_pdf: 0405249v5.pdf
source_sha256: bc699482e5cd7679
toc_source: outline
doc_brief: "Twisted homology of quantum SL (2) — We calculate the twisted Hochschild and cyclic homology (in the sense of Kustermans, Murphy and Tuset) of the coordinate algebra of the quan- tum SL(2) group"
---
Using the above facts it is easy to see that ker ε is generated as both a
left and right A-module by x1,1 := a −1, x1,2 := b, x1,3 := c. For these
elements there exists a Koszul complex (K∗, k), Kn := Kn(xi,j, A), in the
sense of section 2.4 with the xi,j given by


a −1
b
c
q−1a −1
b
c
q−2a −1
b
c

.
(30)
We check by explicit calculation that this Koszul complex is acyclic:
proposition 4.1 The left A-module A/ker ε possesses a resolution (K∗, k)
of the form
0 →A →k3 A3 →k2 A3 →k1 A →A/ker ε →0.
The augmentation map K0 = A →k = A/ker ε is given by the counit ε.
The left A-module morphisms kn : Kn →Kn−1, n = 1, 2, 3, are given by
k1 :


1
0
0

,


0
1
0

,


0
0
1

7→a −1, b, c
k2 :


1
0
0

,


0
1
0

,


0
0
1

7→


b
1 −q−1a
0

,


c
0
1 −q−1a

,


0
c
−b

,
k3 : 1 7→


c
−b
q−2a −1

.
Proof. It follows from Proposition 2.4 (or directly) that this is a complex.
Let (x, y, z)t ∈ker(k1), i.e. x(a−1)+yb+zc = 0. Then πbc(x(a−1)) = 0.
Using the Z-grading we have πbc(x) = 0, so x = x′b + x′′c. Subtracting
k2(x′, x′′, 0)t from (x, y, z)t we get a new element of ker(k1) with x = 0.
Hence πc(y) = πb(z) = 0, so y = y′c, z = z′b, z′ = −y′ and this element
is a multiple of k2(0, 0, 1)t. In a similar manner
x


b
1 −q−1a
0

+ y


c
0
1 −q−1a

+ z


0
c
−b

= 0
implies x = x′c, y = −x′b, x′(q−2a −1) = z for some x′ ∈A.
✷
corollary 4.2 If n > 3, then HHσ
n(A) = 0 for all automorphisms σ.
The morphism between the resulting short complex σA′⊗AK∗and the
standard complex for TorA
n (σA′, k) yielding an isomorphism in homology
is given explicitly by:
1. The map ϕ0 : A →C0 = A is the identity.
10
2. The map ϕ1 : A3 →C1 = A⊗2 is given by


x
y
z

7→(x, a −1) + (y, b) + (z, c).
(31)
Since d(x, 1, 1) = (x, 1) for any x, we have [(x, a −1)] = [(x, a)] in
TorA
1 (σA′, k).
3. The map ϕ2 : A3 →C2 = A⊗3 is given by


x
y
z

7→(x, b, a −1) −(x, q−1a −1, b)+
+ (y, c, a −1) −(y, q−1a −1, c) + (z, c, b) −(z, b, c)
(32)
4. Finally, the map ϕ3 : A →C3 = A⊗4 in the complex for the Tor-
groups is given by x 7→x ⊗v, where
v = −(q−2a −1, b, c) + (q−2a −1, c, b) −(c, q−1a −1, b)+
+ (c, b, a −1) −(b, c, a −1) + (b, q−1a −1, c).
(33)
One sees by direct computation that this is a morphism of complexes,
and by the comparison theorem (see [23], Theorem 2.2.6) this is a quasi-
isomorphism.
4.2
