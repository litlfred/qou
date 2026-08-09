# #P-hard Jones → P≠NP: robustness infrastructure (Mathlib survey + surreal-level grade brick)

**Date.** 2026-08-09.
**Branch.** `claude/pneqnp-robustness-mathlib-infra-2026-08-09`.
**Beans.** milestone `qou-894c`; tasks `qou-h6uw` (Mathlib survey),
`qou-xnln` (sharpen the transfer to a single named hypothesis),
`qou-unl7` (surreal-level brick), `qou-u8ok` (game-birthday assessment).

**One-line honest verdict.** The step *"exact Jones evaluation at a
non-lattice root of unity is #P-hard ⟹ P≠NP"* remains **open** and is
**not made less open** by anything in this branch. What this branch does is
**shrink and name** the gap: it isolates the entire remaining content into a
**single** implication — the counting→decision *transfer*
`(exact-Jones ∉ FP) ⟹ (P ≠ NP)` — states precisely what is known to *block* a
generic proof of that implication (Toda, algebrization, natural proofs), and
adds a sorry-free **surreal-level "grade brick"** that formalizes the honest
*sub*-claim "exponential-in-length cost sits at a strictly higher ω-grade
(transseries level) than any polynomial budget." The brick is real
mathematics; it is **not** P≠NP and does not pretend to be.

---

## 1. Survey — what Mathlib complexity/computability actually offers (task `qou-h6uw`)

I inspected the Mathlib computability/complexity surface. Findings:

| Module | What it gives | What it does NOT give |
|---|---|---|
| `Mathlib.Computability.TuringMachine` | `Turing.TM0`, `TM1`, `TM2` machine models; tape/step semantics; `Turing.TM2ComputableInPolyTime` scaffolding pieces | no complexity *classes* |
| `Mathlib.Computability.Halting` | `Nat.Partrec`, the halting-problem undecidability, `ComputablePred` | no *time*-bounded predicate |
| `Mathlib.Computability.TMComputable` | `Turing.TM2ComputableInTime`, `Turing.TM2ComputableInPolyTime` — a machine computes a function within a stated *time bound* (`Turing.TM2ComputableInTime … (fun n => …)`) | no `P`, no `NP`, no `#P`, no reductions between decision problems as *classes* |
| `Mathlib.Computability.PartrecCode` | Gödel-numbering of partial recursive functions (`Nat.Partrec.Code`) | — |
| `Mathlib.Computability.TMToPartrec` | equivalence TM ↔ partrec | — |
| `Mathlib.Computability.Reduce` | many-one reducibility `≤₀` on *sets* (decidability reductions), `ManyOneDegree` | this is **computability**-reducibility (decidable/undecidable), **not** poly-time reducibility; it cannot express `≤ᵖ` |

**Bottom line.** Mathlib has Turing machines and a *time-bounded computation*
predicate (`TM2ComputableInTime` / `TM2ComputableInPolyTime`) but **no P / NP /
#P classes and no polynomial-time many-one reduction**. `Computability.Reduce`
is the *computability* (Turing/many-one on decidability) reduction, which is the
wrong granularity — it identifies degrees of undecidability, not
polynomial-time complexity.

### What minimal, honest scaffolding IS buildable

- **A time-bounded-acceptance predicate over `TMComputable`.** One could define
  `AcceptsInTime (M) (bound : ℕ → ℕ)` by wrapping
  `Turing.TM2ComputableInTime` on the decision function `ℕ → Bool`. This is
  *honest* — it is literally Mathlib's own time-bounded predicate — but it buys
  little: to state "P" one still needs to quantify over *all* machines and
  *all* polynomial bounds, and to state "NP" one needs a verifier + certificate
  existential. Both are expressible in principle; neither is in Mathlib, and
  writing them is a multi-hundred-line development that would still bottom out
  in the *same* opaque hardness facts (JVW #P-hardness is a *pen-and-paper*
  theorem no Lean library proves).
