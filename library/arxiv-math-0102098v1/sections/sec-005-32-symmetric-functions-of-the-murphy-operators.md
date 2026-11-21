---
doc_id: arxiv-math-0102098v1
doc_title: "Skein theory and the Murphy operators"
section_id: sec-005-32-symmetric-functions-of-the-murphy-operators
section_title: "Symmetric functions of the Murphy operators."
section_number: 3.2
pages: 13-16
source_pdf: 0102098v1.pdf
source_sha256: f4bc5ca0ba1e47aa
toc_source: inferred
doc_brief: "Skein theory and the Murphy operators — The Murphy operators in the Hecke algebra Hn of type A are ex- plicit commuting elements whose sum generates the centre."
---
Symmetric functions of the Murphy operators.
The main result in this paper, besides theorem 2.2 and its consequences, is
an expression for the mth power sum of the Murphy operators in Hn in terms
of the element Pm ∈C.
For this I use a previously unremarked relation between the Hecke alge-
bras and the skein of the annulus. This relation takes the form of a very
natural homomorphism ψn from C to the centre of each algebra Hn.
The diagram
D =
13
determines a map ψn : C →Hn, induced by placing X ∈C around the circle
in D and the identity of Hn on the arc, to get
ψn(X) =
X
∈Hn.
It is clear that
ψn(XY ) =
X
Y
=
Y
X
= ψn(X)ψn(Y ),
so that ψn is an algebra homomorphism.
Moreover the elements ψn(X)
obviously all lie in the centre of Hn, and in fact it follows from theorem
3.9 below that the image of ψn consists af all symmetric polynomials in the
Murphy operators and so, by [4], makes up the whole of the centre in the
generic case.
We already know from theorem 2.2 that the sum P T(j) is essentially
T (n), and we can write T (n) = ψ(X) with X = h1, represented by a single
string around the core of the annulus. We may then look for elements X2
with ψ(X2) = P T(j)2 and more generally ψ(Xm) = P T(j)m.
These can certainly be found for each ﬁxed n, using for example a suitable
polynomial in h1 which depends on n. Much more surprising is the result
of theorem 3.9, that there exists an element Xm independent of n with the
property that
ψn(Xm) =
n
X
j=1
T(j)m,
up to a multiple of the identity. Consequently any other symmetric function
of the Murphy operators can be achieved as ψ(X) where the choice of X is
essentially independent of n.
14
In fact, we can take Xm = Pm, to get the following explicit result, proved
in section 4.
Theorem 3.9 For any n we have
ψn(Pm) −ψ0(Pm) = (sm −s−m)v−m
n
X
j=1
T(j)m.
This is particularly satisfactory in that Pm itself arises as a power sum,
although not of any identiﬁable objects in the ring C itself.
Since any element X ∈C+ can be written as a polynomial in {Pm} we can
then express ψ(X) as a symmetric function of the Murphy operators T(j).
It is useful to be able to write the elements ψ(hi) in terms of the Murphy
operators; theorem 3.9 leads to a compact expression using formal power
series with coeﬃcients in the centre of the Hecke algebra.
I shall do this in terms of the Murphy series HM(t) of the Hecke algebra,
whose coeﬃcients, lying in the centre of Hn, are deﬁned to be the complete
symmetric functions of the elements T(j). Thus the Murphy series in Hn
can be written explicitly as
HM(t) =
n
Y
j=1
(1 −T(j)t)−1.
The series has a formal inverse, EM(−t), where the coeﬃcients of EM(t) =
Q(1 + T(j)t) are the elementary symmetric functions of the elements T(j),
also in the centre of Hn.
Theorem 3.10
ψn(H(t)) = ψ0(H(t)) HM(sv−1t)
HM(s−1v−1t).
Proof :
It is enough to establish that the logarithms of the two sides are
equal. Now
ln(ψn(H(t))) = ψn(ln(H(t))) =
∞
X
m=1
ψn(Pm)
m
tm,
while
ln(HM(t)) =
∞
X
m=1
P T(j)m
m
tm.
15
The coeﬃcients of tm in ln(ψn(H(t))) and in
ln
 
ψ0(H(t)) HM(sv−1t)
HM(s−1v−1t)
!
=
ln (ψ0(H(t))) + ln

HM(sv−1t)

−ln

HM(s−1v−1t)

are equal, by theorem 3.9.
✷
