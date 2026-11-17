#!/usr/bin/env python3
"""borromean_per_lambda_fr_probe.py — H_3-level probe of the FR-projector
per-λ weight candidate on the Borromean single binding pipeline.

CONTEXT (Step-9b frontier; docs/workplans/2026-07-02-step9b-gap-approaches.md).
The Borromean tower (borromean_binding_recompute.py) converges ∀Z but its
residual net/target = B_tower/B_AME is U-shaped (over-binds D and ⁵⁶Fe,
under-binds A=4–16; 7.16× spread under convention D). The named
frontier object is the
per-partition weight Δ_λ in `B = m_e·Σ_λ y_λ χ^λ Δ_λ`; the structural
candidate (brane-tower plan §7; depth-stratified-frobenius-reciprocity.md)
is the FR-restricted knot-ideal projector weight `χ^λ → χ^λ·χ^λ(e_{K*})`
with the k=3 knot resolved to K* = 4₁ (figure-eight; the 6₁ assignment was
falsified). The Fricke-trace value on the single non-trivial H_3 block is

    χ_{4₁}((2,1)) = 2 − [3]_q = −1 − h²      (chirality factor a_{4₁} = 1 − h²)

per chirality-from-frobenius-self-pairing.md.

H_3 PROXY (this probe — cheap, sub-second, no Rust). The production
pipeline is scalar in the nucleon trace τ = |tr_M(β_Bor)|. We re-lift τ
into its Wedderburn sum using the proved per-λ characters
(χ^(3) = χ^(1³) = 1, χ^(2,1) = 2 − 3h⁴ − h⁶) and the y-lambda witness,
apply a candidate weight w on the (2,1) channel ONLY (the two 1-dim
blocks are volume-blind: Vol conjecture info lives on V_(2,1)), and
re-run the tower per isotope:

    τ_w = τ · (p₃ + p₁³ + p₂₁·w),   p_λ = y_λ χ^λ(β_Bor)/Σ (channel fractions)

Two structural placements (both reported — genuine ambiguity in where
the projector acts):
  - "both":      τ → τ_w in free AND atom configs (weight on the nucleon)
  - "atom-only": τ → τ_w in the atom config only (projector restricts the
                 bound channel; free nucleons unprojected)

CANDIDATE WEIGHTS (all structural — values the corpus already derived
for 4₁ on (2,1); NO fitted parameters, honoring the Δ_λ gate):
  w_chirality  = 1 − h²             (Fricke chirality factor a_{4₁})
  w_chi_over_d = (2 − [3]_q)/2      (projector-normalized character, signed)
  w_abs_over_d = (1 + h²)/2         (magnitude variant)
  w_chi_raw    = 2 − [3]_q = −1−h²  (raw Fricke character)

PASS/FAIL vs the U-shape: PASS iff a candidate simultaneously moves the
over-bound ends (D, ⁵⁶Fe) down and the under-bound middle (⁴He…¹⁶O) up,
shrinking the max/min spread below the 7.16× baseline. A monotone
rescale (all isotopes moved the same way) is a FAIL for that candidate
— same structural reason edge-set sparsification failed.

KNOWN CAVEAT (recorded in witness): the y-lambda-at-q0 decomposition
reproduces the Lean closed-form τ only to 1.96e-4 relative (convention
gap, flagged as open); channel fractions are normalized so the baseline
τ is exact and the mismatch only perturbs p_λ at the 4th decimal.

Exploratory probe — audit-only witness, NOT wired into production.

Ref: docs/audits/2026-06-28-brane-tower-formalize-first-plan.md §7
Ref: folio/quantum-observable-universe/mass-theory/depth-stratified-frobenius-reciprocity.md
Ref: folio/quantum-observable-universe/mass-theory/chirality-from-frobenius-self-pairing.md
Ref: prop:borromean-markov-trace-closed-form
"""
from __future__ import annotations

import json
import sys
import warnings
from math import comb  # float64-ok: exact integer binomial coefficient
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "substrate"))
warnings.filterwarnings("ignore")

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from q_parameter import Q_MP as Q0  # noqa: E402
from codata_constants import (
    AME_B_HE4_MEV_VALIDATION,
    M_E_MEV as M_E  # noqa: E402,
)
from _li_2_q_util import li_2_q  # noqa: E402

