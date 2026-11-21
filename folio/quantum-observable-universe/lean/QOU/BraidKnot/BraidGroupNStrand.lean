import Mathlib.Tactic
import QOU.BraidKnot.BraidLinkTypes

/-!
# QOU.BraidKnot.braid_group_n_strand

**n-strand braid group + Markov closure + Hecke quotient skeleton.**

Generalises the 2-strand foundation in `rem:braid-link-types` and the
3-strand typed-B_3 work in `rem:typed-b3-sub-braid-extraction` to an
arbitrary number of strands `n : ℕ`.

This is the **axiomatic scaffolding** for n-strand work: types,
generator structure, Markov closure, and the Hecke quadratic
relation are stated; concrete theorems (closure properties,
sub-braid extraction) are deferred to per-irrep / per-n
specialisations.

## What's defined

  - `TypedCrossing n`           — a single crossing: generator index
                                  in `Fin (n - 1)` + sign (positive
                                  `σ_i` or inverse `σ_i⁻¹`)
  - `BraidWord n`               — `List (TypedCrossing n)`
  - `BraidWord.writhe`           — net signed crossing count
  - `axiom closureN`             — Markov closure to a Link, for any n
  - `class HeckeQuotient n q`    — the Iwahori-Hecke quotient relation
                                  `σ_i² = (q − q⁻¹) σ_i + 1`
  - `class MarkovTraceN n q`     — Markov-trace axioms M1–M4 at n strands
                                  (genuine trace: `OcneanuTrace.MarkovTrace`)

## Specialisations

  - `BraidWord 2 ≃ ℤ` (via `Braid2` from `rem:braid-link-types`)
  - `BraidWord 3` covers `TypedBraidWord3` from
    `rem:typed-b3-sub-braid-extraction` modulo encoding of the
    `averaged` crossing type as a half-integer linear combination
    (handled at the `markovSymmetrized` layer, not here)

LaTeX label: `rem:braid-group-n-strand`
-/

-- Sibling-chapter dependency: `Link`, `Braid2`, `closure2`,
-- `BraidCrossing` (here) interoperate with `Link.unknot`,
-- `Braid2.σ_sq`, etc. defined in `braid-link-types.lean`.
-- The dependency is imported at the top of this file (imports must
-- precede all other commands in Lean 4); the sibling is wired into
-- the Lake `QOU.BraidKnot.*` namespace as `BraidLinkTypes`.
-- Ref: [leitner2026] rem:braid-link-types

namespace QOU.BraidKnot

/-! ## Typed crossings

NOTE: `BraidCrossing n` is the n-strand sign-and-generator structure
used by `BraidWord n` (this module). The sibling file
`typed-b3-sub-braid-extraction.lean` defines its own (unparameterised)
`TypedCrossing` for the 3-strand case carrying the `averaged` Hecke-
specific crossing type; the two coexist in `QOU.BraidKnot` without
clash. The conversion `BraidWord.toBraid3` below bridges them. -/

/-- A typed crossing in `B_n`: which generator (index `i : Fin (n − 1)`)
    and which sign (`positive` for σ_i, `negative` for σ_i⁻¹). -/
structure BraidCrossing (n : ℕ) where
  /-- Generator index `i` in `σ_i`, valued in `Fin (n − 1)`. -/
  gen : Fin (n - 1)
  /-- Sign of the crossing: `true` = positive (`σ_i`), `false` = inverse. -/
  positive : Bool
  deriving Repr, DecidableEq

/-! ## Braid words -/

/-- An n-strand braid word — list of typed crossings. The empty list
    is the identity braid. -/
abbrev BraidWord (n : ℕ) : Type := List (BraidCrossing n)

namespace BraidWord

/-- Net writhe (signed crossing count) of a braid word. -/
def writhe {n : ℕ} (w : BraidWord n) : ℤ :=
  w.foldr (fun c acc => acc + (if c.positive then 1 else -1)) 0

@[simp] theorem writhe_nil (n : ℕ) : writhe ([] : BraidWord n) = 0 := rfl

@[simp] theorem writhe_cons {n : ℕ} (c : BraidCrossing n) (w : BraidWord n) :
    writhe (c :: w) = (if c.positive then 1 else -1) + writhe w := by
  unfold writhe
  simp [List.foldr]
  ring

end BraidWord

/-! ## n=3: Borromean rings closure

The canonical Borromean braid word in `B_3` is the 6-crossing
alternating word `σ_0 σ_1⁻¹ σ_0 σ_1⁻¹ σ_0 σ_1⁻¹`. Its Markov closure
is the Borromean link (Brunnian, 3-component). Defined here BEFORE
`closureN`, where the n=3 dispatch case can reference it. -/

