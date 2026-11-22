---
doc_id: arxiv-math-9802116v1
doc_title: "arXiv:math/9802116v1 [math.QA] 25 Feb 1998"
section_id: sec-006-5-new-quasialgebras
section_title: "New quasialgebras"
section_number: 5
pages: 20-24
source_pdf: 9802116v1.pdf
source_sha256: be7999751ffb6db3
toc_source: inferred
doc_brief: "Quasialgebra structure of the octonions — We show that the octonions are a twisting of the group algebra of Z2 × Z2 × Z2 in the quasitensor category of representations of a quasi-Hopf algebra asso"
---
New quasialgebras
It is clear that there are many examples of quasialgebras kF G according to the group G and the
cochain F. In this section we will consider examples where F 2 = 1; we will see that even in this
case we can obtain very diﬀerent types of algebras.
By Proposition 3.7 we know that if kF G is an n-dimensional composition algebra for the
Euclidean norm, the cochain F is deﬁned by an Hadamard matrix H (that is, a matrix such
that HtH = nI where t is transpose and I is the identity matrix). The matrix entries are
Hx,y = F(x, y) for x, y ∈G. Motivated by this, we begin by considering more general examples
of quasialgebras deﬁned by a cochain given by a normalized Hadamard matrix.
Proposition 5.1 If we consider the symmetric Hadamard matrix
H =


1
1
1
1
1
1
−1
−1
1
−1
1
−1
1
−1
−1
1


as a cochain on the group Z2 × Z2 we obtain a nonsimple, associative and commutative algebra.
Proof
The algebra deﬁned by H and the group (Z2)2 has the multiplication table
e
x
y
z
x
e
−z
−y
y
−z
e
−x
z
−y
−x
e
By straightforward calculations, one can see that this algebra is commutative and associative.
Moreover, I =< e + x, y −z > is an ideal of this algebra. ⊔⊓
Next we consider q = pr where p is an odd prime number. Let χ(x) be the character deﬁned
in the ﬁnite ﬁeld Fq where χ(0) = 0, χ(x) = 1 if x is a square, and χ(x) = −1 if x is not a
square. Consider the matrix Q deﬁned by Qij = χ(ei −ej) (where e1, e2, e3, ...eq are a natural
enumeration of the elements of Fq). Suppose that pr = 3(mod4), that is pr + 1 = 4n for some
n. In this case Q is skew-symmetric and


1
1
. . .
1
−1
...
Q + I
−1


is a well-known skew symmetric Hadamard matrix with many applications (eg in the theory
of Payley matrices). If we multiply each row except the ﬁrst by (-1) we obtain a normalized
Hadamard matrix of order 4n, which we can use as a cochain. In view of Proposition 3.5 we
consider for example the case where n is a power of 2, so pr + 1 = 2m and m ≥2, and we let
G = (Z2)m. The octonions and quaternions appear in this family for p = 7, 3 and r = 1.
Proposition 5.2 The algebras kF Zm
2 where m ≥2 and
H =


1
1
. . .
1
1...
−Q −I
1


is viewed as a cochain, i.e. F(x, x) = −1
(x̸ = e = e0) F(ei, ej) = −χ(ei −ej)
(i > 0)
(j >
0)
(i̸ = j), are simple and noncommutative.
Proof
By computing R(x, y) = F(x, y)/F(y, x) it is easy to see that the kF G are alterco-
mutative (and hence noncommutative). From this, the choice G = (Z2)m and F(x, x) = −1
for x̸ = e, we conclude by Proposition 3.5 that the algebras kF G admit the diagonal strong
involution σ(x) = F(x, x)e, and hence by Proposition 3.6 that they are simple. ⊔⊓
It is known that the Hadamard matrices have only order 2 or 4n. However, we can construct
another class of algebras that have order 3 or 4n + 1 if we deﬁne the cochain by a matrix of the
form


1
1
. . .
1
1...
H
1


where H is an Hadamard matrix. The simplest case is with H an Hadamard matrix of order
two:
Proposition 5.3 Let kF Z3 be a quasialgebra which cochain deﬁned by the matrix,


1
1
1
1
H
1


where H is an Hadamard matrix of order 2.
Then kF Z3 is a nonassociative simple algebra
(commutative or altercommutative).
Proof
If H is an Hadamard matrix of order 2 we have only two diferent possibilities for kF Z3,
with the multiplication table I:
e
x
y
x
−y
e
y
e
x
or the multiplication table II:
e
x
y
x
y
−e
y
e
x
Let I̸ = kF Z3 be an ideal of kF Z3 and let a = P
x∈Z3 αxx an element of I. Then in both cases
(a · x) · y ∈I and if kF Z3 is deﬁned by table I this implies that αx = 0 ( if not, x ∈I and
I = kF Z3).
And if kF Z3 is deﬁned by table II this implies that αe = 0 (if not e ∈I and
I = kF Z3). So I must be zero. On the other hand it is clear that the algebra deﬁned by table I
is commutative and the one deﬁned by the table II is altercommutative.
⊔⊓
Following this idea, one also has
Proposition 5.4 Let kF Z5 be a quasialgebra which cochain F deﬁned by the matrix


1
1
. . .
1
1...
H
1


where H is the Hadamard matrix of order 4 with maximal excess (H = J −2I where J has order
4 and has all elements equal to 1) Then kF Z5 is a simple commutative nonassociative algebra.
One may prove this directly. Related to it is the following general observation:
Proposition 5.5 Let n ≥4 and F(x, y) = (−1)δx,y for x, y̸ = e, then kF Zn is a simple commu-
tative, nonassociative algebra.
Proof
It’s easy to see that these algebras are commutative and nonassociative. To prove that
they are simple we recall that as Zn is a group we know that for x, y ∈Zn we have Lx ·Ly = Lxy
and so Lx · Ly · Lxy = Id if we denote by Lx the map Lx(a) = xa. So let’s consider an ideal
I̸ = kF Zn and let a = P
x∈Zn αxx be an element of I. Now let’s consider an element y ∈Zn
that is diferent from e and has order diferent from 2, 3. Then y · a = P
x∈Zn αxF(y, x)yx =
P
x̸=y∈Zn αxyx −αyy2 is an element of I. Now if we multiply the last element by z = y2 we will
have that the element z · (P
x̸=y∈Zn αxyx −αyy2) = P
x̸=y∈Zn αxy3x + αyy2 is an element of I.
Finally, we multiply the last element by v = y3 and have that the element v · (P
x̸=y∈Zn αxy3x +
αyy2) = −αee + P
x̸=e∈Zn αxx is an element of I. So αee ∈I and αe = 0 and I = 0 or αe̸ = 0
and I = kF Zn. ⊔⊓
Other natural classes of examples (to be considered elsewhere) include the natural generali-
sation of the octonions based on Galois sequences in [9, Chap. 2.]. For example, one may take
G = Z3 × Z3 and F of the form F = e
2πı
3 f, in contrast to the F 2 = 1 case.
