---
doc_id: arxiv-math-9804005v3
doc_title: "RINGS WITH AUSLANDER DUALIZING COMPLEXES"
section_id: sec-053-6-noetherian-connected-filtrations
section_title: "Noetherian Connected Filtrations"
section_number: 6
pages: 30-31
source_pdf: 9804005v3.pdf
source_sha256: 62d069533bb97a00
doc_brief: "RINGS WITH AUSLANDER DUALIZING COMPLEXES — A ring with an Auslander dualizing complex is a generalizati on of an Auslander-Gorenstein ring."
---
In this section we use ﬁltrations to transfer results of Sections 4- 5 on connected
graded algebras to non-graded algebras. Throughout the sectio n A denotes a noe-
therian k-algebra.
RINGS WITH AUSLANDER DUALIZING COMPLEXES 31
Suppose a k-module M is given an increasing ﬁltration F = {FnM }n∈Z with⋂
nFnM = 0 and ⋃
nFnM =M . The Rees module is the graded k[t]-module
ReesFM :=
⨁
n∈Z
FnM ·tn ⊂M [t,t −1]
where t is a central indeterminate. It is easy to check that
(ReesFM )/(t − 1) · (ReesFM ) ∼=M
and
(ReesFM )/t · (ReesFM ) ∼= grFM =
⨁
n∈Z
FnM/Fn−1M.
Now let F = {FnA}n∈Z be a ﬁltration of A such that FnA ·FmA ⊂Fn+mA. The
graded k-algebra ReesFA is called the Rees algebra.
Deﬁnition 6.1. If the Rees algebra Rees FA is a noetherian connected graded k-
algebra then F is called a noetherian connected ﬁltration .
Observe that ReesFA is connected graded iﬀ F0A ∼=k,F−1A = 0 and rankkFnA
< ∞. If Rees FA is noetherian then so is the associated graded algebra gr FA. By
[ATV] Theorem 8.2 the converse is also true – if gr FA is noetherian then so is
ReesFA.
A ﬁltration {FnA} on anA-moduleM withFnA·FmM ⊂Fn+mM gives a graded
module ReesFM over ReesFA. We say {FnA} is a good ﬁltration if ReesFM is a
ﬁnitely generated (Rees FA)-module.
The main result of this section is the following theorem. Part 1 is due to Van
den Bergh ([VdB] Theorem 8.6), but there was a subtle ﬂaw in his stat ement: the
shift by −1 was missing.
Theorem 6.2. Let F be a noetherian connected ﬁltration on A and let ˜A :=
ReesFA.
