---
doc_id: arxiv-2410.20973v1
doc_title: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS"
section_id: sec-012-4-examples
section_title: "Examples"
section_number: 4
pages: 21-36
source_pdf: 2410.20973v1.pdf
source_sha256: 852b7bbc81a62883
doc_brief: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS — We prove conjectures of Garoufalidis-Gu-Mari˜ no [ 9] that perturbative series associated with the hyperbolic knots 4 1 and 5 2 are resurgent and"
---
We now go though two explicit examples. One is associated to the ﬁgur e eight knot 4 1,
where ( A, B) = (1 , 2) and the other is for ( A, B) = (4 , 1). The ﬁrst was studied in [ 9] and
full conjectural answers were given for the resurgent structu res. We will prove the exact
formulas given in [ 9] are correct by applying our method to compute the Borel–Laplace
resummation. A similar analysis for the example ( A, B) = (4 , 1) was carried out in [ 24].
Here again conjectural formulas were given and we will also prove th em.
4.1. The 41 knot. This example corresponds to A = 1 and B = 2. See for example [ 12,
Sec. 7]. We will compute the Borel–Laplace resummation of Φ Ξ with the algorithm described
in Section 3.1. We will see that this exactly matches the numerical predictions of [ 9]. The
critical points for the volume V are at p1 = (−5/6, 0) and p2 = (−1/6, 0) and their critical
values are respectively at V1 =−0.0514175 . . . i and V2 = 0 .0514175 . . . i. Thus the ﬁrst
Stokes line is at eiϑR>0 with ϑ = 3 .1416 and it separates the regions I and II. While the
second one is at ϑ = 1.6733 and separates the regions II and III (see Figure 10).
I
II
III
X
ϑ = π
ϑ = 1.6733ϑ = 1.4683
ϑ = 0
Figure 10. This ﬁgure illustrates the Stokes rays in τ -plane with ϑ =
arg(−1/τ ) forming a peacock pattern. Note that this is stretched in the dire c-
tion of the x-axis and the Stokes rays are all even closer to the vertical line.
To perform the computation, we plot the set Cp0,ϑ and keep track of the branching of the
function V . In the plots, this will be noted at the end point with ( m, n) keeping track of the
sheet of Σ by m∈ Z and analytic continuation of the function V with values n∈ Z so that
for Im( z) > 0 we have V (z) = B Li2(e(z))
(2πi)2 + B
24 + A
2 z(z + 1) + mz + n while for Im( z) < 0 we
have V (z) =−B Li2(e(−z))
(2πi)2 + B
12− B
2 (z− 1
2)2 + A
2 z(z + 1) + mz + n. This allows us to read oﬀ
the state integrals given by the algorithm.
4.1.1. The critical point p2 = (−1/6, 0). The critical point p2 has no Stokes rays for ϑ∈
( π
2 , 3π
2 ). Therefore, computing the Borel–Laplace resummation for a ﬁxe d ϑ∈ ( π
2 , 3π
2 ) will be
enough to determine it for the whole region. We plot the set Cp2,ϑ in Figure 11. We can see
that this steepest descent contour is equivalent to the state inte gral contourJ0,0. Therefore,
the algorithm gives
Ip2,V2,Y = I0,0 , (65)
where for example Y = I , II, III. This is the original Andersen–Kashaev invariant for 4 1 [1,
Eq. (38)] and [ 10, Sec. 1.3]. Therefore, our results gives a reﬁned version of their v olume
22 VERONICA F ANTINI AND CAMPBELL WHEELER
(0, 0)
(−2, 0)
Figure 11. This ﬁgure depicts in orange the set C(−1/6,0),ϑ for ϑ =
arg(−1/τ ) = 3 .1416 and ( A, B) = (1 , 2).
conjecture. In particular, not only does the Andersen–Kashaev invariant have exponential
decay determined by the volume of the ﬁgure eight knot but it is in fac t the resummation
of its own all order asymptotics.
4.1.2. State integrals decomposition in I. Let ϑ∈ I. We plot the set Cp1,ϑ in Figure
12.
We can decompose the thimble in terms on state integrals contours. We have contributions
(0, 0)(2, 2)
(−3, −1)
Figure 12. This ﬁgure depicts in orange the set C(−5/6,0),ϑ for ϑ =
arg(−1/τ ) = 4 .0841, and ( A, B) = (1 , 2). The green lines are parallel to
the lines i/τ . The magenta curve represents the tail at the intersection of the
setC(−5/6,0),ϑ with the lines parallel to i/τ .
fromI0,0 from the intersection of the orange contour with the interval ( −1, 0), which has
(n, m, ℓ) = (0 , 0, 0) and−q2I2,−1 from the intersection of the orange contour with the interval
(−2,−1), which has ( n, m, ℓ) = (2 , 2,−1). We can see that the tail leads to no contribution
as it does not cross the reals and heads to ∞. The algorithm therefore gives
Ip1,V1,I = I0,0− q2I2,−1 = I0,0 +I1,0 , (66)
where the second equality follows from Equation ( 14).
SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS 23
4.1.3. The saddle connection between I and II. The saddle connection is depicted in Fig-
ure 13.
(0, 0)
(−2, 0)
Figure 13. This ﬁgure depicts in orange the set C(−5/6,0),ϑ for ϑ =
arg(−1/τ ) = 3 .1416 and ( A, B) = (1 , 2). The green lines are parallel to the
lines i/τ .
4.1.4. State integrals decomposition in II. Let ϑ∈ II then Cp1,ϑ is depicted in Figure 14.
We can decompose the thimble in terms on state integrals contours. We have contributions
(−2, 0)(−4, −2)
(1, 1)
Figure 14. This ﬁgure depicts in orange the set C(−5/6,0),ϑ for ϑ =
arg(−1/τ ) = 2 .1991, and ( A, B) = (1 , 2). The green lines are parallel to
the lines i/τ . The magenta curve represents the tail at the intersection of the
setC(−5/6,0),ϑ with the lines parallel to 1 /τ .
from−I0,0 from the intersection of the orange contour with the interval ( −1, 0), which has
(n, m, ℓ) = (0 , 0, 0) and I0,−1 from the intersection of the orange contour with the interval
(−2,−1), which has ( n, m, ℓ) = (0 , 0,−1). We can see that the tail leads to no contribution
as it does not cross the reals and heads to ∞. The algorithm therefore gives
Ip1,V1,II = −I0,0 +I0,−1 = −I0,0−I −1,0 , (67)
where the equality follows from Equation ( 14).
24 VERONICA F ANTINI AND CAMPBELL WHEELER
4.1.5. The saddle connection between II and III. The saddle connection is depicted in Fig-
ure
15.
(−2, 0)(−4, −2)
(2, 4)
Figure 15. This ﬁgure depicts in orange the set C(−5/6,0),ϑ for ϑ =
arg(−1/τ ) = 1 .6733, and ( A, B) = (1 , 2). The green lines are parallel to
the lines i/τ .
4.1.6. State integrals decomposition in III. Let ϑ∈ III then Cp1,ϑ is depicted in Figure 16.
This picture gives rise to many intersections between the thimble and the green lines
(−2, 0)
(2, 4)
Figure 16. This ﬁgure depicts in orange the set C(−5/6,0),ϑ for ϑ =
arg(−1/τ ) = 1 .6650 and ( A, B) = (1 , 2). The green lines are parallel to the
lines 1 /τ .
Z + τ −1R. Therefore, it could require iterations of the algorithm. This is indee d true and
will involve two additional integrals at the ﬁrst iteration and an additio nal integral at the
second iteration.
We can decompose the thimble in terms on state integrals contours. We have contributions
of−I0,0 from the intersection of the orange contour with the interval ( −1, 0), which has
(n, m, ℓ) = (0 , 0, 0), I0,−1 from the intersection of the orange contour with the interval
(−2,−1), which has ( n, m, ℓ) = (0 , 0,−1), and−q4I2,−2 from the intersection of the orange
contour with the interval (−3,−2), which has ( n, m, ℓ) = (4 , 2,−2).
At the ﬁrst step of the algorithm we obtain two additional cycles com ing from the magenta
curves as seen in Figure 17. We have a contribution of 4 q2I1,−1 from the intersection of the
SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS 25
(−2, 0)
(2, 4)
(1, 2)
(1, 1)
(−3, 0)
(0, 1)
Figure 17. This ﬁgure depicts in orange the set C(−5/6,0),ϑ for ϑ =
arg(−1/τ ) = 1 .6650, and ( A, B) = (1 , 2). The green lines are parallel to
the lines i/τ . The magenta contours represent half of the additional contours
that appear in the ﬁrst step of the algorithm where we ignore any ze ro contri-
butions. Then the violet contour represents half of the contour that appears
in the second step of the algorithm. The additional contours are all crossing
the real axis, hence they lead to a non-zero state integral.
two magenta contours in (−1, 0), which have ( n, m, ℓ) = (2 , 1,−1). There is a ﬁnal magenta
curve depicted, which has additional intersections with the line τ −1R.
At the second step of the algorithm there is an additional contribut ion coming from the
violet contour in Figure 17. This appears with the constant attached to the magenta contou r
it emanates from multiplied by its own constant. We have a contributio n of −4qI0,0 from
the intersection of the violet contour with the interval ( −1, 0), which has ( n, m, ℓ) = (1 , 0, 0).
The additional state integrals added are depicted in Figure 18.
All together the algorithm produces the function
Ip1,V1,III = −I0,0 +I0,−1 + 4q2I1,−1− 4qI0,0− q4I2,−2 = −I0,0−I −1,0− 9qI0,0 , (68)
where the second equality follows from Equation ( 14).
4.1.7. First few Stokes constants. We can now describe the Stokes matrices. We see from
Equation ( 65), Equation ( 66), Equation ( 67), and Equation ( 68) that
(Ip1,V1,II Ip2,V2,II
)
=
(Ip1,V1,I Ip2,V2,I
) (
1 0
−3 1
)
, (69)
and
(Ip1,V1,III Ip2,V2,III
)
=
(Ip1,V1,II Ip2,V2,II
) (
1 0
−9q 1
)
. (70)
These agree with the Stokes constants computed in [ 9]. Therefore, we see that
SI,II(q) =
(
1 0
−3 1
)
, SII,III(q) =
(
1 0
−9q 1
)
. (71)
26 VERONICA F ANTINI AND CAMPBELL WHEELER
Figure 18. This ﬁgure depicts the contours γe,ϑ that we add at the ﬁrst and
second iteration of the algorithm to Ip1,V1,III as showed in Figure 17.
4.1.8. Computing all Stokes constants. We want to compute the Stokes matrix Sπ−ǫ,0+ǫ for
small ǫ > 0. In order to do this, we will use formulae for state integrals found by [ 10]. This
was the method used in the numerical approach of [ 9]. We can express state integrals—
and therefore their Borel–Laplace resummations—as bilinear combin ations of q = e(τ ) and
~q = e(−1/τ )-series. Consider the collections of q-series
gm(q) =
∞∑
k=0
(−1)k qk(k+1)/2+mk
(q; q)2
k
,
Gm(q) =
∞∑
k=0
(−1)k qk(k+1)/2+mk
(q; q)2
k
(
m− 2E1(q) +
∑
ℓ=1
1 + qℓ
1− qℓ
)
,
(72)
where
E1(q) = −1
4 +
∞∑
k=1
qk
1− qk = − 1
4 +q +2q2 +2q3 +3q4 +2q5 +4q6 +2q7 +4q8 +3q9 +··· . (73)
For example, we have
g0(q) = 1 − q− 2q2− 2q3− 2q4 + q6 + 5q7 + 7q8 + 11q9 + 13q10 + 16q11 +··· ,
G0(q) = 1
2(1− 7q− 14q2− 8q3− 2q4 + 30q5 + 43q6 + 95q7 + 109q8 + 137q9 +··· ) . (74)
SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS 27
Then as shwon in [ 10, Eq. (14)], the state integral is given by the following formula
i~q−1/12q1/12
∫
Jℓ,τ
Φ( zτ, τ )2 e
( 1
2 z(zτ + τ + 1) + mzτ + nz
)
dz
= τ −1gm(q)G−n(~q)− g−n(~q)Gm(q) .
(75)
We can use this to write the Borel–Laplace resummation in matrix form(Ip1,V1,I Ip2,V2,I
)
=
( g0(~q) G0(~q)) (
−1 0
0 τ −1
)(
G0(q) + G1(q) G0(q)
g0(q) + g1(q) g0(q)
)
.
(76)
We can similarly, write(Ip1,V1,X Ip2,V2,X
)
=
( g0(~q) G0(~q)) (
1 0
0 τ −1
)(
−G0(q) G0(q) + G1(q)
−g0(q) g0(q) + g1(q)
)
.
(77)
Then we ﬁnd
7 that the Stokes matrix going from I to X is given by
S+(q)
=
(
G0(q) + G−1(q) G0(q)
g0(q) + g−1(q) g0(q)
) −1(
−1 0
0 1
)(
−G0(q) G0(q) + G1(q)
−g0(q) g0(q) + g1(q)
)
=
(
−1 + 8q + 9q2− 18q3− 46q4 3− 15q− 24q2 + 15q3 + 69q4
−9q− 3q2 + 39q3 + 69q4 −1 + 19q + 17q2− 53q3− 126q4
)
+···
=
(
1 0
−3− 9q− 75q2− 642q3− 5580q4 1
)
×
(
1− 8q− 9q2 + 18q3 + 46q4 0
0 1 + 8 q + 73q2 + 638q3 + 5571q4
)
×
(
1 9 q + 75q2 + 642q3 + 5580q4
0 1
)
+··· .
(78)
One can see exact agreement with the previous computations of th e ﬁrst two Stokes constants
−3 and−9. To compute the next constant −75 using the methods we have described would
presumably involve many iterations of the algorithm and would be best done via computer
implementation, which we have not attempted.
4.2. The case of (A, B) = (4 , 1). We will compute the Borel–Laplace resummation of Φ Ξ
with the algorithm described in Section
3.1. We will see that this exactly matches the
numerical predictions of [ 24, Example 39]. The critical points for the function V and their
critical values are listed below
7To really prove this, one needs to make a full matrix equation by takin g another choice of n in Equa-
tion ( 75), which has exactly the same Stokes automorphisms as discussed in the Section 1.3.
28 VERONICA F ANTINI AND CAMPBELL WHEELER
Table 1:
p1 (−0.5− 0.0317451i, 0) V1 −0.435753
p2 (0.0512932i,−2) V2 0.0127913
p3 (−0.212516− 0.009774i,−1) V3 −0.0801858 + 0.0248584i
p4 (0.212516− 0.009774i,−3) V4 −0.0801858− 0.0248584i
Taking the relative diﬀerence between volumes, the ﬁrst non trivial 8 Stokes line is at eiϑR>0
with ϑ = 1.30955 and it separates the regions I ⋆ and II. The second one is at ϑ = 1.501 and
separates the regions II and III. The third one is at ϑ = 1 .52112 and separates the regions
III and IV. As expected, they form the peacock pattern as illustr ated in Figure 19.
I
I⋆
IIIII
ϑ = π ϑ= 0
Figure 19. This ﬁgure depicts the Stokes rays in τ -plane with ϑ = arg(−1/τ )
forming a peacock pattern. Note that this is stretched in the direc tion of the
x-axis and the Stokes rays are all even closer to the vertical line. In addition,
it is symmetric with respect to the imaginary axis: on the right, the ﬁr st solid
Stokes rays contain the singularties at the points V2− V4, V3− V1, V3− V4 + 1,
V1− V4 + 1, which correspond to ϑ = 1 .83204, ϑ = 1 .64069, ϑ = 1 .62047 and
ϑ = 1 .60935, respectively. The dashed Stokes line corresponds to −V4, with
ϑ = 1 .87141, and crossing that ray there will be no Stokes phenomenon a s
shown in Section 4.2.9.
To perform the computation, we plot the set Cp0,ϑ and keep track of the branching of the
function V . We adopt the same conventions as in Section 4.1.
4.2.1. State integrals decomposition in I. Let ϑ∈ I. We plot the curves Cpj,ϑ for j = 1, 2, 3, 4
in Figure 20. We can decompose the thimble in terms on state integrals contours , hence the
algorithm gives
Ip1,V1,I = I0,0 , Ip2,V2,I = I−2,0 , Ip3,V3,I = I−1,0 , Ip4,V4,I = I−3,1 . (79)
4.2.2. The false saddle connection. Let ϑ = 1.87141, which corresponds to the Stokes line at
the angle arg
(
− 2πi
V4
)
. We plot the set Cp4,ϑ in Figure 21. Moving away from this apparent
saddle, we plot the set Cp4,ϑ in Figure 22 for ϑ = 1.85159.
8By non trivial we mean with non zero Stokes constants. Indeed the line at ϑ = 1. 27018 is not an eﬀective
Stokes line.
SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS 29
(0, 0)
(−1, 0)
(−2, 0)
(−3, 0)
(−2, 0)
(−1, 0) (−3, 0)
(−3, 0)
Figure 20. From the right, this ﬁgure depicts in orange the analytic contin-
uation of the set Cp1,ϑ,Cp2,ϑ,Cp3,ϑ andCp4,ϑ for ϑ = arg(−1/τ ) = 2 .54159 and
(A, B) = (4 , 1). The green lines are parallel to the lines i/τ .
(−3, 0)
Figure 21. This ﬁgure depicts in orange the set Cp4,ϑ for ϑ = arg(−1/τ ) =
1.87141, and ( A, B) = (4 , 1). The green lines are parallel to the lines i/τ .
We can decompose the thimbleCp4,ϑ in terms of state integral contours. We have contribution
of I−3,0 from the intersection of the orange contour with the interval ( −1, 0), which has
(n, m, ℓ) = (0 ,−3, 0). Then, at the second iteration of the algorithm we get the contr ibution
of−I−2,0 from the intersection of the magenta curve with the interval ( −1, 0), which has
(n, m, ℓ) = (0 ,−2, 0). Therefore, we ﬁnd
Ip4,V4,I⋆ =I−3,0−I −2,0 =I−3,1 (80)
30 VERONICA F ANTINI AND CAMPBELL WHEELER
(−3, 0)
(−4, 0)(−1, 0)
Figure 22. This ﬁgure depicts in orange the set Cp4,ϑ for ϑ = arg(−1/τ ) =
1.85159, and ( A, B) = (4 , 1). The green lines are parallel to the lines i/τ . The
magenta curve represents the tail at the intersection of the set Cp4,ϑ with the
green lines.
where in the last equality follows from Equation ( 14). Notice that the set Cp4,ϑ intersects the
interval (0, 1) twice, thus there is no contribution coming from the state integr alI−3,1.
4.2.3. The saddle connection between I and II. The saddle connection is depicted in Fig-
ure 23. Notice that the magenta line hits the critical point p2. This suggests that in the
(−3, 0)
(−4, 0)
(−2, 0)
(−3, 0)
Figure 23. This ﬁgure depicts in orange the set Cp4,ϑ for ϑ = arg(−1/τ ) =
1.83204, and ( A, B) = (4 , 1). The green lines are parallel to the lines i/τ . The
magenta curve represents the tail at the intersection of the set Cp4,ϑ with the
green lines.
state integral decomposition we should see the contribution from I−2,0, as we indeed verify
in Section 4.2.4.
4.2.4. State integrals decomposition in II. Let ϑ∈ II. We plot the curve Cp4,ϑ in Figure 24.
We can decompose the thimble in terms of state integrals contours. We have contributions
ofI−3,0 from the intersection of the orange contour with the interval ( −1, 0), which has
(n, m, ℓ) = (0 ,−3, 0). Then, due to the intersection with the green lines we should run t he
algorithm another time for the magenta contour. The latter inters ects a green line, thus we
apply the algorithm one more time to produce the violet contours. Bo th the magenta and
SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS 31
the violet contours do not contribute as they do not intersect the reals 2.12. Summarising,
the algorithm gives
Ip4,V4,II = I−3,0 =I−3,1 +I−2,0 , (81)
where the second equality follows from Equation ( 14).
(−3, 0)
(−4, 0)
(−2, 0)(−1, 0)
Figure 24. This ﬁgure depicts in orange the set Cp4,ϑ for ϑ = arg(−1/τ ) =
1.74159, and ( A, B) = (4 , 1). The green lines are parallel to the lines i/τ . The
magenta curve represents the tail at the intersection of the set Cp4,ϑ with the
green lines. The violet contour represents half of the contour that appears
when we run the algorithm a second time.
4.2.5. The saddle connection between II and III. The saddle connection is depicted in Fig-
ure 25. Note that it appears in the contours coming from the ﬁrst iteratio n of the algorithm.
(0, 0)
(−1, 0)
(−3, −1)(−2, −1)
(1, 0)
(−1, −1)
(−2, −1)
Figure 25. This ﬁgure depicts in orange the set Cp1,ϑ for ϑ = arg(−1/τ ) =
1.64069 and ( A, B) = (4 , 1). The green lines are parallel to the lines i/τ . The
magenta curves represent the tails at the intersection of the set Cp4,ϑ with the
green lines. The violet contour represents half of the contour that appears
when we run the algorithm a second time. Notice that the magenta contour
splits at the critical point p3 as this is a saddle connection.
32 VERONICA F ANTINI AND CAMPBELL WHEELER
(0, 0)
(−2, −1)
(−1, 0)
Figure 26. This ﬁgure depicts in orange the set Cp1,ϑ for ϑ = arg(−1/τ ) =
1.63159, and ( A, B) = (4 , 1). The green lines are parallel to the lines i/τ . The
magenta curve represents the tail at the intersection of the set Cp4,ϑ with the
green lines.
4.2.6. State integrals decomposition in III. Let ϑ∈ III. We plot the curve Cp2,ϑ in Figure 26.
We can decompose the thimble in terms on state integrals contours. We have contributions
fromI0,0 from the intersection of the orange contour with the interval ( −1, 0), which has
(n, m, ℓ) = (0 , 0, 0). Then due to the intersection with the green line we should study t he
contributions from the magenta line. Since the latter crosses the r eals in the interval (−1, 0),
we get the contribution of I−1,0, which has ( n, m, ℓ) = (0 ,−1, 0). Any other tails lead to no
contribution as they do not cross the reals and head to ∞. The algorithm therefore gives
Ip1,V1,III = I0,0−I −1,0 . (82)
4.2.7. The saddle connection between III and IV. The saddle connection is depicted in Fig-
ure 27.
(−3, 0)
(−4, 0)
(−2, 0)
(−1, 0)
(−4, 1)
(−5, 2)
(−5, 2)
Figure 27. This ﬁgure depicts in orange the set Cp4,ϑ for ϑ = arg(−1/τ ) =
1.62047, and ( A, B) = (4 , 1). The green lines are parallel to the lines i/τ . The
magenta curve represents the tail at the intersection of the set Cp4,ϑ with the
green lines. The violet contour represents half of the contour that appears
when we run the algorithm a second time. While it is hard to see at this sc ale,
the violet contour hits the critical point p3 + 1, which is just above the green
line. Therefore, at this critical angle the violet contour splits at this point.
SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS 33
4.2.8. State integrals decomposition in IV. Let ϑ∈ IV. We plot the set Cp4,ϑ in Figure 28.
We can decompose the thimble in terms of state integrals contours. We have contributions
(−3, 0)
(−2, 1)
(−4, 1)
(−5, 2)
Figure 28. This ﬁgure depicts in orange the set Cp4,τ for ϑ = arg(−1/τ ) =
1.61159, and ( A, B) = (4 , 1). The green lines are parallel to the lines i/τ . The
magenta curves represent the tails at the intersection of the set Cp4,ϑ with the
green lines. The violet contour represents half of the contour that appears
when we run the algorithm a second time.
ofI−3,0 from the intersection of the orange contour with the interval ( −1, 0), which has
(n, m, ℓ) = (0 ,−3, 0). Then, due to the intersection with the green lines we should run t he
algorithm another time for the magenta line. The latter intersects a green line, thus we apply
the algorithm one more time for the violet line. Then we ﬁnd a contribut ion of−q2I−5,1 from
the intersection of the violet line with the interval (0 , 1), which has ( n, m, ℓ) = (2 ,−5, 1).
Summarising, the algorithm gives
Ip4,V4,IV = I−3,0− q2I−5,1 =I−3,0− qI−1,0 , (83)
where the second equality follows from Equation ( 14). Notice that the magenta line in
Figure 28 does not contribute even if it intersects the interval (0 , 1). Indeed it intersects the
green line before intersecting the reals, and this leads to the contr ibution from the violet
tail, as shown in Figure 29.
Figure 29. This ﬁgure depicts in violet the tail that contributes in the de-
composition of the set Cp4,ϑ given by state integral contours.
34 VERONICA F ANTINI AND CAMPBELL WHEELER
4.2.9. First few Stokes constants. We can now describe the Stokes matrices associated to
ﬁrst Stokes rays in Figure
19. From Equations ( 79) and ( 80) we get
( Ip1,V1,I⋆ Ip2,V2,I⋆ Ip3,V3,I⋆ Ip4,V4,I⋆
) = ( Ip1,V1,I Ip2,V2,I Ip3,V3,I Ip4,V4,I
)




