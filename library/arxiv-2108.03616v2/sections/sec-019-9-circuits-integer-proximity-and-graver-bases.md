---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-019-9-circuits-integer-proximity-and-graver-bases
section_title: "Circuits, integer proximity, and Graver bases"
section_number: 9
pages: 36-37
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
We now brieﬂy discuss implications of circuit imbalances to the integer program (IP) of the form
min⟨c,x⟩
Ax =b
x≥ 0,
x∈ Zn.
(IP)
Many algorithms for ( IP) solve the LP-relaxation ﬁrst and deduce from the optimal so lution
of the relaxation information about the IP itself. The follo wing proximity lemma shows that in
case that ( IP) is feasible, the distance of an optimal integral solution t o the optimal solution
of the relaxation can be bounded in terms of max-circuit imba lance ¯κA. So, a local search
within a radius of this guaranteed proximity will provide th e optimal solution for the IP; see
[Lee89, Proposition 4.1].
Lemma 9.1. Letx∗ be an optimal solution to LP(A,b,c ). Then there exists an optimal solution
ˆx to (IP) such that ‖ˆx−x‖1≤n¯κW .
Proof. Let ˆx be an optimal solution to ( IP) that minimizes‖ˆx−x∗‖1 and considerw =x∗−ˆx∈W
and a conformal circuit decomposition w = ∑ k
i=1λigCi for some k≤n and circuits C1,...,C k
andλ1,...,λ k≥ 0. Then,
⟨
c,gCi
⟩
≤ 0 for all i∈ [k] as otherwise x∗−λigCi would be a feasible
solution to the primal of LP(A,b,c ) with strictly better objective than x∗. Further, note that
λi≤ 1 for all i∈ [k] as otherwise ˆx−gCi is a feasible solution to ( IP) that has an objective as
least as good as ˆx and would in ℓ1 norm be strictly closer to x∗ than ˆx. Therefore,
‖ˆx−x∗‖∞≤
k∑
i=1
‖gCi‖∞≤n¯κW.
Another popular and well-studied quantity in integer progr amming is the Graver basis, de-
ﬁned as follows.
36
Deﬁnition 9.2 (Graver basis) . The Graver basis of a matrix A, denoted by G(A), consists of
all g∈ ker(A)∩ Zn such that there exists no h∈ (ker(A)∩ Zn)\{g} such that g and h are
conformal and|hi|≤| gi| for all i∈ [n]. We can further deﬁne
g1(A) := max
v∈G(A)
‖v‖1, g∞(A) := max
v∈G(A)
‖v‖∞. (28)
See [ LHK12] for extensive treatment of the Graver basis and [ EHK+19] for more recent
developments. Clearly, elementary vectors, scaled such th at its entries have greatest common
divisor equal to one belong to the Graver basis: {g∈F (W )∩ Zn : gcd(g) = 1}⊆G (A).
We will furthermore see how the max-circuit imbalance measu re and Graver basis are related.
Lemma 9.3. ¯κA≤ g∞(A)≤n¯κA.
Proof. The ﬁrst inequality follows from the paragraph above, notin g that
{
gC :C∈C (W )
}
⊆G (A),
for the normalized elementary vectors gC with lcm(gC ) = 1. For the second inequality, let
g∈G (A) and g = ∑ k
i=1λigCi be a conformal circuit decomposition where k≤ n. Note that
λi< 1 for all i∈ [k] as otherwise hi would contradict that g∈G (A). Therefore,
‖g‖∞≤
k∑
i=1
λi‖gCi‖∞≤n¯κA. (29)
Using the Steinitz lemma, Eisenbrand and Weismantel [ EHK18, Lemma 2] gave a bound on
g1(A) that only depends on m but is independent of n:
Theorem 9.4. LetA∈ Zm×n. Then g1(A)≤ (2m‖A‖max + 1)m.
