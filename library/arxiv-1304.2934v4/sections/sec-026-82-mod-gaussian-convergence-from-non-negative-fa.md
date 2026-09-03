---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-026-82-mod-gaussian-convergence-from-non-negative-fa
section_title: "Mod-Gaussian convergence from non-negative factorizations"
section_number: 8.2
pages: 64-67
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
following statement, which is stronger than what was announced.
Theorem 8.1. Let (Xn)n∈N be a sequence of bounded random variables with non-negative
integer values, with mean µn, variance σ2
n and third cumulant L3
n. Suppose that the probability
generating function Pn(t) of Xn can be factorized as
Pn(t) = ∏
1≤j≤kn
Pn,j(t), (37)
where
• (kn)n∈N is a sequence of positive integers;
• each Pn,j is a polynomial with non-negative coefﬁcients;
• we assume Ln = o(σn) and Mn = o((Ln)2/σn), where Mn = max1≤j≤kn deg(Pn,j).
Then, the sequence
~Xn = Xn− µn
Ln
converges in the mod-Gaussian sense with limiting function ψ = exp(z3/6) and parameters
tn = σ2
n/L2
n. The convergence takes place of the whole complex plane, with speed of convergence
O(Mn/|Ln|).
MOD-φ CONVERGENCE, I 65
Notice that under the hypotheses of Theorem 8.1, Mn = o(|Ln|): indeed,
Mn≪ (Ln)2
σn
=|Ln||Ln|
σn
≪| Ln|
since Ln = o(σn). On the other hand, in the case where Pn has only real negative roots
−rn,j, then
Pn(t) = C ∏
1≤j≤n
(t + rn,j).
Therefore, we can then apply the above theorem withkn = n and Mn = 1. Besides, our
theorem also contains mod-Gaussian convergence of a sum of i.i.d. bounded variables
with a non-zero third cumulant (see Example 2.2).
Proof. Since Pn(1) = ∏1≤j≤kn Pn,j(1) = 1, we have
Pn(t) = ∏
1≤j≤kn
Pn,j(t)
Pn,j(1).
Therefore, we can assume without loss of generality that Pn,j(1) = 1 (otherwise re-
place Pn,j(t) by Pn,j(t)/Pn,j(1)). Since Pn,j(t) has non-negative coefﬁcients, Pn,j(t) is
the probability generating function of a variable Xn,j (for 1 ≤ j ≤ kn), deﬁned by
P[Xn,j = k] = [ tk]Pn,j(t).
The factorization (37) implies that Xn can be represented as the sum of independent
copies of the variables Xn,j. In particular,
µn = ∑
1≤j≤kn
µn,j;
σ2
n = ∑
1≤j≤kn
σ2
n,j;
L3
n = ∑
1≤j≤kn
L3
n,j
where µn,j, σ2
n,j and L3
n,j are the three ﬁrst cumulants of Xn,j. Notice that each Xn,j, and
hence|Xn,j− µn,j| is bounded by Mn. We will use this repeatedly below. In particular
one has: σ2
n,j≤ (Mn)2 and|L3
n,j|≤ (Mn)3.
Call~ϕn the Laplace transform of~Xn. We have
~ϕn(z) = E
[
exp
( z
Ln
(Xn− µn)
)]
=
kn
∏
j=1
E
[
exp
( z
Ln
(Xn,j− µn,j)
)]
.
Fix K > 0 and assume that Mn|z|
|Ln| ≤ K. From the Taylor expansion
ew = 1 + w + w2
2 + w3
6 + O(w4) (uniformly for|w|≤ K),
66 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
we have that, uniformly for Mn|z|
|Ln| ≤ K,
E
[
exp
( z
Ln
(Xn,j− µn,j)
)]
= 1 +
σ2
n,j z2
2 (Ln)2 +
L3
n,j z3
6 (Ln)3 + O
(
E[(Xn,j− µn,j)4]
(|z|
|Ln|
)4)
.
(38)
Note that, since Mn|z|/|Ln|≤ K, the two ﬁrst terms are bounded. Besides, we have
the following bounds:
⏐⏐⏐⏐⏐⏐
( σ2
n,j z2
2 (Ln)2
)2⏐⏐⏐⏐⏐⏐
≤ E[(Xn,j− µn,j)4]
4
(|z|
|Ln|
)4
;
⏐⏐⏐⏐⏐
σ2
n,j z2
2 (Ln)2×
L3
n,j z3
6 (Ln)3
⏐⏐⏐⏐⏐≤ E[|Xn,j− µn,j|5]
12
(|z|
|Ln|
)5
≤ E[(Xn,j− µn,j)4]
12
(|z|
|Ln|
)4 Mn|z|
|Ln| ;
⏐⏐⏐⏐⏐⏐
( L3
n,j z3
6 (Ln)3
)2⏐⏐⏐⏐⏐⏐
≤ E[(Xn,j− µn,j)6]
36
(|z|
|Ln|
)6
≤ E[(Xn,j− µn,j)4]
36
(|z|
|Ln|
)4( Mn|z|
|Ln|
)2
.
Taking the logarithm of Equation (38) and using log(1 + t) = t + O(t2), we get, thanks
to the above bounds, that
log E
[
exp
( z
Ln
(Xn,j− µn,j)
)]
=
σ2
n,j z2
2 (Ln)2 +
L3
n,j z3
6 (Ln)3 + O
(
E[(Xn,j− µn,j)4]
(|z|
|Ln|
)4)
.
Summing these identities, we obtain
log~ϕn(z) =
( σn
Ln
)2 z2
2 + z3
6 + O
((|z|
|Ln|
)4 kn
∑
j=1
E[(Xn,j− µn,j)4]
)
.
The error term can be bounded as follows:
(|z|
|Ln|
)4 kn
∑
j=1
E[(Xn,j− µn,j)4]≤
(|z|
|Ln|
)4
(Mn)2
kn
∑
j=1
E[(Xn,j− µn,j)2]≤| z|4 (Mn)2(σn)2
|Ln|4 .
By the assumption made on Mn, this is a o(|z|4). Finally, we get
log~ϕn(z) =
( σn
Ln
)2 z2
2 + z3
6 + o(|z|4),
which can be rewritten as
~ϕn(z) e−( σn
Ln )
2 z2
2 = exp
(z3
6
)(
1 + o(|z|4)
)
,
this being uniform for Mn|z|/|Ln|≤ K, thus on compacts of C. This ends the proof of
the theorem. □
MOD-φ CONVERGENCE, I 67
Remark 8.2. Suppose for instance that Mn = 1, i.e., the probability generating function
of Xn has non-negative real roots. Then, the conditions on the ﬁrst cumulants of Xn in
order to apply Theorem 8.1 are
√σn≪ Ln≪ σn,
which are usually easy to check.
