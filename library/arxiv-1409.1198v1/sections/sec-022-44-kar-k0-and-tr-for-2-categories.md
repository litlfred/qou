---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-022-44-kar-k0-and-tr-for-2-categories
section_title: "Kar, K0 and Tr for 2-categories"
section_number: 4.4
pages: 29-30
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
---
deﬁned for (additive) linear categories to the 2-categorical setting. A 2-category C is linear if the
categories C(x, y) are linear for all x, y ∈Ob(C) and the composition functor preserves the linear
structure (see [10] for more details). Similarly, an additive linear 2-category is a linear 2-category in
which the categories C(x, y) are also additive and composition is given by an additive functor.
The following deﬁnitions extend the Karoubi envelope, split Grothendieck group, and trace to the
2-categorical setting.
• Given an additive linear 2-category C, deﬁne the split Grothendieck group K0(C) of C to
be the linear category with Ob(K0(C)) = Ob(C) and with K0(C)(x, y) := K0(C(x, y)) for
any two objects x, y ∈Ob(C). For [f]∼
= ∈Ob(K0(C)(x, y)) and [g]∼
= ∈Ob(K0(C)(y, z)) the
composition in K0(C) is deﬁned by [g]∼
= ◦[f]∼
= := [g ◦f]∼
=.
• The trace Tr(C) of a linear 2-category is the linear category with Ob(Tr(C)) = Ob(C) and
with Tr(C)(x, y) := Tr(C(x, y)) for any two objects x, y ∈Ob(C). For σ ∈EndC(x,y) and
τ ∈EndC(y,z), we have [τ] ◦[σ] = [τ ◦σ]. The identity morphism for x ∈Ob(Tr(C)) = Ob(C)
is given by [1Ix].
• The Karoubi envelope Kar(C) of a linear 2-category C is the linear 2-category with Ob(Kar(C)) =
Ob(C) and with hom categories Kar(C)(x, y) := Kar(C(x, y)).
The composition functor
Kar(C)(y, z) × Kar(C)(x, y) →Kar(C)(x, z) is induced by the universal property of the
Karoubi envelope from the composition functor in C.
The fully-faithful additive functors
C(x, y) →Kar(C(x, y)) combine to form an additive 2-functor C →Kar(C) that is universal
with respect to splitting idempotents in the Hom-categories C(x, y).
30
ANNA BELIAKOVA, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. LAUDA
For categoriﬁcation using K0 it is necessary to consider the 2-category Kar(U(sln)). We will denote
by ˙U the Karoubi envelope of U.
The homomorphisms hC(x,y) taken over all objects x, y ∈Ob(C) give rise to a linear functor
(4.39)
hC : K0(C) →Tr(C)
which is the identity map on objects and sends K0(C)(x, y) →Tr(C)(x, y) via the homomorphism
hC(x,y). It is easy to see that this assignment preserves composition since
hC([g]∼
= ◦[f]∼
=) = hC([g ◦f]∼
=) = [1g◦f] = [1g ◦1f] = [1g] ◦[1f] = hC([g]∼
=) ◦hC([f]∼
=).
(4.40)
In the following sections we study the trace and K0 for the 2-categories ˙U(sln).
