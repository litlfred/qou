---
doc_id: arxiv-2111.04763v2
doc_title: "RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION"
section_id: sec-012-45-xq-series
section_title: "(x,q)-series"
section_number: 4.5
pages: 47-48
source_pdf: 2111.04763v2.pdf
source_sha256: 760a7f9794e8baaa
doc_brief: "RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION — Some years ago, it was conjectured by the first author that the Chern–Simons perturbation theory of a 3-manifold at the trivial flat"
---
variablex. Recall that the matrixJ red
m (x,q) 7 is a fundamental solution to the linearq-
difference equation
fm(x,q)−(1 +x+x −1)fm+1(x,q) + (1 +x+x −1−q 2+m)fm+2(x,q)−f m+3(x,q) = 0(214)
and it is defined by
Jred
m (x,q) =


Am(x,q)A m+1(x,q)A m+2(x,q)
Bm(x,q)B m+1(x,q)B m+2(x,q)
Cm(x,q)C m+1(x,q)C m+2(x,q)

,|q|̸= 1,(215)
where the holomorphic blocks are given by
Am(x,q) =H(x,x −1,qm;q),(216a)
Bm(x,q) =θ(−q 1/2x;q)−2xmH(x,x 2,qmx2;q),(216b)
Cm(x,q) =θ(−q −1/2x;q)−2x−mH(x−1,x−2,qmx−2;q),(216c)
7The matricesJ red
m (x,q)are related to the WronskiansWm(x,q)in [GGMn21, GGMn] by
Jred
m (x,q) =W m(x,q)T.(213)
48 STAVROS GAROUFALIDIS, JIE GU, MARCOS MARIÑO, AND CAMPBELL WHEELER
whereH(x,y,z;q ε) :=H ε(x,y,z;q)for|q|<1andε=±and
H +(x,y,z;q) = (qx;q) ∞(qy;q)∞
∞X
n=0
qn(n+1)zn
(q;q) n(qx;q) n(qy;q) n
,(217a)
H−(x,y,z;q) = 1
(x;q)∞(y;q)∞
∞X
n=0
(−1)n q
1
2n(n+1)x−ny−nzn
(q;q) n(qx−1;q)n(qy−1;q)n
,(217b)
θ(x;q) = (−q
1
2x;q)∞(−q
1
2x−1;q)∞.(217c)
To these series we wish to add an additional series which satisfies the inhomogenousq-
difference equations of the descendant coloured Jones polynomial (163). This can be easily
constructed using the deformations of the Habiro polynomials (165). We find a solution
Dm(x,q) =−
−1X
n=−∞
qmnHn(q)x−n(qx;q) n(q−1x;q−1)n.(218)
(compare with Equation (91)) where|q|<1andm∈Zor|q|>1andm∈Z ≥0, andHn(q)
is the coefficient ofε0δ0 in the expansion ofHn(ϵ,δ;q). In particular, for|q|<1we have
Dm(x,q) =−
∞X
n,k=0
(−1)kqn(n+1)+k(k+1)/2−nk−(m+1)(n+1) (q;q) n+k
(q;q) k(q;q) n(x−1;q)n+1(x;q)n+1
(219)
and we see the(x,q)-seriesD 0(x,q)coincides withf 52(x,q)in [Par20, Par].
This series can be included as the first row of a6×6matrix of(x,q)-series. The latter
might be related to the factorisation of the state integral proposed in Section 4.8.
However, we find that the matrices above and below the reals have different quantum
modular co-cycles related by inversion. This implies that to do a full discussion on resurgence
one needs to understand the monodromy of thisq-holonomic system. Both these issue will
be explored in later publications. For now, we give a description of the Stokes matrices
restricted toτin the upper half plane.
