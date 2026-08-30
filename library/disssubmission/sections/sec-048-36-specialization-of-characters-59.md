---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-048-36-specialization-of-characters-59
section_title: "Specialization of characters 59"
section_number: 3.6
pages: 67-69
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
pointx in X. The passage to a different choice ofx corresponds to an inner
automorphism of the fundamental group, which is not seen on the level of
characters. So we have well-deﬁned restriction homomorphisms
i∗ : Π(X)l−→ Π(Xs)l, χ↦→ χs,
j∗ : Π(X)l−→ Π(Xη)l, χ↦→ χη.
Any characterχ∈ Π(X)l deﬁnes a local systemLχ on X, and forK∈ D(X)
the projection formula shows that
Ψ(Kχη) = i∗(Rj∗(K⊗Λ j∗(Lχ))) = i∗(Rj∗(K)⊗ΛLχ) = Ψ(K)χs.
To apply this formula in relation with the vanishing axiom from section 3.1,
one can use the following well-known result.
LEMMA 3.16. The pull-back homomorphismsi∗ and j∗ on characters
are an epimorphism resp. an isomorphism
Π(Xs)l Π(X)loooo ∼ // Π(Xη)l.
In particular, for all open dense subsets Us⊆ Π(Xs)l and Uη⊆ Π(Xη)l one
can ﬁndχ∈ Π(X)l such that
χs∈ Us and χη∈ Uη.
Proof. Choose any path from the point 0 inXs to the pointx in X. We
ﬁrst claim that the corresponding homomorphism
i∗ : π1(Xs,0)l−→ π1(X,x)l
is injective. To check this, we must by the criterion in [51, exp. V , cor. 6.8]
show that every ﬁnite´etale cover
f : Y−→Xs
of l-primary degree is dominated by a connected componentZ0s⊆ Zs of the
special ﬁbreZs of some ﬁnite´etale cover¯h : Z−→X of l-primary degree as
indicated in the following diagram.
Z0s

  // Zs   // Z
¯h

Y
f

Xs   // X
We can assume thatY is connected and that f is a Galois cover. Since
the prime l is invertible onS, it then follows thatY can be made into a
semiabelian variety such thatf is an isogeny [17]. So by [ 15, th. 7.3.5]
60 Chapter 3 – Perverse sheaves on semiabelian varieties
there exists an isogenyg : Xs−→Y such thatg◦ f and hence alsof◦g is
the multiplication byn = lν for someν. Thus it sufﬁces to treat the case
whereY = Xs and wheref = [n] : Xs−→Xs is the multiplication byn.
If we were dealing with an abelian scheme, we could now takeZ = X
and deﬁne¯h = [n] : X−→X to be the multiplication byn. However, for a
semiabelian scheme the multiplication byn is in general not a ﬁnite´etale
cover. To get around this problem we consider the N´eron model of the
generic ﬁbreXη, which will allow to ﬁnd a ﬁnite´etale coverh : Z−→X
whose base change underS−→S gives the desired¯h. But before we can
carry out this idea, we need to perform a base change to make sure that the
N´eron model does what we want.
Note that X and the special ﬁbreXs do not change if we replace the
given semiabelian schemeX−→S by a base changeX′ = X×S S′−→S′
whereS′ denotes the normalization ofS in a ﬁnite extension of the quotient
ﬁeld κ(η). After such a base change we can assume that alln-torsion points
of the generic ﬁbreXη are deﬁned overκ(η). Then the universal property
of the N´eron model
N−→S
of Xη implies that the multiplication morphism[n] : N−→N has constant
ﬁbre degree over its image and thus restricts to a ﬁnite´etale cover over
the image. This image contains the connected componentN0 which by
prop. 7.4.3 of loc. cit. is isomorphic toX. Hence if we deﬁneh : Z−→X
via the ﬁbre product in the Cartesian diagram
Z
h

  // N
[n]

X   // N
thenh will be a ﬁnite´etale cover ofX. The special ﬁbreZs will in general
not be connected, but on the connected component
Z0
s = Zs∩N0
s = N0
s = Xs
the coverh restricts to the multiplication morphismf = [n] : Xs−→Xs. So
we can putZ = Z×S S and take¯h to be the base change ofh.
Summing up, this shows that the homomorphismi∗ : π1(Xs)l−→π1(X)l
is an embedding. With the same arguments as above one also checks that
the homomorphismj∗ : π1(Xη)l−→π1(X)l is an isomorphism (surjectivity
is in this case clear because a ﬁnite ´etale cover of X is connected iff it
restricts to a connected cover ofXη). From this one deduces that the induced
homomorphisms
Π(X)l−→ Π(Xs)l and Π(X)l−→ Π(Xη)l
