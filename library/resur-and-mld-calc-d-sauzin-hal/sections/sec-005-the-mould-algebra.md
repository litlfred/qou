---
doc_id: resur-and-mld-calc-d-sauzin-hal
doc_title: "Resurgence and Mould Calculus"
section_id: sec-005-the-mould-algebra
section_title: "The mould algebra"
section_number: null
pages: 11-12
source_pdf: Resur_and_Mld_Calc_D_SAUZIN_HAL.pdf
source_sha256: b33f24cc76102f33
doc_brief: "Resurgence and Mould Calculus — 9 sections: Introduction; Alien operators. Alien derivations; Borel-Laplace summation"
---
We have encountered~Rs
Ω-valued moulds in the context
of alien calculus, and Ω′, a rank-one lattice minus the
origin, was then used as alphabet. We now develop
the basics of mould calculus in the broader context of
a commutative Q-algebra A and an arbitrary alpha-
betN . We denote byN the free monoid onN , which
is not supposed to be countable or contained in C,
but, when necessary, we assume N to be a commu-
tative semigroup, in which case we use the notation
‖ω‖ :=ω1 +··· +ωr for any ω =ω1··· ωr∈N .
An A-valued mould on N is just a map M : N →
A; it is customary to use the notation Mω instead
of M(ω). Word concatenation in N induces mould
multiplication:
(M×N)ω :=
∑
(a,b) such that ω=ab
MaNb, (55)
and the space AN of all moulds is thus an associative
A-algebra, non-commutative if N has more than one
element, whose unit is the mould 1 deﬁned by 1∅ = 1
and 1ω = 0 for ω ⁄= ∅ (AN is sometimes denoted
byA⟨⟨N⟩⟩ in algebraic combinatorics). A mould M is
invertible if and only if M ∅ is invertible in A.
There is also an associative non-commutativemould
composition: for each U∈AN , we have an A-algebra
homomorphism M↦→M◦U deﬁned by (M◦U)∅ :=
M ∅ and, for ω⁄= ∅,
(M◦U)ω :=
∑
s≥1,ω 1,...,ωs⁄=∅
ω=ω1···ωs
M‖ω1‖···‖ωs‖Uω1
··· Uωs
.
(56)
We denote byr(ω) the length of a word ω. The iden-
tity mould I deﬁned by Iω := 1 if r(ω) = 1 and 0
otherwise satiﬁes M◦I = M and I◦U = U for all
moulds M and U such that U ∅ = 0. Such U has a
composition inverse if and only Uω is invertible in A
wheneverr(ω) = 1.
A mould M is said to have order ≥ p if Mω = 0
wheneverr(ω)<p . There is correspondingly a notion
of formal convergence (a series of moulds∑Mk is con-
vergent if ord(Mk)→∞ , so that for any given ω only
ﬁnitely many terms contribute), which for instance al-
lows to deﬁne mutually inverse bijections
{M∈AN|M ∅ = 0}
exp
⇄
log
{M∈AN|M ∅ = 1}
(57)
by the usual exponential and logarithm series.
Mould expansions. A-valued moulds often provide the
coeﬃcients of certain multi-indexed expansions in an
associative A-algebra B. We may then restrict to
ﬁnite-support moulds so as to avoid inﬁnite expan-
sions, as we did earlier with N = Ω′, A = ~Rs
Ω and
B = EndC(A), or we may assume B to be a complete
ﬁltered associative algebra, thus endowed with a no-
tion of formal convergence.
Then, given a family ( Bω)ω∈N inB, we extend it
toN by deﬁning B∅ := 1B and
Bω :=Bωr··· Bω1 for any ω =ω1··· ωr∈N , (58)
and consider the mould expansion
M B :=
∑
ω∈N
Mω Bω∈B (59)
associated with M ∈ AN . One can check that
(M× N)B = ( N B)(M B), (exp M)B = exp( M B),
(logM)B = log(M B) when these mould expansions
make sense.
IfB is only supposed to be a Lie algebra, one can
deﬁne another kind of mould expansion: we then set
B[ω] := [Bωr, [... [Bω2,Bω1]... ]] and
M[B] :=
∑
ω⁄=∅
1
r(ω)MωB[ω]. (60)
10
Then, recalling the deﬁnition (19) of alternality,
M and N alternal ⇒ [M,N ][B] =
[
M[B],N [B]
]
.
(61)
IfB is an associative algebra with commutator as Lie
bracket, the two kinds of alternal mould expansions
coincide, as in (20)— cf. the classical Dynkin-Specht-
Wever projection lemma [Reu93].
The set of alternal moulds U that have a composi-
tion inverse is a group for mould composition.
Symmetrality and alternality. Parallel to the deﬁni-
tion (19) of alternality, we have
Deﬁnition 10. A mould M is called symmetral if
M ∅ = 1A and
∑
ω∈N
sh
(a,b
ω
)
Mω =MaMb (62)
for any a,b∈N .
Symmetral moulds form a group for mould multi-
plication; the logarithm map (57) maps it bijectively
to the space of alternal moulds, which is a Lie algebra
for mould commutator. Mould expansions enjoy spe-
cial properties when each Bω acts as a derivation on
some auxiliary algebra, as is the case of ∆ω∈ DerC(A)
when A = ~Rs
Ω:
M alternal ⇒ M B is a derivation
M symmetral ⇒ M B is an automorphism.
The concepts of symmetrality and alternality, intro-
duced in [ ´Eca81], are related to certain combinatorial
Hopf algebras, as emphasized by Menous [Men09] in
his work on the renormalization theory in perturbative
quantum ﬁeld theory. See [LSS19] for the relation to
the Baker-Campbell-Hausdorﬀ formula.
Other types of symmetries. One may also consider
mould expansions based on a family ( Bω)ω∈N of op-
erators that, instead of being derivations, satisfy the
same modiﬁed Leibniz rule (12) as the ∆ +
ω . We
then have parallel statements for the mould expan-
sions associated with moulds enjoying ‘symmetr elity’
or ‘alternelity’, two notions deﬁned in a manner anal-
ogous to symmetrality and alternality but involving,
instead of shuﬄing, ‘contracting shuﬄing’ (also called
stuﬄing).
´Ecalle [ ´Eca02] also introduced ‘symmetr ility’ and
‘alternility’ in his works on MZVs, as well as many
other structures in the context of ‘bimoulds’—see be-
low.
