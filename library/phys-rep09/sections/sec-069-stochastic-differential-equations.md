---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-069-stochastic-differential-equations
section_title: "Stochastic differential equations"
section_number: null
pages: 78-80
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
In recent years, the use of stochastic differential equations (SDEs) has become widespread in the simulation of random
phenomena appearing in physics, engineering, economics etc, such as turbulent diffusion, polymer dynamics and investment
finance [197]. Although models based on SDEs can offer a more realistic representation of the system than ordinary
differential equations, the design of effective numerical schemes for solving SDEs is, in comparison with ODEs, a less
developed field of research. This fact notwithstanding, it is true that, recently, new classes of integration methods have
been constructed which automatically incorporate conservation properties the SDE possesses. Since some of the methods
are based precisely on the Magnus expansion, we briefly review their main features here, and refer the reader to the more
advanced literature on the subject [197-199].

A SDE in its general form is usually written as

d
dy(t) = gol, y¥O)dt+ D gilt, yOAWj®, yO) =o, YER", (346)

j=l

where gj, (j => 0), are m-vector-valued functions. The function go is the deterministic continuous component (called the
drift coefficient), the gj, (j = 1), represent the stochastic continuous components (the diffusion coefficients) and Wj are d
independent Wiener processes. A Wiener process W (also called Brownian motion) is a stochastic process [197] satisfying

w(0) = 0, E[W(t)] = 0, Var[W(t) —W(s)]=t—s, t>s

which has independent increments on non-overlapping intervals. In other words, a Wiener process is normally distributed
with mean or expectation value E equal to zero and variance t.
Eq. (346) can be written in integral form as

t d t
y(t) =yo+ | 80(s, y(s))ds + >> | gi(s, y(s))AW;(s). (347)
0 j=1 0
The d integrals in (347) cannot be considered as Riemann-Stieltjes integrals, since the sample paths of a Wiener process
are not of bounded variation. In fact, if different choices are made for the point 7; (in the subintervals [t;_1, t;] of a given
partition) where the function is evaluated, then the approximating sums for each gj,

N
git. vm) Wi) -—W(ti-1)), = Ot + (1 — @)ti-a, (348)

i=1
converge (in the mean-square sense) to different values of the integral, depending on the value of 6 [35]. Thus, for instance,

b
i] W(t)dW(t) = sw) —wa)) + (0 - ;) (b—a).

If@ = 0, then 7 = t;_, (the left-hand point of each subinterval) and the resulting integral is called an It6 integral; if6 = 1/2
(so that the midpoint is used instead), one has a Stratonovich integral. These are the two main choices and, although they
are related, the particular election depends ultimately on the nature of the process to be modeled [35]. It can be shown that
the Stratonovich calculus satisfies the Riemann-Stieltjes rules of calculus, and thus it is the natural choice here.

When dealing with numerical methods for solving (346), there are two ways of measuring accuracy [197]. The first is
strong convergence, essential when the aim is to get numerical approximations to the trajectories which are close to the exact
solution. The second is weak convergence, when only certain moments of the solution are of interest. Thus, if 7, denotes the
numerical approximation to y(tn) after n steps with constant step size h = (tn — fo)/n, then the numerical solution ¥
converges strongly to the exact solution y with strong global order p if there exist C > 0 (independent of h) and é > Osuch
that

E[|ljn — Y(tn) II] < Ch?, he (0,4).

It is worth noticing that p can be fractional, since the root mean-square order of the Wiener process is h'/?, One of the
simplest procedures for solving (346) numerically is the so-called Euler-Maruyama method [200],
d
Yn = Int YIBiltns Yn)s (349)

j=0
where
h=tni-—th Jo=h, Jj = Wi(tn41) — W(t), j= l,...,d.

This scheme turns out to be of strong order 1/2. Here the J; can be computed as VJhN;, where the Nj are N(0, 1) normally
distributed independent random variables [35].
S. Blanes et al. / Physics Reports 470 (2009) 151-238 229

For the general non-autonomous linear Stratonovich problem defined by

d
dy = Go(tydt+ D> G(HydW;, yO) = yo ER” (350)
j=l
the Magnus expansion for the deterministic case can be extended in quite a straightforward way. It is well worth noting that
in Eq. (350), even when the functions G; are constant, there is no explicit solution [198], unless all the G;, j > 0, commute
with one another, in which case it holds that

d
y(0) = exp (« t+>o cm) Yo. (351)
j=l

In many modeling situations, however, there is no reason to expect that the functions G; associated with the Wiener
processes commute. If, for simplicity, we only consider the autonomous case and write

d
G(t) = Godt + )> Gawj(e),
j=l
then (350) can be expressed as
dy=G(t)ydt, — y(0) = Yo
and thus one can formally apply the Magnus expansion to this equation to get y(t) = exp(2(t))yo. The first term in the
series reads, in this case,

t t d t d
il cwas = | Gods + >| GaW;(s) = Got + D> Gi},
0 0 j=1 70 j=l

where now
t
Ji -|/ dW(s) = W(t) — W,(0).
0

By inserting these expressions into the recurrence associated with the Magnus series, Burrage and Burrage [35] show that
d d d
1
Qt) = v Git 5 v xX (Gi, GiGi — Ju)
j=0 i=0 j=i+1
d dd 1 1
+ ve ve » (Gi, (Gj, Gell (5 ~ Ji) + hin a) ten, (352)
i=0 k=0 j=k+1

where the multiple Stratonovich integrals are defined by

t ps Ss)
Init = [ il of dWj, (S1)---dWj,(S1), ji € (0, 1,..., dh. (353)
0 0 0

Since not all the Stratonovich integrals are independent, one has to compute only d(d + 1)(d + 5)/6 stochastic integral
evaluations to achieve strong order 1.5 with the expression (352) [35]. If, on the other hand, 2(t) is truncated after the first
set of terms, then the resulting numerical approximation

d
y(t) = exp (o as) Yo
j=0

has strong order 1/2, but leads to smaller error coefficients than the Euler-Maruyama method (349) [35]. Furthermore, the
error becomes smaller as the G,G; terms get closer to commuting and the scheme preserves the underlying structure of the
problem.

One should notice, at this point, that Eq. (346) (or, in the linear case, Eq. (350)), has formally the same structure as the
nonlinear ODE (171) appearing in control theory. Therefore, the formalism developed there to get the Chen-Fliess series can
be applied here with the alphabet I = {0, 1, ..., d} and the integrals

t t
(/ 1) (t) -|/ u(s)ds, ([«) (t) -|/ M(s)dWi(s), i= 1,
0 0 i 0

since the Stratonovich integrals satisfy the integration by parts rule. In other words, one can obtain the corresponding
Magnus expansion for arbitrary (linear or nonlinear) stochastic differential equations simply by following the same
procedure as for deterministic ODEs.

With respect to nonlinear Stratonovich stochastic differential equations, it should be remarked that the use of Lie
algebraic techniques, as well as the design of Lie group methods for obtaining strong approximations when the solution
evolves on a smooth manifold, has received considerable attention in the recent literature [201-203].
230 S. Blanes et al. / Physics Reports 470 (2009) 151-238
