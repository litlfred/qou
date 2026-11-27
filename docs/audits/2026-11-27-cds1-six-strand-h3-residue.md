# H₆ → H₃ residue of the six-strand γγ survivors (bean `qou-cds1`, route C step 2)

Date: 2026-11-27. Follows [`2026-11-27-cds1-six-strand-neutral-selection.md`](2026-11-27-cds1-six-strand-neutral-selection.md)
(58 reading-3 survivors among neutral six-strand V-words of length ≤ 6).
Probe: [`six_strand_h3_residue_probe.py`](../../computations/probes/gg_six_strand/six_strand_h3_residue_probe.py),
witness `six-strand-h3-residue.witness.json`. Exact over Q(q); characters
`χ_μ(E_{6→m}(W))` from `gg_ntower_probe.level_chars` (convention-D conditional expectation),
m = 3..6, μ two-row.

## Results

1. **Reading 3 holds at every intermediate level at q₀.** For all 58 survivors and every
   m = 3, 4, 5, 6 and every two-row μ ⊢ m, `χ_μ(E_{6→m}(W)) ≥ 0` at q₀. Step 1 only checked m = 6.
2. **It does not hold on all of q > 1.** Every survivor has some level character that changes sign
   on (1, 2); the smallest such root over all 58 is q ≈ 1.3723, well above q₀ ≈ 1.110. So the
   selection is a statement at q₀ and nearby, not an identity in q.
3. **The H₃ residue is the Borromean core up to a scalar close to 1.** With the H₃ core
   `V³ = (σ₀σ₁⁻¹)³` (χ_(3) = 1, χ_(2,1) = −(q⁴−q²+1)(q⁸−2q⁶−2q²+1)/q⁶):
   - `V₀³` restricts to the core exactly (it already lives in H₃).
   - `V₂³` and `V₃³` have the **same** residue, and for disjoint products the residue factorises:
     `E_{6→3}(V₀³V_j³) = c(q)·V₀³` for j = 2, 3, with the single scalar
     `c(q) = −(q¹²−3q¹⁰+2q⁸−4q⁶+2q⁴−3q²+1)/(q⁴(q²+1)²)`, `c(1) = 1`, `c(q₀) = 0.99856…`.
     The same factorisation holds for every interleaving of V₀ with V₃ and for the block
     arrangements of V₀ with V₂.
   - `V₁³` is not proportional to the core: its (3) and (2,1) ratios differ
     (the (3) ratio is `−(q⁶−3q⁴+2q²−2)/(q²+1)`, 0.99440… at q₀).
   - All residue/core ratios equal 1 at q = 1.

## Reading

Moving from H₆ to H₃ along the neutral, reading-3-selected words changes the core only at
order h² (ratios 1 + O(h²), within 0.6 % of 1 at q₀ for the single cubes). The six-strand level
therefore supplies no factor of order 2 on the V³ base. This is a structural observation; no
measured value enters, and it is not compared against the Q_β target to select anything.

## Scope (not established)

- Words of length ≤ 6 vertices only (inherited from step 1).
- "c(q) factorisation" is observed on the enumerated words, not proved; a Lean proof would go
  through the convention-D Markov property `E(x·y) = x·E(y)` for x in H₃.
- Scope (a): measured on an enumerated class.
