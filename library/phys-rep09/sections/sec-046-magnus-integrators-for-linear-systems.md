---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-046-magnus-integrators-for-linear-systems
section_title: "Magnus integrators for linear systems"
section_number: null
pages: 53-56
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
Since the Magnus series only converges locally, as we have pointed out before, when the length of the time-integration
interval exceeds the bound provided by Theorem 9, and in the spirit of any numerical integration method, the usual
procedure consists of dividing the time interval [to, t;] into N steps such that the Magnus series converges in each subinterval
[tr—1. tn],n = 1,...,N, with ty = ty. In this way, the solution of (223) at the final time ty is represented by

N
¥ (tw) = | [ exp(2(ty, tn—1))Yo, (240)

n=1

and the series 92 (tn, ta_1) has to be appropriately truncated.

Early steps in this approach were taken in [21,130], where second and fourth order numerical schemes were used for
calculations of collisional inelasticity and potential scattering, respectively. Those authors were well aware that the resulting
integration method “would become practical only when the advantage of being able to use bigger step sizes outweighs the
disadvantage in having to evaluate the integrals involved in the Magnus series, and then doing the exponentiation” [130].
Later on, by following a similar approach, Devries [131] designed a numerical procedure for determining a fourth order
approximation to the propagator employed in the integration of the single channel Schrodinger equation, but it was in the
pioneering work [37] where Iserles and Norsett carried out the first systematic study of the Magnus expansion with the
aim of constructing numerical integration algorithms for linear problems. To design the new integrators, the explicit time
dependency of each term 2; had to be analyzed, in particular its order of approximation in time to the exact solution.

Generally speaking, the process of rendering the Magnus expansion, a practical numerical integration algorithm, involves
three steps. First, the 2 series is truncated at an appropriate order. Second, the multivariate integrals in the truncated series
Qirl = an Q; are replaced by conveniently chosen approximations. Third, the exponential of the matrix 2?! has to be
computed. We now briefly consider the first two issues, whereas the general problem of evaluating the matrix exponential
will be treated in Section 5.6.

We have shown in Section 2.6 that the Magnus expansion is time symmetric. As a consequence of Eq. (66), if A(t) is
analytic and one evaluates its Taylor series centered around the midpoint of a particular subinterval [t;, t, + h], then each
term in 2; is an odd function of h, and thus 22,4; = @(h?s+3) fors > 1. Equivalently, 2!5-2] = @ + @(h?5+") and
Qs = 2 + O(h?s+!), In other words, for achieving an integration method of order 2s (s > 1) only terms up to 25-2 in
the 2 series are required [37,39]. For this reason, in general, only even order methods are considered.

Once the series expansion is truncated up to an appropriate order, the multidimensional integrals involved have to be
computed or at least conveniently approximated. Although, at first glance, this seems to be a quite difficult enterprise, it
turns out that their very structure allows one to approximate all the multivariate integrals appearing in 2 just by evaluating
A(t) at the nodes of a univariate quadrature [37].

To illustrate how this task can be accomplished, let us expand the matrix A(t) around the midpoint, t1/2 = t, + h/2, of
the subinterval [tn, thi],

ee 1 A(t)
A(t) = > qj (t — tip)’ , where qj = ja
j=0 .

; (241)

t=t2

and insert the series (241) into the recurrence defining the Magnus expansion (49)-(50). In this way one gets, explicitly, the
expression of 2, up to order h® as

1 1
Q=h — ne n”
1 dg + pet ao t Ol )

