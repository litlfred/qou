---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-018-53-even-characteristics
section_title: "Even Characteristics"
section_number: 5.3
pages: 32-34
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.87
latex_coverage_ratio: 0.996
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
In the previous subsection, we were able to fully characterise the odd theta characteristics on Bring's curve without too much difficulty through the use of existing work giving the stalls of the canonical embedding. The story for even characteristics is different, as the line bundle corresponding to a generic even theta characteristic has no sections, which is an obstacle to their study [@Takagi2009]. In [@Dolgachev1993] the authors were able to use the Scorza correspondence to calculate the orbit decomposition of even spin structures on Klein's curve, but at the time of writing the theory of the Scorza map has not been developed far enough to cover Bring's curve. The Scorza quartic necessary to extend Dolgachev and Kanev's work beyond $g=3$, wherein it becomes a codimension-1 hypersurface in $\mathbb{P}^{g-1}$, has been proven to exist for a generic even spin curve (that is a pair consisting of a curve and an even theta characteristic on it); it has only been explicitly found for trigonal curves in $g=4$ [@Takagi2009]. In [@Burns1983], motivated by its realisation via an elliptic modular surface, Burns identified a theta characteristic on Bring's curve invariant under the $A_5$ subgroup of the automorphism group, though he described this characteristic only in terms of two line bundles on the curve, not directly in terms of points on the curve. We shall now fully classify the orbits of the even characteristics and give an explicit description of Burns' divisor in the process.

We have two distinct methods of probing the orbit decomposition of the theta characteristics on Bring's curve.

1.  Use the method of [@Kallel2006], wherein theta characteristics are identified with vectors in $\mathbb{F}_2^{2g}$, and the action of automorphisms given by the homology representation of the automorphism group of the curve as found using the methods of [@Bruin2019].

2.  Identify theta characteristic with the $2^{2g}$ translates by half-lattice vectors of a half-canonical vector in the Jacobian of the curve, done using the implementation of the Abel-Jacobi map developed by Disney-Hogg [@DisneyHogg2021], and the action of automorphisms given by the cohomology representation of the automorphism group of the curve as found using the methods of [@Bruin2019].

