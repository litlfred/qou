"""Nucleon width as Im Vol_C = CS (prereg computations/probes/nucleon_width/PREREGISTRATION.md).

Uses SnapPy high-precision (~64 digits) geometry, not float64. Prints CS of the Borromean
complement L6a4, of the proton braid closure (σ1σ2^-1)^3 and its mirror, and whether the two
closures are isometric. SnapPy's 'Braid:' manifold is the braid closure together with the braid
axis (it reports 4 cusps against 3 for L6a4); both are given.
"""
import warnings; warnings.filterwarnings("ignore")
import snappy
M = snappy.Manifold('L6a4').high_precision()
print('L6a4 (Borromean) cusps', M.num_cusps(), 'Vol', M.volume(), 'CS', M.chern_simons())
P = snappy.Manifold('Braid:[1,-2,1,-2,1,-2]')
N = snappy.Manifold('Braid:[-1,2,-1,2,-1,2]')
for name, X in (('proton closure+axis', P), ('neutron (mirror) closure+axis', N)):
    print(name, 'cusps', X.num_cusps(), X.identify(), 'CS', X.high_precision().chern_simons())
print('proton ~ neutron isometric:', P.is_isometric_to(N))
