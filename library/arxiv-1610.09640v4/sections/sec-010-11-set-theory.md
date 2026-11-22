---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-010-11-set-theory
section_title: "Set Theory"
section_number: 1.1
pages: 25-25
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
theory. The blanket assumption is that we are given a Grothendieck universe U.
This is a “large” inﬁnite set. A small set, or a U-small set, is a set S that is an
element of U. We want all the products Q
i∈I Si and disjoint unions `
i∈I Si, with
I and Si small sets, to be small sets too. (This requirement is not crucial for us,
and it is more a matter of convenience. When dealing with higher categories, one
usually needs a hierarchy of universes anyhow.) We assume that the axiom of choice
holds in U.
A U-category is a category C whose set of objects Ob(C) is a subset of U, and for
every C, D ∈Ob(C) the set of morphisms HomC(C, D) is small. If Ob(C) is also
small, then C is called a small category. See [5], [102] or [76, Section 1.1]. Another
approach, involving “sets” vs “classes”, can be found in [113].
We denote by Set the category of all small sets. So Ob(Set) = U, and Set is a
U-category. A group (or a ring, etc.) is called small if its underlying set is small.
We denote by Grp, Ab, Rng and Rngc the categories of small groups, small abelian
groups, small rings and small commutative rings respectively. For a small ring A
we denote by Mod A the category of small left A-modules.
By default we work with U-categories, and from now on U will remain implicit.
There are several places in which we shall encounter set theoretical issues (regarding
functor categories and localization of categories); but these problems can be solved
by introducing a bigger universe V such that U ∈V.
