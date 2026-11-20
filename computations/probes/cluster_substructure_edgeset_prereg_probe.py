#!/usr/bin/env python3
"""cluster_substructure_edgeset_prereg_probe.py — FRONT 3, bean `qou-52x7`.

Is the light-isotope binding residual CLUSTER structure rather than body order?

PRE-REGISTERED at docs/audits/2026-08-26-cluster-substructure-prereg.md,
committed at 843391340b7511f131fcd8342f1e1ea1e925384b and pushed BEFORE this
file was written. Read it first: it fixes the quantity, the corpus source, the
numeric support/refutation criteria, and the INTEGER count of schemes tried
(TWO cluster schemes x TWO edge rules = FOUR evaluations, no fifth).

WHAT IS UNDER TEST (scope, per the pre-registration)
-----------------------------------------------------
Cluster structure implemented as an EDGE-SET RESTRICTION on the existing
pairwise family: same derived alpha, same derived L_pp/L_pn/L_nn, only the set
of bonds changes with the cluster decomposition. Cluster structure implemented
as a NEW MANY-BODY TERM (an irreducibly >=3-body alpha term, the SU(4) [1^4]
volume term, connected-sum volume additivity) is a DIFFERENT hypothesis with a
different arity and is NOT tested here.

  H_all     -- clustering explains THE residual, both directions.
  H_partial -- clustering explains only the A >= 6 over-binding.

S-C1, the pre-registered structural claim, checked not assumed:
  every cluster edge set E is a SUBGRAPH of K_A, so if all three per-bond
  energies are strictly positive then B_E <= B_{K_A} and r_E = B_AME/B_E
  >= r_{K_A} pointwise; a single-cluster nucleus has E = K_A exactly and its
  ratio CANNOT MOVE.

NO FLOAT64. Everything is mpmath.mpf at >= 60 dps. The production accessor
`mass_binding_dashboard._bond_type_L` returns `float` (it casts at the return),
so it is NOT used for arithmetic; the identical expression is re-formed in mpf
here and cross-checked against the production floats ONLY to the float64 limit,
which is reported as such and never as "exact".

Run:  PYTHONPATH=computations:computations/substrate \
      python3 -u computations/probes/cluster_substructure_edgeset_prereg_probe.py \
        2>&1 | tee /tmp/cluster_substructure.log

EXPLORATORY -- audit-only witness; no production wiring; no fitted constant.
Audit: docs/audits/2026-08-26-cluster-substructure-verdict.md
"""
from __future__ import annotations

