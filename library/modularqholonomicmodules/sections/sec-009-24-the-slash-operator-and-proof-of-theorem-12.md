---
doc_id: modularqholonomicmodules
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-009-24-the-slash-operator-and-proof-of-theorem-12
section_title: "The slash operator and proof of Theorem 1.2"
section_number: 2.4
pages: 17-20
source_pdf: modular.qholonomic.modules.pdf
source_sha256: 640303a68dd75453
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
---
operator, an important ingredient to express modularity. We will use the usual conventions
for the modular q = e(τ) and the Jacobi t = e(z),λi = e(ui),µi = e(vi),x = e(w) variables,
i.e., ~q = e(−1/τ), ~t = e(z/τ ) and e(x) = e2πix. Now recall the slash operator f|κγ (see,
eg. [12, p.13] and [21]) for γ =
(a b
c d
)
∈ SL2(Z ) acting on a function f(z,τ ) by
(f|κγ)(z,τ ) = (cτ +d)−κf(γ(z,τ )), γ (z,τ ) =
( z
cτ +d,aτ +b
cτ +d
)
. (69)
This action can be extended to a matrix-valued functionF (z,τ ) of weightκ = diag(κ1,...,κ r)
by
(F|κγ)(z,τ ) =F (γ(z,τ ))diag((cτ +d)−κ). (70)
This extension satisﬁes
(F|κγ)|κγ′ =F|κγγ′
(FG )|κγ = (F|κγ)∆γ(G|κγ) (71)
for matrix-valued functions F and G and for γ,γ′∈ SL2(Z ) where ∆γ(τ) = diag((cτ +d)κ).
We can extend these deﬁnitions to include half integral weight using a multiplier system as
done for the Dedekindη-function. In all our examples the relative weightsκi−κj are integers
and the absolute weights are either always integers, or always half-integers. Our choice of
absolute weight depends on the normalisation of our solutions, and multiplying them by
η-functions leads to a shift of the absolute weights by half-integers, but has no eﬀect on the
modularity of the linear q-diﬀerence equation.
Recall the cocycle Ω U,γ from Equation (4), and the corresponding cocycle Ω V,γ. If the
monodromy matrix M = V−1U satisﬁes Equation (6), it follows that the cocycle matrices
associated to U and V are equal:
ΩU,γ = (V
−→
M|κUγ)(V
−→
M)−1 = (V|κVγ)∆κV,γ(
−→
M|κUγ)(V
−→
M)−1
= (V|κVγ)∆κV,γ(
−→
M|κUγ)
−→
M−1V−1 = (V|κVγ)V−1 = ΩV,γ.
(72)
We remark that sometimes the monodromy matrix of the fundamental bases U and V
that come from the algorithm of Section 2.2 satisﬁes Equation (6) on a ﬁnite index subgroup
of SL 2(Z ) (this happens, e.g., in Theorem 1.7) which contains a conjugate of a congruence
subgroup of SL 2(Z ). In this case, an averaging of the monodromy leads to fundamental
solutions whose cocycle extends for all γ∈ SL2(Z ).
In the rest of this subsection, we give a proof of Theorem 1.2
18 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
Proof of Theorem 1.2. Using the behaviour of the slash operator on the product of two ma-
trices (71), it is easy to see that if Equation (6) holds for two elements of SL 2(Z ), it also
holds for their product. Since S and T generate SL2(Z ), part (a) follows.
Part (b) follows from the presentation of SL 2(Z ) given by
SL2(Z ) =⟨S,T | S4 =I,TSTST =S⟩ (73)
and from the cocycle property, which implies that if γ =Ta0STa1STa2...ST arSTar+1, then
Ωγ(z,τ ) =
r∏
j=1
ΩS((TajSTaj+1...T arSTar+1)(z,τ )). (74)
The idea for part (c) is to use reduction theory, with attention paid to the domain of
extension. Fix a cocycle Ω that satisﬁes Ω T =I and ΩS extends as a meromorphic function
to C × C ′. Below, when we say that Ω γ extends, we will mean that it extends to C × C γ.
We will give the proof in several steps.
Step 1. The cocycle property implies that
Ωγ−1(z,τ ) =
(
Ωγ(γ−1(z,τ ))
)−1
. (75)
This, together with the fact that γ−1(τ)−γ−1(∞) = 1/(c(−cτ +a)) imply that Ωγ extends
if and only if Ωγ−1 extends. In particular, applying it to γ =S, where γ−1 =−S, we obtain
that
Ω−S(z,τ ) = (ΩS(−z/τ,−1/τ))−1. (76)
Using our assumptions on ΩS, it follows that Ω−S extends.
Step 2. Suppose now that γ =
(a b
c d
)
∈ SL2(Z ) with a >0 and c >0. It follows by Gauss
reduction theory that we can write
γ =Ta0STa1S...T arSTar+1 (77)
for integers ai where a0≥ 0 and a1,...,a r > 0. Moreover, a0,...,a r can be obtained from
the negative continued fraction expansion (using nearest integers from above, rather than
from below)
a
c = [a0,a 1,...,a r] :=a0− 1/(a1− 1/(a2−... )). (78)
The continued fraction expansion shows that the ﬁrst column of γ agrees with that of the
product Ta0STa1S...T arS, and the last integer ar+1 is chosen so that Equation (77) holds.
Equation (74) implies that Ωγ(z,τ ) is a product ofr matrices ΩS matrices evaluated suitably,
and Ωγ extends to real τ that satisfy (TajSTaj+1...T arSTar+1)(τ) > 0 for all j = 1,...,r .
The key property is that the ﬁrst column of the matrices TajSTaj+1...T arSTar+1 for j =
1,...,r consists of positive integers (with the possible exception of j = r + 1 where the
(2, 1) entry may be zero). It follows that the system of inequalities cascades, and becomes
equivalent to the single inequality τ >−d/c. It follows that Ω γ extends in the case when
γ =
( +∗
+∗
)
∈ SL2(Z ).
The above argument is best explained by an example. Consider the matrix γ =
( 17 29
7 12
)
.
We expand the rational number 17/7 of its ﬁrst column in negative continued fractions
17
7 = [3, 2, 4] = 3− 4
7 = 3− 1
7/4 = 3− 1
2− 1/4
MODULAR q-HOLONOMIC MODULES 19
and obtain that the matrix T 3ST 2ST 4S =
(
17 −5
7 −2
)
, which further adjusting it by multi-
plying it on the right by T 2, gives
γ =
(
17 −5
7 −2
)
T 2 =T 3ST 2ST 4ST 2.
The cocycle property and the fact that
T 2ST 4ST 2 =
(
7 12
4 7
)
, T 4ST 2 =
(
4 7
1 2
)
, T 2 =
(
1 2
0 1
)
implies that
Ωγ(z,τ ) = ΩS
( z
4τ + 7, 7τ + 12
4τ + 7
)
ΩS
( z
τ + 2, 4τ + 7
τ + 2
)
ΩS(z,τ + 2). (79)
The right hand side extends when τ is real that satisﬁes
7τ + 12
4τ + 7 > 0, 4τ + 7
τ + 2 > 0, τ + 2> 0
which (when reading the inequalities from last to ﬁrst and simplifying) is equivalent to the
system τ + 2> 0, 4τ + 7> 0, 7τ + 12> 0, which is equivalent to τ >−12/7 =γ−1(∞).
Step 3. We will now use the element ε =
(−1 0
0 1
)
∈ GL2(Z ) of order 2, and observe that
ε
(a b
c d
)
ε =
( a −b
−c d
)
∈ SL2(Z ) for all
(a b
c d
)
∈ SL2(Z ). In particular, εTε =T−1 andεSε =−S.
It follows that if γ =
(a b
c d
)
∈ SL2(Z ) with a> 0 and c> 0 is given by (77), then
εγε =
(
a −b
−c d
)
=T−a0(−S)T−a1(−S)...T −ar(−S)T−ar+1. (80)
The cocycle property implies that
Ωεγε(z,τ ) =
r∏
j=1
Ω−S((T−aj(−S)T−aj+1...T −ar(−S)T−ar+1)(z,τ )) (81)
where Ω−S(z,τ ) extends for τ < 0 by Step 1. Thus Ω εγε extends when the inequalities
(T−aj(−S)T−aj+1...T −ar(−S)T−ar+1)(τ) < 0 for j = 1,...,r . The key point now is that
these inequalities cascade to a single inequality, namely, τ < d/c= (εγε)−1(∞). It follows
that Ωγ extends when γ =
( +∗
−∗
)
∈ SL2(Z ). In our running example above γ =
( 17 29
7 12
)
, we
have (
17 −20
−7 12
)
=εγε =T−3(−S)T−2(−S)T−4(−S)T−2 (82)
and the cocycle property and the fact that
T−2(−S)T−4(−S)T−2 =
(
7 −12
−4 7
)
, T −4(−S)T−2 =
(
4 −7
−1 2
)
, T −2 =
(
1 −2
0 1
)
implies that
Ωεγε = Ω−S
( z
−4τ + 7, 7τ− 12
−4τ + 7
)
Ω−S
( z
−τ + 2, 4τ− 7
−τ + 2
)
Ω−S(z,τ − 2). (83)
20 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
The right hand side extends when τ is real that satisﬁes
7τ− 12
−4τ + 7 < 0, 4τ− 7
−τ + 2 < 0, τ − 2< 0
which is equivalent to the system 7 τ− 12< 0, 4τ− 7< 0,τ − 2< 0 which is equivalent to
τ <12/7 = (εγε)−1(∞).
Step 4. The cocycle property and the triviality of Ω T = I implies that ΩTγ = Ωγ. Since
T
(a b
c d
)
=
(a+c b+d
c d
)
, it follows that Ωγ (and hence its extension) depends only on the bottom
row (c,d ) ofγ. When γ2,1⁄= 0, the extension follows from either Step 2 or Step 3, depending
on the sign of γ2,1.
This concludes the proof of the theorem. □
