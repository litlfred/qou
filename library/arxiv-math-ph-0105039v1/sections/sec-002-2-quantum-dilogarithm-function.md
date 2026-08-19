---
doc_id: arxiv-math-ph-0105039v1
doc_title: "December 23, 2000 (Revised Edition) Hyperbolic Structure Arising from a Knot Invariant Kazuhiro HIKAMI †"
section_id: sec-002-2-quantum-dilogarithm-function
section_title: "Quantum Dilogarithm Function"
section_number: 2
pages: 2-3
source_pdf: 0105039v1.pdf
source_sha256: 850e6a00721e38d0
doc_brief: "December 23, 2000 (Revised Edition) Hyperbolic Structure Arising from a Knot Invariant Kazuhiro HIKAMI † — We study the knot invariant based on the quantum dilogarithm function."
---
invariant for a hyperbolic knot K gives the hyperbolic volume of the knot complementS3 \ K. As
it is well known that the hyperbolic volume of the ideal tetra hedron is given by the Lobachevsky
function [5, 6] which is closely related with the dilogarith m function, his conjecture may sound
natural. Later in Ref. 7 Kashaev’s knot invariant was shown t o be equivalent with the colored
Jones polynomial at a speciﬁc value, and his conjecture is rewritten as the “volume conjecture”;
‖K‖ = 1
v3
lim
N →∞
2 π
N log |JN (K)|, (1.1)
where ‖K‖ is the Gromov norm of S3 \ K, and v3 is the hyperbolic volume of the regular ideal
tetrahedron. The knot invariant JN (K) is deﬁned from the colored Jones polynomial VN (K; t)
(N-dimensional representation of sℓ2) by
JN (K) = VN (K; e
2 π i
N ).
Thus to clarify a geometrical property of the quantum knot in variants such as the Jones polyno-
mial, it is very fascinating to reveal the 3-dimensional pic ture of this invariant. Recently some
geometrical aspects for the conjecture (1.1) have been proposed in Refs. 8 (see also Ref. [9]) based
on the 3-dimensional picture of Ref. 10.
In this paper we deﬁne the knot invariant as a “non-compact” analogue of Kashaev’s invariant,
or the colored Jones invariant. This is based on an inﬁnite dimensional representation of the quan-
tum dilogarithm function, and both the R-matrix and the invariant are deﬁned in an integral form.
In our construction a parameter γ which corresponds to π/N in eq. (1.1) is regarded as the Planck
constant ℏ/2, and a limit in eq. (1.1) is realized by the classical limitγ → 0. We shall demonstrate
how the hyperbolic structure appears in the classical limit of the non-compact Jones invariant.
2
This paper is organized as follows. In§ 2 we review the properties of the classical and quantum
dilogarithm functions. A key is that both functions satisfy the so-called pentagon identity. Using
these properties we construct a solution of the Yang–Baxter equation in terms of the quantum
dilogarithm function. With this R-operator, we introduce the knot invariant in § 3. This invariant
is given in the integral form from the beginning. We recall th at the integral form of the quantum
dilogarithm function was used in Ref. 4 to elucidate the asym ptotic behavior of the colored Jones
polynomial. In § 4 we show that the hyperbolic structure naturally appears in the classical limit
of our knot invariant. We ﬁnd that in γ → 0 limit the oriented ideal tetrahedron with transverse
oriented faces is associated to the matrix elements of the qu antum dilogarithm function. Corre-
spondingly the R-operator is identiﬁed with the oriented octahedron, whose vertices belong to the
link L. This explains how the octahedron was introduced for each br aiding in Ref. 10. We can
apply the saddle point method to evaluate the asymptotic behavior of the classical limit of the knot
invariant, and we further demonstrate that the saddle point equation for integrals of the knot in-
variant exactly coincides with the hyperbolicity consistency condition in gluing faces. Combining
the fact that the imaginary part of the classical dilogarith m function gives the hyperbolic volume
of the ideal tetrahedron at the critical point, we can conclu de that the invariant is related with the
hyperbolic volume of the knot complement at the critical point. In § 6 we show how to triangulate
the knot complement in a case of the ﬁgure-eight knot. This method can be easily applied to other
knots and links. The last section is devoted to discussions and concluding remarks.
2 Quantum Dilogarithm Function
