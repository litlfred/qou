# The residual shape on the normalised bond-counting law — the asymmetry signal drops from −0.80 to −0.70, the surface signal rises from −0.18 to −0.30, and the residual has the SEMF shape with `R² = 0.96`

**Date:** 2026-09-04 · **Beans:** `qou-yau0` (this), `qou-hfjc` (the normalisation it follows),
`qou-q7ga` (#6611's roast, one row revised), `qou-ib3g` (#6668, cross-referenced) ·
**Arc:** binding law · **Scope:** a diagnostic probe, no fit wired, no Lean needed (everything
rests on #6656's theorems). **Nothing is wired; no production number moves.**

## 1. Why

#6656 showed the forced link-invariant normalisation makes every bond weigh `q/(q²+1)`, so
#6611's additive law becomes `B_norm = (A−1)·ε`, `ε = E₀ ln[2]_q = 2.9242 MeV`, and the
un-normalised law's `(N−Z)` asymmetry — wrong-signed against the data — is a writhe artifact.
#6611's shape analysis (*"the missing term is the symmetry energy: residual correlates −0.804
with `(N−Z)²/A²`, −0.178 with `A^{−1/3}`"*) was measured on the **un-normalised** law and so
carries part of that artifact. My #6656 audit recommended re-measuring it before the author
decides anything about the functional. This is that measurement.

**Cross-reference, not re-derivation.** #6668 (`qou-ib3g`) reports *"the per-nucleon
coefficient at `N = Z` is `E₀·0.698581 = 2.92425 MeV`"* and a required factor `3.0075` to the
peak `B/A`. That coefficient **is `ε`**: the un-normalised pp/nn average is
`−ln(z z')/2 = ln[2]_q` identically (checked to 50 dps), so #6668's factor applies to the
normalised law unchanged and is not re-measured here.

## 2. Probe

`computations/probes/normalised_law_residual_shape_probe.py` — **9/9**, mpmath 50 dps, #6611's
AME selection and helper functions reproduced (2548 measured nuclides), the un-normalised law
as a control.

### Residual correlations, `r = B_exp / B_pred`

| shape | un-normalised (#6611 control) | **normalised (bond counting)** |
|---|---:|---:|
| `(N−Z)²/A²` asymmetry | −0.8038 | **−0.6965** |
| `A^{−1/3}` surface | −0.1781 | **−0.2980** |
| `Z²/A^{4/3}` Coulomb | −0.0439 | −0.0431 |
| `δ/√A` pairing | +0.0961 | +0.0962 |

The control reproduces #6611's `−0.804` / `−0.178` to three decimals. On the normalised law
the asymmetry correlation **falls** by 0.107 and the surface correlation **rises** by 0.120.
The asymmetry shape is still the dominant residual, but #6611's "wrong by 4×" (asymmetry vs
surface) is **2.3×** once the artifact is removed, and the surface term is a live lead again.

### Shape test (diagnostic, not a model)

#6611's decision frame §5.2 named the test: *"falsified by the residual failing to have the
shape `a_S A^{−1/3} + a_C Z²/A^{4/3} + a_A (N−Z)²/A²` — a shape test that needs no scale."*
Least-squares projection of `r_N` onto `[1, A^{−1/3}, Z²/A^{4/3}, (N−Z)²/A², δ/√A]`:

| term | coef / c_V (data) | textbook SEMF `a_i/a_V` |
|---|---:|---:|
| surface | −0.830 | −1.130 |
| Coulomb | −0.0412 | −0.0451 |
| asymmetry | −1.266 | −1.505 |
| pairing | +0.036 | +0.710 |

`R² = 0.9616` (control, un-normalised: 0.9282). All four corrections carry the SEMF sign; the
Coulomb ratio is within 9 %, surface and asymmetry within 27 % and 16 %, pairing is mostly
missed (a small term against a coarse `δ/√A` proxy). **The residual has the SEMF shape.** The
volume coefficient `c_V = 4.667` puts the saturated per-bond energy at `c_V·ε = 13.65 MeV` —
this is the `a_V`-like coefficient of the projection, a different quantity from #6668's
peak-based `3.0075` (which is the realised maximum `B/A` over `ε`), and neither is a criterion.

### `κ` scan on the normalised law, `B ~ ε(A−1) + κ·ε·(N−Z)`

Optimum near `κ = −0.2` (p5–p95 1.1656 against 1.1808 at `κ = 0`); #6611's optimum on its
`ln 2` form was `≈ −0.15`. `κ = 0` (the normalised law) beats the un-normalised `κ_derived =
+0.22` (1.2069). So the data still want a *negative* linear asymmetry beyond bond counting —
the same direction #6611 found, now measured from a derived zero rather than a wrong-signed
derived value.

## 3. What this establishes, and what it does not

- **Established (measured):** removing the writhe artifact shrinks the apparent symmetry
  signal by 13 % of its value and doubles the surface signal's correlation; the normalised
  residual has the SEMF shape at `R² = 0.96` with correct signs and a Coulomb ratio within
  9 % of textbook. The un-normalised law's `−0.804` should no longer be quoted as *the*
  measure of the missing term.
- **Revises one row of #6611's roast** (`qou-q7ga` §7.4 row 7 / the decision frame's demotion
  of the surface term "wrong by 4×"): the factor is 2.3× on the normalised law, and the surface
  term's correlation is 0.30, not 0.18. The demotion was measured on the artifact-bearing law.
- **Not established:** any mechanism. The projection coefficients are what the data would
  need, recorded to be checked against; nothing is wired. The scale gap (#6668's factor 3,
  `qou-59j5`) is untouched and is the same on both laws.
- **Not a model selection:** `R² = 0.96` says the residual is SEMF-shaped; it does not say
  which of the framework's routes produces those terms. #6611's own reading — *"what the law
  earns is that the algebra produces an extensive quantity"* — stands.

## 4. Options for the author (default first; recommendation is judgement)

- **Default — nothing changes.** The numbers are on the record; #6611's decision frame keeps
  its rows, with this note's corrections attached to row 2 (surface) and row 7 (symmetry).
- **Re-order the leads.** With the artifact removed the ranking of missing terms by
  correlation is asymmetry (0.70) > surface (0.30) ≫ pairing (0.10) > Coulomb (0.04), and by
  SEMF-ratio fidelity Coulomb (9 %) > asymmetry (16 %) > surface (27 %). A derived surface
  term (the 3-D coordination geometry #6611 §5.2 describes, "no new constant") is a live lead
  again, not a demoted one. Cost: a decision-frame edit. Risk: none.
- **Adopt the normalised functional in the stated law** — the #6656 §6 decision, unchanged
  by this note except that its "symmetry becomes wholly missing rather than wrong-signed" is
  now quantified: 0.70 correlation with the right sign to supply.

**Recommendation (judgement):** the second option. The shape test the decision frame asked
for has been run on the artifact-free law and passed; the frame's own ranking should be
updated to the numbers that survive.

## 5. Verification

Probe 9/9; the control reproduces #6611's two published correlations to three decimals;
`scripts/precision-gates.sh --changed` (result in the PR body). No Lean changes. Repo CI is
`workflow_dispatch`-only; this agent verification is the gate.
