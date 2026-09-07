---
doc_id: arxiv-0902.0350v1
doc_title: "A REVISION OF THE PROOFOF THE KEPLER CONJECTURE"
section_id: sec-001-1-the-flyspeck-project
section_title: "The Flyspeck project"
section_number: 1
pages: 3-5
source_pdf: 0902.0350v1.pdf
source_sha256: 4591687132c93973
doc_brief: "A REVISION OF THE PROOFOF THE KEPLER CONJECTURE — The Kepler conjecture asserts that no packing of congruent balls in three-dimensional Euclidean space has density greater than that of the"
---
The purpose of a long-term project, called the Flyspeck project, is to give a
formal proof of the Kepler conjecture. This section makes some preliminary
remarks about formal proofs and gives a general overview of the current
status of this project.
1.1. F ormal proof. A formal proof is a proof in which every logical in-
ference has been checked, all the way back to the foundational axioms of
mathematics. No step is skipped no matter how obvious it may be to a
mathematician. A formal proof may be less intuitive, and yet is less suscep-
tible to logical errors. Because of the large number of inferences involved, a
computer is used to check the steps of a formal proof.
It is a large labor-intensive undertaking to transform a traditional proof into
a formal proof. The first stage is to expand the traditional proof in greater
detail. This stage fills in steps that a mathematician would regard as obvi-
ous, works out arguments that the original proof leaves to the reader, and
supplies the assumed background knowledge. In a final stage, the detailed
text is transcribed into a computer-readable format inside a computer proof
assistant. The proof assistant contains mathematical axioms, logical rules
of inference, and a collection of previously proved theorems. It validates
each new lemma by stepping through each inference. No other currently
available technology is able to provide levels of certification of a complex
mathematical proof that is remotely comparable to that available by formal
computer verification. A general overview of formal proofs can be found
at [7], [21], [27].
Proof assistants differ in detail in the way they treat the formalization of
a theorem that is itself a computer verification (such as the proof of the
four color theorem or the proof of the Kepler conjecture). In general, a
formal proof of a computer verification can be viewed as a formal proof of
the correctness of the computer code used in the verification. That is, the
formal proof certifies that the the code is a bug-free implementation of its
specification.
1.2. F ormal proof of the Kepler conjecture. As mentioned above, the
purpose of the Flyspeck project is to give a formal proof of the Kepler
conjecture. (The project nameFlyspeck comes from the acronymFPK, for
the Formal Proofof theKepler conjecture.) This is the most complex formal
4 HALES, HARRISON, MCLAUGHLIN, NIPKOW, OBUA, AND ZUMKELLER
proof ever undertaken. We estimate that it may take about twenty work-
years to complete this formalization project.
The Flyspeck project is introduced in the article [12]. The project page
gives the latest developments [17]. The project is now at an advanced stage;
in fact, we estimate that the project is now about half-way complete. One
of the main purposes of this article is to present a summary of the current
status of this project.
In the original proof of the Kepler conjecture, there was a long mathematical
text and three major pieces of computer code. The written part of the
proof has been substantially revised with aims of the Flyspeck project in
mind. Section 2 compares this revised text with the original. There is now
a good match between the mathematical background assumed in the text
and the mathematical material that is available in the proof assistant HOL
Light. Section 3 describes the current level of support in HOL Light for the
formalization of Euclidean space and measure theory. In the years following
thepublication oftheoriginalproof, S. McLaughlinhasreworkedandlargely
rewrittentheentirebodyofcodeinaformthatismoretransparentandmore
amenable to formalization. Section 4 points out some difficulties in verifying
the computer code in its original form and documents the reimplementation.
There have been three Ph.D. theses written on the Flyspeck project, one
devoted to each of the three major pieces of computer code. The first piece
of computer code uses interval arithmetic to verify nonlinear inequalities. R.
Zumkeller’s thesis [49] develops nonlinear inequality proving inside the proof
assistant Coq. Section 5 gives an example of this work. The second piece of
computer code enumerates all tame graphs. (The definition of tameness is
rather intricate; its key property is that the set of tame graphs includes all
graphs that give a potential counterexample to the conjecture.) G. Bauer’s
thesis, together with subsequent work with T. Nipkow, completes the formal
proof of the enumeration of tame graphs [36]. Section 6 gives a summary of
this formalization project. The third piece of computer code generates and
runs some105 linear programs. These linear programs show that none of the
potential counterexamples to the Kepler conjecture are actual counterexam-
ples. S. Obua’s thesis develops the technology to generate and verify the
linear programs inside the proof assistant Isabelle [38]. Section 7 describes
this research.
The ultimate aim is to develop a complete formal proof of the Kepler con-
jecture within a single proof assistant. Because of the scope of the prob-
lem and the number of researchers involved, different proof assistants have
been used for different parts of the proof: HOL Light for background in Eu-
clidean geometry and the text, Coq for nonlinear inequality verification, and
Isabelle/HOL for graph enumeration and linear programming. This raises
A REVISION OF THE PROOF OF THE KEPLER CONJECTURE 5
the issue of how to translate a formal proof automatically from one proof
assistant to another. Implementations of automated translation among the
proof assistants HOL, Isabelle, and Coq can be found at [39], [32], [47], [4].
