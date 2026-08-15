---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-037-5-from-330-we-also-ﬁnd-the-taylor-expansion-of-i
section_title: "From (3.30) we also ﬁnd the Taylor expansion of I(z;τ ) at z = 0,"
section_number: 5
pages: 37-38
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
doc_brief: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group — We develop several methods that allow us to compute all-loop partition functions in perturbative Chern-Simons theory with"
---
I(z;τ ) = 4
∞∑
k=0
Ck(τ )zk,
with coeﬃcients Ck(τ ) = τ −kCk(1/τ ) given by
C0(τ ) = πi
24
(
τ +τ −1)
, C 1(τ ) =
∫ ∞
0
( 1
sinhx sinhτx − 1
τx 2
)
dx,
C2(τ ) = −πi
2τ , C k(τ ) = 0 for k≥ 4 even,
Ck(τ ) = 2k−1
k!
∫ ∞
0
xk−1dx
sinhx sinhτx for k≥ 3 odd.
By expanding 1/ sinh(x) and 1/ sinh(τx ) as power series in e−x and e−τ x we can evaluate
the last of these expressions to get
Ck(τ ) = 2k+1
k!
∑
m,n>0, odd
∫ ∞
0
e−mx−nτ xxk−1dx = 2
k
∑
s∈Ξ( τ )
s−k (k≥ 3 odd)
with Ξ( τ ) as in (3.35). Dividing by 4 and exponentiating gives the Wei erstrass product
expansion
Φ(z;τ ) = exp
(πi
24
(
τ +τ −1)
+ C1(τ )z− πiz2
2τ
) ∏
s∈Ξ( τ )
(s +z
s−z e−2z/s
)
(3.37)
– 36 –
of Φ( z;τ ). From this expansion, one ﬁnds that Φ( z;τ ) extends meromorphically to C×(
C /integerdivide(−∞, 0]
)
with simple poles and simple zeros for z∈ Ξ(τ ) and z∈− Ξ(τ ) and no other
zeros or poles. (This analytic continuation can also be dedu ced by rotating the path of
integration in (3.21), e.g. by replacing
∫
R(+) by
∫
R(+)/√τ for z suﬃciently small.)
