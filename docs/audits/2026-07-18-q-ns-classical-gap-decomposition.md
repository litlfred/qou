# q-NS classical resolution (q → 1): gap decomposition + attack plan

**Date:** 2026-07-18
**Branch:** `claude/q-ns-classical-gaps-9l9mj9`
**Scope:** the *entire classical* side of the q-Navier–Stokes program — everything
that must hold for the QOU categorical obstruction `NS(A) ≠ 0` to entail an actual
finite-time singularity of the classical incompressible 3D Navier–Stokes equation
(the Clay Millennium formulation).

This doc **decomposes** each open gap into the smallest formalizable sub-claims,
assigns an **epistemic tier**, identifies **what is provable now vs. the genuine
hard wall**, and records three **critical-distance findings** the decomposition
surfaced. It builds on (does not duplicate) the prior triage
[`2026-05-09-conjecture-closure-tractability.md`](2026-05-09-conjecture-closure-tractability.md)
and the cone-quarantine memo
[`2026-05-02-cone-reduction-fluid-bridge.md`](2026-05-02-cone-reduction-fluid-bridge.md).

---

## 0. Honest framing (read first)

The q > 1 side is settled inside the framework: `thm:q-ns-wellposedness` gives global
regularity of the *q-deformed* flow for every `q > 1` (UV damping `[k]_q ~ q^k`, an
enstrophy bound, and uniqueness). **That is not the Clay problem.** The Clay problem is
the single limit `q → 1⁺`, where the deformation that makes the q > 1 proof work
switches off. Every one of the five items below lives entirely at, or across, that
limit.

The master gap is a **transfer statement**, not a computation:

> **Bridge (B).** The categorical obstruction class `NS(A) = e(ξ)|_Σ ∈ H²(Σ, 𝓑)`
> evaluating to `≠ 0` (which it does, unconditionally, from `χ(A) = −6`) *entails*
> that the classical incompressible 3D NS equation, specialised via `q = 1` from the
> q-NS system, develops a finite-time singularity from smooth finite-energy data.

**Bridge (B) is the Clay problem in the blow-up direction.** Proving it is not a matter
of wiring or Lean plumbing — it would be a Fields-medal-level analytic result. The
categorical side (`NS(A) ≠ 0`) is a statement in `H²` of the collision locus of the
*substrate*; the classical side is a statement about weak/strong solutions of a PDE on
`ℝ³`. Nothing in the corpus connects the two rings of definitions. **No agent should
represent Bridge (B), or any of the five sub-items, as closed, closable-by-code, or
"proved modulo wiring."** The correct end-state for the genuinely-open pieces is an
honest, content-bearing *primary-conjecture class* with **no instance** (AGENTS.md
§3b-tax), and downstream results stated *conditional on it*.

What *is* tractable, and what this program delivers, is everything **short of** Bridge
(B): honest naming of the wall, internal-consistency repair, literature de-risking, and
conditional formalization. Those are real, landable contributions. Bridge (B) itself
stays open.

---

## 1. The q-NS conjecture cone (dependency map)

Five class-axiomatised conjectures + one dichotomy carry the classical side. From the
Lean siblings and `uses[]`:

```
conj:regularity-breakdown ─┐  (master classical conjecture: ∃ v₀ ⇒ finite-T blow-up)
conj:critical-exponent ────┤
conj:blowup-yekutieli ─────┼─→ prop:core-levi-form ─→ prop:vorticity-lower-bound
conj:q-aubin-lions ────────┤        (all five carried as [Instance] hypotheses)
conj:ns-counterexample ────┘
conj:levi-degeneracy  (dichotomy A/B — the branch that is undecided)

def:ns-obstruction : NS(A) ∈ H³_loc(A,Θ)   ⟶   NS(A)=e(ξ)|_Σ ∈ H²(Σ,𝓑)   [categorical, unconditional]
        │
        └───────── Bridge (B) ─────────→  classical 3D NS finite-time singularity   [OPEN = Clay]
```

Prior cone-quarantine (2026-05-02) already severed the spurious cross-chapter leak, so
the cone is confined to `fluid-dynamics/`. Prior tiering (2026-05-09) put
`q-aubin-lions`, `ns-counterexample`, `critical-exponent`, `blowup-yekutieli`,
`regularity-breakdown` at **Tier C (open famous math)** and `levi-degeneracy` at Tier B
(real-parameter projection formalizable; full ℂ awaits Mathlib root-of-unity). This doc
does not move any tier — it decomposes the *proof approach* underneath each.

