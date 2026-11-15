---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-025-floquet--magnus-expansion
section_title: "Floquet--Magnus expansion"
section_number: null
pages: 29-30
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
We now turn our attention to a specific case of Eq. (30) with important physical and mathematical applications, namely
when the (complex) n x n matrix-valued function A(t) is periodic with period T. Then further information is available on
the structure of the exact solution, as is given by the celebrated Floquet theorem, which ensures the factorization of the
solution in a periodic part and a purely exponential factor. More specifically,

Y(t) = P(t) exp(tF), (125)
where F and P aren x n matrices, P(t) = P(t + T) for allt and F is constant. Thus, albeit a solution of (30) is not, in general,
periodic, the departure from periodicity is determined by (125). This result, when applied in quantum mechanics, is referred
to as Bloch wave theory [94,95]. It is widely used in problems of solid state physics where space-periodic potentials are quite
common. In Nuclear Magnetic Resonance, this structure is exploited as far as either time-dependent periodic magnetic fields
or sample spinning are involved [24]. Asymptotic stability of the solution Y(t) is dictated by the nature of the eigenvalues
of F, the so-called characteristic exponents of the original periodic system [96].

An alternative manner of interpreting Eq. (125) is to consider the piece P(t), provided it is invertible, to perform a
transformation of the solution in such a way that the coefficient matrix corresponding to the new representation has all
its matrix entries given by constants. Thus the piece exp(tF) in (125) may be considered as an exact solution of the system
(30) previously moved to a representation where the coefficient matrix is the constant matrix F [76]. The t-dependent
change of representation is carried out by P(t). Connecting with Section 2.9, P(t) is the appropriate preliminary linear
transformation for periodic systems. Of course, Floquet theorem by itself gives no practical information about this procedure.
It just states that such a representation does exist. In fact, a serious difficulty in the study of differential equations with
periodic coefficients is that no general method to compute either the matrix P(t) or the eigenvalues of F is known.

Mainly, two ways of exploiting the above structure of Y(t) are found in the literature [97]. The first one consists in
performing a Fourier expansion of the formal solution, leading to an infinite system of linear differential equations with
constant coefficients. Thus, the t-dependent finite system is replaced with a constant one at the price of handling infinite
dimension. Resolution of the truncated system furnishes an approximate solution. The second approach is of perturbative
nature. It deals directly with the form (125) by expanding

P(t)= J Pat) F= Fp. (126)
n=1 n=1

Every term F, in (126) is fixed so as to ensure P,(t) = P,(t +T), which in turn guarantees the Floquet structure (125) at any
order of approximation.

Although the Magnus expansion, such as it has been formulated in this work, does not explicitly provide the structure of
the solution ensured by Floquet theorem, it can be adapted, without special difficulty, to also cope with this situation. The
starting point is to introduce the Floquet form (125) into the differential equation Y’ = A(t)Y. In that way, the evolution
equation for P is obtained:

P'(t) = A(t)P(t) — P(t)F, — P(O) =I. (127)

The constant matrix F is also unknown and we will determine it so as to ensure P(t + T) = P(t). Now we replace the usual
perturbative scheme in Eq. (126) with the exponential ansatz

P(t) = exp(A(t)), A(0) = 0. (128)
Obviously, A(t + T) = A(t) so as to preserve periodicity. Now Eq. (127) conveys

d
a exp(A) = Aexp(A) — exp(A)F, (129)
from which, as with the conventional Magnus expansion, it follows readily that
2 B,
A= > rie (A+ (—1)*1F). (130)

This equation is now, in the Floquet context, the analogue of Magnus equation (39). Notice that if we put F = O then (39) is
recovered. The next move is to consider the series expansions for A and F

A(t) = SOA), F= OK, (131)
k=1 k=1

with A,(0) = O, for all k. Equating terms of the same order in (130) one gets the successive contributions to the series (131).
Therefore, the explicit ansatz we are propounding reads

Y(t) = exp ( a) exp (‘5) . (132)
1 k=1

k=
This can be properly referred as the Floquet-Magnus expansion.
180 S. Blanes et al. / Physics Reports 470 (2009) 151-238

Substituting the expansions of Eq. (131) into (130) and equating terms of the same order, one can write

n-1
A= 2 (WPO+AKDTTPO) Me). (133)

j=0 *°

The terms wY (t) may be obtained by a similar recurrence to that given in Eq. (49)

n-j
wo = [Am. Wien] (1<j<n-1),
P= Di [Aw Wren] sts (134)
w=a, W=0 Mm),
whereas the terms T(t) obey the recurrence relation
n-j
TY =o [Am Ton] A sisn—2,
: » mms Tom <is (135)

1 =F, (n> 0).
Every F, is fixed by the condition A,(t + T) = A,(t). An outstanding feature is that F, can be determined independently
of An(t) as the solution Y(t) = P(t) exp(tF) shrinks to Y(T) = exp(TF). Consequently, the conventional Magnus expansion
Y(t) = exp(2(t)) computed at t = T must furnish

F, = ont) for all n. (136)

The first contributions to the Floquet-Magnus expansion read, explicitly,

ao = f A(x)dx — tF;,
tat
Fi = al A(x)dx,
1 t
Az(t) = al [A(x) + Fi, Ai(x)] dx — tf, (137)
0

1 yt
R= xf [A(x) + Fi, A1(x)] dx.

Moreover, from the recurrence relations (134) and (135) it is possible to obtain a sufficient condition such that convergence
of the series }* A, is guaranteed in the whole interval t € [0, T] [34]. In fact, one can show that absolute convergence of
the Floquet-Magnus series is ensured at least if

T
| |A(t)I|dt < & = 0.20925. (138)
0

Notice that convergence of the series )~ F, is already guaranteed by (136) and the discussion concerning the conventional
Magnus expansion in Sections 2.7.2 and 2.7.3. The bound é; in the periodic Floquet case turns out to be smaller than
the corresponding bound r, = z in the conventional Magnus expansion. At first sight this could be understood as an
impoverishment of the result. However, it has to be recalled that, due precisely to Floquet theorem, once the condition
is fulfilled in one period, convergence is assured for any value of time. On the contrary, in the general Magnus case, the
bound always gives a running condition.