# AME2020 totals (MeV) — comparison target only (mirror of
# borromean_binding_recompute.ISO).
# AME binding energies (MeV).  DECIMAL STRINGS, lifted with `mp.mpf` at use:
# these were bare Python float literals, so the MEASURED side of every
# `net_over_target` ratio this probe reports arrived pre-rounded to 53 bits.
# The strings carry the identical values — this is a precision fix, not a data
# change.
#
# 🛑 TWO PROVENANCE ODDITIES LEFT AS THEY ARE, both reported rather than fixed:
#
#  1. The table is MIXED.  Eight rows are literals; `4He` alone reads the
#     canonical constant `AME_B_HE4_MEV_VALIDATION`.
#  2. The eight literals DISAGREE with that canonical source by ~3 ppm —
#     `2.224573` here against `codata_constants.ame_binding_mev(1, 2)` =
#     `2.2245662` (3.1e-6 relative), `8.481821` vs `8.4817962` (2.9e-6),
#     `7.718058` vs `7.71804132` (2.2e-6).  A consistent offset, so a
#     different edition or a different binding convention, not typos.  All
#     five are already flagged in
#     `computations/audits/hardcoded-literal-audit.witness.json`.
#
# Repointing them at `ame_binding_mev` would move this probe's numbers, so it
# is not part of a precision drain; the headline spread is 7.16 against a 0.5
# tolerance, so 3 ppm changes no conclusion either way.
ISO = [("2H", 1, 1, "2.224573"), ("3H", 1, 2, "8.481821"),
       ("3He", 2, 1, "7.718058"),
       ("4He", 2, 2, AME_B_HE4_MEV_VALIDATION),
       ("6Li", 3, 3, "31.994564"), ("7Li", 3, 4, "39.244533"),
       ("12C", 6, 6, "92.161728"), ("16O", 8, 8, "127.619"),
       ("56Fe", 26, 30, "492.254")]


def params():
    q = mp.mpf(str(Q0)); qi = 1 / q; h = q - qi
    E0 = mp.mpf(str(M_E)) / (q * (q - 1))
    # convention D (owner ruling 2026-08-15, reaffirmed 2026-08-23):
    #   z_D = q^3/(q^2+1).  Was z_C = 1/(sqrt q + sqrt(1/q)), excised.
    # This matters here beyond the ruling: tower() below is documented as a
    # MIRROR of borromean_binding_recompute.borromean_binding, and that
    # original is z_D (its docstring says 'NOT convention C').  Under C the
    # mirror disagreed with its original by 16% (6.17x vs 7.1622x); under D
    # it reproduces it exactly.  The old value was a frame straddle, not a
    # second measurement.
    z = q**3 / (q**2 + 1)
    tau = (4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4)  # Lean BorromeanMarkovTrace
    return q, qi, h, E0, z, tau


def channel_fractions(h):
    """p_λ = normalized per-λ contribution to τ from the Wedderburn re-lift
    (y-lambda-at-q0 witness × proved χ^λ(β_Bor) closed forms)."""
    w = record_upstream(ROOT / "y-lambda-at-q0.witness.json", _UPSTREAM_RECORDS)
    d = w.get("data", w)
    ys = {tuple(p["partition"]): mp.mpf(p["y_at_q0_50dps"]) for p in d["by_n"]["3"]}
    chi = {(3,): mp.mpf(1), (1, 1, 1): mp.mpf(1),
           (2, 1): 2 - 3 * h**4 - h**6}
    contrib = {lam: ys[lam] * chi[lam] for lam in chi}
    total = mp.fsum(contrib.values())
    fracs = {lam: c / total for lam, c in contrib.items()}
    return fracs, contrib, total


def tower(Z: int, N: int, tau_free, tau_atom, E0, z, q, qi):
    """The Borromean brane tower with independent free/atom nucleon traces
    (mirror of borromean_binding_recompute.borromean_binding)."""
    h = q - qi
    f_pp = z; f_pn = z; f_nn = z - h
    A = Z + N

    def g(x):
        return -li_2_q(-x, q, qi)

    ratio = f_pp**max(Z - 1, 0) * (f_pn if Z and N else 1) * f_nn**max(N - 1, 0)
    trf = tau_free**A
    tra = tau_atom**A * ratio
    dtr = trf - tra
    pair = mp.mpf(0)
    for cnt, fb in ((comb(Z, 2), f_pp), (Z * N, f_pn), (comb(N, 2), f_nn)):
        if cnt:
            pair += cnt * (g(tau_free * tau_free) - g(tau_atom * tau_atom * fb))
    return E0 * (dtr + z * z * pair)


