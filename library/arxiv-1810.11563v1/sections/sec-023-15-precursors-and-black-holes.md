---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-023-15-precursors-and-black-holes
section_title: "Precursors and Black Holes"
section_number: 15
pages: 51-54
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
In deﬁning precursor operators in AdS/CFT it is tempting to identify the single qubit
operator W with a local low-dimension CFT ﬁeld. However, local ﬁelds when they act
inject inﬁnite energy into the CFT system and this is not what we want. The remedy is to
smear the ﬁeld over a time interval. We would like the energy of the ﬁeld to be such that
it would increase the entropy of the black hole by one thermal unit. This means that the
energy should be equal to the temperature. We therefore assume that WL is an operator
that adds a thermal quantum to the left-side black hole.
Now let us apply the precursor U†(tw)WL U(tw) to the thermoﬁeld-double state:
|Ψ(tw)⟩ ≡ U†(tw)WL U(tw)|TFD⟩
= WL(tw)|TFD⟩ (15.61)
The operator WL(tL) is a Schrodinger picture operator that acts at t = 0, but its eﬀect
is exactly the same as adding a thermal quantum to the left side at time tw. We will be
especially interested in the case of large negative tw. This shown in ﬁgure 27.
When|tw|>>t∗ the infalling quantum created byWL undergoes a large blue shift as it
falls to the horizon. The result is that for most of its world line it is an extremely energetic
shock wave. This is despite the fact that the thermal quantum makes an extremely small
change in the energy of the black hole.
50
Figure 27
The shock wave has a large eﬀect on the geometry but an easy way to understand it is
through the Dray-’t Hooft eﬀect ( T. Dray and G. ’t Hooft, Nucl. Phys. B253, 173 (1985))
Instead of redrawing the Penrose diagram to reﬂect the gravitational back reaction on the
shape of the diagram we can use the rule that any trajectory crossing the shock wave gets
displaced and jumps as shown in ﬁgure 28 where we see the maximal slice anchored on
both sides at t = 0. The jump is from the point a to the point b.
Without the shock wave the maximal slice at t = 0 has no volume behind the horizon;
it passes right through the bifurcate horizon. But as one can see from ﬁgure 28 the shock
wave causes the maximal slice to gain a signiﬁcant volume as indicated by the dark blue
surfaces.
51
Figure 28
In order to study the eﬀects of such a shock wave I will give a general “master formula”
for the volume of the maximal slice as a function of the anchoring timestL, tR andtw. The
formula was derived by Shenker and Stanford https://arxiv.org/pdf/1306.0622.pdf
in another context but it was shown in Stanford-Susskindhttps://arxiv.org/pdf/1406.
2678.pdf that it is a good approximation to the volume of maximal slices 17. It is a purely
classical consequence of general relativity,
V
Glads
=S log{coshτL +τR
2 +e(|τw|−τ∗)+ 1
2 (τL−τR)} (15.62)
where τ is the dimensionless Rindler time, τ = 2πt/β, and S is the entropy.
Let us consider the complexity V/Glads at tL = tR = 0. The answer should be the
complexity of the precursor itself since the complexity of the TFD is zero. Using S≈K
17It is a good approximation as long as the times are not exponentially large, at which the classical
geometric description is expected to break down.
52
we ﬁnd,
C(0, 0) =K log
(
1 +e(|τw|−τ∗))
, (15.63)
in agreement with 14.60. This is a truly remarkable result that relates classical solutions
of general relativity to properties of quantum circuit complexity.
The relation between complexity and volume is very general. It applies to any number
of shock waves sent in at any times. It also applies to localized non-spherical shock waves,
D. Roberts, D. Stanford and L. Susskind, https://arxiv.org/pdf/1409.8180.pdf .
