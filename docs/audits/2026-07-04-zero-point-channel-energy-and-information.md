# Zero-point channel energy and "energy = information" — identification, invariant, probe

**Date:** 2026-07-04 (session of 2026-07-03)
**Branch:** `claude/parabolic-cylinder-channels-fh08ia` (restarted from main post-#3258)
**Status:** exploratory audit + one Lean invariant (proved) + one parameter-free probe
(negative as sole mechanism, scope-(a), with one tiered near-match). No production
wiring.

## Owner questions

1. The $D_\nu$ (D_ν) interpolation mechanism (PR #3258) *has an energy* — a natural
   quadratic energy metric. Is it missing from mass/binding, and does it need to
   enter $m = \mathrm{Vol}\cdot\rho$ (m = Vol·ρ)?
2. Is the kinetic oscillation energy the *amount of information* in the knot/braid
   channels — "no oscillation = no information = no energy" — and is there a way to
   make that precise?

## 1. The quadratic energy metric already has two corpus names

- **Representation side:** the q-Casimir $C_q$, eigenvalue $[j]_q[j+1]_q$
  ([j]_q[j+1]_q) — the q-deformation of the quadratic $j(j+1)$
  ([`q-casimir`](../../content/quantum-observable-universe/braids-and-knots/q-casimir-unique-proof.md));
  the geodesic-vortex ladder barrier is its increment.
- **Channel-measure side:** the Wedderburn/Plancherel weight
  $\tilde w_\lambda = \dim_q^2(\lambda)/[n]_q!$ (w̃_λ = dim_q²(λ)/[n]_q!) —
  literally quadratic in the channel dimension
  ([`q-plancherel-asymptotic-skeleton`](../../content/quantum-observable-universe/observations/q-plancherel-asymptotic-skeleton.md)).

The $D_\nu$ lens adds the *zero-point* reading: $E_\nu = \hbar\omega(\nu+\tfrac12)$,
and at non-integer $\nu$ (channels mixing mid-interaction) the state carries energy
between the integer channel values — a Casimir-shift/zero-point quantity that
integer-channel bookkeeping does not obviously count.

## 2. The confinement invariant (formalize-first; Lean, proved)

**Answer to "does it enter $m = \mathrm{Vol}\cdot\rho$": no.** Two independent
reasons:

1. $\mathrm{Vol}\cdot\rho$ is not the canonical absolute-mass route (owner ruling
   2026-06-24, [`canonical-mass-formula-guardrail`](../canonical-mass-formula-guardrail.md));
   absolute mass goes through the muon-anchored facade and already matches CODATA.
2. That match itself *confines* any proposed new energy term:
   [`QOU/Mass/AdditiveCorrectionConfinement.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/AdditiveCorrectionConfinement.lean)
   proves (generic linear ordered field, sorry-free) that a term added where
   prediction already matches observation within $\varepsilon$ is bounded by
   $2\varepsilon$ (`additive_correction_confined`), and vanishes if the match is
   exact (`additive_correction_zero_of_exact`).

**Consequence:** the missing quadratic energy, if physical, lives only in the
**binding / convolution-defect sector** — exactly where the ~38% MAE lives.

## 3. "Energy = information" — three precision tiers

The corpus already carries the pieces; the slogan "no oscillation = no information =
no energy" becomes precise at three levels:

1. **Per-crossing (already in the corpus).** Information per elementary crossing is
   the operational entropy $\eta_q = (2q-1)/q^3$ q-bits
   ([`operational-entropy`](../../content/quantum-observable-universe/information-theory/operational-entropy.md)),
   and channel capacity is $\ell\,\eta_q$ for a length-$\ell$ braid
   ([`fibre-channel-capacity`](../../content/quantum-observable-universe/information-theory/fibre-channel-capacity.md)).
   The notation register separately carries a crossing *energy*
   $E_{\mathfrak{H}}$. The precise form of the owner's claim at this tier is a
   **Landauer-type proportionality** $E_{\text{crossing}} \propto k T_q\,\eta_q$
   with $k T_q$ a substrate temperature scale — a *candidate identification*, not
   yet a corpus result.
2. **Thermodynamic (structural).** The binding formula already *is* a free-energy
   difference: $B = E_0 \ln(\mathrm{tr}_M^{\text{free}}/\mathrm{tr}_M^{\text{atom}})$
   reads as $\Delta F = kT \ln(Z_1/Z_2)$ with $E_0$ in the $kT$ slot and the Markov
   trace as partition function. Markov traces on Hecke towers are Gibbs/KMS-type
   states (the Jones/Ocneanu temperature-state reading, inverse temperature
   $\sim \ln q$), so energy and information (entropy) are Legendre-dual by
   construction: the corpus's binding is *already* thermodynamic, with
   $T_q \sim E_0/k$ and information = entropy of the normalized channel measure.
   "No oscillation" = trace concentrated on one channel = zero entropy = zero free
   energy: the slogan holds verbatim at this tier.
3. **Asymptotic (volume conjecture).** $\mathrm{Vol}(K) = \lim_N (2\pi/N)\ln|J_N(K)|$
   — the hyperbolic volume *is* the asymptotic information production rate of the
   knot's colored-Jones channel tower. So $m \sim \mathrm{Vol}\cdot\rho$ already
   reads "mass ∝ channel information rate × density", and $\mathrm{Vol} = 0$ knots
   (unknot; Hopf link — the corpus's volume-less vdW correlation) carry no such
   rate: "no oscillation = no information = no (binding-scale) energy" is exactly
   the $\mathrm{Vol}=0$ statement.

## 4. The zero-point probe — negative as sole mechanism (scope-(a)), one near-match

Probe: [`zero_point_channel_energy_probe.py`](../../computations/zero_point_channel_energy_probe.py)
(witness `zero-point-channel-energy-probe.witness.json`; 70 dps compute /
50-digit serialized values, matching the witness `precisionMetadata`;
parameter-free — scale $E_0$ (E₀), factor $\tfrac12$, canonical channel
measure). Two candidates for the
free-vs-bound zero-point shift $\Delta E(A) = E(3A) - A\,E(3)$ under the normalized
quadratic measure $\hat w_\lambda \propto \dim_q^2$:

| iso | $\Delta E_{\text{info}}$ | $\Delta E_{\text{cas}}$ | $r_{\text{raw}} = B_{\mathrm{AME}}-B(q_0)$ | $r_{\text{even}}$ |
|---|---:|---:|---:|---:|
| ²H | 3.11 | 1.68 | −1.67 | −0.78 |
| ³H | 8.26 | 3.46 | −0.59 | 2.17 |
| ³He | 8.26 | 3.46 | 0.92 | 1.81 |
| ⁴He | **15.07** | 4.49 | **16.32** | 19.08 |

**Findings:**

1. **Refuted as the sole uniform mechanism (scope-(a)).** The residual's *sign flips*
   across isotopes (−1.67 → +16.32 MeV), so no single-sign additive zero-point term
   at fixed per-strand scaling can track all four. Both candidates fail the
   factor-2 tracking test. This constrains the *combination* (an additive
   channel-energy term alone, uniformly scaled), not the ingredient.
2. **Tiered near-match (not wired, not fitted):** for ⁴He — the isotope with the
   dominant residual — the *information* candidate lands within 8% of the raw
   residual ($15.07$ vs $16.32$ MeV). Under the $c_k$-style tiered-reporting rule
   this is recorded as a **near-match observation**: suggestive that a
   channel-information energy at scale $E_0/2$ is the right *order and object* for
   the large-$A$ residual, while the light-isotope sign structure says the true
   term is not uniformly additive (e.g. enters with channel-parity or
   defect-weighted signs).
3. The probe's channel model (bound = $3A$ strands with quadratic measure over all
   $\lambda \vdash 3A$) is the coarsest possible; the production defect
   $\mathrm{tr}_M((\Pi_{\text{free}}-1)\circ\mathcal{M})$ weights channels by the
   actual braid, which the probe deliberately ignores to stay parameter-free.

## 5. Follow-ups (owner-approved; all three landed)

1. **Landauer tier-1 — NEGATIVE, decisive (scope-(a)).**
   [`landauer_crossing_energy_probe.py`](../../computations/landauer_crossing_energy_probe.py)
   (witness `landauer-crossing-energy-probe.witness.json`): the corpus defines
   crossing energy $E_{\mathfrak{H}} = \mathfrak{m}_{\mathfrak{H}} c_q^2$
   (notation table 3) and crossing information $\ell\,\eta_q$ q-bits. The implied
   per-q-bit energy for p/n (Borromean, $\ell = 6$) is
   $kT_{\text{eff}} \approx 17.9$ GeV/q-bit — matching **no** canonical substrate
   scale within 5% (nearest ratio ≈ 42×, $E_0 c_q^2$). The simple per-crossing
   Landauer identification is refuted at tier 1; the thermodynamic tier-2 reading
   is where the energy–information duality actually lives.
2. **Defect-weighted zero-point — NEGATIVE overall (scope-(a)); ⁴He near-match
   SHARPENED.**
   [`defect_weighted_zero_point_probe.py`](../../computations/defect_weighted_zero_point_probe.py)
   (witness `defect-weighted-zero-point-probe.witness.json`; production
   transfer-path channel weights $w_\lambda = y_\lambda(\chi^\lambda_{\text{free}}
   - \chi^\lambda_{\text{atom}})$, fit-free): light isotopes still sign-flip
   (ratios −2.7, −15.1, +9.7), so the channel-information energy is *not* the
   uniform missing term. But the ⁴He ratio moves 0.92 → **0.904**: two independent
   measures (bare Plancherel §4; physical defect weights here) now land the
   channel-information energy within ~10% of the dominant ⁴He residual. Recorded
   tiered (near-match ×2, unwired); the surviving question is why the candidate
   is order-correct exactly where the residual is large and wrong-signed where it
   is small.
3. **KMS/Gibbs content block — landed.**
   [`rem:markov-trace-gibbs-free-energy`](../../content/quantum-observable-universe/mass-endomorphism/markov-trace-gibbs-free-energy.md)
   (`interprets prop:categorical-mass-markov`, cites `jones1987`): tier 2 stated
   in the paper — binding as free-energy difference, $\mathrm{tr}_M$ as
   temperature state, zero-entropy ⇔ zero-information ⇔ zero binding-scale
   energy, and the $\eta_q$ capacity bound as the linear-in-crossings information
   ceiling.

## 6. A-trend extension (owner-approved): the ⁴He near-match was a crossing, not an onset

Probe: [`defect_info_a_trend_probe.py`](../../computations/defect_info_a_trend_probe.py)
(witness `defect-info-a-trend-probe.witness.json`; extends the defect-weighted
channel-information candidate to ⁶Li/⁷Li with $B(q_0)$ computed live from the
production transfer path and $B_{\mathrm{AME}}$ from the vendored AME2020
witness; fit-free).

| iso | A | $B(q_0)$ | $B_{\mathrm{AME}}$ | $r_{\text{raw}}$ | $E_{\text{defect-info}}$ | ratio |
|---|---:|---:|---:|---:|---:|---:|
| ²H | 2 | 3.89 | 2.22 | −1.67 | 4.54 | −2.73 |
| ³H | 3 | 9.07 | 8.48 | −0.59 | 8.82 | −15.06 |
| ³He | 3 | 6.80 | 7.72 | 0.92 | 8.91 | 9.67 |
| ⁴He | 4 | 11.97 | 28.30 | 16.32 | 14.75 | **0.904** |
| ⁶Li | 6 | 20.06 | 31.99 | 11.93 | 31.10 | 2.61 |
| ⁷Li | 7 | 25.24 | 39.25 | 14.01 | 41.66 | 2.97 |

**Verdict — CLOSED, scope-(a).** The deviation from 1 *grows* past ⁴He
(0.10 → 1.61 → 1.97): the candidate's roughly extensive growth crosses the
non-monotone residual curve at $A = 4$, which is all the twice-measured 0.904
ever was. The channel-information zero-point candidate is now closed as a
binding mechanism in **all tested forms** (bare Plancherel §4, defect-weighted
§5.2, A-trend here) — the surviving content of the energy=information thread
is the tier-2 thermodynamic identity (`rem:markov-trace-gibbs-free-energy`),
not a correction term.

**Cross-reference (jet-filtration extensivity, landed upstream 2026-07-03).**
[`prop:jet-filtration-binding-extensive`](../../content/quantum-observable-universe/mass-endomorphism/jet-filtration-binding-extensive.md)
proves the *body-order* series $B(A) = \sum_n \mathfrak{m}_e\,a_D^{(n)} w_n$
(built from the same binding period $a_D^{(n)}$ characterized in the
2026-07-03 audit §10–§11) is monotone extensive. The two results triangulate:
extensive growth is structurally right for binding (their side), but the
*channel-information* extensive candidate overshoots the residual by ~3× at
Li (this probe) — so the correct extensive term must grow more slowly than
the defect-measure log-capacity, pointing at the $w_n$ weights (their open
end) rather than a new energy species (this thread's closed end).
