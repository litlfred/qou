---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS"
section_id: sec-017-62-quantum-mechanics-mu1
section_title: "Quantum Mechanics: M=U(1)"
section_number: 6.2
pages: 50-56
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.99
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS — Interest in combinatorial interpretations of mathematical entities stems from the convenience of the concrete models they provide."
---
[]{#mstuffu1 label="mstuffu1"}

As remarked earlier, the notion of a *phase* is crucial in quantum mechanics. Stuff types, and in particular stuff operators and the inner product of stuff types, proved in the last section to have a close connection to entities which resemble Feynman diagrams, but the only notion of cardinality we had for these was groupoid cardinality, which yields positive real values. We would like to be able to do more, since in quantum mechanics, these diagrams should have not a real cardinality, but a complex amplitude, which has both a magnitude and a phase. This leads us to the idea of $U(1)$-stuff types, since $U(1)$ is the group of phases, corresponding to the unit circle in $\mathbbm{C}$.

### $U(1)$-Stuff Types

From here on, we take $M=U(1)$ - an abelian monoid, and in fact an abelian group - we know that $U(1)$-stuff types exist, and that they have cardinalities in $(\mathbbm{R}^+ \otimes U(1))[\![z]\!]$, which has the obvious homomorphism into $\mathbbm{C}[\![z]\!]$. As we have seen, the cardinalities of $M$-sets for an abelian monoid $M$ lie in $M$, which we can think of ; cardinalities for $M$-groupoids lie in $\mathbbm{R}^+ \otimes M$; cardinalities for $M$-stuff types lie in $(\mathbbm{R}^+ \otimes M)[\![z]\!]$. When $M=U(1)$, this gives $\mathbbm{R}^+ \otimes U(1)$, which has a homomorphism onto $\mathbbm{C}$ $$h : \mathbbm{R}^+ \otimes U(1)\rightarrow \mathbbm{C}$$

We should note that this description of $\mathbbm{C}$ in terms of $\mathbbm{R}^+ \otimes U(1)$ explicitly separates complex numbers into a magnitude and a phase, and while it has a multiplication resembling that for $\mathbbm{C}$, but it fails to capture the addition, which is formal. However, the homomorphism $h$ just imposes the relations which define complex addition. The derived rig homomorphism $h: (\mathbbm{R}^+ \otimes U(1))[\![z]\!]\rightarrow
\mathbbm{C}[\![z]\!]$ behaves similarly. This homomorphism loses information, just as the process of taking cardinalities does, so in fact, when $M=U(1)$, we can define a new cardinality operator:

::: definition
If $\boldsymbol{\operatorname{{X}}}$ is a $U(1)$-groupoid and $\Psi:\boldsymbol{\operatorname{{X}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$ a $U(1)$-stuff type, the **complex cardinality** of $\Psi$ is $h$ applied to the usual $M$-stuff-type cardinality: $$|\Psi|_{\mathbbm{C}} = h \left( \sum_{S \in \mathbbm{N}} |\Psi_n| z^n \right) = \sum_{S \in \mathbbm{N}} h|\Psi_n| z^n$$ where $|\Psi_n|$ is the usual $M$-stuff cardinality, $h$ is the above homomorphism, and addition is in $\mathbbm{C}$.
:::

The complex cardinality is a map which takes a $U(1)$-stuff type and yields a power series in $\mathbbm{C}[\![z]\!]$, namely Fock space. When dealing with $U(1)$-stuff types, we will write $|\Psi|_{\mathbbm{C}}$ as $|\Psi|$, unless otherwise noted.

::: remark
Note that a type which consists of two states over $U(1)$-sets of the same set cardinality but opposite phase will have a cardinality in $(\mathbbm{R}^+ \otimes U(1))[\![z]\!]$ which contains a formal linear combination which is in the *kernel* of $h$. This is the critical fact that when we represent states in Fock space, there can be *interference* between states with opposite phases. In particular, the amplitude for a (categorified) state containing only those two objects will be zero.
:::

### Conjugation and The Inner Product

There is a property of $U(1)$-stuff types which is not generally shared by $M$-stuff types for arbitrary $M$, resulting from the fact that it is an Abelian group. This follows from the fact that there is a nontrivial monoid isomorphism between $U(1)$ and itself, taking each element of $U(1)$ to its multiplicative inverse. There will be such an isomorphism whenever $M$ is an Abelian group. Viewing $U(1)$ as the unit complex numbers, however, allows us to see this as complex conjugation, which is how we will think of it. Thus, there is an operation special to $U(1)$-stuff types:

::: definition
If $\boldsymbol{\operatorname{{X}}}$ is a groupoid with $U(1)$ labelling $f:\boldsymbol{\operatorname{{X}}}\rightarrow U(1)$, its **conjugate** groupoid is the $U(1)$ groupoid whose groupoid is labelling is $\overline{f}$, given by $\overline{f}(x)=\overline{f(x)}$. When we write $\boldsymbol{\operatorname{{X}}}$ for the $U(1)$-groupoid, we write the conjugate as $\overline{\boldsymbol{\operatorname{{X}}}}$. If $\Psi:\boldsymbol{\operatorname{{X}}} \rightarrow \boldsymbol{\operatorname{{FinSet_0}}}$ is a $U(1)$-stuff type, its conjugate $\overline{\Psi}$ is the type which acts like $\Psi$ on the objects of the underlying groupoid of $\boldsymbol{\operatorname{{X}}}$.
:::

This allows us to define a variant of the inner product which has the conjugate-linearity of the usual complex inner product on Fock space. To distinguish this from the (bilinear) inner product $\left\langle{\Psi,\Phi}\right\rangle$, and call it $\left\langle{ \Psi | \Phi }\right\rangle$, also a more familiar notation to physicists:

::: definition
The **Fock space inner product** is given by $$\left\langle{ \Psi | \Phi }\right\rangle = \left\langle{ \overline{\Psi} , \Phi }\right\rangle$$
:::

::: theorem
The Fock space inner product, for $U(1)$-stuff types $\Psi$ and $\Phi$ satisfies $|\left\langle{\Psi | \Phi}\right\rangle| =
\left\langle{|\Psi| | |\Phi|}\right\rangle$, giving the usual conjugate-linear inner product on $\mathbbm{C}[\![z]\!]$.

::: proof
*Proof.* $$\begin{aligned}
|\left\langle{\Psi | \Phi}\right\rangle| & = & \sum_{n\in\mathbbm{N}} |\left\langle{\Psi | \Phi}\right\rangle_n|\\
   \nonumber & = & \sum_{n\in\mathbbm{N}} |\overline{\Psi_n}| \cdot |\Phi_n|\\
   \nonumber & = & \left\langle{\,|\Psi|\, |\, |\Phi|\,}\right\rangle
\end{aligned}$$ ◻
:::
:::

So for $U(1)$-stuff types, we might want to define a new inner product given in terms of the usual $M$-stuff type inner product as $\left\langle{\Psi|\Phi}\right\rangle$. We will discuss briefly in section [\[sec:conjtimereversal\]](#sec:conjtimereversal){reference-type="ref" reference="sec:conjtimereversal"} how to interpret this seemingly arbitrary innovation.

It is worth noting here that the inner product between two states of a $U(1)$-stuff type may be zero. Of course, this can happen with stuff types in any case: for instance, if $\Psi$ is the stuff type for which there is one object in $\boldsymbol{\operatorname{{X}}}$ over every even-cardinality set, with automorphism group the same as that of the set, and no others; and $\Phi$ is similar, but has objects over odd-cardinality sets. These have cardinalities (generating functions) $\cosh(z)$ and $\sinh(z)$ respectively. They are examples of what we called "property types" in section [\[sec:forgetful\]](#sec:forgetful){reference-type="ref" reference="sec:forgetful"} - namely, these types can be interpreted as the properties "being an even set" and "being an odd set". These two stuff types are orthogonal in the sense that their inner product is zero. Here, the interpretation is that there are *no* sets having both properties, and so the stuff-type inner product is the empty groupoid.

However, the situation with $U(1)$-types is more subtle: we may have a nonempty inner product groupoid whose $U(1)$-groupoid cardinality happens to be zero. This arises because we may now have negative (and indeed complex) contributions to the sum giving this cardinality. This is related to the quantum mechanical phenomenon of "destructive interference" between states. In our formalism, this interference occurs when we apply the homomorphism $h: \mathbbm{R}^+ \otimes U(1)\rightarrow \mathbbm{C}$ and its derived variants.

We interpret the cardinality of the groupoid inner product as the usual inner product in quantum-mechanics. This is the amplitude for finding our system in a given state $\Phi$ after setting it up in a state $\Psi$, so this says this amplitude (and hence the probability) is zero.

So the transition amplitudes between some of the "pure" (decategorified) states of which $\psi$ and $\phi$ are superpositions may be nonzero, but the phases with which they appear may allow the transition between $\psi$ and $\phi$ to have zero amplitude. Thus, introducing phases allows destructive interference which makes otherwise feasible transitions impossible. We will see in the next section that this issue of phase is closely related to the concept of *time evolution* in quantum mechanics, and the *propagator*.

In particular, in the harmonic oscillator, the phase of a state changes over time, with a frequency proportional to the energy of that state. This is the effect of the *free propagator* for a system, and it is an operator. So we must describe $U(1)$-stuff operators next, and this propagator in particular.

### $U(1)$-Stuff Operators and Time

We have already noted that $M$-stuff operators act on $M$-stuff types just like ordinary stuff operators acting on stuff types, except that the groupoids are now replaced by $M$-groupoids. The groupoid $T\Psi$ for an $M$-stuff operator $T$ and type $\Psi$ then consists of pairs of objects $t \in T$ and $x \in \boldsymbol{\operatorname{{X}}}$ together with a bijection of their underlying sets. As with the product groupoid, this object is labelled by an element in $M$ given by the product of the labels on $t$ and $x$. This is well defined when $M$ is Abelian, as in the case when $M = U(1)$.

One class of $U(1)$-stuff operators which is particularly relevant to quantum mechanics is that of the *time evolution* operators. These are operators which, when applied to an $M$-stuff type $\Psi$, produce an $M$-stuff type $\Psi'$ for which the $M$-labels on the elements of the underlying sets have labels multiplied by a fixed phase in $U(1)$. An example of an object in such an operator, designated $\theta$, is shown in figure [1](#fig:timeevol){reference-type="ref" reference="fig:timeevol"}. Here, we are showing the operator $E_T$, "time evolution by $T$". We show an object which will evolve a state with three quanta of energy. Here, $\mathrm{e}^{iT}$ is the change of phase corresponding to time evolution of a one-energy-quantum state by $T$. A state with three energy quanta changes phase by $\mathrm{e}^{3iT}$.

<figure id="fig:timeevol">
<div class="center">
<embed src="timeevol.eps" />
</div>
<figcaption><span id="fig:timeevol" label="fig:timeevol"></span>An Object in The <span class="math inline"><em>U</em>(1)</span>-Stuff Operator <span class="math inline"><em>E</em><sub><em>T</em></sub></span></figcaption>
</figure>

Any object in $E_T$ has two projections - each to an underlying set of the same size. This corresponds to the fact that in unperturbed time evolution no interactions are occurring which would change the energy level of the system. An object $t$ in the groupoid of $E_T$, lying over sets with $k$ quanta of energy. There will be just one such object in $E_T$ for each finite set. It is labelled by the phase by which a state with $k$ quanta will change in time $T$. The operator $E_T$ acts on any $U(1)$-stuff type (categorified state) to give state to which this has evolved after a time $T$. An object of the resulting stuff type is shown in figure [2](#fig:timeevolresult){reference-type="ref" reference="fig:timeevolresult"}.

<figure id="fig:timeevolresult">
<div class="center">
<embed src="timeevolresult.eps" />
</div>
<figcaption><span id="fig:timeevolresult" label="fig:timeevolresult"></span>An Object in The <span class="math inline"><em>U</em>(1)</span>-Stuff Type <span class="math inline"><em>E</em><sub><em>T</em></sub><em>Ψ</em></span></figcaption>
</figure>

The object in the groupoid of $E_T \Psi$ is the entire ensemble associated to the finite set $p_2(t)$. It includes the object $t \in
E_T$ itself, as well as $x \in \boldsymbol{\operatorname{{X}}}$, their underlying sets and the bijection $\alpha_{x,t}$ between them, and also their associated labels $\mathrm{e}^{3i \theta}$ and $\mathrm{e}^{i \theta_1}$. This is an object in a product $U(1)$-groupoid: $U(1)\boldsymbol{\operatorname{{Gpd}}}$ is a weak 2-category with (weak) products, of which this is an example. This object in the product groupoid $E_T \times \boldsymbol{\operatorname{{X}}}$ is labelled by the product of the labels on $t$ and $x$, namely $\mathrm{e}^{i \theta_1}
\mathrm{e}^{3i \theta}$.

Suppose the $U(1)$-stuff type in question happens to just be $Z^k$ - the categorified state with just $k$ quanta of energy and no phase angle, or the property type "being an $k$-element finite set labelled by $1
\in U(1)$". Then we get $E_T(Z^k) \cong (\mathrm{e}^{i \theta} Z)^k$, and the same fact holds as an equation for the complex cardinalities. So the $U(1)$-cardinality of a $k$-element $U(1)$-set changes by $\mathrm{e}^{i k
\theta}$ in time $T$, since each quantum picks up a phase rotation of $\mathrm{e}^{i \theta}$ in time $T$. In particular, the phase of an object in a categorified state changes with a frequency proportional to its energy (the size of the underlying set).

Choosing time units so that $\theta=T$, we get a phase change of $\mathrm{e}^{iTk}$ on a state of energy $k$. We can write this as $E_T=\mathrm{e}^{iTN}$, where $N$ is the number operator. To prove this equality at the categorified level (using a categorification of the exponential such as we have already discussed) would require a fully categorified version of the complex numbers. However, for now we can observe that this will be true at the level of cardinalities, and take it as a definition. This arises physically from the Hamiltonian formulation of quantum mechanics. We will not enter into this in detail, but note that the free Hamiltonian is just $H_0 = N$, the number operator in the exponent of the propagator, which measures the energy of a state.

Since $\mathrm{e}^{iTN}$ has exactly one object for each cardinality, the product groupoid $\mathrm{e}^{iTN} \Psi$ is equivalent to the groupoid whose objects are the same as those of $\boldsymbol{\operatorname{{X}}}$, but whose $U(1)$-labellings have been multiplied by phases $\mathrm{e}^{iTk}$, for an object with underlying set $\boldsymbol{k}$. This is the groupoid of the state $\Psi$, time-evolved by $T$. Note that time-evolution by $-T$ will be given by a similar operator $E_{-T} = \mathrm{e}^{-iTN}$: all the object-labels are the inverses of those of $E_T$. We will return to this point in section [\[sec:conjtimereversal\]](#sec:conjtimereversal){reference-type="ref" reference="sec:conjtimereversal"}.

In any case, using these propagators, and the $U(1)$ version of inner product groupoids whose objects resemble Feynman diagram for interactions, we recover a combinatorial interpretation for many of the standard features of the quantum mechanics of the harmonic oscillator.

### Feynman Diagrams And Perturbation

Having found a categorification of the quantum harmonic oscillator, we know that transition amplitudes such as $\left\langle{\psi,p(\frac{\phi^n}{n!})\psi '}\right\rangle$ as a sum over Feynman diagrams. In physically realistic settings, this sort of amplitude often arises when we consider the time-evolution of an oscillator which is perturbed. The *free* oscillator evolves in time according to the operator $E_T=\mathrm{e}^{-iTN}$ described above. The *perturbed* oscillator, on the other hand, describes a situation where the energy of the oscillator is modified by another term: it only approximately matches the description of the free oscillator we have been using. Physically, this represents a potential in which the oscillator is moving. This means that the energy of the oscillator is changed by the addition of an extra term, $V$, which is some function of position, which we think of as a *potential energy*, in addition to the energy in the oscillator proper.

In this case, time evolution can be calculated using the new energy, $H = H_0 + V$. If $V$ is a function of position, then since the position is proportional to $\operatorname{a} + \operatorname{a}^{\ast} = \phi$, we have $V = f(\phi)$, for some function $f$. We will consider the case where $f=p$ is some polynomial (though naturally any analytic function can be approximated this way to some degree, so we can obtain successive approximations by taking a sequence of $p_k$ converging to $f$). Since the energy for the free oscillator is already quadratic in position, we assume that $f$ has minimum degree at least 3. In this case, at the decategorified level, the amplitudes for time evolution by time $t$ associated to the Hamiltonian $H = N + V$, are: $$\label{eq:perturbfeynman}
\left\langle{Z^k|\mathrm{e}^{-iTH}Z^l}\right\rangle = \sum_{n=0}^{\infty} \int_{0 \leq t_1 \leq \dots \leq t_n \leq T} \left\langle{Z^k|\mathrm{e}^{-i(T-t_n)N}V\mathrm{e}^{-i(t_n-t_{n-1})N}V \dots V\mathrm{e}^{-it_1N} Z^l}\right\rangle$$ To avoid considering questions of convergence, we think of this purely as a statement about power series in $T$. It would take us too far afield to derive this standard quantum-mechanical fact in full detail, though background can be found in [@bjordrel], and one derivation of this equation in our setting can be found in [@catquan]. However, we will point out here that it follows from the fact that the evolution of a state is governed by the Schrödinger equation, which amounts to: $$\partial_t \psi = -i (\mathrm{e}^{itH_0}V\mathrm{e}^{-itH_0})$$ Integrating this equation over time, we get $$\psi(t) = -i \int_0^t (\mathrm{e}^{itH_0}V\mathrm{e}^{-itH_0})\psi(t_0) \mathrm{d}t_0 + \psi(0)$$ and by repeated substitution of this expression for $\psi(t)$ into the integral, we get the sum of integrals which appear in the expression above. Taking the inner product with this operator, we finally get the whole expression.

Ideally, we would like to derive this equation entirely at the categorified level. However this would require a more complete understanding of the categorified version of the complex numbers than we have constructed here. To recover time evolution by a phase from an expression of the form $\mathrm{e}^{itH_0}$, we would need to see that the result is indeed a phase in $U(1)$.

However, knowing that the equation holds at the decategorified level allows us to give a simple interpretation for the formula.

::: theorem
The transition amplitude $\left\langle{z^k|\mathrm{e}^{-iTH}z^l}\right\rangle$ for the perturbed harmonic oscillator with potential $V=f(\phi)$ is given by a sum over all Feynman diagrams given as composites of those associated with $V$, from a state with $k$ quanta to one with $l$ quanta. The sum is of an integral over all labellings of the edges of the diagrams such that the total phase along all paths is $\mathrm{e}^{-iT}$.

::: proof
*Proof.* This transition amplitude is the $U(1)$-groupoid cardinality of the inner product $\left\langle{Z^k|E^{iTH}Z^l}\right\rangle$, and given by [\[eq:perturbfeynman\]](#eq:perturbfeynman){reference-type="ref" reference="eq:perturbfeynman"}. Consider the operator in that equation, $$O=\mathrm{e}^{-i(T-t_n)N}V\mathrm{e}^{-i(t_n-t_{n-1})N}V \dots V\mathrm{e}^{-it_1N}$$ We know that the terms $\mathrm{e}^{-i(t_i-t_{i-1})N}$ are just free propagators, which contribute a phase of $\mathrm{e}^{-i()}$ for each quantum of energy. We can think of these operators as having objects given by any number of "strands", one for each quantum, and each strand labelled by a phase $\mathrm{e}^{-i(t_i-t_{i-1})}$, the total number giving the total phase change associated to that energy.

Now consider the $U(1)$-stuff operators $V$. Each of these operators has a groupoid whose objects are naturally identified with Feynman diagrams of the sort associated with $V$. These do not affect phases.

Composing the operators together, we get all possible composites of Feynman diagrams of the type associated to $V$, connected by diagrams whose effect is to label strands by phases associated to the time intervals between interactions. To find the total phase associated to such a composite, we multiply all phases. This is clearly equivalent to multiplying the phases on any labelled edges which are joined by the composition to get a phase on the resulting edge, then multiplying the product of all edges thus produced.

The transition amplitude we want to recover is: $$\sum_{n=0}^{\infty} \int_{0 \leq t_1 \leq \dots \leq t_n \leq T} \left\langle{Z^k|O Z^l}\right\rangle$$ The sum taken over all $n$ simply means that we are taking a groupoid containing all possible $n$-fold composites of this form. The integral over all $n$-part partitions of the interval $[0,T]$ means each such diagram contributes a phase found by integrating over all possible ways of dividing the interval into free and interaction parts. This contribution is weighted by the size of the symmetry group, since the inner product inside the integral is just a $U(1)$-groupoid cardinality.

This proves the statement. ◻
:::
:::

This recovers the usual Feynman rules for calculating transition amplitudes in the oscillator.
