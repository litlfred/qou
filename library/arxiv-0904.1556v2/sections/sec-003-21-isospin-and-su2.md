---
doc_id: arxiv-0904.1556v2
doc_title: "The Algebra of Grand Uniﬁed Theories"
section_id: sec-003-21-isospin-and-su2
section_title: "Isospin and SU(2)"
section_number: 2.1
pages: 6-13
source_pdf: 0904.1556v2.pdf
source_sha256: a1a43786d817f085
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.998
doc_brief: "The Algebra of Grand Uniﬁed Theories — The Standard Model is the best tested and most widely accepted theory of elementary particles we have today."
---
[]{#sec:isospin label="sec:isospin"}

Because like charges repel, it is remarkable that the atomic nucleus stays together. After all, the protons are all positively charged and are repelled from each other electrically. To hold these particles so closely together, physicists hypothesized a new force, the **strong force**, strong enough to overcome the electric repulsion of the protons. It must be strongest only at short distances (about $10^{-15}$ m), and then it must fall off rapidly, for protons are repelled electrically unless their separation is that small. Neutrons must also experience it, because they are bound to the nucleus as well.

Physicists spent several decades trying to understand the strong force; it was one of the principal problems in physics in the mid-twentieth century. About 1932, Werner Heisenberg, pioneer in quantum mechanics, discovered one of the first clues to its nature. He proposed, in [@heisenberg:77], that the proton and neutron might really be two states of the same particle, now called the **nucleon**. In modern terms, he attempted to unify the proton and neutron.

To understand how, we need to know a little quantum mechanics. In quantum mechanics, the state of any physical system is given by a unit vector in a complex Hilbert space, and it is possible to take complex linear combinations of the system in different states. For example, the state for a quantum system, like a particle on a line, is a complex-valued function $$\psi \in L^2({\mathbb R}) ,$$ or if the particle is confined to a 1-dimensional box, so that its position lies in the unit interval $[0,1]$, then its state lives in the Hilbert space $L^2([0,1])$.

We have special rules for combining quantum systems. If, say, we have two particles in a box, particle 1 and particle 2, then the state is a function of both particle 1's position and particle 2's: $$\psi \in L^2([0,1] \times [0,1]),$$ but this is isomorphic to the tensor product of particle 1's Hilbert space with particle 2's: $$L^2( [0,1] \times [0,1] ) \cong L^2([0,1] \otimes L^2([0,1]).$$ This is how we combine systems in general. If a system consists of one part with Hilbert space $V$ *and* another part with Hilbert space $W$, their tensor product $V \otimes W$ is the Hilbert space of the combined system. Heuristically, $$\textit{and} = \otimes.$$ We just discussed the Hilbert space for two particles in a single box. We now consider the Hilbert space for a single particle in two boxes, by which we mean a particle that is in one box, say $[0,1]$, *or* in another box, say $[2,3]$. The Hilbert space here is $$L^2( [0,1] \cup [2,3]) \cong L^2([0,1]) \oplus L^2([2,3]).$$ In general, if a system's state can lie in a Hilbert space $V$ *or* in a Hilbert space $W$, the total Hilbert space is then $$V \oplus W.$$ Heuristically, $$\textit{or} = \oplus.$$

Back to nucleons. According to Heisenberg's theory, a nucleon is a proton *or* a neutron. If we use the simplest nontrivial Hilbert space for both the proton and neutron, namely ${\mathbb C}$, then the Hilbert space for the nucleon should be $${\mathbb C}^2 \cong{\mathbb C}\oplus {\mathbb C}.$$ The proton and neutron then correspond to basis vectors of this Hilbert space: $$p = \left( \begin{array}{c} 1 \\ 0 \end{array} \right) \in {\mathbb C}^2$$ and $$n = \left( \begin{array}{c} 0 \\ 1 \end{array} \right) \in {\mathbb C}^2.$$ But, we can also have a nucleon in a linear combination of these states. More precisely, the state of the nucleon can be represented by any unit vector in ${\mathbb C}^2$.

The inner product in ${\mathbb C}^2$ then allows us to compute probabilities, using the following rule coming from quantum mechanics: the probability that a system in state $\psi \in H$, a given Hilbert space, will be observed in state $\phi \in
H$ is $$\left| \langle \psi , \phi \rangle \right|^2.$$ Since $p$ and $n$ are orthogonal, there is no chance of seeing a proton as a neutron or vice versa, but for a nucleon in the state $$\alpha p + \beta n \in {\mathbb C}^2,$$ there is probability $| \alpha |^2$ that measurement will result in finding a proton, and $|\beta|^2$ that measurement will result in finding a neutron. The condition that our state be a unit vector ensures that these probabilities add to 1.

In order for this to be interesting, however, there must be processes that can turn protons and neutrons into different states of the nucleon. Otherwise, there would be no point in having the full ${\mathbb C}^2$ space of states. Conversely, if there are processes which can change protons into neutrons and back, it turns out we need all of ${\mathbb C}^2$ to describe them.

Heisenberg believed in such processes, because of an analogy between nuclear physics and atomic physics. The analogy turned out to be poor, based on the faulty notion that the neutron was composed of a proton and an electron, but the idea of the nucleon with states in ${\mathbb C}^2$ proved to be a breakthrough.

The reason is that in 1936 a paper by Cassen and Condon [@CassenCondon:nuclearforces] appeared suggesting that the nucleon's Hilbert space ${\mathbb C}^2$ is acted on by the symmetry group ${\rm SU}(2)$. They emphasized the analogy between this and the spin of the electron, which is also described by vectors in ${\mathbb C}^2$, acted on by the double cover of the 3d rotation group, which is also ${\rm SU}(2)$. In keeping with this analogy, the property that distinguishes the proton and neutron states of a nucleon was dubbed **isospin**. The proton was declared the **isospin up** state or $I_3 = \frac{1}{2}$ state, and the neutron was declared the **isospin down** or $I_3 =
-\frac{1}{2}$ state. Cassen and Condon's paper put isospin on its way to becoming a useful tool in nuclear physics.

Isospin proved useful because it formalized the following idea, which emerged from empirical data around the time of Cassen and Condon's paper. Namely: the strong force, unlike the electromagnetic force, is the same whether the particles involved are protons or neutrons. Protons and neutrons are interchangeable, as long as we neglect the small difference in their mass, and most importantly, as long as we neglect electromagnetic effects. One can phrase this idea in terms of group representation theory as follows: the strong force is *invariant* under the action of ${\rm SU}(2)$.

Though this idea was later seen to be an oversimplification, it foreshadowed modern ideas about unification. The proton, living in the representation ${\mathbb C}$ of the trivial group, and the neutron, living in a different representation ${\mathbb C}$ of the trivial group, were unified into the nucleon, with representation ${\mathbb C}^2$ of ${\rm SU}(2)$. These symmetries hold for the strong force, but not for electromagnetism: we say this force 'breaks' ${\rm SU}(2)$ symmetry.

But what does it mean, exactly, to say that a force is invariant under the action of some group? It means that when we are studying particles interacting via this force, the Hilbert space of each particle should be equipped with a unitary representation of this group. Moreover, any physical process caused by this force should be described by an 'intertwining operator': that is, a linear operator that respects the action of this group. A bit more precisely, suppose $V$ and $W$ are finite-dimensional Hilbert spaces on which some group $G$ acts as unitary operators. Then a linear operator $F \colon V \to W$ is an **intertwining operator** if $$F(g \psi) = gF(\psi)$$ for every $\psi \in V$ and $g \in G$.

Quite generally, symmetries give rise to conserved quantities. In quantum mechanics this works as follows. Suppose that $G$ is a Lie group with a unitary representation on the finite-dimensional Hilbert spaces $V$ and $W$. Then $V$ and $W$ automatically become representations of ${\mathfrak{g}}$, the Lie algebra of $G$, and any intertwining operator $F \colon V \to W$ respects the action of ${\mathfrak{g}}$. In other words, $$F(T \psi) = T F(\psi)$$ for every $\psi \in V$ and $T \in {\mathfrak{g}}$. Next suppose that $\psi \in V$ is an eigenvector of $T$: $$T\psi = i \lambda \psi$$ for some real number $\lambda$. Then it is easy to check $F(\psi)$ is again an eigenvector of $T$ with the same eigenvalue: $$T F(\psi) = i \lambda F(\psi)  .$$ So, the number $\lambda$ is 'conserved' by the operator $F$.

The element $T \in {\mathfrak{g}}$ will act as a skew-adjoint operator on any unitary representation of $G$. Physicists prefer to work with self-adjoint operators since these have real eigenvalues. In quantum mechanics, self-adjoint operators are called 'observables'. We can get an observable by dividing $T$ by $i$.

In Casson and Condon's isospin theory of the strong interaction, the symmetry group $G$ is ${\rm SU}(2)$. Here isospin, or more precisely $I_3$, arises as above: it is just the eigenvalue of a certain element of ${\mathfrak{su}}(2)$, divided by $i$ to get a real number. Because any physical process caused by the strong force is described by an intertwining operator, *isospin is conserved*. So, the total $I_3$ of any system remains unchanged after a process that involves only strong interactions.

Nevertheless, for the states in ${\mathbb C}^2$ that mix protons and neutrons to have any meaning, there must be a mechanism which can convert protons into neutrons and vice versa. Mathematically, we have a way to do this: the action of ${\rm SU}(2)$. What does this correspond to, physically?

The answer originates in the work of Hideki Yukawa. In the early 1930s, he predicted the existence of a particle that mediates the strong force, much as the photon mediates the electromagnetic force. From known properties of the strong force, he was able to predict that this particle should be about 200 times as massive as the electron, or about a tenth the mass of a proton. He predicted that experimentalists would find a particle with a mass in this range, and that it would interact strongly when it collided with nuclei.

Partially because of the intervention of World War II, it took over ten years for Yukawa's prediction to be vindicated. After a famous false alarm (see Section [\[sec:generations\]](#sec:generations){reference-type="ref" reference="sec:generations"}), it became clear by 1947 that a particle with the expected properties had been found. It was called the **pion** and it came in three varieties: one with positive charge, the $\pi^+$, one neutral, the $\pi^0$, and one with negative charge, the $\pi^-$.

The pion proved to be the mechanism that can transform nucleons. To wit, we observe processes such as those in Figure [1](#fig:piN_vertices){reference-type="ref" reference="fig:piN_vertices"}, where we have drawn the Feynman diagrams which depict the nucleons absorbing pions, transforming where they are allowed to by charge conservation.

<figure id="fig:piN_vertices">
<div class="center">
<table>
<tbody>
<tr class="odd">
<td style="text-align: center;"><img src="pi-p_vertex" alt="image" /></td>
<td style="text-align: center;"><img src="pi+n_vertex" alt="image" /></td>
</tr>
<tr class="even">
<td style="text-align: center;"><span class="math inline"><em>π</em><sup>−</sup> + <em>p</em> → <em>n</em></span></td>
<td style="text-align: center;"><span class="math inline"><em>π</em><sup>+</sup> + <em>n</em> → <em>p</em></span></td>
</tr>
<tr class="odd">
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="even">
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="odd">
<td style="text-align: center;"><img src="pi0p_vertex" alt="image" /></td>
<td style="text-align: center;"><img src="pi0n_vertex" alt="image" /></td>
</tr>
<tr class="even">
<td style="text-align: center;"><span class="math inline"><em>π</em><sup>0</sup> + <em>p</em> → <em>p</em></span></td>
<td style="text-align: center;"><span class="math inline"><em>π</em><sup>0</sup> + <em>n</em> → <em>n</em></span></td>
</tr>
</tbody>
</table>
</div>
<figcaption>The nucleons absorbing pions.</figcaption>
</figure>

Because of isospin conservation, we can measure the $I_3$ of a pion by looking at these interactions with the nucleons. It turns out that the $I_3$ of a pion is the same as its charge: 1em

::: center
    Pion      $I_3$
  --------- -------
   $\pi^+$     $+1$
   $\pi^0$        0
   $\pi^-$     $-1$
:::

Here we pause, because we can see the clearest example of a pattern that lies at the heart of the Standard Model. It is the relationship between isospin $I_3$ and charge $Q$. For the pion, isospin and charge are equal: $$Q(\pi) = I_3(\pi).$$ But they are also related for the nucleon, though in a subtler way: 1em

::: center
   Nucleon             $I_3$  Charge
  --------- ---------------- --------
     $p$       $\frac{1}{2}$    1
                             
     $n$      $-\frac{1}{2}$    0
:::

1em The relationship for nucleons is $$Q(N) = I_3(N) + \frac{1}{2} .$$ This is nearly the most general relationship. It turns out that, for any given family of particles that differ only by $I_3$, we have the **Gell-Mann--Nishijima formula**: $$Q = I_3 + Y/2$$ where the charge $Q$ and isospin $I_3$ depend on the particle, but a new quantity, the **hypercharge** $Y$, depends only on the family. For example, pions all have hypercharge $Y = 0$, while nucleons both have hypercharge $Y =
1$.

Mathematically, $Y$ being constant on 'families' just means it is constant on representations of the isospin symmetry group, ${\rm SU}(2)$. The three pions, like the proton and neutron, are nearly identical in terms of mass and their strong interactions. In Heisenberg's theory, the different pions are just different isospin states of the same particle. Since there are three, they have to span a three-dimensional representation of ${\rm SU}(2)$.

Up to isomorphism, there is only one three-dimensional complex irrep of ${\rm SU}(2)$, which is ${\rm Sym}^2 {\mathbb C}^2$, the symmetric tensors of rank 2. In general, the unique $(n+1)$-dimensional irrep of ${\rm SU}(2)$ is given by ${\rm Sym}^n {\mathbb C}^2$. Physicists call this the **spin-$n/2$ representation** of ${\rm SU}(2)$, or in the present context, the 'isospin-$n/2$ representation'. This representation has a basis of vectors where $I_3$ ranges from $-n/2$ to $n/2$ in integer steps. Nucleons lie in the isospin-$\frac{1}{2}$ representation, while pions lie in the isospin-$1$ representation.

This sets up an interesting puzzle. We know two ways to transform nucleons: the mathematical action of ${\rm SU}(2)$, and their physical interactions with pions. How are these related?

The answer lies in the representation theory. Just as the two nucleons span the two-dimensional irrep of ${\mathbb C}^2$ of ${\rm SU}(2)$, the pions span the three-dimensional irrep ${\rm Sym}^2 {\mathbb C}^2$ of ${\rm SU}(2)$. But there is another way to write this representation which sheds light on the pions and the way they interact with nucleons: because ${\rm SU}(2)$ is itself a three-dimensional *real* manifold, its Lie algebra ${\mathfrak{su}}(2)$ is a three-dimensional *real* vector space. ${\rm SU}(2)$ acts on itself by conjugation, which fixes the identity and thus induces linear transformations of ${\mathfrak{su}}(2)$, giving a representation of ${\rm SU}(2)$ on ${\mathfrak{su}}(2)$ called the adjoint representation.

For simple Lie groups such as ${\rm SU}(2)$, the adjoint representation is irreducible. Thus ${\mathfrak{su}}(2)$ is a three-dimensional *real* irrep of ${\rm SU}(2)$. This is different from the three-dimensional *complex* irrep ${\rm Sym}^2 {\mathbb C}^2$, but very related. Indeed, ${\rm Sym}^2 {\mathbb C}^2$ is just the complexification of ${\mathfrak{su}}(2)$: $${\rm Sym}^2 {\mathbb C}^2 \cong{\mathbb C}\otimes {\mathfrak{su}}(2) \cong\mathfrak{sl}(2,{\mathbb C}) .$$

The pions thus live in $\mathfrak{sl}(2,{\mathbb C})$, a complex Lie algebra, and this acts on ${\mathbb C}^2$ because ${\rm SU}(2)$ does. To be precise, Lie group representations induce Lie algebra representations, so the real Lie algebra ${\mathfrak{su}}(2)$ has a representation on ${\mathbb C}^2$. This then extends to a representation of the complex Lie algebra $\mathfrak{sl}(2,{\mathbb C})$. And this representation is even familiar---it is the fundamental representation of $\mathfrak{sl}(2,{\mathbb C})$ on ${\mathbb C}^2$.

Quite generally, whenever $\mathfrak{g}$ is the Lie algebra of a Lie group $G$, and $\rho \colon G \times V \to V$ is a representation of $G$ on some finite-dimensional vector space $V$, we get a representation of the Lie algebra $\mathfrak{g}$ on $V$, which we can think of as a linear map $$d\rho \colon\mathfrak{g} \otimes V \to V .$$ And this map is actually an intertwining operator, meaning that it commutes with the action of $G$: since $\mathfrak{g}$ and $V$ are both representations of $G$ this is a sensible thing to say, and it is easy to check.

Pions act on nucleons via precisely such an intertwining operator: $$\mathfrak{sl}(2, {\mathbb C}) \otimes {\mathbb C}^2 \to {\mathbb C}^2 .$$ So, the interaction between pions and nucleons arises naturally from the action of ${\rm SU}(2)$ on ${\mathbb C}^2$ after we complexify the Lie algebra of this group!

Physicists have invented a nice way to depict such intertwining operators---**Feynman diagrams**:

<figure id="fig:piN_vertex">
<div class="center">
<img src="piN_vertex" />
</div>
<figcaption>A nucleon absorbs a pion.</figcaption>
</figure>

Here we see a nucleon coming in, absorbing a pion, and leaving. That is, this diagram depicts a basic *interaction* between pions and nucleons.

Feynman diagrams are calculational tools in physics, though to actually use them as such, we need quantum field theory. Then, instead of just standing for intertwining operators between representations of compact groups such as ${\rm SU}(2)$, they depict intertwining operators between representations of the product of this group and the Poincaré group, which describes the symmetries of spacetime. Unfortunately, the details are beyond the scope of this paper. By ignoring the Poincaré group, we are, in the language of physics, restricting our attention to 'internal degrees of freedom', and their 'internal' (i.e., gauge) symmetries.

Nonetheless, we can put basic interactions like the one in figure [2](#fig:piN_vertex){reference-type="ref" reference="fig:piN_vertex"} together to form more complicated ones, like this:

::: center
![image](piN_exchange)
:::

Here, two nucleons interact by exchanging pions. This is the mechanism for the strong force proposed by Yukawa, still considered approximately right today. Better, though, it depicts all the representation-theoretic ingredients of a modern gauge theory in physics. That is, it shows two nucleons, which live in a representation ${\mathbb C}^2$ of the gauge group ${\rm SU}(2)$, interacting by the exchange of a pion, which lives in the complexified adjoint rep, ${\mathbb C}\otimes {\mathfrak{su}}(2)$. In the coming sections we will see how these ideas underlie the Standard Model.
