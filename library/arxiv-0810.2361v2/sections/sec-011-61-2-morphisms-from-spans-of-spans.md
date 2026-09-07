---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS JEFFREY C. MORTON"
section_id: sec-011-61-2-morphisms-from-spans-of-spans
section_title: "2-Morphisms from Spans of Spans"
section_number: 6.1
pages: 30-35
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
doc_brief: "2-VECTOR SPACES AND GROUPOIDS JEFFREY C. MORTON — This paper describes a relationship between essentially ﬁn ite groupoids and 2-vector spaces."
---
(114), which weakly commutes up to isomorphisms ζs and ζt, gives rise to a diagram
of pullback functors:
(115) [ X1, V ect]
s∗
/d15/d15
[A1, V ect]
s2 ∗
/d38/d38/d78/d78/d78/d78/d78/d78/d78/d78/d78/d78/d78
s1 ∗
/d56/d56/d112/d112/d112/d112/d112/d112/d112/d112/d112/d112/d112
[Y, V ect] [ A2, V ect]
t1 ∗
/d102/d102/d78 /d78 /d78 /d78 /d78 /d78 /d78 /d78 /d78 /d78 /d78
t2∗
/d120/d120/d112 /d112 /d112 /d112 /d112 /d112 /d112 /d112 /d112 /d112 /d112
[X2, V ect]
t∗
/d79/d79
which commutes up to isomorphisms:
(116) ζ∗
s : s∗◦ s∗
1(V ) ˜→t∗◦ s∗
2(V )
and similarly
(117) ζ∗
t : s∗◦ t∗
1(V ) ˜→t∗◦ t∗
2(V )
We want to get a natural transformation from Λ( X1) and Λ( X2) from this dia-
gram. In section 6.2 we show how this can be described as a “pull-push ” process,
similar to the one used to deﬁne the 2-linear maps, but ﬁrst it can be d eﬁned in
terms of the unit and counit maps we have already deﬁned.
Deﬁnition 6.1.1. Given a span between spans, Y : X1→ X2, for X1, X2 : A1→ A2,
then
(118) Λ( Y ) : Λ( X1)→ Λ( X2)
is the natural transformation given as
(119) Λ( Y ) = ǫL,t◦ ((ζt)∗⊗ ((ζs)∗)−1)◦ ηR,s : (t1)∗s∗
1 =⇒ (t2)∗s∗
2
where ǫL,t is the counit (61) for the left adjunction associated to t, and ηR,s is the
unit (58) for the right adjunction associated to s.
We comment here that this composition of left unit followed by right co unit can
be interpreted as a “pull-push” in a sense that can be seen more pre cisely when
we consider this natural transformation in coordinates. In the sp ecial case where
Ai = 1, this recovers groupoidiﬁcation in the sense of Baez and Dolan, a s shown in
Theorem 6.2.1.
Remark 6.1.2. Henceforth, we will assume that the diagram (114) commutes
strictly - that is, ζs and ζt are identity 2-morphisms. This is a mild assumption,
since the diagram can always be “strictiﬁed” by taking equivalent gro upoids for
source and target which are skeletal. Similar arguments will follow thr ough if not,
but in this simpler case, we simply have:
(120) Λ( Y ) = ǫL,t◦ ηR,s : (t1)∗s∗
1 =⇒ (t2)∗s∗
2
2-VECTOR SPACES AND GROUPOIDS 31
For our construction to give a 2-functor, this must agree with com position in two
ways. The ﬁrst is strict preservation of vertical composition; the second is preser-
vation of horizontal composition as strictly as possible (i.e. up to the isomorphisms
β which make comparison possible - as we will see). We will show in
Lemma 6.1.3. The assignment Λ( Y ) to spans of spans given in Deﬁnition 6.1.1
preserves vertical composition strictly: Λ( Y ′◦ Y ) = Λ( Y ′)◦ Λ( Y ).
Proof. Suppose we have a vertical composite of two spans between spans , here
written as 2-cells:
(121) A1
X1
/d28/d28X2 /d47/d47
X3
/d66/d66A2
Y/d11/d19
Y ′
/d11/d19
The composition is given by a weak pullback (taken up to isomorphism) - that
is, a diagram of the form (11), with the Y and Y ′ in place of X and X ′, and the Xi
in place of the Ai. We use the same notation for the maps in all these spans. Of
course, each object in (121) comes equipped with (commuting) map s into A1 and
A2, but we can ignore these here.
So the source and target maps for Y are s and t, and those for Y ′ are s′ and t′,
and we can easily write:
(122) Λ( Y ′)◦ Λ( Y ) = ǫL,t′◦ ηR,s′◦ ǫL,t◦ ηR,s
Now, to write Λ( Y ′◦ Y ), we recall that the vertical composite is formed by weak
pullback of spans, with the resulting source and target maps s◦ S and t′◦ T , where
the groupoid in the span Y ′◦Y is the comma category whose objects are of the form
(y′, g2, y), with g2 : t(y)→ s′(y′) in X2, and S and T are the natural projections
onto Y and Y ′. Then of course
(123) Λ( Y ′◦ Y ) = ǫL,(t′◦T )◦ ηR,(s◦S)
Now, a composite of adjunctions is an adjunction (see for instance MacLane [13]
IV.8), and the unit and counit of the composite is given in a standard w ay, so we
have:
(124) ǫL,(t′◦T ) = ǫL,t′◦ (Id(t′)∗⊗ǫL,T⊗ Id(t′)∗ )
and
(125) ηR,(s◦S) = (Id s∗⊗ηR,S⊗ Ids∗ )◦ ηR,s
So we get
(126) Λ( Y ′◦ Y ) = ǫL,t′◦ (Id(t′)∗⊗ǫL,T⊗ Id(t′)∗ )◦ (Ids∗⊗ηR,S⊗ Ids∗ )◦ ηR,s
So to get strict composition, we just need that
(127) (Id (t′)∗⊗ǫL,T⊗ Id(t′)∗)◦ (Ids∗⊗ηR,S⊗ Ids∗ ) = ηR,s′◦ ǫL,t
This follows the same pattern as the proof for the fact that Λ weak ly preserves
composition of morphisms. Note that the two sides of this expressio n are the top
and bottom of a (weak) pullback square. So in particular, the argum ent for weak
32 JEFFREY C. MORTON
preservation of composition of spans shows that we also have a pullb ack square for
the induced functors.
In particular (ignoring the identity maps), we ﬁrst get the right unit for S :
Y ′◦ Y→ Y , which at y∈ G(y)∼= G(a1) gives:
(128) ηR,S : v↦→
⨁
[(y,f,y ′)]
1
#Aut(y, f, y ′)
∑
g∈Aut(y)
(g−1)⊗ g(v)
and the left counit for T : Y ′◦ Y→ Y ′ takes this to. So this gives
(129) ǫL,T◦ ηR,S : v↦→
∑
[(y,f,y ′)]
1
#Aut(y, f, y ′)
∑
g∈Aut(y)
(g−1)⊗ g(v)
since the target space is now already a tensor product over C[Aut(x2)]. Similarly,
on the other side we have ﬁrst the left counit for t : Y→ X2, then the right unit for
s′ : Y ′→ X2, giving:
(130) ηR,s′◦ ǫL,t : v↦→
∑
[y′]|s′(y′)∼=t(y)
1
#Aut(t(y))
∑
g∈Aut(x2)
g−1⊗ g(v)
Since the sources and targets of the maps (61) and (58) are in a pu llback square,
the coeﬃcients arising from the Nakayama isomorphisms will yield the s ame group
averages, and the terms of the implied direct sum correspond pairw ise. So these
maps are indeed equal. □
We also must show that Λ respects horizontal composition weakly. T o make this
clear, it will be convenient to write source and target 2-linear maps in the form
(108) and (109).
Lemma 6.1.4. The assignment Λ( Y ) to spans of spans given by Deﬁnition 6.1.1
preserves horizontal composition strictly, up to the isomo rphism weakly preserving
composition of the source and target morphisms:
(131)
Λ( A1)
Λ( X ′ 1◦X1)
/d35/d35
Λ( X ′ 2◦X2)
/d59/d59
Λ( X1)
/d42/d42
Λ( X2)
/d52/d52 Λ( A′
2)
Λ( X ′
1)
/d42/d42
Λ( X ′2)
/d52/d52 Λ( A3)Λ( Y )
/d11/d19
Λ( Y ′)
/d11/d19
βX1,X′ 1
/d11/d19
β−1
X2,X′ 2
/d11/d19
= Λ( A1)
Λ( X ′ 1◦X1)
/d38/d38
Λ( X ′ 2◦X2)
/d56/d56Λ( A3)Λ( Y ′◦Y )
/d11/d19
Proof. (Elsewhere, we have used the same notation for horizontal and ve rtical com-
position of all kinds, to simplify notation and because context made t his unambigu-
ous. In this proof it will be helpful to distinguish the two, so we write v ertical com-
position with no symbol, concatenating natural transformations b etween 2-linear
maps.)
2-VECTOR SPACES AND GROUPOIDS 33
Begin by writing the spans explicitly. The situation for a horizontal co mposite
of 2-morphisms in Span( FinGpd) looks like:
(132) X ′1◦ X1
S1
/d122/d122/d118 /d118 /d118 /d118 /d118 /d118 /d118 /d118 /d118 T1
/d36/d36/d72/d72/d72/d72/d72/d72/d72/d72/d72
X1
α1
∼
/d43/d51
s1
/d126/d126/d125 /d125 /d125 /d125 /d125 /d125 /d125 /d125 t1
/d36/d36/d73/d73/d73/d73/d73/d73/d73/d73/d73/d73 X ′
1
s′
1
/d122/d122/d118 /d118 /d118 /d118 /d118 /d118 /d118 /d118 /d118 /d118 t′
1
/d32/d32/d65/d65/d65/d65/d65/d65/d65/d65
A1 Y
s
/d79/d79
t
/d15/d15
σ/d111/d111/d95 /d95 /d95 τ /d47/d47/d95/d95/d95/d95 A2 Y ′
s′
/d79/d79
t′
/d15/d15
σ′
/d111/d111/d95 /d95 /d95 /d95 τ ′
/d47/d47/d95 /d95 /d95 A3
X2
α2
∼
/d43/d51
s2
/d96/d96/d65 /d65 /d65 /d65 /d65 /d65 /d65 /d65 t2
/d58/d58/d118/d118/d118/d118/d118/d118/d118/d118/d118/d118
X ′
2
s′
2
/d100/d100/d73 /d73 /d73 /d73 /d73 /d73 /d73 /d73 /d73 /d73 t′
2
/d62/d62/d125/d125/d125/d125/d125/d125/d125/d125
X ′2◦ X2
S2
/d100/d100/d72 /d72 /d72 /d72 /d72 /d72 /d72 /d72 /d72 T2
/d58/d58/d118/d118/d118/d118/d118/d118/d118/d118/d118
(Note that here again we are assuming the 2-morphisms Y and Y ′ are strict, so
that s1◦ s = s2◦ t and similarly for the other composites. We represent these by
the dotted arrows σ, τ , σ′ and τ ′. As before, a similar argument would go through
if these spans of span maps were only weakly commuting, but we would need the ζ
natural transformations as discussed for (12)).
Now, the functor Λ assigns 2-linear maps to the spans X1, X2, X ′1, and X ′2, and
their composites, and natural transformations to Y and Y ′. Then the horizontal
composite is a natural transformation between 2-linear maps:
(133) Λ( Y ′)◦ Λ( Y ) : Λ( X ′
1)◦ Λ( X1)→ Λ( X ′
2)◦ Λ( X2)
And we can calculate as in the proof of Theorem 6.1.3 that:
(134) Λ( Y ′)(a1) = ǫL,t′ηR,s′ : v↦→
⨁
[y]|s′(y′)∼=x1
#Aut(y)
#Aut(y, f, y ′) v
and
(135) Λ( Y ) = ǫL,tηR,s
So the composite is just
(136) Λ( Y ′)◦ Λ( Y ) = ( ǫL,t′ηR,s′ )◦ (ǫL,tηR,s)
We recall that Λ( X ′)◦ Λ( X) is described explicitly in (108) and Λ( X ′◦ X) in
(109). Finding these for the Xi gives a total of four functors here. We next describe
natural transformations between these.
As shown in Theorem 5.2.1, there are comparison isomorphisms
(137) βXi,X ′i : Λ( X ′i)◦ Λ( Xi)→ Λ( X ′i◦ Xi)
which will necessarily be involved in the isomorphism we are looking for. T hese
derive from the α isomorphisms in the weak pullback in X ′i◦ Xi.
Composing with these comparison isomorphisms as in (131) gives:
(138) (Id s∗
1◦βX1,X ′1◦ Id(t′1)∗ )(ǫL,t′ηR,s′ )(ǫL,tηR,s)(Ids2 ∗◦(βX2,X ′2 )−1◦ Id(t′2)∗ )
34 JEFFREY C. MORTON
Now, the β isomorphisms simply allow us to identify the spaces here, so it suﬃces
to describe the maps, and in particular the coeﬃcients which arise. A t any presheaf
G on A1, in the summand for [ a1]∈ A1 and [ x′
1]∈ X ′
1:
(139) ( ǫL,tηR,s) : v↦→
∑
[y]|s(y)∼=x1
1
#Aut(y)
∑
g∈Aut(x1)
g−1⊗ g(v)
which is a map between spaces of the form (107) associated to X1 and X2. Now
this becomes the v′ when we take the full map between spaces like (108), where we
have:
(140) ( ǫL,t′ηR,s′ ) : v′↦→
∑
[y′]|s′(y)∼=x′1
1
#Aut(y′)
∑
h∈Aut(x′1)
h−1⊗ h(v′)
so ﬁnally we get:
(141)
v↦→
∑
[y′]|s′(y)∼=x′1
1
#Aut(y′)
∑
h∈Aut(x′1)
h−1⊗h
( ∑
[y]|s(y)∼=x1
1
#Aut(y)
∑
g∈Aut(x1)
g−1⊗g(v)
)
which we want to show is the same as the natural transformation as sociated to
Λ( Y ′◦ Y ):
(142) Λ( Y ′◦ Y ) = ǫL,(t,t′)◦ ηR,(s,s′) : Λ( X ′1◦ X1)→ Λ( X ′2◦ X2)
which is a map between two spaces of the form (109).
This Y ′◦Y : X ′1◦X1→ X ′2◦X2 is a span of span maps which is given as follows.
We take the horizontal composite of the spans A1
σ
← Y
τ
→ A2 and A2
σ′
← Y ′ τ ′
→ A3.
This is a weak pullback taken up to isomorphism. The pullback square co mmutes
weakly, say up to ξ. Then the groupoid Y ′◦Y has maps into Y and Y ′, and therefore
by composition with s and s′, it has maps into X1 and X ′1. By the universal
property of the weak pullback X ′1◦ X1, there is a map S : Y ′◦ Y→ X ′1◦ X1.
Similarly, there is T : Y ′◦ Y→ X ′2◦ X2.
We can see what this is by taking the weak pullback giving Y ′◦ Y , which we
take to be the comma category whose objects are of the form ( y, f, y ′) where f :
τ (y)→ σ′(y′) in A2. Then the S and T given by the universal property are just S =
(s, s′) giving objects like ( x1, f, x′1) and T = ( t, t′) giving objects like ( x2, f, x′2).
In particular, the morphism f∈ A2 is left intact. (Diﬀerent isomorphic choices for
weak pullback could of course change f ).
Given this, we have, in the summand for a given [ a1]∈ A1: and a particular
[(x1, f, x′
1)]∈ X ′
1◦ X1, we have:
(143) ηR,(s,s′) : v↦→
⨁
[y,f,y′ ]
s(y)∼=x1
s′(y′)∼=x′
1
1
#Aut(y, f, y ′)
∑
(g,h)∈Aut(x,f,x′)
(g, h)−1⊗ (g, h)(v)
and then
(144)
ǫL,(t,t′)ηR,(s,s′) : v↦→
∑
[y,f,y′ ]
s(y)∼=x1
s′(y′)∼=x′
1
1
#Aut(y, f, y ′)
∑
(g,g′)∈Aut(x,f,x′)
(g, h)−1⊗ (g, h)(v)
2-VECTOR SPACES AND GROUPOIDS 35
So in fact, since we are in a weak pullback square, the size of the auto morphism
groups in the two expressions we have found will be in the same ratios , and so it
becomes clear that, using the β isomorphisms as seen in the proof of Theorem 5.2.1:
(145) Λ( Y ′◦ Y ) = βX1,X ′1(Λ( Y ′)Λ( Y ))(βX2,X ′2 )−1
as required. □
