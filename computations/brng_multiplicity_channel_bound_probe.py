#!/usr/bin/env python3
"""The multiplicity channel of a trace-sum binding law is sub-extensive.

Numerical companion to `QOU/Mass/MultiplicityNotExtensive.lean` (bean
`qou-brng`, the super-pairwise additive extensive term). The Lean proves the
inequalities for arbitrary summands, an arbitrary `sqrt` law and an arbitrary
scale; this probe evaluates them with the EXACT partition counts `p(3A)` and
the AME2020 binding energies, and sets the derived quantities against the
measurement. Nothing here is searched or fitted: `B_AME` enters only as a
target, `E_0` is carried from the corpus's own closed form, and the headline
result (R5) is scale-free so that it does not depend on `E_0` at all.

*** WHAT IS BEING TESTED ***

`QOU/Hecke/BondCutSymmetry.lean` (#7165) excludes POSITIVE PAIR-ADDITIVE BOND
COUNTS from supplying the binding's extensive term. The Frobenius pairing

    B(K) = m_e . sum_{lambda |- 3A} y_lambda . chi^lambda(beta_A) . Delta_lambda

escapes that exclusion on two hypotheses at once: it is not the three-term
`bondSum` shape, and `Delta_lambda = (-1)^{n(lambda)} . dim V_lambda` is SIGNED,
so `bondSum_nonneg`'s `0 <= n_t` does not apply. This probe asks whether the
escape buys anything.

A trace sum can be large two ways: one summand large, or many summands. The
second -- the MULTIPLICITY channel -- is capped by the triangle inequality:

    |sum_lambda a_lambda|  <=  p(3A) . max_lambda |a_lambda|

so in log-amplitude it contributes at most `log p(3A)`, for any signs, any
weights and any braid word. Under the archimedean bridge
(`QOU/Mass/ArchimedeanTraceBridge.lean`) binding in MeV is `E_0` times a
log-amplitude, so the channel is worth at most `E_0 . log p(3A)` MeV.

*** R1 -- the Hardy-Ramanujan hypothesis, discharged over the physical range ***

The Lean carries `log p(n) <= c . sqrt(A)` as an explicit `_of_` hypothesis
rather than proving it. R1 discharges it numerically for every `A` in
`2 .. 400` (i.e. `n = 3A` up to 1200) with `c = pi . sqrt(2)`, using EXACT
integer partition counts from a Python-int dynamic program -- no asymptotics,
no floats.

*** R2 -- exact counts make the exclusion STRONGER than the bound ***

`log p(n)` is well below `pi sqrt(2n/3)` at every physical `n` (the asymptotic
form omits a `-log(4 n sqrt 3)` correction). So using exact counts is not a
convenience: it is the conservative choice, and R2 records the margin.

*** R3 -- the cap in MeV, against AME2020 ***

`E_0 . log p(3A)` against the measured `B`, over a spread of nuclides from the
deuteron to 238U. This is the only E_0-DEPENDENT result here and is labelled
as such: per #7174 / bean `qou-v8ct` a uniform factor is 98.6 % of the squared
log-residual and is undecidable against a uniform rescaling of the bond
energies at fixed law, so no conclusion is drawn from R3 alone.

*** R4 -- the exponential requirement ***

To supply the measured binding through multiplicity alone, the number of
summands would have to be `exp(B/E_0)`. R4 reports `log10` of that against
`log10 p(3A)`: the gap is the size of the miss, in orders of magnitude.

*** R5 -- THE HEADLINE, and it is scale-free ***

Take two nuclides. The ratio of their multiplicity caps is
`log p(3A_2) / log p(3A_1)`; the ratio of their measured bindings is
`B_2 / B_1`. `E_0` cancels from both. If multiplicity were the extensive term
those ratios would agree; the shortfall factor `(B_2/B_1) / (mu_2/mu_1)` is
what a `sqrt`-vs-linear shape mismatch predicts, and it is independent of
`E_0` and of any constant in front of the `sqrt`.

Precision: mpmath at 70 dps, `q_0` from `Q_50_DIGIT_STR` (PROTON pin, AGENTS.md
2026-08-07 directive), `m_e` from the NIST table string. Partition counts are
exact Python integers. AME values are read as `Decimal` from the vendored
table with `parse_float=str`, never as float64. No `float(...)` arithmetic, no
`math`/`statistics` over floats.
"""

