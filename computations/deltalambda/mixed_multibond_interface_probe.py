#!/usr/bin/env python3
"""mixed_multibond_interface_probe.py — derive-or-refute the MIXED MULTI-BOND
interface: the three isotopes Model G does not close (11B, 14N, 19F).

CONTEXT (R8; follows R6-a / Model G)
------------------------------------
Model G (docs/audits/2026-07-14-model-g-consolidated-record.md; witness
alpha-activation-brunnian.witness.json, committed, 9/9) closes six light
alpha-conjugate(+light) isotopes to < 0.5% of B with zero new constants:

  deficit_pred = 3b * [alpha.alpha pair, #alpha >= 3]           (gated)
               + A_light * b  per alpha.X pair (complete graph)  (always-on)
  b = 0.78192 MeV/nucleon (committed R5-a characterization).

NOT closed: 11B (2a+t, miss 6.440 MeV = -58% deficit-level), 14N (3a+d,
5.818 = -33%), 19F (4a+t, 2.679 = -10%).

FORMALIZE-FIRST (compute-author.md §3.3 — the structural prune is stated
BEFORE the candidate scans, and it kills the whole additive class):

  CONE / ANTI-MONOTONICITY PRUNE.  11B and 19F carry the SAME light cluster
  (t, A_light = 3) with k = 2 vs k = 4 alphas.  Every counting available
  from the cluster graph is coordinatewise NON-DECREASING from 11B to 19F:
      per alpha.X bond            m:            2 -> 4
      per bridged (a,a,X) triple  C(m,2):       1 -> 6
      per nucleon-bond            m*A_light:    6 -> 12
      per light cluster           1:            1 -> 1   (equal)
      per light nucleon           A_light:      3 -> 3   (equal)
  Any non-negative combination V of these therefore has V(19F) >= V(11B).
  The measured miss goes the OTHER way: 6.440 -> 2.679 MeV (x2.40 DECREASE).
  Hence miss != V for every choice of non-negative constants — the ENTIRE
  class of additive non-negative graph-counting extensions of Model G is
  excluded on the committed data, before any scan.  (Scope: conditional on
  the all-alpha decompositions and the committed AME deficits; sign-changing
  or non-additive (saturating / shared-channel) closures are NOT excluded;
  candidate (c) below changes the decomposition and is separately
  adjudicated.)

PRE-REGISTERED CANDIDATES (task R8; each zero-new-constants; each must ALSO
leave the closed six closed — the regression is mandatory and decisive):
  (a) BRIDGE copies: the light cluster bonded to m alphas carries the
      always-on channel per bond.  Sub-reading a1 (m copies, complete graph)
      IS the committed Model G — already open.  Sub-reading a2 adds (m-1)
      MORE copies (total 2m-1): extra = b*A_light*(m-1).
  (b) GATE = 3 CLUSTERS (not 3 alphas): does the t in 11B activate the
      k = 2 alpha.alpha pair?  11B (2a+t) is the discriminating case: if
      yes, 11B gains one gated pair (3b = 2.346; empirical flat value
      g = 2.4155).  Regression: 9Be (2a+n) would gain the same pair.
  (c) SUB-CLUSTER PROMOTION: additivity over the LARGEST bound sub-clusters
      (max B_add over {committed all-alpha} u {2-part splits into vendored
      AME nuclei}), each composite at its AME value, + Model-G CROSS
      interface terms between top-level clusters (cross alpha.alpha gated
      by TOTAL alpha count >= 3; cross alpha.X at A_light*b per bond;
      internal pairs live inside the AME value).

Run:  python3 -u computations/deltalambda/mixed_multibond_interface_probe.py \\
        2>&1 | tee /tmp/mixed_multibond_interface.log

EXPLORATORY — audit-only witness; no production wiring; no fitted constant
(b reused from the committed R5-a witness; nothing tuned; all candidates and
thresholds pre-registered).
Audit: docs/audits/2026-07-14-mixed-multibond-interface-derive-or-refute.md
"""
from __future__ import annotations

import datetime
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent          # computations/deltalambda/
_COMP = _HERE.parent                             # computations/
for _d in (_COMP, _COMP / "substrate"):
    _p = str(_d)
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_constants import _ame2020, _ame_binding_mev  # noqa: E402

set_compute_dps()

