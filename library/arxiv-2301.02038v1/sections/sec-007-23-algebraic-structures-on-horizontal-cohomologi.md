---
doc_id: arxiv-2301.02038v1
doc_title: "Contemporary Mathematics Vinogradov’s Cohomological Geometry of Partial Diﬀerential Equations"
section_id: sec-007-23-algebraic-structures-on-horizontal-cohomologi
section_title: "algebraic structures on horizontal cohomologies"
section_number: 2.3
pages: 15-18
source_pdf: 2301.02038v1.pdf
source_sha256: 27b303939826ab39
doc_brief: "Contemporary Mathematics Vinogradov’s Cohomological Geometry of Partial Differential Equations — Secondary Calculus is a formal replacement for diﬀerential cal- culus on the space of solutions of a"
---
2.2 suggest that the horizontal cohomology H •(E ) should be interpreted as “smooth
functions on the space of solutions of the PDE E0”. For this reason we also denote
it
C∞ :=H •(E )
and call it secondary functions adopting a terminology by Vinogradov. Similarly,
the discussion at the end of Example 2.3 suggests that H •(E, V ) should be inter-
preted as “vector ﬁelds on the space of solutions of E0”. For this reason we also
denote it
X :=H •(E, V )
and call it secondary vector ﬁelds . Finally, Example 2.4 suggests that H •(E, V )
should be interpreted as “diﬀerential forms on the space of s olutions of E0”, we
denote
Ω p :=H •(E,∧pV ∗)
and call it secondary diﬀerential p-forms, p = 0, 1,... . This interpretation is sup-
ported by the fact that the above cohomologies possess the ap propriate algebraic
16 F ABRIZIO PUGLIESE, GIOV ANNI SPARANO, AND LUCA VITAGLIAN O
structures for functions, vector ﬁelds, diﬀerential forms . For instance, C ∞ is natu-
rally a (graded) commutative algebra, being the cohomology of a commutative DG
algebra. Similarly, the pair (C ∞, X) is a (graded) Lie-Rinehart algebra. We now
explain the latter claim.
Choose once for all a splitting of the short exact sequence (2 .1):
(2.5) 0 /d47/d47 C /d47/d47T E /d47/d47 V /d47/d47/d102/d102 0.
This induces a direct sum decomposition T E∼
= C⊕ V that allows us to interpret V
as a distribution and transverse vector ﬁelds as honest vect or ﬁelds on E . Dually,
we get a factorization
(2.6) Ω •(E )∼
=
Ω •(E )⊗ V Ω •
that allows us to interpret horizontal diﬀerential forms as honest diﬀerential forms
on E , and in the rest of this section we will do so. Similarly, we un derstand
the embedding Ω •(E, V )֒→Ω •(E,T E ) induced by the splitting (2.5) (and the
factorization (2.6)) and interpret V -valued horizontal diﬀerential forms as honest
vector valued forms on E . Now, recall that vector valued forms are naturally
equipped with a graded Lie bracket: the Frölicher-Nijenhui s bracket [−,−]fn (see,
e.g., [16, Section 16]). Moreover, the resulting graded Lie algebra a cts on diﬀerential
forms via the Lie derivative (along vector valued forms).
Notice that, unless the distribution V ⊆T E is itself involutive, the Frölicher-
Nijenhuis bracket does not preserve V -valued horizontal forms Ω •(E, V ). We can
deﬁne a bracket on Ω •(E, V ) by ﬁrst taking the Frölicher-Nijenhuis bracket, and
then projecting to Ω •(E, V ), but the bracket obtained in this way is not a Lie
bracket (unless V is involutive). However, it gives a honest graded Lie bracke t on
X. Namely, denote by
pr : Ω •(E )→ Ω •(E ), pr : Ω •(E,T E )→ Ω •(E, V )
the (natural) projections. Deﬁne a bracket [−,−]sec on X, the secondary commu-
tator, via:
(2.7) [−,−]sec : X× X→ X, (W, U )↦→[W, U ]sec :=
[
pr[W,U ]fn]
,
where W = [W ], U = [U ] are the cohomology classes of the cocycles W,U ∈
Ω •(E, V ) respectively.
We also deﬁne the secondary Lie derivative :
(2.8) Lsec : X× C∞→ C∞, (W, f )↦→Lsec
W f :=
[
prL
Wω
]
,
where f = [ω] is the cohomology class of the cocycle ω∈ Ω •(E ).
Theorem 2.6. The operations (2.7) and (2.8) are well-deﬁned and independ ent
of the splitting (2.5). Together with them and the graded C∞-module structure on X
induced by the DG (Ω •(E ),d)-module structure on (Ω •(E, V ),d), the pair (C ∞, X)
form a graded Lie-Rinehart algebra.
As for secondary diﬀerential forms, they form a commutative DG algebra. To
see this, consider the splitting (2.5) again and understand the induced factorization
(2.6). For every p,p ′, we have a secondary wedge product :
(2.9) ∧sec : Ω p× Ω p′
→ Ω p+p′
, (ω, ω ′)↦→ω∧sec ω ′ :=
[
ω∧ω′]
,
VINOGRADOV’S COHOMOLOGICAL GEOMETRY OF PDES 17
where ω = [ω], ω ′ = [ω′] are the cohomology classes of the cocycles ω∈ Ω •(E,∧pV ∗),
ω′∈ Ω •(E,∧p′
V ∗).
We also have a secondary diﬀerential . In order to deﬁne it we ﬁrst notice that
the De Rham diﬀerential does not map ∧pV ∗-valued horizontal form to ∧p+1V ∗-
valued horizontal form (unless V is involutive). We can deﬁne a map
Ω •(E,∧pV ∗)→ Ω •(E,∧p+1V ∗)
by ﬁrst taking the De Rham diﬀerential, and then projecting t o Ω •(E,∧p+1V ∗),
but the maps obtained in this way do not square to zero (unless V is involutive).
However, they give a honest diﬀerential on Ω •. Namely, denote by
pr : Ω •(E )→ Ω •(E,∧p+1V ∗)
the projection. Deﬁne a map dsec on Ω • via:
(2.10) dsec : Ω p→ Ω p+1, ω ↦→dsecω :=
[
prdω
]
.
Theorem 2.7. The operations (2.9) and (2.10) are well-deﬁned and indepen -
dent of the splitting (2.5). Together with them Ω • form a commutative DG algebra
(with respect to the total grading , i.e. the grading on Hq(E,∧pV ∗) given by p +q).
Remark 2.8. The secondary diﬀerential (2.10) agrees with that introduc ed in
Example 2.4.
There is a more conceptual way to introduce the operations (2 .9) and (2.10),
based on the Vinogradov’s C -spectral sequence, that we now explain. Namely,
recall the d-closed graded ideal C Ω •⊆ Ω •(E ) from Subsection 2.1 (it consists of
diﬀerential forms vanishing when restricted to vector ﬁeld s in C ). The powers
CpΩ • := C Ω •∧···∧ C Ω •
/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
p times
, p = 0, 1,...
deﬁne a ﬁltration
(2.11) Ω •(E ) = C 0Ω •⊇ C Ω •⊇···⊇ CpΩ •⊇··· ,
by graded d-closed ideals, which in turn determines a spectral sequenc e CE, called
the C -spectral sequence, computing the ordinary De Rham cohomologies of E .
Proposition 2.9. For all p,q , the map
Ω •(E,∧pV ∗)→ Ep,•
0 = CpΩp+•/Cp+1Ωp+•, ω⊗̟↦→ω∧̟ mod Cp+1Ωp+•
is a well-deﬁned cochain isomorphism, where ω∈ Ω •(E ),̟∈ V Ωp, and ω∈ Ω •(E )
is any q-form projecting to ω under Ω •(E )→ Ω •(E ). The induced isomorphism
Ω p =H •(E,∧pV ∗)→ CEp,•
1 =H •(CEp,•
0 ,dp,•
0 )
identiﬁes dsec with the diﬀerential d1 in the ﬁrst page of the C -spectral sequence, and
∧sec with the product structure on CE1 given by the fact that (2.11) is a ﬁltration
by DG ideals.
Hence∧sec,d sec could have been deﬁned via the C -spectral sequence without
using the splitting (2.5). One can even show that there is an a nalogue of the whole
Cartan Calculus on secondary diﬀerential forms and seconda ry vector ﬁelds. All
these operations together form the fundamentals of Vinogradov’s Secondary Calcu-
lus. Most of Vinogradov’s work on PDEs has been based on the follo wing principle:
18 F ABRIZIO PUGLIESE, GIOV ANNI SPARANO, AND LUCA VITAGLIAN O
Secondary Calculus is an appropriate replacement for Diﬀeren tial Calculus on the
space of solutions of a PDE .
We conclude this sections presenting an informal secondarization recipe. Namely,
let Φ be any natural construction in diﬀerential geometry (e.g. f unctions on mani-
folds, vector ﬁelds, the De Rham complex, etc.). The discuss ion in this subsection
suggests the following recipe to ﬁnd the secondary version of Φ , i.e. an appropriate
replacement Φ for the construction Φ on the space of solutions of a PDE E0.
Secondarization Recipe.
(1) Deﬁne the transverse version V Φ of Φ (when Φ is “vector ﬁelds”, then its
transverse version is Γ( V )).
(2) Notice that V Φ is canonically equipped with an action of the Lie algebroid
C giving a DG (Ω •(E ),d)-module structure to Ω •(E )⊗ V Φ (when Φ is
“vector ﬁelds”, then Ω •(E )⊗ V Φ is Ω •(E, V )).
(3) Deﬁne Φ as the horizontal cohomology with coeﬃcients in V Φ : Φ :=
H •(Ω( E )⊗ V Φ,d) (when Φ is “vector ﬁelds”, then Φ is X).
(4) Find the appropriate algebraic structures on Φ (when Φ is “vector ﬁelds”,
then Φ = X is a graded Lie-Rinehart algebra over C ∞).
In the next section we will use this recipe to deﬁne secondary scalar diﬀerential
operators, i.e. an appropriate replacement for scalar diﬀerential op erators on the
space of solutions of a PDE.
