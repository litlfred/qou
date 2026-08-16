---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkaidˆo lectures in Arithmetic Geometry Yves Andr´ e (with appendices by F. Kato and N. Tsuzuki)"
section_id: sec-562-5-berkovich-approach-to-non-archimedean-analysis
section_title: "Berkovich’ approach to non-archimedean analysis"
section_number: 5
pages: 222-227
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry Yves André (with appendices by F. Kato and N. Tsuzuki) — 580 sections: INTRODUCTION; INTRODUCTI"
---
Berkovich’ viewpoint provides an innovative approach to to pological
problems of p-adic geometry and analysis, which is much closer to the fami l-
iar intuition derived from the complex context [ Ber90](5). His analysis, in
fact, generalizes, or properly speaking, “completes” the r igid analysis. This
situation is, according to what he says in the introduction o f his book, some-
how analogous to that of R completing Q. The standard archimedean metric
space Q is totally disconnected. The rigid analytic viewpoint corr esponds,
to some extent, to regarding every rational interval {r∈ Q| a≤r≤b} as
(4)We refer [ BGR84, 9.3.1] for the deﬁnition of open subanalytic spaces.
(5)Already in [ vdP82] the esquisse of Berkovich’ idea can be seen.
5. BERKOVICH’ APPROACH TO NON-ARCHIMEDEAN ANALYSIS 219
“connected”, and considering only those functions which co me from analytic
functions on the corresponding real interval. Berkovich’ n on-archimedean
analysis can be compared, in this context, to analysis on R itself. Namely,
his presentation of analytic spaces complements those of ri gid analysis by
putting some “generic points”, and consequently, simpliﬁe s their topology.
Let us be a little more precise about his theory. Let A be a Banach ring,
i.e., a ring together with a norm ‖·‖with respect to which A is complete.
Deﬁnition 5.1. (1) A semi-norm |·| on A is said to be bounded if there
exists C >0 such that |f|≤ C‖f‖for any f∈ A.
(2) A semi-norm |·| on A is said to be multiplicative if|fg| =|f||g| for
all f,g ∈ A.
Replacing the maximal spectra Spm( A) of rigid geometry, we have:
Deﬁnition 5.2. The Berkovich’ spectrum M(A) for a Banach ring A is the
set of all bounded multiplicative semi-norms on A, endowed with the weakest
topology so that the real valued functions of form |·|↦→|f| for f∈ A are
continuous.
In case A is an aﬃnoid algebra (a strict aﬃnoid algebra, in Berkovich’
term) over K, the aﬃnoid space Spm( A) is naturally viewed as a subspace,
with the relative topology, of the Berkovich’ spectrum M(A). This is done
by identifying an element m in Spm( A) with the unique semi-norm |·| on
A such that m = Ker|·| . The space Spm( A) is identiﬁed, in terms of this
correspondence, with the subspace of M(A) consisting of semi-norms |·|
such that dim K A/ Ker|·| is ﬁnite (the “classical points”).
Example 5.3. Let us consider the usual absolute-value norm |·| ∞ on Z.
The spectrum M(Z) consists of the following points:
(i)|·| ∞,ǫ : = |·| ǫ
∞ (0<ǫ ≤ 1).
(ii) The p-adic norm|·| p,ǫ : with |p|p,ǫ =ǫ (0<ǫ ≤ 1).
(iii) The semi-norm |·| p induced from the trivial norm on Z/pZ.
(iv) The trivial norm |·| 0.
As a topological space, M(Z) is a tree with end points |·| p and|·|∞. Each
of these points is connected by a single edge with |·| 0.
On the Berkovich’ spectrum, the aﬃnoid subdomains (incl. rational sub-
domains) are deﬁned in the similar way to rigid analysis. Thus one can
deﬁne the structure sheaves on spectra, which one calls aﬃno id spaces. The
local data consisting of Berkovich’ aﬃnoids and the structu re sheaves can
glue to locally ringed spaces; thus we obtain analytic spaces in Berkovich’
sense.
Example 5.4. (Cf. [ Ber90, 1.5].) Let K be a non archimedean complete
ﬁeld. An aﬃne space over K is deﬁned by
An
K ={multiplicative seminorm|·| on K[t1,... ,t n]||·| |K is bounded}
220 A. RAPID COURSE IN p-ADIC ANALYSIS.
together with the weakest topology so that |·|↦→|f| (f ∈ K[t1,... ,t n])
is continuous. This has a structure of analytic space so that the analytic
functions over it is characterized by limits of rational fun ctions. When K =
C the space An
K is nothing but the usual aﬃne space in the complex analytic
sense. If K is a non-archimedean ﬁeld, then An
K is a union of balls; i.e., the
spectrum of Tate algebra.
Here are some general properties of Berkovich’ analytic spa ces:
(i) Every connected K-analytic space is arcwise connected.
(ii) If X = M(A) with A an aﬃnoid algebra over K, then Krull-dim A =
dim|X|, where|X| is the underlying topological space of X.
(iii) If a K-analytic space X is smooth, then it is locally contractible.
Relation between Berkovich’ analytic spaces and rigid anal ytic spaces is
as follows. If a Berkovich’ K-analytic space X is formed only by spectra
of (strict) aﬃnoid algebras, we say X is strict. There exists a functor from
the category of separated strict K-analytic spaces to that of separated rigid
analytic spaces over K by
X↦→X0 ={x∈X| [K(x) :K]<∞},
whereK(x) is the residue ﬁeld at x.
Theorem 5.5. This functor is fully-faithful, and preserves ﬁber product s.
APPENDIX B
Overview of theory of p-adic uniformization.
By F. Kato
In this appendix we always denote by K, R, and π a complete discrete
valuation ﬁeld, its valuation ring, and a prime element of R, respectively.
We assume that the residue ﬁeld k = R/πR is ﬁnite and consists of q ele-
ments. The Mumford-Kurihara-Mustaﬁn uniformization is a p rocedure to
construct nice analytic (and in many cases algebraic) varie ties by taking
discrete Schottky-type quotients of a certain p-adic analogue of symmetric
space, so-called Drinfeld symmetric space Ω, or its variants.
1. Bruhat-Tits building.
First we survey the construction of a certain simplicial com plex, called
Bruhat-Tits building (attached to PGL( n + 1,K )), which will be closely
related with the Drinfeld symmetric space. Let n be a positive integer and V
ann+1 dimensional vector space overK. A lattice inV is a ﬁnitely generated
R-submodule of V which spans V overK. Every lattice is therefore a free
R-module of rank n + 1. Let ~∆ 0 be the set of all lattices in V . We say
that two lattices M1 and M2 are similar if there exists λ∈ K× such that
M1 =λM2. The similarity is obviously an equivalence relation. We de note
by ∆ 0 the set of all similarity classes of lattices in V .
Deﬁnition 1.1. The Bruhat-Tits building (attached to PGL(n + 1,K )) is
the ﬁnite dimensional simplicial complex ∆ with the vertex s et ∆ 0 deﬁned
as follows: A ﬁnite subset {Λ 0,... , Λ l} of ∆ 0 forms an l-simplex if and
only if, after permuting indices if necessary, one can choos e Mi ∈ Λ i for
0≤i≤n + 1 such that
M0 ⊋ M1 ⊋ ··· ⊋ Ml ⊋ πM0.
The role of M0 is by no means important; for example, one can shift the
indices like M1 ⊋ ··· ⊋ Ml ⊋ πM0 ⊋ πM1.
To understand the structure of ∆, let us ﬁx one vertex Λ = [ M ]. Suppose
{Λ 0,... , Λ l} is an l-simplex having Λ as a vertex; we may assume Λ = Λ 0,
and can take Mi∈ Λ i for 1≤i≤l such that M ⊋ M1 ⊋ ··· ⊋ Ml ⊋ πM .
Set M i : = Mi/πM . Then we get a ﬂag
M ⊋ M 1 ⊋ ··· ⊋ M l ⊋ 0
221
222 B. OVER VIEW OF THEORY OF p-ADIC UNIFORMIZATION.
of length l + 1 consisting of subspaces of the n + 1-dimensional k-vector
space M = M/πM . Moreover, by the elementary algebra one ﬁnds that
this yields a one-to-one correspondence between l-simplices containing Λ
and length l + 1 frags in M =M/πM . By this quite easy observation one
knows
(i) ∆ is an n-dimensional locally ﬁnite simplicial complex,
(ii) every simplex in ∆ is a face of a chamber, a simplex having maximal
(=n) dimension.
Furthermore, by the construction,
(iii) the group Aut K (V )/K×(∼
= PGL(n + 1,K )) naturally acts on ∆ sim-
plicially.
Example 1.2 (n = 1 case) . In n = 1 case, the vertices adjacent to a ﬁx
vertex Λ are in one-to-one correspondence with the set of all k-rational
points of the projective line P1
k; in particular, each vertex has exactly q + 1
adjacent vertices. Moreover, it can be seen that the simplic ial complex
∆ = ∆ 1 is a tree. The following picture shows how it looks like in case
q = 2:
r
r
❍❍r✟✟r
✟✟r❍❍r
r
✟✟r
r
❍❍r
♣♣♣
♣ ♣ ♣♣♣♣
♣♣♣
♣ ♣ ♣♣♣♣
♣♣♣
♣ ♣ ♣
♣ ♣ ♣♣♣♣
♣♣♣
♣♣♣
In general, the geometrical realization |∆ | of ∆ is known to be a con-
tractible topological space.
Example 1.3 (n = 2 case) . Already in case n = 2, the structure of ∆ = ∆ 2
is fairly complicated. For a ﬁxed vertex Λ, the set of all vert ices adjacent
of Λ is divided in two; one for those corresponding to q2 +q + 1 k-rational
points in P2
k and the other for those corresponding to q2 +q + 1 k-rational
lines in P2
k. So it is convenient to consider the surface B which is obtained
by blowing-up of P2
k at every k-rational points. Two vertices adjacent to Λ
forms with Λ a 2-simplex if and only if the corresponding line s inB intersect.
2. Drinfeld symmetric space.
To each lattice M in V we associate an R-scheme
P(M ) : = Proj(Sym RM ).
Obviously the scheme P(M ) depends only on the similarity class; so we
should write as P(Λ), where Λ = [ M ]. The scheme P(M ) is isomorphic to
Pn
R; but the isomorphism cannot be taken canonically, while the re exists the
