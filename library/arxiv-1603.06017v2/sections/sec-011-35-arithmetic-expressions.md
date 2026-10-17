---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-011-35-arithmetic-expressions
section_title: "Arithmetic Expressions"
section_number: 3.5
pages: 9-11
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
---
3.3
Variables
A variable’s name must start with a letter and can contain upper- and lower-case alphanumerics and underscores. A variable’s
name cannot be E or A.
3.4
Operators
The full list of operators allowed in predicates can be found in Table 3.17. This list has operator precedences. The lower this
number is, the higher the precedence is. For example, multiplication by constant has the highest precedence. Parentheses
override all precedences. All operators are associative from left to right, except for complement ∼, reverse ` , quantiﬁers E
and A, calling $, and indexing [] which are all associative from right to left.
7we prefer this notation to those familiar from mathematical logic, because we want to liken our notation to those of programming languages, as Walnut
is ultimately a programming language.
9
precedence
operator
explanation
examples
1
∗
multiplication by a constant
2∗x and x ∗2
1
/
division by a constant
x/2 but not 2/x
2
+
addition
2
−
subtraction
3
=
equality
3
!=
inequality
3
<
less than
3
>
greater than
3
<=
less than or equal
3
>=
greater than or equal
4
∼
complement
4
`
reverse
5
&
conjunction
5
|
disjunction
5
∧
exclusive disjunction
6
=>
implication
7
<=>
equivalence
8
E
existential quantiﬁer
Ex, y,z or Ex Ey Ez
8
A
universal quantiﬁer
Ax, y,z or Ax Ay Az
9
$
calling
$M(x, y)
9
[]
indexing
T [i + j]
Table 3.1: List of operators in Walnut
3.5
Arithmetic Expressions
The permissible arithmetic operators are +,−,∗,/. Equality = is not an arithmetic operator. A constant expression is an
expression involving only constants and arithmetic operators that evaluates to a natural number, e.g., 4,3+2,6/4,2∗3 but
not −3 nor 2−3. An arithmetic expression is deﬁned recursively in the usual way:
• A constant expression is an arithmetic expression, e.g., 2,10,7−4, but not −1.
• A variable is an arithmetic expression, e.g., x, y,z,etc.
• For arithmetic expression e, the expression (e) is also arithmetic.
• For arithmetic expression e1 and e2 both of e1 +e2 and e1 −e2 are arithmetic expressions.
• For variable x and constant expression c all of x ∗c,c ∗x, and x/c are arithmetic expressions.
• For arithmetic expression e and constant expression c all of (e)∗c, c ∗(e), and (e)/c are arithmetic expressions.
An arithmetic expression on its own is not a predicate, and it is not meaningful to talk about an automaton accepting an
arithmetic expression. For example, talking about an automaton accepting x + y + z = 0 makes sense, while talking about an
automaton accepting x + y + z is not meaningful. Walnut reports an error if the user tries to construct an automaton for an
arithmetic expression.
See Section 4.4 to see how Walnut constructs automaton for valid predicates like
(y1 ⊗y2 ⊗···⊗ym)<(x1 ⊗x2 ⊗···⊗xn),
where the xi and y j are variables or arithmetic constants, ⊗are arithmetic operators, and < is a comparison operator.
10
