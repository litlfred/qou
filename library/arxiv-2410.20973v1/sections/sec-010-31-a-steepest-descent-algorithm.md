---
doc_id: arxiv-2410.20973v1
doc_title: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS"
section_id: sec-010-31-a-steepest-descent-algorithm
section_title: "A steepest descent algorithm"
section_number: 3.1
pages: 17-19
source_pdf: 2410.20973v1.pdf
source_sha256: 852b7bbc81a62883
doc_brief: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS — We prove conjectures of Garoufalidis-Gu-Mari˜ no [ 9] that perturbative series associated with the hyperbolic knots 4 1 and 5 2 are resurgent and"
---
ical value V0∈ C and ϑ∈ arg(C\S(V0))∩ ( π
2 , 3π
2 ). This determines the steepest descent
contourCp0,ϑ and constants ǫ, M > 0 so that all points p /∈ Wǫ,M satisfy [ γp,θ] = 0 (see
Corollary 2.12). Let W = Wǫ,M and consider the set
Z := {p∈ W| Re(e−iϑ(V0− V (p)))∈ cos(2πϑ)Z} . (58)
18 VERONICA F ANTINI AND CAMPBELL WHEELER
We can identify Z with
[
e−iϑ(V− V0)
] −1
(iR/e−iϑZ)∩ W , thusZ has a natural orientation
induced by R. We deﬁne
Z+ :=
[
e−iϑ(V0− V )
] −1
(iR≥0/e−iϑZ)∩ W⊂Z ,
P := {p∈ W∩Z +| Re(z(p)e−iϑ)∈ cos(2πϑ)Z} .
(59)
Notice that P is a ﬁnite set. To each point p∈P\{ p0} we can associate the cycle γp,θ,
which represents a class in H1(Σ , D∞,θ) as in Corollary
2.11. The points p∈P partition the
setZ+ into a set of edges and we deﬁne E to be the set of edges whose end points lie in P,
i.e.
E :=
{
e∈ π0(Z+\P ) : ∂e⊆P
}
. (60)
We denote the boundary of e by (pe, re), where the order respects the orientation of Z+. To
each e∈E we associate a cycle γe,θ, which represents a class in H1(Σ , D∞,θ) as shown in
Corollary 2.11. In order to describe the algorithm we need the following lemma:
Lemma 3.1. Let p = ( z, m)∈ Σ and eiϑ∈ C\S (V0). The sequence of tangent directions
to Γ (z,m+k),ϑ at the point ( z, m + k) is strictly monotone for k∈ sign(Im(z))Z≥0.
Proof. From Equation ( 45) in the proof of Lemma 2.2 and Equation ( 31), the tangent to
Γ (z,m+k),ϑ at the point ( z, m + k) is eiϑ(iV ′(z, m) + ik)−1. □
To the data ( p0, V0, ϑ) we can deﬁne a ﬁnite combination of state integrals. To begin the
algorithm, in place of step (I), we consider the critical point p0 and the lift V0∈ C such that
V0 = V (p0)∈ C/Z, and the thimble Cp0,ϑ as in Corollary 2.3. Then we go on from step (II).
Here is the algorithm:
(I) Let p∈P with a lift of V (p) to C and its associated cycle γp,ϑ (see Deﬁnition 2.9).
(II) The cycle γp,θ can be decomposed as union of γe,θ for every e⊂ γp,θ and γr,θ where
r∈P∩ γp,θ is the last point with respect to the order inherited from γp,θ.
(III) To each γe,θ we associate the integral
∫
γe,θ
e
( A
2 z(z + 1 + 1
τ )τ + mzτ + nτ
)
Φ(( z− ℓ)τ ; τ )B dz , (61)
where m and n are dictated by the original lift of V (p) and ℓ = ⌈Re(z(x)) +
tan(ϑ)Im(z(x))⌉ for some x∈ e, the ceiling of the projection onto the reals parallel
to e−iϑ. If Im( z(pe))Im(z(re)) < 0 then γe,θ is homotopic to a state integral contour,
hence the integral in Equation ( 61) is equal to qnIm,ℓ. Otherwise, it vanishes.
(IV) To each point ( z, m)∈ ∂
(
E∩ γp,θ
)
, we take the collection of points ( z, m± k)∈P
where k = 1, . . . , N and N≤|P| , and the sign ± equals the sign of Im( z). To these
collections we assign the lifts V ((z, m± k)) = V (z, m)± k(z− ℓ) and take their
associated cycles −γ(z,m±k),θ weighted by constants ak∈ Z deﬁned as follows: from
Lemma 3.1 there exists a constant k0 such that
• for 0 < k < k 0, the tangent 6 at ( z, m± k) to the set −γ(z,m±k),θ is in −ieiϑH if
Im(z) > 0, and is in i(A− B)eiϑH if Im( z) < 0,
6If the tangent is equal to ±ieiϑ , then we consider the direction of higher derivatives.
SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS 19
• for k≥ k0, the tangent at ( z, m±k) to the set−γ(z,m±k),θ is in ieiϑH if Im(z) > 0,
and is in −i(A− B)eiϑH if Im( z) < 0,
and ak are the unique constants that satisfy the equation
[
Φ(( w− ℓ)τ ; τ )B− Φ(( w− ℓ− 1)τ ; τ )B]
e
( A
2 w(w + 1 + 1
τ )τ + mwτ
)
=
∑
0<k<k0
akΦ(( w− ℓ0)τ ; τ )Be
( A
2 w(w + 1 + 1
τ )τ + (m± k)wτ
)
+
∑
k≥k0
akΦ(( w− ℓ1)τ ; τ )Be
( A
2 w(w + 1 + 1
τ )τ + (m± k)wτ
)
,
(62)
for every w with Im( w) = Im( z), and where ℓ0 = ℓ + 1 and ℓ1 = ℓ if Im( z) > 0, and
ℓ0 = ℓ + (1− sign(A− B))/2 and ℓ1 = ℓ + (1 + sign(A− B))/2 if Im( z) < 0.
The algorithm terminates if at step (IV) there are no ( z, m± k)∈P .
Corollary 3.2. This algorithm terminates after ﬁnitely many steps producing a func tion
Ip0,V0,ϑ(τ ) given as a Z-linear combination of qnIm,ℓ.
Proof. We can partially order the points p in the set P∩ H according to the Re( z+(p)) and
m∈{ 0, . . . , A− 1}, in particular we use the lexicographic order on R×{ 0, . . . , A− 1}. The
new base points appearing at step (IV) of the algorithm always stric tly increase with respect
to this order. Hence after a ﬁnite number of steps all points will mov e outside P (a ﬁnite
set). A similar argument holds in the lower half-plane. Then from Coro llary 2.12, all of
these points p have trivial associated cycles [ γp,ϑ] = 0. □
Lemma 3.3. The functionIp0,V0,ϑ(τ ) is locally constant as ϑ varies in arg(C\S(V0))∩( π
2 , 3π
2 ).
Proof. For ϑ∈ arg(C\S(V0))∩ ( π
2 , 3π
2 ) contained in a connected component, the sets Z+ are
all homotopic. We can restrict to a compact subinterval and on this compact set of ϑ, we
can choose ǫ, M > 0 uniformly. Then for small enough variations of ϑ, we can identify p∈P
while ϑ varies. Since p can not cross the reals without going through a branch point, which
Z+ does not intersect, the cycles γp,ϑ are all homotopic. This implies that the algorithm
will generically produce the same Ip0,V0,ϑ(τ ) for small variations of ϑ. Besides the generic
behaviour, there are critical directions across which the set P can gain or loose points. Points
inP either appear and disappear in pairs in the interior of W —therefore they will both have
the same sign of Im( z±)—or a single point falls outside the boundary of W . If two points
appear or disappear inside W , given that both points are in the same half plane, the cycle
associated to them is trivial and this does not aﬀect the function Ip0,V0,ϑ(τ ). In the other
case, if a point p∈P falls outside the boundary of W then [ γp,ϑ] = 0 by Corollary 2.12 and
therefore, as [ γp,ϑ] is constant for all ϑ in our compact set, it does not aﬀect Ip0,V0,ϑ(τ ). □
If I denotes a connected component of C\S(V0))∩ ( π
2 , 3π
2 ), then we denote Ip0,V0,I(τ ) the
functionIp0,V0,ϑ(τ ) for any ϑ∈ arg I.
