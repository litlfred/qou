---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-016-41-cross-product
section_title: "Cross Product"
section_number: 4.1
pages: 12-15
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
binary logical operators, i.e., &,|,∧,=>,<=>. Then we move on to quantiﬁcation in Section 4.2, explaining the construction
of automata for predicates formed from E and A operators. In Section 4.3, we discuss construction of automata for the
complement ∼and reverse ` operators. With these tools at our disposal, we are on the right track to construct automata for
complex predicates formed from comparison and arithmetic operators, e.g., ∗,/,>,<=,etc. which we explain in Section 4.4.
4.1
Cross Product
Let M
¡
Q,q0,F,δ,S1,...,Sm
¢
and M′¡
Q′,q′
0,F ′,δ′,S′
1,...,S′
n
¢
be the automaton (x1,...,xm) : P and (x′
1,...,x′
n) : P′ respectively.
Let us assume that if xi = x′
j then Si = S′
j. Let {x′′
1,...,x′′
p} where p ≤m +n be the union of {x1,...,xm} and {x′
1,...,x′
n} and
further assume that the x′′
i are appearing in lexicographic order. Depending on whether x′′
k = xi or x′′
k = x′
j , let S′′
k denote Si or
S′
j respectively. Then the cross product of M and M′ denoted by M × M′ is the tuple
¡
Q ×Q′,(q0,q′
0),δ′′,S′′
1,...,S′′
p
¢
where the transition function is deﬁned to be
δ′′¡
(q,q′),(γ1,...,γp)
¢
=
¡
δ(q,(α1,...,αm)),δ′(q′,(β1,...,βn))
¢
for γk equals αi or βj depending on whether x′′
k = xi or x′′
k = x′
j respectively. Note that M × M′ is not an automaton since a
set of ﬁnal states is not speciﬁed. For F ′′ ⊆Q ×Q′, let (M × M′)(F) denote the automaton
¡
Q ×Q′,(q0,q′
0),F ′′,δ′′,S′′
1,...,S′′
p
¢
.
Theorem 6. For F ′′ =
©
(q,q′) : q ∈F and q′ ∈F ′ª
, the automaton (M × M′)(F ′′) accepts predicate P & P′. Furthermore,
minimizing (M × M′)(F ′′), we obtain automaton (x′′
1,...,x′′
p) : P &P′.
Proof. Based on the deﬁnition for cross product, for M × M′ to be deﬁned, the same variables in P and P′ have to have the
same number systems assigned in P and P′. But that is exactly the same condition that needs to hold for number system
annotations in P &P′ to be consistent (in the sense deﬁned in the last bullet in Page 8).
Let t = (w1,...,wm) and t′ = (w′
1,...,w′
n) such that wi ∈Σ∗
Si and w′
j ∈Σ∗
S′
j where |wi| and |w′
j | are all equal and wi = w′
j
whenever xi = x′
j . Let t′′ = (w′′
1,...,w′′
p) such that w′′
k = wi or w′′
k = w′
j depending on whether x′′
k = xi or x′′
k = x′
j .
We have the following equivalent statements:
1. (M × M′)(F ′′) accepts t′′.
12
2. There is a path from (q0,q′
0) to (q,q′) ∈F ′′ in M × M′ reading t′′.
3. There is a path from q0 to q in M reading t, and there is a path from q′
0 to q′ in M′ reading t′.
4. M accepts t and M′ accepts t′.
5. P is satisﬁed by substituting xi = [wi]Si for all i, and P′ is satisﬁed by substituting x′
j = [w′
j ]S′
j for all j.
6. P &P′ is satisﬁed by substituting x′′
k = [w′′
k]S′′
k.
Obviously both the construction of cross product and minimizing automata can be carried out using algorithmic
procedures. Therefore Theorem 6 gives us a procedure for constructing the automaton for conjunction.
With proper deﬁnitions for F ′′, we have similar theorems for P ⊗P′ when ⊗is any other binary logical operator.
Let us construct the automaton (a,b) : a = 1&b = 2 from (a) : a = 1 in Figure 4.1 and (b) : b = 2 in Figure 4.2.
Figure 4.1: Automaton (a) : a = 1
Figure 4.2: Automaton (b) : b = 2
Recall that transitions not depicted are transitions to a dead state. The cross product operation is depicted below:
Figure 4.3: Cross product (a) : a = 1×(b) : b = 2
Making (1,2) a ﬁnal state, minimizing, and renaming the states, we get the automaton in Figure 4.4.
Figure 4.4: Automaton (a,b) : a = 1&b = 2
13
4.2
Quantiﬁcation
In this section we learn how to construct an automaton (x1,...,xi−1,xi+1,...,xm) : Exi P from automaton (x1,...,xm) : P.
Let M
¡
Q,q0,F,δ,S1,...,Sm
¢
be the automaton (x1,...,xm) : P and let P′ be the predicate Exi P. We ﬁrst construct the
nondeterministic automaton E(M,i)
¡
Q,q0,F,δ′,S1,...,Si−1,Si+1,...,Sm
¢
from M by eliminating the i’th input (coordinate) on all transitions, i.e., letting
δ′¡
q,(α1,...,αi−1,αi+1,...,αm)
¢
=
©
δ(q,(α1,...,αi−1,αi,αi+1,...,αm)) : for all αi ∈ΣSi
ª
.
For example, letting M be the automaton (a,b) : a = 1&b = 2 depicted in Figure 4.4, the automaton E(M,2) is depicted as
follows:
Figure 4.5: Non-deterministic automaton E(M,2)
By the deﬁnition of transition function of E(M,i), i.e., δ′, it is easy to see that if M accepts (w1,...,wi−1,wi,wi+1,...,wm),
then E(M,i) accepts
(w1,...,wi−1,wi+1,...,wm).
However, there might be t = (w1,...,wi−1,wi+1,...,wm) where the |w j | are equal for all j̸ = i and substitutions x j = [w j ]Sj
for all j̸ = i, satisﬁes P′ but E(M,i) does not accept t. In other words, there are cases where E(M,i) does not accept P′.
In our example M accepts (0n1,0n−110) for all n ≥1, and as it is clear E(M,2) accepts (0n1) for all n ≥1. However E(M,2)
does not accept (1), whereas (1) should be accepted by any automaton accepting Eb (a = 1&b = 2).
Therefore, we have to do more work on E(M,i), to get to an automaton for P′. However as we will see in Lemma 1,
the automaton E(M,i) might only miss an insigniﬁcant portion of accepted tuples of an automaton accepting P′. These
insigniﬁcant tuples missed by E(M,i) are those with leading or trailing zeros. The good news is that with a little bit of
technical work, it is possible to revive even these insigniﬁcant tuples.
Lemma 1. Let M,P,P′, and i be as in the discussion above, and suppose t = (w1,...,wi−1,wi+1,...,wm) is some tuple
of same length words. If P′ is satisﬁed with substitutions x j = [w j ]Sj for j̸ = i, then there exists a constant k ≥0 and
tk = (wk,1,...,wk,i−1,wk,i+1,...,wk,m) such that for all j̸ = i we have wk,j = 0kw j or wk,j = w j 0k depending on whether Sj is
msd or lsd, and tk is accepted by E(M,i). It is also the case that whenever tk for any k ≥0, with the appropriate substitutions,
is satisfying P′, then t is also satisfying P′.
Proof. Substitutions x j = [w j ]Sj for j̸ = i satisfying predicate P′ := Exi P means that there exists a natural number v, such that
the substitutions above together with xi = v is satisfying the predicate P. By deﬁnition of number systems, there exists a word
wi such that v = [wi]Si. Also by deﬁnition of number systems for any integer y and word w, if we have y = [w]S, then either
y = [0kw]S for all k ≥0 or y = [w0k]S for all k ≥0 depending on whether S is msd or lsd. Therefore there exists an integer
k such that wk,i is either 0kwi or wi0k depending on whether Sj is msd or lsd and v = [wk,i]Si and |wk,i| = |w j |+k for all
j̸ = i. Therefore (wk,1,...,wk,i−1,wk,i,wk,i+1,...,wk,m) is accepted by M where for all j we have wk,j = 0kw j or wk,j = w j 0k
depending on whether Sj is msd or lsd. Now by deﬁnition of E(M,i), we know that tk = (wk,1,...,wk,i−1,wk,i+1,...,wk,m) is
accepted by E(M,i). This completes the ﬁrst part of the lemma.
The second part follows very easily from the same properties of number systems mentioned in the proof of the ﬁrst part
of the lemma.
Based on Lemma 1, to get (x1,...,xi−1,xi+1,...,xm) : Exi P we just have to construct an automaton from E(M,i) such that
whenever tk for any k ≥0 is accepted, t is also accepted. For the case where all Sj for j̸ = i are either all msd or all lsd, we can
come up with an easy algorithm to revive tuples t from tk. In case of all msd, let I be the set of all states in E(M,i) reachable
14
from the initial state by reading (0,...,0)∗, or in case of all lsd, let F ′ be the set of all states reaching to a ﬁnal state by reading
(0,...,0)∗. We can compute I or F ′ using breadth-ﬁrst search. In the case of msd the nondeterministic automaton8
(Q,I,F,δ′,S1,...,Si−1,Si+1,...,Sn)
and in the case of lsd the nondeterministic automaton
(Q,q0,F ′,δ′,S1,...,Si−1,Si+1,...,Sn)
is equivalent to (x1,...,xi−1,xi+1,...,xm) : Exi P. Determinizing and minimizing this automaton gives us (x1,...,xi−1,xi+1,...,xm) :
Exi P.
In Figure 4.5, the variable a is over msd_2. So the set I is {0,1}, therefore the following nondeterministic automaton
accepts Eb a = 1&b = 2:
Figure 4.6: Non-deterministic automaton accepting Eb a = 1&b = 2
Now determinizing and minimizing this automaton gives us (a) : Eb a = 1&b = 2:
Figure 4.7: (a) : Eb a = 1&b = 2
Currently if for (x1,...,xn) : P it is not the case that for all j̸ = i number systems Sj are all msd or all lsd, then Walnut only
constructs E(M,i) for Exi P, which is not theoretically accurate. So the user has to be very cautious when quantifying
predicates over mixed msd and lsd number systems, or in cases where the quantiﬁed automaton is non-arithmetic. For
a deﬁnition of the latter see Section 5.2.
To obtain an automaton for AxiP, note its equivalence to ∼(Exi ∼(P)), where ∼is the logical complement (negation).
See the next section to learn about the complement operator.
4.3
