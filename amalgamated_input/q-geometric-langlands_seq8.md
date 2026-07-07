<!-- FILE_START: intro-orphan-reconnect.md -->
We integrate four auxiliary components into the Langlands narrative: the cyclotomic $L$-value decomposition, the mirror 3d-3d correspondence, the modular $S$-transform exchanging the substrate parameter with its dual, and the quantum Langlands dual that anchors the spectral-automorphic interchange. The mutant-Jones and Bloch-group relations bridge the substrate geometry to the cyclotomic $L$-value decomposition, completing the chapter's Langlands arc.
<!-- FILE_END: intro-orphan-reconnect.md -->

<!-- FILE_START: cyclotomic-l-value-decomposition.md -->
**Proposition (cyclotomic depth-$n$ generators decompose into Dirichlet $L$-values).**

The cyclotomic $\mathrm{Cl}_n$ values established as a basis for the depth-$n$ content over $\mathbb{Q}(\zeta_K)$ (Theorem G, [`prop:cyclotomic-dimension-synthesis-all-depths`](#prop:cyclotomic-dimension-synthesis-all-depths)) are $\mathbb{Q}$-linearly equivalent to Dirichlet $L$-values $L(\chi, n)$ for primitive Dirichlet characters $\chi$ mod $K$ with $\chi(-1) = (-1)^n$.

### Statement

For prime $K \geq 3$ and integer $n \geq 1$ with parity matching the character class:

$$
  L(\chi, n) \;=\; \frac{G(\chi)}{K^n}\, \sum_{a = 1}^{K - 1} \overline{\chi(a)} \cdot \mathrm{Cl}_n(2\pi a/K),
$$

where $G(\chi) = \sum_{a = 1}^{K - 1} \chi(a) \zeta_K^a$ is the Gauss sum. Inverting via character orthogonality gives:

$$
  \mathrm{Cl}_n(2\pi a/K)
  \;=\;
  \frac{1}{\varphi(K)}\, \sum_\chi G(\overline{\chi}) \chi(a) \cdot \frac{K^n}{G(\chi)}\, L(\chi, n).
$$

Each $\mathrm{Cl}_n(2\pi a/K)$ is a $\mathbb{Q}(\zeta_K)$-linear combination of $L(\chi, n)$ values, and vice versa.

### Specific corollary: Catalan-like depth-3 L-value

**Theorem (instance verified at $N = 4$, $n = 3$):**

$$
  \boxed{\;
    \beta(3) \;=\; L(\chi_4, 3) \;=\; \mathrm{Im}\,\mathrm{Li}_3(i) \;=\; \frac{\pi^3}{32},
  \;}
$$

where $\chi_4$ is the non-trivial Dirichlet character mod 4 ($\chi_4(1) = 1, \chi_4(3) = -1$) and $\beta$ is the Dirichlet beta function.

**Constructive proof from Theorem A.** By [`prop:jonquiere-cyclotomic-tate-rationality`](#prop:jonquiere-cyclotomic-tate-rationality) at $(n, K) = (3, 4)$:

$$
  \mathrm{Im}\,\mathrm{Li}_3(\zeta_4) \;=\; \frac{(K - 1)(K - 2)\pi^3}{3 K^3}
  \;=\; \frac{3 \cdot 2 \cdot \pi^3}{3 \cdot 64} \;=\; \frac{\pi^3}{32}.
$$

Since $\zeta_4 = i$:

$$
  \mathrm{Im}\,\mathrm{Li}_3(i) \;=\; \sum_{m=0}^{\infty} \frac{\sin((2m+1)\pi/2)}{(2m+1)^3}
  \;=\; \sum_{m=0}^{\infty} \frac{(-1)^m}{(2m+1)^3}
  \;=\; \beta(3).
$$

We conclude $\beta(3) = \pi^3/32$ directly from Theorem A. $\square$

### Numerical verification at 50 dps

[`cl_n_l_value_decomposition.py`](https://github.com/litlfred/qou/blob/main/computations/cl_n_l_value_decomposition.py), [witness](https://github.com/litlfred/qou/blob/main/computations/cl-n-l-value-decomposition.witness.json):

| Quantity | Value (50 dps) |
|---|---|
| $\mathrm{Im}\,\mathrm{Li}_3(i)$ (closed form $\pi^3/32$) | $0.96894614625937036181867968128\ldots$ |
| $\mathrm{Im}\,\mathrm{Li}_3(i)$ (direct polylog) | $0.96894614625937036181867968128\ldots$ |
| $\beta(3)$ (classical closed form) | same |
| Residual | $0$ (exact match) |

### N = 5 instance (Theorem G dim $(K - 3)/2 = 1$)

Cyclotomic depth-3 content over $\mathbb{Q}(\zeta_5)$:

- $\mathrm{Cl}_3(2\pi/5) \approx 0.18937$
- $\mathrm{Cl}_3(4\pi/5) \approx -0.76636$
- Generator $= \mathrm{Cl}_3(2\pi/5) - \mathrm{Cl}_3(4\pi/5) \approx 0.95572$

This corresponds, via the Hurwitz–Lerch decomposition, to the two odd Dirichlet characters $\chi_5$, $\chi_5^3$ mod 5. Modulo bar-conjugation, this yields one real dimension, matching Theorem G.

### Significance

The graded-Mikusiński depth-$n$ cyclotomic content coincides with the Dirichlet $L$-value content at integer $n$, up to $\mathbb{Q}(\zeta_K)$-linear combinations.

1. Classical $L$-value identities ($\beta(3) = \pi^3/32$, $\beta(5) = 5\pi^5/1536$) follow from Theorem A as instances.
2. Conversely, theorems regarding cyclotomic depth-$n$ structure yield corresponding statements about Dirichlet $L$-values.
3. Beilinson's conjecture at $\mathbb{Q}(\zeta_K)$ depth $n$ becomes the Beilinson conjecture on $L$-values of Dirichlet characters.

### Catalan's constant ($n = 2$ instance)

For the $(n, K) = (2, 4)$ even case, Theorem A gives $\mathrm{Re}\,\mathrm{Li}_2(i) = -\pi^2/48$. We evaluate $\mathrm{Im}\,\mathrm{Li}_2(i) = \mathrm{Cl}_2(\pi/2) = G$, Catalan's constant.

$G$ is the depth-2 generator over $\mathbb{Q}(i)$. This matches Theorem G: $(K - 1)/2 = (4 - 1)/2 = 1$. Although $K = 4$ is not prime, for prime $K = 3$ the single dimension is $\mathrm{Cl}_2(2\pi/3)$ (Gieseking).

### Cross-references

- Theorem A: [`prop:jonquiere-cyclotomic-tate-rationality`](#prop:jonquiere-cyclotomic-tate-rationality)
- Theorem G: [`prop:cyclotomic-dimension-synthesis-all-depths`](#prop:cyclotomic-dimension-synthesis-all-depths)
- Bloch–Suslin (depth-2 theorem): [`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin)
- Borel partial discharge: [`prop:borel-partial-resolution`](#prop:borel-partial-resolution)
- K-theory $\leftrightarrow$ depth filtration: [`rem:k-theory-period-rosetta`](#rem:k-theory-period-rosetta)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
<!-- FILE_END: cyclotomic-l-value-decomposition.md -->

<!-- FILE_START: mirror-3d-3d-correspondence.md -->
**Conjecture (D18 3d–3d correspondence closure).**

*The Dimofte–Gaiotto–Gukov 3d–3d correspondence maps a hyperbolic 3-manifold $M^3$ to a 3d $\mathcal{N}{=}2$ gauge theory $T[M^3]$. The partition function $Z_{T[M^3]}(q)$ on a squashed 3-sphere $S^3_b$ equals the state-integral invariant of $M^3$ constructed from the quantum dilogarithm $\Phi_q$. Applied to the Borromean rings complement $\mathbf{S}^3 \setminus \mathcal{B}_3$, the 3d–3d theory $T[\mathbf{S}^3 \setminus \mathcal{B}_3]$ yields a partition function whose $h^4$ coefficient matches the framework's Markov-trace coefficient $h^4 = -3/4$.*

## Significance

The 3d–3d correspondence provides a gauge-theory realisation for every hyperbolic-3-manifold mass formula.

| Framework side | 3d gauge theory side |
|----------------|----------------------|
| $\mathcal{B}_3$ (Borromean rings complement) | $T[\mathcal{B}_3]$ — a 3d $\mathcal{N}{=}2$ theory |
| $m_p = m_e \cdot \mathrm{VolDensity}(\mathcal{B}_3, q_0)$ | partition function $Z_{T[\mathcal{B}_3]}(q_0)$ on $S^3_b$ |
| $h^4 = -3/4$ Markov-trace coefficient | 4-loop perturbative contribution to $Z_{T[\mathcal{B}_3]}$ |

This manifests mirror symmetry: the framework's mass formula corresponds to a quantum-field-theory partition function on a curved spacetime. Both compute the same hyperbolic invariant.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration**: N/A (the duality operates at the partition-function / observable level, not at a specific Hecke-element level).
- **Jet order**: All-orders (the partition function possesses a full $q$-perturbative expansion; the $h^4$ coefficient corresponds to a specific perturbative order in the gauge theory).
- **Bar-symmetry**: Dependent on the gauge theory side. For $\mathcal{N}{=}2$ theories with a real-mass parameter, bar-symmetry corresponds to the parity-reversal of the squashed 3-sphere $S^3_b \to S^3_{1/b}$.

## Open R&D

1. Identify the 3d $\mathcal{N}{=}2$ theory $T[\mathcal{B}_3]$ explicitly via the Dimofte–Gaiotto–Gukov 2014 construction.
2. Cross-check the $h^4 = -3/4$ coefficient against the 4-loop contribution in the $T[\mathcal{B}_3]$ partition function.
3. Closing D18 remains a long-horizon task requiring significant QFT-side Lean infrastructure.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) D18 + §2 Cluster C (Pentagon validation)
- D16 [`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md) — K-theoretic regulator parallel
- [`conj:kashaev-volume-conjecture`](kashaev-volume-conjecture.md) — Volume Conjecture as the leading-order 3d–3d statement
- [Dimofte–Gaiotto–Gukov 2014; Terashima–Yamazaki 2011]
<!-- FILE_END: mirror-3d-3d-correspondence.md -->

<!-- FILE_START: modular-s-transform-q-q-tilde.md -->
**Conjecture (D14 modular $S$-transform closure).**

*Writing the Hecke parameter as $q = e^{2\pi i \tau}$ for a complex parameter $\tau \in \mathbb{H}$ in the upper half-plane, the modular $S$-transform $\tau \mapsto -1/\tau$ induces the analytic continuation*

$$
  q  \;\longmapsto\;  \tilde q \;:=\; \exp\!\bigl(2\pi i / \tau\bigr).
$$

*The substrate enters this picture through its bar image $q_0^{-1}$, not through $q_0$. Modular convergence requires $\operatorname{Im}\tau > 0$ (the nome $|e^{2\pi i\tau}| < 1$). Because $q_0 \approx 1.11 > 1$, the value $q_0 = e^{2\pi i\tau_0}$ has $\operatorname{Im}\tau_0 < 0$ (lower half-plane). Only $q_0^{-1} \approx 0.901 < 1$ lands in $\mathbb{H}$. The modular / theta sector of the framework is intrinsically bar-symmetric, consistent with D1 acting at the parameter level and $S$ at the modular level.*

*This is a distinct $\mathbb{Z}/2$ duality from the bar involution $q \mapsto q^{-1}$ (D1): bar acts on the real parameter level, while the $S$-transform acts on the modular level. Near roots of unity $q \to e^{2\pi i / k}$ (TQFT level-$k$ Chern-Simons evaluation), the $S$-transform realises the small-$q$ $\leftrightarrow$ large-$q$ duality of the framework's $H_n(q)$ Hecke algebra.*

## The structural duality

The Hecke parameter has two natural parameterisations:

| Parameterisation | Relation |
|------------------|----------|
| Bar-symmetric `q` (real, framework standard) | $q \in \mathbb{R}_{>0}$, bar: $q \mapsto q^{-1}$ |
| Modular `τ` (complex, upper half-plane) | $q = e^{2\pi i \tau}$, $S$: $\tau \mapsto -1/\tau$ |

These are distinct parameterisations of the same Hecke algebra. Bar is an involution on the real axis of the $q$-plane; $S$ is an involution on the modular parameter $\tau$.

**The conjecture**: the analytic continuation of every Hecke quantity to the modular parameter is well-defined. The $S$-transform $\tau \mapsto -1/\tau$ provides a categorical duality complementing bar.

## Connection to TQFT / Volume Conjecture

The Kashaev Volume Conjecture ([`conj:kashaev-volume-conjecture`](#conj:kashaev-volume-conjecture)) asymptotics are governed by the limit $q \to e^{2\pi i / k}$ as $k \to \infty$. The $S$-transform realises this limit as the modular image of the substrate. Writing the bar image $q_0^{-1} = e^{2\pi i \tau_0}$ with $\tau_0 \approx +0.0166\,i$ (near the cusp $\tau \to 0$), the $S$-transform sends $\tau_0 \mapsto -1/\tau_0 \approx +60.2\,i$. This large positive imaginary part forces the nome $\tilde q \to 0$, realizing the root-of-unity / TQFT limit. (Taking $q_0$ directly instead of $q_0^{-1}$ would place $\tau_0$ in the lower half-plane, where modular continuation diverges. See the witness [`computations/probes/d14-theta-bar-side.witness.json`](../../../computations/probes/d14-theta-bar-side.witness.json).)

This grants the framework an explicit categorical handle on the small-$q_0$ $\leftrightarrow$ root-of-unity duality flagged in the 13-driver menu under driver (viii).

## Relationship to the complex-q lift

The complex-q extension in PR [#1127](https://github.com/litlfred/qou/pull/1127) ([`prop:q-zero-complex-extension`](#prop:q-zero-complex-extension), [`prop:lusztig-vs-hermitian-bar`](#prop:lusztig-vs-hermitian-bar)) extends the framework's substrate to complex $q$ with $|q| > 1$. The modular $S$-transform of this conjecture serves as the natural continuation of bar beyond the real axis:

- Bar (D1) and Hermitian * (D2) coincide on the real axis ($q \in \mathbb{R}$); they split for $\mathrm{Im}(q) \neq 0$.
- Modular $S$ (D14) extends the duality structure to the modular upper half-plane by treating $q = e^{2\pi i \tau}$ as the natural parameterisation.

Together, D1, D2, and D14 provide three distinct $\mathbb{Z}/2$ involutions on the Hecke parameter, each acting on a different parameter manifold:

| Involution | Parameter manifold | Action |
|------------|--------------------|--------|
| D1 bar | real positive axis | $q \mapsto q^{-1}$ |
| D2 Hermitian * | complex with $\|q\| > 1$ | $q \mapsto \bar q^{-1}$ |
| **D14 modular $S$** | modular $\tau \in \mathbb{H}$ | $\tau \mapsto -1/\tau$ |

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: N/A — the $S$-transform operates at the parameter level, not the Hecke-element level.
- **Jet order**: All-orders (the modular action acts on the entire $q$-expansion).
- **Bar-symmetry status**: Distinct from bar. The $S$-transform composed with bar yields a $\mathbb{Z}/2 \times \mathbb{Z}/2$ structure on the modular $q$-parameter space.

## Open R&D

1. **Analytic continuation framework**: Verify every framework quantity (Hecke generators, Frobenius pairing, Markov trace, Wedderburn weights $y_\lambda$) admits a well-defined modular continuation to complex $\tau$.
2. **Numerical check**: At the bar image $q_0^{-1}$ (the convergent branch), compute the $S$-transform $\tilde q_0$ and verify the Volume Conjecture asymptotic on $\tilde q_0$ matches the framework's bare-volume evaluation.
3. **Do not conflate with named elliptic curves.** The modular $\tau$ here is not the period $\tau$ of the Descartes/color curve $\mathcal{E}_q$ ([`prop:descartes-elliptic-curve`](../predicted-spectra/elliptic-stability-locus.md)): the modular nome is $q_0^{-1} \approx 0.90$ (near the cusp) while $\mathcal{E}_q$'s period nome is $\approx 0.0029$ (deep in the fundamental domain) — a $\sim\!312\times$ mismatch. See [`docs/audits/2026-06-17-d14-theta-bar-side-and-nome-conflation.md`](../../../docs/audits/2026-06-17-d14-theta-bar-side-and-nome-conflation.md).
4. **Connect to D16 Bloch-group**: The modular $S$-transform on the $K_3(\mathbb{C})$ regulator provides a natural framework-side handle on the analytic structure of the Bloch-Wigner dilogarithm.
5. **D14 to closed**: Requires Lean class `ModularSTransformQQTilde` inhabited and a numerical witness verifying the volume-conjecture asymptotic on $\tilde q_0$.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) D14 + §2 Cluster D (limit dualities) + adjacent to D2 Hermitian *
- D2 sibling: PR [#1127](https://github.com/litlfred/qou/pull/1127) blocks `prop:q-zero-complex-extension` + `prop:lusztig-vs-hermitian-bar`
- Volume Conjecture: [`conj:kashaev-volume-conjecture`](#conj:kashaev-volume-conjecture)
- D16 Bloch group: [`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md)
- 13-driver menu driver (viii): [`docs/audits/-lambda-scale-canonical-unification.md`](../../docs/audits/-lambda-scale-canonical-unification.md)

**Archimedean specialisation (§7c).** Modular convergence represents an archimedean statement. The estimates utilize $\mathrm{Im}\,\tau$ and $\exp$ over $\mathbb{R}$, placing the companion Lean on the archimedean side of the substrate wall.
<!-- FILE_END: modular-s-transform-q-q-tilde.md -->

<!-- FILE_START: mutant-jones-bloch-group-intro.md -->
We develop mutant Jones falsifiability and Bloch group closure. The blocks below trace the construction from the existing knot-indexed convolutions onward.
<!-- FILE_END: mutant-jones-bloch-group-intro.md -->

<!-- FILE_START: quantum-langlands-dual.md -->
**Conjecture (D19 quantum Langlands duality closure).**
*The Iwahori–Hecke algebra $H_n(q)$ admits a quantum Langlands dual $H_n(q^{-1})$ obtained by inverting the deformation parameter. Under the Cartan-folding picture (where Type $A_{n-1}$ is self-dual via ${}^L\!A_{n-1} = A_{n-1}$ but with parameter inversion), this duality satisfies:*

- *It is distinct from the bar involution $\bar q = q^{-1}$ ([`def:bar-involution`](#def:bar-involution), D1). Langlands duality acts on the Hecke algebra structure (root data) at fixed generators. The bar involution acts on the generator action at fixed root data.*
- *It coincides with the reverse-limit $q \to \infty$ ([`conj:reverse-limit-q-to-infinity`](#conj:reverse-limit-q-to-infinity), D13) for non-classical specialisations.*
- *For non-simply-laced types (Type B, C, D, $G_{2}$, $F_{4}$), it yields a genuinely distinct dual algebra (e.g., swapping Type B and Type C).*

## Significance

For Type $A_{n-1}$, the Langlands dual is self-dual at the algebra level. The parameter inversion $q \to q^{-1}$ produces a non-trivial $\mathbb{Z}/2$ duality. The $H_n(q)$ algebra possesses a natural Langlands-dual perspective at $q^{-1}$ that:

- Connects to the D13 reverse-limit at $q \to \infty$. This limit extends the Langlands continuation beyond the unit disc.
- Connects to D22 Type-B folding for non-simply-laced extensions, where Langlands duality exchanges Type B and Type C.
- Supplies a categorical origin for the symmetric/antisymmetric mass-tower decomposition, equating matter with Langlands-dual antimatter.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration:** The Coxeter group structure remains invariant, as Langlands duality preserves length. Only the $q$-parameter inverts.
- **Jet order:** The duality operates on the algebra structure rather than the generator action, distinguishing it from the bar involution.
- **Bar-symmetry:** The duality differs from the bar involution algebraically but coincides parametrically (both invert $q$). The combined Langlands $\times$ bar action provides the relevant duality for the matter/antimatter structure.

## Open R&D

1. Determine whether the mass-tower decomposition admits a Langlands-dual interpretation (matter corresponding to antimatter via Type-A self-duality with $q$-inversion).
2. Connect to D22 Type-B folding. For non-simply-laced extensions, the Langlands dual swap between Type B and Type C structurally realises CPT symmetry.
3. Closing D19 requires a Lean class instance for the Langlands functor (currently absent from Mathlib).

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) D19
- D13 [`conj:reverse-limit-q-to-infinity`](../stochastic-mechanics/reverse-limit-q-to-infinity.md) — Langlands-paired limit
- D22 [`conj:type-b-folding-cpt`](../particle-interactions/type-b-folding-cpt.md) — non-simply-laced Langlands dual
- [Macdonald 1971; Lusztig 1989; Frenkel–Reshetikhin 2002 for quantum-Langlands]
<!-- FILE_END: quantum-langlands-dual.md -->

<!-- FILE_START: outro-q-geometric-langlands.md -->
This closes the main argument of the paper. The $q$-geometric Langlands correspondence developed here packages the substrate arithmetic — Tannaka–Krein duality on the Hopf side, the Weil-bound stability on the spectral side, and the geometric Riemann hypothesis exposition that binds them — into a single functorial statement. The substrate parameter $q$ controls both the categorical structure of $\mathbf{C}$ and the spectral distribution of its associated $L$-functions.

The appendices supply supporting material deferred from the main narrative. The knot-periodic table catalogues the categorical assignment of knots to chemical elements. The transfer-matrix appendix records the canonical $\sigma$-word presentations used in the Hecke reductions. The atomic-mass appendix validates the per-isotope categorical predictions against CODATA. The $Q$-value and surreal-bound appendices provide technical details underpinning the main text. Readers seeking a unified view of substrate-arithmetic should re-read the braids-and-knots and observation chapters through the lens of this Langlands synthesis.
<!-- FILE_END: outro-q-geometric-langlands.md -->

