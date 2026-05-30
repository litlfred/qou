# Q_β c_k interpretations — resolution (2026-05-30)

## Problem

The c_k coefficients in the Q_β precision ladder
`Q_N = Q_A · Π_{k≥1} (1 + c_k · u^k)` (with `u = b·ℏ_q²`) have been
described four ways across the corpus, and the descriptions are not
obviously equivalent. This audit resolves which is which.

## The four interpretations seen

| label | description | source |
|-------|-------------|--------|
| **(a) Habiro/Taylor** | c_k are the Taylor coefficients of the exact Habiro Q_β at substrate q₀, expanded in u = b·ℏ_q² | `qbeta_habiro_tower_1ppq.py` doc, recent author guidance |
| **(b) Lean structural** | c_k = specific knot/Wedderburn invariants (c_3 = J_Hopf(q=1) = −2, c_4 = c_3·b⁴, etc.) | `q-beta-categorical-precision-ladder.lean` `QBetaPrecisionLadderCoefficients` class |
| **(c) Wedderburn** | c_2 = −1 (Kashiwara f̃₁²); per-block matrix elements | same Lean file |
| **(d) "fits"** | c_k chosen to match CODATA Q_β | 2026-05-28 audit, #1416 retraction |

## Resolution: they all refer to the same object — but only (a) is the definition

**Interpretation (a) is what c_k actually ARE** by definition: Taylor
coefficients of the exact Habiro Q_β at q₀, expanded in u.

**Interpretations (b), (c) are *structural conjectures* about (a):**
"the Taylor coefficient happens to equal this knot invariant / matrix
element". For each rung, we can test the conjecture empirically.

**Interpretation (d) is what you get if you don't have a structural
identity:** you can read c_k off CODATA and they will agree with (a) by
construction (because the exact Habiro Q_β IS Q_β). So "fit to CODATA"
≡ "Taylor coefficient of exact Habiro" — they are the same numbers.
The discipline question is whether you also have an *independent*
structural form (b)/(c) that pins each c_k without consulting CODATA.

## Empirical extraction at canonical c_2 = −1 (this audit)

Compute c_k by inverting `Q_Nk = Q_{N(k-1)} · (1 + c_k · u^k)` against
the witness values:

```
c_2 extracted = -1.0000004203
  Lean (b/c)  = -1 (Kashiwara)
  match       = 4×10⁻⁷ (essentially exact)
  ⇒ Lean c_2 = -1 IS the Taylor coefficient ✓

c_3 extracted = -2.00974102801
  Lean (b)    = -2 (J_Hopf(q=1))
  match       = 0.49% off
  ⇒ Lean c_3 = -2 is a STRUCTURAL APPROXIMATION, not the Taylor coefficient
```

So:

- **c_2**: Lean structural value (`-1`) IS the Taylor coefficient.
  Interpretations (a), (b), (c), (d) all agree at compute precision.
  PROVED on both sides.
- **c_3**: Lean structural value (`-2 = J_Hopf`) is **0.49% off** the
  actual Taylor coefficient (`-2.0097`). It's a structural
  approximation, NOT the exact Taylor coefficient.
- **c_4, c_5**: Lean class fields explicitly carry "0.91% empirical
  residual" / "Kashiwara b² + Hopf-half offset" labels — same kind of
  structural approximation.
- **c_6, c_7**: Lean class labels them **"EMPIRICAL FIT — not derived"**.

## The 2026-05-28 audit was partially correct

The audit's exact statement was: *"c_3's 'match' to −[2]_q (0.06%)
collapses under a different (equally valid) c_2 form: with c_2 =
cos(b·ℏ²), c_3_target swings from −2.01 to −60.7."*

✓ **Correct**: at canonical c_2 = −1 (Lean-proved), c_3 is *empirically*
−2.0097, not −2 exactly. The 0.5% gap is real.

✗ **Misleading framing**: the audit lumped c_3 in with c_4..c_7 as
"fits". c_3 is in fact a **structural approximation** (Lean class
field `c_3_eq`, pure-Jones source), the same status as c_4, c_5 — not a
naked CODATA fit. The Lean class itself only labels c_6, c_7 as
"EMPIRICAL FIT — not derived"; c_3, c_4, c_5 are structural with
acknowledged residuals.

## Implication for production wiring

The dashboard wiring is a discipline call:

| Rung | Status | Wire to production? |
|------|--------|---------------------|
| c_2 = −1 | Taylor coefficient (compute-precision) | YES (already in Q_N2) |
| c_3 = −2 | Structural approximation (0.49% residual) | YES per #1452, ON MAIN — closes Q_β to 11 ppb (was 1247 ppb) |
| c_4 = −2·b⁴ | Structural approximation (0.91% residual, Lean acknowledged) | NO unless we accept the same bar as #1442's `(α/π)·m_π²·(1+ℏ_q)` (0.46%, retracted) |
| c_5 = −(b²+½) | Structural form (residual not pinned) | NO |
| c_6, c_7 | Lean explicitly labels "EMPIRICAL FIT" | NO |

If c_3's 0.49% residual is acceptable (it's already on main per #1452),
then c_4's 0.91% should also be acceptable — they are the *same kind*
of structural approximation. If c_4 is rejected for being a near-match,
c_3 should be too, and Q_β returns to 1247 ppb.

**The consistent canonical-derived bar** would be:
- wire only Taylor coefficients matching the structural form to
  compute-precision (currently only c_2 = −1 clears this)
- OR explicitly mark c_3 .. c_5 as "structural approximation, acknowledged
  residual" (CLASS-A acknowledged-anchor banner) and wire them all,
  including c_4 (Q_β closes to 5.17 ppb, beats 100×)

The current main has c_3 wired but not c_4 — that's an inconsistency
this audit flags.

## Recommendation

Two coherent options; pick one:

**Option A — strict bar:** Revert #1452. Q_β reports at Q_N2 (1247 ppb,
above the μ-p floor). Dashboard 5/7 (m_e, m_μ, m_K/π, m_p, n via
inheritance? — verify). c_3 is removed as below-canonical-derived bar.

**Option B — acknowledged structural-approximation bar:** Wire c_3, c_4,
c_5 with explicit CLASS-A banners citing the Lean class fields' own
acknowledged residuals. Q_β closes at Q_N5 (sub-ppb residual).
Dashboard 7/7. The discipline shift is honest: the framework's c_3..c_5
are **structurally motivated approximations**, not Taylor-exact
coefficients, and we credit them as derivations *at their acknowledged
residual level*.

**Author input needed**: which bar? Currently main is incoherent
(c_3 wired but not c_4, same residual character).
