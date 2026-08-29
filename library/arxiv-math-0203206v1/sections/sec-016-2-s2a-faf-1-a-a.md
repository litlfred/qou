---
doc_id: arxiv-math-0203206v1
doc_title: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories"
section_id: sec-016-2-s2a-faf-1-a-a
section_title: "S2(a) = faf −1 ∀a ∈A,"
section_number: 2
pages: 10-11
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
doc_brief: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups"
---
3. Tripi(f ) = Tripi(f −1), where Tri is the usual trace on B(Hi).
It also satisﬁes S(f ) = f −1 (where the unique extension of S to M (A) is understood).
Proof. To simplify the formulae we introduce the antilinear map χ(a) = S(a∗) which satisﬁes χ2 = idA. For
every i ∈I we pick an antiunitary Ji :Hi →Hi. Now, Jipi(·)J −1
i is a (linear) irreducible representation of A
on Hi for any i ∈I. By Prop. 2.10 there is a unique c(i) ∈I and an invertible Vi :Hi →Hc(i) such that
ViJipiχ(·)J −1
i V −1
i =pc(i). (2.1)
NowUi ≡ViJi is unique up to a scalar. We calculate
Uipi(a)U −1
i =Uipi(χχ(a))U −1
i =pc(i)(χ(a)) = U −1
c(i)pc(c(i))Uc(i).
In the ﬁrst step we have used χ2 = id and then we have used (2.1) twice. This shows that the irreducible
representations pi and pc(c(i)) are equivalent and therefore c is involutive: c(c(i)) = i. From now on we write
ı =c(i). We have
UıUipi(·)U −1
i Uı =pi(·),
and by irreducibility UıUi = ki1 ∈ B(Hi). Using the freedom (up to a scalar) in the choice of the Ui we can
assume that ki = 1 ∀i ∈I. (If i =ı we can absorb ki in Ui. If i ⁄=ı, we can achieve UıUi = 1, and since the Ui
are invertible this implies that automatically kı = 1.)
From (2.1) we obtain piS(a) = U −1
i pı(a∗)Ui and applying this twice yields
piS2(a) = U −1
i pıS(a)∗Ui =U −1
i [U −1
ı pı(a∗)Uı]∗Ui =U −1
i U ∗
ıpi(a)U −1∗
ı Ui.
ThuspiS2(a) = Gipi(a)G−1
i with Gi =U −1
i U ∗
ı =k−1
i UıU ∗
ı positive and invertible for all i ∈I. Deﬁning
Fi =
√
TriG−1
i
TriGi
Gi,
we have
TriFi =
√
TriG−1
i TriGi =TriF −1
i
as required. Obviously, also the Fi are positive and invertible and piS2(a) = Fipi(a)F −1
i . The uniqueness
is obvious in view of the normalizations. It remains to prove S(f ) = f −1, which is clearly equivalent to
piS(f ) = pi(f −1) ∀i. As above, with (2.1) we have piS(f ) = U −1
i pı(f ∗)Ui = U −1
i F ∗
ıUi. On the other hand,
pi(f −1) = F −1
i . Thus we have to show
U −1
i F ∗
ıUi =F −1
i ∀i ∈I.
10
Inserting the deﬁnition of the Fi this is equivalent to
U −1
i
√
TrıG−1
ı
TrıGı
UiU −1∗
ı Ui =
√
TriGi
TriG−1
i
U ∗−1
ı Ui ∀i ∈I.
This is clearly equivalent to
TrıG−1
ı TriG−1
i =TriGi TrıGı ∀i ∈I.
Plugging in Gi =U −1
i U ∗
ı this is an easy computation which we omit. (One uses Uı =U −1
i and cyclicity of the
traces.) ■
Theorem 2.13 A discrete multiplier Hopf ∗-algebra (A, ∆) admits a non-zero left-invariant positive linear
functional ϕ, thus is an aqg.
Proposition 2.14 An aqg (A, ∆) is discrete iﬀ there exists h ∈A such that ah =ε(a)h, for all a ∈A.
Definition 2.15 An aqg (A, ∆) is called compact if A is unital.
Note that an aqg ( A, ∆) is compact iﬀ it is a Hopf ∗-algebra. Hence the analytical extension of a compact
aqg is a compact quantum group in the sense of S.L. Woronowicz. A mu ltiplier Hopf ∗-algebra (A, ∆) with A
unital is not necessarily an aqg, but this is the case whenever A has a C*-algebra envelope. It is easily seen
that (A, ∆) is compact and discrete iﬀ A is ﬁnite dimensional.
Theorem 2.16 Let (A, ∆) be an aqg. Then (A, ∆) is compact iﬀ ( ˆA, ˆ∆) is discrete.
