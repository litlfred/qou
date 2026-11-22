---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-027-a2-double-sine-function
section_title: "A.2 Double Sine function"
section_number: null
pages: 22-23
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
toc_source: outline
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
The special functions used in this note are all build from the so-called double Sine-function.
This function is closely related to the special function here denoted eb(x), which was introduced
under the name of quantum dilogarithm in [FK2]. These special functions are simply related
to the Barnes double Gamma function [Br], and were also introduced in studies of quantum
groups and integrable models in [F2, Ru, Wo, V].
In the strip |Im(x)| < Q
2 , function eb(x) has the following integral representation
eb(x) = exp
(
−
Z
R+i0
dt
4 t
e−2itx
sinh bt sinh t
b
)
,
(A.4)
where the integration contour goes around the pole t = 0 in the upper half–plane. The function
sb(x) is then related to eb(x) as follows
sb(x) = e
iπ
2 x2+ iπ
24 (b2+b−2)eb(x) .
(A.5)
The analytic continuation of sb(x) to the entire complex plane is a meromorphic function with
23
the following properties
functional equation
sb(x + i
2b±1)
sb(x −i
2b±1) = 2 cosh(πb±1x) ,
(A.6)
reﬂection property
sb(x) sb(−x) = 1 ,
(A.7)
complex conjugation
sb(x) = sb(−¯x) ,
(A.8)
zeros / poles
(sb(x))±1 = 0 ⇔±x ∈

iQ
2 +nb+mb−1; n, m ∈Z≥0	
,
(A.9)
residue
Res
x=−i Q
2
sb(x) = i
2π ,
(A.10)
asymptotics
sb(x) ∼
(
e−iπ
2 (x2+ 1
12 (b2+b−2)) for |x| →∞, |arg(x)| < π
2 ,
e+ iπ
2 (x2+ 1
12 (b2+b−2)) for |x| →∞, |arg(x)| > π
2 .
(A.11)
Of particular importance for us is the behavior for b →0, which is given as
eb
 v
2πb

= exp

−
1
2πb2Li2(−ev)

1 + O(b2)

.
(A.12)
In our paper we mainly use the special function Sb(x) deﬁned by
Sb(x) := sb(ix −i
2Q)
(A.13)
and has the properties
self–duality
Sb(x) = Sb−1(x) ,
(A.14)
functional equation
Sb(x + b±1) = 2 sin(πb±1x) Sb(x) ,
(A.15)
reﬂection property
Sb(x) Sb(Q −x) = 1 .
(A.16)
The behavior of Sb(x) for b →0 is then given as
Sb
 ν
2πb

= e−
i
2πb2 ( 1
4ν2−π
2 ν+ 1
6 π2) exp

−
1
2πib2Li2(eiν)

1 + O(b2)

.
(A.17)
In terms of Γb(x) the double Sine-function is given as
Sb(x) =
Γb(x)
Γb(Q −x).
