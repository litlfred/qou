# ζ₄/η-descent (bean 0zr0): the single-fibre test class is a theorem — prune, and the surviving datum

**Date:** 2026-07-03
**Bean:** `0zr0` (odd-sector structure — ζ₄-residue route from
`conj:binding-qbeta-complex-volume`, post h·D+h³·F refutation `08ds`)
**Producer:**
[`computations/qbeta/qbeta_zeta4_eta_descent_probe.py`](../../computations/qbeta/qbeta_zeta4_eta_descent_probe.py)
(witness `qbeta-zeta4-eta-descent.witness.json`, exact, ORD = 17)
**Lineage:** ũ normalization
[`2026-07-03-u-tilde-bar-weight-normalization.md`](2026-07-03-u-tilde-bar-weight-normalization.md)
(beans `ai81`/`08ds`/`mjim`).

## What was asked

After the exact refutation of the `h·D(ũ) + h³·F(ũ)` odd-sector form
(bean `08ds`), the structured surviving hypothesis was: the bar-even and
bar-odd parts (E, O) of net-route log R are the even/odd parts of ONE
function F of a single bar-odd argument η(s) — the ζ₄/complex-volume
single-fibre picture (Lean-proved partner relation
`QOU.Mass.ComplexVolumeZeta4Partner`: ζ₄-rotation negates the bar-even
channel, keeps the bar-odd one).

The probe constructed η canonically (cube-root gauge: val(O) = 3, so
η := s·∛((O/ℓ)/s³), making O = ℓη³ by construction) and ran exact
membership checks: (i) η∘σ = −η; (ii) E ∈ ℚ(√3)[[η²]];
(iii) η² ∈ ℚ(√3)[[ũ]]. All pass exactly through the validity window
(η to s¹⁵, memberships to s¹⁶).

## The prune (formalize-first, applied to our own probe)

**All three checks are theorems.** One-line arguments:

1. **Invariant ring.** σ: q ↦ 1/q acts on ℚ(√3)[[s]] (s = q−1) as an
   order-2 automorphism. An invariant series has even valuation (the
   leading coefficient picks up (−1)^val), so by induction (subtract the
   matching power of any invariant valuation-2 uniformizer w) the
   invariant subring is exactly ℚ(√3)[[w]] — for **any** bar-even w with
   nonzero s²-coefficient. Hence E bar-even ⇒ E ∈ [[η²]], and
   η² ∈ [[ũ]], automatically. This also re-reads the ai81 finding
   "the bar-even part of log R is exactly a ũ-series (margin 9)" as
   **structural, not empirical** — the margin-9 exactness was
   guaranteed; the empirical content of ai81 remains the bar-weight of
   u (u∘σ = q²u) and the exact rung values.
2. **Cube-root uniqueness.** O∘σ = −O identically (O *is* the bar-odd
   projection), so (η∘σ)³ = −O/ℓ = (−η)³ with equal leading terms; a
   formal series has a unique cube root with given leading coefficient,
   so η∘σ = −η. Check (i) is automatic.

So "the net route descends from a single fibre F(η)" is true of **every**
parity split — the test class as posed has no falsifiable content, and
the passing checks validate the series engine, not the physics. (v1 of
the probe also had two mechanical bugs, kept for the record: boundary
"failures" at orders 14–15 were zero-padding truncation artifacts, and
the odd-tail check O/(ℓη³) ∈ [[η²]] was a gauge tautology ≡ 1.)

This is the probe-side mirror of the AGENTS.md formalize-first rule: the
invariant-theory lemma prunes the whole "does it descend?" family before
any further scan. Any future odd-sector proposal must be posed so that
descent/membership is **not** the claim — only distinguished structure
inside the descent can carry content.

## The surviving datum (exact)

The informative output is the **rung arithmetic** of the canonical
descent, E = Σ g_k η^{2k} (rungs exact in ℚ(√3); decimals for scan):

| k | g_k | g_{k+1}/g_k |
|---|-----|-------------|
| 1 | 1.1250000 | −15.848 |
| 2 | −17.829193 | −9.1889 |
| 3 | 163.82866 | −14.214 |
| 4 | −2328.7344 | −16.452 |
| 5 | 38311.204 | −17.787 |
| 6 | −681444.34 | −18.714 |
| 7 | 12752289 | −19.398 |
| 8 | −2.4737154×10⁸ | — |

Two exact consequences, both scope (a):

1. **The cosh/sinh (ζ₄-partner V₀) entire family is falsified.** An
   entire order-1 F (any A·cosh(cη) + B·sinh(cη) dressing) needs
   |g_{k+1}/g_k| → 0 factorially; the exact ratios **grow**. The
   single-fibre function, if analytically continued, is not entire in η.
2. **Finite radius of convergence ≈ 1/20.5 in η.** The ratios increase
   toward ≈ −20 with shrinking increments (−9.2, −14.2, −16.5, −17.8,
   −18.7, −19.4), the signature of a nearest singularity on the negative
   η²-axis at η² ≈ −1/20.5² (alternating signs). Locating/identifying
   that singularity (e.g. a root-of-unity locus of q(η), a natural
   boundary, or a branch point tied to the ζ₄ rotation) is the sharpened
   follow-up question — it is a *number* the ζ₄ route must now explain,
   replacing the refuted functional forms.

## Status

- Bean `0zr0` closed with this prune + datum. No wiring; audit-only.
- Follow-up (queued, not started): identify the η-plane singularity —
  candidate first test: does q(η) hit a root of unity at |η| ≈ 0.0488?
