---
doc_id: arxiv-hep-th-9310164v2
doc_title: "SPHERICAL CATEGORIES"
section_id: page-010
section_title: "Page 10"
section_number: null
pages: 10-10
source_pdf: 9310164v2.pdf
source_sha256: e0972e04667ccc47
toc_source: undetermined
doc_brief: "SPHERICAL CATEGORIES — This paper is a study of monoidal categories with duals where the ten- sor product need not be commutative."
---
10
JOHN W. BARRETT & BRUCE W. WESTBURY
M
Figure 1
Deﬁnition 2.4. Let a be any object in a pivotal category.
Then the monoid
End(a) has two trace maps, trL, trR: End(a) →End(e).
In a pivotal category
trL(f) is deﬁned to be the composite
e
ǫ(a∗)
−−−→a∗⊗a∗∗
1⊗τ −1(a)
−−−−−−→a∗⊗a
1⊗f
−−→a∗⊗a
τ(a∗)⊗τ(a)
−−−−−−−→
a∗∗∗⊗a∗∗
γ(a∗∗,a∗)
−−−−−−→(a∗⊗a∗∗)∗
ǫ∗(a∗)
−−−−→e∗
ν−→e
and trR(f) is deﬁned to be the composite
e
ǫ(a)
−−→a ⊗a∗
f⊗1
−−→a ⊗a∗
τ(a)⊗1
−−−−→a∗∗⊗a∗
γ(a∗,a)
−−−−→(a ⊗a∗)∗
ǫ∗(a)
−−−→e∗
ν−→e
In a strict pivotal category these deﬁnitions simplify to:
trL(f) = ǫ(a∗)(1 ⊗f)ǫ(a∗)∗
trR(f) = ǫ(a)(f ⊗1)ǫ(a)∗
These are called trace maps because they satisfy trL(fg) = trL(gf) and trR(fg) =
trR(gf).
Deﬁnition 2.5. A pivotal category is spherical if, for all objects a and all mor-
phisms f: a →a,
trL(f) = trR(f).
An equivalent condition is that trL(f) = trL(f ∗), for all f: a →a. Also, in a
spherical category, trL(f ⊗g) = trL(f). trL(g) (where the product is in End(e)) for
all f: a →a and all g: b →b.
In the rest of this paper we study additive spherical categories. This means that
each Hom set is a ﬁnitely generated abelian group; and that the data deﬁning the
spherical structure is compatible with the additive structure. This means that ⊗is
Z-bilinear, that ∗is Z-linear and all components of all the natural transformations
in the pivotal data are multilinear over Z.
In any additive monoidal category End(e) is a commutative ring (see [Kelly and
Laplaza 1980]) and we denote this ring by F. In particular the trace map, trL,
takes values in this ring. It follows that an additive monoidal category is F-linear,
by using the structure maps of λ and ρ, and that if the category is pivotal then the
data deﬁning the pivotal structure is F-linear.
The main examples of additive spherical categories arise as the category of rep-
resentations of a Hopf algebra with some additional structure. This is discussed in
detail in the next section.
