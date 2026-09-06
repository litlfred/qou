---
doc_id: arxiv-1609.08719v1
doc_title: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE"
section_id: sec-011-32-lattice-matching
section_title: "Lattice matching"
section_number: 3.2
pages: 10-10
source_pdf: 1609.08719v1.pdf
source_sha256: f61ff2111e9a97f9
doc_brief: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE — We use a large census of hyperbolic 3-manifolds to experimentally investigate a conjecture of Neumann regarding the Bloch Group."
---
manifolds← sort by increasing volume(manifolds)
next i← 2 ⊿ Whichei we seek a manifold for
rational vecs←{ (manifolds 1,e 1)} ⊿ Tuples (M, v), with v∈ Qn
rational basis←{manifolds 1} ⊿ All M associated to some ei
for all M∈manifolds except manifolds 1 do
dep = lindep(vol(M),rational basis) ⊿ Via PARI;⟨dep,volumes⟩ = 0
if dep shows vol(M) is not a linear combination of others then
if dep shows vol(M) is a rational combination of others then
rational vecs←rational vecs∪{ (M),dep −1
1 dep2,3,...,n+1}
else
if next i>n then
return Failure ⊿ There are more than n l.i. manifolds
end if
rational basis←rational basis∪{M}
rational vecs←rational vecs∪{ (M),enext i}
next i←next i + 1
end if
end if
end for
gcd←∞
best det←∞
best basis← ∅
for all B⊆rational vecs with|B| =n do
det← det({v| (M,v )∈B})
if det⁄= 0 then
gcd← fractional gcd(gcd,det )
if det<best det then
best det←det
best basis←B
end if
end if
end for
return (basis, ﬁt ratio) := (best basis, best det
gcd )
3. Experimentation
Our main results are the following data.
For our work, we used the volumes for a large number of hyperbolic 3-manifolds,
which we obtained by performing Dehn surgery on manifolds from a base census.
We used SnapPy [CDW], although for invariant trace ﬁeld calculations we used the
older Snap [Goo] interface.
