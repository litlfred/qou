---
doc_id: arxiv-hep-th-9303139v2
doc_title: "ITFA 93-10 March 1993 A.Morozov"
section_id: sec-040-14-therefore-it-could-be-reasonable-to-use-a-diﬀ
section_title: "Therefore it could be reasonable to use a diﬀerent notation: Ln instead of L2n. We"
section_number: 14
pages: 35-39
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
doc_brief: "ITFA 93-10 March 1993 A.Morozov — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
prefer L2n, because it emphasises the property of the model to be 2-reduction of KP
hierarchy (to KdV), see section 4 below.
32
The ﬁrst two terms together are equal to the sum over all j (including j = i):
−1
2
X
δ
1
λγ −λδ

λ
−a−3
2
γ
−λ
−a−3
2
δ

= 1
2
X
δ
λ
a+ 3
2
γ
−λ
a+ 3
2
δ
λγ −λδ
·
1
λ
a+ 3
2
γ
λ
a+ 3
2
δ
=
=
1
2λa+2
γ
X
δ
λa+2
γ
−λ
1
2γ λ
a+ 3
2
δ
λγ −λδ
·
1
λ
a+ 3
2
δ
.
Similarly, the next two terms can be rewritten as
1
2
X
δ
λ−a−2
γ
q
λγ + √λδ
=
1
2λa+2
γ
X
δ
q
λγ −√λδ
λγ −λδ
=
=
1
2λa+2
γ
X
δ
λ
1
2γ λ
a+ 3
2
δ
−λa+2
δ
λγ −λδ
·
1
λ
a+ 3
2
δ
.
The sum of these two expressions is equal to
1
2λa+2
γ
X
δ
λa+2
γ
−λa+2
δ
λγ −λδ
·
1
λ
a+ 3
2
δ
.
Note that powers a + 2 are already integer and the remaining ratio can be
represented as a sum of a+2 terms. Adding also the last term from the l.h.s.
of (2.60), we ﬁnally obtain:
−
1
λa+1
γ
+ 1
2
a
X
n=−1
1
λn+2
γ
X
δ
1
λ
a−n+ 1
2
δ
=
= 1
2
a
X
n=−1
1
λn+2
γ
(2a −2n + 1)(T + r)2a−2n+1
in accordance with (2.58) and (2.59).
2.8
˜W-constraints for the asymmetric 2-matrix model
We turn now to a very diﬀerent application [38] of the GN equation (2.37).
Namely, we shall now consider FV,n{L} as a building block in construction
33
of conventional discrete two-matrix model
ZN{t, ¯t} ≡c2
N
Z
dHd ¯He
P
k(tkTrHk+¯tkTr ¯
Hk)+TrH ¯
H =
=
Z
dLe
P
k tkTrLkF ¯U,N{L}.
(2.61)
Now L plays the role of H and ¯U( ¯H) = P
k ¯tk ¯Hk.
We can now use GN equation to derive a relation for ZN{t, ¯t}.
Take
(2.37),
 
¯U( ∂
∂Ltr
) + L
!
F ¯U,N{L} = 0,
(2.62)
multiply it by eTrU(L) = e
P
k tkTrLk and integrate over L. In order to express
this relation in terms of t-derivatives of z it is necessary to have some ”scalar”
rather than matrix equations, therefore we”ll actually need to take trace of
(2.62). However, in order not to loose any information, we ﬁrst multiply
(2.62) by Ln and then take the trace. In this way we obtain:
Z
dLe
P
k tkTrLkTrLn
 
¯U( ∂
∂Ltr
) + L
!
F ¯U{L} = 0.
Integration by parts gives:
Z
dLF ¯U{L}Tr
 
