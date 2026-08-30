---
doc_id: arxiv-math-0304010v1
doc_title: "KEROV’S CENTRAL LIMIT THEOREM FOR THE PLANCHEREL MEASURE ON YOUNG DIAGRAMS"
section_id: sec-002-410-thus-the-degree-of-fn-does-not-exceed-1
section_title: "Thus, the degree of ⟨f⟩n does not exceed 1"
section_number: 4.10
pages: 27-33
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
doc_brief: "KEROV’S CENTRAL LIMIT THEOREM FOR THE PLANCHEREL MEASURE ON YOUNG DIAGRAMS — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
2 wt(f ), which implies that (5.4)
has a limit as n→∞ .
Expand f in the basis {p#
ρ}:
f =
∑
ρ
fρp#
ρ .
By virtue of Proposition 5.1,
lim
n→∞
n− wt(f )/2⟨f⟩n = f(1wt(f )/2)
with the understanding that the symbol f(1k/2) means 0 whenever k is odd.
Next, Proposition 4.9 (together with Proposition 4.10) imp lies the multiplicativ-
ity property
(f g)(1wt(f g)/2) = f(1wt(f )/2)g(1wt(g)/2) ,
where f, g are arbitrary weight homogeneous elements. Consequently, it suﬃces to
examine the case f =~pk , i.e., to show that
(~pk)(1k/2) =~pk[Ω] .
27
The right–hand side was found in Proposition 5.3, while the l eft–hand side can be
evaluated using Proposition 3.7. The result is the same, whi ch concludes the proof
of (5.3).
Now let us show that (5.3) implies (5.2). Indeed, (5.2) is equ ivalent to
lim
n→∞
∫ ¯λ(x)−| x|
2 xkdx =
∫ Ω( x)−| x|
2 xkdx in probability, for k = 0, 1, . . . .
By Proposition 2.2, this is equivalent to
lim
n→∞
~pk[¯λ(· )] = ~pk[Ω] in probability, for k = 2, 3, . . . .
Applying Chebyshev’s inequality we see that to prove this, i t suﬃces to check that
the ﬁrst and the second moments of the random variable ~pk[¯λ(· )] converge, as
n→∞ , to ~pk[Ω] and ~p 2
k [Ω], respectively. But this is a particular case of (5.3)
corresponding to f =~pk and f =~p 2
k , respectively. □
Theorem 5.5 (Law of large numbers, 2nd form). Let λ range over Yn, and
let us view ¯λ(· ) as a random function deﬁned on the probability space (Yn, Mn),
where Mn is the Plancherel measure. Let Ω be as above. Then we have
lim
n→∞
sup
x∈R
|¯λ(x)− Ω( x)| = 0 in probability. (5.5)
We need two lemmas.
Lemma 5.6. There exists an interval I⊂ R such that the probability that ¯λ(x)−|x|
is supported by I tends to 1 as n→∞ .
Proof. This follows from a ﬁner result due to Hammersley [Ha]. He has proved that
there exists a constant c such that for any ε > 0
lim
n→∞
Mn{λ∈ Yn|| λ1− c√n| < ε, |λ′
1− c√
n| < ε} = 1.
Actually, the constant c equals 2 (this was ﬁrst proved by Vershik–Kerov [VeK1],
[VeK3]), and at present much more is known about the asymptot ics of λ1, see, e.g.,
the expository paper [AD]. But, for our purpose, the old Hamm ersley’s result is
enough. □
Lemma 5.7. Fix an interval I = [ a, b]⊂ R, and let Σ denote the set of all real–
valued functions σ(x) on R, supported by I and satisfying the Lipschitz condition
|σ(x1)− σ(x2)|≤| x1− x2|.
On the set Σ , the weak topology deﬁned by the functionals
σ↦→
∫
σ(x)xkdx, k = 0, 1, . . . ,
coincides with the uniform topology deﬁned by the supremum n orm‖σ‖= sup|σ(x)|.
This fact was pointed out in [Ke2, §2.5].
Proof. Clearly, the uniform topology is stronger than the weak topo logy. Let us
check the inverse claim. Given x∈ I and ε > 0, let
V (x, ε) ={σ∈ Σ || σ(x)|≤ ε}.
28
Pick points a = ε1 <··· < ε n = b dividing I into subintervals of length ≤ 2ε.
Then, by the Lipschitz condition, the ball ‖σ‖≤2ε contains the intersections of
V (xi, ε)’s. Hence the required claim reduces to the following one:
Fix x∈ I and ε > 0. Then V (x, ε) contains a neighborhood of 0 in the weak
topology.
Let us remark that functions σ∈ Σ are uniformly bounded, ‖σ‖≤(b− a)/2.
Hence the weak topology on Σ will not change if we take, as func tionals, integrals
with arbitrary continuous functions F . Now let us take a continuous function
F (x)≥ 0, concentrated in the ε/2–neighborhood of x and such that
∫
F (y)dy = 1.
We claim that ⏐
⏐
⏐
⏐
∫
σ(x)F (x)dx
⏐
⏐
⏐
⏐≤ ε/2⇒ σ∈ V (x, ε).
Indeed, assume that σ /∈ V (x, ε), i.e., |σ(x)| > ε . Without loss of generality
we may assume that σ(x) > ε . Then, for any y such that |x− y|≤ ε/2, we have
σ(y) > ε/2, hence
∫
σ(y)F (y) > ε/2, which proves our claim. □
Proof of Theorem 5.5. This immediately follows from Theorem 5.4 and Lemmas
5.6, 5.7. □
§6. The central limit theorem for characters
For any f∈ A, we denote by f (n) the random variable deﬁned on the probability
space ( Yn , Mn) and obtained by restricting f to Yn.
By the symbol
d
−→ we will denote convergence of random variables in distribu-
tion, see, e.g. [Sh].
The aim of this section is to prove the following result.
Theorem 6.1 (Central limit theorem for characters).
Choose a sequence {ξk}k=2,3,... of independent standard Gaussian random vari-
ables. As n→∞ , we have



