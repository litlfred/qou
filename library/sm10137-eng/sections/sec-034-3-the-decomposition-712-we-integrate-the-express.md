---
doc_id: sm10137-eng
doc_title: "Sbornik: Mathematics 215:12 1607–1632 Matematicheski˘ı Sbornik 215:12 30–55 Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel "
section_id: sec-034-3-the-decomposition-712-we-integrate-the-express
section_title: "The decomposition (7.12). We integrate the expression for T(x, y) by parts:"
section_number: 3
pages: 17-18
source_pdf: sm10137_eng.pdf
source_sha256: afd51b0231f4dc41
doc_brief: "Sbornik: Mathematics 215:12 1607–1632 Matematicheski˘ı Sbornik 215:12 30–55 Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel S. M. Gorbunov — We"
---
Z ∞
0
D(xt)
r
2
π
1
y b0(t) d(sin(yt −ϕν)) = D(xt)
r
2
π
1
y b0(t) sin(yt −ϕν)

∞
0
−
Z ∞
0
D(xt)
r
2
π
1
y sin(yt −ϕν)b′(t) dt
−
Z ∞
0
xD′(xt)
r
2
π
1
y sin(yt −ϕν)b0(t) dt,
where the first term is zero by Lemma 5 and (7.7). Next we take the following
kernels for the decomposition (7.12):
T0(x, y) = −
Z ∞
0
D(xt)
r
2
π
1
y sin(yt −ϕν)b′(t) dt,
T1(x, y) = −
Z ∞
0
x

D′(xt) −Aν
cos(xt −ϕν)
xt
r
2
π
1
y sin(yt −ϕν)b0(t) dt,
Z(x, y) = −
Z ∞
0
xAν
cos(xt −ϕν)
xt
b0(t)
r
2
π
1
y sin(yt −ϕν) dt.
(7.15)
Trace norm estimates. Before diving into calculations we present several inequal-
ities we need.
Firstly, the Cauchy–Bunyakovsky–Schwarz inequality implies the following:
|b0(t)| =

Z t
0
b′(x) dx

 ⩽
√
t ∥b∥˙H1.
(7.16)
The same argument for the derivative gives
|b′(t)| ⩽
√
t (|b′(0)| + ∥b∥˙H2).
(7.17)
Further, using (7.17) we have
|b0(t)| =

Z t
0
b′(x) dx

 ⩽(|b′(0)| + ∥b∥˙H2)t3/2.
(7.18)
Lastly, observe the identity
d
dt
b0(t)
t

= 1
t2
Z t
0
b′(x) dx −b0(t) +
Z t
0
xb′′(x) dx

= 1
t2
Z t
0
xb′′(x) dx.
The Cauchy–Bunyakovsky–Schwarz inequality implies that

Z t
0
xb′′(x) du

 ⩽t3/2∥b∥˙H2.
Substituting this in yields

d
dt
b0(t)
t


 ⩽∥b∥˙H2
√
t .
(7.19)
1624
S. M. Gorbunov
