"""There is no single "the nucleon NF": three live builders give three alphas,
spanning a SIGN CHANGE. The qou-pdix gate is far worse than 0.58%.

Bean `qou-pdix` (child of `qou-cds1`).

The bean gates branch 3 on the nucleon normal form being "unsettled at 0.58%".
That figure is the COUNIT ratio 1.00579 between two builders. Measured on the
PHASE, across the three builders the tree actually contains, the spread is not
0.58% — it spans a sign change and a factor ~4.5 in magnitude.

## The three builders are three different SYSTEMS, not three bases

This is the caveat to read before using the table. They are not like-for-like:

  single-wrap    a bare A=1 nucleon; the 6-vector [h^2/2, -h/2, -h/2, 0,0,0]
                 asserted in the 2026-06-16 counit-vs-trace audit. What the
                 Q_beta counit chain is built on.

  build_nucleon_nf   a bare nucleon as B_3 + quark crossings, 9 crossings.
                 What the earlier probe called "typed". **Its own docstring
                 declares it DEFECTIVE** -- "NO GLUON TERM -- and this is a
                 DEFECT, not a convention ... 6 (B_3) + 3 (quarks) + 2 (gluon)
                 = 11 is the SDP-consistent budget. Use build_atom_nf".

  build_atom_nf  gluon-complete, and includes ELECTRONS (sigma_1^-1 per Z). So
                 `(0,1) - (1,0)` is neutron minus HYDROGEN, which is the
                 atomic-mass convention beta^- decay actually uses -- arguably
                 the physically right object, but a different object from the
                 bare-nucleon difference the other two compute.

So the spread below is NOT a basis ambiguity and NOT a bookkeeping choice. It
is three different models of the decaying system, and the ladder's N=1 phase
is not robust across them.

## Measured at the proton pin, against the required N=1 factor 0.99839767

    builder                  alpha (C)     cos(alpha)     unexplained
    single-wrap             -0.0523361     0.99863078       +14.5%
    build_nucleon_nf (9cr)  -0.0354101     0.99937313       +60.9%
    build_atom_nf (gluon)   +0.2355793     0.97237929      -1624%

The first two UNDER-correct; the third OVER-corrects by more than an order of
magnitude, with the opposite sign of residual. No choice among them is a small
perturbation of another.

## A docstring defect found on the way, and it is load-bearing

`pyhecke/atom.py` `build_nucleon_nf` retracts the sentence *"No separate gluon
dressing -- B_3 IS the gluon structure"* as unbacked and redirects to
`build_atom_nf`. **That exact sentence still stands verbatim at line 218, in
`build_atom_nf`'s own docstring** -- and there it is not merely unbacked, it is
FALSE ABOUT ITS OWN FUNCTION: lines 252-253 and 264-265 apply `hm(nf, 1, 0, 0)`
twice per nucleon, commented "gluon 1" / "gluon 2". A prior agent corrected one
docstring and left its twin, and the redirect points at the uncorrected one.

The code is right; the redirect is sound; only the line is stale. Recorded
because a reader checking the contract at the function they call would conclude
the opposite of what it does.

Run:  python3 -u computations/qbeta/qbeta_three_nucleon_nf_alpha_spread_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
for _p in (REPO / "tools" / "pyhecke" / "python", REPO / "computations",
           REPO / "computations" / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402

from pyhecke.atom import build_atom_nf_exact  # noqa: E402
from q_parameter import q_at  # noqa: E402 — proton pin
from witness_base import WitnessBuilder  # noqa: E402

CR = [0, 1, 1, 2, 2, 3]           # crossing numbers of the hm NF basis
REQUIRED_N1 = mp.mpf("0.99839767")   # bean entry (8)


def main() -> int:
    mp.mp.dps = 50
    q0 = mp.mpf(str(q_at()))
    h = q0 - 1 / q0
    zC, zD = mp.sqrt(q0) / (q0 + 1), q0**3 / (q0**2 + 1)

    # the gluon-complete atom NF: neutron minus hydrogen (atomic-mass convention)
    d = [a - b for a, b in zip(build_atom_nf_exact(0, 1),
                               build_atom_nf_exact(1, 0))]
    atom = [mp.mpf(x.numerator) / mp.mpf(x.denominator) for x in d]

    single_wrap = [h**2 / 2, -h / 2, -h / 2, mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    typed = [h*(2*h**4 + h**2 - 2)/4,
             h**2*(h**2 + 1)*(2*h**2 + 1)/4,
             h**2*(h**2 - h + 1)*(h**2 + h + 1)/4,
             -h**5/4,
             h*(h**2 + 1)*(h**4 - 2)/4,
             -h**4*(h**2 + 2)/4]

    builders = {"single_wrap": single_wrap,
                "build_nucleon_nf_9cr": typed,
                "build_atom_nf_gluon_complete": atom}

    rows = {}
    for name, v in builders.items():
        eps = sum(v)
        row = {"eps": mp.nstr(eps, 16)}
        for cn, zv in (("C", zC), ("D", zD)):
            trm = sum(c * zv**k for c, k in zip(v, CR))
            a = (eps - trm) / 2
            ca = mp.cos(a)
            row[f"alpha_{cn}"] = mp.nstr(a, 16)
            row[f"cos_alpha_{cn}"] = mp.nstr(ca, 16)
            row[f"unexplained_{cn}"] = mp.nstr(
                (ca - REQUIRED_N1) / (1 - REQUIRED_N1), 10)
        rows[name] = row

    checks: list[tuple[str, bool, str]] = []
    aC = {k: mp.mpf(v["alpha_C"]) for k, v in rows.items()}
    checks.append((
        "three_builders_give_three_distinct_alphas",
        len({str(v) for v in aC.values()}) == 3,
        "no two builders agree on the phase",
    ))
    checks.append((
        "alpha_spans_a_sign_change",
        min(aC.values()) < 0 < max(aC.values()),
        "the bare-nucleon builders give a NEGATIVE phase and the "
        "gluon-complete atom NF a POSITIVE one",
    ))
    checks.append((
        "atom_nf_overcorrects",
        mp.mpf(rows["build_atom_nf_gluon_complete"]["unexplained_C"]) < 0,
        "the gluon-complete builder overshoots the required N=1 factor, "
        "the opposite side from the other two",
    ))
    checks.append((
        "bare_builders_undercorrect",
        all(mp.mpf(rows[k]["unexplained_C"]) > 0
            for k in ("single_wrap", "build_nucleon_nf_9cr")),
        "both bare-nucleon builders fall short",
    ))
    checks.append((
        "spread_far_exceeds_the_recorded_0p58pct",
        abs(max(aC.values()) - min(aC.values())) > abs(min(aC.values())),
        "the phase spread exceeds the magnitude of the smallest phase, so it "
        "is not the 0.58% the bean records from the COUNIT ratio",
    ))

    npass = sum(1 for _, ok, _ in checks if ok)
    for n, ok, why in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {n}: {why}")
    print(f"\n{npass}/{len(checks)} assertions pass\n")
    print(f"  {'builder':<30}{'alpha(C)':>18}{'cos(C)':>18}{'unexplained':>14}")
    for k, v in rows.items():
        print(f"  {k:<30}{v['alpha_C']:>18}{v['cos_alpha_C']:>18}"
              f"{v['unexplained_C']:>14}")

    w = WitnessBuilder("qbeta-three-nucleon-nf-alpha-spread",
                       engine="python+mpmath+pyhecke", output_dir=HERE,
                       _script_path=__file__)
    w.set_description(
        "Three live nucleon-NF builders give three different Q_beta N=1 "
        "phases, spanning a SIGN CHANGE: single-wrap -0.05234, "
        "build_nucleon_nf (9 crossings, self-declared defective) -0.03541, "
        "build_atom_nf (gluon-complete, neutron-minus-hydrogen) +0.23558, all "
        "at convention C and the proton pin. The first two undershoot the "
        "required N=1 factor 0.99839767; the third overshoots by ~16x. They "
        "are three different SYSTEMS, not three bases, so this is not a "
        "convention ambiguity. The qou-pdix gate on branch 3 is therefore far "
        "worse than the 0.58% counit ratio the bean records.")
    w.set_content_block("prop:q-beta-cos-resummation")
    w.add_parameter("q0_anchor", "proton (physical_proton pin)")
    w.add_parameter("required_N1_factor", str(REQUIRED_N1))
    w.add_data("assertions_passed", npass)
    w.add_data("assertions_total", len(checks))
    w.add_data("checks", [{"name": n, "pass": ok, "why": why}
                          for n, ok, why in checks])
    w.add_data("builders", rows)
    w.add_data("caveat", (
        "NOT like-for-like: build_atom_nf includes electrons (sigma_1^-1 per "
        "Z), so (0,1)-(1,0) is neutron minus HYDROGEN — the atomic-mass "
        "convention beta^- decay uses, arguably the physically right object, "
        "but a different object from the bare-nucleon difference the other "
        "two compute."))
    w.add_data("docstring_defect", (
        "pyhecke/atom.py:218 — build_atom_nf's docstring still carries 'No "
        "separate gluon dressing — B_3 IS the gluon structure', the exact "
        "sentence build_nucleon_nf retracts as unbacked while redirecting to "
        "build_atom_nf. There it is FALSE about its own function: lines "
        "252-253 and 264-265 apply two gluon crossings per nucleon. Code is "
        "right, redirect is sound, only the line is stale."))
    for n, ok, _ in checks:
        w.add_assertion(n, "pass" if ok else "fail", "pass")
    w.save()
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
