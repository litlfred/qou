#!/usr/bin/env python3
"""Clustering, per-class summary, ranking, calibration — per preregistration.md §4–6."""
import json, glob, os, math, itertools  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
import numpy as np  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
import ms_lib as S
L = S.L
TOL_E, TOL_SHAPE = 0.4, 0.05
PRIOR = {"nuc9": (234.50, 0.28, 234.55), "A": (291.15, 0.38, 291.17), "B": (295.90, 0.32, 295.84),
         "G": (None, None, 316.09)}

def load_npz(p):
    d = np.load(p); return [d[k] for k in sorted(d.files, key=lambda s: int(s.split("_")[1]))]

def topo_ok(r):
    return bool(r.get("start_certificate") and r.get("end_certificate") and r.get("fine_interpolant_certificate")
                and (r.get("lk_start") == r.get("lk_end")))

def parts(e):
    s = e["self"]
    if len(s) == 2:
        k = int(np.argmax(s)); return dict(E_knot=s[k], E_unknot=s[1 - k], E12=e["mutual"], total=e["total"])
    return dict(E_knot=s[0], total=e["total"])

def main():
    plan = {p["id"]: p for p in json.load(open("ms_plan.json"))}
    shape_cache = json.load(open("shape_cache.json")) if os.path.exists("shape_cache.json") else {}
    starts = {}
    for f in sorted(glob.glob("runs/*.json")):
        d = json.load(open(f)); sid = os.path.basename(f)[:-5]
        if sid.endswith("_p2"): continue
        rs = {r["N"]: r for r in d["runs"] if "E_M16N" in r}
        row = dict(id=sid, cls=d["spec"]["cls"], kind=d["spec"]["kind"], note=d["spec"].get("note", ""),
                   word=d.get("word"), strands=d.get("strands"), initial_total=d["initial"]["total"],
                   attempts=d.get("attempts"), errors=[r for r in d["runs"] if "error" in r],
                   runs={N: dict(E=r["E_M16N"]["total"], parts=parts(r["E_M16N"]), stop=r["stop"], it=r["iterations"],
                                 topo=topo_ok(r), quad=r["quad_diff"], res=r["fine_res_ratio"],
                                 rej=r["guard_rejects"]) for N, r in rs.items()})
        p2 = f"runs/{sid}_p2.json"
        if os.path.exists(p2):
            d2 = json.load(open(p2))
            for r in d2["runs"]:
                if "E_M16N" in r:
                    row["runs"][r["N"]] = dict(E=r["E_M16N"]["total"], parts=parts(r["E_M16N"]), stop=r["stop"],
                                               it=r["iterations"], topo=topo_ok(r), quad=r["quad_diff"],
                                               res=r["fine_res_ratio"], rej=r["guard_rejects"])
        if 256 in rs and os.path.exists(f"curves/{sid}_N256.npz") and row["runs"][256]["parts"].get("E12") is not None:
            if sid not in shape_cache:
                v, _ = S.shape_spectrum(load_npz(f"curves/{sid}_N256.npz"))
                shape_cache[sid] = [float(x) for x in v]  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
        starts[sid] = row
    json.dump(shape_cache, open("shape_cache.json", "w"))
    classes = {}
    for cls in ("nuc9", "A", "B", "G"):
        ids = sorted(s for s in starts if starts[s]["cls"] == cls)
        conv = [s for s in ids if 256 in starts[s]["runs"] and starts[s]["runs"][256]["topo"]
                and starts[s]["runs"][256]["stop"] == "converged"]
        # pairwise matrices
        dshape = {}
        for a, b in itertools.combinations(conv, 2):
            dshape[f"{a}|{b}"] = float(np.max(np.abs(np.array(shape_cache[a]) - np.array(shape_cache[b]))))  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
        def same(a, b):
            ra, rb = starts[a]["runs"][256], starts[b]["runs"][256]
            k = f"{a}|{b}" if f"{a}|{b}" in dshape else f"{b}|{a}"
            return (abs(ra["E"] - rb["E"]) <= TOL_E and abs(ra["parts"]["E12"] - rb["parts"]["E12"]) <= TOL_E
                    and dshape[k] <= TOL_SHAPE)
        # single linkage
        lab = {s: i for i, s in enumerate(conv)}
        changed = True
        while changed:
            changed = False
            for a, b in itertools.combinations(conv, 2):
                if lab[a] != lab[b] and same(a, b):
                    lo = min(lab[a], lab[b]); hi = max(lab[a], lab[b])
                    for s in lab:
                        if lab[s] == hi: lab[s] = lo
                    changed = True
        clusters = {}
        for s, l in lab.items(): clusters.setdefault(l, []).append(s)
        cl = sorted(clusters.values(), key=lambda m: min(starts[s]["runs"][256]["E"] for s in m))
        cl_info = []
        for m in cl:
            E = [starts[s]["runs"][256]["E"] for s in m]
            P = [starts[s]["runs"][256]["parts"] for s in m]
            cl_info.append(dict(members=sorted(m, key=lambda s: starts[s]["runs"][256]["E"]), E_min=min(E), E_max=max(E),
                                spread=max(E) - min(E), E12_mean=float(np.mean([p["E12"] for p in P])),  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
                                E_knot_mean=float(np.mean([p["E_knot"] for p in P])),  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
                                E_unknot_mean=float(np.mean([p["E_unknot"] for p in P]))))  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
        # all certified values (any stop) for the upper bound
        cert_vals = [(starts[s]["runs"][N]["E"], s, N) for s in ids for N in starts[s]["runs"]
                     if N >= 256 and starts[s]["runs"][N]["topo"] and starts[s]["runs"][N]["quad"] < 1e-6]
        UB = min(cert_vals) if cert_vals else None
        best = cl_info[0]["members"][0] if cl_info else None
        est = err = None; dN = None
        if best:
            rb = starts[best]["runs"]
            Nf = max(rb); est = rb[Nf]["E"]
            dN = abs(rb[512]["E"] - rb[256]["E"]) if 512 in rb else None
            err = max(dN if dN is not None else float("nan"), cl_info[0]["spread"]) + max(r["quad"] for r in rb.values())  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
        prior = PRIOR[cls]
        lowered = (UB is not None and prior[0] is not None and UB[0] < prior[0] - prior[1])
        # conjugate-word test: min E per word (braid starts)
        perword = {}
        for s in ids:
            st = starts[s]
            if 256 in st["runs"] and st["runs"][256]["topo"]:
                key = st["note"].split(":")[0] if st["kind"] != "braid" else (str(st["word"]) + f"/n={st['strands']}")
                perword.setdefault(key, []).append((st["runs"][256]["E"], s))
        classes[cls] = dict(ids=ids, converged_at_256=conv, unconverged=[s for s in ids if s not in conv],
                            clusters=cl_info, n_distinct_minima=len(cl_info), dshape=dshape,
                            upper_bound=dict(E=UB[0], start=UB[1], N=UB[2]) if UB else None,
                            best_start=best, estimate=est, err=err, dE_512_256=dN,
                            prior_Einf=prior[0], prior_err=prior[1], prior_UB=prior[2],
                            lowered_beyond_prior_error=lowered,
                            lowered_prior_UB=(UB is not None and UB[0] < prior[2]),
                            per_word_min={k: min(v) for k, v in perword.items()})
    # ranking / separation
    names = [c for c in classes if classes[c]["estimate"] is not None]
    rank = sorted(names, key=lambda c: classes[c]["estimate"])
    sep = {}
    for a, b in itertools.combinations(rank, 2):
        A, B = classes[a], classes[b]
        gap = B["estimate"] - A["estimate"]; tol = A["err"] + B["err"]
        sep[f"{a} < {b}"] = dict(gap=gap, combined_err=tol, separated=bool(gap > tol))
    # calibration
    cal = {s: starts[s] for s in starts if starts[s]["cls"] in ("hopf", "trefoil")}
    json.dump(dict(starts=starts, classes=classes, ranking=rank, separation=sep, calibration=cal,
                   tolerances=dict(E=TOL_E, shape=TOL_SHAPE)), open("results.json", "w"), indent=1, default=str)
    for s in sorted(cal):
        print(s, {N: (round(v["E"], 5), v["parts"], v["stop"], v["topo"]) for N, v in cal[s]["runs"].items()})
    for c in classes:
        k = classes[c]
        print(f"\n== {c}: UB={k['upper_bound']} est={k['estimate']} err={k['err']} dN={k['dE_512_256']} "
              f"minima={k['n_distinct_minima']} lowered={k['lowered_beyond_prior_error']} unconv={k['unconverged']}")
        for i, m in enumerate(k["clusters"]):
            print(f"   cluster {i}: E {m['E_min']:.3f}-{m['E_max']:.3f} E12~{m['E12_mean']:.2f} Ek~{m['E_knot_mean']:.2f} Eu~{m['E_unknot_mean']:.2f} {m['members']}")
        for s in k["ids"]:
            st = starts[s]
            print("   ", s, f"init={st['initial_total']:.1f}", " ".join(f"N{N}:{v['E']:.3f}/{v['stop'][:5]}/{'ok' if v['topo'] else 'TOPO?'}" for N, v in sorted(st["runs"].items())), st["errors"] and "ERR")
    print("\nranking", rank)
    for k, v in sep.items(): print(k, v)

if __name__ == "__main__":
    main()
