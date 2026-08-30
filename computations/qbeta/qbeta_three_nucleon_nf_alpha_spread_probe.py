"""OWNER RULING 2026-08-30: single-wrap is canonical for the Q_beta channel.

Bean `qou-pdix` (child of `qou-cds1`).

> *"single-wrap. it's A=1, no gluon, no electron"*  — owner, 2026-08-30

This probe measured three live nucleon-NF builders giving three different Q_beta
N=1 phases spanning a SIGN CHANGE, and raised the choice with the author rather
than settling it by residual (which would have been the fit the discipline
forbids). The ruling settles it, and the reason is structural rather than
numerical: **free-neutron beta decay is A=1** — one nucleon, no nucleus — so the
gluon dressing and the electron that `build_atom_nf` carries describe a
different system.

    CANONICAL   single-wrap             bare A=1 nucleon                 alpha = -0.0523361
    not this    build_nucleon_nf (9cr)  bare nucleon + quark crossings   alpha = -0.0354101
    not this    build_atom_nf           + gluons + electrons             alpha = +0.2355793

**The corpus split is therefore CORRECT, not inconsistent.** Before the ruling I
framed the Q_beta chain (single-wrap) and the mass compute (`build_atom_nf`) as
using two objects of which "one is wrong for this channel". Neither is wrong:
they describe different systems, and each is used where it belongs. A nucleus
has gluon dressing and electrons; a decaying free neutron does not.

Note this does NOT double-count the electron. The framework's Q_beta carries
`m_e` as an explicit prefactor (`Q_beta = m_e * |q0^2-2q0-1|(q0+1)/(2q0^3)`), so
the emitted electron enters the Q-value there, not inside the normal form. The
atomic-mass convention that compares neutron to HYDROGEN is the bookkeeping of
experiment, not of this construction.

## What the ruling settles, and what it sharpens rather than settling

SETTLED: the builder. `qou-pdix`'s branch-3 acceptance test is now runnable
against a fixed object; the O(t) NF sensitivity established in the retraction
commit no longer blocks it, because there is now one NF.

SHARPENED, NOT SETTLED: with the builder fixed, the C-vs-D tension is exposed
rather than resolved. Bean entry (6)'s Kohno-Drinfeld consistency test — does
`alpha` look like a holonomy angle `c*ln q`, with `c` pinned at order `t^1` so
`t^2` is a prediction — now reads unambiguously:

    single-wrap C   t^1 -1/2   t^2 pred 1/4   actual 1/4    MATCH
    single-wrap D   t^1 -1/2   t^2 pred 1/4   actual 5/4    FAILS

**Under the canonical builder AND the canonical convention D, the ladder phase
fails the holonomy acceptance test at second order.** That was recorded in entry
(6) as a "tension with the ruling"; with the builder ambiguity removed it is no
longer attributable to a modelling choice.

And the residual does not close either: at the proton pin, single-wrap C leaves
14.5% of the required N=1 correction unexplained and single-wrap D leaves 48.9%.
The ruling picks the object; it does not close the ladder.

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

    # ---- the OWNER RULING: single-wrap is canonical. Record it as assertions.
    checks.append((
        "canonical_builder_is_single_wrap",
        "single_wrap" in rows,
        "owner ruling 2026-08-30: single-wrap — A=1, no gluon, no electron",
    ))
    checks.append((
        "canonical_alpha_is_negative",
        mp.mpf(rows["single_wrap"]["alpha_C"]) < 0,
        "the canonical builder gives a NEGATIVE phase; the gluon+electron "
        "builder's positive one belongs to a different system",
    ))

    # ---- with the builder fixed, the C vs D holonomy test reads unambiguously
    import sympy as sp
    t = sp.Symbol("t")
    hs = sp.Symbol("h")
    q_t = 1 + t
    h_t = sp.simplify(q_t - 1 / q_t)
    sw_sym = [hs**2 / 2, -hs / 2, -hs / 2, 0, 0, 0]
    zsym = sp.Symbol("zs")

    def alpha_coeffs(zexpr):
        eps_s = sp.expand(sum(sw_sym))
        tr_s = sp.expand(sum(c * zsym**k for c, k in zip(sw_sym, CR)))
        a = sp.simplify((eps_s - tr_s) / 2)
        ser = sp.expand(sp.nsimplify(sp.series(
            a.subs({zsym: zexpr, hs: h_t}), t, 0, 4).removeO()))
        return [sp.nsimplify(sp.simplify(ser.coeff(t, k))) for k in (1, 2)]

    cC = alpha_coeffs(sp.sqrt(q_t) / (q_t + 1))
    cD = alpha_coeffs(q_t**3 / (q_t**2 + 1))
    # c*ln q prediction: t^2 coefficient is -c1/2
    checks.append((
        "single_wrap_C_passes_holonomy_t2_test",
        cC[1] == -cC[0] / 2,
        f"C: t^2 = {cC[1]}, prediction {-cC[0]/2} — MATCH",
    ))
    checks.append((
        "single_wrap_D_FAILS_holonomy_t2_test",
        cD[1] != -cD[0] / 2,
        f"D: t^2 = {cD[1]}, prediction {-cD[0]/2} — FAILS, and with the "
        f"builder now fixed this is not attributable to a modelling choice",
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
        "OWNER RULING 2026-08-30: single-wrap is canonical for the Q_beta "
        "channel — 'it's A=1, no gluon, no electron'. Three live nucleon-NF "
        "builders give three different Q_beta N=1 "
        "phases, spanning a SIGN CHANGE: single-wrap -0.05234, "
        "build_nucleon_nf (9 crossings, self-declared defective) -0.03541, "
        "build_atom_nf (gluon-complete, neutron-minus-hydrogen) +0.23558, all "
        "at convention C and the proton pin. The first two undershoot the "
        "required N=1 factor 0.99839767; the third overshoots by ~16x. They "
        "are three different SYSTEMS, not three bases, so this is not a "
        "convention ambiguity. The qou-pdix gate on branch 3 is therefore far "
        "worse than the 0.58% counit ratio the bean records. RESOLVED by the "
        "ruling: single-wrap. The corpus split (Q_beta chain on single-wrap, "
        "mass compute on build_atom_nf) is therefore CORRECT — different "
        "systems, each used where it belongs — not an inconsistency. With the "
        "builder fixed, single-wrap C passes the entry-6 holonomy t^2 test "
        "(1/4 = 1/4) and single-wrap D FAILS it (5/4 vs 1/4), so the C-vs-D "
        "tension is now exposed rather than attributable to a modelling "
        "choice. The ruling picks the object; it does not close the ladder "
        "(C still leaves 14.5% of the required correction unexplained).")
    w.set_content_block("prop:q-beta-cos-resummation")
    w.add_parameter("q0_anchor", "proton (physical_proton pin)")
    w.add_parameter("required_N1_factor", str(REQUIRED_N1))
    w.add_data("assertions_passed", npass)
    w.add_data("assertions_total", len(checks))
    w.add_data("checks", [{"name": n, "pass": ok, "why": why}
                          for n, ok, why in checks])
    w.add_data("builders", rows)
    w.add_data("owner_ruling_2026_08_30", (
        "single-wrap is canonical for the Q_beta channel. Verbatim: "
        "\"single-wrap. it's A=1, no gluon, no electron\". Structural, not "
        "numerical: free-neutron beta decay is A=1, so the gluon dressing and "
        "electron that build_atom_nf carries describe a different system. Does "
        "NOT double-count the electron — the framework's Q_beta carries m_e as "
        "an explicit prefactor, so the emitted electron enters there, not "
        "inside the normal form."))
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
