# Photon clasps on the Borromean core: what survives of the "Compton subtraction" proposal

Date: 2026-11-21. Probe: `compton_clasp_probe.py` (exact in ℚ(q), sympy; output
`compton_clasp_probe.out.json`). Lean: `QOU/MassTheory/PhotonClaspChargeForm.lean`
(lean-direct `-DautoImplicit=false -s 65536` exit 0 against the restored
`lake-cache` oleans, no warnings; `#print axioms` shows only `propext`,
`Classical.choice`, `Quot.sound`, no `sorryAx`).

## Setup

The proposal (pasted by the owner from an external discussion) adjoins a fourth
"photon" strand to the Borromean core, lets it clasp quark strands, closes it with
a partial Markov trace and weights the result by quark charges. Translated into
the corpus's objects:

- Hecke algebra `H_n(q)` with `σ² = (q − q⁻¹)σ + 1` (not the TL two-row quotient).
- Ocneanu trace, convention D, `z_D = q³/(q²+1)`, `tr(1) = 1`.
- Core `B = (σ₀σ₁⁻¹)³`. By `borromeanV3A_eq_switched_photon_product` this is
  itself a product of two ruled photons `γ(0,0,qh)·γ(0,0,−q⁻¹h)`.
- Clasp of strand `i` by strand 3: pure-braid generator `A_{i,3}`. Pair clasp:
  `A_{i,3}A_{j,3}`. `E₄ : H₄ → H₃` the conditional expectation.
- `D_ij = tr(B · L_ij)`, symmetrised `S_ij = (D_ij + D_ji)/2`.

## Findings (exact)

1. **Single-strand clasp is a scalar.** `E₄(A_{i,3}) = (q⁴+1)/(q²+1) = 1 + (q−q⁻¹)z_D`
   for every `i`. The proposal's claim holds. So `D_ii = m·tr(B)` with
   `m = (q⁴+1)/(q²+1)`, strand-independent.
2. **Pair clasp is not a scalar,** but it is `a + b·T_{(ij)}` (plus one more term
   for the non-adjacent pair), i.e. it inserts a Hecke transposition, a
   combination of the two `H₂` idempotents, not a TL `e_ij`. It is **order
   dependent**: `L_ij ≠ L_ji`, so `D` is not symmetric. Only its symmetric part
   enters the charge form.
3. **Factorisation up to fifth order.** `S_ij = m²·tr(B) + c_ij` with
   `c₀₁ = c₀₂ = −K/q⁸`, `c₁₂ = +K/q⁶`,
   `K = (q²−1)⁵(q⁴+1)²(q⁴+q²+1)/(2(q²+1)⁴)`.
   Also `tr(B) = 1 − (q²−1)⁴(q⁴+q²+1)/(q⁴(q²+1)²)` (Brunnian: flat to 4th order).
4. **Charge algebra is right.** `Σ QᵢQⱼ D_ij = D_off·Q_tot² + (D_diag − D_off)·ΣQᵢ²`
   and `p − n = D_diag/3 + 2D_off/3` on a symmetric core. This is already in the
   corpus as `ChargeQuadraticSumRule.pn_energy_gap` (`(A+B)/3` with `A = D_diag`,
   `B = 2D_off`). New here: for a general symmetric matrix only the like-flavour
   pair enters off the diagonal (`pMinusN_general`).
5. **p − n is nonzero at q → 1, and equals 1 there**, for all three placements of
   the odd quark: `p − n = tr(B)(m/3 + 2m²/3) + (2/3)c_pair`. At `q = 1`,
   `t = m = 1`, `c = 0`, so `p − n = Q_p² − Q_n² = 1`. All of it is the
   total-charge (Thomson / elastic) piece.
6. **The connected part is fifth order and placement dependent.** With the
   disconnected `tr(B)·tr(L)` removed, `p − n = (2/3)c_pair = ±K/(3q⁶ or 3q⁸)`:
   `+K/(3q⁶)` if the odd quark is strand 0, `−K/(3q⁸)` if strand 1 or 2. The sign
   flips with where the photon strand sits relative to the core, so the
   "structure-dependent" term is not canonical as posed.

## Reading against the rulings

- **Virtual photon.** Closing the fourth strand is emit-and-reabsorb, which the
  2026-11-16 ruling excludes. The algebra above is a statement about `E₄`, not
  about a virtual photon; no ruled mechanism (prior entangled photon, unseen
  emitter) is constructed. Nothing here is a derivation of an EM mass shift.
- **Photon form.** The clasping strand is not `γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹`.
  The proposal's coupling `W_i(λ, γ)` is never defined, so its Feynman–Hellmann
  Hessian has no content beyond "a symmetric bilinear form in the charges".
- **Two-term trace (PR #8804).** The connected trace removes exactly the scalar
  charge part. Finding 5–6 makes that sharp for clasps: what is removed is the
  whole `q → 1` value (`Q_N²`), and what survives is `O((q−1)⁵)` with a sign set
  by an arbitrary strand placement.
- **u/d symmetry.** Charges do break the proved flavour symmetry (`n = p` for
  flavoured strands), but only through `Q_N²` at leading order; the topology of
  the core adds nothing until fifth order.
- **Discarded as non-content:** "UV finiteness" (a finite-dimensional algebra is
  trivially finite), the OPE / counterterm dictionary, the `P₀` ground-state
  projector, the `ν = 0` ↔ Jucys–Murphy identification. None is a statement that
  can be checked.

No empirical value is used anywhere above. The coupling (the overall factor that
would multiply the charge form) is not derived.
