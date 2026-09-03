---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-012-51-group-algebras
section_title: "Group algebras"
section_number: 5.1
pages: 18-23
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an anal ysis of quantum Markov semi-groups."
---
discussed in [BrOz08, Section 15], but we include all proofs for reader’s convenience.
Let Γ be a discrete group. Let π : Γ →U (H) be a unitary representation and b : Γ → H a
1-cocycle for π in the sense that b(xy) = b(x) + πxb(y) for all x, y∈ Γ. Consider left and right
actions of Γ on H⊗ ℓ2(Γ) given by πx⊗ λx and 1⊗ ρy for all x, y∈ Γ respectively. Then using the
canonical basis ( δx)x∈Γ for ℓ2(Γ), one can construct a closable derivation by
∂ : C[Γ]→ H⊗ ℓ2(Γ); ∂(x) = b(x)⊗ ex, x ∈ Γ .
As above, put A := C[Γ] and deﬁne S :A→ H⊗ ℓ2(Γ) by Sex := ∂(x)‖∂(x)‖−1 (and put Sex =
ξ⊗ ex for any ﬁxed unit vector ξ∈ H if ∂(x) = 0). Recall that b is proper if‖b(g)‖→ 0 whenever
g→∞ . In this setting, we prove the following.
Proposition 5.3. Suppose that b is proper and that π is weakly contained in the left regular
representation. Then ∂ and S satisfy all the assumptions in Proposition 5.2.
Proof. Since S is an isometry, Assumption 2 is trivially satisﬁed. Since π≺ λ, it holds that the
representation Γ×Γ∋ (x, y)↦→πx⊗λxρy is weakly contained in the one of Γ×Γ∋ (x, y)↦→λx⊗λxρy,
which is in turn unitarily equivalent to Γ × Γ∋ (x, y)↦→πx⊗ ρy via the unitary ex⊗ ey↦→ex⊗ exy
on ℓ2(Γ)⊗ ℓ2(Γ). We conclude that H⊗ ℓ2(Γ) is weakly contained in the coarse bimodule as A-A
bimodules.
It remains to show that Tx,y is compact for all x, y∈A . For this we can assume x, y∈ Γ. Using
Lemma 5.4 below and using the properness of b, one has ‖Tx,y (eg)‖→ 0 as g →∞ . Observe
that Tx,y (eg)∈ H⊗ Cexgy, hence T ∗
x,y Tx,y ∈ ℓ∞(Γ), so T ∗
x,y Tx,y ∈ c0(Γ). We conclude that Tx,y is
compact. □
L2-COHOMOLOGY, DERIV ATIONS AND SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS 19
Lemma 5.4. For every γ1, γ2∈ Λ , there is a constant Cγ1,γ 2 > 0 such that
‖Tγ1,γ 2(µ)‖ ⩽ Cγ1,γ 2‖∂(µ)‖−1.
Proof. We have,
Tγ1,γ 2(µ) =‖∂(µ)‖−1γ1∂(µ)γ2−‖ ∂(γ1µγ2)‖−1∂(γ1µγ2)
=(‖∂(µ)‖−1−‖ ∂(γ1µγ2)‖−1)γ1∂(µ)γ2−‖ ∂(γ1µγ2)‖−1(γ1∂(µ)γ2 + γ1µ∂(γ2)).
(5.4)
We have that,
‖∂(γ1µγ2)‖−‖ ∂(µ)‖ ⩽ ‖∂(γ2)‖ +‖∂(γ1)‖,
so
‖∂(µ)‖−1−‖ ∂(γ1µγ2)‖−1 ⩽ ‖∂(γ2)‖ +‖∂(γ1)‖
‖∂(γ1µγ2)‖‖∂(µ)‖ ,
converges to 0 with order O(‖∂(µ)‖−2) as ∂ is proper. We conclude that ‖Tγ1,γ 2(µ)‖ converges to
0 with order O(‖∂(µ)‖−1). □
5.2. V on Neumann algebras with ﬁltration. We ﬁx again ( M, τ ) a ﬁnite von Neumann algebra
with (Φ t)t≥0 = (exp(−t∆)) t≥0 a quantum Markov semi-group. Let
∂ :A→ L2(M )∇ : a↦→a⊗ Ω τ
be the derivation of Corollary 3.12. We shall assume that ∆ sa tisﬁes certain properties that are
close to being a length function.
Deﬁnition 5.5. We say that ∆ is ﬁltered if it has a compact resolvent and for every eigenvalue
λ of ∆ there exists a (necessarily ﬁnite dimensional) subspac eA(λ)⊆A such thatA(λ)Ω τ equals
the eigenspace of ∆ at eigenvalue λ≥ 0. Moreover, let λn, n∈ N be an increasing enumeration of
the eigenvalues of ∆, and we assume the spaces A(λn), n∈ N, to be ﬁltered in the sense that
(5.5)
∞⨁
k=0
A(λk) =A and A(λn)A(λm)⊆
m+n⨁
k=0
A(λk) for all n, m∈ N,
where ⨁ means the algebraic direct sum.
Suppose now that ∆ has a compact resolvent with a complete set of eigenvectors ( ei)i inA which
is an orthonormal basis in L2(M ) (for example if ∆ is ﬁltered this holds). Then since it is als o a
linear basis for A, we can deﬁne the map S by ( ei)i and ∂ as in (5.1). Observe that if ei∈A (λn),
then‖∂(ei)‖2 =⟨∆( ei), ei⟩ = λn. Using this, it is easy to see that
(5.6) S(a) = λ
− 1
2
n ∂(a), for all a∈A (λn) and all eigenvalues λn.
In particular, the map S does not depend on the choice of ( ei)i.
Lemma 5.6. Suppose that ∆ has a compact resolvent with a complete set of eigenvectors i nA.
Then the map S in (5.6) is an isometry and hence satisﬁes Assumption 2.
Proof. By deﬁnition, S is given by eigenvectors ( ei)i. Then we have,
⟨S(ei), S(ej)⟩ =‖∂(ei)‖−1‖∂(ej )‖−1⟨∂(ei), ∂(ej )⟩ =‖∂(ei)‖−1‖∂(ej)‖−1⟨∆
1
2 ei, ∆
1
2 ej⟩ = δi,j .
So S is an isometry. □
Lemma 5.7. Suppose that ∆ is ﬁltered, then in fact we have A(λm)A(λn)⊂ ⨁ m+n
k=|m−n|A(λk).
20 MARTIJN CASPERS, YUSUKE ISONO, AND MATEUSZ W ASILEWSKI
Proof. As ∆( x∗) = ∆( x)∗ for x∈ A, the spaces A(λ) are self-adjoint. Now take x∈ A(λm),
y∈A (λn) and z∈A (λk). Assume that m > n and that k < m − n. By assumption we ﬁnd
that y∗z∈ ⨁ n+k
l=0A(λl). As n + k < m this shows that 0 = ⟨y∗zΩ τ , xΩ τ⟩ =⟨zΩ τ , yxΩ τ⟩. So yx is
orthogonal toA(λk). The same holds for xy, which yields the lemma. □
Example 5.8. Let Λ be a discrete ﬁnitely generated group and let L : Λ → N be the length
function given by the graph distance to the identity in the Ca yley graph of Λ. Set ∆ to be the
closure of γ↦→L(γ)γ as an unbounded operator on ℓ2(Λ). Suppose that L is conditionally positive
deﬁnite so that
Q(ξ) =
∑
γ ∈Γ
L(γ)‖ξ(γ)‖2 =⟨∆
1
2 ξ, ∆
1
2 ξ⟩
is a quantum Dirichlet form (see [CiSa03]), i.e. the generat or of a quantum Markov semi-group.
Then ∆ is easily seen to be ﬁltered.
Remark 5.9. Let Γ q(HR) be the q-Gaussian algebra for −1 < q < 1 with the Ornstein-Uhlenbeck
semi-group e−t∆ , see Section 4. Then it follows from the Wick product formula of Lemma 4.3 that
∆ is ﬁltered.
Deﬁnition 5.10. We say that ∆ has subexponential growth if it has a complete set of eigen-
values λ0 < λ 1 < λ 2 < . . . for which
(5.7) lim
n→∞
λn+1
λn
= 1.
Remark 5.11. Subexponential growth of a generator of a quantum Markov sem i-group should be
compared to the amenability results obtained in [CiSa03] an d [Cas18, Appendix]. These results
show that often one cannot expect a growth on the eigenvalues that is more than linear and so in
particular (5.7) holds.
Theorem 5.12. Let M be a ﬁnite von Neumann algebra and let (Φ t)t≥0 = (exp(−t∆)) t≥0 be a
quantum Markov semi-group such that ∆ is ﬁltered with subexponential growth. Let S be as in
(5.6). Then for every x, y∈A the operator Tx,y in (5.2) is compact.
Proof. Fix x, y∈ ⨁ K
k=0A(λk) for some K∈ N. For each eigenvalue λ, let Pλ be the orthogonal
projection onto A(λ)Ω τ and we also regard it as a map A→A (λ). Only in this proof, we will
use the notation ‖a‖∞ for the operator norm for a∈A . Our ﬁrst goal is to prove ‖Tx,y Pλ n‖→ 0
as n→∞ . For this, we have only to prove that ‖Tx,y (an)‖→ 0 as n→∞ , where ( an)n is any
sequence such that an∈A (λn) and‖anΩ τ‖ = 1 for all n∈ N.
Take such a sequence ( an)n and ﬁx n∈ N. Then since xany∈ ⨁ 2K
k=−2KA(λn+k) by Lemma 5.7
(whereA(l) = 0 if l < 0), one has xany = ∑ 2K
k=−2K Pλ n+k (xany) (where Pl = 0 if l < 0), so that
S(xany) =
2K∑
k=−2K
λ
− 1
2
n+k∂(Pλ n+k (xany)).
Using this, we can write
Tx,y (an) = xS(an)y− S(xany) = λ
− 1
2
n x∂(an)y−
2K∑
k=−2K
λ
− 1
2
n+k∂(Pλ n+k (xany))
L2-COHOMOLOGY, DERIV ATIONS AND SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS 21
and further using ∂(xany) = ∑ 2K
k=−2K ∂(Pλ n+k (xany)), this translates into
(5.8) Tx,y (an) = λ
− 1
2
n (x∂(an)y− ∂(xany)) +
2K∑
k=−2K
(λ
− 1
2
n − λ
− 1
2
n+k)∂(Pλ n+k (xany)).
We will show that the ﬁrst and the second term on the right hand side converges to 0 as n→∞ .
We see the second term. Observe that for each −2K ⩽ k ⩽ 2K,
‖∂(Pλ n+k (xany))‖ =‖∆
1
2 (Pλ n+k (xany))‖ = λ
1
2
n+k‖Pλ n+k (xany)‖ ⩽ λ
1
2
n+k‖x‖∞‖y‖∞.
The subexponential growth condition then shows that for any such k,
‖(λ
− 1
2
n − λ
− 1
2
n+k)∂(Pλ n+k (xany))‖ ⩽ λ
1
2
n+k|λ
− 1
2
n − λ
− 1
2
n+k|‖x‖∞‖y‖∞→ 0
as n→∞ . This ﬁnishes the case of the second term.
We next see the ﬁrst term. By using the Leibniz rule, our term i s
(5.9) λ
− 1
2
n (x∂(an)y− ∂(xany)) =−λ
− 1
2
n (∂(x)any + xan∂(y)) .
To estimate this term we ﬁrstly ﬁnd
‖∂(x)any‖2 =‖x⊗∇ anyΩ τ‖2 ⩽ ‖Γ( x, x)‖∞‖anΩ τ‖2‖y‖2
∞ =‖Γ( x, x)‖∞‖y‖2
∞,
hence, as n→∞ ,
(5.10) λ
− 1
2
n ‖∂(x)any‖ ⩽ λ
− 1
2
n ‖Γ( x, x)‖
1
2
∞‖y‖∞→ 0.
This shows that the ﬁrst summand on the right hand side of (5.9 ) converges to 0. For the sec-
ond summand, we ﬁrst observe a couple of preliminary estimat es. Using the equation any =∑ K
k=−K Pλ n+k (any) by Lemma 5.7 (where Pl = 0 if l < 0), we have
‖(∆( an)y− ∆( any))Ω τ‖2 =
‖‖‖‖‖
K∑
k=−K
λnPλ n+k (any)−
K∑
k=−K
λn+kPλ n+k (any)
‖‖‖‖‖
2
=
K∑
k=−K
|λn− λn+k|2 ‖‖Pλ n+k (any)
‖‖2
⩽
K∑
k=−K
|λn− λn+k|2‖y‖2
∞ ,
so that by combining with the subexponential growth conditi on, as n→∞ ,
(5.11) λ−1
n ‖(∆( an)y− ∆( any))Ω τ‖→ 0.
Secondly, as ∆ is self adjoint,
(5.12) λ−1
n τ (∆( y∗a∗
nan)y) = λ−1
n τ (y∗a∗
nan∆( y)) =
K∑
k=0
λk
λn
τ (y∗a∗
nanPλ k (y))→ 0,
as n→∞ , where we used the estimate for each summand as
λk
λn
|τ (y∗a∗
nanPλ k (y))| = λk
λn
|τ (anPλ k (y)y∗a∗
n)| ⩽ λk
λn
‖Pλ k (y)y∗‖∞,
which converges to 0 as n→∞ . Similarly,
(5.13) λ−1
n τ (y∗∆( a∗
nan)y) = λ−1
n τ (a∗
nan∆( yy ∗))→ 0,
22 MARTIJN CASPERS, YUSUKE ISONO, AND MATEUSZ W ASILEWSKI
as n→∞ . Now we ﬁnd that
2|λ−1
n τ (Γ( an, any)y− y∗Γ( an, an)y)|
⩽ λ−1
n |τ (∆( any)∗any− y∗∆( an)∗any)| + λ−1
n |τ (∆( y∗a∗
nan)y)| + λ−1
n |τ (y∗∆( a∗
nan)y)|
⩽ λ−1
n ‖(∆( any)− ∆( an)y)Ω τ‖‖y‖∞ + λ−1
n |τ (∆( y∗a∗
nan)y)| + λ−1
n |τ (y∗∆( a∗
nan)y)|
which converges to 0 as n→∞ by (5.11), (5.12) and (5.13). Essentially the same estimate s show
that
λ−1
n τ (Γ( any, any)− y∗Γ( any, an))→ 0.
We therefore get that, as n→∞ ,
λ−1
n ‖an∂(y)‖2 =λ−1
n τ (Γ( any, any) + y∗Γ( an, an)y− y∗Γ( any, an)− Γ( an, any)y)→ 0.
This shows that, as n→∞ ,
(5.14) λ
− 1
2
n ‖xan∂(y)‖ ⩽ λ
− 1
2
n ‖x‖∞‖an∂(y)‖→ 0.
In all, the convergences (5.14) and (5.10) show that (5.9) an d hence (5.8) goes to 0. We conclude
that Tx,y (an)→ 0 as n→∞ and therefore‖Tx,y Pλ n‖→ 0 as n→∞ .
By Lemma 5.7, for any n, m with|n− m| > 2K, xany and xamy are orthogonal, so that
⟨xan⊗∇ y, xam⊗∇ y⟩ =⟨xan⊗∇ y, xamy⊗∇ 1⟩ =⟨x⊗∇ any, xamy⊗∇ 1⟩ = 0.
This implies⟨x∂(an)y, x∂(am)y⟩ =⟨x∂(an)y, ∂(xamy)⟩ = 0. We obtain
⟨Tx,y (an), Tx,y (am)⟩ = 0, for all n, m with|n− m| > 2K.
It turns out that T ∗
x,y Tx,y Pλ n = ∑ 2K
k=−2K Pλ n+k T ∗
x,y Tx,y Pλ n for all n∈ N (where Pl = 0 if l < 0).
By putting T := T ∗
x,y Tx,y , we see that
T =
∑
n∈N
T Pλ n =
∑
n∈N
2K∑
k=−2K
Pλ n+k T Pλ n =
2K∑
k=−2K
∑
n∈N
Pλ n+k T Pλ n,
where the sum is in the strong topology. For each ﬁxed −2K ⩽ k ⩽ 2K and m∈ N, since Pλ n+k is
orthogonal for diﬀerent n, it holds that‖‖‖‖‖‖
∑
m⩽ n∈N
Pλ n+k T Pλ n
‖‖‖‖‖‖
= sup
m⩽ n∈N
‖Pλ n+k T Pλ n‖ ⩽ sup
m⩽ n∈N
‖Tx,y Pλ n+k‖‖Tx,y Pλ n‖,
which converges to 0 as m→∞ . Thus the sum ∑
n∈N Pλ n+k T Pλ n converges in the norm topology,
hence it is a compact operator. We conclude that T is compact, so Tx,y is also compact. □
We conclude as follows.
Theorem 5.13. Let M be a ﬁnite von Neumann algebra and let (Φ t)t≥0 = (exp(−t∆)) t≥0 be a
quantum Markov semi-group that is gradient coarse and suppo se that ∆ is ﬁltered with subexponen-
tial growth. Assume further that A as deﬁned above is locally reﬂexive. Then M satisﬁes AO +.
Proof. Lemma 5.6 and Theorem 5.12 show that the assumptions of Propo sition 5.2 are satisﬁed.
Therefore this proposition together with local reﬂexivity of A implies that M satisﬁes AO +. □
The following corollary is then a consequence of [Iso15] (se e also [PoVa14]).
Corollary 5.14. Suppose M has the W ∗CMAP. Then under the assumptions of Theorem 5.13, M
is strongly solid.
L2-COHOMOLOGY, DERIV ATIONS AND SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS 23
The following examples are covered by Theorem 5.13.
Corollary 5.15. For|q| ⩽ dim(H)− 1
2 the q-Gaussian algebra Γ q(HR) satisﬁes Condition AO +.
Proof. In case|q| < dim(H)− 1
2 we verify the conditions of Theorem 5.13 as follows. From The orem
4.14 and Remark 5.9 we see that a Γ q(HR) admits a ﬁltered quantum Markov semi-group that is
gradient-S2. From Corollary 3.10 this semi-group is gradient coarse and the conditions of Theorem
5.13 are veriﬁed. In case |q| ⩽ dim(H)− 1
2 we have that Theorem 4.14 and Remark 5.9 show that
Γ q(HR) admits a ﬁltered quantum Markov semi-group that is immedia tely gradient-S2. Then from
[Cas18, Proposition 4.3] and Proposition 4.16 we see that th e semi-group is gradient coarse. We
conclude again by Theorem 5.13. □
As mentioned before, Shlyakhtenko [Shl04] obtained the sam e result for |q| <
√
2− 1 so that up
to dimension 5 we ﬁnd a new range. Other examples include the f ollowing.
Example 5.16. Free group factors with the natural radial semi-group comin g from the length
function. Here conditon AO + is known, see [BrOz08].
Example 5.17. Free orthogonal quantum groups O+
N (tracial case). In [Cas18] a gradient coarse
quantum Markov semi-group was constructed which has the ﬁlt er and subexponential growth prop-
erty. Together with local reﬂexivity (which follows from th e CMAP of [Fre13] or [CFY14]) one
obtains AO +. Here AO + was obtained already in [VaVe07] using boundary actions.
