't Hooft's **Cellular Automaton Interpretation** of
quantum mechanics \cite{thooft2016} introduces the notion of a
**beable algebra** $\mathcal{A}_{\mathrm{beable}}$: a maximal
commuting subalgebra of observables whose simultaneous eigenstates
constitute the ontological basis of the underlying deterministic
automaton. The framework's observable subcategory
$\mathrm{Bun}^{\circ}(\mathbb{P}(V))$
 realises
this notion structurally, with the following dictionary:

| 't Hooft (CAI) | QOU (this framework) |
|---|---|
| beable algebra $\mathcal{A}_{\mathrm{beable}}$ | degree-$0$ algebra $\Gamma(\mathcal{S}, A_0)$ |
| ontological basis | simultaneous eigenstates of the algebra $\Gamma(\mathcal{S}, A_0)$ |
| "elements of reality" | degree-$0$ observables  |
| beable axiom (maximal commuting) | non-degeneracy of the Frobenius pairing on $A_0$ |
| epistemological / templated states | degree-$> 0$ floors of the brane tower |

**Structural vs. axiomatic.**
't Hooft posits the beable algebra as an additional axiom: one
must specify, separately from the dynamics, which subalgebra of
operators is ontological. The QOU observable subcategory removes
this axiomatic freedom: the degree-$0$ algebra
$\Gamma(\mathcal{S}, A_0)$ is **determined** by the bundle data
$\mathcal{S}$, and the non-triviality condition
$\Gamma(\mathcal{S}, A_0) \neq 0$ is a property of the bundle rather than
a choice. The ontological basis is therefore a derived feature of the
categorical structure rather than an input to the theory.

**Maximality.**
't Hooft's beable algebra is by construction maximal commuting
(elements outside it fail to commute with some beable). In QOU
the corresponding maximality is the statement that the degree-$0$
algebra is the **maximal** floor of the brane tower on which the
Frobenius pairing is non-degenerate; higher floors ($A_n$ for
$n \geq 1$) carry richer braided structure and fail the
commutativity required for simultaneous measurement. The
filtration $A_0 \subset A_1 \subset \cdots$ ordered by Frobenius
non-degeneracy is the categorical analogue of the beable / epistemic
split.

**Epistemic states as higher floors.**
The states 't Hooft calls *epistemological* (templated
superpositions used by the observer to encode partial knowledge)
correspond in QOU to elements of the higher brane-tower floors
restricted to $\mathcal{S}$ for $n \geq 1$, which are well-defined as
categorical data, but not directly measurable since the Frobenius
pairing is degenerate or absent at those floors. Projection to
$A_0$ is the QOU realisation of 't Hooft's
"epistemic-to-ontological" projector.

**Consequence: no superselection axiom.**
't Hooft requires a separate superselection postulate to forbid
coherent superpositions across beable sectors. In QOU this
follows automatically from the categorical structure: the
connected components $\pi_0(\mathrm{Bun}^{\circ})$ (the **aeons**)
are precisely the superselection sectors,
and morphisms between distinct aeons are forbidden by the
jet-horizon structure  rather
than by an additional axiom.