- **A poly-bounded predicate on `ℕ → ℕ` cost functions.** This the corpus
  *already* has and uses — `PolyBounded` / `SuperPolynomial` in
  `QOU.Information.SurrealBudgetGrade` / `PhysicalIntractability`. This is the
  right, honest granularity for the QOU argument: it reasons about the *cost*
  of the skein resolution-tree observation, not about literature Turing
  machines. **This is what the surreal brick (§3) builds on.**

### What must stay an opaque cited class

- **#P-hardness of exact Jones evaluation** (Jaeger–Vertigan–Welsh,
  [jaeger1990]) — a literature theorem Lean cannot currently prove; carried as
  the cited hypothesis class `JonesComplexityCitations` (already on `main`,
  `PNeqNpEquivalence.lean`). No instance — a fabricated instance would launder
  the literature into a Lean "proof."
- **NP ⊆ P^#P** ([arora2009]) — likewise a cited field of the same class
  (`counting_dominates_decision`).
- **P, NP, #P themselves** — opaque `Prop` parameters. Mathlib has no
  formalisation; asserting one would add fake precision (AGENTS.md
  §"Axiomatization is NOT a Proof").

**Do not overclaim.** Building the `TMComputable`-based scaffolding would make
the *statements* look more like the literature, but it would **not** close the
gap — the gap is a mathematical transfer theorem, not a missing definition.
The honest move is to keep P/NP opaque and name the transfer precisely (§2).

---

## 2. Sharpening the transfer to a single named hypothesis (task `qou-xnln`)

### The genuinely-true, citable facts

1. **`#P`-hardness of exact Jones at `q₀`.** For a parameter that is not a
   lattice root of unity — in particular the non-torsion substrate
   `q₀ ≈ 1.10998`, which `nontorsion_of_one_lt` proves is non-torsion in
   `𝔾_m(ℝ)` — exact evaluation of the Jones polynomial is `#P`-hard
   (Jaeger–Vertigan–Welsh, [jaeger1990]; Vertigan). Carried as
   `JonesComplexityCitations.jvw_sharp_p_hard`.
2. **`NP ⊆ P^#P`** ([arora2009]); equivalently `FP = #P ⟹ P = NP`. Carried as
   `JonesComplexityCitations.counting_dominates_decision`.
3. **Semisimplicity of `H_n(q₀)`** at `q₀ > 1` (Wenzl genericity,
   `wenzlGeneric_of_one_lt`, sorry-free) — the "no radical pruning of the
   resolution tree" leg. Modulo the cited Wenzl criterion, the semisimplicity
   hypothesis of the counting bound is *discharged* for the real substrate.

### The single open piece (this is the whole gap)

> **THE named hypothesis.** `transfer : (exact-Jones ∉ FP) ⟹ (P ≠ NP)`.

In `PNeqNpEquivalence.lean` this is the `transfer` argument of
`faithfulness_of_transfer`. **Discharging `transfer` (together with the weaker
counting separation `FP ≠ #P`, itself open) IS proving the conjecture.** Every
other leg is either a sorry-free lemma or a cited literature class.

Why the transfer is not free: `#P`-hardness of *one* invariant does **not**
imply `FP ≠ #P` (that is the `FP = #P` question), and `FP ≠ #P` does **not**
imply `P ≠ NP` — the counting separation is *weaker* than the decision
separation (`counting_sep_of_decision_sep : ¬(P=NP) → ¬(FP=#P)`, one direction
only). So the transfer must manufacture a decision separation from a counting
one, against the grain of the known inclusion.

### What is known to BLOCK a generic proof of the transfer

- **Toda's theorem** (`PH ⊆ P^#P`): the entire polynomial hierarchy is
  #P-easy. So "#P is hard" is *consistent with* `P = NP` — a generic
  counting→decision transfer would have to defeat Toda's collapse, i.e. it
  cannot be a black-box counting argument. This is the sharpest single reason
  the step is "an analogy, not a theorem."
- **Algebrization** (Aaronson–Wigderson 2008): any separation whose proof
  relativizes *and* algebrizes cannot separate P from NP. The skein
  observable / Markov trace is *polynomial data* (an algebraic invariant), so a
  separating residue extracted from it algebrizes and is barred. The corpus
  already records this (`SkeinObservationBridge.lean` docstring;
  `SkeinHorizonLowerBound.no_horizon_cost_of_polyObservable`): the separating
  invariant must be **non-algebraic** — a class in `H₁(Σ₄)/HH²(U_q)`, the
  genus-4 Bring residue — precisely because a polynomial shortcut would refute
  the `correct` (black-box) hypothesis of every horizon lower bound.
