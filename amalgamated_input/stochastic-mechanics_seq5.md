<!-- FILE_START: stochastic-mechanics-orphan-reconnect-intro.md -->
Blocks in this section were reconnected during the Phase 7
orphan audit.  They address supplementary stochastic-mechanics
content awaiting thematic placement.
<!-- FILE_END: stochastic-mechanics-orphan-reconnect-intro.md -->

<!-- FILE_START: lusztig-canonical-basis-q-eq-1.md -->
**Conjecture (D24 Lusztig canonical basis closure, conditional on
[`conj:kazhdan-lusztig-classical-limit`](#conj:kazhdan-lusztig-classical-limit)).**
*At the classical limit $q = 1$, the Kashiwara crystal of $H_n(q)$
([`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy),
D12 at $q \to 0$) **decategorifies** to the Lusztig canonical basis
of the group algebra $\mathbb{Z}[S_n]$.  The Kazhdan–Lusztig basis
polynomials $\{P_{y, w}(q)\}$ are the structure constants of this
decategorification, and at $q = 1$ they reduce to integer
multiplicities of canonical-basis elements.  Combined with the
$q \to 0$ Kashiwara limit (D12) and the $q \to \infty$ reverse
limit ([D13](reverse-limit-q-to-infinity.md)), D24 completes the
**Cluster D limit-duality picture** for $H_n(q)$:*

$$
  \begin{array}{c}
    q \to 0 \text{ (Kashiwara crystal)} \\
    \updownarrow \text{ bar} \\
    q \to \infty \text{ (reverse crystal, D13)} \\
    \\
    q = 1 \text{ (Lusztig canonical basis, this conjecture)} \\
    \updownarrow \text{ specialise} \\
    q = q_0 \text{ (substrate, framework production)} \\
  \end{array}
$$

## The full Cluster D limit-duality picture

| Limit | Categorical structure | Tracker row |
|-------|----------------------|-------------|
| $q = 1$ (classical) | Lusztig canonical basis / KL polynomials | **D24** (this conjecture) |
| $q = q_0$ (substrate $\approx$ 1.11) | full Hecke algebra | (production, all rows) |
| $q \to 0$ (Kashiwara) | crystal basis / 0-Hecke | D12 |
| $q \to \infty$ (reverse) | bar-image of Kashiwara | D13 |

D24 ties D12 (Kashiwara) to D1 (bar) via the decategorification
functor: the Lusztig canonical basis at $q = 1$ is the **bar-
invariant Kazhdan–Lusztig basis** of the group algebra, and the
Kashiwara crystal at $q \to 0$ is its quantum lift via canonical-
basis-preserving deformation.

## Connection to D9 (isospin) and D22 (Type-B folding)

- The isospin Z/2 swap (D9) acts on the Lusztig canonical basis as
  the **sign character** of the abelianised $S_n$ — providing a
  classical-limit picture of the canonical isospin.
- Type-B folding (D22) provides the symmetric-crystal structure
  that descends to a **bar-invariant** Lusztig basis at $q = 1$,
  closing the Cluster A (CPT) story at the decategorification
  level.

## Diagnostics

- **GB filtration**: KL polynomials are filtered by length $\ell(w)$
  — the same filtration as the Hecke algebra.
- **Jet order**: $q = 1$ specialisation; KL polynomials evaluated
  at $q = 1$ are integers (the canonical-basis multiplicities).
- **Bar-symmetry**: bar-symmetric by construction (the KL basis IS
  the bar-invariant basis).

## Open R&D

1. Explicit Kashiwara $\to$ Lusztig decategorification functor in Lean.
2. Verify the framework's canonical Wedderburn weights $y_\lambda$
   at $q = 1$ reduce to KL multiplicities.
3. D24 to closed requires Lean class for the decategorification functor;
   partial Mathlib infrastructure for Kazhdan–Lusztig theory exists.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) D24
  + §2 Cluster D (limit dualities D12 / D13 / D24)
- D12 (Kashiwara $q \to 0$):
  [`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy)
- D13 (reverse $q \to \infty$):
  [`conj:reverse-limit-q-to-infinity`](reverse-limit-q-to-infinity.md)
- D9 (isospin classical limit):
  [`conj:isospin-from-canonical-bowtie`](isospin-from-canonical-bowtie.md)
- Upstream conjecture:
  [`conj:kazhdan-lusztig-classical-limit`](#conj:kazhdan-lusztig-classical-limit)
- [Kazhdan–Lusztig 1979; Lusztig 1990; Kashiwara 1991]
<!-- FILE_END: lusztig-canonical-basis-q-eq-1.md -->

<!-- FILE_START: phi-q-aj-machinery-identification.md -->
**Proposition (conditional on [`conj:quantum-langlands-dual`](quantum-langlands-dual.md) + [`conj:dim-master-pentagon`](dim-master-pentagon.md)).**

*Let $K$ be a hyperbolic knot or link with cusp coordinates $(L, M)$ and quantum A-polynomial $\hat{A}_K \in \mathcal{A}_q$ (the q-Weyl algebra over $\mathbb{Z}[q^{\pm 1}]$). Then the $\Phi_q$ (Faddeev dilogarithm) and $\mathrm{Li}_2^q$ (Rogers dilogarithm) asymptotic regulators that appear in the framework's volume-conjecture and substrate-evaluation routes are **specific saddle-point regimes of the AJ-conjecture machinery** $\hat{A}_K \cdot J_N(K; q) = 0$. The identification is algebraic over $\mathbb{Z}[q^{\pm 1}]$ on both sides; the difference between $\Phi_q$ and $\mathrm{Li}_2^q$ contexts is the choice of archimedean saddle (real vs root-of-unity).*

## Statement

Let $K$ be a hyperbolic knot complement and $J_N(K; q) \in \mathbb{Z}[q^{\pm 1}]$ its N-colored Jones polynomial. The AJ Conjecture (Garoufalidis 2004) asserts the existence of a non-trivial q-difference operator $\hat{A}_K \in \mathcal{A}_q$ such that:

$$\hat{A}_K(\hat{L}, \hat{M}; q) \cdot J_N(K; q) \;=\; 0$$

where $\hat{M}f(M) := M\cdot f(M)$ and $\hat{L}f(M) := f(qM)$, with $\hat{L}\hat{M} = q\hat{M}\hat{L}$.

The Kashaev-Murakami-Murakami Volume Conjecture for hyperbolic $K$:

$$\lim_{N \to \infty} \frac{2\pi}{N} \log |J_N(K; e^{2\pi i / N})| \;=\; \mathrm{Vol}(K)$$

is governed in the asymptotic by the geometric component of the classical A-polynomial $A_K(L, M)$ (Garoufalidis-Lê 2015; Hikami 2003).

**The framework's identification:** the dilogarithm regulators that appear in the substrate-evaluation chain — $\Phi_q$ (Faddeev, used in the Pre-Archimedean derivation) and $\mathrm{Li}_2^q$ (Rogers, used in the categorical Schur-Weyl path) — are exactly:

- $\Phi_q$ = saddle-point regime of $\hat{A}_K \cdot J_N = 0$ at $q = e^{2\pi i / N}$ (root-of-unity asymptotic)
- $\mathrm{Li}_2^q$ = saddle-point regime of $\hat{A}_K \cdot J_N = 0$ at $q \in (0, 1)$ (real asymptotic, via Stokes)

The two regimes are related by the modular S-transform $q \leftrightarrow \tilde{q} = e^{2\pi i / \tau}$ ([`conj:modular-s-transform-q-q-tilde`](modular-s-transform-q-q-tilde.md), D14 in the duality tracker).

## Significance

The framework's [`canonical-derivation-cheat-sheet.md`](../../../docs/canonical-derivation-cheat-sheet.md) currently distinguishes $\Phi_q$ vs $\mathrm{Li}_2^q$ contexts pragmatically — using one or the other depending on which gives the cleaner expression for a given derivation. Per the AJ identification, both are the **same algebraic object** ($\hat{A}_K$) viewed through different archimedean lenses. Wiring this explicitly:

1. **Unifies the cheat-sheet's context-sorting** into a single algebraic statement.
2. **Provides the categorical-derivation target** for the rescoped Path B closure question from PR [#1231](https://github.com/litlfred/qou/pull/1231) §11: "why does the Markov-trace closed form have the coefficients it does?"
3. **Pre-Archimedean**: the AJ identity holds over $\mathbb{Z}[q^{\pm 1}]$ (no $\mathbb{R}$ or $\mathbb{C}$ needed); the framework's Pre-Archimedean / Archimedean split passes through this algebraic gate.

## Lean structure

[`phi-q-aj-machinery-identification.lean`](phi-q-aj-machinery-identification.lean) encodes this as a **conditional proposition** under §3b-cond, split explicitly into a provable backbone and conjectural class inputs.

**Proved unconditionally (sorry-free):**

- `qWeyl_commutation` — the q-Weyl relation $\hat{L}\hat{M} = q\hat{M}\hat{L}$ on the function model $\hat{M}f(m) = m \cdot f(m)$, $\hat{L}f(m) = f(qm)$.
- `Annihilates.add_smul` — the solution space of a homogeneous q-difference operator is closed under linear combinations (superposition).
- `saddle_regimes_disjoint` — the two archimedean regimes are genuinely distinct: a real $q \in (0,1)$ satisfies $q^N \neq 1$, so no parameter lies in both regimes.

**Conjectural class inputs (no instances fabricated):**

- Class `QuantumAPolynomial F K` carries the AJ conjecture's content: the operator $\hat{A}_K$ (order, coefficients, homogeneity), the colored Jones tower, the annihilation $\hat{A}_K \cdot J_N = 0$, and non-triviality.
- Class `PhiQRegulator F K` carries the Faddeev identification: the $\Phi_q$-generated saddle tower is annihilated by the same $\hat{A}_K$ in the root-of-unity regime ($q^N = 1$, $q \neq 1$).
- Class `Li2QRegulator K` carries the Rogers identification: the $\mathrm{Li}_2^q$-generated saddle tower is annihilated by the same $\hat{A}_K$ in the real regime $q \in (0,1)$ (stated over $\mathbb{R}$, the archimedean side of the wall).

**Derived conditional theorems** (they compose class fields through the proved superposition lemma — they do not project a conclusion-typed field):

- `phi_q_eq_aj_saddle_root_of_unity`: at every root-of-unity parameter, the Jones tower and the $\Phi_q$ saddle tower lie in the *same* solution space of $\hat{A}_K$ — every linear combination is annihilated.
- `li2_q_eq_aj_saddle_real`: the same at real $q \in (0,1)$ for $\mathrm{Li}_2^q$.
- `phi_q_li2_q_unified_via_aj`: the two lenses on the one algebraic object $\hat{A}_K$ are genuinely different — the regimes are disjoint (unconditional).

The classes encode literature statements (AJ conjecture, dilog-saddle identifications); the framework's contribution is the IDENTIFICATION at the algebraic-over-$\mathbb{Z}[q^{\pm 1}]$ level. The analytic half of the saddle-point statement (asymptotic growth extraction) remains part of the open class inputs.

## Conditional dependencies

**Conditional on [`conj:quantum-langlands-dual`](quantum-langlands-dual.md) + [`conj:dim-master-pentagon`](dim-master-pentagon.md)** because the full identification requires:

1. AJ conjecture proved for $K$ (proved for many: 2-bridge knots, twist knots, most Rolfsen-table knots — Lê 2006; for 𝓑_3 the question is verified open: the link version of the AJ conjecture was only formulated in 2024 with the Hopf and Whitehead links computed, and no Borromean recurrence ideal is published — see [the stage-1b literature audit](../../../docs/audits/2026-07-06-borromean-aj-literature-status.md))
2. The Faddeev / Rogers identifications used in the framework match the literature's exactly (not just up to convention)

For 𝓑_3 specifically, the algebraic side is in literature (Champanerkar 2003 for classical A-polynomials and Bloch invariants of hyperbolic 3-manifolds; Hikami for related quantum work). What's open: explicit verification that the framework's $\Phi_q$ / $\mathrm{Li}_2^q$ choices align with the AJ machinery's saddles.

**Cross-reference:** [`docs/audits/-q0-into-character-variety-minimal-archimedean.md`](../../../docs/audits/-q0-into-character-variety-minimal-archimedean.md) §9 (AJ conjecture crosses archimedean wall) for full background.

**Archimedean specialisation (§7c).** The $\Phi_q$ / $A_J$ regulator identities are stated over real $q$ with the archimedean ordering $0 < q < 1$; this real-analytic regime is the archimedean side of the substrate wall for the generic quantum-$A$-polynomial machinery, acknowledged here.
<!-- FILE_END: phi-q-aj-machinery-identification.md -->

<!-- FILE_START: reverse-limit-q-to-infinity.md -->
**Theorem (D13 reverse-limit closure — algebraic fragment).**
*The Kashiwara crystal limit $q \to 0$
([`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy), D12)
has a structural counterpart at $q \to \infty$, related to the $q
\to 0$ limit by the bar involution $q \mapsto q^{-1}$
([`def:bar-involution`](#def:bar-involution), D1).  The $q \to
\infty$ limit produces a "reverse crystal" whose combinatorial
structure is the bar-image of the Kashiwara crystal, with the
same combinatorial invariants but inverted q-character orderings.
Together, the pair $(q \to 0, q \to \infty)$ + the classical limit
$q = 1$ + the substrate $q = q_0$ form the complete picture of
limit dualities on $H_n(q)$.*

## The four canonical limits of $H_n(q)$

| Limit | Categorical content | Pairing via bar |
|-------|---------------------|-----------------|
| **$q = 1$** (classical) | Lusztig canonical basis / KL polynomials | self-paired (bar fixes $q = 1$) |
| **$q = q_0$** (substrate) | full Hecke at the framework's calibration point | bar-paired with $q = q_0^{-1}$ (NOT $q_0$ itself unless $q_0 = ±1$) |
| **$q \to 0$** (Kashiwara) | crystal basis, 0-Hecke quotient | bar-paired with $q \to \infty$ (this conjecture) |
| **$q \to \infty$** (reverse limit) | reverse crystal | bar-paired with $q \to 0$ |

This conjecture **completes** the picture by explicitly identifying
the $q \to \infty$ limit as the bar-image of the Kashiwara crystal.

## The structural content

Per [`def:bar-involution`](#def:bar-involution), $q \mapsto q^{-1}$
swaps $q = 0$ with $q = \infty$.  The Kashiwara crystal structure
at $q \to 0$ (per [`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy))
therefore has a mirror at $q \to \infty$:

- Crystal nodes $\leftrightarrow$ reverse-crystal nodes (same set)
- Crystal arrows of weight $i$ $\leftrightarrow$ reverse-crystal arrows of weight $-i$
- Plain Hecke quadratic $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ at
  $q \to 0$ becomes $\sigma_i^2 = -q^{-1}\sigma_i + 1 + O(q)$ (giving
  $\sigma_i^{-1} = \sigma_i$ on the 0-Hecke quotient) vs at
  $q \to \infty$: $\sigma_i^2 = q\sigma_i + 1 + O(q^{-1})$ (giving a
  symmetric limit on the $\infty$-Hecke quotient — the bar image)

The conjecture is that this is a **true categorical duality**, not
just a formal involution on the parameter: every Kashiwara crystal
construction has a reverse-crystal analogue at $q \to \infty$,
related by bar.

## Significance

D12 (Kashiwara $q \to 0$) is partially formalised in the framework
via [`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy).
The framework does NOT currently use the $q \to \infty$ limit
explicitly — but every Kashiwara-crystal result has a bar-paired
counterpart at $q \to \infty$ that can be derived for free.

For the matter/antimatter discussion (per AGENTS.md §7b + D22 Type-B
folding): if matter is identified with Kashiwara crystal fixed
points (at $q \to 0$), antimatter corresponds to
reverse-crystal fixed points (at $q \to \infty$), and the bar
involution swaps them. This gives a **structural source for
matter-antimatter conjugation** orthogonal to the color-tube C
action of [D6](c-from-color-flavor-swap.md).

## Diagnostics

- **GB filtration level**: same as the Kashiwara crystal at $q \to 0$
  (the bar-image preserves Coxeter length).
- **Jet order**: $h^0$ (the limit duality is at the level of the
  Hecke parameter $q$ itself, not the $h$-expansion).
- **Bar-symmetry status**: bar-paired by construction — the $q \to
  \infty$ limit IS the bar-image of the $q \to 0$ limit.

## Open R&D

1. **Author the explicit reverse-crystal construction** in Lean
   paired with `CrystalIsospinDegeneracy`.
2. **Verify** that every Kashiwara result in the framework has a
   reverse-crystal counterpart by bar — the "for free" claim
   above.
3. **Connect to matter/antimatter via D22 Type-B folding**: stable
   matter = $q \to 0$ Kashiwara fixed points; stable antimatter =
   $q \to \infty$ reverse-crystal fixed points; bar swaps them.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) D13
  + §2 Cluster D (limit dualities D12 $\leftrightarrow$ D13 $\leftrightarrow$ D24)
- Paired Kashiwara limit:
  [`prop:crystal-isospin-degeneracy`](#prop:crystal-isospin-degeneracy)
  (D12)
- Bar involution: [`def:bar-involution`](#def:bar-involution) (D1)
- Type-B folding for CPT: [`conj:type-b-folding-cpt`](type-b-folding-cpt.md) (D22)
- Lusztig canonical basis ($q = 1$): D24 (literature-only currently)
<!-- FILE_END: reverse-limit-q-to-infinity.md -->

<!-- FILE_START: outro-stochastic-mechanics.md -->
This closes the stochastic-mechanics chapter.  The Markov closure
map, $\varphi_q$ AJ machinery, Lusztig canonical basis at $q = 1$,
and reverse limit $q \to \infty$ assembled here give the
substrate-level stochastic content that the classical-limit and
information-theoretic chapters consume as input.  The reconnected
orphan blocks land the bridge between the Markov closure map and
the classical-limit construction explicitly, closing the
stochastic-mechanics narrative arc.

The next chapter (climax: volume-mass duality) extracts the
hyperbolic-volume content that pairs with the substrate-level
mass spectrum, and the chapters after that specialise the duality
to atomic isotopes and the $\beta$-decay $Q$-value predictions.
<!-- FILE_END: outro-stochastic-mechanics.md -->

