---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-097-64-the-ﬁbres-of-multiple-abel-jacobi-maps-143
section_title: "The ﬁbres of multiple Abel-Jacobi maps 143"
section_number: 6.4
pages: 151-152
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
THEOREM 6.6. There exists a Zariski-open dense subset U⊆ X such
that for u∈U(C) the ﬁbre F= f−1α (u) is smooth of Euler characteristic
χ(F) = ( −1)d−g ∑
c1,...,cn≥0
c1+···+cn=g
g!
c1!···cn!
n
∏
k=1
(2(g−1−ck)
dk−ck
).
Proof. SinceCα is smooth, the morphismfα : Cα−→X restricts to a
smooth morphism over some Zariski-open dense subsetU⊆ X. Then in
particular the ﬁbreF = f−1α (u) is smooth for allu∈ U(C). Furthermore,
if i : F ↪→ Cα denotes the embedding of such a ﬁbre, we have an exact
sequence of tangent bundles
0−→TF−→i∗(TCα)−→i∗(f∗
α(TX))−→0.
SinceTX is the trivial bundle, it follows thatct(F) =i∗(ct(Cα)). Hence the
Gauss-Bonnet formula and the projection formula show that
(i) χ(F) = degF(cd−g(F)) = degCα([F]·cd−g(Cα))
where[F]∈ H2g(Cα) denotes the fundamental class ofF. To compute the
Chern polynomial ofCα =Cd1×···× Cdn, note that the tangent bundle of
this direct product splits as
TCα = p∗
1(TCd1)⊕···⊕ p∗
n(TCdn)
so thatct(Cα) =∏n
k=1 p∗
k(ct(Cdk))in the ringH•(Cα)[t]. For the Chern class
in question this implies
(ii) cd−g(Cα) = ∑
c1,...,cn≥0
c1+···+cn=g
n
∏
k=1
p∗
k(cdk−ck(Cdk)).
Now consider the fundamental class[F] of the ﬁbreF = f−1α (u). The class
of a point is [u] = 1
g![Θ]g = η1··· ηg by the Poincar´e formula, using the
notations of the previous section. By the above remarks about the K¨unneth
isomorphism we havef∗α(ηi) = f∗α(λi)· f∗α(λg+i) = ∑n
k,l=1 p∗
k(λi)· p∗
l (λg+i)
so that
(iii) [F] = f∗
α [u] =
n
∑
k1,...,kg=1
l1,...,lg=1
g
∏
i=1
p∗
ki(λi)· p∗
li(λg+i).
In view of corollary 6.5 the only summands in (iii) which possibly have a
non-zero cup product with (ii) are those withki = li for alli. By the same
corollary, each of these summands gives in (i) the contribution
n
∏
k=1
(2(g−1−ck)
dk−ck
) where ck = #{i| ki = k}.
144 Chapter 6 – The generic rank of Brill-Noether sheaves
Finally, forc1, . . . ,cn∈ N0 withc1 +··· +cn = g there are precisely g!
c1!···cn!
partitions of{1, . . . ,g} inton disjoint subsets of sizec1, . . . ,cn, so there are
precisely as many corresponding choices ofk1, . . . ,kg. □
