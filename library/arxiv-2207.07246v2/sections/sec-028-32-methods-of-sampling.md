---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-028-32-methods-of-sampling
section_title: "Methods of Sampling"
section_number: 3.2
pages: 64-66
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
In this section, we apply the Monte Carlo method described in section 3.1 to our
PIMC algorithm. The Plr(R) in Eq.(2.92) is exactly the π(s) in section 3.1. State
s in π(s) means a particular choice of {l,r,R}, and ∑
s in Eq.(3.1) is the same as
∑
l
∑
r
∫
dR in Eq.(2.87). We have
s ={l,r,R}, (3.8)
π(s) =Plr(R), (3.9)
∑
s
π(s) =
∑
l
∑
r
∫
DRPlr(R) = 1. (3.10)
The proposed transition probability T (s→s′) can be decomposed into two parts.
First we propose a transition for the left and right order of the trial wave function
{l,r} to transit to a new pair {l′,r′}, mark it Tlr→l′r′. Then, based on the new {l′,r′},
we choose a new conﬁgurationR′ based on the new proposed transition probability
Tl′r′(R→R ′). In such a way we have
T (s→s′) =Tlr→l′r′Tl′r′(R→R ′). (3.11)
We can just randomly pick {l′,r′} so that Tlr→l′r′ equal to its inverse transition
probabilityTl′r′→lr, so they are canceled in Eq.(3.7). Considering Eqs.(2.92,2.94,2.95),
we can write down,
π(s′)T (s′→s)
π(s)T (s→s′) = fV
l′r′(R′)gF (R′)Tlr(R′→R )
fV
lr (R)gF (R)Tl′r′(R→R ′), (3.12)
and we can judge if we accept the new state s′ by Eq.(3.7) which now becomes,
A(s→s′)=min
[
1,fV
l′r′(R′)gF (R′)Tlr(R′→R)
fV
lr (R)gF (R)Tl′r′(R→R′)
]
. (3.13)
54
In the program, we do an equivalent two-stage judgement. At stage one, we randomly
pick{l′,r′}, and judge if we accept the new order by
A(s→s′)=min
[
1,fV
l′r′(R)gF (R)
fV
lr (R)gF (R)
]
. (3.14)
No matter{l′,r′} is accepted or not (the acceptance rate for {l,r}→{ l′,r′}≈ 99%),
we mark the left and right order after the judgement as {l,r}. At the stage two, we
propose the new conﬁguration R′ and judge if it is accepted or not by
A(s→s′)=min
[
1,fV
lr (R′)gF (R′)Tlr(R′→R)
fV
lr (R)gF (R)Tlr(R→R′)
]
. (3.15)
Since fV
l′r′(R′) and fV
lr (R) are sandwiched between the trial wave functions, there
is no obvious ways to cancel them out in the numerator and denominator, so we leave
them alone. However, the proposed probability Tl′r′(R→R ′) is something we can
deal with. There can usually be two choices.
Choice 1 Make the proposed probability as,
Tl′r′(R→R ′) =Tlr(R′→R ), (3.16)
and by doing this, Eq.(3.12) can be simpliﬁed as,
π(s′)T (s′→s)
π(s)T (s→s′) = fV
l′r′(R′)gF (R′)
fV
lr (R)gF (R) , (3.17)
and then we can judge if we accept the new state s′ by,
A(s→s′) = min
[
1,fV
l′r′(R′)gF (R′)
fV
lr (R)gF (R)
]
. (3.18)
Choice 2 Make the proposed transition probability Tl′r′(R→R ′) and Tlr(R′→R )
in a way such that
gF (R′)Tlr(R′→R ) =gF (R)Tl′r′(R→R ′), (3.19)
55
and by doing this, Eq.(3.12) can be simpliﬁed as,
π(s′)T (s′→s)
π(s)T (s→s′) = fV
l′r′(R′)
fV
lr (R) , (3.20)
and then judge if we accept the new state s′ by the simpliﬁed version of Eq.(3.7),
A(s→s′) = min
[
1,fV
l′r′(R′)
fV
lr (R)
]
. (3.21)
In our work, diﬀerent methods of sampling means diﬀerent choices of proposed
transition probability Tl′r′(R→R ′) and Tlr(R′→R ). No matter what the choice is,
they all correspond to the same target distribution π(s). However, diﬀerent choices of
proposed transition probability will lead to diﬀerent convergence speed. So in order
to achieve the target distribution π(s) eﬃciently and quickly, we need to mainly use
eﬃcient proposed transition probabilities.
