---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-Body Systems in Lattice Effective Field Theory"
section_id: sec-053-partial-wave-decomposition
section_title: "Partial wave decomposition"
section_number: null
pages: 89-90
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
toc_source: outline
doc_brief: "Few-Body Systems in Lattice Effective Field Theory — 62 sections: Front matter; Introduction and Motivation; The standard model of particle phy"
---
In the following we give the deﬁnition of special functions used throughout the thesis. A basis of spherical
functions is given by the spherical harmonics Yl,lz(φ, θ), where l = 0, 1, 2, ∞and lz = −l, −l + 1, . . . , l.
They are deﬁned as
Yl,lz(φ, θ) = (−1)lz
"2l + 1
4π
(l −lz)!
(l + lz)!
# 1
2
Pl,lz(cos θ) exp

ilzφ

,
(A.1)
with the Laguerre polynomials,
Pl,lz(x) = (1 −x2)
lz
2 dlz
dxlz Pl(x).
(A.2)
Pl(x) are the Legendre polynomials
Pl(x) =
1
2ll!
dl
dxl

x2 −1
l .
(A.3)
The spherical harmonics have the following properties,
Yl,lz(θ, φ) = (−1)lz h
Yl,lz(θ, φ)
i∗,
(A.4)
D
Yl,lz(φ, θ)

 Yl′,l′
z(φ, θ)
E
= δl,l′δlz,l′
z
(A.5)
∞
X
l=0
lX
lz=−l

Yl,lz(φ, θ)
E D
Yl,lz(φ′, θ′)

 = δφ,φ′δθ,θ′.
(A.6)
The Riccati-Bessel functions are deﬁned recursively by
yl+1(z) = −y′
l(z) + (l + 1)z−1y(z),
(A.7)
where yl(z) is the regular [irregular] solution ul(z) [nl(z)]. The ﬁrst solutions have the form
u0(z) = sin(z),
(A.8)
n0(z) = cos(z).
(A.9)
83
Appendix A Special functions and algebras
As the Riccati-Bessel functions do not represent in- and outgoing wave functions, we have to use the
Hankel functions, which are a linear combination of the former ones deﬁned as
h±
l (z) = ul (z) ± inl (z) .
(A.10)
Then h±
l (z) represents an outgoing and incoming partial wave, respectively.
The conﬂuent hypergeometric function which is necessary for the Coulomb wave functions reads
F(a, b; z) =
∞
X
n=0
Γ(a + n)
Γ(a)
Γ(b)
Γ(b + n)
zn
n!.
(A.11)
Similar to the regular and irregular Bessel functions, there exists a second conﬂuent hypergeometric
function U which is deﬁned as
U(a, b; z) =
Γ(1 −b)
Γ(a −b + 1)F(a, b; z) + Γ(b −1)
Γ(a)
z1−bF(a −b + 1, 2 −b; z).
(A.12)
Depending on the evaluation procedure, it may be useful to replace the functions F and U by the
corresponding Whittaker functions,
Mk,m(z) = exp
−z
2

zm+ 1
2 F
 
m −k + 1
2; 1 + 2m; z
!
,
(A.13)
Wk,m(z) = exp
−z
2

zm+ 1
2 U
 
m −k + 1
2; 1 + 2m; z
!
.
(A.14)
The aforementioned Γ function is deﬁned by
Γ(z + 1) =
Z ∞
0
dt tz exp(−t),
(A.15)
and fulﬁlls the recursive equation
Γ(z + 1) = zΓ(z).
(A.16)
