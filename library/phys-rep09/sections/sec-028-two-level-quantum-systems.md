---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-028-two-level-quantum-systems
section_title: "Two-level quantum systems"
section_number: null
pages: 39-43
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
The generic Hamiltonian for a two-level quantum system can be written down in the form
H(t) =

E1(t)
C(t)
C∗(t)
E2(t)

(189)
where E1(t), E2(t) are real functions and C(t) is, in general, a complex function of t. We define the solvable piece of the
Hamiltonian as the diagonal matrix
H0(t) =

E1(t)
0
0
E2(t)

(190)
and all the time-dependent interaction described by the function C(t) is considered as a perturbation. In the Interaction
Picture, the new Hamiltonian reads (see (92))
HI(t) =


0
C(t) exp

i
Z t
0
dt′ω(t′)

C∗(t) exp

−i
Z t
0
dt′ω(t′)

0


(191)
with ω = (E1 −E2)/¯h. Suppose now that H0 is time-independent. Then U(t) = exp( ˜H0t)UI(t). Without loss of generality,
the H0 may be rendered traceless, so that E1 = −E2 ≡E. Thus ±E denote the eigenenergies associated to the eigenvectors
190
S. Blanes et al. / Physics Reports 470 (2009) 151–238
|+⟩≡(1, 0)T, |−⟩≡(0, 1)T of H0, the unperturbed system. In terms of Pauli matrices the Hamiltonian in this case may be
expressed as
H(t) =
1
2 ¯hωσ3 + f (t)σ1 + g(t)σ2,
(192)
where f = Re(C) and g = −Im(C).
Since H0 is diagonal, the transition probability between eigenstates |+⟩, |−⟩of H0 is simply
P(t) = |⟨+|UI(t)|−⟩|2.
(193)
As the evaluation of (193) requires the computation and manipulation of exponential matrices involving Pauli matrices,
formulas (18) and (19) in Section 1.2 come in handy here.
Next, we study two particular cases of interaction for which the exact solution of the time evolution operator admits an
analytic expression.
1- Rectangular step. Suppose that in (192) g = 0, namely,
H(t) =
1
2 ¯hωσ3 + f (t)σ1
(194)
with f = 0 for t < 0 and f = V0 for t ≥0. Alternatively, if we restrict ourselves to compute an observable such as the
transition probability, this example is equivalent to a rectangular mound (or rectangular barrier) of width T = t above. The
exact solution for this problem reads
U(t, 0) = exp

−i
ω
2 σ3 +
V0
¯h σ1

t

,
(195)
which yields the exact transition probability
Pex =
4γ 2
4γ 2 + ξ 2 sin2 p
γ 2 + ξ 2/4
(196)
between eigenstates |+⟩, |−⟩of H0. Here we have denoted γ ≡V0t/¯h and ξ ≡ωt.
The Interaction Picture is defined here by the explicit integration of the diagonal piece in the Hamiltonian, so that
U = exp(−iξσ3/2)UI, where UI stands for the time evolution operator in the Interaction Picture and obeys
U′
I = ˜HI(t)UI,
UI(0) = I
(197)
with
HI(t) = f (t)(σ1 cos ξ −σ2 sin ξ).
(198)
A computation with the usual time-dependent perturbation theory gives for the first orders (formula (52))
P(1)
pt = P(2)
pt =
4γ 2
ξ 2 sin2(ξ/2)
(199)
P(3)
pt = P(4)
pt = γ 2
ξ 2

2 sin ξ
2 −γ 2
3ξ 2

9 sin ξ
2 + sin
3ξ
2 −6ξ cos ξ
2 + 4 sin3 ξ
2
2
.
Notice that P(i)
pt > 1 may happen in the equations above because the unitary character of the operator U(t) is not preserved
by the usual time-dependent perturbation formalism.
In this example it is not difficult to compute the first four terms in the Magnus series corresponding to UI(t) = exp Ω(t)
in (197). To facilitate the notation, we define s = sin ξ and c = cos ξ. The Magnus approximants in the Interaction Picture
may be written down in terms of Pauli matrices and read explicitly
Ω1 = −iγ
ξ [σ1s + σ2(1 −c)]
Ω2 = −i
γ
ξ
2
σ3(s −ξ)
Ω3 = −i
γ
ξ
3 1
3{σ1[3ξ(1 + c) −(5 + c)s] + σ2[(3ξ −s)s −4(1 −c)]}
Ω4 = −i
γ
ξ
4 1
3σ3[(4c + 5)ξ −(c + 8)s].
(200)
S. Blanes et al. / Physics Reports 470 (2009) 151–238
191
Fig. 3. Rectangular step: Transition probabilities as a function of ξ, with γ = 1.5. The solid line corresponds to the exact result (196). Broken lines stand
for approximations obtained via ME, and lines with symbols correspond to perturbation theory, according to the legend. Computations up to fourth order,
in the Interaction Picture.
Fig. 4.
Rectangular step: Transition probabilities as a function of ξ, with γ = 2. Lines are coded as in Fig. 3. Computations up to fourth order, in the
Interaction Picture.
The first two formulae for the approximate transition probabilities are, respectively
P(1)
M = sin2

