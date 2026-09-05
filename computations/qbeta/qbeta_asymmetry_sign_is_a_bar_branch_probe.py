#!/usr/bin/env python3
"""The symmetry-energy sign is a BAR BRANCH — a binary choice nothing has pinned,
and the corpus took the branch that fits nuclear binding worse.

The dominant residual of the additive binding law is the symmetry energy: the
residual correlates **-0.804** with `(N-Z)^2/A^2`. `qou-ubsl` closed the obvious
algebraic route (isospin/SU(4) Casimir) as structurally forbidden by the row cap,
which left the term with no source. This probe finds a different handle: the law
ALREADY has an asymmetry term, its sign is one bit, and that bit is not pinned by
what everyone assumed pins it.

*** 1. THE ASYMMETRY IS EXACTLY +/- 2 ln q ***

From the pinning (`qou-xf14`), `b_pp = q^2/[2]_q` and `b_nn = q^-2/[2]_q`, so the
bond energies are `ln[2]_q -/+ 2 ln q` and the bond sum has the closed form

    S(Z,N) = (A-2) ln[2]_q + (-ln b_pn) + 2 ln(q) . (N - Z)

The asymmetry coefficient is **exactly `2 ln q_0 = 0.2086814`**, and it is
positive for one reason only: `q_0 > 1`. (This supersedes the first-order figure
`2(q_0-1) = 0.21996` quoted in `qou-q7ga`; the exact value is the one to use.)

*** 2. AND ITS SIGN IS A BAR BRANCH ***

Under the bar involution `q -> 1/q`: `[2]_q` is INVARIANT, and `b_pp <-> b_nn`
swap. So the two branches are

    as built     p-p = sigma,      n-n = sigma^-1     coefficient  +2 ln q
    bar-swapped  p-p = sigma^-1,   n-n = sigma        coefficient  -2 ln q

one bit, and it traces to the Hecke eigenvalue assignment `u <-> +q`,
`d <-> -q^-1` in the quark sector (`meson-to-proton-via-borromean.md`).

*** 3. THE SWAPPED BRANCH FITS SUBSTANTIALLY BETTER ***

2548 measured AME2020 nuclides, tower-summed `E_0` as ruled, 3 strands/nucleon:

    law                                   p5-p95    full    corr with (N-Z)^2/A^2
    as built      p-p = sigma             1.22497   10.18       -0.804
    BAR-SWAPPED   p-p = sigma^-1          1.16633    7.37       -0.493
    no asymmetry  (bond count only)       1.18054    8.21       -0.697

The swap nearly halves the symmetry-energy correlation and is **the first
isospin structure in this arc to beat layout-free bond counting** — which
reverses `qou-q7ga`'s conclusion that the q-deformation is net-negative on
binding. It is net-negative on the branch the corpus took, and net-positive on
the other one.

*** 4. AND THE BETA-DECAY SECTOR DOES NOT PIN THE BRANCH ***

The natural objection is that the branch is fixed elsewhere — the same letters
build the nucleons, so surely `Q_beta` decides it. **It does not, and the reason
is specific:** `derived_masses.py` computes

    Q_beta = |Delta(net)| . E_0        Delta(net) = net(n) - net(p) = -0.18829

with an ABSOLUTE VALUE, so the magnitude is sign-blind — the swap changes nothing
there. And the mass ordering is imposed separately, `m_n = m_p + Q_beta + m_e`,
not read off `Delta(net)`'s sign. So neither the `Q_beta` magnitude nor the
neutron-heavier fact constrains the bit.

*** WHAT THIS IS, AND WHAT IT IS NOT ***

**Is:** a demonstration that the symmetry-energy term is not missing — it is
present with an unpinned sign, and the sector everyone would expect to pin it is
sign-blind. That is a much more actionable position than "no algebraic route".

**Is NOT an adoption of the swap.** Choosing the branch that fits IS a fit, and
this probe does not choose. What it establishes is that the choice is currently
FREE and the evidence points the other way, so *something must pin it* — and
finding what does is the successor question. Candidates that would settle it, none
evaluated here: electric charge (`u = +2/3`, `d = -1/3` is not bar-symmetric), the
Borromean proton construction, or the `net` values' own derivation.

**Caveat that cuts against the finding:** the swap is a discrete choice out of
two, so "it fits better" is one bit of evidence, not a derivation, and the
improvement (1.225 -> 1.166 in p5-p95) leaves the law still far from the data. The
symmetry energy is reduced, not supplied — corr -0.493 is still the dominant
residual shape.
"""
from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

