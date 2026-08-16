---
doc_id: arxiv-0904.1556v2
doc_title: "The Algebra of Grand Uniﬁed Theories"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 0904.1556v2.pdf
source_sha256: a1a43786d817f085
doc_brief: "The Algebra of Grand Unified Theories — The Standard Model is the best tested and most widely accepte d theory of elementary particles we have today."
---
The Standard Model of particle physics is one of the greatest trium phs of physics.
This theory is our best attempt to describe all the particles and all t he forces of
nature... except gravity. It does a great job of ﬁtting experiments we can do in the
lab. But physicists are dissatisﬁed with it. There are three main reas ons. First, it
leaves out gravity: that force is described by Einstein’s theory of g eneral relativity,
which has not yet been reconciled with the Standard Model. Second, astronomical
observations suggest that there may be forms of matter not cov ered by the Standard
Model—most notably, ‘dark matter’. And third, the Standard Model is complicated
and seemingly arbitrary. This goes against the cherished notion tha t the laws of
nature, when deeply understood, are simple and beautiful.
For the modern theoretical physicist, looking beyond the Standar d Model has
been an endeavor both exciting and frustrating. Most modern att empts are based on
string theory. There are also other interesting approaches, suc h as loop quantum
gravity and theories based on noncommutative geometry. But bac k in the mid
1970’s, before any of the currently popular approaches rose to prominence, physicists
pursued a program called ‘grand uniﬁcation’. This sought to unify the forces and
particles of the Standard Model using the mathematics of Lie group s, Lie algebras,
and their representations. Ideas from this era remain inﬂuential, b ecause grand
uniﬁcation is still one of the most fascinating attempts to ﬁnd order and beauty
lurking within the Standard Model.
1
This paper is a gentle introduction to the group representations th at describe
particles in the Standard Model and the most famous grand uniﬁed t heories. To
make the material more approachable for mathematicians, we limit ou r scope by
not discussing particle interactions or ‘symmetry breaking’—the way a theory with
a large symmetry group can mimic one with a smaller group at low energie s. These
topics lie at the very heart of particle physics. But by omitting them, we can
focus on ideas from algebra that many mathematicians will ﬁnd familiar , while
introducing the unfamiliar ways that physicists use these ideas.
In fact, the essential simplicity of the representation theory invo lved in the
Standard Model and grand uniﬁed theories is quite striking. The usu al textbook
approach to particle physics proceeds through quantum ﬁeld theo ry and gauge the-
ory. While these subjects are very important to modern mathemat ics, learning
them is a major undertaking. We have chosen to focus on the algebr a of grand
uniﬁed theories because many mathematicians have the prerequisit es to understand
it with only a little work.
A full-ﬂedged treatment of particle physics requires quantum ﬁeld t heory, which
uses representations of a noncompact Lie group called the Poincar ´ e group oninﬁnite-
dimensional Hilbert spaces. This brings in a lot of analytical subtleties, which make
it hard to formulate theories of particle physics in a mathematically rig orous way.
In fact, no one has yet succeeded in doing this for the Standard Mo del. But by ne-
glecting the all-important topic of particle interactions, we can rest rict attention to
ﬁnite-dimensional Hilbert spaces: that is, ﬁnite-dimensional complex inner product
spaces. This makes our discussion purely algebraic in ﬂavor.
Every theory we consider has an ‘internal symmetry group’ or ‘gau ge group’.
This is a compact Lie group, say G. Particles then live in representations of G on a
ﬁnite-dimensional Hilbert space V . More precisely: V can always be decomposed as
a direct sum of irreducible representations, or irreps—and for our limited purposes,
particles are basis vectors of irreps . This provides a way to organize particles, which
physicists have been exploiting since the 1960s.
The idea of ‘uniﬁcation’ has a clear meaning in these terms. Suppose V is a
representation, not only of G, but also some larger group H havingG as a subgroup.
Then we expect V to decompose into fewer irreps as a representation of H than as
a representation of G, because elements of H can mix diﬀerent irreps of G. So: by
introducing a larger symmetry group, particles can be uniﬁed into lar ger irreps.
‘Grand uniﬁcation’ occurs when the compact Lie group G is simple, and thus
not a product of other groups. A gauge theory based on G requires an invariant
inner product on its Lie algebra. When G is simple, this form is unique up to a
scale factor, which physicists call a ‘coupling constant’: this measur es the strength
of the force corresponding to G. When G is the product of simple factors, there
is one coupling constant for each factor of G. So, by using a simple Lie group as
gauge group, we minimize the number of coupling constants.
In this paper, we give an account of the algebra behind the Standar d Model
and three attempts at uniﬁcation: Georgi and Glashow’s SU(5) the ory, Georgi’s
theory based on the group Spin(10) (physicists call this the SO(10 ) theory), and
the Pati–Salam model. All three date to around 1974. The ﬁrst two a re known
as grand uniﬁed theories, or GUTs, because they are based on simp le Lie groups.
The Pati–Salam model is diﬀerent: while it is called a GUT by some authors , and
does indeed involve uniﬁcation, it is based on the Lie group SU(2) × SU(2) × SU(4),
which is merely semisimple.
It is important to note that these theories have their problems. Th e SU(5) theory
predicts that protons will decay more quickly than they do, and it re quires certain
2
trends to hold among the relative strengths of forces at high ener gies—trends which
the data do not support. The SO(10) theory may still be viable, esp ecially if at low
enough energies it reduces to the Pati–Salam model. However, the is sues involved
are complex. For details, see the paper by Bertolini et al and the many references
therein [4].
Nonetheless, it is still very much worthwhile for mathematicians to st udy the
algebra of grand uniﬁed theories. First, even apart from their phy sical signiﬁ-
cance, these theories are intrinsically beautiful mathematical str uctures. Second,
they provide a nice way for mathematicians to get some sense of the jigsaw puzzle
that physicists are struggling to solve. It is certainly hopeless tryin g to under-
stand what physicists are trying to accomplish with string theory wit hout taking
a look at grand uniﬁed theories. Finally, grand uniﬁed theories can be generalized
by adding ‘supersymmetry’—and the resulting generalizations are co nsidered seri-
ous contenders for describing the real world. For some recent ov erviews of their
prospects, see Pati [26, 27] and Peskin [29].
This is how we shall proceed. In Section 2 we start by describing the S tandard
Model. After a brief nod to the electron and photon, we explain some nuclear
physics in Section 2.1. We start with Heisenberg’s old attempt to think of the
proton and neutron as two states of a single particle, the ‘nucleon’, described by a 2-
dimensional representation of SU(2). The idea of uniﬁcation throu gh representation
theory traces its origins back to this notion.
After this warmup we tour the Standard Model in its current form. In Section 2.2
we describe the particles called ‘fundamental fermions’, which const itute matter. In
Section 2.3 we describe the particles called ‘gauge bosons’, which carry forces. Apart
from the elusive Higgs boson, all particles in the Standard Model are of these two
kinds. In Section 2.4 we give a more mathematical treatment of thes e ideas: the
gauge bosons are determined by the Standard Model gauge group
GSM = U(1) × SU(2) × SU(3),
while the fundamental fermions and their antiparticles are basis vec tors of a highly
reducible representation of this group, which we call F ⊕F ∗. Here F describes the
fermions, while F ∗ describes their antiparticles.
Amazingly, using the ideas of gauge theory and quantum ﬁeld theory , plus
the ‘Higgs mechanism’ for symmetry breaking, we can recover the d ynamical laws
obeyed by these particles from the representation of GSM onF ⊕F ∗. This informa-
tion is enough to decode the physics of these particles and make pre dictions about
what is seen in the gigantic accelerators that experimental physicis ts use to probe
the natural world at high energies. Unfortunately, to explain all th is would go far
beyond the modest goals of this paper. For a guide to further stud y, see Section
1.1.
Having acquainted the reader with the Standard Model of particle p hysics in
Section 2, we then go on to talk about grand uniﬁed theories in Sectio n 3. These
theories go beyond the Standard Model by ‘extending’ the gauge g roup. That is, we
pick a way to include GSM in some larger group G, and choose a representation V
ofG which reduces to the Standard Model representation F ⊕F ∗ when we restrict
it to GSM. We describe how this works for the SU(5) theory (Section 3.1), th e
SO(10) theory (Section 3.2), and the Pati–Salam model (Section 3.3 ). Of course,
since we do not discuss the dynamics, a lot will go unsaid about these G UTs.
As we proceed, we explain how the SU(5) theory and the Pati–Salam m odel are
based on two distinct visions about how to extend the Standard Mod el. However, we
will see that the SO(10) theory is an extension of both the SU(5) th eory (Section 3.2)
3
and the Pati–Salam model (Section 3.4). Moreover, these two rout es to the SO(10)
theory are compatible in a precise sense: we get a commuting square of groups, and
a commuting square of representations, which ﬁt together to for m a commuting
cube (Section 3.5).
In Section 4, we conclude by discussing what this means for physics: namely,
