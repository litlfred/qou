---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-021-61-weak-stability-preservation
section_title: "Weak stability preservation"
section_number: 6.1
pages: 21-22
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
Borcea and Brändén deﬁne the following symbol:
SymbBB(T ) := T [(x + z)λ] =

μ≤λ
λ
μ

zλ−μT (xμ)
They then obtain the following characterization of stability-preserving linear operators.
Theorem 1.1 (Borcea–Brändén) Fix λ ∈Nm
0 and any linear operator T : Cλ[x1, . . . , xm] →
C[x1, . . . , xm]. The following are equivalent.
(i) T maps Hm
+-stable polynomials to weakly Hm
+-stable polynomials.
(ii) One of the following holds:
(a) SymbBB(T ) is H2m
+ -stable.
(b) T has image of dimension at most one, and is of the form
T : p →q · ψ(p)
where q ∈C[x1, . . . , xm] is Hm
+-stable, and ψ is some linear functional.
Using our terminology, this is a characterization of weak stability-preserving linear oper-
ators. This fantastic result perhaps has but one unfortunate piece: the degeneracy condition
(ii)(b). Its necessity is demonstrated in the following.
Example 6.1 Deﬁne T : Cn[x] →C[x] via:
T :
n

k=0
n
k

akxk →(an + an−2)xn
This operator obviously preserves weak H+-stability. We then have that SymbBB(T ) =
(z2 + 1)xn, which is not H2
+-stable.
As we will see below, this condition can be removed once we only consider strong stability-
preserving operators. So then, maybe strong stability is the more natural notion? However
“natural” it is, unfortunately it leaves out operators one might wish to consider. The most
fundamental of such operators is the derivative operator ∂x. While ∂x preserves strong H+-
stability, it only preserves weak H+-stability. Speciﬁcally, 1 ∈Cn[x] is H+-stable (all its
roots are at ∞), but ∂x1 ≡0. With this, one obviously wants to be able to include weak
stability preserving operators in any characterization of H+-stability preserving operators.
We discuss how to use our strong stability preservation characterization to deal with operators
like ∂x in Example 6.8.
1380
J. Leake
