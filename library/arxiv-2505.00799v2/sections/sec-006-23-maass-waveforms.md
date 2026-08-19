---
doc_id: arxiv-2505.00799v2
doc_title: "QUANTUM MODULAR FORMS AND RESURGENCE"
section_id: sec-006-23-maass-waveforms
section_title: "Maass Waveforms"
section_number: 2.3
pages: 13-15
source_pdf: 2505.00799v2.pdf
source_sha256: cc9d2ab4c6c79b50
doc_brief: "QUANTUM MODULAR FORMS AND RESURGENCE — In 2010, Zagier described a new phenomenon which he called quantum mod- ularity."
---
forms for SL2(Z). We also refer the reader to [9,23] for a more thorough introduction to the
theory.
We begin with a smooth function u: H→ C satisfying the following.
(1) For all γ = (a b
c d)∈ Γ0(N) and for all z∈ H, we have u(γz) =u(z);
(2) If ∆ :=−y2

∂2
∂x2 + ∂2
∂y 2

is the hyperbolic Laplacian, then ∆u =λu for some λ∈ C.
14 ELEANOR MCSPIRIT AND LARRY ROLEN
Such a function necessarily admits a Fourier–Whittaker expansion. If the zeroth Fourier–
Whittaker coefficient vanishes andu is square-integrable on a fundamental domain of SL2(Z)
with respect to the hyperbolic measure, then we say that u is a Maass waveform.
We call λ the eigenvalue of u and if λ =s(1−s), then s is called its spectral parameter.
Such a function u(z) has an expansion of the form
(2.3) u(z) =√y
X
n∈Z̸=0
AnKs−1/2(2π|n|y)e2πinx, (z =x +iy∈ H),
where Kν(x) is the K-Bessel function of order ν.
In the central result of [25], Lewis and Zagier gave a correspondence between Maass
waveforms and three different classes of functions. While all show up in our results, we will
only recall two of them here. Let u(z) be a Maass waveform with spectral parameter s,
whereℜ(s) > 0. Then associated to u are a pair of Dirichlet L-series Lε(ρ), ε ={0, 1},
convergent in some right half-plane, such that the functions Λ ε(ρ) :=γs(ρ +ε)Lε(ρ), where
γs(ρ) := 1
4πρ Γ
ρ−s + 1/2
2

Γ
ρ +s− 1/2
2

,
are entire functions of finite order and satisfy
Λε(1−ρ) = (−1)εΛε(ρ).
From the coefficients in the expansion of u in (2.3), their Dirichlet series take the form
Lε(ρ) :=
∞X
m=1
Am + (−1)εA−m
mρ , (ε∈{ 0, 1}).
Moreoever, there is also a corresponding holomorphic periodic functionf : C\R→ C, defined
by
f(z) :=



P∞
n>0Anns−1/2qn, if z∈ H,
−P∞
n<0An|n|s−1/2qn, if z∈ H−,
where H− denotes the lower half-plane. From this point on, we will abuse notation and use
f to refer to the restriction of f to the upper half-plane. Throughout, we will prove results
forf in the upper half-plane, but the corresponding results for f in the lower half-plane are
completely analogous, and in fact f on C\R is really a single holomorphic quantum modular
form.
We will also consider one non-cuspidal case in our work. We will define the non-holomorphic
Eisenstein series with spectral parameter s by
QUANTUM MODULAR FORMS AND RESURGENCE 15
(2.4)
Es(z) :=ζ(2s)ys + π1/2Γ(s− 1
2)
Γ(s) ζ(2s− 1)y1−s
+ 4πs
Γ(s)
√y
∞X
n=1
n1/2−sσ2s−1(n)Ks−1/2(2πny) cos(2πnx),
where σν(n) := P
d|ndν is the ν-th sum of divisors function. We will specifically analyze
the case where s = 1/2. As is standard, we will write d(n) for σ0(n). For the associated
holomorphic periodic function in this case, we pick the normalization
f(z) := 1− 4
∞X
n=1
d(n)qn.
Above, we gave the functional equations for the pair of L-functions associated to a Maass
waveform. Here, we state the analogous result for our Eisenstein series of interest. The
corresponding L-function is proportional to
ζ2(ρ) =
∞X
m=1
d(m)
mρ , ℜ(ρ)> 1,
where ζ(ρ) is the Riemann zeta function. The completion of the function ζ2(ρ) has mero-
morphic continuation to C with a pole at s = 1 and satisfies the functional equation
π−ρΓ
ρ
2
2
ζ2(ρ) =π−(1−ρ)Γ
1−ρ
2
2
ζ2(1−ρ).