2γ
ξ
sin(ξ/2)

P(2)
M =
4γ 2
ξ 2
sin2 λ
λ2
sin2(ξ/2),
λ = [4 sin2(ξ/2) + γ 2
ξ 2 (sin ξ −ξ)2]1/2.
(201)
We omit explicit expressions for P(3)
M and P(4)
M since they are quite involved. However, we include their outputs in Figs. 3–5,
where we plot the first to fourth order approximate transition probabilities with ME in the Interaction Picture and compare
them to the exact case, and also with perturbation theory outputs. In Figs. 3 and 4 we set γ = 1.5 and γ = 2 respectively,
whereas in Fig. 5 we fix ξ = 1.
We observe that for the Magnus expansion in the Interaction Picture, the smaller the value of the parameter ξ, the better
the approximate solution works. As a matter of fact, in the sudden limit, ξ ≪1, ME furnishes the exact result; unlike
perturbation theory. As far as the intensity of the perturbation γ increases, the quality of the approximations spoils. This
effect is much more dramatic for the standard perturbation theory.
192
S. Blanes et al. / Physics Reports 470 (2009) 151–238
Fig. 5.
Rectangular step: Transition probabilities as a function of γ , with ξ = 1. Lines are coded as in Fig. 3. Computations up to fourth order, in the
Interaction Picture.
On the other hand, it is clear from (198) that
Z t
−∞
∥HI(t1)∥2 dt1 =
Z t
0
|f (t1)| dt1 = V0 t,
whence
R t
−∞∥˜HI(t1)∥2 dt1 = γ , and thus Theorem 9 guarantees that the Magnus expansion in the Interaction Picture is
convergent if γ < π. Notice that this is always the case for the parameters considered in Figs. 3–5. The estimate γ < π
for the convergence domain in the Interaction Picture should be compared with the corresponding one in the Schrödinger
picture:
Z t
−∞
∥˜H(t1)∥2 dt1 =
r
γ 2 + ξ 2
4 < π.
Notice then that, as pointed out in Section 2.9, a change of picture allows us to improve the convergence of the Magnus
expansion.
2- Hyperbolic secant step: Rosen–Zener model. In the Rosen–Zener Hamiltonian [121] the interaction C(t) in (189) is given
by the real function V(t) = V0 sech(t/T), where T determines the time-scale. We will use the notation γ = πV0T/¯h and
ξ = ωT = 2ET/¯h.
The corresponding Hamiltonian in terms of Pauli matrices is
H(t) = Eσ3 + V(t)σ1 ≡a(t) · σ,
V(t) = V0/ cosh(t/T),
(202)
with a ≡(V(t), 0, E). In the Interaction Picture one has
HI(s) = V(s)(σ1 cos(ξs) −σ2 sin(ξs))
(203)
in terms of the dimensionless time-variable s = t/T. Notice that ξ measures the ratio between the interaction time T and
the internal time of the system ¯h/2E. From (203), and after straightforward calculation, the first and second ME operators
are readily obtained.
The exact result for the transition probability (provided the time interval extends from −∞to +∞), as well as
perturbation theory and Magnus expansion up to second order read [15]
Pex =
sin2 γ
cosh2(πξ/2)
P(1)
pt = P(2)
pt =
γ 2
cosh2(πξ/2)
P(1)
M = sin2[γ / cosh(πξ/2)]
P(2)
M =
sin2 λ
λ2
γ 2
cosh2(πξ/2)
(204)
λ = γ

1
cosh2(πξ/2) + γ 2g2(ξ)
π 4
1/2
,
g(ξ) = 8ξ
∞
X
k=0
2k + 1
[(2k + 1)2 + ξ 2]2 .
S. Blanes et al. / Physics Reports 470 (2009) 151–238
193
Fig. 6. Rosen–Zener model: Transition probabilities (204) as a function of ξ, with γ = 1.5. The solid line stands for the exact result. Broken lines stand
for approximations obtained via ME, and triangles correspond to perturbation theory, according to the legend. Computations up to second order, in the
Interaction Picture.
Fig. 7. Rosen–Zener model: Transition probabilities as a function of γ , with ξ = 0.3. Lines are coded as in Fig. 6. Computations up to second order, in the
Interaction Picture.
In Figs. 6 and 7 we plot some results from the formulae in (204). In Fig. 6 we take γ = 1.5 and in Fig. 7 we set ξ = 0.3.
Similarly to the case of the rectangular step, we observe in Fig. 6 that the Magnus expansion works better in the sudden
regime defined by ξ ≪1, namely, when the internal time of the system ¯h/2E is much larger than the time scale T of the
perturbation. Also, Fig. 7 illustrates how the approximations spoil as far as the intensity γ increases. Notice, in both figures,
the unitarity violation of the approximation built with the usual perturbation theory.
In this case, a simple calculation shows that
Z ∞
−∞
∥˜HI(t)∥2 dt = (1/¯h)
Z ∞
−∞
|V(t)| dt = V0πT/¯h = γ ,
and thus the Magnus series converges at least for γ < π.
