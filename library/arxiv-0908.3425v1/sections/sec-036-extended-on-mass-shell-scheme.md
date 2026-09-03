---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer"
section_id: sec-036-extended-on-mass-shell-scheme
section_title: "Extended on-mass-shell scheme"
section_number: null
pages: 62-64
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer — We provide an introduction to the basic concepts of chiral pe rturbation theory and discuss some"
---
In the following, we will concentrate on yet another solutio n which has been motivated in Ref.
[Gegelia and Japaridze, 1999] and has been worked out in deta il in Ref. [Fuchs et al., 2003a]. The cen-
tral idea of the extended on-mass-shell (EOMS) scheme consi sts of performing additional subtractions
beyond the ~MS scheme such that renormalized diagrams satisfy the power counting. Terms violating
the power counting are analytic in small quantities and can t hus be absorbed in a renormalization of
counter terms.
In order to illustrate the approach, let us consider a simpli ﬁed version of the integral H, namely its
value in the chiral limit,
H(p2,m 2, 0;n) = −i
∫ dnk
(2π)n
1
[(k −p)2 −m2 +i0+](k2 +i0+),
where
∆ = p2 −m2
m2 = O(q)
is a small quantity. Applying the power-counting rules of Se c. 4.2.2, we want the renormalized integral
to be of order D =n − 1 − 2 = n − 3. Introducing C(z, ∆) = z2 − ∆ z(1 −z) −i0+, we obtain
H(p2,m 2, 0;n) = κ(m;n)
∫ 1
0
dz [C(z, ∆)]
n
2 −2, (228)
where κ(m;n) is given in Eq. (220). For the purpose of evaluating the inte gral of Eq. (228) we write
∫ 1
0
dz [C(z, ∆)]
n
2 −2 = (−∆)
n
2 −2
∫ 1
0
dzz
n
2 −2
(
1 − 1 + ∆
∆ z
) n
2 −2
and apply Eqs. 15.3.1 and 15.3.4 of Ref. [Abramowitz and Steg un, 1972] to obtain
H(p2,m 2, 0;n) = κ(m;n)
Γ
(
n
2 − 1
)
Γ
(
n
2
) F
(
1, 2 − n
2 ;n
2 ; p2
m2
)
, (229)
where F (a,b ;c;z) is the hypergeometric function [Abramowitz and Stegun, 19 72]. In order to discuss
the power-counting properties of H (in the chiral limit) in terms of ∆, we make use of Eq. 15.3.6 of
Ref. [Abramowitz and Stegun, 1972] to re-write Eq. (229) as
H(p2,m 2, 0;n) = mn−4
(4π)
n
2

Γ
(
2 − n
2
)
n − 3 F
(
1, 2 − n
2 ; 4 −n; −∆
)
+(−∆) n−3 Γ
(n
2 − 1
)
Γ(3 −n)F
(n
2 − 1,n − 2;n − 2; −∆
)]
. (230)
62
Making use of
F (a,b ;c;z) = 1 + ab
c z + a(a + 1)b(b + 1)
c(c + 1)
z2
2 + · · · (231)
for |z| < 1 and the fact that ∆ counts as a small quantity of O(q), we immediately see that the ﬁrst
term of Eq. (230) contains a contribution which does not sati sfy the above power counting, i.e., which
is not proportional to O(q) as n → 4. Using the expansion of Eq. (231) together with Γ(1 + x) = xΓ(x)
we obtain, as n → 4,
H = mn−4
(4π)
n
2

 Γ
(
2 − n
2
)
n − 3 +
(
1 − p2
m2
)
ln
(
1 − p2
m2
)
+
(
1 − p2
m2
)2
ln
(
1 − p2
m2
)
+ · · ·

, (232)
where · · · refers to terms which are at least of O(q3) or O(n − 4). Note that we count a term of the
type −∆ ln( −∆) as O(q). If we subtract
mn−4
(4π)
n
2
Γ
(
2 − n
2
)
n − 3 (233)
from Eq. (232) we obtain as the renormalized integral
HR(p2,m 2, 0;n) = mn−4
(4π)n/2


(
1 − p2
m2
)
ln
(
1 − p2
m2
)
+
(
1 − p2
m2
)2
ln
(
1 − p2
m2
)
+ · · ·

