---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-035-61-a-summary-of-the-results-to-come
section_title: "A summary of the results to come"
section_number: 6.1
pages: 46-50
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
doc_brief: "Standard model physics from an algebra? — 57 sections: Abstract; Acknowledgements; Introduction"
---
Using only the algebra of the complex octonions, which we will introduce, we expose an
intrinsic structure to a generation of quarks and leptons. This algebraic structure mimics
familiar quantum systems, which have a vacuum state acted upon by raising and lowering
operators. In this case, the neutrino poses as the vacuum state, and electrons and quarks
pose as the excited states. These results are simply the analogue of the Fock space we
found earlier in Section 4.6.1.
With these raising and lowering operators in hand, we are then able to construct a
number operator in the usual way,
N =
∑
i
α†
iαi. (6.2)
It will be seen that N has eigenvalues given by {0, 1, 1, 1, 2, 2, 2, 3}. At ﬁrst sight, these
eigenvalues might not look familiar, that is, until they are divided by 3.N/3 has eigenvalues
38
{0, 1
3, 1
3, 1
3, 2
3, 2
3, 2
3, 1}, which can now be recognized as the electric charges of a neutrino
(or anti-neutrino), a triplet of anti-down quarks, a triplet of up quarks, and a positron.
We will then deﬁne our electric charge, Q, as
Q≡ N
3. (6.3)
As N must take on integer values, Q must be quantized. Hence, the model oﬀers at this
early stage a straightforward explanation for the quantization of electric charge.
As we will show, the remaining states within a generation are related to these particles
by complex conjugation, and hence are acted upon by −Q∗ in the usual way.
The anti-commuting ladder operators, mentioned above, can be seen to possess a certain
symmetry generated uniquely by su(3)c and u(1)em, the two unbroken symmetries of the
standard model. These generators of SU (3)c do indeed match those of [41], and ﬁt in
perfectly with Q, the U(1)em generator mentioned above. Under these symmetries, we
ﬁnd that our Fock space, and its complex conjugate, together transform as would a full
generation of quarks and leptons.
Ours is certainly not the ﬁrst instance where G¨ unaydin and G¨ ursey’s model has been
adapted. As an extension of their model, [26], [27], Dixon describes electric charge as
a mix of quaternionic and octonionic objects. It would be interesting to see if a ladder
system could be found, which alternately gives Dixon’s Q as a number operator. Readers
are encouraged to see [26], [27], or other examples of his extensive work.
Since the time of ﬁrst writing, more octonionic chromo-electrodynamic models have
been found. Most noteworthy of all were three papers written in the late 1970s, [8],
[13], and [14], which could also be considered as extensions of G¨ unaydin and G¨ ursey’s
model, [42]. In these papers, the authors use two separate ladder systems: system (a)
ﬁts with the octonionic ladder operators of [42], and system (b) is introduced as quater-
nionic. By combining the two systems, they describe the electric charge generator not as a
number operator, but as the diﬀerence between the number operators of the two systems.
References [8], [13], and [14] are important papers, worth careful reconsideration by the
community.
Our results diﬀer from earlier versions in that we will be constructing a generation of
quarks and leptons explicitly as minimal left ideals of a Cliﬀord algebra, generated only
by the complex octonions. In doing so, we will use just a single octonionic ladder system,
with its complex conjugate. This in turn allows us to deﬁne electric charge more simply
as Q = N/3, thereby exposing a more direct route to the two unbroken gauge symmetries
39
of the standard model. Furthermore, our formalism naturally relates particles and anti-
particles using only the complex conjugate, i↦→−i, which is not a feature of these earlier
models. Finally, as our generation of quarks and leptons will be constructed from Cliﬀord
algebra elements, not column vectors, we will then be free to model weak isospin, using
right multiplication of this same Cliﬀord algebra onto these minimal left ideals.
6.2 Introduction to C⊗ O
The complex octonions are not a tool commonly used in physics, so we introduce them
here.
The generic element of C⊗ O is written∑7
n=0Anen, where the An are complex coeﬃ-
cients. The en are octonionic imaginary units (e2
n =−1), apart frome0 = 1, which multiply
according to Figure 6.1. The complex imaginary unit i commutes with the octonionic en.
e e
e
e
e e
e3
4
6
7
1
5
2
Figure 6.1: Multiplication of octonionic imaginary units
Any three imaginary units on a directed line segment in Figure 6.1 act as if they were
a triplet of Pauli matrices, σm. (More precisely, they behave as −iσm.) For example,
e6e1 =−e1e6 =e5, e1e5 =−e5e1 =e6, e5e6 =−e6e5 =e1, e4e1 =−e1e4 =e2, etc.
The multiplication rules for these imaginary units can be deﬁned by setting e1e2 =e4,
and then applying the following rules, as shown in [4].
40
eiej =−ejei i⁄=j,
eiej =ek ⇒ ei+1ej+1 =ek+1,
eiej =ek ⇒ e2ie2j =e2k.
(6.4)
It is indeed true that the octonions form a non-associative algebra, meaning that the
relation (ab)c = a(bc) does not always hold. The reader can check this by ﬁnding three
imaginary units, which are not all on the same line segment, and substituting them as in
a, b, and c.
The octonionic automorphism group is G2, which is a 14-dimensional exceptional Lie
group. Its Lie algebra may be represented by the generators
Λ1 = i
2
(
e1 (e5 · )−e3 (e4 · )
)
, Λ8 = i
2
√
3
(
e1 (e3 · ) +e4 (e5 · )− 2e2 (e6 · )
)
,
Λ2 =−i
2
(
e1 (e4 · ) +e3 (e5 · )
)
, g 9 =− i
2
√
3
(
e1 (e5 · ) +e3 (e4 · ) + 2e2 (e7 · )
)
,
Λ3 = i
2
(
e4 (e5 · )−e1 (e3 · )
)
, g 10 = i
2
√
3
(
e1 (e4 · )−e3 (e5 · ) + 2e6 (e7 · )
)
,
Λ4 = i
2
(
e2 (e5 · ) +e4 (e6 · )
)
, g 11 =− i
2
√
3
(
e4 (e6 · )−e2 (e5 · ) + 2e1 (e7 · )
)
,
Λ5 = i
2
(
e5 (e6 · )−e2 (e4 · )
)
, g 12 =− i
2
√
3
(
e2 (e4 · ) +e5 (e6 · )− 2e3 (e7 · )
)
,
Λ6 = i
2
(
e1 (e6 · ) +e2 (e3 · )
)
, g 13 =− i
2
√
3
(
−e1 (e6 · ) +e2 (e3 · ) + 2e4 (e7 · )
)
,
Λ7 = i
2
(
e1 (e2 · ) +e3 (e6 · )
)
, g 14 = i
2
√
3
(
−e1 (e2 · ) +e3 (e6 · ) + 2e5 (e7 · )
)
,
(6.5)
acting on the octonions. Here, the nested brackets indicate that the generators are con-
structed from chains of octonions, multiplying from right to left.
The eight objects, Λ i, generate SU (3) ⊂ G2. This SU (3) may be deﬁned as the
subgroup of G2 which leaves the octonionic unit e7 invariant. Of course, alternate SU (3)
subgroups of G2 may be found, which correspond to other imaginary units. For a more
thorough introduction of O see [4], [23], [56].
Finally, we deﬁne three notions of conjugation on an element a in C⊗ O. The complex
conjugate ofa, denoteda∗, maps the complexi↦→−i, as would be expected. The octonionic
conjugate of a, denoted ˜a, takes each of the octonionic imaginary units en ↦→ −en for
n = 1,... 7. That which we will call the hermitian conjugate of a, denoted a†, performs
both of these maps simultaneously, i↦→−i and en↦→−en for n = 1,... 7. The conjugate
41
and the hermitian conjugate each reverse the order of multiplication, as is familiar from
the hermitian conjugate of a product of matrices.
