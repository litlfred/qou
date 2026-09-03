---
doc_id: arxiv-1712.08953v1
doc_title: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY"
section_id: sec-028-5-shortest-word-theory
section_title: "Shortest word theory"
section_number: 5
pages: 25-26
source_pdf: 1712.08953v1.pdf
source_sha256: 005e0b1ad63c173e
doc_brief: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY — The oriented skein category OS(z, t ) is a ribbon category which un- derpins the deﬁnition of the HOMFLY-PT invariant of an orien ted link, in the"
---
For the next few sections, we assume that k is a ﬁeld of characteristic p≥ 0 and
z =q−q−1 for q∈ k ×\{± 1}. Since we are going to be discussing linear representa-
tions rather than tensor ones, it is natural to replace the catego ryOS (z,t ) with the
associative algebra
OS =
⨁
a,b∈⟨↑,↓⟩
1aOS1b where 1 aOS1b := HomOS (z,t)(b, a),
multiplication being induced by composition in OS(z,t ). This algebra is locally unital
rather than unital, with a distinguished system of local units given by the mutu-
ally orthogonal idempotents {1a| a∈⟨↑,↓⟩}. The functor category Mod- OS(z,t ) of
OS (z,t )-modules as deﬁned in the introduction may be identiﬁed with the usu al alge-
braic category Mod-OS of all rightOS-modulesM which are locally unital in the sense
that M =⨁
a∈⟨↑,↓⟩M 1a. The additive Karoubi envelope ˙OS (z,t ) is equivalent to the
full subcategory pMod- OS of Mod-OS consisting of ﬁnitely generated projective mod-
ules, i.e., modules isomorphic to ﬁnite direct sums of right ideals eOS for idempotents
e∈ OS. This means that we may identify K0( ˙OS (z,t )) with the split Grothendieck
group K0(pMod-OS); the resulting ring structure on K0(pMod-OS) is determined by
[eOS][fOS ] = [(e⊗f )OS]
for idempotents e,f ∈OS.
Each 1 aOS1b is ﬁnite-dimensional by Theorem 1.2, hence, OS is locally ﬁnite-
dimensional, and Mod- OS is a locally Schurian category in the sense of [BD, §2]. We
will freely use the general language and results about such catego ries explained there,
most of which boil down to the observation that Mod- OS is a Grothendieck category.
In particular, we let lfdMod- OS be the subcategory of Mod- OS consisting of all locally
ﬁnite-dimensional modules , i.e., the OS-modules M such that dim k M 1a <∞ for all
a∈⟨↑,↓⟩. These are exactly the modules that have ﬁnite composition multiplicit ies.
Any ﬁnitely generated OS-module M is locally ﬁnite-dimensional, so that pMod- OS
is a subcategory of lfdMod- OS.
In this section, we are going to classify the irreducible OS-modules. The key to our
approach is that the algebra OS has a triangular decomposition. Any ribbon has three
sorts of component:
• cups whose boundary is on y = 1;
• caps whose boundary is on y = 0;
• propagating strands whose boundary intersects both y = 0 and y = 1.
The cups and caps carry an overall orientation that is either leftwa rd or rightward, while
the propagating strands are either upward strands or downward strands. Introduce the
following locally unital subalgebras of OS:
OS◦
r,s: The k -span of all ribbons that have r propagating upward strands and s
propagating downward strands, no components that are cups or caps, and in
which propagating upward strands only cross underneath propag ating down-
ward strands.
OS◦: ⨁
r,s≥0OS◦
r,s.
OS +: The k -span of all ribbons that have no components that are caps and in w hich
no two propagating strands cross.
OS♯: The k -span of all ribbons with no components that are caps and in which pr op-
agating upward strands only cross underneath propagating down ward strands.
OS−: The k -span of all ribbons that have no components that are cups and in w hich
no two propagating strands cross.
