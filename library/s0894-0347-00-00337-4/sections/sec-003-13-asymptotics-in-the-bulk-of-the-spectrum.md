---
doc_id: s0894-0347-00-00337-4
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4"
section_id: sec-003-13-asymptotics-in-the-bulk-of-the-spectrum
section_title: "Asymptotics in the bulk of the spectrum"
section_number: 1.3
pages: 4-6
source_pdf: S0894-0347-00-00337-4.pdf
source_sha256: 1c6848281fc2804c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4 — 22 sections: Front matter; Plancherel measures; Introduction"
---
1.3. Asymptotics in the bulk of the spectrum. Given a sequence of subsets
X(n) = {x1(n) < · · · < xs(n)} ⊂Z ,
where s = |X(n)| is some ﬁxed integer, we call this sequence regular if the limits
ai = lim
n→∞
xi(n)
√n ,
(1.10)
dij = lim
n→∞(xi(n) −xj(n))
(1.11)
exist, ﬁnite or inﬁnite.
Here i, j = 1, . . . , s.
Observe that if dij is ﬁnite, then
dij = xi(n) −xj(n) for n ≫0.
ASYMPTOTICS OF PLANCHEREL MEASURES
485
In the case when X(n) can be represented as X(n) = X′(n) ∪X′′(n) and the
distance between X′(n) and X′′(n) goes to ∞as n →∞we shall say that the
sequence splits; otherwise, we call it nonsplit. Obviously, X(n) is nonsplit if and
only if all xi(n) stay at a ﬁnite distance from each other.
Deﬁne the correlation functions ϱ(n, · ) of the measures Mn by the same rule as
in (1.4):
ϱ(n, X) = Mn ({λ | X ⊂D(λ)}) .
We are interested in the limit of ϱ(n, X(n)) as n →∞. This limit will be computed
in Theorem 3 below. As we shall see, if X(n) splits, then the limit correlations factor
accordingly.
Introduce the following discrete sine kernel which is a translation invariant kernel
on the lattice Z,
S(k, l; a) = S(k −l, a) ,
k, l ∈Z ,
depending on a real parameter a:
S(k, a) = sin(arccos(a/2) · k)
πk
,
k ∈Z .
Note that S(k, a) = S(−k, a) and for k ≥1 we have
S(k, a) =
√
4 −a2
2π
Uk−1(a/2)
k
,
where Uk is the Tchebyshev polynomials of the second kind. We agree that
S(0, a) = arccos(a/2)
π
,
S(∞, a) = 0
and also that
S(k, a) =
(
0 ,
a ≥2 or a ≤−2 and k̸ = 0 ,
1 ,
a ≤−2 and k = 0 .
The following result describes the local structure of a Plancherel typical partition.
Theorem 3. Let X(n) ⊂Z be a regular sequence and let the numbers ai, dij be
deﬁned by (1.10), (1.11). If X(n) splits, that is, if X(n) = X′(n) ∪X′′(n) and the
distance between X′(n) and X′′(n) goes to ∞as n →∞, then
lim
n→∞ϱ(n, X(n)) = lim
n→∞ϱ(n, X′(n)) · lim
n→∞ϱ(n, X′′(n)) .
(1.12)
If X(n) is nonsplit, then
lim
n→∞ϱ (n, X(n)) = det
h
S(dij, a)
i
1≤i,j≤s ,
(1.13)
where S is the discrete sine kernel and a = a1 = a2 = . . . .
We prove this theorem in Section 3.
Remark 1.4. Notice that, in particular, Theorem 3 implies that, as n →∞, the
shape of a typical partition λ near any point of the limit curve Ωis described by
a stationary random process. For distinct points on the curve Ωthese random
processes are independent.
486
A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
Remark 1.5. By complementation (see Sections A.3 and 3.2), one obtains from The-
orem 3 an equivalent statement about the asymptotics of the following correlation
functions:
ρ(n, X) = Mn ({λ | X ⊂Fr(λ)}) .
Remark 1.6. The discrete sine kernel was studied before (see [44, 45]), mainly as a
model case for the continuous sine kernel. In particular, the asymptotics of Toeplitz
determinants built from the discrete sine kernel was obtained by H. Widom [45]
who was answering a question of F. Dyson. We thank S. Kerov for pointing out
this reference.
Remark 1.7. Note that, in particular, Theorem 3 implies that the limit density (the
1-point correlation function) is given by
ϱ(∞, a) =





1
π arccos(a/2) ,
|a| ≤2 ,
0 ,
a > 2 ,
1 ,
a < −2 .
(1.14)
This is in agreement with the Logan-Shepp-Vershik-Kerov result about the limit
shape Ω. More concretely, the function Ωis related to the density (1.14) by
ϱ(∞, u) = 1 −Ω′(u)
2
,
which can be interpreted as follows. Approximately, we have
#

i

λi −i
√n
∈[u, u + ∆u]

≈√n ϱ(∞, u) ∆u .
Set w =
i
√n. Then the above relation reads ∆w ≈ϱ(∞, u) ∆u and it should be
satisﬁed on the boundary v = Ω(u) of the limit shape.
Since v = u + 2w, we
conclude that
ϱ(∞, u) ≈dw
du = 1 −Ω′
2
,
as was to be shown.
Remark 1.8. The discrete sine kernel S becomes especially nice near the diagonal,
that is, where a = 0. Indeed,
S(x, 0) =







1/2 ,
x = 0 ,
(−1)(x−1)/2.
(πx) ,
x = ±1, ±3, . . . ,
0 ,
x = ±2, ±4, . . . .
