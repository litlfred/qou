---
doc_id: download-1
doc_title: "Central and L p -concentration of 1-Lipschitz maps into R -trees"
section_id: sec-010-4-the-necessity-in-proposition-212-for-r-trees
section_title: "The necessity in Proposition 2.12 for R-trees."
section_number: 4
pages: 13-16
source_pdf: Download (1).pdf
source_sha256: bbb001c909958e8a
toc_source: inferred
doc_brief: "Central and L p -concentration of 1-Lipschitz maps into R -trees — In this paper, we study the Le´vy-Milman concentration phenomenon of 1-Lipschitz maps from mm-spaces to R-trees."
---
The necessity in Proposition 2.12 for R-trees.
In order to prove the main theorems, we extend the necessity in Proposition
2.12 to R-trees:
PROPOSITION 4.1.
Let T be an R-tree and  2 B1ðTÞ. Then, we have
Central and Lp-concentration of 1-Lipschitz maps into R-trees
495
ccðÞ;T 0ðÞ  0 for any T 0 2 C 0
TðcðÞÞ.
PROOF.
For simplicity, we assume that ðTÞ ¼ 1. We shall approximate
the measure  by a measure whose support lies on a simplicial tree in T. Given
n 2 N, there exists a compact subset Kn  T such that ðT n KnÞ < 1=n and
R
TnKn dTðcðÞ; wÞdðwÞ < 1=n. Take a ð1=nÞ-net fzn
i gln
i¼1 of Kn with mutually
diﬀerent elements such that dTðcðÞ; zn
1Þ < 1=n. We then take a sequence fAn
i gln
i¼1
of mutually disjoint Borel subset of Kn such that zn
i 2 An
i , An
i  BTðzn
i ; 1=nÞ, and
Kn ¼ Sln
i¼1 An
i .
Deﬁne
the
Borel
probability
measure
n
on
fzn
i gln
i¼1
by
nðfzn
1gÞ :¼ ðAn
1Þ þ ðT n KnÞ and nðfzn
i gÞ :¼ ðAn
i Þ for i  2.
CLAIM 4.2.
dW
1 ðn; Þ ! 0 as n ! 1.
PROOF.
We shall show that
lim
n!1
Z
T
dTðcðÞ; wÞdnðwÞ ¼
Z
T
dTðcðÞ; wÞdðwÞ:
ð4:1Þ
Since
Z
T
dTðcðÞ; wÞdnðwÞ ¼
X
ln
i¼1
dTðcðÞ; zn
i ÞðAn
i Þ þ dTðcðÞ; zn
1ÞðT n KnÞ;
we have
Z
T
dTðcðÞ; wÞdnðwÞ 
X
ln
i¼1
dTðcðÞ; zn
i ÞðAn
i Þ

 < 1
n2 :
ð4:2Þ
By An
i  BTðzn
i ; 1=nÞ, we get
X
ln
i¼1
dTðcðÞ; zn
i ÞðAn
i Þ 
Z
Kn
dTðcðÞ; wÞdðwÞ


ð4:3Þ
¼
X
ln
i¼1
Z
An
i
fdTðcðÞ; wÞ  dTðcðÞ; zn
i ÞgdðwÞ

 
X
ln
i¼1
Z
An
i
dTðw; zn
i ÞdðwÞ  1
n :
Hence, combining (4.2) with (4.3) and
Z
Kn
dTðcðÞ; wÞdðwÞ 
Z
T
dTðcðÞ; wÞdðwÞ

 
Z
TnKn
dTðcðÞ; wÞdðwÞ < 1
n ;
496
K. FUNANO
we obtain (4.1). The same way as the above proof shows that the sequence fng1
n¼1
converges weakly to the measure . Therefore, by using Lemma 2.14, this
completes the proof of the claim.

Applying Claim 4.2 to Theorem 2.15, we get cðnÞ ! cðÞ as n ! 1. Since
the convex hull in T of the set fzn
i gln
i¼1 is a simplicial tree with ﬁnite vertex set and
cðnÞ is contained in the convex hull by Proposition 2.13, it follows from
Proposition 2.12 that c eT;cðnÞðnÞ  0 for any eT 2 C 0
TðcðnÞÞ. Let T 0 2 C 0
TðcðÞÞ.
Assume ﬁrst that cðnÞ 2 T n T 0 for inﬁnitely many n 2 N. Then, taking Tn 2
C 0
TðcðnÞÞ with T 0  Tn, we have
cT 0;cðÞðnÞ  cTn;cðnÞðnÞ þ dTðcðnÞ; cðÞÞ  dTðcðnÞ; cðÞÞ:
Therefore, we obtain cT 0;cðÞðÞ ¼ limn!1 cT 0;cðÞðnÞ  0.
We
consider
the
other
case
that
cðnÞ 2 T 0
for
any
n 2 N.
Let
zn 2 ½cðÞ; cð1ÞT be the unique point such that
dTðzn; cðnÞÞ ¼ inffdTðz; cðnÞÞ j z 2 ½cðÞ; cð1ÞTg:
Since cðnÞ 2 T 0 for all n 2 N and cðnÞ ! cðÞ as n ! 1, by taking a subse-
quence, we may assume that dTðcðÞ; znþ1Þ  dTðcðÞ; znÞ for any n 2 N. For each
n  2, we take Tn 2 C 0
TðznÞ and eTn 2 C 0
TðcðnÞÞ such that cð1Þ 2 Tn and cð1Þ 2
eTn. Observe that Tn  Tnþ1. Since Tn  eTn, we have
cTn;znðnÞ  c eT;cðnÞðnÞ þ dTðcðnÞ; znÞ  dTðcðnÞ; znÞ:
ð4:4Þ
We also easily see
CLAIM 4.3.
T 0 n fcðÞg ¼ S1
n¼2 Tn.
The same proof as Claim 4.2 implies that
sup
Z
A
dTðzn; wÞdnðwÞ
Z
A
dTðzn; wÞdðwÞ

jAT is a Borel subset


!0 as n!1:
Combining this with (4.4) and Claim 4.3, we obtain
cT 0;cðÞðÞ ¼ lim
n!1 cTn;znðÞ ¼ lim
n!1 cTn;znðnÞ  lim
n!1 dTðcðnÞ; znÞ ¼ 0:
This completes the proof of the proposition.

Central and Lp-concentration of 1-Lipschitz maps into R-trees
497
The author does not know whether the converse of Proposition 4.1 holds or
not.