¯U(−∂
∂Ltr
) + L
!
Lne
P
k tkTrLk.
(2.63)
Now we need to introduce a new class of operators [38]. Consider the
action of Tr ∂m
∂Lm
tr Ln on eTrU(L) = e
P
k tkTrLk. It gives some linear combination
of terms like
trLa1...trLaletrU(L) =
∂l
∂ta1...∂tal
e−trU(L)
i.e. we obtain a combination of diﬀerential operators with t-derivatives, to
be denoted ˜W(t):
˜W (m+1)
n−m (t)etrU(L) ≡Tr ∂m
∂Lm
tr
LnetrU(L),
m, n ≥0.
(2.64)
34
For example,
˜W (1)
n
= ∂
∂tn
,
n ≥0;
˜W (2)
n
=
∞
X
k=0
ktk
∂
∂tk+n
+
n
X
k=0
∂2
∂tk∂tn−k
,
n ≥−1;
˜W (3)
n
=
∞
X
k,l=1
ktkltl
∂
∂tk+l+n
+
∞
X
k=1
ktk
X
a+b=k+n
∂2
∂ta∂tb
+
+
∞
X
k=1
ktk
X
a+b=n+1
∂2
∂ta∂tb+k−1
+
X
a+b+c=n
∂3
∂ta∂tb∂tc
+ (n + 1)(n + 2)
2
∂
∂tn
;
. . .
(2.65)
Note, that while ˜W (1)
n
and ˜W (2)
n
are just the ordinary (U(1)-Kac Moody and
Virasoro operators respectively, the higher ˜W (m)-operators do not coincide
with the generators of the W-algebras: already
˜W (3)
n̸
= W (3) =
∞
X
k,l=1
ktkltl
∂
∂tk+l+n
+ 2
∞
X
k=1
ktk
X
a+b=k+n
∂2
∂ta∂tb
+4
3
X
a+b+c=n
∂3
∂ta∂tb∂tc
.
˜W-operators (in variance with ordinary W-operators) satisfy recurrent rela-
tion:
˜W (m+1)
n
=
∞
X
k=1
ktk ˜W (m)
n+k +
m+n−1
X
k=0
∂
∂tk
· ˜W (m)
n−k,
n ≥−m.
(2.66)
Actually not too much is already known about the ˜W operators and the
structure of ˜
W-algebras (in particular it remains unclear whether the neg-
ative harmonics ˜W (m+1)
n
with n < −m can be introduced in any reasonable
way), see [38] for some preliminary results.
Equation (2.63) can now be represented in terms of the ˜W-operators:
Z
dLF ¯U{L}

X
k≥1
k¯tk
 
−∂
∂Ltr
!k−1
+ L

LneTrU(t) =
=

X
k≥1
(−)k−1k¯tk ˜W (k)
n+1−k + ˜W (1)
n+1

ZN{t, ¯t} = 0.
(2.67)
35
This relation is highly asymmetric in t and ¯t, and in fact it provides a suitable
description of the WI only in the somewhat peculiar case when potential
¯U( ¯H) is a polinomial of finite degree. See refs.[57] and [38] for discussion of
such asymmetric models.
2.9
˜W-constraints for generic 2-matrix model
When both potentials U and ¯U in (2.61) are generic formal seria, eqs.(2.67)
represent only a one-parametric subset of the 2-parametric family of WI.
Before we describe the whole set, let us emphasize that the two-matrix model
(2.61) is the one, where the action is not of the most general form, consistent
with some symmetry. Therefore it is not covariant under arbitrary change
of variables H, ¯H −→f(H, ¯H), ¯f(H, ¯H), and our usual method of derivation
of Ward identities does not work. The reason why generic 2-matrix model
with action containing all the possible combinations Tr(Ha1 ¯Hb1Ha2 ¯Hb2...)
is never considered seriously is essentially our poor understanding of the
unitary-matrix interals for ”non-eigenvalue” theories, to which class such
generic model belongs. For reasons to be explained in the next section such
problems do not arise for the models of the form (2.61) or (2.33), and this is
why they attracted most attention so far. Hopefully the problems with the
unitary-matrix integrals are temporal and this restricted class of multimatrix
models will be unlarged, this should be especially easy to do in the part of
the theory dealing with constraint algebras, but this subject is beyond the
scope of the present notes.
In order to derive the complete set of WI for the model (2.61), we apply
the following semi-artiﬁcial trick. Note that exponential eTrH ¯
H satisﬁes:
