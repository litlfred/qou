# α\* presentation-dependence — H_3 vs H_5 — discriminating test result

**Source.** `tools/hecke-engine/src/bin/dump_block_matrices.rs` extended with
`evaluate_all_blocks` PSD report on the symmetric part of ρ_λ(T_w),
matching `sdp_verifier`'s convention.

## The discriminating test

³H at H_5 fails PSD on all d_λ ≥ 4 blocks (α\* = 0.424). To decide
between hypotheses for that anomaly:

- H1: wrong historical knot ID (8_11 mismatched)
- H2: Hoefsmit sign-bug at d_λ ≥ 4
- H3: Markov-stabilization sign error H_4 → H_5

Take a **known-good** atom (proton, α\* = 1 at native H_3) and
Markov-stabilize it to H_5 by appending σ_3 σ_4. The Markov closure
is unchanged; the Markov-trace value is unchanged (modulo a
z-factor per stabilization). If H1 holds, proton-at-H_5 should
remain α\* = 1 (it's the same link; only the historical-ID issue
plagues ³H).

## Result

```
## proton (native H_3, [1, -2, 1, -2, 1, -2])
  α* = 1.000   (witness)

## proton-H5 (stabilized to H_5, [1, -2, 1, -2, 1, -2, 3, 4])
  λ                     d_λ  min eig (sym)  max eig (sym)  PSD?
  [5]                      1       1.232052       1.232052  ✓
  [4, 1]                   4      -0.606253       1.249239  ✗
  [3, 2]                   5      -0.617185       1.216098  ✗
  [3, 1, 1]                6      -0.625631       1.239561  ✗
  [2, 2, 1]                5      -0.606546       0.822343  ✗
  [2, 1, 1, 1]             4      -0.609945       0.818101  ✗
  [1, 1, 1, 1, 1]          1       0.811654       0.811654  ✓
  α* < 1
```

**Proton-at-H_5 fails PSD on every d_λ ≥ 4 block.**

## Implication

The Markov closure of `[1,-2,1,-2,1,-2,3,4]` equals the Markov
closure of `[1,-2,1,-2,1,-2]` (one σ_n stabilization preserves the
closure up to ambient isotopy of the link). **Same link → same
hyperbolic volume, same Jones polynomial, same Markov trace.** Yet
the PSD-cone α\* number changes from 1.000 to < 1 just by changing
the Hecke-algebra representative.

Therefore **α\* is not a Markov-class invariant** — it depends on
the specific braid-word representative within the Markov-equivalence
class. The α\* = 0.424 number for ³H/8_11 alone cannot refute the
historical knot ID; the same identity test on a different
representative of 8_11's Markov class might give α\* = 1.

## What this rules in / out for ³H

- **H1 (wrong knot ID for ³H) cannot be concluded from α\*
  alone.** A separate Markov-class-invariant test (symbolic tr_M
  evaluated against `J_{8_11}(q)`) is needed to refute the ID.
- **H2 (Hoefsmit sign-bug at d_λ ≥ 4) is now the leading
  hypothesis** for the *evaluator* anomaly: if all multi-d blocks
  in proton-H_5 are also indefinite under Hoefsmit's seminormal
  form, the issue is in the projection at d ≥ 4.
- **H3 (Markov-stabilization sign error) merges with H2**: the
  effect of appending σ_n to an x ∈ H_{n-1} is precisely what gets
  evaluated under Hoefsmit at the new partitions of n; if H2
  governs, H3 follows.

## Follow-up: natural H_5 elements all fail at d_λ ≥ 4

To isolate H2 (general d ≥ 4 issue) from a stabilization-specific
effect, the dump-block-matrices binary now also handles two
"natural" H_5 elements (no H_{n-1} factorisation):

  σ_1 σ_2 σ_3 σ_4 σ_3 σ_2 σ_1     (5-strand cycle)
  σ_1 σ_2 σ_3 σ_4 σ_1 σ_2 σ_3 σ_1 σ_2 σ_1   (positive half-twist Δ_5)

Both fail the symmetric-part PSD test on every d_λ ≥ 4 block, with
min eigenvalues of order O(1). The cycle even fails the d_λ = 1
sign block.

