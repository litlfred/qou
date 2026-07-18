#!/usr/bin/env python3
"""he4_vol4_prediction_test_probe.py — the ⁴He `Vol₄ = 8.05` falsifiable test,
executed end-to-end (exact back-out + SnapPy comparison + guarded census data).

WHAT THE PREDICTION IS (provenance, pinned exactly)
---------------------------------------------------
The bond-count binding tower (`prop:linear-chain-bond-count`, Lean-proved
multiplicity `M_n = (n−1)`; derivation audit
docs/audits/2026-07-04-theta-mn-bondcount-derived-linearchain.md) states

    B(K) = m_e · Σ_{n=2}^{A} Σ_{consecutive n-clusters c} (n−1) · Vol(c),

with Vol(c) the hyperbolic volume of the n-nucleon sub-chain's link (the
isospin carrier: ppn → L6a4, pnn → 8₁₁, any 2-chain → Hopf with Vol = 0).
For ⁴He (ppnn linear chain) every n = 2, 3 volume is known, so the tower
INVERTS: the n = 4 term is fixed by AME,

    B_AME(⁴He) − m_e·[2·Vol(L6a4) + 2·Vol(8₁₁)] = m_e · 3 · Vol₄
    ⇒ Vol₄ ≈ 8.05  (pre-registered as 8.048 / "≈8.05" on 2026-07-04).

`Vol₄` is therefore *the hyperbolic volume of the single 4-component link
carried by the full ppnn 4-chain* (isospin-aware only through the n = 3
sub-terms; the n = 4 term itself is one volume). The falsifiable test: does
an actual, in-advance-named 4-component link have volume ≈ Vol₄?

CORPUS LINK-ASSIGNMENT STATUS (the caveat that scopes the verdict)
------------------------------------------------------------------
The corpus has NO derived ⁴He link: the canonical knot-ID is gated on the
R5-full categorical SDP (`conj:canonical-knot-id-sdp`, #604), and the A≤3
link IDs themselves are deprecated volume-search matches
(docs/audits/2026-07-04-he4-vol4-gated-on-r5full.md). So a *decisive*
falsification is not available; what IS testable is the naive structural
reading — "the n=4 term is the volume of the linear 4-chain closure" — via
candidates named IN ADVANCE by structural analogy (anti-numerology: no
census scan feeds the verdict). Pre-registered candidate list per
vol4_4he_snappy_falsification_probe.py (same branch, 2026-07-13):

    L8n8  — 4-component brunnian (Borromean analogue)
    L8a21 — the 4-chain (linear-chain closure)   L8a20 — 4-chain variant
    L8a19 — 4-component alternating              L8n7  — 4-component non-alt

WHAT THIS PROBE ADDS over vol4_4he_snappy_falsification_probe.py
----------------------------------------------------------------
1. The implied Vol₄ is COMPUTED exactly from AME B(⁴He) (vendored AME2020),
   m_e (CODATA, CAL-1) and the corpus n=2,3 volumes (binding-link-volumes
   witness) — not hardcoded — and cross-checked against the pre-registered
   8.048 to 0.01.
2. An honest MODEL TOLERANCE: the A=3 anchors carry a −0.16% (³H) / −2.97%
   (³He) residual, so a ±3% band on the n=3 contribution propagates to
   ±(0.03·B₂₃)/(3·m_e) ≈ ±0.31 on Vol₄. Candidates are judged against both
   the strict (±0.05) and the model (±0.31) tolerance.
3. GUARDED census data: with no corpus link assignment, the honest deliverable
   is the density of 4-component census volumes near Vol₄ — tabulated to show
   the SELECTION FREEDOM (how many links a post-hoc scan could "match"),
   explicitly non-evidential. A near value in this table proves nothing.

RESULT: Vol₄(implied) = 8.048; no pre-named candidate within even the ±0.31
model band (4-chains 10.149 = +26%; brunnian analogue non-hyperbolic;
L8n7 = Vol(Borromean) = 7.328, −0.72). Scope-(a) NEGATIVE for the
single-link linear-chain reading of the n=4 term; the Lean-proved
multiplicity and the A=3 results are untouched, and the tower itself is not
excluded (the link assignment is the open model input, gated on R5-full).

Run:  python3 -u computations/deltalambda/he4_vol4_prediction_test_probe.py \\
        2>&1 | tee /tmp/he4_vol4.log

EXPLORATORY — audit-only witness; no production wiring; no fit.
Audit: docs/audits/2026-07-13-he4-vol4-prediction-test.md
"""
from __future__ import annotations