-1 -1 1
22 = W®—[a, bh ( —[ap, —I(n, on”
2 D [ao, a4] + (= [do, a3] + Fa l™ a!) + O(n’)

1 1
23=1° (sepia do, a2] — 49h do, a) + 0(n’) (242)

1
24 = WF lao. do, do, 41] + O(N’),

whereas 25 = O(h’), 25 = O(h’) and 2; = O(h*), Here we write for clarity [aj,,4i,,...,4i_,. i]
[ai,, [ai,,[..-, [ai_,, ai,]...]]]. Notice that, as anticipated, only odd powers of h appear in £2 and, in particular, 22i+1
O(h74+3) fori > 1.

Let us denote a; = h'aj_,. Then [aj,, a), ... , &j_,, i] is an element of order h"'*”"*"!, In fact, the matrices {aj};>1 can be
considered as the generators (with grade i) of a graded free Lie algebra £(a1, a2, ...) [62]. It turns out that it is possible to
build methods of order p = 2s by considering only terms involving a1, ..., a; in 2. Then, these terms can be approximated
204 S. Blanes et al. / Physics Reports 470 (2009) 151-238

by appropriate linear combinations of the matrix A(t) evaluated at different points. In particular, up to order four, we have
to approximate

1
2 = on ~ lor, a2] + O(n), (243)
whereas, up to order six, the relevant expression is

1 1 1 1
Q=a —= a3 — —[Q4, a: =——[a2, a ——[11, a1, a
ita 3 lm 21 + saqlo2 al + sEple 1,3]

1 1
— 5p lea: 1, oa] + Fag let 1 a] + OCH”). (244)
In order to present methods which can be easily adapted for different quadrature rules, we introduce the averaged (or

generalized momentum) matrices

1 trth t 1 h/2
A (h) = al (t — t2) A(dt = al A(t + tr)dt (245)
W Sen Rn Jinja
fori = 0,...,s— 1. If their exact evaluation is not possible, or is computationally expensive, a numerical quadrature may
be used instead. Suppose that bj, c;, (i = 1,..., k), are the weights and nodes of a particular quadrature rule, say X (we will

use X = G for Gauss-Legendre quadratures and X = NC for Newton-Cotes quadratures) of order p, respectively [45],
tath k
AO = i] A(dt = h > bA, + O(HP*),
th i=1

with A; = A(t, + cjh). Then it is possible to approximate all the integrals A® (up to the required order) by using only the
evaluations A; at the nodes c; of the quadrature rule required to compute A. Specifically,

k i
1
AX =h)y (5-3) a i=0,...,s—1, (246)
jal

or equivalently, A® = hf, (a) A; with (a°”) =bj(G— 4).
ij ij
In particular, if fourth and sixth order Gauss-Legendre quadrature rules are considered, then for s = k = 2 we have [45]

1 1 V3 1, v3
bj =b=-, q=--—S, OQ=- —,
nr) 2 6 a= at
to order four, whereas for s = k = 3,
5 4 1 V15 1 1 V15
b, = b3 = —, by = -, q=--—, Q=-, GQ3=-+—,
mee 18 29 m2 4 a) 3= at 10
to order six, so that
5 4 5
1 1 1 9 18
(2,2) 2 2 (3,3) V15 V15
= , =|_ : (247)
ot ve wap 360° 36
1 1
12 12 Tog 1
24 24

Furthermore, substituting (241) into (245) we find (neglecting higher order terms)

s S.4—(-1iti

A= T) a = Y° a, 0<i<s-1. 248
dX yas » G+ pai oP (248)
If this relation is inverted (to order four, s = 2, and six, s = 3) one has
9
(2) @-1_(1 0 3) g 9 5
Res) =(5 bh): R"=!10 12 0 (249)

—-15 O- 180
S. Blanes et al. / Physics Reports 470 (2009) 151-238 205

respectively, so that the corresponding expression of q; in terms of A” or A; is given by

s

k
a; = > (R), Am? = hy (RQ) Ay (250)
j=l

jl

Thus, by virtue of (250) we can write $2(h) in terms of the univariate integrals (245) or in terms of any desired quadrature
tule. In this way, one gets the final numerical approximations to 2. Fourth and sixth-order methods can be obtained
by substituting in (243) and (244), respectively. The algorithm then provides an approximation for Y(t,,1) starting from
Yn © Y (tn), With tha. = th +h.

The observant reader surely has noticed that, up to order h°, there are more terms involved in (242) than those considered
in (243) or (244): specifically, 5% in (243) and wos and — alo. ot4] in (244). The reason is that 2'*! can be approximated
by A®, A, A® up to order h® and then, these omitted terms are automatically reproduced when either A®, A , A? are
evaluated analytically or are approximated by any symmetric quadrature rule of order six or higher.