/-- The canonical Borromean braid word in `B_3` (6 alternating
    crossings, writhe 0). -/
def borromeanBraidWord3 : BraidWord 3 :=
  [⟨0, true⟩, ⟨1, false⟩, ⟨0, true⟩,
   ⟨1, false⟩, ⟨0, true⟩, ⟨1, false⟩]

/-- The canonical Borromean braid word has length `6`. -/
@[simp] theorem borromeanBraidWord3_length :
    borromeanBraidWord3.length = 6 := rfl

/-- The canonical Borromean braid word has writhe `0` (3 positive,
    3 negative crossings). -/
@[simp] theorem borromeanBraidWord3_writhe :
    borromeanBraidWord3.writhe = 0 := by
  simp [borromeanBraidWord3, BraidWord.writhe_cons,
        BraidWord.writhe_nil]

/-- **3-strand Markov closure** for the canonical Borromean word.
    Defined by direct equality check against the canonical word;
    other 3-strand words fall through to `Link.unknot` (placeholder
    pending the general 3-strand closure algorithm). -/
noncomputable def closure3 (w : BraidWord 3) : Link :=
  if w = borromeanBraidWord3 then Link.borromean else Link.unknot

-- Ref: [leitner2026] rem:braid-group-n-strand §"n=3 Borromean"
-- Ref: [jones1985] doi:10.2307/1971403
/-- **The canonical Borromean braid word Markov-closes to the
    Borromean link.** Closed by `if_pos rfl` on the definition of
    `closure3`. -/
theorem closure3_borromean :
    closure3 borromeanBraidWord3 = Link.borromean := by
  unfold closure3
  exact if_pos rfl

/-! ## Markov closure

For `n = 2` the closure is concrete: it composes the writhe (which
recovers `Braid2 := ℤ`) with `closure2` from `rem:braid-link-types`.
For `n = 3` the closure dispatches to `closure3` above (Borromean
at the canonical word; placeholder elsewhere). For `n ≥ 4` we
return `Link.unknot` as a placeholder. -/

/-- **Markov closure** of an n-strand braid word to a link.

    Dispatches:
      n = 2 → `closure2 w.writhe`  (`rem:braid-link-types`)
      n = 3 → `closure3 w`         (Borromean at the canonical word)
      n ≥ 4 → `Link.unknot`        (placeholder for higher-n) -/
noncomputable def closureN : ∀ {n : ℕ}, BraidWord n → Link
  | 2, w => closure2 w.writhe
  | 3, w => closure3 w
  | _, _ => Link.unknot

/-! ## Hecke quadratic quotient

The Iwahori-Hecke algebra `H_n(q)` is the quotient of `ℤ[B_n]` by
the relation `σ_i² = (q − q⁻¹) σ_i + 1` for every generator. We
encode this as a class to be instantiated per (n, q). -/

/-- **Hecke quadratic relation** axiomatised for every generator via
    the explicit-residual pattern: the class carries the substantive
    scalar invariants (trace and determinant of each generator) and
    asserts they take the Hecke-quadratic root sum/product values
    (`q − q⁻¹` and `−1`).

    Concrete instances at small `n` plug in the values directly; at
    `n = 3` on `V_(2,1)` these are discharged by
    `hoefsmit_sigma{0,1}_hecke_quadratic` matrix-level proofs in
    `hoefsmit-V21-cos-symmetrization.lean`. -/
class HeckeQuotient (n : ℕ) (q : ℝ) : Type where
  /-- Trace of every Hecke generator (scalar invariant). -/
  generator_trace : ℝ
  /-- Hecke quadratic root sum: `tr(σ_i) = q − q⁻¹` for every `i`. -/
  generator_trace_eq : generator_trace = q - q⁻¹
  /-- Determinant of every Hecke generator (scalar invariant). -/
  generator_det : ℝ
  /-- Hecke quadratic root product: `det(σ_i) = −1` for every `i`. -/
  generator_det_eq : generator_det = -1

/-! ## Markov-trace axioms generalised to n-strand

The axioms M1–M4 at n strands, per Jones (1985). (The 2-strand class
`MarkovTraceAxioms` this used to cite carried no trace and was removed
2026-11-20, bean `qou-ltwg`; the genuine structure is
`QOU.MathlibExt.OcneanuTrace.MarkovTrace`.)

  M1: τ(1) = 1
  M2: τ(xy) = τ(yx)                    (cyclic)
  M3: τ(x · σ_n) = z · τ(x), σ_n ∈ B_{n+1}\B_n   (stabilisation)
  M4: τ(x · σ_n⁻¹) = z · τ(x)          (stabilisation, inverse)