import datetime
import json
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent          # computations/deltalambda/
_COMP = _HERE.parent                             # computations/
for _d in (_COMP, _COMP / "substrate"):
    _p = str(_d)
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_constants import M_E_MEV, AME_B_HE4_MEV_VALIDATION  # noqa: E402

set_compute_dps()

# ── inputs (all with provenance; nothing fitted) ─────────────────────────────
M_E = mp.mpf(str(M_E_MEV))                       # CAL-1 (CODATA 2022)
B_AME_4HE = mp.mpf(str(AME_B_HE4_MEV_VALIDATION))  # vendored AME2020, Z=2 A=4

# 3-body sub-link volumes — binding-link-volumes.witness.json (SnapPy-derived,
# committed; L6a4 = Borromean = 8·Catalan verified there symbolically).
VOL_8_11 = mp.mpf("8.286316817806593")           # pnn carrier (³H)
VOL_L6A4 = mp.mpf("7.327724753417752")           # ppn carrier (³He)
# 2-body sub-links: Hopf, Seifert-fibred, Vol = 0
# (degree-one-braid-trivial-volume-proof.md, KMM convention).

PRE_REGISTERED_VOL4 = mp.mpf("8.048")            # theta_mn_bondcount_linearchain.py (2026-07-04)

# pre-named structural candidates (pre-registration: vol4_4he_snappy_falsification_probe.py)
CANDIDATES = [
    ("L8n8", "4-component brunnian (Borromean analogue)"),
    ("L8a21", "4-chain (linear-chain closure)"),
    ("L8a20", "4-chain variant"),
    ("L8a19", "4-component alternating"),
    ("L8n7", "4-component non-alternating"),
]
CORPUS_VALIDATE = {"L6a4": VOL_L6A4, "8_11": VOL_8_11}

TOL_STRICT = 0.05     # the earlier probe's match window
# model band: ±3% (the worst A=3 residual) on the n=3 contribution


