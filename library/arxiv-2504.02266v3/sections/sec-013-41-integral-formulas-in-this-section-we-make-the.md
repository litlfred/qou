---
doc_id: arxiv-2504.02266v3
doc_title: "Knizhnik-Zamolodchikov equations in Deligne categories"
section_id: sec-013-41-integral-formulas-in-this-section-we-make-the
section_title: "Integral formulas. In this section we make the same assumptions for 𝑡as in the"
section_number: 4.1
pages: 10-13
source_pdf: 2504.02266v3.pdf
source_sha256: a12193f740b6ee53
toc_source: inferred
---
Lemma 3.5. We wish to write explicit integral formulas for the flat sections of the ∇𝐾𝑍(ℏ)
connection on Hom-spaces 3.4. Due to Theorem 3.4 it suffices to find flat sections of the
dynamical connection (3.25) for the Lie algebra gl𝑛+𝑚and the weight space 𝑊𝛾⊤[𝛽].
Explicitly, we are looking for solutions 𝑢: {(𝑧1, . . . , 𝑧𝑛+𝑚) ∈C𝑛+𝑚| 𝑧𝑖̸ = 𝑧𝑗} →𝑊𝛾⊤[𝛽] to
the equations
𝑑𝑢= −ℏ
∑︁
1≤𝑖<𝑗≤𝑛+𝑚
𝑑𝑧𝑖−𝑑𝑧𝑗
𝑧𝑖−𝑧𝑗
𝑒−𝛼𝑒𝛼𝑢
(4.1)
where 𝛼is the root 𝜃𝑖−𝜃𝑗of gl𝑛+𝑚and 𝑒±𝛼are the corresponding normalized root vectors.
From [17][Theorems 3.1, 3.2] and [23], we have integral solutions to these equations,
which we will now describe. Let 𝑓𝑖= 𝐸𝑖+1,𝑖∈gl𝑛+𝑚for 1 ≤𝑖≤𝑛+ 𝑚−1 be the
standard lowering operators; associated with them are the simple roots 𝛼𝑖= 𝜃𝑖−𝜃𝑖+1.
Write 𝛾⊤−𝛽as a sum of simple roots 𝜆= ∑︀𝑛+𝑚−1
𝑖=1
𝑚𝑖𝛼𝑖for some 𝑚𝑖∈Z≥0 (note that
𝛾⊤−𝛽stabilizes for generic 𝑡, so the 𝑚𝑖do too). Let 𝑚= ∑︀𝑛+𝑚−1
𝑖=1
𝑚𝑖, and let 𝑐be the
unique non-decreasing function {1, . . . , 𝑚} →{1, . . . , 𝑛+ 𝑚−1} such that |𝑐−1(𝑖)| = 𝑚𝑖
for all 1 ≤𝑖≤𝑛+ 𝑚−1.
Let 𝑥∈C and 𝑡1, . . . , 𝑡𝑚be the coordinates on the space
(C ∖{𝑥})𝑚∖
⋃︁
1≤𝑖<𝑗≤𝑚
{𝑡𝑖= 𝑡𝑗}.
(4.2)
For permutations 𝜎∈𝑆𝑚define the differential 𝑚-forms
𝜔𝜎(𝑥) = 𝑑log(𝑡𝜎(1)−𝑡𝜎(2))∧· · ·∧𝑑log(𝑡𝜎(𝑚−1)−𝑡𝜎(𝑚))∧𝑑log(𝑡𝜎(𝑚)−𝑥),
𝑑= 𝑑𝑡,
𝜔𝜎:= 𝜔𝜎(0).
(4.3)
Also define the operator 𝑓𝑐(𝜎) := 𝑓𝑐(𝜎(1)) · · · 𝑓𝑐(𝜎(𝑚)). Let 𝑣denote the highest weight vector
in 𝑊𝛾⊤. The 𝑊𝛾⊤[𝛽]-valued differential 𝑚-form 𝜔is defined as
𝜔(𝑡1, . . . , 𝑡𝑚, 𝑥) =
∑︁
𝜎∈𝑆𝑚
(−1)|𝜎|𝜔𝜎(𝑥)𝑓𝑐(𝜎)𝑣.
(4.4)
We can also define 𝜔= 𝜔(𝑡1, . . . , 𝑡𝑚, 0).
Let us introduce the master functioñ︀
Φ(𝑥) :=
∏︁
1≤𝑖≤𝑚
(𝑡𝑖−𝑥)−(𝛼𝑐(𝑖),𝛾⊤) ∏︁
𝑖<𝑗
(𝑡𝑖−𝑡𝑗)(𝛼𝑐(𝑖),𝛼𝑐(𝑗)),
Φ :=̃︀Φ(0).
(4.5)
Theorem 4.1 ([17, 23]). For any appropriate cycle
Γ ∈𝐻𝑚((C ∖{𝑥})𝑚∖
⋃︁
1≤𝑖<𝑗≤𝑚
{𝑡𝑖= 𝑡𝑗})
(4.6)
the sections
𝑢(𝑧1, . . . , 𝑧𝑛+𝑚, 𝑥) :=
∫︁
Γ
exp
(︃
ℏ
(︃𝑚
∑︁
𝑖=1
(︀
𝑧𝑐(𝑖) −𝑧𝑐(𝑖)+1
)︀
𝑡𝑖−⟨𝛾⊤, 𝑧⟩𝑥
)︃)︃̃︀
Φ−ℏ(𝑥)𝜔(𝑡, 𝑥) (4.7)
KNIZHNIK-ZAMOLODCHIKOV EQUATIONS IN DELIGNE CATEGORIES
11
satisfy both the trivial Knizhnik-Zamolodchikov connection (in the single variable 𝑥)
𝑑+ ℏ𝑧,
𝑑= 𝑑𝑥
(4.8)
where we view 𝑧= (𝑧1, . . . , 𝑧𝑛+𝑚) as an element of the standard Cartan subalgebra of
gl𝑛+𝑚, and the dynamical equations for
∇′
𝐷:= 𝑑𝑧+ ℏ
(︃𝑛+𝑚
∑︁
𝑖=1
𝛽𝑖𝑥𝑑𝑧𝑖+
∑︁
1≤𝑖<𝑗≤𝑛+𝑚
𝑑𝑧𝑖−𝑑𝑧𝑗
𝑧𝑖−𝑧𝑗
𝑒−𝛼𝑒𝛼
)︃
.
(4.9)
We have the following consequence of this theorem.
Corollary 4.2. The sections 𝑢(𝑧1, . . . , 𝑧𝑛+𝑚, 0) satisfy the dynamical equations for ∇𝐷
from Theorem 3.4.
Let us fix an ordering 𝑙: {1, . . . , 𝑚} →{1, . . . , 𝑚} of the set {1, . . . , 𝑚}. For each 𝑙we
construct a cycle in Γ𝑙∈𝐻𝑚((C ∖{0})𝑚∖⋃︀
1≤𝑖<𝑗≤𝑚{𝑡𝑖= 𝑡𝑗}) given by the picture below,
0
𝑡𝑙−1(1)
...
𝑡𝑙−1(𝑚)
Pic. 1. Integration contours for Γ𝑙.
Theorem 4.3. The sections of the form
𝑢𝑙:=
∫︁
Γ𝑙
exp
(︃
ℏ
𝑚
∑︁
𝑖=1
(︀
𝑧𝑐(𝑖) −𝑧𝑐(𝑖)+1
)︀
𝑡𝑖
)︃
Φ−ℏ𝜔
(4.10)
span the space of solutions of the dynamical equations in 𝑊𝛾⊤[𝛽]. The integrals converge
in the region Re(ℏ(𝑧𝑖−𝑧𝑖+1)) < 0.
Proof. Consider a limit ℏ= 𝜖, 𝑧𝑖= 𝑧′
𝑖/𝜖, 𝜖→0 so that Re(𝑧′
𝑖−𝑧′
𝑖+1) < 0. By deforming
the contours of integration we may assume that both “tails” of each individual contour
are close to the real line.
0
𝑡𝑙−1(1)
. . .
𝑡𝑙−1(𝑚)
Pic. 2. Deformation of the cycle Γ𝑙.
We may note that the integral 𝑢𝑙(𝑧′
𝑖, 𝜖) converges absolutely in 𝜖, so it is holomorphic in
𝜖and we may consider 𝑢𝑙(𝑧′
𝑖, 0). Assume for simplicity that we are working with only
one term 𝜔𝜎of 𝜔. When we let 𝜖= 0, the function under the integral (4.10) becomes
holomorphic on C𝑚∖(⋃︀
𝑖<𝑗{𝑡𝑖= 𝑡𝑗} ∪⋃︀
𝑖{𝑡𝑖= 0}). If we look at the function 𝑢𝑙(𝑧′
𝑖, 0)
without the integral over 𝑡𝑙−1(1), the resulting function 𝑓1(𝑡𝑙−1(1), 𝑧′
𝑖) is either holomorphic
or meromorphic in 𝑡𝑙−1(1) with the only simple pole at 𝑡𝑙−1(1) = 0 depending on the last
factor of 𝜔𝜎in the denominator. Therefore, if we perform the missing integration in 𝑡𝑙−1(1)
and pinch two tails of integration from 𝑎+𝑖0+ to +∞+𝑖0+ and back from +∞−𝑖0+ to
𝑎−𝑖0+ where 𝑎∈R>0, they will cancel each other out. Thus the resulting integral com-
putes the residue of 𝑓1(𝑡𝑙−1(1), 𝑧′
𝑖) at 𝑡𝑙−1(1) = 0. If 𝜔𝜎does not have a pole at 𝑡𝑙−1(1) = 0,
12
P. Etingof ⋆, I. Motorin*, A. Varchenko♢, and I. Zhu†
then the integral is zero.
This argument shows that we may algebraically compute the residue of the function
exp
(︃𝑚
∑︁
𝑖=1
(𝑧′
𝑐(𝑖) −𝑧′
𝑐(𝑖)+1)𝑡𝑖
)︃
1
(𝑡𝜎(1) −𝑡𝜎(2))(𝑡𝜎(2) −𝑡𝜎(3)) . . . (𝑡𝜎(𝑚−1) −𝑡𝜎(𝑚))𝑡𝜎(𝑚)
(4.11)
at 𝑡𝑙−1(1) = 0 and then perform the other 𝑚−1 integrations. If 𝜎(𝑚) = 𝑙−1(1), the residue
is equal to
exp
(︃𝑚−1
∑︁
𝑖=1
(𝑧′
𝑐(𝑖) −𝑧′
𝑐(𝑖)+1)𝑡𝑖
)︃
1
(𝑡𝜎(1) −𝑡𝜎(2))(𝑡𝜎(2) −𝑡𝜎(3)) . . . (𝑡𝜎(𝑚−2) −𝑡𝜎(𝑚−1))𝑡𝜎(𝑚−1)
.
(4.12)
Now we can consider the same argument for the next variable 𝑡𝑙−1(2) and so on. From
this we see that
∫︁
Γ𝑙
exp
(︃𝑚
∑︁
𝑖=1
(𝑧′
𝑐(𝑖) −𝑧′
𝑐(𝑖)+1)𝑡𝑖
)︃
𝜔𝜎= (−2𝜋i)𝑚𝛿𝜎,𝑙−1∘𝑤,
(4.13)
where 𝑤(𝑖) = 𝑚+ 1 −𝑖, 1 ≤𝑖≤𝑚. Then we have
𝑢𝑙(𝑧′
𝑖, 0) =
∫︁
Γ𝑙
∑︁
𝜎∈𝑆𝑚
𝜔𝜎𝑓𝑐(𝜎)𝑣= (−2𝜋i)𝑚𝑓𝑐(𝑙−1∘𝑤)𝑣.
(4.14)
The vectors 𝑓𝑐(𝜎)𝑣span 𝑊𝛾⊤[𝛽], so the solutions (4.10) span the space of all solutions in
𝑊𝛾⊤[𝛽].
□
Remark 4.4. For large integer 𝑡there is a natural embedding
𝜙: 𝑊𝛾⊤→Λ𝛾1𝑊⊗· · · ⊗Λ𝛾𝑡𝑊
(4.15)
which sends the highest-weight vector of 𝑊𝛾⊤to the product of highest-weight vectors.
One might also try to write solutions for large integer 𝑡using Theorem 3.1 in [17] on the
gl𝑛+𝑚weight space (Λ𝛾1𝑊⊗· · · ⊗Λ𝛾𝑡𝑊) [𝛽]. However, we can show that the solutions
obtained in this way actually lie in the image of 𝜙, and are in fact the same as the
solutions obtained in Theorem 4.3. Explicitly, the “new” solutions are described as follows:
let 𝑃be the set of sequences 𝜎= (𝑖1
1, . . . , 𝑖1
𝑠1; . . . ; 𝑖𝑡
1, . . . , 𝑖𝑡
𝑠𝑡) consisting of the numbers
1, . . . , 𝑚arranged into 𝑡rows. For each such sequence, define the differential form 𝜔𝜎=
𝜔𝑖1
1,...,𝑖1𝑠1 ∧· · · ∧𝜔𝑖𝑡
1,...,𝑖𝑡𝑠𝑡where 𝜔𝑖1,...,𝑖𝑠:= 𝑑log(𝑡𝑖1 −𝑡𝑖2) ∧· · · ∧𝑑log(𝑡𝑖𝑠−1 −𝑡𝑖𝑠) ∧𝑑log(𝑡𝑖𝑠).
Also define the vector 𝑓𝜎𝑣:= 𝑓𝑐(𝑖1
1) · · · 𝑓𝑐(𝑖1𝑠1)𝑣1 ⊗· · · ⊗𝑓𝑐(𝑖𝑡
1) · · · 𝑓𝑐(𝑖𝑡𝑠𝑡)𝑣𝑡where 𝑣𝑗is the
highest-weight vector in Λ𝛾𝑗𝑊. Then the “new” solutions are given by
𝑢𝑙=
∫︁
Γ𝑙
exp
(︃
ℏ
𝑚
∑︁
𝑖=1
(︀
𝑧𝑐(𝑖) −𝑧𝑐(𝑖)+1
)︀
𝑡𝑖
)︃
Φ−ℏ̃︀𝜔
(4.16)
wherẽ︀
𝜔:=
∑︁
𝜎∈𝑃
(−1)|𝜎|𝜔𝜎𝑓𝜎𝑣.
(4.17)
Here |𝜎| is the sign of the permutation associated to 𝜎– note that the sequence
(𝑖1
1, . . . , 𝑖1
𝑠1, . . . , 𝑖𝑡
1, . . . , 𝑖𝑡
𝑠𝑡) is related to a standard sequence (1, . . . , 𝑚) by a unique per-
mutation. By repeatedly using Lemma 7.4.4 from [23] and the formula for the action of a
Lie algebra g on a tensor product of g-modules, we can re-arrange terms in (4.16). This
way we can see that the solutions (4.16) are the same as (4.10).
KNIZHNIK-ZAMOLODCHIKOV EQUATIONS IN DELIGNE CATEGORIES
13
Example 4.5. As in Example 3.1, consider the case when 𝜆, 𝜇= 0 and 𝑚= 𝑛so we
have HomRep(𝐺𝐿𝑡)(1, 𝑉*⊗𝑚⊗𝑉⊗𝑚) ∼= C[𝑆𝑚]. This is also identified with the gl2𝑚-weight
space 𝑊𝛾⊤[𝛽] where
𝛾⊤= (𝑡, . . . , 𝑡
⏟ ⏞ 
𝑚times
, 0, . . . , 0
⏟ ⏞ 
𝑚times
).
(4.18)
The difference 𝛾⊤−𝛽is written as the sum of simple roots ∑︀2𝑚−1
𝑖=1
𝑚𝑖𝛼𝑖where 𝑚𝑖=
𝑚−|𝑚−𝑖|, so our solutions involve 𝑚= 𝑚2 integrations.
