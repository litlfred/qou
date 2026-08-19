---
doc_id: arxiv-1003.4485v2
doc_title: "email: baez@math.ucr.edu huerta@math.ucr.edu"
section_id: sec-008-43-tangent-2-groups
section_title: "Tangent 2-Groups"
section_number: 4.3
pages: 33-37
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describ e parallel trans- port for particles and strings in terms of 2-connections on 2 -bundles."
---
We have seen that any group representation gives a 2-group. But any Lie group
G has a representation on its own Lie algebra: the adjoint represent ation. This
lets us build a 2-group from the crossed module where:
• G is any Lie group,
• H is g regarded as a vector space and thus an abelian Lie group,
• α is the adjoint representation, and
• t is trivial.
We call this the tangent 2-group T G of the Lie group G. Why? We have
already seen that for any Lie 2-group, the group of all 2-morphism s is the
semidirect product G ⋉ H. In the case at hand, this semidirect product is just
33
G ⋉ g, with G acting on g via the adjoint representation. But as a manifold,
this semidirect product is nothing other than the tangent bundle T G of the Lie
group G. So, the tangent bundle T G becomes a group, and this is the group of
2-morphisms of T G.
By Theorem 3, a 2-connection on a trivial T G-2-bundle consists of a g-valued
1-form A and a g-valued 2-form B such that the curvature F = dA + A ∧ A
satisﬁes
F = 0,
since t(B) = 0 in this case. Where can we ﬁnd such 2-connections? We can ﬁnd
them as solutions of a ﬁeld theory called 4-dimensional BF theory!
BF theory is a classical ﬁeld theory that works in any dimension. So, tak e an
n-dimensional oriented manifold M as our spacetime. The ﬁelds in BF theory
are a connection A on the trivial principal G-bundle over M , together with a
g-valued (n − 2)-form B. The action is given by
S(A, B) =
∫
M
tr(B ∧ F ).
Setting the variation of this action equal to zero, we obtain the follo wing ﬁeld
equations:
dB + [A, B] = 0 , F = 0.
In dimension 4, B is a g-valued 2-form—and thanks to the second equation, A
and B ﬁt together to deﬁne a 2-connection on the trivial T G-2-bundle over M .
It may seem dull to study a gauge theory where the equations of mo tion
imply the connection is ﬂat. But there is still room for some fun. We se e this
already in 3-dimensional BF theory, where B is a g-valued 1-form rather than a
2-form. This lets us package A and B into a connection on the trivial T G-bundle
over M . The ﬁeld equations
dB + [A, B] = 0 , F = 0
then say precisely that this connection is ﬂat.
When the group G is the Lorentz group SO(2 , 1), T G is the corresponding
Poincar´ e group. With this choice of G, 3d BF theory is a version of 3d general
relativity. In 3 dimensions, unlike the more physical 4d case, the equ ations
of general relativity say that spacetime is ﬂat in the absence of matter. And
at ﬁrst glance, 3d BF theory only describes general relativity without matter.
After all, its solutions are ﬂat connections.
Nonetheless, we can consider 3d BF theory on a manifold from which the
worldline of a point particle has been removed. In the Bohm–Aharono v eﬀect, if
we carry a charged object around a solenoid, we obtain a nontrivial phase even
though the U(1) connection A is ﬂat outside the solenoid. Similarly, in 3d BF
theory, the connection ( A, B) will be ﬂat away from the particle’s worldline, but
34
it can have a nontrivial holonomy around a loop γ that encircles the worldline:
γ
This holonomy says what happens when we parallel transport an obj ect around
our point particle. The holonomy is an element of the Poincar´ e group . Its
conjugacy class describes the mass and spin of our particle. So, massive spinning
point particles are lurking in the formalism of 3d BF theory!
Even better, this theory predicts an upper bound on the particle’s mass,
roughly the Planck mass. This is true even classically. This may seem st range,
but unlike in 4 dimensions, where we need c, GNewton and ℏ to build a quantity
with dimensions of length, in 3-dimensional spacetime we can do this us ing only
c and GNewton. So, ironically, the ‘Planck mass’ does not depend on Planck’s
constant.
Furthermore, in this theory, particles have ‘exotic statistics’, mea ning that
the interchange of identical particles is governed by the braid grou p instead of
the symmetric group. Particles with exotic statistics are also known as ‘anyons’.
In the simplest examples, the anyons in 3d gravity reduce to bosons or fermions
in the GNewton → 0 limit.
There is thus a wealth of interesting phenomena to be studied in 3d BF
theory. See the paper by Baez, Crans and Wise [9] for a quick over view, and
the work of Freidel, Louapre and Baratin for a deep treatment of t he details
[21, 53].
The case of 4d BF theory is just as interesting, and not as fully explored.
In this case the ﬁeld equations imply that A and B deﬁne a 2-connection on
the trivial T G-2-bundle over M . But in fact they say more: they say precisely
that this 2-connection is ﬂat . By this we mean two things. First, the holonomy
hol(γ) along a path γ does not change when we change this path by a homotopy.
Second, the holonomy hol(Σ) along a surface Σ does not change whe n we change
this surface by a homotopy. The ﬁrst fact here is equivalent to the equation
F = 0. The second is equivalent to the equation dB + [A, B] = 0.
When the group G is the Lorentz group SO(3 , 1), 4d BF theory is sometimes
called ‘topological gravity’. We can think of it as a simpliﬁed version of ge neral
relativity that acts more like gravity in 3 dimensions. In particular, we can
copy what we did in 3 dimensions, and consider 4d BF theory on a manifold
from which the worldlines of particles and the worldsheets of strings have been
removed. Some of what we will do here works for more general grou ps G, but
let us take G = SO(3, 1) just to be speciﬁc.
First consider strings. Take a 2-dimensional manifold X embedded in a 4-
dimensional manifold M , and think of X as the worldsheet of a string. Suppose
35
we can ﬁnd a small loop γ that encircles X in such a way that γ is contractible
in M but not in M − X. If we do 4d BF theory on the spacetime M − X, the
holonomy
hol(γ) ∈ SO(3, 1)
will not change when we apply a homotopy to γ. This holonomy describes the
‘mass density’ of our string [9, 20].
Next, consider particles. Take a curve C embedded in M , and think of C as
the worldline of a particle. Suppose we can ﬁnd a small 2-sphere Σ in M − C
that is contractible in M but not M − C. We can think of this 2-sphere as a
2-morphism Σ: 1 x ⇒ 1x in the path 2-groupoid of M . If we do 4d BF theory
on the spacetime M − C, the holonomy
hol(Σ) ∈ so(3, 1)
will not change when we apply a homotopy to Σ. So, this holonomy desc ribes
some information about the particle—but so far as we know, the phy sical mean-
ing of this information has not been worked out.
What if we had a ﬁeld theory whose solutions were ﬂat 2-connections for the
Poincar´ e 2-group? Then we would have
hol(Σ) ∈ R4
and there would be a tempting interpretation of this quantity: name ly, as the
energy-momentum of our point particle. So, the puzzle posed at th e end of the
previous section is a tantalizing one.
One may rightly ask if the ‘strings’ described above bear any relation to those
of string theory. If they are merely surfaces cut out of spacetim e, they lack the
dynamical degrees of freedom normally associated to a string. Cer tainly they
do not have an action proportional to their surface area, as for t he Polyakov
string. Indeed, one may ask if ‘area’ even makes sense in 4d BF theory. After
all, there is no metric on spacetime: the closest substitute is the so(3, 1)-valued
2-form B.
Some of these problems may have solutions. For starters, when we remove
a surface X from our 4-manifold M , the action
S(A, B) =
∫
M−X
tr(B ∧ F )
is no longer gauge-invariant: a gauge transformation changes the action by a
boundary term which is an integral over X. We can remedy this by introducing
ﬁelds that live on X, and adding a term to the action which is an integral over X
involving these ﬁelds. There are a number of ways to do this [14, 49, 5 9, 50, 73].
For some, the integral over X is proportional to the area of the string worldsheet
in the special case where the B ﬁeld arises from a cotetrad (that is, an R4-valued
1-form) as follows:
B = e ∧ e
36
where we use the isomorphism Λ 2R4 ∼
= so(3, 1). In this case there is close rela-
tion to the Nambu–Goto string, which has been carefully examined by Fairbairn,
Noui and Sardelli [50].
This is especially intriguing because when B takes the above form, the BF
action becomes the usual Palatini action for general relativity:
S(A, e) =
∫
M
tr(e ∧ e ∧ F )
where ‘tr’ is a suitable nondegenerate bilinear form on so(3, 1). Unfortunately,
solutions of Palatini gravity typically fail to obey the condition t
(B) = F when
we take B = e∧e. So, we cannot construct 2-connections in the sense of Theorem
3 from these solutions! If we want to treat general relativity in 4 dim ensions as
a higher gauge theory, we need other ideas. We describe two possib ilities at the
end of Section 4.5.