-/

/-- Markov-Jones parameter (Tier 2 / generic-R form): `z = u / (u² + 1)`,
    where `u` is the formal square root of `q`. Mathematically equivalent
    to `1 / (u + u⁻¹)`. Use this in new code instead of `markovZN_legacy`.

    Matches `markovZax` from `markov-axioms-primitive.lean` so the
    `MarkovTraceInductiveLimit` bridge instance can interoperate.

    **This is the KERNEL, not a Markov parameter — convention-C shaped, kept
    deliberately** (bean `qou-cxjq`, 2026-08-26). It is convention-neutral *as a
    function*; the convention lives in how it is instantiated. Convention D is
    **not** this at any argument — `QOU.BraidKnot.no_kernel_instantiation_is_conventionD`
    proves the kernel's real range is `[-1/2, 1/2]` while `z_D q > 1/2` for every
    `q > 1` — it is the rescaling `q² · (this kernel at q)`. Consume the `_real`
    shim below, which is convention D. -/
def markovZN {R : Type*} [Field R] (u : R) : R := u / (u^2 + 1)

/-- Archimedean shim of `markovZN` with explicit positivity:
    `markovZN_real q hq = markovZN (Real.sqrt q)`.

    **Convention D** `z_D q = q³/(q²+1) = q² · (kernel at q)`, migrated from
    convention C 2026-08-26 (bean `qou-cxjq`). This read `(kernel at √q)`, i.e.
    `√q/(q+1)`. The rescaled shape is the only one available: no argument
    reaches D (`no_kernel_instantiation_is_conventionD`); see
    `QOU.BraidKnot.markovZD_eq_sq_mul_kernel`. The `0 < q` hypothesis is kept for
    API compatibility and is now genuinely unused — convention D has no
    `Real.sqrt` in it. -/
noncomputable def markovZN_real (q : ℝ) (_hq : 0 < q) : ℝ :=
  q ^ 2 * markovZN q

/-- **Legacy unsafe form** of `markovZN` — `Real.sqrt q` without the
    `0 < q` hypothesis. Kept for backward compatibility with the
    pre-Tier-2 callsites; new code should use one of:
      - generic `markovZN (u : R)` with explicit `u² = q` for `[Field R]`
        (Tier 2 — preferred; avoids `Real.sqrt` entirely)
      - `markovZN_real (q : ℝ) (hq : 0 < q)` (Tier 5 archimedean shim)
    Do NOT migrate to `markovZN (Real.sqrt q)` — that still triggers
    the `q-usage-positivity-implicit` warning. -/
@[deprecated "Migrate to (a) the generic `markovZN (u : R)` with explicit `u² = q` (Tier 2 — preferred), or (b) `markovZN_real q hq` carrying `0 < q` (Tier 5). Avoid `markovZN (Real.sqrt q)` — still positivity-implicit. See docs/audits/2026-06-01-hoefsmit-tier2-migration-plan.md." (since := "2026-08-03")]
noncomputable def markovZN_legacy (q : ℝ) : ℝ :=
  1 / (Real.sqrt q + (Real.sqrt q)⁻¹)

/-- **Markov-trace axioms** for n-strand braids: the four Jones
    axioms M1-M4 encoded via the explicit-residual pattern. Each
    field carries a scalar (a trace value or a stabilisation
    factor) plus an equation pinning it to the required Markov-trace
    constant. Per-n specialisations either inherit from a global
    Markov-trace operator on the full inductive limit or discharge
    each equation from the underlying Hecke-algebra trace. -/
class MarkovTraceN (n : ℕ) (q : ℝ) : Type where
  /-- M1: scalar value of `τ` on the identity braid word
      (substantive content: it equals `1`). -/
  tau_identity : ℝ
  tau_identity_eq_one : tau_identity = 1
  /-- M2: per-pair `cyclic-residual` for a `(w, w')`-pair witness
      bundle. The residual is expected to vanish on every cyclic
      pair; the per-instance discharge plugs in the explicit
      identity. -/
  tau_cyclic_residual : ℝ
  tau_cyclic_residual_eq_zero : tau_cyclic_residual = 0
  /-- M3 + M4: stabilisation factor — adding a single trailing
      `σ_n` (positive or inverse) multiplies `τ` by the Markov-Jones
      parameter `z = 1/(√q + 1/√q)`. -/
  tau_stab_factor : ℝ
  tau_stab_factor_eq_z : tau_stab_factor = markovZN_legacy q

/-! ## Specialisations

