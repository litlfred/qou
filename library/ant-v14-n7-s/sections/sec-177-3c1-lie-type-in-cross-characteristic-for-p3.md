---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory"
section_id: sec-177-3c1-lie-type-in-cross-characteristic-for-p3
section_title: "3C1. Lie type in cross-characteristic for p=3"
section_number: null
pages: 302-308
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
toc_source: outline
---
type in nondeﬁning characteristic. That is, we deal with the case S is of the form G/Z(G) for G a ﬁnite
group of Lie type of simply connected type deﬁned over a ﬁeld Fq with 3∤q. (Given Proposition 3.8, this
will complete the proof of parts (i) and (ii) of Theorem 3.7.)
We will use 8m to denote the m-th cyclotomic polynomial in the variable q. Note that using e.g.,
[Malle 2007, Lemma 5.2], 3 divides 8m if and only if m = 3id for some i ≥0, where d is the order of q
modulo 3, and in this case 3 ∥8m unless m = d.
Proposition 3.9. Let S be a simple group of Lie type deﬁned over Fq with 3∤q and assume S is not one of
the groups PSLϵ
n(q) with n ≤3. Then there exist three nontrivial characters χ1, χ2, χ3 ∈Irr3′(B0(S))σ1
such that χ1 and χ2 extend to Aut(S).
Further, if S is not PSLϵ
4(q) nor PSp4(2a) with a odd, then χ1, χ2, and χ3 may be chosen to extend to
Aut(S).
Proof. We may assume that S is not isomorphic to one of the groups considered in Proposition 3.8.
Keep the notation and considerations for G, ˜G, ˜T, and ˜S from Section 3A. By the work of Lusztig
[1988], the unipotent characters of ˜G are trivial on Z( ˜G) and restrict irreducibly to G. Further, when
viewed as characters of ˜S, they are extendible to Aut(S), by [Malle 2008, Theorems 2.4 and 2.5], aside
from some speciﬁc exceptions. The only unipotent characters which take irrational values occur for
exceptional groups and have values in Q(
√
−1, ζ3, ζ5, √q), where ζ3 and ζ5 are third and ﬁfth roots of
unity, respectively, by [Geck 2003, Proposition 5.6 and Table 1]. In any case, the unipotent characters are
σ1-invariant, since √q is a sum of roots of unity of order relatively prime to 3.
Let d be the order of q modulo 3. In particular, we have d = 1 or 2. If d = 1, unipotent characters of
degree relatively prime to 3 are constituents of the Harish-Chandra induced character R ˜G
˜T (1) using [Malle
Galois action on the principal block and cyclic Sylow subgroups
1969
Type
Condition on d
Character
χ(1)
(notation from [Carter 1985, 13.9])
G2(q)
d = 1
φ2,2
1
2q82
286
φ1,3′
1
3q8386
d = 2
G2[1]
1
6q82
186
φ1,3′
1
3q8386
3D4(q)
d = 1, 2
φ1,3′
q812
φ1,3′′
q7812
F4(q)
d = 1
φ4,1
1
2q82
282
688
φ8,3′
q382
488812
d = 2
B2,ϵ
1
2q1382
182
388
B2,1
1
2q82
182
388
E6(q)
d = 1, 2
φ20,2
q2848588812
φ20,20
q20848588812
2E6(q)
d = 1, 2
φ4,1
q28488810812
φ4,13
q208488810812
E7(q)
d = 1, 2
φ7,1
q87812814
φ7,46
q4687812814
E8(q)
d = 1, 2
φ8,1
q82
488812820824
φ35,2
q28587810814815820830
2B2(q),
Note: 3∤|S|
2B2[a]
1
√
2q(q2 −1)
q2 = 22m+1
2B2[b]
1
√
2q(q2 −1)
2F4(q),
Note: 3 | (q2 + 1)
cusp
1
12q482
182
2(8′
8)2812(8′
24)2
q2 = 22m+1
cusp
1
12q482
182
2(8′′
8)2812(8′′
24)2
Table 2. Some unipotent characters in Irr3′(B0(S))σ1 for exceptional types with 3∤q.
2007, Corollary 6.6]. Further, by [Enguehard 2000, Theorem A], all members of R ˜G
˜T (1) lie in the same
block, namely B0( ˜G).
If d = 2, then the centralizer of a Sylow d-torus is a maximal torus, using e.g., [Malle and Späth 2016,
Lemma 3.2]. Unipotent blocks of ˜G are parametrized by certain ˜G-conjugacy classes of pairs ( ˜L, λ)
where ˜L is a d-split Levi subgroup of ˜G and λ is a d-cuspidal unipotent character of ˜L, by [Enguehard
2000, Theorem A]. Further, a unipotent character in the block parametrized by ( ˜L, λ) can have 3′-degree
1970
Noelia Rizo, A. A. Schaeﬀer Fry and Carolina Vallejo
n
Additional Condition on n, e
Partition
χ(1)q′
n ≥6
e = 2 and n even; or
(1, n −1)
qn−1−ϵn−1
q−ϵ
e = 1 and 3∤(n −1)
(1n−2, 2)
n ≥6
e | n and 3∤n
(2, n −2)
(qn−ϵn)(qn−3−ϵn−3)
(q−ϵ)(q2−1)
(1n−4, 2, 2)
n ≥6
3 | n; or
(1, 1, n −2)
(qn−1−ϵn−1)(qn−2−ϵn−2)
(q−ϵ)(q2−1)
e = 2 and n odd and 3 | (n −2)
(1n−3, 3)
n ≥6
e = 2 and n odd and 3 | (n −1)
(1, 1, 2, n −4)
(qn−ϵn)(qn−2−ϵn−2)(qn−3−ϵn−3)(qn−5−ϵn−5)
(q−ϵ)2(q2−1)2(q2+1)
(2, n −2)
(qn−ϵn)(qn−3−ϵn−3)
(q−ϵ)(q2−1)
n = 5
e = 1
(1, 4)
(q + ϵ)(q2 + 1)
(1, 1, 1, 2)
n = 5
e = 2
(2, 3)
q5−ϵ
q−ϵ
(1, 1, 3)
(q2 + 1)(q2 + ϵq + 1)
n = 4
e = 2
(1, 3)
q2 + ϵq + 1
(1, 1, 2)
n = 4
e = 1
(2, 2)
q2 + 1
Table 3. Some unipotent characters in Irr3′(B0(S))σ1 for type Aϵ
n−1(q) with n ≥4 and 3∤q.
only when ˜L is the centralizer of a Sylow d-torus, using [Malle 2007, Corollary 6.6]. This yields that
again in the case d = 2, there is a unique block of ˜G containing unipotent characters of 3′-degree.
Hence when 3∤q, every unipotent character in Irr3′( ˜G) is a member of Irr3′(B0( ˜G))σ1, and restricts to
a member of Irr3′(B0(G))σ1 trivial on the center. Then this restriction may be viewed as an element of
Irr3′(B0(S))σ1, using e.g., [Cabanes and Enguehard 2004, Lemma 17.2].
In particular, since the Steinberg character has degree a power of q, it sufﬁces to ﬁnd two more unipotent
characters of 3′-degree that are not one of the exceptional cases in [Malle 2008, Theorem 2.5]. In what
follows, we will use the notation and degrees for unipotent characters as in [Carter 1985, Sections 13.8
and 13.9].
Exceptional Types. In the case that S is an exceptional group of Lie type deﬁned over Fq with 3∤q, we
list in Table 2 two unipotent characters invariant under Aut(S) that have degree relatively prime to 3,
completing the proof in this case.
Types An−1 and 2An−1, n ≥4. In this case, let S be PSLϵ
n(q) with n ≥4 and ϵ ∈{±1}. Write e ∈{1, 2}
for the number such that q ≡ϵe (mod 3). That is, e is the order of ϵq modulo 3. Two unipotent characters
are in the same 3-block of ˜G = GLϵ
n(q) if and only if they have the same e-core (see [Fong and Srinivasan
Galois action on the principal block and cyclic Sylow subgroups
1971
1982]). For n ≥5 or for (n, e) = (4, 2), the unipotent characters described in Table 3 are Aut(S)-invariant
members of Irr3′(B0(S))σ1.
Now assume n = 4 and e = 1. Then the unipotent character in the last line of Table 3 is an Aut(S)-
invariant member of Irr3′(B0(S))σ1. In this case, 1S, StS, and the character listed are the only unipotent
characters in Irr3′(S). However, since e = 1, we see that every unipotent character is a member of the
principal block of ˜G, which means that E3( ˜G, 1) is comprised of only one block. Let ζ ∈F×
q2 with order 3.
Then taking s to be the element diag(ζ, ζ, ζ, 1) of ˜G∗∼= GLϵ
4(q), the semisimple character χs ∈E( ˜G, s)
lies in the principal block of ˜G and is trivial on Z( ˜G) since s ∈SLϵ
4(q) ∼= [ ˜G∗, ˜G∗]. Further, we see using
Lemma 3.1 that χs is ﬁxed by σ1.
Since C ˜G∗(s) ∼= GLϵ
1(q) × GLϵ
3(q), we see
χs(1) = (q + ϵ)(q2 + 1).
Further, since the semisimple classes of ˜G are determined by their eigenvalues and Z( ˜G) is comprised of
scalar matrices, we see that s is not conjugate to sz for any nontrivial z ∈Z( ˜G). Hence χs|G is irreducible,
by the second-to-last paragraph of Section 3A, and is therefore a member of Irr3′(B0(G)), since the
principal block of G is the only block covered by the principal block of ˜G. But since Z(G) ≤Z( ˜G) is
in the kernel of χs, this character is therefore a member of Irr3′(B0(G/Z(G)))σ1 = Irr3′(B0(S))σ1, again
using [Cabanes and Enguehard 2004, Lemma 17.2]. Note that this character is not Aut(S)-conjugate to
1S, StS, nor the unipotent character labeled by (2, 2), which completes the proof for S = PSLϵ
n(q) with
n ≥4.
Types Bn and Cn, n ≥2. When S is type Bn or Cn with n ≥2 deﬁned in characteristic different than 3,
Table 4 exhibits at least two distinct unipotent characters in Irr3′(B0(S))σ1 that are Aut(S)-invariant, with
the exception of the case S = PSp4(2a) with a odd. In the latter situation, we may instead consider the
characters indexed by
  1 2
