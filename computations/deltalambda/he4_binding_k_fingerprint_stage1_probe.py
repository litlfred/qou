#!/usr/bin/env python3
"""he4_binding_k_fingerprint_stage1_probe.py

⛔ VOID — SAME-DAY CORRECTION (2026-07-13, later the same day). This probe
evaluated the GP Laurent characters AT q₀, but the GP kernel's variable is
√q (generator eigenvalues (v², −v⁻²) = paper (q, −q⁻¹) at q = v²), so every
number below is the paper trace at q₀², not q₀ — the headline "best plain K
rel Δ = 14.7%" is void. The constituent product (plain Borromean nucleons)
and the {3,6,9} seam placement were also wrong: the canonical ⁴He word is
p(0)·σ₂·p(3)·cw₅·n(6)·σ₈⁻¹·n(9) — canonical 11-crossing operator-valued
nucleon blocks joined by ONE pair-typed crossing per seam at generators
{2,5,8} — explicit in `mass_at_3A_proper.atom_braid_word_3A`, no search
needed. See `he4_binding_k_presentation_correction_probe.py` (+witness) for
the measured presentation identity, the certified operator dictionary, and
the end-to-end reproduction of the combiner traces. Stage-2 (PSD/LP) remains
the open question. Kept for the record; do not cite its numbers.

A=4 extension of the canonical binding-K search — STAGE 1 (trace fingerprint),
unblocked by the in-sandbox `pyhecke-native` build (2026-07-13).

Canonical procedure (identical to the A≤3 `binding_k_enumerator.py` stage 1,
extended to A=4 with zero new freedom):

  - constituent product `cp` = 4 Borromean nucleon words `[1,-2,1,-2,1,-2]`
    shifted to offsets {0,3,6,9} in B₁₂ (the same `constituent_product_word`
    rule as A≤3);
  - K candidates over the inter-nucleon generators {σ₃^{±1}, σ₆^{±1}, σ₉^{±1}}
    (the A=4 minimal set, same rule that gave {σ₃^{±1}} at A=2 and
    {σ₃^{±1}, σ₆^{±1}} at A=3), word length 1..L_MAX, inverse-adjacent pruned;
  - fingerprint: tr_M(cp ++ K) at H₁₂(q₀) vs the CANONICAL ⁴He atomic trace
    tr_M(T_⁴He) = 0.0553584262667831… (the 77/77 chi-cache combiner value,
    certified 1 ppQ today) — the same "match the historical atom trace"
    criterion the A≤3 search used (NOT an AME anchor-inversion; B_AME is not
    consulted).

Compute: exact q-Laurent characters per shape via the Rust Geck–Pfeiffer
kernel (`pyhecke_native.chi_lambdas_via_gp`, ~2.3 s/candidate for all 77
partitions of 12), evaluated at the 50-digit q₀ with mpmath (NO FLOAT in the
evaluation path); Wenzl weights y_λ from `wenzl-y-lambda-h12.witness.json`.

HONEST SCOPE (stage 1 of 2): this ranks candidates by the Markov-trace
fingerprint only. The A≤3 procedure's stage 2 (per-block PSD filter +
operator-selection LP with duals) is NOT run here (it needs per-block H₁₂
matrices — the seminormal-mpfr path measured impractically slow in-sandbox).
A fingerprint hit is a CANDIDATE, not an identification; the convention gap is
flagged (candidates are plain braid words; the canonical target trace carries
the averaged/color-weighted interfaces). Nothing is wired; scope-(a).
"""
from __future__ import annotations

import json
import time
import sys
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
Q0_STR = "1.1099785955573347117485528280749490295019743898536"
L_MAX = 3
GENS = [3, -3, 6, -6, 9, -9]
NUCLEON = [1, -2, 1, -2, 1, -2]
OFFSETS = (0, 3, 6, 9)


def cp_word() -> list:
    w = []
    for off in OFFSETS:
        w += [(g + off) if g > 0 else (g - off) for g in NUCLEON]
    return w


def to_tuples(word: list) -> list:
    return [((1, g) if g > 0 else (-1, -g)) for g in word]


def candidates(l_max: int) -> list:
    out = []
    frontier = [[]]
    for _ in range(l_max):
        nxt = []
        for w in frontier:
            for g in GENS:
                if w and w[-1] == -g:      # prune immediate inverse
                    continue
                nw = w + [g]
                nxt.append(nw)
                out.append(nw)
        frontier = nxt
    return out


