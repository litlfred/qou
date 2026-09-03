---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-020-46-indexing-an-automatic-word
section_title: "Indexing an Automatic Word"
section_number: 4.6
pages: 18-19
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
Suppose W is an n-dimensional automatic word and M
¡
Q,q0,O,δ,Σ,S1,S2,...,Sn
¢
is its corresponding automaton with
output. Also let α be an alphabetic constant. We note that (x1,x2,...,xn) : W [x1][x2]···[xn] = @α is the automaton
¡
Q,q0,F,δ,S1,S2,...,Sn
¢
when minimized, where F =
©
q : O(q) = α
ª
. Similar arguments can be made for other comparison operators.
Suppose W1 and W2 are m- and n-dimensional automatic words, respectively, and let M1 and M2 be their corresponding
automata with output. We note that (x1,x2,...,xm, y1, y2,..., yn) : W1[x1][x2]···[xm] = W2[y1][y2]···[yn] is (M1×M2)(F) when
minimized, where F contains all (q1,q2) where q1 and q2 are states of M1 and M2, respectively, and they have the same
output. Similar arguments can be made for other comparison operators.
The above statements can be proved easily using the semantic rule explained in Section 3.6. Now what if indices are
arithmetic expressions and/or predicates with one free variable? The construction is based on substitutions similar to the
ones mentioned for calling expressions in Section 4.5.
18
5
