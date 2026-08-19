---
doc_id: arxiv-1003.4485v2
doc_title: "email: baez@math.ucr.edu huerta@math.ucr.edu"
section_id: sec-005-34-2-connections
section_title: "2-Connections"
section_number: 3.4
pages: 21-27
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describ e parallel trans- port for particles and strings in terms of 2-connections on 2 -bundles."
---
3.4 2-Connections
A 2-connection is a recipe for parallel transporting both 0-dimensio nal and
1-dimensional objects—say, particles and strings. Just as we can describe a
connection on a trivial bundle using a Lie-algebra valued diﬀerential f orm, we
can describe a 2-connection using a pair of diﬀerential forms. But there is a
deeper way of understanding 2-connections. Just as a connectio n was revealed
to be a smooth functor
hol: P1(M ) → G
for some Lie group G, a 2-connection will turn out to be a smooth 2-functor
hol: P2(M ) → G
for some Lie 2-group G. Of course, to make sense of this we need to deﬁne a
‘2-functor’, and say what it means for such a thing to be smooth.
The deﬁnition of 2-functor is utterly straightforward: it is a map be tween
2-categories that preserves everything in sight. So, given 2-cat egories C and D,
a 2-functor F : C → D consists of:
• a map F sending objects in C to objects in D,
• another map called F sending morphisms in C to morphisms in D,
• a third map called F sending 2-morphisms in C to 2-morphisms in D,
such that:
• given a morphism f : x → y in C, we have F (f ): F (x) → F (y),
21
• F preserves composition for morphisms, and identity morphisms:
F (f g) = F (f )F (g)
F (1x) = 1 F (x),
• given a 2-morphism α: f ⇒ g in C, we have F (α): F (f ) ⇒ F (g),
• F preserves vertical and horizontal composition for 2-morphisms, and
identity 2-morphisms:
F (α · β) = F (α) · F (β)
F (α ◦ β) = F (α) ◦ F (β)
F (1f ) = 1 F (f ).
There is a general theory of smooth 2-groupoids and smooth 2-fu nctors [16,
88]. But here we prefer to take a more elementary approach. We alr eady know
that for any Lie 2-group G, the morphisms and 2-morphisms each form Lie
groups. Given this, we can say that for any smooth manifold M , a 2-functor
hol: P2(M ) → G
is smooth if:
• For any smoothly parametrized family of lazy paths γs (s ∈ [0, 1]n) the
morphism hol( γs) depends smoothly on s, and
• For any smoothly parametrized family of lazy surfaces Σ s (s ∈ [0, 1]n) the
2-morphism hol(Σ s) depends smoothly on s.
With these deﬁnitions in hand, we are ﬁnally ready to understand the basic
result about 2-connections. It is completely analogous to Theorem 1:
Theorem 3. For any Lie 2-group G and any smooth manifold M , there is a
one-to-one correspondence between:
1. 2-connections on the trivial principal G-2-bundle over M ,
2. pairs consisting of a smooth g-valued 1-form A and a smooth h-valued
2-form B on M , such that
t(B) = dA + A ∧ A
where we use t: h → g, the diﬀerential of the map t: H → G, to convert B
into a g-valued 2-form, and
3. smooth 2-functors
hol: P2(M ) → G
where P2(M ) is the path 2-groupoid of M .
22
This result was announced by Baez and Schreiber [16], and a proof c an be
be found in the work of Schreiber and Waldorf [88]. This work was deep ly
inspired by the ideas of Breen and Messing [29, 30], who considered a s pecial
class of 2-groups, and omitted the equation t(B) = dA + A ∧ A, since their sort
of connection did not assign holonomies to surfaces. One should also compare
the closely related work of Mackaay, Martins, and Picken [67, 69], an d the work
of Pfeiﬀer and Girelli [76, 58].
In the above theorem, the ﬁrst item mentions ‘2-connections’ and‘2-bundles’—
concepts that we have not deﬁned. But since we are only talking abo ut 2-
connections on trivial 2-bundles, we do not need these general concepts yet.
For now, we can take the third item as the deﬁnition of the ﬁrst. The n the con-
tent of the theorem lies in the diﬀerential form description of smoot h 2-functors
hol: P2(M ) → G . This is what we need to understand.
A 2-functor of this sort must assign holonomies both to paths and s ur-
faces. As you might expect, the 1-form A is primarily responsible for deﬁn-
ing holonomies along paths, while the 2-form B is responsible for deﬁning
holonomies for surfaces. But this is a bit of an oversimpliﬁcation. Whe n com-
puting the holonomy of a surface, we need to use A as well as B!
Another surprising thing is that A and B need to be related by an equation
for the holonomy to be a 2-functor. If we ponder how the holonomy of a surface
is actually computed, we can see why this is so. We shall not be at all rig orous
here. We just want to give a rough intuitive idea of how to compute a h olonomy
for a surface, and where the equation t(B) = dA + A ∧ A comes from. Of course
dA + A ∧ A = F
is just the curvature of the connection A. This is a big clue.
Suppose we are trying to compute the holonomy for a surface star ting from
a g-valued 1-form A and an h-valued 2-form B. Then following the ideas of
calculus, we can try to chop the surface into many small pieces, com pute a
holonomy for each one, and multiply these together somehow. It is e asy to chop
a surface into small squares. Unfortunately, the deﬁnition of 2-c ategory doesn’t
seem to know anything about squares! But this is not a serious prob lem. For
example, we can interpret this square:
• •
f/d111/d111
•
h
/d79/d79
•k
/d111/d111
g
/d79/d79
α/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
as a 2-morphism α: f g ⇒ hk. We can then compose a bunch of such 2-
23
morphisms:
• •/d111/d111 •/d111/d111 •/d111/d111
•
/d79/d79
•/d111/d111
/d79/d79
•/d111/d111
/d79/d79
•/d111/d111
/d79/d79
/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
•
/d79/d79
•/d111/d111
/d79/d79
•/d111/d111
/d79/d79
•/d111/d111
/d79/d79
/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
with the help of a trick called ‘whiskering’.
Whiskering is a way to compose a 1-morphism and a 2-morphism. Suppo se
we want to compose a 2-morphism α and a morphism f that sticks out like a
whisker on the left:
z• y•
f/d111/d111 •x
g
/d119/d119
g′
/d103/d103 α
/d11/d19
We can do this by taking the horizontal composite 1 f ◦ α:
z• y•
f
/d118/d118
f
/d104/d104 1f
/d11/d19 •x
g
/d119/d119
g′
/d103/d103 α
/d11/d19
We call the result f ◦ α, or α left whiskered by f . Similarly, if we have a
whisker sticking out on the right:
z• y•
g
/d118/d118
g′
/d104/d104 α
/d11/d19 x•
f/d111/d111
we can take the horizontal composite α ◦ 1f :
z• y•
g
/d118/d118
g′
/d104/d104 α
/d11/d19 •x
f
/d119/d119
f
/d103/d103 1f
/d11/d19
and call the result α ◦ f , or α right whiskered by f .
With the help of whiskering, we can compose 2-morphisms shaped like a r-
bitrary polygons. For example, suppose we want to horizontally com pose two
squares:
• •
f/d111/d111 •
f ′
/d111/d111
•
h
/d79/d79
•k
/d111/d111
ℓ
/d79/d79
•
k′
/d111/d111
g
/d79/d79
α/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
β/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
24
To do this, we can left whisker β by f , obtaining this 2-morphism:
f ◦ β: f f′g ⇒ f ℓk′
• •
f/d111/d111 •
f ′
/d111/d111
•
ℓ
/d79/d79
•
k′
/d111/d111
g
/d79/d79
β/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
Then we can right whisker α by k′, obtaining
α ◦ k′: f ℓk′ ⇒ hkk ′
• •
f/d111/d111
•
h
/d79/d79
•k
/d111/d111
ℓ
/d79/d79
•
k′
/d111/d111
α/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
Then we can vertically compose these to get the desired 2-morphism :
(α ◦ k′) · (g ◦ β): f f′g ⇒ hkk ′
• •
f/d111/d111 •
f ′
/d111/d111
•
h
/d79/d79
•k
/d111/d111
ℓ
/d79/d79
•
k′
/d111/d111
g
/d79/d79
α/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
β/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
The same sort of trick lets us vertically compose squares. By iterat ing these
procedures we can deﬁne more complicated composites, like this:
• •/d111/d111 •/d111/d111 •/d111/d111 •/d111/d111
•
/d79/d79
•/d111/d111
/d79/d79
•/d111/d111
/d79/d79
•/d111/d111
/d79/d79
•/d111/d111
/d79/d79
/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
•
/d79/d79
•/d111/d111
/d79/d79
•/d111/d111
/d79/d79
•/d111/d111
/d79/d79
•/d111/d111
/d79/d79
/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
/d123/d3 ⑧⑧⑧⑧⑧⑧⑧⑧
Of course, one may wonder if these more complicated composites ar e unambigu-
ously deﬁned! Luckily they are, thanks to associativity and the inte rchange law.
This is a nontrivial result, called the ‘pasting theorem’ [77].
By this method, we can reduce the task of computing hol(Σ) for a lar ge
surface Σ to the task of computing it for lots of small squares. Ultim ately, of
course, we should take a limit as the squares become smaller and smalle r. But
25
for our nonrigorous discussion, it is enough to consider a very small square like
this:
•
•
Σ/d123/d3 ⑧⑧⑧⑧⑧⑧
/d111/d111/d79/d79
γ2
γ1
We can think of this square as a 2-morphism
Σ: γ1 ⇒ γ2
where γ1 is the path that goes up and then across, while γ2 goes across and
then up. We wish to compute
hol(Σ): hol( γ1) ⇒ hol(γ2).
On the one hand, hol(Σ) involves the 2-form B. On the other hand, its source
and target depend only on the 1-form A:
hol(γ1) = P exp
( ∫
γi
A
)
, hol(γ2) = P exp
( ∫
γ2
A
)
.
So, hol(Σ) cannot have the right source and target unless A and B are related
by an equation!
Let us try to guess this equation. Recall from Theorem 2 that a 2-m orphism
α: g1 ⇒ g2 in G is determined by an element h ∈ H with g2 = t(h)g1. Using
this, we may think of hol(Σ): hol( γ1) → hol(γ2) as determined by an element
h ∈ H with
P exp
( ∫
γ2
A
)
= t(h) P exp
( ∫
γ1
A
)
,
or in other words
t(h) = P exp
( ∫
∂Σ
A
)
(1)
where the loop ∂Σ = γ2γ−1
1 goes around the square Σ. For a very small square,
we can approximately compute the right hand side using Stokes’ the orem:
P exp
( ∫
∂Σ
A
)
≈ exp
( ∫
Σ
F
)
.
On the other hand, there is an obvious guess for the approximate v alue of h,
which is supposed to be built using the 2-form B:
h ≈ exp
( ∫
Σ
B
)
.
For this guess to yield Equation (1), at least to ﬁrst order in the size of our
square, we need
t(exp
( ∫
Σ
B
)
) ≈ exp
( ∫
Σ
F
)
.
26
But this will be true if
t(B) = F.
And this is the equation that relates A and B!
What have we learned here? First, for any surface Σ: γ1 ⇒ γ2, the holonomy
hol(Σ) is determined by an element h ∈ H with
P exp
( ∫
γ2
A
)
= t(h) P exp
( ∫
γ1
A
)
In the limit where Σ is very small, this element h depends only on B:
h ≈ exp
( ∫
Σ
B
)
.
But for a ﬁnite-sized surface, this formula is no good, since it involve s adding
up B at diﬀerent points, which is not a smart thing to do. For a ﬁnite-sized
surface, h depends on A as well as B, since we can approximately compute h
by chopping this surface into small squares, whiskering them with pa ths, and
composing them—and the holonomies along these paths are compute d using A.
To get the exact holonomy over a ﬁnite-sized surface by this method, we
need to take a limit where we subdivide the surface into ever smaller sq uares.
This is the Lie 2-group analogue of a Riemann sum. But for actual calc ulations,
this process is not very convenient. More practical formulas for c omputing
holonomies over surfaces can be found in the work of Schreiber and Waldorf
[88], Martins and Picken [69].
