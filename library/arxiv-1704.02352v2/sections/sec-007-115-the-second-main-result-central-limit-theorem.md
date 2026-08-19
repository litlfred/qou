---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-007-115-the-second-main-result-central-limit-theorem
section_title: "The second main result: Central Limit Theorem"
section_number: 1.15
pages: 9-13
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Y oung diagrams which can be regarded as a natural one-parameter deformation of so me classi- cal Y"
---
notations from Theorem 1.3. The difference
(1.17) ∆ n := √
n (ωΛ n − ωΛ ∞) .
is a random function on the real line which quantiﬁes the (sui tably rescaled)
discrepancy between the shape of the random (anisotropic) Y oung diagram
Λ n and the limit shape. We will regard ∆ n as a Schwartz distribution on the
real line R or, more precisely, as a random vector from this space.
The following result is a generalization of Kerov’s CLT [Ker 93a, IO02]
which concerned Plancherel measure in the special case α = 1 as well as a
generalization of its extension by the ﬁrst-named author an d Féray [DF16]
for the generic ﬁxed value of α > 0. Indeed, Example 1.2 shows that the
assumptions of the following theorem are fulﬁlled for χn := χreg, thus CLT
holds for Jack–Plancherel measure in a wider generality, when α = α(n)
may vary with n.
On the other hand the following result is also a generalizati on of the re-
sults of the second-named author [ ´Sni06] who considered a setup similar to
the one below in the special case α = 1.
Theorem 1.5 (Central Limit Theorem) . We keep the assumptions and the
notations from Theorem 1.3.
Then for n → ∞ the random vector ∆ n converges in distribution to some
(non-centered) Gaussian random vector ∆ ∞ valued in the space (R[x])′ of
distributions, the dual space to polynomials.
10 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
The above statement about the convergence of the random vect or ∆ n
should be understood in a rather speciﬁc sense, formulated w ith help of
some suitable test functions. Namely, for each ﬁnite collec tion of polyno-
mials f1, . . . , fk ∈ C[x] we claim that the joint distribution of the random
variables
⟨∆ n, fi⟩ :=
∫
R
∆ n(x)fi(x) dx for i ∈ {1, . . . , k}
converges to the Gaussian distribution.
Informally speaking: asymptotically, for n → ∞
ωΛ n ≈ ωΛ ∞ + 1√n ∆ ∞
where ωΛ ∞ is a deterministic curve and ∆ ∞ is a Gaussian process.
Remark 1.6. In order to prove Theorem 1.5 it is enough to show that the
joint distribution of any ﬁnite family of random variables (Yk)k≥2 converges
as n → ∞ to a (non-centered) Gaussian distribution, where
(1.18) Yk := k − 1
2
∫
uk−2 ∆ n(u) du
is (up to a simple scalar factor) the value of the Schwartz dis tribution ∆ n
evaluated on a suitable polynomial test function.
The proof is postponed to Section 6.
1.16. Example. Let α > 0 be a ﬁxed positive integer. For a given integer
i > 0 consider the rectangular Y oung diagram
(iαi) := (i, . . . , i
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft/bracehtipupright
αi times
)
with n′ := αi2 boxes. We will assume that n′ is an even number. The
special case α = 1 was considered already by Biane [Bia98, Figures 1–3].
Using a random iterative procedure introduced by Kerov [Ker 96] which
is an inverse of the Plancherel growth process and which willbe presented in
detail in a forthcoming paper [D ´S18] we remove half of the boxes from the
rectangular Y oung diagram(iαi); the resulting random Y oung diagram with
n := 1
2n′ boxes will be denoted by λn. We will use the same transformation
T := T√ α
n ,
√ 1
αn
in order to scale both the original rectangular Y oung diagra m (iαi) as well
as the resulting random Y oung diagram λn.
We notice that the anisotropic Y oung diagram T (iαi) is a square, see
Figure 3; we shall denote it by S. As we shall see in [D ´S18], the distri-
bution of the random Y oung diagram λn can be equivalently formulated
JACK-DEFORMED RANDOM YOUNG DIAGRAMS 11
x
√ 2
y
√ 2
u
−
√
2
√
2
v
√
2
2
√
2
FIGURE 3. The green square S depicts the anisotropic
Y oung diagram T (iαi) in the Russian coordinate system.
The blue hatched triangle depicts the limit shape Λ ∞; the
blue dashed line depicts the corresponding proﬁle ωΛ ∞.
via (1.7) in terms of the corresponding natural reducible Ja ck character and
Theorem 1.3 as well as Theorem 1.5 are applicable. Thus the se quence of
random anisotropic Y oung diagrams Λ n = T λn converges to some deter-
ministic limit Λ ∞. Not very surprisingly, this limit Λ ∞ turns out to be the
bottom half of the square S, see Figure 3.
Figures 4 and 5 are an illustration of the Law of Large Numbers (Theo-
rem 1.3): as the number of boxes n → ∞ tends to inﬁnity, suitably scaled
random Y oung diagrams Λ n indeed seem to converge to the deterministic
limit Λ ∞.
In order to speak about CLT one should consider a more reﬁned s caling:
the one in which one stretches the second Russian coordinate v by a factor
of √n. This scaling has a bizarre feature: each individual box is d rawn
as a parallelogram in which the difference vmax − vmin = √α + 1√α of
the v-coordinates of the top and the bottom vertex does not depend on n
so one cannot claim that the size of an individual box converges to zero;
nevertheless the area of an individual box does converge to zero. Figures 6–
8 illustrate this choice of the scaling.
12 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
FIGURE 4. Diagonal gray lines form a heatmap showing
probabilities that a given segment belongs to the proﬁle of
the random Y oung diagram Λ n (the intensity of color corre-
sponds to the probability). The rectangular grid of anisotr op-
ically stretched boxes is clearly visible. The blue dashed l ine
depicts the limit proﬁle ωΛ ∞. In order to save space, only the
neighborhood of Λ ∞ is shown. The red solid line depicts the
mean value t ↦→EωΛ n(t). In this example α = 4 , i = 5 ,
n = 50.
FIGURE 5. The analogue of Figure 4 for α = 4, i = 10, n =
200. The increased number of boxes is compensated by a
decrease of the size of the individual boxes. With this choic e
of scaling, the ﬂuctuations of random Y oung diagrams Λ n
around Λ ∞ tend to zero as n → ∞.
Theorem 1.5 implies in particular that the limit
(1.19) E∆ ∞ = lim
n→∞
E∆ n
exists as a Schwartz distribution on the real line; the conve rgence holds in
the weak sense, i.e. the limit∫
uk E∆ ∞(u) du := lim
n→∞
∫
uk E∆ n(u) du
exists and is ﬁnite for an arbitrary integer k ≥ 0.
The convergence in (1.19) is illustrated in Figures 6–8: the function E∆ n
is the difference between the red solid curve (i.e. the plot o f √n EωΛ n) and
the blue dashed curve (i.e. the plot of √n ω Λ ∞). As one can see on these
examples, the function E∆ n has oscillations of period and amplitude related
to the grid of the boxes of the Y oung diagrams. Asn → ∞, the amplitude of
these oscillations does not converge to zero (so that the con vergence in the
JACK-DEFORMED RANDOM YOUNG DIAGRAMS 13
FIGURE 6. The analogue of Figure 4 for the proﬁles√n ω Λ n for which only the second Russian coordinate v
was anisotropically stretched by factor √n. In this exam-
ple α = 4, i = 5, n = 50.
supremum norm does not hold) but their frequency tends to inﬁ nity (which
is sufﬁcient for convergence in the weak topology).
The central limit theorem in Theorem 1.5 is somewhat reminis cent to
CLT for random walks. A signiﬁcant difference lies in the nat ure of the limit
object: in the case of the random walks it is the Brownian moti on which has
continuous trajectories while in the case considered in The orem 1.5 it is a
random Schwartz distribution ∆ ∞ for which computer simulations (such
as the one shown in Figure 9) suggest that it has quite singula r ‘trajecto-
ries’, reminiscent to that of the white noise. A systematic i nvestigation of
such trajectory-wise properties of ∆ ∞ via short-distance asymptotics of the
covariance of the corresponding Gaussian ﬁeld is out of the s cope of the
current paper.
