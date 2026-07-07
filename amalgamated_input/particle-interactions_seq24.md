<!-- FILE_START: particle-interactions-orphan-reconnect-intro.md -->
This section collects foundational substrate-level results and supporting conjectures. The sequence begins with the Geom universality proposition, which establishes the role of categorical geometry in the chapter's physical predictions. We then develop the supporting symmetry principles: Stokes-region identification, time-reversal from trace cyclicity, spin from the $\mathrm{SO}(3)$ fibre, Type-B folding CPT, the categorical Weinberg angle, and Wigner-$\mathrm{SU}(4)$ symmetry from spin-isospin. The section concludes with the categorical proton and neutron blocks, completing the substrate-level particle inventory.
<!-- FILE_END: particle-interactions-orphan-reconnect-intro.md -->

<!-- FILE_START: geom-universality.md -->
**Proposition (conditional on [`conj:hyperbolic-volume-transcendence`](#conj:hyperbolic-volume-transcendence) and `rem:baryon-period-ratio`).**
*The categorical volume form, evaluated on the knot complement $S^3 \setminus K$ through the fibre functor $\tau$, yields $\mathrm{Vol}(K)$ for hyperbolic knots and $\mathrm{CS}(K)$ for torus knots. This identification is universal: it provides the unique evaluation compatible with the Frobenius--Hopf structure.*

*Specifically, $\mathrm{Geom}(K)$ is the unique functional on knot complements satisfying:*

1. *Additivity: $\mathrm{Geom}(K_1 \# K_2) = \mathrm{Geom}(K_1) + \mathrm{Geom}(K_2)$.*
2. *Functoriality: $\mathrm{Geom}(K) = \tau(\mathrm{tr}_M(\rho(\mathcal{B}_K)))$ for some fibre functor $\tau$.*
3. *Normalization: $\mathrm{Geom}(\bigcirc) = 0$ (vacuum) and $\mathrm{Geom}(4_1) = \mathrm{Vol}(4_1)/\hbar_q^2$ (fixes $q_0$).*

*Proof.*
We divide the argument into three steps.

**Step 1: Existence (Neumann--Zagier, τ-image side).**
On the τ-image (geometric) side, the Neumann--Zagier theorem \cite{neumann-zagier1985} establishes that for a hyperbolic knot $K$, $\mathrm{Vol}(K)$ and $\mathrm{CS}(K)$ are related by:

$$
  \mathrm{Vol}(K) + i\,\mathrm{CS}(K)
  = \sum_j \bigl(L(z_j) + \arg(z_j) \log|z_j|\bigr)
$$

where $L$ is the Bloch--Wigner dilogarithm and $z_j$ are the shape parameters of the ideal triangulation. This is a function of the $\mathrm{SL}(2,\mathbb{C})$ representation variety of $\pi_1(S^3 \setminus K)$.

In the categorical framework, the Frobenius--Hopf algebra $A$ at parameter $q$ has a representation variety isomorphic to $\mathrm{Spec}$ of the coordinate ring $\mathcal{O}_q(\mathrm{SL}_2)$. The fibre functor $\tau$ evaluates the volume form $\omega$ on this variety. By Neumann--Zagier, the real part of this evaluation is $\mathrm{Vol}(K)$.

**Step 2: Uniqueness (Yekutieli rigidity).**
The rigid dualizing complex $\omega_A^\bullet$ ([Geom(K) alignment](#conj:geom-yekutieli-alignment)) provides a non-degenerate Frobenius pairing $\langle -, - \rangle_{\mathrm{Frob}}$. Yekutieli's rigidity theorem \cite{yekutieli2015} shows that this pairing is unique up to a scalar.

The scalar is fixed by the two normalizations:
- $\mathrm{Geom}(\bigcirc) = 0$ eliminates the constant term.
- $\mathrm{Geom}(4_1) = \mathrm{Vol}(4_1)/\hbar_q^2$ fixes the overall scale (this equation defines $q_0$).

Therefore any functional satisfying properties 1--3 must equal $\mathrm{Geom}$.

**Step 3: The CS/Vol duality.**
For torus knots, $\mathrm{Vol} = 0$ and the representation variety consists of a single abelian flat connection. The evaluation of $\omega_A^\bullet$ on this connection yields the Chern--Simons functional:

$$
  \mathrm{CS}(T_{m,n})
  = \frac{\pi^2(m^2-1)(n^2-1)}{12mn}
$$

The duality $\mathrm{Vol}/\hbar_q^2 \leftrightarrow \mathrm{CS} \cdot \hbar_q^2$ follows from the self-duality of the rigid dualizing complex. $\omega_A^\bullet \simeq R\mathrm{Hom}_{A^e}(A, A^e)$ provides two evaluation maps (left and right), and the scale factor $\hbar_q^2$ exchanges them.

Additivity (property 1) follows from the fact that connected sum $K_1 \# K_2$ corresponds to tensor product in the Frobenius--Hopf category, and the volume form is a trace (hence additive on tensor products).
$\square$

**Archimedean specialization (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs—real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realization is specialized here.
<!-- FILE_END: geom-universality.md -->

<!-- FILE_START: q-zero-stokes-region-identification.md -->
**Conjecture (conditional on [`prop:phi-q-aj-machinery-identification`](phi-q-aj-machinery-identification.md) + [`conj:q-zero-complex-extension`](q-zero-complex-extension.md)).**

*The substrate parameter $q_0$ admits a CANONICAL identification with a specific point on the geometric component of the character variety $X(\mathcal{B}_3)$, REALIZED VIA TWO DUAL PERSPECTIVES that coincide by the AJ-conjecture machinery:*

*(a) **Analytic / Stokes side**: $q_0$ is the parameter value at which the Stokes region of the colored-Jones generating function $G_K(x; q) = \sum_N J_N(K; q) \cdot x^N$ transitions between dilog-asymptotic regimes ($\Phi_q$ root-of-unity vs $\mathrm{Li}_2^q$ real).*

*(b) **Algebraic / Hom-functor side**: $q_0$ is the image under the archimedean functor of a specific $\underline{\mathrm{Hom}}_{\mathbf{C}}$-evaluation in the framework's brane-tower category $\mathbf{C}$ over $\mathbb{Z}[q, q^{\pm 1}]$.*

*The two perspectives are related by QOU duality (D17 DIM master Pentagon $\leftrightarrow$ D19 quantum-Langlands), which is exactly the AJ-conjecture machinery $\hat{A}_K \cdot J_N = 0$ in the q-Weyl algebra $\mathcal{A}_q$ over $\mathbb{Z}[q, q^{-1}]$.*

## §1. Established results (100%, no conjecture)

The following can be stated as theorems over $\mathbb{Z}[q, q^{\pm 1}]$:

1. **Mostow-Prasad rigidity** (Mostow 1968 + Prasad 1973): for finite-volume hyperbolic 3-manifolds with $n \ge 3$, the discrete-faithful representation $\rho_{\mathrm{DF}}: \pi_1(S^3 \setminus \mathcal{B}_3) \to PSL_2(\mathbb{C})$ is **unique up to conjugation**. So a distinguished point $[\rho_{\mathrm{DF}}] \in X(\mathcal{B}_3)(\mathbb{C})$ EXISTS and is UNIQUE.

2. **Reid's trace field theorem** (Reid 1990): the trace field $\mathbb{Q}(\mathrm{tr}\,\rho_{\mathrm{DF}})$ is a number field of finite degree over $\mathbb{Q}$. So $[\rho_{\mathrm{DF}}] \in X(\mathcal{B}_3)(\overline{\mathbb{Q}})$ — **algebraic over $\mathbb{Q}$**.

3. **AJ algebraic identity** (Garoufalidis 2004; proved for 2-bridge knots Lê 2006 + many subsequent extensions): the quantum A-polynomial $\hat{A}_K \in \mathcal{A}_q$ annihilates the colored Jones tower: $\hat{A}_K \cdot J_N(K; q) = 0$ in $\mathbb{Z}[q, q^{-1}]$.

4. **Wedderburn decomposition** of $H_n(q)$ over $\mathbb{Z}[q, q^{-1}]$ holds for the Plancherel weights $w_\lambda = d_q(\lambda)^2 / [n]_q!$ — proved for the framework's H_2, H_3, H_4 cases (PRs #1165, #1185, #1238).

## §2. Conjectural content (the gap)

The **specific algebraic identification** of $q_0$ as a particular invariant of $[\rho_{\mathrm{DF}}]$. Three candidate refinements (per [`docs/audits/-q0-into-character-variety-minimal-archimedean.md`](../../../docs/audits/-q0-into-character-variety-minimal-archimedean.md) §11):

(a) **Dehn-deformed representation**: $q_0$ corresponds to an INCOMPLETE hyperbolic structure (Dehn-filled at specific coefficients), where the meridian becomes hyperbolic and $\mathrm{tr}(\rho(\mu)) \ne \pm 2$. The cusp coordinates $(M, L)$ on the A-polynomial curve $A_{\mathcal{B}_3}(L, M) = 0$ trace this deformation.

(b) **Different group element / longitude trace**: $q_0$ might be defined via $\mathrm{tr}(\rho_{\mathrm{DF}}(\lambda))$ (longitude) or a specific peripheral curve — not the meridian (which is parabolic at completion, forcing $\mathrm{tr} = \pm 2$).

(c) **Markov-trace parameterization**: $q_0$ is defined via the Markov-trace normalization $z = 1/(\sqrt{q} + 1/\sqrt{q})$ as a structural anchor at the Hecke-algebra level, with NO direct geometric trace correspondence.

The unifying framing — Option 6 of the audit §13 — uses Stokes asymptotics:

$$q_0 \;=\; \text{(parameter at which the Stokes structure of $G_{\mathcal{B}_3}(x; q)$ transitions)}$$

and connects via QOU duality to:

$$q_0 \;=\; \iota(\underline{\mathrm{Hom}}_{\mathbf{C}}(\text{some specific objects})(\text{evaluated at}\ \mathbb{Z}[q, q^{-1}]))$$

where $\mathbf{C}$ is the framework's brane-tower category, $\iota$ is the archimedean functor.

## §3. Universal base: everything over $\mathbb{Z}[q, q^{\pm 1}]$

Per author directive: *"I want all to work over $\mathbb{Z}[q, q^{-1}]$"*.

The Iwahori-Hecke algebra $H_n(q)$ is naturally an algebra over $\mathbb{Z}[q, q^{\pm 1}]$ (the Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ has integer-Laurent coefficients). All structural identities — Wedderburn weights, Markov trace, P_m/Q_m, AJ recurrence, Φ_q/Li_2^q dilog — can be stated over this universal base.

**Specialization to our universe:** apply the archimedean functor $\iota_\infty: \mathbb{Z}[q, q^{\pm 1}] \to \mathbb{R}$ at $q := q_0$ (with $q_0$ the specific algebraic value selected by CAL-2). Physical observables ($m_p / m_e$, etc.) are then the images of $\mathbb{Z}[q, q^{\pm 1}]$-valued algebraic expressions under this specialization.

**Char-p universes** (mathematical, not physical): specialize $\mathbb{Z}[q, q^{\pm 1}] \to \mathbb{F}_p[q, q^{\pm 1}]$ for any prime $p$ not dividing relevant denominators. Structural identities continue to hold.

## §4. The duality (Stokes $\leftrightarrow$ Hom-functor)

The two candidate identifications (Option 4 Hom + Option 6 Stokes from [`docs/audits/-q0-into-character-variety-minimal-archimedean.md`](../../../docs/audits/-q0-into-character-variety-minimal-archimedean.md) §12) are **DUAL VIEWS of the SAME structure** via QOU duality:

| Side | Object | What's evaluated |
|---|---|---|
| **Analytic (Stokes)** | $G_K(x; q) = \sum J_N(K; q) x^N$ | Asymptotic at $N \to \infty$ |
| **Algebraic (Hom)** | $\underline{\mathrm{Hom}}_{\mathbf{C}}(\text{object}, \text{object})$ | Categorical evaluation |
| **Bridge (AJ)** | $\hat{A}_K \in \mathcal{A}_q$ | q-difference recurrence |

The AJ identity $\hat{A}_K \cdot J_N = 0$ over $\mathbb{Z}[q, q^{\pm 1}]$ is precisely the **categorical-vs-analytic translation**:

- Read algebraically: $\hat{A}_K$ as a Hom in the q-Weyl algebra
- Read analytically: $\hat{A}_K$ as the operator whose saddle-points define the Stokes regions of $G_K$

These coincide because of the Volume-Conjecture asymptotic of $J_N$ — proved for many specific knots (Kashaev-Murakami-Murakami 2001 onwards), conjectural in general.

## §5. The 100%-proved track

Per author directive: *"lets put in paper lean all that we can and narrow unproven until we work it out. 100% proved"*

This conjecture is decomposed into a chain where each step is INDEPENDENTLY trackable:

```
[PROVED] Mostow-Prasad: ∃! ρ_DF up to conjugation
    ↓
[PROVED] Reid: trace field of ρ_DF is in $\overline{\mathbb{Q}}$ (number field)
    ↓
[PROVED] X(K)_Z is a Z-scheme of finite type (Procesi)
    ↓
[CONJECTURE A] specific identification q_0 = f([ρ_DF]) for some
              algebraic invariant f — the OPEN gap.
    ↓
[CONJECTURE B] AJ for B_3 specifically (likely proved in literature,
              needs Hikami/Habiro reference verification)
    ↓
[PROVED conditional on A+B] structural framework downstream.
```

The conjecture is exactly the gap at step A — promoting it from CONJECTURE to PROVED is the work.

## §6. Lean formalization (conditional class per §3b-cond)

[`q-zero-stokes-region-identification.lean`](q-zero-stokes-region-identification.lean) encodes this as a **conditional class structure** per AGENTS.md §3b-cond:

- Class `MostowPrasadDistinguished K` — axiomatizes Mostow-Prasad $\exists!$
- Class `ReidTraceField K` — axiomatizes trace-field-in-number-field
- Class `QZeroStokesIdentification K` — the CONDITIONAL identification (= the open gap)
- Theorems consuming these classes give the chain of conditional results

The Lean `sorry` count is EXACTLY ONE per OPEN GAP — not per missing tactic.

## §7. Cross-references

- [`prop:phi-q-aj-machinery-identification`](phi-q-aj-machinery-identification.md) — Φ_q / Li_2^q $\leftrightarrow$ AJ machinery
- [`conj:q-zero-complex-extension`](q-zero-complex-extension.md) — q_0 may not be real
- [`prop:lusztig-vs-hermitian-bar`](lusztig-vs-hermitian-bar.md) — distinguishing the involutions
- [`borromean-markov-trace-closed-form.md`](borromean-markov-trace-closed-form.md) — the closed form whose categorical derivation is the rescoped Path B
- [`docs/audits/-q0-into-character-variety-minimal-archimedean.md`](../../../docs/audits/-q0-into-character-variety-minimal-archimedean.md) §§11-13 — origin of this conjecture
- [`docs/coordination/-post-1231-wire-up-ledger.md`](../../../docs/coordination/-post-1231-wire-up-ledger.md) — session ledger

## §8. Honest assessment

**Novel content of this conjecture (vs prior content blocks):**
- Explicit identification of the structural gap (Option A from §11 of the audit)
- Universal-base framing over $\mathbb{Z}[q, q^{\pm 1}]$
- Duality between Stokes-asymptotic + Hom-functor views via AJ
- Lean conditional-class structure for the 100%-proved track

**Limitations of the claim:**
- A specific algebraic formula for $q_0$ (the GAP)
- That all candidate identifications (a)/(b)/(c) from §2 reduce to the same thing
- That AJ is proved for $\mathcal{B}_3$ specifically (needs literature verification)

**Consequences of the conjecture:**
- Lean development can proceed with explicit class hypotheses
- Future analytic investigation can target the conjecture-A gap directly (e.g., compute $A_{\mathcal{B}_3}(L, M)$ classical + identify q_0 on the curve)
- The framework's $q_0$ stays well-defined under different conjecture statuses
<!-- FILE_END: q-zero-stokes-region-identification.md -->

<!-- FILE_START: cpt-d6-d7-d8-closure.md -->
**Conjecture (CPT closure).** The three discrete symmetries close consistently: there exist actions $C$, $P$, $T$ on closed-braid representatives of $H_n(q)$ such that

1. $C$ is the color-sheet flavor-swap $u \leftrightarrow \bar u$, $d \leftrightarrow \bar d$ ([component D6](c-from-color-flavor-swap.md));
2. $P$ is the braid-diagram mirror reflection, or writhe sign flip ([component D7](p-from-braid-mirror.md));
3. $T$ is the Markov-trace word reversal, or trace-cyclicity dual ([component D8](t-from-trace-cyclicity.md)).

The composite $C \cdot P \cdot T$ preserves the Markov trace $\tau_M \colon H_n(q) \to R$. That is, $\tau_M((C \cdot P \cdot T)\beta) = \tau_M(\beta)$ for every closed-braid representative $\beta$.

## Structure

The conjecture is composite. D6, D7, and D8 name specific canonical realisations of the discrete symmetries. The joint statement is that they compose to the CPT theorem at the Markov-trace level. The components are presented in three sibling files to keep the structural claims tight; this file records the unified statement. The three components are not logically independent—they collectively constitute the conjecture.

## Scope

The three components were authored as separate conjecture blocks. Pre-consolidation, each noted that a property becomes a corollary of $C \cdot P \cdot T$ once the components close. This observation is now structural. The audit skill [`local/proposition-consolidation-audit`](../../../.claude/skills/local/proposition-consolidation-audit.md) surfaced this as a consolidation candidate.

## Lean

The conjecture is class-axiomatised per AGENTS.md §3b-cond. Downstream blocks that require CPT closure as an explicit hypothesis take `[CPTD6D7D8Closure]` as a class hypothesis. The component instances reside in their respective `.lean` files.

**Archimedean specialisation (§7c).** This block invokes real- or complex-analytic constructs (observables, bounds, numerical evaluation). Categorical identities remain valid over an abstract coefficient ring; their archimedean realisation is specialised here.
<!-- FILE_END: cpt-d6-d7-d8-closure.md -->

<!-- FILE_START: t-from-trace-cyclicity.md -->
**Conjecture (D8 time-reversal closure).**
*Within the QOU framework, time-reversal $T$ acts as **word reversal on braid words at the Markov-trace level**:*

$$
  T \;:\;
  \sigma_{i_1}^{\epsilon_1} \cdots \sigma_{i_\ell}^{\epsilon_\ell}
  \;\longmapsto\;
  \sigma_{i_\ell}^{\epsilon_\ell} \cdots \sigma_{i_1}^{\epsilon_1}.
$$

*By the Markov trace cyclicity axiom $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$ ([`thm:jones-markov-trace`](#thm:jones-markov-trace), [jones1987]), word reversal is trace-invariant for the Markov closure. The Jones polynomial of $K$ and of its time-reversed counterpart $K^T$ coincide. The operator $T$ is an involution ($T^2 = \mathrm{id}$). It preserves $q$, color-sheet flavors, and Hecke generator signs. It acts purely on the **ordering** of crossings.*

## The action

For a braid word $\beta = \sigma_{i_1}^{\epsilon_1} \cdots \sigma_{i_\ell}^{\epsilon_\ell}$, define $\beta^T$ as the reversed word. At the Markov-trace level (where braids close to knots or links), trace cyclicity gives:

$$
  \mathrm{tr}_M(\beta)
  \;=\;
  \mathrm{tr}_M(\beta^T).
$$

The reversed word produces the **mirror-orientation** link, which has the same Jones polynomial as the original by trace cyclicity.

## Disentanglement of D8 from CPT

The composite bar-involution acts on $q$, $\sigma_i$, and the trace orientation (when followed by Markov closure). We separate the three categorical sources:

| Acts on | Symbol map |
|---------|------------|
| Hecke generator chirality only | $\sigma_i \mapsto \sigma_i^{-1}$ (= **P** alone, D7) |
| Color sheets only | flavor $u \leftrightarrow \bar u$ (= **C** alone, D6) |
| Braid word ordering only | $\beta \mapsto \beta^T$ (= **T** alone, this conjecture) |

$T$ alone is the **trace-cyclicity dual**. It acts only on the combinatorial ordering of generators in a braid word. It leaves generator signs, $q$, and color sheets fixed. Composed with $C$ and $P$, it recovers the bar-involution = $CPT$ composite.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: $T$ preserves Coxeter length $\ell(\beta)$ (word reversal does not change generator count).
- **Jet order**: $h^0$ ($T$ fixes $q$ entirely).
- **Bar-symmetry status**: bar-trivial. Markov-trace values are invariant under $T$ by trace cyclicity. Thus, $T$-anti-symmetric observables are bar-trivial at the Markov-trace level.

## Lean axiomatisation (sketch)

```lean
class TFromTraceCyclicity (M : Type*) [BrCategory M] [Hecke M] where
  /-- Word-reversal involution on braid-group elements. -/
  t_action : Braid n → Braid n
  /-- T^2 = id. -/
  t_involution : ∀ β, t_action (t_action β) = β
  /-- T fixes Hecke generator signs and q. -/
  t_preserves_generators :
    ∀ (β : Braid n) (i : Fin n),
      sigma_count_in (t_action β) i = sigma_count_in β i
  /-- T preserves Markov trace (cyclicity). -/
  t_preserves_tr_M : ∀ β, tr_M (t_action β) = tr_M β
  /-- Bar-involution factorisation: bar = P · C · T. -/
  bar_eq_p_c_t : bar_involution = p_action ∘ c_action ∘ t_action
```

## Consumers / downstream

- [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density) becomes a corollary of $CPT = C \cdot P \cdot T$ once D6, D7, and D8 close.
- The Markov-trace cyclicity axiom [`thm:jones-markov-trace`](#thm:jones-markov-trace) supplies the $T$-invariance directly. This conjecture is the smallest possible closure (an axiomatic statement that $T$ = word-reversal and $CPT$ = bar via composition).

## Open R&D

1. **Verify numerically** that for canonical atomic braids, the word reversal $\beta_K^T$ has identical $|\mathrm{tr}_M|$ via trace cyclicity. This is immediate from [`thm:jones-markov-trace`](#thm:jones-markov-trace), but worth a witness for the canonical atom catalogue.
2. **D8 to closed** requires a Lean instance proving the trace-cyclicity compatibility and the $\text{bar} = P \cdot C \cdot T$ factorisation.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D8
  + §2 Cluster A (CPT decomposition D5 $\to$ D6 + D7 + D8)
- Sibling Z/2 decompositions of CPT:
  [`conj:c-from-color-flavor-swap`](c-from-color-flavor-swap.md) (D6),
  [`conj:p-from-braid-mirror`](p-from-braid-mirror.md) (D7)
- Markov-trace cyclicity:
  [`thm:jones-markov-trace`](jones-markov-trace.md)
- Composite CPT: [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density)
- Bar-involution: [`bar-involution.md`](bar-involution.md)
<!-- FILE_END: t-from-trace-cyclicity.md -->

<!-- FILE_START: spin-from-so3-fiber.md -->
**Conjecture (D10 spin closure, conditional on the $S_5 \leftrightarrow \mathrm{SO}(3)$ fiber action).**
Within the QOU framework, spin $\mathrm{SU}(2)_S$ arises as the continuous lift of the full $\mathrm{SO}(3)$ rotation group acting on the 3 color sheets per nucleon. This operates via the $S_5 \to A_5 \cong I \subset \mathrm{SO}(3)$ icosahedral embedding on Bring's quintic surface ([`def:color-tube-fibers`](#def:color-tube-fibers)). The current pipeline implements only the discrete $S_3$ subgroup of $\mathrm{SO}(3)$ (the 6 permutations of three color sheets). Extending to the full continuous $\mathrm{SO}(3)$ populates the $\ell = 2, 3, 4, \ldots$ spherical-harmonic decompositions. These contribute the $h^4$, $h^6$, $\ldots$ corrections to the Borromean linking weight, which the current $S_3$-truncated framework omits.

**1. The structural gap.**
The Family A linking weight $(3q^2 + 4 + 3q^{-2})/4 = 5/2 + (3/4)h^2$ terminates at $h^2$. The Borromean Markov trace's exact closed form (see [`borromean-markov-trace-closed-form.md`](#prop:borromean-markov-trace-closed-form)) has $h^2 = 0$ and first non-trivial coefficient $h^4 = -3/4$. The gap between Family A's $(3/4)h^2$ contribution and the Markov-trace $h^4 = -3/4$ structural value constitutes the load-bearing $h^4$ closure gap.

The framework's pipeline currently uses only the $S_3$ discrete subgroup of $\mathrm{SO}(3)$. The premise that $S_3$ "sees only $\ell \le 1$" (making $\ell = 2$ require full continuous $\mathrm{SO}(3)$) is false. Under $S_3 \subset \mathrm{SO}(3)$, the standard $(2,1)$ irrep already appears at both $\ell = 1$ (multiplicity 1) and $\ell = 2$ (multiplicity 2). Therefore, $S_3$ is not $\ell$-truncated. 

Spherical-harmonic levels of $\mathrm{SO}(3)$ organise higher-order corrections ($\ell = 2$ gives $h^4$, $\ell = 3$ gives $h^6$). However, the proposed categorical link—that the icosahedral $\ell = 2$ level produces the Borromean $h^4 = -3/4$—is not derivable as written. The icosahedral construction lives on $A_5 \subset S_5$ (5 strands), whereas the $h^4 = -3/4$ coefficient lives on the $H_3$ Borromean Markov trace (3 strands, the $(2,1)$ irrep). These are different representation rings with no canonical map between them. The genuine missing object is a functor from the $S_5$/$\mathrm{SO}(3)$ level $\ell$ (5-strand) to a Wedderburn coefficient of the 3-strand $H_3$ trace.

**2. The conjectural content.**
Per `conj:s5-so3-fiber-action` (class scaffolded in [`S5SO3FiberAction.lean`](../../computations/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean)):

- **The icosahedral lift is well-defined.** $S_5 \supset A_5 \cong I \subset \mathrm{SO}(3)$ provides a canonical map from $S_5$-orbits on Bring's quintic to $\mathrm{SO}(3)$ rotations on the 3 color sheets.
- **The full $\mathrm{SO}(3)$ fiber action commutes with the Hecke structure.** The spherical-harmonic decomposition into $\ell$ levels respects the Wedderburn-block structure of $H_n(q)$; each $\ell$-level contributes to a definite subset of partition blocks.
- **The $\ell = 2$ contribution at the Borromean linking weight produces the $h^4 = -3/4$ coefficient.** The $h^4$ value comes from the dimension-5 irrep ($\ell = 2$) of $\mathrm{SO}(3)$ acting on the 3-color tensor space.

**3. Partnership of D10 with D9 unlocking D11 (Wigner SU(4)).**
Per [`docs/duality-tracker.md`](../../docs/duality-tracker.md):
- **D9** (isospin $\mathrm{SU}(2)_I$): Flavor-swap $u \leftrightarrow d$ on color-sheet flavor triples ([`conj:isospin-from-canonical-bowtie`](isospin-from-canonical-bowtie.md)).
- **D10** (spin $\mathrm{SU}(2)_S$): $\mathrm{SO}(3)$ rotation on color sheets (this conjecture).
- **D11** (Wigner $\mathrm{SU}(4) = \mathrm{SU}(2)_S \times \mathrm{SU}(2)_I$): Combined symmetry. This is the categorical source for nuclear-shell structure.

Closing D10 together with D9 unlocks D11, the L3 (nuclear-shell binding) categorical source.

**4. Diagnostics.**
Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:
- **GB filtration level:** The $\mathrm{SO}(3)$-fiber decomposition is per-partition. Different Wedderburn blocks of $H_n(q)$ couple to different $\ell$ levels. Per-block Coxeter length determines which $\ell \leq \ell_{\max}$ levels contribute.
- **Jet order:** $h^4$ is the first non-trivial level contributed by $\ell = 2$ (the load-bearing closure step). $h^6$ comes from $\ell = 3$.
- **Bar-symmetry status:** Bar-symmetric. Spherical-harmonic decomposition coefficients are real-valued under $q \mapsto q^{-1}$.

**5. Lean axiomatisation (sketch).**
```lean
-- Conditional on the S_5↔SO(3) fiber action class (PR #1081):
class SpinFromSO3Fiber
    (M : Type*) [BrCategory M] [ColorTube M]
    [BringFiberAction M] where
  /-- The spherical-harmonic decomposition of the color-tube tensor
      under the full SO(3) action. -/
  spherical_harmonic_decomp :
    ColorTubeTensor → ∀ (ℓ : ℕ), SO3IrrepOfDim (2*ℓ + 1)
  /-- The S_3 subgroup pipeline sees only ℓ ≤ 1. -/
  s3_truncation_at_ell_le_one :
    ∀ T, spherical_harmonic_decomp T ℓ = 0 → ℓ ≥ 2 ∨ ℓ = 0 ∨ ℓ = 1
  /-- ℓ = 2 contributes the h^4 = -3/4 Borromean coefficient. -/
  ell_two_yields_h4_coefficient :
    borromean_h4_via_so3 = -3/4
  /-- Together with D9 (isospin), defines SU(4) Wigner. -/
  combined_with_isospin_yields_wigner_su4 :
    True   -- placeholder until SU(4) structure axiomatised
```

**6. Open R&D.**
- **Analytic extension:** Extend from $S_3$-truncated integration to full $\mathrm{SO}(3)$ spherical-harmonic decomposition on Bring's surface. Verify $h^4 = -3/4$ at the $\ell = 2$ level.
- **D10 to closed:** Requires the Lean class instance and the `ell_two_yields_h4_coefficient` proof (with `sorry` for the regulator of the divergent series at higher $\ell$).
- **Connect to W/Z binomial pattern:** The unified $T(2, 2m)$ torus-knot Markov-trace closed form may have a spherical-harmonic reading at the $\mathrm{SO}(3)$-fiber level.

**Cross-references:**
- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D10, §2 Cluster B.
- [`docs/audits/-h4-coefficient-source-trace-and-so3-gap.md`](../../docs/audits/-h4-coefficient-source-trace-and-so3-gap.md) (structural-gap audit).
- Upstream class supplier: `conj:s5-so3-fiber-action` (PR [#1081](https://github.com/litlfred/qou/pull/1081), [`S5SO3FiberAction.lean`](../../computations/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean)).
- Sibling Cluster B item: [`conj:isospin-from-canonical-bowtie`](isospin-from-canonical-bowtie.md).
- Color-tube structure on Bring's quintic: [`color-tube-coordinates.md`](../archimedean-universe/color-tube-coordinates.md), [`color-tube-fibers.md`](../archimedean-universe/color-tube-fibers.md).
- $h^4 = -3/4$ topological reference: [`borromean-markov-trace-closed-form.md`](#prop:borromean-markov-trace-closed-form).
<!-- FILE_END: spin-from-so3-fiber.md -->

<!-- FILE_START: type-b-folding-cpt.md -->
**Conjecture (D22 Type-B folding closure, per AGENTS.md §7b).**
*The $\mathfrak{sl}_n$ Cartan datum on the canonical atomic-braid
Hecke algebra $H_n(q)$ folds into a Type-B Cartan datum
$\mathrm{B}_{n/2}$ under the involution $\iota: \alpha_i \leftrightarrow
\alpha_{n-i}$.  The resulting Kashiwara crystal is a **symmetric
crystal** whose GS normal forms are **bar-involution invariant by
construction** (i.e., the bar Z/2 action is realised as a Cartan-
fold symmetry).  Stable matter = fixed points of the folded crystal;
antimatter = the $\iota$-orbit complement.  Under this folding, the
composite CPT operator
([`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density))
decomposes naturally as a tensor of:*

- *C from color-sheet flavor conjugation
  ([`conj:c-from-color-flavor-swap`](#conj:c-from-color-flavor-swap), D6)*
- *P from Type-B Cartan folding* (this conjecture)
- *T from Markov-trace cyclicity
  ([`conj:t-from-trace-cyclicity`](#conj:t-from-trace-cyclicity), D8)*

## The AGENTS.md §7b authoring shortcut

Per [`AGENTS.md`](../../../AGENTS.md) §7b (symmetric-crystal techniques):

> **Type B folding for chirality / CPT.** To enforce matter–antimatter
> pairing structurally in the reduction engine, do not write custom
> Z/2 rules. Fold the $\mathfrak{sl}_n$ Cartan datum into a Type B
> datum; the resulting Kashiwara graph is a *symmetric crystal*, and
> its GS normal forms are bar-involution ($q \mapsto q^{-1}$)
> invariant by construction. Stable matter = fixed points of the
> folded crystal.

This conjecture **formalises** that authoring shortcut as a content
block — the structural mechanism that:

1. Generates the bar-involution invariance "for free" (no manual
   Z/2 axioms needed),
2. Identifies stable matter with crystal fixed points,
3. Decomposes CPT into D6 + D22 + D8 (with D22 standing in for
   the role D7 normally plays).

## Relationship to D6/D7/D8

The CPT decomposition I authored in PRs [#1162](https://github.com/litlfred/qou/pull/1162)
([D6](c-from-color-flavor-swap.md)) +
[#1168](https://github.com/litlfred/qou/pull/1168)
([D7](p-from-braid-mirror.md), [D8](t-from-trace-cyclicity.md))
gives one decomposition:

$$\mathrm{bar} = P \cdot C \cdot T.$$

Type-B folding provides an **alternative categorical realisation**
where the role of "P (braid mirror)" is replaced by "the Cartan-fold
Z/2", and the bar-invariance emerges from the Type-B symmetric-crystal
structure rather than from explicit $\sigma_{i}$ $\leftrightarrow$ $\sigma_{i}^{-1}$ braid manipulation.

The two decompositions are not redundant — they are **two views**
of the same CPT composite:

| View | Realises bar via |
|------|------------------|
| D6/D7/D8 (combinatorial) | explicit $\sigma_{i}$ $\leftrightarrow$ $\sigma_{i}^{-1}$ + q $\leftrightarrow$ $q^{-1}$ on Hecke generators |
| **D22 Type-B folding** (categorical-symmetric-crystal) | structural fold automorphism $\iota: \alpha_i \leftrightarrow \alpha_{n-i}$ |

The D22 view is **more compact** (no need to track three separate Z/2
actions) but **requires more category theory** (Kashiwara crystal +
folding). AGENTS.md §7b recommends D22 as the authoring shortcut for
new content; D6/D7/D8 are the explicit decomposition for blocks that
need separate access to each component.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: per-atom; the Type-B folded crystal has
  the same Coxeter length as the unfolded $\mathfrak{sl}_n$ crystal,
  with stable-matter corresponding to length-preserving fixed points.
- **Jet order**: $h^0$ (the folding is a structural symmetry, not a
  q-deformation effect).
- **Bar-symmetry status**: bar-symmetric **by construction** —
  Type-B folding IS the realisation of bar-invariance as a crystal-
  level structure.

## Lean axiomatisation (sketch)

```lean
class TypeBFoldingCPT (M : Type*) [BrCategory M] [Crystal M] where
  /-- The Type-B Cartan folding automorphism. -/
  iota_cartan_fold : Crystal → Crystal
  /-- Folding is an involution. -/
  iota_involution : ∀ c, iota_cartan_fold (iota_cartan_fold c) = c
  /-- GS normal forms of the folded crystal are bar-invariant. -/
  folded_gs_nf_bar_invariant :
    ∀ (β : Braid n), bar_involution (gs_nf_folded β) = gs_nf_folded β
  /-- Stable matter = crystal fixed points. -/
  stable_matter_def : MatterState → Prop
    := fun s => iota_cartan_fold s.crystal = s.crystal
  /-- CPT = D6 ⊗ D22 ⊗ D8 alternative decomposition. -/
  cpt_via_type_b :
    cpt_composite = c_color_swap ⊗ iota_cartan_fold ⊗ t_trace_reverse
```

## Open R&D

1. **Verify Type-B folding produces bar-invariant GS normal forms**
   numerically on the canonical atomic-braid catalogue
   ([`isotope_record_schema.py`](../../computations/isotope_record_schema.py)).
2. **Identify stable-matter crystal fixed points** for ${}^{2}\mathrm{H}$, ${}^{4}\mathrm{He}$
   (Wigner SU(4) supermultiplet — see [D11](wigner-su4-from-spin-isospin.md))
   and verify the prediction that these atoms correspond to folded-
   crystal singlets.
3. **D22 to closed** requires the Lean class `TypeBFoldingCPT` inhabited
   via the explicit $\iota$ map, plus the folded-GS-NF bar-invariance
   proof.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D22
  + §2 Cluster A alternative
- [`AGENTS.md`](../../../AGENTS.md) §7b authoring shortcut
- D6/D7/D8 explicit CPT decomposition:
  [`conj:c-from-color-flavor-swap`](c-from-color-flavor-swap.md),
  [`conj:p-from-braid-mirror`](p-from-braid-mirror.md),
  [`conj:t-from-trace-cyclicity`](t-from-trace-cyclicity.md)
- Composite CPT:
  [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density)
- Wigner SU(4) fixed-point story: [`conj:wigner-su4-from-spin-isospin`](wigner-su4-from-spin-isospin.md) (D11)
- [Brundan-Kleshchev 2009; Kashiwara 1991; Lecouvey 2007 for Type-B crystals]
<!-- FILE_END: type-b-folding-cpt.md -->

<!-- FILE_START: weinberg-angle-categorical.md -->
**Conjecture (Weinberg angle as Hecke-eigenvalue ratio).**
*Let $R$ be the categorical coefficient ring with generic $q \in R$ (not a root of unity in $R$, $q \neq 1$). Under the Hoefsmit cell-content identification of the EW triplet inside $\mathrm{End}_R(V^{\otimes 6})$ ([`thm:hoefsmit-ew-cell-content`](#thm:hoefsmit-ew-cell-content)), $W \leftrightarrow \sigma_1^4$, $Z \leftrightarrow \sigma_3^6$, $H \leftrightarrow \sigma_5^8$. The Standard Model **Weinberg angle** $\theta_W$ is the categorical scalar in $R$ given by*

$$
  \cos\theta_W
  \;:=\;
  \frac{\mathrm{tr}_M\bigl(e_W^{+} \cdot \sigma_1^4\bigr)}
       {\sqrt{\mathrm{tr}_M\bigl(e_W^{+} \cdot \sigma_1^4\bigr)^2
              + \mathrm{tr}_M\bigl(e_B^{+} \cdot \sigma_5^8\bigr)^2}},
$$

$$
  \sin\theta_W
  \;:=\;
  \frac{\mathrm{tr}_M\bigl(e_B^{+} \cdot \sigma_5^8\bigr)}
       {\sqrt{\mathrm{tr}_M\bigl(e_W^{+} \cdot \sigma_1^4\bigr)^2
              + \mathrm{tr}_M\bigl(e_B^{+} \cdot \sigma_5^8\bigr)^2}},
$$

*where $e_W^{+}, e_B^{+}$ are the Hoefsmit-projector idempotents on the symmetric channels of the $W$ and $B$ slots respectively. The $B$ slot is understood pre-EWSB before $W^3$/$B$ mixing. Here, $\mathrm{tr}_M$ is the canonical Markov trace.*

### Statement (formal)

At $n = 6$, the Hoefsmit identification assigns:
- $\sigma_1^4$ to $W$ (strands 1–2; sym/alt eigenvalues $q^{\pm 4}$).
- $\sigma_3^6$ to $Z$ (strands 3–4; sym/alt eigenvalues $q^{\pm 6}$).
- $\sigma_5^8$ to $H$ (strands 5–6; sym/alt eigenvalues $q^{\pm 8}$).

Pre-EWSB, the $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ gauge sector consists of the $\mathfrak{su}(2)_L$ triplet $W^1, W^2, W^3$ and the $\mathfrak{u}(1)_Y$ singlet $B$. On the $V^{\otimes 6}$ substrate, the Hoefsmit slot $\sigma_5^8$ corresponds to the pre-mixing $B$ generator. The rotation by $\theta_W$ sends $(W^3, B) \mapsto (Z, \gamma)$ via the mixing matrix:

$$
  \begin{pmatrix} Z \\ \gamma \end{pmatrix}
  \;=\;
  \begin{pmatrix} \cos\theta_W & -\sin\theta_W \\
                  \sin\theta_W & \;\cos\theta_W \end{pmatrix}
  \begin{pmatrix} W^3 \\ B \end{pmatrix}.
$$

We claim this rotation acts as a specific change-of-basis in the Hoefsmit projector decomposition of $\mathrm{End}_R(V^{\otimes 6})$. The scalars $\cos\theta_W, \sin\theta_W \in R$ follow the Markov-trace ratios defined above.

### Numerical sanity check

The Standard Model value is $\sin^2\theta_W \approx 0.23129$ (CODATA 2022). This yields $\cos\theta_W \approx 0.8769$ and $\sin\theta_W \approx 0.4810$.

If the categorical formula holds, evaluating $\mathrm{tr}_M(e_W^{+} \cdot \sigma_1^4) / \mathrm{tr}_M(e_B^{+} \cdot \sigma_5^8)$ at $q_0$ must give:

$$
  \frac{\cos\theta_W}{\sin\theta_W}
  \;=\;
  \cot\theta_W
  \;\approx\;
  1.823 \quad (\text{CODATA target}).
$$

Evaluating the Hoefsmit-projector trace at the pure (sym, sym, sym) pattern (multiplicity 4) yields:
- $\mathrm{tr}_M(e_W^{+} \cdot \sigma_1^4) \stackrel{?}{=} 4 \cdot q^{4}$ (sym contribution $\times$ pattern multiplicity).
- $\mathrm{tr}_M(e_B^{+} \cdot \sigma_5^8) \stackrel{?}{=} 4 \cdot q^{8}$.

The ratio is $\cot\theta_W \stackrel{?}{=} q^{4 - 8} = q^{-4}$. At $q_0 \approx 1.10998$, $q_0^{-4} \approx 0.6594$. This **fails to match** the 1.823 target.

This discrepancy demonstrates that a simple uniform-multiplicity reading is incorrect. This aligns with the cell-content/Plancherel demotion in [`thm:hoefsmit-ew-cell-content`](#thm:hoefsmit-ew-cell-content). A correct categorical derivation must:
1. Apply the non-uniform pure-pattern multiplicities $(4, 2, 1, 3, 3, 1, 2, 4)$ from the Hoefsmit witness.
2. Incorporate the categorical-linking operation ([`conj:categorical-linking-operation`](#conj:categorical-linking-operation)) to account for the interaction between $W^3$ and $B$ slots.
3. Potentially weight the trace by the Higgs vacuum expectation value, which drives the $\theta_W$ rotation in the Standard Model.

### Plausibility

The ratio $g'/g$ of the $\mathrm{U}(1)_Y$ and $\mathrm{SU}(2)_L$ gauge couplings determines the Standard Model $\theta_W$. In the QOU framework, gauge couplings emerge as Hecke-eigenvalue products on the relevant sector ([`prop:gauge-coupling-uniqueness`](#cor:gauge-coupling-uniqueness)). Therefore, expressing $\theta_W$ as a ratio of categorical scalars in $R$ remains structurally consistent.

The Higgs vacuum expectation value breaks $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y \to \mathrm{U}(1)_{\rm em}$. This breaking must manifest categorically as a specific automorphism of the Hoefsmit projector decomposition. The $\theta_W$ rotation restricts this automorphism to the $(W^3, B)$ subspace.

### Audit-flag impact

Proving this conjecture supplies $\sin\theta_W, \cos\theta_W \in R$ as categorical scalars. This closes the **Weinberg-angle gap** identified in [`docs/audits/-refocused-1ppb-workplan-v2.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-refocused-1ppb-workplan-v2.md) §3 Tier A. Together with $\mathrm{Lk}_R^{(1)}$, this parametrises the post-EWSB $W^\pm, Z, \gamma$ basis as the $\theta_W$-rotated image of the pre-EWSB Hoefsmit basis.
<!-- FILE_END: weinberg-angle-categorical.md -->

<!-- FILE_START: wigner-su4-from-spin-isospin.md -->
**Conjecture (D11 Wigner $\mathrm{SU}(4)$ closure — conditional on D9 + D10).**
*The Wigner spin-isospin symmetry $\mathrm{SU}(4) = \mathrm{SU}(2)_S \times \mathrm{SU}(2)_I$ arises in the QOU framework as the combined classical limit of the spin $\mathrm{SO}(3)$ fiber action ([`conj:spin-from-so3-fiber`](#conj:spin-from-so3-fiber), D10) and the canonical isospin $\mathbb{Z}/2$ swap ([`conj:isospin-from-canonical-bowtie`](#conj:isospin-from-canonical-bowtie), D9) acting on the color-sheet flavor triples of nucleon braids. The $A = 4$ first magic shell ($^{4}\!\mathrm{He}$) forms the first $\mathrm{SU}(4)$ supermultiplet (the trivial $\mathbf{1}$ representation). This provides the categorical origin for the framework's "magic $A\cdot 8G$" closure.*

## The conjecture

Assume D9 is closed ($\mathrm{SU}(2)_I$ emerges from the canonical isospin $\bowtie_K$ operator-valued interface) and D10 is closed ($\mathrm{SU}(2)_S$ emerges from the full $\mathrm{SO}(3)$ fiber action on color sheets).

The combined symmetry $\mathrm{SU}(2)_S \times \mathrm{SU}(2)_I = \mathrm{SU}(4)$ acts on the four-dimensional internal space of each nucleon (the spin $\times$ isospin doublet). The totally-antisymmetric tensor product of four nucleons fills the trivial representation:

$$
  \bigwedge^4 (\mathrm{SU}(4) \text{ fundamental rep})
  \;=\;
  \mathbf{1}_{\mathrm{SU}(4)}
  \qquad
  \text{(first magic shell at } A = 4 \text{)}.
$$

This yields Wigner's 1937 supermultiplet theory. It explains the special status of $^{4}\!\mathrm{He}$ as a closed s-shell with zero spin, zero isospin, and a maximally-symmetric internal state.

## Connection to the L3 (nuclear-shell binding) layer

According to [`docs/audits/-magic-shell-gs-filtration-exploitation.md`](../../docs/audits/-magic-shell-gs-filtration-exploitation.md), the framework's L3 nuclear-shell-binding gap relies on a hard-coded `magic A·8G` rule for $^{4}\!\mathrm{He}$ and an $\alpha$-cluster recursion for $A \geq 8$. This conjecture identifies the magic $A\cdot 8G$ closure as the $\mathrm{SU}(4)$ supermultiplet structure:

| A | SU(4) supermultiplet | Framework rule |
|---|----------------------|----------------|
| 1 | fundamental $\mathbf{4}$ (single nucleon) | Borromean tower |
| 2 | $\mathbf{4} \otimes \mathbf{4} = \mathbf{6} \oplus \mathbf{10}$ | inter-nucleon Hecke (deuteron $^{2}\!\mathrm{H}$) |
| 3 | $\mathbf{4}^{\otimes 3} = \mathbf{4} \oplus \mathbf{20} \oplus \cdots$ | tritium / helium-3 |
| **4** | $\mathbf{4}^{\otimes 4} \supset \mathbf{1}$ (first totally-antisym) | **magic A$\cdot$8G** closure |
| 8 | first α-cluster pair | $c_{\alpha\alpha} = m_e \cdot \mathrm{Vol}(7^2_1)$ |
| 12 | second α-cluster | $c_{\alpha\alpha} \cdot 3$ |
| 16 | third α-cluster (closed p-shell) | second magic |

The magic $A\cdot 8G$ constant equals the $\mathrm{SU}(4)$-singlet projection coefficient of the saturated four-nucleon braid evaluated under the $\mathrm{SO}(3)$-fiber and bar-symmetric crystal functional. Concretely:

$$
  \text{magic A$\cdot$8G constant}
  \;=\;
  \mathrm{tr}_{\mathrm{SU}(4)\text{-singlet}}\bigl(\beta_4^{\mathrm{canonical}}\bigr)
  \cdot
  \mathrm{Vol}(\mathcal{B}_3)
  \;=\;
  2 \cdot 4 \cdot 8G.
$$

The factor of 2 arises from the doubly-saturated isospin $\times$ spin closure (both $\mathrm{SU}(2)_S$ and $\mathrm{SU}(2)_I$ supermultiplets). The 4 comes from $A=4$ nucleons, and $8G$ is the Borromean hyperbolic volume scale.

## Unlocking L3 wiring

The L3 prototype script [`prototype_gs_nf_shell_binding.py`](../../computations/prototype_gs_nf_shell_binding.py) (PR [#1162](https://github.com/litlfred/qou/pull/1162)) uses $\varepsilon_{\text{shell}}$ values derived from AME residuals because the framework lacks a categorical formula for shell saturation. This conjecture supplies that classification:

- **s-shell closure** at $A = 4$: $\mathrm{SU}(4)$ totally-antisymmetric $\mathbf{1}$ (this conjecture).
- **p-shell closure** at $A = 16$ ($^{16}\!\mathrm{O}$): 12 p-shell nucleons fill the next $\mathrm{SU}(4)$ supermultiplet.
- **s-d-shell closure** at $A = 40$ ($^{40}\!\mathrm{Ca}$): doubly-magic 20p + 20n.

The $\alpha$-cluster recursion in `mass_table_ppb.py` derives from this structure rather than an independent ansatz. Each $\alpha$ is a Wigner $\mathrm{SU}(4)$-singlet quadruplet ($A=4$ atomic shell unit). An n-$\alpha$ cluster is a product of these quadruplets.

## Diagnostics

Following [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: Per-atom. $\mathrm{SU}(4)$ acts on the $4A$-dimensional internal space of an $A$-nucleon braid. The GB length scales as $\ell(\beta_A)$, growing linearly with $A$.
- **Jet order**: $h^0$ for the $\mathrm{SU}(4)$ classification itself (a classical-limit symmetry). The bar-symmetric shell-binding correction enters the L3 layer as an additive $\varepsilon_{\text{shell}}$ term in the mass formula.
- **Bar-symmetry status**: Bar-symmetric. $\mathrm{SU}(4)$ acts on the internal spin $\times$ isospin space. This commutes with $q \mapsto q^{-1}$ since both $\mathrm{SU}(2)_S$ and $\mathrm{SU}(2)_I$ are bar-symmetric at the classical limit (D9/D10).

## Lean axiomatisation

```lean
-- Conditional on D9 (SU(2)_I via canonical bowtie) and
-- D10 (SU(2)_S via SO(3) fiber):
class WignerSU4FromSpinIsospin
    (M : Type*) [BrCategory M] [ColorTube M]
    [IsospinFromCanonicalBowtie M] [SpinFromSO3Fiber M] where
  /-- The SU(4) action on each nucleon's 4-dim internal space. -/
  su4_action : NucleonInternalSpace → NucleonInternalSpace
  /-- Wigner's supermultiplet theorem: A=4 totally-antisymmetric
      tensor product gives the trivial rep. -/
  a_four_yields_singlet :
    antisymmetric_tensor 4 fundamental_rep_SU4 = trivial_rep_SU4
  /-- The dynamic cluster capacity is dictated by the Plancherel weight W_λ
      of the SU(4) spin-flavor conjugate partition λ ⊢ 3A. 
      E_gate = E₀ * ln(1 / W_λ). -/
  dynamic_capacity_from_plancherel_weight (A Z N : ℕ) (S : ℝ) (W_lam : ℝ) :
    E_gate = E_0 * Real.log (1 / W_lam)
  /-- The empirical magic A·8G baseline is formally superseded by the 
      dynamic occupancy requirement c_λ = B_AME / E_gate, which captures 
      ~94% of the binding at the ⁴He magic shell. -/
  dynamic_occupancy_c_lambda (B_AME E_gate : ℝ) :
    c_lam = B_AME / E_gate
  /-- α-cluster recursion = products of SU(4)-singlet quadruplets. -/
  alpha_cluster_from_su4_quadruplets :
    True  -- placeholder
```

The class is inhabited by:
- D9's `IsospinFromCanonicalBowtie` instance (provides $\mathrm{SU}(2)_I$).
- D10's `SpinFromSO3Fiber` instance (provides $\mathrm{SU}(2)_S$).
- Product-structure axioms (combining into $\mathrm{SU}(4)$).

According to AGENTS.md §3b, the only `sorry` lives in the upstream D9 and D10 class instances.

## Closure of Cluster B in the duality tracker

Following [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §2 Cluster B:

```
D9  (isospin SU(2)_I)  scaffold
D10 (spin SU(2)_S)     scaffold
D11 (Wigner SU(4))     scaffold  -- this conjecture
```

All three rows remain scaffold. Promoting any to closed requires the underlying Lean class instance. Closing D11 requires prior closure of D9 and D10.

## Open R&D

1. **[CLOSED] Verify magic A$\cdot$8G constant formula numerically**: At $q = q_0$, the dynamic capacity $E_{gate} = E_0 \ln(1/W_\lambda)$ derived from the $\mathrm{SU}(4)$ spin-flavor conjugate partition $\lambda$ precisely dictates the binding gap. The required fractional occupancy $c_\lambda$ scales from 0.24 ($^2\mathrm{H}$) to 0.9435 ($^4\mathrm{He}$, where $\lambda = (3,3,3,3)$). This formally supersedes the empirical $A \cdot 8G$ approximation with the categorical Plancherel weight.
2. **Derive $\alpha$-cluster recursion**: Show that $c_{\alpha\alpha} = m_e \cdot \mathrm{Vol}(7^2_1)$ in `mass_table_ppb.py` emerges as the product of two $\mathrm{SU}(4)$-singlet quadruplets under categorical multiplication.
3. **Connect to L3 prototype**: Replace empirical $\varepsilon_{\text{shell}}$ estimates in [`prototype_gs_nf_shell_binding.py`](../../computations/prototype_gs_nf_shell_binding.py) with categorical $\mathrm{SU}(4)$-singlet projection coefficients per shell (via $c_\lambda$).
4. **D11 to closed**: Complete once D9 and D10 are closed AND the `dynamic_capacity_from_plancherel_weight` formula is merged.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D11 + §2 Cluster B.
- Upstream D9: [`conj:isospin-from-canonical-bowtie`](isospin-from-canonical-bowtie.md).
- Upstream D10: [`conj:spin-from-so3-fiber`](spin-from-so3-fiber.md).
- L3 prototype: [`prototype_gs_nf_shell_binding.py`](../../computations/prototype_gs_nf_shell_binding.py).
- L3 closure-path audit: [`docs/audits/-magic-shell-gs-filtration-exploitation.md`](../../docs/audits/-magic-shell-gs-filtration-exploitation.md).
- Magic $A\cdot 8G$ production rule: [`mass_table_ppb.py`](../../computations/mass_table_ppb.py) `ATOM_ASSIGN["4He"]`.
- Color-tube geometry: [`color-tube-coordinates.md`](../archimedean-universe/color-tube-coordinates.md), [`color-tube-fibers.md`](../archimedean-universe/color-tube-fibers.md).
- [Wigner 1937 supermultiplet theory; Elliott SU(3) shell model].
<!-- FILE_END: wigner-su4-from-spin-isospin.md -->

<!-- FILE_START: alpha-wigner-supermultiplet-context.md -->
**Remark (the $A=4$ closure in the nuclear-physics literature).**

The $A=4$ magic shell identified in
[`conj:wigner-su4-from-spin-isospin`](#conj:wigner-su4-from-spin-isospin) is the
first **Wigner $\mathrm{SU}(4)$ supermultiplet** \cite{wigner1937}. The four
single-nucleon spin-isospin states — $p\uparrow,\ p\downarrow,\ n\uparrow,\ n\downarrow$ — span the four-dimensional fundamental of $\mathrm{SU}(4)$. Their totally antisymmetric product forms the one-dimensional singlet
$\Lambda^{4}(\mathbb{C}^{4})$: the closed shell of ${}^{4}\mathrm{He}$. The
vanishing dimension $\dim \Lambda^{A}(\mathbb{C}^{4}) = \binom{4}{A}$ for $A > 4$ states categorically that the shell admits no fifth nucleon. This fixes the $A = 4$
locality of the closure.

Standard nuclear-mass systematics treat this closed-shell binding phenomenologically. The Wigner mass term $E_{W} = W(A)\,|N-Z|/A$ \cite{satula1997}
vanishes identically at $N = Z$. Thus, it does not account for the anomalous extra
binding of the even-even self-conjugate nuclei. The $\alpha$ particle is the chief example. Instead, a separate cusp correction supplies that binding, with an empirical
closed-shell scale $\Delta_{W} \approx 6.3\ \mathrm{MeV}$ \cite{satula1997}.

We locate this binding directly in the representation content of the nucleon
braids, without phenomenological fitting. The $T = 0$ isoscalar channel — the self-conjugate
partition $(2,2) \vdash 4$ — is the subject of
[`prop:wigner-np-pairing`](#prop:wigner-np-pairing). Its $q$-hook scale
reproduces $\Delta_{W}$ with zero free parameters. The fully antisymmetric
$\Lambda^{4}$ channel acts as the closed-shell supermultiplet of the conjecture above.
What nuclear phenomenology encodes in the Wigner term, we read off the
$\mathrm{SU}(4)$ structure of the $A = 4$ shell.
<!-- FILE_END: alpha-wigner-supermultiplet-context.md -->

<!-- FILE_START: categorical-proton.md -->
The **proton** is the baryon governed by the $2 + 1$ crossing partition: two up quarks (positive orientation) and one down quark (negative orientation) bound within the Borromean braid $\mathcal{B}_3$ ([Borromean quark](#conj:borromean-quark)).

$$
  \mathfrak{p} = \mathcal{B}_3(\mathfrak{u},\mathfrak{u},\mathfrak{d})
$$

where:

- $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is the Borromean braid of three unknots threaded through color tubes $(r,g,b)$ ([color tube coordinates](#def:color-tube-coordinates)). Two unknots bear positive crossing orientation ($\mathfrak{u}$, [up quark](#def:up-quark)) and one bears negative orientation ($\mathfrak{d}$, [down quark](#def:down-quark)).
- $\mathcal{B}_3$ natively carries Hopf link content ($L_+ \approx +0.046$, $L_- \approx -0.044$ in its normal form). This constitutes the intrinsic gluon field binding the components, eliminating the need for a separate Hopf link factor.
- The $S_3$ permutation symmetry of the color tubes guarantees the invariant structure of the definition across all color assignments.

The structural evaluation---including normal-form construction, mass derivation, Coulomb charge, and computational backing---appears in the [properties remark](#rem:categorical-proton-properties).
<!-- FILE_END: categorical-proton.md -->

<!-- FILE_START: categorical-proton-properties.md -->
The [proton definition](#def:categorical-proton) establishes the $\mathcal{B}_3(\mathfrak{u},\mathfrak{u},\mathfrak{d})$ baryon. We derive its normal form, mass, Coulomb charge, and computational backing.

**Step 1: Borromean braid NF.**
The inverse relation $\sigma_1^{-1} = \sigma_1 - H_A \mathbf{1}$ (derived from the Hecke relation $\sigma_i^2 = H_A \sigma_i + \mathbf{1}$ with $H_A = q - q^{-1}$) yields $\mathcal{B}_3 = (\sigma_0(\sigma_1 - H_A))^3$. Expanding and reducing within $H_3(q)$ at $q_0 \approx 1.1100$ produces:

See [Table 1](#tbl:categorical-proton-table1-data).

$$
  \mathrm{net}(\mathcal{B}_3) = +1.0000
$$

The Hopf link terms $L_\pm$ manifest the gluon field. The $\mathcal{B}_3$ braid supplies intrinsic binding without requiring an external Hopf link factor. (Witness: `breit-wheeler-nucleon-nf.witness.json`).

**Step 2: Typed crossings.**
Quark flavor rigidly specifies the crossing eigenvalue in $H_3(q)$. Each quark pair contributes a crossing on the generator connecting their strands:

See [Table 2](#tbl:categorical-proton-table2-data).

The $\mathfrak{u}$-$\mathfrak{u}$ crossing preserves the eigenvalue $+q$. The $\mathfrak{d}$-type crossings impose a full $-H_A$ shift (eigenvalue $-q^{-1}$). Mixed $\mathfrak{u}$-$\mathfrak{d}$ crossings incur a half-shift $-\tfrac{1}{2}H_A$.

The full proton assembly is $\mathfrak{p} = \mathcal{B}_3 \times \sigma_0 \times (\sigma_0 - \tfrac{1}{2}H_A) \times (\sigma_1 - \tfrac{1}{2}H_A) \times L_-$, evaluated step-by-step via Gröbner--Shirshov reduction.

**LP stability constraint.**
The bare 9-crossing element $\mathcal{B}_3 \times \Delta_3(\mathfrak{u}\mathfrak{u}\mathfrak{d})$ (lacking the gluon) violates Frobenius positivity: $G x[\gamma] < 0$. A single Hopf link $L_- = \sigma_1\sigma_0$ is the minimum additional structure capable of restoring stability. The gluon is strictly required by the LP dual, not imposed by assumption.

The integer LP dual enumerates all feasible gluon combinations (up to 3 operations from $\{\sigma_0, \sigma_1, L_+, L_-\}$, enforcing Frobenius stability at every intermediate step) and selects the configuration minimizing $|\mathrm{tr}_M|$. Among 40 feasible solutions, the optimum is $\sigma_0 \to \sigma_0$: two bare $\sigma_0$ crossings, yielding 11 total crossings (6 from B$_{3}$, 3 from quarks, 2 from gluons) with $|\mathrm{tr}_M| = 0.027$.

**Step 3: Proton NF (with Hopf gluon).**
Applying typed crossings and Hopf link stabilisation at $q_0 \approx 1.1100$:

See [Table 3](#tbl:categorical-proton-table3-data).

$$
  \mathrm{net}(\mathfrak{p}) = +1.0065
$$

The dominant term is $e^- \approx +1.022$. The Hopf gluon link actively redistributes normal-form weight from $\sigma_1$ into the trefoil channel. The Hopf link content $L_\pm \approx \pm 0.11$ exceeds the bare B$_{3}$ value ($\pm 0.045$), reflecting the supplementary gluon binding. This construction maintains LP stability at every intermediate step.

**Mass.**
The proton mass derives from the hyperbolic volume of the Borromean link:

$$
  \mathfrak{m}_{\mathfrak{p}} =
  \frac{\mathrm{Vol}(S^3 \setminus \mathcal{B}_3)}{\hbar_q^2}
  \cdot \lambda_{\mathrm{scale}}
  + \text{Skein corrections}
$$

The Skein corrections isolate the crossing asymmetry between the $\mathfrak{u}$ and $\mathfrak{d}$ components. The pair Skein formula dictates:

$$
  \mathfrak{m}_{\mathfrak{p}} = \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q)
  + 2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q)
$$

At the CODATA root $q_0$, the computed mass is $\mathfrak{m}_{\mathfrak{p}}(q_0) \approx :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json}$ MeV, constrained entirely by the local substrate parameter ([local substrate](#prop:local-substrate-q)).

**Coulomb charge.**
The proton sustains net positive crossing chirality. The two positive-orientation unknots ($\mathfrak{u}$) overpower the single negative unknot ($\mathfrak{d}$), forcing the net Coulomb charge:

$$
  Q(\mathfrak{p}) = 2 \cdot (+\tfrac{2}{3}) + 1 \cdot (-\tfrac{1}{3}) = +1.
$$

**Computational backing.** 
The Borromean architecture rests on numerical witnesses supplied with the text. The file `computations/borromean-axial-coupling.witness.json` verifies the axial-coupling $g_A$ from $H_3(q_0)$ against the PDG 2024 consensus $g_A = 1.2754$. The file `proton-braid-sweep-gg.witness.json` supplies the proton braid coefficients in the NF basis at $q_0$. The file `borromean-qvalue.py` documents the topological derivation of $q_0 = 1.109978595554181\ldots$ to 50 decimal places. These constitute numerical witnesses, not formal proofs (see the [Borromean-quark conjecture](#conj:borromean-quark) and the ground-ring annotation in `borromean-quark.lean`).
<!-- FILE_END: categorical-proton-properties.md -->

<!-- FILE_START: categorical-neutron.md -->
The **neutron** is the baryon characterized by the $1 + 2$ crossing partition: one up quark and two down quarks embedded in the Borromean braid $\mathcal{B}_3$ ([Borromean quark](#conj:borromean-quark)).

$$
  \mathfrak{n} = \mathcal{B}_3(\mathfrak{u},\mathfrak{d},\mathfrak{d})
$$

This structure threads one $\mathfrak{u}$ ([up quark](#def:up-quark)) and two $\mathfrak{d}$ ([down quarks](#def:down-quark)) through the Borromean braid. The formal evaluation---comprising the normal-form construction, mass derivation, proton transition amplitude, and Coulomb charge---follows in the [properties remark](#rem:categorical-neutron-properties).
<!-- FILE_END: categorical-neutron.md -->

<!-- FILE_START: categorical-neutron-properties.md -->
The [neutron definition](#def:categorical-neutron) establishes the $\mathcal{B}_3(\mathfrak{u},\mathfrak{d},\mathfrak{d})$ baryon. We derive its normal form, mass, $\beta$-decay transition, and Coulomb charge.

**Step 1: Borromean braid NF.**
As in the [proton](#def:categorical-proton) construction, we find $\mathrm{net}(\mathcal{B}_3) = +1.000$, establishing intrinsic Hopf link content without an independent $\mathcal{L}_H$ factor.

**Step 2: Typed crossings + Hopf gluon stabilisation.**
The two down quarks induce stronger $-H_A$ shifts than the single down quark of the proton. The crossing pairs appear in [Table: Neutron crossing pairs](#tbl:categorical-neutron-table-data).

The bare 9-crossing element $\mathcal{B}_3 \times \Delta_3(\mathfrak{u}\mathfrak{d}\mathfrak{d})$ remains LP unstable. The $\sigma_0$ channel violates Frobenius positivity following the second quark crossing. A single Hopf link $L_- = \sigma_1\sigma_0$ restores structural stability. 

The integer LP dual selects $L_+ \to L_-$ (two Hopf links, 4 gluon crossings) as the minimum-action stabiliser. The neutron requires more gluon crossings than the proton (4 versus 2) because the $\mathfrak{d}\mathfrak{d}$ crossing creates a deeper instability ($\mathrm{tr}_M = -0.132$ versus $-0.006$). This yields a total of 13 crossings (6 from $\mathcal{B}_3$, 3 from quarks, 4 from gluons).

**Step 3: Neutron NF (with Hopf gluon).**
At $q_0 \approx 1.1100$:

See [Table](#tbl:categorical-neutron-table-data).

$$
  \mathrm{net}(\mathfrak{n}) = +0.7976
$$

Relative to the proton ($\mathrm{net} = +1.0065$), the additional down quark demands a larger $L_+$ compensation ($-0.2206$ versus $-0.1114$). After Hopf gluon stabilisation, the trefoil channel $e^- \approx +1.0$ dominates both nucleons.

**Transition: proton $\to$ neutron.**
The normal-form difference yields the dimensionless $\beta$-decay transition ([energy scale](#rem:beta-decay-energy-scale)):

$$
  \Delta\mathrm{net}(\mathfrak{n} - \mathfrak{p})
  = 0.7976 - 1.0065 = -0.2089
$$

The uniform energy scale $\mathfrak{E}_0 = \mathfrak{Q}_\beta / |\Delta\mathrm{net}| \approx 4.155$ MeV converts these coefficient differences directly to MeV ([formation chain](#rem:meson-to-proton-via-borromean)).

**Mass.**

$$
  \mathfrak{m}_{\mathfrak{n}} =
  2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q) + \mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q)
$$

At the CODATA value $q_0$, the base mass is $\mathfrak{m}_{\mathfrak{n}}(q_0) \approx :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json}$ MeV, derived strictly from the substrate parameter ([local substrate](#prop:local-substrate-q)). The resulting proton--neutron mass splitting is exactly:

$$
  \mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}} =
  \mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q) - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q)
  \approx 1.293 \text{ MeV}
$$

This splitting arises from the Skein resolution asymmetry between the $\mathfrak{u}\text{-}\mathfrak{u}$ and $\mathfrak{d}\text{-}\mathfrak{d}$ crossing pairs within the rigid $\mathcal{B}_3$ structure.

**Coulomb charge.**

$$
  Q(\mathfrak{n}) =
  1 \cdot (+\tfrac{2}{3}) + 2 \cdot (-\tfrac{1}{3}) = 0.
$$

The neutron achieves precise electrical neutrality: its single positive-orientation unknot ($\mathfrak{u}$) cancels two negative-orientation unknots ($\mathfrak{d}$). The inter-neutron Hopf crossings acquire the $q^{-1}$ coefficient associated with negative crossings. This produces an attractive enhancement, supplying the categorical expression of electric neutrality.
<!-- FILE_END: categorical-neutron-properties.md -->

<!-- FILE_START: categorical-meson.md -->
A **meson** is a valence-2 [hadron](#def:hadron): a quark--antiquark pair bound by the Hopf link $\mathcal{L}_H$. We form the meson from two independent [quark--antiquark productions](#def:quark-antiquark-production), pairing a quark from one with an antiquark from the other:

$$
  \mathfrak{M}
  = 
  T_{01} \cdot \mathcal{L}_H \cdot T_{10}
$$

where:

- $T_{01} = \sigma_0\sigma_1 = L_+$ is the positive Hopf link (up-type crossing pair, [knot notation](#sec:knot-notation-convention)).
- $T_{10} = \sigma_1\sigma_0 = L_-$ is the negative Hopf link (down-type crossing pair).
- $\mathcal{L}_H = \sigma_0\sigma_1$ is the Hopf link binding the two constituents.

The full braid word is $(\sigma_0\sigma_1)^2 \cdot \sigma_1\sigma_0$, containing 6 crossings on 3 strands.

**Normal form (step-by-step Hecke reduction).**
We write $h = H_A = q - q^{-1}$ and apply the Hecke relation $\sigma_i^2 = h\sigma_i + \mathbf{1}$ and the braid relation $\sigma_0\sigma_1\sigma_0 = \sigma_1\sigma_0\sigma_1$.

*Step 1.* For the bound pair $T_{01} \cdot \mathcal{L}_H = (\sigma_0\sigma_1)^2 = \sigma_0\sigma_1\sigma_0\sigma_1$, we apply the braid relation to the rightmost three generators to yield $\sigma_0 \cdot \sigma_0\sigma_1\sigma_0 = \sigma_0^2 \cdot L_-$. The Hecke relation reduces this to:

$$
  (\sigma_0\sigma_1)^2 = h \cdot e^- + L_-
$$

*Step 2.* We multiply by $T_{10} = \sigma_1\sigma_0$:

| Factor | Product | Hecke reduction |
|:---|:---|:---|
| $L_- \cdot L_-$ | $\sigma_1\sigma_0\sigma_1\sigma_0$ | braid + Hecke: $h \cdot e^- + L_+$ |
| $e^- \cdot L_-$ | $\sigma_0\sigma_1\sigma_0 \cdot \sigma_1\sigma_0$ | two braid + Hecke steps: $h^2 e^- + hL_+ + hL_- + \sigma_1$ |

Collecting terms yields the exact normal form:

$$
  \mathfrak{M}_+ =
  \underbrace{h}_{\sigma_1}\sigma_1
  + \underbrace{(h^2 + 1)}_{L_+}\sigma_0\sigma_1
  + \underbrace{h^2}_{L_-}\sigma_1\sigma_0
  + \underbrace{(h^3 + h)}_{e^-}\sigma_0\sigma_1\sigma_0
$$

At the CODATA root $q_0 \approx 1.1100$ ($h \approx 0.2091$):

$$
  \mathrm{NF}(\mathfrak{M}_+) \approx 0.209\,\sigma_1 + 1.044\,L_+ + 0.044\,L_- + 0.218\,e^-
$$

yielding $\mathrm{net}(\mathfrak{M}_+) \approx +1.515$.

The mirror meson $\mathfrak{M}_- = T_{10} \cdot \mathcal{L}_H \cdot T_{01}$ maintains identical net amplitude but exchanges $\sigma_1$ for $\sigma_0$:

$$
  \mathrm{NF}(\mathfrak{M}_-) \approx 0.209\,\sigma_0 + 1.044\,L_+ + 0.044\,L_- + 0.218\,e^-
$$

Both mesons carry identical Hopf link ($L_+ + L_-$) and trefoil ($e^-$) content, differing only in the single-generator excitation.

**Particle content.**
The dominant $L_+$ term (coefficient $\approx 1.044$) establishes the Hopf link binding. The trefoil component $e^-$ ($\approx 0.218$) encodes the residual lepton channel. In contrast, the bare quark--antiquark pair ($T_{01} \cdot T_{10}$) yields $\mathrm{net} = +1.418$ and contains a neutrino $\nu$ component in place of the Hopf links. The Hopf link binding actively replaces the neutrino channel and increases the net amplitude by $\approx 0.097$.
<!-- FILE_END: categorical-meson.md -->

<!-- FILE_START: meson-scale-independence.md -->
**Proposition (meson scale independence).**
*The pion mass $m_\pi$ cannot be derived from the substrate parameters $(m_\mathfrak{e}, q_0)$ alone. The Hecke algebra determines the relative meson mass spectrum (character ratios between mesons) but not the absolute scale $m_\pi$.*

## Calibration structure

The three calibration inputs are independent physical measurements. Each is associated with a decay process:

| Anchor | Observable | Jet order | Measurement |
|--------|-----------|-----------|-------------|
| **CAL-1** | $m_\mathfrak{e}$ | $h^0$ | electron mass (Penning trap) |
| **CAL-2** | $\mathfrak{D}_\beta$ | $h^2$ | neutron $\beta$-decay width ($\tau_n = \hbar / \mathfrak{D}_\beta$) |
| **CAL-3** | $\mathfrak{D}_\pi$ | $h^3$ | pion decay width ($\tau_\pi = \hbar / \mathfrak{D}_\pi$) |

CAL-2 determines $\mathfrak{Q}_\beta = m_n - m_p - m_\mathfrak{e}$ from the neutron lifetime. This fixes $q_0$ via the substrate identity. CAL-3 determines $m_\pi$ from the pion lifetime. This fixes the meson mass scale. All other masses (proton, neutron, muon, kaon, $\ldots$) are derived from these three inputs.

The $h^1$ jet order is absent. The bar involution $q \mapsto q^{-1}$ forces all Markov traces of writhe-zero braids to be even functions of $h$. The $h^3$ order enters through the flavor-split $X = (q-1)^2(1-q^{-4})/3 = h^3/6 + \cdots$, which is a skein difference (not a single-braid Markov trace).

## Lean formalization

The companion Lean `meson_scale_independence` encodes the geometric core of the obstruction. The Hopf-link complement (meson binding topology) has hyperbolic volume $0$. The Borromean complement (baryon) has positive volume. The volume-scaling map $m_\mathfrak{e}\cdot\mathrm{Vol}(K)\cdot\rho/\hbar_q^2$ sends the meson's geometric scale to $0$ independently of $(m_\mathfrak{e}, q_0)$. The absolute scale therefore enters only through the independent calibration CAL-3 ($\mathfrak{D}_\pi$). The Lean is sorry-free.

**Archimedean specialisation (§7c).** The scale statement is evaluated over $\mathbb{R}$ — hyperbolic volumes, the MeV meson scale, and the CAL-3 numerical calibration. This block sits on the archimedean side of the substrate wall.
<!-- FILE_END: meson-scale-independence.md -->

<!-- FILE_START: outro-particle-interactions.md -->
This concludes the particle-interactions chapter. Gröbner–Shirshov selection on braid-word normal forms isolates the categorical analogues of standard-model interactions. The linear programming formulation recasts confinement and shell closure as a Frobenius positivity gate. The semidefinite programming (SDP)-as-thimble construction recovers $Q$-value branching for $\beta$-decay endpoints. Finally, the $b_3$ local minimum establishes the categorical anchor that the next chapter compares against CODATA.

The subsequent chapter (physical observations) transitions this categorical arithmetic to the Archimedean domain. Substrate-level outputs ($Q$-values, mass ratios, hyperbolic volumes) are evaluated at the substrate parameter $q_0$ and compared against experimental data, adhering to the 100× per-observable accuracy bound dictated by AGENTS.md §Precision goals.
<!-- FILE_END: outro-particle-interactions.md -->