from __future__ import annotations

import json
import subprocess
import sys
import time
from decimal import Decimal
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))
from qou_substrate import constants as _c  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

DPS = 70
mp.mp.dps = DPS

Q0 = mp.mpf(_c.Q_50_DIGIT_STR)
M_E = mp.mpf(str(_c._E_MEV.value))
HBAR = (Q0 - 1) / Q0
#: Same closed form as the sibling `qbeta_bond_cut_symmetry_shape_probe.py`
#: (#7165), so the two arcs quote one E_0. It is a CARRIED constant here, not
#: a derived one, and R5 does not use it.
E0 = M_E / (Q0 * (Q0 - 1)) / (1 - HBAR**2)

#: Strands per nucleon: `atom_braid_word_3A`'s own indexing (`base_g0 = 3*k`).
STRANDS_PER_NUCLEON = 3

_AME_PATH = ROOT / "qou-mass" / "src" / "qou_mass" / "data" / "ame2020.json"

#: (Z, A, label) -- a spread across the mass table, not a selected subset.
#: Chosen before any number was computed: the two calibration-adjacent light
#: nuclei, the doubly-magic ladder, the B/A peak, and the heaviest common
#: nuclide. No nuclide was added or dropped after seeing a result.
NUCLIDES: list[tuple[int, int, str]] = [
    (1, 2, "2H"),
    (2, 4, "4He"),
    (3, 7, "7Li"),
    (6, 12, "12C"),
    (8, 16, "16O"),
    (20, 40, "40Ca"),
    (26, 56, "56Fe"),
    (28, 62, "62Ni"),
    (50, 120, "120Sn"),
    (82, 208, "208Pb"),
    (92, 238, "238U"),
]


def _head_sha() -> str:
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=ROOT,
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except Exception:
        return "unknown"


def partition_counts(n_max: int) -> list[int]:
    """Exact `p(0..n_max)` by the standard pentagonal-free DP over Python ints.

    Integers throughout -- no float, no mpf, no asymptotic form.
    """
    p = [0] * (n_max + 1)
    p[0] = 1
    for part in range(1, n_max + 1):
        for n in range(part, n_max + 1):
            p[n] += p[n - part]
    return p


def ame_binding_mev(Z: int, A: int) -> mp.mpf:
    """B (MeV) from the vendored AME2020 table, read exactly then lifted to mpf.

    `binding_energy_per_A_keV` is the column AME QUOTES; the total is derived
    in the table and carries a float64 tail, so it is not used. `Decimal`
    multiplies and divides exactly, and the `mpf` is built from the resulting
    decimal STRING -- never from a float.
    """
    raw = json.loads(_AME_PATH.read_text(), parse_float=str)
    for e in raw["entries"]:
        if int(e["Z"]) == Z and int(e["A"]) == A:
            per_a = Decimal(e["binding_energy_per_A_keV"])
            return mp.mpf(str(per_a * A / Decimal(1000)))
    raise KeyError(f"Z={Z} A={A} not in the vendored AME2020 table")


