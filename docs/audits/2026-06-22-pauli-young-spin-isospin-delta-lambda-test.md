# Parameter-free Pauli–Young / Wigner-SU(4) spin-isospin Δ_λ — decisive test

**Date:** 2026-06-22
**Branch:** `claude/pauli-young-delta-test-hgp6jc`
**Verdict:** **FAILS CLEANLY.** The spin-isospin projection underbinds every
light nucleus by 94–99.99 %, monotonically worse with A. Being parameter-free
it cannot be a soft fit, so this is a genuine refutation — a 7th Δ_λ direction
closed, this time with *zero* tunable knobs (unlike the six fit-based ansätze
and Option-E v1–v9).

## What was tested

The Δ_λ gate is the per-partition binding density in the canonical Path-D
formula

$$B(K) = m_e\,\Big|\sum_{\lambda \vdash 3A} y_\lambda(q_0)\,\chi^\lambda(\beta_K)\,\Delta_\lambda(K)\Big|.$$

All prior closure attempts supplied Δ_λ as a *q-dependent expression chosen to
land on AME* (a fit). This test supplies Δ_λ from the **Pauli principle +
Wigner's SU(4) supermultiplet symmetry** — integer representation-theory
multiplicities, nothing to tune.

### The construction (no free parameters)

- Each nucleon is a 3-strand baryon whose strands sit in the spatially
  symmetric s-shell → trivial $S_3$ → the complete homogeneous symmetric
  function $h_3$.
- The $A$ baryon-centers occupy the lowest spatial orbital ⇒ spatial
  wavefunction fully **symmetric** ⇒ by Pauli the spin-isospin wavefunction is
  fully **antisymmetric**: the SU(4) supermultiplet $[1^A]$.
  - $A=2$ deuteron: $[1,1]$ = SU(4) **6** = $(S{=}1,T{=}0)\oplus(S{=}0,T{=}1)$ — the $np$ channel.
  - $A=3$ ³H/³He: $[1,1,1]$ = SU(4) **4̄** = $(S{=}\tfrac12,T{=}\tfrac12)$ — mirror pair.
  - $A=4$ ⁴He: $[1^4]$ = SU(4) **singlet** $(S{=}0,T{=}0)$ — the α; SU(4) shell closure.
  - $A>4$: $e_A$ of a 4-dim spin-isospin space **vanishes** — closure *predicted*, not imposed.
- On the $n=3A$ strands, "$A$ symmetric baryons combined fully
  antisymmetrically under exchange" is exactly the **plethysm $e_A[h_3]$**, so

$$\boxed{\;\Delta_\lambda(A) \;=\; \langle\, s_\lambda,\; e_A[h_3]\,\rangle \in \mathbb{Z}_{\ge 0}\;}$$

(the multiplicity of the $S_{3A}$ irrep $\lambda$ in $e_A[h_3]$).

### Engine verification (before trusting physics)

- Murnaghan–Nakayama $\chi^\lambda_\mu$: $\sum_\lambda (f^\lambda)^2 = n!$ at $n=3,6,9$ ✓; spot characters ✓.
- Plethysm dims: $\sum_\lambda \Delta_\lambda f^\lambda = 10$ for $e_2[h_3]$ (= index $6!/(3!^2\,2!)$) ✓; $=280$ for $e_3[h_3]$ (= $9!/(6^3\,3!)$) ✓.
- $y_\lambda(q_0)$, $\chi^\lambda(\beta_K)$, $m_e$ are the canonical cached witnesses (not refit).

## Result

| atom | nonzero Δ_λ blocks | B_pred (MeV) | B_AME (MeV) | rel. error |
|------|--------------------|--------------|-------------|------------|
| ²H (deuteron) | 2 — λ=(5,1),(3,3) | 0.1276 | 2.2246 | **−94.27 %** |
| ³H (tritium)  | 4 | 0.02405 | 8.4818 | **−99.72 %** |
| ³He           | 4 | 0.04188 | 7.7180 | **−99.46 %** |
| ⁴He (α)       | 10 | 0.002972 | 28.2957 | **−99.99 %** |

**Deuteron 0.572 pn-weight cross-check** (the
`signed_crossing_feasibility_probe.py` observable
$(B/E_0)/L_{pn}$, $E_0=m_e/(q_0(q_0-1))=4.186$ MeV): AME gives 0.5719
(reproducing the known 0.572); this construction predicts **0.0328** — off by
~17×.

## Reading

1. **Clean failure, monotone in A.** The error worsens 94 % → 99.7 % → 99.99 %.
   The Pauli-allowed plethysm projects the Markov trace onto very few blocks
   with tiny integer weights (deuteron: just λ=(5,1) and (3,3), each ×1), so the
   binding undershoots more as A grows and the channel becomes a smaller slice
   of the full trace. This is the opposite signature to the fit-based ansätze,
   which were tuned to the deuteron and then drifted on the heavier isotopes.
2. **One qualitative success.** The SU(4) shell closure ($e_A[h_3]=0$ for
   $A>4$ in 4 spin-isospin states) drops out for free and correctly singles out
   ⁴He as the last s-shell supermultiplet — but this is structural, not the
   binding magnitude.
3. **Cannot be rescued by tuning.** Zero parameters means the only way to move
   the number is to change the *channel* (e.g. $h_2[h_3]$, the spin-isospin
   *symmetric* "10", or the full $h_3^2$). Those are physically the wrong
   supermultiplet for the deuteron, and would be a different (and now
   non-canonical) construction. So within the Pauli-Young hypothesis the answer
   is fixed and wrong.

## Conclusion

The spin-isospin / Pauli-Young route does **not** close Δ_λ. It joins the
refuted directions, with the distinction that it required no fit to refute —
the representation theory alone forces a ~17× underbinding of the deuteron.
The honest frontier remains PROBE 2 (A=4 multi-nucleon interface operator) and
the GAP-A-3/A-4 categorical level-selection conjectures, per
[`docs/coordination/option-e.md`](../coordination/option-e.md).

## Artifacts

- Probe: [`computations/probes/pauli_young_spin_isospin_delta_lambda_probe.py`](../../computations/probes/pauli_young_spin_isospin_delta_lambda_probe.py)
- Witness: [`computations/pauli-young-spin-isospin-delta-lambda.witness.json`](../../computations/pauli-young-spin-isospin-delta-lambda.witness.json)

## Cross-refs

- [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md) — the gate + six failed ansätze
- [`docs/coordination/option-e.md`](../coordination/option-e.md) — Option-E v1–v9 ledger
- [`computations/probes/signed_crossing_feasibility_probe.py`](../../computations/probes/signed_crossing_feasibility_probe.py) — the 0.572 pn-weight object
