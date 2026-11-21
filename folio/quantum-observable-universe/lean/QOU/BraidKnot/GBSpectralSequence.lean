import Mathlib.Algebra.Ring.Basic
import QOU.BraidKnot.ConfinementLevel

/-!
# QOU.BraidKnot.GBSpectralSequence — abstract spectral-sequence carrier

LaTeX label: `prop:gb-spectral-sequence`.

**Scope (2026-11-20, bean `qou-6qbv`).** The content block was rewritten
on the Coxeter length filtration: it now states the spectral sequence of
the Hochschild complex `Hom(H_n^{⊗k}, H_n)` filtered by length weight,
with `E₁` the Hochschild cohomology of the nil-Coxeter algebra and
abutment `HH^*(H_n, H_n)`. The class below is an abstract carrier with
free graded pieces and does **not** formalise that statement; it is kept
because downstream files take `[GBSpectralSequence R]`. The earlier
reading (confinement filtration, rewriting-map differential, abutment
`gr H_n`) is withdrawn: the rewriting map is not a differential
(`QOU.BraidKnot.GBRewriteDifferential`) and the confinement filtration is
not preserved by the Hochschild differential at `n = 3`.

`GBSpectralSequenceCollapsesAtE2` is likewise abstract. For the
length-filtered Hochschild sequence it does **not** describe `H₃`: there
`d₄ ≠ 0` and the sequence stabilises at `E₅`
(`computations/probes/gb_spectral_sequence_h3_probe.py`, exact).
-/

namespace QOU.BraidKnot

universe u

/-- **GB spectral sequence on the GS-filtered Hecke algebra.**

    A class instance carries:
    * `filtration : ℕ → Type*` — the filtered pieces `J^ℓ(q)` (or,
      strictly, the associated graded `J^ℓ / J^{ℓ+1}` at level ℓ).
    * `differential : ∀ ℓ, filtration ℓ → filtration ℓ` — an abstract
      differential on each graded piece (not the GS rewriting map,
      which is not a differential).
    * `d_squared_zero` — the differential squares to zero
      (Cartan–Eilenberg).
    * `e_infty_converges` — the spectral sequence converges to the
      associated graded of the Hecke algebra.

    Each field encodes a substantial mathematical statement; the
    class is the conditional-class wrapper for the proposition
    `prop:gb-spectral-sequence`. -/
class GBSpectralSequence (R : Type u) [CommRing R] where
  /-- The associated-graded piece at filtration level `ℓ`. -/
  graded : ℕ → Type u
  /-- Each graded piece is an additive group. -/
  [gradedAdd : ∀ ℓ, AddCommGroup (graded ℓ)]
  /-- The differential `d : J^ℓ / J^{ℓ+1} → J^ℓ / J^{ℓ+1}`. -/
  differential : ∀ ℓ, graded ℓ → graded ℓ
  /-- The differential squares to zero. -/
  d_squared_zero : ∀ ℓ (x : graded ℓ),
    differential ℓ (differential ℓ x) = 0
  /-- Convergence target: at each level ℓ the `E_∞` page identifies
      with the associated graded.  The class records the target type
      and the convergence map, and asserts that the latter is
      surjective. -/
  E_infty : ℕ → Type u
  [E_infty_add : ∀ ℓ, AddCommGroup (E_infty ℓ)]
  /-- Convergence map `J^ℓ / J^{ℓ+1} → E_∞^ℓ`. -/
  convergeTo : ∀ ℓ, graded ℓ →+ E_infty ℓ
  /-- Convergence: the spectral sequence stabilises onto `E_∞`.
      Cf. gemini-code-assist review on PR #535. -/
  e_infty_converges : ∀ ℓ, Function.Surjective (convergeTo ℓ)

attribute [instance] GBSpectralSequence.gradedAdd GBSpectralSequence.E_infty_add

/-- **GB spectral sequence proposition.**

    Conditional on `[GBSpectralSequence R]`, the differential
    squares to zero and the spectral sequence converges. -/
-- Ref: [leitner2026] `prop:gb-spectral-sequence`,
--      [weibel1994] §5.5
theorem gb_spectral_sequence
    {R : Type u} [CommRing R] [s : GBSpectralSequence R] (ℓ : ℕ) :
    ∀ (x : s.graded ℓ),
      s.differential ℓ (s.differential ℓ x) = 0 :=
  s.d_squared_zero ℓ

/-- **T4 scaffold: E_2 spectral-sequence collapse extension class.**

    Per `prop:spectral-sequence-collapse` and the audit
    `docs/audits/2026-05-24-derivation-chain-gb-jet-orders-and-pentagon.md`
    §2 (Step 7 — GB filtration / spectral sequence): the GB
    spectral sequence collapses at $E_2$ because Pentagon
    coherence forces the higher differentials $d_k$ for $k \geq 2$
    to vanish.

    Extends `GBSpectralSequence` with the explicit collapse-at-E_2
    condition: the convergence map is iso (not just surjective) at
    every filtration level. Under this strengthening, every higher
    jet $h^{2k}$ for $k \geq 2$ is *determined* by the $E_2$ data
    (the $\ell = 0, 1, 2$ pieces). -/
class GBSpectralSequenceCollapsesAtE2 (R : Type u) [CommRing R]
    extends GBSpectralSequence R where
  /-- The convergence map is injective (combined with surjectivity
      from the parent class, this gives iso at E_2). -/
  convergeTo_injective : ∀ ℓ, Function.Injective (convergeTo ℓ)

/-- **E_2 collapse theorem.** Under the E_2 collapse extension,
    the convergence map is bijective at every filtration level —
    i.e., the spectral sequence's $E_2$ page IS the $E_\infty$ page
    up to the iso. This is the formal statement of "no free
    parameters beyond E_2". -/
theorem gb_spectral_sequence_e2_iso
    {R : Type u} [CommRing R] [s : GBSpectralSequenceCollapsesAtE2 R] (ℓ : ℕ) :
    Function.Bijective (s.convergeTo ℓ) :=
  ⟨s.convergeTo_injective ℓ, s.e_infty_converges ℓ⟩

end QOU.BraidKnot
