---
doc_id: arxiv-math-0102098v1
doc_title: "Skein theory and the Murphy operators"
section_id: sec-002-2-geometric-views-of-the-murphy-operators
section_title: "Geometric views of the Murphy operators."
section_number: 2
pages: 5-8
source_pdf: 0102098v1.pdf
source_sha256: f4bc5ca0ba1e47aa
toc_source: inferred
doc_brief: "Skein theory and the Murphy operators — The Murphy operators in the Hecke algebra Hn of type A are ex- plicit commuting elements whose sum generates the centre."
---
Geometric views of the Murphy operators.
The Murphy operators M(j) and their sum M have simple skein represen-
tatives as shown here, using Rn
n(v, s) as the model for the Hecke algebra
Hn.
Theorem 2.1 (Ram). The Murphy operator M(j) can be represented in Hn
by a single braid T(j), up to linear combination with the identity.
5
Theorem 2.2 (Morton). The sum M of the Murphy operators can be rep-
resented in Hn by a single tangle T (n), again up to linear combination with
the identity.
Proof of theorem 2.1:
In [15] Ram notes that M(j) can almost be repre-
sented by the single braid T(j) pictured, where ‘almost’ means that M(j) is
a linear combination of T(j) and the identity.
Set
T(j) =
j
in Hn, for each j ≤n including the case T(1) = 1.
Skein theory shows
quickly that T(j) −1 = zM(j), giving
M(j) = T(j) −1
s −s−1 .
✷
The elements T(j) will do equally well in place of M(j), so long as z̸ = 0,
in other words away from C[Sn].
It is clear geometrically that the elements T(j) all commute. It is not
immediately clear that the sum of these elements is in the centre of Hn,
although their product is the full twist, a well-known central element.
Proof of theorem 2.2:
Set
T (n) =
in Rn
n ∼= Hn(z), with the coeﬃcient ring extended to include v±1.
6
Apply the skein relation at one crossing to get
=
+ z
.
Hence T (n) = T (n−1) + zv−1T(n), using the standard inclusion of Hn−1 in Hn
to interpret T (n−1) as an element of Hn. Then
T (n) −T (0) = zv−1
n
X
j=1
T(j),
by induction on n. Here T (0) is just a scalar multiple of the identity, repre-
sented by a single disjoint simple loop alongside the identity braid. Since a
trivial loop in any Homﬂy skein contributes the scalar δ = (v−1 −v)/z we
can rewrite the equation as
T (n) −v−1 −v
z
= zv−1
n
X
j=1
T(j) = z2v−1M + nzv−1.
Then
T (n) = z2v−1M +
 
nzv−1 + v−1 −v
z
!
× 1,
and hence, again away from z = 0, we can write M as a linear combination
of T (n) and 1.
✷
From this representation it is quite obvious that T (n), and thus M, is in
the centre of Hn.
There is a known set of idempotent elements, Eλ, one for each partition
λ of n, which were originally described algebraically by Gyoja [5].
Skein
pictures of these based on the Young diagram for λ were given by Aiston and
myself [13]. We showed there, in a skein based counterpart of the results of
[8], that MEλ = mλEλ for an explicit scalar mλ and that mλ̸ = mµ when
λ̸ = µ.
It follows at once that T (n)Eλ = tλEλ, where the scalars tλ are
diﬀerent for each partition λ.
7
