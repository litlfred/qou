---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-005-a-proof-of-magnus-theorem
section_title: "A proof of Magnus' Theorem"
section_number: null
pages: 9-11
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
The proof of this theorem is largely based on the derivative of the matrix exponential map, which we discuss next. Given
a scalar function w(t) € R, the derivative of the exponential is given by d exp(w(t))/dt = w'(t) exp(w(t)). One could think
of a similar formula for a matrix §2(t). However, this is not the case, since in general [§2, 2’] # 0. Instead, one has the
following result.

Lemma 2. The derivative of a matrix exponential can be written alternatively as

d

(a) a exp(2(t)) = d expe (2’(t)) exp(2(t)), (33)
d

(b) a exp(2(t)) = exp(2(t))d exp_an(2'(0)), (34)

d 1
(©) 4, exp(2(t) = | XO 2! (tet 2 dx, (35)
0
160 S. Blanes et al. / Physics Reports 470 (2009) 151-238

where d exp, (C) is defined by its (everywhere convergent) power series

_< 1 k _ exp(ade) — 1
dexpg(C) = > TT ad, (C) = ado (C). (36)

Proof. Let 2(t) be a matrix-valued differentiable function and set
a
Yo,th= ry: (exp(o 2 (t))) exp(—0 2(t))

foro, t € R. Differentiating with respect too,
oY
do

a a
vs (exp(o 2) 2) exp(—o 2) + Fy: (exp(o @)) (—@) exp(—o 2)

= (exn1o.2)2" + 2 (exp(o 22)) 2) exp(—o 2) — 2 (exp(o 2)) 2 exp(—o 2) = exp(o 2)Q’ exp(—o 2)

ioc] k

exp(ad,.o)(2") = » —ad'(2').
k=

where the first equality in the last line follows readily from (12) and (13). On the other hand

1
4 exp 92) exp(—2) = Y(1, t) = [ 8 ve, t)do (37)
dt 0 00

since Y(0, t) = 0, and

_ Kk _ = 1 k y
[ dv. t)do = [x Soo ad K (2')do = Dd er ite?

from which formula (33) follows. The convergence of the power series (36) is a consequence of the boundedness of the ad
operator: ||adg|| < 2||2|].
Multiplying both sides of (33) by exp(—2), we have
de? et-2 —]
~2_ = e- &dexpy(Q')e® = e*4-2d expy (Q’) = ————_ = dexp_o(2’)
dt ad_o

from which (34) follows readily. Finally, Eq. (35) is obtained by taking

15 1
| —Y(o,t)do -|/ exp(o 2)’ exp(—o 2)do
0 do 0

in(37).

According to Rossmann [46] and Sternberg [47], formula (33) was first proved by F. Schur in 1890 [48] and was taken up
later from a different point of view by Poincaré (1899), whereas the integral formulation (35) has been derived a number of
times in the physics literature [19].

As a consequence of the Inverse Function Theorem, the exponential map has a local inverse in the vicinity of a point 2
at which dexpg = (exp(adg) — I)/adg is invertible. The following lemma establishes when this takes place.

Lemma 3 (Baker 1905). If the eigenvalues of the linear operator adg are different from 2mmi withm € {+1,+2,...}, then
dexPg is invertible. Furthermore,

dexps'(C) = = “>i a Kad (C) (38)

and the convergence of the d expy' expansion is certainly assured if ||92|| < z.
Proof. The “igenvales of d expg are of the form
e’—1
HDD = plo

k>0

where v is an eigenvalue of adg. By assumption, the values of jz are non-zero, so that d expg is invertible. By definition
of the Bernoulli numbers, the composition of (38) with (36) gives the identity. Convergence for ||2|| < 2 follows from
\|Jadg|| < 2||2|| and from the fact that the radius of convergence of the series expansion for x/(e*— 1) is27.
S. Blanes et al. / Physics Reports 470 (2009) 151-238 161

It remains to determine the eigenvalues of the operator ada. In fact, it is not difficult to show that if $2 has n eigenvalues
{aj, j= 1,2,...,n}, then adg has rn? eigenvalues {Aj — Ak, j,k = 1,2,..., nj.
As a consequence of the previous discussion, Theorem 1 can be rephrased more precisely in the following terms.

Theorem 4. The solution of the differential equation Y' = A(t)Y with initial condition Y(0) = Yo can be written as Y(t) =
exp({2(t))Yo with 2(t) defined by

Q! = dexpy'(A(t)), 2(0) =O, (39)
where
© B,
dexp,'(A) = )- —ad' (A).
exp’ (A) > pide)

Proof. Comparing the derivative of Y(t) = exp(2(t))Yo,
dy
dt

with Y’ = A(t)Y, we obtain A(t) = d exp, (2’). Applying the inverse operator d exp! to this relation yields the differential

equation (39) for Q(t).

d
=a (exp(2(t))) Yo = d expo (2’) exp(2(t))Yo

Taking into account the numerical values of the first few Bernoulli numbers, the differential equation (39) therefore
becomes

1 1
2! = A(t) — 3 l2. AI + pl? [2, A(t)]] +--+,
which is nonlinear in Q. By defining
t
e2=0, a= [ A(ty)dty,
0
and applying Picard fixed point iteration, one gets
‘ 1 1
a= | A= fal" alt —[alh' pal" aly +--+) dtr
0 2 12
and lim,_... @!"!(t) = Q(t) ina suitably small neighborhood of the origin.
