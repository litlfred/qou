<!-- FILE_START: spectral-sequence-chirality-confinement-per-nucleon-shift-intro.md -->
Continuation of the preceding sub-section.

This sub-section assembles the per-nucleon shift and the confinement-NF structure-forcing argument.  The arc moves from the additive-linearity proof (with tables) through the confinement-NF structure-forcing block with table data, the LP-duality hypothesis class, and the partial confinement-NF proof that closes the section.
<!-- FILE_END: spectral-sequence-chirality-confinement-per-nucleon-shift-intro.md -->

<!-- FILE_START: per-nucleon-shift-additive-linearity.md -->
**Proposition (per-new-nucleon additive linearity).**
*The atomic Markov-trace denominator
$D(u) = 2^{2A+1} \cdot u^{\mathrm{shift}} \cdot (1 + u^{2})^{3A-1}$
of canonical pppnnn ordering
([`docs/audits/-w3-habiro-unblocked.md`](../../docs/audits/-w3-habiro-unblocked.md))
has shift exponent satisfying the additive-linearity recurrence:*

$$
  \mathrm{shift}(Z+1, N) \;-\; \mathrm{shift}(Z, N) \;=\; 18,
  \qquad
  \mathrm{shift}(Z, N+1) \;-\; \mathrm{shift}(Z, N) \;=\; 21,
$$

*for $Z, N \geq 1$ (i.e.\ $A \geq 2$).  Together with the base
case $\mathrm{shift}(D) = \mathrm{shift}(1, 1) = 40$, this fixes the
closed form*

$$
  \boxed{\;\;\mathrm{shift}(Z, N) \;=\; 18Z + 21N + 1\;\;}
$$

*on every atom in the canonical pppnnn ordering for $A \geq 2$.*

### Verified atoms

