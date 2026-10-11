---
doc_id: arxiv-hep-lat-9806003v2
doc_title: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra"
section_id: sec-003-3-data-analysis
section_title: "Data analysis"
section_number: 3
pages: 2-3
source_pdf: 9806003v2.pdf
source_sha256: e34739e703aae6db
toc_source: inferred
---
In this section we give a detailed analysis of the data introduced in the previous section in the bulk of the spectrum.
We start with a description of the numerical unfolding approaches and their properties in Sec. III A. After a short
discussion of the nearest neighbor distribution in Sec. III B, we present data for spectral two–point correlations at
2
large scales in Sec. III C. From this we identify the equivalent of a Thouless energy. Furthermore we discuss higher
order correlators, in particular three–point correlations in Sec. III D. A qualitative explanation of deviations from
RMT predictions which are not due to the Thouless energy is given in Sec. III E.
A. Unfolding
As RMT is capable of making predictions for the ﬂuctuations on the scale of the mean level spacing, one has to
remove the inﬂuence of the level density by unfolding the spectra. The cumulative spectral function
N(λ) =
Z λ
−∞
dλ′
V/2
X
i=1
δ(λ′ −λi) ,
(3)
is the number of levels below or at the energy λ. It is frequently referred to as staircase function. It can be separated
into an average part Nave(λ), whose derivative is the level density, and a ﬂuctuating part Nﬂuc(λ),
N(λ) = Nave(λ) + Nﬂuc(λ) .
(4)
The average part is determined by gross features of the system and has to be removed. The ﬂuctuating part is in
all relevant systems of order O(1) and contains the correlations to be analyzed. After extraction of the average part
Nave(λ), it is unfolded from the spectra by the introduction of a dimensionless energy variable
ξi = Nave(λi) .
(5)
In this variable, the spectra have mean level spacing unity everywhere,
1/ρave(ξ) ≡1,
(6)
where ρave(ξ) = dNave(ξ)/dξ. However, the extraction of Nave(λ) from the data is non–trivial in our case because
little is known analytically about the level density of QCD spectra, particularly in lattice calculations. We thus have
to resort to phenomenological unfolding procedures. Faulty unfolding leads to wrong results, especially on such large
energy scales that we are interested in. In the subsequent Secs. III A 1, III A 2 and III A 3, we discuss three diﬀerent
