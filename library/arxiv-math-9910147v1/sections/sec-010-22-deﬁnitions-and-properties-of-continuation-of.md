---
doc_id: arxiv-math-9910147v1
doc_title: "Tensor Products of Principal Unitary Representations of Quantum Lorentz Group and Askey-Wilson Polynomials E. Buffenoir ∗"
section_id: sec-010-22-deﬁnitions-and-properties-of-continuation-of
section_title: "Deﬁnitions and properties of continuation of quantum 6j symbols"
section_number: 2.2
pages: 5-7
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
---
In order to understand the problem of continuation of quantum 6 j symbols the reader is invited
to read the appendix of [1] where deﬁnitions, proofs, as well as ref erences on 6j(1) are given.
Let us give a deﬁnition which is essential in order to describe the comp lex continuations of
quantum 6j symbols (the notations are explained in the appendix of the present work).
Deﬁnition 1 Let X = {(T,U,V,X,Y,Z ) ∈ C6, (2T,T +U −V,T +V −U,T +Y −Z,T +Z −Y ) ∈
N5}, we deﬁne for any (T,U,V,X,Y,Z ) ∈ X,
N
(
T U
X Y
V
Z
)
= eiπ(T +Y −Z) q(T +Y −Z)(U−T +Y −X+1)+(V +Y −X)(T +V −U)ν1(dZ )ν1(dV ) ×
× (U −T +X −Y +1)∞ ω(Y ;V,X )ω(T ;Y,Z )ω(T ;V,U )
(T −U +X +Y +1)∞(2T + 1)∞(1)∞ ω(U ;X,Z ){{ T U
X Y
V
Z
}}
= N
( T U
X Y
V
Z
)
4Φ 3
[
U− V− T U +V− T+1 Z − Y− T − Z− Y− T− 1
− 2T − Y− X− T+U U +X− Y− T+1
]
. (18)
It is important to understand that for ( T,U,V,X,Y,Z ) ∈ X, N
( T U
X Y
V
Z
)
and
{{ T U
X Y
V
Z
}}
are both square roots of rational functions in the variables q2T,q 2U,q 2V,q 2X,q 2Y,q 2Z. This is a
simple consequence of the fact that the hypergeometric series is o f terminating type.
We have been very cautious with the determination of the signs. This annoying problem al-
ready appeared in the case of 6 j(0) but can be handled quite easily. This problem is strengthned
in the case of 6j(1) and 6j(3) because in that case we really have to take square roots of com plex
numbers. This is the reason why we introduced a particular square r oot, denoted ν∞(x) of the
Eulerian product (x)∞ for x ∈ C.
5
It will sometimes be useful to have the explicit value of the 6 j symbols when one of the spins
is equal to 0 or 1
2 . From the last deﬁnition we easily get:
∀A,B,C ∈ C,
{{
0 C
A B
C
B
}}
= 1 (19)
{{ 1
2 C + 1
2
A B
C
B + 1
2
}}
= ν1(B +C −A + 1)ν1(A +B +C + 2)
ν1(2C + 2)ν1(2B + 1)
{{ 1
2 C + 1
2
A B
C
B − 1
2
}}
= − ν1(A +B −C)ν1(A +C −B + 1)
ν1(2C + 2)ν1(2B + 1) qC+B−A+1
{{ 1
2 C − 1
2
A B
C
B + 1
2
}}
= ν1(A +C −B)ν1(A +B −C + 1)
ν1(2C)ν1(2B + 1) qC+B−A
{{ 1
2 C − 1
2
A B
C
B − 1
2
}}
= ν1(A +B +C + 1)ν1(C +B −A)
ν1(2C)ν1(2B + 1) . (20)
The usual 6 j(0) symbols which properties were described in the last section and d enoted{
A B
D E
C
F
}
(0)
where A,B,C,D,E,F ∈ 1
2 Z+, are given by:
{
A B
D E
C
F
}
(0)
=
{{
A B
D E
C
F
}}
Y (0)
(A,B,C )Y (0)
(A,E,F )Y (0)
(D,B,F )Y (0)
(D,E,C ). (21)
This expression can easily be obtained from the usual expressions [1 5, 16] using the inversion
relation and the Sears identities (91,99) recalled in the appendix.
In the previous formula, and in the following ones, we will make a distinc tion between the
ﬁrst part of the right handside, which is called ”explicit value”, and th e second part, products
of Y functions and called ”selection rules”.
In order to describe properties of continuation of 6j symbols, we w ill make in the sequel a
convenient abuse of notation, which greatly simpliﬁes formulae:
if X1 ∈ C is ﬁxed, if k is a positive integer and f : Ck+1 → C is a function, a series of the
type∑
X2,X3,...,Xk
f (X1,X 2,...,X k) will always be deﬁned as
∑
X2,X3,...,Xk
f (X1,X 2,...,X k) =
∑
n1,n2,...,nk∈ 1
2 Z
f (X1,X 1 +n1,...,X k +nk). (22)
Note that we will only use the notation X0,X 1 to denote a couple of complex numbers such
that X0 = −X1 − 1, and X0 −X1 ∈ 1
2 Z, (this notation will be explained in the next part.)
Let us deﬁne the involutive endomorphism of the complex line: ∀X ∈ C,X ↦→X = −X − 1,
as we will see it is important to understand the action of this symmetr y on the 6 j symbols.
In [18, 1] two types of 6 j(1) symbols were deﬁned. The ﬁrst type is a family of numbers
denoted
{
A B
X1 X2
C
X3
}
(1)
and the second one is denoted
{
A X2
B X1
X3
X4
}
(1)
, where both are
deﬁned for A,B,C ∈ 1
2 Z+, ∀i,j ∈ {1, · · ·, 4},X i ∈ C − 1
2 Z+,X i −Xj ∈ 1
2 Z.
Their explicit expressions are given by
{
A B
X1 X2
C
X3
}
(1)
=
{{
A B
X1 X2
C
X3
}}
Y (1)
(A,X2−X3)Y (1)
(B,X1−X3)Y (1)
(C,X1−X2)Y (0)
(A,B,C ),
{
A X2
B X1
X3
X4
}
(1)
=
{{
A X2
B X1
X3
X4
}}
Y (1)
(A,X2−X3)Y (1)
(A,X1−X4)Y (1)
(B,X1−X3)Y (1)
(B,X2−X4). (23)
6
These formulae deserve some remarks, concerning the very word of ”continuation”. The explicit
value of the 6j(1) is a regular function when the Xi approach half-integer values, but the selection
rules appears to be diﬀerent, i.e the support of the continuated 6j (1) are larger than that of the
6j(0) symbols. Nethertheless, for ﬁxed I,J ∈ 1