0

and
 0 1 2
∅

with degrees q
2(q2 +1) and q
2(q −1)2, respectively. (Note that we
do not consider PSp4(2) ∼= S6.) These characters lie in Irr3′(B0(S))σ1 and the latter character extends to
Aut(S). (However, we remark that the ﬁrst character is not Aut(S)-invariant, as in this case it is switched
with
  0 1
2

under the action of the graph automorphism, by [Malle 2008, Theorem 2.5]).
Type Dn and 2Dn, n ≥4. In this case, if S is not D4(q), Tables 5 and 6 list at least two distinct unipotent
characters that are Aut(S)-invariant members of Irr3′(B0(S))σ1. If S is D4(q) and 3 | (q −1), we may
instead take the unipotent characters labeled by symbols
  1
0
3
2

and
 3
1

with χ(1)q′ = 1
2(q + 1)3(q3 + 1)
and (q2 + 1)2, respectively. When 3 | (q + 1), we may take the characters index by
 3
1

and
  0 1 2 3
∅

, the
latter of which satisﬁes χ(1)q′ = 1
2(q −1)3(q3 −1).
□
We next establish Theorem 3.7 for the case that S has cyclic Sylow 3-subgroups, which we recall from
Proposition 3.6 occurs when S = PSL2(q) for 3∤q and when S = PSLϵ
3(q) for 3 | (q + ϵ).
Proposition 3.10. Let S = PSL2(q) with 3∤q or PSLϵ
3(q) with 3 | (q + ϵ). Then there exist nontrivial
χ1, χ2 ∈Irr3′(B0(S))σ1 such that χ1 extends to Aut(S).
1972
Noelia Rizo, A. A. Schaeﬀer Fry and Carolina Vallejo
Conditions on q, n
Symbol
χ(1)q′  possibly excluding factors of 1
2

