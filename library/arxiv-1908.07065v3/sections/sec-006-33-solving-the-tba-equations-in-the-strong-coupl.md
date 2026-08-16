---
doc_id: arxiv-1908.07065v3
doc_title: "Prepared for submission to JHEP Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-006-33-solving-the-tba-equations-in-the-strong-coupl
section_title: "Solving the TBA equations in the strong coupling region"
section_number: 3.3
pages: 18-20
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve ofN = 2, SU (2) super Yang–Mills"
---
As we have argued, Borel sums of quantum periods are solutions to the TBA equations (3.30),(3.55).
In principle the resummed quantum periods can be computed from these TBA equations by using
the dictionaries (3.39) and (3.63). In practice, however, these equations are diﬃcult to use. First
of all, one needs information on the boundary conditions at strong coupling in order to solve the
equations. In addition, the standard tools to solve these equations numerically converge very
slowly.
Let us ﬁrst consider the simplest example at u = 0, where the TBA system collapses to a
single equation (3.38), which we reproduce here (we have absorbed the factor ξ in (3.38) in the
angle θ)
ϵ(θ) =πeθ−
∫
R
log(1 + e−ϵ(θ′))
π cosh(θ−θ′) dθ′. (3.69)
The solution can be identiﬁed with the quantum dyon period through the dictionary
ϵ(θ) = 1
ℏs(ΠD)(u = 0, ℏ) , ℏ = Π(0)
D π−1e−θ = 16√π
Γ
( 1
4
)2 e−θ . (3.70)
– 17 –
Furthermore, the asymptotic behavior of the solution ϵ(θ) as θ→∞ is of the form
ϵ(θ)∼πeθ +
∑
n≥1
ϵ(n)e(1−2n)θ, (3.71)
whose coeﬃcients are identiﬁed with the quantum corrections to the dyon period
ϵ(n) = 1
π2n−1 (Π(0)
D )2n−1Π(n)
D . (3.72)
It turns out that the equation (3.69) admits many possible boundary conditions at θ→−∞ .
This is in stark contrast to the TBA equations for polynomial potentials studied in [7, 8], where
the equations themselves ﬁx the behavior of the solutions at θ → −∞. One possibility for
the boundary conditions at θ→−∞ is the linear behavior (5.28). This type of behavior was
considered by Zamolodchikov in [19] but in a slightly diﬀerent context, as we will discuss in Sec.
5 (see also Appendix B). However, it can be seen that this is not well suited for the quantum
periods we are studying 2. One quick way to see this is that the linear boundary condition with
P⁄= 0 implies ϵ(1)<−1/3 (c.f. (B.29)), while from the quantum Matone relation (2.27) we ﬁnd
ϵ(1) = 1
π Π(0)
D Π(1)
D = 1
2πi
(
Π(0)
A Π(1)
B − Π(0)
B Π(1)
A
)
=−1
3. (3.73)
It turns out that the appropriate boundary condition in this case is given by
ϵ(θ) =−2 log
(
−2θ
π
)
+··· , θ →−∞ . (3.74)
This boundary condition for the TBA equation (3.69) was also studied by Zamolodchikov in
[43]3. One can use a small modiﬁcation of the “dilogarithm trick” of [44] to show that, with the
boundary condition (3.74), one has indeed (3.73) (in the context of [43], this calculation gives
the central charge c = 1 for the corresponding sinh-Gordon theory).
To implement numerically the boundary condition (3.74), we borrow a trick from [19]. We
deﬁne a continuous function
f1(θ) =−2 log
(
1 + 2
π log(1 + e−θ)
)
, (3.75)
which has the same boundary behavior as (3.74) and is exponentially suppressed when θ→ +∞.
We then look for a function F1(θ) which satisﬁes
f1(θ) =
∫
R
K(θ−θ′)F1(θ′)dθ′ , K (θ) = 1
π cosh(θ) . (3.76)
The generic solution to this linear integral equation is
F1(θ) = 1
2
(
f1
(
θ + iπ
2
)
+f1
(
θ− iπ
2
))
. (3.77)
2In [7] it was also pointed out that (3.69) admits many boundary conditions at θ → −∞. However, it is
claimed there that the correct boundary condition for the quantum period is precisely of the type (B.14), namely,
ϵ(θ)∼θ/2 +... for θ→−∞ , which is not quite correct for the reasons explained here.
3Alternatively we can justify this boundary condition by using the results in section 5, see equation (5.40).
– 18 –
ℏ = 1 ℏ = 1/2
TBA 6.62781 13.47880
Borel sum 6.62781917 ... 13.47880936...
Table 5: Quantum dyon period at u = 0.
ℏ = 1 ℏ = 1/2
TBA 9 .16476 18 .61486
Borel sum 9 .16476545... 18.61486738...
Table 6: Quantum dyon period at u = 1/3.
For our particular f1(θ), we thus have
F1(θ) =− log
(
1 + 2
π log(1 + ie−θ)
)
− log
(
1 + 2
π log(1− ie−θ)
)
. (3.78)
This is a real function for θ∈ R. The TBA equation (3.69) can then be written as
ϵ(θ) =πeθ +f1(θ)−
∫
R
dθ′ 1
π cosh(θ−θ′)
(
log(1 + e−ϵ(θ′)) +F1(θ′)
)
, (3.79)
where both boundary conditions at ±∞ are explicitly spelt out.
The numerical solution to the TBA equation (3.69) converges rather slowly, and we managed
to obtain 6 stabilised digits for ℏ = 1 and 7 stabilised digits for ℏ = 1/2. These results, on the
other hand, do agree with the Borel resummation of the quantum dyon period. See Table 5.
Let us now move away from the point u = 0 but remain in the strong coupling region with
u∈ (−1, 0)∪ (0, 1). The TBA system (3.33) has two integral equations coupled to each other.
Nevertheless, at θ → −∞the ﬁrst terms ∝ eθ on the r.h.s. of both equations in (3.33) are
negligible, and the TBA system also collapses to the single equation (3.69) (with the ﬁrst term
on the r.h.s. suppressed). Therefore both ϵd(θ),ϵm(θ) should have the same boundary condition
as (3.74), in other words
ϵd(θ)∼ϵm(θ)∼− 2 log
(
−2θ
π
)
+... , θ →−∞ . (3.80)
This is corroborated by the fact that the Matone relation (3.73) can be reproduced with this
boundary behavior by using again a slight modiﬁcation of the “dilogarithm trick” [44]. We use
again the trick of inserting the pair of f1(θ),F 1(θ′) functions, and we ﬁnd that the numerical
solution to the TBA system (3.33) has roughly the same speed of convergence as the solution
to (3.69) for u = 0. We tabulate the results for u = 1/3 in Tables 6,7 and they also agree with
the Borel sum of the quantum periods. Note that the TBA system is solved with θ∈ R, which
in light of (3.39) corresponds to real ℏ for the quantum dyon period and to imaginary ℏ for the
quantum monopole period.