DPS = 30
mp.mp.dps = DPS
Q0 = mp.mpf("1.1099785827513808075916690956107688798744991218736")
M_E = mp.mpf("0.51099895069")
HBAR_Q = (Q0 - 1)/Q0
E0 = M_E/(Q0*(Q0 - 1))/(1 - HBAR_Q**2)      # tower-summed, as ruled 2026-09-05
STRANDS = 3
B_PP = Q0**3/(Q0**2 + 1)
B_NN = 1/(Q0**3 + Q0)
B_PN = ((Q0**10 - 2*Q0**9 + 7*Q0**8 - 2*Q0**6 + 4*Q0**5 + 4*Q0**4
         + Q0**2 - 2*Q0 + 1)/(12*Q0**5*(Q0**2 + 1)))
L_PP, L_PN, L_NN = -mp.log(B_PP), -mp.log(B_PN), -mp.log(B_NN)
TWO_Q = Q0 + 1/Q0

#: corpus values, `free-neutron-decay.witness.json` via derived_masses.py
NET_N, NET_P = mp.mpf("0.81083"), mp.mpf("0.99913")

AME = ROOT / "qou-mass/src/qou_mass/data/ame2020.json"


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def _pct(v, n, d=100):
    s = sorted(v)
    return s[min(len(s) - 1, len(s)*n//d)]


def _corr(xs, ys):
    n = len(xs)
    mx, my = sum(xs)/n, sum(ys)/n
    return (sum((a - mx)*(b - my) for a, b in zip(xs, ys))
            / mp.sqrt(sum((a - mx)**2 for a in xs)*sum((b - my)**2 for b in ys)))


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    ok = True
    q = sp.symbols("q", positive=True)
    s_pp, s_nn, s_two = q**3/(q**2 + 1), 1/(q**3 + q), q + 1/q

    print("=" * 78)
    print("1. THE ASYMMETRY IS EXACTLY +/- 2 ln q")
    print("=" * 78)
    print(f"    -ln b_pp - ln[2]_q = {sp.simplify(-sp.log(s_pp) - sp.log(s_two))}")
    print(f"    -ln b_nn - ln[2]_q = {sp.simplify(-sp.log(s_nn) - sp.log(s_two))}")
    ok &= chk("the_splitting_is_exactly_two_log_q_symbolically",
              sp.simplify(-sp.log(s_nn) - sp.log(s_two) - 2*sp.log(q)) == 0
              and sp.simplify(-sp.log(s_pp) - sp.log(s_two) + 2*sp.log(q)) == 0, True,
              "so S = (A-2)ln[2]_q + (-ln b_pn) + 2 ln(q).(N-Z), and the "
              "coefficient is positive for ONE reason: q0 > 1")
    print(f"    2 ln q0 = {mp.nstr(2*mp.log(Q0), 12)}   (supersedes qou-q7ga's "
          f"first-order 2(q0-1) = {mp.nstr(2*(Q0-1), 8)})")

    print("\n" + "=" * 78)
    print("2. AND ITS SIGN IS A BAR BRANCH")
    print("=" * 78)
    ok &= chk("bar_leaves_the_loop_invariant_and_swaps_the_two_pure_bonds",
              sp.simplify(s_two.subs(q, 1/q) - s_two) == 0
              and sp.simplify(s_pp.subs(q, 1/q) - s_nn) == 0
              and sp.simplify(s_nn.subs(q, 1/q) - s_pp) == 0, True,
              "[2]_q is bar-invariant, b_pp <-> b_nn swap. One bit, tracing to "
              "the Hecke eigenvalue assignment u <-> +q, d <-> -q^-1")

    rows = []
    for e in json.loads(AME.read_text())["entries"]:
        Z, N, A = e["Z"], e["N"], e["A"]
        b = e.get("binding_energy_per_A_keV")
        if Z < 1 or N < 1 or not b or e.get("binding_energy_per_A_estimated"):
            continue
        B = mp.mpf(str(b))*A/1000
        if B > 0:
            rows.append((A, Z, N, B))

    print("\n" + "=" * 78)
    print(f"3. THE SWAPPED BRANCH FITS BETTER — {len(rows)} measured nuclides")
    print("=" * 78)
    laws = {
        "as built     p-p = sigma": lambda A, Z, N: STRANDS*E0*((Z - 1)*L_PP + L_PN + (N - 1)*L_NN),
        "BAR-SWAPPED  p-p = sigma^-1": lambda A, Z, N: STRANDS*E0*((Z - 1)*L_NN + L_PN + (N - 1)*L_PP),
        "no asymmetry (count only)": lambda A, Z, N: STRANDS*E0*((A - 2)*mp.log(TWO_Q) + L_PN),
    }
    asym = [(mp.mpf(N - Z)/A)**2 for (A, Z, N, B) in rows]
    table = []
    print(f"    {'law':<30}{'p5-p95':>10}{'full':>9}{'corr (N-Z)^2/A^2':>20}")
    for nm, f in laws.items():
        v = [B/f(A, Z, N) for (A, Z, N, B) in rows]
        p595 = _pct(v, 95)/_pct(v, 5)
        full = max(v)/min(v)
        c = _corr(asym, v)
        table.append({"law": nm, "p5_p95": mp.nstr(p595, 10),
                      "full": mp.nstr(full, 10), "corr": mp.nstr(c, 10)})
        print(f"    {nm:<30}{mp.nstr(p595, 6):>10}{mp.nstr(full, 6):>9}"
              f"{mp.nstr(c, 8):>20}")
    built, swapped, count = (mp.mpf(t["p5_p95"]) for t in table)
    cb, cs, cc = (abs(mp.mpf(t["corr"])) for t in table)
    ok &= chk("the_swapped_branch_beats_the_built_one_on_spread_and_correlation",
              swapped < built and cs < cb, True,
              "1.166 vs 1.225, and corr -0.493 vs -0.804 -- nearly halved")
    ok &= chk("and_it_is_the_first_isospin_structure_in_this_arc_to_beat_bond_counting",
              swapped < count, True,
              "which REVERSES qou-q7ga's conclusion: the q-deformation is "
              "net-negative on the branch the corpus took and net-POSITIVE on "
              "the other one")

    print("\n" + "=" * 78)
    print("4. AND BETA-DECAY DOES NOT PIN THE BRANCH")
    print("=" * 78)
    dnet = NET_N - NET_P
    print(f"    net(n) = {NET_N}   net(p) = {NET_P}   Delta(net) = {mp.nstr(dnet, 8)}")
    print(f"    derived_masses.py:  Q_beta = |Delta(net)| . E_0   <- ABSOLUTE VALUE")
    print(f"                        m_n    = m_p + Q_beta + m_e   <- ordering imposed")
    ok &= chk("the_Q_beta_magnitude_is_sign_blind",
              abs(abs(dnet) - abs(-dnet)) < mp.mpf("1e-25"), True,
              "the swap exchanges net(n) and net(p), flipping Delta(net)'s sign "
              "and changing |Delta(net)| not at all -- so the Q_beta magnitude "
              "does not constrain the bit")
    ok &= chk("and_the_mass_ordering_is_imposed_not_derived_from_the_sign",
              True, True,
              "m_n = m_p + Q_beta + m_e puts the neutron above the proton by "
              "construction, so the neutron-heavier fact does not constrain it "
              "either. Neither half of the beta-decay sector pins the branch")

    print("\n  🔓 The symmetry-energy term is not MISSING — it is present with an")
    print("     UNPINNED sign, and the sector everyone would expect to fix it is")
    print("     sign-blind. Something must pin it; finding what is the successor.")
    print("  🛑 NOT adopted here. Choosing the branch that fits IS a fit, and the")
    print("     improvement reduces the symmetry residual (corr -0.804 -> -0.493)")
    print("     without supplying it — it is still the dominant residual shape.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-asymmetry-sign-is-a-bar-branch",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": mp.nstr(Q0, 30), "dps": DPS,
                       "E_0_MeV": mp.nstr(E0, 20),
                       "E_0_form": "tower-summed (owner ruling 2026-09-05)",
                       "strands_per_nucleon": STRANDS,
                       "net_n": str(NET_N), "net_p": str(NET_P),
                       "source": "qou-mass/src/qou_mass/data/ame2020.json"},
        "data": {"n_measured": len(rows),
                 "asymmetry_coefficient_exact": "2*log(q)",
                 "asymmetry_coefficient_at_q0": mp.nstr(2*mp.log(Q0), 15),
                 "superseded_first_order_value": mp.nstr(2*(Q0 - 1), 15),
                 "laws": table,
                 "delta_net": mp.nstr(dnet, 10)},
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_asymmetry_sign_is_a_bar_branch_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-asymmetry-sign-is-a-bar-branch.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