Another important issue involved in any approximation based on the Magnus expansion is the number of commutators
appearing in £2. As is already evident from (242), this number rapidly increases with the order, and so it might constitute
a major factor in the overall computational cost of the resulting numerical methods. It is possible, however, to design an
optimization procedure aimed at reducing this number to a minimum [40]. For instance, a straightforward counting of
the number of commutators in (244) suggests that it seems necessary to compute seven commutators up to order six in h,
whereas the general analysis carried out in [40] shows that this can be done with only three commutators. More specifically,
the scheme

Ci = [1, a],
1

C= —Foler, 203 + Ci] (251)

1 1
Ql =a —a —[—-20a, — a: Cy, @& QQ],
nD at sal 1 3 +C1, a2 + G]

verifies that 2'°1 = 2 + @(h’). Three is, in fact, the minimum number of commutators required to get a sixth-order
approximation to 2.

This technique to reduce the number of commutators is, indeed, valid for any element in a graded free Lie algebra. It has
been used, in particular, to obtain approximations to the Baker-Campbell-Hausdorff formula up to a given order, with the
minimum number of commutators [132].

As an illustration, next we provide the relevant expressions for integration schemes of order 4 and 6, which readily follow
from the previous analysis.

Order 4. Choosing the Gauss—Legendre quadrature rule, one has to evaluate

1 V3 1. J3
w=a(ne(3-2)0), maa(ns ($2163), (252)

and thus, taking Q,° in (247), R® in (249) and substituting in (250) we find

h hV/3
a) = =(A, + Ap), 2 = ——(A2 — Aj). (253)
2 12
Then, by replacing in (243) we obtain
h V3
Qh) = (Ay + Az) — hb? Ai, A
(h) 36 1+ Aa) 1D! 1 Aa] (254)
Yn41 = exp(2!)(h)) Yn.
Alternatively, evaluating A at equispaced points, with k = 3 andc; = 0,c. = 1/2,c3 = 1; by = b3 = 1/6, b2 = 2/3
(i.e., using the Simpson rule to approximate , han A(s)ds),

h
A, =A(tn), A(t ;): A3 = A(t, + h)

we have instead a; = BAL + 4A) + A3), @2 = h(A3 — A), and then

h rn
24h) = am + 4A + A3) — wh + 4Ay + A3, Az — Ail. (255)
206 S. Blanes et al. / Physics Reports 470 (2009) 151-238

It should be noticed that other possibilities not directly obtainable from the previous analysis are equally valid. For instance,
one could consider

h h2
ah) = gi + 442 +43) — 55IAi. Al. (256)

Although apparently more A evaluations are necessary in (255) and (256), this is not actually the case, since A3 can be reused
at the next integration step.

Order 6. In terms of Gauss—Legendre collocation points, one has

1 J15 1 1. J15
A, =Alt, --~—)h), A =Al(th4+=-h), A=Alt, -~+——)h
1 («+(; 7) ) 2 (‘+ 5h) 3 («+ (3+ =) )

and similarly we obtain

V15h 10h
a; =hA, a = a As — AD, a3 = zy As — 2A +A), (257)
which are then inserted in (251) to get the approximation Y,,,; = exp(2"!)y,,.

If the matrix A(t) is only known at equispaced points, we can use the Newton-Cotes (NC) quadrature values with s = 3
and k = 5, b; = bs = 7/90, bz = ba = 32/90, b3 = 12/90 and c; = (j— 1)/4, j = 1, ..., 5. Then, using the corresponding

matrix Qe? from (246) we get
1
a= a0 (—7(A; + As) + 28(A2 + Ag) + 18A3)
1
m= TE (7(As — Ai) + 16(Aq — A2)) (258)

1
w= 3 (7(A; + As) — 4(Az + Ag) — 6A3) -

Both schemes involve the minimum number of commutators (three) and require three or four evaluations of the matrix A(t)
per integration step (observe that As can be reused in the next step in the Newton-Cotes implementation because c, = 0
and cs = 1).

Higher orders can be treated in a similar way. For instance, an 8th-order Magnus method can be obtained with only six
commutators [40]. Also variable step size techniques can be easily implemented [39,133].