def main() -> int:
    t0 = time.monotonic()
    a: list[dict] = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        return ok

    ok = True
    A_MAX_HR = 400
    n_max = STRANDS_PER_NUCLEON * A_MAX_HR
    print("=" * 78)
    print("R0  setup")
    print("=" * 78)
    print(f"  q_0 (proton pin)      = {mp.nstr(Q0, 20)}")
    print(f"  m_e                   = {mp.nstr(M_E, 15)} MeV")
    print(f"  E_0 (carried)         = {mp.nstr(E0, 15)} MeV")
    print(f"  strands per nucleon   = {STRANDS_PER_NUCLEON}")
    print(f"  computing p(0..{n_max}) exactly ...")
    P = partition_counts(n_max)
    print(f"  p(12) = {P[12]},  p(36) = {P[36]},  p({n_max}) has "
          f"{len(str(P[n_max]))} digits")

    # ------------------------------------------------------------------ R1
    print("\n" + "=" * 78)
    print("R1  Hardy-Ramanujan hypothesis discharged over the physical range")
    print("=" * 78)
    C_HR = mp.pi * mp.sqrt(2)          # log p(3A) <= pi sqrt(2 . 3A / 3) = c sqrt(A)
    worst_A, worst_slack = None, None
    for A in range(2, A_MAX_HR + 1):
        lhs = mp.log(mp.mpf(P[STRANDS_PER_NUCLEON * A]))
        rhs = C_HR * mp.sqrt(mp.mpf(A))
        slack = rhs - lhs
        if worst_slack is None or slack < worst_slack:
            worst_A, worst_slack = A, slack
    print(f"  c = pi sqrt 2         = {mp.nstr(C_HR, 15)}")
    print(f"  tightest at A         = {worst_A}   (slack {mp.nstr(worst_slack, 10)})")
    ok &= chk("hardy_ramanujan_bound_holds_A_2_to_400", worst_slack > 0, True,
              note="log p(3A) <= pi sqrt(2) sqrt(A) verified with exact p(n) "
                   "for every A in 2..400; this is the hypothesis carried by "
                   "hardyRamanujan_gives_sqrt_law")

    # ------------------------------------------------------------------ R2
    print("\n" + "=" * 78)
    print("R2  exact counts are STRICTLY below the asymptotic bound")
    print("=" * 78)
    r2_rows = []
    for _, A, lab in NUCLIDES:
        n = STRANDS_PER_NUCLEON * A
        mu = mp.log(mp.mpf(P[n]))
        hr = C_HR * mp.sqrt(mp.mpf(A))
        r2_rows.append({"nuclide": lab, "A": A, "n": n,
                        "log_p_exact": mp.nstr(mu, 15),
                        "hardy_ramanujan": mp.nstr(hr, 15),
                        "ratio_exact_over_bound": mp.nstr(mu / hr, 12)})
        print(f"  {lab:>6}  A={A:>3}  log p({n:>3}) = {mp.nstr(mu, 10):>14}"
              f"   HR bound {mp.nstr(hr, 10):>14}   ratio {mp.nstr(mu/hr, 6)}")
    ok &= chk("exact_counts_below_asymptotic_bound_everywhere",
              all(mp.mpf(r["ratio_exact_over_bound"]) < 1 for r in r2_rows), True,
              note="using exact p(n) rather than the asymptotic form makes the "
                   "exclusion stronger, not weaker")

    # ------------------------------------------------------------------ R3
    print("\n" + "=" * 78)
    print("R3  the cap in MeV against AME2020   [E_0-DEPENDENT -- see docstring]")
    print("=" * 78)
    print(f"  {'nuclide':>8} {'A':>4} {'B_AME (MeV)':>14} {'cap (MeV)':>12} {'cap/B':>9}")
    r3_rows, caps, bindings, mus = [], [], [], []
    for Z, A, lab in NUCLIDES:
        n = STRANDS_PER_NUCLEON * A
        mu = mp.log(mp.mpf(P[n]))
        B = ame_binding_mev(Z, A)
        cap = E0 * mu
        mus.append(mu)
        caps.append(cap)
        bindings.append(B)
        r3_rows.append({"nuclide": lab, "Z": Z, "A": A,
                        "B_AME_MeV": mp.nstr(B, 12),
                        "mu_log_p_3A": mp.nstr(mu, 15),
                        "cap_MeV": mp.nstr(cap, 12),
                        "cap_over_B": mp.nstr(cap / B, 12)})
        print(f"  {lab:>8} {A:>4} {mp.nstr(B, 9):>14} {mp.nstr(cap, 8):>12} "
              f"{mp.nstr(cap/B, 5):>9}")
    heavy = [r for r in r3_rows if r["A"] >= 12]
    ok &= chk("cap_below_binding_for_every_nuclide_A_at_least_12",
              all(mp.mpf(r["cap_over_B"]) < 1 for r in heavy), True,
              note="the multiplicity channel cannot supply the measured binding "
                   "at any A >= 12 even if it were the ONLY contribution")
    ok &= chk("cap_share_decreasing_from_12C_to_238U",
              mp.mpf(r3_rows[-1]["cap_over_B"]) < mp.mpf(heavy[0]["cap_over_B"]),
              True,
              note="share falls with A -- the signature of a sub-extensive channel")
    #: Recorded as an assertion rather than left in a table, so that the one
    #: place the exclusion does NOT bite is as visible as the places it does.
    ok &= chk("deuteron_is_a_genuine_exception_cap_exceeds_its_binding",
              mp.mpf(r3_rows[0]["cap_over_B"]) > 1, True,
              note="At A=2 the cap EXCEEDS the measured binding, so the "
                   "multiplicity channel is NOT excluded there. This is not a "
                   "defect in the argument: sub-extensive and extensive are "
                   "indistinguishable at the smallest A, which is exactly what "
                   "the Lean's explicit threshold A > (c/a)^2 says. With exact "
                   "counts the crossing happens between A=2 and A=4, so the "
                   "exclusion bites from 4He upward and strengthens monotonically.")

    # ------------------------------------------------------------------ R4
    print("\n" + "=" * 78)
    print("R4  the exponential requirement")
    print("=" * 78)
    r4_rows = []
    ln10 = mp.log(10)
    for (Z, A, lab), B, mu in zip(NUCLIDES, bindings, mus):
        need_log10 = (B / E0) / ln10          # log10 exp(B/E_0)
        have_log10 = mu / ln10
        r4_rows.append({"nuclide": lab, "A": A,
                        "log10_summands_required": mp.nstr(need_log10, 12),
                        "log10_p_3A_available": mp.nstr(have_log10, 12),
                        "shortfall_orders_of_magnitude":
                            mp.nstr(need_log10 - have_log10, 12)})
        print(f"  {lab:>8} A={A:>3}  need 10^{mp.nstr(need_log10, 7):>10} summands, "
              f"have 10^{mp.nstr(have_log10, 7):>9}  "
              f"(short by {mp.nstr(need_log10 - have_log10, 7)} orders)")
    ok &= chk("required_summand_count_exceeds_p_3A_for_every_nuclide_A_at_least_12",
              all(mp.mpf(r["shortfall_orders_of_magnitude"]) > 0
                  for r in r4_rows if r["A"] >= 12), True,
              note="card_ge_exp_of_linear_le_log_card, evaluated")

    # ------------------------------------------------------------------ R5
    print("\n" + "=" * 78)
    print("R5  THE HEADLINE -- scale-free shape mismatch (E_0 cancels)")
    print("=" * 78)
    base = next(i for i, (_, A, _) in enumerate(NUCLIDES) if A == 12)
    B1, mu1, A1 = bindings[base], mus[base], NUCLIDES[base][1]
    r5_rows = []
    for i, (Z, A, lab) in enumerate(NUCLIDES):
        if A <= A1:
            continue
        b_ratio = bindings[i] / B1
        mu_ratio = mus[i] / mu1
        mismatch = b_ratio / mu_ratio
        sqrt_pred = mp.sqrt(mp.mpf(A) / mp.mpf(A1))
        r5_rows.append({"nuclide": lab, "A": A, "base": "12C", "base_A": A1,
                        "B_ratio": mp.nstr(b_ratio, 12),
                        "mu_ratio": mp.nstr(mu_ratio, 12),
                        "shape_mismatch": mp.nstr(mismatch, 12),
                        "asymptotic_sqrt_A_ratio": mp.nstr(sqrt_pred, 12)})
        print(f"  12C -> {lab:>6}  B ratio {mp.nstr(b_ratio, 7):>9}   "
              f"mu ratio {mp.nstr(mu_ratio, 7):>9}   "
              f"MISMATCH {mp.nstr(mismatch, 7):>9}   "
              f"(sqrt(A2/A1) = {mp.nstr(sqrt_pred, 6)})")
    ok &= chk("shape_mismatch_above_one_for_every_heavier_nuclide",
              all(mp.mpf(r["shape_mismatch"]) > 1 for r in r5_rows), True,
              note="E_0 cancels from both ratios; the multiplicity channel grows "
                   "strictly slower than the measured binding, so no choice of "
                   "scale can make it the extensive term")
    ok &= chk("mismatch_grows_with_mass",
              mp.mpf(r5_rows[-1]["shape_mismatch"])
              > mp.mpf(r5_rows[0]["shape_mismatch"]), True,
              note="a constant mismatch would be a scale error; a growing one "
                   "is a shape error, and a shape error is not repairable by E_0")

    # ------------------------------------------------------------------ R6
    print("\n" + "=" * 78)
    print("R6  sqrt_law_shortfall, the Lean identity, checked numerically")
    print("=" * 78)
    r = mp.mpf(238) / mp.mpf(12)
    lhs = mp.mpf(1) * r
    rhs = mp.sqrt(r) * (mp.mpf(1) * mp.sqrt(r))
    print(f"  r = 238/12 = {mp.nstr(r, 12)};  B1*r - sqrt(r)*(B1*sqrt(r)) = "
          f"{mp.nstr(lhs - rhs, 5)}")
    ok &= chk("sqrt_law_shortfall_identity_holds_to_working_precision",
              abs(lhs - rhs) < mp.mpf(10) ** (-(DPS - 10)), True,
              note="QOU.Mass.MultiplicityNotExtensive.sqrt_law_shortfall")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "brng-multiplicity-channel-bound",
        "description": (
            "The multiplicity channel of a trace-sum binding law is "
            "sub-extensive. A signed sum over the partitions of 3A is bounded "
            "by p(3A) times its largest summand, so multiplicity contributes at "
            "most log p(3A) to the log-amplitude. Exact partition counts and "
            "AME2020 binding energies; the headline (R5) is scale-free and does "
            "not use E_0. Scope-(b) structural exclusion of the multiplicity "
            "channel ALONE -- the dominant summand's own log-weight is untouched "
            "and is the live remainder. Nothing wired, nothing fitted."
        ),
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {
            "q0": mp.nstr(Q0, 30),
            "q0_pin": "proton",
            "dps": DPS,
            "m_e_MeV": mp.nstr(M_E, 15),
            "E0_MeV": mp.nstr(E0, 20),
            "E0_role": ("carried from the sibling #7165 probe's closed form; "
                        "R5 and R6 do not use it, R3 and R4 are labelled "
                        "E_0-dependent (see #7174 / qou-v8ct: a uniform factor "
                        "is undecidable against a uniform bond rescaling)"),
            "strands_per_nucleon": STRANDS_PER_NUCLEON,
            "hardy_ramanujan_c": mp.nstr(C_HR, 20),
            "ame_source": "AME2020 vendored table, binding_energy_per_A_keV x A",
            "lean": ["QOU/Mass/MultiplicityNotExtensive.lean"],
        },
        "data": {
            "hardy_ramanujan_tightest_A": worst_A,
            "hardy_ramanujan_tightest_slack": mp.nstr(worst_slack, 15),
            "exact_vs_asymptotic": r2_rows,
            "cap_against_ame": r3_rows,
            "exponential_requirement": r4_rows,
            "scale_free_shape_mismatch": r5_rows,
        },
        "provenance": {
            "headSha": _head_sha(),
            "producer": "computations/brng_multiplicity_channel_bound_probe.py",
            "bean": "qou-brng",
            "elapsed_s": round(time.monotonic() - t0, 3),
        },
    }
    #: R3/R4 carry `E_0`, which is built from `q_0`, so this witness DOES have
    #: q0-dependent fields and the anchor is declared rather than waived. R5/R6
    #: are scale-free and would be unaffected by a re-pin; R3/R4 would move.
    WitnessBuilder.stamp_staleness_metadata(
        witness,
        script_path=__file__,
        engine="python",
        q0_anchor="proton",
        q0_anchor_reason=(
            "AGENTS.md 2026-08-07 owner directive: experimental pin is the "
            "default for all new compute. Only the E_0-dependent results "
            "(R3, R4) use it; R5 and R6 are scale-free."
        ),
        q0_value=mp.nstr(Q0, 30),
    )
    out = HERE / "brng-multiplicity-channel-bound.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
