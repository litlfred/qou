---
doc_id: arxiv-1406.4088v2
doc_title: "Ab initio calculation of the neutron-proton mass difference"
section_id: sec-005-23-hex-smearing
section_title: "HEX smearing"
section_number: 2.3
pages: 17-17
source_pdf: 1406.4088v2.pdf
source_sha256: d8f2ff1efb5bea30
toc_source: outline
doc_brief: "Ab initio calculation of the neutron-proton mass difference — 27 sections: Front matter; 1; Outline"
---
HEX smearing
In our study, the gluon ﬁelds U have undergone three levels of HEX smearing (39). The smearing procedure
replaces the original gluon ﬁelds U with the HEX smeared ˜U:
Vµ,νρ,x = exp
ρ1
2
X
±σ̸=µ,ν,ρ
n
Uσ,x Uµ,x+σ U †
σ,x+µ U †
µ,x −h.c.

−1
3Tr[.]
o
Uµ,x,
Wµ,ν,x = exp
ρ2
2
X
±ρ̸=µ,ν
n
Vρ,µν,x Vµ,νρ,x+ρ V †
ρ,µν,x+µ U †
µ,x −h.c.

−1
3Tr[.]
o
Uµ,x,
˜Uµ,x = exp
ρ3
2
X
±ν̸=µ
n
Wν,µ,x Wµ,ν,x+ν W †
ν,µ,x+µ U †
µ,x −h.c.

−1
3Tr[.]
o
Uµ,x.
(S6)
For further details on our implementation see (23).
Here, we illustrate our procedure of iterated HEX smearings on lattices generated in the pure-gauge case
with a Wilson action. We generated sets of matched lattices with a ﬁxed box length in units of the Sommer
scale L/r0 = 3. We used the formula for r0/a as a function of the gauge coupling from (40), which is based
on data from (41). A wide range of lattice spacings were covered from a = 0.245 fm down to a = 0.046 fm.
We consider the three-fold HEX smeared plaquette as a function of g2 on these lattices with special attention
to the g2 →0 behavior. Since the last step in Eq. (S6) is standard stout smearing, we restrict ourselves to
ρ3 = 0.12. This value has been used in many studies based on stout smearing in the past and is considered safe
by perturbative considerations (39). Hence, only two parameters need to be tuned to optimize the scaling to the
continuum limit. We selected the value ρHEX = (0.22, 0.15, 0.12) as our preferred HEX-smearing parameter.
These parameters correspond to αHYP = (0.44, 0.60, 0.72) in the HYP-smearing scheme. In Fig. S1 we show
results for the average plaquette, ⟨U□⟩, for three different smearing levels. ⟨U□⟩approaches 1 monotonically
in the continuum limit.
