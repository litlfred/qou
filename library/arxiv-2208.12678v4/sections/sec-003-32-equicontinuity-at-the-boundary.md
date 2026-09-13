---
doc_id: arxiv-2208.12678v4
doc_title: "STATIONARY CURVES UNDER THEM ÖBIUS-PLATEAU ENERGY"
section_id: sec-003-32-equicontinuity-at-the-boundary
section_title: "Equicontinuity at the Boundary"
section_number: 3.2
pages: 4-5
source_pdf: 2208.12678v4.pdf
source_sha256: 406d36ff4968091d
---
Lemma 8. Suppose

µk : [a,b ]→ R3	
is a sequence of continuous curves that converges uniformly to µ∞.
Then the diameters of the images converge: diam(µk([a,b ]))→ diam(µ∞([a,b ])).
Proof. Let ε > 0 and choose N large such that ∥µk−µ∞∥C0 < ε
2 for k > N. Let x,y ∈ [a,b ] such that
|µ∞(x)−µ∞(y)| = diam(µ∞([a,b ])). From uniform convergence we have, for any s,t∈ [a,b ] and k>N ,
|µk(s)−µ∞(s)|, |µk(t)−µ∞(t)|< ε
2.
We have the following lower-bound for diam(µk([a,b ])),
diam(µ∞([a,b ])) =|µ∞(x)−µ∞(y)|
≤|µ∞(x)−µk(x)| +|µk(x)−µk(y)| +|µk(y)−µ∞(y)|
≤ diam(µk([a,b ])) +ε.
Let s,t∈ [a,b ], then we have
|µk(s)−µk(t)|≤| µk(s)−µ∞(s)| +|µ∞(s)−µ∞(t)| +|µ∞(t)−µk(t)|
≤ diam(µ∞([a,b ])) +ε.
Taking a max over s,t in the above inequality yields
diam(µk([a,b ]))≤ diam(µ∞([a,b ])) +ε.
□
We also state the Courant-Lebesgue lemma which is essential for proving equicontinuity of our maps at
the boundary. First, for p∈D and ρ> 0, we define the circles
Cρ(p) ={q∈D : |p−q| =ρ}.
STATIONARY CUR VES UNDER THE M ¨OBIUS-PLATEAU ENERGY 5
Lemma 9 (Courant-Lebesgue). Let u : D→ R3 with u∈ C 0(D)∩W 1,2(D) where e(u)≤ K/2 for some
K >0. Then, for all 0<δ ≪ 1, there exist ρ∈ [δ,
√
δ] such that for all p∈D,
[diam(u(Cρ(p)))]2≤ 8π2K
− logδ.
Proof. See [CM11] Lemma 4.11. □
For the rest of this section, fix three distinct points p1,p 2,p 3∈ ∂D. For each k, we can find a unique
conformal diffeomorphism φk :D→D such that
uk◦φk(pi) =γk(pi) for i = 1, 2, 3.(7)
Proposition 1. The maps ˜uk :=uk◦φk are equicontinuous on ∂D.
Proof. Since{˜uk} is a minimizing sequence (and e[·] is conformally invariant), we can assume that e(˜uk)≤
K/2 for some K >0. Let ε> 0 and without loss of generality assume that
ε< lim inf
k→∞

min
i̸=j
|γk(pi)−γk(pj)|

,
which exists since theγk are all simple closed curves, along withγ∞. Since γ∞ is simple, closed and has finite
arc-length, there is some d0 > 0 such that for p,q ∈ ∂D with 0 <|γ∞(p)−γ∞(q)| < d0, γ∞(∂D)\{p,q}
has exactly one component with diameter, diam ∞≤ ε
2 [CM11, Proof of Lemma 4.14]. Call the closure of
this component Γ. Let N > 0 such that ∥γk−γ∞∥C0 < ε
4 for k > N. Then, from Lemma 8, the sub-arc
of γk(∂D) parametrized by the same part of ∂D that parametrizes Γ has diameter (denoted diam k) ε
2-close
to the diameter of Γ, i.e. |diamk− diam∞|< ε
2. Thus, diamk <ε . It follows that |γk(p)−γk(q)|< ε
2 +d0.
Henceforth, write d := ε
2 +d0 and let k>N .
Takeδ <1 small enough such that 8π2K
− logδ < d2 and not more than one of the pi’s is in B(p,
√
δ). Given
anyp∈∂D, from Lemma 9, there exists ρ∈ [δ,
√
δ] such that
diam(˜uk(Cρ(p)))2 < 8π2K
− logδ <d 2.
In other words, diam(˜uk(Cρ(p)))<d . Cρ(p) divides ∂D into two components, A1 and A2. Without loss of
generality, letA1 be the component that contains fewer than two of p1,p 2,p 3.
Denote the images, G1 = u(A1) and G2 = u(A2). Due to monotonicity, G1 will also contain fewer than
two of γk(p1),γk(p2),γk(p3). Since diam(˜uk(Cρ(p))) < d, from Lemma 9, diam( Gi) < εfor at least one of
i = 1, 2. However, from the chosen value ofε, this component cannot contain more than one ofγk(p1),γk(p2),
or γk(p3). Thus, the component has to be G1.
In conclusion, we have shown that there is ρ> 0 such that|p−q|<ρ implies|γk(p)−γk(q)|<ε . □
