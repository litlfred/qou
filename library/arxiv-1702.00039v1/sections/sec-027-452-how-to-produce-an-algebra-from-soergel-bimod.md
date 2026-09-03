---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY"
section_id: sec-027-452-how-to-produce-an-algebra-from-soergel-bimod
section_title: "How to produce an algebra from Soergel bimodules"
section_number: 4.5.2
pages: 26-27
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
doc_brief: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
Let us introduce the
Notation 4.4 If p =∑
iaivi∈N[v,v−1] and M is a graded bimodule, we will
denote byp·M the graded bimodule
⨁
i∈Z
M(i)⊕ai
26
One can see that Soergel bimodules encode all the information of the Hecke
algebra. Let us try to make this idea more precise. Consider the following
“algebra”NB(S3) overN[v,v−1] (this is not a ring because it lacks of additive
inverse, soNB(S3) is strictly speaking not an algebra, but apart from this “de-
tail” it satisﬁes all the other deﬁning properties of an algebra): the elements
of NB(S3) are Soergel bimodules modulo isomorphism. We denote by ⟨M⟩
the isomorphism class of M . In this algebra, the sum is deﬁned to be direct
sum⟨M⟩ +⟨N⟩ := ⟨M⊕ N⟩, the product is deﬁned to be tensor product
⟨M⟩·⟨ N⟩ :=⟨MN⟩ and multiplication byv is shifting your graded bimodule
by 1, i.e. v·⟨M⟩ :=⟨M(1)⟩.
Proposition 4.5 There is an isomorphism of “algebras”
NB(S3)∼=
⨁
w∈S3
N[v,v−1]bw⊂H =
⨁
w∈S3
Z[v,v−1]bw
⟨Bw⟩↦→ bw.
Proof The equations (19), (20), (21), (22) and Proposition 4.3 tell us that the
multiplication rules in both algebras are equal. The only problem that might
appear is that NB(S3) might not be free as a N[v,v−1]- module over the set
⟨Bw⟩w∈S3 , i.e. one might have that
∑
w∈S3
pw⟨Bw⟩∼=
∑
w∈S3
qw⟨Bw⟩
with pw,q w ∈ N[v,v−1]. But this is not possible because we have that the
category of Z-graded ﬁnitely generated R-bimodules (or, what is the same,
R⊗RR-modules) admits the Krull-Schmidt Theorem. For a proof see [Pi, Sec-
tion 5.4].
