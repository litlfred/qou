#!/usr/bin/env python3
"""he4_binding_k_presentation_correction_probe.py — SAME-DAY CORRECTION of the
A=4 stage-1 / stage-1.5 probes (he4_binding_k_fingerprint_stage1_probe.py,
he4_binding_k_averaged_interface_probe.py): both evaluated the Rust
Geck-Pfeiffer characters in the WRONG PRESENTATION, so their headline numbers
(best plain K rel Δ = 14.7%; averaged 3-bond rel Δ = 3.8% / "96.2% captured")
are VOID as paper-convention quantities. This probe measures the convention
identity, certifies the corrected pipeline end-to-end against the certified
combiner traces, and records the honest resolution of the A=4 binding-K
question.

THE ERROR (one layer, measured here):

  The Rust GP kernel (`pyhecke_native.chi_lambdas_via_gp`) returns Laurent
  polynomials in a variable v whose generator eigenvalues are (v², −v⁻²) —
  i.e. the paper presentation (q, −q⁻¹) with q = v². Stage 1/1.5 evaluated
  the GP Laurent AT q₀, which is the paper trace at q₀², not at q₀. The
  correct evaluation point is v = √q₀. Measured: on the plain Borromean word
  at H₃, GP(√q₀) ≡ seminormal(q₀) to all 50 digits, while GP(q₀) is off 2.6%.

PIN NUANCE (documented, NOT a stage-1/1.5 error): `q_parameter` is
anchor-adaptive — producers listed in `q0_anchor_manifest.json` `ideal_muon`
resolve the canonical-muon pin from `q-pinning-50-digit.witness.json`
(1.10997859555733471989976…), while ad-hoc shells resolve the proton pin
(1.10997858275138080759…). The certified chi-cache/combiner chain is
coherently MUON-pinned. Stage 1/1.5 hardcoded a muon string that agrees with
the canonical witness value to ~1e-17, so the pin contributed nothing to
their error — but any correction probe importing q_parameter from a
non-manifest process would silently get the proton pin (an 8.8e-8-level
trap, measured); this probe therefore loads the pinning witness directly.

WHAT THE CANONICAL ⁴He WORD ACTUALLY IS (read off `atom_braid_word_3A`; no
fingerprint search needed): T_⁴He = p(0)·σ₂·p(3)·cw₅·n(6)·σ₈⁻¹·n(9) — four
canonical 11-crossing nucleon blocks (NOT plain Borromean [σ₁σ₂⁻¹]³: each
block contains σ⁻¹ and averaged crossings) joined by exactly ONE
inter-nucleon crossing per adjacent seam, at generators {2,5,8} (0-based),
PAIR-TYPED:

    p-p seam (gen 2) → plain σ
    p-n seam (gen 5) → color-weighted average  σ − h(½−δ/4)·I
    n-n seam (gen 8) → σ⁻¹

Stage-1's "one crossing per interface emerges" was a (mis-evaluated)
rediscovery of explicit builder structure; its constituent product (plain
Borromean nucleons) and seam placement ({3,6,9}) were also both wrong.

OPERATOR DICTIONARY (paper presentation, σ⁻¹ = σ − h), certified below:
    (c,d,g)=(1,0,g)    → σ_g           → GP (1, g+1)
    (1,−h,g)           → σ_g⁻¹         → GP (−1, g+1)
    (1,−h/2,g)         → (σ+σ⁻¹)/2     → GP (0, g+1) = σ+σ⁻¹ UNnormalized:
                                          divide the trace by 2 per such crossing
    (1,−h(½−δ/4),g)    → aσ + bσ⁻¹, a=½+δ/4, b=½−δ/4, δ=_avg_color_delta()
                                        → two weighted GP branches

CERTIFICATION: reproduce the certified combiner traces for proton, neutron,
deuteron, ⁴He end-to-end through GP with the dictionary above at v=√q_muon.
p/n are exact-dictionary words (tolerance 1e-15); D/⁴He carry one
color-weighted crossing whose δ enters as f64 in the builder (tolerance
1e-12).

Scope-(a); audit-only; no fit; nothing wired. Stage-2 (per-block PSD +
operator-selection LP) remains the open, non-tautological question.
"""
from __future__ import annotations

