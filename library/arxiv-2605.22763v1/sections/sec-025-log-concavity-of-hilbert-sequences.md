---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
section_id: sec-025-log-concavity-of-hilbert-sequences
section_title: "Log-Concavity of Hilbert Sequences"
section_number: null
pages: 51-57
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
toc_source: outline
doc_brief: "Advancing Mathematics Research with AI-Driven Formal Proof Search — 29 sections: Front matter; Introduction; AlphaProof Nexus"
---
Pure 𝑂-sequences, introduced in the context of Stanley’s work on Hilbert functions of mono-
mial level algebras in the late 1970s, have been studied intensively over the last fifteen years
[57]. They exhibit surprisingly strong positivity phenomena, especially in small codimension
and type. Although pure 𝑂-sequences are not log-concave in general, the case of codimension
3 and type 2 remained open for over a decade [9, 68]. The following theorem establishes
log-concavity in precisely this remaining case.
Theorem. Every pure 𝑂-sequence of codimension 3 and type 2 is log-concave.
Terminology. A monomial 𝑥𝑚(0)
0
𝑥𝑚(1)
1
𝑥𝑚(2)
2
in three variables is identified with its exponent
vector 𝑚= (𝑚(0), 𝑚(1), 𝑚(2)) ∈ℕ3. We write 𝑚′ ≤𝑚for coordinate-wise inequality and
|𝑚| = 𝑚(0) + 𝑚(1) + 𝑚(2) for total degree. A finite order ideal Γ ⊂ℕ3 is a finite set closed
downward under this order: if 𝑛∈Γ and 𝑚≤𝑛, then 𝑚∈Γ.
A monomial 𝑚∈Γ is maximal if every 𝑛∈Γ with 𝑚≤𝑛also satisfies 𝑛≤𝑚. The ideal is
pure if all maximal monomials have the same total degree; this common degree is the socle
degree. The type is the number of maximal monomials. The pure 𝑂-sequence of Γ is
ℎΓ(𝑑) = #{𝑚∈Γ : |𝑚| = 𝑑}.
For a monomial 𝑔, we simply write ℎ𝑔(𝑑) = #{𝑢≤𝑔: |𝑢| = 𝑑}. The 𝑂-sequence is log-concave
if
ℎΓ(𝑖−1)ℎΓ(𝑖+ 1) ≤ℎΓ(𝑖)2
(0 < 𝑖< 𝑒),
where 𝑒is the socle degree of Γ. We write 1𝑃for the indicator of the condition 𝑃.
Proof. Let Γ be a pure order ideal in three variables and suppose that its two maximal
monomials are 𝑚1 ≠𝑚2. Since Γ is pure, |𝑚1| = |𝑚2| = 𝑒. Every element of a finite order
ideal lies below a maximal element, so
Γ = {𝑢: 𝑢≤𝑚1} ∪{𝑢: 𝑢≤𝑚2},
After possibly interchanging 𝑚1 and 𝑚2, there is a coordinate 𝑥∈{0, 1, 2} such that
𝑚2(𝑥) > 𝑚1(𝑥),
𝑚2(𝑦) ≤𝑚1(𝑦)
(𝑦≠𝑥).
(1)
Indeed, the three integers 𝑚1(𝑖) −𝑚2(𝑖) sum to zero and are not all zero, hence one sign
occurs in a minority position; if necessary we swap the two monomials so that the minority
sign is negative.
Let 𝑐= 𝑚1(𝑥) + 1, and define
𝑀red(𝑦) =
(
𝑚2(𝑥) −𝑚1(𝑥) −1,
𝑦= 𝑥,
𝑚2(𝑦),
𝑦≠𝑥.
51
Advancing Mathematics Research with AI-Driven Formal Proof Search
Then |𝑀red| = 𝑒−𝑐. For 𝑢≤𝑚2, condition (1) implies
𝑢̸ ≤𝑚1
⇐⇒
𝑢(𝑥) ≥𝑐.
If 𝑑≥𝑐, the map 𝑢↦→𝑢−𝑐𝑒𝑥bijects {𝑢≤𝑚2 : |𝑢| = 𝑑, 𝑢(𝑥) ≥𝑐} with {𝑣≤𝑀red : |𝑣| = 𝑑−𝑐}.
If 𝑑< 𝑐, the first set is empty. Hence the 𝑂sequence of Γ can be written as
𝐻(𝑑) := ℎΓ(𝑑) = ℎ𝑚1(𝑑) + 1𝑑≥𝑐ℎ𝑀red(𝑑−𝑐).
(2)
We need to prove that 𝐻(𝑑−1)𝐻(𝑑+ 1) ≤𝐻(𝑑)2 holds for 0 < 𝑑< 𝑒.
For an integer-valued sequence 𝐹: ℕ→ℤ, define the first and scond difference sequences
as
Δ𝐹(0) = 𝐹(0),
Δ𝐹(𝑑) = 𝐹(𝑑) −𝐹(𝑑−1)
(𝑑> 0),
Δ2𝐹(0) = Δ𝐹(0),
Δ2𝐹(𝑑) = Δ𝐹(𝑑) −Δ𝐹(𝑑−1)
(𝑑> 0).
We first prove an elementary divisor-count formula for a single monomial. Let 𝑚= (𝛼, 𝛽, 𝛾)
be a monomial. For 𝑝, 𝑞∈ℕ, set
𝐿𝑝,𝑞(𝑘) = #{𝑟∈ℕ: 𝑟< 𝑝, 𝑟≤𝑘, 𝑘−𝑟< 𝑞}.
Thus 𝐿𝑝,𝑞(𝑘) counts the number of pairs (𝑟, 𝑠) with 0 ≤𝑟< 𝑝, 0 ≤𝑠< 𝑞, and 𝑟+ 𝑠= 𝑘. A direct
box count gives
ℎ𝑚(𝑡) =
𝑡∑︁
𝑘=0
1𝑡−𝑘<𝛾+1 𝐿𝛼+1,𝛽+1(𝑘).
With the convention Δ𝐹(0) = 𝐹(0), the first-difference identities are
Δ𝐿𝑝,𝑞(𝑡) = 1𝑡<𝑝+ 1𝑡<𝑞−1𝑡<𝑝+𝑞
(𝑡≥0),
and hence
Δℎ𝑚(𝑡) = 𝐿𝛼+1,𝛽+1(𝑡) −1𝑡≥𝛾+1 𝐿𝛼+1,𝛽+1(𝑡−𝛾−1)
(𝑡≥0).
Taking one more difference gives, for every 𝑡> 0,
Δ2ℎ𝑚(𝑡) = 1𝑡≤𝛼+ 1𝑡≤𝛽+ 1𝑡≤𝛾−1𝑡≤𝛼+𝛽+1 −1𝑡≤𝛽+𝛾+1
−1𝑡≤𝛾+𝛼+1 + 1𝑡≤𝛼+𝛽+𝛾+2.
(3)
In particular, Δ2ℎ𝑚(𝑡) ≤1. The same bound holds for the shifted sequence 𝑡↦−→1𝑡≥𝑐ℎ𝑀red(𝑡−𝑐),
because below the shift its second difference is zero, and from the shift onward it is the
second difference of the principal sequence of 𝑀red. Therefore Δ2𝐻(𝑡) ≤2.
Formula (3) also implies the following useful dichotomy. If 𝑡> 0 and Δ2ℎ𝑚(𝑡) = 1, then
either
𝑡≤𝑚(0),
𝑡≤𝑚(1),
𝑡≤𝑚(2),
(L)
or
𝑡≥𝑚(0) + 𝑚(1) + 2,
𝑡≥𝑚(1) + 𝑚(2) + 2,
𝑡≥𝑚(0) + 𝑚(2) + 2,
𝑡≤|𝑚| + 2. (U)
We refer to these as the lower and upper alternatives. For 𝑡= 0, the lower alternative is
automatic.
We shall also use the following elementary consequences of the same box count.
52
Advancing Mathematics Research with AI-Driven Formal Proof Search
1. If 𝑡≤𝑚(𝑖) for all 𝑖, then
2ℎ𝑚(𝑡) = (𝑡+ 1)(𝑡+ 2),
Δℎ𝑚(𝑡) = 𝑡+ 1.
(5)
2. If 𝑡≥𝑚(𝑖) + 𝑚( 𝑗) for every pair {𝑖, 𝑗}, and 𝑡≤|𝑚| + 2, then,
2ℎ𝑚(𝑡) = (|𝑚| + 1 −𝑡)(|𝑚| + 2 −𝑡).
(6)
3. If 𝑡≥𝑚(𝑖) + 𝑚( 𝑗) + 1 for every pair {𝑖, 𝑗}, and 𝑡≤|𝑚| + 2, then
Δℎ𝑚(𝑡) = −(|𝑚| + 2 −𝑡).
(7)
4. For all 𝑡,
2ℎ𝑚(𝑡) ≤(|𝑚| −𝑡+ 1)(|𝑚| −𝑡+ 2).
(8)
5. If 2𝑡≥|𝑚| + 1, then
Δℎ𝑚(𝑡) ≤0.
(9)
Now fix 0 < 𝑑< 𝑒= |𝑚1| = |𝑚2|. Using 𝐻(𝑑) = 𝐻(𝑑−1) + Δ𝐻(𝑑) and Δ𝐻(𝑑+ 1) =
Δ𝐻(𝑑) + Δ2𝐻(𝑑+ 1) gives
𝐻(𝑑)2 −𝐻(𝑑−1)𝐻(𝑑+ 1) = (Δ𝐻(𝑑))2 −𝐻(𝑑−1)Δ2𝐻(𝑑+ 1).
(10)
Since 𝐻(𝑑−1) ≥0 and Δ2𝐻(𝑑+ 1) ≤2, it is enough to prove the following two statements:
Δ2𝐻(𝑑+ 1) = 1
=⇒
𝐻(𝑑−1) ≤(Δ𝐻(𝑑))2,
(11)
and
Δ2𝐻(𝑑+ 1) = 2
=⇒
2𝐻(𝑑−1) ≤(Δ𝐻(𝑑))2.
(12)
Indeed, if Δ2𝐻(𝑑+ 1) ≤0, equation (10) is immediate; if it is 1 or 2, then (11) or (12)
applies.
Write 𝑓(𝑡) = ℎ𝑚1(𝑡) and 𝑔(𝑡) = 1𝑡≥𝑐ℎ𝑀red(𝑡−𝑐), so that 𝐻= 𝑓+ 𝑔. Since Δ2 𝑓≤1 and
Δ2𝑔≤1, if Δ2𝐻(𝑑+ 1) = 1, then either
Δ2 𝑓(𝑑+ 1) = 1,
Δ2𝑔(𝑑+ 1) = 0,
(A)
or
Δ2 𝑓(𝑑+ 1) = 0,
Δ2𝑔(𝑑+ 1) = 1.
(B)
If Δ2𝐻(𝑑+ 1) = 2, then
Δ2 𝑓(𝑑+ 1) = Δ2𝑔(𝑑+ 1) = 1.
(C)
Case A1: (A)+(L) for 𝑓. Suppose equation (A) holds and the lower alternative (L) holds
for 𝑓with 𝑡= 𝑑+ 1. Then in particular 𝑑+ 1 ≤𝑚1(𝑥) < 𝑐, thus 𝑔(𝑑−1) = 𝑔(𝑑) = 0, hence
Δ𝑔(𝑑) = 0 and therefore
𝐻(𝑑−1) = 𝑓(𝑑−1),
Δ𝐻(𝑑) = Δ 𝑓(𝑑).
By (5), 2 𝑓(𝑑−1) = 𝑑(𝑑+ 1) and Δ 𝑓(𝑑) = 𝑑+ 1. Therefore
𝐻(𝑑−1) = 𝑓(𝑑−1) ≤(𝑑+ 1)2 = (Δ 𝑓(𝑑))2 = (Δ𝐻(𝑑))2.
53
Advancing Mathematics Research with AI-Driven Formal Proof Search
This proves (11) in this case.
Case A2: (A)+(U) for 𝑓. Assume equation (A) holds and the upper alternative (U) holds for
𝑓with 𝑡= 𝑑+ 1. Let us introduce the shorthand notation 𝜌= 𝑒−𝑑. Then (U) gives 𝜌≥−1.
Applying (6) and (7) gives
2 𝑓(𝑑−1) = (𝜌+ 2)(𝜌+ 3),
Δ 𝑓(𝑑) = −(𝜌+ 2).
(13)
The shifted summand satisfies
Δ𝑔(𝑑) ≤0,
2𝑔(𝑑−1) ≤(𝜌+ 2)(𝜌+ 3),
2𝑔(𝑑) ≤(𝜌+ 1)(𝜌+ 2).
(14)
Indeed, the two inequalities for 𝑔(𝑑−1) and 𝑔(𝑑) follow from the universal upper bound (8),
applied to the shifted sequence. For the sign of Δ𝑔(𝑑), if 𝑑< 𝑐, then Δ𝑔(𝑑) = 0. If 𝑑≥𝑐, then
the upper alternative for 𝑓implies
𝑑≥𝑚1(𝑥) + 𝑚1(𝑦) + 1,
𝑑≥𝑚1(𝑥) + 𝑚1(𝑧) + 1,
where {𝑥, 𝑦, 𝑧} = {0, 1, 2}. Adding these inequalities gives
2𝑑≥2𝑚1(𝑥) + 𝑚1(𝑦) + 𝑚1(𝑧) + 2 = 𝑒+ 𝑚1(𝑥) + 2.
Since 𝑐= 𝑚1(𝑥) + 1 and |𝑀red| = 𝑒−𝑐, this is equivalent to 2(𝑑−𝑐) ≥|𝑀red| + 1. Thus the
midpoint monotonicity (9) applies to the shifted 𝑀red-sequence and gives Δ𝑔(𝑑) ≤0.
To prove (11), by (13) it remains to show
𝑓(𝑑−1) + 𝑔(𝑑−1) ≤ −(𝜌+ 2) + Δ𝑔(𝑑)2.
By (13) and (14), this follows from
(𝜌+ 2)(𝜌+ 3) + 2𝑔(𝑑−1) ≤2 −(𝜌+ 2) + Δ𝑔(𝑑)2.
(15)
Since 𝑔(𝑑) = 𝑔(𝑑−1) + Δ𝑔(𝑑), the third inequality in (14) gives
2𝑔(𝑑−1) ≤(𝜌+ 1)(𝜌+ 2) −2Δ𝑔(𝑑).
Therefore the difference between the right-hand side and the left-hand side of (15) is at least
2 −(𝜌+ 2) + Δ𝑔(𝑑)2 −(𝜌+ 2)(𝜌+ 3) − (𝜌+ 1)(𝜌+ 2) −2Δ𝑔(𝑑)
= 2Δ𝑔(𝑑) Δ𝑔(𝑑) −2(𝜌+ 2) + 1
.
This is nonnegative because Δ𝑔(𝑑) ≤0, 𝜌≥−1, and hence
Δ𝑔(𝑑) −2(𝜌+ 2) + 1 ≤0.
Thus (11) holds in this case, and we completed the (A) case.
For the two cases when (B) holds, that is Δ2𝑔(𝑑+ 1) = 1, we use the following shift
reduction. If
Δ2𝐻(𝑑+ 1) = 1
and
𝐻(𝑑+ 1) ≤(Δ𝐻(𝑑+ 1))2,
54
Advancing Mathematics Research with AI-Driven Formal Proof Search
then
𝐻(𝑑−1) ≤(Δ𝐻(𝑑))2.
(16)
Indeed, Δ𝐻(𝑑) = Δ𝐻(𝑑+ 1) −1 and 𝐻(𝑑−1) = 𝐻(𝑑+ 1) −Δ𝐻(𝑑+ 1) −Δ𝐻(𝑑). Therefore
𝐻(𝑑−1) = 𝐻(𝑑+ 1) −2Δ𝐻(𝑑+ 1) + 1 ≤(Δ𝐻(𝑑+ 1))2 −2Δ𝐻(𝑑+ 1) + 1 = (Δ𝐻(𝑑))2.
Case B1: (B)+(L) for 𝑔. Assume equation (B) holds and the lower alternative (L) holds for
𝑔with 𝑡= 𝑑+ 1. Let 𝐷= 𝑑+ 1. Since Δ2𝑔(𝐷) = 1, necessarily 𝐷≥𝑐, and Δ2ℎ𝑀red(𝐷−𝑐) = 1.
In the lower subcase 𝐷−𝑐≤𝑀red(𝑖) for every 𝑖. Then 𝐷−𝑐+ 1 ≥1, and the lower formula
(5) gives
2𝑔(𝐷) = (𝐷−𝑐+ 1)(𝐷−𝑐+ 2),
Δ𝑔(𝐷) = 𝐷−𝑐+ 1.
(17)
We next prove two bounds for 𝑓at 𝐷:
𝑓(𝐷) ≤(𝐷+ 1)Δ 𝑓(𝐷),
Δ 𝑓(𝐷) = 𝑐.
(18)
First, since Δ2 𝑓(𝐷) = 0, the explicit formula (3), together with the lower inequalities for 𝑀red,
implies
𝐷≤𝑚1(0) + 𝑚1(1) + 1,
𝐷≤𝑚1(1) + 𝑚1(2) + 1,
𝐷≤𝑚1(0) + 𝑚1(2) + 1.
(19)
Indeed, the two pair inequalities involving 𝑥follow directly from 𝐷−𝑐≤𝑀red(𝑦) ≤𝑚1(𝑦) for
𝑦≠𝑥. The remaining pair inequality follows from (3): if it failed, then the corresponding
two single indicators would be zero; since 𝐷≥𝑐= 𝑚1(𝑥) + 1, the 𝑥-single indicator is also
zero, and the right-hand side of (3) would be negative, contradicting Δ2 𝑓(𝐷) = 0.
Thus, in (3) for 𝑓at 𝐷, all three pair indicators and the triple indicator are equal to 1.
Since Δ2 𝑓(𝐷) = 0, exactly two of the three single indicators are equal to 1. Moreover the
𝑥-single indicator is zero, because 𝐷≥𝑚1(𝑥) + 1. Hence the two remaining single indicators
are equal to 1.
It follows that for every 1 ≤𝑘≤𝐷, the same two single indicators are still equal to 1,
while the three pair indicators and the triple indicator are also equal to 1. Therefore
Δ2 𝑓(𝑘) ≥2 −3 + 1 = 0
(1 ≤𝑘≤𝐷).
Thus the first differences Δ 𝑓(𝑘) are nondecreasing on {0, 1, . . . , 𝐷}. Since
𝑓(𝐷) =
𝐷
∑︁
𝑗=0
Δ 𝑓( 𝑗),
we get
𝑓(𝐷) ≤(𝐷+ 1)Δ 𝑓(𝐷).
This proves the first inequality in (18).
For the second inequality in (18), relabel the two coordinates different from 𝑥as 𝑦, 𝑧,
and write
𝐴= 𝑚1(𝑦) + 1,
𝐵= 𝑚1(𝑧) + 1,
55
Advancing Mathematics Research with AI-Driven Formal Proof Search
and recall 𝑐= 𝑚1(𝑥) + 1. Using the box-count formula with 𝑥as the third coordinate, the
first-difference formula gives
Δ 𝑓(𝐷) = 𝐿𝐴,𝐵(𝐷) −𝐿𝐴,𝐵(𝐷−𝑐),
because 𝐷≥𝑐. From the preceding paragraph, 𝐷< 𝐴and 𝐷< 𝐵, hence
𝐿𝐴,𝐵(𝐷) = 𝐷+ 1,
𝐿𝐴,𝐵(𝐷−𝑐) = 𝐷−𝑐+ 1.
Therefore
Δ 𝑓(𝐷) = (𝐷+ 1) −(𝐷−𝑐+ 1) = 𝑐,
proving (18). Using (17) and (18), we have
2𝐻(𝐷) = 2 𝑓(𝐷) + 2𝑔(𝐷) ≤2Δ 𝑓(𝐷)(𝐷+ 1) + (𝐷−𝑐+ 1)(𝐷−𝑐+ 2).
Also, by (17),
Δ𝐻(𝐷) = Δ 𝑓(𝐷) + Δ𝑔(𝐷) = Δ 𝑓(𝐷) + (𝐷−𝑐+ 1).
Thus it is enough to show
2Δ 𝑓(𝐷)(𝐷+ 1) + (𝐷−𝑐+ 1)(𝐷−𝑐+ 2) ≤2 Δ 𝑓(𝐷) + 𝐷−𝑐+ 12.
Since 𝐷+ 1 = (𝐷−𝑐+ 1) + 𝑐, the difference between the right-hand side and the left-hand
side is
2Δ 𝑓(𝐷) Δ 𝑓(𝐷) −𝑐 + 2Δ 𝑓(𝐷)(𝐷−𝑐+ 1) + (𝐷−𝑐+ 1)(𝐷−𝑐).
This is nonnegative because Δ 𝑓(𝐷) ≥𝑐and 𝐷−𝑐+ 1 ≥1. Therefore 𝐻(𝐷) ≤(Δ𝐻(𝐷))2. By
the shift reduction (16), this proves (11).
Case B2: (B)+(U) for 𝑔. Again let 𝐷= 𝑑+ 1 and put 𝜌= 𝑒−𝐷. The upper alternative for
ℎ𝑀red at 𝐷−𝑐gives 𝜌≥−2. Since |𝑀red| = 𝑒−𝑐, formulas (6) and (7) give
2𝑔(𝐷) = (𝜌+ 1)(𝜌+ 2),
Δ𝑔(𝐷) = −(𝜌+ 2).
(20)
For the first summand, the universal upper bound (8) gives
2 𝑓(𝐷) ≤(𝑒−𝐷+ 1)(𝑒−𝐷+ 2) = (𝜌+ 1)(𝜌+ 2).
(21)
It remains to justify the sign of Δ 𝑓(𝐷). Since 𝑔is in the upper alternative at 𝐷, we have
𝐷−𝑐≥𝑀red(0) + 𝑀red(1) + 2, 𝐷−𝑐≥𝑀red(1) + 𝑀red(2) + 2, 𝐷−𝑐≥𝑀red(0) + 𝑀red(2) + 2.
Adding these three inequalities gives
3(𝐷−𝑐) ≥2|𝑀red| + 6 = 2(𝑒−𝑐) + 6.
Hence
2(𝐷−𝑐) ≥2
3
 2|𝑀red| + 6 = |𝑀red| + 1 + |𝑀red| + 9
3
> |𝑀red| + 1,
because |𝑀red| ≥0. Therefore
2𝐷= 2(𝐷−𝑐) + 2𝑐≥(𝑒−𝑐+ 1) + 2𝑐= 𝑒+ 𝑐+ 1 ≥𝑒+ 1.
56
Advancing Mathematics Research with AI-Driven Formal Proof Search
By midpoint monotonicity (9), applied to 𝑓= ℎ𝑚1, we get Δ 𝑓(𝐷) ≤0. Using (20), (21), we
get
2𝐻(𝐷) ≤2(𝜌+ 1)(𝜌+ 2),
Δ𝐻(𝐷) = Δ 𝑓(𝐷) −(𝜌+ 2).
Since 𝜌≥−2 and Δ 𝑓(𝐷) ≤0, we have
(𝜌+ 1)(𝜌+ 2) ≤ −Δ 𝑓(𝐷) + 𝜌+ 22.
giving the desired 𝐻(𝐷) ≤(Δ𝐻(𝐷))2. By the shift reduction (16), this proves (11).
Case C: (C) holds. So here Δ2𝐻(𝑑+ 1) = 2 and hence Δ2 𝑓(𝑑+ 1) = Δ2𝑔(𝑑+ 1) = 1. Since
Δ2𝑔(𝑑+ 1) = 1, necessarily 𝑑+ 1 ≥𝑐. Therefore the lower alternative (L) for 𝑓is impossible,
because it would imply 𝑑+ 1 ≤𝑚1(𝑥) < 𝑐. Hence 𝑓is in its upper alternative, that is, (U)
holds for 𝑓. The lower alternative (L) for 𝑔is also impossible. Indeed, if 𝑑+ 1 −𝑐≤𝑀red(𝑖)
for every 𝑖, then, choosing any 𝑦≠𝑥, we get
𝑑+ 1 ≤𝑚1(𝑥) + 1 + 𝑀red(𝑦) = 𝑚1(𝑥) + 1 + 𝑚2(𝑦) ≤𝑚1(𝑥) + 1 + 𝑚1(𝑦).
But the upper alternative for 𝑓gives 𝑑+ 1 ≥𝑚1(𝑥) + 𝑚1(𝑦) + 2, a contradiction. Thus 𝑔is
also in its upper alternative, and (U) holds for 𝑔. Put 𝜌= 𝑒−𝑑again. Since |𝑀red| = 𝑒−𝑐, we
also have |𝑀red| −(𝑑−𝑐) = 𝑒−𝑑= 𝜌. The upper formulas (6) and (7), applied to 𝑓and to
the shifted summand 𝑔, give
2 𝑓(𝑑−1) = (𝜌+ 2)(𝜌+ 3),
Δ 𝑓(𝑑) = −(𝜌+ 2),
and
2𝑔(𝑑−1) = (𝜌+ 2)(𝜌+ 3),
Δ𝑔(𝑑) = −(𝜌+ 2).
Therefore
2𝐻(𝑑−1) = 2(𝜌+ 2)(𝜌+ 3),
Δ𝐻(𝑑) = −2(𝜌+ 2).
Since the upper alternative for 𝑓gives 𝜌≥−1, we have
(Δ𝐻(𝑑))2 −2𝐻(𝑑−1) = 4(𝜌+ 2)2 −2(𝜌+ 2)(𝜌+ 3) = 2(𝜌+ 2)(𝜌+ 1) ≥0.
which proves (12). This completes the proof of (11) and (12), and hence by (10) 𝐻(𝑑−
1)𝐻(𝑑+ 1) ≤𝐻(𝑑)2. Since 0 < 𝑑< 𝑒was arbitrary and 𝐻is the pure 𝑂-sequence of Γ by (2),
the theorem follows.
□
The Lean proof for the problem can be found at https://github.com/google-dee
pmind/alphaproof-nexus-results/tree/main/APNOutputs/AICollaborator/A
lgebraicGeometry.
