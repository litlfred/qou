---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum"
section_id: sec-006-32-integral-transformations
section_title: "Integral transformations"
section_number: 3.2
pages: 19-22
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual ˆA as a von Neumann algebra."
---
Here we describe several properties of the quantum dilogarithm inv olving integra-
tions.
Lemma 3.7. [2, (3.31), (3.32)] We have the following Fourier transform ation
formula:
∫
R+i0
e2πitr e−πit2
Gb(Q +it)dt =
¯ζb
Gb( Q
2−ir)
=gb(e2πbr), (3.24)
∫
R+i0
e2πitr e−πQt
Gb(Q +it)dt =ζbGb(Q
2−ir) = 1
gb(e2πbr) =g∗
b (e2πbr), (3.25)
where the contour goes above the pole at t = 0.
Using the reﬂection properties, we also obtain
∫
R+i0
e2πitreπQtGb(−it)dt =
¯ζb
Gb( Q
2−ir)
, (3.26)
∫
R+i0
e2πitreπit2
Gb(−it)dt =ζbGb(Q
2−ir), (3.27)
where again the contour goes above the pole at t = 0.
19
Lemma 3.8. [2, B.4] q-Binomial Theorem: For positive self-adjoint variables u,v
with uv =q2vu, we have:
(u +v)ib−1t =
∫
C
( it
iτ
)
b
uib−1(t−τ )vib−1τdτ, (3.28)
where the q-beta function (or q-binomial coeﬃcient) is given by
(
t
τ
)
b
= Gb(−τ )Gb(τ−t)
Gb(−t) , (3.29)
and C is the contour along R that goes above the pole at τ = 0 and below the pole
at τ =t.
Lemma 3.9. [32, Lem 15] We have the Tau-Beta Theorem:
∫
C
e−2πτ βGb(α +iτ )
Gb(Q +iτ )dτ = Gb(α)Gb(β)
Gb(α +β) , (3.30)
where the contour C goes along R and goes above the poles of Gb(Q +iτ ) and below
those of Gb(α +iτ ). By the asymptotic properties of Gb, the integral converges for
Re(β)> 0,Re (α +β)<Q .
Lemma 3.10. Rewriting the integral transform in [44] in terms of Gb, we obtain
the 4-5 relation given by:
∫
C
dτe −2πγτ Gb(α +iτ )Gb(β +iτ )
Gb(α +β +γ +iτ )Gb(Q +iτ ) = Gb(α)Gb(β)Gb(γ)
Gb(α +γ)Gb(β +γ), (3.31)
where the contour C goes along R and goes above the poles of the denominator, and
below the poles of the numerator. By the asymptotic properti es of Gb, the integral
converges for Re(γ)> 0.
An important corollary of Lemma 3.9 is the following:
Corollary 3.11. Letf (z)∈W (cf. Deﬁnition 2.23), then we have
lim
ǫ− →0
∫
C
Gb(Q−ǫ)Gb(iz)
Gb(Q +iz−ǫ) f (z)dz =f (0), (3.32)
where the contour go above the poles of the denominator and be low the poles of
the numerator. Alternatively, we can shift the poles so that the expression is an
integration over R:
lim
ǫ− →0
∫
R
Gb(Q− 2ǫ)Gb(iz +ǫ)
Gb(Q +iz−ǫ) f (z)dz =f (0). (3.33)
Formally as distribution,
Gb(Q)Gb(ix)
Gb(Q +ix) =δ(x), x ∈ R. (3.34)
20
Proof. By Lemma 3.9, we have
lim
ǫ− →0
∫
R
Gb(Q− 2ǫ)Gb(iz +ǫ)
Gb(Q +iz−ǫ) f (z)dz
= lim
ǫ− →0
∫
R
∫
C
e−2πτ (iz+ǫ)Gb(Q− 2ǫ +iτ )
Gb(Q +iτ ) f (z)dτdz,
where the contour C goes above the pole at τ = 0.
Now by Corollary 3.4, the integrand in τ has asymptotics
⏐
⏐
⏐
⏐e−2πτ ǫGb(Q− 2ǫ +iτ )
Gb(Q +iτ )
⏐
⏐
⏐
⏐∼
{ e−2πτ ǫ τ−→∞
e2πτ ǫ τ−→−∞ .
Hence the integrand is absolutely convergent in both τ and z. Hence we can inter-
change the integration order of τ and z,
= lim
ǫ− →0
∫
C
∫
R
e−2πτ (iz+ǫ)Gb(Q− 2ǫ +iτ )
Gb(Q +iτ ) f (z)dzdτ
= lim
ǫ− →0
∫
C
e−2πτ ǫGb(Q− 2ǫ +iτ )
Gb(Q +iτ ) (Ff )(τ )dτ,
whereF is the Fourier transform. Since f ∈ W,Ff ∈ W as well, hence the
integrand is absolutely convergent independent of ǫ. Hence we can interchange the
limit and ﬁnally obtain
=
∫
R
lim
ǫ− →0
e−2πτ (iz+ǫ)Gb(Q− 2ǫ +iτ )
Gb(Q +iτ ) (Ff )(τ )dτ
=
∫
R
(Ff )(τ )dτ
= f (0),
where the last line follows from the properties of Fourier transform .
Remark 3.12. This is just the analogue of the delta function as a hyperfunc tion.
Since the integrand is 0 unless z is close to 0, it suﬃces to notice that near z = 0 ,
from the analytic properties for Gb we have Gb(z)∼ 1
Gb(Q−z)∼ 1
2πz , so that
lim
ǫ− →0
Gb(Q− 2ǫ)Gb(iz +ǫ)
Gb(Q +iz−ǫ)
∼ lim
ǫ− →0
2ǫ
2πi(iz−ǫ)(iz +ǫ)
= lim
ǫ− →0
1
2πi
( 1
z−iǫ− 1
z +iǫ
)
= δ(z).
21
Intuitively, restricting to x∈ R, Gb(Q)Gb(ix)
Gb(Q+ix) is always 0 unless x = 0 , in which
case it is ∞. The properties of Gb say that it gives the right normalization to be a
delta function.
The other variants which we will also use include:
Corollary 3.13. Forf (x)∈W , we have
lim
ǫ− →0
∫
R
Gb(ǫ−ix)Gb(ǫ +ix)
Gb(2ǫ) f (x)dx = f (0), (3.35)
lim
ǫ− →0
∫
R
Gb(ǫ +ix−b)Gb(Q +b− 2ǫ)
Gb(Q +ix−ǫ) f (x)dx = −q2f (0) +f (−ib), (3.36)
or formally
Gb(−ix)Gb(ix)
Gb(0) = δ(x), (3.37)
Gb(ix−b)Gb(Q +b)
Gb(Q +ix) = −q2δ(x) +δ(x +ib), (3.38)
which follows from the functional properties of Gb(x) and similar arguments as
above.
A particular important case in the study of modular double (see the n ext sec-
tion) is proved in [2, Lem 3] and [44] which can also be obtained from the above
arguments:
Corollary 3.14. Let u,v be positive self-adjoint operators satisfying uv = q2vu.
By taking t−→−ib−1 in Lemma 3.8 we obtain
(u +v)1/b2
=u1/b2
+v1/b2
. (3.39)
