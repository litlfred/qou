---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-012-28-generalization-to-un
section_title: "Generalization to U(N)"
section_number: 2.8
pages: 21-22
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
For simplicity, in this paper we mostly consider Chern-Simons theory onM3 with gauge group
beingG =SU (2) and the 3d/3d dual theoryT [M3;SU (2)]. However, in principle, everything
we say above and below for SU (2) can be easily generalized to the SU (N) or U(N) case;
there are no obstructions for that. In particular, the formulae appearing in Conjecture 2.1
generalize as follows for G =U(N):
ZU(N)k[M3] = (i
√
2k)N(b1(M3)−1)/2 ∑
a∈ (TorH1(M3,Z))N/SN
eπik ∑N
i=1𝓁k(ai,ai)Za(q), (2.42)
Za(q) =
∑
b∈ (TorH1(M3,Z))N/SN
eπik ∑N
i=1𝓁k(ai,ai)Sab ˆZb(q)
⏐⏐⏐
q→e
2πi
k
, (2.43)
Sab =
∑
σ∈SNe2πi ∑N
i=1𝓁k(ai,bσ(i))
|StabSN (a)|·| TorH1(M3, Z)|N/2, (2.44)
ˆZa(q)∈ (N!)−cq∆aZ[[q]]. (2.45)
As before, using the linking pairing one can identify (Tor H1(M3))N/SN with the set of
connected components of abelian ﬂat connections:
(TorH1(M3))N/SN
𝓁k∼= Hom
(
TorH1(M3),U (1)N)
/SN ∼= π0Mab
ﬂat(M3,U (N)) (2.46)
where SN is the permutation group of a set with N elements. The factorization formulae
(2.37) and (2.39) generalize as follows
I(q,t ) =
∑
a∈ (TorH1(M3,Z))N/SN
|Wa|ˆZa(q,t )ˆZa(q−1,t−1), (2.47)
Itop(q,t ) =
∑
a∈ (TorH1(M3,Z))N/SN
|Wa|ˆZa(q,t )ˆZa(q−1,t ), (2.48)
with
Wa≡ StabSN (a). (2.49)
Physically, there are several ways to understand the special role of abelian ﬂat connections
or, more generally, reducible ﬂat connections for G of higher rank. As we already mentioned
in section 2.2, from the viewpoint of quantum ﬁeld theory (on ﬁvebrane world-volume or
its various reductions and limits) this follows directly from the resurgent analysis. On the
other hand, by looking at the same system ( 2.13) from the vantage point of the Calabi-Yau
3-fold, the set (2.46) which labels the new invariants ˆZa(q) and their categoriﬁcationHa[M3]
can be understood as charges of the BPS states or enumerative invariants of the Calabi-Yau
3-fold. We elaborate on this perspective in the following two subsections, expanding the web
of dualities and interpretations.
– 20 –
