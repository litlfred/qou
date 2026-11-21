---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-060-81-2-categorical-notation
section_title: "2-Categorical Notation"
section_number: 8.1
pages: 143-145
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
morphisms of functors (i.e. natural transformations). The language and notation
of ordinary category theory that we used so far is not adequate for this purpose.
Therefore we will now introduce notation from the theory of 2-categories. (We will
not give a deﬁnition of a 2-category here; but it is basically the structure of Cat
that is mentioned below.) For more details on 2-categories the reader can look at
[102] or [171, Section 1].
Consider the set Cat of all categories. The set-theoretical aspects are neglected,
as explained in Subsection 1.1. (Brieﬂy, the precise solution is this: Cat is the set
of all U-categories; so Cat is a subset of a bigger Grothendieck universe, say V, and
it is a V-category.)
The set Cat is the set of objects of a 2-category. This means that in Cat there
are two kinds of morphisms: 1-morphisms between objects, and 2-morphisms be-
tween 1-morphisms. There are several kinds of compositions, and these have several
properties. All this will be explained below.
Suppose C0, C1, . . . are categories, namely objects of Cat.
The 1-morphisms
between them are the functors. The notation is as usual: F : C0 →C1 denotes a
functor.
Suppose F, G : C0 →C1 are functors.
The 2-morphisms from F to G are
the morphisms of functors (i.e. the natural transformations), and the notation is
η : F ⇒G.
The double arrow is the distinguishing notation for 2-morphisms.
When specializing to an object M ∈C0 we revert to the single arrow notation,
namely ηM : F(M) →G(M) is the corresponding morphism in C1. The diagram
depicting this is
C0
F
"
G
=
η


C1
We shall refer to such a diagram as a 2-diagram.
Each object (category) C has its identity 1-morphism (functor) IdC : C →C.
Each 1-morphism F has its identity 2-morphism (natural transformation) idF :
F ⇒F.
Now we consider compositions. For functors there is nothing new: given functors
F1 : C0 →C1 and F2 : C1 →C2, their composition, that we now call horizontal
This material will be published by Cambridge University Press as Derived Categories by Amnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works. c⃝Amnon Yekutieli, 2019.
143
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
composition, is the functor F2 ◦F1 : C0 →C2. The diagram is
C0
F1
/
F2 ◦F1
8
C1
F2
/ C2
This can be viewed as a commutative 1-diagram, or as a shorthand for the 2-diagram
C0
F1
/
F2 ◦F1
;
C1
F2
/
id


C2
in which id is the identity 2-morphism of F2 ◦F1.
The complication begins with compositions of 2-morphisms.
Suppose we are
given 1-morphisms Fi, Gi : Ci−1 →Ci and 2-morphisms ηi : Fi ⇒Gi.
In a
diagram:
C0
F1
"
G1
=
η1


C1
F2
"
G2
=
η2


C2
The horizontal composition is the morphism of functors η2 ◦η1 : F2 ◦F1 ⇒G2 ◦G1.
The diagram is
C0
F2 ◦F1
$
G2 ◦G1
:
η2 ◦η1


C2
Exercise 8.1.1. For an object M ∈C0, give an explicit formula for the morphism
(η2 ◦η1)M : (F2 ◦F1)(M) →(G2 ◦G1)(M)
in the category C2.
Suppose we are given 1-morphisms E, F, G : C0 →C1, and 2-morphisms
ζ : E ⇒F and η : F ⇒G. The diagram depicting this is
C0
E

F
/
G
I
ζ


η


C1
The vertical composition of ζ and η is the 2-morphism η ∗ζ : E →G. Notice the
new symbol for this operation. The corresponding diagram is
C0
E
$
G
:
η ∗ζ


C1
Exercise 8.1.2. For an object M ∈C0, give an explicit formula for the morphism
(η ∗ζ)M : E(M) →G(M) in the category C1.
144
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Something intricate occurs in the situation shown in the next diagram.
C0
E1

F1
/
G1
I
ζ1 

η1


C1
E2

F2
/
G2
I
ζ2 

η2


C2
It turns out that
(η2 ∗ζ2) ◦(η1 ∗ζ1) = (η2 ◦η1) ∗(ζ2 ◦ζ1)
as morphisms E2 ◦E1 ⇒G2 ◦G1. This is called the exchange property.
Exercise 8.1.3. Prove the exchange property.
Just like abstract categories, we can talk about triangulated categories. There is
the 2-category TrCat of all (K-linear) triangulated categories. The objects here are
the triangulated categories (K, T); the 1-morphisms are the triangulated functors
(F, τ); and the 2-morphisms are the morphisms of triangulated functors η. This is
what we are going to use later in this section.
