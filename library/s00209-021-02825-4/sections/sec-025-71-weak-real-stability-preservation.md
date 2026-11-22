---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-025-71-weak-real-stability-preservation
section_title: "Weak real stability preservation"
section_number: 7.1
pages: 27-28
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
T is almost equivalent to real stability of the associated symbol SymbBB(T ). We have to say
“almost equivalent” here because there are certain weak real stability preserving operators for
which the corresponding symbol is not real stable. As before, this implies a certain dimension
restriction: such operators must have image of dimension at most two.
We will now characterize all strong real stability preserving linear operators. As above,
strong real stability preservation will serve to eliminate the degeneracy condition of the
Borcea–Brändén characterization. In this section, we duplicate the outline of our previous
discussion on complex operators, making use of arguments similar to those found in [1] to
ﬁll in the gaps.
Further, we also obtain a characterization of a certain class of operators which preserve
ray- and interval-rootedness. The question of a full characterization of such operators is as
of yet still an open problem (see [3]). Here, we answer this question for operators which
preserve both strong ray- or interval-rootedness as well as weak real-rootedness.
7.1 Weak real stability preservation
Borcea and Brändén obtain the following characterization of weak real stability preserving
linear operators. Recall the notion of proper position (denoted by ≪) given in Deﬁnition 4.8.
Theorem 1.2 (Borcea–Brändén) Fix λ ∈Nm
0 and any linear operator T : Rλ[x1, . . . , xm] →
R[x1, . . . , xm]. The following are equivalent.
(i) T maps real stable polynomials to weakly real stable polynomials.
(ii) One of the following holds:
(a) SymbBB(T ) is H2m
+ -stable.
(b) SymbBB(T ) is (Hm
−× Hm
+)-stable.
(c) T has image of dimension at most two, and is of the form
T : p →q · ψ1(p) + r · ψ2(p)
where q,r ∈R[x1, . . . , xm] are weakly real stable such that q ≪r, and ψ1, ψ2 are
real linear functionals.
As in the case of complex operators, the degeneracy condition (ii)(c) is the result of allow-
ing weak real stability preserving operators. We now give an example which demonstrates
its necessity.
1386
J. Leake
Example 7.1 Deﬁne T : Rn[x] →R[x] via:
T :
n

k=0
n
k

akxk →anxn + an−2xn−1 = (anx + an−2)xn−1
This operator obviously preserves weak real stability. We then have that SymbBB(T ) =
(z2 + x)xn−1, which is not H2
+-stable nor (H−× H+)-stable.
Again, the degeneracy condition is required for the characterization but obscures the con-
nection between an operator and its symbol. To remove it, we now turn to our characterization
of strong real stability preserving operators.
