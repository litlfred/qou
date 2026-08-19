---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMA TION JESSICA S. PURCELL"
section_id: sec-015-43-boundary-bound
section_title: "Boundary bound"
section_number: 4.3
pages: 21-28
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION JESSICA S. PURCELL — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp sh ape."
---
a parameterization of the cone deformation such that the sum of the terms
bj is of order n. We ﬁrst need two lemmas. Lemma 4.3 gives us an initial
bound on each bj. Lemma 4.4 will allow us to improve this bound. It is in
the proof of Lemma 4.3, giving the initial bounds on the bj, that we use the
positivity result of Lemma 4.1.
Finally, in Theorem 4.6 at the end of this subsection, we put t hese lemmas
together to record the main result of the section: the bound o n the sum∑ bj.
Lemma 4.3. Suppose we have a cone deformation given as a linear combi-
nation of deformations, as above, where cone angles go from 0 to 2π along
the singular locus. Suppose also that S = ( s1, . . . , sn) is chosen such that
22 JESSICA S. PURCELL
for each time t, bj(S) ≥ 0 for all j. Suppose the tube radius R is bounded
below by R1 ≥ 0.56 for each t. Then
bj(S) ≤ s2
j C(R1),
where C(R1) is a function of R1 alone which approaches 0 as R1 approaches
inﬁnity.
Proof. First, since we’re considering a ﬁxed Vj, we will drop the subscript j
in our notation throughout the proof (i.e. Vj = V, (η0)j = η0, s j = s, etc).
Modify a calculation (p. 382 and 383 of [14]) to include s, and equation
(17) of that paper can be written:
bj(S)
Area(∂V ) ≤ s2
8m4 ,
where m = α sinh2 R is the length of a meridian on ∂U .
We will bound the term Area( ∂V ) s2/(8m4).
Let A = Area( ∂V ). Let h denote the height of ∂V , i.e. the length of an
arc perpendicular to the meridian. So h = ℓ cosh R, where ℓ is the length of
the singular locus of the solid torus V , and A = mh.
Consider
Φ = 8m4
A = 8m3
h = 8α3 sinh3 R
ℓ cosh R .
We will bound Φ below, therefore bounding its reciprocal abo ve.
Let
Υ( R) = 3.3957 tanh R
2 cosh 2R .
It was shown in [14] (see Theorem 4.4, Corollary 5.1, and the c omments on
the multicusp case on p. 411), that αℓ ≥ Υ( R).
Then
Φ = 8α3 sinh3 R
ℓ cosh R = 4α3
ℓ
1
Υ( R) g(R)
where
g(R) = 2Υ( R) sinh3 R
cosh R = 2Υ( R) tanh R sinh2 R = 3.3957 tanh4 R
1 + tanh2 R .
So
Φ ≥ 4α3
ℓ
1
αℓ g(R) = 4
( α
ℓ
) 2
g(R).
Note that g(R) is increasing with R. Hence since R ≥ R1, g(R) is bounded
below by g(R1). Thus we focus on the term α/ℓ in Φ.
Deﬁne u = α/ℓ. In our hyperbolic cone deformation, the initial cone angle
α is zero. As α approaches 0, u approaches L2
0, where L0 is the normalized
length of the curve which becomes the meridian (i.e. bounds a singular
solid disc) under the cone deformation (see equation (37) of [14]). We will
estimate u = (u0 + ∆ u) = ( L2
0 + ∆ u).
CUSP SHAPES UNDER CONE DEFORMATION 23
Reworking the calculations of [14] to include the speed s, and taking
derivatives with respect to cone angle α rather than time, we may rewrite
Proposition 5.6 of that paper as:
1
α
du
dα ≥ − 2(1 + tanh2 R)
3.3957 tanh3 R = − 2 tanh R
g(R) ,
provided that R ≥ R1 ≥ 0.531.
It is at this step, to use Proposition 5.6 of [14], that we have required S
to be chosen so that bj(S) > 0.
Thus
∆ u ≥
∫ α=2π
α=0
−2α tanh R
g(R) dα ≥ − tanh R1
g(R1)
∫ 2π
0
2αdα = −(2π)2 tanh R1
g(R1) .
So
u2 ≥ (L2
0 − (2π)2 tanh(R1)/g(R1))2,
provided the term L2
0−(2π)2 tanh(R1)/g(R1) is non–negative. We can ensure
this quantity is non–negative by ensuring L2
0 is large. This can be done
following [14]. The following result is essentially equati on (47) of that paper.
(24) L2
0 ≥ 2(2π)2
3.3957(1 − tanh R) exp
( ∫ tanh R
1
F (w)dw
)
= I(R),
provided the tube radius is at least R throughout the deformation. Here
F (w) = −(1 + 4w + 6w2 + w4)/((w + 1)(1 + w2)2) is an integrable function.
The right hand side I(R) of (24) is increasing with R, so it can be bounded
below by a constant in terms of R1.
L2
0 ≥ I(R1)
Now if R1 ≥ 0.56, then I(R1) − 2(2π)2 tanh(R1)/g(R1) ≥ 0.
Putting this together,
Φ ≥ 4
(
I(R1) − (2π)2 tanh R1
g(R1)
) 2
g(R1).
The right hand side of the above equation is a constant, ~C0(R1).
Thus we have
bj(S) ≤ A
8m4 s2 = 1
Φ s2 ≤ s2
~C0(R1)
= s2 C(R1).
□
The result of Lemma 4.3 gives us a bound on the sum of the bj in terms
of ¯s. If we could choose ¯s = (1, . . . ,1) (all cone angles increasing at the same
rate), then Lemma 4.3 would give a bound on ∑ bj of order n. However,
our choice of ¯s comes from Lemma 4.1. By the proof of that lemma, we may
assume only that ¯s is in the simplex T = {¯s |∑ sj = n, sj ≥ 0}. A priori, ¯s
could be close to a vertex of T , say ( n, 0, . . . ,0), in which case Lemma 4.3
gives only a bound of order n2 on∑ bj.
24 JESSICA S. PURCELL
T{2,3}
T{1,2}
T2
(1, 1, 1) = T{1,2,3}
T{1,3}
(0, 3, 0)(3, 0, 0)
(0, 0, 3)
T1
T3
Figure 2. Faces TI illustrated when n = 3.
For our applications, we need the bound of order n. We will obtain this
better estimate by again revisiting the choice of the point ¯s = (s1, s2, . . . , sn).
This is done in Lemma 4.4.
Lemma 4.4. There exists a point S = ( s1, . . . , sn) in T such that each
bj(S) ≥ 0, j = 1 , . . . , n, and for any index j with sj ⁄= min {s1, . . . , sn}, we
have bj(S) = 0 .
Proof. First we set up some notation.
Notation. Let B = {¯s | bj(¯s) ≥ 0, j = 1, . . . , n} (so the interior of B is the
set Bn of Lemma 4.2). Again we may normalize such that the points ¯ s lie
in the simplex T = {(s1, . . . , sn)|∑ si = n, si ≥ 0}.
We deﬁne some sets in B. For each j = 1 , 2, . . . , n, let ej be the set of
all points in B such that bj > 0 and for i ⁄= j, bi = 0. Note for j = n, en
corresponds to the set En in Lemma 4.2. (So in particular, en consists of an
odd number of points.)
Let b{i,j} be the set b{i,j} = B∩(∩k⁄=i,j{bk = 0}). Note b{i,j} has dimension
1, with components with boundary in ei and ej.
In general, let I be a k-element subset I = {i1, i2, . . . , ik} ⊆ { 1, . . . , n}.
Let bI = B ∩ (∩j /∈I {bj = 0}). Notice bI is bounded by components bIj where
j ∈ I, and Ij is the ( k − 1)-element set obtained by removing j from I.
Now we deﬁne some sets in the simplex T = {¯s|∑ si = n}. Let Ti be
the region in which si ≤ sj for all indices j. Ti has dimension n − 1. Let
T{i,j} = Ti ∩ Tj. Thus each Ti is bounded by faces T{i,j} where j ranges
over all elements of {1, . . . , n} − {i}, as well as faces on ∂T . Generally, let
I be a k-element subset of {1, . . . , n}. Let TI = ∩j∈ITj. Note the boundary
faces of TI are the faces given by TI∪{k}, where k ranges over all elements of
{1, . . . , n} − I, as well as faces in ∂T . See Figure 2 for an illustration when
n = 3.
We will make transversality assumptions that allow us to ign ore the
boundary faces of TI on ∂T . In particular, assume that B lies in the interior
of T , so the sets bI do not meet ∂T . If this is not the case, we may apply
the argument below to level sets bI = ǫ, then take the limit as ǫ → 0. Since
CUSP SHAPES UNDER CONE DEFORMATION 25
B is closed, we will obtain the desired result. Similarly, we w ill assume that
the bI ’s and the TI ’s all intersect transversely.
We will use the transversality assumption that B does not meet ∂T in
the arguments below. In particular, we will be considering t he intersection
of subsets of B with boundary faces of TI . Since B does not meet ∂T , this
allows us to ignore the faces of TI which lie on ∂T in our argument.
Now, note the lemma will be immediately true if we can ﬁnd some index
j such that ej is in the region Tj: for on ej, bi = 0 for all i ⁄= j, and in Tj,
sj is minimum. So assume this never happens.
Generally, if for some k-element set I ⊆ { 1, . . . , n}, bI ∩ TI is nonempty,
we obtain a point which satisﬁes the lemma. So we will assume t his also
never happens. We will show that in this case, the point (1 , 1, . . . ,1) is in
B, thus concluding the proof. To prove this, we need another su blemma.
Lemma 4.5. Let #(·) denote the number of elements of a ﬁnite set. As-
suming that each bI ∩ TI is empty,
∑
I
#(bI∪{n} ∩ ∂TI ) ≡
∑
J
#(bJ∪{n} ∩ ∂TJ ) ≡ 1 mod 2 ,
where the ﬁrst sum is over all (k + 1)-element subsets I of {1, . . . , n − 1},
and the second sum is over all k-element subsets J of {1, . . . , n− 1}.
Check that the statement of the lemma makes sense: Note if J is a k-
element set, then bJ∪{n} is k-dimensional. TJ is ( n − k) dimensional, so its
boundary faces are ( n − k − 1)-dimensional. Thus the intersections in the
statement of the lemma are 0-dimensional manifolds, consis ting of a ﬁnite
number of points.
Also notice that when k = (n − 2) in the above lemma, there exists only
one ( k + 1)-element subset I, namely I = {1, . . . , n − 1}. So bI∪{n} is the
whole set B. On the other hand, the boundary ∂TI in this case must be the
point in the intersection of all the Ti, or the point (1 , . . . ,1). Thus the ﬁrst
sum counts the number of times the point (1 , . . . ,1) appears in B. Hence
showing this number is odd will ﬁnish the proof of Lemma 4.4.
Proof. We prove Lemma 4.5 by induction on k.
We start by showing what essentially is the case k = 0. That is, we show
n−1∑
i=1
#(b{i,n} ∩ ∂Ti) ≡
n−1∑
i=1
#(en ∩ Ti) mod 2 .
Since we are assuming en ∩ Tn = ∅, the second sum in the above equation
is just the number of points of en (since en is disjoint from each Ti ∩ Tj by
transversality). That number of points is odd by Lemma 4.2, s o this will
give us the basis step of our induction.
26 JESSICA S. PURCELL
Consider b{i,n} ∩ Ti. This is a 1–manifold, consisting of closed curves and
arcs. Each arc has two endpoints. So
n−1∑
i=1
#∂(b{i,n} ∩ Ti) ≡ 0 mod 2
On the other hand,
n−1∑
i=1
#∂(b{i,n} ∩ Ti) =
n−1∑
i=1
#(∂b{i,n} ∩ Ti) +
n−1∑
i=1
#(b{i,n} ∩ ∂Ti).
So∑
i⁄=n #(b{i,n} ∩ ∂Ti) has the same parity as ∑
i⁄=n #(∂b{i,n} ∩ Ti).
Consider ∂b{i,n} ∩ Ti. Note ∂b{i,n} consists of points in ei and en. By
assumption, ei is never in Ti. Thus
n−1∑
i=1
#(∂b{i,n} ∩ Ti) =
n−1∑
i=1
#(en ∩ Ti) = #( en).
So∑
i⁄=n #(b{i,n} ∩ ∂Ti) is odd.
Our proof for general k follows essentially the same lines as the proof
above.
Suppose 1 ≤ k ≤ n − 2. We need to show
∑
I
#(bI∪{n} ∩ ∂TI ) ≡
∑
J
#(bJ∪{n} ∩ ∂TJ ) mod 2 ,
where the ﬁrst sum is over ( k + 1)-element subsets of {1, . . . , n− 1} and the
second is over k-element subsets.
Fix some ( k + 1)-element subset I, and again consider bI∪{n} ∩ TI . This is
a 1–manifold. Its components are closed curves and arcs. Aga in the number
of endpoints of these arcs is even. So when we sum over all such I,
∑
I
#∂(bI∪{n} ∩ TI ) ≡ 0 mod 2 .
On the other hand,
∑
I
#∂(bI∪{n} ∩ TI ) =
∑
I
#(∂bI∪{n} ∩ TI ) +
∑
I
#(bI∪{n} ∩ ∂TI ).
Thus we consider ∑
I #(∂bI∪{n} ∩ TI ). We want it to have the same par-
ity as ∑
J #(bJ∪{n} ∩ ∂TJ ), where J ranges over all k-element subsets of
{1, . . . , n− 1}. We show now that the two sums are actually equal, which
concludes the proof.
Consider ∂bI∪{n}. This consists of bI , as well as things of the form bIj∪{n}
where Ij is the k-element set obtained from I by removing the element
j ∈ I. Since by assumption, bI ∩ TI is empty, ∂bI∪{n} ∩ TI is the union of
sets bIj ∪{n} ∩ TI , where j ranges over all elements of I.
Then
(25)
∑
I
#(∂bI∪{n} ∩ TI ) =
∑
I
∑
j∈I
#(bIj∪{n} ∩ TI ).
CUSP SHAPES UNDER CONE DEFORMATION 27
We will change our method of counting in (25) above. Replace t he terms
Ij with k-element subsets J of {1, . . . , n− 1}. We will run through all such
J. Then I will run through the ( k + 1)-element subsets given by J ∪ {i},
where i is some element of {1, . . . , n − 1} − J. So the right hand side of
equation (25) is equal to
∑
J
∑
i∈{1,...,n−1}−J
#(bJ∪{n} ∩ TJ∪{i}).
On the other hand, we know the boundary ∂TJ is equal to the union of
all faces TJ∪{j}, where j ranges over all elements of {1, . . . , n} −J. The only
such face we are missing in our sum above is TJ∪{n}. But by assumption,
the intersection of bJ∪{n} with TJ∪{n} is trivial. Thus
∑
J
∑
i∈{1,...,n−1}−J
#(bJ∪{n} ∩ TJ∪{i}) =
∑
J
#(bJ∪{n} ∩ ∂TJ ).
□
This concludes the proof of Lemma 4.4. □
Lemmas 4.3 and 4.4 together give the desired bound on ∑ bj:
Theorem 4.6. Let X be a hyperbolic manifold with n+k cusps connected to
a manifold M with k cusps by a cone deformation. (So in particular, there
are n components of the singular locus, and cone angles at each com ponent
go from 0 to 2π.) Suppose during the deformation, the tube radius about the
singular locus remains larger than R1 ≥ 0.56. Then the deformation can be
parameterized so that at each time: min sj = 1 and the sum of the boundary
terms satisﬁes
n∑
j=1
bj ≤ n C(R1).
Moreover, we can assume the deformation has reached the hype rbolic struc-
ture on M by time t = (2π)2.
Proof. By Lemma 4.4, we may ﬁnd a value S in T such that each bj(S) ≥ 0
and such that if for any index j, sj ⁄= min {s1, . . . , sn}, then bj(S) = 0.
Denote the minimum value of the sj by s: s = min {s1, . . . , sn}. Then
Lemma 4.3 implies that
(26)
n∑
j=1
bj =
∑
{j|bj⁄=0}
bj ≤
∑
{j|bj⁄=0}
s2 C(R1) ≤ ns2 C(R1).
First, we need to check that s is not equal to zero. Suppose not. That
is, suppose s = 0. Then by (26), ∑ n
j=0 bj = 0. Recall that by equation (16)
and the remark right after it, the sum of all bj’s equal zero only if the entire
deformation is trivial. But this is possible only if each sj = 0. Since the
point (0 , 0, . . . ,0) is not in the simplex T , this is impossible.
28 JESSICA S. PURCELL
Now, recall the terms sj aﬀect the rate of change of the deformation.
Thus we may rescale them without changing the tube radius. Fo r the point
S in T , divide each sj by s. Replace S by this rescaled point, and denote
the rescaled point by the same notation: S = ( s1, . . . , sn). So each sj ≥ 1.
Also, s = min{sj} = 1.
Thus equation (26) gives:
n∑
j=1
bj ≤ n C(R1).
Finally, to notice that the deformation is complete by time t = (2 π)2 as
claimed, recall that if sj = 1 throughout the deformation, then the cone
angle is changing at a rate at which αj will reach 2 π at time t = (2π)2. (See
the discussion at the beginning of §4.1.) Since sj ≥ 1 always, the rate of
change may only be faster. Thus each cone angle reaches 2 π by the time
t = (2π)2. □
When we combine Theorem 4.6 with the results of Theorem 3.3 an d The-
orem 3.6, we have completed the proofs of Theorems 1.2 and 1.3 .