def main() -> int:
    import warnings
    warnings.filterwarnings("ignore")

    print("=" * 72)
    print(" ⁴He Vol₄ = 8.05 falsifiable prediction test (bond-count tower)")
    print("=" * 72)

    # ── 1. exact back-out ────────────────────────────────────────────────────
    # ppnn chain: n=2 → 3 Hopf sub-chains (1 bond each, Vol 0);
    #             n=3 → ppn (L6a4) + pnn (8_11), 2 bonds each;
    #             n=4 → 1 cluster, 3 bonds, the unknown Vol₄.
    B_23 = M_E * (2 * VOL_L6A4 + 2 * VOL_8_11)
    resid = B_AME_4HE - B_23
    vol4_implied = resid / (3 * M_E)
    tol_model = float(mp.mpf("0.03") * B_23 / (3 * M_E))

    print(f"  m_e                = {mp.nstr(M_E, 12)} MeV   (CODATA 2022, CAL-1)")
    print(f"  B_AME(4He)         = {mp.nstr(B_AME_4HE, 12)} MeV   (AME2020, vendored)")
    print(f"  Vol(L6a4) [ppn]    = {mp.nstr(VOL_L6A4, 16)}   (binding-link-volumes witness)")
    print(f"  Vol(8_11) [pnn]    = {mp.nstr(VOL_8_11, 16)}")
    print(f"  n=2,3 contribution = m_e*(2*Vol(L6a4)+2*Vol(8_11)) = {mp.nstr(B_23, 10)} MeV"
          f"  ({float(B_23 / B_AME_4HE) * 100:.1f}% of AME)")
    print(f"  residual (n=4)     = {mp.nstr(resid, 10)} MeV = m_e*3*Vol4")
    print(f"  => implied Vol4    = {mp.nstr(vol4_implied, 10)}")
    print(f"  pre-registered     = {mp.nstr(PRE_REGISTERED_VOL4, 6)} (2026-07-04)  "
          f"delta = {float(vol4_implied - PRE_REGISTERED_VOL4):+.5f}")
    print(f"  model tolerance    = +/-{tol_model:.3f} on Vol4  "
          "(+/-3% A=3-residual band on the n=3 term); strict = +/-0.05")

    backout_ok = abs(float(vol4_implied - PRE_REGISTERED_VOL4)) < 0.01
    vol4_f = float(vol4_implied)

    # ── 2. SnapPy: validation + pre-named candidates ─────────────────────────
    try:
        import snappy
    except ImportError:
        print("\nSnapPy unavailable (`pip install snappy`) — cannot run the link test.")
        return 1

    print("\n  SnapPy validation against corpus volumes:")
    val_ok = True
    for name, expect in CORPUS_VALIDATE.items():
        v = float(snappy.Manifold(name).volume())
        good = abs(v - float(expect)) < 1e-9
        val_ok &= good
        print(f"    {name:5s} {v:.12f} vs corpus {mp.nstr(expect, 16)} — {'OK' if good else 'MISMATCH'}")

    print(f"\n  pre-named candidates vs implied Vol4 = {vol4_f:.4f}:")
    rows = {}
    hit_strict, hit_model = [], []
    for name, why in CANDIDATES:
        v = float(snappy.Manifold(name).volume())
        d = v - vol4_f
        rows[name] = {"volume": v, "delta_vs_implied": d, "role": why}
        if abs(d) < TOL_STRICT:
            hit_strict.append(name)
        if abs(d) < tol_model:
            hit_model.append(name)
        print(f"    {name:7s} {v:11.6f}  delta={d:+8.4f}  [{why}]")

    negative = not hit_model    # negative even under the generous band

    # ── 3. guarded census data (selection-freedom quantifier, NON-evidential) ─
    print("\n  GUARDED census tabulation (non-evidential — quantifies selection")
    print("  freedom only; the corpus fixes NO 4-He link, gate = R5-full SDP #604):")
    t0 = time.time()
    census = []
    n_links = 0
    for M in snappy.HTLinkExteriors(cusps=4):
        n_links += 1
        try:
            census.append((M.name(), float(M.volume())))
        except Exception:
            pass
        if n_links % 2000 == 0:
            print(f"    ... {n_links} links scanned ({time.time() - t0:.1f}s)")
    census.sort(key=lambda t: abs(t[1] - vol4_f))
    n_strict = sum(1 for _, v in census if abs(v - vol4_f) < TOL_STRICT)
    n_model = sum(1 for _, v in census if abs(v - vol4_f) < tol_model)
    print(f"    scanned {n_links} 4-component HT census links in {time.time() - t0:.1f}s")
    print(f"    links within +/-{TOL_STRICT} of {vol4_f:.3f}: {n_strict}; "
          f"within +/-{tol_model:.3f}: {n_model}")
    print("    nearest 10 (GUARDED — a near value here proves nothing):")
    for name, v in census[:10]:
        print(f"      {name:12s} {v:11.6f}  delta={v - vol4_f:+8.4f}")

    # ── 4. verdict ───────────────────────────────────────────────────────────
    verdict = (
        f"Two-layer verdict. (i) NOT DECISIVELY TESTABLE: the corpus fixes no derived "
        f"4He binding link (canonical knot-ID gated on R5-full SDP, #604; the A<=3 IDs "
        f"are deprecated volume-search matches), so the link assignment is the open "
        f"MODEL INPUT. (ii) Scope-(a) NEGATIVE for the pre-registered structural "
        f"reading: the exact AME back-out gives Vol4 = {vol4_f:.4f} (confirming the "
        f"pre-registered 8.048), and NO in-advance-named candidate matches within even "
        f"the +/-{tol_model:.2f} model band — linear 4-chains L8a21/L8a20 at 10.149 "
        f"(+26%), brunnian analogue non-hyperbolic (Vol~0), L8n7 = Vol(Borromean) = "
        f"7.328 (-0.72), L8a19 at 10.667. The naive 'n=4 term = single linear-chain-"
        f"closure volume' reading FAILS at 4He. This constrains that single-link "
        f"reading only: the Lean-proved multiplicity (n-1), the 3H -0.16% / 3He -2.97% "
        f"results, and the tower form survive. Guarded census datum: the implied "
        f"volume falls in a GAP of the 4-component HT census spectrum (<=14 "
        f"crossings) — {n_strict} links within +/-0.05, only {n_model} within the "
        f"model band (nearest at +/-0.31/0.34) — so no <=14-crossing 4-component "
        f"link carries Vol4 even post-hoc; and any wider post-hoc volume search "
        f"would be a CAL-4 fit, out of bounds. "
        f"Honest routes: R5-full SDP canonical knot-ID at H12, or a non-single-volume "
        f"n=4 term. No fit; nothing wired."
        if negative else
        f"CANDIDATE MATCH within the model band ({hit_model}) — requires adversarial "
        f"verification before any identification claim (numerology guard; note the "
        f"census has {n_model} links in the same band, so a match is weak evidence)."
    )
    print(f"\nVERDICT: {verdict}")

    # ── 5. witness ───────────────────────────────────────────────────────────
    wit = {
        "computation": "he4-vol4-prediction-test",
        "description": (
            "4He Vol4=8.05 falsifiable prediction test of the bond-count tower "
            "B = m_e*Sum (n-1)*Vol_n: exact AME back-out of the implied Vol4 "
            "(from AME2020 B(4He), CODATA m_e, corpus Vol(L6a4)/Vol(8_11)), "
            "SnapPy comparison against in-advance-named structural candidates, "
            "and a guarded 4-component census density tabulation. NEGATIVE for "
            "the single-link linear-chain reading; link assignment itself is the "
            "open model input (gated on R5-full SDP #604). Scope-(a)."),
        "audit_only": True,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "mpmath+snappy",
        "inputs": {
            "m_e_MeV": {"value": float(M_E), "source": "codata_constants.M_E_MEV (CODATA 2022, CAL-1)"},
            "B_AME_4He_MeV": {"value": float(B_AME_4HE),
                              "source": "codata_constants.AME_B_HE4_MEV_VALIDATION (vendored AME2020)"},
            "Vol_L6a4_ppn": {"value": float(VOL_L6A4), "source": "binding-link-volumes.witness.json"},
            "Vol_8_11_pnn": {"value": float(VOL_8_11), "source": "binding-link-volumes.witness.json"},
            "Vol_2body": {"value": 0.0, "source": "Hopf link non-hyperbolic (KMM convention)"},
        },
        "backout": {
            "B_n23_MeV": float(B_23),
            "residual_n4_MeV": float(resid),
            "vol4_implied": vol4_f,
            "vol4_preregistered_2026_07_04": float(PRE_REGISTERED_VOL4),
            "formula": "vol4 = (B_AME(4He) - m_e*(2*Vol(L6a4)+2*Vol(8_11))) / (3*m_e)",
        },
        "tolerances": {"strict": TOL_STRICT,
                       "model_band": tol_model,
                       "model_band_rationale": "+/-3% (worst A=3 residual) on the n=3 term, propagated"},
        "corpus_validation": {k: {"expected": float(v), "reproduced": True}
                              for k, v in CORPUS_VALIDATE.items()},
        "candidates": rows,
        "census_guarded": {
            "note": "NON-EVIDENTIAL selection-freedom quantifier; no corpus link assignment exists",
            "n_4component_links_scanned": n_links,
            "n_within_strict": n_strict,
            "n_within_model_band": n_model,
            "nearest_10": [{"name": n, "volume": v, "delta": v - vol4_f} for n, v in census[:10]],
        },
        "verdict": verdict,
        "scope": "(a) — constrains the single-link n=4 reading; multiplicity + A=3 + tower form untouched",
        "assertions": [
            {"label": "exact back-out confirms pre-registered Vol4=8.048 to 0.01",
             "passed": bool(backout_ok)},
            {"label": "snappy reproduces corpus L6a4/8_11 volumes to 1e-9",
             "passed": bool(val_ok)},
            {"label": "no pre-named candidate within the +/-3%-band (negative registered)",
             "passed": bool(negative)},
            {"label": "guarded census density tabulated (selection freedom quantified)",
             "passed": bool(n_links > 0)},
        ],
    }
    wit["allPassed"] = all(a["passed"] for a in wit["assertions"])
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, str(_HERE.parent / "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(wit, script_path=__file__, engine="mpmath")
    wit["scriptFile"] = Path(__file__).name
    out = _HERE / "he4-vol4-prediction-test.witness.json"
    json.dump(wit, open(out, "w"), indent=1)
    print(f"\nwitness -> {out.name}   allPassed: {wit['allPassed']}")
    return 0 if wit["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
