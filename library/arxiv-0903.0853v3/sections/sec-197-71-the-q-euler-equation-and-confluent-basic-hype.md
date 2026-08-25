---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-197-71-the-q-euler-equation-and-confluent-basic-hype
section_title: "THE q-EULER EQUATION AND CONFLUENT BASIC HYPERGEOMETRIC SERIES 117"
section_number: 7.1
pages: 123-124
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
Takinga :=b := 0 yields:
ˆf =
∑
n≥0
1
(q−1;q−1)n
qn(n+1)/2zn.
The recurrence relation un+1
un
= q2n+2
qn+1− 1 gives the homogeneous equation
q2zσ 2
qf−σqf +f = 0. The convergent solution is f0 := 1
zθq
g0, where g0 =
∑ γnzn∈ 1 +zC{z} is solution of the equation ( σ2
q−σq +qz)g = 0. The
corresponding recurrence relation ( q2n−qn)γn +qγn−1 = 0 can be solved
exactly and entails:
g0 =
∑
n≥0
(−1)nq−n2
(q−1;q−1)n
zn.
The corresponding factorisation is L =
(
σq− g0
σqg0
)(
qzσ q− σqg0
g0
)
. Follow-
ing [62] (3), one can prove the following formula for the Stokes operator s:
Sλ ˆf−Sµ ˆf = (q−1;q−1)2
∞
θq(−λ/µ)θq(z/λµ)
θq(−1/λ)θq(−1/µ)θq(λ/z)θq(z/µ)
∑
n∈Z
(−1)nq−n2
(q−1;q−1)n
zn.
We shall not attempt to prove this, but a similar formula is ch ecked in the
next case.
Takinga := 0,b :=q−1 yields:
ˆf =
∑
n≥0
qn(n+1)/2zn = Q(qz),
which is solution of the q-Euler equation (qzσ q− 1)f =−1. A solution of the
associated homogeneous equation is 1
θq(qz) = 1
θq(1/z), so that, for any two
λ,µ⁄∈[1;q] (authorized directions of summation):
Sλ ˆf−Sµ ˆf = K(λ,µ,z )
θq(1/z) ,
where K is q-invariant in each of the three arguments. We assume λ⁄= µ;
then, as a function of z, the numerator K is elliptic with simple zeroes over
[−1;q] and at most simple poles over [−λ;q] and [−µ;q]; thus:
K(λ,µ,z ) =K ′(λ,µ ) θq(1/z)θq(z/λµ)
θq(λ/z)θq(zµ) ,
3. Note that [ 21] contains similar formulas.
118 CHAPTER 7. EXAMPLES OF THE STOKES PHENOMENON
whereK ′(λ,µ ) is independent of z and, as a function of λ, has at most simple
poles over [1;q] and [µ;q]; thus:
K ′(λ,µ )θq(z/λµ)
θq(λ/z) =K ′′θq(z/λµ)θq(−λ/µ)
θq(λ/z)θq(−1/λ) ,
where K ′′ is independent of λ,µ,z . Last, we get:
Sλ ˆf−Sµ ˆf =C θq(−λ/µ)θq(z/λµ)
θq(−1/λ)θq(−1/µ)θq(λ/z)θq(z/µ)·
We shall now see that C =−θq′(−1) = ( q−1;q−1)3
∞. The second equality
follows immediately from Jacobi Triple Product Formula. Note that, by simple
singularity analysis, one may write:
Sλ ˆf =
∑
n∈Z
αn
z +λqn·
Since Sλ ˆf(0) = 1, we have ∑ αnq−n = λ. On the other hand, from the
functional equation, taking residues yields the recurrenc e relation: αn−1 =
−λαnqn−1, then αn = (−1/λ)nq−n(n−1)/2α0 and in the end:
λ =α0
∑
n∈Z
(−1/λ)nq−n(n−1)/2 =α0θq(−1/λ) =⇒α0 = λ
θq(−1/λ)·
On the other hand:
α0 = lim
z→−λ
(z +λ)(Sλ ˆf−Sµ ˆf)
= lim
z→−λ
(z +λ)C θq(−λ/µ)θq(z/λµ)
θq(−1/λ)θq(−1/µ)θq(λ/z)θq(z/µ)
=C 1
θq(−1/λ)
−λ
θq′(−1),
whence the desired conclusion.
