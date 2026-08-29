---
doc_id: arxiv-1105.0091v1
doc_title: "E-mail: meliot@phare.normalesup.org"
section_id: sec-001-3-observables-of-young-diagrams-and-their-cumula
section_title: "Observables of Young diagrams and their cumulants"
section_number: 3
pages: 22-31
source_pdf: 1105.0091v1.pdf
source_sha256: 7d6f72e016b25027
doc_brief: "E-mail: meliot@phare.normalesup.org — In this paper, we review the representation theory of the inﬁnite symmetric group, and we extend the works of Kerov and Vershik by proving that the irreducible"
---
For the asymptotic analysis of Young diagrams, we are basically going to
use a method of moments, but we have to deﬁne precisely what we mean by
the moments of a partition. We shall essentially follow [IO02], and [Śni06b,
FM10] for the combinatorics of cumulants.
3.1 Polynomial functions on Young diagrams
If λ is a partition, we associate to it two ﬁnite alphabetsA(λ) and B(λ)
called theFrobenius coordinates:
A(λ) =
{
λ1− 1
2,λ 2− 3
2,...,λ d− 2d− 1
2
}
;
B(λ) = A(λ′) =
{
λ′
1− 1
2,λ′
2− 3
2,...,λ ′
d− 2d− 1
2
}
.
Here, d is the size of the diagonal ofλ, that is to say the number of boxes of
the Young diagram ofλ that belong to the ﬁrst diagonal.
A central limit theorem for the characters ofS∞ and H (S∞) 23
Example. If λ = (6, 3, 2, 2), its Young diagram is
and the Frobenius coordinates areA ={ 11
2, 3
2} and B ={ 7
2, 5
2} — they are
easily computed by drawing the diagonal and measuring the rows and columns
starting from the diagonal.
The Frobenius momentsof λ are the power sums
pk(λ) = pk
(
A(λ)−B(λ)
)
=
( d∑
i=1
ak
i
)
+ (−1)k−1
( d∑
i=1
bk
i
)
.
For instance,p1(λ) = |λ| for any partition. The functionspk generate freely
over C an algebra called the algebra ofobservables of diagrams, and de-
noted O (cf. [KO94,IO02]). This algebra is isomorphic toSym, and it is nat-
urally graded bydegpk =k. It does not contain all the polynomial functions
of the coordinates of the partitions, but it will prove suﬃciently large5 in our
setting.
We now deﬁne new functions on Young diagrams by renormalizing the
values of the irreducible characters of the symmetric groups. Recall that for
any partitionsλ,µ of the same size,χλ(µ) denotes the value of thenormalized
irreducible character ofSn of labelλ on a permutation of cycle typeµ; thus,
ζλ(µ) = (dim λ)χλ(µ). Then, for any partitionsλ,µ, we set:
Σµ(λ) =
{
n(n− 1)... (n−|µ| + 1)χλ(µ⊔ 1n−|µ|) if n =|λ|≥| µ|,
0 otherwise.
For convenience, we will denoten(n− 1)··· (n−k + 1) = n↓k for anyn and
k — this is the Pochhammer symbol for falling factorials. Thus,Σµ(λ) =
|λ|↓|µ|χλ(µ⊔ 1|λ|−|µ|). An essential result exposed in details in [IO02] is the
following:
Theorem 8. Viewed as a function on Young diagrams,Σµ is an element of
O, and is of degree|µ|. Moreover,
∀µ, Σµ =pµ + (terms of degree at most|µ|− 1),
see [IO02, Proposition 3.4].
5 However, we should mention that there is a bigger algebra of observables of diagrams
that contains O, is isomorphic toQSym and allows to decompose the observables ofO in
combinatorial summands; see in particular [DFŚ10].
24 Pierre-Loïc Méliot
Example. Actually, there is an explicit formula for theΣk’s that is due to
Wassermann ([Was81], [IO02, Proposition 3.3]). Hence, one can computeΣ1 =
p1, Σ2 =p2, Σ3 =p3− 3
2p11 + 5
4p1, Σ4 =p4− 4p21 + 11
2p2.
Theorem 8 implies in particular that the symbolsΣµ factorize in higher degree,
that is to say that for any partitionsµ and ν,
ΣµΣν =Σµ⊔ν + (terms of degree at most|µ| +|ν|− 1).
The next paragraph is devoted to a better description of the productsΣµΣν;
we shall rely on the formalism of partial permutations (cf. [IK99]). To conclude
this paragraph, let us compute the expectation of a symbolΣµ(λ) when λ is
chosen randomly according to a measurePn,ω (we suppose thatn≥|µ|):
En,ω[Σµ(λ)] = n↓|µ| ∑
λ∈Yn
Pn,ω[λ] χλ(µ⊔ 1n−|µ|)
=n↓|µ| ∑
λ∈Yn
sλ(A−B +γE ) ζλ(µ⊔ 1n−|µ|)
=(Frobenius formula ) n↓|µ|pµ⊔1n−|µ| (A−B +γE )
=n↓|µ|pµ(A−B +γE ).
Theorem 8 implies that(Σµ)µ∈Y is a linear basis ofO; hence, by using this
simple formula, we will be able to compute the expectation ofany observable
of diagrams under a coherent measurePn,ω. In particular, we shall compute
in Sections 4 and 5 the joint moments of the Frobenius observablespk; they
will provide information on the geometry of the random partitions under the
probability measures Pn,ω.
3.2 Ivanov-Kerov algebra of partial permutations
If σ∈ S∞, we call admissible set forσ a ﬁnite subsetS⊂ N∗ such that
if x /∈ S, then σ(x) = x. A partial permutation is a pair (σ,S ) with S
admissible set forσ. Said in other words, a partial permutation is a subset
S⊂ N∗ and a permutationσ∈ S(S). One can multiply these objects by the
rule
(σ,S )× (τ,T ) = (στ,S ∪T ).
We denote deg(σ,S ) = card S, and we construct a graded algebra A∞ by
looking at all the formal linear combinations of partial permutations with
bounded degree. For anyn, this algebraA∞ can be projected onto the group
algebra CSn:
πn : A∞→ CSn
(σ,S )↦→
{
σ if S⊂ [ [1,n ] ],
0 otherwise.
A central limit theorem for the characters ofS∞ and H (S∞) 25
There is a natural action ofS∞ on A∞: on the basis elements (σ,S ), it is
deﬁned by
(σ,S )τ = (τστ−1,τ (S)),
and it is compatible with the product of partial permutations. Moreover, two
partial permutations (σ,S ) and (τ,T ) are conjugated if and only ifcardS =
cardT, and the cyclic type ofσ|S is the same as the cyclic type ofτ|T. Thus,
the invariant algebra B∞ = ( A∞)S∞ (called the Ivanov-Kerov algebra)
has a linear basis labelled by partitions of arbitrary size:
B∞ = Vect((Aλ)λ∈Y), with Aµ =
∑
|S|=|µ|
∑
σ∈S(S)
t(σ)=µ
(σ,S ).
Actually, we would rather use a renormalized version of this basis, deﬁned as
follows:
Σµ =
∑[
(a11,...,a 1µ1 )(a21,...,a 2µ2 )··· (ar1,...,a rµr ),{aij}1≤i≤𝓁(µ)
1≤j≤µi
]
where the sum is taken over injective N∗-valued functions i,j ↦→ aij with
1≤i≤𝓁(µ) and 1≤j≤µi.
Proposition 9. The family (Σµ)µ∈Y is a linear basis ofB∞, and for anyn
and any partitionλ∈ Yn,
Σµ(λ) = χλ(πn(Σµ)).
Proof. Here, an irreducible character χλ is extended by linearity from the
group Sn to the algebra CSn. It is not hard to see thatΣµ is a multiple of
Aµ for any partitionµ; hence, (Σµ)µ is indeed a linear basis of B∞. Now,
for anyn, πn(Σµ) consists inn↓|µ| elements of Sn of cycle typeµ⊔ 1n−|µ|,
corresponding to all the possible|µ|-arrangements of theaij’s. Hence,
χλ(πn(Σµ)) = n↓|µ|χλ(µ⊔ 1n−|µ|) = Σµ(λ).
Now, Proposition 9 allows to compute a product of two symbolsΣ in B∞
instead of O. Indeed, for any partitionsλ,µ,ν ,
Σµ(λ)Σν(λ) = χλ(πn(Σµ)) χλ(πn(Σν)) = χλ(πn(Σµ)πn(Σν))
=χλ(πn(Σµ×B∞Σν)) = (Σµ×B∞Σν)(λ)
where we used the fact that for any elementsa,b of the centerZ(CSn) of the
group algebra, and any normalized irreducible characterχλ of Sn, χλ(ab) =
χλ(a)χλ(b)— this is true for any ﬁnite group. With this new point of view, the
combinatorics of the symbolsΣ has been investigated by P. Śniady in [Śni06a,
Śni06b], and later by V. Féray and the author in [FM10]. Thus, one can give
a semi-explicit description of a productΣµΣν by usingpartial matchings.
26 Pierre-Loïc Méliot
To this purpose, let us introduce some additional notations. We denote byAk
the set ofk-arrangements of integers inN∗, and ifA = (a1,...,a k)∈ Ak, we
denote byC(A) the corresponding k-cycle, viewed as a partial permutation
with support{a1,...,a k}. Then,Σµ can be rewritten as
Σµ =
∑
∀i, Ai∈Aµi
∀i⁄=j, Ai∩Aj =∅
C(A1)C(A2)··· C(A𝓁(µ)),
and given two partitionsµ and ν,
ΣµΣν =
∑
∀i, Ai∈Aµi
∀i⁄=j, Ai∩Aj =∅
∑
∀k, Bk∈Aνk
∀k⁄=l, Bk∩Bl=∅
C(A1)··· C(A𝓁(µ))C(B1)··· C(B𝓁(ν)).
To any sequences(aij)i,j and (bkl)k,l appearing in this expression, we associate
a partial matching of the setIA of the (i,j )’s with the setIB of the (k,l )’s:
(i,j )∼ (k,l ) if aij =bkl.
Then, given a partial matchingM of IA with IB, if we sum the products
C(A1)··· C(A𝓁(µ))C(B1)··· C(B𝓁(ν))
corresponding to this partial matching, we obtain a termΣρ(M,µ,ν ): indeed,
if one knows which of theaij’s are equal to which of thebkl’s, then one can
rewrite the product as a product ofdisjoint cycles in a way that does not
depend on the values of thea’ and theb’s (cf. [FM10, §3.4]). Thus:
Lemma 10. For any partitionµ and ν,
ΣµΣν =
∑
M
Σρ(M,µ,ν )
where the sum runs over all the partial matchingsM of IA with IB.
We refer again to [FM10] for more details on this combinatorial lemma. The
reader should also notice that the degree of a termΣρ(M,µ,ν ) corresponding to
a partial matchingM is|µ| +|ν|−| M|, where|M| is the size of the partial
matching, that is to say the number of pairs(a∈IA,b∈IB) in M.
Example. Let us compute the term of higher degree and the subdominant term
of a productΣµΣν.
0. If degΣρ(M,µ,ν ) =|µ| +|ν|, then|M| = 0, andM =∅. The cycles corre-
sponding to the empty matching are disjoint ones; thus, the only term of
degree|µ| +|ν| in ΣµΣν is indeedΣµ⊔ν.
A central limit theorem for the characters ofS∞ and H (S∞) 27
1. If degΣρ(M,µ,ν ) =|µ| +|ν|− 1, then|M| = 1 and M contains only one
pair (a,b ). Suppose thata is in a cycleC(Ai) of lengthµi, and thatb is
in a cycleC(Bj) of lengthνj. Then,C(Ai) andC(Bj) intersect in exactly
one point, so their product is a(µi +νj− 1)-cycle; and all the other cycles
C(Ai′) or C(Bj′) stay disjoint. Thus, such a matching yields a term
Σ(µ⊔ν⊔{µi+νj−1})\{µi,νj},
and one has to sum over all possible matchings of size1 to get the sub-
dominant term ofΣµΣν.
So, for any partitionsµ = (µ1,...,µ r) and ν = (ν1,...,ν s),
ΣµΣν =Σµ⊔ν +
r∑
i=1
s∑
j=1
µiνjΣ(µ⊔ν⊔{µi+νj−1})\{µi,νj}
plus an observable of degree at most|µ|+|ν|− 2. In particular, for two symbols
Σl and Σm corresponding to cycles,
ΣlΣm =Σl,m +lmΣl+m−1 + (observable of degree at mostl +m− 2).
3.3 Śniady’s theory of cumulants of observables
In order to prove results of asymptotic gaussian behaviour in the setting of
the representation theory ofS∞, we shall use in Section 5 Śniady’s theory of
cumulants of observables(cf. [Śni06a,Śni06b]), though in a setting that is
slightly diﬀerent from the setting of his papers, and with another gradation on
the algebra O. IfX1,...,X r are real random variables deﬁned on a common
probability space, we recall that theirjoint cumulantis deﬁned by:
k(X1,X 2,...,X r) = ∂r
∂t1∂t2··· ∂tr
⏐⏐⏐⏐
t=0
log E [exp(t1X1 +t2X2 +··· +trXr)].
In particular, k(X) = E[X] is the expectation and k(X,Y ) = E[XY ]−
E[X] E[Y ] is the covariance. With the deﬁnition given above, it is obvious
that a gaussian vectorX = (X1,...,X n) is characterized by the vanishing
of all the joint cumulants of the coordinates of orderr ≥ 3. On the other
hand, one can give an equivalent combinatorial deﬁnition of the joint cumu-
lants. For any integern, we denote byPn the set ofset partitionsof [ [1,n ] ],
and ifπ = π1⊔π2⊔···⊔ πs is such a set partition, we denote𝓁(π) = s and
µ(π) = (−1)𝓁(π)−1 (𝓁(π)− 1)!. Then,
k(X1,X 2,...,X r) =
∑
π∈Pr
µ(π)


𝓁(π)∏
i=1
E

∏
j∈πi
Xj



.
28 Pierre-Loïc Méliot
Example. For instance, whenr = 3, one has to sum over the5 set partitions
of P3, andk(X,Y,Z ) is equal to
E[XYZ ]− E[XY ] E[Z]− E[XZ ] E[Y ]− E[YZ ] E[X] + 2 E[X] E[Y ] E[Z].
Now, in the algebra of observables of diagramsO, we can in fact deﬁne
three kind of cumulants. First, ifP is a probability law on partitions, then
anyX∈ O can be considered as a random variableX(λ), and one can deﬁne
the joint cumulant of observablesX1,...,X r. That said, one can deﬁne on
O≃ B∞ anewproduct •,called disjointproduct ,andgivenbythefollowing
rule:
∀µ,ν, Σµ•Σν =Σµ⊔ν.
This new product is the restriction toB∞ of the disjoint product of partial
permutations:
(σ,S )• (τ,T ) =
{
(στ,S ⊔T ) if S∩T =∅,
0 otherwise.
We will denote byO• the algebra of observables endowed with this new prod-
uct. Thedisjoint cumulantof some observablesX1,...,X r is then deﬁned
exactly in the same way as for the standard cumulant:
k•(X1,X 2,...,X r) =
∑
π∈Pr
µ(π)

 ∏
i≤𝓁(π)
E


•∏
j∈πi
Xj



.
Finally, we deﬁne theidentity cumulantof observablesX1,...,X r as the
new observable
kid(X1,X 2,...,X r) =
∑
π∈Pr
µ(π)


•∏
i≤𝓁(π)

∏
j∈πi
Xj



.
The three kind of cumulants are related by the following identity, that can be
understood as a computation of expectationvia conditioning, see [Bri69] and
[Śni06b, Lemma 4.8]:
k(X1,...,X r) =
∑
π∈Pr
k•(
kid(Xj∈π1 ),k id(Xj∈π2 ),...,k id(Xj∈π𝓁(π) )
)
.
The expansion of an identity cumulantkid(Σl1,...,Σ lr ) in partial per-
mutations has been computed in [FM10, Lemma 19]. Given arrangements
A1,...,A r, we deﬁne a relation∼ by i∼ j ⇐⇒ Ai∩Aj ⁄=∅. The tran-
sitive cloture of∼ is an equivalence relation, and we denote byπ(A1,...,A r)
the corresponding set partition inPr.
A central limit theorem for the characters ofS∞ and H (S∞) 29
Lemma 11. For anyl1,...,l r,
kid(Σl1,...,Σ lr ) =
∑
∀i, Ai∈Ali
π(A1,...,Ar)=[ [1,r] ]
C(A1)C(A2)··· C(Ar).
Proof. The three kind of cumulants can be deﬁned inductively by the relations:
X1X2··· Xr =
∑
π∈Pr
kid(Xj∈π1 )•kid(Xj∈π2 )•···• kid(Xj∈π𝓁(π) ) ;
E[X1X2··· Xr] =
∑
π∈Pr
k(Xj∈π1 )k(Xj∈π2 )··· k(Xj∈π𝓁(π) ) ;
E[X1•X2•···• Xr] =
∑
π∈Pr
k•(Xj∈π1 )k•(Xj∈π2 )··· k•(Xj∈π𝓁(π) ).
In particular, the ﬁrst relation enables us to prove Proposition 11 by induction
on r, see [FM10, Lemma 19].
Now, the degree inO≃ B∞ is the restriction of the degreedeg(σ,S ) =|S|
of the algebra of partial permutationsA∞. However, in any product of cycles
appearing in the expansion ofkid(Σl1,...,Σ lr ), the joint support of the cycles
C(A1),...,C (Ar) has for cardinality at mostl1 +l2 +··· +lr− (r− 1) —
this is imposed by the conditionπ(A1,...,A r) = [ [1,r ] ]. Hence, Proposition 11
implies that
∀l1,...,l r, degkid(Σl1,...,Σ lr )≤l1 +··· +lr− (r− 1).
This leads to the following estimate, that will be crucial in the proof of our
central limit theorem for the irreducible characters ofS∞.
Theorem 12. Forω∈Ω, we denote bykn,ω and k•
n,ω the cumulant and the
disjoint cumulant of observables with respect to the expectationEn,ω. For any
observables X1,...,X r,
k•
n,ω(X1,...,X r) = O
(
ndegX1+···+degXr−r+1)
;
kn,ω(X1,...,X r) = O
(
ndegX1+···+degXr−r+1)
.
Proof. Because of the multilinearity of cumulants and of some compatibility
relation withrespect to theproducts (see [Śni06b,Theorem4.4]), it issuﬃcient
to prove these estimates for an algebraic basis ofO• or O, so we will suppose
in the following thatXi =Σli with positive integersl1,...,l r≥ 1. Now, notice
that for any partitionµ,
En,ω[Σµ] = pµ(A−B +γE ) n↓|µ| =pµ(A−B +γE ) En,ω[Σ1|µ| ].
30 Pierre-Loïc Méliot
Thus, one can rewrite a disjoint cumulantk•
n,ω(Σl1,...,Σ lr ) as follows:
k•
n,ω(Σl1,...,Σ lr ) =
∑
π∈Pr
µ(π)

 ∏
i≤𝓁(π)
En,ω


•∏
j∈πi
Σlj




=pl1,...,lr (A−B +γE )
∑
π∈Pr
µ(π)

 ∏
i≤𝓁(π)
En,ω


•∏
j∈πi
Σ1lj




=pl1,...,lr (A−B +γE ) k•
n,ω(Σ1l1,...,Σ 1lr ).
So, in order to prove the estimate for disjoint cumulants, it is suﬃcient to treat
the case of observablesΣ1l. However, for these observables, the expectation
En,ω[Σ1l ] = n↓l does not depend onω, and the estimate is simply an algebraic
result on the degree of some polynomial combinations of falling factorials of
n. It has been proved in [Śni06b, Lemma 4.8] that:
k•
n(Σ1l1,...,Σ 1lr ) = O
(
nl1+···+lr−r+1)
.
Thus, the proof is complete for the disjoint cumulants. As for the standard
cumulants, one uses the aforementioned formula:
kn,ω(X1,...,X r) =
∑
π∈Pr
k•
n,ω
(
kid(Xj∈π1 ),k id(Xj∈π2 ),...,k id(Xj∈π𝓁(π) )
)
.
Since the estimate for disjoint cumulants has been proved, it suﬃces now to
show that for any set partitionπ∈ Pr,


𝓁(π)∑
i=1
degkid(Xj∈πi)

−𝓁(π) + 1≤ degX1 +··· + degXr−r + 1.
This is trivial because of Proposition 11:
𝓁(π)∑
i=1
degkid(Xj∈πi)≤
𝓁(π)∑
i=1

∑
j∈πi
degXi−|πi| + 1


≤ degX1 +··· + degXr−r +𝓁(π).
Notice that the estimates of our Theorem can be made independent ofω: in-
deed, for any integersl1,...,l r,|pl1,...,lr (A−B +γE )|≤ 1, and these quantities
are the only ones that depend explicitly onω in our proof.
A particular case of Theorem 12 is whenr = 1; thus,En,ω[X] = O(ndegX ) for
any observableX. This simple fact and the multiplicativity of the irreducible
characters of S∞ will now be used in Section 4, in which we shall recall the
results of Kerov and Vershik (see [KV81a]) and their proofs.
A central limit theorem for the characters ofS∞ and H (S∞) 31