def main() -> int:
    q0 = mp.mpf(Q0_STR)
    shapes = pn.partitions_of(12)
    y = {tuple(e["partition"]): mp.mpf(e["y_lambda"])
         for e in json.load(open(COMP / "wenzl-y-lambda-h12.witness.json"))["data"]["per_partition"]}
    combiner = json.load(open(COMP / "canonical-tr-m-via-chi-cache.witness.json"))
    target = None
    for r in (combiner.get("data", {}).get("results") or combiner.get("results") or []):
        if r.get("atom") == "helium-4":
            target = mp.mpf(str(r["tr_M_q0"]))
    assert target is not None, "canonical 4He trace not found in combiner witness"

    cp = cp_word()

    def tr_M(word_ints: list) -> mp.mpf:
        res = pn.chi_lambdas_via_gp(shapes, 12, to_tuples(word_ints))
        tot = mp.mpf(0)
        for lam, laurent in zip(shapes, res):
            chi = mp.mpf(0)
            for expo, coeff in laurent:
                c = mp.mpf(coeff) if "/" not in coeff else \
                    mp.mpf(coeff.split("/")[0]) / mp.mpf(coeff.split("/")[1])
                chi += c * q0 ** expo
            tot += y[tuple(lam)] * chi
        return tot

    print("=" * 72)
    print(" A=4 binding-K fingerprint — STAGE 1 (canonical A≤3 rule extended)")
    print("=" * 72)
    print(f" canonical target tr_M(T_4He at H12) = {mp.nstr(target, 16)}")
    cp_tr = tr_M(cp)
    print(f" cp alone (no binding): tr_M = {mp.nstr(cp_tr, 12)}   Δ={mp.nstr(cp_tr - target, 6)}")

    cands = candidates(L_MAX)
    print(f" enumerating {len(cands)} K candidates (len ≤ {L_MAX} over ±{{3,6,9}}, pruned)…")
    rows = []
    t0 = time.time()
    for i, K in enumerate(cands):
        v = tr_M(cp + K)
        rows.append((abs(v - target), K, v))
        if (i + 1) % 25 == 0:
            el = time.time() - t0
            print(f"   {i+1}/{len(cands)}  elapsed {el:.0f}s  eta {el/(i+1)*(len(cands)-i-1):.0f}s",
                  flush=True)
    rows.sort(key=lambda r: r[0])

    print("\n top 10 by |tr_M(cp·K) − target|:")
    top = []
    for d, K, v in rows[:10]:
        rel = d / abs(target)
        top.append({"K_word": K, "tr_M": mp.nstr(v, 16),
                    "abs_delta": mp.nstr(d, 8), "rel_delta": mp.nstr(rel, 6)})
        print(f"   K={str(K):22s} tr_M={mp.nstr(v, 12):>16}  |Δ|={mp.nstr(d, 4)}  rel={mp.nstr(rel, 4)}")

    best = rows[0]
    verdict = (
        f"A=4 STAGE-1 fingerprint (canonical A≤3 rule, zero new freedom): best "
        f"plain inter-nucleon K = {best[1]} with tr_M = {mp.nstr(best[2], 12)} vs "
        f"canonical target {mp.nstr(target, 12)} (rel Δ = {mp.nstr(best[0]/abs(target), 4)}). "
        "Candidates ranked by Markov-trace fingerprint ONLY — stage 2 (per-block "
        "PSD + operator-selection LP) not run (H12 matrices impractical in-sandbox); "
        "plain-vs-averaged interface convention flagged. A fingerprint hit is a "
        "CANDIDATE for the 4He binding link, not an identification. No AME input; "
        "no fit; nothing wired. Scope-(a)."
    )
    print("\nVERDICT:", verdict)

    import datetime
    wit = {
        "computation": "he4-binding-k-fingerprint-stage1",
        "description": "A=4 extension of the canonical binding-K search, stage 1 "
                       "(trace fingerprint), unblocked by the in-sandbox pyhecke-native "
                       "build. cp = 4 Borromean nucleons at offsets {0,3,6,9}; K over "
                       "{σ3,σ6,σ9}^{±1} len≤3; fingerprint vs the certified 77/77 "
                       "canonical 4He trace. Exact GP q-Laurent + 50-dps evaluation "
                       "(no float in the eval path). Stage 2 (PSD+LP) remaining. "
                       "Scope-(a); no fit; nothing wired.",
        "audit_only": True,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "pyhecke_native(GP)+mpmath", "dps": 50,
        "target_canonical_trace": mp.nstr(target, 20),
        "cp_trace_no_binding": mp.nstr(cp_tr, 20),
        "n_candidates": len(cands), "L_max": L_MAX, "generators": GENS,
        "top10": top,
        "verdict": verdict,
        "scope": "(a) — stage-1 fingerprint only; stage-2 PSD/LP + convention reconciliation open",
        "assertions": [
            {"label": "canonical target loaded from certified combiner", "passed": True},
            {"label": "enumeration completed over full pruned candidate set",
             "passed": len(rows) == len(cands)},
        ],
    }
    wit["allPassed"] = all(a["passed"] for a in wit["assertions"])
    out = HERE / "he4-binding-k-fingerprint-stage1.witness.json"
    json.dump(wit, open(out, "w"), indent=1)
    print("witness ->", out.name, " allPassed:", wit["allPassed"])
    return 0 if wit["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
