---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-095-b2-difference-modules-over-difference-rings
section_title: "Difference modules over difference rings"
section_number: B.2
pages: 142-145
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
in the category ModDK,σ of left DK,σ-modules. We shall give two alternative
A.2. DIFFERENCE MODULES OVER DIFFERENCE RINGS
137
description of these modules.
To a left DK,σ-module M, we associate the pair (V, Φ), where the K-module
V is obtained from M by restriction of scalars and where Φ is the σ-linear (or
semi-linear) automorphism of V deﬁned by x 7→σ.x (external multiplication
in the DK,σ-module M). The property of σ-linearity means:
∀λ ∈K , ∀x ∈V , Φ(λx) = σ(λ)Φ(x).
Conversely, from such a pair (V, Φ), we can recover M as the DK,σ-
module having V
as underlying group and the external product deﬁned
by (P akσk).x := P akΦk(x).
The fact that we do get a DK,σ-module
depends on the σ-linearity of Φ. If the DK,σ-module N likewise corresponds
to the pair (W, Ψ), then DK,σ-linear maps from M to N are exactly the same
as K-linear maps f : V →W such that Ψ ◦f = f ◦Φ. The category ModDK,σ
is therefore equivalent to the following category: objects are the pairs (V, Φ),
where V is a K -module and Φ is a σ-linear automorphism of V ; morphisms
from (V, Φ) to (W, Ψ) are K-linear maps f : V →W such that Ψ ◦f = f ◦Φ.
From now on, we shall move freely from DK,σ-modules to pairs (V, Φ) and
conversely.
For any K-module V , write σ∗V the K-module obtained by restriction
of scalars through σ : K →K. This means that, writing µ.x the external
multiplication on V , the external multiplication on σ∗V is deﬁned by the
formula: (λ, x) 7→σ(λ).x. It follows that a σ-linear automorphism Φ : V →V
is just a K-linear isomorphism from V to σ∗V . This allows for yet another de-
scription of the category ModDK,σ. Noting that LK(V, W) = LK(σ∗V, σ∗W),
we will ﬁnd that many linear properties of DK,σ-modules (like the deﬁnition
and study of tensor products in paragraph A.2.4; or the deﬁnition and study
of “internal Hom” in paragraph A.2.5) are then immediate consequences of
general linear algebra over K.
From general properties of the restriction of scalars, it follows that a se-
quence M′ →M →M′′ in ModDK,σ is exact if, and only if, it is exact as a se-
quence of K-modules. However, if an exact sequence 0 →M′ →M →M′′ →
0 splits in ModDK,σ it splits in ModK, but not conversely. Any such exact se-
quence is isomorphic to one where M = (V, Φ), M′ = (V ′, Φ′), M′′ = (V ′′, Φ′′),
where V ′ is a sub-K-module of V and Φ′ = Φ|V , and where V ′′ = V/V ′ and
Φ′′ is induced by Φ.
138
APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFERENCE MODULES
Deﬁnition A.2.1. — A diﬀerence module over the diﬀerence C-algebra
(K, σ) (more shortly, over K) is a left DK,σ-module which, by restriction of
scalars to K, yields a ﬁnite rank projective K-module.
In our second description, this is a pair (V, Φ) such that V is a ﬁnite rank
projective K-module. We require that the module be projective for technical
reasons (such that good behaviour under extension of scalars). The ﬁniteness
condition is natural in the context of functional equations.
Example A.2.2. — We write 1 and call unit diﬀerence module the DK,σ-
module (K, σ). As a DK,σ-module, is isomorphic to DK,σ/DK,σ(σ −1).
For any invertible matrix A ∈GLn(K), putting ΦA(X) := A−1(σX), we deﬁne
a diﬀerence module (Kn, ΦA). For instance, if n = 1 and A = (1), this is 1.
Any diﬀerence module (V, Φ) such that V is free over K is isomorphic to some
(Kn, ΦA).
We write DiffMod(K, σ) the full subcategory of ModDK,σ with objects
the diﬀerence modules over K.
Like ModDK,σ, it is abelian and C-linear.
Thus, monomorphisms, epimorphisms, isomorphisms and exact sequences in
DiffMod(K, σ) are the same thing as in ModDK,σ. Moreover, since an exten-
sion of ﬁnite rank projective K-modules is a ﬁnite rank projective K-module
it follows that DiffMod(K, σ) is a thick subcategory of ModDK,σ, so that the
calculus of extensions in DiffMod(K, σ) is the restriction of the calculus of ex-
tensions in ModDK,σ. For instance, computing Exti(M, N) in DiffMod(K, σ)
or in ModDK,σ is the same.
Remark A.2.3. — Many constructions still make sense, and many proper-
ties remain true, and moreover useful, without the projectiveness or ﬁnite-
ness conditions.
For instance, one may want to consider diﬀerence exten-
sion rings of (K, σ), that is, diﬀerence rings (K′, σ′) such that K ⊂K′ and
σ′
|K = σ; in some interesting cases, K′ is not a ﬁnite K-module: for instance,
C({z}) ⊂C((z)). We will sometimes brieﬂy mention these generalisations,
for future reference.
A.2.3. The functor Γ. —
Let M
:= (V, Φ) and N
:= (W, Ψ) two
diﬀerence modules.
Write Lσ(V, W) := LK(V, σ∗W) the K-module of σ-
linear maps from V to W. For simplicity, we shall also (improperly) write
LK(M, N) := LK(V, W) and Lσ(M, N) := Lσ(V, W).
A.2. DIFFERENCE MODULES OVER DIFFERENCE RINGS
139
For any K-linear map f : V →W, the map Ψ ◦f −f ◦Φ is σ-linear from
V to W. The map tΦ,Ψ : f 7→Ψ ◦f −f ◦Φ from LK(M, N) to Lσ(M, N) is
C-linear and, by deﬁnition, Hom(M, N) is its kernel. We thus have an exact
sequence of C-modules:
0 →Hom(M, N) →LK(M, N)
tΦ,Ψ
−→Lσ(M, N).
This sequence is clearly functorial in M and in N (contravariant in M, covari-
ant in N). We shall see later that, under appropriate assumptions, its cokernel
is the module Ext(M, N) (theorem A.4.1).
Deﬁnition A.2.4. — The functor Γ of solutions is deﬁned as:
M ❀Γ(M) := Hom(1, M).
Proposition A.2.5. — The functor M ❀Γ(M) from diﬀerence modules to
C-modules is left exact, and one has an identiﬁcation:
Γ(M) = {v ∈V | Φ(v) = v}.
Proof. — The functoriality and exactness are plain. The identiﬁcation comes
as follows: under the usual identiﬁcation f 7→v := f(1) of LK(K, V ) with V ,
the condition Φ ◦f = f ◦σ translates into Φ(v) = v.
The i-th right derived functor of Γ is given by:
M ❀Γi(M) = Exti(1, M).
Remark A.2.6. — The contents of this paragraph remain valid without con-
ditions for all DK,σ-modules.
