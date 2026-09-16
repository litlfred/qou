---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-008-33-the-trace-and-idempotent-completions
section_title: "The trace and idempotent completions"
section_number: 3.3
pages: 15-16
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a high er categorical level."
---
/CZ
is an endomor-
phism p : V →V satisfying the relation p2 =p. In this case, (Id V −p) :V →V is also an idempotent
and together these two idempotents decompose the space V into a direct sum of the image of the
projection p and the image of the projection Id V −p.
More generally, idempotents can be deﬁned in any category C as endomorphisms e : x →x satisfying
e2 =e, but here we will always assume that C is a linear category.
e
e
x
x
= e
x
x
An idempotent e : x →x in C is said to split if there is an object y and morphisms g : x →y,h : y →x
such that hg =e and gh = 1 y.
h
g
x
x
= e
x
x
g
h
y
y
= 1y
y
y
Unfortunately, even in an additive category C it is not always possible to split idempotents. Such
phenomenon occurs quite often when studying additive categories C deﬁned diagrammatically by gen-
erators and relations [36, 51, 5]. In this case, making sense out of the “image” of a diagram is not
usually possible. A common solution is to enlarge the category C by passing to the Karoubi envelope
Kar(C) (also called idempotent or Cauchy completion ) of C. The Karoubi envelope can be thought of
as a minimal enlargement of the category C in which all idempotents split.
More formally, the Karoubi envelope Kar( C) is the category whose objects are pairs ( x,e ) of objects
x ∈ Ob(C) and an idempotent endomorphism e :x →x in C. The morphisms
f : (x,e ) → (y,e ′)
are morphisms f : x →y in C such that f =e′fe , or alternatively such that
f
x
y
= f
e
e′
x
y
.
Composition is induced by the composition in C and the identity morphism is e : (x,e ) → (x,e ). Kar( C)
is equipped with a linear category structure.
16 ANNA BELIAKOV A, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. L AUDA
We can identify (x, 1x) with the object x of C. This identiﬁcation gives rise to a natural embedding
functor ι : C → Kar(C) such that ι(x) = ( x, 1x) for x ∈ Ob(C) and ι(f : x → y) = f . The Karoubi
envelope Kar(C) has the universality property that if F : C → D is a linear functor to a linear category
D with split idempotents, then F extends to a functor from Kar( C) to D uniquely up to natural
isomorphism [10, Proposition 6.5.9].
Example 4. Consider the Temperley-Lieb category TL deﬁned over C(q), where q is an indeter-
minant with q = −A2. The Karoubi envelope Kar(TL) is equivalent as a category to the c ategory
of ﬁnite-dimensional representations of quantum sl2 ([29] and [53]). The irreducible N -dimensional
representation arises as the image of a certain idempotent called Jones-Wenzl idempotent.
Exercise 11. Show that the Karoubi envelope of an additive category is add itive.
The following proposition illustrates one of the key advantages of th e trace, namely its invariance
under passing to the Karoubi envelope.
Proposition 3.2. The map Tr(ι) : Tr( C) − →Tr(Kar(C)) induced by ι is bijective.
Proof. Recall that an endomorphism f : (x,e ) → (x,e ) in Kar( C) is just a morphism f : x → x in C
satisfying the condition that f =efe . Deﬁne a map u : Tr(Kar( C)) − →Tr(C) sending [f ] ∈ Tr(Kar(C))
to [f ] ∈ Tr(C). Then one can check that u is an inverse to Tr( ι). □
Example 5. Adding Jones-Wenzl idempotents as objects into TL does not aﬀec t Tr(TL).