---

## 2. Gap-by-gap decomposition

Each gap: **sub-claims → tier → attack route → provable-now vs. wall.**
Tiers: `proved` · `symbolic-exact` · `conditional` (+ named hypothesis) · `heuristic`
(scaling/closure) · `open-analytic` (genuine PDE wall).

### Gap 1 — The categorical→classical bridge (Bridge B). **The core gap.**

| Sub-claim | Tier | Note |
|---|---|---|
| B0. `NS(A) = e(ξ)|_Σ ≠ 0` from `χ(A) = −6` | `symbolic-exact` | Categorical; evaluates unconditionally. Kummer non-divisibility ⇒ nonzero Euler class. **Not** in dispute. |
| B1. `NS(A) = 0 ⟺ q-NS globally regular for the specialised flow` | `conditional` | The obstruction-tower lift criterion. Internal to the substrate; plausibly formalizable as a lift-obstruction ⟺ splitting statement. |
| B2. specialised-`q=1` flow *is* the classical incompressible NS on ℝ³ | `open-analytic` | The identification of the `q=1` limit of the categorical flow with the honest PDE. **Undefined rigorously** — the q-NS system lives on `Ω¹(A)`, not on `L²_σ(ℝ³)`. |
| B3. `NS(A) ≠ 0 ⇒ classical finite-time blow-up` | `open-analytic` | = Bridge (B) = Clay. Requires B2 + a genuine blow-up construction. |

**Attack route (formalize-first).** The only honest, landable move is to **name** the
bridge as an explicit primary-conjecture class `CategoricalClassicalNSBridge` whose
fields are the *hypotheses* (B2 identification map; B1 lift-criterion) — never the
conclusion — and restate any downstream "classical blow-up" claim as conditional on it.
That converts a hidden Clay-sized assumption into a visible, auditable one. **This PR
lands that class** (T4/T6). It does **not** discharge it.

**Wall.** B2 and B3 are the Clay wall. There is no known route from an `H²`-class
obstruction to a PDE singularity; even stating B2 rigorously requires a functor from the
categorical Hodge complex `Ω¹(A)` to Leray–Hopf space that the corpus does not have.

### Gap 2 — `conj:levi-degeneracy` (which branch?).

Dichotomy: **(A)** `C_L(κ) = O(1)` ⇒ blow-up; **(B)** `C_L(κ) ~ κ` ⇒ regular.

| Sub-claim | Tier | Note |
|---|---|---|
| L1. `cond(𝓛_Θ) = max(λ∥,λ⊥)/min(λ∥,λ⊥) = (aspect ratio)²·(1+O(ℏ_q²))` | **`proved`** (Lean) | `core_levi_ratio_eq_aspect_sq`, sorry-free, conditional on the 5 classes. The *geometry* of the condition number is done. |
| L2. for `q > 1`: `cond ≤ 1 + C₀ℏ_q²` (bounded) | `conditional` | `core_levi_cond_bound`; the regular side. |
| L3. the growth rate of `C_L(κ)` as `κ → ∞` (which branch) | `open-analytic` | The undecided computation. Needs the *evolution* of an anti-parallel vortex pair, not just the pointwise identity. |
| L4. exhaustiveness of the dichotomy (A xor B) | **flag** | See Finding 3 — intermediate `C_L ~ κ^β`, `0<β<1`, is not excluded and would break the clean xor. |

**Attack route.** L3 reduces (via L1) to the **core aspect-ratio evolution**
`a⊥(t)/a∥(t)` of a colliding vortex pair — a concrete self-similar-collision ODE/PDE
question, more tractable than full Clay because it is a *local* geometry near `Σ`.
Numerical route: integrate the q-deformed Biot–Savart / Madelung pair-collision at a
ladder `q_κ = e^{iπ/κ}` and measure `cond` growth. **But** the numeric would only
*suggest* a branch; a proof needs a rigorous collision-rate bound. Realistic near-term:
formalize L1/L2 (done) and state L3 as the open branch selector.

### Gap 3 — `conj:regularity-breakdown` (the master classical conjecture).

