---
doc_id: arxiv-hep-th-9310164v2
doc_title: "SPHERICAL CATEGORIES"
section_id: page-009
section_title: "Page 9"
section_number: null
pages: 9-9
source_pdf: 9310164v2.pdf
source_sha256: e0972e04667ccc47
toc_source: undetermined
doc_brief: "SPHERICAL CATEGORIES — This paper is a study of monoidal categories with duals where the ten- sor product need not be commutative."
---
SPHERICAL CATEGORIES
9
Deﬁnition 2.1. A pivotal category is a category with duals together with a mor-
phism ǫ(c): e →c ⊗c∗for each object c ∈C.
The conditions on the components of ǫ are the following:
(1) For all morphisms, f: a →b, the following diagram commutes
e
ǫ(a)
−−−−→a ⊗a∗
ǫ(b)
y
yf⊗1
b ⊗b∗−−−−→
1⊗f ∗
b ⊗a∗
(2) For all objects a, the following composite is the identity map of a∗:
a∗
λ−1(a∗)
−−−−−→e ⊗a∗
ǫ(a∗)⊗1
−−−−−→(a∗⊗a∗∗) ⊗a∗
α(a∗,a∗∗,a∗)
−−−−−−−−→a∗⊗(a∗∗⊗a∗)
1⊗γ(a∗,a)
−−−−−−→
a∗⊗(a ⊗a∗)∗
1⊗ǫ(a)∗
−−−−−→a∗⊗e∗
1⊗ν−1
−−−−→a∗⊗e
ρ(a∗)
−−−→a∗
(3) For all objects a and b the following composite is required to be ǫ(a ⊗b):
e
ǫ(a)
−−→a ⊗a∗
1⊗λ−1(a∗)
−−−−−−−→a ⊗(e ⊗a∗)
1⊗(ǫ(b)⊗1)
−−−−−−−→a ⊗((b ⊗b∗) ⊗a∗)
1⊗α(b,b∗,a∗)
−−−−−−−−→a ⊗(b ⊗(b∗⊗a∗))
α−1(a,b,b∗⊗a∗)
−−−−−−−−−−→(a ⊗b) ⊗(b∗⊗a∗)
1⊗γ(b,a)
−−−−−→(a ⊗b) ⊗(a ⊗b)∗
These conditions imply that the strict extension is a pivotal category in the
sense of [Freyd and Yetter 1989]. This is clear once it has been shown that ǫ is
well-deﬁned on the strict extension.
The functor ∗and the maps ǫ are not independent. The maps ǫ determine ∗.
This observation is in [Kelly and Laplaza 1980] where the maps ǫ are taken as more
fundamental than ∗. In [Turaev 1992] it is noted that the maps ǫ also determine γ.
Lemma 2.2. In any pivotal category, for any morphism f: a →b the following
composite is f ∗:
b∗
ρ−1(b∗)
−−−−−→b∗⊗e
1⊗ǫ(a)
−−−−→b∗⊗(a ⊗a∗)
1⊗(f⊗1)
−−−−−→b∗⊗(b ⊗a∗)
α−1(b∗,b,a∗)
−−−−−−−−→(b∗⊗b)⊗a∗
(τ(b∗)⊗τ(b))⊗1
−−−−−−−−−−→(b∗∗∗⊗b∗∗)⊗a
γ(b∗∗,b∗)⊗1
−−−−−−−→(b∗⊗b∗∗)∗⊗a∗
ǫ∗(b∗)⊗1
−−−−−→e∗⊗a∗
ν−1⊗1
−−−−→e ⊗a∗
λ(a∗)
−−−→a∗
Proof. This follows directly from conditions (1) and (2) of the preceding deﬁnition.
Remark 2.3. Note also that a pivotal category is closed, in the sense that there are
natural isomorphisms, for all a, b and c;
Hom(a ⊗b, c) ∼= Hom(b, a∗⊗c)
Hom(a, b ⊗c) ∼= Hom(a ⊗c∗, b)
Hom(a ⊗b, c) ∼= Hom(a, c ⊗b∗)
Hom(a, b ⊗c) ∼= Hom(b∗⊗a, c)