The two methods have different strengths, namely that the first uses exact computations rather than approximations with multi-precision arithmetic, but the second can concretely relate theta characteristics from their representation to an actual divisor (class). Both methods not only verify Corollary [\[cor: Orbit decomposition of odd theta characteristics\]](#cor: Orbit decomposition of odd theta characteristics){reference-type="ref" reference="cor: Orbit decomposition of odd theta characteristics"} but also gives the following result.

::: theorem
The orbit decomposition of even theta characteristics on Bring's curve is $$\label{eq:evencharacteristics}
136 = 1 + 5+5+5+10+10+10+30+30+30  .$$
:::

::: corollary
Bring's curve has a unique theta characteristic invariant under the action of the automorphism group, which is also the theta characteristic invariant under the $A_5$ subgroup found in [@Burns1983].
:::

The existence of the unique invariant theta characteristic was known in [@Braden2012], but it had not been identified. This we rectify with the following result.

::: theorem
[]{#invarianttheta label="invarianttheta"} The theta characteristic $\Delta$ (defined in Example [\[example: theta characteristic on Bring\'s curve\]](#example: theta characteristic on Bring's curve){reference-type="ref" reference="example: theta characteristic on Bring's curve"}) is the unique invariant theta characteristic in on Bring's curve.
:::

::: proof
*Proof.* We first consider the action of $S$ on $a$, $b$, $c$, $d$. We have $$\begin{aligned}
a:=[0:0:1]&\simeq[2t^3:t:1]\xrightarrow{S}[2t^3:\zeta t:\zeta^{-1}]=[2 \zeta t^3:\zeta^2 t:1]
=[2(\zeta^2 t)^3:\zeta^2 t:1]\\& =[2\epsilon^3:\epsilon:1],\\
 b:=[0:1:0]&\simeq[2t^2:1/t:1]\xrightarrow{S}[2t^2:\zeta/ t:\zeta^{-1}]=
 [2 \zeta t^2:\zeta^2/ t:1]=[2(t/{\zeta^2})^2:\zeta^2/ t:1]\\ 
 c:=[1:0:0]_2&\simeq[1:t:t^4]\xrightarrow{S}[1:\zeta t:\zeta^{-1} t^4]=[1:\zeta t:(\zeta t)^4],\\
 d:=[1:0:0]_1&\simeq[1:t^4:t]\xrightarrow{S}[1:\zeta t^4:\zeta^{-1} t]=[1:(\zeta^{-1} t)^4: \zeta^{-1} t].
\end{aligned}$$ Thus $a$, $b$, $c$ and $d$ are invariant under the symmetry $S$ and consequently $\Delta= 3a+b-c$ is also invariant.

Similarly, as mentioned in Proposition [\[prop: U is an automorphism\]](#prop: U is an automorphism){reference-type="ref" reference="prop: U is an automorphism"}, the action of $U$ on $a,b,c,d$ can be calculated as $$a \mapsto c \mapsto b \mapsto d \mapsto a  ,$$ and so $$\Delta  = 3a+b-c \mapsto 3c+d-b = 3a+b-c - (3a+2b-4c-d) = \Delta - (x) \sim \Delta  .$$ We have thus shown that $\Delta$ is invariant under $\left\langle S, U \right\rangle$. To complete the proof that $\Delta$ is the invariant theta characteristic, one could attempt to show that $\Delta$ is invariant under the action of $R$ by direct computation, but this proves to be difficult. It is instead better to check in Sage that the unique spin structure invariant under the whole automorphism group is actually also the unique spin structure invariant under the subgroup generated by $S$ and $U$. In fact, by Theorem 1.2 of [@Kallel2006] and our work in §[\[sec: quotients by subgroups\]](#sec: quotients by subgroups){reference-type="ref" reference="sec: quotients by subgroups"}, we know there is a unique theta characteristic invariant under $\left\langle S \right\rangle$[^1], and this completes the proof. ◻
:::

This proof strategy is similar to the identification of the unique invariant theta characteristic on Klein's curve in [@Kallel2006].[^2]

We now want to make the connection to [@Burns1983]. Recall Lemma [\[quaddif\]](#quaddif){reference-type="ref" reference="quaddif"} and Proposition [\[prop: quadric of canonical embedding isomorphic to PxP\]](#prop: quadric of canonical embedding isomorphic to PxP){reference-type="ref" reference="prop: quadric of canonical embedding isomorphic to PxP"}. This gives us two degree-3 maps $f_i : \mathcal{B} \to \mathbb{P}^1$, namely $f_i = \left. \pi_i \circ \varphi^{-1}\right\rvert_{\mathcal{B}}$, $i=1,2$, where $\varphi$ was the isomorphism $\mathbb{P}^1 \times \mathbb{P}^1 \to \mathcal{Q}$, and $\pi_i$ the projection to the two factors of $\mathbb{P}^1 \times \mathbb{P}^1$. What are the corresponding divisors? Working in the $L_a$ coordinates, we can use Sage to find that $f_1^{-1}([1:0]) = 2[0:0:0:1]+[1:0:0:0] = 2b+c := L^\prime$, while $f_2^{-1}([1:0]) = 2[0:1:0:0]+[0:0:0:1]= 2d+b := L$.

::: prop
[]{#burnsLs label="burnsLs"} The divisors $L$, $L^\prime$ satisfy the properties described in [@Burns1983], namely $$\begin{aligned}
    \Delta &\sim 3(L^\prime -L) + L, \quad 
    \mathcal{K}_\mathcal{B} \sim L+L^\prime, \quad  
    0 \sim 5(L^\prime - L)  . 
\end{aligned}$$
:::

::: proof
*Proof.* This is straightforward verification from the definitions. ◻
:::

Note we can connect this back to the degree-3 map given by Klein. We know from [@Weber2005] that we expect this map to be branched at face-centres of the $\left\{ 5, 5  |  3 \right\}$ tessellation, and these come from face-centres of the $\left\{ 5,4 \right\} _6$ tessellation, and indeed recall we saw that $a,b,c,d$ were face-centres.

An additional characterisation of the invariant theta characteristic is given by the following result.

::: prop
[]{#szegoinvt label="szegoinvt"} In the homology basis of [@Riera1992], the RCV satisfies $$K_a = \frac{1}{10}(
3 , 2 , -2 , -3
) + \Im(\tau_0)(
1 , -2 , -2 , 1
)i  = \mathcal{A}_a(\Delta) .$$ As such, in the R&R homology basis, the unique invariant theta characteristic is the divisor (class) of the Szëgo kernel, i.e. $\Delta = \Delta_S$.
:::

::: proof
*Proof.* The first equality is shown analytically in [@Braden2012]. The second is shown numerically in the corresponding notebooks, using the Abel-Jacobi map developed by Disney-Hogg [@DisneyHogg2021]. To verify the RCV, we implemented the methodology of [@Deconinck2015] using the theta function in Sage developed by Bruin and Ganjian [@Bruin2021]. While these calculations are numerical in nature, the calculations can be done with arbitrary binary precision. We were satisfied by calculating with 400 binary digits of precision, giving an absolute error of less than $10^{-118}$ for the first equality, and of less than $10^{-23}$ for the second equality. ◻
:::

[^1]: Under the action of $S$, the orbit decompositions are $120=24\times 5$ and $136 = 1+27\times 5$.

[^2]: The final part of the proof in that paper, showing invariance under the order-2 generator of $PSL_2(\mathbb{F}_7)$, is in our opinion incomplete; Kallel (private correspondence) believes our reasoning correct. The theorem remains correct nevertheless, as one can check using their methodology that invariance under the order-7 generator is enough to specify the unique invariant spin structure, as the decompositions are $28=4\times 7$ and $36 =1 + 5 \times 7$. It is a curious coincidence that in both cases it was a generator of order 2 for which the direct calculation was difficult.
