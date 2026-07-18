# Execution plan — 2cvs meromorphic route + my68 Habiro-ring infra

**Date:** 2026-07-18
**Beans:** `qou-2cvs` (endowment, meromorphic route B) + `qou-my68` (GS-filtration
↔ cyclotomic `same_element`); parent `qou-89f9`.
**Branch:** `claude/alien-calculus-habiro-50257v` (post-#3966/#3994 merges).
**Status:** WORKPLAN. Both are multi-week formalizations that need a **full-build
Lean session** (see §0). No Lean is written here that cannot be verified; this is
the formalize-first lemma chain a full-build session (or sibling agent) executes.

## 0. Tooling correction — surmountable, not impossible (updates #3994 §3)

The merged scoping doc (`2026-07-18-endowment-scope-meromorphic-wall.md`) called
the meromorphic API "blocked in this sandbox." Refined finding: **`github.com` is
reachable** (`git ls-remote` on `leanprover-community/mathlib4` succeeds), so the
`Mathlib.Analysis.Meromorphic.*` oleans are **buildable from source** — the wall
is a *long analysis-cone build*, not an impossibility. The blocked pieces are only
the release server + `lake exe cache get`. Practical route for execution:

1. `git clone --depth 1 https://github.com/leanprover-community/mathlib4.git` (or
   reuse a sibling clone); set the `insteadOf` redirect (AGENTS.md §Mathlib cache).
2. `lake build Mathlib.Analysis.Meromorphic.Divisor` (builds the missing cone
   against the cached oleans; expect tens of minutes, one-time).
3. Seed the result onto a `lake-cache/*` orphan branch so the next session
   restores instead of rebuilding.

Everything below assumes step 1–2 done.

## 1. `qou-2cvs` — meromorphic route (B): rigidity for the true `Φ_b`

**Goal.** Replace the idealized nowhere-zero-entire `uniqueUpToScalar` (already
reduced in `FaddeevRigidityReduction`) with a statement about the *meromorphic*
`Φ_b`, dropping `nowhere zero` and using divisors.

**Why route B, not A.** Route A (add an entireness field) is false for `Φ_b`
(zeros on the `b`-lattice via `phi_b_zero`, poles on the dual lattice) — see #3994.
Route B is the physical one.

**Lemma chain (formalize-first):**

1. **`FaddeevPhi` meromorphic field.** Extend the class with
   `merom : MeromorphicOn Φ Set.univ` (true for `Φ_b`; the honest strengthening,
   unlike an entireness field). Keep the difference equations.
2. **Same order from the shared q-difference equation.** For two solutions
   `Φ, Ψ` of `f(z+c) = P(z)·f(z)` with the *same* `P`:
   `meromorphicOrderAt Ψ z₀ - meromorphicOrderAt Φ z₀` is invariant under `z₀ ↦
   z₀ + c` (the prefactor `P` contributes equally to both). Combined with the
   `⟨ib, i/b⟩` lattice covering all of ℂ (already: `exists_period_basis`), the
   order-difference is **constant**; evaluate at one regular point ⇒ it is `0`.
   So `ord Φ = ord Ψ` everywhere.
   - API: `meromorphicOrderAt`, `MeromorphicAt.order_smul`/`order_mul`,
     `MeromorphicOn.divisor`.
3. **Ratio has empty divisor ⇒ holomorphic + nonvanishing.** `ord(Ψ/Φ) = ord Ψ −
   ord Φ = 0` everywhere ⇒ `Ψ/Φ` extends to an **entire, nowhere-zero** function
   (`MeromorphicOn.divisor` zero ⇒ `AnalyticOnNhd`; nonvanishing from order 0).
   - API: `MeromorphicOn.divisor_eq_zero_iff`, `MeromorphicAt.analyticAt` under
     nonneg order.
4. **Feed the existing reduction.** With `Ψ/Φ` entire (step 3), the two periods
   (`ratio_ib_periodic` + `ratio_ibinv_periodic`, the latter promoted to
   everywhere via the merged `periodic_of_continuous_of_eqOn_dense` — the dual
   lattice is discrete ⇒ complement dense), and `exists_period_basis`, apply
   upstream `ratio_const_of_doublyPeriodic` ⇒ `∃ c, Ψ = c·Φ`. **`uniqueUpToScalar`
   discharged for meromorphic `Φ_b`.**

**Milestones:** M1 meromorphic field + `phi_b` is `MeromorphicOn` (needs the
integral/product `Φ_b` — currently axiomatized, so M1 is itself conditional on the
`PhiBProd` construction); M2 same-order lemma (step 2, the core); M3 empty-divisor
⇒ entire (step 3); M4 assemble (step 4, mechanical given M1–M3). M2 is the
genuine new mathematics; M1 inherits the open `Φ_b`-existence conjecture.

**Anti-laundering:** M1's meromorphic field must be *proved* for the constructed
`Φ_b` (`PhiBProd` branch) or carried as the honest open conjecture — not asserted.
The same-order lemma (M2) must be derived from the difference equations, not
assumed.

## 2. `qou-my68` — Habiro-ring `same_element`

**Goal.** Discharge `HabiroGBSameElement` (merged, no instance): the Habiro
cyclotomic construction and the GB residue-spectral construction give the *same*
`f ∈ Ẑ[q]`.

**Two layers:**

- **(Fixed-braid, polynomial shadow — tractable first).** For a fixed braid both
  reps are honest polynomials in `ℤ[u]` (the trace terminates). The injectivity
  reduces to: *two polynomials agreeing at all roots of unity are equal.* The
  roots of unity in ℂ are an **infinite** set, so `Polynomial.eq_of_infinite_eval_eq`
  closes it — modulo the lemma `rootsOfUnity_infinite` (an injection
  `n ↦ primitive (n+1)-th root`, distinct by multiplicative order via
  `Complex.isPrimitiveRoot_exp` + `IsPrimitiveRoot.injOn`-style order distinctness).
  This is the finite face of Habiro injectivity and the **first verifiable brick**
  — API-light (`Polynomial`, `Complex.isPrimitiveRoot_exp`), no Habiro completion
  needed. *(Deferred here only for lack of Mathlib source to pin exact lemma
  names; it is a days-scale, not weeks-scale, task.)*
- **(General, the real infra — weeks).** Formalize `Ẑ[q] = lim_n ℤ[q]/(q;q)_n`
  (inverse limit), the cyclotomic-coefficient coordinates `a_m`, and the
  root-of-unity evaluation embedding `Ẑ[q] ↪ ∏_ζ ℤ[ζ]` (Habiro 2004). Then the
  GS-filtration graded trace (`prop:graded-markov-trace-from-gs-filtration`) and
  the cyclotomic projection (`prop:residue-at-root`) are shown to be the same
  element by agreeing at every root of unity (each is `tr_M` projected the same
  way). Needs the Hecke/GS-filtration infra in `QOU.AlgebraicSubstrate`.

**Milestones:** N1 `rootsOfUnity_infinite` + polynomial-shadow `same_element` for
fixed braids (days; unblocks the proton/neutron/deuteron instances of
`HabiroGBSameElement` concretely). N2 Habiro-ring inverse-limit skeleton. N3
evaluation embedding + injectivity. N4 GS-filtration ↔ cyclotomic identification.
N1 is the recommended immediate next step in a full-build session.

**Anti-laundering:** N1 proves the *polynomial* same-element (real, for fixed
braids); it does **not** prove the general GS ↔ cyclotomic identification (N4) —
label them distinctly.

## 3. Recommended sequencing (full-build session)

1. Unblock (§0 steps 1–2), seed the cache branch.
2. **N1** (my68 polynomial-shadow injectivity) — days, discharges the concrete
   atom instances of `HabiroGBSameElement`.
3. **M2** (2cvs same-order lemma) — the core new mathematics of the meromorphic
   route; M3/M4 follow mechanically.
4. M1 / N2–N4 are the weeks-scale infra; schedule as a dedicated epic under
   `qou-08a2` (keystone de-abstraction).

Nothing here is fitted, wired, or axiomatized. The idealized-vs-physical
distinction (2cvs) and the polynomial-vs-general distinction (my68) are the two
honesty lines to hold while executing.
