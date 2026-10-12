---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-058-stochastic-differential-equations
section_title: "Stochastic differential equations"
section_number: null
pages: 78-80
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
In recent years, the use of stochastic differential equations (SDEs) has become widespread in the simulation of random
phenomena appearing in physics, engineering, economics etc, such as turbulent diffusion, polymer dynamics and investment
finance [197]. Although models based on SDEs can offer a more realistic representation of the system than ordinary
differential equations, the design of effective numerical schemes for solving SDEs is, in comparison with ODEs, a less
developed field of research. This fact notwithstanding, it is true that, recently, new classes of integration methods have
been constructed which automatically incorporate conservation properties the SDE possesses. Since some of the methods
are based precisely on the Magnus expansion, we briefly review their main features here, and refer the reader to the more
advanced literature on the subject [197–199].
A SDE in its general form is usually written as
dy(t) = g0(t, y(t))dt +
d
X
j=1
gj(t, y(t))dWj(t),
y(0) = y0,
y ∈Rm,
(346)
where gj, (j ≥0), are m-vector-valued functions. The function g0 is the deterministic continuous component (called the
drift coefficient), the gj, (j ≥1), represent the stochastic continuous components (the diffusion coefficients) and Wj are d
independent Wiener processes. A Wiener process W (also called Brownian motion) is a stochastic process [197] satisfying
W(0) = 0,
E[W(t)] = 0,
Var[W(t) −W(s)] = t −s,
t > s
which has independent increments on non-overlapping intervals. In other words, a Wiener process is normally distributed
with mean or expectation value E equal to zero and variance t.
Eq. (346) can be written in integral form as
y(t) = y0 +
Z t
0
g0(s, y(s))ds +
d
X
j=1
Z t
0
gj(s, y(s))dWj(s).
(347)
The d integrals in (347) cannot be considered as Riemann–Stieltjes integrals, since the sample paths of a Wiener process
are not of bounded variation. In fact, if different choices are made for the point τi (in the subintervals [ti−1, ti] of a given
partition) where the function is evaluated, then the approximating sums for each gj,
N
X
i=1
gj(τi, y(τi))(Wj(ti) −Wj(ti−1)),
τi = θti + (1 −θ)ti−1,
(348)
converge (in the mean-square sense) to different values of the integral, depending on the value of θ [35]. Thus, for instance,
Z b
a
W(t)dW(t) =
1
2(W 2(b) −W 2(a)) +

θ −
1
2

(b −a).
If θ = 0, then τi = ti−1 (the left-hand point of each subinterval) and the resulting integral is called an Itô integral; if θ = 1/2
(so that the midpoint is used instead), one has a Stratonovich integral. These are the two main choices and, although they
are related, the particular election depends ultimately on the nature of the process to be modeled [35]. It can be shown that
the Stratonovich calculus satisfies the Riemann–Stieltjes rules of calculus, and thus it is the natural choice here.
When dealing with numerical methods for solving (346), there are two ways of measuring accuracy [197]. The first is
strong convergence, essential when the aim is to get numerical approximations to the trajectories which are close to the exact
solution. The second is weak convergence, when only certain moments of the solution are of interest. Thus, if ˆyn denotes the
numerical approximation to y(tn) after n steps with constant step size h = (tn −t0)/n, then the numerical solution ˆy
converges strongly to the exact solution y with strong global order p if there exist C > 0 (independent of h) and δ > 0 such
that
E[∥ˆyn −y(tn)∥] ≤Chp,
h ∈(0, δ).
It is worth noticing that p can be fractional, since the root mean-square order of the Wiener process is h1/2. One of the
simplest procedures for solving (346) numerically is the so-called Euler–Maruyama method [200],
yn+1 = yn +
d
X
j=0
Jjgj(tn, yn),
(349)
where
h = tn+1 −tn,
J0 = h,
Jj = Wj(tn+1) −Wj(tn),
j = 1, . . . , d.
This scheme turns out to be of strong order 1/2. Here the Jj can be computed as
√
hNj, where the Nj are N(0, 1) normally
distributed independent random variables [35].
S. Blanes et al. / Physics Reports 470 (2009) 151–238
229
For the general non-autonomous linear Stratonovich problem defined by
dy = G0(t)y dt +
d
X
j=1
Gj(t)ydWj,
y(0) = y0 ∈Rm
(350)
the Magnus expansion for the deterministic case can be extended in quite a straightforward way. It is well worth noting that
in Eq. (350), even when the functions Gj are constant, there is no explicit solution [198], unless all the Gj, j ≥0, commute
with one another, in which case it holds that
y(t) = exp
 
