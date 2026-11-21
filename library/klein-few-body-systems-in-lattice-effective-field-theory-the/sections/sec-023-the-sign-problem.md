---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-Body Systems in Lattice Effective Field Theory"
section_id: sec-023-the-sign-problem
section_title: "The sign problem"
section_number: null
pages: 42-45
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
toc_source: outline
doc_brief: "Few-Body Systems in Lattice Effective Field Theory — 62 sections: Front matter; Introduction and Motivation; The standard model of particle phy"
---
As long as the system scales only proportional to the number of particles and L3 in the spatial size, we
do not have any storing problems for a large number of particles or a large box size. Sure enough, in
fermionic Monte Carlo systems one has to deal with a sign problem. While we interpret the Boltzman
factor as a probability factor and as such allows us to calculate the average of any observable just by
summing over its value for any conﬁgurations weighted by its probability, this is not possible anymore if
the weight is oscillating between negative and positive, which occurs by the exchange of two fermions
just by Fermi statistics. Such a new conﬁguration would cancel the old one making it very hard to extract
any valuable information from a Monte Carlo simulation. To be speciﬁc, we follow [105] and consider a
fermionic and bosonic path integral,
Z f =
X
n
Sign (n) exp [−S (n)] ,
(3.78)
Zb =
X
n
exp [−S (n)] ,
(3.79)
36
3.8 The sign problem
with Sign(n) = ±1 depending on the conﬁguration n of the system. S (n) is an action of a bosonic system.
Any fermionic observable is calculated as
⟨O⟩f = 1
Z f
X
n
O (n) Sign (n) exp [−S (n)] ,
(3.80)
which directly gives the expectation value of the Sign operator itself,

Sign
 =
Z f
Zb
∝exp
h
−βV

ff −fb
i
,
(3.81)
where the last equation is valid for large βV with the inverse temperature β = 1/(kBT) and f f , fb the
free energy of the fermionic and bosonic system, respectively. Due to the Pauli principle the free energy
density for fermions must be larger than the one for bosons and as such the average sign tends towards
zero exponentially for larger volumes.
Generally, the sign problem becomes severe when very sharp potentials are employed or when including
many fermions. In the framework of NLEFT, we can use a relatively low cutoﬀand trigonometric
discretization schemes are used to reduce the sign problem. Concerning this thesis we restrict the Monte
Carlo calculation to 4He, which is almost a SU(4) eigenstate. SU(4) symmetric problems do not suﬀer
from the sign problem and consequently, we do not expect too severe problems for the 4He calculation.
37
CHAPTER 4
