---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-015-41-semiclassical-asymptotics-of-the-quantum-dilo
section_title: "Semiclassical asymptotics of the quantum dilogarithm"
section_number: 4.1
pages: 15-16
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
It is well-known that the semiclassical asymptotics, i.e. the small γ asymptotics of
the quantum dilogarithm Sγ, is given by Euler’s dilogarithm
Li2(z) = −
∫ z
0
Log(1 −w)
w dw (4.22)
for z ∈ C\]1, ∞[. Here and elsewhere Log denotes the principal logarithm. For
ζ ∈ C satisfying either Re( ζ) = ±π and Im(ζ) ≥ 0 or |Re(ζ)| < π one can check
(see Appendix A) that
1
2√−1γ Li2(−e
√−1ζ) = 1
4
∫
CR
eζz
sinh(πz)γz 2 dz,
hence we have that
Sγ(ζ) = exp
( 1
2√−1γ Li2(−e
√−1ζ ) +Iγ(ζ)
)
(4.23)
for such ζ, where
Iγ(ζ) = 1
4
∫
CR
eζz
z sinh(πz)
( 1
sinh(γz ) − 1
γz
)
dz.
Lemma 3. If |Re(ζ)|<π then
|Iγ(ζ)| ≤ A
( 1
π − Re(ζ) + 1
π + Re(ζ)
)
γ +B
(
1 +e−Im(ζ)R
)
γ,
16 Asymptotics of the quantum invariants for the ﬁgure 8 knot
and for |Re(ζ)| ≤ π we have
|Iγ(ζ)| ≤ 2A +B
(
1 +e−Im(ζ)R
)
γ,
where A and B are positive constants only depending on R.
A proof is given in Appendix A. On the unit circle the imaginary part of th e
dilogarithm is given by Clausen’s function Cl 2, i.e.
Im
(
Li2(eiθ)
)
= Cl 2(θ) =
∞∑
n=1
sin(nθ)
n2 = −
∫ θ
0
Log
⏐
⏐
⏐
⏐2 sin
(t
2
) ⏐
⏐
⏐
⏐dt (4.24)
forθ ∈ R. One sees that Cl 2 is increasing on [0 ,π/ 3] ∪ [5π/3, 2π] and decreasing on
[π/3, 5π/3]. In particular, Cl 2 attains its maximum value at π/3 and its minimum
value at 5π/3. Moreover
−Cl2
(5π
3
)
= Cl 2
(π
3
)
= −2
∫ π/6
0
Log|2 sin(φ)|dφ = 2J
(π
6
)
= 1
