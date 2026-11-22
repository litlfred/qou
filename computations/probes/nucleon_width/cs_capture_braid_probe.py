"""CS of the hydrogen capture-braid closure, both electron placements.

Prereg: computations/probes/nucleon_width/PREREGISTRATION.md, Addendum 1.
SnapPy high precision; no float64 arithmetic. Generators are 1-indexed (sigma_0 -> 1).
"""
import warnings; warnings.filterwarnings("ignore")
import snappy

core_L = [1, -2] * 3
cap_L = [-3, -2, -1, -1, -2, -3]          # (s2 s1 s0 s0 s1 s2)^-1
core_R = [2, -3] * 3
cap_R = [-1, -2, -3, -3, -2, -1]          # (s0 s1 s2 s2 s1 s0)^-1
WL, WR = core_L + cap_L, core_R + cap_R

def report(name, M):
    H = M.high_precision()
    try:
        cs = H.chern_simons()
    except ValueError as e:
        cs = f"not computed ({e}); solution type {M.solution_type()}"
    print(f"{name}: cusps {M.num_cusps()}, identify {M.identify()}, "
          f"Vol {H.volume()}, CS {cs}")
    return M

closures = {}
for name, w in (("W_L", WL), ("W_R", WR)):
    L = snappy.Link(braid_closure=w)
    print(f"{name} link components {len(L.link_components)}")
    closures[name] = report(f"{name} closure", L.exterior())
    report(f"{name} closure+axis", snappy.Manifold("Braid:" + str(w)))

ref = snappy.Manifold("Braid:" + str(core_L))
report("Borromean closure+axis (reference)", ref)
print("W_L closure ~ W_R closure:", closures["W_L"].is_isometric_to(closures["W_R"]))
print("W_L closure ~ Borromean+axis:", closures["W_L"].is_isometric_to(ref))
print("W_R closure ~ Borromean+axis:", closures["W_R"].is_isometric_to(ref))
