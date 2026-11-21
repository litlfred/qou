---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-022-36-specialization-of-characters
section_title: "Specialization of characters"
section_number: 3.6
pages: 66-69
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
Let X −→S be a semiabelian scheme as above. Since we assumed the
prime number l to be invertible on S, we know from [17] that the (tame)
pro-l fundamental groups
π1(Xη,0)l = π t
1(Xη,0)l
and
π1(Xs,0)l = π t
1(Xs,0)l
are free Zl-modules of ﬁnite rank. However, the basic example of abelian
varieties with semiabelian reduction illustrates that in general π1(Xs,0)l
will have strictly smaller rank than π1(Xη,0). To complete the proof of
lemma 3.13 we thus need to justify why in passing from the generic to the
special ﬁbre, we retain enough characters to apply the generic vanishing
assumption from section 3.1 on both ﬁbres. To this end, let Π(X)l denote
the group of all continuous characters of π1(X,x)l for any chosen geometric
3.6. Specialization of characters
59
point x in X. The passage to a different choice of x corresponds to an inner
automorphism of the fundamental group, which is not seen on the level of
characters. So we have well-deﬁned restriction homomorphisms
i∗:
Π(X)l −→Π(Xs)l,
χ 7→χs,
j∗:
Π(X)l −→Π(Xη)l,
χ 7→χη.
Any character χ ∈Π(X)l deﬁnes a local system Lχ on X, and for K ∈D(X)
the projection formula shows that
Ψ(Kχη) = i∗(R j∗(K ⊗Λ j∗(Lχ))) = i∗(R j∗(K)⊗Λ Lχ) = Ψ(K)χs.
To apply this formula in relation with the vanishing axiom from section 3.1,
one can use the following well-known result.
LEMMA 3.16. The pull-back homomorphisms i∗and j∗on characters
are an epimorphism resp. an isomorphism
Π(Xs)l
Π(X)l
oo
∼
/ Π(Xη)l.
In particular, for all open dense subsets Us ⊆Π(Xs)l and Uη ⊆Π(Xη)l one
can ﬁnd χ ∈Π(X)l such that
χs ∈Us
and
χη ∈Uη.
Proof. Choose any path from the point 0 in Xs to the point x in X. We
ﬁrst claim that the corresponding homomorphism
i∗:
π1(Xs,0)l −→π1(X,x)l
is injective. To check this, we must by the criterion in [51, exp. V, cor. 6.8]
show that every ﬁnite ´etale cover
f :
Y −→Xs
of l-primary degree is dominated by a connected component Z0
s ⊆Zs of the
special ﬁbre Zs of some ﬁnite ´etale cover ¯h : Z −→X of l-primary degree as
indicated in the following diagram.
Z0
s

 
/ Zs  
/ Z
¯h

Y
f

Xs  
/ X
We can assume that Y is connected and that f is a Galois cover. Since
the prime l is invertible on S, it then follows that Y can be made into a
semiabelian variety such that f is an isogeny [17]. So by [15, th. 7.3.5]
60
Chapter 3 – Perverse sheaves on semiabelian varieties
there exists an isogeny g : Xs −→Y such that g ◦f and hence also f ◦g is
the multiplication by n = lν for some ν. Thus it sufﬁces to treat the case
where Y = Xs and where f = [n] : Xs −→Xs is the multiplication by n.
If we were dealing with an abelian scheme, we could now take Z = X
and deﬁne ¯h = [n] : X −→X to be the multiplication by n. However, for a
semiabelian scheme the multiplication by n is in general not a ﬁnite ´etale
cover. To get around this problem we consider the N´eron model of the
generic ﬁbre Xη, which will allow to ﬁnd a ﬁnite ´etale cover h : Z −→X
whose base change under S −→S gives the desired ¯h. But before we can
carry out this idea, we need to perform a base change to make sure that the
N´eron model does what we want.
Note that X and the special ﬁbre Xs do not change if we replace the
given semiabelian scheme X −→S by a base change X′ = X ×S S′ −→S′
where S′ denotes the normalization of S in a ﬁnite extension of the quotient
ﬁeld κ(η). After such a base change we can assume that all n-torsion points
of the generic ﬁbre Xη are deﬁned over κ(η). Then the universal property
of the N´eron model
N −→S
of Xη implies that the multiplication morphism [n] : N −→N has constant
ﬁbre degree over its image and thus restricts to a ﬁnite ´etale cover over
the image. This image contains the connected component N0 which by
prop. 7.4.3 of loc. cit. is isomorphic to X. Hence if we deﬁne h : Z −→X
via the ﬁbre product in the Cartesian diagram
Z
h

 
/ N
[n]

X  
/ N
then h will be a ﬁnite ´etale cover of X. The special ﬁbre Zs will in general
not be connected, but on the connected component
Z0
s = Zs ∩N0
s = N0
s = Xs
the cover h restricts to the multiplication morphism f = [n] : Xs −→Xs. So
we can put Z = Z ×S S and take ¯h to be the base change of h.
Summing up, this shows that the homomorphism i∗: π1(Xs)l −→π1(X)l
is an embedding. With the same arguments as above one also checks that
the homomorphism j∗: π1(Xη)l −→π1(X)l is an isomorphism (surjectivity
is in this case clear because a ﬁnite ´etale cover of X is connected iff it
restricts to a connected cover of Xη). From this one deduces that the induced
homomorphisms
Π(X)l −→Π(Xs)l
and
Π(X)l −→Π(Xη)l
