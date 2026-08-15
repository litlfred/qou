---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-023-82-asymptotics-of-the-r-matrix-using-ideal-octah
section_title: "Asymptotics of the R-matrix using ideal octahedra"
section_number: 8.2
pages: 19-21
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
by ratios of ﬁve quantum factorials (see Equations ( 26)), Proposition 8.2 gives a formula for the asymptotic
behavior of the entries of the R-matrix when evaluated at e2πi/n . This is the content of the next proposition.
Proposition 8.5. (a) Suppose that α, β, κ are real numbers that satisfy the inequalities
(33) α, β, κ ∈ [0, 1] 0 ≤ β + κ ≤ 1, 0 ≤ α − κ ≤ 1.
Then the following limit exists
(34) r+(α, β, κ) := lim
n→∞
1
n log |evn(R+(n; ⌊nα⌋, ⌊nβ⌋, ⌊nκ⌋))|,
and is equal to
(35) r+(α, β, κ) = [ −Λ( π(β + κ)) + Λ( πβ) + Λ( πκ) − Λ( πα) + Λ( π(α − κ))]/π.
(b) r+(α, β, κ) equals to 1 /(2π) times the volume of an ideal octahedron with vertices
(36) (0 , 1, ∞, zκ , (zβ zκ − 1)/(zβ − 1), zα ) ∈ (C \ {0, 1})6
20 STA VROS GAROUF ALIDIS AND THANG TQ L ˆE
where ( zα , zβ , zκ ) = ( e2πiα , e2πiβ , e2πiκ ).
(c) Suppose that α, β, κ are real numbers that satisfy:
α, β, κ ∈ [0, 1] 0 ≤ α + κ ≤ 1, 0 ≤ β − κ ≤ 1.
Then the following limit exists
r−(α, β, κ) := lim
n→∞
1
n log |evn(R−(n; ⌊nα⌋, ⌊nβ⌋, ⌊nκ⌋))|.
and is equal to
(37) r−(α, β, κ) = r+(β, α, κ).
Proof. (a) Observe that
|evn({j})| = |evn({n − j})| = 2 sin(jπ/n), and |evn({n − 1}!)| =
n−1∏
j=1
2 sin(jπ/n) = n.
From these, we have that
(38) |evn({j}!)| = n
|evn({n − 1 − j}!)| .
Using ( 26) and then ( 38), we have
(39)
|evn(R+(n; a, b, k))| = |evn({b + k}!)| |evn({n − 1 + k − a}!)|
|evn({b}!)| |evn({k}!)| |evn({n − 1 − a}!)|
= |evn({b + k}!)| |evn({a}!)|
|evn({b}!)| |evn({k}!)| |evn({a − k}!)|
Proposition 8.2 concludes the proof of (a). (b) was pointed out to us by D. Thurst on. Although this fact
is not used in the proof of Proposition 8.6 nor in the proof of Theorem 1.13, it is an interesting geometric
fact. To prove it, recall that the boundary of 3-dimensional hype rbolic space is C ∪ {∞}. Let Tz denote
the regular ideal tetrahedron of shape z ∈ C − {0, 1}. Tz is isometric to the ideal tetrahedron with ordered
vertices at 0 , 1, ∞ and z in the boundary of 3-dimensional hyperbolic space. For z ∈ C \ {0, 1}, the ideal
octahedron Tz is isometric to T1/ (1−z) and Tz/ (z−1) by an orientation-preserving isometry, and isometric to
T1/z , T(1−z)/z and T(z−1)/z by an orientation-reversing isometry. Thus, when z ∈ C \ {0, 1}, we have:
(40) vol( Tz) = vol( T1/ (1−z)) = vol( Tz/ (z−1)) = −vol(T1/z ) = −vol(T(1−z)/z ) = −vol(T(z−1)/z )
The shape of the ideal tetrahedron with distinct ordered vertices (z0, z1, z2, z3) in C ∪ {∞} is given by the
cross-ratio
(41) [ z0 : z1 : z2 : z3] = (z0 − z3)(z1 − z2)
(z0 − z2)(z1 − z3)
following the convention of [ DZ06, Eqn.1.4]. If ( α1, α2, α3) denote the three dihedral angles of Tz at opposite
pairs of edges, then the volume vol( Tz) is given by [ Rat06, Thm.10.4.10]
vol(Tz) = Λ( α1) + Λ( α2) + Λ( α3)
If the shape parameter z = eiθ is a complex number of magnitude 1, then the dihedral angles of Tz coincide
with the angles of an isosceles triangle with angles ( θ, (π − θ)/2, (π − θ)/2). In that case, we have
vol(Teiθ ) = Λ ( θ) + Λ
(π − θ
2
)
+ Λ
(π − θ
2
)
.
The following symmetries of the Lobachevsky function [ Rat06, Thm.10.4.3,10.4.4]
Λ( −θ) = −Λ( θ), 1
2 Λ(2 θ) = Λ( θ) + Λ
(
θ + π
2
)
ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT 21
imply that
(42) vol(Teiθ ) = 2Λ
(θ
2
)
.
Now, we return to the proof of part (b). Fix α, β, κ as in (33) and consider the complex numbers of magnitude
1:
(zα , zβ , zκ ) = ( e2πiα , e2πiβ , e2πiκ )
Consider ﬁve ideal tetrahedra with shapes
(43) ( zβ zκ )−1, z β , z κ , z −1
α , z α z−1
κ
Equations (
35) and ( 42) implies that the sum of their volumes is given by 2 π r+(α, β, κ). Now consider the
ideal octahedron with vertices
(A, B, C, D, E, F ) = (0 , 1, ∞, zκ , (zβ zκ − 1)/(zβ − 1), zα )
drawn as follows:
It can be triangulated into ﬁve ideal tetrahedra ABDE , BDCE , ABCD , ABCF and ACDF with ordered
vertices and with shape parameters
{
1 − 1
zβ zκ
, zβ
zβ − 1 , zκ
zκ − 1 , zα
zα − 1 , zα
zκ
}
computed according to Equation ( 41). Adding up the volumes of these tetrahedra, with proper orienta tions
concludes the proof of (b). (c) is analogous to (a). We thank the r eferee for correcting the vertices of the
octahedron in an earlier version of this paper. □
