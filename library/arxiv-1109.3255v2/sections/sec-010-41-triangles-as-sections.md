---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE"
section_id: sec-010-41-triangles-as-sections
section_title: "Triangles as sections"
section_number: 4.1
pages: 32-40
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
schetz ﬁbration having as base a strip with a Z–family of critical values. Once this is
done, we can apply a TQFT for counting sections of Lefschetz ﬁbra tions developed
by Seidel [41, 39].
We consider the deformation of the Lefschetz ﬁbration over the t riangle where the
critical values bubble out along one of the sides. At the end of this de generation, we
count sections of a trivial ﬁbration over a (k+3)–gon, along with sections of k identical
ﬁbrations, each having a disk with one critical value and one boundar y marked point.
Each of these ﬁbrations is equipped with a Lagrangian boundary con dition given by
following the degeneration of the original Lagrangian submanifolds. The sections of
the trivial ﬁbration over the ( k + 3)–gon can be reduced to counts in the ﬁber, while
the counts of the k other parts are identical, and can be computed directly using the
techniques of [39].
4.1. Triangles as sections. Let q1 ∈ HF 0(L(0),L (n)) and q2 ∈ HF 0(L(n),L (n +
m)) be two degree zero morphisms whose Floer product µ2(q2,q 1) we wish to compute.
Suppose that p ∈ HF 0(L(0),L (n +m)) contributes to this product. Let S denote
a disk with three boundary punctures, and a complex structure th at is allowed to
vary. To ﬁnd the coeﬃcient of p inµ2(q2,q 1), we count pseudo-holomorphic triangles,
that is, pseudo-holomorphic maps u :S →X(B) that send the punctures to q1,q 2,p
and the boundary components to L(0),L (n),L (n +m). Various authors have studied
the construction of such invariants; we follow the theory as develo ped by Seidel in
[41, 39].
MIRROR OF THE PROJECTIVE PLANE 33
Because we want to make contact with the theory of pseudo-holom orphic sections of
Lefschetz ﬁbrations, we need to import the setup from [39, §2.1]. Let π :E →B be a
exact symplectic Lefschetz ﬁbration. We choose primitive θ for the symplectic form ω
such that the Liouville vector ﬁeld Z deﬁned on the ﬁber M byιZ(ω|M ) = θ|M points
outward along the boundary of M. The ﬂow of Z deﬁnes a collar [ −ǫ, 0] ×M →M,
and we let σ be the function on a neighborhood of ∂M given by projection to the
[−ǫ, 0] factor. We pick an almost complex structure j on the base of the ﬁbration, we
always consider an almost complex structure J on the total space which is compatible
relative to j, meaning
(1) J is integrable in a neighborhood of each critical point,
(2) π is a (J,j )-holomorphic map,
(3) For each ﬁber Ez, the form ω(·,J ·)|TE z is symmetric and positive deﬁnite
(4) on a neighborhood of the horizontal boundary of E, J satisﬁes θ ◦J =d(eσ).
Later on, in Section 4.4, we will also need to consider J which are horizontal, meaning
that J preserves the horizontal subspaces of the symplectic connectio n. Once we
extend the Lagrangian boundary condition Section 4.2 so that our L agrangians are
compact in each ﬁber, these conditions imply that the curves we wish to count lie in
a compact subset disjoint from the horizontal boundary [39, Lem ma 2.2]. The second
condition is particularly useful because it allows us to study pseudo- holomorphic
curves by projecting them to the base of the ﬁbration.
Consider the projection of such a triangle to the base by w : X(B) → X(I).
This yields a 2-chain on the base with boundary on the corresponding base paths
ℓ(0),ℓ (n),ℓ (n +m) with corners at the points w(q1),w (q2),w (p). This projection is
not necessarily embedded, so the next step is to pass to the univer sal cover of the
base. Let ˜X(I) denote inﬁnite strip which is the universal cover of the annulus, an d
let ˜w : ˜X(B) → ˜X(I) denote the induced ﬁbration. We denote by π : ˜X(B) →X(B)
the covering map. When drawing pictures in the base ˜X(I), we can represent it as
[−1, 1] × R, with the inﬁnite direction drawn vertically. With this convention, the
path ℓ(d) lifts to a Z-family of paths which have slope −d.
Figure 8 shows the universal cover of X(I), with the base paths for L(0),L(1), and
L(2).
The choice of lift of q1 determines a lift of L(0) and L(n), which then determines a
lift of q2 and of L(n +m), which in turn determines where the lift of any p must lie.
By looking at the slopes of the base paths ℓ(0),ℓ (n),ℓ (n +m) involved, we obtain the
following proposition:
Proposition 4.1. In the terminology of Deﬁnition 4, Suppose that q1 = qa,i lies in
the ﬁber indexed by a/n, and that q2 =qb,j lies in the ﬁber indexed by b/m. Then any
p contributing to the product is qa+b,h for some h, that is, it lies in the ﬁber indexed
by (a +b)/(n +m)
We can rephrase this proposition as saying that we can introduce a s econd grading
on HF ∗(L(d),L (d +n)) where HF ∗,a(L(d),L (d +n)) is generated by qa,i for i ∈
{0, 1,...
⌊
n−|a|
2
⌋
}, and that µ2 respects this grading.
We must now consider two cases: either the input generators q1 andq2 lie in diﬀerent
ﬁbers of w, or they lie in the same ﬁber. The rest of this section is devoted to ca se
where q1 and q2 lie in diﬀerent ﬁbers, which is the more diﬃculty one. In the case
34 JAMES PASCALEFF
Figure 8. The universal cover of X(I).
whereq1 andq2 lie in the same ﬁber, the preceding proposition says that the output p
must also lie in the same ﬁber. This means that we can compute the con tribution of p
toµ2(q2,q 1) by counting triangles that lie entirely in this ﬁber, since the project ion of
such a triangle to the base must be constant. We will employ an altern ative strategy
where we perturb one of the base paths, say ℓ(0), by a small amount so that there
are no points where all three base paths intersect. This forces th e triangle in the
ﬁber to spread out over a small triangle in the base, so that in partic ular it cannot be
constant. With this proviso, the arguments in this section apply with out exception.
Now we show that any triangles contributing to the product of inter est are sections
of the Lefschetz ﬁbration ˜w : ˜X(B) → ˜X(I):
Proposition 4.2. Let u :S →X(B) be a pseudo-holomorphic triangle contributing
to the component of p in µ2(q2,q 1), such that q1 and q2 do not lie in the same ﬁber of
w. Then there is a triangle T in ˜X(I) bounded by appropriate lifts of ℓ(0),ℓ (n) and
ℓ(n +m), a holomorphic isomorphism τ :S →T , and a pseudo-holomorphic section
s :T → ˜X(B), such that u =π ◦s ◦τ .
Conversely, any pseudo-holomorphic section s : T → ˜X(B) with boundary on
L(0),L (n),L (n +m) which maps the corners to q2,q 1,p contributes to the coeﬃcient
of p in µ2(q2,q 1).
Proof. Since u :S →X(B) is a map from a simply-connected domain, there is a lift
˜u : S → ˜X(B). Since q1 and q2 are not in the same ﬁber, the image of u cannot
be contained entirely within a ﬁber. The triangle T and the lifts of the ℓ(d) are
determined by the considerations from the previous proposition. C learly ˜w ◦ ˜u deﬁnes
a 2-chain in ˜X(I), which by maximum principle is supported on T . By positivity
of intersection with the ﬁbers of ˜ w, all components of this 2-chain are positive, and
the map ˜w ◦ ˜u : S → T is a ramiﬁed covering. However, if the degree were greater
than one, then ∂S would have to wind around ℓ(0),ℓ (n),ℓ (n +m) more than once,
contradicting the boundary conditions we placed on the map u.
MIRROR OF THE PROJECTIVE PLANE 35
Since the projection ˜w : ˜X(B) → ˜X(I) is holomorphic, the composition ˜ w ◦ ˜u :
S → T is a holomorphic map which sends the boundary to the boundary and t he
punctures to the punctures, so it is a holomorphic isomorphism, and we let τ be its
inverse.
For the converse, uniformization for the disk with three boundary punctures yields
a complex structure on S and a map τ :S →T , such the composition ˜u =s ◦τ is the
desired triangle in ˜X(B). Composing this with π : ˜X(B) →X(B) yields the triangle
in X(B). □
Proposition 4.3. Suppose q1 = qa,i lies in the ﬁber indexed by a/n, and q2 = qb,j
in the ﬁber indexed by b/m. Then the sections in Proposition 4.2 cover the critical
values of the Lefschetz ﬁbration k times, where
• k = 0 if a and b are both non-negative or both non-positive.
• k = min(|a|, |b|) if a and b have diﬀerent signs.
Proof. We identify ˜X(I) with [ −1, 1] × R. The critical values lie at the points {0} ×
(Z + 1
2 ).
Ifa andb are both non-negative or both non-positive, then the triangle T is entirely
to one side of the vertical line {0} × R where all the critical values lie.
Suppose a and b have opposite signs and |a| ≤ |b|. Then the output point lies at
(a +b)/(n +m), which has the same sign as b. The side of T corresponding to ℓ(n)
crosses the line {0} ×R at (0,a ), while the side corresponding to ℓ(0) crosses at (0, 0),
so the distance is |a|, and in fact the set {0} × (Z + 1
2) contains |a| points in this
interval.
If |b| ≤ |a|, the output point at ( a +b)/(n +m) has the same sign as a, and so we
need to look at where ℓ(n +m) intersects the line {0} ×R. This happens at (0 ,a +b),
and the distance to (0 ,a ) is |b|. □
With the notation introduced so far, we can state the main result of our computa-
tion for µ2(qb,j,q a,i).
Proposition 4.4. Suppose that qa,i ∈HF 0(L(0),L (n)) and qb,j ∈HF 0(L(n),L (n +
m)) as in Deﬁnition 4, and let k be as in Proposition 4.3. Then
(65) µ2(qb,j,q a,i) =
k∑
s=0
(k
s
)
qa+b,i+j+s
Proof. This proposition is the combination of Propositions 4.8, 4.10, 4.12, 4.13 , and
4.24. □
The proof of Proposition 4.4 is where most of the technical work of t his paper is
spent, and it will occupy Sections 4.2–4.6. Sections 4.2 and 4.3 presen t a technique
for degenerating the total space of the Lefschetz ﬁbration to b reak these counts into
simpler pieces. Sections 4.4 and 4.5 compute these pieces, and Sectio n 4.6 determines
the signs.
We shall now reformulate Proposition 4.4 in algebro-geometric terms . Let
(66) A =
∞⨁
d=0
Ad =
∞⨁
d=0
H 0(P2, OP2(d)) ∼= K[x,y,z ]
36 JAMES PASCALEFF
be the homogeneous coordinate ring of P2. We write elements of Ad =H 0(P2, OP2(d))
as degree d homogeneous polynomials in the variables x,y,z . Deﬁne
(67) p =xz −y2,
and set, for a ∈ {−d,...,d }, i ∈ {0,...,
⌊
d−|a|
2
⌋
},
(68) Qa,i =
{
x−apiyd+a−2i if a ≤ 0
zapiyd−a−2i if a> 0
}
∈Ad.
Proposition 4.5. TakeQa,i ∈An and Qb,j ∈Am, then in A,
(69) Qa,iQb,j =
k∑
s=0
(k
s
)
Qa+b,i+j+s
wherek = min(|a|, |b|) if a and b have diﬀerent signs, and k = 0 otherwise.
Proof. The case where a and b have the same sign is obvious.
Suppose that a ≤ 0 and b ≥ 0, and suppose that |a| ≤ |b|. Then we have a +b ≥ 0,
and k = −a.
(70) Qa,iQb,j =x−apiyn+a−2izbpjym−b−2j =za+b(xz)kpi+jyn+m+a−b−2(i+j)
Since xz =p +y2, we have
(71) ( xz)k =
k∑
s=0
(k
s
)
psy2(k−s)
(72) Qa,iQb,j =
k∑
s=0
(k
s
)
za+bpi+j+sy(n+m)−(a+b)−2(i+j+s)
and the monomial on the right is just Qa+b,i+j+s. The other cases are similar. □
The operation µ2 determines a product, q2 ·q1 = ( −1)|q1|µ2(q2,q 1). The sign is
present to connect the conventions for an A∞-category at those of a dg-category; in
the case all morphisms have degree zero the sign is trivial. The followin g proposition
states how our Lagrangian intersections give rise to a distinguished basis of the homo-
geneous coordinate ring A. From the preceding propositions, we can deduce Theorem
1.1.
Proposition 4.6. The map ψd,n :HF 0(L(d),L (d +n)) →An deﬁned by
(73) ψd,n :qa,i ↦→Qa,i
is an isomorphism. We have
(74) ψd,n+m(q1 ·q2) = ψd,n(q1) ·ψd+n,m(q2)
Proof. That ψd,n is an isomorphism is because it maps a basis to a basis. The other
statement is the combination of Propositions 4.4 and 4.5. □
Thus the proof of Theorem 1.1 will be complete once we prove Propos ition 4.4,
which in turn depends on Propositions 4.8, 4.10, 4.12, 4.13, and 4.24. T he rest of this
section is devoted to the proofs of these propositions.
MIRROR OF THE PROJECTIVE PLANE 37
4.2. Extending the ﬁber. One problem with our Lagrangian boundary conditions
L(d) is that they intersect the horizontal boundary ∂hX(B). This raises the possibility
that as we degenerate the ﬁbration, part of a pseudo-holomorph ic section can escape
through ∂hX(B).
We now describe a technical trick that, by attaching bands to the ﬁ ber, allows us
to close up the Lagrangians for the purpose of a particular comput ation, and thereby
use only the results in the literature on sections with Lagrangian bou ndary conditions
disjoint from the boundaries of the ﬁbers. Proposition 4.7 states t hat this attachment
does not change the spaces of holomorphic curves that we wish to c ount, because they
do not enter the bands. On the other hand, when we degenerate t he ﬁbration, we
ﬁnd that some of these curves degenerate into curves that do en ter the bands.
The starting point for this construction is, given inputs a1 and a2, to consider the
portion of the ﬁbration ˜X(B)|T →T lying over the triangle T in the base. We recall
the assumption from section 3.2 that the symplectic connection is ac tually ﬂat near the
horizontal boundary. After passing to the universal cover of th e base, the symplectic
monodromies around the boundaries of X(I) can be trivialized, and the ﬁbration is
actually symplectically trivial near the horizontal boundary. We also assume that
the boundary intersections of our Lagrangians have been positive ly perturbed as in
Section 3.3.4, so that they do not intersect at the boundary. Afte r trivializing the
ﬁbration near the horizontal boundary, we ﬁnd that in each ﬁber Fz of ˜X(B)|T →T ,
there are six points on ∂Fz (three on either component), arising as the symplectic
parallel transport of the boundary points of L(0), L(n), and L(n +m). These are
the points where the Lagrangians L(0),L (n),L (n +m) are allowed to intersect ∂Fz
(though L(d) ∩∂Fz is only nonempty if z ∈ ℓ(d) is on the appropriate boundary
component of the triangle T ). The two sets of three points on each component of
∂Fz are matched according to which Lagrangian they come from, and we extend the
ﬁber Fz to ˆFz by attaching three bands running between the two components of Fz
according to this matching. We call the resulting ﬁbration ˆXT → T . We have an
embedding ι : ˜X(B)|T → ˆXT .
Over the component of ∂T where the Lagrangian boundary condition L(0) lies,
we extend L(0) to ˆL(0), closing it up ﬁberwise to a circle by letting it run through
the corresponding band in ˆFz. Similarly we close up L(n) and L(n +m) to their
hat-versions, each passing through a diﬀerent band.
Figure 9 shows the cylinder with a band attached. The actual exten ded ﬁber has
three such bands.
It is immediate from the construction that ˆXT \image(ι) is symplectically a product.
Let us use a complex structure which is also a product in this region. T ransversality
can be achieved using such structures because all intersection po ints lie in image( ι),
and hence any pseudo-holomorphic section must also pass through image(ι), where
we are free to perturb J as usual. We have the following proposition:
Proposition 4.7. Any pseudo-holomorphic section s : T → ˆXT with boundary con-
ditions ˆL(d), d = 0,n,n +m lies within image(ι).
Proof. Let p : ˆXT \ image(ι) → ˆF denote the projection to the ﬁber, whose image
consist of the bands. Let us consider one band containing the Lagr angianL. Introduce
38 JAMES PASCALEFF
Figure 9. Attaching a band to close up one of the Lagrangians in the ﬁber.
coordinates (s,t ) ∈ [0,a ] × [−1, 1] on the band such that the part of the Lagrangian
within the band is L = [0,a ] × {0}.
Let V ⊂T be the preimage of the open band (0 ,a ) × [−1, 1] under p ◦s. The set
V is relatively open. Let V ◦ = V \∂T . As the map p ◦s : V ◦ → [0,a ] × [−1, 1] is
actually a holomorphic map between Riemann surfaces, the open map ping theorem
implies that the image W = (p ◦s)(V ◦) is an open subset of (0 ,a ) × (−1, 1). Also,
the boundary of W is contained in the union of the Lagrangian [0 ,a ] × {0} (where
the boundary of the domain is sent) and the ends of the band {0,a } × (−1, 1) (where
image of V connects to the rest of the holomorphic curve). The only such W is the
empty set. □
4.3. Degenerating the ﬁbration. By propositions 4.2 and 4.7, in order to com-
pute the Floer product between two morphisms q1 ∈ HF 0(L(0),L (n)) and q2 ∈
HF 0(L(n),L (n +m)), it is just as good to count sections of the ﬁbration ˆXT → T
with Lagrangian boundary conditions ˆL(0), ˆL(n), ˆL(n +m).
In order to obtain these counts, we will consider a degeneration of the Lefschetz
ﬁbration. We consider a one-parameter family of Lefschetz ﬁbrat ions ˆX r →T r, which
for r = 1 is simply the one we started with. As r goes to zero, the ﬁbration deforms
so that all of the k critical values contained within T move toward the side of T
corresponding to ℓ(n). In the limit, a disc bubble appears around each critical value,
and atr = 0, the base T has broken into a (k+3)-gon, with k “new” vertices along the
side corresponding to ℓ(n), each of which joins to a disk with a single critical value. We
can equip each ﬁbration with Lagrangian boundary conditions varyin g continuously
with r, and degenerating to a collection of Lagrangian boundary condition s for each
of the component ﬁbrations at r = 0.
MIRROR OF THE PROJECTIVE PLANE 39
Figure 10. Degenerating the ﬁbration.
The base of the Lefschetz ﬁbration undergoes the degeneration shown in ﬁgure 10.
This ﬁgure shows speciﬁcally the case for the product of x ∈ CF ∗(L(0),L (1)) and
z ∈CF ∗(L(1),L (2)). The marked point on the upper portion is the Lefschetz critic al
value, while the marked points on the lower portion are the Lefschet z critical value
and a node.
When performing this construction carefully, it is better to describ e this family as
a smoothing of the degenerate r = 0 end. Let T 0 be a disk with ( k + 3) boundary
punctures. We emphasize that the conformal structure of T 0 is ﬁxed. Let ˆX 0 →T 0
be a symplectically trivial Lefschetz ﬁbration. Let D1,...,D k denote the k disks
with one boundary puncture that are our “bubbles”. For each i letEi →Di denote a
Lefschetz ﬁbration with a single critical value, and which is trivial nea r the puncture.
Let the symplectic monodromy around ∂Di be denoted τi.
We will equip each of the components of this ﬁbration with a Lagrangia n boundary
condition as follows.
• The base T 0 has one boundary component corresponding to ℓ(0), one bound-
ary component corresponding to ℓ(n +m), and (k + 1) boundary components
corresponding to ℓ(n). Since the ﬁbration ˆX 0 → T 0 is trivial, it suﬃces to
describe each boundary condition in the ﬁber. Over the point where ℓ(0) and
ℓ(n +m) come together, we identify the ﬁber with that of ˆX 1 →T 1, and take
ˆL(0)0 and ˆL(n +m)0 to be the corresponding Lagrangians.
• Over thek+1 boundary components of T 0 corresponding to ℓ(n), we construct
a sequence ˆL(n)0
i of Lagrangians. At the puncture where ℓ(0) and ℓ(n) come
together, we take ˆL(n)0
0 to have the same position relative to ˆL(0)0 (already
constructed) that ˆL(n) has relative to ˆL(0) in the original ﬁbration. As we
pass each of the new punctures where the disks are attached, th e monodromies
τi must be applied. So we let
(75) ˆL(n)0
i =τi( ˆL(n)0
i−1)
40 JAMES PASCALEFF
This can be done so that, over the puncture where ℓ(n) and ℓ(n +m) come
together, ˆL(n)0
k and ˆL(n +m)0 intersect as the original ˆL(n) and ˆL(n +m)
do.
• Over the k disks Di, we take a Lagrangian boundary condition which inter-
polates between ˆL(n)0
i−1 and ˆL(n)0
i . This is possible because each Di contains
a single Lefschetz critical value.
Note that at this stage we only care about the twists τi up to Hamiltonian isotopy,
but we will make a particular choice in §4.4, as required by the technical considerations
there. This gives us τi such that ˆL(n)0
i−1 and ˆL(n)0
i have one intersection point over
i-th new puncture of T 0.
Since the boundary conditions agree over the corresponding punc tures, we can glue
the components over T 0 and D1,...,D k with large gluing length in order to obtain
ˆX ǫ →T ǫ for small ǫ> 0, which has three boundary components and k critical values
all near the ℓ(n) boundary. There is a family of Lefschetz ﬁbrations interpolating
between ˆX ǫ →T ǫ back to our original ˆX 1 →T 1, along which the critical values move
back to their original points.
We equipT 0 andD1,...,D k with complex structures, and equip T ǫ with a family of
complex structures jǫ converging to those in the limit. All total spaces are equipped
with relatively compatible almost complex structures.
Now we appeal to the gluing theorem [39, Proposition 2.2] telling us ho w the curve
counts behave under the degeneration.
Proposition 4.8. The count of pseudo-holomorphic sections of ˆX 1 → T 1, with La-
grangian boundary conditions ˆL(d), d = 0,n,n +m is obtained from the counts of
sections of ˆX 0 →T 0 and Ei →Di by gluing together sections whose values over the
punctures match.
Proof. Considering pseudo-holomorphic sections of the ﬁbrations ˆX ǫ → T ǫ, as long
as the gluing length is large, the sections for r = ǫ will be obtained from sections
overT 0 andD1,...,D k by gluing sections with matching values at the punctures [39,
Proposition 2.2]. During the deformation from r =ǫ tor = 1, no Floer strip breaking
can occur because our Lagrangians ˆL(d), d = 0,n,n +m do not bound any strips,
even topologically, so the count remains the same at r = 1. □
