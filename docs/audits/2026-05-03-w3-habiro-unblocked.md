# W-3 unblocked: cyclotomic Habiro coefficients for A ≥ 3

**Date:** 2026-05-03
**Branch:** `claude/w3-w4-followups`
**Ref:**
- [`habiro_coefficients_extended.py`](../../folio-assistant/computations/habiro_coefficients_extended.py)
- [`habiro-coefficients-extended.witness.json`](../../folio-assistant/computations/habiro-coefficients-extended.witness.json)

## Background

The previous symbolic-q pipeline,
[`habiro_coefficients_atomic.py`](../../folio-assistant/computations/habiro_coefficients_atomic.py),
took 10+ minutes per atom even for the deuteron (A = 2) and was
documented as **intractable for A ≥ 3** (it builds Hoefsmit-symbolic
matrices over partitions of 3·A and runs simplification on the full
seminormal Markov-trace expression). That blocker had been the
binding constraint for:

- W-3 (Term-6 cluster extension to higher-A atoms in
  [`docs/audits/2026-05-03-next-session-plan-to-1ppb.md`](2026-05-03-next-session-plan-to-1ppb.md))
- The “analytical D(u)” research question raised in the W-3 explore
  pass (see PR #521,
  [`habiro-coefficients-interpolate.witness.json`](../../folio-assistant/computations/habiro-coefficients-interpolate.witness.json)).

## Resolution

The **`markov_peel.tr_M_atomic(..., return_symbolic=True)`** path that
landed in PR #520 produces a sympy expression in q in seconds rather
than minutes:

| Atom | A | n_strands | sympy ops | wall time |
|------|---|-----------|-----------|-----------|
| D    | 2 | 6         | 1,449     | 2 s       |
| T    | 3 | 9         | 12,164    | 4 s       |
| ³He  | 3 | 9         | 5,420     | 3 s       |
| ⁴He  | 4 | 12        | 38,840    | 20 s      |
| ⁵Li  | 5 | 15        | 95,640    | 95 s      |
| ⁶Li  | 6 | 18        | (pending) | ~10 min   |

A single `sp.together(...)` then collapses the rational expression
to numerator/denominator form, and the existing
`habiro_coefficients_atomic.to_u_polynomial` + `cyclotomic_expansion`
pipeline produces the integer Habiro coefficients without
modification.

## Closed-form structure of D(u)

For every atom we have tested, the Markov-normalisation denominator
admits a clean factored form:

| Atom | A | D(u) (factored) |
|------|---|-----------------|
| D    | 2 | `2^5  · u^40 · (1 + u²)^5`   |
| T    | 3 | `2^7  · u^61 · (1 + u²)^8`   |
| ³He  | 3 | `2^7  · u^58 · (1 + u²)^8`   |
| ⁴He  | 4 | `2^9  · u^79 · (1 + u²)^11`  |
| ⁵Li  | 5 | `2^11 · u^97 · (1 + u²)^14`  |

Two regularities are immediate:

- **Power of 2:** `2^(2A + 1)` (5, 7, 7, 9, 11 for A = 2..5).
- **Cyclotomic exponent:** `(1 + u²)^(3A − 1)` (5, 8, 8, 11, 14 for A
  = 2..5).

The u-shift residual carries an isospin-dependent fine structure
(T = 61 vs ³He = 58 at A = 3) that no clean closed form has been
found for yet — it is left as an open observation.

## Proof of the closed form (2^(2A+1) and (1+u²)^(3A-1))

See [`d_u_closed_form_proof.py`](../../folio-assistant/computations/d_u_closed_form_proof.py)
and its witness
[`d-u-closed-form-proof.witness.json`](../../folio-assistant/computations/d-u-closed-form-proof.witness.json).

### `(1 + u²)^(3A − 1)` factor

The Ocneanu / Markov trace formula for an n-strand braid
β ∈ B<sub>n</sub> with image ρ(β) ∈ H<sub>n</sub>(q) is

> tr<sub>M</sub>(β)  =  z<sup>n − 1</sup> · trace<sub>M</sub>(ρ(β))

where z = 1 / (q<sup>1/2</sup> + q<sup>−1/2</sup>) is the Markov
parameter and trace<sub>M</sub> is the Hecke-algebra Ocneanu trace.
Substituting q = u² gives

> z = u / (1 + u²)  ⇒  z<sup>n−1</sup> = u<sup>n−1</sup> / (1 + u²)<sup>n−1</sup>.

For an atomic braid the strand count is n = 3A, so clearing the
denominator from tr<sub>M</sub>(u²) yields exactly (1 + u²)<sup>3A − 1</sup>
in D(u).  ∎

### `2^(2A + 1)` factor

