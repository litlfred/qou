#!/usr/bin/env python3
"""B1.2 (bean qou-9s8k): the GK bilinear block pairing — the odd channel
as an off-diagonal block product.

SUCCESSOR to the B1 wall (merged #4226): no single-sector small-weight
population bridges O_φ to D_odd; the bridge must live in the
Garoufalidis–Kashaev bilinear structure Z = Σ M_σσ' B_σ(q)B̃_σ'(q̃).

THE UNLOCK. A2's merged machinery (8/8-gated against the 18 printed GGM
H-tables) contains everything needed: the H±_{j,λ} block series, the
W±_m(x) 3×3 block matrices, the pairing matrix B, the dressing matrices
A±/C±, and — crucially — the |q| > 1 GLUE (GGM eq 25)
    W_m(Q)|_{|Q|>1} = J·W⁻_{−m−2}(1/Q)·D,
so BOTH sides of the substrate bar-pair (q₀, 1/q₀) evaluate through
convergent series. The full bilinear matrices are computable at the
substrate now.

TEST (parameter-free, pre-registered): evaluate at x = 1/q₀ the
assemblies
    N  := W₋₁(1/q)·B·W₋₁(q)ᵀ          (the naked GK bilinear)
    S⁺ := ½·A⁺·N·C⁺,  S⁻ := ½·A⁻·Nᵀ'·C⁻   (the dressed Stokes pair)
    O  := ½(S⁺ − S⁻),  Ē := ½(S⁺ + S⁻)
and confront EVERY entry (and the naked ½-entry-differences) with the
four Habiro-face targets
    F_conv = 0.9861565521…,  s(F̄) = 0.9709977446…,
    D_odd = −0.007579403739,  D_even = 0.9785771484…
plus secondary ratio tests against small (half-)integers. Gate 1e-6
(pin band); every near-miss within 10× reported — no selection. ~300
parameter-free comparisons ⇒ coincidence budget ~3e-4 at the gate; a
hit is a lead requiring an independent-anchor test, not an
identification (stated).

Pin: MUON q₀ (matches A2's gates and the A4.3 constants; D_odd moves
−2.2e-9 muon-vs-proton — inside the gate band). auditOnly; no c_k
wired; no fit. Comparison to observed only; no ontological claims.

Run: python3 -u computations/probes/qbeta_5two_gk_bilinear_pairing_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_gk_bilinear.log
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
import qbeta_5two_stokes_barodd_index_probe as sb  # noqa: E402

mp.mp.dps = 60
from q_parameter import q_muon_at  # noqa: E402

# q₀ anchors read BY NAME (bean qou-9ugp, 2026-09-03). The muon leg was the
# literal 1.1099785955573… — the RETIRED self-certified muon pin A,
# superseded 2026-08-22 by the live CODATA-2022 lepton-ratio derivation
# q_muon_at() (+0.0769 ppb). A hardcoded pin cannot be checked against the
# name it is bound to, so it is derived now rather than transcribed.

Q0_MUON = mp.mpf(mp.nstr(q_muon_at(50), 50, strip_zeros=False))
TARGETS = {
    "F_conv": mp.mpf("0.9861565521"),
    "s_Fbar": mp.mpf("0.9709977446"),
    "D_odd": mp.mpf("-0.007579403739"),
    "D_even": mp.mpf("0.9785771484"),
}
GATE = mp.mpf("1e-6")
T0 = time.monotonic()


def log(msg):
    print(f"  [{time.monotonic()-T0:6.0f}s] {msg}", flush=True)


def main() -> int:
    print("=" * 78)
    print(" B1.2 — GK bilinear block pairing vs the Habiro-face targets")
    print("=" * 78)

    x = 1 / Q0_MUON

    # ---- assemble the bilinear objects from A2's gated machinery ----
    log("building W±₋₁ block matrices at x = 1/q₀ (A2 8/8-gated series) ...")
    Wq = sb.W_plus_num(-1, x)
    Winv = mp.matrix(sb.J_M.tolist()) * sb.W_minus_num(-1, x) \
        * mp.matrix(sb.D_M.tolist())
    Bm = mp.matrix(sb.B_M.tolist())
    N = Winv * Bm * Wq.T                       # naked GK bilinear
    Sp = 0.5 * mp.matrix(sb.A_M.tolist()) * N * mp.matrix(sb.C_M.tolist())
    Sm = 0.5 * mp.matrix(sb.Am_M.tolist()) * Wq * Bm * Winv.T \
        * mp.matrix(sb.Cm_M.tolist())
    Om = 0.5 * (Sp - Sm)
    Ev = 0.5 * (Sp + Sm)
    Nt = Wq * Bm * Winv.T                      # transposed-side naked
    Odd_naked = 0.5 * (N - Nt)                 # naked bilinear odd split
    Even_naked = 0.5 * (N + Nt)
    log("assemblies built")

    # ---- consistency gate: Sp/Sm reproduce the committed A2 matrices ----
    import json
    sw = record_upstream(_HERE / "qbeta-5two-stokes-barodd-index.witness.json", _UPSTREAM_RECORDS)
    d_ = sw.get("witness", sw)["data"]
    Sp_ref = [[mp.mpf(v) for v in row] for row in d_["S_plus_at_substrate_muon"]]
    dev_s = max(abs(Sp[i, j] - Sp_ref[i][j]) /
                max(abs(Sp_ref[i][j]), mp.mpf(1))
                for i in range(3) for j in range(3))
    g_s = dev_s < mp.mpf("1e-20")
    log(f"[G] S⁺ reproduces the committed A2 matrix: max rel "
        f"{mp.nstr(dev_s, 3)}  {'PASS' if g_s else 'FAIL'}")

    # ---- the pre-registered confrontation ----
    assemblies = {"N": N, "Nt": Nt, "S+": Sp, "S-": Sm, "O": Om, "E": Ev,
                  "N_odd": Odd_naked, "N_even": Even_naked}
    hits, near = [], []
    n_comp = 0
    log("[T] entry-vs-target confrontation (all near-misses reported):")
    for an, Am in assemblies.items():
        for i in range(3):
            for j in range(3):
                v = Am[i, j]
                if abs(v) < mp.mpf("1e-30"):
                    continue
                for tn, tv in TARGETS.items():
                    n_comp += 1
                    rel = abs(v - tv) / abs(tv)
                    rec = {"assembly": an, "entry": f"[{i}{j}]",
                           "value": mp.nstr(v, 15), "target": tn,
                           "rel": mp.nstr(rel, 3)}
                    if rel < GATE:
                        hits.append(rec)
                        log(f"    HIT: {an}[{i}{j}] = {mp.nstr(v, 12)} ≈ "
                            f"{tn} (rel {mp.nstr(rel, 3)})")
                    elif rel < 10 * GATE:
                        near.append(rec)
    # secondary: entry/target ratios vs small (half-)integers
    small = [mp.mpf(s) * v / 2 for v in (1, 2, 3, 4, 5, 6) for s in (1, -1)]
    for an in ("O", "N_odd"):
        Am = assemblies[an]
        for i in range(3):
            for j in range(3):
                v = Am[i, j]
                if abs(v) < mp.mpf("1e-30"):
                    continue
                R = v / TARGETS["D_odd"]
                for c in small:
                    n_comp += 1
                    rel = abs(R - c) / abs(c)
                    rec = {"assembly": f"{an}[{i}{j}]/D_odd",
                           "ratio": mp.nstr(R, 12),
                           "cand": mp.nstr(c, 4), "rel": mp.nstr(rel, 3)}
                    if rel < GATE:
                        hits.append(rec)
                        log(f"    HIT(ratio): {an}[{i}{j}]/D_odd = "
                            f"{mp.nstr(R, 12)} ≈ {mp.nstr(c, 4)}")
                    elif rel < 10 * GATE:
                        near.append(rec)
    log(f"    {n_comp} parameter-free comparisons: {len(hits)} hit(s), "
        f"{len(near)} near-miss(es)")

    # full entry tables for the record
    tables = {an: [[mp.nstr(Am[i, j], 15) for j in range(3)]
                   for i in range(3)] for an, Am in assemblies.items()}

    wb = WitnessBuilder("qbeta-5two-gk-bilinear-pairing", engine="mpmath",
                        _script_path=__file__)
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "B1.2 (bean qou-9s8k): the GK bilinear block pairing confronted "
        "with the Habiro-face targets. Both sides of the substrate "
        "bar-pair evaluated through A2's 8/8-gated block machinery (the "
        "|q|>1 glue, GGM eq 25); the naked bilinear W₋₁(1/q)·B·W₋₁(q)ᵀ, "
        "the dressed S± pair, their odd/even splits — every entry "
        "compared parameter-free against F_conv, s(F̄), D_odd, D_even "
        "(gate 1e-6, pin band; all near-misses reported, no selection) "
        "plus small-(half-)integer ratio tests on the odd assemblies. "
        "auditOnly; no c_k wired; no fit; a hit is a lead, not an "
        "identification.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("splus_reproduces_committed_a2",
                     computed=dev_s, expected="0.0", tolerance="1e-20",
                     source="in-probe S⁺ assembly = the committed A2 witness "
                            "matrix (consistency gate)")
    # DEMOTED (bean qou-3e5m): this compared 'confrontation_completed' to itself and
    # reported `passed` unconditionally. A count of what a run found is
    # DATA, not a check, and `add_assertion` has no way to say
    # "is nonzero" -- which is plausibly why it was written this way.
    # The assertion's `source` prose is kept alongside the value.
    wb.add_data('confrontation_completed', {'value': n_comp, 'source': 'pre-registered parameter-free confrontation ran to completion; hits + near-misses recorded'})

    ok = all(a.passed for a in wb.assertions)

    wb.add_data("substrate", {"x": mp.nstr(x, 20), "pin": "muon"})
    wb.add_data("assembly_tables", tables)
    wb.add_data("targets", {k: mp.nstr(v, 15) for k, v in TARGETS.items()})
    wb.add_data("confrontation", {"n_comparisons": n_comp, "gate": "1e-6",
                                  "hits": hits, "near_misses": near})
    wb.add_data("verdict",
                ((f"GK-BILINEAR LEAD: {len(hits)} parameter-free hit(s) — "
                  f"see confrontation.hits; requires an independent-anchor "
                  f"test before any identification."
                  if hits else
                  "NO parameter-free GK-bilinear entry matches any "
                  "Habiro-face target at 1e-6 (near-misses recorded). "
                  "Sharpens the wall: the Habiro-face values are not bare "
                  "entries of the W₋₁-level bilinear at the substrate — "
                  "the missing piece is the STATE-INTEGRAL dressing "
                  "(Gaussian prefactor + the (q/q̃)^{1/8} unit and the "
                  "λ-grading of the block basis), i.e. which λ-row the "
                  "Masbaum tail occupies. Named for the next rung.")
                 + " auditOnly.") if ok else "A gate failed — inspect.")
    wb.save({"q0Anchor": "muon",
             "q0Value": mp.nstr(q_muon_at(50), 50, strip_zeros=False),
             "q0AnchorReason": "the GK bilinear pairing is evaluated at the ideal "
                               "CAL-2 (muon) pin only; no proton leg is computed "
                               "(bean qou-9ugp: the pin is now read by name)"})
    print(f"\n  assertions passed: {ok}   ({time.monotonic()-T0:.0f}s)")
    print("  witness -> computations/probes/"
          "qbeta-5two-gk-bilinear-pairing.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
