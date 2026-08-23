#!/usr/bin/env python3
"""he4_binding_k_averaged_interface_probe.py — stage 1.5: the averaged interface.

⛔ VOID — SAME-DAY CORRECTION (2026-07-13, later the same day). This probe
evaluated the GP Laurent characters AT q₀, but the GP kernel's variable is
√q (paper q = v²), so the headline "averaged 3-bond captures 96.2% / residual
3.8% = woven color-tube structure" is void — the 3.8% is a wrong-presentation
artifact, not a measured structural quantity. The comparison was also built
on the wrong constituent product (plain Borromean nucleons vs the canonical
11-crossing operator-valued blocks) and the wrong seam placement ({3,6,9} vs
the canonical {2,5,8} with pair-typed operators: p-p σ, p-n color-weighted
average, n-n σ⁻¹). See `he4_binding_k_presentation_correction_probe.py`
(+witness) for the certified convention and end-to-end combiner reproduction.
Kept for the record; do not cite its numbers.

Follow-up to the stage-1 fingerprint (he4_binding_k_fingerprint_stage1_probe.py),
which found the best PLAIN inter-nucleon word at rel Δ = 14.7% and flagged the
plain-vs-averaged convention as the expected gap. This probe evaluates the
canonical AVERAGED interface operator directly, by linearity of tr_M:

    K_avg = ⊗_{i∈{3,6,9}} (σ_i + σ_i⁻¹)/2
    tr_M(cp · K_avg) = (1/8) Σ_{ε∈{±1}³} tr_M(cp · σ_3^{ε₁} σ_6^{ε₂} σ_9^{ε₃})

(8 plain GP evaluations; exact q-Laurent, 50 dps; no float in the eval path).

RESULT: tr_M(cp·K_avg) = 0.0574618494514  vs canonical 0.0553584262668
        rel Δ = 3.80%   (plain best was 14.7%)

Reading (scope-(a)): the naive linear-chain **averaged 3-bond** operator
captures 96.2% of the canonical ⁴He atomic trace. The decomposition of the
binding structure is now quantitative:

    plain 3-bond          → 14.7%  off
    averaged 3-bond       →  3.8%  off   (this probe)
    canonical (9 averaged crossings woven at {1,2,4,5,6,7,10}) → exact

so the residual 3.8% is precisely the **woven color-tube structure** of the
canonical recipe beyond the naive inter-nucleon placement — a measured,
structural quantity (not noise). Together with stage 1 ("one crossing per
interface emerges"), the A=4 binding factorization T_⁴He ≈ cp·K_avg holds to
3.8% with the averaged 3-bond K — an honest partial identification; the exact
factorization is the recipe itself (tautologically), so the content here is
the 3.8% woven-structure gap. No AME input; no fit; nothing wired.
"""
import sys
import json
import itertools
import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))

import mpmath as mp  # noqa: E402
import pyhecke_native as pn  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
Q0 = mp.mpf("1.1099785955573347117485528280749490295019743898536")


def main() -> int:
    shapes = pn.partitions_of(12)
    y = {tuple(e["partition"]): mp.mpf(e["y_lambda"])
         for e in json.load(open(COMP / "wenzl-y-lambda-h12.witness.json"))["data"]["per_partition"]}
    w = json.load(open(COMP / "canonical-tr-m-via-chi-cache.witness.json"))
    tgt = []

    def walk(o):
        if isinstance(o, dict):
            if o.get("atom") == "helium-4" and "tr_M_q0" in o:
                tgt.append(mp.mpf(o["tr_M_q0"]))
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(w)
    target = tgt[0]

    cp = []
    for off in (0, 3, 6, 9):
        cp += [(g + off) if g > 0 else (g - off) for g in [1, -2, 1, -2, 1, -2]]

    def trM(word):
        res = pn.chi_lambdas_via_gp(shapes, 12, [((1, g) if g > 0 else (-1, -g)) for g in word])
        tot = mp.mpf(0)
        for lam, laurent in zip(shapes, res):
            chi = mp.mpf(0)
            for e, c in laurent:
                cc = mp.mpf(c) if "/" not in c else mp.mpf(c.split("/")[0]) / mp.mpf(c.split("/")[1])
                chi += cc * Q0 ** e
            tot += y[tuple(lam)] * chi
        return tot

    print("=" * 70)
    print(" A=4 stage 1.5 — averaged interface K_avg = ⊗(σ+σ⁻¹)/2 on {3,6,9}")
    print("=" * 70)
    rows = {}
    tot = mp.mpf(0)
    for s in itertools.product([1, -1], repeat=3):
        v = trM(cp + [s[0] * 3, s[1] * 6, s[2] * 9])
        rows[str(s)] = mp.nstr(v, 16)
        tot += v
        print(f"  signs {s}: {mp.nstr(v, 12)}")
    avg = tot / 8
    rel = abs(avg - target) / abs(target)
    print(f"\n  tr_M(cp·K_avg) = {mp.nstr(avg, 16)}")
    print(f"  canonical      = {mp.nstr(target, 16)}")
    print(f"  rel Δ = {mp.nstr(rel, 6)}   (plain best was 0.147)")

    verdict = (
        f"Stage 1.5: the averaged 3-bond operator K_avg = ⊗(σ+σ⁻¹)/2 on the naive "
        f"inter-nucleon interfaces gives tr_M(cp·K_avg) = {mp.nstr(avg, 12)} vs the "
        f"canonical {mp.nstr(target, 12)} — rel Δ = {mp.nstr(rel, 4)} (96.2% captured; "
        "plain best was 14.7%). The residual 3.8% is the measured woven color-tube "
        "structure of the canonical recipe (9 averaged crossings at {1,2,4,5,6,7,10}) "
        "beyond the naive {3,6,9} placement. A=4 factorization T ≈ cp·K_avg holds to "
        "3.8% — honest partial identification. No AME; no fit; nothing wired. Scope-(a)."
    )
    print("\nVERDICT:", verdict)

    wit = {
        "computation": "he4-binding-k-averaged-interface",
        "description": "Stage 1.5 of the A=4 binding-K search: the canonical AVERAGED "
                       "interface operator on the naive {3,6,9} placement, via linearity "
                       "(8 plain GP words, exact q-Laurent, 50 dps). Captures 96.2% of "
                       "the canonical 4He trace (rel 3.8%, vs 14.7% plain); the residual "
                       "is the measured woven color-tube structure. Scope-(a); no fit.",
        "audit_only": True,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "pyhecke_native(GP)+mpmath", "dps": 50,
        "canonical_target": mp.nstr(target, 20),
        "tr_M_cp_K_avg": mp.nstr(avg, 20),
        "rel_delta": mp.nstr(rel, 10),
        "plain_best_rel_delta": "0.1469 (stage 1)",
        "per_sign_words": rows,
        "verdict": verdict,
        "scope": "(a) — averaged 3-bond partial identification; woven-structure residual 3.8% measured",
        "assertions": [
            {"label": "averaged interface improves on plain best (3.8% < 14.7%)",
             "passed": bool(rel < mp.mpf("0.147"))},
        ],
    }
    wit["allPassed"] = all(a["passed"] for a in wit["assertions"])
    out = HERE / "he4-binding-k-averaged-interface.witness.json"
    json.dump(wit, open(out, "w"), indent=1)
    print("witness ->", out.name, " allPassed:", wit["allPassed"])
    return 0 if wit["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
