---
doc_id: arxiv-1003.4485v2
doc_title: "email: baez@math.ucr.edu huerta@math.ucr.edu"
section_id: sec-004-33-2-groups
section_title: "2-Groups"
section_number: 3.3
pages: 15-21
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describ e parallel trans- port for particles and strings in terms of 2-connections on 2 -bundles."
---
symmetries in gauge theory, these describe symmetries in higher ga uge theory.
3.3 2-Groups
Just as a group was a groupoid with one object, we deﬁne a 2-group to be a
2-groupoid with one object. This deﬁnition is so elegant that it may be hard to
understand at ﬁrst! So, it will be useful to take a 2-group G and chop it into
four bite-sized pieces of data, giving a ‘crossed module’ ( G, H, t, α). Indeed, 2-
groups were originally introduced in the guise of crossed modules by t he famous
topologist J. H. C. Whitehead [93]. In 1950, with help from Mac Lane [66 ], he
used crossed modules to generalize the fundamental group of a sp ace to what
we might now call the ‘fundamental 2-group’. But only later did it beco me clear
that a crossed module was another way of talking about a 2-groupo id with just
one object! For more of this history, and much more on 2-groups, see [13].
Let us start by seeing what it means to say a 2-group is a 2-groupoid with
one object. It means that a 2-group G has:
• one object:
•
• morphisms:
• •
g
/d118/d118
15
• and 2-morphisms:
• •
g
/d2/d2
g′
/d92/d92
α
/d11/d19
The morphisms form a group under composition:
• •
g
/d118/d118 •
g′
/d118/d118 = • •
gg′
/d118/d118
The 2-morphisms form a group under horizontal composition:
• •
g1
/d120/d120
g′
1
/d102/d102 α1
/d11/d19
g2
/d120/d120
g′
2
/d102/d102 α2
/d11/d19 = • •
g1g2
/d122/d122
g′
1g′
2
/d100/d100 α1◦α2
/d11/d19
In addition, the 2-morphisms can be composed vertically:
• •
g
/d1/d1 g′
/d111/d111
g′′
/d93/d93
α
/d11/d19
α′
/d11/d19
= • •
g
/d122/d122
g′′
/d100/d100 α′·α
/d11/d19
Vertical composition is also associative with identity and inverses. Bu t the 2-
morphisms do not form a group under this operation, because a give n pair may
not be composable: their source and target may not match up. Fina lly, vertical
and horizontal composition are tied together by the interchange la w, which says
the two ways one can read this diagram are consistent.
• •
g1
/d125/d125 g′
1/d111/d111
g′′
1
/d97/d97
α/d11/d19
α′
/d11/d19
•
g2
/d125/d125 g′
2/d111/d111
g′′
2
/d97/d97
β/d11/d19
β′
/d11/d19
Now let us create a crossed module ( G, H, t, α) from a 2-group G. To do
this, ﬁrst note that the morphisms of the 2-group form a group by themselves,
with composition as the group operation. So:
• Let G be the set of morphisms in G, made into a group with composition
as the group operation:
• •
g
/d118/d118 •
g′
/d118/d118 = • •
gg′
/d118/d118
16
How about the 2-morphisms? These also form a group, with horizont al com-
position as the group operation. But it turns out to be eﬃcient to fo cus on a
subgroup of this:
• Let H be the set of all 2-morphisms whose source is the identity:
• •
1•
/d122/d122
t(h)
/d100/d100 h
/d11/d19
We make H into a group with horizontal composition as the group oper-
ation:
• •
1•
/d120/d120
t(h)
/d102/d102 h/d11/d19 •
1•
/d120/d120
t(h′)
/d102/d102 h′
/d11/d19 = • •
1•
/d122/d122
t(hh′)
/d100/d100 hh′
/d11/d19
Above we use hh′ as an abbreviation for the horizontal composite h ◦ h′ of two
elements of H. We will use h−1 to denote the horizontal inverse of an element
of H. We use t(h) to denote the target of an element h ∈ H. The deﬁnition of
a 2-category implies that t: H → G is a group homomorphism:
t(hh′) = t(h)t(h′).
This homomorphism is our third piece of data:
• A group homomorphism t: H → G sending each 2-morphism in H to its
target:
• •
1•
/d122/d122
t(h)
/d100/d100 h
/d11/d19
The fourth piece of data is the subtlest. There is a way to ‘horizonta lly conju-
gate’ any element h ∈ H by an element g ∈ G, or more precisely by its identity
2-morphism 1 g:
• •
g
/d120/d120
g
/d102/d102 1g/d11/d19 •
1•
/d120/d120
t(h)
/d102/d102 h/d11/d19 •
g−1
/d120/d120
g−1
/d102/d102 1g−1
/d11/d19
The result is a 2-morphism in H which we call α(g)(h). In fact, α(g) is an
automorphism of H, meaning a one-to-one and onto function with
α(g)(hh′) = α(g)(h) α(g)(h′).
17
Composing two automorphisms gives another automorphism, and th is makes
the automorphisms of H into a group, say Aut( H). Even better, α gives a
group homomorphism
α: G → Aut(H).
Concretely, this means that in addition to the above equation, we ha ve
α(gg ′) = α(g)α(g′).
Checking these two equations is a nice way to test your understand ing of 2-
categories. A group homomorphism α: G → Aut(H) is also called an action
of the group G on the group H. So, the fourth and ﬁnal piece of data in our
crossed module is:
• An action α of G on H given by:
• •
g
/d120/d120
g
/d102/d102 1g/d11/d19 •
1•
/d120/d120
t(h)
/d102/d102 h/d11/d19 •
g−1
/d120/d120
g−1
/d102/d102 1−1
g/d11/d19 = • •
1
/d120/d120
t(α(g)(h))
/d102/d102 α(g)(h)/d11/d19
A crossed module ( G, H, t, α) must also satisfy two more equations which follow
from the deﬁnition of a 2-group. First, examining the above diagram , we see
that t is G-equivariant, by which we mean:
• t(α(g)h) = g(t(h))g−1 for all g ∈ G and h ∈ H.
Second, the Peiﬀer identity holds:
• α(t(h))h′ = hh′h−1 for all h, h′ ∈ H.
The Peiﬀer identity is the least obvious thing about a crossed module. It
follows from the interchange law, and it is worth seeing how. First, we have:
hh′h−1 = • •
1•
/d122/d122
t(h)
/d100/d100 h
/d11/d19 •
1•
/d122/d122
t(h′)
/d100/d100 h′
/d11/d19 •
1•
/d122/d122
t(h−1)
/d100/d100 h−1
/d11/d19
where—beware!—we are now using h−1 to mean the horizontal inverse of h,
since this is its inverse in the group H. We can pad out this equation by
vertically composing with some identity morphisms:
hh′h−1 = • •
1•
/d126/d126
t(h)/d111/d111
t(h)
/d96/d96
h
/d11/d19
1t(h)
/d11/d19
•
1•
/d126/d126 1•/d111/d111
t(h)
/d96/d96
11•
/d11/d19
h
/d11/d19
•
1•
/d126/d126 t(h−1)/d111/d111
t(h−1)
/d96/d96
h−1
/d11/d19
1t(h−1 )
/d11/d19
18
This diagram describes an unambiguous 2-morphism, thanks to the in terchange
law. So, we can do the horizontal compositions ﬁrst and get:
hh′h−1 = • •
1•
/d122/d122 1•/d111/d111
t(hh′h−1)
/d100/d100
11•
/d11/d19
α(t(h))(h′)
/d11/d19
But vertically composing with an identity 2-morphism has no eﬀect. So , we
obtain the Peiﬀer identity:
hh′h−1 = α(t(h))(h′).
All this leads us to deﬁne a crossed module (G, H, t, α) to consist of:
• a group G,
• a group H,
• a homomorphism t: H → G, and
• an action α: G → Aut(H)
such that:
• t is G-equivariant:
t(α(g)h) = g(t(h))g−1
for all g ∈ G and h ∈ H, and
• the Peiﬀer identity holds for all h, h′ ∈ H:
α(t(h))h′ = hh′h−1.
In fact, we can recover a 2-group G from its crossed module ( G, H, t, α), so
crossed modules are just another way of thinking about 2-groups . The trick to
seeing this is to notice that 2-morphisms in G are the same as pairs ( g, h) ∈
G × H. Such a pair gives this 2-morphism:
• •
1•
/d120/d120
t(h)
/d102/d102 h/d11/d19 •
g
/d120/d120
g
/d102/d102 1g/d11/d19
We leave it to the reader to check that every 2-morphism in G is of this form.
Note that this 2-morphism goes from g to t(h)g. So, when we construct a
2-group from a crossed module, we get a 2-morphism
(g, h): g → t(h)g
19
from any pair ( g, h) ∈ G × H. Horizontal composition of 2-morphisms then
makes G × H into a group, as follows:
(g, h) ◦ (g′, h′) =
• •
1•
/d125/d125
t(h)
/d97/d97 h/d11/d19 •
g
/d125/d125
g
/d97/d97 1g/d11/d19 •
1•
/d125/d125
t(h′)
/d97/d97 h′
/d11/d19 •
g′
/d125/d125
g′
/d97/d97 1g′
/d11/d19 =
• •
1•
/d125/d125
t(h)
/d97/d97 h/d11/d19 •
g
/d125/d125
g
/d97/d97 1g/d11/d19 •
1•
/d125/d125
t(h′)
/d97/d97 h′
/d11/d19 •
g−1
/d125/d125
g−1
/d97/d97 1g−1
/d11/d19 •
g
/d125/d125
g
/d97/d97 1g/d11/d19 •
g′
/d125/d125
g′
/d97/d97 1g′
/d11/d19 =
• •
1•
/d125/d125
t(h)
/d97/d97 h/d11/d19 •
1•
/d117/d117
t(α(g)(h′))
/d105/d105 α(g)(h′)/d11/d19 •
gg′
/d120/d120
gg′
/d102/d102 1gg′
/d11/d19 =
• •
1•
/d119/d119
t(hα(g)(h′))
/d103/d103 hα(g)(h′)
/d11/d19
•
gg′
/d120/d120
gg′
/d102/d102 1gg′
/d11/d19 = (gg ′, hα(g)(h′)).
So, the group of 2-morphisms of G is the semidirect product G ⋉ H, deﬁned
using the action α.
Following this line of thought, the reader can check the following:
Theorem 2. Given a crossed module (G, H, t, α), there is a unique 2-group G
where:
• the group of morphisms is G,
• a 2-morphism α: g ⇒ g′ is the same as a pair (g, h) ∈ G × H with g′ =
t(h)g,
• the vertical composite of (g, h) and (g′, h′), when they are composable, is
given by
(g, h) · (g′, h′) = ( g′, hh′),
• the horizontal composite of (g, h) and (g′, h′) is given by
(g, h) ◦ (g′, h′) = ( gg ′, hα(g)(h′)).
Conversely, given a 2-group G, there is a unique crossed module (G, H, t, α)
where:
• G is the group of morphisms of G,
20
• H is the group of 2-morphisms with source equal to 1•,
• t: H → G assigns to each 2-morphism in H its target,
• the action α of G on H is given by
α(g)h = 1 g ◦ h ◦ 1g−1 .
Indeed, these two processes set up an equivalence between 2-gr oups and
crossed modules, as described more formally elsewhere [13, 51]. It t hus makes
sense to deﬁne a Lie 2-group to be a 2-group for which the groups G and H in
its crossed module are Lie groups, with the maps t: H → G and α: G → Aut(H)
being smooth. It is worth emphasizing that in this context we use Aut (H) to
mean the group of smooth automorphisms of H. This is a Lie group in its own
right.
In Section 4 we will use Theorem 2 to construct many examples of Lie 2 -
