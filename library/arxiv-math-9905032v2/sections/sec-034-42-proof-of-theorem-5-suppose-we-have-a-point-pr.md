---
doc_id: arxiv-math-9905032v2
doc_title: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS"
section_id: sec-034-42-proof-of-theorem-5-suppose-we-have-a-point-pr
section_title: "Proof of Theorem 5. Suppose we have a point process on R"
section_number: 4.2
pages: 26-28
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
doc_brief: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
with determinantal correlation functions
ρk(x1, . . . , xk) = det[ K(xi, xj)]1≤i,j ≤k ,
for some kernel K(x, y). Let I be a possibly inﬁnite interval I ⊂ R.
By [ K]I we denote the operator in L2(I, dx) obtained by restricting
the kernel on I × I. Assume [ K]I is a trace class operator. Then
the intersection of the random conﬁguration X with I is ﬁnite almost
surely and
Prob{|X ∩ I| = N} = dN
dzN det
(
1 − z[K]I
)⏐
⏐
⏐
⏐
z=1
.
In particular, the probability that X ∩ I is empty is equal to
Prob{X ∩ I = ∅} = det
(
1 − [K]I
)
.
More generally, if I1, . . . , Im is a ﬁnite family of pairwise noninter-
secting intervals such that the operators [ K]I1, . . . ,[K]Im are trace class
then
(4.2) Prob {|X ∩ I1| = N1, . . . ,|X ∩ Im| = Nm}
= ∂N1+···+Nm
∂z N1
1 . . . ∂zNm
m
det
(
1 − z1[K]I1 − · · · − zm[K]Im
)⏐
⏐
⏐
⏐
z1=···=zm=1
.
Here operators {[K]Ii} are considered to be acting in the same Hilbert
space, for example, in L2(I1 ⊔ I2, ⊔ · · · ⊔ Im, dx).
ASYMPTOTICS OF PLANCHEREL MEASURES 27
In case of intersecting intervals I1, . . . , Im, the probabilities
Prob{|X ∩ I1| = N1, . . . ,|X ∩ Im| = Nm}
are ﬁnite linear combinations of expressions of the form (4. 2). There-
fore, in order to show the convergence in distribution of poi nt processes
with determinantal correlation functions, it suﬃces to sho w the con-
vergence of expressions of the form (4.2).
The formula (4.2) is discussed, for example, in [33]. It rema ins valid
for processes on a lattice such as Z in which case the kernel K should
be an operator on ℓ2(Z).
As veriﬁed, for example, in Proposition A.11 in the Appendix , the
right-hand side of (4.2) is continuous in each [ K]Ii with respect to the
trace norm. We shall show that after a suitable embedding of ℓ2(Z)
inside L2(R) the kernel J(x, y; θ) converges to the Airy kernel A(x, y)
as θ → ∞.
Namely, we shall consider a family of embeddings ℓ2(Z) → L2(R),
indexed by a positive number r > 0, which are deﬁned by
ℓ2(Z) ∋ χk ↦→r1/ 6 χ[
k−2r
r1/ 3 , k+1−2r
r1/ 3
] ∈ L2(R) , k ∈ Z ,(4.3)
where χk ∈ ℓ2(Z) is the characteristic function of the point k ∈ Z and,
similarly, the function on the right is the characteristic f unction of a
segment of length r−1/ 3. Observe that this embedding is isometric.
Let Jr denote the kernel on R × R that is obtained from the kernel
J( · , · , r2) on Z × Z using the embedding (4.3). We shall establish the
following
Proposition 4.3. We have
[Jr][a, ∞) → [A][a, ∞) , r → ∞ ,
in the trace norm for all a ∈ R uniformly on compact sets in a.
This proposition immediately implies Theorem 5 as follows
Proof of Theorem 5. Consider the left-hand side of (4.1) and choose
for each ai a pair of functions k−
i (r), k+
i (r) ∈ Z such that
k−
i (r) − 2r
r1/ 3 = a−
i (r) ≤ ai ≤ a+
i (r) = k+
i (r) − 2r
r1/ 3
and a−
i (r), a+
i (r) → ai as r → ∞. Then, on the one hand, the probabil-
ity in left-hand side of (4.1) lies between the correspondin g probabilities
for a−
i (r) and a+
i (r). On the other hand, the probabilities for a−
i (r) and
a+
i (r) can be expressed in the form (4.2) for the kernel Jr and by Propo-
sitions 4.3 and continuity of the Airy kernel they converge t o one and
same limit given by the Airy kernel as r → ∞.
