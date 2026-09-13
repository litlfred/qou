---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-027-31-metropolis-algorithm
section_title: "Metropolis Algorithm"
section_number: 3.1
pages: 61-64
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
and Whitlock (1986)).
3.1 Metropolis Algorithm
In general, for a normalized probability distribution π(s) such that∑
sπ(s) = 1,
⟨F⟩ the expectation value of function F (s) is,
⟨F⟩ =
∑
s
F (s)π(s), (3.1)
where the letter s means a set of variables which can describe a state. In the Monte
Carlo method, if we can samplen states which eﬀectively explore the state space ofπ(s)
and are distributed according to π(s), denoting those states as {s0,s 1,s 2...,sn}∈ s,
then the expectation value⟨F⟩ can be calculated by,
⟨F⟩ =
∑n
i=0F (si)
n . (3.2)
So it is clear that we need to make a process which can continuously generate
a series of states {s0,s 1,s 2,s 3...} such that they distributed according to a target
distribution π(s). In order to do so, we need a transition probability P(s→s′) which
is the probability for state s to transit to s′. Once this process reaches its equilibrium
51
status, it must satisfy,
∑
s
π(s)P(s→s′) =π(s′). (3.3)
We can require the number of states that make transition from any s to s′ equals
that transit from s′ back to s,
π(s)P(s→s′) =π(s′)P(s′→s). (3.4)
Eq.(3.4) is the detailed balance condition (Ceperley (1995)). Note that ∑
s′P(s→
s′) =∑
sP(s′→s) = 1, so once we reach the detailed balance, Eq.(3.3) the equilibrium
status will automatically become valid and therefore the states we generated will indeed
be distributed according to π(s).
The transition probability can be written as,
P(s→s′) =T (s→s′)A(s→s′), (3.5)
where T (s→s′) is a proposed transition probability and A(s→s′) is the acceptance
probability which will be used to judge if the proposed transition is accepted or not.
With Eq.(3.5), the detailed balance equation Eq.(3.4) can be further written as,
A(s→s′)
A(s′→s) = π(s′)T (s′→s)
π(s)T (s→s′). (3.6)
A common choice of the acceptance probabilityA(s→s′) which can satisfy Eq.(3.6)
and thus the detailed balance condition is (Kalos and Whitlock (1986)),
A(s→s′) = min
[
1,π(s′)T (s′→s)
π(s)T (s→s′)
]
. (3.7)
As we can see, the normalization factors in π(s) and π(s′) and that in T (s→s′)
and T (s′→s) will be canceled out in Eqs.(3.6,3.7) so those factors are irrelevant in
calculating A. In order to make the value of A(s→ s′) larger, we can try to make
T (s′→s) similar withπ(s), andT (s′→s) similar withπ(s′), such that the numerator
52
and denominator in Eq.(3.7) can largely cancel. That will usually make the calculation
eﬃcient. In the ideal case, if we can make T (s′→s) =π(s) and T (s′→s′) =π(s′),
thenA(s→s′) = 1 so we just need to always accept the new proposed states, but this
is normally not possible, and if possible the Metropolis method would be unnecessary.
The basic procedure for the Monte Carlo method is described as follows.
Step 1 For the current state s, propose a new state s′ according to the proposed
transition probability T (s→s′).
Step 2 For the proposed new state s′, use Eq.(3.7) to calculate the acceptance rate
A(s→s′).
Step 3 Generate a uniform random number a which ranges from 0 to 1. If a≤A(s→
s′), the new state s′ is accepted, so set the accepted state s′ as the current state
s, namely s =s′, and keep s′ as a sample, then go to step 1 and continue. Else,
the new state s′ is rejected which means the state s is accepted and kept as the
sample, so set the accepted state s as our current state s, then go to step 1 and
continue.
After looping over the procedure for enough times, all those ‘current state’ s in
step 1 will eventually be distributed according to the desired distribution π(s).
Note that the choice of T and therefore A are not unique. In order to make the
algorithm more robust, we usually include diﬀerent types of moves with correspondingly
proposed transition probability T , and acceptance rate A, and this will still lead to
the target distribution π(s), as long as the detailed balance condition Eq.(3.6) holds
for each type of move. Any such choice that has transitions between any two allowed
states by a series of moves and has some rejections will converge to samples of π(s).
Also, the choice of T determines how eﬃcient the Monte Carlo procedure is. A poorly
53
chosenT can make the code run for a very long time but still not able to form π(s).
So T is crucial in the algorithm, we will discuss our choice of T in the next section.
