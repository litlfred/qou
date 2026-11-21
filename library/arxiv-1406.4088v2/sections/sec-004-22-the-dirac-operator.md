---
doc_id: arxiv-1406.4088v2
doc_title: "Ab initio calculation of the neutron-proton mass difference"
section_id: sec-004-22-the-dirac-operator
section_title: "The Dirac operator"
section_number: 2.2
pages: 16-17
source_pdf: 1406.4088v2.pdf
source_sha256: d8f2ff1efb5bea30
toc_source: outline
doc_brief: "Ab initio calculation of the neutron-proton mass difference — 27 sections: Front matter; 1; Outline"
---
The Dirac operator
The Wilson operator with tree-level clover improvement (36) is chosen as our lattice Dirac operator. The
starting point is the gauge-covariant Dirac operator, which acts on a spinor ﬁeld, ψ, as follows:
(D[U, A; e, q, m]ψ)x =
(4
a + m)ψx−
−1
2a
X
µ
h
(1 + γµ) exp(ieqa ˜Aµ,x) ˜Uµ,xψx+µ + (1 −γµ) exp(−ieqa ˜Aµ,x−µ) ˜U †
µ,x−µψx−µ
i
+
−ia
4
X
ν>µ

F ( ˜U)
µν,x + eqF ( ˜
A)
µν,x

[γµ, γν]ψx.
The gauge-invariance of the quark action is ensured by exponentializing the non-compact photon ﬁelds. We use
the MILC convention for the gamma matrices γµ (37). Note also that this Dirac operator differs from the usual
deﬁnition by an extra minus sign in front of the γ’s. F (U)
µν,x is the usual discretization of the gluon ﬁeld strength
tensor and is built up from the products of the gluon links along the “clover” path. F (A)
µν,x is a discretization
of the electromagnetic ﬁeld strength tensor. It is chosen as the sum of the photon ﬁelds around a two-by-two
plaquette centered at x in the µ −ν plane. Gluon and photon ﬁelds ( ˜U and ˜A) that enter the Dirac operator are
obtained by smearing the original gluon and photon ﬁelds. In this work the gluon ﬁelds have undergone three
levels of HEX smearing. The parameters of the HEX smearing procedure are chosen with care, as described in
Sec. 2.3. We smear the photon ﬁelds with the following transformation
Aµ,x →˜Aµ,x = 0.9 · Aµ,x + 0.1 ·
X
±ν̸=µ
(Aν,x + Aµ,x+ν −Aν,x+µ) ,
where A−ν,x = −Aν,x−ν.
The most important advantage of smearing is the reduction of the additive quark mass renormalization. In
our case, it has two contributions: one stems from non-trivial gluon ﬁelds, the other is due to the presence
of photons. Although a large additive renormalization is not a problem of principle, a small one facilitates
tuning the parameters in dynamical simulations. For illustration of the effect we deﬁne the electromagnetic
mass renormalization δ by a neutral mesonic state, which is obtained by dropping the disconnected part of the
propagator of the quark–anti-quark system. δ is deﬁned as the shift in the bare quark mass to get the same
meson mass as in the e = 0 case, see also Ref. (38). At a lattice spacing of 0.10 fm and a coupling of e = 1
the shift for the up quark is about δu = −0.070 without photon smearing, which is about the same size as the
additive mass renormalization coming from the gluons. With our smearing recipe we have a four times smaller
value δu = −0.017.
As any smearing, our choices for the photon and gluon ﬁelds change the results by effects that disappear in
the continuum limit. In Secs. 2.3 and 4 we demonstrate the advantages of our smearing choices.
