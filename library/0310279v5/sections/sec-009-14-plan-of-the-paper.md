---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS"
section_id: sec-009-14-plan-of-the-paper
section_title: "Plan of the paper"
section_number: 1.4
pages: 17-19
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
toc_source: outline
doc_brief: "Stabilization in the braid groups I: MTWS — 41 sections: Front matter; Introduction; The problem"
---
Plan of the paper
In Section 2 we set up the topological construction which will be the basis for our work.
We will show that there is a very special isotopy that takes us from X+ to X−. The trace
of the isotopy will be seen to be an immersed annulus CA whose double point set is the
union of ﬁnitely many pairwise disjoint clasp arcs. We call it a ‘clasp annulus’.
The principle tool in our proof of Theorem 2 is the study of certain ‘braid foliations’
of the immersed annulus CA and its preimage PA. Braid foliations were used by
the authors in earlier work [8]–[10], but always in the setting of embedded surfaces.
In Section 3 we review the ideas that we need from the literature on braid foliations.
Readers who are familiar with the literature will probably want to pass quickly over
Section 3, referring to it instead, as needed, later in the paper. In Section 4 we study
braid foliations of our immersed annulus. We will need to do hard technical work to
arrange things so that the clasp arcs are close to or contained in a union of leaves and
have nice neighborhoods (we call them normal neighborhoods) on the preimage annulus
PA.
In Section 5 we learn how to translate data in the braid foliation of CA and the induced
foliation of PA into data about the passage from the closed braid X+ to the closed braid
X−. The tools that are needed become increasingly complicated as we proceed. First,
we ask how far we can get with exchange moves and destabilizations. Flypes enter the
picture next, but in the form of very rudimentary examples which we call ‘microﬂypes’.
A rather surprising use of stabilization becomes apparent in Section 5.3. Brieﬂy, we learn
that stabilization is the tool for creating ﬂypes with weighted strands and complicated
braiding assignments in the moving blocks out of microﬂypes. G–exchange come into
play next. There are hints in this part of the work about the need for G–ﬂypes, however
the reasons for needing G–ﬂype templates will not become clear until we are part way
through the proof of the MTWS.
The proof of Theorem 2 is given in Section 6. We will see how G–ﬂype templates
arise. The most difﬁcult part of the argument will be the proof that for each ﬁxed braid
Geometry & Topology 10 (2006)
430
Joan S Birman and William W Menasco
index m = b(X+) the cardinality |T (m)| is bounded. The ﬁniteness can, perhaps, be
understood by appreciating that the ‘inﬁnite parts’ are pushed into the blocks in the
block-strand diagrams of the templates in T (m). This is, perhaps, the key point about
block-strand diagrams and templates: they are at the same time both very ﬂexible and
very inﬂexible. A given template supports a huge family of knots and links, because
there are no restrictions on the braiding assignments in the blocks, but on the other hand
a template always supports at most a special family of links.
The paper ends, in Section 7 with a discussion of open problems suggested by the
MTWS and by its proof. In a separate paper [6] several applications will be given to the
study of transversal knot types in the standard contact structure on R3.
Conventions
Results which will be used explicitly in the proof of the MTWS are highlighted by
calling them ‘propositions’ rather than ‘lemmas’. There are many remarks, scattered
throughout the paper. Most of them are guides to the reader. The end of a remark is
indicated by the symbol ♦.
Acknowledgments
The authors single out for special thanks John Etnyre, Keiko Kawamuro and the
unknown G&T referee. All three studied our manuscript with care and attention to
details in the proof, and asked the kind of questions that can only be asked by an expert,
leading us to clarify many tricky points.
This work has been in progress for so many years that it’s difﬁcult for us to even
remember everyone else who helped. With apologies for oversights we also thank Tara
Brendle, Oliver Dasbach, Ivan Dynnikov, Brian Mangum, Walter Neumann, Nancy
Wrinkle, Joel Zablow, Xingru Zhang, Joseph Birman and Melissa Menasco.
The ﬁrst author acknowledges partial support from the US National Science Foundation,
under grants DMS-9402988, 9705019, 9973232 and 0405586. She also wishes to
thank the Mathematics Department at the Technion (Israel Institute of Technology) for
hospitality during several visits when this paper was the main focus of her work. The
second author acknowledges partial support from the US National Science Foundations,
under grants DMS-9200881, 9626884 and 0306062; and the Mathematical Sciences
Research Institute, where he was a Visiting Member during winter/spring of 1997.
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
431
