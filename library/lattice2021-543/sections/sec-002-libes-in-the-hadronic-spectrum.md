---
doc_id: lattice2021-543
doc_title: "The neutron-proton mass diﬀerence"
section_id: sec-002-libes-in-the-hadronic-spectrum
section_title: "LIBEs in the hadronic spectrum"
section_number: null
pages: 4-5
source_pdf: LATTICE2021_543.pdf
source_sha256: 3a255daa50ebd5a4
toc_source: outline
doc_brief: "The neutron-proton mass difference — 9 sections: Front matter; QCD+QED at LO; Introduction"
---
The LIBEs in the hadronic spectrum can be drawn from Feynman diagrams. For mesons the
explicit expressions are provided in [6]. For baryons the drawing convention is analogous to [4]:
¯ΔM퐶(1)
푁= −
+
,
...
.
,
(5)
¯ΔC퐶(1)
푁= −
+
,
...
.
,
(6)
¯Δself퐶(1)
푁= −
−
+
+
,
...
.
,
(7)
¯Δexch퐶(1)
푁= −
+
,
...
.
,
(8)
¯Δloop퐶(1 푓)
푁
= −
+
,
...
.
.
(9)
The dots “...” are a shorthand to denote the other diagrams trivially obtained considering the
insertions on the other legs. The index 푖= 1, 2, 3 in ¯Δ푥퐶(푖)
푁corresponds to the quark propagator
with the insertion of the current generating the slope (except for ¯Δexch퐶(푖)
푁, where 푖denotes the leg
unaﬀected by the photon exchange). The
and
are the insertions of the scalar and pseudoscalar
currents respectively. For the Ω−it’s akin, diﬀering for ﬂavor content, spin 3/2 projection, and with
a factor 2 in front of the diagrams with crossed quark legs. From the above equations we deﬁne the
ratios R푥
푖= −휕푡[ ¯Δ푥퐶(푖)
R /퐶(0)
R ] for 푥∈{M, C, self, exch} and Rloop
푖푓
= −휕푡[ ¯Δ푥퐶(푖푓)
R
/퐶(0)
R ] , where
R = 푁, Ω . The LIBEs in the nucleon doublet then assume the following form (see eq. (3)):
Δ푀푛= −Δ푚푢푁M
1 −Δ푚푑푁M
2 −Δ푚푑푁M
3 + Δ푚(푐푟)
푢
푁C
1 + Δ푚(푐푟)
푑
푁C
2 + Δ푚(푐푟)
푑
푁C
3
+ 푞2
푢푁self
1
+ 푞2
푑푁self
2
+ 푞2
푑푁self
3
+ 푞푢푞푑푁exch
3
+ 푞푢푞푑푁exch
2
+ 푞2
푑푁exch
1
+
Õ
푓∈(푠푒푎)
푞푓
h
푞푢푁loop
1 푓
+ 푞푑푁loop
2 푓
+ 푞푑푁loop
3 푓
i
+ [isosymm. vac. pol. diag.]
,
(10)
and
Δ푀푝= −Δ푚푑푁M
1 −Δ푚푢푁M
2 −Δ푚푢푁M
3 + Δ푚(푐푟)
푑
푁C
1 + Δ푚(푐푟)
푢
푁C
2 + Δ푚(푐푟)
푢
푁C
3
+ 푞2
푑푁self
1
+ 푞2
푢푁self
2
+ 푞2
푢푁self
3
+ 푞푑푞푢푁exch
3
+ 푞푑푞푢푁exch
2
+ 푞2
푢푁exch
1
+
Õ
푓∈(푠푒푎)
푞푓
h
푞푑푁loop
1 푓
+ 푞푢푁loop
2 푓
+ 푞푢푁loop
3 푓
i
+ [isosymm. vac. pol. diag.]
.
(11)
The neutron-proton mass diﬀerence at LO is:
푀푛−푀푝= −2Δ푚푢푑[푁M
1 −푁M
2 −푁M
3 ] + 2Δ푚(푐푟)
푢푑[푁C
1 −푁C
2 −푁C
3 ]
+ (푞2
푢−푞2
푑)[푁self
1
−푁self
2
−푁self
3
−푁exch
1
]
+
Õ
푓∈(푠푒푎)
푞푓(푞푢−푞푑)
h
푁loop
1 푓
−푁loop
2 푓
−푁loop
3 푓
i
.
(12)
4
PoS(LATTICE2021)543
푀푛−푀푝in Lattice QCD+QED at LO in IB
Simone Romiti
Finally the IB correction to 푀Ω−is:
Δ푀Ω−= −Δ푚푠[ΩM
1 + ΩM
2 + ΩM
3 ] + Δ푚(푐푟)
푠
[ΩC
1 + ΩC
2 + ΩC
3 ]
+ 푞2
푠[Ωself
1
+ Ωself
2
+ Ωself
3
+ Ωexch
3
+ Ωexch
2
+ Ωexch
1
]
+
Õ
푓∈(푠푒푎)
푞푓푞푠
h
Ωloop
1 푓
+ Ωloop
2 푓
+ Ωloop
3 푓
i
+ [isosymm. vac. pol. diag.]
.
(13)
In this work we neglect the (disconnected) isosymmetric vacuum polarization diagrams, and
work in the electroquenched approximation: sea quarks are neutral with respect to the photon ﬁeld,
i.e. all diagrams with photons attached to quark loops vanish. This gives the numerical advantage
of not having to evaluate the LIBEs also in the sea quark determinant.
