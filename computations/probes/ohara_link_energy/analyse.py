#!/usr/bin/env python3
"""Extrapolation and pairwise separation per preregistration.md section 6."""
import json, glob, itertools, math  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
import numpy as np  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities

TWO_PI2 = 2 * math.pi ** 2

def extrap(Ns, Es):
    """E(N) = Einf + c N^-p through 3 points (p free), plus p=1,2 two-point fits."""
    out = {}
    N1, N2, N3 = Ns; E1, E2, E3 = Es
    fits = {}
    for p in (1.0, 2.0):
        a, b = N2 ** -p, N3 ** -p
        c = (E2 - E3) / (a - b); fits[f"p={int(p)}"] = E3 - c * b
    d1, d2 = E1 - E2, E2 - E3
    pfree = None
    if d1 != 0 and 0 < d2 / d1 < 2 ** -0.5:   # p_free > 0.5 required (POST-HOC guard)
        r = d2 / d1  # = (N2^-p - N3^-p)/(N1^-p - N2^-p) = 2^-p for doubling
        pfree = -math.log2(r)
        Einf = E3 - d2 * r / (1 - r)
        fits["p_free"] = Einf
    else:
        Einf = None
    cands = [v for v in fits.values() if v is not None]
    best = fits.get("p_free", fits["p=2"])
    spread = max(cands) - min(cands)
    err = max(abs(E3 - best), spread)
    out.update(Einf=best, err=err, p_free=pfree, fits=fits, monotone=(d1 >= 0 and d2 >= 0))
    return out

def main():
    res = {}
    for f in sorted(glob.glob("runs/*.json")):
        d = json.load(open(f))
        tag = f.split("/")[-1][:-5]
        runs = [r for r in d["runs"] if "E_final_M16N" in r]
        row = dict(word=d["word"], strands=d["strands"], R_over_a=d["R_over_a"],
                   components=d["components"], lk=d["linking_number_braid"],
                   self_writhe=d["self_writhe"], initial=d["initial"]["4096"], runs={})
        for r in runs:
            row["runs"][r["N"]] = dict(E=r["E_final_M16N"], quad=r["quad_diff"], stop=r["stop"],
                                       it=r["iterations"],
                                       topo=bool(r["start_certificate"] and r["end_certificate"] and r["fine_interpolant_certificate"] and (r["lk_start"] == r["lk_end"])),
                                       rej=r["guard_rejects"], bal=r["balances"])
        if len(runs) == 3:
            Ns = [r["N"] for r in runs]
            for key in ("total", "mutual", "self0", "self1"):
                if key == "total": Es = [r["E_final_M16N"]["total"] for r in runs]
                elif key == "mutual":
                    if runs[0]["E_final_M16N"]["mutual"] is None: continue
                    Es = [r["E_final_M16N"]["mutual"] for r in runs]
                else:
                    k = int(key[-1])
                    if k >= len(runs[0]["E_final_M16N"]["self"]): continue
                    Es = [r["E_final_M16N"]["self"][k] for r in runs]
                ex = extrap(Ns, Es)
                quad = max(r["quad_diff"] for r in runs)
                ex["err"] += quad
                row[f"extrap_{key}"] = ex
            row["upper_bound_total"] = min(r["E_final_M16N"]["total"] for r in runs)
        res[tag] = row
    # POST-HOC landscape/stopping error floor, measured from runs that must agree:
    # conjugate pairs at N=256 and the R/a-start spread at N=64.
    diffs = []
    def tot(tag, N):
        try: return res[tag]["runs"][N]["E"]["total"]
        except KeyError: return None
    for a, b in (("gluon_s0_s1", "nuc11_interleaved"), ("gluon_s1_s0", "gluon_s1_s1")):
        if tot(a, 256) and tot(b, 256): diffs.append(abs(tot(a, 256) - tot(b, 256)))
    for base in ("nuc9", "cal_hopf_s1^2"):
        vals = [tot(t, 64) for t in (base, base + "_Roa2", base + "_Roa4.5") if tot(t, 64)]
        if len(vals) > 1: diffs.append(max(vals) - min(vals))
    floor = max(diffs) if diffs else 0.0
    for n, r in res.items():
        if "extrap_total" in r:
            r["extrap_total"]["err_extrap_only"] = r["extrap_total"]["err"]
            r["extrap_total"]["err"] = r["extrap_total"]["err"] + floor
            r["N_converged"] = r["extrap_total"]["p_free"] is not None
    # pairwise separation on total
    names = [n for n in res if "extrap_total" in res[n] and "_" in n]
    sep = {}
    for a, b in itertools.combinations(names, 2):
        A, B = res[a]["extrap_total"], res[b]["extrap_total"]
        gap = abs(A["Einf"] - B["Einf"]); tol = A["err"] + B["err"]
        sep[f"{a} | {b}"] = dict(gap=gap, combined_err=tol, separated=gap > tol)
    json.dump(dict(candidates=res, separation=sep, landscape_error_floor=floor, floor_inputs=diffs), open("results.json", "w"), indent=1)
    print("landscape floor", floor, diffs)
    for n, r in res.items():
        if "extrap_total" in r:
            e = r["extrap_total"]
            print(f"{n:28s} Einf={e['Einf']:.4f} +- {e['err']:.4f}  p={e['p_free']}  UB={r['upper_bound_total']:.4f}  "
                  + " ".join(f"N{N}:{v['E']['total']:.4f}/{v['stop']}/{'ok' if v['topo'] else 'TOPO?'}" for N, v in r["runs"].items()))
    for k, v in sep.items():
        print(f"{k:60s} gap={v['gap']:.4f} err={v['combined_err']:.4f} {'SEPARATED' if v['separated'] else 'not separated'}")

if __name__ == "__main__":
    main()
