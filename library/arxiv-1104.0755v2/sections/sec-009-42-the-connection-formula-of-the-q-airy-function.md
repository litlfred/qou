---
doc_id: arxiv-1104.0755v2
doc_title: "A connection formula between the Ramanujan function and the q -Airy function"
section_id: sec-009-42-the-connection-formula-of-the-q-airy-function
section_title: "The connection formula of the q-Airy function"
section_number: 4.2
pages: 10-12
source_pdf: 1104.0755v2.pdf
source_sha256: d2fbbea44598e8f4
toc_source: outline
doc_brief: "A connection formula between the Ramanujan function and the q -Airy function — We show a connection formula between two diﬀerent q-Airy func- tions."
---
The connection formula of the q-Airy function
Applying the q-Borel transformation in 4.1 to the equation (7) and using
lemma 6, we obtain the ﬁrst order q-diﬀerence equation
g(qτ) = (1 + q2τ)(1 −q2τ)g(τ).
Since g(0) = 1, g(τ) is given by an inﬁnite product
g(τ) =
1
(−q2τ; q)∞(q2τ; q)∞
which has single poles at

τ; τ = ±q−2−k,
∀k ∈Z≥0
	
.
By Cauchy’s residue theorem, the q-Laplace transform of g(τ) is
f(t) = 1
2πi
Z
|τ|=r
g(τ)θ
 t
τ
 dτ
τ
= −
X
k≥0
Res

g(τ)θ
 t
τ
 1
τ ; τ = −q−2−k

−
X
k≥0
Res

g(τ)θ
 t
τ
 1
τ ; τ = q−2−k

where 0 < r < r0 := 1/|q2|. We can culculate the residue from lemma 7 and
lemma 2 .
Lemma 7 For any k ∈N, λ ∈C∗, one can get;
1. Res

1
(τ/λ; q)∞
1
τ : τ = λq−k

= (−1)k+1q
k(k+1)
2
(q; q)k(q; q)∞
,
2.
1
(λq−k; q)∞
=
(−λ)−kq
k(k+1)
2
(λ; q)∞(q/λ; q)k
,
λ̸ ∈qZ.
Summing up all of residues, we obtain
f(t) =
θ(q2t)
(q, −1; q)∞
1ϕ1

0, −q; q, 1
t

+
θ(−q2t)
(q, −1; q)∞
1ϕ1

0, −q; q, −1
t

.
Combining with lemma3, we get a connection formula for z(t) = E(t)f(t).
Finally, we acquire the following connection formula between the Ramanujan
function and the q-Airy function.
10
Theorem
For any x ∈C∗,
Aq2

−q3
x2

=
1
(q, −1; q)∞

θ
x
q

Aiq(−x) + θ

−x
q

Aiq(x)

.
Here, both Aq(x) and Aiq(x) are deﬁned by convergent series on whole of the
complex plain. The connection formula above is valid for any x ∈C∗.
Acknowledgement
The author express his thanks to Professor Yousuke Ohyama for his careful
conduct and kindly encouragement. The author also expresses his thanks to
Mr. Nobutaka Nakazono from Kyushu University for his valuable comments.
This work is partially supported by the Mitsubishi foundation.
References
[1] G. E. Andrews, Ramanujan’s ”lost” notebook. VIII: the entire Rogers-
Ramanujan function, Adv. Math.191 (2005), no. 2, 393-407.
[2] G. D. Birkhoﬀ, The generalized Riemann problem for linear diﬀerential
equations and the allied problems for linear diﬀerence and q-diﬀerence
equations, Proc. Am. Acad. Arts and Sciences, 49 (1914), 521 −568.
[3] G. Gasper and M. Rahman (1990). Basic Hypergeometric Series . En-
cycl. Math. Appl. Cambridge Univ. Press , Cambridge.
[4] W. Hahn, Beitr¨age zur Theorie der Heineschen Reihen. Die 24 Inte-
grale der Hypergeometrischen q-Diﬀerenzengleichung. Das q-Analogon
der Laplace-Transformation. Math. Nachr. 2, (1949). 340–379.
[5] T. Hamamoto, K. Kajiwara, N. S. Witte, Hypergeometric solutions to
the q-Painlev´e equation of type (A1 + A′
1)(1), Int. Math. Res. Not. Vol.
2006, Article ID 84619, Pages 1 −26.
[6] M. E. H. Ismail, Asymptotics of q-Orthogonal Polynomials and a q-Airy
Function, Int. Math. Res. Not. (2005), No. 18 1063–1088.
11
[7] K. Kajiwara, T. Masuda, M. Noumi, Y. Ohta, and Y. Yamada, Hyper-
geometric solutions to the q-Painlev´e equations, Int. Math. Res. Not.
(2004), no. 47, 2497–2521.
[8] Y. Ohyama A uniﬁed approach to q-special functions of the Laplace
type, arXiv:1103.5232.
[9] S. Ramanujan, The Lost Notebook and Other Unpublished Papers (In-
tro by G. E. Andrews), Narosa, New Delhi, 1988.
[10] R. F. Swarttouw and H. G. Meijer A q-analogue of the Wronskian and
a second solution of the Hahn-Exton q-Bessel diﬀerence equation Proc.
Am. Math. Soc. 129 (1994), 855–864.
[11] G. N. Watson, The continuation of functions deﬁned by generalized
hypergeometric series, Trans. Camb. Phil. Soc. 21 (1910), 281–299.
[12] C. Zhang, Remarks on some basic hypergeometric series, in “Theory
and Applications of Special Functions”, Springer (2005), 479–491.
[13] C. Zhang, Sur les fonctions q-Bessel de Jackson, J. Approx. Theory, 122
(2003), 208–223.
[14] C. Zhang, Une sommation discr`e pour des ´equations aux q-diﬀ´erences
lin´eaires et `a coeﬃcients, analytiques:
th´eorie g´en´erale et exemples,
in “Diﬀerential Equations and Stokes Phenomenon”, World Scientiﬁc
(2002), 309–329.
12
