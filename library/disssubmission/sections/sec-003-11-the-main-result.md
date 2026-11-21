---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-003-11-the-main-result
section_title: "The main result"
section_number: 1.1
pages: 17-19
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
Let X be a complex abelian variety. For characters χ : π1(X,0) −→C∗
of the fundamental group we denote by Lχ the corresponding local system
of complex vector spaces on X of rank one, and for a bounded constructible
sheaf complex K ∈Db
c (X,C) we consider the twist Kχ = K ⊗C Lχ. With
these notations, our vanishing theorem can be formulated as
THEOREM 1.1. Let P ∈Perv(X,C) be a perverse sheaf. Then for most
characters χ we have
Hi(X,Pχ) = 0
for
i̸ = 0.
Here we use the following terminology: For abelian subvarieties A ⊆X
let K(A) be the group of characters χ : π1(X,0) −→C∗whose restriction
to the subgroup π1(A,0) ⊆π1(X,0) is trivial. We then say that a statement
holds for most characters χ if it holds for all χ in the complement of a thin
set of characters, where by a thin set of characters we mean a ﬁnite union
of translates χi ·K(Ai) for certain non-zero abelian subvarieties Ai ⊆X and
suitable characters χi of π1(X,0). The same terminology will be used in
theorems 1.4 and 1.5 below for line bundles L ∈Pic0(X).
The statement of theorem 1.1 can be sharpened as follows. Let Π(X)
denote the group of characters χ of the fundamental group π1(X,0); this is
a complex algebraic torus. For a perverse sheaf P ∈Perv(X,C) we deﬁne
the spectrum
S (P) =

χ ∈Π(X) | Hi(X,Pχ)̸ = 0 for some i̸ = 0
	
to be the locus of all characters χ ∈Π(X) for which the vanishing in the
above theorem fails in some cohomology degree. We will see in section 1.5
9
10
Chapter 1 – Vanishing theorems on abelian varieties
below that the spectrum S (P) is not just contained in a thin subset but
actually equal to such a set, in other words
S (P) =
n[
i=1
χi ·K(Ai)
is a ﬁnite union of translates of algebraic subtori K(Ai) ⊂Π(X) for certain
abelian subvarieties Ai ⊆X and χi ∈Π(X). Furthermore, if the perverse
sheaf P is of geometric origin in the sense of [10, sect. 6.2.4], we will see
that the characters χi can be chosen to be of ﬁnite order.
Our proof of theorem 1.1 is based on two ingredients. The main part
is an abstract Tannakian argument to be given in chapter 2 below: Using a
general construction of Andr´e and Kahn [1] we show that a certain quotient
of the category of semisimple perverse sheaves on X is a rigid symmetric
monoidal semisimple abelian category, and via a criterion by Deligne [30]
we deduce that this category is super Tannakian in a sense to be explained
below. To see that in the case at hand the construction leads to a Tannakian
category in the usual sense, we require the second ingredient of the proof
which is of a more geometric ﬂavour: A classiﬁcation of perverse sheaves
on X with Euler characteristic zero. This classiﬁcation is independent from
the Tannakian arguments and uses the theory of D-modules, extending the
results of Franecki and Kapranov [37]. We will discuss it in section 1.4,
and this is the only place where we need to work over the base ﬁeld C. The
arguments of chapter 2 also work for l-adic perverse sheaves on abelian
varieties over the algebraic closure of a ﬁnite ﬁeld.
Our theorem easily generalizes to a relative vanishing theorem for a
homomorphism of abelian varieties as we explain in section 1.2. From a
different point of view, it can also be reformulated as a statement about
constructible sheaves: Indeed, using d´evissage for the perverse t-structure
together with Verdier duality one checks that the theorem is equivalent to
the statement that any semi-perverse complex K satisﬁes Hi(X,Kχ) = 0 for
all i > 0 and most characters χ. Note that for any constructible sheaf F the
degree shift K = F[dim(SuppF)] is a semi-perverse sheaf complex, so we
in particular obtain
THEOREM 1.2. Let F be a constructible sheaf on X. Then for most
characters χ we have
Hi(X,Fχ) = 0
for
i > dim(SuppF).
This can be viewed as an analog of the Artin-Grothendieck afﬁne vanishing
theorem in the same way as one can consider the generic vanishing theorem
of Green and Lazarsfeld [47, th. 1] as an analog of the Kodaira-Nakano
vanishing theorem. Motivated by this observation, in section 1.3 we explain
