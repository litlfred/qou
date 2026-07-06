# adhb — Term-5 `a_K·B_bulk` is a Bethe–Weizsäcker FIT; do NOT wire it into the R5 canonical solver (2026-06-30)

**Bean:** `adhb` (He-3 / deuteron R5 binding magnitude deficit).

**Context.** A prior investigation of `adhb` recommended closing the He-3
magnitude deficit by **wiring "Term 5" (`a_K·B_bulk`) into the R5 canonical
knot solver's `cost_for_candidate`** — Term 5 alone reaches ~0.86 % for ³He.
Before any solver change, a no-fit provenance check was run on `B_bulk`. It
came back **FITTED**. This note records the verdict so the Term-5 wiring is
not re-pitched.

## Verdict: FITTED — wiring `a_K·B_bulk` would import a liquid-drop fit

`computations/bw_chirality_isotopes.py:100-109` defines `B_bulk` as the
**literal Bethe–Weizsäcker liquid-drop formula**:

```
B_bulk = λ_V·A − λ_S·A^(2/3) − a_asym·(N−Z)²/(4A) ± δ_P/√A
```

The coefficients (`bw_chirality_isotopes.py:74-80`) are written as q-integer
products whose values **match the historically AME-fitted BW coefficients**:

| coeff | q-expression | q-value (MeV) | AME-**fitted** (MeV) | err |
|---|---|---|---|---|
| λ_V (volume) | `2·[2]_q·[7]_q·m_e` | 15.67 | 15.56 | +0.7 % |
| λ_S (surface) | `2·[4]_q²·m_e` | 17.26 | 17.23 | +0.2 % |
| λ_C (Coulomb) | `(q−q⁻¹)·[6]_q·m_e` | 0.68 | 0.70 | −2.1 % |
| a_asym | `3·[2]_q·[7]_q·m_e` | 23.51 | 23.29 | +0.9 % |
| δ_P (pairing) | `[3]_q·[7]_q·m_e` | 11.86 | 12.00 | −1.2 % |

The source block
[`q-integer-mass-formula.md`](../../content/quantum-observable-universe/mass-theory/q-integer-mass-formula.md)
is a **`conjecture`** (`conj:q-integer-mass-formula`, Lean `not_checked`) whose
own table column is labeled *"Fitted (MeV)"*. The integer exponents
(`2,4,6,7`) are post-hoc rationalized to reproduce the empirical magnitudes —
the hidden-degrees-of-freedom / match-to-fit pattern the critical-distance
license flags. `a_K` itself (`bw_chirality_isotopes.py:83-86`) is a derived
per-knot-type factor, but `Term 5 = a_K · B_bulk` multiplies it onto the
fitted liquid-drop base, so the **product is fitted output**. Prior
adjudications agree: `docs/audits/2026-05-18-m-p-item-b-t5-categorical-attribution.md`
§3/§7c, `docs/audits/2026-05-09-mass-table-fitting-audit.md` (BW family
flagged ⛔ "pure curve-fit").

**Therefore: do NOT add `a_K·B_bulk` to `cost_for_candidate` in
`r5_full_canonical_knot_solver.py`.** Doing so would make the canonical
solver's binding a BW fit dressed as a derivation, and the resulting "0.86 %
for ³He" would be a fitted number, not a prediction.

## The fit-free chirality is a DIFFERENT object (and still does not close adhb)

The mass-binding dashboard's `B_qCLT_fac` chirality
(`mass_binding_dashboard.py:261-269`) is **not** `a_K·B_bulk`:

```
B_chir = α·(A−1)·(L̄ − L_pn),   α = E₀ = m_e/(q₀(q₀−1)),   L = 1 − tr_atom/tr_free
```

This is **fit-free** — only q₀ + m_e (CAL-1/CAL-2) and the Markov trace; the
code comment states *"ZERO AME / CODATA beyond the CAL-1 m_e unit and CAL-2
q₀."* The +0.86 / −0.65 MeV ³H/³He split is trace-derived. But:

- It still under-binds ⁴He by ~2.4× (dashboard `err qCLT_fac = 2.39`).
- The **deuteron remains blocked** independent of any chirality term: `6₂`
  is PSD-infeasible (`alpha_gap = 0.89`) and `tr_M(β_D) ≡ 0` in ℚ(q); the
  deuteron needs the H_{3A}=H₆ binding-operator search (`conj:canonical-knot-id-sdp`
  leg b), which the H₃-only solver (`assert n_0 == 3`) cannot do.

So even the fit-free route does not mechanically close `adhb`.

## Disposition

`adhb` stays **research-grade open**. The closure requires (a) the H₆/H₉
binding-operator search for the deuteron and (b) a fit-free magnitude
ingredient — *not* the BW-fitted six-term Term 5. No code changed; no fit
wired. The valuable output of this investigation is the negative result:
**`a_K·B_bulk` is a fit; keep it out of the canonical solver.**
