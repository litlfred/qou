#!/usr/bin/env python3
"""Run one start of the multi-start plan (ms_plan.json). Usage: ms_run.py START_ID
Flow, guard, certificates and evaluator are ohara_lib's, unchanged."""
import sys, json, time
import numpy as np  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
import ms_lib as S
L = S.L

def load_npz(p):
    d = np.load(p); return [d[k] for k in sorted(d.files, key=lambda s: int(s.split("_")[1]))]

def energy(X, mult):
    e = L.link_energy_spectral([L.fourier_resample(c, mult * len(c)) for c in X])
    return dict(self=[float(x) for x in e["self"]], mutual=None if e["mutual"] is None else float(e["mutual"]),  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
                total=float(e["total"]))  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities

def main():
    sid = sys.argv[1]
    plan = {p["id"]: p for p in json.load(open("ms_plan.json"))}
    p = plan[sid]
    cls = p["cls"]
    certify = S.make_certify(cls)
    lkT = S.lk_target(cls)
    out = dict(spec=p, runs=[])
    t0 = time.time()
    if p["kind"] == "braid":
        w, n = S.W.REPS[cls][p["word"]] if p["word"] in S.W.REPS[cls] else (p["word_list"], p["strands"])
        warp = S.random_warp(p["warp_seed"], total=p.get("warp_amp", 0.6)) if p.get("warp_seed") is not None else None  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
        dense = S.braid_curves_var(w, n, 4096, R=p["R_over_a"], a=1.0, zamp=p.get("zamp", 1.0), warp=warp)
        out.update(word=w, strands=n, warp=warp)
        out["initial"] = energy(dense, 1)
    else:
        src = load_npz(p["source"])
        base = [L.fourier_resample(c, 16 * len(c)) for c in src]
        if p["kind"] == "mobius":
            dense = S.mobius_image(base, p["seed"]); out["attempts"] = 1
        elif p["kind"] == "perturb":
            for att in range(1, 31):
                dense = S.perturb(base, p["eps"], p["seed"] * 100 + att)
                Pt = [L.resample_equal_arclength(c, p["schedule"][0][0]) for c in dense]
                ok = certify(Pt) and (len(Pt) == 1 or abs(L.linking_number(*Pt)) == lkT)
                if ok and L.guard_distances(Pt)[0] > 0: break
            out["attempts"] = att
        elif p["kind"] == "continue":
            dense = base
        out["initial"] = energy(dense, 1)
    print(sid, "initial", out["initial"], flush=True)
    X = None
    for N, cap, tol in p["schedule"]:
        t1 = time.time()
        srcc = dense if X is None else [L.fourier_resample(c, 16 * len(c)) for c in X]
        P = [L.resample_equal_arclength(c, N) for c in srcc]
        cert0 = certify(P)
        lk0 = L.linking_number(P[0], P[1]) if len(P) == 2 else None
        if not cert0 or (lk0 is not None and abs(lk0) != lkT):
            out["runs"].append(dict(N=N, error="start certificate failed", lk=lk0)); print("  start cert FAILED", N, flush=True); break
        fl = L.LinkFlow(P, lk0 if lk0 is not None else 0, certify=certify)
        r = fl.run(cap, rel_tol=tol)
        X = fl.X
        cert1 = certify(X)
        lk1 = L.linking_number(X[0], X[1]) if len(X) == 2 else None
        fine = [L.fourier_resample(c, 8 * N) for c in X]
        cert_fine = certify(fine) and (len(fine) == 1 or L.linking_number(fine[0], fine[1]) == lk0)
        _, dres_f = L.guard_distances(fine)
        e8, e16 = energy(X, 8), energy(X, 16)
        Ep = fl.E_poly(X)
        rr = dict(N=N, cap=cap, tol=tol, stop=r["stop"], iterations=r["iterations"], accepted=r["accepted"],
                  guard_rejects=r["guard_rejects"], balances=r["balances"],
                  start_certificate=bool(cert0), end_certificate=bool(cert1), fine_interpolant_certificate=bool(cert_fine),
                  lk_start=lk0, lk_end=lk1, dmin=r["dmin"], res_ratio=r["dres"], fine_res_ratio=float(dres_f),  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
                  E_poly_end=float(Ep[2]), E_M8N=e8, E_M16N=e16, quad_diff=abs(e8["total"] - e16["total"]),  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
                  history=r["history"][::5] + [r["history"][-1]], seconds=time.time() - t1)
        out["runs"].append(rr)
        np.savez(f"curves/{sid}_N{N}.npz", *X)
        print(f"  N={N} stop={r['stop']} it={r['iterations']} E={e16['total']:.4f} parts={[round(x,3) for x in e16['self']]},{e16['mutual']} "
              f"quad={rr['quad_diff']:.1e} cert={cert0},{cert1},{cert_fine} lk={lk0},{lk1} rej={r['guard_rejects']} t={rr['seconds']:.0f}s", flush=True)
        json.dump(out, open(f"runs/{sid}.json", "w"), indent=1)
    out["seconds"] = time.time() - t0
    json.dump(out, open(f"runs/{sid}.json", "w"), indent=1)

if __name__ == "__main__":
    main()
