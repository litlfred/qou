---
doc_id: arxiv-1001.2933v4
doc_title: "Analytic Continuation Of Chern-Simons Theory"
section_id: sec-001-2-overview
section_title: "Overview"
section_number: "2"
pages: 7-8
source_pdf: 1001.2933v4.pdf.txt
source_sha256: b02636c86d593c02
toc_source: inferred
doc_brief: "Analytic Continuation Of Chern-Simons Theory — The title of this article refers to analytic continuation of three-dimensional ChernSimons gauge theory away from integer values of the usual coupling"
---
2 Overview
We begin by considering Chern-Simons gauge theory with the gauge group G a complex Lie
group such as SL(2, C). Let A be a connection on a G-bundle E over a three-manifold M.
Such a connection has a complex-valued Chern-Simons invariant
W(A) = 1
4π
Z
M
Tr A ∧ dA +
2
3
A ∧ A ∧ A

, (2.1)
which we have normalized to be gauge-invariant modulo 2π. (For G = SL(N, C), the symbol
Tr denotes the trace in the N-dimensional representation. In general, it denotes a suitably
normalized quadratic form on the Lie algebra g of G.) Just as in the case of a compact
group, W(A) is gauge-invariant modulo 2π. The indeterminacy in W(A) is real, and is the
same as it would be if G were replaced by a maximal compact subgroup H, because G is
contractible onto H.
3
Thus the imaginary part of W(A) is actually a well-defined real number, while its real
part takes values in R/2πZ. To obtain a quantum field theory, we wish to start with a
classical action I that is a linear combination of Re W and Im W. The quantum theory is
based upon integrating the expression exp(iI), and for this function to be well-defined, I
must be defined mod 2π. Because of the indeterminacy in Re W, its coefficient must be
an integer, while (if the only desired condition is to ensure that exp(iI) is a well-defined
complex-valued function) the coefficient of Im W may be an arbitrary complex number. The
action therefore has the general form
I = −s Im W + ℓ Re W, s ∈ C, ℓ ∈ Z. (2.2)
Alternatively, we can write
I =
t W
2
+
et W
2
=
t
8π
Z
M
Tr A ∧ dA +
2
3
A ∧ A ∧ A+
et
8π
Z
M
Tr 
A ∧ dA +
2
3
A ∧ A ∧ A

,
(2.3)
with
t = ℓ + is, et = ℓ − is. (2.4)
There is more to life, however, than making sure that exp(iI) is a well-defined complexvalued function. We also want to integrate this function over the space Y of gauge fields
3The indeterminacy in W(A) comes from its change in going around a loop in the space of connections
modulo gauge transformations, and this change only depends on the homotopy class of the loop. Since G
is contractible to H, any family of g-valued connections on M can be deformed to a family of h-valued
connections, where g, h are the Lie algebras of G and H. So the indeterminacy in the Chern-Simons function
for gauge group G reduces to that for gauge group H.
7

modulo gauge transformations. This makes sense straightforwardly only if s is real, for then
I is real and the integrand exp(iI) of the path integral is bounded. The path integral
Z
Y
DA DA exp(iI) (2.5)
is then an infinite-dimensional oscillatory integral. In this respect, it is like any Lorentz
signature Feynman integral (though here we are doing topological field theory rather than
quantum field theory on a manifold of Lorentz signature). If s is not real, the path integral
is not convergent; our task is to make sense of it anyway.
