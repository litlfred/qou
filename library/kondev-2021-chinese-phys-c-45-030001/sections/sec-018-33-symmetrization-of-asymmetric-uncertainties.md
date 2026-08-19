---
doc_id: kondev-2021-chinese-phys-c-45-030001
doc_title: "Chinese Physics C PAPER • OPEN ACCESS The NUBASE2020 evaluation of nuclear physics properties * To cite this article: F.G. Kondev et al 2021 Chinese Phys. C 45 030001"
section_id: sec-018-33-symmetrization-of-asymmetric-uncertainties
section_title: "Symmetrization of asymmetric uncertainties"
section_number: 3.3
pages: 14-14
source_pdf: Kondev_2021_Chinese_Phys._C_45_030001.pdf
source_sha256: 29b14ce8a7c0ecac
doc_brief: "Chinese Physics C PAPER • OPEN ACCESS The NUBASE2020 evaluation of nuclear physics properties * To cite this article: F.G. Kondev et al 2021 Chinese Phys. C 45 030001 — 31 sections: Physics Division"
---
Experimental results are sometimes reported in the litera-
ture with asymmetric uncertainties, e.g. X +a
−b , and it is a policy
of NUBASE to symmetrize these uncertainties.
Similarly to the previous version of N UBASE [1–4], the
asymmetric uncertainty is associated with a two-piece normal
distribution (sometimes called “split-normal distribution” or
“Fechner distribution”), T N(X, a, b), and the symmetrization
is achieved by mapping this distribution into a normal (sym-
metric) distribution, N(µ, σ ), where µ is the mean value and
σ is the standard deviation.
The probability density function of a two-piece normal
distribution is given as:
f (x) =
{
A× exp[−(x− X)2/2a2] if x > X,
A× exp[−(x− X)2/2b2] if x < X (7)
It has a modal (most probable) value of x = X, a standard de-
viation b for x<X and a standard deviation a for x>X (see
Figure 7), with A = (
√
π/2× (a + b))−1. This distribution is
formed by taking the left half of a normal distributionN(X, b)
and the right half of a normal distributionN(X, a) and scaling
them to give a common value of f(x)=A at the mode X (see
Figure 7). The mean value and the variance of this distribu-
tion can be determined as [24]:
µ = X +
√
2/π× (a− b) (8)
σ 2 = (1− 2/π)× (a− b)2 + a× b (9)
The median value m, which divides the distribution into
two equal areas is then:
m =
{
X + a
√
2× erf−1( a−b
2a
)
if a > b,
X + b
√
2× erf−1( a−b
2b
)
if b > a. (10)
If one takes erf−1(z)≃√πz/2 then
m− X≃
√
π/8× (a− b)≃ 0.6267× (a− b) (11)
In order to allow for a small non-linearity that appears for
high values of m− X, equation 11 is modiﬁed to:
m≃ X + 0.64× (a− b) (12)
Following the above approach, the two-piece normal dis-
tribution T N(X, a, b) is mapped into an equivalent normal
(symmetric) distribution N( m,σ) (see Figure 7) that have a
mean value equal to the median value m (equation 12) and
variance σ (equation 9). As a consequence, X +a
−b is sym-
metrized to m±σ and the latter is adopted in NUBASE 2020.
