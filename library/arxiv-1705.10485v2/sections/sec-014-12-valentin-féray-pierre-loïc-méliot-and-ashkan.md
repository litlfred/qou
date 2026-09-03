---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-014-12-valentin-féray-pierre-loïc-méliot-and-ashkan
section_title: "Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali"
section_number: 12
pages: 12-12
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
1
2π
∫
R
ˆf(ξ)ˆµ(−ξ)dξ = i
2π
⟨
pv
(1
ξ
)⏐⏐⏐⏐ˆφˆµ−ˆφ
⟩
+f(0)
= lim
ε→0
(
i
2π
∫
|ξ|≥ε
ˆφ(ξ)
(ˆµ(−ξ)− 1
ξ
)
dξ
)
+f(0)
= 1
2π
∫
R
ˆφ(ξ)
(ˆµ(−ξ)− 1
−iξ
)
dξ +f(0).
Indeed, the function ξ ↦→ ˆµ(−ξ)−1
−iξ is continuous on R and bounded, with value ˆµ′(0)
i =
∫
Rxµ (dx) at
ξ = 0; it can therefore be integrated against the functionˆφ which is integrable (and even with compact
support). On the other hand,
∫
R
f(x)µ(dx) =
∫
x∈R
∫ x
y=0
φ(y)dyµ(dx) +f(0)
=
∫
(x,y)∈R2
(1x>y>0− 1x<y<0)φ(y)dyµ(dx) +f(0)
=
∫
y∈R
φ(y)F (y)dy +f(0), with F (y) =µ((y,∞))− 1y≤0.
One has
∫
R|F (y)|dy =
∫∞
y=0µ((y,∞)) +
∫ 0
y=−∞µ((−∞,y )) =
∫
R|x|µ(dx), which is ﬁnite. In the integral
above, we can therefore considerF (y)dy as a ﬁnite signed measure, and the Parseval formula applies by
Lemma 10. One computes readily
ˆF (ξ) = ˆµ(ξ)− 1
iξ ,
which ends the proof. ⊓ ⊔
Remark 15.The Parseval formula of Proposition 14 extends readily to ﬁnite signed measuresµ such that∫
R|x||µ|(dx)< +∞. Actually, it is suﬃcient to have a ﬁnite signed measureµ such that
ˆµ(ξ)−ˆµ(0)
ξv
is bounded in a vicinity of0, for somev >0. Then, (ˆµ(ξ)−ˆµ(0))/ξ is integrable in a neighborhood of0.
This ensures that the distributionf(x) (respectively, the distributionˆf(ξ)) can be evaluated against the
measure µ(x) (respectively, againstˆµ(ξ)), and then, the proof of Parseval’s formula is analogous to the
previous arguments.