| Sub-claim | Tier | Note |
|---|---|---|
| R1. ∃ smooth finite-energy `v₀` forcing finite-T singularity | `open-analytic` | = Clay blow-up. |
| R2. enstrophy blow-up `∫|ω|² → ∞` at finite `T*` | `open-analytic` | Equivalent to R1 by BKM (`∫‖ω‖_∞ = ∞`); enstrophy form is the q-NS order parameter. |
| R3. vortex-sheet concentration, `d_H(singular set) = 2` | `open-analytic` | **In tension** with Caffarelli–Kohn–Nirenberg: the *parabolic* Hausdorff dim of the singular set of a suitable weak solution is `≤ 1`. A `d_H = 2` **spatial** sheet is not immediately excluded by CKN (different measure), but the claim needs reconciliation — see Finding 2 note. |
| R4. self-similar Leray profile `V(ξ)` solving Leray eqns, `V ∈ L²` | **REFUTED as written** | See **Finding 1**: Nečas–Růžička–Šverák (1996) ⇒ no nontrivial such profile. |

**Attack route.** R2 is the right order parameter to keep. R3 must be restated against
CKN. **R4 must be re-scoped** off backward-self-similar to *discretely* self-similar
(DSS) or Type-II (non-self-similar) blow-up — the only forms not killed by the 1996
no-go. This is a content-honesty fix (T3), landable, and it *sharpens* the conjecture
rather than weakening the program.

### Gap 4 — The "three obstructions" (heuristics).

| Obstruction | Tier | What it actually is |
|---|---|---|
| O1. loss of UV regularization, `[k]_1 = k`, quadratic dissipation vs cubic nonlinearity | `heuristic` | A restatement that 3D NS is **energy-supercritical / L²-critical** — the classical reason the problem is hard. No new leverage. |
| O2. `ν_q = (q−1)/2q → 0` | `heuristic` | The vanishing-viscosity limit; well-known to be singular. True but not a mechanism. |
| O3. cascade becomes continuous, transfer `→ ε_k^{−1/3}` | `heuristic` | Kolmogorov cascade heuristic; not a theorem for NS. |

**Assessment.** All three are *faithful* but are re-descriptions of the single fact that
`q → 1` removes the sub-critical regularization that makes the q > 1 proof close. **None
is an independent proof ingredient.** They belong in the exposition as *motivation*, and
should not be cited as if they collectively "establish" breakdown (the re-scope commit
`a81fa777` already caveated the top-level claim; these three lines should carry the same
"suggest, not establish" register). No new formalization; keep as motivation.

### Gap 5 — Critical exponent `α` in `Ω(q) ~ (q−1)^{−α}`.

**Corpus already has values** (so the task's "undetermined" is imprecise — see Finding
2). Two *different* heuristics give two *different* answers:

| Route | α | Source | Tier |
|---|---|---|---|
| Naive Gronwall on `dΩ/dt ≤ Λ_q Ω`, `Λ_q ~ (q−1)^{−1}` | **1** | `p2-critical-exponent.md` (called "too crude") | `heuristic` |
| Cascade-depth `Ω ≲ N_eff^{4/3}`, `N_eff ~ ln(1/ε)/ε` | **4/3** (+ log) | `p2-critical-exponent.md` boxed result | `heuristic` |
| Energy-dissipation closure `ε = ν_q·Ω`, `ε = O(1)` | **1** | this doc (§3) | `heuristic` |

**Attack route.** Neither is rigorous and they disagree. The honest move (T2) is to state
each α **conditional on its named closure hypothesis** rather than box a single value.
`α = 1` follows from the standard turbulence closure `Ω = ε/ν_q` *iff* the mean
dissipation `ε` stays bounded away from 0 as `q → 1`; `α = 4/3` follows from a Kolmogorov
`E(k) ~ k^{−5/3}` spectrum truncated at `N_eff`. Both assumptions are falsifiable and
neither is proved. Formalize as a conditional scaling lemma with the closure as an
explicit hypothesis (T6). Determining α rigorously is Tier C (needs the actual q-NS
spectrum, i.e. essentially the turbulence closure problem).

---

## 3. Critical-distance findings

**Finding 1 (literature no-go vs. R4). The self-similar Leray clause is refuted as
written.** `conj:regularity-breakdown` item 3 and `leray-profile` posit a nontrivial
backward-self-similar profile `V(ξ)` with `V ∈ L²` solving the Leray equations. Nečas,
Růžička & Šverák, *On Leray's self-similar solutions of the Navier–Stokes equations*,
**Acta Math. 176 (1996) 283–294**, DOI 10.1007/BF02551584, prove that any such profile
with `V ∈ L³(ℝ³)` (and Tsai 1998, ARMA 143, for local-energy conditions) must be
**trivial (`V = 0`)**. A finite-energy `L²` profile is even more constrained. **The
clean self-similar ansatz cannot be the blow-up mechanism.** The framework must move to
*discretely* self-similar (Chae–Wolf, Bradshaw–Tsai — these *exist* forward but are not
blow-up) or genuinely *Type-II* (non-self-similar) scenarios. Recommended action:
re-scope R4 + `leray-profile` from "self-similar `V`" to "discretely-self-similar /
Type-II asymptotics (backward self-similar excluded by NRŠ 1996)". This does not weaken
the program; it removes a clause that is provably false.