1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1



 . (84)
Therefore we learn that there is no Stokes jump between region I and I⋆. Then, from
Equations (
79) and ( 81) we ﬁnd
(
Ip1,V1,II Ip2,V2,II Ip3,V3,II Ip4,V4,II
)
=
(
Ip1,V1,I Ip2,V2,I Ip3,V3,I Ip4,V4,I
)




1 0 0 0
0 1 0 1
0 0 1 0
0 0 0 1



 . (85)
From Equations (
81) and ( 82), we ﬁnd
(
Ip1,V1,III Ip2,V2,III Ip3,V3,III Ip4,V4,III
)
=
(
Ip1,V1,II Ip2,V2,II Ip3,V3,II Ip4,V4,II
)




1 0 0 0
0 1 0 0
−1 0 1 0
0 0 0 1



 . (86)
Finally, from Equations (
82) and ( 83) we ﬁnd
(
Ip1,V1,IV Ip2,V2,IV Ip3,V3,IV Ip4,V4,IV
)
=
(
Ip1,V1,III Ip2,V2,III Ip3,V3,III Ip4,V4,III
)




1 0 0 0
0 1 0 0
0 0 1 −q
0 0 0 1



 .
(87)
Therefore, we see that
SI,I⋆(q) =




1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1



 , SI,II(q) =




