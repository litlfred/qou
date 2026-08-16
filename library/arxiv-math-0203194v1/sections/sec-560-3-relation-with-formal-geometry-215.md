---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkaidˆo lectures in Arithmetic Geometry Yves Andr´ e (with appendices by F. Kato and N. Tsuzuki)"
section_id: sec-560-3-relation-with-formal-geometry-215
section_title: "RELATION WITH FORMAL GEOMETRY. 215"
section_number: 3
pages: 219-221
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry Yves André (with appendices by F. Kato and N. Tsuzuki) — 580 sections: INTRODUCTION; INTRODUCTI"
---
respectively. We glue them as U =V−1 and get U1∪ U2→ D1 = SpfR{T},
which is the formal blow-up along the ideal ( π,T ). Meanwhile, the analytic
reduction is obtained by gluing the following two aﬃne sets:
U 1 = Spec k [T ],
U 2 = Spec k [T,V ]/(TV ),
this is the normal crossing of the aﬃne line with coordinate T and the
projective line with the inhomogeneous coordinate V .
We are going to state the Raynaud’s theorem, which provides a close
relationship between rigid geometry and formal geometry; w e need some
terminology:
Deﬁnition 3.10 (Admissible formal scheme) . An R-formal scheme (2) X is
said to be admissible if it is Zariski locally isomorphic to admissible Spf A
with A admissible in the sense of Deﬁnition 3.4.
Deﬁnition 3.11 (Admissible formal blow-up) . Let X be an admissible for-
mal scheme. An admissible formal blow-up of X is the formal blow-up along
a coherent open ideal I⊂O X, i.e.,
X′ = lim
− →
λ
Proj
∞⨁
n=0
(
In⊗OXOX/πλ
)
−→ X.
We are going to construct the functor from the category of adm issible
formal schemes to the category of rigid analytic spaces; let us start by ob-
serving the aﬃne case. From an aﬃne admissible formal scheme X = SpfA,
it is easy to get the corresponding rigid analytic space: we j ust set
Arig : = A⊗RK
which is an aﬃnoid algebra over K. If A is presented asA =R{t1,... ,t n}/a,
then K{t1,... ,t n}/aK{t1,... ,t n} gives a presentation of Arig.
To globalize, we need to see the compatibility with localiza tion. Let us
consider the completed localization A{f−1} ofA with respect to f∈A. The
corresponding aﬃnoid algebra is
A{f−1}⊗ RK = A{T}/(1−Tf )⊗RK
= Arig{T}/(1−Tf ) = Arig{f−1},
and the latter is the aﬃnoid algebra attached to the rational subdomain
{x∈ SpmArig|| f|≥ 1};
this means that the completed localization of formal scheme s just corre-
sponds to the localization of rigid spaces with respect to th e G-topology. So
we globalize the recipe as above to obtain the functor
Rig : X↦→Xrig
from admissible formal R-schemes to K-rigid analytic spaces. The rigid
analytic space Xrig is called the Raynaud generic ﬁber of X.
(2)We follow [ EGA I , §10] for generalities of formal schemes.
216 A. RAPID COURSE IN p-ADIC ANALYSIS.
Proposition 3.12. The functor Rig maps admissible formal blow-up’s of ad-
missible formal schemes to isomorphisms of rigid analytic s paces.
Proof. This has already been essentially shown just before the Slog an.
Indeed, we may limit ourselves to the aﬃne case, for the cente rs of blow-up’s
are coherent. We have seen in this case that the Raynaud gener ic ﬁber of
admissible formal blow-up’s is the decomposition into rati onal subdomains,
which does not change the analytic structure.
Now we state the theorem of Raynaud:
Theorem 3.13 (Raynaud 1972). The functor gives the equivalence of the
following categories,
(i) the category of quasi-compact admissible formal R-schemes, localized
by admissible formal blow-up’s,
(ii) the category of quasi-compact and quasi-separated rig id analytic spaces
overK.
The reader ﬁnds a nice comprehensive account of the proof of t his the-
orem in [ BL93].
4. T opology of Rigid Analytic Space.
In this section, we assume, for simplicity, that K is algebraically closed.
Deﬁnition 4.1. (1) A rigid analytic space X is said to be quasi-compact
if every admissible covering of X has a ﬁnite admissible reﬁnement.
(2) A rigid analytic space X is said to be connected if there is no admis-
sible covering{Ui}i∈I of X such that
⋃
i∈I1
Ui∩
⋃
i∈I2
Ui =∅ and
⋃
i∈I1
Ui⁄=∅⁄=
⋃
i∈I2
Ui
for some non-empty subsets I1,I 2⊆I with I =I1⊔I2.
Since admissible coverings of aﬃnoids are ﬁxed as ﬁnite, eve ry aﬃnoid
is quasi-compact. So, we see that a rigid analytic space is qu asi-compact
if and only if it is a ﬁnite union of aﬃnoids. It is easy to see th at a rigid
analytic space X is connected if and only if the ring Γ( X,OX ) has no other
idempotent than 0 and 1.
Deﬁnition 4.2. A morphism π : Y → X of rigid analytic spaces over K
is said to be an analytic covering if there exists an admissible covering (3)
{Xi}i∈I of X such that for each i∈I π−1(Xi) is isomorphic to the disjoint
union of copies of Xi. A connect rigid analytic space X is said to be simply
connected if there is no other connected analytic covering over X than the
trivial one id : X→X (cf. [ vdP87]).
(3)or else a topological covering, referring to the Grothendie ck topology; cf. Chapter I,
§§1.4