**Finding 2 (internal inconsistency + imprecise "open"). α is not "undetermined" — it
is over-determined and inconsistent.** The corpus asserts `α = 4/3` (boxed,
`p2-critical-exponent.md`) while `regularity-breakdown.md` treats α as unknown and the
naive Gronwall in the same file gives `α = 1`. Per AGENTS.md corpus-grep discipline, the
honest status is **"two conflicting heuristic values, neither rigorous,"** not
"undetermined." Keep both, tier them, name the closures (T2). Separately, R3's `d_H = 2`
spatial sheet should be reconciled with CKN's parabolic-`dim ≤ 1` singular-set bound
(they measure different sets, so no contradiction is proved, but the paper should say so
explicitly rather than leave the reader to notice).

**Finding 3 (dichotomy may not be exhaustive). `conj:levi-degeneracy` claims "exactly
one of (A) `C_L = O(1)`, (B) `C_L ~ κ`."** These are not complementary: an intermediate
`C_L(κ) ~ κ^β` with `0 < β < 1` satisfies neither, and is precisely the kind of marginal
rate that vortex-collision scaling tends to produce. As stated the conjecture could be
**vacuously false** (neither branch holds) rather than a genuine dichotomy. Recommended:
restate as a *trichotomy* keyed on `β = lim sup log C_L / log κ` — `β = 0` (blow-up),
`β = 1` (regular via sheet-flattening), `0 < β < 1` (marginal, undetermined) — or prove
that the marginal window is empty. The Lean `LeviDegeneracy` class currently encodes only
the degeneracy *set*, not the growth rate, so it does not yet capture the dichotomy at
all (a separate honesty gap).

---

## 4. What is provable now vs. the wall (summary table)

| Item | Provable now | The wall |
|---|---|---|
| Bridge B | name it as a conditional class (T4/T6) | B2 identification + B3 blow-up = **Clay** |
| Levi L1/L2 | **already Lean-proved** (conditional) | L3 branch-selection (collision rate) |
| Reg-breakdown R2 | keep as order parameter | R1/R2 existence = **Clay** |
| Reg-breakdown R4 | **re-scope off self-similar** (Finding 1) | DSS/Type-II construction = open |
| 3 obstructions | keep as motivation, "suggest" register | — (not proof ingredients) |
| α | state 2 values conditional on named closures (T2/T6) | rigorous α = turbulence closure = Tier C |

**Net:** the program's *honest* deliverables here are (i) a named bridge class, (ii) the
already-proved Levi geometry, (iii) a corrected self-similar clause, (iv) a reconciled
tiered α. The Clay core (B2/B3/R1/R2) stays open and is correctly class-axiomatised with
no instance.

---

## 5. Attack plan / bean map

| Bean | Item | Deliverable | Status |
|---|---|---|---|
| `qou-40vh` | T1 | this doc | in-progress → done on commit |
| `qou-15gb` | T2/§Gap5 | tier the two α values, name closures | queued |
| `qou-xq2w` | T3/Finding 1 | NRŠ tension → re-scope self-similar clause | queued |
| `qou-g1h7` | T4/Gap1 | name `CategoricalClassicalNSBridge` primary-conj class | queued |
| `qou-3g5m` | T5/Finding 3 | trichotomy re-statement of Levi dichotomy | queued |
| `qou-l5pt` | T6 | Lean: bridge class + α conditional scaling lemma, sorry-free | queued |

**Discipline note.** Everything above respects: *Axiomatization is NOT a Proof* (the
bridge class is the open wall, not a closure), *Conditional-proved ≠
premise-established* (downstream stays conditional), and *Before declaring "refuted"*
(Finding 1 is scope-**(b) structural exclusion** — it cites a *proved* no-go theorem
(NRŠ 1996) forbidding the ingredient, so the strong wording is licensed; Findings 2–3 are
scope-**(a)** consistency/exhaustiveness flags, not exclusions).
