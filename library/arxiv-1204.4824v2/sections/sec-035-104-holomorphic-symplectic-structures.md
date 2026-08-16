---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-035-104-holomorphic-symplectic-structures
section_title: "Holomorphic symplectic structures"
section_number: 10.4
pages: 66-67
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
In this section we explain one of the important properties of Ψ W: both its domain and
codomain are holomorphic symplectic, and ΨW is a holomorphic symplectic map,
Ψ∗
W(ϖC) =ϖΣ. (10.17)
We begin withM(Σ,GL (1); m). The easiest way to understand its holomorphic sym-
plectic form is to recall that on the space of untwisted connections there is a standard such
form [51, 52]. This form, formally speaking, is obtained by symplectic quotient from
ϖΣ =
∫
Σ
δα∧δα (10.18)
– 64 –
where α denotes the abelian connection 1-form. 31 Using a choice of spin structure on Σ
to relate twisted and untwisted connections we can transfer this holomorphic symplectic
structure toM(Σ,GL (1); m); by abuse of notation we denote that structure also as ϖΣ.
Similarly,MF (C,GL (K); m) has symplectic form obtained by symplectic quotient
from
ϖC =
∫
C
TrδA∧ δA (10.19)
withA the nonabelian connection 1-form. Again we use a spin structure on C to pass
between twisted and untwisted connections.
To see why (10.17) is true, ﬁrst consider variations δα which have support away from
the spectral networkW. In this case the corresponding variation ofA is simplyδA =π∗δα.
It follows easily that for such variations we have ϖΣ(δα,δα′) = ϖC(δA,δA′). If δα has
support intersectingW then the situation is slightly more involved: there is a distribution-
valued contribution to δA supported on W. By a gauge transformation δα→ δα + dχ
we may assume however that δα vanishes in neighborhoods of joints. So it is enough to
consider what happens in a patch intersecting only a single wall pc ofW. Taking local
coordinates (x,y ) on C where pc is the locus y = 0, one ﬁnds the form
δA =π∗δα +s(x)δ(y)dy, (10.20)
where in the decomposition (10.10) s(x) is oﬀ-diagonal and π∗δα diagonal. One thus has
Tr(s(x)dy∧π∗δα′) = 0, so the last term in (10.20) does not contribute to ϖ; we get once
again ϖΣ(δα,δα′) =ϖC(δA,δA′).