1 0 0 0
0 1 0 1
0 0 1 0
0 0 0 1



 ,
SII,III(q) =




1 0 0 0
0 1 0 0
−1 0 1 0
0 0 0 1



 , SIII,IV(q) =




1 0 0 0
0 1 0 0
0 0 1 −q
0 0 0 1



 .
(88)
4.2.10. Computing all Stokes constants. We can again compute the Stokes matrix SI,X using
quantum modularity [
13] or equivalently the factorisations of the state integrals [ 9, 10]. Here
it is more complicated than 4 1 or ( A, B) = (1 , 2) from Section 4.1 as one needs to use an
“untrapping” of the state integral and various identities between q-series and state integrals.
This was all done in [ 24, Sec. 10.1]. To give these results we need some notation.
Let Θ( q) be the matrix whose columns are given by the coeﬃcients of ǫ0, ǫ1, ǫ2, ǫ4 respec-
tively of the series
exp
( 1
2 ǫ + 1
4ǫ2E2(q)
)




θ(− exp(ǫ); q4)
−q5/8 exp(ǫ/4)θ(−q exp(ǫ); q4)
q12/8 exp(ǫ/2)θ(−q2 exp(ǫ); q4)
−q21/8 exp(3ǫ/4)θ(−q3 exp(ǫ); q4)



 , (89)
SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS 35
where θ(x; q) = ( qx; q)∞(x−1; q)∞(q; q)∞ and E2(q) =− 1
24 +∑ ∞
k=1 k qk
1−qk . Let
G(t; q) =
∞∑
k=0
q3k(4k+1)/2t4k
(q; q)4k








1
(q;q)4k
q3k+ 3
4 t
(q;q)4k+1
q6k+ 9
4 t2
(q;q)4k+2
q9k+ 9
2 t3
(q;q)4k+3
q4k
(q;q)4k
q3k+ 3
4 +4k+1t
(q;q)4k+1
q6k+ 9
4 +4k+2t2
(q;q)4k+2
q9k+ 9
2 +4k+3t3
(q;q)4k+3
q8k
(q;q)4k
q3k+ 3
4 +8k+2t
(q;q)4k+1
q6k+ 9
4 +8k+4t2
(q;q)4k+2
q9k+ 9
2 +8k+6t3
(q;q)4k+3
q12k
(q;q)4k
q3k+ 3
4 +12k+3t
(q;q)4k+1
q6k+ 9
4 +12k+6t2
(q;q)4k+2
q9k+ 9
2 +12k+9t3
(q;q)4k+3








, (90)
P (q) =




1 0 0 0
−q−3 − q−2 − q−1 q−3 + q−2 + 2q−1 + 1 + q −q2 − q3 − q4 − q5 − q12 q12
q−5 + q−4 + q−3 −q−5 − 2q−4 − 2q−3 − 2q−2 − q−1 + q3 1 + 2q + 2q2 + q3 + q4 + q10 + q11 −q10 − q11
−q−6 − q−1 q−6 + q−5 + q−4 − q2 −q−1 − 1 − q − q9 q9