- **Natural proofs** (Razborov–Rudich): a "natural" (largeness + constructivity)
  circuit lower bound cannot separate under standard crypto assumptions. The
  QOU residue would need to be non-natural — the topological/cohomological
  character of the `χ(A)` residue is the corpus's proposed escape, but this is
  a *hope*, not a discharge.

**Honest status of the transfer.** It routes through a **non-algebraic,
non-natural** separating invariant that defeats Toda's collapse. The corpus
*names a candidate* for that invariant (the genus-4 residue) but does **not**
prove it non-algebraic. That non-algebraicity proof is the actual P≠NP-hard
core and stays open (coordination ledger `skein-observation-bridge.md`
"Next non-overlapping task").

---

## 3. The surreal-level grade brick (task `qou-unl7`) — sorry-free

New module `QOU/Information/SkeinSurrealGrade.lean`. This formalizes the honest
core of "complexity ↔ surreal birthday/length", **as a conditional whose
hypothesis is the growth bound** (formalize-first: the growth bound is the
honest input; the grade gap is *derived*).

### The mathematics

- **Transseries level = ω-grade.** Berarducci–Mantova: the surreals are the
  universal transseries field; a growth function's *level* orders it against
  iterated exp/log. In the coarser ω-monomial grade the corpus already uses,
  `nᵏ` has magnitude `ωᵏ` (finite) and `2ⁿ` has magnitude above every `ωᵏ`:
  this is exactly `SuperPolynomial` vs `PolyBounded`, i.e.
  `ord_ω(2ⁿ) > ord_ω(nᵏ)` for every `k`. The `P ⊊ EXP` band-gap reads as this
  ω-grade strict inequality — proved sorry-free on `main`
  (`not_polyBounded_of_superPoly`, the "surreal squeeze").
- **`len` is the finite birthday shadow.** A finite braid word's surreal
  sign-expansion length is literally its `ℕ` length, and the birthday of a
  finite ordinal `n` is `n`. So the ℕ-valued filtration
  `SkeinObservationSystem.len` is the *finite (birthday `< ω`, archimedean)
  shadow* of the surreal length. The exponential blow-up lives in the **cost
  as a function of** this level — `3^{len}` — never in the level of any single
  word (`birthdayShadow_lt_omega0`).

### The brick (decl signatures, all sorry-free)

- `SkeinObservationSystem.birthdayShadow (sys) (P) : Ordinal := (sys.len P : Ordinal)`
  and `birthdayShadow_lt_omega0 : sys.birthdayShadow P < Ordinal.omega0` — the
  finite-band placement of a single state.
- `LevelZero (g : ℕ → ℕ) : Prop := PolyBounded g` (transseries level 0 band).
- `LevelGeOne (g : ℕ → ℕ) : Prop := SuperPolynomial g` (level ≥ 1 band).
- `level_gap : LevelGeOne g → ¬ LevelZero g` — the level bands are disjoint
  (the ω-grade squeeze), the honest core of `P ⊊ EXP`.
- `levelGeOne_of_exp_growth : (∀ n, 2 ^ n ≤ g n) → LevelGeOne g` — **the
  conditional**: the *hypothesis is the exponential growth bound*, the level-≥1
  grade is *derived*.
- `horizonCostOfLen (lenFamily : ℕ → ℕ) : ℕ → ℕ := fun n => 3 ^ (lenFamily n)`.
- `two_pow_le_horizonCostOfLen : (∀ n, n ≤ lenFamily n) → ∀ n, 2^n ≤ horizonCostOfLen lenFamily n`.
- **Main brick** `horizonCostOfLen_levelGeOne : (∀ n, n ≤ lenFamily n) → LevelGeOne (horizonCostOfLen lenFamily)`
  and `not_levelZero_horizonCostOfLen : (∀ n, n ≤ lenFamily n) → ¬ LevelZero (horizonCostOfLen lenFamily)`
  — **conditional on the linear-in-length growth hypothesis** `hlin`, the
  horizon cost is level ≥ 1, so no polynomial budget dominates it.