import datetime
import json
import os
import sys
from pathlib import Path

# Resolve the ENTIRE module graph (q_parameter → hecke_core → word builder →
# _avg_color_delta) at the certified chain's canonical-muon pin. Without this,
# a non-manifest process gets the proton pin and the color-weighted δ drifts
# by the pin difference — measured as an irreducible 5.9e-11 floor on the
# deuteron/⁴He reproductions (vs 6e-31 with the pin aligned).
os.environ.setdefault("QOU_Q0_ANCHOR", "ideal")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
import pyhecke_native as pn  # noqa: E402
import hecke_core  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from canonical_braid_crossings import _avg_color_delta  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def load_canonical_q() -> str:
    """The certified chain's pin: canonical-muon q from the pinning witness
    (q_parameter is anchor-adaptive and would resolve PROTON in this
    non-manifest process — see docstring)."""
    d = json.loads((COMP / "q-pinning-50-digit.witness.json").read_text())
    q = d["derived_50_digit"]["q"]
    assert q.startswith("1.109978595557"), q
    return q


def classify_word(triples, h_f64):
    """(c,d,g) → (kind ∈ {s,i,a,cw}, 1-based generator).

    h_f64 must be the h the word was built with (hecke_core.h in THIS
    process); the mapping to symbolic operator kinds is pin-independent."""
    kinds = []
    for (c, d, g0) in triples:
        assert abs(float(c) - 1.0) < 1e-12
        df = float(d)
        if abs(df) < 1e-12:
            kinds.append(("s", g0 + 1))
        elif abs(df + h_f64) < 1e-9:
            kinds.append(("i", g0 + 1))
        elif abs(df + h_f64 / 2) < 1e-9:
            kinds.append(("a", g0 + 1))
        else:
            # color-weighted p-n crossing: d = −h(½−δ/4)
            assert abs(df + h_f64 * (0.5 - float(_avg_color_delta()) / 4)) < 1e-9, d
            kinds.append(("cw", g0 + 1))
    return kinds