(91)
and
F (q) = P (q)




1 0 0 0
0 1 0 0
0 0 q−4 0
0 0 0 q−12



 G(q−3/8; q)Θ( q) . (92)
The ﬁrst column of F (q) is given by
∞∑
k=0
q2k(k+1)
(q; q)k




q−2k
q−k
1
qk



 . (93)
The matrix F (q) can be extended to |q|⁄= 1 using the relations θ(x; q−1) = θ(x−1; q)−1 and
E2(q−1) = −E2(q). Let f (q) be the third row of F (q). Then using the identities of [
24,
Sec. 10.1], we ﬁnd that
(Ip1,V1,I Ip2,V2,I Ip3,V3,I Ip4,V4,I
)
= f (q−1)




1 0 0 0
0 τ 0 0
0 0 τ 2 0
0 0 0 τ 4




−1
F (q−1)−1




0 0 1 0
1 0 0 0
0 1 0 0
0 0 0 q−1




−1
.
(94)
This exactly agrees with the conjectures [
24, Ex. 61] for the Borel–Laplace resummation in
region I. A similar computation shows that in the region X we also ﬁnd ag reement with the
conjectures and
(Ip1,V1,X Ip2,V2,X Ip3,V3,X Ip4,V4,X
)
= f (q−1)




1 0 0 0
0 −τ 0 0
0 0 τ 2 0
0 0 0 τ 4




