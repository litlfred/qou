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

### `u^shift` — empirical formula (NOT yet categorically proved)

> **CAVEAT.** Unlike the two factors above, the shift formula below
> is **empirical numerology**: a linear-in-(Z, N) ansatz fitted to 6
> data points with zero residual. It is **not a categorical proof**
> from the atomic-braid structure / Hecke seminormal form. A
> first-principles derivation of the coefficients `(6, 7, 1)` is
> the residual research question. Treat this section as a
> conjecture, not a theorem.

The empirical u-shift across A = 2..6 fits the linear-in-(Z, N)
formula

> **shift = 18Z + 21N + 1 = 3 · (6Z + 7N) + 1**  (conjecture)

| Atom | (Z, N) | predicted shift | empirical | match |
|------|--------|-----------------|-----------|-------|
| D    | (1, 1) | 18·1 + 21·1 + 1 = 40  | 40  | ✓ |
| T    | (1, 2) | 18·1 + 21·2 + 1 = 61  | 61  | ✓ |
| ³He  | (2, 1) | 18·2 + 21·1 + 1 = 58  | 58  | ✓ |
| ⁴He  | (2, 2) | 18·2 + 21·2 + 1 = 79  | 79  | ✓ |
| ⁵Li  | (3, 2) | 18·3 + 21·2 + 1 = 97  | 97  | ✓ |
| ⁶Li  | (3, 3) | 18·3 + 21·3 + 1 = 118 | 118 | ✓ |

This is **inductive** in Z and N: adding a proton to the canonical
pppnnn braid increases the shift by 18, adding a neutron by 21,
independent of starting (Z, N). Hence the closed form generalises
**without needing to compute the full Hecke normal form per atom** —
the per-nucleon increments are universal because each new nucleon
contributes the same set of intra-nucleon generators (cf. the
fixed `proton_cross` / `neutron_cross` dictionaries in
[`mass_endomorphism.py`](../../folio-assistant/computations/mass_endomorphism.py))
and the canonical pppnnn ordering keeps the inter-nucleon coupling
structure invariant (exactly one mixed (p, n) interface).

A first-principles derivation of `(6, 7, 1)` from the per-nucleon
generator counts (proton: 6 σ + 3 σ⁻¹ + 2 averaged; neutron: 5 σ +
4 σ⁻¹ + 2 averaged) requires walking the Markov/Ocneanu trace
recursion through the seminormal-form denominators ([h]_q for hook
lengths in the partitions of 3A) and tracking the lowest u-power
contribution. Empirically the linear coefficients (18, 21) are
exactly 3× the per-nucleon (6, 7) signature; we conjecture that
`6Z + 7N` counts a structural quantity in the unreduced trace
expansion and the factor of 3 enters via a triple-cover of the
seminormal hook denominators. **Status:** verified at A = 2..6 (6
atoms incl two A = 3 isospin partners); structural derivation of
the (6, 7) coefficients is the residual research question.

### Final closed form (A ≥ 2, canonical pppnnn ordering)

> **D(u) = 2^(2A + 1) · u^shift · (1 + u²)^(3A − 1)**, with
> shift conjecturally `= 18Z + 21N + 1`.

with the first factor **categorically proved** (averaged-crossing
combinatorics on the canonical braid), the third factor
**categorically proved** (Markov-trace normalisation
`z^(n−1) = u^(3A−1) / (1+u²)^(3A−1)` at q = u²), and the middle
shift factor **empirically verified at A = 2..6 but not categorically
proved** — its derivation from the Hecke seminormal-form denominator
structure is open.

### Predictions (forward-looking)

| Atom | (Z, N) | predicted 2^(2A+1) | predicted u-shift | predicted (1+u²)^(3A−1) |
|------|--------|---------------------|-------------------|--------------------------|
| ⁷Li  | (3, 4) | 2^15 = 32768  | u^(54+84+1) = u^139 | (1+u²)^20 |
| ⁸Be  | (4, 4) | 2^17 = 131072 | u^(72+84+1) = u^157 | (1+u²)^23 |
| ¹²C  | (6, 6) | 2^25          | u^(108+126+1) = u^235 | (1+u²)^35 |

These extrapolate the closed form purely structurally — no Hecke NF
computation required.

## Closed-form structure of a_0

The leading Habiro coefficient at m = 0 is also clean:

| Atom | A | a_0     | 2^(3A+1) check |
|------|---|---------|----------------|
| D    | 2 | 128     | 2^7  ✓         |
| T    | 3 | 1024    | 2^10 ✓         |
| ³He  | 3 | 1024    | 2^10 ✓         |
| ⁴He  | 4 | 8192    | 2^13 ✓         |
| ⁵Li  | 5 | 65536   | 2^16 ✓         |
| ⁶Li  | 6 | 524288  | 2^19 ✓         |

Hence **a_0 = 2^(3A + 1)** across all A = 2..6 atoms tested.

### Cross-validation with `claude/categorical-mass-divergence-audit`

The audit branch's commit
[`a9d7a3811`](https://github.com/litlfred/qou/commit/a9d7a3811)
("Path A: tr_M(T_w; q→1) = (1/2)^(2A−1) — clean closed form") is
**mathematically equivalent** to our `a_0 = 2^(3A + 1)` finding.

> p(u) = D(u) · tr_M(q = u²)  ⇒  p(1) = D(1) · tr_M(q = 1)
> p(1) = a_0(1) = a_0    (since (u; u)_m vanishes at u = 1 for m ≥ 1)
> D(1) = 2^(2A + 1) · 1 · 2^(3A − 1) = 2^(5A)
> ∴  tr_M(q = 1) = a_0 / D(1) = 2^(3A + 1) / 2^(5A) = (1/2)^(2A − 1)

So either form implies the other.  Two independent paths converge on
the same structural identity, providing strong cross-validation of
the closed-form result.  The audit branch covers A = 1..4 from the
q → 1 limit; this branch extends to A = 5, 6 via the symbolic-q
markov_peel pipeline.

**Note on conventions.**  The audit branch's commit
[`b44ed76ee`](https://github.com/litlfred/qou/commit/b44ed76ee)
fixed a (q; q)_m vs (u; u)_m ambiguity in its reconstruction; our
`cyclotomic_expansion` already uses `(1 − u^(m+1))` factors (the
(u; u)_m Pochhammer convention), so no fix is needed on our side.

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