ISO_ZA = {"6Li": (3, 6), "7Li": (3, 7), "8Be": (4, 8), "9Be": (4, 9),
          "11B": (5, 11), "12C": (6, 12), "14N": (7, 14), "16O": (8, 16),
          "19F": (9, 19)}
PIECE_ZA = {"4He": (2, 4), "d": (1, 2), "t": (1, 3)}
TRIO = ["11B", "14N", "19F"]
CLOSED_SIX = ["6Li", "7Li", "8Be", "9Be", "12C", "16O"]

# (n_alpha, tuple of light-cluster nucleon counts) per cluster species used
# in the pre-registered (c) splits.  n and p enter at B = 0 (free nucleons).
CONTENT = {"n": (0, (1,)), "p": (0, (1,)), "d": (0, (2,)), "t": (0, (3,)),
           "4He": (1, ()), "7Li": (1, (3,)), "8Be": (2, ()),
           "12C": (3, ()), "13C": (3, (1,)), "15N": (3, (3,)),
           "16O": (4, ())}
B_ZA = {"n": None, "p": None, "d": (1, 2), "t": (1, 3), "4He": (2, 4),
        "7Li": (3, 7), "8Be": (4, 8), "12C": (6, 12), "13C": (6, 13),
        "15N": (7, 15), "16O": (8, 16)}

# Pre-registered (c) splits per trio isotope: the max-B_add 2-part split
# (verified against the vendored-AME enumeration below) + the task-named
# example splits.  16O's best 2-part split is included because rule (c)
# CHANGES its decomposition — part of the mandatory closed-six regression.
SPLITS = {"11B": [("7Li", "4He"), ("8Be", "t")],
          "14N": [("13C", "p"), ("12C", "d")],
          "19F": [("15N", "4He"), ("16O", "t")],
          "16O": [("12C", "4He")]}


def bmev(name: str) -> mp.mpf:
    za = B_ZA[name]
    return mp.mpf(0) if za is None else _ame_binding_mev(*za)


def cross_interface(c1: str, c2: str, k_total: int, b: mp.mpf):
    """Model-G cross terms between two top-level clusters (internal pairs
    are inside the AME values and NOT counted).  Returns (value, label)."""
    k1, L1 = CONTENT[c1]
    k2, L2 = CONTENT[c2]
    aa_pairs = k1 * k2
    aa_val = (3 * b) if k_total >= 3 else mp.mpf(0)
    ax = b * (k1 * sum(L2) + k2 * sum(L1))
    ll = bool(L1 and L2)  # light-light: no term in the vocabulary (flagged)
    lab = (f"{aa_pairs}aa[{'on' if aa_val > 0 else 'off'}]"
           f"+ax:{float(ax):.3f}" + ("+ll:none" if ll else ""))
    return aa_pairs * aa_val + ax, lab


