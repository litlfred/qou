---
doc_id: arxiv-math-0611181v2
doc_title: "Proof of the volume conjecture for Whitehead chains Roland van der Veen"
section_id: sec-001-proof-of-the-main-theorem
section_title: "Proof of the main theorem"
section_number: null
pages: 3-6
source_pdf: 0611181v2.pdf
source_sha256: 6931e3ebca584de9
doc_brief: "Proof of the volume conjecture for Whitehead chains Roland van der Veen — We prove the volume conjecture for an inﬁnite family of links called White- head chains that generalizes both the Whitehead"
---
In this section we give an overview of the proof of the main theorem, postponing
the proofs of the more technical lemmas to the next section.
The ﬁrst step is to obtain an expression for the colored Jones polyn omials
of a general Whitehead chain.
Lemma 1. Let a,b,c,d be integers, with b ≥ 2 and c,d ≥ 0. We have the
following formulas for the colored Jones polynomial:
JN (Wa, 1,c,d )(e
2πi
N ) = φN
N −1∑
n=0
(2n + 1)χ4a−c+d
N,n
( N −1−n∑
k=0
Sn,k
) c+d
JN (Wa,b,c,d )(e
2πi
N ) = 0 when N is even and for N = 2M + 1 we have:
JN (Wa,b,c,d )(e
2πi
N ) = φNN bχ4a−c+d
N,M
( M∑
k=0
SM,k
) c+d
Where we deﬁne φN = exp
(
(N −1)(c−d)
N πi
)
ifc+d = 1 andφN = (−1)(N −1)(c−d)
otherwise, and we deﬁne χ and S by
χN,n = exp
( n(n + 1 −N )
2N πi
)
, S n,k =
n∏
j=1
2 sin2( (k+j)π
N )
sin( jπ
N )
3
Proof. Recall that the unnormalized N -colored Jones invariants are intertwining
operators of VN ⊗VN , where VN corresponds to the N -dimensional irreducible
representation of sl2. Using the decomposition VN ⊗VN = ⨁ N −1
n=0 V2n+1 one
can write the unnormalized colored Jones invariants of the tangles in ﬁgure 1 in
the following way [11]:
˜JN (t) =
N −1⨁
n=0
Tangle(n,t ) · idV2n+1
were the function Tangle( n,t ) depends on the tangle and t = eh. If we deﬁne
[n] = t
n
2 −t− n
2
t
1
2 −t− 1
2
then the functions for the tangles in ﬁgure 1 are:
T(n,t ) = tn(n+1), B(n,t ) = [N (2n + 1)]
[2n + 1]
C(n,t ) = t(N 2−1)/ 2+N (N −1)/ 2
N −1−n∑
k=0
t−N (n+k)
n∏
j=1
(1 −tN −j−k)(1 −tj+k)
1 −tj
The colored Jones polynomials of the mirror-images of these tangles are obtained
by replacing t by t−1. The factor t(N 2−1)/ 2 in the formula for C( n,t ) is a
correction due to framing that should be included only if both strand s in the
clasp belong to the same component. For Whitehead chains this mean s that it
should be included only when c +d = 1.
By the multiplicativity of the colored Jones invariant with respect to c om-
position of tangles we can now calculate the colored Jones polynomial of all
Whitehead chains. The general formula for the normalized version o f the col-
ored Jones polynomial of the Whitehead chains is:
JN (Wa,b,c,d )(t) =
N −1∑
n=0
[2n + 1]
[N ] T(n,t )aB(n,t )bC(n,t )cC(n,t −1)d
The factor [2n+1]
[N ] comes from the normalization and from taking the closure of
composition of the tangles.
Routine calculations now yield the above formulas.
From now on we will use the shorthand JN,a,b,c,d =JN (Wa,b,c,d )(e
2πi
N ).
The next step in proving the main theorem is to investigate the asymp totics
of the above formulas for the colored Jones polynomials as N → ∞. The factors
Sn,k turn out to play a crucial role because they dominate the absolute v alue
of the ( n,k )-th term. There exists a unique maximum ˜SN = S⌊ N
2 ⌋, ⌊ N
4 ⌋ for
the Sn,k . This term dominates all others so that most of the asymptotics of
JN,a,b,c,d can be read oﬀ from this term only. In order to make this precise we
need to compare the other values of Sn,k to the maximum value.
4
Let us choose a ﬁxed number δ ∈ ( 1
2, c+d+5
2(c+d+4) ) once and for all, where the
numbers c and d are the parameters of Wa,b,c,d . Deﬁne n′ = |n −
⌊ N
2
⌋
| and
k′ = |k −
⌊ N
4
⌋
| to be the distances from the maximum. The next lemma shows
how we can estimate the other values of Sn,k .
Lemma 2. Using the above deﬁnitions of n′,k ′ and δ we have:
a) If n′ +k′<N δ then Sn,k ˜S−1
N = exp(− π
N (n′2 + 2n′k′ + 2k′2)) + O(N 3δ−2), as
N → ∞.
b) There areC,ǫ> 0 such that if n′ +k′ ≥N δ thenSn,k ˜S−1
N <C exp(−ǫN 2δ−1)
In lemma 3 the asymptotics of the maximum value ˜SN are expressed using the
Lobachevski function Λ( θ) = −
∫ θ
0 log |2 sin(x)|dx.
Lemma 3. ˜SN ∼ exp
( 4N
π Λ( π
4 ) − 1
2 log 2N
)
, N → ∞
The asymptotics of JN,a, 1,c,d is reduced to that of ˜SN by the following lemma.
By CS we mean the constant deﬁned in the statement of the main the orem.
Lemma 4. There is a nonzero constant C ∈ C such that:
JN,a, 1,c,d ∼CN (c+d+3)/ 2 ˜Sc+d
N e
iCS
2π , N → ∞
There is a similar lemma for the case b ≥ 2. We conﬁne ourselves to the odd-
colored Jones polynomials, since the even ones are 0 in e
2πi
N . In lemma 5 we
reduce the asymptotics of the odd colored Jones polynomial to tho se of the
maximal term ˜SN :
Lemma 5. Forb ≥ 2 and N odd we have: JN,a,b,c,d ∼
exp
(
−(c +d) log
√
2 + (4a + 3c − 3d)πi/4
)
N (c+d+2b)/ 2 ˜Sc+d
N e
iCS
2π
Postponing the proofs of these lemmas to the next subsection we c an now prove
the main theorem.
Proof. (of the main theorem)
Using an explicit decomposition of the complement into ideal octahedr a it can
be shown that Vol( Wa,b,c,d ) = 8(c +d)Λ( π
4 ), see [10]. Let us ﬁrst suppose that
b = 1. According to lemma 4 there is a constant C′ such that we have:
JN,a, 1,c,d ∼ exp
(
log( ˜Sc+d
N ) + c +d + 3
2 log(N ) +Ni CS
2π +C′
)
Using lemma 3 we get:
∼ exp 1
2π ((Vol(Wa, 1,c,d ) +iCS)N + 3π log(N ) +E), N → ∞
The case b ≥ 2 follows in the same way by combining lemma 3 and lemma 5.
5
