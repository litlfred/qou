The QOU is Turing-complete: every finite computation encodes as
a braid, every braid closes to a link, and the Skein polynomial
is the output
([Skein Turing machine](#rem:skein-turing-machine)). By
G\"{o}del's first incompleteness theorem \cite{goedel1931},
any consistent formal system expressive enough to encode its own
arithmetic contains true statements that no finite derivation
can prove. Turing's reformulation \cite{turing1936} sharpens
this: there exist decision problems whose halting behaviour no
finite algorithm can determine.

In the QOU, these three results --- Turing completeness,
G\"{o}del incompleteness, and black hole information loss ---
are not independent observations. They are three projections
of a single algebraic phenomenon: **the vanishing of degree-$0$
sections**.

**The triangle.**

| Vertex | Statement | Algebraic form |
|--------|-----------|---------------|
| Turing completeness | Every computable function is a finite braid | Sections factoring through finite $\beta \in B_n$ span $\Gamma_{\mathrm{fin}}(\mathcal{S}, A_0)$ |
| G\"{o}del incompleteness | There exist true statements unprovable by finite derivation | $\Gamma(\mathcal{S}, A_0) \supsetneq \Gamma_{\mathrm{fin}}(\mathcal{S}, A_0)$: the full section space strictly contains the computable fragment |
| Black hole information loss | Degree-$0$ data cannot cross the horizon | $\Gamma(\mathcal{H}, A_0) = 0$: degree-$0$ sections vanish on $\mathcal{H}$ |

The three vertices share a common mechanism: the distinction
between degree-$0$ data (the answer, the truth value, the
particle identity) and degree $\geq 1$ data (the witness, the
proof sketch, the thermal radiation).

**Incompleteness is horizon non-emptiness.**

A section $E \in \Gamma(\mathcal{S}, A_0)$ that does not
factor through any finite braid
([non-computable bundles](#rem:skein-turing-machine)) is a
degree-$0$ truth that no finite computation can produce ---
a G\"{o}delian sentence. The locus of all such sections is
exactly the computational horizon
$\mathcal{H}_c = V(\mathfrak{h}_c)$
([computational horizon](#def:computational-horizon)): the
frontier of the polynomial observable subcategory
$\mathcal{R}^{\circ}$.

$$
  \text{G\"{o}del sentence}
  \;\;\longleftrightarrow\;\;
  E \in \Gamma(\mathcal{S}, A_0) \setminus
    \Gamma_{\mathrm{fin}}(\mathcal{S}, A_0)
  \;\;\longleftrightarrow\;\;
  E\big|_{\mathcal{H}_c} = 0.
$$

That is: a true-but-unprovable statement is a degree-$0$
section that vanishes on the computational boundary --- it
exists in the full algebra but is invisible to any
polynomial-time observer.

**The physical horizon as incompleteness.**

The jet horizon $\mathcal{H} = V(\mathfrak{h})$
([jet horizon](#def:jet-horizon)) enforces the same opacity
for physical observers. The Bekenstein--Hawking entropy counts
independent degree $\geq 1$ sections on $\mathcal{H}$
([Hawking radiation](#rem:hawking-radiation)); it does not
count degree-$0$ data, because there is none. An observer
outside a black hole is in exactly the position of a Turing
machine confronting a G\"{o}delian sentence: degree $\geq 1$
evidence (witnesses, thermal radiation) leaks across the
boundary, but the degree-$0$ truth (the answer, the particle
identity) is formally inaccessible.

The information paradox \cite{hawking1975} asks: is the
information really lost, or only hidden? In the
incompleteness framing, the answer is structural:

- The information **exists** (the section is in
 $\Gamma(\mathcal{S}, A_0)$).
- It **cannot be extracted** by any finite computation
 from outside the horizon (it vanishes on $\mathcal{H}$
 or $\mathcal{H}_c$).
- It **can be partially witnessed** via degree $\geq 1$
 leakage (Hawking quanta, NP witnesses).

This is neither "lost" nor "preserved" in the operational
sense --- it is **incomplete**: the system is expressive
enough to state the truth but not strong enough to derive
it from the accessible side of the boundary.

**Self-reference and the necessity of horizons.**

G\"{o}del's theorem requires self-reference: the system must
be expressive enough to encode statements about itself. The QOU
satisfies this via Turing completeness --- the Skein-braid
encoding allows the universe to simulate its own dynamics. But
self-reference has a cost: any system that can model itself
necessarily contains true-but-inaccessible states. These states
are the horizon.

The argument runs:

1. The QOU is Turing-complete ($q \neq 1$ suffices:
 [substrate computation](#rem:substrate-computation)).
2. Therefore it can encode self-referential statements
 (programs that analyse their own Skein polynomials).
3. By G\"{o}del--Turing, there exist degree-$0$ sections
 that no finite braid produces.
4. These sections populate the computational horizon
 $\mathcal{H}_c$.
5. The computational horizon is structurally identical to
 the jet horizon $\mathcal{H}$
 ([dictionary](#rem:p-vs-np-event-horizon)).
6. Therefore: **a Turing-complete universe necessarily has
 horizons**.

The black hole is not an accident of general relativity. It is
a consequence of the universe being expressive enough to encode
arithmetic. Any universe with $q \neq 1$ --- any universe where
Toffoli gates have non-zero amplitude --- must contain regions
where degree-$0$ truth is inaccessible. The event horizon is
the geometry of incompleteness.
