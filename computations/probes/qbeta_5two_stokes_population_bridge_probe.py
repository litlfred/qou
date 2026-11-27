#!/usr/bin/env python3
"""B1 (bean qou-ossd): the Stokes-population bridge attack — O_φ ↔ D_odd
at function level via sector amplitudes + the A2 S± data.

THE OPEN PROBLEM (named by A6.2). Two derived-grade odd numbers exist:
the saddle-side σ-pair projection O_φ = Im φ_σ1(−ln q₀) = +0.0109090 and
the Habiro-face function value D_odd = −0.007579403739 (median). The
bridge is the SECTOR POPULATION: which transseries sectors, with what
integer/Stokes weights, assemble the Habiro-face value on the real-q ray.

WHAT THIS PROBE ESTABLISHES:
  T1 — STRUCTURAL PRUNING (derived): at x₀ = −ln q₀ the σ-pair
       exponentials carry |e^{iV_{1,2}/x₀}| = e^{+13.2} ≈ 5.5e5 while the
       Habiro value is O(1): ANY nonzero integer population of the
       growing σ-pair sectors overshoots by ≥ 4 orders ⇒ n₁ = n₂ = 0 on
       this ray. (Consistent with A4.3's Stokes-free substrate ray and
       with #4213's GZ weight rule — the σ-pair ray carries integer
       Stokes constants; here the RAY POPULATION is forced zero.) The
       odd channel on the real-q ray must route through the REAL saddle
       σ₃ (pure phase, |e^{iV₃/x₀}| = 1) and/or the trivial sector —
       exactly the A2 structural finding (Ind^rot bar-even; the odd
       lives in S⁺ vs S⁻).
  T2 — the sector-amplitude table (exact, convention-stated): per-saddle
       Gaussian factors 1/√(V₀''), phases e^{iV_σ/x₀}, resummed φ_σ(x₀)
       (σ₁ from the A4.2 witness; σ₃ generated at the real root by the
       per-saddle engine), and the mirror (x → −x) combinations that a
       bar-odd projection selects.
  T3 — PRE-REGISTERED assembly family (parameter-free; entropy-guarded):
       ratio-normalized candidates D_odd / channel for the σ₃ phase
       channels (sin/cos/mirror-odd combination) × GZ weight powers
       x^{0, 1/2, 3/2} (#4213's weight family), tested against small
       (half-)integers and the A2 odd-matrix entries O_ij. Match gate
       1e-6 relative (band-limited by the muon/proton pin spread ~1e-6
       on S±); EVERY candidate within 10× of a hit is reported — no
       selection. ~180 candidates ⇒ coincidence budget ≲ 2e-4 at the
       gate; a hit is a lead, not an identification (stated).

Pin convention: MUON q₀ (matches the committed A2 S± matrices and the
A4.3 substrate constants); D_odd(muon) = median − 2.2e-9 per the g3
cross-check — folded into the gate band. auditOnly; no c_k wired; no
fit (integers/matrix entries only, bounds pre-registered, all
near-misses reported). Comparison to observed only; no ontological
claims.

Run: python3 -u computations/probes/qbeta_5two_stokes_population_bridge_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_stokes_pop.log
"""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from qbeta_5two_phi_series_engine_probe import (  # noqa: E402
    build_vertex_tower, phi_series_at, OMAX)

mp.mp.dps = 60

# q0 read BY NAME from `q_parameter` (bean qou-9ugp, 2026-09-03). It was the
# literal 1.1099785955573... -- the RETIRED self-certified muon pin A,
# superseded 2026-08-22 by the CODATA-2022 lepton-ratio derivation. There is
# no comparison leg here, so the 2026-08-30 owner ruling puts this producer
# on the PROTON default; the pin moves 11.54 ppb.
# The NAME Q0_MUON is kept so its call sites stay legible; it holds the proton
# pin, which is what this producer computes at.
Q0_MUON = Q_MP
# Canonical GGM saddle values — computed from the 5₂ cubic, not hardcoded.
# GGM convention (Im V₁ = Vol) mandated by the Stokes population argument
# (GGM eqs 82–83). The prior literal Im V₁ = 1.3790860299 is NOT the H-series
# extraction convention V_eff = V_GGM + π²/2 = 1.379194309661… — it sits
# 1.08e-4 away (that identification belongs to V_DOM = 1.37919426157, |Δ| =
# 4.8e-8, in the median-Borel probe). Im V₁'s provenance remains unexplained;
# either way it is not the V the published Stokes formulas use.
from fivetwo_saddle_values import saddle_values  # noqa: E402
V1, V2, V3 = saddle_values("ggm")
D_ODD = mp.mpf("-0.007579403739")          # g3 median (proton); muon −2.2e-9
O_PHI = mp.mpf("0.0109089607387")          # A6.2 σ-pair projection
GATE = mp.mpf("1e-6")                      # pin-band-limited match gate
T0 = time.monotonic()


