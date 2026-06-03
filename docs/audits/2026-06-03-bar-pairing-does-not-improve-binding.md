# Two bars: τ realizes `|·|` because q₀ is real — the mirror pairing is the observation only on |q|=1

**Date:** 2026-06-03
**Compute:** [`derive_binding_bar_pairing.py`](../../folio-assistant/computations/derive_binding_bar_pairing.py)
→ `derive-binding-bar-pairing.witness.json`
**Status:** DERIVATION. The conceptual reason τ uses the modulus, with the
binding numbers as the confirming symptom (not the reason). Follow-up to the
#1738 modulus → bar/signed cleanup.

## Notation (this resolves the conflated "bar")

There are **two distinct involutions**, and they must not share a glyph:

| symbol | name | what it is |
|---|---|---|
| `\overline{x}` | **conjugation bar** | the archimedean place's involution (the QM bar, `\|ψ\|²=ψ\overline{ψ}`) |
| `f(q⁻¹)`, or `\mathrm{b}(f)` | **Hecke / KL bar** | the *fibre-level* duality `q ↦ q⁻¹` (Kazhdan–Lusztig; §7b "bar-involution invariant"), written **functionally** — it is literally substitution `q→q⁻¹`, so a `q`-function `f` has bar `f(q⁻¹)` (operator form `\mathrm{b}(f)`) |

They are **equal only on the unit circle** `|q| = 1` (root of unity): there
`q⁻¹ = \overline{q}`, so `f(q⁻¹) = \overline{f(q)}` and `tr_M(q)·tr_M(q⁻¹) =
tr_M·\overline{tr_M} = |tr_M|²`.

## The question (author 2026-06-03)

Two challenges, both correct:

1. *"the archimedean observation must stay `|χ(q₀)|` — but 'the numbers are
   empirically better' is not a reason. Is that what τ does?"*
2. *"the imaginary bar-length — can the observable really be in ℂ but we only
   do the ℝ?"*

#1738 had justified `|·|` by "the bar-pairing `χ^λ(q₀)·χ^λ(q₀⁻¹)` underbinds."
That is fitting, not deriving. **Retracted.** The reason must come from what τ
*is*.

## Derivation — τ is the archimedean realization at q₀ ∈ ℝ

τ evaluates the categorical object at the substrate anchor q₀ and takes the
archimedean magnitude — i.e. the **conjugation bar** `\overline{\cdot}`, which at
real q₀ is **trivial** (`tr_M(q₀)` is real), so the magnitude collapses to the
ordinary modulus `|·|`. The framework already commits to this elsewhere: the
Markov transition *probability* is `tr_M·\overline{tr_M}` and
[`markov-disambiguation.md`](../../content/quantum-observable-universe/braids-and-knots/markov-disambiguation.md)
records that it "reduces to `|tr_M|²` at real q₀" — that is the **conjugation**
bar, trivial at the real anchor.

The Hecke/KL bar `f(q⁻¹)` (`q ↦ q⁻¹`) is a **different** map: it sends
q₀ ≈ 1.1097 to q₀⁻¹ ≈ 0.9009, a *different* archimedean point. So
`tr_M(q₀)·tr_M(q₀⁻¹)` pairs two **different** evaluations — it is a
two-place pairing, **not** a single observation. It would coincide with the
observation only at `|q|=1` (the TQFT / unitary regime).

**So the observation operator is fixed by *where the substrate lives*:** real
line (`|q|≠1`) ⇒ `|·|` (conjugation bar, trivial); unit circle ⇒ the `q⁻¹`
mirror. The framework pins q₀ real (Im(q₀)=0, the `lusztig_q_0_imaginary_part_zero`
constraint), so τ realizes `|χ(q₀)|`. **This is the derivation, not the fit.**

## (0) Is the observable in ℂ while we keep only ℝ?

No information is discarded at the observation. At real q₀ the per-channel
character is **exactly real** — verified: `max_λ |Im χ^λ(q₀)| = 0.0` over the
deuteron's Wedderburn blocks. So `|χ^λ(q₀)|` projects nothing away; there is no
ℂ→ℝ truncation at the observation step.

The imaginary bar-length is **manufactured by the mirror pairing**: 5 of the
deuteron's channels have `χ^λ(q₀)·χ^λ(q₀⁻¹) < 0` (sign flip between q₀ and
q₀⁻¹ — the q-Reeb arccosh / hyperbolic channels), so `√(·)` is imaginary. That
is a property of the `q→q⁻¹` bar, not of the observable.

**Where a ℂ observable *would* be physical: a resonance.** `mass + i·Γ/2` is the
pole of an *unstable* state (§7b: resonances = Demazure sub-crystals, broken-
symmetry evaluation). So the honest split is:

- **Stable** state (D, T, ³He, ⁴He — all stable) ⇒ real observable ⇒ `|χ(q₀)|`,
  the binding. We "only do ℝ" *because these nuclei have no width* — not by fiat.
- **Unstable** state ⇒ the imaginary part is the **decay width**; one would keep
  `mass + iΓ/2` and *not* project to ℝ.

This reframes the growth channels: their imaginary bar-length `√(tr_M(q₀)·tr_M(q₀⁻¹))` is plausibly
**width content**, integrating to zero for a stable ground state. *(Hypothesis,
not a proof — flagged as such.)*

## The numbers — confirming symptom, not the reason

Deuteron (n = 6, pure-Python Hoefsmit χ at q₀ and q₀⁻¹, Wenzl y_λ):

| per-block realization | B (MeV) | err vs AME (2.2246) |
|---|---|---|
| **archimedean** `Σ_λ y_λ \|χ^λ(q₀)\|` (τ) | 2.304 | **+3.6 %** |
| **mirror** `Σ_λ y_λ √(χ^λ(q₀)·χ^λ(q₀⁻¹))` | 0.660 | **−70.3 %** |

The −70 % is the *symptom* of evaluating at the wrong place (the mirror point
q₀⁻¹), exactly as the derivation predicts — not the reason for choosing `|·|`.
(T, n = 9, behind `QOU_BAR_INCLUDE_T=1`, did not finish in the compute budget;
the deuteron is decisive on its own — a −70 % vs +3.6 % gap is far beyond any
A-dependence. A Rust per-partition χ kernel would make T/³He/⁴He cheap.)

## Status (honestly marked)

- **Derived:** the two-bars / place argument (real anchor ⇒ conjugation bar ⇒
  `|·|`; the `q⁻¹` mirror = observation only on `|q|=1`); and
  `Im χ^λ(q₀) = 0` (nothing discarded at observation). This makes #1738's
  signed-categorical + `|·|`-at-observation correct *on principle*, not on fit.
- **Conjectural:** imaginary bar-length ↔ decay width (resonance) for
  unstable states.
- **Open:** *why* q₀ is real/archimedean rather than a root of unity — the
  substrate-derivation question (Subgoal-2, owner-declined).

The Hecke/KL bar `f(q⁻¹)` remains the right tool for the **fibre-level** identities
(Habiro recursion, α_EM `[2]_q·(1−h²α)`, the c_k fibre framing). It is the
archimedean **realization** that must stay `|·|`, by Im(q₀)=0.
