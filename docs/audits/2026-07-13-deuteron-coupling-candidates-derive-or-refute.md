# Deuteron entanglement coupling x ≈ 1/√2 — derive-or-refute: one exact symbolic survivor (S₀₀ at n=2), numerically refuted; the resummation never reaches B_D at *any* coupling

**Date:** 2026-07-13 · **Branch:** `claude/mass-binding-errors-9zqpal` ·
**Probe:** [`deuteron_coupling_s00_probe.py`](../../computations/deltalambda/deuteron_coupling_s00_probe.py)
(+ [`deuteron-coupling-s00-derive-or-refute.witness.json`](../../computations/deltalambda/deuteron-coupling-s00-derive-or-refute.witness.json)) ·
**Scope:** (a) negative, no fit. Closes Target 2 of
[`2026-07-13-a3-split-borromean-redirect-and-deuteron-coupling.md`](2026-07-13-a3-split-borromean-redirect-and-deuteron-coupling.md)
and **corrects** an extrapolation in
[`2026-07-13-deuteron-wall-full-transseries-negative.md`](2026-07-13-deuteron-wall-full-transseries-negative.md) (#3736).

## The question

The full level-1/2 Borel–Laplace median resummation of the Gevrey-1/2 binding
period undershoots `B_D = 2.225 MeV` ~37× at every substrate coupling
(`ℏ_q², ℏ_q, t = ln q₀ ≈ 0.10`); #3736 reported that it "reaches B_D only as
x → 1/√2", the Borel radius — and pinning `x = 1/√2` by fiat is circular. Target
2 asked: does the corpus supply an **independent, derived** quantity equal to
≈ 0.707 that could serve as the entanglement coupling of the Hopf (two-nucleon)
bipartition? Formalize-first: every candidate is checked **symbolically** before
any numerics; no wide scan.

## Candidate table

| # | Candidate | Symbolic value | = 1/√2? | Structurally motivated as the coupling? |
|---|---|---|---|---|
| C1 | Hopf-link Jones / Markov trace `J_Hopf(q) = −(q+q⁻¹) = −[2]_q` | `J_Hopf(1) = −2` exact; `\|J_Hopf(1)\|^{−1/2} = 1/√2` exact; `1/√([2]_{q₀}) = 0.70519` | only via an inverse-square-root transform (exact at q=1, −0.27% at q₀) | **No — relabel.** Nothing selects the `^{−1/2}` transform; the bare corpus object is `−2`, not `0.707`. |
| C2 | **S-matrix / Verlinde amplitude of the n=2 bipartition**: corpus keystone `bwS0(λ) = d_q(λ)/D` ([`KeystoneVerlindeSMatrixBridge.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/KeystoneVerlindeSMatrixBridge.lean)); at n=2 both blocks `(2),(1,1)` have `d_q = 1` at **every** q (Lean-witnessed, [`WLambdaMTCLocalizationObligation.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaMTCLocalizationObligation.lean) non-vacuity witness) | `D = √2`, `S₀₀ = 1/√2` **exact, q-independent**. Equivalently `W_λ = (1/2, 1/2)` = Hopf-pair reduced-density eigenvalues, Schmidt amplitude `1/√2`, entanglement entropy `ln 2` — the SU(2)₁-style match | **YES — exact** | **Partial, not derived** (see below) — and numerically refuted even if granted |
| C3 | Cusp modulus / geometric data of the Hopf link | — | — | **Empty.** The Hopf link is not hyperbolic (Vol = 0, Seifert fibered); no cusp moduli exist. |
| C4 | q-rotational / trace constants: `μ₀/m_e = 2/(3(q−q⁻¹)) = 3.1889`, `ℏ_q = 0.0991`, `ℏ_q² = 0.0098`, `t = 0.1043`, `E₀ = (q−q⁻¹)/2 = 0.1045`; Markov parameter `z = 1/[2]_v = 0.4993` (`z(1) = 1/2` exact, `√z(1) = 1/√2` exact, `√z(q₀) = 0.70663`); fusion-frame `g = 1/√(1+[2]_v²) = 0.4467` (`= 1/√5` at q=1) | none equal 0.707 bare; `√z` hits it via an unmotivated square root (exact at q=1, −0.07% at q₀) | approximately, only through transforms | **No — relabel.** Same objection as C1; `g` (the corpus's own two-nucleon channel normalization, [`deuteron_tower_fusion_frame_probe.py`](../../computations/substrate/deuteron_tower_fusion_frame_probe.py)) is `1/√5`, **not** `1/√2`. |
| C5 | Bridge Stokes datum `A_ω = 4√2·e^{−3/8} = 3.888` | contains √2 | no (wrong magnitude; and its √2 **is** the singularity data) | **Circular by construction** — it is the period's own alien datum. |

## The C2 survivor, and why it still fails

C2 is a genuine finding: the corpus **does** supply an independent, derived,
exact `1/√2` — the Verlinde/bwS0 vacuum amplitude of the two-block n=2
bipartition, precisely the `dim/√(total dim)` object the task hypothesized
(`S₀₀ = 1/√2` of SU(2)₁-like two-object categories). It is not numerology: it is
q-independent, Lean-witnessed at the block level, and it *is* the Schmidt
amplitude of the maximally-entangled Hopf-pair reduced density matrix
(`W_λ = 1/2, 1/2`). Three things nonetheless kill the closure:

1. **The identification is a relabel, not a derivation.** No argument in the
   corpus (or constructed here) shows the Borel–Laplace expansion variable of
   the binding period *is* the bipartition amplitude. Worse, `S₀₀` is a
   fibre-level (root-of-unity / MTC) object while the coupling is an
   archimedean evaluation at real `q₀ > 1` — the corpus itself proves no
   compact MTC hosts the substrate anchor
   ([`s5-so3-keystone.md`](../coordination/s5-so3-keystone.md), 2026-06-22
   banner). Using `S₀₀` as an archimedean coupling is exactly the standing
   `bwS0_eq_hecke` archimedean-continuation open, not a new derivation.
2. **The two √2's share an origin — that explains the coincidence without a
   closure.** The Borel radius `ξ₀ = 1/√2` of the involution-number period
   comes from the 2-cycle term `x²/2` of the EGF `e^{x+x²/2}`; `S₀₀`'s `√2`
   comes from the 2 Wedderburn blocks of n=2. Both are "the 2 of the two-body
   system". A shared combinatorial origin is not an identification of the
   coupling with the amplitude.
3. **Decisively: even granting `x = 1/√2`, the number is wrong.** The median
   resummation at the derived coupling gives `m_e·ReP = 0.44 MeV` at ε = 0.02
   — **20% of B_D**, a 5× undershoot. Because the coupling sits exactly *on*
   the singularity, the value is ε-prescription-sensitive (0.38 → 0.92 MeV
   over ε = 0.1 → 0.002; the jump below ε ≈ 0.01 is the contour slipping past
   a Padé pole) — but even the most favorable prescription reaches only
   **41% of B_D**.

## Corrective finding — the #3736 premise was an extrapolation error

#3736's table stopped at x = 0.5 (19.0% of B_D) and extrapolated "reaches B_D
only as x → 1/√2". Scanning the **whole coupling axis** (ε = 0.02):

| x | m_e·ReP | % of B_D |
|---|---|---|
| 0.40 | 0.371 MeV | 16.7 |
| 0.50 | 0.445 MeV | 20.0 |
| **0.58–0.60** | **0.463 MeV** | **20.8 (global max)** |
| 0.7071 (= 1/√2) | 0.443 MeV | 19.9 |
| 0.85 | 0.385 MeV | 17.3 |
| 1.5 | 0.083 MeV | 3.7 |

The median sum **plateaus at ~21% of B_D near x ≈ 0.6 and then decreases — it
never reaches B_D at any coupling.** (Lateral sums `\|P₊\|` peak ≈ 50%.) So
Target 2's gate ("a closure needs x derived at ≈ 0.707") **dissolves**: there
is no coupling, derived or otherwise, at which this resummation closes the
deuteron. The route is not a one-parameter fit awaiting a derivation of the
parameter — it is short by ≥ 2.4× everywhere on the parameter axis. (Held to
scope-(a): "this construction, alone, at any coupling, on this machinery" —
the ε-prescription sensitivity on-singularity is why this is not a proved
scope-(b) exclusion.)

## Verdict (scope-(a), no fit)

**No independent derivation of x closes the route — and no x could.** The one
exact symbolic candidate (`S₀₀ = 1/√2` at n=2, a real corpus object worth
recording) is (i) connected to the coupling only by relabel across the standing
fibre→archimedean gap, and (ii) numerically insufficient even when granted
(20–41% of B_D). Combined with the whole-axis plateau, the Gevrey-1/2
entanglement-dual resummation for the deuteron is now closed negatively at a
stronger level than #3736: **distinct-mechanism, at every coupling.** The
working deuteron channel remains the q-rotational `μ₀·ℏ_q·J_q²` route
(B_D to −9%, 0 params). No wiring; no tier change.

## Honesty note

The S₀₀ match was the strongest pro-closure candidate available and was checked
first symbolically (exact) and then run on the existing trans-series machinery
at the derived value rather than being either dismissed or tuned. The negative
is reported with the ε-prescription caveat stated; the corrective finding about
#3736's extrapolation is a strengthening of that audit's own negative, not a
reversal.
