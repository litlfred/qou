---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-009-42-gradient-sp-estimates
section_title: "Gradient-Sp estimates"
section_number: 4.2
pages: 11-16
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an anal ysis of quantum Markov semi-groups."
---
We will consider the operator Ψ a,b associated to the Ornstein-Uhlenbeck semigroup. We will ne ed a
formula for products of Wick words to be able to work with this operator. We will follow Eﬀros-Popa
[EﬀPop03] (see also [DeSch18]).
Deﬁnition 4.2. Let n1, . . . , nk be natural numbers. By P ⩽ 2(n1⊗···⊗ nk) we denote the set of
partitions of the set [ n], where n = n1 +··· + nk, with blocks of size at most two, such that there is
no pairing inside the sets{1, . . . , n1},{n1 +1, . . . , n1+n2}, . . . ,{n−nk +1, . . . , n}. For π∈ P ⩽ 2(n1⊗
···⊗ nk) we will deﬁne the number of crossings cr(π). Let π = ( l1, r1), . . . ,(lm, rm), s1, . . . , sl be
the blocks of the partition, so 2 m + l = n; we will denote by P (π) the set of pairs and by S(π) the
set of singletons. We will denote by c(π) the usual crossing number, i.e. the number of pairs ( li, ri)
and (lj, rj) such that li < lj < r i < r j. The symbol d(π) will denote the set of degenerate crossings,
i.e. the number of triples x < y < z such that ( x, z) = ( li, ri) for some i and y = sj for some j, i.e.
y is not paired with anything. The crossing number cr(π) is deﬁned to be cr(π) = c(π) + d(π).
While cumbersome to formally deﬁne, the crossing number is e asy to compute, provided that we
have a graphical representation of the partition available :
1 2 3 4 5 6 7 8 9 10 11
For this partition π there are two regular crossings (i.e. c(π) = 2) and 5 degenerate crossings, so
cr(π) = 7.
We are now ready to state the multiplication formula for Wick words (cf. [EﬀPop03, Theorem
3.3]).
Lemma 4.3. Let ξ = ξ1⊗···⊗ ξn∈ H ⊗n, where n = n1 +··· + nk. Let us call ξ1, . . . ,ξk the
tensors that arise from this decomposition of n, i.e. ξ1 = ξ1⊗···⊗ ξn1, ξ2 = ξn1+1⊗···⊗ ξn1+n2,
etc. We have the following formula
(4.1) Wq(ξ1) . . . Wq(ξk) =
∑
π ∈P ⩽ 2(n1⊗···⊗nk)
qcr(π )

 ∏
(l,r )∈P (π )
⟨Iξ l, ξr⟩

 Wq(ξS(π )),
12 MARTIJN CASPERS, YUSUKE ISONO, AND MATEUSZ W ASILEWSKI
where ξS(π ) := ξs1⊗···⊗ ξsl if S(π) ={s1 < s 2 <··· < s l}.
This formula will be instrumental in the proof of the next pro position.
Proposition 4.4. Take operators in Aq of the form
a = Wq(ξ) = Wq(ξ1⊗ . . .⊗ ξn), b = Wq(η ) = Wq(η1⊗ . . .⊗ ηk), x = Wq(µ ) = Wq(µ1⊗ . . .⊗ µm),
where each ξi, ηi, µi∈ H; deﬁne also v := ξ⊗ µ⊗ η . Then we have
∆( axb)− ∆( ax)b + a∆( x)b− a∆( xb)(4.2)
=−2
∑
π ∈P ⩽ 2(n⊗m⊗k)
|(l, r)∈ P (π) : l∈ [n], r∈ [k]| qcr(π )

 ∏
(l,r )∈P (π )
⟨Iv l, vr⟩

 Wq(vS(π )).
