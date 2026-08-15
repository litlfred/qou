---
doc_id: arxiv-math-0411647v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS"
section_id: sec-009-41-free-cumulants
section_title: "Free cumulants"
section_number: 4.1
pages: 26-27
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear combination of indicators of many"
---
V and a map M : NC(X) → V called the moment map. Usually, the space
V carries some kind of multiplicative structure and there exi sts a sequence
M1, M 2, . . . , called moment sequence, such that for every non–crossing
partition ρ = {ρ1, . . . , ρ r} the moment map is given by a multiplicative
extension
(4.1) Mρ =
∏
1≤s≤r
M|ρ s|.
For every integer n ≥ 1 the Speicher’s free cumulantRn [Spe94, Spe97,
Spe98] is deﬁned by
(4.2) Rn =
∑
ρ∈NC(1,2,...,n )
Moebρcomp Mρ,
where the sum runs over all non–crossing partitions of the se t {1, 2, . . . , n }
and Moeb is the M¨ obius function on the lattice of non–crossing partitions
given explicitly by
Moebσ =
∏
1≤s≤r
(− 1)|σ s|− 1c|σ s |− 1
for σ = {σ 1, . . . , σ r}and where ck = (2k)!
(k+1)!k! denotes the Catalan number.
We are going to use in this article the following deﬁning prop erty of the
M¨ obius function [Spe94].
Lemma 4.1. For every ρ ∈ NC(1, 2, . . . , n )
∑
π ∈NC(1,...,n )
π ≤ρ
Moebπ =
{
1 if ρ is trivial,
0 otherwise.
One can show [Spe94] that if (4.1) holds then the moments can b e com-
puted from the corresponding cumulants by the following sim ple formula
(4.3) Mn =
∑
ρ∈NC(1,...,n )
Rρ ,
where similarly as in (4.1) for every non–crossing partition ρ = {ρ1, . . . , ρ r}
we set
Rρ =
∏
1≤s≤r
R|ρ s|.
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 27
In a typical application the moments Mn are real numbers given by
Mn =
∫∞
− ∞
xn dµ (x),
where µ is a probability measure on R with all moments ﬁnite or given by
Mn = E(Xn), where X is some random variable. It is easy to check that in
this case the free cumulant Rn behaves like a homogeneous polynomial of
degree n in a sense that the free cumulant Rn(Dpµ ) of the dilated measure
is related to the free cumulant Rn(µ ) of the original measure by
Rn(Dpµ ) = pnRn(µ ).
This very simple scaling property is very useful in the study of asymptotic
properties. Another advantage of free cumulants is that thegenerating func-
tion (called V oiculescu’sR–transform [VDN92]) of the sequence of free cu-
mulants of a given measure µ can be computed directly from the Cauchy
transform of µ which is very useful in practical applications.
The deﬁnition of the free cumulants itself does not involve t he multi-
plicative structure of V; this structure is accessed only implicitly through
the moment map M. Therefore a question arises if there are some reason-
able generalizations of (4.1). The key point is that we need t o deﬁne the
moments Mρ only for non–crossing partitions ρ and it is well–known that
non–crossing partitions of n–element set are in correspondence with cer-
tain ways of writing brackets in a product of n factors and hence recursive
deﬁnitions of Mρ can be successfully applied. Canonical examples are pro-
vided by operator–valued free probability [Spe98]. In the following we will
use this weakness of requirements for the moment mapM in order to deﬁne
and study the partition–valued free cumulants.
