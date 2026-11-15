---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-070-e2-euclidean-response-functions-in-different-coo
section_title: "E.2 Euclidean Response Functions in Different Coordinates"
section_number: null
pages: 163-165
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
Euclidean Response Functions in Diﬀerent Coordinates
In all the ρ(k), we can choose ri to be particle i’s absolute position, we can also
choose ri to be particle i’s relative position in the center of mass frame. The response
functions calculated using the center of mass ri multiply by a factor of e−k2τ/2M will
be those calculated using the absolute coordinate ri, where M = Am is the total mass
of system. This can be explained by decomposing the separable Hamiltonian into the
center of mass part HCM = P 2/2M, where P = PA
i=1 pi is the total momentum, and
a relative part Hrel ﬁrst (Messiah (2014)), then make use of the momentum translation
operators.
The relevant part in Eq.(4.41) in absolute coordinate is
⟨Φ0|
X
j
e−ik·ˆrje−Hτ X
n
eik·ˆrn|Φ0⟩= ⟨Φ0|
X
j
e−ik·ˆrje−P 2
2M τe−Hrelτ X
n
eik·ˆrn|Φ0⟩. (E.38)
The total momentum P of the ground state |Φ0⟩is 0, and the momentum translation
operator eik·ˆrn will move particle n’s momentum by k, therefore P
n eik·ˆrn will change
the system’s total momentum from 0 to k and we have
X
n
eik·ˆrn|Φ0⟩= |k⟩.
(E.39)
Also consider that the Hamiltonian is translational invariant, so [H, P ] = 0 and
therefore [Hrel, P ] = 0, so e−Hrelτ and e−P 2
2M τ commute, then Eq.(E.38) becomes,
⟨Φ0|
X
j
e−ik·ˆrje−P 2
2M τe−Hrelτ X
n
eik·ˆrn|Φ0⟩
= ⟨Φ0|
X
j
e−ik·ˆrje−Hrelτe−P 2
2M τ X
n
eik·ˆrn|Φ0⟩
= e−k2τ
2M ⟨Φ0|
X
j
e−ik·ˆrje−Hrelτ X
n
eik·ˆrn|Φ0⟩.
(E.40)
The relevant part in Eq.(4.41) in the center of mass coordinate is
⟨Φ0|
X
j
e−ik·(ˆrj−ˆ
RCM)e−P 2
2M τe−Hrelτ X
n
eik·(ˆrn−ˆ
RCM)|Φ0⟩,
(E.41)
where ˆRCM =
P
i ˆri
A
is the center of the mass operator. Note that e−ik· ˆ
RCM is also a
momentum translation operator which changes the system’s total momentum by −k,
e−ik· ˆ
RCM|Φ0⟩= e−ik·
P
i ˆri
A |Φ0⟩= | −k⟩.
(E.42)
So, the combined operator P
n eik·(ˆrn−ˆ
RCM) = e−ik· ˆ
RCM P
n eik·ˆrn does not change the
system’s total momentum. Therefore, the ground state’s total momentum P remains
153
zero after being operated by P
n e±ik·(ˆrn−ˆ
RCM). Also, ˆRCM commutes with Hrel so
e±ik· ˆ
RCM and e−Hrelτ commute with each other. Taking all these into consideration,
Eq.(E.41) becomes,
⟨Φ0|
X
j
e−ik·(ˆrj−ˆ
RCM)e−P 2
2M τe−Hrelτ X
n
eik·(ˆrn−ˆ
RCM)|Φ0⟩
= ⟨Φ0|
X
j
e−ik·ˆrjeik· ˆ
RCMe−Hrelτe−ik· ˆ
RCM X
n
eik·ˆrn|Φ0⟩
= ⟨Φ0|
X
j
e−ik·ˆrje−Hrelτ X
n
eik·ˆrn|Φ0⟩
(E.43)
Comparing Eq.(E.40) and Eq.(E.43), we see that the center of mass result Eq.(E.43)
need to multiply by the factor of e−k2τ
2M to match the result in absolute coordinate
Eq.(E.40). Take 4He as an example, in our plots, k = 350 MeV/c, m = 939 MeV/c2,
M = 4m = 8, so the factor e−k2τ
2M becomes e−16.3τ. We calculate our response functions
in the center of mass frame ﬁrst because it will give lower variance compared with
absolute coordinate (laboratory frame). We then multiply our results by e−16.3τ in
order to compare with the results in Carlson and Schiavilla’s 1994 paper which are
marked as the red dots in Figs. 4.12 and 4.13.
154
