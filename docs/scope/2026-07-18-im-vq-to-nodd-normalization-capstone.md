# The Im 𝔙_q → N_odd normalization capstone — precise open statement

**Date:** 2026-07-18 · **PR:** #3813 · **Tier:** formalize-first scoping (states
the open problem + constraints + minimal path; nothing wired, nothing fitted).

After the A_ω fork resolution
([`2026-07-18-a-omega-fork-resolution.md`](../audits/2026-07-18-a-omega-fork-resolution.md))
— both branches (deformed median resummation; non-amphichiral 5₂) blocked by the
Lean-proved anchor-invariance prune — the single genuinely-open target is the
geometric normalization that carries the anchor-dependence. This note states it
precisely.

## The target (already characterized; the capstone must reproduce it)

The bar-odd `S` is the `1/u³` ladder-inversion of a **smooth** numerator
(`QOU.QBeta.BarOddLadderShape`, KC21/KC22):

    S(q) = N_odd(q) / u(q)³,   N_odd(q) := S(q)·u(q)³,   u = b·ℏ_q².

`N_odd(q)` is smooth, `O(10⁻⁸)`, with a simple zero at `q*` (the decay-sector
determination of q₀, 80.3% muon-ward), slope `A'(q*) ≈ +2.37`. Its sign-flip and
2.44% cross-anchor swing are **representational** — the `1/u³` amplification of a
smooth numerator crossing zero — and the precision limit is the **experimental
Q_β** (`dq*/dQ_β ≈ −0.54`), not any resummation. This `N_odd(q)` is the exact,
already-committed target (the q* probes, `qbeta_kc19_kappatilde_barodd_source_test`).

## The capstone (open)

> **Conjecture (Im 𝔙_q → N_odd).** There is a geometric quantum-volume functional
> `𝔙_q(q)` (the anchor-dependent complex volume at the substrate q₀) whose
> imaginary part *is* the smooth bar-odd numerator:
>
>     Im 𝔙_q(q) = N_odd(q) = S(q)·u(q)³   (up to a fixed, derived normalization).

This is what the anchor-invariance prune leaves open: `𝔙_q` at q₀ is
anchor-dependent by construction (evaluated at the moving substrate q₀), so it is
*not* excluded by `no_anchor_invariant_realizes_swing` — unlike a fixed knot's
CS, a topological Stokes integer, or the perturbative/saddle faces (all
anchor-invariant, all excluded).

## Constraints the geometric `Im 𝔙_q` must satisfy (formalize-first checklist)

1. **Bar-odd.** `σ(Im 𝔙_q) = −Im 𝔙_q` under `q → q⁻¹` (the sinh channel). Any
   candidate must be intrinsically bar-odd.
2. **Smoothness + simple zero at q*.** Differentiable, `Im 𝔙_q(q*) = 0`,
   `d/dq[Im 𝔙_q](q*) = A'(q*) ≈ +2.37 > 0` (the `hasDerivAt_S_at_qstar` exactness:
   at q* the S-slope is *exactly* `A'/u(q*)³`, no log-derivative correction).
3. **Magnitude O(10⁻⁸).** `Im 𝔙_q(q₀) ≈ N_odd(q₀)`, not the O(0.05) meridian scale
   (the deformed-tower `Im 𝔙̃_b = 0.0585` is the |S|-scale of `S`, i.e. `u³`
   *times* larger than `N_odd` — a candidate must be the numerator, not `S`).
4. **Anchor-dependent, not anchor-invariant.** Must genuinely vary with q₀ at the
   `A'`-slope; excludes every fixed topological datum (prune).

## Pre-named geometric ingredients (not fitted; candidates for the derivation)

- **The 5₂ writhe datum `D_odd = ½(q²−q⁻²) = sinh(u_sub)`** (this session,
  `qbeta_5two_reeb_trace_probe`). A genuine bar-odd sinh-object — satisfies (1),
  but is smooth O(0.21), not O(10⁻⁸): it is a bar-odd *ingredient* of the right
  parity/type, not `Im 𝔙_q` itself. Its role, if any, is as the bar-odd carrier
  the geometric normalization dresses down by `u³·(smooth)`.
- **The deformed complex volume `𝔙(u)`** at the substrate meridian `u = 2 ln q₀`
  (the Ohtsuki/κ̃ tower). Its `Im` at u=0 is 0 (amphichiral); the u-deformed `Im`
  is smooth O(0.05) (the |S|-scale). Candidate for `𝔙_q` *before* the `u³`
  numerator normalization.
- **The `s5-so3` keystone `W_λ` index** (icosahedral geometric realization,
  owner-reversed in scope) — the differential-geometry route to the categorical
  weights that could supply the `A'`-slope from geometry.

## Minimal derivation path (what would close it)

1. **Derive the normalization `Im 𝔙_q → N_odd`** — the map from the geometric
   quantum-volume imaginary part to the `u³`-suppressed numerator. This is *not*
   a resummation (both faces of that are anchor-blind); it is the geometric
   identification of the smooth numerator with a quantum-volume Im.
2. **The anchor-dependence enters through `𝔙_q` being evaluated at the moving
   q₀** — the derivation must show `d/dq[Im 𝔙_q](q*) = A'(q*)` from geometry, not
   fit it. Constraint (2) is the falsifiable target.
3. **Precision ceiling is experimental.** Even a correct geometric `Im 𝔙_q` is
   pinned to the `q*` precision `σ(q*) ≈ 296 ppb` (from `σ(Q_β)`); a ~26× sharper
   neutron Q_β would make q* an arbiter of the μ–p tension.

## Honesty gates (standing)

- No fit: a candidate `Im 𝔙_q` obtained by inverting the anchors is a fit, must
  be labelled one, and may not be wired as canonical (§Axiomatization-is-not-a-
  proof; the anti-laundering rule). Only a *derived* `Im 𝔙_q` closes it.
- The `2·Vol(4₁) = 4.06 ≈ |ratio −4.0751|` (0.38%) coincidence stays
  anti-numerology, **not wired**.
- A §3b conjecture carrier for this capstone (content-bearing class, no instance
  = the open state) is the appropriate Lean representation once a specific
  geometric `𝔙_q` candidate is proposed; premature axiomatization without a
  derivation candidate would be a vacuous carrier.

## Cross-references

- Fork resolution: [`2026-07-18-a-omega-fork-resolution.md`](../audits/2026-07-18-a-omega-fork-resolution.md).
- Ladder shape + rigidity: `QOU.QBeta.BarOddLadderShape`, `MonodromyDatumRigidity`,
  `DoublyPeriodicLiouville` (PR #3813).
- Anchor-invariance prune: `QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing`.
- Swing lives in `D(u)`: the odd-channel q-Borel/Écalle acceleration (sibling #3818).
