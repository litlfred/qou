---
doc_id: s00526-018-1443-6
doc_title: "On the analyticity of critical points of the Möbius energy"
section_id: sec-007-23-faà-di-brunos-formula
section_title: "Faà di Bruno's formula"
section_number: 2.3
pages: 6-7
source_pdf: s00526-018-1443-6.pdf
source_sha256: 34f3cd94e3b2d9d7
toc_source: outline
doc_brief: "On the analyticity of critical points of the Möbius energy — We prove that smooth critical points of the Möbius energy E parametrized by arc-length are analytic."
---
For two functions f , g ∈Ck(R, R) Faà di Bruno’s formula tells us that
 d
dt
k
g( f (t))
=
	
m1+2m2+···kmk=k,
m1,...,mk∈N0
k!
m1!1!m1m2!2!m2 . . . mk!k!mk g(m1+···+mk)( f (t))
k
j=1
( f ( j)(t))m j .
Mishkov [27] generalized this formula to the multivariate case.
Lemma 2.6 Let U ⊆R be a neighborhood of 0 and f ∈Ck(U, Rn), n ∈N. Moreover, let
V ⊆Rn be a neighborhood of f (0) such that f (U) ⊆V and g ∈Ck(V , R). Then we have
for any k ∈N0 and x ∈U
∂kg( f (x)) =
	
0
	
1
· · ·
	
k
k!
k
i=1(i!)ri k
i=1
n
j=1 qi j!
(∂αg)( f (x))
k
i=1

f (i)
1 (x)
qi1 · · ·

f (i)
n (x)
qin
where the sums are over all non-negative integer solutions of the following equations
	
0
: r1 + 2r2 + · · · + krk = k,
	
1
: q11 + q12 + · · · + q1n = r1
...
	
k
: qk1 + qk2 + · · · + qkn = rk
and α := (α1, . . . , αn) with α j := q1 j + q2 j + · · · + qkj for 1 ≤j ≤n.
On the analyticity of critical points of the Möbius energy
Page 7 of 28
16
Remark 2.7 In the following we will not need the precise form of Faà di Bruno’s formula in the
multivariate case but only the fact that there is a universal polynomial p(n)
k
with non-negative
coefﬁcients independent of f , g such that
∂kg( f (x)) = p(n)
k ({∂αg}|α|≤k, {∂j fi}i=1,...,n, j=1,...,k)
(2.2)
for all f ∈Ck(R, Rn), g ∈Ck(Rn, R), n ∈N and k ∈N0. Furthermore, p(n)
k
is one-
homogeneous in the ﬁrst entries.
