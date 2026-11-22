---
doc_id: arxiv-2007.15570v1
doc_title: "A quantum Monte Carlo based approach to intranuclear cascades"
section_id: sec-009-a-mean-free-path
section_title: "A Mean free path"
section_number: null
pages: 6-7
source_pdf: 2007.15570v1.pdf
source_sha256: 6e46f4346a29fd83
toc_source: outline
doc_brief: "A quantum Monte Carlo based approach to intranuclear cascades — 16 sections: Front matter; A quantum Monte Carlo based approa; I Introduction"
---
The simplest validation consists of calculating the
mean free path of a nucleon travelling through a medium
of uniformly distributed nucleons, with ﬁxed interaction
cross sections. Our goal is to obtain
λmfp = 1
σρ,
(11)
where σ is the nucleon-nucleon cross section, and ρ is the
number density of nucleons. We simulate a background
of static, randomly and uniformly distributed protons
and neutrons at rest. For an event, we insert into the
medium a test particle with a ﬁxed energy and propa-
gate it through the medium. When the ﬁrst interaction
happens, we record the length the test particle has trav-
eled. Figure 5 shows the distribution of lengths traveled
for a 500 MeV test proton in a 0.16 nucleons/fm3 back-
ground density of nucleons, assuming a ﬁxed interaction
cross section of 50 mb, and using the Gaussian interac-
tion probability. The expected distributions, according
to Eq. (11), are also shown for the ﬁtted (black line)
and the expected (orange line) values of the mean free
path. The nuclear density and interaction cross section
were chosen arbitrarily. Adjusting these values does not
change the agreement between the expected mean free
path and the calculated mean free path. While not shown
here, using the cylinder interaction probability does not
change the results either. As we can see, our code cor-
rectly reproduces the expected behavior for the mean free
path, allowing us to proceed to more complex tests of our
INC.
B.