Inspection of `atomic_braid_to_crossings(Z, N, include_inter=True)`
(see [`folio-assistant/computations/hecke_character_symbolic.py`](../../folio-assistant/computations/hecke_character_symbolic.py)
together with the per-nucleon crossing tables `proton_cross` /
`neutron_cross` in
[`mass_endomorphism.py`](../../folio-assistant/computations/mass_endomorphism.py))
shows three classes of crossings, each tagged "sigma", "sigma_inv",
or "averaged".  The "averaged" generator represents the operator
(σ + σ<sup>−1</sup>) / 2; its 1/2 prefactor becomes a factor of 2 in
D(u) for every averaged crossing in the braid.

Counting averaged crossings:

- **Per nucleon:** exactly 2 (the two ud-pair couplings, one at
  gen_idx 0 and one at gen_idx 1, marked `(1.0, -h/2)` in the
  per-nucleon dictionaries).  Total intra-nucleon: **2A**.
- **Inter-nucleon (canonical pppnnn ordering):** the link between
  adjacent nucleons of types (p, p) is `sigma`, between (n, n) is
  `sigma_inv`, and between (p, n) is `averaged`.  In the canonical
  ordering with all Z protons followed by all N neutrons, there is
  exactly **one** (p, n) interface for any (Z, N) with Z, N ≥ 1.
  Total inter-nucleon averaged: **1**.

Total averaged crossings: 2A + 1 ⇒ D(u) carries the prefactor
**2<sup>2A + 1</sup>**.  ∎

### Predictions (forward-looking)

| Atom | A | predicted 2^(2A+1) | predicted (1+u²)^(3A−1) |
|------|---|---------------------|--------------------------|
| ⁶Li  | 6 | 2^13 = 8192         | (1+u²)^17               |
| ⁷Li  | 7 | 2^15 = 32768        | (1+u²)^20               |
| ⁸Be  | 8 | 2^17 = 131072       | (1+u²)^23               |

These predictions are verified by `d_u_closed_form_proof.py` against
the structural braid-crossing count.  Numerical confirmation against
markov_peel symbolic awaits the corresponding witness rows for
A ≥ 6.

## Closed-form structure of a_0

The leading Habiro coefficient at m = 0 is also clean:

| Atom | A | a_0     | 2^(3A+1) check |
|------|---|---------|----------------|
| D    | 2 | 128     | 2^7  ✓         |
| T    | 3 | 1024    | 2^10 ✓         |
| ³He  | 3 | 1024    | 2^10 ✓         |
| ⁴He  | 4 | 8192    | 2^13 ✓         |

Hence **a_0 = 2^(3A + 1)** across all A = 2, 3, 4 atoms tested.

## Implications

1. **W-3 is unblocked.** The Mittag-Leffler full pole sum
   (`term6_full_pole_sum.py`) needs the cyclotomic Habiro
   coefficients to evaluate Term 6 at higher-A atoms; this script now
   provides them. The previous interpolate-path note that the
   “analytical D(u) is the next step” is superseded.
2. **No D(u) sampling needed.** The numerical-interpolation path
   ([`habiro_coefficients_interpolate.py`](../../folio-assistant/computations/habiro_coefficients_interpolate.py))
   was scaffolded as a fallback; with markov_peel symbolic available,
   sampling D(u) by Vandermonde + rounding is no longer required.
3. **Closed-form D(u) is a structural finding.** The 2^(2A+1) ·
   u^? · (1+u²)^(3A−1) pattern strongly suggests a categorical
   derivation from the Hoefsmit–Yangian seminormal denominators
   (axial-distance factors for adjacent contents) combined with the
   atomic-braid word length. Documenting this for paper-side follow-up.

## What this does NOT close

- **Family-4 B_pred** (⁶Li, ⁷Li, ⁹Be, ¹¹B, ¹⁴N, ¹⁹F): closing the
  Kashaev-law-style formula `B = ρ_F · m_e · Vol_hyp(K)` for these
  atoms still requires a derivation of ρ_F or, equivalently, the
  structural prefactor in the categorical-mass identity
  `B = m_e · ρ_t · tr_M(T_w)`. The implied ρ_t values are now
  exposed per-atom in
  [`b-over-a-v5-unified.witness.json`](../../folio-assistant/computations/b-over-a-v5-unified.witness.json)
  as a research diagnostic but admit no clean closed form so far
  (D = 11.21, T = 159.5, ³He = 73.1, ⁴He = 1000.5; no obvious A·c^A
  fit). This is the W-1 / GAP-A residue.
- **W-2 (real) — N_v categorical derivation**: still pending. N_v is
  q-independent and cannot be probed by the multi-q test that
  refuted W-2's b8 / q^(1/12) candidates in PR #521.

## References

- `markov_peel.tr_M_atomic` — PR #520 / PR #516 (#508).
- W-3 explore note from PR #521:
  [`habiro-coefficients-interpolate.witness.json`](../../folio-assistant/computations/habiro-coefficients-interpolate.witness.json).
- 1-ppb workplan:
  [`docs/audits/2026-05-03-next-session-plan-to-1ppb.md`](2026-05-03-next-session-plan-to-1ppb.md).
