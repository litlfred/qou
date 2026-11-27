---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-5
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
The mechanism responsible for the emergence of the rich structure of conformal ﬁeld theories (CFTs) in the
continuum limit of discrete (not necessarily integrable) lattice models has attracted growing interest in the last
few years. There are several reasons for this. On the one hand, this is part of the more general question of
how one can approximate ﬁeld theories using discrete systems, with the ultimate goal of carrying out more
eﬃcient (quantum) simulations [3–5]. On the other hand, the possibility of observing, on the lattice, properties
2
“analogous” to those of CFTs opens the door to the introduction of new discrete mathematical tools with a
smorgasbord of exciting potential applications [6, 7]. Finally, the study of non-unitary CFTs—which play, in
particular, a crucial role in our description of geometrical statistical models (such as percolation or polymers),
or of transitions between plateaux in the integer quantum Hall eﬀect—is mired in the technical diﬃculties
that emerge when the representation theory of the Virasoro algebra is not semi-simple. In many cases, only
a bottom-up approach, where things are studied starting at the level of the lattice model, has made progress
possible. An example of this was, at central charge c = 0, the determination of the logarithmic coupling (also
variantly known as indecomposability parameter, beta-invariant, orb-number) between the stress-energy tensor
and its logarithmic partner in the bulk CFT [8–11].
Many aspects of CFTs can of course be approached using lattice-model discretizations. In some cases,
results for well-chosen ﬁnite systems are already directly relevant to the continuum limit. This is the case, for
instance, of modular transformations (studied as early as [12]; see also [13] for more recent work on this) and
fusion rules [14, 15]. In other cases, the precise connection with CFT can only be made after the continuum
limit is taken. Examples of this include the determination of three-point functions [16, 17], and more recently,
of four-point functions [18–21].
Underlying the relationship between lattice discretization and CFT is the central question of the role of
conformal transformations (and thus the Virasoro algebra) in lattice models. In an early work by Koo and
Saleur [1], a very simple construction was proposed where the Virasoro algebra Vir (or the product Vir ⊗ Vir
of left and right Virasoro algebras) could be obtained starting with Fourier modes of the local energy and
momentum densities in ﬁnite spin chains (such as XXZ), and taking the limit of large chains while restricting
to “scaling states”, which are states belonging to the continuum limit. The restriction to scaling states is done
through a double-limit procedure that we call the “scaling limit” and denote by ↦→. (See [1] and below for
more detail on this). The evidence for the validity of the construction in [1] came from exact results in the
case of the Ising model combined with rather elementary numerical checks. Quite recently, the construction
was put on more serious mathematical footing (and further checked for symplectic fermions) in [22–24]. It was
also revisited extensively for the Ising case using the language of anyons in [25]. In [25], a set of conditions for
the construction to work more generally—together with more precise deﬁnitions of the scaling limit—were also
given.
The purpose of this paper is twofold. On the one hand, we wish to revisit the proposal of [1] by carrying
out much more sophisticated numerics than was possible at the time. This involves in particular the techniques
of lattice form factors, thanks to which matrix elements of the discrete Virasoro generators can be expressed in
closed form using Bethe-ansatz roots. By contrast, in [1], only eigenstates were obtained with the Bethe ansatz,
while matrix elements were calculated by brute-force numerics. The quantitative improvement is substantial.
While in [1] only chains up to length ten or so were studied, we are easily able in this paper to tackle lengths
up to 80. Our results fully conﬁrm the validity of the proposal in [1], and shed some extra light on the nature
of the scaling limit, and the convergence of the lattice Virasoro algebra to Vir ⊗ Vir.
On the other hand, the growing interest in logarithmic CFT has made it crucial to understand in detail
the nature of Vir⊗ Vir modules appearing in the continuum limit of speciﬁc lattice models when some of the
parameters take on values such that the representation theory of Vir ⊗ Vir becomes non-semi simple, and the
detailed information how irreducible modules are glued in a particular physical model of interest cannot be
obtained from general principles. This information is crucial to answer a variety of questions: chief among
these is the nature of ﬁelds whose conformal weights are in the extended Kac table, h = hr,s with r,s ∈ N∗.
While in unitary CFTs the resulting degenerate behaviour implies the existence of certain diﬀerential equations
satisﬁed by the correlators of these ﬁelds, such result does not necessarily hold in the non-unitary case, where
Virasoro “norm-squares” are not positive deﬁnite any longer (see more discussion of this below). The second
purpose of this paper is to ﬁnd out speciﬁcally what kind of Virasoro modules occur in the XXZ chain when the
Virasoro representations are degenerate—that is, (some) ﬁelds belong to the extended Kac table. We will do
this straightforwardly, by exploring the action of the lattice Virasoro generators, and checking directly whether
the relevant combinations vanish or not—in technical parlance, whether “null states” or “singular vectors” are
zero indeed. This is of course of utmost importance in practice, as this criterion determines the applicability of
the BPZ formalism [26] to the determination of correlation functions, such as the four-point functions currently
under investigation [19–21]. We shall ﬁnd some unexpected results, that we hope to complete in a subsequent
paper [27] by studying the cases when the central charge is rational (e.g., the case c = 0 with applications to
percolation).
A similar investigation in the cognate link-pattern representation of the XXZ chain (relevant for the cor-
responding loop model) has already appeared in a companion paper [2]. We will remark on the important
diﬀerences between the two representations throughout the present paper.
The paper is organized as follows. Section 2 discusses general algebraic features. We consider successively
the aﬃne Temperley-Lieb algebra and its representations, the issues of indecomposability, and recall the basic
Koo-Saleur conjecture which proposes lattice regularizations for the generators of the Virasoro algebra. In
section 3 we discuss expected features of the continuum limit, based in part on the Dotsenko-Fateev or Feigin-
3
Fuchs free-boson construction. We also discuss partly the issue of scalar products—with more remarks on this
topic being given in Appendix A. In section 4 we recall several aspects of the Bethe-ansatz solution of the XXZ
chain, in particular those concerning the form-factor calculations and the deﬁnition of scaling states. Relations
between the form factors show that duality relations between certain expected continuum modules are already
present at ﬁnite size. In section 5 we discuss the continuum limit of the Koo-Saleur generators in the non-
degenerate case, where none of the conjectured conformal weights belong to the extended Kac table. Following
this, section 6 discusses their continuum limit in the degenerate cases where the conjectured conformal weights
take on values in the extended Kac table. Section 7 discusses the nature of the convergence of the Koo-Saleur
generators to their Virasoro-algebra continuum limit. Finally, section 8 contains our concluding remarks.
Several technical aspects are addressed in the appendices. In appendix A we brieﬂy remind the reader
of the physical meaning of the “conformal scalar product” for which L‡
n = L−n (we reserve the notation †
for another scalar product). In appendix B we discuss the form factors for the Koo-Saleur generators. In
appendix C more details about numerical results for the action of the Koo-Saleur generators are provided.
A proof of (133), an expression involving the ground-state expectation of two neighbouring Temperley-Lieb
generators that we initially conjectured based on our numerical results, is provided in appendix D. In appendix
E we discuss in further detail the continuum limit of commutators of Koo-Saleur generators. Details about
a particular commutation relation—which we call the chiral-antichiral commutator—are given in appendix F.
Finally, the last appendix G discusses a natural variant of the Koo-Saleur construction in the case of the XXZ
chain considered as a system of central charge c = 1.
Main results: Our main results for relations between form factors and lattice duality are given in equations
(86) and (97). Our main results for the nature of the modules arising in the continuum limit are given in
equations (108) and (111). Our main results for the nature of the convergence of the Koo-Saleur generators are
given in (124), (133),(134) and (135).
Notations and deﬁnitions
We gather here some general notations and deﬁnitions that are used throughout the paper:
• Ta
N(m) — the aﬃne Temperley–Lieb algebra onN = 2L sites with parameter m. We shall later parametrize
the loop weight as m = q + q−1, with q =eiγ and
γ = π
x + 1. (1)
• Wj,eiφ — standard module of the aﬃne Temperley-lieb algebra with 2j through-lines and pseudomomentum
φ/2. We deﬁne a corresponding electric charge as1
eφ≡ φ
2π. (2)
• Vr,s — Verma module for the conformal weight hr,s when r,s /∈ N∗.
• V(d)
r,s — the (degenerate) Verma module for the conformal weight hr,s when r,s∈ N∗.
• ~V(d)
r,s — the (degenerate) co-Verma module for the conformal weight hr,s when r,s∈ N∗.
• Xr,s — irreducible Virasoro module for the conformal weight hr,s.
• A conformal weight hr,s with r,s ∈ N∗ will be called degenerate. For such a weight, there exists a
descendent state that is also primary: this descendent is often called a null or singular vector or state. We
will denote by Ar,s the combination of Virasoro generators producing the null state corresponding to the
degenerate weighthr,s. Ar,s is normalized so that the coeﬃcient of Lrs
−1 is equal to unity. Some examples
are
A1,1 = L−1, (3a)
A1,2 = L2
−1− 2(2h1,2 + 1)
3 L−2, (3b)
A2,1 = L2
−1− 2(2h2,1 + 1)
3 L−2. (3c)
1Note that the twist term in [12], which was denoted there q2t, reads in these notations as eiφ. It corresponds to e2iK in many
of our other papers [22–24,28], to z2 in the Graham–Lehrer work [29], and to the parameter x in the work of Martin–Saleur [30].
4
• We will in part of this paper use the Dotsenko-Fateev construction [31]. For theories with central charge
c = 1− 6
x(x+1), this involves in particular screening charges α+ =
√
(x + 1)/x and α− =−
√
x/(x + 1),
and the set of vertex operator charges α(e,m ) = 1
2(eα+−mα−) and ¯α(e,m ) = 1
2(eα+ +mα−). Instead
of “Coulomb gas” labels e,m we will use “Kac” labels r,s , with
αr,s = 1−r
2 α+ + 1−s
2 α−. (4)
Of course these labels are not independent in a free-ﬁeld theory with charge at inﬁnity, and one has
α−e,m =α(e,m ) +α0. (5)
We deﬁne the background charge
α0 = α+ +α−
2 = 1
2
√
x(x + 1)
(6)
and introduce the notation
αc≡ 2α0−α (7)
for the conjugate charge to a charge α. Note that αc
r,s =α−r,−s. The conformal weight corresponding to
a charge α is h =α2− 2αα0.
• Fα — Fock space generated from :eiαϕ:, where ϕ denotes a free bosonic ﬁeld.
• We will in this paper restrict to generic values of the parameter q (i.e., q not a root of unity), and thus to
generic values of x (i.e., x irrational). Even in this case, we will encounter situations where some of the
modules of interest are not irreducible anymore. We will refer to these situations as “non-generic” when
applied to modules of the aﬃne Temperley-Lieb algebra, and “degenerate” when applied to modules of
the Virasoro algebra. In earlier papers, we have referred to such cases as “partly non-generic” and “partly
degenerate”, respectively, since having q a root of unity adds considerably more structure to the modules.
We will not do so here, the context clearly excluding q a root of unity.
• We shall discuss two scalar products, denoted by ⟨−,−⟩ and (−,−), which are deﬁned such that for
any two primary states V1,V 2 we have⟨V1,LnV2⟩ =⟨L†
nV1,V 2⟩ and (V1,LnV2) = (L‡
nV1,V 2), where L†
n
is discussed below and L‡
n = L−n is the usual conformal conjugate [26]. The scalar product ⟨−,−⟩ is
positive deﬁnite and will be used for most parts of the paper. When using this scalar product we shall
also use the bra-ket notation:|V⟩ denotes a state V (primary or not) and⟨V| its dual,⟨V1|V2⟩≡ ⟨V1,V 2⟩
and⟨V1|O|V2⟩≡ ⟨V1, OV2⟩ for an operator O acting on|V1⟩ (with V1,V 2 being primary or not).
• We shall call states going over to well deﬁned states in the continuum limit CFT scaling states . The
notion of scaling states is made more precise in terms of the Bethe ansatz in Section 4.1. We shall call
the double limit procedure of restricting to a ﬁxed number of scaling states, and allowing this number
to become inﬁnite only after N→∞ , the scaling limit, using the notation ↦→. Weak convergence under
the condition that everything is restricted to scaling states will be called scaling-weak convergence, and
is discussed in more detail in Section 7.1.
