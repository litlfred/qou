---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-000-1-introduction-and-summary
section_title: "Introduction and summary"
section_number: 1
pages: 4-11
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
In this paper we study objects which we call spectral networks. A spectral network W is
made up of walls drawn on a punctured real surface C. Here is a picture of one:
12
21
21
12
21
12 23
23
13
32
31
32
(12)
(12)
(23)
13
23
23
32
32 31
(23)
Figure 1 . A spectral network, drawn on the stereographic projection of C = S2, with a single
puncture at inﬁnity. All of the walls eventually asymptote to this puncture. The walls are labeled
by pairs ij, where i, j are sheets of a 3-fold covering Σ → C. The branch points of the covering
are shown as orange crosses. We have trivialized the covering over the complement of some branch
cuts, shown as wavy orange lines.
Each wall carries some extra discrete data: a pair ij and (roughly) an integer µ. The
labels i and j are drawn from the set of sheets of a ﬁnite branched covering Σ →C. The
walls and their discrete data obey certain local constraints: for example,
• each simple branch point of the covering Σ →C gives birth to three walls;
• when an ij wall and a jk wall intersect, a new ik wall is born at their intersection
point.
In§2-§8 of this paper we study some particular spectral networks which arise naturally
in physics. In §9 we axiomatize the notion of spectral network. In §10 we describe a more
mathematical application, to coordinate systems on moduli spaces of ﬂat connections.
Those sections are mostly self-contained.
Here is how spectral networks arise in physics. Fix an N = 2 supersymmetric theory
T in d = 4 and a point u of the Coulomb branch. Also ﬁx a 1/2-BPS surface defect Sz
which has a 1-complex-dimensional space C of UV parameters, and is massive in the IR,
with ﬁnitely many vacua for any ﬁxed z. These data determine a 1-parameter family of
spectral networksWϑ drawn onC, labeled by phases ϑ∈ R/2πZ. Namely,Wϑ is the locus
– 2 –
of z∈ C for which the surface defect Sz carries a BPS soliton whose central charge Z is
aligned with−eiϑ. The discrete data µ on the walls keep track of the degeneracies of these
BPS solitons. The points of the ﬁnite cover Σ → C overz∈ C are the vacua of Sz. The
dataij on the walls keep track of which vacua of Sz are being interpolated by the solitons.
In this paper, for concreteness, we focus on a particular (large) class ofN = 2 theories,
namely the theories of class S [1–3]. These are the theories S[g,C,D ], associated to a Lie
algebra g (which we take to be g =AK−1), punctured Riemann surface C, and a collection
D of defects placed at the punctures of C. They are obtained by a partially topologically
twisted compactiﬁcation of the six-dimensional (2, 0) theoryS[g]. A point u of the Coulomb
branch here means a tuple (φ2,...,φ K), where each φr is a meromorphic r-diﬀerential on
C, with poles at the defects. In these theories there is a canonical surface defect Sz whose
parameter space is C. Moreover, in these theories the covering Σ → C can be identiﬁed
with the Seiberg-Witten curve [4, 5] and is given concretely by (2.1) below.
The spectral networksWϑ arising from theories of class S can be described concretely.
The walls of the network are solutions of diﬀerential equations, given in (3.1) below. The
full network is built up by a continuous process: three walls are born from each branch
point of the covering Σ and ﬂow according to (3.1); whenever two walls intersect, they can
give birth to an additional wall. This process is described in §5.4.
Here are some of the uses of the spectral networks Wϑ:
Framed BPS states. By letting the parameter z of a surface defect vary along a
path℘ inC, one can deﬁne a supersymmetric interfaceL℘,ϑ [5]. KnowingWϑ andµ allows
one to determine the complete spectrum of BPS states of these interfaces, called “framed
BPS states.” In fact, the framed BPS spectrum turns out to be overdetermined, so much
so that one can use its consistency to compute µ.
Jumps ofWϑ and the 4d BPS spectrum. As the parameter ϑ is varied,Wϑ also
varies. There are some critical phases ϑc at which the topology of Wϑ suddenly changes
(in a precise sense explained in §6). These critical phases ϑc are the phases of the central
charges Zγ of BPS states in the d = 4 theory S[g,C,D ]. Moreover, one can read oﬀ the
degeneracies Ω(γ) of these BPS states from the topology of Wϑ=ϑc.
We ﬁnd in this way that BPS states in S[g,C,D ] correspond to certain “ﬁnite webs”
of strings on C, which appear inside the spectral network Wϑ at the critical phase. Some
pictures of ﬁnite webs appear in Figure 2. The role of ﬁnite webs in the BPS spectrum was
already expected [3, 6–8], but our analysis here gives a much more precise understanding of
how to compute the corresponding BPS degeneracies Ω(γ) than was previously available. It
also provides a geometric argument (if not quite a proof) that the degeneracies so computed
obey the wall-crossing formula of Kontsevich-Soibelman [9], as well as its extension to
include the coupling between 2d and 4d BPS states, given in [5].
This story can be thought of as a broad generalization of parts of [3, 5], where we
explained why the counts of ﬁnite webs obey the wall-crossing formulas in the case K = 2.
In fact, our approach here leads to a simpler and more conceptual understanding even of
that case.
– 3 –
The 4d BPS spectrum of N = 2 theories has been investigated by many authors re-
cently; see in particular [10, 11]. One advantage of our approach here via spectral networks
is that, given a point u of the Coulomb branch, one can determine any particular BPS
degeneracy Ω(γ) at u just by drawing the network Wϑ=argZγ corresponding to u. The
spectral network also gives more precise information — not only the 4d BPS degeneracies
Ω(γ) but also some enhancements ω(γ,·), which keep track of the interaction between the
4d BPS state and the surface defects Sz.
Moduli of ﬂat connections. Suppose we compactify on S1 both the d = 4 theory
and the surface defects Sz. The ground states of Sz on S1 form a K-dimensional vector
space Ez; letting z vary we obtain a rank K vector bundle E overC. Now take a path ℘
in C from z1 to z2. The vacuum expectation value ⟨L℘,ϑ⟩ of the corresponding interface
wrapped on S1 is an isomorphism from Ez1 to Ez2. In other words, the bundle E is
equipped with a natural connection [4], which moreover is actually ﬂat. 1
On the other hand, we could also take the perspective of the IR (abelian) theory. From
that point of view we would have surface defects labeled by points on Σ rather than on
C, with 1-dimensional spaces of vacua, thus forming a line bundle L over Σ. Considering
interfaces between these surface defects, we see thatL too is naturally equipped with a ﬂat
connection.
So, to each vacuum of the compactiﬁcation of thed = 4 theory onS1, we have assigned
on the one hand a ﬂat rank K connection over C, and on the other hand a ﬂat rank 1
connection over the covering Σ. This induces a correspondence Ψ Wϑ between the two
types of connection, which turns out to be (at least locally) an isomorphism of moduli
spaces. Moreover, we can compute ΨWϑ concretely: the key is the framed BPS degeneracies
mentioned above, which (roughly) give the coeﬃcients in the expansion of a UV interface
L℘,ϑ in terms of IR interfaces. Upon taking expectation values this becomes an expansion
of the vacuum expectation value ⟨L℘,ϑ⟩ in terms of “Darboux coordinates” as described
e.g. in §5.8 of [5]. In particular, the correspondence Ψ Wϑ is determined by the spectral
networkWϑ.
Cluster coordinate systems. Since the space of ﬂat rank 1 connections over Σ is
a product of copies of C×, another way to describe the last item is to say that Ψ Wϑ is a
local coordinate system on the moduli space M of ﬂat rank K connections over C. The
construction of ΨWϑ fromWϑ can be generalized: it uses only some general properties of
Wϑ, which we abstract into a deﬁnition of “spectral network”. Given any spectral network
W there is a corresponding ΨW.
We conjecture that ΨW is a particularly nice coordinate system: it is a cluster coordi-
nate system, in the sense of [12]. Indeed, Fock and Goncharov proved [13] that the spaces
M we consider admit an atlas of cluster coordinate systems. 2 ForK = 2 the cluster atlas
consists precisely of the coordinate systems ΨW. For K >2, Fock and Goncharov did not
give a completely explicit description of the atlas — rather they described some particular
1We are oversimplifying slightly here: the precise story, laid out in the main text, involves a slight
twisting of the notion of ﬂat connection. This twisting does not modify the basic picture and can safely be
ignored at ﬁrst.
2This fact implies e.g. that these spaces admit a natural quantization [12, 14].
– 4 –
cluster coordinate systems. The most general cluster coordinate system would be obtained
by beginning with one of these and performing some sequence of coordinate transforma-
tions known as “mutations”; each mutation generates a new coordinate system, and the
cluster atlas is the set of all coordinate systems obtained in this way. We conjecture that
our ΨW are coordinate systems in the cluster atlas. 3
How do the mutations arise in our story? Small deformations of the spectral network
W leave the coordinate system ΨW invariant. However, there are some natural “degenera-
tions” of spectral networks which interpolate between “inequivalent”W. We have already
seen these degenerations in this introduction: they occur in the families Wϑ when the pa-
rameterϑ is adjusted to a critical phase ϑc. When such a degeneration occurs, Ψ W jumps
by an automorphism K of the torus of ﬂat rank 1 connections on Σ. This K is simply
determined by the degeneracies Ω(γ) read oﬀ from the degenerate network (see (10.28) for
its explicit form.) K has a form very similar to that of a cluster mutation, and part of our
conjecture is that for the simplest types of degenerations it is indeed a mutation.
Very recently Goncharov has also deﬁned some new geometric objects which he calls
spectral webs [15], and which correspond to coordinate systems in the cluster atlas. Despite
the similar nomenclature, this deﬁnition is diﬀerent from our deﬁnition of spectral networks.
It should be interesting to compare the two constructions.
WKB expansions and spectral networks as Stokes diagrams. One of the key
tools in [3] was the WKB approximation, applied to the ζ→ 0 behavior of families of ﬂat
SL(2, C) connections of the form
∇(ζ) =Rϕ
ζ +D +Rζ ¯ϕ. (1.1)
Such families are associated with solutions of Hitchin’s equations [16] and naturally arise
in theories of class S.
Some aspects of the WKB approximation are diﬃcult to generalize to rank K > 2,
and for a long time this proved a stumbling block to giving nontrivial illustrations of the
general statements of [5, 17] in the higher rank case. As we brieﬂy explain in §10.9, the
spectral networks Wϑ in theories of class S appear to be the key missing ingredient to
solve this problem: they provide a way of constructing a basis of ∇(ζ)-ﬂat sections in each
connected component of the complement of Wϑ, with “good WKB asymptotics” as ζ→ 0
in a half-plane Hϑ. Thus, the walls of the spectral networksWϑ also have an interpretation
as Stokes curves. Similar statements have appeared before in the mathematical literature,
e.g. [18, 19] and especially [20] which contains some examples of spectral networks with
K = 3.
Open problems
Our work in this paper leaves many directions unexplored or incompletely explored. Here
are a few:
3Again, here we are glossing over some slight diﬀerences between our setup and that of Fock-Goncharov,
and ignoring some extra discrete “ﬂag data” attached to the connections.
– 5 –
1. We discuss the theories S[g,C,D ] only for g of type A. There should be a closely
parallel story for g of type D or E. Some parts of this story are easy to predict:
the walls of the spectral networks will be labeled (locally) by roots of g, and spectral
networks will correspond to coordinate systems on moduli spaces of g-connections
overC. It would be desirable to work out this picture in detail.
2. Even in the case of type A our story is not quite complete. We take the charges of
BPS states to be valued in the lattice Γ =H1(Σ; Z), but according to the more precise
picture in [3, 21], it is better to identify the charge lattice as a certain subquotient
of H1(Σ; Z). This is related to the fact that our nonabelianization map Ψ Wϑ most
directly produces connections with structure group GL(K, C), while the physically
relevant objects should really be connections with structure group SL(K, C), con-
sidered modulo some further discrete equivalences [21]. There are likely to be some
topological subtleties here which deserve careful consideration.
3. Many of the results of [3] for K = 2 are subsumed in the present paper and extended
to K >2. However, there is one important piece of [3] which we have not extended
to K >2. Namely, we gave a recipe for computing an object called the “spectrum
generator,” which completely determines the whole 4d BPS spectrum of the theory
at any point u. This recipe uses only the combinatorics of a single spectral network
Wϑ, for a ﬁxed generic ϑ. It would be desirable to extend it to the case K > 2,
and also to types D and E. One could further ask for an extension of the spectrum
generator to include the 2d spectrum. 4
4. It would be desirable to generalize our discussion of BPS indices to include informa-
tion about the spins of the BPS states. This means taking y⁄=±1 in the various
indices deﬁned below. Some aspects of the “motivic 2d-4d wall-crossing formula”
which governs these degeneracies were spelled out in [5], but important details re-
main to be ﬁlled in.
5. In §10.7 we paint a heuristic picture of the “space of all spectral networks,” which
would be nice to spell out more precisely.
6. We conjecture in §10.8 that the coordinate systems Ψ W on the space M of ﬂat
connections are cluster coordinate systems. It would be very interesting to prove this
conjecture. It would be even more interesting if it turned out that the Ψ W actually
exhaust the set of cluster coordinate systems. This might be of some internal use for
the study of cluster varieties, e.g. for the positivity conjectures of [13].
7. In this paper we always require that the curve C carries at least one defect Dn. This
restriction (which we also imposed in [3]) leads to some simpliﬁcations. One reason
for these simpliﬁcations is that the walls inWϑ are solutions of diﬀerential equations,
and it seems that these equations generically imply that each wall is “attracted”
4In the case K = 2 this has been worked out by Pietro Longhi.
– 6 –
asymptotically to some defect. In particular, any open path ℘ on C meetsWϑ only
ﬁnitely many times.
This contrasts sharply with the case without defects: in that case, a typical open path
on℘ may meetWϑ inﬁnitely many times. We are hopeful that all of the constructions
of this paper still make sense in that setting, but there will be issues of convergence
to consider.
Fortunately, some things can be said about the asymptotic behavior of the walls even
in the case without defects. For example, in the case K = 2 the walls in Wϑ are
horizontal trajectories of a holomorphic quadratic diﬀerential e2iϑφ2, and the leading
asymptotic behavior of a generic such trajectory is classiﬁed by a virtual “limit cycle”
in H1(C, R), with deviations governed by certain Lyapunov exponents; see [22] for a
very useful review. One can hope that using these kinds of results (and their to-be-
developed generalizations for K >2) it will be possible to extend everything in this
paper to the case without defects.
8. In this paper we mainly work at a generic point of the Coulomb branch, where the
gauge symmetry group in the IR is abelian. If the parameters at the defects are
adjusted carefully (or if there are no defects at all) there may also be points where
the unbroken gauge symmetry is nonabelian. The physics of this situation is much
less explored than the fully abelian case. Nevertheless, much of what we have said
should have an extension to this situation.
In particular, a spectral network W associated to a K-fold covering Σ→ C should
give not only a map ΨW between moduli of ﬂat GL(1) connections on Σ and moduli
of ﬂat GL(K) connections on C, but more generally a map ΨW,N between moduli of
ﬂat GL(N) connections on Σ and moduli of ﬂat GL(NK ) connections on C.5 Our
construction of ΨW in§10 is set up in a way that should generalize directly to this
setting. We understand that similar constructions will appear in upcoming work of
Goncharov and Kontsevich.
9. In this paper we encounter several tricky sign issues. One of these ﬁrst pops up as
an ambiguity in the notion of “fermion number,” which leads to an ambiguity in the
sign of the 2d BPS degeneracies, and recurs many times thereafter. We have found
a scheme for ﬁxing this sign ambiguity, which we use systematically throughout the
paper: very roughly speaking, it amounts to considering paths on C and Σ weighted
by signs which keep track of the parity of the number of times the tangent direction
to the path winds around the circle. Our slavish implementation of this scheme has
various consequences, leading us e.g. to consider twisted ﬂat connections on C and Σ
in§10 rather than ordinary ﬂat connections. (Twisted connections onC also appeared
in [13], and this was a useful clue which helped us to ﬁnd our sign prescription.)
5One way of thinking about this is that the K-fold covering Σ could arise as a non-reduced degeneration
of an NK -fold covering, where the sheets coalesce in groups of N. Readers who prefer to think in terms of
M-theory ﬁvebranes might say that we consider the theory of NK ﬁvebranes wrapped on C⊂ T∗C, and
then move to a point of the Coulomb branch represented by N ﬁvebranes wrapped on Σ⊂T∗C.
– 7 –
While this scheme leads to a consistent picture both mathematically and physically,
we cannot say that we have really understood from physical ﬁrst principles why it
works so well. It would be very good to have a better understanding of how our sign
rule arises from the physics of the six-dimensional theory S[g].
10. In this paper we consider spectral networks Wϑ associated to a phase ϑ and a point
u of the Coulomb branch. It is natural to ask whether every spectral network W
(modulo the natural notion of equivalence described in §10.6) arises asWϑ for some
(u,ϑ ). If the answer is “no,” can we classify those spectral networks which do occur?
11. It is natural to ask whether the framed BPS degeneracies can be categoriﬁed. We
have done some work along these lines with E. Witten, and we hope to return to it.
12. The networksWϑ we study onC are made up of “S-walls,” the loci where framed 2d-
4d BPS state degeneracies jump. They depend on a point u of the Coulomb branch
B, so reallyWϑ =Wϑ(u) although we usually do not write this dependence explicitly.
On the other hand, very similar networks Dϑ appear directly on B: they are made
up of “K-walls,” the loci where 4d framed BPS state degeneracies jump. Dϑ can be
studied by methods very similar to the methods we employ here forWϑ. In particular
this gives another scheme for computing the pure 4d BPS state degeneracies Ω( γ),
parallel to what we do here for µ(a). (This has also been pointed out by Kontsevich-
Soibelman.) Networks very similar to Dϑ have appeared previously in the mirror
symmetry literature, e.g. [23–27].
The family of networks Wϑ(u) on C and the single network Dϑ onB can be uniﬁed
into a network DWϑ onB× C. We believe that this is really the most natural
perspective, although we do not adopt it explicitly in this paper.
13. We give a recipe for determining the BPS degeneracies Ω( γ) from a degenerate spec-
tral network, and work out several examples, but not many. It would be interesting
to use spectral networks to study the spectrum of concrete theories, beyond the few
examples we consider in §8. One obvious possibility would be to consider the stan-
dard SU (K) gauge theories coupled to fundamental hypermultiplets. Even the BPS
spectrum of the pure SU (3) theory has been the source of some controversy; in this
paper we study it at strong coupling but do not analyze the more intricate weak-
coupling spectrum. It would be interesting to compare results obtained from spectral
networks with those in [28–31].
14. In the degenerate spectral networks we do examine we do not work out any example
where the resulting |Ω(γ)| > 2, which would suggest the possibility of higher spin
states in the BPS spectrum. It would be interesting to ﬁnd a degenerate spectral
network which gives such higher spin states.
15. In this paper we have made some signiﬁcant progress in the determination of BPS
spectra for a large class of N = 2 ﬁeld theories. We hope that these techniques can
shed light on some broader questions of general interest, such as to what extent the
– 8 –
BPS spectrum uniquely determines a theory, and whether one can always engineer a
theory to produce a desired (consistent) BPS spectrum.
Finally, we mention that in a companion paper [32] we apply the techniques of this
paper to make a more direct connection to the work of Fock and Goncharov on higher
Teichm¨ uller theory [13]. We also ﬁnd a formula for the spectrum generator for a special
class of spectral networks, valid for all K≥ 2; this gives an implicit determination of the
BPS spectrum in the corresponding theories.
