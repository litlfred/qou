---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-018-44-arithmetic-and-comparison-operators
section_title: "Arithmetic and Comparison Operators"
section_number: 4.4
pages: 16-17
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
Recall that for every number system S that we use in Walnut the three automata (a,b,c) : ?S a = b +c, (a,b) : ?S a = b10, and
(a,b) : ?S a < b are deﬁned. In this section we show that using these three automata and the decision procedure outlined in
Sections 4.1–4.3, we can construct automata for more complex relative expressions with lots of arithmetic operators.
9Unlike the reverse operator, operands for logical operators are predicates. The reader however understands the very thin and superﬁcial distinction
between automata and predicates in this article.
10This automaton does not need to be deﬁned explicitly by the user, because we assumed for all number systems S in Walnut a =S b if and only if a = b.
16
For a constant c > 0, a natural number, automata (a) : ?S a = c can be constructed recursively using automata (b) : ?S b = c′
and (a,b) : ?S a = b + 1 where c′ is the predecessor of c, i.e., c′ + 1 = c. For example, predicate ?S a = 2 is equivalent to
?S Eb a = b +1&b = 1. Similarly ?S b = 1 is equivalent to ?S Eb2 b = b2 +1&b2 = 0. Based on Deﬁnition 2, for all number
systems S, the automaton for ?S b2 = 0 is the simple automaton accepting 0∗. To construct automaton (a,b) : ?S a = b +1,
just note that the predicate is equivalent to ?S Ec a = b +c &c = 1.
A similar recursive argument can be applied to obtain (a,b) : a = c ∗b for a constant c > 0, i.e., one can construct
(a,b) : (a = b2 +b)&(b2 = c′ ∗b) where c′ is the predecessor of c. The similar argument can be applied to obtain automata for
division by constants or subtraction.
To construct (a,b) : ?S a <= b, note its equivalence to (a,b) : ?S a < b | a = b. With similar arguments, one can construct
automaton for other comparison operators.
It is important to understand Walnut’s construction of
(y,x1,x2,...,xn) : ?S y <(x1 ⊗1 x2 ⊗2 ···⊗n−1 xn)
where n ≥3. Here < denotes an arbitrary comparison operator, and the ⊗i are arbitrary arithmetic operators. Also let y and
xi be variables or arithmetic constants. All arithmetic operators in Walnut are associative from left to right; see Section 3.4.
Based on this, Walnut ﬁrst transforms the predicate to an equivalent predicate
(y,x1,x2,...,xn) : ?S Ey1,..., yn−2 (y1 = x1 ⊗1 x2)&(y2 = y1 ⊗2 x3)&···&(y = yn−2 ⊗n−1 xn).
Now Walnut has all the resources necessary to construct this last automaton.
For example, to construct (a) : 0<=(a −1+1), Walnut ﬁrst transforms it to (a) : Eb (b = a −1)&(0 = b +1). The automaton
is depicted below:
Figure 4.12: Automaton for 0<=a −1+1 does not accept 0∗
There is something here that is worth noting. Note how this automaton does not accept 0? In arithmetic over integers
a = 0 satisﬁes the predicate. However in Presburger arithmetic setting a = 0 gives b = −1, which is not acceptable, since
Presburger arithmetic is deﬁned over natural numbers. In order to ﬁx this issue, try to always postpone subtraction and
division to the rightmost position in your predicates. For example, writing (a) : 0 <= (a +1−1) results in
Figure 4.13: Automata for 0<=a +1−1 accepts 0∗
4.5