G0 t +
d
X
j=1
GjWj(t)
!
y0.
(351)
In many modeling situations, however, there is no reason to expect that the functions Gj associated with the Wiener
processes commute. If, for simplicity, we only consider the autonomous case and write
G(t) ≡G0 dt +
d
X
j=1
GjdWj(t),
then (350) can be expressed as
dy = G(t)y dt,
y(0) = y0
and thus one can formally apply the Magnus expansion to this equation to get y(t) = exp(Ω(t))y0. The first term in the
series reads, in this case,
Z t
0
G(s)ds ≡
Z t
0
G0ds +
d
X
j=1
Z t
0
GjdWj(s) = G0 t +
d
X
j=1
GjJj,
where now
Jj =
Z t
0
dW(s) = Wj(t) −Wj(0).
By inserting these expressions into the recurrence associated with the Magnus series, Burrage and Burrage [35] show that
Ω(t) =
d
X
j=0
GjJj +
1
2
d
X
i=0
d
X
j=i+1
[Gi, Gj](Jji −Jij)
+
d
X
i=0
d
X
k=0
d
X
j=k+1
[Gi, [Gj, Gk]]

1
3(Jkji −Jjki) +
1
12
Ji(Jjk −Jkj)

+ · · · ,
(352)
where the multiple Stratonovich integrals are defined by
Jj1j2···jl(t) =
Z t
0
Z sl
0
· · ·
Z s2
0
dWj1(s1) · · · dWjl(sl),
ji ∈{0, 1, . . . , d}.
(353)
Since not all the Stratonovich integrals are independent, one has to compute only d(d + 1)(d + 5)/6 stochastic integral
evaluations to achieve strong order 1.5 with the expression (352) [35]. If, on the other hand, Ω(t) is truncated after the first
set of terms, then the resulting numerical approximation
y(t) = exp
 
d
X
j=0
GjJj
!
y0
has strong order 1/2, but leads to smaller error coefficients than the Euler–Maruyama method (349) [35]. Furthermore, the
error becomes smaller as the GiGj terms get closer to commuting and the scheme preserves the underlying structure of the
problem.
One should notice, at this point, that Eq. (346) (or, in the linear case, Eq. (350)), has formally the same structure as the
nonlinear ODE (171) appearing in control theory. Therefore, the formalism developed there to get the Chen–Fliess series can
be applied here with the alphabet I = {0, 1, . . . , d} and the integrals
Z
0
µ

(t) =
Z t
0
µ(s)ds,
Z
i
µ

(t) =
Z t
0
µ(s)dWi(s),
i ≥1,
since the Stratonovich integrals satisfy the integration by parts rule. In other words, one can obtain the corresponding
Magnus expansion for arbitrary (linear or nonlinear) stochastic differential equations simply by following the same
procedure as for deterministic ODEs.
With respect to nonlinear Stratonovich stochastic differential equations, it should be remarked that the use of Lie
algebraic techniques, as well as the design of Lie group methods for obtaining strong approximations when the solution
evolves on a smooth manifold, has received considerable attention in the recent literature [201–203].
230
S. Blanes et al. / Physics Reports 470 (2009) 151–238