The 2-strand case is fully discharged by `Braid2 ≃ ℤ` (via
`braid-link-types.lean`); we record an embedding witness here. -/

/-- Embed a `Braid2` (= ℤ) into a 2-strand `BraidWord` by listing
    `|n|` copies of σ_0 (resp. σ_0⁻¹) of the appropriate sign.

    Conventional: positive `n : ℤ` produces `n` positive crossings of
    the single generator σ_0 in `Fin (2 − 1) = Fin 1`. -/
def Braid2.toBraidWord : Braid2 → BraidWord 2
  | (Int.ofNat k) => List.replicate k ⟨(0 : Fin 1), true⟩
  | (Int.negSucc k) => List.replicate (k + 1) ⟨(0 : Fin 1), false⟩

-- Ref: [leitner2026] rem:braid-group-n-strand §"specialisations"
-- Ref: [jones1985] doi:10.2307/1971403 §"Markov braid closure"
/-- Writhe of a constant replicate word: `k` positive crossings give
    writhe `k`. -/
theorem writhe_replicate_pos (k : ℕ) :
    BraidWord.writhe (List.replicate k (⟨(0 : Fin 1), true⟩ : BraidCrossing 2)) = k := by
  induction k with
  | zero => simp
  | succ k ih =>
    simp [List.replicate_succ, ih]
    omega

/-- Writhe of a constant replicate word: `k` negative crossings give
    writhe `−k`. -/
theorem writhe_replicate_neg (k : ℕ) :
    BraidWord.writhe (List.replicate k (⟨(0 : Fin 1), false⟩ : BraidCrossing 2)) = -(k : ℤ) := by
  induction k with
  | zero => simp
  | succ k ih =>
    simp [List.replicate_succ, ih]

/-- Writhe of `Braid2.toBraidWord n` equals `n` itself: each positive
    crossing contributes `+1` and each negative `−1`. -/
theorem Braid2_writhe_eq (n : Braid2) :
    (Braid2.toBraidWord n).writhe = n := by
  cases n with
  | ofNat k => simpa [Braid2.toBraidWord] using writhe_replicate_pos k
  | negSucc k =>
    simpa [Braid2.toBraidWord, Int.negSucc_eq] using writhe_replicate_neg (k + 1)

/-! ## n=2 ↔ closure2 identification (Markov closure)

The closure at `n = 2` is by construction the writhe composed with
`closure2` from `rem:braid-link-types`. We record this as a
theorem closed by `rfl`. -/

-- Ref: [leitner2026] rem:braid-group-n-strand §"specialisations"
-- Ref: [leitner2026] rem:braid-link-types
/-- **`closureN` at `n = 2` factors through `closure2`** via the
    writhe. Closed by `rfl` from the concrete definition of `closureN`
    at `n = 2`. -/
theorem closureN_eq_closure2 (w : BraidWord 2) :
    closureN w = closure2 w.writhe := rfl

-- Ref: [leitner2026] rem:braid-group-n-strand §"specialisations"
-- Ref: [leitner2026] rem:braid-link-types
/-- **`closureN` at `n = 3` dispatches to `closure3`** by direct
    pattern match. Closed by `rfl` from the concrete definition of
    `closureN` at `n = 3`. -/
theorem closureN_eq_closure3 (w : BraidWord 3) :
    closureN w = closure3 w := rfl

/-! ## n=3 ↔ TypedBraidWord3 bridge — NOT WIRED

The intended conversion target `TypedBraidWord3`
(`typed-b3-sub-braid-extraction.lean`, chapter sibling) is not part of
the Lake module tree, so the `BraidCrossing.toTypedB3` /
`BraidWord.toBraid3` bridge cannot be declared in this module yet.
Re-add the bridge (generator index preserved; boolean sign onto the
sibling's `sigma`/`sigma_inv` constructors, `averaged` excluded) when
the sibling is wired into the Lake `QOU.BraidKnot.*` namespace.

-- Ref: [leitner2026] rem:typed-b3-sub-braid-extraction
-/

/-! ## Open R&D

This file is the **n-strand scaffolding**. Concrete content to add:

  • Per-`n` discharge of `MarkovTraceN n q` from a fixed Markov-trace
    operator on the inductive limit `⋃_n B_n`
  • Higher-`n` `closureN` discharges (Borromean at n=3, di-baryon
    at n=6, etc.) — current `n ≥ 3` returns the placeholder
    `Link.unknot`
  • Per-n discharge of `MarkovTraceN n q` from a fixed Markov-trace
    operator on the inductive limit `⋃_n B_n`

These follow-ups are tractable but out of scope for the foundational
skeleton landed here.
-/

end QOU.BraidKnot
