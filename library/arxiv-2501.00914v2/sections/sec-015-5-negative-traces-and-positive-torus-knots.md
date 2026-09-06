---
doc_id: arxiv-2501.00914v2
doc_title: "L-SPACES AND KNOT TRACES"
section_id: sec-015-5-negative-traces-and-positive-torus-knots
section_title: "Negative traces and positive torus knots"
section_number: 5
pages: 23-24
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
doc_brief: "L-SPACES AND KNOT TRACES — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
The goal of this section is to prove Theorem 1.5, which we restate here as follows:
Theorem 5.1.LetT p,q be a positive torus knot, and suppose for some knotK⊂S 3 and some
integern≤0thatX n(K)∼=Xn(Tp,q). ThenK=T p,q.
Forn= 0 this follows from Theorem 1.2, since positive torus knots are L-space knots. We prove
this theorem below, assuming some propositions which we will establish later in this section:
Proof of Theorem 5.1.Comparing the boundaries of the traces, we must haveS 3
n(K)∼= S3
n(Tp,q).
Thus if eitherKorT p,q is unknotted then the other one must be as well, because all slopes are
characterizing for the unknot [KMOS07]. From now on we assume that both knots are nontrivial,
and we observe that sinceTp,q is an L-space knot, Theorem 1.3 says thatKmust also be an L-space
knot – in particular, it is fibered [Ghi08, Ni07] – and thatg(K) =g(T p,q).
We know from geometrization for Haken manifolds thatKmust be either a torus knot, a satellite
knot, or a hyperbolic knot [Thu82, Corollary 2.5]. In each case, the identificationS 3
n(K)∼=S3
n(Tp,q)
will give us a contradiction:
•Proposition 5.2 says that ifK̸=T p,q is a torus knot, theng(K)̸=g(T p,q).
•Proposition 5.5 says that ifKis a satellite L-space knot, thenn≥2g(K)−1.
•Proposition 5.7 says that ifKis a hyperbolic L-space knot then 0<n<4g(K).
SinceKis indeed an L-space knot andg(K) =g(T p,q), this means that the only way we can have
Xn(K)∼=Xn(Tp,q) for anyn≤0 is ifK=T p,q.□
The following subsections are dedicated to the proofs of Propositions 5.2, 5.5, and 5.7.
5.1.Torus knots.It is possible for two different torus knots to have a common surgery; in Ap-
pendix A we will prove Theorem A.1, providing a two-parameter family of examples where the
resulting 3-manifold is always a lens space. However, in these examples we are about to show that
the torus knots in question cannot have the same Seifert genus, so Theorem 1.3 will tell us that
the corresponding traces must be different.
Proposition 5.2.Suppose for somer∈Qand some nontrivial torus knotsT a,b ̸=T c,d that
S3
r (Ta,b)∼=S3
r (Tc,d). Thenr̸= 0andg(T a,b)̸=g(T c,d).
Proof.LetA,B,C,Ddenote the absolute values ofa,b,c,dfor convenience. The caser= 0 is ruled
out by Lemma 2.11, so we will suppose thatr̸= 0; then we can apply the surgery formula for the
Casson–Walker invariant [Wal92], which says that
λ(S3
r (K)) =λ(S 3
r (U)) + 1
r
∆′′
K(1)
2 .
SinceS 3
r (Ta,b)∼=S3
r (Tc,d), it follows that
1
2∆′′
Ta,b(K) = 1
2∆′′
Tc,d(K).
These values are known explicitly: one can show as in, for example, [McC23, Appendix A] that
(5.1)
∆′′
Ta,b(1)
2 = (a2−1)(b 2−1)
24 =g(T a,b)· (A+ 1)(B+ 1)
12 ,
and likewise forT c,d.
24 JOHN A. BALDWIN AND STEVEN SIVEK
If we assume thatg(T a,b) =g(T c,d), then we get the system of equations
(A−1)(B−1) = (C−1)(D−1) (5.2)
(A+ 1)(B+ 1) = (C+ 1)(D+ 1) (5.3)
where (5.2) is equivalent to 2g(Ta,b) = 2g(Tc,d), and (5.3) comes from applying (5.1) to ∆ ′′
Ta,b(1) =
∆′′
Tc,d(1) and then dividing by (5.2). Subtracting (5.2) from (5.3) gives us
2(A+B) = 2(C+D),
soA+B=C+D, and if we add this to (5.2) then we getAB=CDas well. Now we have
{A,B}={C,D}, because these are the sets of roots of the quadratic polynomials
x2−(A+B)x+AB=x 2−(C+D)x+CD,
so it must be the case thatT c,d =T−a,b.
We have now shown that{T a,b,Tc,d}={T A,B,T−A,B}, and thus
S3
r (TA,B)∼=S3
r (T−A,B)∼=−S3
−r(TA,B).
The dimension of dHFis preserved by orientation reversal, so it follows that
(5.4) dim dHF(S 3
r (TA,B)) = dimdHF(S 3
−r(TA,B)).
SinceT A,B is an L-space knot of genusg=g(T a,b), we have
ˆr0(TA,B) = ˆν(TA,B) = 2g−1,
see e.g. [BS21, Remark 10.9]. Writingr=p/qfor coprime integersp,qwithp̸= 0 andq >0, we
apply Proposition 4.2 to (5.4) to see that
q(2g−1) +|p−q(2g−1)|=q(2g−1) +|−p−q(2g−1)|,
which simplifies to
p−q(2g−1) =±(p+q(2g−1)).
But this is only possible if eitherp= 0 orq= 0, and in either case we have a contradiction. Thus
we must have hadg(T a,b)̸=g(T c,d) after all.□