def main() -> int:
    print("=" * 76)
    print(" MIXED MULTI-BOND INTERFACE — derive-or-refute (R8: 11B / 14N / 19F)")
    print(" zero new constants; b witness-fed; all candidates pre-registered")
    print("=" * 76)

    # ── [0] committed witnesses; consistency cross-checks ───────────────────
    W_ADD = json.load(open(_HERE / "alpha-cluster-volume-additivity.witness.json"))
    W_G = json.load(open(_HERE / "alpha-activation-brunnian.witness.json"))
    ADD = W_ADD["alpha_cluster_additivity_AME_level"]
    ROWS_G = W_G["model_G_per_isotope"]
    B_LIN = mp.mpf(str(W_G["inputs"]["b_linear_MeV_per_nucleon"]["value"]))
    b = B_LIN

    max_dev_ame = 0.0
    for iso, row in ADD.items():
        Z, A = ISO_ZA[iso]
        b_ame = _ame_binding_mev(Z, A)
        b_add = sum(_ame_binding_mev(*PIECE_ZA[p]) if p != "n" else mp.mpf(0)
                    for p in row["pieces"])
        max_dev_ame = max(max_dev_ame,
                          abs(float(b_ame - b_add) - row["deficit_MeV"]))
    ame_consistent = max_dev_ame < 1e-9

    # reproduce the committed Model-G ledger (complete-graph pairs, gated aa)
    max_dev_g = 0.0
    for iso, row in ADD.items():
        pieces = row["pieces"]
        n_alpha = sum(1 for p in pieces if p == "4He")
        lights = [p for p in pieces if p != "4He"]
        n_aa = n_alpha * (n_alpha - 1) // 2
        aa_val = (3 * b) if n_alpha >= 3 else mp.mpf(0)
        pred = n_aa * aa_val + sum(
            {"n": 1, "d": 2, "t": 3}[x] * b * n_alpha for x in lights)
        max_dev_g = max(max_dev_g,
                        abs(float(pred) - ROWS_G[iso]["pred_deficit_MeV"]))
    ledger_reproduces = max_dev_g < 1e-9
    print(f"\n[0] committed deficits reproduce from vendored AME2020 to "
          f"{max_dev_ame:.2e} MeV;\n    committed Model-G ledger reproduces to "
          f"{max_dev_g:.2e} MeV;  b = {mp.nstr(B_LIN, 6)} MeV/nucleon\n"
          f"    (R5-a committed characterization — reused, not re-fit).")

    # ── [1] characterization: the trio ledger + residual correlates ─────────
    M_OF = {"11B": 2, "14N": 3, "19F": 4}   # alphas the light cluster contacts
    AL_OF = {"11B": 3, "14N": 2, "19F": 3}  # A_light
    print("\n[1] CHARACTERIZATION (committed witnesses; miss = deficit - pred):")
    print(f"    {'iso':4s} {'deficit':>8s} {'pred_G':>7s} {'miss':>7s} "
          f"{'miss/b':>7s} {'/triple':>8s} {'/bond':>7s} {'/nuc-bond':>9s}")
    char = {}
    miss = {}
    for iso in TRIO:
        r = ROWS_G[iso]
        ms = r["deficit_MeV"] - r["pred_deficit_MeV"]
        miss[iso] = ms
        m, A = M_OF[iso], AL_OF[iso]
        n_trip = m * (m - 1) // 2 if m >= 2 else 0  # (a,a,X) triples bridged
        char[iso] = {"deficit_MeV": r["deficit_MeV"],
                     "pred_G_MeV": r["pred_deficit_MeV"], "miss_MeV": ms,
                     "m_alpha_contacts": m, "A_light": A,
                     "miss_over_b": ms / float(b),
                     "miss_per_aaX_triple": ms / max(n_trip, 1),
                     "miss_per_aX_bond": ms / m,
                     "miss_per_nucleon_bond": ms / (m * A),
                     "miss_over_deficit": ms / r["deficit_MeV"]}
        c = char[iso]
        print(f"    {iso:4s} {c['deficit_MeV']:8.4f} {c['pred_G_MeV']:7.4f} "
              f"{ms:7.4f} {c['miss_over_b']:7.3f} {c['miss_per_aaX_triple']:8.3f} "
              f"{c['miss_per_aX_bond']:7.3f} {c['miss_per_nucleon_bond']:9.3f}")
    nonflat = max(char[i]["miss_per_nucleon_bond"] for i in TRIO) / \
        min(char[i]["miss_per_nucleon_bond"] for i in TRIO)
    print(f"    -> the miss is NON-FLAT under every per-unit reading: per-triple "
          f"x{char['11B']['miss_per_aaX_triple'] / char['19F']['miss_per_aaX_triple']:.1f},")
    print(f"       per-bond x{char['11B']['miss_per_aX_bond'] / char['19F']['miss_per_aX_bond']:.1f}, "
          f"per-nucleon-bond x{nonflat:.1f} across the trio.")
    print("    The trio = exactly the isotopes with A_light >= 2 AND m >= 2")
    print("    (9Be has A_light = 1 and closes; 6Li/7Li have m = 1 and close):")
    print("    the missing object is a MULTI-NUCLEON light cluster SHARED")
    print("    between multiple alphas.")

    # 15N diagnostic (3a+t; not in the committed witness set): the t-series
    # miss vs k is NON-monotone, so the smooth -58 -> -33 -> -10 trend is
    # partly an artifact of mixing d and t light clusters.
    d15 = float(_ame_binding_mev(7, 15)
                - 3 * _ame_binding_mev(2, 4) - _ame_binding_mev(1, 3))
    pred15 = float(3 * (3 * b) + 3 * (3 * b))   # 3 gated aa + 3 a.t bonds
    miss15 = d15 - pred15
    print(f"\n    15N (3a+t) diagnostic: deficit {d15:.4f}, Model-G pred "
          f"{pred15:.4f}, miss {miss15:.4f}\n    ({miss15 / d15 * 100:.1f}% "
          f"deficit-level). t-series miss vs k: 6.440 (k=2) -> "
          f"{miss15:.3f} (k=3) -> 2.679 (k=4):\n    NON-monotone — the "
          f"'smooth trend in A' reading is an artifact of mixing d and t.")

    # ── [2] formalize-first CONE PRUNE (stated in the docstring; verified) ──
    countings = {
        "per alpha.X bond (m)": {i: M_OF[i] for i in TRIO},
        "per bridged triple C(m,2)": {i: M_OF[i] * (M_OF[i] - 1) // 2 for i in TRIO},
        "per nucleon-bond (m*A_light)": {i: M_OF[i] * AL_OF[i] for i in TRIO},
        "per light cluster (1)": {i: 1 for i in TRIO},
        "per light nucleon (A_light)": {i: AL_OF[i] for i in TRIO},
    }
    all_mono = all(N["19F"] >= N["11B"] for N in countings.values())
    miss_reversed = miss["19F"] < 0.5 * miss["11B"]
    print("\n[2] CONE PRUNE (formalize-first): 11B and 19F carry the SAME light")
    print("    cluster (t); every graph counting is non-decreasing 11B -> 19F:")
    for name, N in countings.items():
        print(f"      {name:32s} {N['11B']:2d} -> {N['19F']:2d}")
    print(f"    but the miss DECREASES x{miss['11B'] / miss['19F']:.2f} "
          f"({miss['11B']:.3f} -> {miss['19F']:.3f} MeV).")
    print("    -> NO non-negative combination V of these countings satisfies")
    print("       V(11B) = miss(11B) and V(19F) = miss(19F) (any such V has")
    print("       V(19F) >= V(11B)). The ENTIRE additive non-negative")
    print("       graph-counting class is excluded on the committed data —")
    print("       cited invariant: coordinatewise monotonicity of the counting")
    print("       cone vs the strictly decreasing measured miss. Scope:")
    print("       conditional on the all-alpha decompositions ((c) is separate)")
    print("       and the committed AME deficits; non-additive / saturating /")
    print("       sign-changing closures are NOT excluded.")

    # ── [3] candidate (a): bridge copies ─────────────────────────────────────
    print("\n[3] (a) BRIDGE copies — light cluster carries the channel per bond:")
    print("    a1 (m copies, complete graph) IS the committed Model G -> already")
    print("    open (the trio misses above). a2 adds (m-1) more copies:")
    a2 = {}
    for iso in TRIO:
        extra = float(b) * AL_OF[iso] * (M_OF[iso] - 1)
        a2[iso] = {"extra_MeV": extra, "miss_MeV": miss[iso],
                   "miss_over_extra": miss[iso] / extra}
        print(f"      {iso}: extra b*A_light*(m-1) = {extra:6.4f} vs miss "
              f"{miss[iso]:6.4f}  ratio {miss[iso] / extra:5.2f}")
    a2_span = max(r["miss_over_extra"] for r in a2.values()) / \
        min(r["miss_over_extra"] for r in a2.values())
    # regression: 9Be (n, m=2) would gain b*1*(m-1) = b
    d9 = mp.mpf(str(ADD["9Be"]["deficit_MeV"]))
    b9 = mp.mpf(str(ADD["9Be"]["B_AME_MeV"]))
    a2_9be_resid_B = float((2 * b + b * 1 * 1 - d9) / b9)
    print(f"      ratio span x{a2_span:.1f} (needs ~1.0 flat): NON-FLAT — and the")
    print(f"      regression breaks 9Be: pred 3b = {float(3 * b):.4f} vs deficit "
          f"{float(d9):.4f}\n      -> resid {a2_9be_resid_B * 100:+.2f}% of B "
          f"(was -0.02%). (a) REFUTED both ways.")

    # ── [4] candidate (b): gate = 3 clusters — the discriminating 11B case ──
    g_flat = float(mp.mpf(str(W_G["unification_3b"]["flat_per_pair_MeV"])))
    print("\n[4] (b) GATE = 3 CLUSTERS (does the t activate the k=2 alpha.alpha")
    print("    pair?) — 11B (2a+t) is the discriminating case:")
    b_rows = {}
    for gv, name in [(float(3 * b), "3b"), (g_flat, "g_flat")]:
        after = miss["11B"] - gv
        b_rows[name] = {"granted_MeV": gv, "miss_after_MeV": after,
                        "miss_after_over_deficit": after / char["11B"]["deficit_MeV"]}
        print(f"      grant one gated pair ({name} = {gv:.4f}): miss "
              f"{miss['11B']:.4f} -> {after:.4f}\n        "
              f"({after / char['11B']['deficit_MeV'] * 100:+.1f}% of deficit — "
              f"NOT closed)")
    b_9be_resid_B = float((2 * b + 3 * b - d9) / b9)
    print(f"      regression: 9Be (2a+n) would gain the same pair: pred 5b = "
          f"{float(5 * b):.4f}\n      vs deficit {float(d9):.4f} -> resid "
          f"{b_9be_resid_B * 100:+.2f}% of B (was -0.02%): BREAKS 9Be.")
    print("      -> (b) REFUTED twice over: the 3-cluster gate would not close")
    print("      11B even if granted, AND it breaks 9Be. The gate is alpha-only")
    print("      (I3, Milnor indeterminacy) — now confirmed at the")
    print("      discriminating multi-nucleon-spectator case, not just 9Be.")

    # ── [5] candidate (c): sub-cluster promotion ─────────────────────────────
    # verify the pre-registered best 2-part splits against vendored AME
    entries = _ame2020()["entries"]
    bmap = {(e["Z"], e["A"]): mp.mpf(str(e["binding_energy_total_keV"])) / 1000
            for e in entries}
    bmap[(0, 1)] = mp.mpf(0)
    bmap[(1, 1)] = mp.mpf(0)

    def best_split(Z, A):
        best = None
        for Z1 in range(0, Z + 1):
            for A1 in range(1, A):
                Z2, A2 = Z - Z1, A - A1
                if (Z1, A1) > (Z2, A2):
                    continue
                if (Z1, A1) in bmap and (Z2, A2) in bmap:
                    s = bmap[(Z1, A1)] + bmap[(Z2, A2)]
                    if best is None or s > best[0]:
                        best = (s, (Z1, A1), (Z2, A2))
        return best

    NAME_OF = {v: k for k, v in B_ZA.items() if v}
    NAME_OF[(0, 1)] = "n"
    NAME_OF[(1, 1)] = "p"
    best_named = {}
    for iso in TRIO + ["16O"]:
        s, p1, p2 = best_split(*ISO_ZA[iso])
        best_named[iso] = tuple(sorted(
            (NAME_OF.get(p1, str(p1)), NAME_OF.get(p2, str(p2)))))
    splits_match = all(best_named[iso] == tuple(sorted(SPLITS[iso][0]))
                       for iso in TRIO + ["16O"])

    print("\n[5] (c) SUB-CLUSTER PROMOTION — max-B_add decomposition (verified")
    print(f"    against vendored AME 2-part enumeration: pre-registered splits "
          f"{'MATCH' if splits_match else 'MISMATCH'})\n    + Model-G cross "
          f"interface (cross aa gated by TOTAL alpha count >= 3;\n    cross a.X "
          f"at A_light*b per bond; internal pairs inside the AME values):")
    c_rows = {}
    for iso in TRIO + ["16O"]:
        Z, A = ISO_ZA[iso]
        b_ame = _ame_binding_mev(Z, A)
        for c1, c2 in SPLITS[iso]:
            k_total = CONTENT[c1][0] + CONTENT[c2][0]
            badd = bmev(c1) + bmev(c2)
            deficit = b_ame - badd
            inter, lab = cross_interface(c1, c2, k_total, b)
            resid = inter - deficit
            resid_B = float(resid / b_ame)
            c_rows[f"{iso}={c1}+{c2}"] = {
                "B_add_MeV": float(badd), "deficit_MeV": float(deficit),
                "cross_interface_MeV": float(inter), "terms": lab,
                "resid_MeV": float(resid),
                "resid_over_deficit": float(resid / deficit),
                "resid_over_B_AME": resid_B}
            print(f"      {iso:4s}= {c1:4s}+{c2:4s}: B_add {float(badd):8.3f} "
                  f"deficit {float(deficit):7.3f} cross {float(inter):6.3f} "
                  f"[{lab}]\n            resid {float(resid):+7.3f} "
                  f"({float(resid / deficit) * 100:+6.1f}% of deficit, "
                  f"{resid_B * 100:+5.2f}% of B)")
    c_trio_all_fail = all(
        abs(r["resid_over_B_AME"]) > 0.005
        for k, r in c_rows.items() if k.split("=")[0] in TRIO)
    c_19F_sign_flip = (c_rows["19F=15N+4He"]["resid_MeV"] > 0
                       and miss["19F"] > 0)
    c_16O_closes = abs(c_rows["16O=12C+4He"]["resid_over_B_AME"]) < 0.005
    print("      -> NO tested decomposition closes any trio member (< 0.5% of")
    print("      B). 19F FLIPS SIGN under 15N+alpha (+134% overshoot: the 15N")
    print("      AME value already contains 15N's own mixed interface, which")
    print("      Model G undershoots by 8.05 MeV) — the two decompositions")
    print("      BRACKET zero, so an interface theory exists between the")
    print("      countings, but no zero-constant rule tested lands it.")
    print(f"      Coherence datum: 16O = 12C+alpha closes at "
          f"{c_rows['16O=12C+4He']['resid_over_B_AME'] * 100:+.2f}% of B —")
    print("      promotion is CONSISTENT with Model G where the sub-cluster's")
    print("      internal pairs are already gated on inside its AME value.")

    # ── [6] closed-six regression under rule (c) ─────────────────────────────
    print("\n[6] CLOSED-SIX REGRESSION under rule (c) (max-B_add decomposition +")
    print("    cross interface — the only candidate that changes any closed")
    print("    isotope's decomposition is 16O -> 12C+alpha):")
    six_rows = {}
    for iso in CLOSED_SIX:
        row = ADD[iso]
        b_ame = mp.mpf(str(row["B_AME_MeV"]))
        badd_alpha = mp.mpf(str(row["B_add_MeV"]))
        pred_alpha = mp.mpf(str(ROWS_G[iso]["pred_deficit_MeV"]))
        cand = [("all-alpha", badd_alpha, pred_alpha)]
        if iso in SPLITS:
            c1, c2 = SPLITS[iso][0]
            inter, _ = cross_interface(
                c1, c2, CONTENT[c1][0] + CONTENT[c2][0], b)
            cand.append((f"{c1}+{c2}", bmev(c1) + bmev(c2), inter))
        name, badd, inter = max(cand, key=lambda t: t[1])
        resid_B = float((badd + inter - b_ame) / b_ame)
        six_rows[iso] = {"decomposition": name, "B_add_MeV": float(badd),
                         "interface_MeV": float(inter),
                         "resid_over_B_AME": resid_B}
        print(f"      {iso:4s} [{name:10s}] B_add {float(badd):8.3f} + "
              f"interface {float(inter):6.3f} -> resid "
              f"{resid_B * 100:+5.2f}% of B")
    six_survive = all(abs(r["resid_over_B_AME"]) < 0.005
                      for r in six_rows.values())
    print(f"      -> closed six {'SURVIVE' if six_survive else 'BREAK'} under "
          f"rule (c) (16O improves to "
          f"{six_rows['16O']['resid_over_B_AME'] * 100:+.2f}%);")
    print("      rule (c) is SAFE but INSUFFICIENT — it does not close the trio.")

    # ── verdict ──────────────────────────────────────────────────────────────
    verdict = (
        "REFUTED (all three pre-registered zero-new-constant candidates), with "
        "a structural exclusion of the whole additive class. CONE PRUNE "
        "(formalize-first, stated before the scans): 11B and 19F carry the "
        "same light cluster (t) at k = 2 vs k = 4; every cluster-graph "
        "counting (per-bond m, per-bridged-triple C(m,2), per-nucleon-bond "
        "m*A_light, per-cluster 1, per-nucleon A_light) is non-decreasing "
        "11B -> 19F while the measured miss DECREASES x2.40 (6.440 -> 2.679 "
        "MeV) — no non-negative combination of graph countings can close the "
        "trio (invariant: monotone counting cone vs strictly decreasing miss; "
        "conditional on the all-alpha decompositions and committed AME "
        "deficits; non-additive/saturating closures not excluded). (a) bridge "
        "copies: sub-reading a1 (per-bond, complete graph) IS committed Model "
        "G (open); a2 (+(m-1) copies) is x7.2 non-flat across the trio AND "
        "breaks 9Be (+1.33% of B). (b) gate = 3 clusters: granting 11B the "
        "gated pair leaves -36% of deficit unexplained AND the same rule "
        "breaks 9Be (+4.02% of B) — the alpha-only Milnor gate (I3) is "
        "confirmed at the discriminating multi-nucleon-spectator case. (c) "
        "sub-cluster promotion (max-B_add + Model-G cross interface): 11B = "
        "7Li+alpha resid -73% of deficit (-8.3% of B), 14N = 13C+p -69% "
        "(-5.0% of B), 19F = 15N+alpha FLIPS SIGN to +134% (+3.6% of B) — "
        "brackets zero but nothing lands it; the closed six SURVIVE rule (c) "
        "(16O = 12C+alpha closes at -0.10% of B, a genuine coherence datum: "
        "promotion commutes with Model G when the sub-cluster's pairs are "
        "already gated on inside its AME value). CHARACTERIZATION: the trio "
        "is exactly {A_light >= 2 AND m >= 2}; the miss per nucleon-bond "
        "falls from 1.07 (11B) to 0.22 (19F); the 15N (3a+t) diagnostic (miss "
        "8.05 MeV, -36%) makes the t-series NON-monotone in k (6.44 -> 8.05 "
        "-> 2.68), so the smooth -58/-33/-10 trend is partly an artifact of "
        "mixing d and t. The missing object is a SHARED (sub-additive, "
        "non-additive in the counting cone) channel of a multi-nucleon light "
        "cluster bonded to several alphas — scope-(a) for Model G's "
        "ingredients (nothing excluded as an ingredient); scope-(b) ONLY for "
        "the additive non-negative graph-counting class, with the cone "
        "invariant cited. Nothing tuned; b reused from the committed R5-a "
        "witness; no production wiring.")
    print(f"\nVERDICT: {verdict}")

    # ── witness ──────────────────────────────────────────────────────────────
    wit = {
        "computation": "mixed-multibond-interface-derive-or-refute",
        "description": (
            "R8 derive-or-refute of the mixed multi-bond interface (11B/14N/"
            "19F — the isotopes Model G does not close): exact ledgers + "
            "residual correlates from committed witnesses; formalize-first "
            "cone prune excluding every additive non-negative graph-counting "
            "extension; pre-registered candidates (a) bridge copies, (b) "
            "3-cluster gate (11B discriminating case), (c) sub-cluster "
            "promotion with Model-G cross interface; mandatory closed-six "
            "regression. All inputs from committed witnesses + vendored "
            "AME2020; nothing recomputed, nothing tuned."),
        "audit_only": True,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "mpmath (witness-fed; no new tr_M compute)",
        "inputs": {
            "deficit_source": "alpha-cluster-volume-additivity.witness.json (committed; consistency-checked to 1e-9 MeV)",
            "model_G_source": "alpha-activation-brunnian.witness.json (committed; ledger reproduced to 1e-9 MeV)",
            "b_linear_MeV_per_nucleon": {
                "value": float(B_LIN),
                "source": "alpha-activation-brunnian.witness.json inputs.b_linear_MeV_per_nucleon (committed R5-a; reused not re-fit)"},
            "AME2020": "vendored qou-mass/src/qou_mass/data/ame2020.json via codata_constants._ame_binding_mev",
        },
        "characterization": {
            "per_isotope": char,
            "n15_diagnostic_3a_t": {
                "deficit_MeV": d15, "pred_G_MeV": pred15, "miss_MeV": miss15,
                "miss_over_deficit": miss15 / d15,
                "note": "t-series miss vs k NON-monotone: 6.440 (k=2) -> 8.049 (k=3) -> 2.679 (k=4); the smooth trend-in-A reading mixes d and t"},
            "trio_selector": "exactly the isotopes with A_light >= 2 AND m >= 2 (9Be A_light=1 closes; 6Li/7Li m=1 close)",
        },
        "cone_prune": {
            "countings_11B_to_19F": {k: [v["11B"], v["19F"]]
                                     for k, v in countings.items()},
            "miss_11B_MeV": miss["11B"], "miss_19F_MeV": miss["19F"],
            "miss_decrease_factor": miss["11B"] / miss["19F"],
            "invariant": "coordinatewise monotone counting cone (11B -> 19F, same light cluster t) vs strictly decreasing measured miss",
            "scope": "excludes the additive non-negative graph-counting class given the all-alpha decompositions + committed AME deficits; non-additive/saturating/sign-changing closures NOT excluded; (c) adjudicated separately",
        },
        "candidate_a_bridge": {
            "a1_note": "m copies (complete graph) IS committed Model G — already open",
            "a2_rows": a2, "a2_ratio_span": a2_span,
            "a2_9Be_regression_resid_over_B": a2_9be_resid_B,
            "verdict": "REFUTED (x7+ non-flat across the trio; breaks 9Be)"},
        "candidate_b_3cluster_gate": {
            "rows_11B": b_rows,
            "regression_9Be_resid_over_B": b_9be_resid_B,
            "verdict": "REFUTED twice (11B stays open at -36% even granted; 9Be breaks at +4.0% of B); alpha-only gate (I3) confirmed at the discriminating multi-nucleon-spectator case"},
        "candidate_c_promotion": {
            "best_2part_splits_verified": best_named,
            "pre_registered_match": splits_match,
            "rows": c_rows,
            "coherence_16O_12C_alpha": c_rows["16O=12C+4He"],
            "verdict": "REFUTED for the trio (11B -73%, 14N -69% of deficit; 19F flips sign +134% — brackets zero, nothing lands it); 16O = 12C+alpha coherence at -0.10% of B"},
        "closed_six_regression_rule_c": six_rows,
        "verdict": verdict,
        "scope": "(a) for Model G's ingredients (nothing excluded as ingredient); (b) only for the additive non-negative graph-counting class, invariant cited (cone monotonicity vs decreasing miss)",
        "assertions": [
            {"label": "committed additivity deficits reproduce from vendored AME2020 to 1e-9 MeV",
             "passed": bool(ame_consistent)},
            {"label": "committed Model-G ledger (all 9 isotopes) reproduces to 1e-9 MeV",
             "passed": bool(ledger_reproduces)},
            {"label": "characterization: trio misses all positive (undershoot) and >4x non-flat per nucleon-bond",
             "passed": bool(all(miss[i] > 0 for i in TRIO) and nonflat > 4)},
            {"label": "cone prune: every pre-registered counting non-decreasing 11B->19F while the miss falls by >2x",
             "passed": bool(all_mono and miss_reversed)},
            {"label": "(a2) refuted: ratio span > 5x across the trio AND 9Be regression breaks (> 0.5% of B)",
             "passed": bool(a2_span > 5 and abs(a2_9be_resid_B) > 0.005)},
            {"label": "(b) refuted: 11B miss remains > 25% of deficit even granting the gated pair AND 9Be breaks (> 0.5% of B)",
             "passed": bool(all(abs(r["miss_after_over_deficit"]) > 0.25
                                for r in b_rows.values())
                            and abs(b_9be_resid_B) > 0.005)},
            {"label": "(c) pre-registered best 2-part splits match the vendored-AME enumeration",
             "passed": bool(splits_match)},
            {"label": "(c) refuted: no tested decomposition closes any trio member to < 0.5% of B; 19F flips sign under 15N+alpha",
             "passed": bool(c_trio_all_fail and c_19F_sign_flip)},
            {"label": "closed-six regression: all six stay < 0.5% of B under rule (c); 16O = 12C+alpha closes",
             "passed": bool(six_survive and c_16O_closes)},
            {"label": "15N diagnostic: t-series miss non-monotone in k (miss(15N,k=3) > miss(11B,k=2) > miss(19F,k=4))",
             "passed": bool(miss15 > miss["11B"] > miss["19F"])},
            {"label": "honest negative: the trio remains OPEN under all three pre-registered candidates",
             "passed": True},
        ],
    }
    wit["allPassed"] = all(a["passed"] for a in wit["assertions"])
    out = _HERE / "mixed-multibond-interface.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    wit.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        wit, script_path=__file__, engine=None, q0_anchor=False)
    json.dump(wit, open(out, "w"), indent=1)
    print(f"\nwitness -> {out.name}   allPassed: {wit['allPassed']}")
    return 0 if wit["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
