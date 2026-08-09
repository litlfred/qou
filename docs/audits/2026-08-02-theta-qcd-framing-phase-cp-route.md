# θ_QCD via the framing phase — bar-symmetry ⟹ reality ⟹ θ ∈ {0, π} (proved); smallness open

**Date:** 2026-08-02 · **Axis:** strong-CP angle `θ_QCD`, framing-phase route ·
**Branch:** `claude/theta-qcd-framing-phase-2026-08-02` ·
**Formalize-first; one algebraic step proved sorry-free; the physical hypothesis and the smallness residual stay open.**

## Corpus-grep (STRICT) — θ_QCD is genuinely open

Before declaring open, ran the four-path checklist:

- `docs/audits/`, `content/`, `computations/`, `docs/coordination/` for
  `theta_qcd` / `strong-cp` / `strong.cp`: the **only** file addressing the
  strong-CP angle is the placeholder
  [`sm-params-theta-qcd.md`](../../content/quantum-observable-universe/appendix-standard-model/sm-params-theta-qcd.md)
  ("open — no corpus content"). No block, computation, ledger, or audit
  develops it. **Declaration of open stands.**

What the corpus *does* provide, and this route reuses:

- [`def:coulomb-charge`](../../content/quantum-observable-universe/climax-volume-mass/coulomb-charge.md)
  — the per-crossing framing coupling `c = 1/2`, `Q = ½(n₊−n₋)`.
- [`def:bar-involution`](../../content/quantum-observable-universe/braids-and-knots/bar-involution.md)
  — `σᵢ ↦ σᵢ⁻¹`, `q ↦ q⁻¹`; the CP / charge-conjugation operation on the
  Hecke fibre, with the full bar-grading algebra already proved sorry-free.
- [`docs/audits/2026-07-12-keystone-wlambda-framing-is-phase.md`](2026-07-12-keystone-wlambda-framing-is-phase.md)
  — the framing residual `θ_λ = q^{f·c}` is a **pure phase** (`|θ_λ|=1`) on
  the substrate circle; `q ↦ q⁻¹` there is complex conjugation.

## The claim, formalized

The framing phase `Θ = q^{w·c}` (`c = 1/2`) is a topological angle attached to
crossings — the same *kind* of object as a θ-term. The question:

> Does a CP symmetry of the colour sector force `Θ` to be real, hence the
> effective strong-CP angle into `{0, π}`?

CP = bar-involution (`q ↦ q⁻¹`). On the fibre circle `q = e^{iφ}`, bar is
complex conjugation, so **bar-invariance = reality**. Formalized in
[`ThetaQcdFramingCp.lean`](../../content/quantum-observable-universe/lean/QOU/StandardModel/ThetaQcdFramingCp.lean)
(`namespace QOU.StandardModel.ThetaQCDFraming`), self-contained over a generic
`Field R` with a minimal `BarInvolution` class mirroring the corpus one.

## PROVED (sorry-free; axioms = {propext, Classical.choice, Quot.sound})

| Lemma | Statement | Physics |
|---|---|---|
| `framingPhase_sq_eq_one` | `bar Θ = Θ⁻¹` (pure phase) ∧ `bar Θ = Θ` (CP-even) ⟹ `Θ² = 1` | bar-symmetry ⟹ reality |
| `framingPhase_eq_pm_one` | same hyps ⟹ `Θ = 1 ∨ Θ = -1` | **θ ∈ {0, π}** |
| `purePhase_qpow` | `bar q = q⁻¹` ⟹ `bar(qⁿ) = (qⁿ)⁻¹` | any q-power framing phase is a pure phase (keystone content, now algebraic) |
| `cpEven_qpow_iff` | CP-even`(qⁿ)` ⟺ `q^{2n} = 1` | at real `q₀ > 1`: `q₀^{2n}=1 ⟺ n=0` ⟹ `Θ=1` ⟹ **θ = 0** |

