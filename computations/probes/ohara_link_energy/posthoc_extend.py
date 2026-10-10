#!/usr/bin/env python3
"""POST-HOC: continue the N=256 flowed curve with tighter stop (1e-8 over 300 steps, cap 4000)."""
import sys, json, numpy as np, ohara_lib as L  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
from run_candidate import WORDS, KNOT_ALEX
name = sys.argv[1]
bt = json.load(open("braid_topology.json"))[name]
d = np.load(f"curves/{name}_N256.npz"); X = [d[k] for k in sorted(d.files)]
ref_link = L.alexander_from_poly(bt["alexander_t"])
ref_comp = [L.alexander_from_poly(KNOT_ALEX[sw]) for sw in bt["self_crossing_writhe"]]
def certify(curves):
    if len(curves) == 2:
        v, _ = L.alexander_values(curves)
        if not L.same_up_to_units(v, ref_link): return False
    return all(L.same_up_to_units(L.alexander_values([c])[0], r) for c, r in zip(curves, ref_comp))
lk0 = L.linking_number(X[0], X[1])
fl = L.LinkFlow(X, lk0, certify=certify)
r = fl.run(4000, rel_tol=1e-8)  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
X = fl.X
e = L.link_energy_spectral([L.fourier_resample(c, 16 * 256) for c in X])
e8 = L.link_energy_spectral([L.fourier_resample(c, 8 * 256) for c in X])
fine = [L.fourier_resample(c, 8 * 256) for c in X]
out = dict(name=name, stop=r["stop"], iterations=r["iterations"], guard_rejects=r["guard_rejects"],
           cert=bool(certify(X) and certify(fine)), lk=(lk0, L.linking_number(*X), L.linking_number(*fine)),
           E=dict(self=[float(x) for x in e["self"]], mutual=float(e["mutual"]), total=float(e["total"])),  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
           quad=float(abs(e["total"] - e8["total"])))  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
np.savez(f"curves/{name}_N256_ext.npz", *X)
json.dump(out, open(f"runs_posthoc/{name}_N256_ext.json", "w"), indent=1)
print(out, flush=True)
