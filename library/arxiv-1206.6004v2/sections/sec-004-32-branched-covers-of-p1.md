---
doc_id: arxiv-1206.6004v2
doc_title: ""
section_id: sec-004-32-branched-covers-of-p1
section_title: "Branched covers of P1"
section_number: 3.2
pages: 4-6
source_pdf: 1206.6004v2.pdf
source_sha256: b490672c8c3557dd
doc_brief: "Bring’s Curve: its Period Matrix and the Vector of Riemann Constants ⋆ — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
duplicate_of: "sigma12-065"
---
We now consider the curve (2.1) as a branched cover of P1 withx as the coordinate. The affine
part of the HC curve is obtained by setting z = 1 in (2.1) yielding
xy5 +x +x2y2−x4y− 2y3 = 0. (3.2)
Bring’s Curve: its Period Matrix and the Vector of Riemann Constants 5
There are 5 sheets above the generic x, with branch points at 0,∞ and
{ζk
4
(
1674± 870i
√
15
)1/5 : k∈{ 0,..., 4}
}
.
There is also a double solution at x = ζk but these are precisely the singular points similar to
[1, 1, 1] we investigated before and after resolution the cover is regular there.
Atx = 0 we have two preimages, one corresponding to [0 , 0, 1] with an expansion
y = 1
21/3x1/3 +··· , (3.3)
where three sheets come together, and the other corresponding to [0 , 1, 0] with expansion
y =
√
2x−1/2 +··· (3.4)
where two sheets come together. Similarly at x =∞ we have two preimages after desingu-
larisation: [1 , 0, 0]1 where from [1 ,t 4,t ]≡ [t−1,t 3, 1] and y ≈ x−3; and [1 , 0, 0]2 where from
[1,t,t 4]≡ [t−4,t−3, 1] and y≈x3/4. The other 10 branch points correspond to the solutions of
256x10− 837x5 + 3456 = 0 and have two sheets coming together at each 3.
3.3 Real paths on the Hulek–Craig curve
The real structure of the HK curve leads to real ovals. Here we shall show there is in fact one.
We begin by looking at portions of this oval, which we shall refer to as a ‘real path’ and then
indicate how they join together 4. The real paths in this cover will be of particular interest later
on so we will take some time to explore their nature now. We begin with the affine curve,
further noting what happens at the real infinite points [0 , 1, 0], [1, 0, 0]1,2 which compactify the
real curve.
First, if the number of real roots of (3.2) considered as a polynomial in y changes then its
discriminant
∆(x) =−x3(
256x20− 1349x15 + 5386x10− 7749x5 + 3456
)
=−x3(
256u2− 837u + 3456
)
(u− 1)2, u =x5, (3.5)
must vanish there. The only real roots of the equation ∆( x) = are x = 0, 1, so we are reduced
to considering the intervals (−∞, 0), (0, 1), (1,∞).
• If x< 0 then there is just one real root.
• If 0 <x< 1 then there are three real roots.
• If x> 1 then there are also three real roots.
Referring to the expansions (3.3) and (3.4) we see that a real path starting withx< 0 moving
towardsx = 0 must be approaching [0, 0, 1] along the expansion y = 2−1/3x1/3 +··· (i.e. y→ 0
too). Continuity demands that when extended pastx = 0 it too should havey small and positive
for small x> 0. We will call this path γ0.
3We remark that the Maple command monodromy(xy5 + x + x2y2− x4y− 2y3, x, y,showpaths) will produce the
monodromy data for the HK curve, together with the paths and sheet numbering necessary to make sense of this
data. The branch point 0 has monodromy [1 , 2][3, 4, 5] while that of∞ is [1, 4, 5, 2]; these are the cycle structures
described above. The remaining ten branch points arranged with increasing argument have monodromies [1 , 4],
[2, 4], [2, 5], [1, 5], [1, 3], [2, 3],[2, 4], [1, 4], [1, 5] respectively, here indicating the two sheets that come together.
4The Maple command plot real curve(xy5 + x + x2y2− x4y− 2y3, x, y) will in fact plot this directly.
6 H.W. Braden and T.P. Northover
We now turn our attention to another real path approaching x = 0, this time for x >0. It
must lie on the expansion y =
√
2x−1/2 +··· and hence y is either large and positive or large
and negative; we will call these paths γ+ and γ−. In fact the expansion is telling us that γ+
and γ− meet at [0, 1, 0] and we could form a single continuous path, but we will maintain the
distinction for now.
In summary we have three real paths coming out of x = 0 along the positive axis, satisfying
(for small x> 0),
y(γ−)≪ 0<y (γ0)≪y(γ+).
Now we are ready to consider what happens at x = 1. On the desingularised curve there are
three real points here (the two from desingularising y = 1 and the remaining real root α). Each
of the curves coming out of x = 0 must pass through one of them. Further, the order of the
y values among the paths must be the same approaching x = 1 as it was leaving x = 0 since,
otherwise, they would have crossed in between and this would have shown itself in (3.5).
The three expansions near x = 1 in order of increasing y for x< 1 are
y≈α, y ≈ 1 + (x− 1)−1 +
√
5
2 , y ≈ 1 + (x− 1)−1−
√
5
2 .
Thus the path that started y≪ 0 must pass through the first point, y≈ 0 must pass through
the second and y≫ 0 the third. Significantly this means the latter two paths actually cross at
x = 1 and for x = 1 +ϵ we have
y(γ−)<y (γ+)< 1<y (γ0).
Finally we consider the remaining points [1 , 0, 0]1,2 at∞. Recall the expansions (3.1). If
x≪ 0 then naturally there is only one real path, which arrives at [1 , 0, 0]1 with small y. If
x≫ 0 the situation is very similar to x = 0: two expansions with |y|≫ 0 arriving at [1, 0, 0]2
and one lying between these with y≈ 0. As before, the paths cannot have crossed between
x = 1 andx =∞ and so we are forced to conclude that γ− has the expansiony≈−x3/4,γ+ has
the expansion y≈x−3 and γ0 has the expansion y≈x3/4 near∞.
Putting these facts together we can plot Fig. 1 (the joined semicircular dots represent the
same point on the curve, separated to show the distinct y values of paths entering them). We
discover that all the paths (γ−,γ0,γ+ and thex< 0 path) actually form part of one large closed
loop showing that the real structure of the HK curve has one oval. (Another proof of this will
be given in the next section.)
4 The Riera and Rodr´ ıguez hyperbolic model
