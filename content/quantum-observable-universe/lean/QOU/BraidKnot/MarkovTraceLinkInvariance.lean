import QOU.BraidKnot.IwahoriHeckeAPI

/-!
# QOU.BraidKnot.MarkovTraceLinkInvariance — the Markov trace is a link invariant

**Tier-3 (bean `60iz`, epic `08a2`) — general-`H_n(q)` completion of the Jones /
knot-invariant mechanism**, built on the sibling-landed abstract Iwahori–Hecke
API `QOU.BraidKnot.IwahoriHeckeAPI` (commits `c2035fb1`/`1fe4bc37`), which
provides the element algebra (`sigma`, `markov_trace`) together with the two
Markov-move axiom classes.

Per Markov's theorem the closure of a braid is a well-defined link invariant
exactly when the trace functional is invariant under the **two Markov moves**:

* **Move I (stabilisation)** `tr_{n+1}(ι a · σ_n) = z · tr_n(a)` — already proved
  *generically* in the API as `markovTrace_stab_comm`
  (from `MarkovTraceStabilisation` + `MarkovTraceCyclic`).
* **Move II (conjugation)** `tr(b · a · b⁻¹) = tr(a)` — proved here as
  `markovTrace_conj_invariant`, directly from Markov-trace cyclicity.

Together they establish that the Markov trace descends to a knot/link invariant
— the general-braid mechanism behind the framework convention
`J_L(q) = tr_M(ρ(β_L))` (AGENTS.md §7a, `thm:jones-markov-trace`). This is the
general-`H_n(q)` companion to the **Hopf-link-specific** `JonesViaMarkovTrace`
(PR #2815, on the thinner `MarkovTraceTower`): #2815 covered the `σ₁²` closure;
this file gives the *arbitrary-braid-word* value `jonesOfBraid` and the move-II
half of the invariance, the part that was BLOCKED on the `H_n(q)` element algebra.

The `IwahoriHeckeAlgebra` structure carries its `Ring` as a *field* (`H.ring`),
not a typeclass instance; we register it once as a `local instance` (per
gemini-code-assist review on PR #2844) so `*` / `1` / `markov_trace` resolve
without per-statement `letI`, keeping the signatures clean and robust against
downstream unification issues.

Sorry-free. (Verification note: this file imports the `IwahoriHeckeAPI`
element-algebra cone, whose `Mathlib.Data.Nat.Dist` / `Mathlib.RingTheory.Idempotents`
oleans are absent from the sandbox's partial `lake-cache`; it is authored against
the fully-read API and gated on CI's full-Mathlib build.)
-/

namespace QOU.BraidKnot.IwahoriHeckeAPI

namespace IwahoriHeckeAlgebra

variable {n : ℕ} {R : Type*} [CommRing R] {q : R} {h_unit : IsUnit q}
variable (H : IwahoriHeckeAlgebra n R q h_unit)

/-- Register the carrier's `Ring` (a structure field) as a `local instance`, so
    `*` / `1` / `markov_trace` resolve without `letI` in every statement below.
    Local to this section: it does not leak past `end IwahoriHeckeAlgebra`. -/
local instance : Ring H.carrier := H.ring

/-- **Jones value of a positive braid word** `w` (a list of generator indices),
    via the Markov trace on `H_n(q)`: `J(w) = tr_M(∏_k σ_{w_k})`. The Hecke image
    is the ordered product of the generators named by `w`, built with core
    `List.foldr` (no `BigOperators` dependency). -/
noncomputable def jonesOfBraid (w : List (Fin (n - 1))) : R :=
  H.markov_trace (List.foldr (· * ·) 1 (w.map H.sigma))

/-- **Markov move II — conjugation invariance of the Markov trace.** For any
    `a` and any `b` with a left inverse `binv` (`binv * b = 1`),

      `tr_M(b · a · binv) = tr_M(a)`.

    Immediate from cyclicity `tr_M(x y) = tr_M(y x)`:
    `tr_M((b a)·binv) = tr_M(binv·(b a)) = tr_M((binv b)·a) = tr_M(1·a) = tr_M(a)`.
    The second of the two Markov moves (move I is `markovTrace_stab_comm` in
    `IwahoriHeckeAPI`); together they make `tr_M` a link invariant. Sorry-free. -/
theorem markovTrace_conj_invariant [MarkovTraceCyclic H]
    (a b binv : H.carrier) (hb : binv * b = 1) :
    H.markov_trace (b * a * binv) = H.markov_trace a := by
  rw [MarkovTraceCyclic.cyclic (b * a) binv, ← mul_assoc, hb, one_mul]

end IwahoriHeckeAlgebra

end QOU.BraidKnot.IwahoriHeckeAPI
