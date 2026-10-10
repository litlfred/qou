---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-007-left-and-right-adjoints-of-kernels
section_title: "Left and right adjoints of kernels."
section_number: null
pages: 14-16
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasiz ing the importance of a pairing which generalizes Mukai’s pairi ng on the cohomology of K3"
---
In an arbitrary 2-category a given 1-morphism might or might not have a
left or a right adjoint, but in the 2-category V ar every 1-morphism, that is
every kernel, has both a left and a right adjoint. We will see b elow that for
a kernel Φ : X→ Y there are adjunctions
Φ∨ ◦ ΣY ⊣ Φ ⊣ ΣX ◦ Φ∨ ,
14
where Φ∨ : Y→ X means the object HomD(X×Y)(Φ, OX×Y) considered as an
object in D(Y × X). This should be compared with the fact that if M is an
A-B-bimodule then M∨ is naturally a B-A-bimodule. We shall see that the
two adjunctions above are related in some very useful ways.
Proposition 2. If X is a space and ∆ : X→ X × X is the diagonal embedding
then ∆∗ : D(X)→ D(X × X), the push-forward on derived categories, is a
monoidal functor where D(X) has the usual monoidal tensor product ⊗ and
D(X × X) has the composition ◦ as the monoidal structure.
Proof. The proof is just an application of the projection formula.
This has the following immediate consequence.
Lemma 3. If E and F are dual as objects in D(X) then ∆∗E and ∆∗F are
both left and right adjoint to each other as 1-morphisms in V ar.
In order not to hold-up the ﬂow of the narrative, the proofs of the re-
maining results from this section have been relegated to App endix A.
We begin with some background on the Serre kernel ΣX. Recall from
Section 2 that the anti-Serre kernel Σ− 1
X is deﬁned to be ∆∗ω− 1
X [− dim X],
and that the Serre kernel ΣX is denoted by a dashed-dotted line, while the
anti-Serre kernel Σ− 1
X is denoted by a dashed-dotted line with a horizontal
bar. The above proposition means that we actually have maps
, , ,
satisfying the following relations
= , = , = ,
and all obvious variations thereof.
In the appendix it is shown that for a kernel Φ there are natural mor-
phisms
ǫ
Φ : Φ ◦ ΣX ◦ Φ∨ → O∆ and γΦ : Σ− 1
X → Φ∨ ◦ Φ, denoted in the
following fashion, where the solid, upward oriented lines a re labelled with Φ
and the solid, implicitly downward oriented lines are label led by Φ∨ :
ǫ
Φ : and γΦ : .
The main property of
ǫ
Φ and γΦ is that if we deﬁne ǫΦ , ǫΦ , ηΦ and ηΦ via
ηΦ : := , ηΦ : := ,
15
ǫΦ :=
ǫ
Φ ∨ = , ǫΦ :=
ǫ
Φ = ,
then these are the units and counits of adjunctions
Φ∨ ◦ ΣY ⊣ Φ ⊣ ΣX ◦ Φ∨ .
