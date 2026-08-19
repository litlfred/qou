---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-144-7b-proofs-of-technical-lemmas
section_title: "7B. Proofs of technical lemmas"
section_number: null
pages: 278-280
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
Proof of Lemma 5.2. This argument originates in [Heath-Brown 2013, §4] and is similar but not identical
to lemmas in [Heath-Brown and Pierce 2015; Pierce 2016]; for completeness we provide an argument.
The ﬁrst property in Lemma 5.2 is a direct result of the deﬁnition of A(m). Since each A(m) is a
nonnegative integer,
∑
m
A(m)≤
∑
m
A(m)2,
and it sufﬁces to prove the third property. We write
∑
m
A(m)2=
∑
m
#
{
p, p′, a, a′: mi≤ Ni− aiq
p < mi+ Hi/P, mi≤ Ni− a′
iq
p′ < mi+ Hi/P
}
≪
( n∏
i=1
Hi
P
)
#
{
p, p′, a, a′: 0≤
⏐⏐⏐⏐
Ni− aiq
p − Ni− a′
iq
p′
⏐⏐⏐⏐≤ Hi/P
}
=‖ H‖P−n ∑
p,p′∈P
M(p, p′), (7-11)
where
M(p, p′)= #
{
a, a′, 0≤ ai< p, 0≤ a′
i< p′: 0≤
⏐⏐⏐⏐
Ni− aiq
p − Ni− a′
iq
p′
⏐⏐⏐⏐≤ Hi/P
}
.
First consider p= p′. Then
M(p, p)≤ #
{
a, a′:|(Ni− aiq)−(Ni− a′
iq)|≤ p(Hi/P)≤ 2Hi, i= 1,..., n
}
≤ #
{
a, a′:| ai− a′
i|≤ 2Hi/q< 2, i= 1,..., n
}
.
Here we have used Hi< q. This shows that once a is chosen, there are at most 3n choices for a′, so that
M(p, p)≪ Pn and hence∑
p=p′∈P M(p, p′)≪ Pn+1, which sufﬁces for our desired bound for (7 -11).
Next, consider the case p⁄= p′. For each i= 1,..., n we choose (by Bertrand’s postulate) a prime li
such that
q
Hi
< li≤ 2q
Hi
.
(Here we use the assumption that Hi< q for each i.) For each i, let Mi=[ Nili/q] or Mi=[ Nili/q]+ 1,
so that li ∤ Mi. Then|Nili/q− Mi|≤ 1 implies that|Ni− q Mi/li|≤ q/li, so that
M(p, p′)≪ #
{
a, a′:
⏐⏐⏐⏐
q Mi/li− aiq
p − q Mi/li− a′
iq
p′
⏐⏐⏐⏐≤ Hi
P+ q
li p+ q
li p′, i= 1,..., n
}
≪ #
{
a, a′:|(p′− p)Mi−(ai p′− a′
i p)li|≤ 12P, i= 1,..., n
}
.
Burgess bounds for short character sums evaluated at forms 1945
Given p, p′ and an integer δ, for each ﬁxed index i there is at most one way to choose ai, a′
i with
0≤ ai< p, 0≤ a′
i< p′ such that ai p′− a′
i p=δ. Thus
∑
p⁄= p′∈P
M(p, p′)≪ #
{
p⁄= p′∈ P, u=(u1,..., un),|ui|≤ 12P: Mi(p′− p)≡ ui(modli), i= 1,..., n
}
.
Now we use the fact that li ∤ Mi. Thus for a ﬁxed i, the condition Mi(p′− p)≡ ui(mod li) determines
p′− p uniquely modulo li, and hence uniquely in Z, as long as P < li, which is guaranteed by the
assumption P< q/Hi, that is P Hi< q. In particular, there is at most one value for the difference p′− p
that will satisfy all n conditions. So we may choose p freely and then p′ is determined. As a result, after
counting up the possible choices for u, we conclude that
∑
p⁄= p′∈P
M(p, p′)≪ Pn+1.
Applying this in (7-11), we conclude that
∑
m
A(m)2≪‖ H‖P. □
Proof of Lemma 6.4. We may restrict our attention to permutations that map {1,..., M} to itself, or
equivalently, we may suppose going forward that M= n. For indeed, any indices i that occur in the sums
such that i≤ M butσ(i)> M, clearly contribute no more to the left-hand side than to the right-hand side,
since ti≤ tσ(i).
Now letσ be the permutation that minimizes
a1tσ( 1)+···+ antσ( n); (7-12)
if there is more than one such permutation, we choose σ to be the one with the greatest number of
ﬁxed points. We will show that σ is the identity. For suppose otherwise, and let i be the smallest index
such thatσ(i)⁄= i. Thenσ(i)> i and hence tσ(i)≥ ti. Furthermore, denoting by k the index such that
σ( k)= i, we must also have that k> i and hence ak≤ ai. We then see that(tσ(i)− ti)(ai− ak)≥ 0, or
equivalently, tσ(i)ai+ tiak≥ tiai+ tσ(i)ak. Deﬁne a new permutation σ′ byσ′(u)= u for u= 1,..., i,
σ′(k)= σ(i), and σ′(u)= σ( u) for all the remaining u∈{ i+ 1,..., n}\{ k}. Then we see that
tσ(i)ai+ tσ( k)ak≥ tσ′(i)ai+ tσ′(k)ak so that (7-12) does not increase in value if we replace σ byσ′, andσ′
must also be a minimizer. Yetσ′ has one more ﬁxed point than σ , which is a contradiction. We conclude
thatσ is the identity. □
Proof of Lemma 7.1. By the deﬁnition of the θ j, the sum over j= 0, 1,..., n− 1 takes the form
1+
n−1∑
j=1
q j/2K
−θ j
1 = 1+
n−2∑
j=1
q j/2K− jθ1
1 + q(n−1)/2K−(r−1)
1 ≤ 1+
n−1∑
j=1
(q1/2K−θ1
1 ) j (7-13)
in which θ1=⌊(r− 1)/(n− 1)⌋. Here we have used the fact that for j= n− 1, θn−1= r− 1≥
(n− 1)⌊(r− 1)/(n− 1)⌋= (n− 1)θ1. Now we see from the right-most expression that under the
1946 Lillian B. Pierce and Junyan Xu
assumption (7-3), all terms j≥ 2 are dominated by j= 0, 1. On the other hand, we see from the middle
expression that if (7-3) does not hold, then that expression is≫ 1, as claimed.
It remains to examine the terms with j= n, which we divide into the even and odd cases. For n≥ 2
even, the j= n term is
qn/2(K1··· Kn/2)−(2r−1)≤ qn/2K−(2r−1)n/2
1 ≤(q1/2K−θ1
1 )n,
where we have used the orderingK1≤ K2≤···≤ Kn and the fact that(2r−1)(n/2)≥n(r−1)/(n−1)≥nθ1
holds when n≥ 2. Thus the above expression is≪ 1 under the assumption (7-3).
For n≥ 3 odd, the j= n term is
qn/2(K1··· K(n−1)/2)−(2r−1)K−r
(n+1)/2≤ qn/2K−{(2r−1)(n−1)/2+r}
1 ≤(q1/2K−θ1
1 )n,
upon verifying that n≥ 2 sufﬁces to show that(2r− 1)(n− 1)/2+ r≥ n(r− 1)/(n− 1)≥ nθ1. Under
the assumption (7-3) we see that the j= n term is also≪ 1. This concludes the proof of Lemma 7.1. □
