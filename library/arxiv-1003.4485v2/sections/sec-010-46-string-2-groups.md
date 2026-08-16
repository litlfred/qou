---
doc_id: arxiv-1003.4485v2
doc_title: "email: baez@math.ucr.edu huerta@math.ucr.edu"
section_id: sec-010-46-string-2-groups
section_title: "String 2-Groups"
section_number: 4.6
pages: 40-44
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describ e parallel trans- port for particles and strings in terms of 2-connections on 2 -bundles."
---
The Lie 2-groups discussed so far are easy to construct. The str ing 2-group is
considerably more subtle. Ultimately it forces upon us a deeper conc eption of
what a Lie 2-group really is, and a more sophisticated approach to hig her gauge
theory. Treated in proper detail, these topics would carry us far b eyond the
limits of this quick introduction. But it would be a shame not to mention t hem
at all.
Suppose we have a central extension of a Lie group G by an abelian Lie
group A. In other words, suppose we have a short exact sequence of Lie g roups
1 → A → H
t
→ G → 1
where the image of A lies in the center of H. Then we can construct an action
α of G on H as follows. The map t: H → G describes H as a ﬁber bundle
over G, so choose a section of this bundle: that is, a function s: G → H with
t(s(g)) = g, not necessarily a homomorphism. Then set
α(g)h = s(g)hs(g)−1.
Since A is included in the center of H, α is independent of the choice of s.
Thanks to this, we do not need a global smooth section s to check that α(g)
depends smoothly on g: it suﬃces that there exist a local smooth section in
a neighborhood of each g ∈ G, and indeed this is always true. We can use
these local sections to deﬁne α globally, since they must give the same α on
overlapping neighborhoods.
Given all this, we can check that t is G-equivariant and that the Peiﬀer
identity holds. So, we obtain a Lie 2-group where:
• G is any Lie group,
• H is any Lie group,
• t: H → G makes H into a central extension of G,
• α is given by α(g)h = s(g)hs(g)−1 where s: G → H is any section.
40
We call this the central extension 2-group C(H
t
→ G).
To get concrete examples, we need examples of central extension s. For any
choice of G and A, we can always take H = G × A and use the ‘trivial’ central
extension
1 → A → A × G → G → 1.
For more interesting examples, we need nontrivial central extens ions. These
tend to arise from problems in quantization. For example, suppose V is a ﬁnite-
dimensional symplectic vector space : that is, a vector space equipped with
a nondegenerate antisymmetric bilinear form
ω: V × V → R.
Then we can make H = V × R into a Lie group called the Heisenberg group ,
with the product
(u, a)(v, b) = ( u + v, a + b + ω(u, v)).
The Heisenberg group plays a fundamental role in quantum mechanic s, because
we can think of V as the phase space of a classical point particle. If we let
G stand for V regarded as an abelian Lie group, then elements of G describe
translations in phase space: that is, translations of both position a nd momen-
tum. The Heisenberg group H describes how these translations commute only
‘up to a phase’ when we take quantum mechanics into account: the p hase is
given by exp( iω(u, v)). There is a homomorphism t: H → G that forgets this
phase information, given by
t(u, a) = u.
This exhibits H as a central extension of G. We thus obtain a central extension
2-group C(H
t
− →G), called the Heisenberg 2-group of the symplectic vector
space V .
The applications of Heisenberg 2-groups seem largely unexplored, a nd should
be worth studying. So far, much more work has been put into under standing 2-
groups arising from central extensions of loop groups. The reaso n is that central
extensions of loop groups play a basic role in string theory and confo rmal ﬁeld
theory, as nicely explained by Pressley and Segal [78].
Suppose that G is a connected and simply-connected compact simple Lie
group G. Deﬁne the loop group Ω G to be the set of all smooth paths γ: [0, 1] →
G that start and end at the identity of G. This becomes a group under pointwise
multiplication, and in fact it is a kind of inﬁnite-dimensional Lie group [71].
For each integer k, called the level, the loop group has a central extension
1 → U(1) → ˆΩ kG
t
− →Ω G → 1.
These extensions are all diﬀerent, and all nontrivial except for k = 0. In physics,
they arise because the 2d gauge theory called the Wess–Zumino–Wit ten model
has an ‘anomaly’. The loop group Ω G acts as gauge transformations in the
classical version of this theory. However, when we quantize the th eory, we obtain
41
a representation of Ω G only ‘up to a phase’—that is, a projective representation.
This can be understood as an honest representation of the centr al extension
ˆΩ kG, where the integer k appears in the Lagrangian for the Wess–Zumino–
Witten model.
Starting from this central extension we can construct a central extension
2-group called the level-k loop 2-group of G, Lk(G). This is an inﬁnite-
dimensional Lie 2-group, meaning that it comes from a crossed modu le where
the groups involved are inﬁnite-dimensional Lie groups, and all the m aps are
smooth. Moreover, it ﬁts into an exact sequence
1 → L k(G) → ST RIN G k(G) − →G → 1
where the middle term, the level-k string 2-group of G, has very interesting
properties [8].
Since the string 2-group ST RIN G k(G) is an inﬁnite-dimensional Lie 2-
group, it is a topological 2-group. There is a way to take any topolog ical 2-
group and squash it down to a topological group [8, 18]. Applying this trick
to ST RIN G k(G) when k = 1, we obtain a topological group whose homotopy
groups match those of G—except for the third homotopy group, which has been
made trivial. In the special case where G = Spin( n), this topological group is
called the ‘string group’, since to consistently deﬁne superstrings p ropagating
on a spin manifold, we must reduce its structure group from Spin( n) to this
group [94]. The string group also plays a role in Stolz and Teichner’s wor k on
elliptic cohomology, which involves a notion of parallel transport over surfaces
[90]. There is a lot of sophisticated mathematics involved here, but ult imately
much of it should arise from the way string 2-groups are involved in th e parallel
transport of strings! The work of Sati, Schreiber and Stasheﬀ [83 ] provides good
evidence for this, as does the work of Waldorf [91].
In fact, the string Lie 2-group had lived through many previous inca rnations
before being constructed as an inﬁnite-dimensional Lie 2-group. B rylinski and
McLaughlin [33] thought of it as a U(1) gerbe over the group G. The fact that
this gerbe is ‘multiplicative’ makes it something like a group in its own right
[32]. This viewpoint has also been explored by Murray and Stevenson [7 5].
Later, Baez and Crans [7] constructed a Lie 2-algebra stringk(g) correspond-
ing to the string Lie 2-group. For pedagogical purposes, our discu ssion of Lie
2-groups has focused solely on ‘strict’ 2-groups, where the 1-mo rphisms satisfy
the group axioms strictly, as equations. However, there is also an e xtensive
theory of ‘weak’ 2-groups, where the 1-morphisms obey the grou p axioms only
up to invertible 2-morphisms [13]. Following this line of thought, we may also
deﬁne weak Lie 2-algebras [81], and the Lie 2-algebra stringk(g) is one of these
where only the Jacobi identity fails to hold strictly.
The beauty of weak Lie 2-algebras is that stringk(g) is very easy to describe in
these terms. In particular, it is ﬁnite-dimensional. The hard part is c onstructing
a weak Lie 2-group corresponding to this weak Lie 2-algebra. It is ea sy to check
that any strict Lie 2-algebra has a corresponding strict Lie 2-grou p. Weak Lie 2-
algebras are more tricky [13]. Baez, Crans, Schreiber and Stevens on [8] dodged
42
this problem by showing that the string Lie 2-algebra is equivalent (in some
precise sense) to a strict Lie 2-algebra, which however is inﬁnite-dim ensional.
They then constructed the inﬁnite-dimensional strict Lie 2-group corresponding
to this strict Lie 2-algebra. This is just ST RIN G k(G) as described above.
On the other hand, a ﬁnite-dimensional model of the string 2-grou p was
recently introduced by Schommer-Pries [85]. This uses an improved d eﬁnition
of ‘weak Lie 2-group’, based on an important realization: the correc t maps
between smooth groupoids are not the smooth functors, but som ething more
general [64]. We have already mentioned this in our discussion of conn ection:
a smooth functor hol: P1(M ) → G is a connection on the trivial principal G-
bundle over M , while one of these more general maps is a connection on an
arbitrary principal G-bundle over M . If we take this lesson to heart, we are led
into the world of ‘stacks’—and in that world, we can ﬁnd a ﬁnite-dimens ional
version of the string 2-group.
There has also been progress on constructing weak Lie n-groups from weak
Lie n-algebras for n > 2. Getzler [56] and Henriques [61] have developed an
approach that works for all n, even n = ∞. Their approach is able to handle
weak Lie ∞-algebras of a sort known as ‘ L∞-algebras’. Quite roughly, the
idea is that in an L∞-algebra, the Jacobi identity holds only weakly, while the
antisymmetry of the bracket still holds strictly.
In fact, L∞-algebras were developed by Stasheﬀ and collaborators [68, 84]
before higher gauge theory became recognized as a subject of st udy. But more
recently, Sati, Schreiber, Stasheﬀ [82, 83] have developed a lot o f higher gauge
theory with the help of L∞-algebras. Thanks to their work, it is becoming
clear that superstring theory, supergravity and even the myste rious ‘M -theory’
have strong ties to higher gauge theory. For example, they argue that 11-
dimensional supergravity can be seen as a higher gauge theory gov erned by a
certain ‘Lie 3-superalgebra’ which they call sugra(10, 1). The number 3 here
relates to the 2-brane solutions of 11-dimensional supergravity: just as parallel
transport of strings is described by 2-connections, the parallel t ransport of 2-
branes is described by 3-connections, which in the supersymmetric case involve
Lie 3-superalgebras.
In fact, sugra(10, 1) is one of a family of four Lie 3-superalgebras that extend
the Poincar´ e Lie superalgebra in dimensions 4, 5, 7 and 11. These ca n be built
via a systematic construction starting from the four normed divisio n algebras:
the real numbers, the complex numbers, the quaternions and the octonions [11].
These four algebras also give rise to Lie 2-superalgebras extending the Poincar´ e
Lie superalgebra in dimensions 3, 4, 6, and 10. The Lie 2-superalgebr as are
related to superstring theories in dimensions 3, 4, 6, and 10, while th e Lie 3-
superalgebras are related to super-2-brane theories in dimension s 4, 5, 7 and 11.
All these theories, and even their relation to division algebras, have been known
since the late 1980s [42]. Higher gauge theory provides new insights in to the
geometry of these theories. In particular, the work of D’Auria, Ca stellani and
Fr´ e [41] can be seen asimplicitly making extensive use of Lie n-superalgebras—
but this only became clear later, through the work of Sati, Schreibe r and Stasheﬀ
[83].
43
Alas, explaining these fascinating issues in detail would vastly expand the
scope of this paper. We should instead return to simpler things: gau ge trans-
formations, curvature, and nontrivial 2-bundles.
