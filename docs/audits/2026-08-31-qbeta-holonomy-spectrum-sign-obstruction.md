# Branch 3: a real-spectrum holonomy is on the wrong side of 1

**Date:** 2026-08-31 · **Beans:** `qou-pdix` (route 5) / `qou-cds1` (branch 3) ·
**Scope:** (b) — a structural exclusion citing a proved inequality.

**Artifacts.**
[`QOU/QBeta/HolonomySpectrumSignObstruction.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/HolonomySpectrumSignObstruction.lean)
(6 theorems, sorry-free, axioms `[propext, Classical.choice, Quot.sound]`) ·
[`qbeta_holonomy_spectrum_sign_obstruction_probe.py`](../../computations/qbeta/qbeta_holonomy_spectrum_sign_obstruction_probe.py)
(6/6).

---

## What was open

Branch 3 / route 5 is the last live way to earn the ladder's cosine:
`EigenphaseCarrier` is vacuous, the braid-image branch is excluded in every
convention, "M arbitrary" is circular. `PhaseFailsLogFunctionalEquation` then
closed the **constant-residue** horn — Kohno–Drinfeld *fixes the scale*
(braiding `= P exp(ħt/2)`, `t` eigenvalues `±1`, matched to the Hecke eigenvalues
`{q, −q⁻¹}` by **`ħ = 2 ln q`**), so a constant-residue angle is `c · ln q`, and
`α` fails the doubling identity `f(q²) = 2f(q)` that every `c·ln` satisfies.

That left three survivors, recorded verbatim in `qou-pdix`:

> *a connection whose residues depend on `q`, a non-flat construction, or a
> genuinely `q`-dependent-parameter transcendental object is untouched*

**This audit closes all three at once, by a sign argument that never reads the
residues.**

## The argument

The correction is read as the normalised character of a holonomy — the
`EigenphaseCarrier` shape, `tr M = 2 cos α`. Measured, that character is
**strictly below 1**:

| | value |
|---|---|
| full correction `Q_β/Q_A` | 0.998325 |
| ladder cosine factor, convention C | 0.998399 |
| ladder cosine factor, convention D | 0.998999 |

A generator with **real** spectrum `±a` gives character

```
(eᵃ + e⁻ᵃ)/2 = cosh a ≥ 1        for every real a
```

with equality only at `a = 0`. The bound is quantified over **all** real `a`, so
a `q`-dependent residue merely changes which `a` occurs — the bound is unmoved.
That is the residue-independent step, and it is why this reaches the three
survivors the functional-equation argument could not.

At the Kohno–Drinfeld value the miss is elementary. `ħ = 2 ln q₀ = 0.208681` is
**real**, because `q₀ = 1.10998 > 1` is real, so the generator eigenvalues
`±ln q₀` are real and

```
(q + q⁻¹)/2 − 1 = (q−1)²/(2q)
```

a square over a positive — never negative. Numerically **1.005448** against a
required **0.998399**: not merely off by 0.706 %, but **on the wrong side of 1**.

| generator eigenvalue `a` | `cosh a` | below the target? |
|---|---|---|
| 0 | 1.000000 | no |
| `ln q₀` = 0.104341 | 1.005448 | no |
| 0.0566 | 1.001602 | no |
| 1 | 1.543081 | no |
| −0.5 | 1.127626 | no |

None, and none can be.

### Formalised

| theorem | statement |
|---|---|
| `two_le_add_inv` | `0 < x → 2 ≤ x + x⁻¹` |
| `real_spectrum_character_ge_one` | `1 ≤ (eᵃ + e⁻ᵃ)/2` for **every** real `a` — the residue-independent step |
| `correction_below_one_excludes_real_spectrum` | `κ < 1 → κ ≠ (eᵃ + e⁻ᵃ)/2` |
| `kd_character_sub_one` | `(q + q⁻¹)/2 − 1 = (q−1)²/(2q)` |
| `kd_holonomy_cannot_realise_subunit_correction` | `0 < q → κ < 1 → κ ≠ (q + q⁻¹)/2` |
| `kd_character_eq_one_iff` | equality only at the classical point `q = 1` |

No analysis, no transcendence, no appeal to `cosh` — the whole obstruction is
`(x−1)² ≥ 0`.

## What route 5 is left with

Not *"find a connection"* but **"find one whose generator is elliptic at real
`q`"**: `det A > 0` for the traceless generator, spectrum `±iθ` rather than `±a`.
The required `θ` is 0.0565947; Kohno–Drinfeld gives `det A = −(ln q₀)² =
−0.010887 < 0`, hyperbolic.

So the surviving construction has to put the imaginarity somewhere — and the
corpus already names that place: **`conj:im-q-physical-role`**, whose "phase
coordinate" candidate role is exactly this. That is a materially narrower and
more checkable ask than the open construction problem `qou-pdix` currently
records.

### A new tier-0 discriminator

`qou-pdix`'s replacement acceptance test (D1–D6) tests `α`'s functional shape and,
in D5/D6, the construction's definition. This adds a **tier-0** condition:

> **D0 — the generator must be elliptic at real `q`.**

Like D5/D6 it is *read, not run*: it is a condition on the generator, not on
`α`'s output. It is distinct from that test's "cosh-shaped" validation row, which
checks the shape of `α` as a function of `q`, not the spectrum of a generator.

## What this does not claim

It does **not** show no connection exists, does not derive `α`, does not
adjudicate a convention, and wires nothing. It shows the elliptic requirement is
not optional — and therefore that any candidate offered against route 5 which
does not say where its imaginarity comes from has already failed, before any of
D1–D6 is checked.

Anchor: experimental (proton) pin, per the 2026-08-07 owner directive.
