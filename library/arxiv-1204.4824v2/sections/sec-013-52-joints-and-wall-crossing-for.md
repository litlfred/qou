---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-013-52-joints-and-wall-crossing-for
section_title: "Joints and wall-crossing for"
section_number: 5.2
pages: 23-30
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
Deﬁne a joint to be a point z ∈ C where at least two S-walls intersect. A joint thus
supports at least two charges, say ¯a∈ Γij(z,z ) and ¯b∈ Γkl(z,z ).
ij
ij kl
kl
Figure 9 . The local picture around a joint where exactly two S-walls meet. We also show two
paths ℘, ℘′ on C which are related to one another by regular homotopy across the joint.
The simplest situation arises if the joint z supports only these two charges, so exactly
twoS-walls meet there. This can only occur if i⁄= l and j⁄= k. In that case the local
picture around z is as shown in Figure 9.
Now let us consider what happens to the soliton degeneracies µ as we move across a
joint. As it turns out, we can answer this question completely by considering the defect
operators attached to the paths℘,℘′ onC shown in Figure 9. The requirement of homotopy
invariance says that
F (℘,ϑ ) =F (℘′,ϑ ). (5.1)
To understand what this really means, let us evaluate both sides using the rules of §4.4,
and then deform all the resulting paths on ˜Σ so that they run directly into the joint z,
– 21 –
with a common tangent vector ˜z at z. Then we obtain
D(℘+)(1 +µ(a,p )Xa˜z)(1 +µ(b,q )Xb˜z)D(℘−) =
D(℘+)(1 +µ(b,q′)Xb˜z)(1 +µ(a,p′)Xa˜z)D(℘−). (5.2)
The paths a˜z and b˜z are not composable in either direction (since a˜z runs from ˜z(i) to ˜z(j)
while b˜z runs from ˜z(k) to ˜z(l)), so we have Xa˜zXb˜z =Xb˜zXa˜z = 0. Considering the terms
linear in Xa˜z and Xb˜z in (5.2) then gives
µ(a,p ) =µ(a,p′), (5.3)
µ(b,q ) =µ(b,q′). (5.4)
In short: when an S-wall of type ij and anS-wall of type kl meet transversely, they cross
without any changes in µ.
ij
jk
ik
ij
ik
jk
Figure 10. The local picture around a generic collision between three S-walls.
A more interesting situation arises when anS-wall of type ij and anS-wall of type jk
meet transversely. Suppose the two walls support charges ¯a∈ Γij(z,z ) and ¯b∈ Γjk(z,z ).
(Note that in this case we must have i⁄=k; otherwise the two walls would obey the same
diﬀerential equation, and it would be impossible for them to intersect transversely.) In this
case the joint z supports both ¯a and ¯b, which are composable since z(j) is both the end of
¯a and the start of ¯b. Hence the joint also supports a third charge ¯ c = ¯a + ¯b∈ Γik(z,z ),
and so there could be a third S-wall meeting z. When µ is generic enough, the picture is
as shown in Figure 10. 17
The condition
F (℘,ϑ ) =F (℘′,ϑ ) (5.5)
becomes
D(℘+)(1 +µ(a,p )Xa˜z)(1 +µ(c,q )Xc˜z)(1 +µ(b,r )Xb˜z)D(℘−) = (5.6)
D(℘+)(1 +µ(b,r′)Xb˜z)(1 +µ(c,q′)Xc˜z)(1 +µ(a,p′)Xa˜z)D(℘−).
17One might think that there is a second, inequivalent possibility: one could have exchanged the ij and
jk labels in Figure 10. This gives a new picture, which is not related to Figure 10 by a rotation, but is
related to Figure 10 by an orientation-reversing map. Fortunately, our rules for computing F (℘,ϑ ) do not
use the orientation of C. So our analysis is fully general.
– 22 –
Using Xa˜zXb˜z = (−1)w(a˜z+b˜z,c˜z)Xc˜z and Xb˜zXa˜z = 0, (5.6) implies
µ(a,p′) =µ(a,p ), (5.7)
µ(b,r′) =µ(b,r ), (5.8)
µ(c,q′) =µ(c,q ) + (−1)w(a˜z+b˜z,c˜z)µ(a,p )µ(b,r ). (5.9)
The result (5.9) says that the number of solitons carrying charge ¯c changes as we move
the modulus z of the surface defect Sz across the joint. This reﬂects the phenomenon
of decay/formation of bound states between solitons of charges ¯ a and ¯b. Indeed (5.9) is
the same wall-crossing formula which was discovered in [38] in the context of pure 2d
theories, and was reinterpreted in the 2d-4d context in [5]. Our derivation of it here, using
consistency of the framed 2d-4d BPS spectrum, is essentially the same as the one given in
[5].
There are a few important special cases which deserve separate discussion. One arises
when µ(c,q ) = 0, so that we actually have only two S-walls intersecting, of types ij and
jk. In this case the situation is as shown in Figure 11: the wall q′ is born from the joint,
and (5.9) reduces to µ(c,q′) = (−1)w(a˜z+b˜z,c˜z)µ(a,p )µ(b,r ).
ij
jkij
ik
jk
Figure 11. A collision between S-walls, at which a new S-wall is born.
The reverse situation is also allowed: if µ(c,q ) =−(−1)w(a˜z+b˜z,c˜z)µ(a,p )µ(b,r ), then
(5.9) gives µ(c,q′) = 0, so the wall q “dies” at the joint, as shown in Figure 12.
ij
jkij
ik
jk
Figure 12. A collision between S-walls, at which anS-wall dies.
So far we have described some local properties of Wϑ and µ. In the next few sections
we describe a recipe for explicitly constructing them.
5.3 The mass ﬁltration; Wϑ[Λ] and µ[Λ] for small Λ
We begin with the observation that Wϑ carries a useful ﬁltration. Namely, for any Λ > 0
(with dimensions of mass), we can deﬁne a new objectWϑ[Λ] by truncating all theS-walls:
for a wall w supporting a charge ¯a,Wϑ[Λ] includes only the portion of w with|Z¯a| < Λ.
So
Wϑ[Λ]⊂W ϑ[Λ′] for Λ≤ Λ′ (5.10)
– 23 –
and
Wϑ = lim
Λ→∞
Wϑ[Λ]. (5.11)
We also deﬁne a truncated version µ[Λ] of the soliton degeneracies µ: µ[Λ](a) is deﬁned
only for charges a with|Z¯a|< Λ, and for such charges it agrees with µ(a).
For small enough Λ, we can describeWϑ[Λ] andµ[Λ] simply and explicitly. The reason
is that charges ¯a∈ Γ(z,z ) with|Z¯a|< Λ are represented by very short paths on Σ between
distinct lifts z(i) and z(j) of z. The only way to get such a short path is for z to be close
to an (ij) branch point b: then if we take ¯a∈ Γ(z,z ) to be a path running from z(i) to
the ramiﬁcation point over b and returning to z(j), we indeed have|Z¯a|→ 0 as z→ b. We
could also have considered the charge−¯a∈ Γ(z,z ), corresponding to a path running in the
opposite direction. These two charges are exchanged by the monodromy when z goes once
around b. They are the only charges which become massless at b.
So, to determine Wϑ[Λ] for Λ small, we just have to describe the S-walls supporting
these light charges. Letting z be a local coordinate with z = 0 at b, we have Z¯a∼ z3/2
and Z−¯a∼−z3/2 (the square-root branch cut arises from the monodromy ¯a→− ¯a noted
above.) It follows that there are 3 S-walls emerging from the branch point, as shown in
Figure 13.
ij
ji ij
(ij)
(ij)
Figure 13. The 3 S-walls emerging from a branch point. Because the two relevant sheets of the
covering Σ→C are exchanged by monodromy around the branch point, we cannot assign labels to
the trajectories globally; instead we have chosen a branch cut and a labeling of the sheets i and j
on the complement of the cut. We also label the cut with the transposition ( ij) which relates the
sheets on the two sides of the cut.
If z lies on one of these three S-walls near b, then there is a light 2d-4d BPS soliton
on the surface defect Sz, with central charge in R−eiϑ.18 This BPS soliton is represented
by a short ﬁnite open web N(z), consisting of a single BPS string connecting z to b, as
illustrated in Figure 14. In accordance with the general rules of §3.2, the charge ¯a of this
BPS state is ¯a = [N(z)Σ], where N(z)Σ is the lift of N(z) to Σ, i.e. a short path on Σ
running from z(i) to the ramiﬁcation point over b and then back to z(j).
As we have mentioned in§3.5, however, to ﬁx the sign of the BPS degeneracy for this
soliton, we need to choose a lift from the charge ¯ a to a class a. Suppose we make the
18In a sense it would be better to refer to these light states simply as “2d” solitons rather than “2d-4d,”
since their existence does not depend much on the coupling to the 4d theory. Indeed, the existence of these
light states can be deduced from a universal computation involving the simplest nontrivial Landau-Ginzburg
model. See Section 8.1 of [5] for further discussion.
– 24 –
(ij)
ij
Figure 14. A ﬁnite open web N(z) consisting of a single short ij-trajectory, with one end on the
(ij)-branch point b and one end on z. This ﬁnite open web represents a light BPS soliton on the
surface defect Sz.
most obvious choice, namely the one determined by the web N(z): a = [N(z)˜Σ]. Let p
denote theS-wall on which z sits. Then ﬁnally µ(a,p ) is a well deﬁned integer, and it is
meaningful to ask what it is. We have a single isolated 2d-4d BPS web here, so it should
contribute just a single state; the only question is whether we will have µ(a,p ) = +1 or
µ(a,p ) =−1. We claim that the correct answer is
µ(a,p ) = +1. (5.12)
Indeed, this is forced on us by the requirement of homotopy invariance, which we discuss
in§5.6 below.
5.4 Wϑ[Λ] and µ[Λ] for general Λ
We have determinedWϑ[Λ] and µ[Λ] for small Λ. Now we can ask how Wϑ[Λ] and µ[Λ]
evolve as Λ increases. Using the properties of Wϑ and µ we have already determined, it is
straightforward to deduce the answer.
The threeS-walls emerging from each branch point b ﬂow according to the diﬀerential
equation (3.1), for a distance determined by the cutoﬀ Λ. When we increase Λ enough, it
might happen that anS-wall of type ij intersects anotherS-wall of type jk. At this point
a newS-wall of type ik is born, as shown in Figure 11. The soliton degeneracy µ on this
new wall is determined by the soliton degeneracies on its parents, as in (5.9). 19 This new
“secondary”S-wall, in turn, also evolves according to (3.1). As Λ increases the secondary
walls can intersect with other S-walls and give birth to yet more progeny, and so on. In
Figure 15 we give an illustration of the growth of Wϑ[Λ] with Λ in one particular theory
S[g,C,D ].
We may also have intersections where three S-walls meet at a point, as in Figure 10.
(The reader might feel that this phenomenon should not occur generically; indeed, three
arbitrary trajectories of types ij, jk, ik would be unlikely to intersect at a single point,
but theS-walls are not arbitrary trajectories. We include an example in Figure 16.)
There is one more complicated phenomenon which one can imagine: what would hap-
pen if an S-wall of type ij ran directly into an ( ij) branch point? In this case it would
not be immediately clear how to continue the network Wϑ[Λ] and the BPS degeneracies
µ[Λ]. This puzzling-looking situation cannot occur when ϑ is generic. It does occur for
non-generic ϑ, and this fact plays a crucial role in the considerations of §6 below.
19Note that if two S-walls carrying charges ¯a∈ Γij, ¯b∈ Γjk meet at a joint z∈ C, the joint is visible
inWϑ[Λ] beginning at Λ = Max(|Z¯a(z)|,|Z¯b(z)|), but theS-wall born from the joint does not appear until
Λ =|Z¯a(z)| +|Z¯b(z)|.
– 25 –
Figure 15 . Sample Wϑ[Λ] in the theory S[A2, CP1,D ] where the Dn are 3 full defects (blue
dots at z =−1, 0, 1). We choose ϑ = π/4, φ2 = 2
(z−1)2 + 2
(z+1)2− 4
z2 , φ3 = 1−3(z−1)+6(z−1)2
(z−1)3 +
1+3(z+1)+6(z+1)2
(z+1)3 − 2+12z2
z3 . The plots shown are at Λ = 1, 2, 5, 12, 20,∞. At Λ = 0 threeS-walls are
born at each of the 6 branch points (orange crosses); at larger values of Λ, additional S-walls are
born at intersections. As Λ →∞ allS-walls asymptotically approach the defects. Some S-walls
are cut oﬀ by the boundary of the plot; the visible range is a square with side length 2 .6. See [43]
for an animated version of this ﬁgure.
We have now given a recipe for constructingWϑ[Λ] andµ[Λ] for any Λ> 0 and generic
ϑ.Wϑ[Λ] consists of a ﬁnite number ofS-walls for any Λ. Taking the limit Λ→∞ we obtain
the fullWϑ andµ. So we have now managed to determine all of the soliton degeneracies of
the theory (including their tricky signs) using only the constraint of homotopy invariance!
More precisely, so far we have ﬁxed some ϑ and determined all µ(a,p ) — i.e. we de-
terminedµ(a) when the parameter z of the surface defect lies on an S-wall supporting the
charge a. This is not what one would usually mean by “determining the soliton degen-
eracies”: what one would usually mean is that we ﬁx some z once and for all, and then
compute all µ(a) for a∈ ˜Γ(˜z, ˜z). The point is that, for any a∈ ˜Γ(˜z, ˜z), there is some ϑ for
which z does lie on an S-wall supporting a: namely, ϑ = arg−Z¯a. So for each a we can
draw the corresponding networkWϑ=arg−Z¯a and use it to compute µ(a).
– 26 –
Figure 16. A portion of a sample Wϑ, exhibiting an intersection between three S-walls, marked
by a yellow dot. The region in the blue box is blown up at right. The S-walls which appear
somewhere in the genealogy of the three intersecting S-walls are shown in black; other S-walls are
shown in gray. There are six branch points (orange crosses). This example arises in the theory
S[A3,C = CP1,D ] with φ2 =−10z dz2, φ3 = 4 dz3, φ4 = 9z2 dz4. We took ϑ = 1.841, but we
emphasize that this triple intersection persists for nearby ϑ as well.
5.5 Wϑ near full defects
On a close look at Figure 15, one notices that as Λ → ∞, all of the S-walls in W[Λ]
asymptotically approach the full defects Dn.
To understand this concretely, let us consider the general behavior of ij-trajectories
around a full defect. In a local coordinate z where the defect is at z = 0, we have
λ(i) =m(i) dz
z +··· (5.13)
where··· denotes regular terms. ij-trajectories near z = 0 thus behave asymptotically like
z(t) =z0 exp(ξ(ij)t), (5.14)
where we deﬁned
ξ(ij) = eiϑ
m(i)−m(j). (5.15)
As t→∞ , we have z(t)→ 0 if and only if Re ξ(ij) < 0. This suggests a natural ordering
on the sheets in a neighborhood of z = 0: we say that i<j if Ree−iϑm(i) < Ree−iϑm(j).
ij-trajectories near z = 0 asymptote to z = 0 if and only if i<j in this ordering.
In the coordinate z, these infalling trajectories asymptotically approach logarithmic
spirals. Passing to the covering coordinate w = logz, the ij-trajectories are straight lines,
w(t) =w0 +ξ(ij)t. (5.16)
Now suppose we have an infalling asymptotic S-wall of type ij and another of type jk
(so i<j <k .) Assuming arg ξ(ij)⁄= argξ(jk), these two walls intersect at inﬁnitely many
– 27 –
points as they spiral into z = 0. Each intersection gives birth to a new S-wall of type
ik, which also spirals into z = 0. This new S-wall can in turn intersect other inspiraling
S-walls and give birth to yet more progeny. The strict ordering of the sheets ensures that
the progeny cannot commit incest with one another. Nevertheless, for K >2 there are an
inﬁnite number of joints accumulating at the full defect. See Figure 17 for an illustration.
Similar (but more involved) remarks should apply for more general types of defect.
Figure 17. S-walls falling into a full defect, shown in the covering coordinate w = logz. There
is a single ij wall and a single jk wall. We have i < j < kin the ordering described in the text.
Each intersection between these two walls generates a new ik wall. There are inﬁnitely many such
intersections, accumulating at the defect, which generate inﬁnitely many ik walls.
Based on computer experimentation, we expect that the behavior observed in Figure
15 is indeed generic: whenever there is a defect with suﬃciently generic mass parameters,
and ϑ is generic, all S-walls in Wϑ should asymptotically approach punctures. In the
case K = 2 this follows directly from known mathematical results on the trajectories of
quadratic diﬀerentials [44] (see [3] for an account of this.) For K > 2 the analogous
foundational results are not yet available as far as we know. It would be very desirable to
work this out.