**This is generic.** The symmetric-part of Hoefsmit's seminormal
ρ_λ(braid_word) at d_λ ≥ 4 generically has both signs of
eigenvalues for non-trivial braids, regardless of stabilization
or knot ID.

The proton/neutron at native H_3 happen to pass (`α* = 1`) because
their alternating 6-letter Borromean has a special structure that
makes ρ_{(2,1)} eigenvalues both ≈ 1 (the d_λ = 2 case).

## Reinterpretation: what α\* actually measures

The α\* metric in `prop:atom-knot-mass-derivation`'s "PSD-cone α\*
ranking" table tests whether the symmetric part of ρ_λ(braid_word)
at q_0 has all-positive eigenvalues, blended with identity by α.

But:

- **ρ_λ(braid_word) is generally non-symmetric** at d_λ ≥ 2 (Hoefsmit's
  matrices have upper-triangular plus 2×2-block form per σ_i; products
  are generically non-symmetric).
- Markov-equivalent braid words (same closure, same link) give
  *different* α\* (proton at H_3 vs proton-H_5 above).
- "Natural" H_5 braids almost always fail the test.

**Therefore α\* < 1 is not a structural refutation of the
historical knot ID, nor of the categorical pipeline; it just
records that this particular braid representative has an
indefinite-symmetric-part ρ_λ at some d_λ ≥ 4.** The metric is
sensitive to the choice of representative, not the underlying
link.

## What the 1 ppb investigation should focus on instead

1. **Markov-class invariants.** tr_M(T_w) in ℚ(q), |tr_M(T_w)|,
   q-Murnaghan–Nakayama character values χ_λ(T_w). These are
   independent of the braid representative (modulo Markov moves)
   and are the actual quantities that enter the mass identity
   B(𝔥) = m_e · ρ · |tr_M(T_w)|.
2. **The actual joint-tower SDP's PSD constraint.** That constraint
   is `ρ_λ(T_w) ⪰ 0` where T_w is the SDP *variable* (a candidate
   canonical Hecke element to be solved for), not a fixed braid
   word. The R5-full path solves for T_w; the R5-minimal verifier
   tests a *given* T_w. The two tests don't address the same
   question.
3. **Symbolic tr_M evaluation in MPFR @ 50 dps.** Already validated
   end-to-end for the proton (commit `d7d1311b`); extend to neutron,
   ²H, ³H, ³He, electron, and the magic-A clusters.

## Reframing the master prop

The "5 of 7 blocks fail PSD — *largest gap* in registry" diagnostic
for ³H/8_11 in `prop:atom-knot-mass-derivation` should be revised
to acknowledge that this is a generic feature of multi-d Hoefsmit
projections at d_λ ≥ 4, not a structural anomaly specific to
8_11. The master prop's α\* table remains useful as a *consistency
check on a specific representative*, but should not be read as a
refutation of historical knot IDs.

The actual structural test for "is K_historical the right knot
for atom 𝔥?" is: does the symbolic tr_M(T_w_historical, q) match
the published Jones polynomial J_{K_historical}(q) up to writhe
normalisation? This is the test atom_nf_symbolic_D.py was set up
to perform; the per-isotope refresh is straightforward.

## Reframing the master prop's α\* table

The α\* table in
[`prop:atom-knot-mass-derivation`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)
("PSD-cone α\* ranking, Rust R5-minimal") interprets α\* < 1 as a
PSD-cone gap that "quantifies the gap from the boundary in the
α-direction". This interpretation is **valid for the specific
representative** the witness records, but should not be over-read
as a structural refutation of the historical knot ID. The
α\* values for ²H (0.546) and ³H (0.424) are evidence of a
suboptimal braid-word presentation, not necessarily of a wrong
knot.

A Markov-class-invariant audit — comparing the symbolic tr_M(T_w)
in ℚ(q) against the published Jones polynomial J_K(q) for each
historical K — is the correct path to confirming or refuting the
historical IDs. That work belongs to Plan G's expansion (currently
unblocked only for ³He) and to the R5-full SDP-as-solver
deliverable.