def log(msg):
    print(f"  [{time.monotonic()-T0:6.0f}s] {msg}", flush=True)


def load_phi_sigma1():
    w = record_upstream(_HERE / "qbeta-5two-phi-series-engine.witness.json", _UPSTREAM_RECORDS)
    P = {0: mp.mpc(1)}
    for k, v in w["data"]["P_coefficients"].items():
        m = re.match(r"\(?\s*([-\d.e]+)\s*([+-])\s*([\d.e]+)j\)?", v)
        r_, s_, i_ = m.groups()
        P[int(k)] = mp.mpc(mp.mpf(r_), mp.mpf(i_) * (1 if s_ == "+" else -1))
    return P


def main() -> int:
    print("=" * 78)
    print(" B1 — Stokes-population bridge: sector amplitudes + assembly family")
    print("=" * 78)

    x0 = -mp.log(Q0_MUON)

    # ---- saddles + Gaussian data (V₀'' = 3x/(1−x) + 2 at the root) ----
    roots = mp.polyroots([1, -2, 3, -1], maxsteps=100, extraprec=80)
    x_real = [r for r in roots if abs(mp.im(r)) < mp.mpf("1e-40")][0]
    x_geo = [r for r in roots if mp.im(r) > 0][0]
    g2 = {s: 3 * z / (1 - z) + 2
          for s, z in (("s1", x_geo), ("s3", mp.mpf(mp.re(x_real))))}
    C = {s: 1 / mp.sqrt(-g2[s]) for s in g2}      # Gaussian ∝ 1/√(−V₀'')
    log(f"saddles: x₃ = {mp.nstr(mp.re(x_real), 10)}  x₁ = "
        f"{mp.nstr(x_geo, 10)}")
    log(f"V₀'': σ₃ {mp.nstr(g2['s3'], 8)}  σ₁ {mp.nstr(g2['s1'], 8)};  "
        f"|C₃/C₁| = {mp.nstr(abs(C['s3'] / C['s1']), 8)}")

    # ---- φ series: σ₁ from the witness; σ₃ generated at the real root ----
    P1 = load_phi_sigma1()
    log("generating φ_σ3 at the real root (per-saddle engine) ...")
    tw = build_vertex_tower(OMAX)
    P3 = phi_series_at(mp.mpc(mp.re(x_real)), tw)
    log("φ_σ3 done")

    def phi_eval(P, x):
        return sum(P[k] * x ** k for k in range(OMAX + 1))

    phi1_p = phi_eval(P1, x0)
    phi3_p = phi_eval(P3, x0)
    phi3_m = phi_eval(P3, -x0)
    reality3 = max(abs(mp.im(phi3_p)), abs(mp.im(phi3_m)))
    g_r3 = reality3 < mp.mpf("1e-40")
    log(f"φ_σ1(x₀) = {mp.nstr(phi1_p, 12)}")
    log(f"φ_σ3(±x₀) = {mp.nstr(mp.re(phi3_p), 12)}, "
        f"{mp.nstr(mp.re(phi3_m), 12)}  (Im ≤ {mp.nstr(reality3, 3)}: "
        f"{'PASS' if g_r3 else 'FAIL'})")

    # ---- T1: the σ-pair population is forced ZERO on the real-q ray ----
    E1 = mp.e ** (1j * V1 / x0)
    E3 = mp.e ** (1j * V3 / x0)
    amp1 = abs(E1) * abs(phi1_p) * abs(C["s1"])
    amp3 = abs(E3) * abs(mp.re(phi3_p)) * abs(C["s3"])
    overshoot = amp1 / max(abs(D_ODD), mp.mpf("1e-3"))
    g_t1 = overshoot > mp.mpf("1e4")
    log(f"[T1] |σ-pair amplitude| = {mp.nstr(amp1, 6)} "
        f"(|e^{{iV₁/x₀}}| = {mp.nstr(abs(E1), 6)}); overshoot vs O(1) "
        f"Habiro scale ×{mp.nstr(overshoot, 4)}")
    print(f"    ⇒ integer σ-pair population n₁ = n₂ = 0 FORCED on the "
          f"real-q ray: {'PASS' if g_t1 else 'FAIL'}")
    print(f"      (|σ₃ amplitude| = {mp.nstr(amp3, 6)} — O(1) oscillatory, "
          f"the only viable odd carrier)")

    # ---- T2/T3: channels × weights × candidate weights ----
    # mirror structure: E₃(−x₀) = conj(E₃(x₀)); φ₃(±x₀) real ⇒ the bar-odd
    # (x ↔ −x) projection of the σ₃ sector is sin(V₃/x₀)-weighted:
    s_phase = mp.sin(V3 / x0)
    c_phase = mp.cos(V3 / x0)
    ch = {
        "sin_mirror_odd": s_phase * (mp.re(phi3_p) + mp.re(phi3_m)) / 2,
        "sin_plus_only": s_phase * mp.re(phi3_p),
        "cos_mirror_even_diff": c_phase * (mp.re(phi3_p) - mp.re(phi3_m)) / 2,
    }
    weights_x = {"w0": mp.mpf(1), "w12": abs(x0) ** mp.mpf("0.5"),
                 "w32": abs(x0) ** mp.mpf("1.5")}    # GZ weight family (#4213)
    # candidate multipliers: small (half-)integers + the A2 odd-matrix entries
    sw = record_upstream(_HERE / "qbeta-5two-stokes-barodd-index.witness.json", _UPSTREAM_RECORDS)
    d_ = sw.get("witness", sw)["data"]
    Sp = [[mp.mpf(v) for v in row] for row in d_["S_plus_at_substrate_muon"]]
    Sm = [[mp.mpf(v) for v in row] for row in d_["S_minus_at_substrate_muon"]]
    Omat = [[(Sp[i][j] - Sm[i][j]) / 2 for j in range(3)] for i in range(3)]
    cand = {}
    for v in (1, 2, 3):
        for s in (1, -1):
            cand[f"{s*v}"] = mp.mpf(s * v)
            cand[f"{s*v}/2"] = mp.mpf(s * v) / 2
    for i in range(3):
        for j in range(3):
            if abs(Omat[i][j]) > mp.mpf("1e-12"):
                cand[f"O[{i}{j}]"] = Omat[i][j]

    log("[T3] pre-registered assembly scan (all near-misses reported):")
    hits, near = [], []
    n_cand = 0
    for chn, chv in ch.items():
        if abs(chv) < mp.mpf("1e-30"):
            continue
        for wn, wv in weights_x.items():
            base = chv * wv * C["s3"]
            R = D_ODD / base
            for cn, cv in cand.items():
                n_cand += 1
                relE = abs(R - cv) / abs(cv)
                rec = {"channel": chn, "weight": wn, "cand": cn,
                       "R": mp.nstr(R, 12), "rel": mp.nstr(relE, 3)}
                if relE < GATE:
                    hits.append(rec)
                    log(f"    HIT: {chn}·{wn} / {cn}: rel {mp.nstr(relE,3)}")
                elif relE < 10 * GATE:
                    near.append(rec)
    log(f"    scanned {n_cand} parameter-free candidates: "
        f"{len(hits)} hit(s), {len(near)} near-miss(es)")
    # honest ratio table for the record (channel values themselves)
    ratio_tab = {f"{chn}|{wn}": mp.nstr(D_ODD / (chv * wv * C['s3']), 12)
                 for chn, chv in ch.items() if abs(chv) > mp.mpf("1e-30")
                 for wn, wv in weights_x.items()}

    verdict_hit = bool(hits)
    wb = WitnessBuilder("qbeta-5two-stokes-population-bridge",
                        engine="mpmath", _script_path=__file__)
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "B1 (bean qou-ossd): the Stokes-population bridge attack. T1 "
        "(derived pruning): the σ-pair sectors carry e^{+13.2}-growing "
        "exponentials at x₀ = −ln q₀ vs the O(1) Habiro value — integer "
        "population n₁ = n₂ = 0 is FORCED on the real-q ray; the odd "
        "channel must route through the real saddle σ₃ (pure phase) — "
        "consistent with A4.3's Stokes-free ray, #4213's GZ weight rule, "
        "and A2's Ind^rot-bar-even finding. T2: the exact sector-"
        "amplitude table (Gaussian factors, phases, resummed φ_σ1/φ_σ3 "
        "with the per-saddle engine). T3: pre-registered parameter-free "
        "assembly family (σ₃ phase channels × GZ weight powers × small "
        "(half-)integers + A2 O-matrix entries), gate 1e-6 (pin-band), "
        "every near-miss reported — no selection. auditOnly; no fit; "
        "no c_k wired; a hit is a lead, not an identification.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("sigma3_series_real",
                     computed=float(reality3), expected=0.0, tolerance=1e-40,
                     source="the real-saddle φ_σ3 series is real at ±x₀")
    # Was `computed=float(overshoot), expected=float(overshoot)` with
    # `tolerance = overshoot/2 if g_t1 else 0.0` — and that tolerance dance is
    # why it could not fail either way: with `g_t1` true the tolerance is
    # enormous, and with it false the tolerance is 0 but both sides are still
    # the same expression (bean `qou-26f2`). The predicate the source states
    # is already computed on line 149 as `g_t1 = overshoot > 1e4`, and was
    # used only to pick that tolerance. Asserting it directly is the fix.
    wb.add_assertion("sigma_pair_population_forced_zero",
                     computed=bool(g_t1), expected=True,
                     source=f"σ-pair amplitude overshoots the Habiro scale "
                            f"by > 1e4 (measured {mp.nstr(overshoot, 6)}) "
                            f"⇒ n₁ = n₂ = 0 on the real-q ray "
                            f"(derived pruning)")
    # Was `computed=float(n_cand), expected=float(n_cand)` — the loop counter
    # against itself, so a scan that stopped early would have agreed with
    # itself and passed. "Ran to completion" means the triple loop visited the
    # whole pre-registered family, so the expected count is rebuilt here from
    # the three factors instead of read back off the loop.
    _n_channels = sum(1 for chv in ch.values() if abs(chv) >= mp.mpf("1e-30"))
    wb.add_assertion("assembly_scan_completed",
                     computed=n_cand,
                     expected=_n_channels * len(weights_x) * len(cand),
                     tolerance=0,
                     source=f"pre-registered parameter-free scan ran to "
                            f"completion: {_n_channels} live channel(s) × "
                            f"{len(weights_x)} weight(s) × {len(cand)} "
                            f"candidate(s); hits+near-misses recorded in full")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("substrate", {"x0": mp.nstr(x0, 15), "pin": "muon "
                              "(matches committed A2 S± + A4.3 constants)"})
    wb.add_data("sector_table", {
        "V": {"s1": mp.nstr(V1, 15), "s2": mp.nstr(V2, 15),
              "s3": mp.nstr(V3, 15)},
        "V0pp": {s: mp.nstr(g2[s], 15) for s in g2},
        "abs_E": {"s1": mp.nstr(abs(E1), 10), "s3": mp.nstr(abs(E3), 10)},
        "phi_at_x0": {"s1": mp.nstr(phi1_p, 20),
                      "s3_plus": mp.nstr(mp.re(phi3_p), 20),
                      "s3_minus": mp.nstr(mp.re(phi3_m), 20)},
        "amplitudes": {"sigma_pair": mp.nstr(amp1, 10),
                       "sigma3": mp.nstr(amp3, 10)}})
    wb.add_data("t1_pruning", {"overshoot": mp.nstr(overshoot, 8),
                               "conclusion": "n1 = n2 = 0 forced on the "
                                             "real-q ray"})
    wb.add_data("t3_scan", {"n_candidates": n_cand, "gate": "1e-6",
                            "hits": hits, "near_misses": near,
                            "ratio_table": ratio_tab})
    wb.add_data("verdict",
                ((f"BRIDGE LEAD FOUND: {len(hits)} parameter-free assembly "
                  f"hit(s) at 1e-6 — see t3_scan.hits; a lead requiring an "
                  f"independent-anchor test before any identification."
                  if verdict_hit else
                  "NO parameter-free assembly matches at 1e-6 (all "
                  "near-misses recorded). The derived content stands: the "
                  "σ-pair population is FORCED ZERO on the real-q ray (T1) "
                  "— O_φ and D_odd are NOT directly bridged by a "
                  "small-integer σ₃ assembly in the pre-registered family; "
                  "the bridge needs the trivial-sector/block-level pairing "
                  "(GK bilinear structure), named as the wall.")
                 + " auditOnly.") if ok else "A gate failed — inspect.")
    wb.save()
    print(f"\n  assertions passed: {ok}   ({time.monotonic()-T0:.0f}s)")
    print("  witness -> computations/probes/"
          "qbeta-5two-stokes-population-bridge.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
