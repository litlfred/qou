---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-009-3-the-coend-for-module-categories
section_title: "The (co)end for module categories"
section_number: 3
pages: 10-15
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B → C is an exact"
---
In this Section we recall the notion of relative (co)ends ; a tool developed
in [ 3] in the context of representations of tensor categories, ge neralizing the
well-known notion of (co)ends in category theory.
LetC be a tensor category and M be a left C-module category. Assume
thatA is a category and S :Mop×M→A is a functor equipped with
natural isomorphisms
(3.1) βX
M,N :S(M,X⊲N )→S(X ∗⊲M,N ),
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 11
for any X ∈C ,M,N ∈M . We shall say that β is a prebalancing of the
functor S. Sometimes we shall say that it is a C-prebalancing, to emphasize
the dependence on C.
Deﬁnition 3.1. The relative end of the pair ( S,β ) is an object E ∈ A
equipped with dinatural transformations πM :E ..− →S(M,M ) such that
(3.2)
S(M,M )
S((X ∗⊲X )⊲M,M ) S(X ∗⊲ (X⊲M ),M )
S(X⊲M,X ⊲M )
E
S(evop
X ⊲idM ,idM )
S(mop
X∗,X,M ,idM )
βX
X⊲M,M
πX⊲MπM
for any X∈C ,M ∈M , and is universal with this property. This means
that, if ~E∈A is another object with dinatural transformations ξM : ~E ..− →
S(M,M ), such that they fulﬁll ( 3.2), there exists a unique morphism h :
~E→E such that ξM =πM◦h.
The relative end depends on the choice of the prebalancing. W e will
denote the relative end as
∮
M ∈M(S,β ), or sometimes simply as
∮
M ∈MS,
when the prebalancing β is understood from the context.
The relative coend of the pair ( S,β ) is deﬁned dually. This is an object
C∈A equipped with dinatural transformations πM : S(M,M ) ..− →C such
that
(3.3)
S(M,M )
S(M, (X ∗⊗X)⊲M ) S(M,X⊲ (X ∗⊲M ))
S(X ∗⊲M,X ∗⊲M )
C
S(idM ,coevX ⊲idM )
S(idM ,mX,X ∗,M )
βX
M,X ∗⊲M
πX∗⊲MπM
for any X∈C ,M ∈M , universal with this property. This means that, if
~C∈A is another object with dinatural transformations λM :S(M,M ) ..− →~C
12 LENTNER AND MOMBELLI
such that they satisfy ( 3.3), there exists a unique morphism g :C→ ~C such
that g◦πM = λM . The relative coend will be denoted
∮ M ∈M(S,β ), or
simply as
∮ M ∈MS.
A similar deﬁnition can be made for right C-module categories. Let A
be a category, and N be a right C-module category endowed with a functor
S :N op×N→A with a prebalancing
γX
M,N :S(M ⊳X,N )→S(M,N ⊳ ∗X),
for any M,N ∈N , X∈C .
Deﬁnition 3.2. The relative end for S is an object E∈A equipped with
dinatural transformations λN :E ..− →S(N,N ) such that
(3.4)
S(N,N )
S(N,N ⊳ (X⊗ ∗X)) S(N, (N ⊳X)⊳ ∗X)
S(N ⊳X,N ⊳X)
E
S(idN ,idN ⊳ evX )
S(id,id⊗m−1
N,X,∗X )
γX
N,N ⊳X
λN ⊳XλN
for anyN∈N ,X∈C . We shall also denote this relative end by
∮
N ∈N (S,γ ).
Similarly, the relative coend is an object C∈B with dinatural transfor-
mations λN :S(N,N ) ..− →C such that
(3.5)
S(N,N )
S(N ⊳(∗X⊗X),N ) S((N ⊳∗X)⊳X,N )
S(N ⊳∗X,N ⊳ ∗X)
C
S(idN ⊳ coevop
X ,idN )
S(m−1 op
N,∗ X,X ,idN )
γX
N ⊳∗ X,N
λN ⊳∗ XλN
for any N ∈ N, X ∈ C. We shall also denote this relative coend by∮ N ∈N (S,γ ).
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 13
In the next Proposition we collect some results about the rel ative (co)end
that will be useful. The reader is referred to [ 3, Prop. 3.3], [ 3, Prop. 4.2].
Proposition 3.3. AssumeM,N are left C-module categories, and S, ~S :
Mop×M→A are functors equipped with C-prebalancings
βX
M,N :S(M,X⊲N )→S(X ∗⊲M,N ),
~βX
M,N : ~S(M,X⊲N )→ ~S(X ∗⊲M,N ),
X∈C ,M,N ∈M . The following assertions holds
(i) Assume that the module ends
∮
M ∈M(S,β ),
∮
M ∈M( ~S, ~β) exist and
have dinatural transformations π, ~π, respectively. If γ : S→ ~S is
a natural transformation such that
(3.6) ~βX
M,Nγ(M,X⊲N ) =γ(X ∗⊲M,N )βX
M,N,
then there exists a unique map ˆγ :
∮
M ∈M(S,β )→
∮
M ∈M( ~S, ~β) such
that
~πM ˆγ =γ(M,M )πM
for any M∈M . If γ is a natural isomorphism, then ˆγ is an iso-
morphism.
(ii) For any pair of C-module functors (F,c ), (G,d ) :M→N , the func-
tor
HomN (F (−),G (−)) :Mop×M→ vect k
has a canonical prebalancing given by
(3.7) βX
M,N : Hom N (F (M ),G (X ⊲N))→ HomN (F (X ∗⊲M ),G (N ))
βX
M,N (α) = (evX ⊲ id G(N ))m−1
X ∗,X,G(N )(id X ∗⊲d X,Nα)cX ∗,M,
for any X∈C ,M,N ∈M . There is an isomorphism
Natm(F,G )≃
∮
M ∈M
(HomN (F (−),G (−)),β ).
□
The next result will be needed later. It follows from a combin ation of [ 3,
Prop. 3.3] (ii) and [ 3, Lemma 3.6]. Let M be a leftC-module category, then
N =Mop is a right C-module category with right action given by
M ⊳X =X ∗⊲M.
AssumeA is a category equipped with a functor
S :N op×N→A ,
together with a prebalancing
βX
M,N :S(M ⊳X,N )→S(M,N ⊳ ∗X).
The functor
HomA(S(−,−),U ) :Mop×M→ vect k,
14 LENTNER AND MOMBELLI
has a natural prebalancing
γX
M,N : Hom A(S(M,N ⊳ ∗X),U )→ HomA(S(M ⊳X,N ),U ),
γX
M,N (f ) = f◦βX
M,N.
The proof of the next statement is similar to the proof of [ 3, Prop. 3.3 (ii)].
Proposition 3.4. If the coend
∮
M ∈N (S,β ) exists, then for any object U∈
A, the end
∮
M ∈M HomA(S(−,−),U ) exists, and there is an isomorphism
∮
M ∈M
HomA(S(−,−),U )≃ HomA(
∮ M ∈N
(S,β ),U ).
Moreover, if
∮
M ∈M HomA(S(−,−),U ) exists for any U∈A , then the coend∮ M ∈N (S,β ) exists. □
The proof of the next result is completely analogous to the pr oof in the
case of usual coend.
Lemma 3.5. LetM be a right C-module category, S :Mop×M→A
a functor equipped with a prebalancing γ. If F :A→A ′ is a right exact
functor, then there is an isomorphism
F (
∮ M ∈M
(S,γ ))≃
∮ M ∈M
(F◦S,F (γ)).
□
We shall also need the next result.
Lemma 3.6. LetM,N be rightC-module categories and let (J,c ) :M→N
be an equivalence of C-module categories. Assume that S :N op×N →A
is a functor equipped with a prebalancing β. The functor S(J(−),J (−)) :
Mop×M→A has a prebalancing γ given by
γV
M,N =S(id J(M ),c N,∗V )βV
J(M ),J (N )S(c−1
M,V, id J(N ))
for any M,N ∈M . There is an isomorphism
∮ M ∈M
(S(J(−),J (−)),γ )≃
∮ N ∈N
(S,β ).
Proof. We only sketch the proof. Let λN : S(N,N ) →
∮ N ∈N (S,β ) the
associated dinatural transformations. If we deﬁne πM = λJ(M ), for any
M∈M , one can verify that these are dinatural transformations an d they
satisfy ( 3.5). Universality of π follows from the universality of λ and the
fact that J is an equivalence of categories. □
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 15