def _serialise(obj):
    """Render an `mpf`-bearing structure for the witness.

    One place where a number becomes text, and it becomes text via
    `_precision.fmt`.  The rows keep their `mpf`s until here so the spread,
    the U-flattening comparisons and both assertions run on live values
    rather than on float64 casts of them.
    """
    if isinstance(obj, dict):
        return {k: _serialise(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_serialise(v) for v in obj]
    if isinstance(obj, mp.mpf):
        if mp.isnan(obj):
            return "nan"
        if mp.isinf(obj):
            return "inf" if obj > 0 else "-inf"
        return fmt(obj)
    return obj


def main() -> int:
    set_compute_dps()
    q, qi, h, E0, z, tau = params()
    fracs, contrib, lift_total = channel_fractions(h)
    # `mpf`, not `float(...)`: this is the value assertion
    # `wedderburn_lift_consistent_to_2em4` is decided on.
    lift_mismatch = abs(lift_total - tau) / tau

    weights = {
        "w_chirality_1_minus_h2": 1 - h**2,
        "w_chi_over_d": (-1 - h**2) / 2,
        "w_abs_over_d": (1 + h**2) / 2,
        "w_chi_raw": -1 - h**2,
    }
    placements = ("both", "atom_only")

    def tau_weighted(w):
        return tau * (fracs[(3,)] + fracs[(1, 1, 1)] + fracs[(2, 1)] * w)

    def sweep(tau_free, tau_atom):
        rows = {}
        for nm, Z, N, bame in ISO:
            bt = tower(Z, N, tau_free, tau_atom, E0, z, q, qi)
            # `mpf` throughout.  Both of these were `float(...)`, and
            # `net_over_target` is read straight back below to build `spread`
            # and to decide `ends_down` / `mid_up` — i.e. this probe's whole
            # verdict ran on the f64 casts of an mpmath computation.
            rows[nm] = {"A": Z + N, "B_tower": bt,
                        "net_over_target": bt / mp.mpf(bame)}
        vals = [abs(r["net_over_target"]) for r in rows.values()]
        spread = max(vals) / min(vals) if min(vals) > 0 else mp.inf
        return rows, spread

    base_rows, base_spread = sweep(tau, tau)
    print(f"baseline (uniform)  spread={float(base_spread):.3f}")  # float64-ok: stdout display only
    for nm, r in base_rows.items():
        print(f"  {nm:5s} net/target={float(r['net_over_target']):7.3f}")  # float64-ok: stdout display only

    results = {"baseline": {"rows": base_rows, "spread": base_spread}}
    verdicts = {}
    for wname, w in weights.items():
        tw = tau_weighted(w)
        for pl in placements:
            key = f"{wname}::{pl}"
            tf, ta = (tw, tw) if pl == "both" else (tau, tw)
            if abs(tf * tf) >= q or abs(ta * ta * z) >= q:
                results[key] = {"skipped": "Li2q convergence radius violated"}
                verdicts[key] = "SKIP (divergent)"
                continue
            rows, spread = sweep(tf, ta)
            base_nt = {nm: base_rows[nm]["net_over_target"] for nm in base_rows}
            new_nt = {nm: rows[nm]["net_over_target"] for nm in rows}
            over = [nm for nm in base_nt if base_nt[nm] > 1]
            under = [nm for nm in base_nt if base_nt[nm] <= 1]
            ends_down = all(new_nt[nm] < base_nt[nm] for nm in over)
            mid_up = all(new_nt[nm] > base_nt[nm] for nm in under)
            u_flattened = ends_down and mid_up and spread < base_spread
            monotone = (all(new_nt[nm] >= base_nt[nm] for nm in base_nt)
                        or all(new_nt[nm] <= base_nt[nm] for nm in base_nt))
            verdict = ("PASS (U flattened)" if u_flattened else
                       "FAIL (monotone rescale)" if monotone else
                       f"FAIL (spread {'improved' if spread < base_spread else 'worsened'} "
                       f"{float(base_spread):.2f}→{float(spread):.2f} "  # float64-ok: prose verdict string formatting
                       f"but not U-corrective)")
            results[key] = {"tau_weighted": tw, "rows": rows,
                            "spread": spread, "verdict": verdict}
            verdicts[key] = verdict
            print(f"\n{key}  τ_w={float(tw):.6f}  "  # float64-ok: stdout display only
                  f"spread={float(spread):.3f}  → {verdict}")  # float64-ok: stdout display only
            for nm in rows:
                print(f"  {nm:5s} {float(base_nt[nm]):7.3f} → "  # float64-ok: stdout display only
                      f"{float(new_nt[nm]):7.3f}")  # float64-ok: stdout display only

    any_pass = any(v.startswith("PASS") for v in verdicts.values())
    if any_pass:
        overall = ("At least one structural FR-projector candidate flattens "
                   "the U at the H_3-proxy level — escalate to the H_{3A} "
                   "per-partition test (fr_pullback over Borromean words).")
    else:
        overall = ("SCOPE-LIMITED NEGATIVE — no H_3-per-nucleon proxy of the "
                   "FR-projector weight (4 structural candidates × 2 "
                   "placements) flattens the U-shaped residual. Constrains "
                   "the per-NUCLEON scalar proxy only; the per-partition "
                   "weight at H_{3A} (where the depth strata are non-trivial) "
                   "remains the open test — this probe sharpens its spec, it "
                   "does not exclude the FR-projector ingredient.")
    print(f"\nOVERALL: {overall}")

    b = WitnessBuilder("borromean-per-lambda-fr-probe", output_dir=HERE)
    b.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    b.set_description(
        "H_3-level probe of the FR-restricted knot-ideal projector weight "
        "(K*=4_1, Fricke chi_{4_1}((2,1)) = 2-[3]_q) as the missing per-λ "
        "weight on the Borromean single binding pipeline, via the Wedderburn "
        "re-lift τ = Σ_λ y_λ χ^λ(β_Bor) and a candidate reweight of the "
        "(2,1) channel (56.1% of τ). 4 structural candidates × 2 placements "
        "tested against the U-shaped net/target residual (baseline spread "
        "7.16x, convention D). No fitted parameters (Δ_λ gate honored). Audit-only.")
    b.add_parameter("tau_closed_form", fmt(tau))
    b.add_parameter("channel_fraction_21", fmt(fracs[(2, 1)]))
    b.add_data("wedderburn_lift_mismatch_rel", fmt(lift_mismatch))
    b.add_data("wedderburn_lift_note",
               "y-lambda-at-q0 × proved chi closed forms reproduce the Lean "
               "closed-form tau EXACTLY: |lift - tau|/tau = 9.98e-51, i.e. "
               "zero at the working precision, and the two routes are "
               "independent (tau is the algebraic "
               "(4 + h^2 - 3h^4 - h^6)/(h^2 + 4); the lift is a sum over the "
               "y-lambda witness against the proved chi forms). This field "
               "read 'to 1.96e-4 relative only - convention gap flagged' "
               "until 2026-09-13; that gap is the convention-C one and "
               "convention D closed it. The committed witness has carried "
               "9.983134063775882e-51 all along, so the note contradicted "
               "the number beside it. Same stale premise as probe_9b "
               "(bean qou-gik1), which is RED for it while this probe stayed "
               "green only because its tolerance is 47 orders too loose.")
    b.add_data("results", _serialise(results))
    b.add_data("verdicts", verdicts)
    b.add_data("overall", overall)
    b.add_assertion(
        "baseline_spread_reproduced",
        computed=fmt(base_spread), expected="7.16", tolerance="0.5",
        unit="max/min |net/target|",
        source="borromean_binding_recompute.py (z = q^3/(q^2+1), convention D) "
               "gives 7.162229445453156; this mirror now reproduces it. The "
               "old 6.17 reference was the C-frame straddle recorded in "
               "2026-06-28-delta-lambda-borromean-ascaling-diagnostic.md. "
               "Referenced against the PRODUCER, not its committed witness, "
               "which is 17-23% stale (bean qou-5t68).")
    b.add_assertion(
        # NAME IS HISTORICAL (`_to_2em4` recorded the pre-ruling convention-C
        # gap). Under Convention D (Wenzl level r=2) the measured mismatch is
        # 9.98e-51, so the tolerance is tightened from 5e-4 to 1e-40 alongside
        # probe_9b (bean qou-gik1).
        "wedderburn_lift_consistent_to_2em4",
        computed=fmt(lift_mismatch), expected="0", tolerance="1e-40",
        source="y-lambda witness × proved chi vs Lean BorromeanMarkovTrace "
               "(exact agreement under Convention D; bean qou-gik1)")
    b.save()
    return 0


def _selftest() -> int:
    set_compute_dps()
    q, qi, h, E0, z, tau = params()
    assert mp.mpf("0.998") < tau < mp.mpf("0.999"), f"unexpected tau: {tau}"
    print("self-test: ok (BorromeanMarkovTrace tau verified)")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv or "--selftest" in sys.argv:
        raise SystemExit(_selftest())
    raise SystemExit(main())