import json
import sys
from itertools import combinations
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (_COMP, _COMP / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

DPS = 60
mp.mp.dps = DPS

# ---------------------------------------------------------------- constants


def derived_constants():
    """alpha = E0 = m_e/(q0(q0-1)) and the three per-bond L, all in mpf.

    Reproduces `mass_binding_dashboard._constants` and `._bond_type_L` exactly,
    minus their float() casts. Convention D, proton pin, colour-weighted,
    writhe-normalised.
    """
    from q_parameter import Q_50_DIGIT_STR as Q50
    from codata_constants import M_E_MEV
    from _li_2_q_util import flavor_split_leading

    with mp.workdps(DPS):
        q0 = mp.mpf(str(Q50))
        me = mp.mpf(str(M_E_MEV))
        import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
        alpha = _qbeta_e0.order_zero_scaled(me, q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)

        h = q0 - 1 / q0
        z = q0 ** 3 / (q0 ** 2 + 1)                    # convention D
        delta = flavor_split_leading(q0)
        t = mp.mpf(1) / 2 - delta / 4                  # colour weight
        d = {"pp": mp.mpf(0), "pn": -h * t, "nn": -h}
        de = {"pp": mp.mpf(1), "nn": mp.mpf(-1), "pn": 2 * t - 1}
        lw = mp.log(1 - h)
        L = {k: -mp.log(z + v) - de[k] / 2 * lw for k, v in d.items()}
    return alpha, q0, me, L


# ------------------------------------------------------- isotopes + schemes

# (name, Z, N) -- FIXED in the pre-registration, six nuclides. No additions.
ISOTOPES = [
    ("2H", 1, 1),
    ("3H", 1, 2),
    ("3He", 2, 1),
    ("4He", 2, 2),
    ("6Li", 3, 3),
    ("7Li", 3, 4),
]

# Cluster schemes -- TWO, fixed in the pre-registration. Each maps (Z,N) to a
# list of clusters, a cluster being a (z, n) pair.
SCHEMES = {
    # C1 maximal-alpha (standard cluster model): d, t, h, alpha, alpha+d, alpha+t
    "C1": {
        (1, 1): [(1, 1)],                     # 2H  = d
        (1, 2): [(1, 2)],                     # 3H  = t
        (2, 1): [(2, 1)],                     # 3He = h
        (2, 2): [(2, 2)],                     # 4He = alpha
        (3, 3): [(2, 2), (1, 1)],             # 6Li = alpha + d
        (3, 4): [(2, 2), (1, 2)],             # 7Li = alpha + t
    },
    # C2 alpha-plus-free-nucleons: only a FILLED [1^4] is a cluster.
    "C2": {
        (1, 1): [(1, 0), (0, 1)],
        (1, 2): [(1, 0), (0, 1), (0, 1)],
        (2, 1): [(1, 0), (1, 0), (0, 1)],
        (2, 2): [(2, 2)],
        (3, 3): [(2, 2), (1, 0), (0, 1)],
        (3, 4): [(2, 2), (1, 0), (0, 1), (0, 1)],
    },
}


def _pair_counts(z, n):
    """(n_pp, n_pn, n_nn) for the complete graph on z protons + n neutrons."""
    return (z * (z - 1) // 2, z * n, n * (n - 1) // 2)


def edges_KA(clusters):
    """K_A -- the complete graph on ALL nucleons, ignoring the decomposition."""
    Z = sum(c[0] for c in clusters)
    N = sum(c[1] for c in clusters)
    return _pair_counts(Z, N)


def edges_E1(clusters):
    """E1 -- intra-cluster complete graphs, NO inter-cluster edge."""
    pp = pn = nn = 0
    for z, n in clusters:
        a, b, c = _pair_counts(z, n)
        pp += a
        pn += b
        nn += c
    return (pp, pn, nn)


def edges_E2(clusters, best_type):
    """E2 -- E1 plus one inter-cluster bond per cluster pair, of the type that
    MAXIMISES B (deliberately the most favourable inter-cluster assignment, so
    a refutation under E2 refutes every inter-cluster bond assignment)."""
    pp, pn, nn = edges_E1(clusters)
    k = len(clusters)
    extra = k * (k - 1) // 2
    add = {"pp": [extra, 0, 0], "pn": [0, extra, 0], "nn": [0, 0, extra]}[best_type]
    return (pp + add[0], pn + add[1], nn + add[2])


def edges_chain(clusters):
    """The linear-chain minimum edge set (A-1 bonds, ordering p^Z n^N) -- the
    corpus's B_sym edge count. Used ONLY for refutation criterion R-iii."""
    Z = sum(c[0] for c in clusters)
    N = sum(c[1] for c in clusters)
    # word p...p n...n : (Z-1) pp bonds, 1 pn bond, (N-1) nn bonds
    return (max(Z - 1, 0), 1 if (Z and N) else 0, max(N - 1, 0))


def B_of(counts, alpha, L):
    pp, pn, nn = counts
    return alpha * (pp * L["pp"] + pn * L["pn"] + nn * L["nn"])


# ------------------------------------------------------------------- report


def main():
    alpha, q0, me, L = derived_constants()

    from codata_constants import ame_binding_mev

    ns = lambda x, d=6: mp.nstr(x, d)  # noqa: E731  -- display only

    print("=" * 78)
    print("FRONT 3 -- cluster substructure as an EDGE-SET restriction")
    print("pre-registration: docs/audits/2026-08-26-cluster-substructure-prereg.md")
    print("                  committed 843391340b7511f131fcd8342f1e1ea1e925384b")
    print("=" * 78)
    print(f"\ndps = {mp.mp.dps}   q0 = {ns(q0, 20)} (proton pin)")
    print(f"m_e = {ns(me, 12)} MeV     alpha = E0 = {ns(alpha, 12)} MeV")
    print("\nper-bond L (convention D, colour-weighted, writhe-normalised, mpf):")
    for k in ("pp", "pn", "nn"):
        print(f"   L_{k} = {ns(L[k], 15)}     alpha*L_{k} = {ns(alpha * L[k], 12)} MeV")

    # --- S-C1 premise check: are all three bond energies strictly positive? ---
    signs = {k: (alpha * L[k] > 0) for k in L}
    positive = all(signs.values())
    print("\n-- S-C1 premise: all three per-bond energies strictly positive?")
    for k in ("pp", "pn", "nn"):
        print(f"     alpha*L_{k} > 0 : {signs[k]}")
    print(f"   => S-C1 premise {'HOLDS' if positive else 'FAILS -- S-C1 RETRACTED'}")

    best_type = max(("pp", "pn", "nn"), key=lambda k: L[k])
    print(f"\n-- E2 inter-cluster bond type (B-maximising) = {best_type}"
          f"   (alpha*L = {ns(alpha * L[best_type], 10)} MeV)")

    # --- float64 cross-check against the production accessor, to its limit ---
    xcheck = None
    try:
        import mass_binding_dashboard as mbd
        prod = mbd._bond_type_L()          # returns float -- display only
        # repr() as a STRING, never a JSON float: the whole point of this
        # block is to record what the float64 production path returns, and
        # writing it as a JSON number would put raw float64 INTO the witness
        # (raw-float64 ratchet). repr() is lossless for a binary64.
        xcheck = {k: {"prod_float64_repr": repr(prod[k]), "mpf": mp.nstr(L[k], 20),
                      "abs_diff": mp.nstr(abs(mp.mpf(repr(prod[k])) - L[k]), 4)}
                  for k in ("pp", "pn", "nn")}
        print("\n-- cross-check vs production `_bond_type_L` (which returns float):")
        for k in ("pp", "pn", "nn"):
            print(f"     {k}: prod(f64)={prod[k]!r}  mpf={mp.nstr(L[k], 20)}"
                  f"  |diff|={xcheck[k]['abs_diff']}")
        print("     agreement is at the limit of the float64 the production path"
              "\n     returns; this does NOT establish agreement beyond ~1e-16.")
    except Exception as exc:                                  # pragma: no cover
        print(f"\n-- cross-check skipped: {exc}")

    rows = []
    print("\n" + "=" * 78)
    print("THE FOUR PRE-REGISTERED EVALUATIONS (+ the K_A baseline, recomputed)")
    print("=" * 78)
    hdr = (f"\n{'iso':>5} {'A':>2} {'k':>2} | {'edges':>12} | "
           f"{'B_model':>10} | {'B_AME':>10} | {'r=AME/mod':>10} | {'|r-1|':>7}")

    for scheme in ("C1", "C2"):
        for rule in ("KA", "E1", "E2"):
            label = "K_A baseline" if rule == "KA" else f"{scheme} + {rule}"
            if rule == "KA" and scheme == "C2":
                continue          # K_A does not depend on the scheme
            print(f"\n--- {label} ---")
            print(hdr)
            for name, Z, N in ISOTOPES:
                clusters = SCHEMES[scheme][(Z, N)]
                A = Z + N
                if rule == "KA":
                    cnt = edges_KA(clusters)
                elif rule == "E1":
                    cnt = edges_E1(clusters)
                else:
                    cnt = edges_E2(clusters, best_type)
                Bm = B_of(cnt, alpha, L)
                Ba = ame_binding_mev(Z, A)
                if Bm == 0:
                    r = mp.inf
                    dev = mp.inf
                else:
                    r = Ba / Bm
                    dev = abs(r - 1)
                nchain = sum(edges_chain(clusters))
                rows.append({
                    "scheme": scheme, "rule": rule, "iso": name, "Z": Z, "N": N,
                    "A": A, "n_clusters": len(clusters),
                    "n_pp": cnt[0], "n_pn": cnt[1], "n_nn": cnt[2],
                    "n_edges": sum(cnt), "n_edges_chain": nchain,
                    "single_cluster": len(clusters) == 1,
                    "B_model_mev": mp.nstr(Bm, 18),
                    "B_ame_mev": mp.nstr(Ba, 18),
                    "ratio_ame_over_model": ("inf" if Bm == 0 else mp.nstr(r, 18)),
                    "abs_ratio_minus_1": ("inf" if Bm == 0 else mp.nstr(dev, 12)),
                })
                estr = f"{cnt[0]}pp {cnt[1]}pn {cnt[2]}nn"
                rs = "  inf   " if Bm == 0 else f"{ns(r, 6):>10}"
                ds = "  inf  " if Bm == 0 else f"{ns(dev, 4):>7}"
                print(f"{name:>5} {A:>2} {len(clusters):>2} | {estr:>12} | "
                      f"{ns(Bm, 7):>10} | {ns(Ba, 7):>10} | {rs} | {ds}")

    # ------------------------------------------------------------- verdicts
    def get(scheme, rule, iso):
        for r in rows:
            if r["scheme"] == scheme and r["rule"] == rule and r["iso"] == iso:
                return r
        raise KeyError((scheme, rule, iso))

    def ratio(row):
        return None if row["ratio_ame_over_model"] == "inf" else mp.mpf(
            row["ratio_ame_over_model"])

    print("\n" + "=" * 78)
    print("PRE-REGISTERED VERDICTS")
    print("=" * 78)

    verdicts = {}

    # S-C1 (i): single-cluster nuclei must have r unchanged from K_A.
    sc1_ok, sc1_detail = positive, []
    for scheme in ("C1", "C2"):
        for name, Z, N in ISOTOPES:
            base = get("C1", "KA", name)
            for rule in ("E1", "E2"):
                row = get(scheme, rule, name)
                if row["single_cluster"]:
                    same = (row["ratio_ame_over_model"]
                            == base["ratio_ame_over_model"]) if rule == "E1" else None
                    if rule == "E1" and not same:
                        sc1_ok = False
                    if rule == "E1":
                        sc1_detail.append(
                            {"scheme": scheme, "iso": name,
                             "r_KA": base["ratio_ame_over_model"],
                             "r_E1": row["ratio_ame_over_model"],
                             "unchanged": bool(same)})
    print(f"\nS-C1 (subgraph monotonicity): "
          f"{'CONFIRMED' if sc1_ok else 'FALSIFIED -- RETRACTED'}")
    for d in sc1_detail:
        if d["scheme"] == "C1":
            print(f"   {d['scheme']} {d['iso']:>4} single-cluster: "
                  f"r unchanged = {d['unchanged']}")
    verdicts["S_C1"] = {"confirmed": bool(sc1_ok),
                        "premise_all_bond_energies_positive": bool(positive),
                        "single_cluster_ratios": sc1_detail}

    # S-C1 (ii): r_E >= r_KA pointwise. Reported SPLIT BY RULE, because only
    # E1 is a faithful typed subgraph of K_A. E2 assigns the B-MAXIMISING type
    # to every inter-cluster bond (pre-registered as the most favourable
    # choice), which RE-TYPES pairs -- e.g. under C2 the 2H p-n pair becomes an
    # inter-cluster bond typed nn, and alpha*L_nn > alpha*L_pn -- so E2 is an
    # UPPER BOUND on B for any inter-cluster typing, NOT a subgraph. The
    # subgraph invariant therefore constrains E1 only, and that is what S-C1
    # actually licenses.
    mono_by_rule = {}
    for rule in ("E1", "E2"):
        ok, viol = True, []
        for scheme in ("C1", "C2"):
            for name, Z, N in ISOTOPES:
                rk = ratio(get("C1", "KA", name))
                re_ = ratio(get(scheme, rule, name))
                if re_ is not None and re_ < rk:
                    ok = False
                    viol.append({"scheme": scheme, "iso": name,
                                 "r_KA": mp.nstr(rk, 10), "r_E": mp.nstr(re_, 10)})
        mono_by_rule[rule] = {"holds": bool(ok), "violations": viol}
        print(f"S-C1 (ii) r_E >= r_KA pointwise, rule {rule}: {ok}"
              + ("" if ok else f"   violations: "
                 f"{[(v['scheme'], v['iso']) for v in viol]}"))
    print("   E1 is the faithful typed subgraph; E2 re-types inter-cluster bonds")
    print("   to the B-maximising type, so E2 bounds B ABOVE and r BELOW.")
    verdicts["S_C1_ii_pointwise_monotone_by_rule"] = mono_by_rule

    # E2 as a LOWER BOUND on r: is the cluster edge set still too WEAK at
    # 6Li/7Li even with the most favourable inter-cluster typing?
    print("\n-- E2 gives a LOWER bound on r for any inter-cluster typing:")
    lower = {}
    for scheme in ("C1", "C2"):
        for iso in ("6Li", "7Li"):
            rr = ratio(get(scheme, "E2", iso))
            lower[f"{scheme}:{iso}"] = mp.nstr(rr, 12)
            print(f"     {scheme} {iso:>4}: r >= {ns(rr, 6)}"
                  f"   ({'model still TOO WEAK' if rr > 1 else 'model too strong'})")
    verdicts["E2_lower_bound_on_r"] = lower

    # R-ii: is 4He's ratio unchanged across EVERY declared pair?
    r_he_ka = get("C1", "KA", "4He")["ratio_ame_over_model"]
    he_unchanged = all(
        get(s, ru, "4He")["ratio_ame_over_model"] == r_he_ka
        for s in ("C1", "C2") for ru in ("E1", "E2"))
    print(f"\nR-ii  4He ratio unchanged across all 4 evaluations: {he_unchanged}"
          f"   (r = {r_he_ka[:8]})")
    print(f"      => H_all {'REFUTED (R-ii fires)' if he_unchanged else 'not refuted by R-ii'}")
    verdicts["R_ii_he4_immovable"] = bool(he_unchanged)
    verdicts["H_all"] = "REFUTED" if he_unchanged else "NOT_REFUTED_BY_R_ii"

    # S-i / R-i on 6Li + 7Li.
    print("\nS-i / R-i  (6Li and 7Li, zero new constants):")
    s_i = False
    r_i = True
    per_pair = {}
    for scheme in ("C1", "C2"):
        for rule in ("E1", "E2"):
            devs = {}
            for iso in ("6Li", "7Li"):
                row = get(scheme, rule, iso)
                d = (None if row["abs_ratio_minus_1"] == "inf"
                     else mp.mpf(row["abs_ratio_minus_1"]))
                devs[iso] = d
            worst = None if any(v is None for v in devs.values()) else max(devs.values())
            per_pair[f"{scheme}+{rule}"] = (
                "inf" if worst is None else mp.nstr(worst, 8))
            if worst is not None and worst <= mp.mpf("0.10"):
                s_i = True
            if worst is not None and worst <= mp.mpf("0.25"):
                r_i = False
            ws = "inf" if worst is None else ns(worst, 5)
            print(f"   {scheme}+{rule}: max|r-1| over (6Li,7Li) = {ws:>10}"
                  f"   [<=0.10 support | <=0.25 avoids R-i]")
    print(f"   S-i (<=0.10 on both, some pair): {s_i}")
    print(f"   R-i (NO pair within 0.25):       {r_i}")
    verdicts["S_i"] = bool(s_i)
    verdicts["R_i"] = bool(r_i)
    verdicts["per_pair_worst_dev_6Li_7Li"] = per_pair

    # S-ii: does the supporting pair degrade the other four?
    print("\nS-ii  (does a pair degrade {2H,3H,3He,4He} vs K_A baseline?)")
    s_ii = {}
    base_worst = max(mp.mpf(get("C1", "KA", i)["abs_ratio_minus_1"])
                     for i in ("2H", "3H", "3He", "4He"))
    for scheme in ("C1", "C2"):
        for rule in ("E1", "E2"):
            vals = [get(scheme, rule, i)["abs_ratio_minus_1"]
                    for i in ("2H", "3H", "3He", "4He")]
            w = ("inf" if "inf" in vals
                 else mp.nstr(max(mp.mpf(v) for v in vals), 8))
            ok = (w != "inf") and mp.mpf(w) <= base_worst
            s_ii[f"{scheme}+{rule}"] = {"worst": w, "no_worse_than_KA": bool(ok)}
            print(f"   {scheme}+{rule}: worst |r-1| = {w:>12}   "
                  f"(K_A baseline {ns(base_worst, 5)})  no worse: {ok}")
    verdicts["S_ii"] = s_ii
    verdicts["KA_baseline_worst_dev_light4"] = mp.nstr(base_worst, 8)

    # R-iii: cluster edge set must sit between chain and K_A.
    print("\nR-iii  (cluster edge set between chain and K_A?)")
    r_iii = {}
    for scheme in ("C1", "C2"):
        for rule in ("E1", "E2"):
            bad = []
            for name, Z, N in ISOTOPES:
                row = get(scheme, rule, name)
                ka = sum(edges_KA(SCHEMES[scheme][(Z, N)]))
                if not (row["n_edges_chain"] <= row["n_edges"] <= ka):
                    bad.append({"iso": name, "n_edges": row["n_edges"],
                                "n_chain": row["n_edges_chain"], "n_KA": ka})
            r_iii[f"{scheme}+{rule}"] = bad
            print(f"   {scheme}+{rule}: below-chain isotopes = "
                  f"{[b['iso'] for b in bad] or 'none'}")
    verdicts["R_iii_below_chain"] = r_iii

    verdicts["H_partial"] = (
        "SUPPORTED" if (s_i and not r_i) else
        ("REFUTED" if r_i else "NEITHER_SUPPORTED_NOR_REFUTED"))
    print(f"\nH_partial: {verdicts['H_partial']}")
    print(f"H_all:     {verdicts['H_all']}")

    # -------------------------------------------------------------- witness
    from q_parameter import Q_50_DIGIT_STR as _Q50_PROTON
    out = {
        # q₀-anchor stamp (added 2026-08-26). `inputs.q0_proton_pin` below
        # records the pin in a field NAME, which `q0_anchor_consistency_audit`
        # does not read; without these two keys the witness sat in
        # Q0_ANCHOR_MISSING, indistinguishable from a producer that forgot.
        # They belong at the document ROOT — the audit reads the top level, so
        # nesting them under "witness" leaves the verdict unchanged (measured:
        # still Q0_ANCHOR_MISSING on the first attempt at this fix).
        "q0Anchor": "proton",
        "q0Value": _Q50_PROTON,
        "witness": {
            "schema": "qou-probe/v1",
            "kind": "exploratory-probe",
            "prereg": "docs/audits/2026-08-26-cluster-substructure-prereg.md",
            "prereg_commit": "843391340b7511f131fcd8342f1e1ea1e925384b",
            "bean": "qou-52x7",
            "precision_dps": DPS,
            "float64_used_in_arithmetic": False,
        },
        "inputs": {
            "q0_proton_pin": mp.nstr(q0, 50),
            "m_e_mev": mp.nstr(me, 20),
            "alpha_E0_mev": mp.nstr(alpha, 30),
            "L": {k: mp.nstr(L[k], 30) for k in L},
            "alpha_L_mev": {k: mp.nstr(alpha * L[k], 30) for k in L},
            "convention": "D (z = q^3/(q^2+1)), colour-weighted, writhe-normalised",
            "E2_inter_cluster_bond_type": best_type,
            "production_float64_crosscheck": xcheck,
        },
        "schemes": {s: {f"{z},{n}": v for (z, n), v in SCHEMES[s].items()}
                    for s in SCHEMES},
        "rows": rows,
        "verdicts": verdicts,
    }
    wp = _COMP / "probes" / "cluster-substructure-edgeset.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    out.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        out, script_path=__file__, engine=None, q0_anchor=None)
    wp.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\nwitness -> {wp}")


if __name__ == "__main__":
    main()
