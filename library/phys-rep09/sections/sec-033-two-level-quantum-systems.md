---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-033-two-level-quantum-systems
section_title: "Two-level quantum systems"
section_number: null
pages: 39-43
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
The generic Hamiltonian for a two-level quantum system can be written down in the form

no=(2 2) ow

where E;(t), E2(t) are real functions and C(t) is, in general, a complex function of t. We define the solvable piece of the
Hamiltonian as the diagonal matrix

Holt) = (0° Eo) (190)

and all the time-dependent interaction described by the function C(t) is considered as a perturbation. In the Interaction
Picture, the new Hamiltonian reads (see (92))

t

0 C(t) exp (if
0

C*(t) exp (-i[ av'ott)) 0
0

with w = (E; — E2)/h. Suppose now that Hp is time-independent. Then U(t) = exp(Hot)U; (t). Without loss of generality,
the Ho may be rendered traceless, so that E,) = —E, = E. Thus +E denote the eigenenergies associated to the eigenvectors

av'wtt))

A(t) = (191)
190 S. Blanes et al. / Physics Reports 470 (2009) 151-238

|+) = (1, 0)", |—) = (0, 1)" of Ho, the unperturbed system. In terms of Pauli matrices the Hamiltonian in this case may be
expressed as

1
H(t) = ghoos +f(t)or +g (to, (192)

where f = Re(C) and g = —Im(C).
Since Hp is diagonal, the transition probability between eigenstates |+), |—) of Ho is simply
P(t) = (H1U(0)|-)’. (193)

As the evaluation of (193) requires the computation and manipulation of exponential matrices involving Pauli matrices,
formulas (18) and (19) in Section 1.2 come in handy here.

Next, we study two particular cases of interaction for which the exact solution of the time evolution operator admits an
analytic expression.

1- Rectangular step. Suppose that in (192) g = 0, namely,

H(t) = shes +f(t)or (194)

with f = 0 fort < Oandf = Vo fort > 0. Alternatively, if we restrict ourselves to compute an observable such as the
transition probability, this example is equivalent to a rectangular mound (or rectangular barrier) of width T = t above. The
exact solution for this problem reads

vi
U(t, 0) = exp (- (Sa + pa) ‘) . (195)

which yields the exact transition probability
ay

ae ae (196)

between eigenstates |+), |—) of Ho. Here we have denoted y = Vot/h and é = at.
The Interaction Picture is defined here by the explicit integration of the diagonal piece in the Hamiltonian, so that
U = exp(—iéo3/2)U), where U; stands for the time evolution operator in the Interaction Picture and obeys

2

Pex

Ul) =HA,(t)U;, U0) =1 (197)
with
H(t) =f (t)(o1 cosé — 02 sin€). (198)
A computation with the usual time-dependent perturbation theory gives for the first orders (formula (52))

2

4y* |
Py = Py) = ro sin?(é/2) (199)
2 2 2
Y _€§ Y _€§ 3g g 3 §
P® — p® — —_ | asin — — (9sin= +sin = — 6£ cos= + 4sin?=)] .
pt pt f2 2 362 2 2 & 2 2

Notice that pe > 1 may happen in the equations above because the unitary character of the operator U(t) is not preserved
by the usual time-dependent perturbation formalism.

In this example it is not difficult to compute the first four terms in the Magnus series corresponding to U;(t) = exp 92(t)
in (197). To facilitate the notation, we define s = sin€ and c = cosé. The Magnus approximants in the Interaction Picture
may be written down in terms of Pauli matrices and read explicitly

2 =-iXos+n(1—ol

2
%=~i( ) o3(s — &)

3
2 =-i( ) Floil3EC1 +0) — G + 0)s] + oxlGE —3)s— 40-1

24 =~i(

wr |S

wr |S

4
) foal(de + 5) ~ (C+ 8)s). (200)

wr
S. Blanes et al. / Physics Reports 470 (2009) 151-238 191

Exact

— -— = Magnus-1
ames f Magnus-2
—-—-= Magnus-3
meres Magnus-4
—=— Pert.-1.2
—A— Pert.-3.4

Transition Probability (y=1.5)

0.0 T T

Fig. 3. Rectangular step: Transition probabilities as a function of €, with y = 1.5. The solid line corresponds to the exact result (196). Broken lines stand
for approximations obtained via ME, and lines with symbols correspond to perturbation theory, according to the legend. Computations up to fourth order,
in the Interaction Picture.

Exact

— — — Magnus-1

z

S = Magnus-3
2

FA »»* Magnus-4
$s —=— Pert.-1.2
a

c —A— Pert.-3.4
g

A

4

£

ec

Fig. 4. Rectangular step: Transition probabilities as a function of &, with y = 2. Lines are coded as in Fig. 3. Computations up to fourth order, in the
Interaction Picture.

The first two formulae for the approximate transition probabilities are, respectively

