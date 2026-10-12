#!/usr/bin/env python3
"""Route 2, option 1b (beans qou-99qc, qou-pzsi): ropelength with a same-loop-up-to-symmetry
rule, on fresh 13-letter words.

Implements preregistration-sameloop.md. No Q_beta / CODATA / mass input anywhere.

Same-loop rule (preregistration §2).  Work in the original coordinates of
Delta = Delta(2,4,5) = <s, u> (bring_route2_probe.delta245).  For each loop, the frame
matrix M of bring_loop_energy_probe.loop_setup puts the lifted axis on the imaginary axis
with the segment midpoint at i; so the axis in original coordinates is M^-1(imaginary
axis), its midpoint m = M^-1(i), and its endpoints x1, x2 = M^-1(0), M^-1(inf).

R(z) = -conj(z) acts on matrices as (a,b,c,d) -> (a,-b,-c,d); it fixes s up to sign and
sends u to u^-1 exactly, so Delta* = <Delta, R> = Delta u Delta R.  Two loops are one
loop iff some g in Delta*, with d(m2, g m1) <= L/2, maps {x1, x2} onto {y1, y2}.  The ball
is enumerated by breadth-first search over s, u, u^-1 (pruned at L/2 + SLACK, the same
pruning bring_loop_energy_probe.enumerate_kernel uses), once from m1 and once from R(m1).

Arithmetic: mpmath mpf at 30 dps; no float64.
"""
import itertools
import json
import sys
import time
from collections import Counter
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
import bring_route2_probe as R2  # noqa: E402
import bring_loop_energy_probe as E  # noqa: E402
import option1_ropelength_probe as O1  # noqa: E402

mp.mp.dps = 30
R2.mp.mp.dps = 30
DIGITS = 25
WORDLEN = 13
SLACK = mp.mpf(2)
MATCH = mp.mpf(10) ** -20
T0 = time.time()


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def act_ext(A, z):
    """Moebius action allowing z = inf (None) and returning None for inf."""
    a, b, c, d = A
    if z is None:
        return None if abs(c) < MATCH else a / c
    den = c * z + d
    if abs(den) < MATCH * (1 + abs(z)):
        return None
    return (a * z + b) / den


def refl(A):
    return (A[0], -A[1], -A[2], A[3])


def geometry(st):
    Mi = E.minv(st["M"])
    m = E.act(Mi, mp.mpc(0, 1))
    ends = (act_ext(Mi, mp.mpf(0)), act_ext(Mi, None))
    return m, ends


def same_point(z, w):
    if z is None or w is None:
        return z is None and w is None
    return abs(z - w) <= MATCH * (1 + abs(w))


def maps_axis(g, ends1, ends2):
    a, b = act_ext(g, ends1[0]), act_ext(g, ends1[1])
    return ((same_point(a, ends2[0]) and same_point(b, ends2[1]))
            or (same_point(a, ends2[1]) and same_point(b, ends2[0])))


def isometric(g1, g2, L, s, u):
    """Search g in Delta* with d(m2, g m1) <= L/2 mapping axis 1 onto axis 2."""
    m1, e1 = g1
    m2, e2 = g2
    cap = mp.cosh(L / 2 + SLACK)
    capL = mp.cosh(L / 2)
    ui = E.minv(u)
    gens = [s, u, ui]
    nseen = 0
    for orient, (p, ends) in (("+", (m1, e1)),
                              ("-", (-mp.conj(m1), tuple(None if x is None else -x for x in e1)))):
        seen = {E.key((1, 0, 0, 1))}
        frontier = [(1, 0, 0, 1)]
        if E.cosh_dist(m2, p) <= capL and maps_axis((1, 0, 0, 1), ends, e2):
            return orient, (1, 0, 0, 1), 1
        while frontier:
            nxt = []
            for h in frontier:
                for g in gens:
                    h2 = E.mmul(h, g)
                    cd = E.cosh_dist(m2, E.act(h2, p))
                    if cd > cap:
                        continue
                    kk = E.key(h2)
                    if kk in seen:
                        continue
                    seen.add(kk)
                    nxt.append(h2)
                    if cd <= capL and maps_axis(h2, ends, e2):
                        return orient, (h2 if orient == "+" else refl(h2)), nseen + len(seen)
            frontier = nxt
        nseen += len(seen)
    return None, None, nseen


