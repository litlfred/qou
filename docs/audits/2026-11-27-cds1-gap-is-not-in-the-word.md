# The Q_β magnitude gap is not in the choice of γγ word (bean `qou-cds1`, synthesis)

Date: 2026-11-27. Owner card "Pick the next attack on the Q_β gap", recommended option
"Synthesis + Lean factorisation" (worked while the card is open).

## Statement

On the ruled base (ε = Markov trace at z_D, scored element V³ selected by γγ + linking
neutrality, rulings 2026-11-20/21/25), the scored `Q_β = |ε(V³)|·E₀ = 0.3254 MeV` sits about a
factor 2.4 below CODATA. This note collects the evidence that **no choice of γγ word closes that
factor**, so the gap belongs to conjecture C1 (which functional is the decay trace) or C3 (the
energy map) of `QOU.QBeta.DecayConjectures`, both owner questions.

## Evidence

1. **Four strands, climbing family** (PR #9530, Lean, scope (b), invariant writhe):
   `e₀e₂Σ₁ᶜ` has no neutral term for c ≥ 1.
2. **Six strands, selection** (PR #9536, scope (a), length ≤ 6): neutral + reading 3 keeps 58
   words, all products of cores `V_i³`.
3. **Six strands, H₆ → H₃** (PR #9556): the H₃ part of every survivor is the core times a
   scalar within 0.6 % of 1 at q₀.
4. **The scalar is the Markov trace of the core** (this PR,
   [`six_strand_markov_factor_probe.py`](../../computations/probes/gg_six_strand/six_strand_markov_factor_probe.py), 5/5, exact):

       c(q) = tr_M(V³) = −(q¹²−3q¹⁰+2q⁸−4q⁶+2q⁴−3q²+1) / (q⁴(q²+1)²),   tr_M(V³)(q₀) = 0.998562…

   `E_{6→3}(V₂³) = E_{6→3}(V₃³) = tr_M(V³)·1` and `E_{6→3}(V₀³V₃³) = tr_M(V³)·V₀³`: a second
   nucleon core reaches H₃ as a factor `tr_M(V³)`, which is 1 + O(h²). `E_{6→3}(V₁³)` is not a
   scalar but is within 0.6 % of the core on both blocks.
5. **One shared element** (PR #9453, Lean, scope (b)): if both nucleons carry the same element,
   only the Cartan weight separates them; the linear energy map makes the neutron lighter for
   every element, and the Gibbs map gives the word-independent cell `2E₀·log q`. No word can
   move it.
6. **Other parameter-free routes** (PRs #9475, #9544, #9560): Gibbs + Coulomb needs λ ≈ 9·α·E₀
   for Q_β; the V³ diagonal gives 0.79–0.94 MeV for the split; the four-strand lepton reading
   at most 0.354 MeV.

## Consequence

Within the γγ grammar, extra cores contribute powers of `tr_M(V³) = 1 + O(h²)`, and a single
shared element cannot separate the nucleons beyond the Cartan weight. A factor of order 2 must
come from C1 or C3, not from the word. This is scope (a) for items 2–4 (enumerated lengths) and
scope (b) for items 1 and 5 (proved invariants).

## Not established

- Lean form of item 4. The repo's `MarkovTrace` class is single-level (`tr(xσ_{n−1}) = z·tr(x)`)
  and has no tower inclusion, so the shifted-copy factorisation `E_{6→3}(x·y) = tr_M(y)·x` cannot
  be stated against it as is. Tracked as a follow-up in the bean.
- Lengths above 6 vertices.
