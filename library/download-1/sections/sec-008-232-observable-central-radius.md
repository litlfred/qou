---
doc_id: download-1
doc_title: "Central and L p -concentration of 1-Lipschitz maps into R -trees"
section_id: sec-008-232-observable-central-radius
section_title: "Observable central radius."
section_number: 2.3.2
pages: 9-11
source_pdf: Download (1).pdf
source_sha256: bbb001c909958e8a
toc_source: inferred
doc_brief: "Central and L p -concentration of 1-Lipschitz maps into R -trees — In this paper, we study the Le´vy-Milman concentration phenomenon of 1-Lipschitz maps from mm-spaces to R-trees."
---
Observable central radius.
Let Y be a metric space and assume that  2 B1ðY Þ has the center of mass.
We denote by BY ðy; rÞ the closed ball in Y centered at y 2 Y and with radius
r > 0.
For
any
 > 0,
putting
m :¼ ðY Þ,
we
deﬁne
the
central
radius
CRadð; m  Þ of  as the inﬁmum of  > 0 such that ðBY ðcðÞ; ÞÞ  m  .
Let ðX; dX; XÞ be an mm-space with X 2 B1ðXÞ and Y a centric metric
space. For any  > 0, we deﬁne
ObsCRadY ðX; Þ :¼ supfCRadðfðXÞ; m  Þ j f : X ! Y is a 1-Lipschitz mapg;
and call it the observable central radius of X.
LEMMA 2.16 (cf. [7, Section 3(1/2).31]).
For any  > 0, we have
diamð; m  Þ  2 CRadð; m  Þ:
In particular, we get
ObsDiamY ðX; Þ  2 ObsCRadY ðX; Þ:
REMARK 2.17.
From the above lemma, we see that the central concen-
tration implies the concentration. The converse is not true in general. For
example, let us consider the mm-spaces Xn :¼ fxn; yng with the distance function
dXn given by dXnðxn; ynÞ :¼ n and with the Borel probability measure Xn given by
XnðfxngÞ :¼ 1  1=n and XnðfyngÞ :¼ 1=n. Then, 1-Lipschitz maps fn : Xn ! R
deﬁned by fnðxÞ :¼ dXnðx; xnÞ satisfy that cððfnÞðXnÞÞ ¼ 1 for all n 2 N, whereas
the maps fn concentrate to 0 and ObsDiamRðXn; Þ ! 0 as n ! 1 for any
 > 0.
LEMMA 2.18.
Let  2 B1ðRnÞ with m :¼ ðRnÞ. Then, for any p  1 and
 > 0, we have
CRadð; m  Þ 
VpðÞ
ðmÞ1=p :
ð2:1Þ
In the case of p ¼ 2, we also have the better estimate
CRadð; m  Þ  V2ðÞ
ﬃﬃﬃﬃﬃﬃﬃﬃﬃ
2m
p
:
ð2:2Þ
Central and Lp-concentration of 1-Lipschitz maps into R-trees
491
PROOF.
We shall prove that ðRn n BRnðcðÞ; 0ÞÞ   for 0 :¼ VpðÞ=
ðmÞ1=p. Suppose that ðRn n BRnðcðÞ; 0ÞÞ > . From Lemma 2.11, we get
Z
Rn jcðÞ  xjpdðxÞ  VpðÞp
m
:
Hence, by Chebyshev’s inequality, we see that
VpðÞp
m
¼ p
0 <
Z
Rn jcðÞ  xjpdðxÞ  VpðÞp
m
;
which is a contradiction. Therefore, we obtain ðBRnðcðÞ; 0ÞÞ  m   and so
(2.1).
Since
Z
Rn jcðÞ  xj2dðxÞ ¼ V2ðÞ2
2m
;
the same argument yields (2.2). This completes the proof.

COROLLARY 2.19.
Let X be an mm-space with X 2 B1ðXÞ. Then, for any
p  1, we have
ObsCRadRnðX; Þ 
1
ðmÞ1=p Obs Lp-VarRnðXÞ:
ð2:3Þ
In the case of p ¼ 2, we also have the better estimate
ObsCRadRnðX; Þ 
1
ﬃﬃﬃﬃﬃﬃﬃﬃﬃ
2m
p
Obs L2-VarRnðXÞ:
ð2:4Þ
COROLLARY 2.20.
Let X be an mm-space. Then, for any p  1 and  > 0,
we have
SepðX; ; Þ 
2
ðmÞ1=p Obs Lp-VarRðXÞ:
ð2:5Þ
In the case of p ¼ 2, we also have
SepðX; ; Þ 
ﬃﬃﬃﬃﬃﬃﬃﬃ
2
m
r
Obs L2-VarRðXÞ:
ð2:6Þ
492
K. FUNANO
PROOF.
Assume ﬁrst that there is a 1-Lipschitz function f : X ! R such
that fðXÞ =2 B1ðRÞ. From Ho¨lder’s inequality, we have
R
R jx  yjpdfðXÞðyÞ ¼
þ1 for any x 2 X. This implies VpðfÞ ¼ þ1 and so Obs Lp-VarRðXÞ ¼ þ1.
We consider the other case that fðXÞ 2 B1ðRÞ for any 1-Lipschitz function
f : X ! R. Combining Proposition 2.4 with Lemma 2.16 and (2.3), we have
SepðX; ; Þ 
2
ðm0Þ1=p Obs Lp-VarRðXÞ
for any  > 0 > 0. Letting 0 ! , we have (2.5). Replacing (2.3) with (2.4) in the
above argument, we also obtain (2.6).