3 | (q −1) or
3 | (q + 1); n even; 3∤(n −1) or
  0 1
n

(qn−1+1)(qn+1)
q+1
3 | (q + 1); n odd; 3∤n
3 | (q −1); 3∤n
  0 2
n−1

(q2n−1)(qn−3+1)(qn−1+1)
q4−1
3 | (q −1); 3∤(n −1) or
  1 n
0

(qn−1−1)(qn+1)
q−1
3 | (q + 1); n even
3 | (n −1)
  1 n−1
1

(q2n−1)(q2(n−2)−1)
(q2−1)2
3 | (q + 1); n odd or
  0 n
1

(qn−1+1)(qn−1)
q−1
3 | (q −1); 3∤n
3 | (q + 1); n odd; 3 | n or
3 | (q + 1); n even; 3 | (n −2) or
  0 1 n
1 2

(q2(n−1)−1)(qn−1)(qn−2+1)
(q2−1)2
3 | (q −1); 3 | (n −2)
Table 4. Some unipotent characters in Irr3′(B0(S))σ1 for type Bn(q) and Cn(q) with
n ≥2 and 3∤q.
Proof. First let S = PSL2(q) with 3∤q. In this case, every character of S is either 3-defect zero or has
degree prime to 3. As before, the Steinberg character is a member of Irr3′(B0(S))σ1 and extends to Aut(S).
Further, the only two unipotent characters, 1 ˜G and St ˜G, both lie in the principal block of ˜G = GL2(q),
and hence there is a unique unipotent block of ˜G. We may take χ1 = StS as before.
Now, let s ∈˜G = GL2(q) have eigenvalues ζ, ζ −1, where ζ ∈F×
q2 has order 3. Then the semisimple
character χs ∈E( ˜G, s) ⊆E3( ˜G, 1) lies in the principal block of ˜G and is trivial on Z( ˜G) since s ∈
SL2(q) ∼= [ ˜G∗, ˜G∗]. Since sz is not conjugate to s for 1̸ = z ∈Z( ˜G∗), we also see χs is irreducible on
restriction to G. Further, Lemma 3.1 yields that χs is ﬁxed by σ1. Then the restriction (χs)G lies in
B0(G) since the principal block of ˜G covers a unique block of G. Finally, in this case χs(1) = q + η,
where η ∈{±1} is such that 3 | q −η. Hence this character may be viewed as a member of Irr3′(B0(S))σ1,
arguing as before.
Now let S = PSLϵ
3(q) with 3 | (q + ϵ). Then
S = G = SLϵ
3(q)
and
˜G∗∼= ˜G = G × Z( ˜G).
Since the unipotent characters of G are 1G, StG, and a character of degree q(q + ϵ), we see that again
B0(G) is the only unipotent block of maximal defect (as the other has defect zero). Then every character
of E3(G, 1) with 3′-degree is a member of B0(G). We may again take χ1 = StG. Taking s ∈˜G∗to have
Galois action on the principal block and cyclic Sylow subgroups
1973
Conditions on q, n
Symbol
χ(1)q′  possibly excluding factors of 1
2

