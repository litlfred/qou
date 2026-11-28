**Proposition.** Split the five strands of $5 = C \oplus V$ into colour $C = \{0,1,2\}$ and
isospin $V = \{3,4\}$, and call an even subset $S$ a *quark state* when
$1 \le |S \cap C| \le 2$. Then:

1. the quark states are exactly the twelve subsets
   $\{c,3\}$, $\{c,4\}$, $\{c,c+1\}$ and $\{c\}^c$ for $c \in C$ (indices of $c+1$ mod $3$),
   all different; the other four even subsets $\varnothing$, $\{3,4\}$, $\{3\}^c$, $\{4\}^c$
   are colour singlets;
2. at $\alpha = 1/6$ the charges $y_S$ of these four shapes are $+2/3$, $-1/3$, $-2/3$,
   $+1/3$, independent of $c$, and they are the charges `slotCharge` assigns to the slots
   colour$\wedge 3$, colour$\wedge 4$, colour$\wedge$colour and colour;
3. these four charges are distinct, so any assignment of slots to the eight
   first-generation quark states that reproduces their charges, with the dual flag as
   sign, is the Georgi–Glashow assignment of
   [`prop:strand-slot-separates-gen1`](strand-slot-separates-gen1.md).

So the slot is the shape of an even subset, and the Georgi–Glashow embedding
\cite{baez-huerta2010} is no longer an input once matter is the even part
([`prop:even-strand-generation`](even-strand-generation.md)). The degree-$4$ shape
$\{c\}^c$ carries the $\bar 5$ charge $-y_c$ by complementation; the $\bar 5$ is not
put in separately.

**Proof.** Items 1 and the distinctness in 3 are finite checks over the sixteen even
subsets. Item 2 uses $y_i = (-\tfrac13, -\tfrac13, -\tfrac13, 1, 0)$ at $\alpha = 1/6$ and
$y_{\{c\}^c} = -y_c$. The forcing in item 3 follows from distinctness and the charge of
each state.

**What stays an input.** The dual flag: which states lie in the even part and which in
its conjugate. It equals the helicity, so it carries the open chirality sign.

## Lean structure

`QOU.EightfoldWay.SlotFromEvenShape`: `quark_iff_slotSubset`, `card_quarkEven`,
`card_leptonEven`, `stateCharge_slotSubset`, `slotCharge_injective`, `slot_forced`.
Sorry-free; base ring $\mathbb{Q}$.
