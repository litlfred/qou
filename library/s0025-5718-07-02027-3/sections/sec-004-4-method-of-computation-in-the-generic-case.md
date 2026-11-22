---
doc_id: s0025-5718-07-02027-3
doc_title: "Li(p)-service? An algorithm for computing p-adic polylogarithms"
section_id: sec-004-4-method-of-computation-in-the-generic-case
section_title: "Method of computation in the generic case"
section_number: 4
pages: 6-8
source_pdf: S0025-5718-07-02027-3.pdf
source_sha256: 080b5ac8542ff19c
toc_source: outline
doc_brief: "Li(p)-service? An algorithm for computing p-adic polylogarithms — We describe an algorithm for computing Coleman’s p-adic poly- logarithms up to a given precision."
---
In this section we explain how to compute Lin(z) on all residue discs except U0,
U1 and U∞. The residue discs U0 and U∞were discussed in the previous section,
and U1 will be dealt with in Section 5.
We begin with a well known observation.
Proposition 4.1. Every residue disc other than U0 and U∞is Uζ for a unique
root of unity ζ of order dividing pf −1 for some f > 0, known as the Teichm¨uller
representative of this residue disc.
Proof. For the residue disc Ub the reduction ¯b satisﬁes ¯bpf −1 = 1 for some f > 0
because Ub̸ = U0 or U∞. Since Cp is complete we can apply Hensel’s lemma to lift
¯b to a unique solution of xpf −1 = 1 in Ub, which is ζ.
□
The key observation for the computation of Lin(z) is the following.
Proposition 4.2. Suppose that ζ̸ = 1 is a (pf −1)-th root of unity. Then
Lin(ζ) =

pnf −1
−1 
pnfLi(p)
n (ζ) + pn(f−1)Li(p)
n (ζp) + · · · + pnLi(p)
n (ζpf−1)

.
Proof. This formula is derived in [3] as part of the proof of Corollary 2.2 there. For
completeness, we recall the easy proof. For any z in Cp with zpk̸ = 1 we have
k−1

r=0
p−rnLi(p)
n (zpr) =
k−1

r=0
p−rn(Lin(zpr) −p−nLin(zpr+1)) = Lin(z) −p−nkLin(zpk)
since the second sum is telescopic. Setting z = ζ and k = f we have ζpf = ζ; hence
f−1

r=0
p−rnLi(p)
n (ζpr) = (1 −p−nf)Lin(ζ) = p−nf(pnf −1)Lin(ζ),
so
Lin(ζ) = (pnf −1)−1
f−1

r=0
pn(f−r)Li(p)
n (ζpr),
as required.
□
Proposition 4.2 implies that if we are able to compute Li(p)
n (z), then we can ﬁnd
Lin(z) at least for z = ζ. For this calculation we use a power series expansion of
Li(p)
n (z) around ∞as in the next result (but see also Remark 8.5). Then Proposi-
tion 4.4 below will show how to use the value of Lin(ζ) in order to compute Lin(z)
for z in Uζ.
Li(p)-SERVICE? AN ALGORITHM FOR p-ADIC POLYLOGARITHMS
1111
Proposition 4.3. We have Li(p)
n (z) = gn(1/(1 −z)) for a power series gn(v) in
Q[[v]], convergent for v in Cp with |v| < p1/(p−1). It is determined inductively by
g0(v) = v −1 −
(v −1)p
vp −(v −1)p ,
g′
n+1(v) = −gn(v)
v −v2 = −gn(v)
v
(1 + v + v2 + · · · )
(n ≥0) ,
and
gn(0) = 0
(n ≥1) .
Proof. By Theorem 2.7 we can write Li(p)
n (z) = gn(1/(1 −z)) with gn(v) a power
series that converges when |v| < p1/(p−1). To determine the relations satisﬁed by
the gn(v) we ﬁrst write u = 1−z and let fn(u) = Li(p)
n (1−u) for n ≥0. Using (2.5)
the equations in (2.6) become
f0(u) = 1 −u
u
−
(1 −u)p
1 −(1 −u)p
and
f ′
n+1(u) = −fn(u)
1 −u .
Next we set v = 1/u and let gn(v) = fn(1/v) to ﬁnd
g0(v) = v−1−
(v −1)p
vp −(v −1)p
and
g′
n+1(v) = −gn(v)
v −v2 = −gn(v)
v
(1+v+v2+· · · )
as required. We then have gn(0) = Li(p)
n (∞) = 0 for all n ≥0 by Theorem 2.7(3).
Clearly, these relations determine gn(v) inductively by integration. Because the
denominator vp−(v−1)p of g0(v) is a unit in Z[[v]] we see that g0(v) is in Z[[v]] and
hence that gn(v) is in Q[[v]] for n ≥1. Finally, we observe that v = 1/(1 −z).
□
Proposition 4.4. Let ζ̸ = 1 be a (pf −1)-th root of unity. For z in Uζ we have
that Lin(z) = Fn,ζ(z −ζ) for a power series Fn,ζ(t) with coeﬃcients in Qp(ζ). It
converges for |t| < 1 and can be found inductively by the formulae
F0,ζ(t) =
ζ + t
(1 −ζ) −t = (1 −ζ)−1

ζ +
t
1 −ζ +
t2
(1 −ζ)2 + · · ·

(4.5)
and, for n ≥0,
F ′
n+1,ζ(t) = Fn,ζ(t)
ζ + t
= ζ−1Fn,ζ(t)(1 −ζ−1t + ζ−2t2 −· · · )
(4.6)
as well as
Fn+1,ζ(0) = Lin+1(ζ) .
(4.7)
Proof. The fact that Lin(z) is rigid analytic on Uζ and therefore has a power series
expansion as above was stated in Theorem 2.7(1).
The ﬁrst two formulae are
immediate consequences of (2.4). Integration then determines Fn+1,ζ(t) for n ≥
0, except for its constant term, which is given by the last equation.
Since by
Proposition 4.3 Li(p)
n (ζ) is in Qp(ζ) the same holds for Lin(ζ) by Proposition 4.2.
The claim about the coeﬃcients is then clear from the inductive formulae.
□
For use in some of the estimates in the following sections we also prove a few
results about the absolute values of Li(p)
n (z) and Lin(z) (cf. [3]). Note that if |z| < 1,
then |Li(p)
n (z)| = |z| by (3.3).
1112
AMNON BESSER AND ROB DE JEU
Proposition 4.8. If z in Cp satisﬁes |z −1| = 1, then |Li(p)
Li(p)
n (z) =
Z∗
where µz is the measure on Zp such that µz(a + pkZp) =
za
Proof. We have that Li(p)
n (ζ)| ≤1 so that Li(p)
Corollary 4.10. If ζ is a root of unity of order pkm with m > 1 not divisible by
p, then |Lin(ζ)| ≤p(k−1)n.
n (ζ) and |Li(p)
