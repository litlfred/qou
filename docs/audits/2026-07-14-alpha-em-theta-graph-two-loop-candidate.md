# α_EM 2-loop: the θ-graph candidate −[3]_q/(8π)² — parameter-free, 1.3σ, with an exact resummation

**Date:** 2026-07-14 · **Branch:** `claude/canonical-derivation-c-k-n00n2h` ·
**Probe:** [`alpha_em_theta_graph_two_loop_probe.py`](../../computations/alpha_em_theta_graph_two_loop_probe.py)
(+ witness) · **Tier:** **named near-match candidate** (dictated object, exact
evaluation, inside 2σ; sign + per-loop measure not yet derived) · **Scope:**
(a); nothing wired; the window used only to falsify.

## The grammar (dictated by the established terms)

The α_EM ladder's working terms follow one rule — ladder term at loop order L
= (bare Penrose evaluation of the L-loop vacuum graph, fundamental matter) /
(π·dim H¹(M_Bring))^L:

| L | vacuum graph | bare evaluation | measure | term |
|---|---|---|---|---|
| 0 (zero-mode) | — | dim H¹/Area | — | 2/(3π) — **proved** (#1444) |
| 1 | circle (fermion loop) | `[2]_q` | 8π | `α[2]_q/(8π)` — **the working form-B H, reproduced exactly** |
| 2 | **θ-graph** (unique 1PI 2-loop topology: fermion cycle color 1, internal photon edge color 2 = the spin-1 channel of A⊗A) | `θ(1,1,2) = [3]_q` (evaluator validated: `θ(a,a,0)=[a+1]`, symmetry) | (8π)² | `−α²[3]_q/(8π)²` — **this candidate** |

Because the Schwinger factor's "derived" tier fell to the
[phase-3b exact check](2026-07-14-alpha-em-phase3-schwinger-coefficient-exact-check.md),
the target is the **total** O(α²) coefficient: `L₂_req = −4.30(±0.39)×10⁻³`
at the proton pin.

## Result

- `−[3]_q/(8π)² = −4.82×10⁻³` — ratio **1.12** of required, **inside the 2σ
  window** (≈1.33σ). The corpus-template measure alternates (8π·12π, 36π²)
  both miss.
- **Parameter-free ladder** `1/α = T + α[2]_q/(8π) − α²[3]_q/(8π)²`:
  residual **−0.200 ppb = 1.3σ** at the proton pin — closer to CODATA than
  form B (+0.313 ppb = 2.1σ). Muon anchor: +78.6 ppb — the known ~80 ppb
  anchor tension of the T-term, essentially unmoved by the new term (α_EM's
  independent proton preference stands).
- **Exact resummation (structural reading).** The implied tower
  `Σ_{L≥1} (−1)^{L+1} α^L [L+1]_q/(8π)^L` resums in closed form:

  `Σ_{L≥0} (−1)^L [L+1]_q x^L = 1/((1+qx)(1+x/q)) = 1/(1 + [2]_q·x + x²)`,
  `x = α/(8π)`

  — the reciprocal of the **Hecke characteristic polynomial** evaluated at
  −x: the whole loop tower is the two-eigenvalue-channel geometric dressing
  of the vertex insertion. The alternating sign is then a single global
  dressing-sign convention (the standard −α of a dressed propagator), not a
  per-order choice. Numerically identical to the L≤2 truncation
  (O(α³) ≈ 10⁻¹⁷).

## Honest tier assessment (numerology guards)

**For:** the object is dictated (unique 1PI topology; photon = the framework's
own spin-1 channel; coloring forced by admissibility); the evaluation is
classical and exact; the grammar reproduces the established L=1 term exactly;
the candidate was tested single-shot against a pre-stated window; the
resummation gives the sign structure one global convention instead of
per-order choices.

**Against (why this is NOT "derived"):** (i) the per-loop measure 1/(8π) is
itself only structurally identified (phase 4's rigorous derivation is open —
and now load-bearing for two terms); (ii) the global dressing sign is
convention-consistent but underived; (iii) 1.3σ is *consistent*, not
confirming — the candidate over-shoots the central value by 12%, and a
future σ_α improvement could falsify it cleanly (a genuinely good property);
(iv) exactly one candidate was tested, but the grammar itself was read off
two established terms — the L=1 consistency is necessary, not sufficient.

**Falsifiable prediction:** if the θ-term is right, improved α measurements
should move the central value toward `1/α = 137.035999057`, i.e. ~0.2 ppb
BELOW current CODATA (form B predicts ~0.3 ppb above).

## What would promote this to derived

1. The phase-4 rigorous shadow-world measure calculation (fixes 1/(8π) per
   loop — the same open item the 1-loop term needs).
2. A derivation of the dressed-propagator inversion (why 1/α picks up the
   `1/(1+[2]x+x²)` dressing) — this would also settle the sign.
3. The phase-3b exact gate: any realization must reproduce these terms from
   the singlet-channel algebra (the gate the old Schwinger story failed).

## Cross-references

- Tier calibration that reframed the target: [`2026-07-14-alpha-em-phase3-schwinger-coefficient-exact-check.md`](2026-07-14-alpha-em-phase3-schwinger-coefficient-exact-check.md)
- Headline docs to update on promotion (not before): [`2026-07-11-path-to-1ppq-alpha-em-opportunity.md`](2026-07-11-path-to-1ppq-alpha-em-opportunity.md)
- Phase 2 (−445% was Hecke-word candidates — the graph-evaluation class was untested); phases 3/4 caveats.
