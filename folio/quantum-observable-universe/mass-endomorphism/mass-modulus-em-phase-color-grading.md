The factorization of [Color and spacetime are orthogonal $S_2\times S_3$ factors of the Bring Galois group $S_5$](#prop:color-spacetime-s5-factorization) fixes how the three observables of a Bring-embeddable knot sit on the single trace scalar $\mathrm{tr}_M$ and its trace algebra $H_2(q)\oplus H_3(q)$.

## Three readings of one trace

We write the trace scalar in polar form:
$$
  \mathrm{tr}_M \;=\; \lVert\mathrm{tr}_M\rVert\,\exp\!\big(i\,\arg\mathrm{tr}_M\big).
$$
This forms the multiplicative companion of the additive complex-volume reconstruction $\mathrm{Re}\mathfrak{V}+i\mathrm{Im}\mathfrak{V}=\mathfrak{V}$ ([Complex-volume unification](#conj:binding-qbeta-complex-volume)). We then have:

| reading | quantity | sector | character |
|---|---|---|---|
| **mass** | modulus $\lVert\mathrm{tr}_M\rVert$ | both | nonnegative magnitude |
| **electromagnetism** | argument $\arg\mathrm{tr}_M$ | spacetime / $S_2$ | continuous $U(1)$ |
| **color** | $S_3$ irrep grading | color / $S_3$ | discrete |

Mass evaluates the magnitude that survives both sectors. The argument evaluates the continuous $U(1)$ framing/Chern–Simons phase. This provides the $\mathrm{Im}\mathfrak{V}$ channel, picked up as the ribbon twist $q^{2w\,c(\lambda)}$ on a framed knot of writhe $w$. The identification of this channel with a bar-odd part is conjectural ([The binding trace and the $\mathfrak{Q}_\beta$ residue are the bar-even and bar-odd parts of one fibre element](../mass-theory/bar-parity-split.md)). It lives in the spacetime block, where we read it as the electromagnetic phase. Color provides the discrete grading of the algebra element across the $H_3(q)$ representations, before the trace collapses it to a scalar.

## Color is not the phase

The color factor $S_3$ fixes the spacetime coordinates. The spacetime factor $S_2$ fixes the color coordinates ([Color and spacetime are orthogonal $S_2\times S_3$ factors of the Bring Galois group $S_5$](#prop:color-spacetime-s5-factorization), parts 1–2). Therefore, color and electromagnetism form independent coordinates. The discrete color charge is not a function of the continuous phase, and conversely. The rigidity in part $3$ of that proposition makes this non-coincidence sharp. A continuous winding argument cannot factor through a finite group such as $\mu_5$. Thus, $\arg\mathrm{tr}_M$ remains structurally barred from being a color character.

The two remain nonetheless faces of one substrate. The Galois group $S_5$ properly contains $S_2\times S_3$. Its remaining generators carry spacetime indices into color indices. An electromagnetic-to-color relation therefore forms an $S_5$ statement, realized by those off-block generators, not a relation internal to the $U(1)$ phase.

## Archimedean realization

The polar split provides the archimedean reading. The modulus and argument require the realization of the trace over $\mathbb{C}$, on the far side of the substrate-to-archimedean wall. The structural content of [Color and spacetime are orthogonal $S_2\times S_3$ factors of the Bring Galois group $S_5$](#prop:color-spacetime-s5-factorization)—the faithful $S_2\times S_3\hookrightarrow S_5$ embedding, the orthogonality of the two sectors, and the divisibility rigidity—is generic and requires no such realization.

## Relation to the literature

The individual ingredients form classical results. The imaginary partner of a hyperbolic volume forms a Chern–Simons invariant (Neumann–Zagier \cite{neumann-zagier1985}). The colored-Jones asymptotics realize this complex volume at roots of unity (Volume Conjecture \cite{kashaev1997, murakami-murakami2001}). The Jones polynomial forms a Chern–Simons expectation value whose framing dependence produces the $U(1)$ phase (Witten \cite{witten1989}, Reshetikhin–Turaev \cite{reshetikhin1991}). The complexified continuation of the phase forms Witten \cite{witten2011}, and the bar-involution structure of the root-of-unity asymptotics forms the quantum-modularity of Zagier \cite{zagier2010}. The quantum dilogarithm controlling the asymptotics forms Faddeev–Kashaev \cite{faddeev1994}.

Read against this work, two of our identifications constitute recombinations and two are specific to this framework. The reading *modulus/argument = volume/Chern–Simons* and the placement of the argument as a $U(1)$ framing phase restate the cited results. The identification of the **modulus with mass** $\lVert\mathrm{tr}_M\rVert$ and of **color with the $S_3\subset S_5$ representation grading of the Bring quintic's Galois group** are our own. The literature offers the nearby $A_5$ / $S_5$ flavor and modular-flavor symmetries rather than this trace-algebra grading. Our contribution forms the group-theoretic statement that these three readings are orthogonal sectors of one trace object, alongside the rigidity barring the continuous phase from being the discrete color charge.

## Classical antecedents of the involutive reading

Resolving one object into observables under an involution is a recurring structure. Four classical instances frame ours:

- **Frobenius–Schur indicator.** The character involution $\chi\mapsto\chi(g^{-1})$ \cite{frobenius-schur1906}—the bar-involution $q\mapsto q^{-1}$ on the Hecke side—sorts every irreducible representation as real, quaternionic, or complex. The bar-even (binding, $\cosh$) and bar-odd ($\beta$-decay, $\sinh$) channels construct the rank-one shadow of this trichotomy on the trace.
- **Modular conjugation.** The Markov trace forms a trace on a finite von Neumann algebra \cite{jones1985}. Every such algebra carries the Tomita–Takesaki modular conjugation $J$ and modular operator $\Delta$ \cite{takesaki1970}. The observable elements are the $J$-fixed (self-adjoint) ones, and $a=\tfrac12(a+a^*)+\tfrac12(a-a^*)$ forms the algebra-level bar-parity split. The polar reading (mass $=\lVert\mathrm{tr}_M\rVert$, phase $=\arg\mathrm{tr}_M$) provides its modulus–modular-flow form.
- **Weil operator.** On a polarized Hodge structure, the Weil operator \cite{weil1958} supplies the complex structure packaging real harmonic periods into a polarized complex period. The complex volume $\mathrm{Vol}+i\,\mathrm{CS}$ \cite{neumann-zagier1985} provides such a period, and $H^1(\mathrm{Bring})=2W$ forms such a structure—the Hodge-theoretic home of the complex-volume half.
- **Conjugate-variable amplitude.** The oscillator amplitude $a=q+ip$ combines a canonically conjugate pair through the symplectic complex structure, with $\lVert a\rVert^2$ the energy and $\arg a$ the phase.

In physics, this reading follows the **complex-energy / resonance** tradition. A state forms a complex pole $\mathfrak{E}_{\mathrm{pole}}=\mathfrak{m}-i\Gamma/2$ (Gamow \cite{gamow1928}, Breit–Wigner \cite{breit-wigner1936}) whose real part gives mass and whose imaginary part gives decay width. The bound sector lies on the conjugation-fixed real axis, and the optical theorem ties the imaginary part to the total decay rate. The Kramers–Kronig dispersion relations \cite{kronig1926} lock the reactive (real) and absorptive (imaginary) parts of one causal response. There, the involution is complex conjugation / time reversal. Here, the bar-involution $q\mapsto q^{-1}$ plays that role at the fibre level. We claim not the involutive reading itself, but its realization on the categorical knot trace, where $\mathrm{Im}(q_0)=0$ at the archimedean level renders the two parts separately real observable shadows.
