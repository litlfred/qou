# c₃⟺q₀ follow-ups: every *real*-magnitude route is closed by a proved invariant; one *fibre-level complex* object survives (and it is the same object for c₃, Δ_λ, and q₀)

**Date:** 2026-07-19 · **Branch:** `claude/agent-pickup-stalled-rtugin` ·
**Axis:** c₃ / Q_β bar-odd swing / Δ_λ closure / q₀ unification ·
**Tier:** consolidation of three follow-up probes · **Discipline:** no fit,
nothing wired, no tier change.

This consolidates the three next-steps the PR #4064 c₃⟺q₀ synthesis proposed,
each pursued independently. They converge: the **real** routes are all closed by
**proved invariants**, and the single surviving open object is a **fibre-level
complex** phase — which is the *same* object for the swing, the Δ_λ closure, and
the q₀ derivation.

## The three follow-ups and their disposition

| # | Proposed route | Disposition | Closing invariant |
|---|----------------|-------------|-------------------|
| **1** | Δ_λ min-norm in the **bar-odd sector** (sign is bar-odd on conjugate pairs) | **already closed** | ℓ¹-ceiling (triangle bound): sign-only re-derivation ≤ 0.36–0.59 × target |
| **2** | **Hilbert–Schmidt matrix-O** resolvent `⟨O,(G−μ)⁻¹O⟩` for the swing | **scope-(a) closed for a *real* resolvent** | bar-parity (`fig8Trace_im_odd`): a real Gram resolvent is bar-EVEN |
| **swing** | swing = **self-dual-locus pole** `1/|u²−1|` | **refuted** | q\* is a *simple* zero (S′,S″ finite); swing is the `1/u³` ladder artifact |

Details:

- **#1 — bar-odd sector already pruned.** The Δ_λ *sign* is proved exact
  (`(−1)^{n(λ)}·dim`; Lean `deltaSign_mixed`, PR #2416), so "min-norm in the
  bar-odd sector" is a *sign/chirality-only* re-derivation (`|Δ_λ|=dim` fixed).
  That class is proved-excluded by the ℓ¹-ceiling invariant
  ([`delta_lambda_l1_ceiling_sign_prune.py`](../../computations/delta_lambda_l1_ceiling_sign_prune.py);
  `‖c‖₁/tgt = 0.358–0.592 < 1` for D/T/³He/⁴He). A magnitude-adding ingredient
  is necessary; a bar-odd magnitude solve against AME is a fit.
  [`2026-07-19-delta-lambda-barodd-sector-already-pruned.md`](2026-07-19-delta-lambda-barodd-sector-already-pruned.md).

- **#2 — real matrix resolvent is bar-even.** Feeding the matrix figure-eight
  operator O through the canonical H₃(q) Gram resolvent
  ([`qbeta_c3_barodd_hs_matrix_resolvent_probe.py`](../../computations/qbeta/qbeta_c3_barodd_hs_matrix_resolvent_probe.py),
  3/3, no fit): no sign flip at any geometric μ (`HS(p)/HS(m)≈+1.0000` vs target
  `−4.08`, incl. the near-pole μ), the pairing is **bar-EVEN**, and the Gram
  eigenvalues shift only ~3×10⁻⁸ (≪ the ~0.014 min gap) so no geometric pole
  enters the anchor window without a ~10⁻⁸ fit — and it would *diverge* (pole),
  not *zero-cross* like S at q\*. A real resolvent built from bar-even
  Markov-trace data cannot carry the bar-ODD S. Reconfirms, from a matrix
  direction, the corpus's bar-parity obstruction and the NZ-deformation argument
  (`qbeta_c3_barodd_nz_deformation_probe.py` finding 4).

- **swing — not a self-dual pole.** The swing is the `1/u³` extractor artifact
  over a *simple* zero of S, not a pole; the pole form `1/|u²−1|≈1` is ~6 orders
  too small. [`2026-07-19-c3-swing-selfdual-pole-vs-ladder.md`](2026-07-19-c3-swing-selfdual-pole-vs-ladder.md).

## The convergence — one surviving object

Removing the closed routes leaves a single open object, and **#2, #3, and the
swing all name it**:

- **#2** (bar-parity): the flip needs a **complex / fibre-level** pole — the
  q-Pochhammer denominator pole `x=q^{−k}` (Lean `qPochDenom_eq_zero_at_pole`)
  combined with the cusp phase `ω=e^{iπ/3}` (Lean `CuspShapeBarParity`) —
  the open **pole→cusp phase `φ(q₀)`** already set up in
  [`qbeta_c3_barodd_pole_cusp_phase_probe.py`](../../computations/qbeta/qbeta_c3_barodd_pole_cusp_phase_probe.py).
- **#3** (F-construction scope): α_EM **R1 is already CLOSED** (merged
  #4039/#4040/#4045; the residual `1/(8π)` is owner-gated R2 physics, explicitly
  *not* Lean-proved). The genuine c₃⟺q₀ crux is **`bwS0_eq_hecke`** — continuing
  the fibre vacuum row `d_q(λ)/D` from a root-of-unity fibre (`q=i`) to real
  `q₀>1` (`s5-so3-keystone.md`; owner-un-gated 2026-07-11).