3∤(n −1)
  1 n
0 1

q2(n−1)−1
q2−1
3 | n
  1 2 n
0 1 2

(q2(n−2)−1)(q2(n−1)−1)
(q2−1)2(q2+1)
3 | (n −2) or
  n−2
2

(q2(n−1)−1)(qn−1)(qn−4+1)
(q2−1)2(q2+1)
3 | (q + 1); 3 | n; n odd
3 | (q −1); 3 | (n −1) or
  1 n−1
0 2

(qn−1)(qn−2−1)(qn−1+1)(qn−3+1)
(q−1)2(q2+1)
3 | (q + 1); n odd
3 | (q −1); 3 | (n −2) or
3 | (q + 1); 3∤n; n even or
  0 n−1
1 2

(qn−1)(qn−2+1)(qn−1−1)(qn−3+1)
(q2−1)2
3 | (q + 1); 3 | n; n odd
3 | (q −1); 3∤n or
  n−1
1

(qn−1)(qn−2+1)
q2−1
3 | (q + 1); 3 | (n −1) or
3 | (q + 1); 3 | (n −2); n even or
3 | (q + 1); 3 | n; n odd
Table 5. Some unipotent characters in Irr3′(B0(S))σ1 for type Dn(q) with n ≥5 and 3∤q.
eigenvalues {ζ, ζ −1, 1}, where ζ ∈F×
q2 has order 3, the corresponding character of G has degree q3 −ϵ,
and we may again view (χs)G as a character of Irr3′(B0(S))σ1.
□
Proposition 3.11. Let S = PSLϵ
3(q) with 3 | (q −ϵ). Then there exist nontrivial χ1, χ2, χ3 ∈Irr3′(B0(S))σ1
such that χ1 and χ2 extend to Aut(S).
Proof. In this case, we see that all three unipotent characters are members of Irr3′( ˜G) and that there
is a unique unipotent block B0( ˜G). Further, the unipotent characters are rational-valued, and therefore
are members of Irr3′(B0( ˜G))σ1. Then we may take χ1 and χ2 to be the restrictions to G (viewed as a
character of S) of the two nontrivial unipotent characters.
The semisimple element s ∈˜G∗with eigenvalues {ζ, ζ −1, 1}, where ζ ∈F×
q2 has order 3, is now
conjugate to sz where z = ζ · I3 ∈Z( ˜G∗). The corresponding semisimple character has degree χs(1) =
(q + ϵ)(q2 + ϵq + 1), so χs ∈Irr(B0( ˜G))σ1 satisﬁes 3 ∥χs(1) and is not irreducible on restriction to G.
Then the constituents of the restriction to G are members of Irr3′(B0(G)), and are trivial on Z(G) since
s ∈[ ˜G∗, ˜G∗] ∼= G, so it sufﬁces to see that they are also σ1-invariant, using the character table available
in CHEVIE.
□
Together, Propositions 3.9 through 3.11 yield Theorem 3.7 for the simple groups of Lie type in
nondeﬁning characteristic, completing parts (i) and (ii).
1974
Noelia Rizo, A. A. Schaeﬀer Fry and Carolina Vallejo
Conditions on q, n
Symbol
χ(1)q′  possibly excluding factors of 1
2

