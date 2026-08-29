---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
2
2
Basics
3
2.1
Words and Automata . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
2.2
Number Systems
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
2.3
Automatic Words . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2.4
Automata accepting Predicates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
3
Syntax and Semantic of Predicates in Walnut
9
3.1
Alphabets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
3.2
Arithmetic and Alphabetic Constants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
3.3
Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
3.4
Operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
3.5
Arithmetic Expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
3.6
Indexing Expressions and Their Semantic Rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
3.7
Calling Expressions and Their Semantic Rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
3.8
Relative Expressions
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
3.9
Predicates
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
4
Decision Procedure: Walnut’s Implementation
12
4.1
Cross Product . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
4.2
Quantiﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
4.3
Complement and Reverse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
4.4
Arithmetic and Comparison Operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
4.5
Calling an Automaton
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
4.6
Indexing an Automatic Word . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
5
Special Automata in Walnut
19
5.1
True and False Automata . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
5.2
Non-arithmetic Automata . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
6
Installation
20
6.1
Eclipse
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
1
arXiv:1603.06017v2  [cs.FL]  25 May 2021
7
Commands
20
7.1
eval: eval <name> <predicate> . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
7.2
def: def <name> <predicate> . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
7.3
macro: macro <name> <template>
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
7.4
Matrices with eval and def . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
7.5
reg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
7.6
load: load <ﬁle name> . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
8
Working with Input/Output
32
8.1
Deﬁning Automata in Text Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
8.2
Deﬁning New Automatic Words
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
8.3
Deﬁning New Number Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
8.4
Converting .gv ﬁles to .jpeg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
34
References
34
1
Introduction
Walnut is a software package that implements a mechanical decision procedure for deciding certain combinatorial properties
of some special words referred to as automatic words or automatic sequences. To learn more about automatic words and
their applications, see [2]. To learn about decision procedures for automatic words, see Schaeffer’s Master’s thesis [8] and the
survey paper [9]. To read more about decidable properties of automatic words, refer to [4]. To read about another software
package that provided a similar mechanical decision procedure for automatic words, and was developed before Walnut, read
Goc’s Master’s thesis [7]. To see applications of Walnut, refer to [10–15].
The aim of this article is to introduce Walnut and explain its core features. This article consists of four parts: basics,
syntax, implementation, and the Walnut guide. In the ﬁrst part, Section 2, we establish the basic notation and concepts.
We go over words, automata, number systems, automatic words, and Presburger arithmetic. We learn what it means for an
automaton to accept a predicate. We also learn how to automatically decide properties of automatic words.
The second part, Section 3, talks about the building blocks of predicates: constants, variables, operators, and different
types of expressions. The semantics of predicates in Presburger arithmetic are well-known and are not explained, whereas
semantic rules for calling and indexing, with which we extend the Presburger arithmetic to include automatic words, are
explained in detail.
The third part, Sections 4 and 5, explains the decision procedure implemented in Walnut. The cross product of two
automata, which is behind the construction of automata for all binary logical operators, is introduced. Building on that,
we see how to construct automata for predicates from automata for subpredicates. In Section 5, we talk about two types of
automata that do not appear often in Walnut, but are nevertheless important to understand.
The fourth and last part, Sections 6–8, starts with Walnut’s installation and goes over all of its commands, i.e., exit, eval,
def, reg, and load. In Section 8, we learn how to manually deﬁne automata in text ﬁles. We also learn how to deﬁne new
number systems.
If you are already familiar with the objects described in the ﬁrst sentence of this introduction, you can skip Section 2
and come back to it only as a reference. For a more comprehensive treatment of the theory behind decision procedures for
automatic words refer to [4, 8, 9].
Since this article is more about Walnut than the theory behind it, when we explain the latter, we use Walnut’s notation as
opposed to the more familiar mathematical notation. For example, we use & and A for conjunction and universal quantiﬁer
as opposed to ∧and ∀of mathematical logic 1. As another example, when we deﬁne structures such as number systems
or objects such as automatic words, we give the deﬁnitions that are closer to Walnut’s capabilities than the most general
theoretical ones possible. This will help the reader make a smoother transition from the theory to its application in Walnut.
You can download Walnut from Jeffrey Shallit’s website, or alternatively from GitHub. Walnut is written in Java and
is open source. It is licensed under GNU General Public License. We would appreciate it if users cite this article in their
publications. For automata minimization Walnut relies on Valmari’s minimization algorithm [6]. In order to use this
minimization algorithm in Walnut, we manually translated Valmari’s C++ implementation [5] almost varbatim to Java. For
1Users enter logical predicates in a terminal when they use Walnut. We ﬁnd that entering latex-like commands in the terminal, e.g., \forall, does not
improve the readability.
2
converting regular expressions to automata, Walnut relies on the automata library in [3]. We would greatly appreciate it if
users report bugs to sh2mousa@uwaterloo.ca. The author would like to thank Jeffrey Shallit for revising this article.
2
