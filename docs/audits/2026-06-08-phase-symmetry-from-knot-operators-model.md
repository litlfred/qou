# Phase symmetry from knot operators — the matter-state hierarchy

**Date:** 2026-06-08
**Branch:** `claude/gallant-bohr-w9f6a6` (PR #1999), frontier thread
**Status:** design / model doc — captures the owner's mechanism before
committing to content-block structure. Content blocks (the proposition +
H₂O phase examples) follow once this design settles.

## 0. The owner's model (verbatim distillation)

Across 2026-06-08 the owner specified the mechanism:

1. **`q` determines the available phases.** The substrate parameter sets
   the *confinement-level* ladder of the "molecular meta-structure" —
   which phases of matter are stable at all.
2. **The knot determines the energy cost** of each phase transition, via
   the *existing* phase-transition formulae (`[n_K]_q`).
3. **Temperature is the likelihood of interactions** — it drives the
   inter-molecular knot operations that move between phases.
4. **Each phase has a specific symmetry, inherited from the knot
   operator that formed it.** Gas, liquid, ice are reached by distinct
   inter-molecular braiding operations; the symmetry of the resulting
   link IS the phase's symmetry.
5. **That phase symmetry explains electron-shell structure in crystals**
   (crystal-field splitting, bands, "electron shells on crystals").

This is the fully-specified form of the session-opening hypothesis:
*hierarchies of matter-states are based on the knot symmetries of the
constituent parts.*

## 1. The three-level hierarchy

```
 q  ─────────────►  confinement levels J^ℓ(q)  ─────►  AVAILABLE PHASES
(substrate)          (def:confinement-level)            {gas, liquid, solid,…}
                                                              │
 knot operator that REACHES a phase  ──── energy cost ───────┤  (when)
   (inter-molecular braiding)        ──── symmetry  ─────────┤  (what shape)
                                                              ▼
                                              PHASE SYMMETRY (point/space group)
                                                              │
                                              acts on Hopf-trefoil shells
                                                              ▼
                                       ELECTRON-SHELL STRUCTURE IN THE PHASE
                                       (crystal-field splitting, bands)
```

- **Level 1 (q → phases).** [`def:confinement-level`](../../content/quantum-observable-universe/particle-interactions/confinement-level.md):
  the filtration `J^ℓ(q)` sorts Wedderburn-block knot operators by energy;
  a phase = a confinement stratum, and `q` fixes which strata are
  non-empty. *This is why the phase set is q-dependent.*
- **Level 2 (knot operator → cost + symmetry).** The transition
  gas→liquid→solid is a sequence of inter-molecular **knot operations**
  (§3). Each operation has (a) an **energy cost** from the existing
  [`prop:phase-transition-boundary`](../../content/quantum-observable-universe/information-theory/phase-transition-boundary.md)
  `[n_K]_q` machinery, and (b) a **symmetry** = the automorphism group of
  the resulting link. *This is the new content.*
- **Level 3 (phase symmetry → shells).** The phase symmetry reduces the
  free-atom shell symmetry, splitting/banding the Hopf-trefoil shells
  ([`def:electron-shell`](../../content/quantum-observable-universe/predicted-spectra/electron-shells-hopf.md)).
  *This is the "electron shells on crystals" consequence.*

## 2. H₂O as the worked example — the molecular braid

Following the CH₄ template ([`def:ch4-molecular-braid`](../../content/quantum-observable-universe/molecular-construction/ch4-molecular-braid.md)),
H₂O is the bent, lone-pair variant:

- **Constituents:** one oxygen `O(8,8) ∈ H₂₄(q)` (A+Z = 16+8 = 24
  strands), valence 2 + **2 lone pairs**
  ([`valence-from-braid`](../../content/quantum-observable-universe/molecular-construction/valence-from-braid.md));
  two hydrogens `H_k ∈ H₂(q)`.
- **Molecular braid:** `M(O, H₁, H₂) ∈ H₂₈(q)` (24 + 2 + 2). Two single
  O–H σ-bonds = 2 shared electron trefoils, each Hopf-linked O↔H (2
  attractive `σ⁻¹` crossings per bond).
- **Geometry (LP dual, no geometric input):** exactly the CH₄
  computation with **2 of the 4 tetrahedral sites occupied by lone
  pairs** acting as "phantom hydrogens" (the NH₃ → H₂O extension of
  [`ch4-tetrahedral-symmetry`](../../content/quantum-observable-universe/molecular-construction/ch4-tetrahedral-symmetry.md)):
  Td → **C₂ᵥ**, bond angle pushed from 109.5° toward the observed
  **104.5°** by the two lone-pair "phantom" sites.
- **The four directions that matter for ice:** 2 donor H's + 2 acceptor
  lone pairs = **4 ≈-tetrahedral H-bond directions per molecule.** These
  are intrinsic to the H₂O braid and are what tile into the lattice.

## 3. The phase ladder = inter-molecular Hopf-link count

A phase transition is microscopically a **knot operation on the
inter-molecular link**, not on the single-molecule braid:

| phase | inter-molecular Hopf links per H₂O | link symmetry | Hecke channel |
|-------|-----|-----|-----|
| **gas** | 0 (free molecules) | full permutation `S_N` (no order) | symmetric (eigenvalue `q`) |
| **liquid (water)** | partial / fluctuating (≈3.4 avg, transient) | broken, dynamic — a **simple Hopf link** between transient pairs | mixed channel |
| **solid (ice Ih)** | **4 rigid** (2 donor + 2 acceptor) | tetrahedral vertex → **hexagonal P6₃/mmc** | antisymmetric (eigenvalue `−q⁻¹`) |

- **gas → liquid:** the knot operator forms a **Hopf link** between two
  previously-unbound H₂O (owner: "a simple knot like Hopf"). Cost set by
  `[n_K]_q` at the liquid confinement level.
- **liquid → ice:** the operator rigidifies each molecule's links to the
  full **4-coordinate tetrahedral vertex**; these vertices tile into the
  hexagonal ice network at a further energy cost.

This dissolves the §-prior naive ratio puzzle
([`2026-06-08-phase-transition-ratio-formalize-first.md`](2026-06-08-phase-transition-ratio-formalize-first.md)):
the "knot" in `[n_K]_q` is the **inter-molecular link** being formed, and
its `q` is the **confinement-level q of that phase** — not q₀ evaluated
on the single-molecule diagram. Owner: *"it depends on knot and q
value."* Correct — and they are the *inter-molecular* knot and the
*phase's* q.

## 4. Crystal structure of ice (owner's direct question)

**Ice Ih is hexagonal** (space group `P6₃/mmc`); O atoms on a
wurtzite-type hexagonal lattice, each tetrahedrally H-bonded to 4
neighbours. Reconciling the owner's two guesses:

- **"parallelogram lattice"** ✓ the hexagonal primitive cell is a 120°
  rhombus (parallelogram).
- **"triangular lattice"** ✓ the hexagonal lattice points form a
  triangular net in the basal plane.
- **the load-bearing fact:** local coordination is **tetrahedral**
  (≈109.5°), set by the molecule's 4 H-bond directions (§2). Tetrahedral
  vertices + the constraint that they tile periodically ⇒ the open
  hexagonal Ih network (also why ice is *less dense* than water — the
  tetrahedral network is open, not close-packed).

**Proton disorder / residual entropy.** Each O has 4 H-bonds but only 2
carry "its" H (Pauling ice rules); the choice of which 2 of 4 is
disordered, giving residual entropy `≈ R ln(3/2)`. In framework terms:
the 4 Hopf links are present but only 2 are **donor-oriented** — this is
exactly the **mixed-channel partial occupation** of the link, and is a
clean target the framework should reproduce (Pauling's `(3/2)` from the
2-of-4 Hopf orientation count).

## 5. Phase symmetry from the knot operator (the new proposition)

**Claim.** The symmetry group of a phase equals the automorphism group of
the inter-molecular link produced by the phase-forming knot operator:

`Sym(phase) = Aut(L_operator)`.

- gas: `L = ∅` ⇒ `Aut = S_N` (full exchange, structureless).
- ice Ih: `L =` the tetrahedral-vertex Hopf network ⇒ `Aut = P6₃/mmc`.

Backbone already proven: [`cor:knot-factor-borromean-composite`](../../content/quantum-observable-universe/mass-theory/knot-factor-borromean-composite.md)
shows a composite link's invariants **factor through** the constituent
links' invariants — i.e. constituent knot symmetry composes into the
composite. The phase-symmetry claim is the condensed-matter instance:
the lattice's symmetry is *assembled from* the per-molecule Hopf-vertex
symmetry. This is the formal form of "phase symmetry ← knot operator."

## 6. Electron shells in crystals (the owner's payoff question)

Free-atom electron shells = Hopf-linked trefoils with the full rotational
symmetry of the isolated Hopf chain
([`def:electron-shell`](../../content/quantum-observable-universe/predicted-spectra/electron-shells-hopf.md)).
Put the atom in a phase and the **phase symmetry (§5) acts on the shell
trefoils**:

1. **Crystal-field splitting.** The lattice point group (from the knot
   operator) reduces the free-atom shell symmetry, *splitting* a
   degenerate shell into sub-levels labelled by the point group's
   irreps — categorically, the shell's Hopf sub-links that were
   exchange-equivalent under `SO(3)` are no longer equivalent under
   `P6₃/mmc`. This is crystal-field theory with the point group *derived*
   from the phase-forming knot operator, not imposed.
2. **Band formation = extended threading link.** Benzene's delocalised π
   electrons are the **threading link `T(2,6)`** spanning the 6-ring
   ([`benzene-threading-emergence`](../../content/quantum-observable-universe/molecular-construction/benzene-threading-emergence.md)).
   A crystal is the **3-D periodic extension**: the outer-shell trefoils
   Hopf-link into a lattice-spanning threading link, delocalising into a
   **band**. The transfer-matrix / Chebyshev recurrence of
   [`prop:shell-structure-eigenvalues`](../../content/quantum-observable-universe/predicted-spectra/shell-structure-eigenvalues.md)
   becomes the **band dispersion** when iterated over the lattice (the
   Chebyshev `U_{n-1}` over `n` sites = a tight-binding band).
3. **Why ice is an insulator:** the tetrahedral Hopf network is fully
   *closed* (every shell trefoil in a complete sub-link) — no open
   threading link spans the lattice ⇒ no conduction band ⇒ wide gap.
   Contrast a metal: an *open* outer threading link ⇒ partially filled
   band.

So "electron shell structure on crystals" = the phase-symmetry from the
knot operator acting on the Hopf-trefoil shells: **splitting** (point
group) + **banding** (extended threading link). One mechanism, both
effects.

## 7. Content blocks to author (build plan for the frontier thread)

On the *fixed* molecular chapter (per the currency audit):

1. `def:h2o-molecular-braid` (+ `.md` + `.lean`) — §2, CH₄-analogous,
   in molecular-construction §"Water".
2. `rem:h2o-bent-geometry` — C₂ᵥ + 104.5° from 2 lone-pair phantom sites.
3. `def:intermolecular-hopf-phase` — the phase = inter-molecular
   Hopf-link count ladder (§3).
4. `prop:phase-symmetry-from-knot-operator` — `Sym(phase)=Aut(L)` (§5),
   built on `cor:knot-factor-borromean-composite`. (Conjecture or
   §3b-cond conditional, depending on what is provable.)
5. `ex:ice-Ih-hexagonal` — the tetrahedral-vertex → P6₃/mmc tiling +
   the Pauling 2-of-4 residual-entropy reading (§4).
6. `rem:electron-shells-in-crystal` — crystal-field splitting + band =
   extended threading link (§6), `interprets` the phase-symmetry prop.

All at **q₀** (per the owner's q-regime decision). Numerical claims
reported **tiered**; the inter-molecular `[n_K]_q` energies need the
canonical compute (currently sandbox-blocked — see currency audit) so
they land as a witnessed follow-up.

## 8. Open questions for the owner

1. **Provability of §5.** Is `Sym(phase)=Aut(L)` a clean theorem from
   `cor:knot-factor-borromean-composite`, or a conjecture? (Affects block
   kind — proposition vs conjecture.)
2. **Liquid channel.** Is liquid the *mixed* Hecke channel (transient
   partial Hopf links) as in §3, or a distinct confinement level? The
   `phase-transition-interpretation` block says mixed channel — confirm.
3. **Scope of the frontier PR.** Author all of §7 in PR #1999, or split
   the ice-lattice/electron-shell blocks (5,6) into a follow-up once the
   H₂O + phase blocks (1–4) are reviewed?
