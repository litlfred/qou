#!/usr/bin/env python3
"""The bar swap is REFUTED: it breaks the bound and trades one shape error for
another. The corpus's branch stands — but still by convention, not derivation.

`qou-y2np` found the symmetry-energy sign is a bar branch, that the swapped
branch fits better on spread, and that beta-decay does not pin the bit. The
instruction was to **adopt the swap if the data holds**. Tested properly, it does
not, for two independent reasons — and the charge test named as the pinning
candidate comes back weak.

*** 1. THE SWAP DESTROYS THE UPPER BOUND ***

The owner ruling of 2026-09-05 (brane-tower `E_0`) made the law ONE-SIDED: an
upper bound on binding for 2547 of 2548 measured nuclides. That property has a
physical reason — every SEMF correction SUBTRACTS from the volume term, so a law
omitting all of them belongs above the data.

    branch      nuclides exceeding B <= 3.E_0.S       (measured / all)
    as built              1 / 2548                      1 / 3554
    BAR-SWAPPED         845 / 2548                   1018 / 3554

**845 violations against 1.** The band medians show why: swapped, the A = 40-160
bands sit ABOVE 1 (1.028, 1.021, 0.994) while as-built stays below throughout
(0.860 -> 0.961 -> ... -> 0.796). The swap moves the law INTO the data rather
than above it, which is the wrong side for a law with only negative corrections
outstanding.

*** 2. AND IT REDISTRIBUTES SHAPE ERROR RATHER THAN REMOVING IT ***

    branch      (N-Z)^2/A^2      A^(-1/3)      Z^2/A^(4/3)
    as built      -0.804          -0.178         -0.044
    BAR-SWAPPED   -0.493          -0.376         -0.068

The swap nearly halves the ASYMMETRY correlation and more than DOUBLES the
SURFACE one. Its p5-p95 improvement (1.225 -> 1.166) is real but is bought by
moving error from one channel to another, not by removing it. That is what a
one-bit reparameterisation can do and it is not what a missing term looks like.

*** 3. THE CHARGE TEST — selects the corpus's branch, but proves little ***

`sigma^2 = h.sigma + 1` has eigenvalues `{+q, -1/q}` (solved, not asserted).
Matching the SIGN of the quark charge to the SIGN of the eigenvalue —
`u = +2/3 -> +q`, `d = -1/3 -> -1/q` — reproduces the corpus's assignment, hence
`p-p = sigma`, `n-n = sigma^-1`.

**Two reasons that is weak evidence, both stated because they cut against it:**

  (a) **One bit against one bit.** Two binary labels agree; that happens half the
      time by chance. It carries no more weight than the coincidence it is.
  (b) **The eigenvalue sign is not about charge.** In `V (x) V` the eigenvalue
      `+q` belongs to the SYMMETRIC part and `-q^-1` to the ANTISYMMETRIC part,
      so the sign encodes pairing statistics. Reading it as a charge sign is a
      category slip, and the magnitudes do not corroborate: eigenvalue ratio
      `q^2 = 1.2321` against charge ratio `2`.

So charge does NOT pin the branch. What selects it is §1 — a structural property
of the whole table, not a coincidence of two signs.

*** VERDICT ***

**Not adopted.** The corpus's branch stands, now with an actual argument behind
it (the bound) rather than only convention. But the *reason* `u -> +q` remains
underived: §1 tells us which branch survives, not why the algebra picks it. That
obligation is recorded on `qou-y2np`, which stays open.

**And the symmetry energy is still missing.** `corr = -0.804` stands. The swap
was a promising handle and it is refuted; `qou-ubsl`'s SU(4) route remains
structurally forbidden. The dominant residual shape has no source.
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
E0 = M_E/(Q0*(Q0 - 1))/(1 - HBAR_Q**2)      # tower-summed, as ruled
STRANDS = 3
B_PP = Q0**3/(Q0**2 + 1)
B_NN = 1/(Q0**3 + Q0)
B_PN = ((Q0**10 - 2*Q0**9 + 7*Q0**8 - 2*Q0**6 + 4*Q0**5 + 4*Q0**4
         + Q0**2 - 2*Q0 + 1)/(12*Q0**5*(Q0**2 + 1)))
L_PP, L_PN, L_NN = -mp.log(B_PP), -mp.log(B_PN), -mp.log(B_NN)

AME = ROOT / "qou-mass/src/qou_mass/data/ame2020.json"


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def built(A, Z, N):
    return STRANDS*E0*((Z - 1)*L_PP + L_PN + (N - 1)*L_NN)


def swapped(A, Z, N):
    return STRANDS*E0*((Z - 1)*L_NN + L_PN + (N - 1)*L_PP)


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
    allr, meas = [], []
    for e in json.loads(AME.read_text())["entries"]:
        Z, N, A = e["Z"], e["N"], e["A"]
        b = e.get("binding_energy_per_A_keV")
        if Z < 1 or N < 1 or not b:
            continue
        B = mp.mpf(str(b))*A/1000
        if B <= 0:
            continue
        est = bool(e.get("binding_energy_per_A_estimated"))
        allr.append((A, Z, N, B, est))
        if not est:
            meas.append((A, Z, N, B, est))

    print("=" * 78)
    print("1. THE SWAP DESTROYS THE UPPER BOUND")
    print("=" * 78)
    viol = {}
    for nm, f in (("as built", built), ("BAR-SWAPPED", swapped)):
        row = {}
        for tag, rs in (("measured", meas), ("all", allr)):
            v = [B/f(A, Z, N) for (A, Z, N, B, est) in rs]
            row[tag] = sum(1 for x in v if x > 1)
            print(f"    {nm:<12} {tag:<9}: {row[tag]:>4} of {len(rs)} exceed the law")
        viol[nm] = row
    ok &= chk("the_swap_turns_one_violation_into_hundreds",
              viol["BAR-SWAPPED"]["measured"] > 100*viol["as built"]["measured"], True,
              "845 against 1. The ruling made the law one-sided for a physical "
              "reason -- every SEMF correction SUBTRACTS -- and the swap moves "
              "it INTO the data instead of above it")

    print("\n    band medians (measured) — swapped crosses 1 in the mid-A range:")
    bands = []
    for k in range(8):
        sub = [r for r in meas if 40*k <= r[0] < 40*(k + 1)]
        if len(sub) < 20:
            continue
        b1 = _pct([B/built(A, Z, N) for (A, Z, N, B, est) in sub], 50)
        b2 = _pct([B/swapped(A, Z, N) for (A, Z, N, B, est) in sub], 50)
        bands.append({"band": f"{40*k}-{40*k+39}", "n": len(sub),
                      "built": mp.nstr(b1, 8), "swapped": mp.nstr(b2, 8)})
        print(f"      A {40*k:>3}-{40*k+39:<3} n={len(sub):>4}   built "
              f"{mp.nstr(b1, 6):>9}   swapped {mp.nstr(b2, 6):>9}")
    ok &= chk("as_built_stays_below_one_in_every_band_and_swapped_does_not",
              all(mp.mpf(b["built"]) < 1 for b in bands)
              and any(mp.mpf(b["swapped"]) > 1 for b in bands), True,
              "the swapped A = 40-160 bands sit above 1")

    print("\n" + "=" * 78)
    print("2. AND IT REDISTRIBUTES SHAPE ERROR RATHER THAN REMOVING IT")
    print("=" * 78)
    shapes = {
        "(N-Z)^2/A^2": [(mp.mpf(N - Z)/A)**2 for (A, Z, N, B, est) in meas],
        "A^(-1/3)   ": [mp.mpf(A)**(-mp.mpf(1)/3) for (A, Z, N, B, est) in meas],
        "Z^2/A^(4/3)": [mp.mpf(Z*Z)/mp.mpf(A)**(mp.mpf(4)/3) for (A, Z, N, B, est) in meas],
    }
    corrs = {}
    for nm, f in (("as built", built), ("BAR-SWAPPED", swapped)):
        ys = [B/f(A, Z, N) for (A, Z, N, B, est) in meas]
        corrs[nm] = {k: mp.nstr(_corr(x, ys), 8) for k, x in shapes.items()}
        print(f"    {nm:<12} " + "   ".join(
            f"{k} {mp.nstr(_corr(x, ys), 6):>10}" for k, x in shapes.items()))
    asym_b = abs(mp.mpf(corrs["as built"]["(N-Z)^2/A^2"]))
    asym_s = abs(mp.mpf(corrs["BAR-SWAPPED"]["(N-Z)^2/A^2"]))
    surf_b = abs(mp.mpf(corrs["as built"]["A^(-1/3)   "]))
    surf_s = abs(mp.mpf(corrs["BAR-SWAPPED"]["A^(-1/3)   "]))
    ok &= chk("the_swap_halves_the_asymmetry_error_and_doubles_the_surface_error",
              asym_s < asym_b/1.5 and surf_s > 2*surf_b, True,
              "error moves between channels rather than out of the law -- what "
              "a one-bit reparameterisation does, not what a missing term "
              "looks like")

    print("\n" + "=" * 78)
    print("3. THE CHARGE TEST — selects the corpus's branch, but proves little")
    print("=" * 78)
    q, Lam = sp.symbols("q Lam", positive=True), sp.Symbol("Lam")
    qq = sp.symbols("q", positive=True)
    eig = sp.solve(sp.Eq(Lam**2, (qq - 1/qq)*Lam + 1), Lam)
    print(f"    eigenvalues of sigma: {[sp.simplify(x) for x in eig]}")
    print("    sign-matching  u = +2/3 -> +q,  d = -1/3 -> -1/q  gives the")
    print("    corpus's assignment: p-p = sigma, n-n = sigma^-1.")
    ok &= chk("the_eigenvalues_are_plus_q_and_minus_one_over_q",
              set(sp.simplify(x) for x in eig) == {qq, -1/qq}, True,
              "solved from sigma^2 = h.sigma + 1, not asserted")
    ratio_eig = Q0**2
    print(f"    but |eigenvalue| ratio q^2 = {mp.nstr(ratio_eig, 8)} vs "
          f"|charge| ratio 2")
    ok &= chk("the_magnitudes_do_not_corroborate_the_sign_match",
              abs(ratio_eig - 2) > mp.mpf("0.5"), True,
              "(a) one bit agreeing with one bit happens half the time by "
              "chance; (b) in V(x)V the eigenvalue +q belongs to the SYMMETRIC "
              "part and -q^-1 to the ANTISYMMETRIC part, so the sign encodes "
              "pairing statistics, not charge. Reading it as a charge sign is a "
              "category slip. Charge does NOT pin the branch")

    print("\n  🛑 NOT ADOPTED. The corpus's branch stands — selected by §1, a")
    print("     structural property of the whole table, not by the sign coincidence.")
    print("  🔓 But WHY the algebra picks u -> +q is still underived. §1 says which")
    print("     branch survives, not why. That obligation stays open on qou-y2np.")
    print("  🛑 And the symmetry energy is STILL missing: corr -0.804 stands, the")
    print("     swap is refuted, and qou-ubsl's SU(4) route remains forbidden.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-bar-branch-refuted",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": mp.nstr(Q0, 30), "dps": DPS,
                       "E_0_MeV": mp.nstr(E0, 20),
                       "E_0_form": "tower-summed (owner ruling 2026-09-05)",
                       "strands_per_nucleon": STRANDS,
                       "verdict": "swap NOT adopted; corpus branch stands"},
        "data": {"n_measured": len(meas), "n_all": len(allr),
                 "violations": viol, "band_medians": bands,
                 "correlations": corrs,
                 "eigenvalues": "{+q, -1/q}",
                 "eigenvalue_magnitude_ratio": mp.nstr(ratio_eig, 12),
                 "charge_magnitude_ratio": "2"},
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_bar_branch_refuted_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-bar-branch-refuted.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