3∤(n −1)
  0 1 n
1

q2(n−1)−1
q2−1
3 | (n −1) or
  1 n−1
∅

(qn+1)(qn−2−1)
q2−1
3 | (q −1); 3 | n or
3 | (q + 1); 3 | n; n even or
3 | (q + 1); 3 | (n −2); n odd
3 | (q −1); 3∤(n −1) or
3 | (q + 1); 3 | (n −2) or
  2 n−2
∅

(q2(n−1)−1)(qn+1)(qn−4−1)
(q2−1)2(q2+1)
3 | (q + 1); 3 | n; n even
3 | n
  0 1 2 n
1 2

(q2(n−1)−1)(q2(n−2)−1)
(q2−1)2(q2+1)
3 | (q −1); 3 | (n −1)
3 | (q + 1); 3∤n; n odd
  1 2 n−1
0

(qn+1)(qn−1+1)(qn−2−1)(qn−3−1)
(q2−1)2
3 | (q + 1); 3 | n; n even
3 | (q −1); 3 | n
3 | (q + 1); 3 | (n −1); n even
  0 1 n−1
2

(qn+1)(qn−1−1)(qn−2−1)(qn−3+1)
(q2−1)2
3 | (q + 1); 3 | (n −2); n odd
Table 6. Some unipotent characters in Irr3′(B0(S))σ1 for type 2Dn(q) with n ≥4 and 3∤q.
