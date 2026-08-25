---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-039-108-coordinate-systems-and-a-cluster-conjecture
section_title: "Coordinate systems and a cluster conjecture"
section_number: 10.8
pages: 71-72
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
Let us consider a spectral network W for which (10.25) is saturated. In this case, as we
have noted, ΨW is at least locally one-to-one. Thus the holonomies ˜Y˜γ of∇ab = Ψ−1
W (∇),
where ˜γ runs over a basis of H1(˜Σ; Z), provide local coordinates onMF (C,GL (K); m).
It is natural to ask whether Ψ W might be even globally one-to-one, so that it would
give global coordinates on its whole imageUW. We conjecture that this is indeed the case.33
At least in the case K = 2 this conjecture is true: in this case the coordinate system in
question is essentially the Fock-Goncharov coordinate system [3, 13]. Some further special
cases in which the conjecture is true will be treated in [32].
As we noted above, ifW andW′ are equivalent nondegenerate spectral networks then
ΨW and ΨW′ are related by parallel transport, in the sense explained under (10.26). Thus
we can roughly say that ΨW is constant asW varies within one of the cells of X. IfW and
W′ are in neighboring cells, then the story is more interesting: taking a path W(t) fromW
toW′, there is a critical t =tc whereW(t) becomes a degenerate spectral network. At this
moment ΨW(t) jumps discontinuously. This jump should be determined by the arguments
of§6.3. Indeed, by the same formulas we used there (and assuming the same conjectures we
assumed there), the degenerate networkW(tc) determines integers Ω(γ) and distinguished
lifts ˜γ, for γ lying in a semilattice Γ c⊂H1(Σ(tc); Z) with a single generator. Using these
data we deﬁne a (birational) automorphism K ofM(Σ(tc),GL (1); m), by its action on the
holonomies ˜Y˜γ of∇ab around 1-cycles ˜γ:
K( ˜Y˜γ) = ˜Y˜γ
∏
γ′∈Γc
(1 + ˜Y˜γ′)⟨γ,γ′⟩Ω(γ′). (10.28)
When t crosses tc, the map ΨW(t) jumps by composition with K, so
ΨW(∇ab) = ΨW′(K±1(∇ab)) (10.29)
(where the sign ±1 is determined by which direction we cross the cell boundary, and we
must bear in mind the comment under (10.27).)
Finally, we conjecture that the coordinate systems we have deﬁned are actually cluster
coordinates.34 The spacesM(C) which we are considering are indeed cluster varieties, as
shown by Fock-Goncharov in [13]. However, relatively few of the cluster coordinate systems
onM(C) have been described explicitly. We believe that for eachW, the coordinate system
induced by ΨW should be an element of the cluster atlas. So in particular, we conjecture
that there is an algorithm which determines from a W a ﬁnite set of charges γn
W∈ Γ. The
γn
W should be the elements of a cluster seed, with exchange matrix given by the intersection
pairings: ϵnm =⟨γn,γm⟩. Informally speaking, the γn
W should be the charges of ﬁnite webs
which can appear inside of W whenW degenerates; said otherwise, the γn
W label faces of
33This is the moment where it is important that we use the moduli space MF (C,GL (K); m) with ﬂag
data rather than justM(C,GL (K); m). If we usedM(C,GL (K); m), then ΨW would be only ﬁnite-to-one.
34It was noted in [9, 21] that the K-transformations which appeared there could be viewed as cluster
transformations in an appropriate sense; see also [10, 38, 48, 53, 54] for further discussion of the relation of
cluster varieties to four-dimensionalN = 2 theory.
– 69 –
the boundary of the cell in X containingW. Finally, theK-transformation (10.28), in the
simplest case where there is only a single Ω( γ) = 1 contributing, should be identiﬁed with
the action of a mutation on cluster variables.
This conjecture is true when K = 2, and in [32] we will give some additional evidence
for it in some special cases with K >2. In general, though, we do not know how to prove
it, or even how to read oﬀ the γn
W fromW.
It is natural to wonder further whether spectral networks might give all of the coordi-
nate systems in the cluster atlas on M.
