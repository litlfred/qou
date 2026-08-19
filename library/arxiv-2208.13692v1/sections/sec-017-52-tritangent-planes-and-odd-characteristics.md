---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-017-52-tritangent-planes-and-odd-characteristics
section_title: "Tritangent Planes and Odd Characteristics"
section_number: 5.2
pages: 31-32
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
doc_brief: "European Journal of Mathematics (2024) 10:3 RESEARCH ARTICLE — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
canonical embedding of a curve in Pg−1, the intersection with a hyperplane gives an eﬀective
element of the canonical divisor class of the curve, as it corresponds to the zero-locus of a
diﬀerential on the curve. A tritangent plane is a plane that intersects the curve tangentially
in three points. If a hyperplane is tangent at each intersection (i.e. the intersection is of
order 2) then this naturally constructs an eﬀective theta divisor on the curve, and moreover
every such theta characteristic θ gives a hyperplane [CKRSN19]. For any sextic that is
the intersection of a smooth quadric and smooth quartic in P3, for example Bring’s curve,
the 120 tritangent planes are in 1-1 correspondence with the 120 odd theta characteristics
[HL17, Theorem 2.2].
On Bring’s curve we have the following result about these planes.
Proposition 5.6 ([Edg81]). The 120 tritangent planes on Bring’s curve split into two
classes, 60 in each class;
(1) those where all three contact points are Weierstrass points, and
(2) those where only one contact points is a Weierstrass point.
32 H. W. BRADEN AND LINDEN DISNEY-HOGG
Planes in the ﬁrst and second class respectively have equations (recalling notation from §3.1)
Π(1)
αjk :=
{xj
β − xk
γ = 0
}
,
Π(2)
ijk :={(α− 1)(α + 4)xi + (β− 1)(β + 4)xj + (γ− 1)(γ + 4)xk = 0},
where [xi]∈ P4 and i,j,k distinct.
To clarify the notation we have used for the planes, recall that the position of the indices
on Weierstrass points Wijk indicates which root was equal to xi. The same principle holds
for Π(1)
αjk, Π(1)
iβk, and Π(1)
ijγ.
Corollary 5.7. The orbit decomposition of odd theta characteristics on Bring’s curve is
(19) 120 = 20 + 20 + 20 + 60 .
Proof. The characteristics coming from the triangent planes are
T (1)
αjk =
5∑
i=1
i⁄=j,k
Wijk,
T (2)
ijk =Wijk +O+
ijk +O−
ijk.
Here we deﬁne the points O±
ijk by, for example,
O±
345 =
[
1±i
√
15
2 : 1∓i
√
15
2 :α2 +α + 1,β 2 +β + 1,γ 2 +γ + 1
]
.
A simple orbit-stabiliser argument then gives the orbit decomposition as, for example, T (1)
α45
is stabilised by the symmetric group S{1,2,3} and T (2)
345 is stabilised by S{1,2}. □
Remark 5.8. While we were able to proceed analytically here characterising the orbits of
the odd characteristics using the work of earlier authors who had identiﬁed the tritangent
planes of the curve we also may obtain the orbit structure numerically using Sage. Given a
homology representation of the automorphism group, the algorithm to compute the orbits is
exact, but the current implementation in Sage requires ﬂoating point arithmetic to calculate
this representation.
