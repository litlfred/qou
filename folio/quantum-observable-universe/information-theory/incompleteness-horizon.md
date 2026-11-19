The QOU is Turing-complete: every finite computation encodes as a braid, every braid closes to a link, and the Skein polynomial acts as the output ([Skein Turing machine](#rem:skein-turing-machine)). By G\"{o}del's first incompleteness theorem \cite{goedel1931}, any consistent formal system expressive enough to encode its own arithmetic contains true statements that evade finite derivation. Turing's reformulation \cite{turing1936} sharpens this: decision problems exist whose halting behaviour no finite algorithm can determine.

In the QOU, Turing completeness, G\"{o}del incompleteness, and black hole information loss are not independent. They arise as three projections of a single algebraic phenomenon: **the vanishing of degree-$0$ sections**.

**The triangle.**

| Vertex | Statement | Algebraic form |
|--------|-----------|---------------|
| Turing completeness | Every computable function is a finite braid | Sections factoring through finite $\beta \in B_n$ span $\Gamma_{\mathrm{fin}}(\mathcal{S}, A_0)$ |
| G\"{o}del incompleteness | There exist true statements unprovable by finite derivation | $\Gamma(\mathcal{S}, A_0) \supsetneq \Gamma_{\mathrm{fin}}(\mathcal{S}, A_0)$: the full section space strictly contains the computable fragment |
| Black hole information loss | Degree-$0$ data cannot cross the horizon | $\Gamma(\mathcal{H}, A_0) = 0$: degree-$0$ sections vanish on $\mathcal{H}$ |

These three vertices share a common mechanism: the categorical distinction between degree-$0$ data (the answer, truth value, or particle identity) and degree $\geq 1$ data (the witness, proof sketch, or thermal radiation).

**Incompleteness is horizon non-emptiness.**

A section $E \in \Gamma(\mathcal{S}, A_0)$ that does not factor through any finite braid ([non-computable bundles](#rem:skein-turing-machine)) constitutes a degree-$0$ truth that no finite computation can yield. It acts as a G\"{o}delian sentence. The locus of all such sections is precisely the computational horizon $\mathcal{H}_c = V(\mathfrak{h}_c)$ ([computational horizon](#def:computational-horizon)). This horizon defines the frontier of the polynomial observable subcategory $\mathcal{R}^{\circ}$:

$$
  \text{G\"{o}del sentence}
  \;\;\longleftrightarrow\;\;
  E \in \Gamma(\mathcal{S}, A_0) \setminus
    \Gamma_{\mathrm{fin}}(\mathcal{S}, A_0)
  \;\;\longleftrightarrow\;\;
  E\big|_{\mathcal{H}_c} = 0.
$$

A true-but-unprovable statement thus functions as a degree-$0$ section that vanishes on the computational boundary. It persists in the full algebra but remains invisible to any polynomial-time observer.

**The physical horizon as incompleteness.**

The jet horizon $\mathcal{H} = V(\mathfrak{h})$ ([jet horizon](#def:jet-horizon)) enforces identical opacity for physical observers. The Bekenstein--Hawking entropy counts independent degree $\geq 1$ sections on $\mathcal{H}$ ([Hawking radiation](#rem:hawking-radiation)). It counts no degree-$0$ data, because none survives. An observer outside a black hole occupies the exact position of a Turing machine confronting a G\"{o}delian sentence: degree $\geq 1$ evidence (witnesses, thermal radiation) leaks across the boundary, but the degree-$0$ truth (the answer, the particle identity) remains formally inaccessible.

The information paradox \cite{hawking1975} asks whether information is lost or merely hidden. In the incompleteness framing, the answer is structural:

- The information exists (the section resides in $\Gamma(\mathcal{S}, A_0)$).
- It cannot be extracted by any finite computation from outside the horizon (it vanishes on $\mathcal{H}$ or $\mathcal{H}_c$).
- It can be partially witnessed via degree $\geq 1$ leakage (Hawking quanta, NP witnesses).

The information is neither "lost" nor "preserved" operationally. It is incomplete. The system is expressive enough to state the truth, but lacks the strength to derive it from the accessible side of the boundary.

**Self-reference and the necessity of horizons.**

G\"{o}del's theorem requires self-reference: the system must encode statements about itself. The QOU meets this requirement via Turing completeness; the Skein-braid encoding empowers the universe to simulate its own dynamics. Self-reference exacts a cost: any system modeling itself must contain true-but-inaccessible states. These states form the horizon.

The argument is linear:

1. The QOU is Turing-complete ($q \neq 1$ suffices: [substrate-independence of computation](#rem:substrate-computation)).
2. It can therefore encode self-referential statements (programs analysing their own Skein polynomials).
3. By G\"{o}del--Turing, degree-$0$ sections exist that no finite braid produces.
4. These sections populate the computational horizon $\mathcal{H}_c$.
5. The computational horizon is structurally identical to the jet horizon $\mathcal{H}$ ([dictionary](#rem:p-vs-np-event-horizon)).
6. Therefore, a Turing-complete universe necessarily manifests horizons.

The black hole is not an accident of general relativity: it follows from any universe expressive enough to encode arithmetic. Any universe with $q \neq 1$ — where Toffoli gates carry non-zero amplitude — must host regions where degree-$0$ truth remains inaccessible.
