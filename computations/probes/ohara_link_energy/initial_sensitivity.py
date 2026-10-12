import json, numpy as np, ohara_lib as L  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
from run_candidate import WORDS
out = {}
for name, (w, n) in WORDS.items():
    out[name] = {}
    for Roa in (2.0, 3.0, 4.5, 6.0):
        e = L.link_energy_spectral(L.closed_braid_curves(w, n, 4096, R=Roa, a=1.0))
        e2 = L.link_energy_spectral(L.closed_braid_curves(w, n, 2048, R=Roa, a=1.0))
        out[name][Roa] = dict(self=[float(x) for x in e["self"]], mutual=None if e["mutual"] is None else float(e["mutual"]),  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
                              total=float(e["total"]), quad_diff_2048_vs_4096=float(abs(e["total"] - e2["total"])))  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
        print(name, Roa, [round(x, 4) for x in e["self"]], None if e["mutual"] is None else round(e["mutual"], 4), round(e["total"], 4), f"{abs(e['total']-e2['total']):.1e}", flush=True)
json.dump(out, open("initial_sensitivity.json", "w"), indent=1)
