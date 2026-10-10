> **DEPRECATED on 2026-05-24.** Undated audit document classified as workplan / status snapshot / migration-handoff / one-off investigation whose findings have been integrated into main or whose plan has been executed. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T5 for the deprecation rationale.

# ³He +81 ppm outlier — investigation note

**Date:** 2026-04-27
**Branch:** `claude/he3-outlier`
**Witness:** `computations/low-isotope-mass-table.witness.json`
**Feeder:** `computations/sweeps/low_isotope_binding_sweep.py`
  → consumed by `low_isotope_mass_table.py`

## Outlier

| isotope | strategy | B_pred (MeV) | B_AME (MeV) | residual | M_err (ppm) |
|---|---|---|---|---|---|
| ³H  | `census:8_11,ρ=2m_e`     | 8.4686 | 8.4818 | −0.013 | +4.7 |
| ³He | `census:Borromean,ρ=2m_e`| 7.4889 | 7.7180 | −0.229 | +81.6 |
| ⁴He | α-cluster                | 28.2957| 28.2957| ~0     | 0.002 |

³He is an order of magnitude worse than its A=3 neighbour ³H and far
worse than α-cluster magic isotopes (⁴He 0.002, ¹²C 0.55, ¹⁶O 8.4 ppm).

## Hypotheses checked

1. **Bug in Borromean census assignment.**  Ruled out.  ³He → L6a4
   (Borromean rings, $V = 8G \approx 7.32772$) is the standard
   identification and is consistent across `mass-table-best`,
   `mass-table-no-fit`, and `mass-table-ppb` witnesses (all give the
   identical 7.4889 MeV prediction).
2. **Numerics / precision.**  Ruled out.
   $B_{\text{pred}} = 2 m_e \cdot 8G = 7.48891930977096$ MeV is exact
   to all printed digits; truncation $\varepsilon = 0$.
3. **ρ_F = 2m_e is the wrong choice.**  Ruled out.  ρ=m_e gives 3.74
   MeV (residual −3.97 MeV, 51%); ρ=3m_e gives 11.23 MeV
   (residual +3.52 MeV, 46%).  The exact ρ that fits is 2.0612 m_e —
   ρ=2m_e is correct to 3% and is *definitionally* mandated
   (Z=2 protons → 2 unit charges).
4. **Genuine structural under-binding.**  **Confirmed.**  The
   narrative `derived-mass-formula-light-isotopes.md` explicitly
   lists ³He under the documented systematic under-prediction
   (−32% on B), alongside D (+41%), T (−38%), ⁴He (−76%).  The
   "binding under-prediction is structural: the formula misses an
   intra-shell binding mechanism present in nature" — addressed
   by the open `conj:shell-correction-term-seven`.

## Why ³H predicts well but ³He does not

The same formula structure ($\rho_F = 2 m_e$, V = census volume)
works on ³H to 0.16% and fails on ³He at 3%.  The L6a4 ↔ ³He
match has α* = 1.000 (all blocks PSD) in the SDP audit
(`atom-knot-mass-derivation.md`), so the *knot identification*
is internally consistent.  What's missing is the
proton-pair-specific contribution: ³He has $n_{pp} = 1$,
³H has $n_{pp} = 0$.  This is exactly the gap the existing
`he3_tighten_pp.py` exploration tries to close, with five
algebraically-natural candidates ($H_q((2,1))$, $H_q((1,1,1))$,
$H_q((2,1))/\dim_q$, $H_q((2,2))/\dim_q$, etc.) — none yet
selected by an independent principle, hence the patch is held
back to keep the registry parameter-free.

Numerically, the missing contribution is +0.229 MeV — close to
$m_e \cdot H_q((2,1)) \approx +0.6$ MeV scaled by $1/A = 1/3$,
i.e. the $T = 1$ same-flavour pairing analogue of $\Delta_W$.
The principled fix is therefore expected to come from the
$T=1$ pp-pairing channel rather than from a Coulomb subtraction.

## Conclusion

**Status: still unexplained at the principled (zero-fit) level —
but recognised as a documented framework gap.**

No code/data change applied.  No `Vol(K)` entry, ρ_F prefactor,
or census assignment is wrong; the witness is producing the
honest output of the current formula.  Hand-fitting a
pp-correction here would (a) duplicate the existing tighten
exploration and (b) introduce a discrete model-selection choice
that the framework explicitly refuses to commit to without
independent derivation.

## Recommendation

Track ³He as a tier-1 test case for `conj:shell-correction-term-seven`
(GB-filtration $\ell = 5$ patch).  The +0.229 MeV residual is the
target a successful Term-7 derivation must close, in tandem with
the other $A \leq 4$ residuals (D, T, ⁴He).  No action on the
witness pipeline.
