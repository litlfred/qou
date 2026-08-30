---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-162-55-analytic-classification-of-linear-q-differenc
section_title: "ANALYTIC CLASSIFICATION OF LINEAR q-DIFFERENCE EQUATIONS 95"
section_number: 5.5
pages: 101-102
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
Then the conjugacy equation (σqF)A0 = AF admits a unique solution F =
(Fij) in G such that Fij∈ Matri,rj(OΛ i,j
Λ i,...,Λ j−1) for i<j
Proof. — Take A in the form (3.2). The conjugacy equation (5.39) is equiva-
lent to the following system; for1 ≤i<j ≤k:
zµj −µi(σqFij)Aj =AiFij +z−µi
j∑
ℓ=i+1
UiℓFℓj.
After J.P. B´ ezivin [7], we know that the formal solution ˆFij hasq-Gevrey order
1/(µj−µj−1) for i<j .
Let 1 <j ≤k and consider the formal solution ˆFj−1,j of equation:
(5.40) zµj −µj−1(σqY ) Aj =Aj−1 Y +z−µj−1Uj−1,j.
After the theorem of Borel-Ritt 5.3.3, there exists a functi on Φ j−1,j∈ AΛ j−1
q
with ˆFj−1,j as an asymptotic expansion at zero. Putting Y = Z + Φj−1,j in
equation (5.40), one gets, from theorem 5.3.5:
zµj −µj−1(σqY ) Aj =Aj−1 Y + Hj−1,j
θΛ j−1
,
where Hj−1,j denotes a meromorphic function in a neighborhood of z = 0.
Putting Z := X
θΛ j−1
one ﬁnds:
‖Λj−1‖(σqX) Aj =Aj−1 X +Hj−1,j .
By the non-resonancy assumption, this yields a unique solut ion that is mero-
morphic at z = 0. It follows that the equation admits a unique solution in
class AΛ j−1
q which is asymptotic to the series ˆFj−1,j; the uniqueness is obvious.
This solution will be written Fj−1,j.
Now consider the equation satisﬁed by ˆFj−2,j:
(5.41) zµj −µj−2(σqY ) Aj =Aj−2 Y +z−µj−2
(
Uj−2,j−1Fj−1,j +Uj−2,j
)
.
Choosing a function Φ j−2,j in AΛ j−1
q with ˆFj−2,j as an asymptotic expansion,
the change of unknown function Y = Z + Φj−2,j
θΛ j−1
transforms (5.41) into:
‖Λj−1‖ zµj−1−µj−2 (σqX) Aj =Aj−2 X +Hj−2,j ,
where Hj−2,j is a function meromorphic at z = 0. We are thus led back to
a similar situation as in equation (5.40), with µj−1−µj−2 instead of µj−
µj−1. One thus gets a solution of (5.41) in OΛ j−2,Λ j−1 which is asymptotic to
96 CHAPTER 5. SUMMATION AND ASYMPTOTIC THEORY
ˆFj−2,j along the divisors (Λ j−2, Λj−1 + Λj−2). By considering the associated
homogeneous equation, one checks that this solution is uniq ue.
Iterating the process, one shows that there is a unique solut ion Fi,j in
OΛ i,j
Λ i,...,Λ j−1 which is asymptotic to the formal solution ˆFij for all i<j .
Theorem 5.5.3 can be extended in the following way.
Corollary 5.5.4 . — Let B1,B 2 ∈ G(C{z}) be such that (A0)−1 Bi ∈
G(C{z}), i = 1, 2, and consider the associated q-diﬀerence equation:
(5.42) ( σqY ) B1 =B2Y .
Then, for any given generic partition of divisors (Λ1,..., Λk−1) for A0, there
exists, in G, a unique matrix solution Y := (Yi,j) of (5.42) and such that, for
each pair i<j of indices, Yi,j∈ Matri,rj(OΛ i,j
Λ i,...,Λ j−1).
Proof. — Recall that (5.42) is analytically conjugated to an equat ion of form
(5.39); see section 2.3. The result follows from propositio n 5.4.6 and the fact
that OΛ i,j
Λ i,...,Λ j−1⊂ OΛ i,j +1
Λ i,...,Λ j) for all i<j .
An obvious consequence of theorem 5.5.3 and corollary 5.5.4is the following.
Theorem 5.5.5 (Existence of asymptotic solutions)
The functions F = (Fi,j) and Y = (Yi,j) respectively considered in theorem
5.5.3 and corollary 5.5.4 both admit an asymptotic expansio n in the following
sense: for all pairs (i,j ) withi<j , the blocks Fi,j andYi,j have an asymptotic
expansion at 0 along divisors (Λj, Λi,j), according to deﬁnition 5.4.8.
Proof. — Immediate, with help of theorem 5.4.7.