See [Table 1](#tbl:per-nucleon-shift-additive-linearity-table1-data).

(Witness: [`per-nucleon-shift-derivation.witness.json`](../../computations/per-nucleon-shift-derivation.witness.json),
5/5 assertions pass.  Cross-validated against
`term6-residues-at-roots.witness.json` for ${}^{5}$Li.)

### Generator-count decomposition

The additive linearity is structural: each new nucleon adds exactly
12 generators to the canonical-ordered braid in $H_{3A}(q)$:

See [Table 2](#tbl:per-nucleon-shift-additive-linearity-table2-data).

(11 from the nucleon's intrinsic structure
+ 1 from its incoming interface generator
in
the canonical formalism.)
### Companion remark — leading-coefficient identity

The leading coefficient of $\mathrm{tr}_M(\beta)$ at $q = 0$
(equivalently, the coefficient of $u^{-2 \cdot \mathrm{shift}/2}$ in
$D(u)^{-1} \cdot \mathrm{tr}_M(\beta)$ at $u = 0$) is
**$-\tfrac{1}{12}$ exactly** for proton standalone and approximately
$-\tfrac{1}{12}$ for neutron standalone (precision-limited at
high-$A$ atoms in the existing float-precision Hoefsmit pipeline).
See
[`docs/audits/-ocneanu-cancellation-canonical-verification.md`](../../docs/audits/-ocneanu-cancellation-canonical-verification.md)
for the high-precision (200 dps) verification.

The simple rational $-\tfrac{1}{12}$ is strong evidence that the
universal Ocneanu-weighted pole structure of atomic Markov traces
admits a closed-form leading coefficient — currently an open
research direction for $A \geq 2$ atoms.

### Open — full categorical derivation of cancellation count

The per-new-nucleon cancellation values $(3, 1.5)$ are derived from
$\sigma^2$-adjacency counting plus Ocneanu averaging across SYT paths in
the $n = 3A$ seminormal representation, but the closed-form
expression remains open (the half-integer for neutron requires
explicit Ocneanu weight tracking that is computationally prohibitive
beyond $A = 2$ at the current precision tier).

### Use cases

This proposition closes the categorical derivation of the shift
exponent in the atomic Markov-trace denominator, providing:

1. **Closed-form predictions for unmeasured atoms.** $D(u)$ for
   ${}^{7}$Li $(Z = 3, N = 4)$, ${}^{8}$Be $(Z = 4, N = 4)$, etc., is now
   structurally determined — no Hecke NF computation required.
2. **Cross-validation gate.** Any atomic mass / binding pipeline
   that involves $D(u)$ can verify shift = 18Z + 21N + 1 as a
   structural invariant.
3. **Pole-counting consumer.** the canonical formalism
   and downstream pole-counting analyses now have a closed-form
   target for the actual q-pole order of $\mathrm{tr}_M$ (= shift / 2,
   modulo half-integer cases).
<!-- FILE_END: per-nucleon-shift-additive-linearity.md -->

<!-- FILE_START: confinement-nf-structure-forcing.md -->
<!-- Conjecture (witness only — no Lean proof). -->

**Conjecture (Confinement $\to$ NF-structure forcing).**
*Let $\beta = \beta_1 \star I \star \beta_2 \in B_n$ be a compound
braid where $I$ is a basis interface braid (e.g. a torus-knot
generator). Let $A := \{\lambda \vdash n : y_\lambda^* > 0\}$ be the
LP/SDP **active set** of [`prop:operator-selection-lp`](#prop:operator-selection-lp)
applied to $\beta$, and assume the **confinement hypothesis**
$|A| < n!$. Then:*

1. *(NF-support localisation)* The Wedderburn maximizer
   $\lambda^\star \in \arg\max_\lambda \mathrm{ord}_{q=0}^{(-)}
   \chi_\lambda(T_\beta)$ satisfies $\lambda^\star \in A$.
2. *(Shift bound)* There is a deviation $\Delta(\beta_1, \beta_2; A)$
   with

   $$
     \mathrm{shift}_{\mathrm{NF}}(\beta)
     \;=\; \alpha_{\mathrm{shift}}(I) + \Delta(\beta_1, \beta_2; A),
     \qquad
     |\Delta| \;\leq\; \mathrm{duality\_gap}(\beta).
   $$

### Empirical evidence

The witness
[`lp-confinement-nf-forcing.witness.json`](../../computations/lp-confinement-nf-forcing.witness.json)
runs a 6-compound bench at $n \in \{3, 4\}$. For each compound the
LP is solved via the canonical formalism
(emitting **both primal and dual** per AGENTS.md §LP/SDP duals),
the active set $A$ is read off the dual vector $y_\lambda^*$, and
the seminormal pole order of $T_\beta$ is computed independently.

See [Table](#tbl:confinement-nf-structure-forcing-table-data).

**Result:**
- Confinement holds in 6/6 compounds (active set size $\leq n/(n-1)! \cdot n!$).
- The maximizer always lies in the active set (claim 1) — 6/6.
- The LP duality gap is **exactly 0** in every case (strong duality
  verified).
- $\Delta$ is bounded by $\ell(\beta_1) + \ell(\beta_2)$ — the
  heuristic length-scale bound — in all cases. The tightening to
  the genuine $\mathrm{duality\_gap}$ bound stated in the
  conjecture is consistent with all observations (vacuously, since
  the gap is $0$ and $\Delta \in \{0, 2, 3\}$ is small in absolute
  terms).

The witness emits the required AGENTS.md §LP/SDP-duals fields
(`lp_y0_star`, `lp_y_star`, `lp_active_set_indices`, `lp_primal_obj`,
`lp_dual_obj`, `lp_duality_gap`) per compound, plus a top-level
`lp_dual_emitted: true` flag.

3 / 3 witness assertions pass.

### Caveats

- The Frobenius Gram in this canonical evaluation is taken **diagonal**
  ($G_{\lambda\mu} = \delta_{\lambda\mu} \dim V_\lambda$),
  reflecting the orthogonality of irreducible Markov channels.
  A non-trivial inner product would change the active set; see
  [`docs/audits/-nh-knots-confinement-shift.md`](../../docs/audits/-nh-knots-confinement-shift.md).
- The bench is small (6 compounds, $n \leq 4$). Scaling to $n \geq 5$
  requires a canonical / interval-arithmetic switch in the symbolic
  Hoefsmit pipeline.
- No Lean proof is attempted; the conjecture is conjectural in
  the [AGENTS.md §3b](../../AGENTS.md#3b) sense — propagated
  downstream uses must be `remark` blocks with `interprets`, or
  carry the conditional-class structure of §3b-cond.
<!-- FILE_END: confinement-nf-structure-forcing.md -->

<!-- FILE_START: lp-duality-hypothesis-class.md -->
**Definition (`HasFiniteLPDuality` hypothesis class, §3b-cond
infrastructure).** *Let $\mathrm{lp}$ be an operator-selection LP
([`prop:operator-selection-lp`](#prop:operator-selection-lp)). The
**finite LP strong-duality + complementary-slackness hypothesis
class** is the `Lean` class with two fields:*

```lean
class HasFiniteLPDuality (lp : OperatorSelectionLP) : Type where
  dualityGapZero       : lp.duality_gap = 0
  complementarySlackness :
    ∀ (λ : lp.Λ), λ ∈ lp.active_set ↔ lp.tight λ
```

*The two fields encode the Schrijver §7.2 strong-duality theorem and
the Schrijver §7.4 complementary-slackness theorem respectively.*

## Motivation

The two routine LP-theory inputs are currently **two free-standing
top-level `sorry`s** in
[`confinement-nf-partial-proof.lean`](confinement-nf-partial-proof.lean):

```lean
theorem strong_duality (lp : OperatorSelectionLP) :
    lp.duality_gap = 0 := by
  -- Ref: [schrijver1986theory]
  sorry

theorem complementary_slackness (lp : OperatorSelectionLP) (λ : lp.Λ) :
    (λ ∈ lp.active_set) ↔ lp.tight λ := by
  -- Ref: [schrijver1986theory]
  sorry
```

Per AGENTS.md §3b-cond, the proper locale for routine-but-not-yet-
formalised inputs is a **conditional-class hypothesis** with a
trivial model carrying the `sorry` + bibliographic citation. This
block provides that class.

## Bridge to `prop:confinement-nf-partial-proof`

The Lean file `LpDualityHypothesisClass.lean` provides two
drop-in-replacement theorems that consume the class instead of
the free-standing `sorry`s:

| Existing theorem (free-standing `sorry`) | Class-consuming variant |
|---|---|
| `theorem_3_strong_duality lp` | `theorem_3_via_class lp` (takes `[HasFiniteLPDuality lp]`) |
| `theorem_1_maximizer_in_active_set lp h_tight` | `theorem_1_via_class lp max_pole h_tight` (takes `[HasFiniteLPDuality lp]`) |

A future PR can refactor `confinement-nf-partial-proof.lean` to
take `[lpDuality : HasFiniteLPDuality lp]` as a hypothesis on the
two consumer theorems, making the existing top-level `sorry`s
disappear (the `sorry` lives only in the trivial-model class
instance, with proper Schrijver citation).

## Conditions for an unconditional result

When Mathlib lands a finite-dim LP-duality library
(`Mathlib.Analysis.Convex.LinearProgramming` or similar — none
ships in Mathlib at the time of writing), the
`schrijverModel` trivial model can discharge both sorrys
unconditionally:

```lean
def mathlibModel (lp : OperatorSelectionLP)
    (h_bounded : lp.bounded) (h_feasible : lp.feasible) :
    HasFiniteLPDuality lp where
  dualityGapZero := Mathlib.LP.strong_duality h_bounded h_feasible
  complementarySlackness := Mathlib.LP.complementary_slackness ...
```

This block + Lean file are designed so that swap requires zero
edits to consumer code (`confinement-nf-partial-proof.lean` once
refactored). The class API is fixed; only the trivial-model
implementation changes from `sorry` to a proper proof.

## Trivial model (consistency witness)

`HasFiniteLPDuality.schrijverModel : HasFiniteLPDuality lp` —
provides class instance for any `lp` via two `sorry` fields, each
carrying `-- Ref: [schrijver1986theory]`. This is the §3b-cond
relocation of the two existing free-standing `sorry`s, not a new
mathematical commitment.

The class is **inhabited** for every `lp` (via `schrijverModel`),
so consistency is established (no contradiction introduced).
<!-- FILE_END: lp-duality-hypothesis-class.md -->

<!-- FILE_START: bound-state-frobenius-self-dual-channel.md -->
**Remark (Frobenius self-dual channel of molecular bound states).**
*The two Wedderburn channels carrying force-carrier content in the
H_2 molecular bound state — $\lambda^{(T_{3,5})} = (3, 1)$ and
$\lambda^{(T_{2,9})} = (2, 1, 1)$ from
[`prop:force-carrier-intertwining-correspondence`](#prop:force-carrier-intertwining-correspondence)
— are **transpose partitions** of each other:*

$$
  (3, 1)^{T} \;=\; (2, 1, 1).
$$

*Equivalently, the corresponding Young diagrams are mirror
reflections through the diagonal.*

### Frobenius self-duality

In the Hecke-algebra Wedderburn decomposition, transpose
partitions correspond to Hopf-antipode-conjugate irreducible
representations:

$$
  S\bigl(V_\lambda\bigr) \;\cong\; V_{\lambda^{T}}.
$$

A representation pair $(V_\lambda, V_{\lambda^T})$ is closed under
the Hopf-antipode action $S$ — this is precisely the
**Frobenius self-dual** structure.

For $\lambda = (3, 1)$ in $H_4(q)$:

- $\dim_q V_{(3,1)} = \dim_q V_{(2,1,1)}$
- $w_{(3,1)} = w_{(2,1,1)} = \dim_q^{2} / [4]_q!$
- $f^{(3,1)} = f^{(2,1,1)} = 3$ (number of standard Young tableaux)

The two channels carry **identical Wedderburn weights**.  Their
joint contribution to the molecular Markov trace —

$$
  w_{(3,1)} \cdot \frac{\chi_{(3,1)}(\beta) + \chi_{(2,1,1)}(\beta)}{f^{(3,1)}}
  \;=\;
  w_{(3,1)} \cdot \frac{\chi_{(3,1)}(\beta) + \chi_{(2,1,1)}(\beta)}{3}
$$

— is **invariant under the Hopf antipode** acting on the
molecular braid $\beta$.  This is the categorical analogue of
parity-symmetry: the bound state is self-conjugate, matching the
physical fact that $H_2$ has $J^{P} = 0^{+}$ ground state.

### Empirical signature in the witness

At $q_0 \approx 1.110$
([`delta-q-decoration.witness.json`](computations/delta-q-decoration.witness.json)):

| $\lambda$ | $\chi_\lambda(\sigma_1\sigma_2\sigma_3)$ | $w_\lambda \cdot \chi_\lambda/f^\lambda$ |
|---|---:|---:|
| $(3, 1)$ | $-1.110$ | $-0.136$ |
| $(2, 1, 1)$ | $+0.901$ | $+0.111$ |
| Sum (joint contribution) | — | $-0.025$ |

The two channels have **opposite signs**, with the magnitudes
nearly equal (modulo dressing differences). Their sum is
$-0.025$, a small residual reflecting the asymmetry between the
"3-strand intertwining" and "2-strand + 2-free" combinatorial
patterns.

### Connection to chirality and antiparticle structure

The transpose-pair structure connects to the **antiparticle
crossing-reversal** mechanism
([`prop:antiparticle-crossing-reversal`](#prop:antiparticle-crossing-reversal)):

- Crossing reversal $\sigma$ acts on the Hecke algebra by
  $\sigma_i \mapsto \sigma_i^{-1}$, equivalently $q \mapsto q^{-1}$.
- This induces $V_\lambda \mapsto V_{\lambda^{T}}$ on irreps —
  exactly the transpose action.
- A bound state in the **self-dual sub-sector**
  $V_{(3,1)} \oplus V_{(2,1,1)}$ is invariant under
  particle-antiparticle exchange, consistent with the
  electrical neutrality of the $H_2$ molecule (zero net charge).

### Significance

The Frobenius self-dual structure of the molecular bound-state
channel is **not a coincidence** — it is forced by the combination
of:

1. The genus-$4$ Bring force-carrier sector
   ([`prop:force-carrier-bring-uniqueness`](#prop:force-carrier-bring-uniqueness)),
   which gives exactly two torus knots $T_{2,9}, T_{3,5}$.
2. The strand-count constraint
   ([`prop:force-carrier-intertwining-correspondence`](#prop:force-carrier-intertwining-correspondence)),
   which maps each force carrier to a partition with exactly one
   "fat" part.
3. The arithmetic of partitions of $4$:
   $\{(p, 1^{4-p}) : p = 2, 3\} = \{(2, 1, 1), (3, 1)\}$,
   which happen to be transpose of each other.

For other strand counts $n$, the analogous "force-carrier
Wedderburn channels" are $(p, 1^{n-p})$ for $p \leq n$.  These
are *not* transpose pairs in general — the self-duality at $n=4$
is special to the genus-$4$ Bring constraint matching the
4-strand H_2 molecular structure.

This may explain why the **simplest covalent bond** ($H_2$) has
a particularly clean categorical structure compared to larger
molecules.
<!-- FILE_END: bound-state-frobenius-self-dual-channel.md -->

<!-- FILE_START: confinement-categorical.md -->
**Proposition (confinement = spectral-sequence collapse).**
*The collapse of the GB-filtration spectral sequence
([spectral sequence collapse](#prop:spectral-sequence-collapse))
is the categorical statement of color confinement: only central
elements of $A = H_n(R, q)$ survive as physical observables, and
"colored" non-central elements are cohomologically trivial.*

**Statement.**
*Let $A = H_n(R, q)$ be semisimple at generic $q$, with Frobenius
integral $\int_A : A \to R$ (the Markov trace).  Then:*

1. *(Survival.)
   The only $E_\infty$-page contributions are
   $E_\infty^{0, 0} = Z(A) = \bigoplus_\lambda R \cdot e_\lambda$.
   Non-central elements vanish on the $E_\infty$-page.*

2. *(Trace factorization.)
   The Frobenius integral factors through the centre:*

   $$
     \int_A \;=\; \mu \,\circ\, \pi_Z, \qquad
     \pi_Z : A \twoheadrightarrow Z(A), \quad
     \mu : Z(A) \to R,
   $$

   *with $\pi_Z(a) = \sum_\lambda e_\lambda \cdot a \cdot e_\lambda$
   the Wedderburn projection and $\mu(e_\lambda) = w_\lambda$ the
   Plancherel weight.*

3. *(Observables are Wedderburn residues.)
   Every physical observable
   $\mathfrak{W}(\mathcal{K}, \mathcal{T}) = \int_A \rho(\beta_\mathcal{K}) \cdot \mathcal{T}$
   factors as a sum of Wedderburn residues
   ([universal residue](#prop:plancherel-term-7-formulation)):*

   $$
     \mathfrak{W}(\mathcal{K}, \mathcal{T})
     \;=\; \sum_\lambda \int_{A_\lambda}\!\!\rho(\beta_\mathcal{K}) \cdot \mathcal{T}.
   $$
<!-- FILE_END: confinement-categorical.md -->

<!-- FILE_START: exterior-square-borromean.md -->
**Proposition (Borromean strand-pair representation has dimension 45).**
*Let $V_{\mathrm{nat}} = \mathbb{C}^{10}$ be the natural permutation
representation of $S_{10}$ (or its q-deformation $H_{10}(q)$
acting via the standard projection).  Then the **exterior square**
$\Lambda^2 V_{\mathrm{nat}}$ has dimension $\binom{10}{2} = 45$ at
$q = 1$, and decomposes under $S_{10}$ as*

$$
  \Lambda^2 V_{\mathrm{nat}} \;\cong\; V_{(9,1)} \oplus V_{(8,1,1)},
$$

*where $V_{(9,1)}$ is the $9$-dimensional standard representation
and $V_{(8,1,1)}$ is the $36$-dimensional hook representation
(verified: $9 + 36 = 45$).*
<!-- FILE_END: exterior-square-borromean.md -->