def main():
    checks = {}
    classes = {}
    for w in itertools.product((0, 1), repeat=WORDLEN):
        classes.setdefault(O1.canon(w), []).append(w)
    checks["class_count_is_316"] = len(classes) == 316
    log(f"{len(classes)} classes of {WORDLEN}-letter words")
    s_mp, u_mp = R2.delta245()
    s, u = E.from_mp(s_mp), E.from_mp(u_mp)
    rho, sigmas = R2.s5_epimorphisms()
    checks["R_s_R_is_s_projectively"] = all(abs(x + y) < MATCH for x, y in zip(refl(s), s))
    checks["R_u_R_is_u_inverse"] = all(abs(x - y) < MATCH for x, y in zip(refl(u), E.minv(u)))

    ref = json.loads(Path(__file__).with_name("results.json").read_text())["rows"]
    for name in ("gluon_s1_s0", "nuc11_gen_grouped"):
        row = O1.route2_row(tuple(R2.CANDIDATES[name]))
        checks[f"reproduce_L_{name}"] = (mp.nstr(row["L"], DIGITS)
                                         == mp.nstr(mp.mpf(ref[name]["bring_length"]), DIGITS))

    rows = [O1.route2_row(c) for c in sorted(classes)]
    loops = sorted([r for r in rows if r["status"] == "loop"], key=lambda r: (r["L"], r["word"]))
    log(f"{len(loops)} loops, {len(rows) - len(loops)} without a loop")
    key = lambda v: mp.nstr(v, DIGITS)  # noqa: E731

    # ---- setup + geometry for every loop
    geo = {}
    for r in loops:
        st = E.loop_setup(r["word"], s_mp, u_mp, sigmas[0], rho, row=r)
        checks[f"loop_L_matches_{r['word']}"] = key(st["L"]) == key(r["L"])
        r["_st"] = st
        geo[r["word"]] = geometry(st)
    log("loop setup done")

    # ---- check 3: every loop isometric to itself
    self_ok = True
    for r in loops:
        o, g, _ = isometric(geo[r["word"]], geo[r["word"]], r["L"], s, u)
        self_ok &= o is not None
    checks["every_loop_isometric_to_itself"] = self_ok

    # ---- isometry classes, equal-L groups only (preregistration §2)
    iso = []  # list of lists of rows; first element is the lexicographically smallest word
    by_L = {}
    for r in loops:
        by_L.setdefault(key(r["L"]), []).append(r)
    for Lk, grp in by_L.items():
        grp = sorted(grp, key=lambda r: r["word"])
        reps = []
        for r in grp:
            placed = False
            for cl in reps:
                o, g, n = isometric(geo[cl[0]["word"]], geo[r["word"]], r["L"], s, u)
                if o is not None:
                    r["isometry"] = {"to": cl[0]["word"], "orientation": o}
                    cl.append(r)
                    placed = True
                    break
            if not placed:
                reps.append([r])
        iso.extend(reps)
        log(f"L={Lk[:12]}: {len(grp)} loops -> {len(reps)} isometry classes")
    iso.sort(key=lambda cl: (cl[0]["L"], cl[0]["word"]))

    # ---- tau once per isometry class, collar bound may skip
    best = None
    for cl in iso:
        r = cl[0]
        L = r["L"]
        lb = L / mp.asinh(6 * mp.pi / L)
        for x in cl:
            x["Lambda_lower_bound"] = lb
        if best is not None and lb > best * (1 + mp.mpf(10) ** -DIGITS):
            for x in cl:
                x["Lambda"] = "not enumerated: lower bound exceeds the computed minimum"
            log(f"class {r['word']} L={mp.nstr(L, 10)} skipped (bound {mp.nstr(lb, 8)})")
            continue
        th = O1.thickness(r["_st"])
        checks[f"radius_certified_{r['word']}"] = th["certified"]
        lam = mp.inf if (th["tau"] == 0 or not th["primitive"]) else L / th["tau"]
        for x in cl:
            x.update({k: v for k, v in th.items()})
            x["Lambda"] = lam
            x["tau_from"] = r["word"]
        if lam != mp.inf:
            best = lam if best is None else min(best, lam)
        log(f"class {r['word']} (size {len(cl)}) L={mp.nstr(L, 12)} tau={mp.nstr(th['tau'], 12)} "
            f"Lambda={mp.nstr(lam, 15)} |ker|={th['kernel_elements']}")

    # ---- check 5: tau invariance on a second member of the largest computed class
    computed = [cl for cl in iso if isinstance(cl[0].get("Lambda"), mp.mpf)]
    big = max(computed, key=lambda cl: (len(cl), -cl[0]["L"]))
    if len(big) >= 2:
        th2 = O1.thickness(big[1]["_st"])
        checks["tau_invariance_second_member"] = key(th2["tau"]) == key(big[0]["tau"])
        log(f"tau check {big[1]['word']}: {mp.nstr(th2['tau'], 15)} vs {mp.nstr(big[0]['tau'], 15)}")
    else:
        checks["tau_invariance_second_member"] = "no class with two members"

    # ---- pass test
    finite = [cl for cl in computed if cl[0]["Lambda"] != mp.inf]
    lam_min = min(cl[0]["Lambda"] for cl in finite)
    winners = [cl for cl in finite if key(cl[0]["Lambda"]) == key(lam_min)]
    lmin = iso[0][0]["L"]
    lwin = [cl for cl in iso if key(cl[0]["L"]) == key(lmin)]
    summary = {
        "classes": len(classes), "loops": len(loops), "no_loop": len(rows) - len(loops),
        "isometry_classes": len(iso),
        "isometry_class_sizes": sorted(Counter(len(cl) for cl in iso).items()),
        "Lambda_min": key(lam_min),
        "Lambda_minimiser_isometry_classes": [[x["word"] for x in cl] for cl in winners],
        "Lambda_PASS": len(winners) == 1,
        "Lambda_value_multiplicities_by_isometry_class":
            sorted(Counter(key(cl[0]["Lambda"]) for cl in finite).items(), key=lambda kv: mp.mpf(kv[0])),
        "L_min": key(lmin), "L_minimiser_isometry_classes": len(lwin), "L_PASS": len(lwin) == 1,
        "L_value_multiplicities_by_isometry_class":
            sorted(Counter(key(cl[0]["L"]) for cl in iso).items(), key=lambda kv: mp.mpf(kv[0])),
        "self_crossing_classes": [cl[0]["word"] for cl in computed if cl[0]["Lambda"] == mp.inf],
        "skipped_by_collar_bound": [cl[0]["word"] for cl in iso if isinstance(cl[0]["Lambda"], str)],
    }

    # ---- check 4 (post-hoc, not part of the verdict): regroup option 1 minimisers
    o1 = json.loads(Path(__file__).with_name("results_option1.json").read_text())
    o1rows = {r["word"]: r for r in o1["rows"]}
    mins = o1["summary"]["Lambda_minimisers"]
    o1_iso = []
    o1_geo = {}
    for w in mins:
        r = O1.route2_row(tuple(int(c) for c in w))
        st = E.loop_setup(w, s_mp, u_mp, sigmas[0], rho, row=r)
        o1_geo[w] = (geometry(st), r["L"])
    for w in mins:
        placed = False
        for cl in o1_iso:
            if key(o1_geo[cl[0]][1]) != key(o1_geo[w][1]):
                continue
            o, g, n = isometric(o1_geo[cl[0]][0], o1_geo[w][0], o1_geo[w][1], s, u)
            if o is not None:
                cl.append(w)
                placed = True
                break
        if not placed:
            o1_iso.append([w])
    posthoc = {"note": "POST-HOC, not part of the verdict (preregistration-sameloop.md §6.4)",
               "option1_minimisers": len(mins), "isometry_classes": [cl for cl in o1_iso],
               "option1_Lambda_min": o1["summary"]["Lambda_min"],
               "option1_rows_consistent": all(w in o1rows for w in mins)}
    log(f"post-hoc: option 1's {len(mins)} minimisers -> {len(o1_iso)} isometry classes")

    print(json.dumps(summary, indent=1, default=str))
    print(json.dumps(posthoc, indent=1, default=str))
    bad = [k for k, v in checks.items() if v is False]
    for k in bad:
        print("FAIL " + k)
    print("checks:", sum(1 for v in checks.values() if v is True), "/", len(checks), "pass")

    def ser(r):
        out = {}
        for k, v in r.items():
            if k.startswith("_"):
                continue
            out[k] = mp.nstr(v, DIGITS) if isinstance(v, mp.mpf) else v
        return out

    Path(__file__).with_name("results_sameloop.json").write_text(json.dumps(
        {"recipe": "preregistration-sameloop.md", "mp_dps": mp.mp.dps, "slack": str(SLACK),
         "summary": summary, "posthoc_option1": posthoc, "checks": checks,
         "isometry_classes": [[x["word"] for x in cl] for cl in iso],
         "rows": [ser(r) for r in rows]}, indent=1, default=str) + "\n")
    sys.exit(0 if not bad else 1)


if __name__ == "__main__":
    main()
