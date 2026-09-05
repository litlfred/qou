---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS JEFFREY C. MORTON"
section_id: sec-006-43-units-and-counits
section_title: "Units and Counits"
section_number: 4.3
pages: 18-22
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
doc_brief: "2-VECTOR SPACES AND GROUPOIDS JEFFREY C. MORTON — This paper describes a relationship between essentially ﬁn ite groupoids and 2-vector spaces."
---
the adjunction in which f∗ is a left adjoint, and that in which it is a right adjoint.
These are described in the next section.
To describe f∗ in more detail, we use the fact that both Y and X are equivalent
to unions of ﬁnite groups, and so a V ect-presheaf on Y is a functor which assigns
a representation of Aut(y) to each object y∈ Y. Furthermore, if Y and X are
skeletal, then f : Y→ X on objects can be any set map, taking objects in Y to
objects in X. For morphisms, f gives, for each object y∈ Y, a homomorphism
from the group Aut(y) = hom( y, y) to the group Aut(f (y)).
So the pullback f ∗ is fairly straightforward: given F : X→ V ect, the pullback
f ∗F = F◦ f : Y→ V ect assigns to each y∈ Y the vector space F (f (y)), and
gives a representation of Aut( y) on this vector space where g : y→ y acts by f (g).
This is the pullback representation . If f is an inclusion, this is usually called the
restricted representation. The pushforward, or adjoint of pullback, for an inclusion
is generally called ﬁnding the induced representation. We remark that for the case
where f is an inclusion, Sternberg [17] gives some classical discussion of this f or
complex representations, as does Benson [6] for more modules ove r the group ring
with a more general base ring R. Here we use the same term for the more general
case when f is any homomorphism.
For any presheaf F , the pushforward f∗F is determined by the colimit for each
component of that essential preimage. Then for each x∈ X, we ﬁrst get:
(45)
⨁
g:f (y) → x
F (y)
2-VECTOR SPACES AND GROUPOIDS 19
Which is just the direct sum (i.e. biproduct) over the isomorphism clas ses in the
essential preimage of the corresponding vector spaces. Howeve r, this is not the
colimit: an object in the essential preimage is a pair ( y, g), but we note that if y
and y′ are isomorphic in Y, such isomorphisms induce isomorphisms of the spaces
F (y), and the colimit will be a quotient which identiﬁes these spaces. In ge neral, the
colimit will be a direct sum over isomorphism classes [ y] in the essential preimage.
Each term of the sum is isomorphic to the induced representation of F (y) under
the homomorphism determined by f .
Now, consider what the induced representations are for each isom orphism class.
Any isomorphism class [ y] of objects in Y determines a group G = Aut(y), and sim-
ilarly [ x]∈ X determines H = Aut(x). So this reduces to the case where Y and X
are just groups (seen as one-object categories), so we have a g roup homomorphism
f : G→ H. Using the induced algebra homomorphism f : C[G]→ C[H], one can
directly construct the induced homomorphism as a quotient: f∗V = C[H]⊗C[G] V .
So for general groupoids, with V = F (y), we have the direct sum:
(46) ( f∗F )(x) =
⨁
f (y)∼=x
C[Aut(x)]⊗C[Aut(y)] F (y)
Figure 5 illustrates the induced representation schematically, for a single object.
Figure 5. Induced Representation from Homomorphism
4.3. Units and Counits. We have observed that the pullback and pushforward
maps f ∗ and f∗ are both left and right adjoints. Thus there are two adjunctions
to consider: f ∗⊣ f∗, where pushforward is right adjoint to pullback; and f∗⊣ f ∗
where pushforward is left adjoint to pullback. For convenience, we refer to these
as the “right adjunction” and “left adjunction” respectively, aft er the position of
the pushforward. Each adjunction has unit and counit, so there a re four natural
transformations to describe. We will identify them as “right” and “le ft” unit and
counit following the convention above. Thus, we have:
ηL : Id[Y,V ect] =⇒ f ∗f∗(47)
ǫL :f∗f ∗ =⇒ Id[X,V ect](48)
ηR : Id[X,V ect] =⇒ f∗f ∗(49)
ǫR :f ∗f∗ =⇒ Id[Y,V ect](50)
20 JEFFREY C. MORTON
Once again, it is useful for practical calculations to have a coordina te-dependent
form for these maps, but there is a convenient intrinsic deﬁnition wh ich we shall
describe ﬁrst. Here again, we note that Benson [6] describes the c ase where f is an
inclusion, in a more general setting than the complex representatio ns we consider
here.
To begin with, we should describe the functors f ∗f∗ (“push-pull”), which is
an endofunctor on [ Y, V ect], and f∗f ∗ (“pull-push”), which is an endofunctor on
[X, V ect].
For the “push-pull”, f ∗f∗, we ﬁrst push a V ect-presheaf F on Y to one on X,
then pull back to Y. On each object y∈ Y, this gives a new presheaf where the
vector space F (y) is replaced by the pullback (i.e. induced representation of Aut(y))
of f∗F (f (y)). But f∗F is a presheaf on X, which, at each x∈ X, gives a colimit over
the essential preimage of x in Y, namely ⨁
[y′]|f (y′)∼=x C[Aut(x)]⊗C[Aut(y′)] F (y′).
In the case where x = f (y), this means we get:
(51) f ∗f∗F (x) =
⨁
[y′]|f (y′)∼=f (y)
C[Aut(f (y))]⊗C[Aut(y′)] F (y′)
thought of as a (left) representation of Aut(y) in the obvious way (i.e. g∈ Aut(y)
acts on this space as f (g)).
For the “pull-push”, f∗f ∗, we ﬁrst pull a V ect-presheaf G on X back to f ∗G
on Y. At each y ∈ Y, this assigns the vector space f ∗G(y) = G(f (y)) as a
representation of Aut(y). We then push forward to X to get, at each x∈ X, that:
(52) f∗f ∗G(x) =
⨁
[y]|f (y)∼=x
C[Aut(x)]⊗C[Aut(y)] G(x)
Note that a priori the last space would be G(f (y)), but since f (y)∼= x, we have also
that G(f (y))∼= G(x) as representations of Aut(y). Here we are implicitly taking
a colimit over the essential preimage of x, whose objects are not just y such that
f (y)∼= x, but rather such y equipped with a speciﬁc isomorphism. These therefore
induce speciﬁc isomorphisms of G(f (y)) and G(x), and the quotient implied by the
colimit identiﬁes these spaces.
Now, the description above accords with the usual description of t hese functors
in the left adjunction. Since the adjunction is ambidextrous, it applie s in both
cases, but to describe the unit and counit properly, we should note that in general
the canonical description of the left and right adjunctions are diﬀe rent. (Here again
we note that Benson [6] shows this for modules over general rings , which in our
case are the group algebras C[Aut(y)] etc., in the case of inclusion) We need to take
account of the speciﬁc isomorphism between the form we have pres ented (natural
for the left adjunction), and the form which is natural for the righ t adjunction.
The right adjoint is given as:
(53) f∗F (y) =
⨁
[y]|f (y)∼=x
homC[Aut(x)](C[Aut(y)], F (y))
(Note that the case for groups, namely when Y and X have only one object, appears
in each term of this direct sum). The Nakayama isomorphism gives the duality
between the two descriptions of f∗, in terms of hom C[Aut(x)] and⊗C[Aut(x)], by
means of the exterior trace map . The groupoid case is just the direct sum of group
2-VECTOR SPACES AND GROUPOIDS 21
cases, which looks like:
(54)
N :
⨁
[y]|f (y)∼=x
homC[Aut(y)](C[Aut(x)], F (y))→
⨁
[y]|f (y)∼=x
C[Aut(x)]⊗C[Aut(y)] F (y)
given by the exterior trace map in each factor of the sum:
(55) N :
⨁
[y]|f (y)∼=x
φy↦→
⨁
[y]|f (y)∼=x
1
#Aut(y)
∑
g∈Aut(x)
g−1⊗ φy(g)
Note that the exterior trace map gives an Aut(x)-invariant vector, but the normal-
ization is by the size of Aut(y). In the case where the homomorphism is an inclusion,
this is interpreted as trace given by a sum over cosets of Aut(y) in Aut(x), (which is
the situation usually presented in the group case). We remark here that this factor
will be important in interpreting our 2-functor Λ as a form of groupo idiﬁcation.
We can now write down the units and counits explicitly for both adjunc tions in
our preferred notation.
The left and right units are natural transformations which, for ea ch V ect-
presheaf on Y or X respectively, gives a morphism which is itself a natural trans-
formation. So, in particular the left unit
(56) ηL(F )(y) : F (y)→
⨁
[y′]|f (y′)∼=f (y)
C[Aut(f (y))]⊗C[Aut(y′)] F (y′)
is given by the natural map into the counit:
(57) v↦→
⨁
[y]
(1⊗ v)
Notice the unit map has no contribution in the image from any y′ which is not
in the isomorphism class [ y]. (It is a canonical map out of the limit which gives the
usual form for f∗.)
The right unit map
(58) ηR(G)(x) : G(x)→
⨁
[y]|f (y)∼=x
C[Aut(x)]⊗C[Aut(y)] f ∗G(x)
is found by composing the Nakayama isomorphism (55) with the group oid form of
the canonical map for the right adjoint. This is a direct sum, in which e ach factor
is given by the multiplication map:
(59) v↦→
(
g↦→g(v)
)
Thus, the composite is:
(60) ηR(G)(x) : v↦→
⨁
[y]|f (y)∼=x
1
#Aut(y)
∑
g∈Aut(x)
g−1⊗ g(v)
The left and right counits are natural transformations which, for each V ect-
presheaf on X or Y respectively, gives a morphism which is itself a natural trans-
formation. So in particular, the left counit
(61) ǫL(G)(x) :
⨁
[y]|f (y)∼=x
C[Aut(x)]⊗C[Aut(y)] f ∗G(x)→ G(x)
22 JEFFREY C. MORTON
is given by summing multiplication maps:
(62)
⨁
[y]|f (y)∼=x
gy⊗ v↦→
∑
[y]|f (y)∼=x
f (gy)v
The right counit map
(63) ǫR(F )(y) :
⨁
[y′]|f (y′)∼=f (y)
C[Aut(f (y))]⊗C[Aut(y′)] F (y′)→ F (y)
is given by composing the inverse of the Nakayama isomorphism (55) w ith the
evaluation map from the canonical form of the right adjoint. Again, the only factor
which contributes is y′∼= y, and so we have:
(64)
⨁
[y′]|f (y′)∼=f (y)
φy′↦→φy(1)
So ﬁnally, (by using that C[Aut(f (y))] is canonically isomorphic to its dual using
the canonical inner product on the group algebra) the composite is :
(65) ǫR(F )(y) :
⨁
[y′]|f (y′)∼=f (y)
gy′⊗ vy′↦→ #Aut(y)
#Aut(f (y)) gy(vy)
Here we are implicitly using the fact that the objects y′ in the essential preim-
age come equipped with isomorphisms f (y′)→ f (y) which induce speciﬁed isomor-
phisms Aut(f (y′))∼= Aut(f (y)). In the colimit which gave the direct sum over
isomorphism classes, these are all naturally identiﬁed.
A straightforward check (cancelling the Nakayama isomorphisms) v eriﬁes the
unit and counit identities:
(ǫL· Id f∗ )◦ (Id f∗· ηL) = Id f∗(66)
(Id f ∗· ǫL)◦ (ηL· Id f ∗ ) = Id f ∗(67)
(ǫR· Id f ∗)◦ (Id f ∗· ηR) = Id f ∗(68)
(Id f∗· ǫR)◦ (ηR· Id f∗ ) = Id f∗(69)