−1
F (q−1)−1




0 0 1 0
1 0 0 0
0 0 0 q−1
0 1 0 0




−1
.
(95)
36 VERONICA F ANTINI AND CAMPBELL WHEELER
This implies that
S+(q) =




0 0 1 0
1 0 0 0
0 1 0 0
0 0 0 q−1



 F (q−1)




1 0 0 0
0 −1 0 0
0 0 1 0
0 0 0 1



 F (q−1)−1




0 0 1 0
1 0 0 0
0 0 0 q−1
0 1 0 0




−1
=








0 0 1 0
1 0 0 0
0 1 0 0
0 0 0 q



 F (q)




1 0 0 0
0 −1 0 0
0 0 1 0
0 0 0 1



 F (q)−1




0 0 1 0
1 0 0 0
0 0 0 q−1
0 1 0 0




−1



−T
=




1− q− 2q2 q2 q −q− q2
1 + q + q2 1− q− q2 −1 + q + q2 1− q2
−1− q q + q2 1− q− 2q2 2q2
1− q2 −q 2q + q2 1− q− 2q2



 + O(q3)
=




1 0 0 0
0 1 0 1
0 0 1 0
0 0 0 1








1 0 0 0
0 1 0 0
−1 0 1 0
0 0 0 1








1 0 0 0
0 1 0 0
0 0 1 −q
0 0 0 1



··· .
(96)
The second equality follows from the duality of [
9, Conj. 1] and can be explicitly proved in
this example. This exactly agrees with the computations of Equation (88).
