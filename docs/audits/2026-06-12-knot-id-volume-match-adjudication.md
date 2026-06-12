# Knot-id volume fork — adjudicated: the names are right, the digits are stale

**Date:** 2026-06-12 · **Branch:** `claude/determined-gates-ekdwbt` (PR #2192)
**Probe:** [`probes/knot_id_volume_match_adjudication.py`](../../folio-assistant/computations/probes/knot_id_volume_match_adjudication.py)
(witness `knot-id-volume-match-adjudication.witness.json`, 7/7 assertions)
**Follows:** [`2026-06-06-thread2-deuteron-perknot-gating.md`](2026-06-06-thread2-deuteron-perknot-gating.md)
§Update 2026-06-12 (the live-SnapPy census verification that found the fork
is systematic).

## The question

`conj:canonical-knot-id-sdp` §"Historical evidence" prints volumes
{3.16396, 3.42721, 5.33349} that census-identify as **{6₁, 8₁, 6³₁}** —
subscript-neighbours of the knots the table names, **{6₂, 8₁₁, L6a4}** —
while production (`per-atom-hyperbolic-volume.witness.json`) and the SDP
partial closure use the named set. Which knot set does the historical
volume-matching evidence actually support?

## The reconstructed law

The conjecture's statement fixes the matching shape: binding is a Hecke
functional times the hadronic scale. The simplest zero-free-parameter
volume-level form consistent with the framework's canonical mass formula
(`m(K) = m_e·Vol(K)·ρ(K)/ℏ_q²`, cheat-sheet §9) is

$$
B_{\mathrm{AME}}(\mathfrak{H}) \;\approx\; \rho \cdot m_e \cdot \mathrm{Vol}(K),
$$

with $m_e$ = CAL-1, Vol from the live census (ManifoldHP), and $\rho$ the
conjecture table's own multiplicity column {1, 2, 2}. No fit: every input
is pinned.

*Caveat:* the original table's match formula was never written down; this
is a reconstruction. Its claim to being the original is that it reproduces
the table's claimed quality pattern ("<1 %", "<0.5 % after ρ=2", "<2 %
after correction") — but only for the **named** knots (²H lands at 1.09 %,
marginally above the "<1 %" wording).

## Results (witness, AME B from `ame-2020-binding-energies.witness.json`; ³He literature AME2020)

| nucleus | named knot | rel err (table ρ) | orphan manifold | rel err (table ρ) | orphan best ρ ≤ 4 |
|---|---|---|---|---|---|
| ²H | 6₂ (4.40083) | **+1.09 %** | 6₁ (3.16396) | −27.3 % | 27.3 % (ρ=1) |
| ³H | 8₁₁ (8.28632) | **−0.16 %** | 8₁ (3.42721) | −58.7 % | 17.4 % (ρ=4) |
| ³He | L6a4 (7.32772) | **−2.97 %** | 6³₁ (5.33349) | −29.4 % | 5.9 % (ρ=3) |

The steelman column lets the orphan set pick its best integer multiplicity
per nucleus; the deuteron still fails at **every** ρ ≤ 4, so no
multiplicity convention rescues the orphan set.

## Verdict

- **The knot NAMES {6₂, 8₁₁, L6a4} are right.** Recomputed properly, the
  volume-matching evidence stream agrees with production wiring and the
  SDP partial closure — the "two diverging evidence streams" reading in
  the thread-2 update is dissolved.
- **The printed volume DIGITS are stale** — survivors of an earlier draft
  (internally consistent with 𝔈₀ ≈ 4.1505 ≈ 8.122·m_e, recorded here only
  as provenance of the stale column, not endorsed). The 6₁ value also
  leaked into `MostowRigidity.lean:264`.
- **Production needs no change** (it was already on the named set's true
  census volumes).

## Recommended mechanical fixes (owner-confirm, thread-4 close-out)

1. `conj-canonical-knot-id-sdp.md` §Historical evidence: replace the three
   volume digits with the named knots' census values (4.40083, 8.28632,
   7.32772) and recompute or drop the "Vol/𝔈₀" column (its 𝔈₀ ≈ 4.1505
   normalisation belongs to the stale draft).
2. `lean/QOU/Encounter/MostowRigidity.lean:264`: the comment citing
   "Vol(6_1) ≈ 3.16396" — re-point at the adjudicated assignment (or
   rephrase as an explicit 6₁ example without deuteron context).
3. The 6₁-vs-6₂ *identity* question raised in the thread-2 doc is answered
   by this adjudication at the volume-matching level; the SDP-uniqueness
   claim of `conj:canonical-knot-id-sdp` itself remains open (unchanged).