PP = sin? (= siné/2))
2 gin2 2
(2) - “ sin2(E/2), A= [4sin2(E/2) + easing ery? (201)

We omit explicit expressions for Pe and po since they are quite involved. However, we include their outputs in Figs. 3-5,
where we plot the first to fourth order approximate transition probabilities with ME in the Interaction Picture and compare
them to the exact case, and also with perturbation theory outputs. In Figs. 3 and 4 we set y = 1.5 and y = 2 respectively,
whereas in Fig. 5 we fix € = 1.

We observe that for the Magnus expansion in the Interaction Picture, the smaller the value of the parameter é, the better
the approximate solution works. As a matter of fact, in the sudden limit, « 1, ME furnishes the exact result; unlike
perturbation theory. As far as the intensity of the perturbation y increases, the quality of the approximations spoils. This
effect is much more dramatic for the standard perturbation theory.
192 S. Blanes et al. / Physics Reports 470 (2009) 151-238

1.0
08 5 |

e /

ty

2 064 ii

Fs i k

2 yy Exact \ \\,

= \ Ay

= 04 — — = Magnus-1 YVAN

§ 04- \ AEN

2 \ Ny

a | me cores Magnus-2 .

2 \ N\'\

£ —-—- Magnus-3 \ \A
0.2 4 - ~ Magnus-4 \ oh

‘ Sy
a Pert-1.2 ‘\ i N
—A— Pert-3.4 wo NS
00 4 1 ; yw
0 1 2 3
Y

Fig. 5. Rectangular step: Transition probabilities as a function of y, with € = 1. Lines are coded as in Fig. 3. Computations up to fourth order, in the
Interaction Picture.

On the other hand, it is clear from (198) that
t t
il Hi (t1)\l2 dt, =/ If (t)| dt: = Vot,
—oo )

whence Soo |Ar(ty) ll2 dt, = y, and thus Theorem 9 guarantees that the Magnus expansion in the Interaction Picture is
convergent if y < z. Notice that this is always the case for the parameters considered in Figs. 3-5. The estimate y < 7
for the convergence domain in the Interaction Picture should be compared with the corresponding one in the Schrédinger
picture:

to) 2
il W(t)ledt, = /y24+ © <m.
0 4

Notice then that, as pointed out in Section 2.9, a change of picture allows us to improve the convergence of the Magnus
expansion.
2- Hyperbolic secant step: Rosen-Zener model. In the Rosen-Zener Hamiltonian [121] the interaction C(t) in (189) is given
by the real function V(t) = Vo sech(t/T), where T determines the time-scale. We will use the notation y = mVoT/h and
& = oT = 2ET/h.

The corresponding Hamiltonian in terms of Pauli matrices is

H(t) = Eo3+ V(t)o; =a(t)-o, V(t) = Vo/cosh(t/T), (202)
with a = (V(t), 0, E). In the Interaction Picture one has
H,(s) = V(s)(o cos(&s) — o2 sin(&s)) (203)

in terms of the dimensionless time-variable s = t/T. Notice that € measures the ratio between the interaction time T and
the internal time of the system f/2E. From (203), and after straightforward calculation, the first and second ME operators
are readily obtained.

The exact result for the transition probability (provided the time interval extends from —oo to +00), as well as
perturbation theory and Magnus expansion up to second order read [15]

sin’ y
cosh? (sé /2)
2
pO — p@ _ Y
pe PE cosh? (st  /2)

= sin’[y/ cosh(ré /2)]
2

ex =

as
ll

_ sin? a y
42> cosh2(ré /2)

_ 1 vere]? ok H1
=7 arm ca + 86 = 85) ee

(204)
S. Blanes et al. / Physics Reports 470 (2009) 151-238 193

1.0 =
~
STN \
‘* ‘ Exact
“ \ \

os . \ \ — — — Magnus-1
gq
L
5 06-4
2
5
©
a
°
a 04-4
c
2
2
8
£ 024

0.0 T T T T

0.0 0.3 0.6 0.9 1.2 15

g

Fig. 6. Rosen-Zener model: Transition probabilities (204) as a function of €, with y = 1.5. The solid line stands for the exact result. Broken lines stand
for approximations obtained via ME, and triangles correspond to perturbation theory, according to the legend. Computations up to second order, in the
Interaction Picture.

1.0 T 7 N
7 N
} «.., “sy
J : \
= 08 | pc a i
S T L, \ x
& Ty \
2 06-4 7 4 \
5 Y : \
3 :
8 Ty : \
a ou i i \
& . y Exact i" \
b= . x
5 — — — Magnus-1 ‘ \
r O25 YP rrr Magnus-2 1 \
—v— Pert-1.2 i,
0.0 T T .
0 1 2 3
ey,

Fig. 7. Rosen-Zener model: Transition probabilities as a function of y, with € = 0.3. Lines are coded as in Fig. 6. Computations up to second order, in the
Interaction Picture.

In Figs. 6 and 7 we plot some results from the formulae in (204). In Fig. 6 we take y = 1.5 and in Fig. 7 we set € = 0.3.

Similarly to the case of the rectangular step, we observe in Fig. 6 that the Magnus expansion works better in the sudden
regime defined by  < 1, namely, when the internal time of the system f/2E is much larger than the time scale T of the
perturbation. Also, Fig. 7 illustrates how the approximations spoil as far as the intensity y increases. Notice, in both figures,
the unitarity violation of the approximation built with the usual perturbation theory.

In this case, a simple calculation shows that

co oo
il Hi (0) lla dt = alm [ |V(t)| dt = VorT/h= y,
—00 —oo
and thus the Magnus series converges at least for y < 7.
