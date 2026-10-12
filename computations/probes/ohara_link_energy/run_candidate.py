#!/usr/bin/env python3
"""Flow one candidate per preregistration.md. Usage: run_candidate.py NAME [R_over_a] [Ns] [caps]"""
import sys, json, time
import numpy as np  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
import ohara_lib as L

NUC9 = [0, 1] * 3 + [0, 0, 1]
WORDS = {
    "cal_hopf_s1^2": ([0, 0], 2), "cal_hopf_3strand": ([0, 0, 1], 3),
    "cal_T24_s1^4": ([0, 0, 0, 0], 2), "cal_trefoil_s1^3": ([0, 0, 0], 2),
    "nuc9": (NUC9, 3), "nuc11_interleaved": (NUC9 + [0, 0], 3),
    "nuc11_gen_grouped": ([0] * 7 + [1] * 4, 3),
    "gluon_s1_s0": (NUC9 + [1, 0], 3), "gluon_s0_s1": (NUC9 + [0, 1], 3),
    "gluon_s1_s1": (NUC9 + [1, 1], 3),
}
KNOT_ALEX = {0: "1", 2: "1", 1: "1", 3: "t**2 - t + 1", 5: "t**4 - t**3 + t**2 - t + 1",
             7: "t**6 - t**5 + t**4 - t**3 + t**2 - t + 1"}

def main():
    name = sys.argv[1]
    Roa = float(sys.argv[2]) if len(sys.argv) > 2 else 3.0  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
    Ns = [int(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3 else [64, 128, 256]
    caps = [int(x) for x in sys.argv[4].split(",")] if len(sys.argv) > 4 else [6000, 4000, 3000]
    tag = sys.argv[5] if len(sys.argv) > 5 else ""
    w, n = WORDS[name]
    bt = json.load(open("braid_topology.json"))[name]
    comps = L.braid_components(w, n)
    out = dict(name=name, word=w, strands=n, R_over_a=Roa, components=len(comps),
               strands_per_component=[len(c) for c in comps],
               linking_number_braid=bt["linking_number"], self_writhe=bt["self_crossing_writhe"])
    # initial energy, spectral, two resolutions
    init = {}
    for M in (2048, 4096):
        curves = L.closed_braid_curves(w, n, M, R=Roa, a=1.0)
        init[M] = L.link_energy_spectral(curves)
    out["initial"] = {str(k): dict(self=[float(x) for x in v["self"]],  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
                                   mutual=None if v["mutual"] is None else float(v["mutual"]),  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
                                   total=float(v["total"])) for k, v in init.items()}  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
    print(name, "initial", out["initial"]["4096"], flush=True)
    dense = L.closed_braid_curves(w, n, 4096, R=Roa, a=1.0)
    # references for certificates
    ref_link = L.alexander_from_poly(bt["alexander_t"])
    ref_comp = [L.alexander_from_poly(KNOT_ALEX[sw]) for sw in bt["self_crossing_writhe"]]
    # component order in braid_topology matches L.braid_components (same algorithm)
    def certify(curves):
        if len(curves) == 2:
            v, _ = L.alexander_values(curves)
            if not L.same_up_to_units(v, ref_link): return False
        for c, r in zip(curves, ref_comp):
            v, _ = L.alexander_values([c])
            if not L.same_up_to_units(v, r): return False
        return True
    runs = []
    X = None
    for N, cap in zip(Ns, caps):
        t0 = time.time()
        src = dense if X is None else [L.fourier_resample(c, 16 * len(c)) for c in X]
        P = [L.resample_equal_arclength(c, N) for c in src]
        cert0 = certify(P)
        lk0 = L.linking_number(P[0], P[1]) if len(P) == 2 else None
        if not cert0 or (lk0 is not None and abs(lk0) != bt["linking_number"]):
            print("  start certificate FAILED at N", N, flush=True)
            runs.append(dict(N=N, error="start certificate failed"))
            break
        fl = L.LinkFlow(P, lk0 if lk0 is not None else 0, certify=certify)
        r = fl.run(cap)
        X = fl.X
        cert1 = certify(X)
        lk1 = L.linking_number(X[0], X[1]) if len(X) == 2 else None
        ev = {}
        for mult in (8, 16):
            e = L.link_energy_spectral([L.fourier_resample(c, mult * N) for c in X])
            ev[mult] = dict(self=[float(x) for x in e["self"]],  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
                            mutual=None if e["mutual"] is None else float(e["mutual"]),  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
                            total=float(e["total"]))  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
        # isotopy of the smooth interpolant evaluated: certify the fine polygon too
        fine = [L.fourier_resample(c, 8 * N) for c in X]
        cert_fine = certify(fine) and (len(fine) == 1 or abs(L.linking_number(fine[0], fine[1])) == bt["linking_number"])
        dmin_f, dres_f = L.guard_distances(fine)
        Ep = fl.E_poly(X)
        rr = dict(N=N, cap=cap, stop=r["stop"], iterations=r["iterations"], accepted=r["accepted"],
                  guard_rejects=r["guard_rejects"], balances=r["balances"],
                  start_certificate=bool(cert0), end_certificate=bool(cert1),
                  fine_interpolant_certificate=bool(cert_fine), lk_start=lk0, lk_end=lk1,
                  dmin=r["dmin"], res_ratio=r["dres"], fine_res_ratio=float(dres_f),  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
                  E_poly_end=dict(self=[float(x) for x in Ep[0]], mutual=None if Ep[1] is None else float(Ep[1]), total=float(Ep[2])),  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
                  E_final_M8N=ev[8], E_final_M16N=ev[16],
                  quad_diff=abs(ev[8]["total"] - ev[16]["total"]),
                  history=r["history"][::5] + [r["history"][-1]], seconds=time.time() - t0)
        runs.append(rr)
        np.savez(f"curves/{name}{tag}_N{N}.npz", *X)
        print(f"  N={N} stop={r['stop']} it={r['iterations']} E16N={ev[16]} quad={rr['quad_diff']:.1e} "
              f"cert={cert0},{cert1},{cert_fine} lk={lk0},{lk1} bal={r['balances']} rej={r['guard_rejects']} t={rr['seconds']:.0f}s", flush=True)
    out["runs"] = runs
    json.dump(out, open(f"runs/{name}{tag}.json", "w"), indent=1)

if __name__ == "__main__":
    main()