Proof. We determine the four summands in
(4.3) ∆( axb) + a∆( x)b− ∆( ax)b− a∆( xb).
Note that the formula for a triple product from the Lemma 4.3 c an be obtained by applying the
formula for double products twice. It means that we can compu te axb as either ( ax)b or a(xb). The
fact that the crossings that we compute on the way add up to the crossing number of the whole
partition is not hard to check, but not immediate. For instan ce, if we compute axb as ( ax)b, then
ﬁrst we get a sum over partitions of n⊗ m and then over partitions of ( n + m)⊗ k, where you
remove the nodes from [ n + m] that have already been paired; you have to check that the sum of
the crossing numbers of these partitions is equal to the cros sing number of the resulting partition
of n⊗ m⊗ k.
Once we have this observation, it is not hard to arrive at the f ormula. Indeed, each of the four
terms in (4.3) will feature a sum as in the formula for a triple product of Wick words, but with
coeﬃcients coming from the Laplacian. In case of ∆( axb) the coeﬃcient is equal to n + m + k−
2|P (π)|. For ∆( ax)b the coeﬃcient is equal to n + m− 2|{(l, r)∈ P (π) : l∈ [n], r∈ [m]}|. The term
a∆( x)b just yields m. The last one, a∆( xb), produces m + k− 2|{(l, r)∈ P (π) : l∈ [m], r∈ [k]}|.
If we compute ∆( axb)− ∆( ax)b + a∆( x)b− a∆( xb) then the result is −2|{(l, r)∈ P (π) : l∈ [n], r∈
[k]}|. Indeed, the pairings between [ n] and [ m] are accounted for by ∆( ax)b, the ones between [ m]
and [ k] by a∆( xb), and only pairings between [ n] and [ k] are left. □
We now have a formula for Ψ a,b (x). In order to estimate the Sp-norm of this map, we will
estimate separately the Sp-norms of Ψ a,b restricted to H ⊗m
q for each m /greaterorequalslant0. Recall that on an
N -dimensional Hilbert space we can estimate the Sp-norm by the operator norm, namely ‖T‖p ⩽
N
1
p‖T‖. Therefore we will be concerned only with the operator norm o f Ψ a,b restricted to H ⊗m.
Proposition 4.5. Let ξ := ξ1⊗···⊗ ξn∈ H ⊗n, η := η1⊗···⊗ ηn∈ H ⊗k and consider a := W (ξ)
and b := W (η ). Then the norm of Ψ a,b restricted to H ⊗m
q can be estimated as follows
(4.4) ‖Ψ a,b
|H ⊗ m
q
‖ ⩽ C(q, ξ, η , dim(H))|q|m.
In order to obtain useful estimates, we need to replace the fo rmula (4.1) by a new one, which
takes into account the q-deformed inner products. We will only consider the case of 2 or 3 Wick
words for simplicity. We will need operators R∗
n,k : H ⊗n+k→ H ⊗n+k given by
R∗
n,k (v1⊗···⊗ vn) =
∑
A⊂[n+k]:|A|=n
qi(A)vA⊗ v[n]\A,
L2-COHOMOLOGY, DERIV ATIONS AND SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS 13
where i(A) = ∑ n
l=1(il− l) if A ={i1 < i 2 <··· < i n}; one can interpret this number as the cost of
moving elements of A to the left of [ n + k] or, equivalently, cost of moving its complement to the
right. Now we can rewrite the formula for the double product o f Wick words.
Lemma 4.6. For (µ = µ1⊗···⊗ µm and η = η1⊗···⊗ ηk) we have
(4.5) W (µ )W (η )Ω =
m∧k∑
j=0
(Idm−j⊗ mj⊗ Idk−j)(R∗
m−j,j (µ )⊗ R∗
j,k −j(η )),
where mj : H ⊗j
q ⊗ H ⊗j
q → C is the inner product pairing given by mj(v⊗ w) =⟨Iv, w⟩.
Proof. Note that in Lemma 4.3 the crossings of partitions come from t wo sources; from pairing a
subset of [ m] with a subset of [ k] (the degenerate crossings) and from crossings inside thes e subsets.
If you ﬁx the subsets and sum over all partitions that pair the se two subsets, the crossings can be
incorporated into the deﬁnition of the q-deformed inner product, and the numbers i(A) appearing
in the deﬁnition of R∗
n,k count exactly the number of degenerate crossings. □
We can iterate this to obtain a formula for W (ξ)W (µ )W (η ). But if we do not introduce a simpler
notation, it will get very complicated. We will start from an element of a triple tensor product
H ⊗n⊗ H ⊗m⊗ H ⊗k. One thing that we will have to do is to apply inner product pai ring between
any two of them, and we need a notation for that. So we will use t he notation mab
j to denote the
pairing of H ⊗j from between the a-th and b-th space, e.g. m13
j will ﬁrst split H ⊗n⊗ H ⊗m⊗ H ⊗k
into H ⊗n−j⊗ H ⊗j⊗ H ⊗m⊗ H ⊗j⊗ H ⊗k−j and then pair the two H ⊗j spaces. Another thing is that
operators R∗
n,k only split the tensor power into two factors, but we will have to do it again, so we
need a notation for that as well. The deﬁning property of oper ators R∗
n,k is P n+k
q = (P n
q⊗ P k
q )R∗
n,k
(cf. [Kro00, Lemma 5]). It motivates the following deﬁnitio n.
Deﬁnition 4.7. We deﬁne the operator R∗
n,k,l : H ⊗n+k+l→ H ⊗n+k+l to be the unique operator
such that P n+k+l
q = (P n
q ⊗ P k
q⊗ P l
q)R∗
n,k,l .
Later on we will have to use boundedness of these operators. I n order to achieve that goal we
will need the following simple lemma.
Lemma 4.8. We have
R∗
n,k,l = (R∗
n,k ⊗ Idl)R∗
n+k,l = (Id n⊗ R∗
k,l )R∗
n,k +l.
Proof. The equality P n+k
q = (P n
q ⊗ P k
q )R∗
n,k means exactly that R∗
n,k is the adjoint of the ‘identity’
map Rn,k : H ⊗n
q ⊗ H ⊗k
q → H ⊗n+k
q . By the same token R∗
n,k,l is the adjoint of the identity map
Rn,k,l : H ⊗n
q ⊗ H ⊗k
q ⊗ H ⊗l
q → H ⊗n+k+l
q , which can be obtained by composition Rn+k,l (Rn,k ⊗ Idl)
or Rn,k +l(Idn⊗ Rk,l ).
□
We are ready to state a new formula for a triple product.
Proposition 4.9. Let ξ∈ H ⊗n, µ∈ H ⊗m, and η∈ H ⊗k. Then we have
(4.6)
W (ξ)W (µ )W (η )Ω =
∑
j,r,s
qr(m−j−s)m13
r m12
s m23
j (R∗
n−r−s,r,s (ξ)⊗ R∗
s,m −s−j,j (µ )⊗ R∗
j,r,k −j−r(η ))
14 MARTIJN CASPERS, YUSUKE ISONO, AND MATEUSZ W ASILEWSKI
Proof. The ﬁrst step is to apply formula (4.5) to W (µ )W (η ). It means that we apply the operator∑
j mj(R∗
m−j,j ⊗ R∗
j,k −j) to µ⊗ η . We denote the result by µ⊗W η = ∑
j µ⊗j
W η . And then
we repeat the procedure to obtain a formula for the triple pro duct, but we have to be careful at
this point. If we just used the formula for a double product, w e would have to apply the operator∑
p mp(R∗
n−p,p⊗ R∗
p,m +k−2j) to ξ⊗ (µ⊗j
W η ) and sum over j. Now the tensors µ and η are mixed
and we do not want to let that happen. So we will pair a subset of [n] with a subset of [ m + k− 2j]
(with some elements removed by the ﬁrst pairing) but we will s plit the latter into parts lying in
[m] and [ k]; say they have cardinalities s and r (so p = r + s). The issue is that we have to
move this whole subset to the left of [ m + k− 2j], pair with the corresponding subset of [ n] and
compute the inner product in H ⊗s+r
q , which is not what we want; we prefer H ⊗s
q ⊗ H ⊗r
q . Because
of the formula P s+r
q = ( P s
q⊗ P r
q )R∗
s,r , we can achieve this goal by applying (Id n−r−s⊗ R∗
s,r ) to
R∗
n−p,p (ξ). Note that our pairing m involves a second ingredient, the complex conjugation I, which
reverses the order of the tensor (i.e. I(v1⊗···⊗ vn) = Iv n⊗···⊗ Iv 1). So we should consider the
operator IP s+r
q instead. To make things easier, we will denote by I j the conjugation I acting on
H ⊗j. We have to compute I s+rP s+r
q = I s+r(P s
q⊗ P r
q )R∗
s,r . Because I s+r reverses the order, we get
I s+r(P s
q⊗ P r
q )R∗
s,r = (I rP r
q⊗ I sP s
q )R∗
r,s . Thus we can write ms+r = mrms(R∗
r,s⊗ Ids+r). It follows
that we can replace the pairing ms+r by mrms at the cost of applying Id n−r−s⊗ R∗
r,s to R∗
n−p,p (ξ);
by Lemma 4.8 this is the same as R∗
n−r−s,r,s (ξ).
Look now at the part coming from µ⊗j
W η ; we have a tensor of rank s coming from µ and
a tensor of rank r coming from η . We have to think about the cost of moving it to the left of
[m + k− 2j]. The µ part we can simply move to the left and it is accounted for by ap plying the
operator R∗
s,m −j−s. The η part we move to the left of [ k− j] using the operator R∗
r,k −j−r and then
we have to move it to be adjacent to the µ part. There are m− j− s nodes that we have to cross,
and the subset has cardinality r, so the cost is equal to r(m− j− s). It means that our formula
can be written as∑
j,r,s
qr(m−j−s)m13
r m12
s (R∗
m−r−s,r,s (ξ)⊗ (R∗
s,m −j−s⊗ R∗
r,k −j−r)(µ⊗j
W η )).
It is not yet exactly the formula (4.6), but it is very close to it. Recall that µ⊗j
W η is equal to
mj(R∗
m−j,j (µ )⊗ R∗
j,k −j(η )). So we arrive at
(R∗
s,m −j−s⊗ R∗
r,k −j−r)(mj(R∗
m−j,j (µ )⊗ R∗
j,k −j(η ))).
Note that we can either apply the pairing immediately, just l ike in the formula above, but we can
also ﬁrst apply identities on the spaces that will be paired, and apply the pairing afterwards. Thus
we get
mj((R∗
s,m −j−s⊗ Idj)R∗
m−j,j (µ )⊗ (Idj⊗ R∗
r,k −j−r)R∗
j,k −j(η )).
By Lemma 4.8, we get ( R∗
s,m −j−s⊗Idj)R∗
m−j,j = R∗
s,m −j−s,j and (Idj⊗R∗
r,k −j−r)R∗
j,k −j = R∗
j,r,k −j−r.
In order to ﬁnish the proof, it suﬃces to add the decoration 23 to mj to make it m23
j , which exactly
matches the formula (4.6). □
Remark 4.10. In order to pass to the formula for Ψ a,b (µ ) we just need to multiply each summand
in (4.6) by −2r.
In order to ﬁnish the proof of Proposition 4.5, we just need bo unds for the inner product pairings
and the operators R∗
n,k .
Lemma 4.11. Let H be a Hilbert space. The inner product pairing m : H⊗ H→ C has norm√
dim(H).
L2-COHOMOLOGY, DERIV ATIONS AND SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS 15
Proof. Let ( ei)i∈I be an orthonormal basis of H. Then the norm of v := ∑
i∈I ei⊗ ei is equal to√
|I|, while m(v) =|I|, so the norm is at least
√
|I|. On the other hand, a simple Cauchy-Schwarz
estimate shows that it is not larger than that. □
Lemma 4.12. Recall that the norm of R∗
n,k : H ⊗n+k→ H ⊗n+k is bounded by C(q). Then the norm
R∗
n,k : H ⊗n+k
q → H ⊗n
q ⊗ H ⊗k
q is not greater than
√
C(q).
Proof. Because of the formula P n+k
q = ( P n
q ⊗ P k
q )R∗
n,k , we get P n+k
q ⩽ C(q)P n
q ⊗ P k
q . Indeed, if
we have an equality A = BT for positive operators A and B then A2 = BT T ∗B ⩽ ‖T‖2B2, hence
A ⩽ ‖T‖B, as square root is an operator monotone function. The majori sation P n+k
q ⩽ C(q)P n
q⊗P k
q
shows that‖Rn,k‖ ⩽
√
C(q), therefore also ‖R∗
n,k‖ ⩽ C(q). □
Corollary 4.13. We have ‖R∗
n,k,l ‖ ⩽ C(q), where R∗
n,k,l is viewed as an operator from H ⊗n+k+l
q
to H ⊗n
q ⊗ H ⊗k
q ⊗ H ⊗l
q .
Proof. By Lemma 4.8 we can express R∗
n,k,l as ( R∗
n,k ⊗ Idl)R∗
n+k,l , and then we can appeal to the
lemma above. □
Proof of Proposition 4.5. Let µ ∈ H ⊗m
q and consider Ψ a,b (µ ). According to Proposition 4.9 we
have
Ψ a,b (µ ) =−2
∑
j,r,s
rqr(m−j−s)m13
r m12
s m23
j (R∗
n−r−s,r,s (ξ)⊗ R∗
s,m −s−j,j (µ )⊗ R∗
j,r,k −j−r(η )).
We may assume that r /greaterorequalslant1 (otherwise the corresponding summand is equal to zero), so the
(absolute value of the) factor qr(m−j−s) is bounded above by |q|m, up to a constant depending
on q, n, and k. As each of j, r, and s is bounded by either n or k, the range of summation is
ﬁnite, so it suﬃces to bound uniformly the norm of each summan d. If we treat R∗
n,k as a map
from H ⊗n+k
q to H ⊗n
q ⊗ H ⊗k
q , then each summand in (4.6) should be thought of as an element of
the space H ⊗n−r−s
q ⊗ H ⊗m−s−j
q ⊗ H ⊗k−j−r
q and this norm is bounded by a constant depending on
q and dim( H) (coming from the inner product pairing). Because the norm o f the identity map
Rn−r−s,m −s−j,k −j−r : H ⊗n−r−s
q ⊗ H ⊗m−s−j
q ⊗ H ⊗k−j−r
q → H ⊗m+n+k−2(j+r+s)
q has norm at most
C(q), the norm in H ⊗m+n+k−2(j+r+s)
q is bounded uniformly as well, which ends the proof. □
Theorem 4.14. Suppose that |q| < dim(H)− 1
p . Then the Ornstein-Uhlenbeck quantum Markov
semi-group (Φ t)t≥0 is gradient-Sp. If |q| ⩽ dim(H)− 1
p then (Φ t)t≥0 is immediately gradient-Sp.
Proof. We we will estimate the Sp norm of Ψ a,b by ∑ ∞
m=0‖Ψ a,b
|H ⊗ m
q
‖p. Because dim( H ⊗m
q ) =
dim(H)m, we may estimate ‖Ψ a,b
|H ⊗ m‖p by dim( H)
m
p‖Ψ a,b
|H ⊗ m
q
‖. The bound for this norm is pro-
vided by Proposition 4.5, so we get
‖Ψ a,b‖p ⩽ C(q, ξ, η , dim(H))
∞∑
m=0
(
|q| dim(H)
1
p
) m
.
This series is convergent if |q| < dim(H)− 1
p .
16 MARTIJN CASPERS, YUSUKE ISONO, AND MATEUSZ W ASILEWSKI
If|q| = dim( H)− 1
p , then we want to show that the maps Ψ a,b
t are in Sp for any t > 0. Running
again the same computation, we get the estimate
‖Ψ a,b
t ‖p ⩽ C(q, ξ, η , dim(H))
∞∑
m=0
e−tm
(
|q| dim(H)
1
p
) m
= C(q, ξ, η , dim(H))
n∑
m=0
e−tm,
and this series is convergent. □