def main() -> int:
    q_str = load_canonical_q()
    q0 = mp.mpf(q_str)
    v = mp.sqrt(q0)
    h_f64 = float(hecke_core.h)  # this process's word-builder h
    delta = mp.mpf(float(_avg_color_delta()))
    b_cw = mp.mpf(1) / 2 - delta / 4    # σ⁻¹ weight of the p-n crossing
    a_cw = 1 - b_cw                      # σ weight

    y_cache: dict[int, dict] = {}

    def y_of(n):
        if n not in y_cache:
            y_cache[n] = {tuple(k): mp.mpf(str(val))
                          for k, val in y_lambda_at(n, q0).items()}
        return y_cache[n]

    def gp_trM(word_signed, n, point):
        shapes = pn.partitions_of(n)
        y = y_of(n)
        res = pn.chi_lambdas_via_gp(shapes, n, word_signed)
        tot = mp.mpf(0)
        for lam, laurent in zip(shapes, res):
            chi = mp.mpf(0)
            for e, cstr in laurent:
                cc = mp.mpf(cstr) if "/" not in cstr else \
                    mp.mpf(cstr.split("/")[0]) / mp.mpf(cstr.split("/")[1])
                chi += cc * point ** e
            tot += y[tuple(lam)] * chi
        return tot

    def canonical_trace_via_gp(Z, N):
        """Evaluate the FULL operator-valued canonical word through GP(√q)."""
        n = 3 * (Z + N)
        kinds = classify_word(atom_braid_word_3A(Z, N), h_f64)
        n_avg = sum(1 for k in kinds if k[0] == "a")
        n_cw = sum(1 for k in kinds if k[0] == "cw")
        assert n_cw <= 1, "probe handles ≤1 color-weighted crossing"

        def build(cw_branch):
            w = []
            for (kind, g1) in kinds:
                if kind == "s":
                    w.append((1, g1))
                elif kind == "i":
                    w.append((-1, g1))
                elif kind == "a":
                    w.append((0, g1))   # GP sign 0 = σ+σ⁻¹ (unnormalized)
                else:                    # cw → per-branch σ / σ⁻¹
                    w.append((cw_branch, g1))
            return w

        if n_cw:
            val = a_cw * gp_trM(build(1), n, v) + b_cw * gp_trM(build(-1), n, v)
        else:
            val = gp_trM(build(None), n, v)
        return val / mp.mpf(2) ** n_avg, kinds, n_avg, n_cw

    # ── certified combiner targets ────────────────────────────────
    w = json.load(open(COMP / "canonical-tr-m-via-chi-cache.witness.json"))
    targets: dict[str, mp.mpf] = {}

    def walk(o):
        if isinstance(o, dict):
            if "atom" in o and "tr_M_q0" in o:
                targets[o["atom"]] = mp.mpf(str(o["tr_M_q0"]))
            for x in o.values():
                walk(x)
        elif isinstance(o, list):
            for x in o:
                walk(x)
    walk(w)

    print("=" * 72)
    print(" LAYER 1 — presentation pin: plain Borromean [σ₁σ₂⁻¹]³ at H₃")
    print("=" * 72)
    plain = [(1, 1), (-1, 2)] * 3
    semi = mp.mpf(0)
    for lam, chi_str in pn.chi_lambda_all_partitions_mpfr(3, plain, q_str, 50):
        semi += y_of(3)[tuple(lam)] * mp.mpf(chi_str)
    gp_v = gp_trM(plain, 3, v)
    gp_q = gp_trM(plain, 3, q0)
    rel_v = abs(gp_v - semi) / abs(semi)
    rel_q = abs(gp_q - semi) / abs(semi)
    print(f"  seminormal(q)  = {mp.nstr(semi, 25)}")
    print(f"  GP(√q)         = {mp.nstr(gp_v, 25)}   rel Δ = {mp.nstr(rel_v, 4)}")
    print(f"  GP(q)          = {mp.nstr(gp_q, 25)}   rel Δ = {mp.nstr(rel_q, 4)}")
    layer1_pass = rel_v < mp.mpf("1e-40")

    print()
    print("=" * 72)
    print(" LAYER 2 — end-to-end: canonical operator words through GP(√q)")
    print("=" * 72)
    rows = {}
    checks = []
    for atom, Z, N, tol in (("proton", 1, 0, "1e-15"), ("neutron", 0, 1, "1e-15"),
                            ("deuteron", 1, 1, "1e-12"), ("helium-4", 2, 2, "1e-12")):
        val, kinds, n_avg, n_cw = canonical_trace_via_gp(Z, N)
        tgt = targets[atom]
        rel = abs(val - tgt) / abs(tgt)
        ok = rel < mp.mpf(tol)
        checks.append((atom, ok))
        rows[atom] = {
            "gp_reproduction": mp.nstr(val, 25),
            "combiner_target": mp.nstr(tgt, 25),
            "rel_delta": mp.nstr(rel, 6),
            "n_crossings": len(kinds), "n_averaged": n_avg,
            "n_color_weighted": n_cw, "tolerance": tol, "passed": ok,
        }
        print(f"  {atom:9s} GP(√q) = {mp.nstr(val, 20):>24}  target = "
              f"{mp.nstr(tgt, 20):>24}  rel = {mp.nstr(rel, 4)}  "
              f"{'OK' if ok else 'FAIL'}")

    verdict = (
        "SAME-DAY CORRECTION of A=4 stage 1/1.5: both probes evaluated GP Laurent "
        "characters at q₀ where the GP variable is √q (generator eigenvalues "
        "(v², −v⁻²) = paper (q, −q⁻¹) at q = v²) — so the published 14.7% / 3.8% "
        "residuals are VOID as paper-convention quantities, and their 'woven-"
        "structure 3.8%' interpretation is retracted. Convention now measured and "
        "certified: GP(√q) ≡ seminormal(q) exactly (50-digit match, plain word) "
        "and the full operator dictionary (σ; σ⁻¹ = σ−h; averaged = (σ+σ⁻¹)/2 via "
        "GP sign 0 ÷2; color-weighted aσ+bσ⁻¹) reproduces the certified combiner "
        "traces for proton, neutron, deuteron, ⁴He end-to-end through GP at the "
        "canonical-muon pin. The canonical ⁴He binding structure needs no "
        "fingerprint search — it is explicit in atom_braid_word_3A: one "
        "inter-nucleon crossing per adjacent seam at generators {2,5,8} (0-based), "
        "pair-typed (p-p: σ; p-n: color-weighted average; n-n: σ⁻¹), joining four "
        "canonical 11-crossing nucleon blocks. Stage-2 (per-block PSD + "
        "operator-selection LP) remains the open, non-tautological question. "
        "Scope-(a); no fit; nothing wired."
    )
    print("\nVERDICT:", verdict)

    wit = {
        "computation": "he4-binding-k-presentation-correction",
        "description": "Same-day correction of the A=4 stage-1/stage-1.5 probes: "
                       "the GP-kernel presentation identity is measured (GP variable "
                       "v = √q; evaluating at q computes the paper trace at q²) and "
                       "the full operator dictionary is certified end-to-end against "
                       "the certified combiner traces (p, n, D, 4He). Canonical seam "
                       "structure read off the builder: one pair-typed crossing per "
                       "seam at generators {2,5,8}. Stage-1/1.5 headline residuals "
                       "(14.7%, 3.8%) are void.",
        "audit_only": True,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "pyhecke_native(GP + seminormal-mpfr) + mpmath", "dps": 50,
        "q_pin": {
            "used": "canonical muon, q-pinning-50-digit.witness.json derived_50_digit.q",
            "value": q_str,
            "note": "q_parameter is anchor-adaptive (q0_anchor_manifest.json): "
                    "ideal_muon producers resolve this value; ad-hoc shells resolve "
                    "the proton pin — an 8.8e-8-level trap for reproduction scripts. "
                    "Stage-1/1.5's hardcoded muon string agreed to ~1e-17 (pin was "
                    "NOT their error; the presentation was).",
        },
        "presentation": {
            "gp_variable": "v with generator eigenvalues (v², −v⁻²); paper q = v²",
            "correct_eval_point": "v = √q₀",
            "layer1_plain_word": {"rel_at_sqrt_q": mp.nstr(rel_v, 6),
                                  "rel_at_q": mp.nstr(rel_q, 6)},
        },
        "operator_dictionary": {
            "sigma": "(1,0,g) → GP (1,g+1)",
            "sigma_inv": "(1,−h,g) → GP (−1,g+1)  [σ⁻¹ = σ − h]",
            "averaged": "(1,−h/2,g) → GP (0,g+1) = σ+σ⁻¹ unnormalized; ÷2 per crossing",
            "color_weighted": "(1,−h(½−δ/4),g) → (½+δ/4)·σ + (½−δ/4)·σ⁻¹, "
                              "δ = _avg_color_delta()",
        },
        "canonical_4he_structure": {
            "word": "p(0)·σ₂·p(3)·cw₅·n(6)·σ₈⁻¹·n(9)",
            "seam_generators_0based": [2, 5, 8],
            "seam_operators": {"p-p (gen 2)": "plain σ",
                               "p-n (gen 5)": "color-weighted average",
                               "n-n (gen 8)": "σ⁻¹"},
            "note": "nucleon blocks are the canonical 11-crossing operator words, "
                    "NOT plain Borromean [σ₁σ₂⁻¹]³; stage-1/1.5's constituent "
                    "product and its {3,6,9} seam placement were therefore also wrong",
        },
        "end_to_end": rows,
        "voided_claims": [
            "stage-1 'best plain K rel Δ = 14.7%' (he4-binding-k-fingerprint-stage1)",
            "stage-1.5 'averaged 3-bond captures 96.2% / residual 3.8% = woven "
            "structure' (he4-binding-k-averaged-interface)",
        ],
        "verdict": verdict,
        "scope": "(a) — convention correction + certification; stage-2 PSD/LP still open",
        "assertions": [
            {"label": "GP(√q) ≡ seminormal(q) on plain word (≤1e-40)",
             "passed": bool(layer1_pass)},
            *[{"label": f"end-to-end combiner reproduction: {a}", "passed": bool(ok)}
              for a, ok in checks],
        ],
    }
    wit["allPassed"] = all(a["passed"] for a in wit["assertions"])
    out = HERE / "he4-binding-k-presentation-correction.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(wit, script_path=__file__, engine="mpmath")
    wit["scriptFile"] = _os.path.basename(__file__)
    json.dump(wit, open(out, "w"), indent=1)
    print("witness ->", out.name, " allPassed:", wit["allPassed"])
    return 0 if wit["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