p#
k
(n)
nk/2



k=2,3,...
d
−→{
√
kξk}k=2,3,... (6.1)
In more detail, for any ﬁxed N = 2, 3, . . ., the joint distribution of N− 1 random
variables
p#
k
(n)
√
k nk/2 , 2≤ k≤ N,
weakly tends, as n→∞ , to the standard Gaussian measure on RN−1. Note that
we could take equally well in (6.1) the random variables
nk/2
√
k
χλ
(k,1n− k)
dim λ , 2≤ k≤ N,
where λ∈ Yn is the random Plancherel diagram.
The proof of Theorem 6.1 will be given after some preparation work, based on
Propositions 4.11, Proposition 4.12, and Corollary 4.13.
29
It will be convenient to extend the algebra A: we adjoin to it the square root of
the element p#
1 = p1 and then localize over the multiplicative family generated by√
p#
1 . Let Aext denote the resulting algebra. As a basis in Aext one can take the
elements of the form
p#
ρ · (p#
1 )m/2 , m 1(ρ) = 0 , m ∈ Z. (6.2)
We equip Aext with a ﬁltration by assigning to p#
ρ · (p#
1 )m/2 the degree deg 1(· ) =
|ρ|1 + m. That is, the N th term of the ﬁltration is spanned by all basis elements
(6.2) with|ρ|1 + m≤ N . Here N ranges over Z. On the subalgebra A⊂ Aext, this
ﬁltration agrees with that induced by the Kerov degree. Inde ed, this claim follows
from Proposition 4.11.
Since p#
1
(n)
≡ n, the symbol f (n) makes sense for any f ∈ Aext. Speciﬁcally,
if f = g(p#
1 )m/2 with g∈ A and m∈ Z then f (n) = g(n)· nm/2. Note also that
Proposition 5.2 admits the following extension:
Proposition 6.2. For any f∈ Aext,⟨f⟩n is a Laurent polynomial in n1/2 whose
degree with respect to n is bounded from above by 1
2 deg1(f ).
Proof. Evident from Proposition 5.2 and the fact that p#
1
(n)
≡ n. □
Let Hm(x), where m = 0 , 1, 2, . . ., be the Hermite polynomials in the normal-
ization of [Sz], [Er]. We shall need slightly modiﬁed polyno mials, which we denote
byHm(x):
Hm(x) = 2 −m/2 Hm(
√
2x) = m!
[m/2]∑
j=0
(−1/2)jxm−2j
j!(m− 2j)! .
These are monic polynomials, which form the orthogonal syst em with respect to
standard Gaussian measure (2 π)−1/2 exp(−x2/2)dx. They are characterized by the
recurrence relation
xHm =Hm+1 + mHm−1 (6.3)
together with the initial data H0 = 1,H1 = x.
For an arbitrary partition ρ, we deﬁne the element ηρ∈ Aext, which is a normal-
ization of p#
ρ :
ηρ = p#
ρ
(p#
1 )m1(ρ)∏
k≥2(k(p#
1 )k)mk(ρ)/2
= p#
ρ
(p#
1 )|ρ|1/2∏
k≥2 kmk(ρ)/2
. (6.4)
Note that deg 1(ηρ) = 0.
We abbreviate ηk = η(k) . Note that
ηk = p#
k
√
k (p#
1 )k/2
, k = 2, 3, . . . . (6.5)
30
Proposition 6.3. For any partition ρ, we have
ηρ =
∏
k≥2
Hmk(ρ)(ηk) + . . . (6.6)
where dots denote a remainder term with deg1(· ) < 0.
In particular, ηρ does not depend, up to terms of negative degree, from the valu e
of m1(ρ).
Proof. Examine ﬁrst the particular case ρ = ( km), where k = 2 , 3, . . . and m =
1, 2, . . . . Then our claim means that
η(km) =Hm(ηk) + . . . .
Taking σ = (km) in Proposition 4.12 we get
p#
(km)· p#
k = p#
(km+1) + k m p#
(km− 1,1k) +··· = p#
(km+1) + k m p#
(km− 1)· (p#
1 )k + . . .
for any m≥ 1, where dots mean lower degree terms. This is equivalent to
η(km)· ηk = η(km+1) + m η(km− 1) + . . . , m ≥ 1, (6.7)
where dots mean terms of negative degree. Within these terms , (6.7) coincides with
the recurrence relation (6.3), which proves (6.6).
The case of an arbitrary ρ is reduced to the particular case ρ = ( km) using
Corollary 4.13. □
The next claim is a well–known general result. It justiﬁes th e moment method,
which is a convenient tool for checking convergence in distr ibution.
Proposition 6.4. Let a(n) be a sequence of real random variables. Assume that
a(n) have ﬁnite moments of any order, and the moments converge, as n→∞ , to
the respective moments of a random variable a. Finally, assume that a is uniquely
determined by its moments, which holds, e.g., if the charact eristic function of a is
analytic.
Then a(n) d
−→ a. Moreover, this claim also holds when the variables in quest ion
take vector values, i.e., when each a(n), as well as a, is a system of random variables.
Sketch of proof. Let P (n) denote the distribution of the random variable a(n) and
P be the distribution of a. We have to prove that P (n) weakly converges to P as
n→∞ . The assumption on the moments implies that {P (n)} is a tight family of
probability measures on R. So, it suﬃces to prove that any partial weak limit P ′ of
the sequence {P (n)} coincides with P . Using again the condition on the moments
one can show that the moments of P ′ exist and coincide with the limits of the
respective moments of {P (n)}. Hence, these are exactly the moments of P . By the
uniqueness assumption, P ′ = P . □
For another proof, see Feller [Fe, ch. VIII, §6, Example b].
Proof of Theorem 6.1. We must prove that
{η(n)
k }k≥2
d
−→{ ξk}k≥2 , n →∞ .
31
By Proposition 6.4, it suﬃces to check that
⟨
∏
k≥2
ηmk
k ⟩n→⟨
∏
k≥2
ξmk
k ⟩Gauss , n →∞ , (6.8)
for any ﬁnite collection {mk}k≥2 of nonnegative integers, where the brackets
⟨·⟩Gauss mean expectation with respect to the standard Gaussian meas ure. The
uniqueness hypothesis of Proposition 6.4 is clearly satisﬁ ed.
The limit relations (6.8) are equivalent to the following on es:
⟨
∏
k≥2
Hmk (ηk)⟩n→
∏
k≥2
⟨Hmk (ξk)⟩Gauss
for any ﬁnite collection {mk∈ Z+}.
If all the numbers mk are equal to 0 then the expressions in both sides equal
1, and there is nothing to prove. So, let us assume that some of the mk’s are
nontrivial. Then the right–hand side vanishes, because, fo r a standard Gaussian ξ,
⟨Hm(ξ)⟩Gauss = 1√
2π
∫
R
Hm(x)e−x2/2dx = 0, m = 1, 2, . . . ,
by the orthogonal property of the polynomials Hm.
Let us examine the left–hand side. Set ρ = (∏
k≥2 kmk ). By Proposition 6.2,
∏
k≥2
Hmk (ηk) = ηρ + a “remainder term” of strictly negative degree .
By our assumption, ρ is nonempty. Moreover, m1(ρ) = 0, so that ρ⁄= (1 r). By
Proposition 5.1,⟨ηρ⟩n≡ 0. Finally, by Proposition 6.2,
⟨the “remainder term” ⟩n = O(n−1/2). (6.9)
This concludes the proof. □
Theorem 6.1 can be generalized as follows:
Theorem 6.5. Let ρ range over the set of all partitions. We have
{η(n)
ρ }
d
−→{
∏
k≥2
Hmk(ρ)(ξk)} , n →∞ ,
where, as before, ξ2, ξ3, . . . are independent standard Gaussians.
Proof. The above argument shows that any mixed moment of the random v ariables
from the left–hand side converges, as n→∞ , to the respective moment of the
random variables from the right–hand side. However, we cann ot use the moment
method, because a polynomial in Gaussian variables does not necessarily satisfy
the uniqueness assumption mentioned in Proposition 6.4. Fo r this reason we argue
in a diﬀerent way.
Assume that
{a(n)
1 , a(n)
2 , . . .}
d
−→{ a1, a2, . . .} , n →∞ ,
32
where a(n) = {a(n)
1 , a(n)
2 , . . .} are families of random variables depending on n
and a ={a1, a2, . . .} is one more family of random variables. Next, assume that
f1(x) = f1(x1, x2, . . .), f2(x) = f2(x1, x2, . . .), . . . are continuous functions in real
variables x = ( x1, x2, . . .), where each function actually depends on ﬁnitely many
variables only. Then
{f1(a(n)), f2(a(n)), . . .}
d
−→{ f1(a), f2(a), . . .} , n →∞ .
Using this general fact we conclude from Theorem 6.1 that any polynomial in
η(n)
2 , η(n)
3 , . . . converges in distribution to the same polynomial in ξ2, ξ3, . . .. More-
over, this also holds for any ﬁnite system of polynomials. By virtue of (6.9), each
ηρ is a polynomial in η(n)
2 , η(n)
3 , . . ., within a “remainder term”. So we only need to
check that the “remainder term” does not aﬀect the convergen ce in distribution.
Remark that the “remainder term” is of the form r(n), where r is an element of
Aext of strictly negative degree. It follows that any moment of r(n) tends to 0 as
n→∞ , which implies that r(n) d
−→ 0. This shows that the “remainder term” is
negligible. □
For a diﬀerent proof of Theorems 6.1 and 6.5, see [Ho].
§7. The central limit theorem for Young diagrams
Given λ∈ Yn , we set
∆ λ(x) =
√n