- **Corpus cross-check** `horizonCostOfLen_boundary_eq_physicalCost :
  horizonCostOfLen (fun n => 3 * n) = physicalCost` — the boundary family
  (`c = 3N` crossings, `len =` crossing count) recovers the corpus
  `physicalCost = 3^{3n}`, and `horizonCostOfLen_levelGeOne` re-derives
  `physicalCost_superPoly`. This anchors the abstract brick to the already-proved
  `#P`-over-moduli result.
- **Single-instance shadow** `not_polyObservable_id_of_birthday_horizon` — ties
  the birthday-shadow horizon cost `3^{len P}` of one state to
  `SkeinObservationSystem.not_polyObservable_id_of_horizon_cost` (the existing
  bridge lemma), in surreal-grade language.

### What the brick honestly is — and is NOT

- **IS:** a machine-checked statement that *exponential-in-length observation
  cost occupies a strictly higher transseries level (ω-grade) than any
  polynomial budget*, with the growth bound as an explicit hypothesis and the
  grade gap derived. It is the surreal-language home for the `P ⊊ EXP`-shaped
  sub-fact the QOU horizon actually supports (bandwidth-limited / query-model).
- **IS NOT:** P≠NP. The hypothesis `hlin`/`hgrow` (the cost really is
  exponential in the length) is the *black-box / no-shortcut* assumption that
  algebrization bars from crossing to the decision axis. The brick constrains
  *magnitude vs budget*; it says nothing about whether a **decision** procedure
  can shortcut the observation via an algebraic (polynomial) invariant. That
  crossing is §2's open `transfer`. (Scope-(a) negative, AGENTS.md: this is a
  "cost-alone" statement, not a structural exclusion of a poly decision route.)

---

## 4. Game-birthday angle (task `qou-u8ok`) — real structure or analogy?

Claim under assessment: *PSPACE / PH alternation ↔ the birthday of the Skein
ternary resolution-tree game.*

**Verdict: analogy, not (yet) real structure — with one genuine hook.**

- **The genuine hook.** The skein resolution tree *is* a finite ternary game
  tree (three channels `L₊ / L₋ / L₀` per crossing), and the alternation depth
  of a game tree is a bona-fide ordinal (its game-birthday in the Conway sense).
  The QBF/alternation ↔ game-tree-depth correspondence is standard (PSPACE =
  the poly-depth alternating tree). So there *is* a well-defined birthday of the
  resolution game, and it is finite (= tree depth = `O(c)` = `O(len)`).
- **Why it is only an analogy here.** (i) The Skein tree's leaves are *summed*
  (a trace / counting object), not *alternated* (∃/∀). Counting over a tree is
  `#P`; alternation over a tree is `PSPACE`. Reading the *same* tree as an
  alternating game is a **different** semantics on the same combinatorial
  object — the corpus's observable is the Markov trace (a sum), so the
  operative class is `#P`, not `PSPACE`. (ii) The game-birthday is finite
  (`O(c)`), so it lands in the same *finite birthday band* (`< ω`) as `len`
  itself — it does **not** supply a new ω-grade separation. The birthday that
  matters for the ω-grade argument is the birthday of the *cost-as-function-of-
  size*, not of one tree.
- **Where it could become real.** If one defined an *alternating* skein
  semantics (min/max over channels instead of sum) whose value is the degree-0
  observation, the alternation depth would be a genuine PSPACE-flavoured
  invariant and its transfinite iteration (a *tower* of trees indexed by
  problem size) would have an ω-or-higher birthday. That is not in the corpus
  and is not claimed here. Recorded as a candidate, not a result.

---

## 5. Files

- `content/quantum-observable-universe/lean/QOU/Information/SkeinSurrealGrade.lean` — the brick (new, sorry-free).
- Registered in `content/quantum-observable-universe/lean/QOU.lean`.

Nothing wired to production; no content block promoted. The two cited classes
(`JonesComplexityCitations`, `WenzlCriterion`) remain instance-free.
