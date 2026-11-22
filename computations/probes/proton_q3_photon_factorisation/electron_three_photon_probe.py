#!/usr/bin/env python3
"""Is the electron word s0 s1 s0 a three-photon product gamma1*gamma2*gamma3 in H_3(q)?

Photon (owner ruling 2026-11-20): gamma = 1 + phi0*s0 + phi1*s1 + phi01*s0*s1^{-1}.

Model-internal arithmetic only. q = 11/10 is a sample point of the formal variable, not a
substrate anchor; no experimental value enters. mpmath at 60 dps, no float arithmetic.

H_3(q) is semisimple at generic q, so gamma1*gamma2*gamma3 = lam*s0s1s0 holds iff it holds
in the trivial character (s -> q), the sign character (s -> -1/q) and the 2-dim block.
With gamma3 fixed and lam = 1 that is 6 equations in the 6 weights of gamma1, gamma2.
Newton from a recorded seed converges to residual < 1e-50 with a nonsingular Jacobian,
so an isolated solution exists there (Newton-Kantorovich style evidence; not a proof).
Contrast: two photons cannot do it (ElectronNotTwoPhoton.lean, sorry-free).
"""
import json, pathlib
import mpmath as mp
mp.mp.dps = 60
q = mp.mpf(11) / 10
S0 = mp.matrix([[q, 0], [1, -1 / q]]); S1 = mp.matrix([[-1 / q, 1], [0, q]])
S1i = mp.matrix([[-q, 1], [0, 1 / q]]); C = S0 * S1i; I = mp.eye(2)
M = lambda a, b, c: I + a * S0 + b * S1 + c * C
tr = lambda a, b, c: 1 + q * (a + b) + c
sg = lambda a, b, c: 1 - (a + b) / q + c
E = S0 * S1 * S0
g3 = [mp.mpf(3) / 10, mp.mpf(-7) / 10, mp.mpf(9) / 20]
lam = mp.mpf(1)
def F(*x):
    P = M(*x[0:3]) * M(*x[3:6]) * M(*g3)
    return [P[0, 0] - lam * E[0, 0], P[0, 1] - lam * E[0, 1], P[1, 0] - lam * E[1, 0],
            P[1, 1] - lam * E[1, 1],
            tr(*x[0:3]) * tr(*x[3:6]) * tr(*g3) - lam * q ** 3,
            sg(*x[0:3]) * sg(*x[3:6]) * sg(*g3) + lam / q ** 3]
seed = [mp.mpf(s) for s in ("-45.9720308947", "35.8133528577", "10.4776605468",
                            "1.19719151778", "0.976727560112", "0.956289957858")]
sol = mp.findroot(F, seed, tol=mp.mpf(10) ** -55, maxsteps=100)
res = max(abs(v) for v in F(*sol))
J = mp.matrix(6, 6); hstep = mp.mpf(10) ** -28
for j in range(6):
    xp = list(sol); xm = list(sol); xp[j] += hstep; xm[j] -= hstep
    fp, fm = F(*xp), F(*xm)
    for i in range(6): J[i, j] = (fp[i] - fm[i]) / (2 * hstep)
detJ = mp.det(J)
blocks = [[mp.det(M(*g)), tr(*g), sg(*g)] for g in (sol[0:3], sol[3:6], g3)]
checks = {
    'residual_below_1e-50': res < mp.mpf(10) ** -50,
    'jacobian_nonsingular': abs(detJ) > 1,
    'all_photons_invertible': all(all(abs(v) > mp.mpf(10) ** -3 for v in bl) for bl in blocks),
}
out = {
    'question': 'is s0s1s0 a three-photon product (lam = 1)?',
    'q_sample': '11/10 (formal variable sample, not an anchor)',
    'gamma3': [mp.nstr(v, 10) for v in g3],
    'gamma1': [mp.nstr(v, 40) for v in sol[0:3]],
    'gamma2': [mp.nstr(v, 40) for v in sol[3:6]],
    'residual': mp.nstr(res, 5), 'detJ': mp.nstr(detJ, 20),
    'blocks_det_triv_sign': [[mp.nstr(v, 15) for v in bl] for bl in blocks],
    'checks': checks,
    'verdict': 'yes numerically (isolated, nondegenerate); two photons provably cannot',
}
print(json.dumps(out, indent=1))
pathlib.Path(__file__).with_name('electron_three_photon_result.json').write_text(json.dumps(out, indent=1) + '\n')
assert all(checks.values()), checks
