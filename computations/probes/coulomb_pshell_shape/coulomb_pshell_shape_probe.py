"""Derived p-shell Coulomb shape factor for 5 <= A <= 16 (beans qou-tcl3, qou-usft).

Replaces the imported uniform ball above A = 4 with the same construction that gave
the s-shell f = 0.520011 (coulomb_shape_factor_qbessel_probe.py, PR #9665/#9699).

PRE-REGISTRATION (written before any p-shell number was computed; nothing tuned)
  * Same arena, lattice step p = 1/q0, base p^2, Hahn-Exton J_nu, full Jackson lattice.
  * Same rule nu = l + 1/2:  s-shell nu = 1/2, p-shell (l = 1) nu = 3/2.
  * Shell filling of the CHARGE: Z <= 2 protons in 0s, Z - 2 in 0p (valid for Z <= 8).
  * Both orbitals on the SAME lattice at the same dilation index n = 0 (the
    Koelink-Swarttouw normalisation point). Alternates n_p = +-1 reported, never selected.
  * Density = (min(Z,2) * rho_s + max(Z-2,0) * rho_p) / Z, each rho normalised to 1.
  * f := E * r_rms (unit charge), as in CoulombShellShapeFactor.lean.
Comparison (AME mirror splits) uses coulomb_energy's CAL-3 radius with c = 1 as on main;
c is an open owner card, so the comparison is reported for c = 1 only and labelled.
mpmath, 60 dps.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
COMP = HERE.parents[1]
for p in (COMP / "substrate", COMP, COMP / "probes"):
    sys.path.insert(0, str(p))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from coulomb_shape_factor_qbessel_probe import (  # noqa: E402
    hahn_exton_on_lattice, shell_f, shell_f_double_sum)

mp.mp.dps = 60
STEP = Q_50_DIGIT_STR
p = 1 / mp.mpf(STEP)
TAIL = mp.mpf(10) ** -25


def orbital(nu, n_shift):
    """Normalised shell weights {k: P_k} of J_nu(p^{k+n}; p^2) on radius p^k."""
    out = {}
    kmin = -2
    small = 0
    while small < 4:
        kmin -= 1
        w = p ** (2 * kmin) * hahn_exton_on_lattice(nu, kmin + n_shift, STEP) ** 2
        small = small + 1 if w < TAIL ** 2 else 0
    kmax = int(mp.ceil(2 * mp.log(TAIL) / ((2 + 2 * nu) * mp.log(p)))) + 5 - n_shift
    for k in range(kmin, kmax + 1):
        out[k] = p ** (2 * k) * hahn_exton_on_lattice(nu, k + n_shift, STEP) ** 2
    tot = mp.fsum(out.values())
    return {k: v / tot for k, v in out.items()}


def mixed_f(Z, rho_s, rho_p):
    ns, np_ = min(Z, 2), max(Z - 2, 0)
    keys = sorted(set(rho_s) | set(rho_p))
    rs = [p ** k for k in keys]
    ws = [(ns * rho_s.get(k, 0) + np_ * rho_p.get(k, 0)) / Z for k in keys]
    return shell_f(rs, ws)[0], shell_f_double_sum(rs, ws)


half, three_half = mp.mpf(1) / 2, mp.mpf(3) / 2
rho_s = orbital(half, 0)
checks = []
f_s = mixed_f(2, rho_s, {})[0]
checks.append(("s-shell f reproduces 0.520011 (PR #9665)", abs(f_s - mp.mpf("0.520011")) < mp.mpf("5e-7")))

BALL = mp.mpf(3) / 5 * mp.sqrt(mp.mpf(3) / 5)
results = {}
for n_shift, tag in ((0, "primary n_p = 0"), (1, "alternate n_p = +1"), (-1, "alternate n_p = -1")):
    rho_p = orbital(three_half, n_shift)
    row = {}
    for Z in range(3, 9):
        f, f2 = mixed_f(Z, rho_s, rho_p)
        if n_shift == 0:
            checks.append((f"Z={Z}: cumulative sum = Lean double sum", abs(f - f2) < mp.mpf(10) ** -40))
        row[Z] = f
    results[tag] = row
    print(tag, " ".join(f"Z={Z}:{mp.nstr(row[Z], 7)}" for Z in range(3, 9)))
print("uniform ball (imported, main):", mp.nstr(BALL, 7))

# comparison only: mirror splits with main's CAL-3 radius (c = 1)
from coulomb_energy import alpha_em_hbar_c_mev_fm, nuclear_radius_fm  # noqa: E402
aHc = alpha_em_hbar_c_mev_fm()


def EC(Z, A, f):
    rrms = mp.sqrt(mp.mpf(3) / 5) * nuclear_radius_fm(A)
    return f * Z * (Z - 1) * aHc / rrms


AME = [("7Li/7Be", 7, 3, "1.643920"), ("11B/11C", 11, 5, "2.763600"),
       ("13C/13N", 13, 6, "3.003000"), ("15N/15O", 15, 7, "3.536700")]
print("\nCOMPARISON ONLY (AME2020; radius CAL-3 with c = 1, an open owner card):")
prim = results["primary n_p = 0"]
for name, A, Zl, d in AME:
    dB = mp.mpf(d)
    ball = EC(Zl + 1, A, BALL) - EC(Zl, A, BALL)
    der = EC(Zl + 1, A, prim[Zl + 1]) - EC(Zl, A, prim[Zl])
    print(f"  {name:9s} AME {mp.nstr(dB,6)}  ball {mp.nstr(ball,6)} ({mp.nstr(100*(ball/dB-1),3)}%)"
          f"  p-shell {mp.nstr(der,6)} ({mp.nstr(100*(der/dB-1),3)}%)")

print()
ok = all(c for _, c in checks)
for n, c in checks:
    print(("PASS " if c else "FAIL ") + n)
sys.exit(0 if ok else 1)
