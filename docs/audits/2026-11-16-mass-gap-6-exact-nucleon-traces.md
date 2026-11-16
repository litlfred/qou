# Mass gap 6: the atom trace on the interleaved Borromean core is exact

**Status.** The gap is closed for the trace object. The new Lean file compiles
with `lean -DautoImplicit=false -s 65536` (exit 0), and `#print axioms` on
`tr_protonWord`, `tr_neutronWord`, `protonPoly_conventionD` and
`neutronPoly_conventionD` shows only `propext`, `Classical.choice` and
`Quot.sound`: no `sorryAx`. No compute value and no mass value moves.
Beans: `qou-5zl1` (block factorisation), `qou-hu1f` (interleaved core ruling).

## The gap as stated

> "Markov trace isn't exact on the interleaved Borromean core; the product
> formula is exact only on grouped words."

The second clause is true and stays true. The **per-generator** product
`tr = ∏_gen (w₊ p(q) + w₋ p(−1/q))` needs each generator's letters to be
contiguous, and the owner-ruled interleaved core `(σ₀σ₁⁻¹)³` breaks that.
The counterexample `tr(σ₀σ₁σ₀) = hz² + z ≠ z³` is enough.

The first clause no longer holds. The pipeline does not need the
per-generator product.

## What was already proved (sorry-free on `main`)

`QOU.Mass.AtomTraceFactorisation.tr_atomWord` covers every Markov trace on a
braided tower:

    tr(W_atom) = ∏_{k} (z + d_k) · P_p^Z · P_n^N

Here `P_p` and `P_n` are the traces of the proton and neutron words on strands
`0, 1, 2`. The proof chains three results:

- the disjoint-block law `HeckeSandwichReduces.disjointBlock_of_braided`;
- block shift-invariance `BraidedBlockShiftTrace.tr_wordVal_shift`;
- the bond-letter product `ProductionChainBondProduct.tr_productionChain_braided`.

It is insensitive to the letter order inside a block, so it holds for the
interleaved word.

**What was missing:** `P_p` and `P_n` were left as abstract traces.

## New: `P_p`, `P_n` exactly

File: `lean/QOU/Mass/NucleonWordTraceClosedForm.lean`. It embeds the H₃
normal-form basis `1, g₀, g₁, g₁g₀, g₀g₁, g₀g₁g₀` into `A`. It then shows that
right multiplication by `g₀` and `g₁` acts as `H3.mulσ₀` / `H3.mulσ₁` on
coordinates; only the quadratic and braid relations are used. The Markov
property gives the basis traces `H3.TRM`. The results:

- `tr_wordVal_eq_trM`: the trace of any affine-letter word on `g₀, g₁` is
  `H3.trM` of a coordinate fold.
- `tr_protonWord` and `tr_neutronWord`: `P_p` and `P_n` are explicit
  polynomials in `h`, `z` and the averaged-letter shift `a`.
- `protonPoly_conventionD` and `neutronPoly_conventionD` give the forms at
  `z = q³/(q²+1)`, `h = q − q⁻¹`, `a = −h/2`:

      P_p = (q⁴+1)(q¹⁸ − 3q¹⁶ + 7q¹⁴ − 8q¹² + 10q¹⁰ − 9q⁸ + 10q⁶ − 6q⁴ + 3q² − 1) / (4q⁹(q²+1)²)
      P_n = (q⁴+1)(q¹⁴ − 3q¹² + 4q¹⁰ − 4q⁸ + 5q⁶ − 4q⁴ + 3q² − 1) / (4q⁹)

The colour-weighted p–n bond shift is `d = −h(1 − δ/2)/2`, with
`δ = (q−1)²(1−q⁻⁴)/3` (`_li_2_q_util.flavor_split_leading`). That is rational
in `q`, so `tr(W_atom) ∈ ℚ(q)` for every nucleus.

## Checks (measured 2026-11-16)

1. **Two independent exact routes agree.** One is the S₃ permutation-basis
   Hecke product; the other is the H₃ normal-form fold that the Lean file uses.
   Both were computed in sympy over `ℚ(q)`.
2. **Borromean core.** The bare `(σ₀σ₁⁻¹)³` at convention D equals
   `(4+h²−3h⁴−h⁶)/(h²+4)`, which is
   `BraidsAndKnots.borromean_markov_trace_closed_form`. The symbolic difference
   is 0.
3. **Against production.** The closed form was compared with
   `tr_M_at_q0_50dps` in `atomic-tr-m-mpfr-50dps-proton.witness.json` (proton
   pin) and `atomic-tr-m-mpfr-50dps.witness.json` (muon pin). Each was
   evaluated at the witness's own 50-digit `q₀`. The cases are proton,
   neutron, ²H, ³H and ³He. **Worst relative difference: 1.2e-49**, which is
   the producer's 50-dps floor. Words were read from `atom_canonical_crossings`
   with the default `intra_order="borromean"`.

## What this does NOT establish

- That the Python producer emits exactly these letters. The words are
  transcribed, and no Lean object reads `atom_braid_word_3A`.
- Anything about the bond scalars `d_k` beyond their production values (bean
  `qou-qqm4`).
- Any binding energy or `c_k`. The trace is exact, and what the pipeline does
  with it is unchanged.
