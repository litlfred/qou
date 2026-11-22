---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-019-5-integral-transforms-for-d-modules
section_title: "Integral transforms for D-modules"
section_number: 5
pages: 30-31
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
We continue with our standing assumptions of preceding sections. In particular, by a scheme, we
mean a quasi-compact, separated derived scheme. By a stack, we mean a quasi-compact stack with
aﬃne diagonal, and by a representable morphism, we mean a quasi-compact schematic morphism.
A stack is safe if its de Rham cohomology functor is continuous, and more generally, a morphism is
safe if the pushforward of D-modules along it is continuous.
In the previous section, we recalled that for any stacks X1, X2, external tensor product induces
an equivalence
D(X1) ⊗D(X2)
∼
/ D(X1 × X2).
Verdier duality induces a canonical self-duality
D(X1) ≃D(X1)′
If in addition X1 is safe, then the integral transform construction provides a description of the
resulting equivalence
D(X1 × X2)
∼
/ FunL(D(X1), D(X2))
M ✤
/ π2∗(π!
1(−) ⊗M)
The above equivalences ﬁt into a canonically commuting diagram
D(X1) ⊗D(X2)
∼

∼
/ D(X1 × X2)
∼

D(X1)′ ⊗D(X2)
∼
/ FunL(D(X1), D(X2))
Namely, for M1 ∈D(X1), M2 ∈D(X2), there is a canonical identity
π2∗(π!
1(−) ⊗(π!
1M1 ⊗π!
2M2)) ≃Γ(X1, M1 ⊗−) ⊗M2 ≃HomD(X1)(DX1M1, −) ⊗M2
between going around the upper right and the lower left parts of the diagram.
30
In this section, we will record some simple relative versions of the above assertions. While we
will consider very restrictive hypotheses, the assertions often fail in any more relaxed setting.
