---
doc_id: descendants-colored-jones
doc_title: "The descendant colored Jones polynomials"
section_id: sec-009-an-example
section_title: "An example"
section_number: null
pages: 23-24
source_pdf: descendants_colored_jones.pdf
source_sha256: f00693a5926c074f
doc_brief: "The descendant colored Jones polynomials — We discuss two realizations of the colored Jones polyno- mials of a knot, one appearing in an unnoticed work of the second author in 1994 on quantum"
---
In this sub-section we write an explicit expression for the invariant ⟨41⟩N,n of
the simplest hyperbolic knot 4 1 in the case of a primitive N-th root of unity
ζ and a color n ∈ Z/NZ.T h ei n v a r i a n ti sa nN × N matrix whose entries
Mi,j := ⟨i|⟨41⟩N,n|j⟩ are given by
Mi,j =
∑
k1,...,k7
j
i
k1
k2
k3
k4
k5
k6
k7
n
=
∑
k1,...,k7
Vi,k3−n,k7−n,k2 (¯ζ)ζk2−k7+(k2−k3+1+n)n
Vk6,k4,k7−n,k3−n−1(ζ)ζk6−k3+1+(k6−k7+1+n)n
Vk1,k5,k2−n,k4−n−1(¯ζ)ζk4−k1−1+(k4−k5−1−n)n
Vk1,k6−n,j−n,k5 (ζ)ζj−k5+(j−k1−1−n)n
=
∑
k1,...,k7
Vi,k3−n,k7−n,k2 (¯ζ)Vk6,k4,k7−n,k3−n−1(ζ)Vk1,k5,k2−n,k4−n−1(¯ζ)
× Vk1,k6−n,j−n,k5 (ζ)ζ(j−k1+k2−k3+k4−k5+k6−k7)(n+1)
=
∑
k1,...,k7
Vi,k3,k7,k2 (¯ζ)Vk6,k4,k7,k3−1(ζ)Vk1,k5,k2−n,k4−n−1(¯ζ)Vk1,k6−n,j−n,k5 (ζ)
× ζ(j−k1+k2−k3+k4−k5+k6−k7−2n)(n+1)
=
∑
k1,...,k7
V0,k3,k7,k2 (¯ζ)Vk6,k4,k7,k3−1(ζ)Vk1,k5,k2−n,k4−n−1(¯ζ)
× Vk1,k6−n,j−i−n,k5 (ζ)ζ(j−i−k1+k2−k3+k4−k5+k6−k7−2n)(n+1)
=
∑
k1,...,k7
V0,k3,k7,k2 (¯ζ)V0,k4,k7−k6,k3−k6−1(ζ)V0,k5,k2+k1−k6,k4+k1−1(¯ζ)
× V0,k1,j−i−k6+k1,k5 (ζ)ζ(j−i+2k1+k2−k3+k4−k5−k7)(n+1).
(61)
2330 Stavros Garoufalidis and Rinat Kashaev
The above is a sum over ( Z/NZ)7 and it is not clear how to simplify
to sum in fewer variables. Numerical calculations suggest that ⟨K⟩N,n is a
multiple of the identity matrix.