. (234)
The subtracted term of Eq. (233) is local in the external mome ntump, i.e., it is a polynomial inp2 and
can thus be obtained by a ﬁnite number of counter terms in the m ost general eﬀective Lagrangian.
We have seen in Eq. (230) that the one-loop integral is of the t ype
H ∼F (n, ∆) + ∆ n−3G(n, ∆) ,
where F and G are hypergeometric functions and are analytic in ∆ for any n. The observation central
for the setting up of a systematic method is the fact that the p art proportional to F can be obtained
by ﬁrst expanding the integrand in small quantities and then performing the integration for each term
[Gegelia et al., 1994] (see Sec. 4.3.5 for an illustration of the general method). We now apply a conven-
tional renormalization prescription which allows us to ide ntify those terms which we subtract from a
given integral without explicitly calculating the integral beforehand. In essence we work wit h a modiﬁed
integrand which is obtained from the original integrand by s ubtracting a suitable number of counter
terms. The meaning of suitable in the present context will be explained in a moment. To that end we
consider the series
∞∑
l=0
(p2 −m2)l
l!


(
1
2p2pµ
∂
∂pµ
)l
1
[k2 − 2k ·p + (p2 −m2) +i0+](k2 +i0+)


p2=m2
= 1
(k2 − 2k ·p +i0+)(k2 +i0+)
⏐
⏐
⏐
⏐
⏐
p2=m2
+(p2 −m2)
[
1
2m2
1
(k2 − 2k ·p +i0+)2 − 1
2m2
1
(k2 − 2k ·p +i0+)(k2 +i0+)
− 1
(k2 − 2k ·p +i0+)2(k2 +i0+)
]
p2=m2
+ · · ·, (235)
where [· · ·]p2=m2 means that we consider the coeﬃcients of (p2−m2)l only for four-momentapµ satisfying
the on-mass-shell condition. Although the coeﬃcients stil l depend on the direction of pµ, after integra-
tion of this series with respect to the loop momentum k and evaluation of the resulting coeﬃcients for
63
p2 =m2, the integrated series is a function of p2 only. In fact, as was shown in Ref. [Gegelia et al., 1994],
the integrated series exactly reproduces the ﬁrst term of Eq . (230). At this point we stress that
−i
∫ dnk
(2π)n
1
(k2 − 2k ·p +i0+)(k2 +i0+)
⏐
⏐
⏐
⏐
⏐
p2=m2
and [
−i
∫ dnk
(2π)n
1
(k2 − 2k ·p +p2 −m2 +i0+)(k2 +i0+)
]
p2=m2
are not the same for n ≤ 3.
The formal deﬁnition of the EOMS renormalization scheme is t hen as follows: we subtract from the
integrand of H(p2,m 2, 0;n) those terms of the series of Eq. (235) which violate the powe r counting.
These terms are always analytic in the small parameter and do not contain infrared singularities. In
the above example we only need to subtract the ﬁrst term. All t he higher-order terms contain infrared
singularities. For example, the last term of the second coeﬃ cient would generate a behavior k3/k4 of
the integrand for n = 4. The integral of the ﬁrst term of Eq. (235) is given by Eq. (2 33), and we end
up with Eq. (234) for the renormalized integral:
HR =H −Hsubtr = O(qn−3).
Since the subtraction point is p2 = m2, the renormalization condition is denoted “extended on-ma ss-
shell” (EOMS) scheme in analogy with the on-mass-shell reno rmalization scheme in renormalizable
theories. In the general case including the pion mass, one wo uld consider the series
1
(k2 − 2k ·p +i0+) (k2 +i0+)
⏐
⏐
⏐
⏐
⏐
p2=m2
+ (p2 −m2)
[
1
2m2
1
(k2 − 2k ·p +i0+)2 + · · ·
]
p2=m2
+M 2 1
(k2 − 2k ·p +i0+) (k2 +i0+)2
⏐
⏐
⏐
⏐
⏐
p2=m2
+ · · ·
instead of Eq. (235). However, it would still be only the cont ribution resulting from the ﬁrst term that
were to be subtracted.
Within the EOMS framework it is straightforward to obtain a c onsistent power counting in mani-
festly Lorentz-invariant baryon ChPT including, e.g., vector mesons [Fuchs et al., 2003b] or the ∆(1232)
resonance [Hacker et al., 2005] as explicit degrees of freed om. Moreover, the infrared regularization
of Becher and Leutwyler can be reformulated in a form analogo us to the EOMS renormalization
scheme and can thus be applied straightforwardly to multi-l oop diagrams with an arbitrary number of
particles with arbitrary masses [Schindler et al., 2004a] ( see also Refs. [Lehmann and Prezeau, 2002],
[Bruns and Meißner, 2005], [Bruns and Meißner, 2008]). The a pplication of both infrared and extended
on-mass-shell renormalization schemes to multi-loop diag rams was explicitly demonstrated by means of
a two-loop self-energy diagram [Schindler et al., 2004b].
