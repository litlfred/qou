---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras"
section_id: sec-010-2-the-weak-hopf-calculus
section_title: "The Weak Hopf Calculus"
section_number: 2
pages: 4-6
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
doc_brief: "Weak Hopf Algebras — We give an introduction to the theory of weak Hopf algebras pr oposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
2.1 The axioms
Deﬁnition 2.1 A weak bialgebra (WBA) is a quintuple (A,µ,u, ∆ ,ε ) satisfying Axioms 1, 2,
and 3 below. If (A,µ,u, ∆ ,ε,S ) satisﬁes Axioms 1, 2, 3, and 4 below it is called a weak Hopf
algebra (WHA).
Axiom 1. A is a ﬁnite dimensional associative algebra over a ﬁeld K with multiplication
µ:A ⊗A →A and unit u:K →A. I.e. µ and u are K-linear and satisfy
Associativity: µ ◦ (µ ⊗ id ) = µ ◦ (id ⊗µ) ( A.1)
Unit property: µ ◦ (u ⊗ id ) = id = µ ◦ (id ⊗u) ( A.2)
(Later on we will suppress µ and u, just write xy for µ(x,y ) and use the unit element
1 := u(1) instead of u.)
Axiom 2. A is a coalgebra over K with comultiplication ∆: A →A ⊗A and counitε:A →K.
I.e. ∆ and ε are K-linear and satisfy
Coassociativity: (∆ ⊗ id ) ◦ ∆ = (id ⊗ ∆) ◦ ∆ ( A.3)
Counit property: (ε ⊗ id ) ◦ ∆ = id = (id ⊗ε) ◦ ∆ ( A.4)
Axiom 3. For compatibility of the algebra and coalgebra structures w e assume
Multiplicativity of the coproduct: For all x,y ∈A
∆( xy) = ∆( x)∆( y) ( A.5)
Weak multiplicativity of the counit: For all x,y,z ∈A
ε(xyz) = ε(xy(1))ε(y(2)z) ( A.6a)
ε(xyz) = ε(xy(2))ε(y(1)z) ( A.6b)
Weak comultiplicativity of the unit:
∆ 2(1) = (∆(1) ⊗ 1)(1 ⊗ ∆(1)) ( A.7a)
∆ 2(1) = (1 ⊗ ∆(1))(∆(1) ⊗ 1) ( A.7b)
Axiom 4. There exists a K-linear map S:A →A, called the antipode, satisfying the following
Antipode axioms: For all x ∈A
x(1)S(x(2)) = ε(1(1)x)1(2) (A.8a)
S(x(1))x(2) = 1(1)ε(x1(2)) ( A.8b)
S(x(1))x(2)S(x(3)) = S(x) ( A.9)
4
In eqs. (A.6-9) we used a standard suﬃx notation for (iterate d) coproducts, omitting as usual
summation indices and a summation symbol.
In the terminology of [14] ( A,µ,u, ∆ ,ε ) is called a weak bialgebra if it satisﬁes the Ax-
ioms (A.1-5). There a weak bialgebra is called monoidal if it satisﬁes (A.6) and it is called
comonoidal if it satisﬁes (A.7). As has been explored in detail in [14], t hese (co)monoidality ax-
ioms are precisely designed to render the category of A-modules (the category of A-comodules,
respectively) monoidal.
The dual of a weak bialgebra (weak Hopf algebra) A is the dual space ˆA := Hom K(A,K )
equipped with structure maps ˆ µ, ˆu, ˆ∆ , ˆε (, ˆS) deﬁned by transposing the structure maps of A
by means of the canonical pairing ⟨, ⟩: ˆA ×A →K :
⟨ϕψ,x ⟩ := ⟨ϕ ⊗ψ, ∆( x)⟩
⟨ˆ1,x ⟩ := ε(x)
⟨ˆ∆( ϕ),x ⊗y⟩ := ⟨ϕ,xy ⟩
ˆε(ϕ) := ⟨ϕ, 1⟩
⟨ˆS(ϕ),x ⟩ := ⟨ϕ,S (x)⟩
where ϕ,ψ ∈ ˆA and x,y ∈A.
Let f and g be maps from the m-fold tensor product A⊗m to the n-fold tensor product
A⊗n such that they are composites of tensor products of the struc ture maps µ,u, ∆ ,ε,S and
of the twist maps τij interchanging the i-th and the j-th A factors. Then the equality f = g
is called an A-statement. Similarly one deﬁnes the ˆA-statements. Now every A-statement
Q :: f =g determines an equivalent ˆA-statementQT :: fT =gT obtained by reversing the
order of composition and replacing µ with ˆ∆, u with ˆε, ∆ with ˆ µ, ε with ˆu, and S with ˆS.
The statement QT is called the transpose ofQ.If we now substitute µ,u, ∆ ,ε,S , respectively in
place of ˆµ, ˆu, ˆ∆ , ˆε, ˆS in the statement QT we obtain a new A-statementQ∼ :: f ∼ =g∼ which
is not equivalent to Q in general. This Q∼ will be called the dual of Q. For example one can
easily verify that the WBA axioms satisfy ( A.1)∼ = (A.3), (A.2)∼ = (A.4), (A.5)∼ = (A.5),
(A.6a)∼ = (A.7a), and (A.6b)∼ = (A.7b). Thus the weak bialgebra axioms form a selfdual set
of statements. This implies that the dual of a WBA is a WBA, too . The same holds for weak
Hopf algebras, since each one of the antipode axioms is a self dual statement. As a consequence
of selfduality if Q is a true statement in a WBA or in a WHA then Q∼ is also true there. This
principle extends also to statements involving both A and ˆA structure maps and canonical
pairing(s).
As has been proven in [14], the above selfdual set of WHA axiom s are equivalent to the
non-selfdual set of axioms given in [20]. In this work we will gradually reproduce all axioms of
[20] as a consequence of the present ones.
For a weak Hopf algebra ( A, 1, ∆ ,ε,S ) the following conditions are equivalent
• A is a Hopf algebra;
• ∆(1) = 1 ⊗ 1 ;
• ε(xy) = ε(x)ε(y) ;
• S(x(1))x(2) = 1ε(x) ;
• x(1)S(x(2)) = 1ε(x) .
The proof of these assertions are either trivial or will beco me trivial after acquainting the weak
Hopf calculus developed in the next subsections, see also [1 4].
5