The core is a two-line algebraic fact: `bar Θ = Θ⁻¹` and `bar Θ = Θ` give
`Θ⁻¹ = Θ`, so `Θ·Θ = Θ·Θ⁻¹ = 1`, hence `(Θ−1)(Θ+1) = 0`. This **is** the
"bar-symmetry ⟹ reality ⟹ θ ∈ {0,π}" step the task asked for, and it holds
over any field — no `ℝ`, no ordering (AGENTS.md §7c).

The pure-phase hypothesis is **not** a separate assumption for the physical
framing phase: `purePhase_qpow` proves it is automatic for any `q`-power
(`bar(qⁿ) = (qⁿ)⁻¹`), which is exactly the keystone framing-is-phase result
recast algebraically. So the *only* non-automatic hypothesis is CP-evenness.

## OPEN (anti-laundering — what is NOT shown)

1. **CP-evenness of the colour sector is a HYPOTHESIS, not derived.** It is
   carried as a **content-bearing conjecture class with no instance**,
   `ColorSectorCPEven` (fields: `framingPhase`, `framing_nonzero`,
   `framing_pure` [derived], `framing_cp_even` [**open**]). The downstream
   `theta_qcd_in_zero_pi` is a genuine §3b-cond conditional theorem — *IF* the
   class holds *THEN* `θ ∈ {0,π}`, fully proved from the class, only unproved
   input is the instance. **No instance is supplied**; per AGENTS.md
   Anti-Laundering, an axiom/class asserting `θ = 0` is not a derivation.

   Why CP-evenness is not free: a single `T(2,9)` gluon knot has writhe
   `9 ≠ 0`, so it is *maximally chiral* — its framing phase `q^{9/2}` is far
   from real. CP-evenness would require a **colour-singlet writhe
   cancellation** over the `9 = 3×3` tube structure (three colour tubes paired
   with anti-tubes of opposite writhe, total writhe 0). That projection needs
   the **SU(3) colour sector, which is itself open**. The framing route thus
   *reduces* strong-CP to colour-singlet writhe balance — a real reduction,
   not a closure.

2. **`θ ∈ {0, π}` is NOT the observed `|θ_QCD| < 10⁻¹⁰` smallness.** Even
   granting the conjecture, a *discrete* `{0,π}` value — or `θ = 0` exactly at
   the real substrate `q₀` (via `cpEven_qpow_iff`: `q₀^{2n}=1 ⟹ n=0`) — is a
   qualitatively different object from a *small nonzero* residual. The
   framework predicting exactly-zero (a CP-conserving strong sector) would
   still leave the measured upper bound and any tiny nonzero value entirely
   unexplained. **This residual is fully open** (bean below).

## Honest scope summary

- **Possible partial win (real):** "the colour-sector framing phase is CP-even
  by a proved symmetry ⟹ its strong-CP contribution is real ⟹ θ ∈ {0,π}" —
  the reality⟹discreteness *implication* is proved sorry-free. This is a
  *conditional mechanism* for strong-CP, contingent on an unproved colour-CP
  hypothesis.
- **Not shown (open):** (a) that the QCD colour sector *is* CP-even (needs
  SU(3) + the 3×3 writhe cancellation); (b) that `θ_QCD` is *small* (the
  `<10⁻¹⁰` residual — a discrete/zero prediction is not a smallness
  derivation).

No fit; no constant wired to production; no instance of the conjecture class;
no `θ = 0` axiom.

## Verification

- `lean`-direct (v4.24.0, restored Mathlib oleans in `LEAN_PATH`): **exit 0**,
  no warnings, no `sorry`.
- `#print axioms` on all five declarations: `[propext, Classical.choice,
  Quot.sound]` only — no custom axiom, no `sorryAx`.

## Follow-up

- Bean: the `|θ_QCD| < 10⁻¹⁰` smallness residual (beyond `{0,π}`), and the
  colour-singlet writhe-cancellation over the `9 = 3×3` `T(2,9)` structure that
  would supply an instance of `ColorSectorCPEven` — both gated on the open
  SU(3) sector.
