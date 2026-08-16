---
doc_id: arxiv-1003.4485v2
doc_title: "email: baez@math.ucr.edu huerta@math.ucr.edu"
section_id: sec-007-41-shifted-abelian-groups
section_title: "Shifted Abelian Groups"
section_number: 4.1
pages: 27-33
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describ e parallel trans- port for particles and strings in terms of 2-connections on 2 -bundles."
---
Any group G automatically gives a 2-group where H is trivial. Then higher
gauge theory reduces to ordinary gauge theory. But to see what is new about
higher gauge theory, let us instead suppose that G is the trivial group. Then
t and α are forced to be trivial, and t is automatically G-equivariant. On the
other hand, the Peiﬀer identity
α(t(h))h′ = hh′h−1
is not automatic: it holds if and only if H is abelian!
27
There is also a nice picture proof that H must be abelian when G is trivial.
We simply move two elements of H around each other using the interchange
law:
• •
1
/d90/d90
1
/d4/d4 h
/d11/d19 • •
1
/d90/d90
1
/d4/d4 h′
/d11/d19
= • •/d111/d111/d89/d89
/d5/d5 h
/d11/d19
1
/d11/d19
• •/d111/d111/d89/d89
/d5/d5 1
/d11/d19
h′
/d11/d19
= • •/d89/d89 /d111/d111/d5/d5
h
/d11/d19
h′
/d11/d19
= • •/d111/d111/d89/d89
/d5/d5 1
/d11/d19
h′
/d11/d19
• •/d111/d111/d89/d89
/d5/d5 h
/d11/d19
1
/d11/d19
= • •/d90/d90
/d4/d4 h′
/d11/d19 • •/d90/d90
/d4/d4 h
/d11/d19
As a side-beneﬁt, we see that horizontal and vertical composition must be equal
when G is trivial. This proof is called the ‘Eckmann–Hilton argument’, since
Eckmann and Hilton used it to show that the second homotopy group of a space
is abelian [43].
So, we can build a 2-group where:
• G is the trivial group,
• H is any abelian Lie group,
• α is trivial, and
• t is trivial.
This is called the shifted version of H, and denoted b H.
In applications to physics, we often see H = U(1). A principal bU(1)-2-
bundle is usually called a U(1) gerbe , and a 2-connection on such a thing is
usually just called a connection. By Theorem 3, a connection on a triv ial U(1)
gerbe is just an ordinary real-valued 2-form B. Its holonomy is given by:
hol: • •
γ
/d118/d118
↦→ 1
hol: • •/d90/d90
/d4/d4 Σ
/d11/d19 ↦→ exp
(
i
∫
Σ
B
)
∈ U(1).
28
The book by Brylinski [31] gives a rather extensive introduction to U (1)
gerbes and their applications. Murray’s theory of ‘bundle gerbes’ g ives a dif-
ferent viewpoint [74, 89]. Here let us discuss two places where U(1) g erbes
show up in physics. One is ‘multisymplectic geometry’; the other is ‘2-fo rm
electromagnetism’. The two are closely related.
First, let us remember how 1-forms show up in symplectic geometry a nd
electromagnetism. Suppose we have a point particle moving in some ma nifold
M . At any time its position is a point q ∈ M and its momentum is a cotangent
vector p ∈ T ∗
q M . As time passes, its position and momentum trace out a curve
γ: [0, 1] → T ∗M.
The action of this path is given by
S(γ) =
∫
γ
(
pi ˙qi − H(q, p)
)
dt
where H: T ∗M → R is the Hamiltonian. But now suppose the Hamiltonian
is zero! Then there is still a nontrivial action, due to the ﬁrst term. We can
rewrite it as follows:
S(γ) =
∫
γ
α
where the 1-form
α = pidqi
is a canonical structure on the cotangent bundle. We can think of α as connec-
tion on a trivial U(1)-bundle over T ∗M . Physically, this connection describes
how a quantum particle changes phase even when the Hamiltonian is ze ro! The
change in phase is computed by exponentiating the action. So, we ha ve:
hol(γ) = exp
(
i
∫
γ
α
)
.
Next, suppose we carry our particle around a small loop γ which bounds a
disk D. Then Stokes’ theorem gives
S(γ) =
∫
γ
α =
∫
D
dα
Here the 2-form
ω = dα = dpi ∧ dqi
is the curvature of the connection α. It makes T ∗M into a symplectic man-
ifold, that is, a manifold with a closed 2-form ω satisfying the nondegeneracy
condition
∀v ω (u, v) = 0 = ⇒ u = 0.
29
The subject of symplectic geometry is vast and deep, but sometime s this simple
point is neglected: the symplectic structure describes the change in phase of a
quantum particle as we move it around a loop:
hol(γ) = exp
(
i
∫
D
ω
)
.
Perhaps this justiﬁes calling a symplectic manifold a ‘phase space’, tho ugh his-
torically this seems to be just a coincidence.
It may seem strange to talk about a quantum particle tracing out a lo op
in phase space, since in quantum mechanics we cannot simultaneously know a
particle’s position and momentum. However, there is a long line of work , begin-
ning with Feynman, which computes time evolution by an integral over paths
in phase space [40]. This idea is also implicit in geometric quantization, whe re
the ﬁrst step is to equip the phase space with a principal U(1)-bund le having a
connection whose curvature is the symplectic structure. (Our dis cussion so far
is limited to trivial bundles, but everything we say generalizes to the nontrivial
case.)
Next, consider a charged particle in an electromagnetic ﬁeld. Suppo se that
we can describe the electromagnetic ﬁeld using a vector potential A which is
a connection on trivial U(1) bundles over M . Then we can pull A back via
the projection π: T ∗M → M , obtaining a 2-form π∗A on phase space. In the
absence of any other Hamiltonian, the particle’s action as we move it a long a
path γ in phase space will be
S(γ) =
∫
γ
α + e π∗A
if the particle has charge e. In short, the electromagnetic ﬁeld changes the
connection on phase space from α to α + e π∗A. Similarly, when the path γ is a
loop bounding a disk D, we have
S(γ) =
∫
D
ω + e π∗F
where F = dA is the electromagnetic ﬁeld strength. So, electromagnetism also
changes the symplectic structure on phase space from ω to ω + e π∗F . For more
on this, see Guillemin and Sternberg [60], who also treat the case of no nabelian
gauge ﬁelds.
All of this has an analog where particles are replaced by strings. It h as been
known for some time that just as the electromagnetic vector pote ntial naturally
couples to point particles, there is a 2-form B called the Kalb–Ramond ﬁeld
which naturally couples to strings. The action for this coupling is obta ined
simply by integrating B over the string worldsheet. In 1986, Gawedski [54]
showed that the B ﬁeld should be seen as a connection on a U(1) gerbe. Later
Freed and Witten [52] showed this viewpoint was crucial for underst anding
anomaly cancellation. However, these authors did not actually use t he word
30
‘gerbe’. The role of gerbes was later made explicit by Carey, Johnson and
Murray [34], and even more so by Gawedski and Reis [55].
In short, electromagnetism has a ‘higher version’. What about symp lectic
geometry? This also has a higher version, which dates back to 1935 w ork by
DeDonder [39] and Weyl [92]. The idea here is that an n-dimensional classical
ﬁeld theory has a kind of ﬁnite-dimensional phase space equipped wit h a closed
(n + 2)-form ω which is nondegenerate in the following sense:
∀v1, . . . , vn+1 ω(u, v1, . . . , vn) = 0 = ⇒ u = 0.
Such a n-form is called a multisymplectic structure , or more speciﬁcally, an
n-plectic structure For a nice introduction to multisymplectic geometry, see
the paper by Gotay, Isenberg, Marsden, and Montgomery [57].
The link between multisymplectic geometry and higher electromagnet ism
was made in a paper by Baez, Hoﬀnung and Rogers [10]. Everything is c losely
analogous to the story for point particles. For a classical bosonic s tring prop-
agating on Minkowski spacetime of any dimension, say M , there is a ﬁnite-
dimensional manifold X which serves as a kind of ‘phase space’ for the string.
There is a projection π: X → M , and there is a god-given way to take any map
from the string’s worldsheet to M and lift it to an embedding of the worldsheet
in X. So, let us write Σ for the string worldsheet considered as a surfac e in X.
The phase space X is equipped with a 2-plectic structure: that is, a closed
nondegenerate 3-form, say ω. But in fact, ω = dα for some 2-form α. Even
when the string’s Hamiltonian is zero, there is a term in the action of th e string
coming from the integral of α:
S(Σ) =
∫
Σ
α.
We may also consider a charged string coupled to a Kalb–Ramond ﬁeld. This
begins life as a 2-form B on M , but we may pull it back to a 2-form π∗B on X,
and then
S(Σ) =
∫
Σ
α + e π∗B.
In particular, suppose Σ is a 2-sphere bounding a 3-ball D in X. Then by
Stokes’ theorem we have
S(Σ) =
∫
D
ω + e π∗Z
where the 3-form
Z = dB
is the Kalb–Ramond analog of the electromagnetic ﬁeld strength, an d e is the
string’s charge. (The Kalb–Ramond ﬁeld strength is usually called ‘ H’ in the
physics literature, but that conﬂicts with our usage of H to mean a Lie group,
so we shall call it ‘ Z’.)
In summary: the Kalb–Ramond ﬁeld modiﬁes the 2-plectic structure on the
phase space of the string . The reader will note that we have coyly refused to
31
describe the phase space X or its 2-form α. For this, see the paper by Baez,
Hoﬀnung and Rogers [10]. In this paper, we explain how the usual dyn amics of a
classical bosonic string coupled to a Kalb–Ramond ﬁeld can be describ ed using
multisymplectic geometry. We also explain how to generalize Poisson br ackets
from symplectic geometry to multisymplectic geometry. Just as Pois son brackets
in symplectic geometry make the functions on phase space into a Lie a lgebra,
Poisson brackets in multisymplectic geometry give rise to a ‘Lie 2-algeb ra’. Lie
2-algebras are also important in higher gauge theory in the same way that Lie
algebras are important for gauge theory. Indeed, the ‘string 2-g roup’ described
in Section 4.6 was constructed only after its Lie 2-algebra was found [7]. Later,
this Lie 2-algebra was seen to arise naturally from multisymplectic geo metry
[15].
4.2 The Poincar´ e 2-Group
Suppose we have a representation α of a Lie group G on a ﬁnite-dimensional
vector space H. We can regard H as an abelian Lie group with addition as the
group operation. This lets us regard α as an action of G on this abelian Lie
group. So, we can build a 2-group G where:
• G is any Lie group,
• H is any vector space,
• α is the representation of G on H, and
• t is trivial.
In particular, note that the Peiﬀer identity holds. In this way, we se e that
any group representation gives a crossed module—so group repre sentations are
secretly 2-groups!
For example, if we let G be the Lorentz group and let α be its obvious
representation on R4:
G = SO(3, 1)
H = R4
we obtain the so-called Poincar´ e 2-group, which has the Lorentz group as its
group of morphisms, and the Poincar´ e group as its group of 2-mor phisms [13].
What is the Poincar´ e 2-group good for? It is not clear, but there a re some
clues. Just as we can study representations of groups on vector spaces, we can
study representations of 2-groups on ‘2-vector spaces’ [6, 24, 38, 48]. The rep-
resentations of a group are the objects of a category, and this s ort of category
can be used to build ‘spin foam models’ of background-free quantum ﬁeld theo-
ries [5]. This endeavor has been most successful with 3d quantum gr avity [53],
but everyone working on this subject dreams of doing something sim ilar for 4d
quantum gravity [80]. Going from groups to 2-groups boosts the d imension of
everything: the representations of a 2-group are the objects o f a 2-category, and
Crane and Sheppeard outlined a program for building a 4-dimensional spin foam
32
model starting from the 2-category of representations of the P oincar´ e 2-group
[36].
Crane and Sheppeard hoped their model would be related to quantu m grav-
ity in 4 spacetime dimensions. This has not come to pass, at least not y et—but
this spin foam model does have interesting connections to 4d physics. The spin
foam model of 3d quantum gravity automatically includes point partic les, and
Baratin and Freidel have shown that it reduces to the usual theor y of Feynman
diagrams in 3d Minkowski spacetime in the limit where the gravitational con-
stant GNewton goes to zero [21]. This line of thought led Baratin and Freidel to
construct a spin foam model that is equivalent to the usual theory of Feynman
diagrams in 4d Minkowski spacetime [22]. At ﬁrst the mathematics un derlying
this model was a bit mysterious—but it now seems clear that this mode l is based
on the representation theory of the Poincar´ e 2-group! For a pr eliminary report
on this fascinating research, see the paper by Baratin and Wise [23].
In short, it appears that the 2-category of representations of the Poincar´ e
2-group gives a spin foam description of quantum ﬁeld theory on 4d M inkowski
spacetime. Unfortunately, while spin foam models in 3 dimensions can b e ob-
tained by quantizing gauge theories, we do not see how to obtain this 4d spin
foam model by quantizing a higher gauge theory. Indeed, we know o f no classi-
cal ﬁeld theory in 4 dimensions whose solutions are 2-connections on a principal
G-2-bundle where G is the Poincar´ e 2-group.
However, if we replace the Poincar´ e 2-group by a closely related 2- group,
this puzzle does have a nice solution. Namely, if we take
G = SO(3, 1)
H = so(3, 1)
and take α to be the adjoint representation, we obtain the ‘tangent 2-group ’ of
the Lorentz group. As we shall see, 2-connections for this 2-gro up arise naturally
as solutions of a 4d ﬁeld theory called ‘topological gravity’.