- **swing / capstone** (result 3+5): the underlying decay projection `Im 𝔙` is
  smooth and lives at the fibre (complex, root-of-unity) level; `Im(q₀)=0` is an
  *archimedean* constraint, not a fibre one (AGENTS.md "Im(q) at fibre vs
  observable level").

These are one object: the **fibre-level complex phase, evaluated by continuation
from root-of-unity to the real substrate `q₀`.** The bar-odd flip (swing sign),
the Δ_λ magnitude ingredient, and the q₀ zero `q*` are three shadows of that
continuation. The real-`q` / real-resolvent / sign-only shadows are provably
insufficient — exactly because the object is fibre-complex, not archimedean-real.

## Correction (2026-07-19, post-frontier-grep): the surviving object splits into a proved-closed VALUE leg and an open SHAPE leg

A follow-up corpus-grep of the fibre frontier
([`2026-07-18-ck-odd-fibre-attack-options.md`](2026-07-18-ck-odd-fibre-attack-options.md);
~24 landed/in-progress 5₂ probes) sharpens "the surviving open object": it is
**not simply open**. It has two legs that must be kept apart:

- **VALUE leg — PROVED-CLOSED (measurement-limited).** The *numeric position* of
  `q*` — hence the swing value — is not derivable below the experimental `Q_β`
  floor. Sorry-free Lean: `QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing`
  (no anchor-invariant fibre datum equals the swinging `S`; scope-(b)) +
  `QOU.QBeta.MeasurementLimitedFloor` (the L2 gate arithmetic). The `2026-07-18`
  attack map records the same as its structural fact 1 (`dq*/dQ_β ≈ −0.54`; a
  fibre derivation supplies the **shape**, not the sub-floor **value**).
- **SHAPE leg — open, actively worked.** A fibre derivation must produce the
  bar-odd carrier `N_odd` with the right shape (simple zero at `q*`, slope
  `≈ +2.37`). This is the 5₂-chiral fibre program (4₁ is amphichiral ⇒ its
  bar-odd channel vanishes identically, so the odd datum needs the chiral 5₂);
  A1 (chirality state integral), A4.1/A4.2 (φ-series engine to order 24), and
  A5.2 (N=3 cable arbitration) have landed there.

This corrects the headline above: the swing/Δ_λ/`q*` shadows converge on a fibre
object whose **value is proved un-derivable** and whose **shape** is the live
front — not a single wholly-open object.

## Typed target (this branch): `SelfDualLocusTargetSpec.lean`

To make the SHAPE leg a *typed* object rather than prose, this branch adds
[`QOU/QBeta/SelfDualLocusTargetSpec.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/SelfDualLocusTargetSpec.lean)
(sorry-free, generic-`R`, §7c), mirroring the honest
`QOU.Archimedean.TauFunctorTargetSpec` pattern: `BarOddCarrierTarget` types the
interface a fibre derivation must supply (a bar-odd carrier `N` with `σ(N x)=−N x`
and a zero at `qStar`), a proved consequence (`even_symmetrization_at_star`: the
odd carrier contributes nothing to the bar-even channel at `q*`), and a
machine-checked honesty theorem (`trivial` / `trivial_carrier_zero`: the `N ≡ 0`
carrier satisfies every field, so the interface *alone* is content-free — the wall
is the fibre provenance of the specific `N` plus the proved-closed value leg,
never the interface). Nothing is wired; `q*`'s value stays measurement-limited.

## Recommended next step (typed, no-fit; not executed here)

Per the #3 scout's plan, the cheapest way to convert the surviving "shared simple
zero q\*" from a numerical coincidence into a **typed structural object** (or an
honest scope-(a) negative) reuses two *sorry-free* Lean building blocks —
`KeystoneSelfDualSpectralNarrowing.lean` (self-dual `C=+1` sector, eigenvalues
4th-roots of unity) and `CrossingWeightAffine.lean` (bar-odd ladder part linear
in `(w−w₀)` × fixed kernel) — plus the **already-proved** α_EM N3 braid-twist ↔
deck-generator conjugacy (`alpha_em_r1_n3_eigenline_probe.py`, sympy-exact):

1. Type the q₀=c₃ target as a Lean `TargetSpec` (fibre-level, generic-`R`, §7c) —
   *a typed target, not a claim it is inhabited*.
2. Run one bounded, exact, kill-criteria-pre-stated naturality-square probe:
   does the α_EM N3 braid twist act compatibly on the self-dual `C=+1`
   vacuum-row sector, with `q*` the point where its crossing-weight departure
   `(w−w₀)` vanishes bar-oddly? Discriminates "q\* structural" from "q\*
   numerical coincidence (fit — reject)".

Anti-laundering stays in force (AGENTS.md): a q\* numerical match, an
AME-inversion, or an axiomatized conditional class is **not** a derivation and
may not wire to production.
