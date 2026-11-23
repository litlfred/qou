#!/usr/bin/env python3
"""faddeev_niemi_qh34_binding_prereg_probe.py — pre-registered test of the
Faddeev-Niemi |Q_H|^{3/4} energy class against the QOU binding gap.

PRE-REGISTRATION: docs/audits/2026-08-26-faddeev-niemi-prereg.md, committed at
d3819883225e50cb66a59efa3f7f1676ac2bd4ae BEFORE this file was written.  Every
criterion below (isotope set, three forms per target, fit rule, support and
refutation bounds) is fixed by that document.  Nothing here may be added to it.

Claim under test
----------------
Faddeev-Niemi (library/arxiv-hep-th-9610193v1) record the Vakulenko-Kapitanski
bound H >= c |Q_H|^{3/4} on the Faddeev-model Hamiltonian, Q_H the Hopf
invariant.  Hypothesis H: the missing QOU binding term has that form, with one
global constant c and a Q_H fixed by topology ahead of the data.

Three forms per target, and no fourth:
    F1  B = c A^{3/4}   (1 param)  Q_H ~ A    -- chain-like linking, degree 1
    F2  B = c A^{3/2}   (1 param)  Q_H ~ A^2  -- quadratic self-linking / flux
    F3  B = c A^{p}     (2 param)  over-permissive superset; bounds the class

Targets: primary B_AME (vendored AME2020, exact route); secondary the residual
R = B_AME - B_sym over the six B_sym/A values RECORDED in
docs/audits/2026-08-25-low-isotope-binding-error-staleness-vs-gap.md section 4
(read from that committed audit, NOT recomputed here -- so labelled).

Fit rule (pre-registered, closed form, no optimiser): least squares in log
space.  F1/F2: ln c = mean_i(ln B_i - p ln A_i).  F3: linear regression of
ln B on ln A.

Structural prediction S1, also pre-registered and itself at risk: for any real
p, B = c A^p gives B/A = c A^{p-1}, strictly monotone for p != 1 and constant
for p = 1, while the empirical B_AME/A is non-monotone with an interior maximum
near A = 56.  Hence no pure power law reproduces the measured A-dependence and
S-ii cannot be met by any p.  S1 is FALSIFIED, and retracted in the report, if
F3 reaches <= 0.10 max relative residual.

Precision: mpmath.mpf end to end at 60 dps.  No float64 anywhere; float() only
inside f-strings for display.  No statistics.mean over floats.

Usage:  python3 computations/probes/faddeev_niemi_qh34_binding_prereg_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import _path_bridge  # noqa: F401,E402 -- Phase 6 bridge
import mpmath as mp  # noqa: E402

from codata_constants import ame_binding_mev  # noqa: E402

DPS = 60

#: Pre-registered isotope set, (Z, A, label).  Fixed in the prereg; not edited.
NUCLIDES: list[tuple[int, int, str]] = [
    (1, 2, "2H"), (1, 3, "3H"), (2, 3, "3He"), (2, 4, "4He"),
    (3, 6, "6Li"), (3, 7, "7Li"), (4, 9, "9Be"), (5, 11, "11B"),
    (6, 12, "12C"), (7, 14, "14N"), (8, 16, "16O"), (12, 24, "24Mg"),
    (14, 28, "28Si"), (20, 40, "40Ca"), (26, 56, "56Fe"), (28, 58, "58Ni"),
    (50, 120, "120Sn"), (82, 208, "208Pb"), (92, 238, "238U"),
]

#: B_sym/A in MeV/nucleon, READ FROM the committed audit
#: docs/audits/2026-08-25-low-isotope-binding-error-staleness-vs-gap.md section 4.
#: These are NOT recomputed here.  Strings -> mpf; never float literals.
B_SYM_PER_A_FROM_AUDIT: dict[str, str] = {
    "2H": "1.416", "4He": "2.170", "12C": "2.673",
    "56Fe": "2.898", "208Pb": "2.991", "238U": "2.998",
}

# Pre-registered decision bounds.
mp.mp.dps = max(DPS, mp.mp.dps)
SUPPORT_MAX_REL = mp.mpf("0.10")
REFUTE_MAX_REL = mp.mpf("0.25")
P_WINDOW = (mp.mpf("0.70"), mp.mpf("0.80"))


def _mean(xs: list[mp.mpf]) -> mp.mpf:
    """Arithmetic mean in mpf.  Not statistics.mean -- that accumulates in float."""
    return mp.fsum(xs) / mp.mpf(len(xs))


def fit_fixed_exponent(A: list[mp.mpf], B: list[mp.mpf], p: mp.mpf) -> mp.mpf:
    """Log-space least squares for B = c A^p with p held fixed.  Returns c."""
    return mp.e ** _mean([mp.log(b) - p * mp.log(a) for a, b in zip(A, B)])


def fit_free_exponent(A: list[mp.mpf], B: list[mp.mpf]) -> tuple[mp.mpf, mp.mpf]:
    """Closed-form regression of ln B on ln A.  Returns (c, p)."""
    x = [mp.log(a) for a in A]
    y = [mp.log(b) for b in B]
    xbar, ybar = _mean(x), _mean(y)
    num = mp.fsum([(xi - xbar) * (yi - ybar) for xi, yi in zip(x, y)])
    den = mp.fsum([(xi - xbar) ** 2 for xi in x])
    p = num / den
    return mp.e ** (ybar - p * xbar), p


def max_rel_residual(A: list[mp.mpf], B: list[mp.mpf],
                     c: mp.mpf, p: mp.mpf) -> tuple[mp.mpf, int]:
    """max_i |c A_i^p / B_i - 1|, and the index attaining it."""
    rels = [abs(c * a ** p / b - 1) for a, b in zip(A, B)]
    worst = max(range(len(rels)), key=lambda i: rels[i])
    return rels[worst], worst


def sign_obstruction(B: list[mp.mpf], labels: list[str]) -> list[str]:
    """Rows where the target is <= 0.

    NOT anticipated by the pre-registration, and it is the stronger result.
    The Faddeev Hamiltonian H = int (g/2)(d n)^2 + e^2 F^2 is a sum of squares,
    hence H >= 0, and the Vakulenko-Kapitanski bound H >= c|Q_H|^{3/4} has
    c > 0, so c|Q_H|^{3/4} >= 0 identically.  A non-negative functional cannot
    equal a target that changes sign -- no choice of c or Q_H repairs it.  This
    is the same shape as the KL-positivity prune AGENTS.md licenses as a
    scope-(b) exclusion: a mixed-sign target against a provably non-negative
    weight.  Reported, never silently dropped.
    """
    return [lab for lab, b in zip(labels, B) if b <= 0]


def run_target(name: str, labels: list[str], A: list[mp.mpf],
               B: list[mp.mpf], source_note: str) -> dict:
    print(f"\n{'=' * 74}\nTARGET: {name}\n  source: {source_note}\n"
          f"  n = {len(A)} nuclides\n{'=' * 74}")

    out: dict = {"target": name, "n": len(A), "forms": {}}

    neg = sign_obstruction(B, labels)
    out["sign_obstruction"] = neg
    if neg:
        print(f"\n  *** SIGN OBSTRUCTION -- target is non-positive at: "
              f"{', '.join(neg)}")
        print("  c|Q_H|^(3/4) >= 0 for every c > 0 and every Q_H (the Faddeev")
        print("  Hamiltonian is a sum of squares; Vakulenko-Kapitanski bounds it")
        print("  from BELOW by a non-negative quantity).  A mixed-sign target is")
        print("  therefore unreachable by the class for ANY c and ANY Q_H.")
        print("  => REFUTED on sign, scope (b), invariant = non-negativity of the")
        print("     Faddeev energy.  The log-space fits below are UNDEFINED on a")
        print("     negative target (ln of a negative is complex); their numbers")
        print("     are NOT reported and must not be quoted.")
        out["verdict"] = "REFUTE (b) -- sign"
        return out

    for tag, p_fixed in (("F1  B = c A^(3/4)", mp.mpf(3) / 4),
                         ("F2  B = c A^(3/2)", mp.mpf(3) / 2)):
        c = fit_fixed_exponent(A, B, p_fixed)
        rel, i = max_rel_residual(A, B, c, p_fixed)
        verdict = ("SUPPORT" if rel <= SUPPORT_MAX_REL
                   else "REFUTE (R-i)" if rel > REFUTE_MAX_REL else "inconclusive band")
        print(f"\n{tag}   [1 free param]")
        print(f"  c            = {mp.nstr(c, 12)}")
        print(f"  max rel resid= {mp.nstr(rel, 8)}  at {labels[i]}")
        print(f"  S-i (<= 0.10): {verdict}")
        out["forms"][tag.split()[0]] = {"c": mp.nstr(c, 15),
                                        "max_rel": mp.nstr(rel, 10),
                                        "worst": labels[i], "verdict": verdict}

    c, p = fit_free_exponent(A, B)
    rel, i = max_rel_residual(A, B, c, p)
    p_ok = P_WINDOW[0] <= p <= P_WINDOW[1]
    r_ok = rel <= SUPPORT_MAX_REL
    verdict = "SUPPORT (S-ii)" if (p_ok and r_ok) else "REFUTE"
    reasons = []
    if not p_ok:
        reasons.append("R-ii: p outside [0.70, 0.80]")
    if rel > REFUTE_MAX_REL:
        reasons.append("R-i: max rel resid > 0.25")
    elif not r_ok:
        reasons.append("S-ii residual bound 0.10 not met")
    print(f"\nF3  B = c A^p   [2 free params -- MORE freedom than H allows]")
    print(f"  p            = {mp.nstr(p, 12)}   window [0.70, 0.80]: "
          f"{'IN' if p_ok else 'OUT'}")
    print(f"  c            = {mp.nstr(c, 12)}")
    print(f"  max rel resid= {mp.nstr(rel, 8)}  at {labels[i]}")
    print(f"  verdict      : {verdict}" + (f"  [{'; '.join(reasons)}]" if reasons else ""))
    out["forms"]["F3"] = {"c": mp.nstr(c, 15), "p": mp.nstr(p, 15),
                          "max_rel": mp.nstr(rel, 10), "worst": labels[i],
                          "p_in_window": p_ok, "verdict": verdict,
                          "reasons": reasons}

    # S1 premise check: is B/A non-monotone with an interior maximum?
    per_a = [b / a for a, b in zip(A, B)]
    imax = max(range(len(per_a)), key=lambda i: per_a[i])
    interior = 0 < imax < len(per_a) - 1
    rises = any(per_a[i + 1] > per_a[i] for i in range(len(per_a) - 1))
    falls = any(per_a[i + 1] < per_a[i] for i in range(len(per_a) - 1))
    print(f"\n  S1 premise -- shape of (target)/A:")
    print(f"    max at {labels[imax]} = {mp.nstr(per_a[imax], 8)} MeV/nucleon; "
          f"interior maximum: {interior}")
    print(f"    rises somewhere: {rises};  falls somewhere: {falls}  "
          f"=> non-monotone: {rises and falls}")
    print(f"    S1 falsified by F3 reaching <= 0.10? "
          f"{'YES -- RETRACT S1' if r_ok else 'no -- S1 stands'}")
    out["s1"] = {"argmax": labels[imax], "max_per_A": mp.nstr(per_a[imax], 10),
                 "interior_max": interior, "non_monotone": rises and falls,
                 "s1_falsified": bool(r_ok)}
    return out


def main() -> int:
    mp.mp.dps = DPS

    labels = [lab for _, _, lab in NUCLIDES]
    A_all = [mp.mpf(a) for _, a, _ in NUCLIDES]
    B_all = [ame_binding_mev(z, a) for z, a, _ in NUCLIDES]

    print(f"Faddeev-Niemi |Q_H|^(3/4) -- PRE-REGISTERED probe   (mpmath dps={DPS})")
    print(f"prereg: docs/audits/2026-08-26-faddeev-niemi-prereg.md @ d3819883225e")
    print(f"\n{'iso':>7} {'A':>5} {'B_AME (MeV)':>16} {'B_AME/A':>12}")
    for lab, a, b in zip(labels, A_all, B_all):
        print(f"{lab:>7} {int(a):>5} {mp.nstr(b, 10):>16} {mp.nstr(b / a, 8):>12}")

    res_primary = run_target(
        "PRIMARY -- total binding B_AME",
        labels, A_all, B_all,
        "codata_constants.ame_binding_mev -> vendored AME2020 table (exact)")

    # Secondary: residual R = B_AME - B_sym on the six audit-recorded rows.
    sec = [(lab, a, b) for lab, a, b in zip(labels, A_all, B_all)
           if lab in B_SYM_PER_A_FROM_AUDIT]
    sec_labels = [lab for lab, _, _ in sec]
    sec_A = [a for _, a, _ in sec]
    sec_R = [b - mp.mpf(B_SYM_PER_A_FROM_AUDIT[lab]) * a for lab, a, b in sec]
    print(f"\n{'iso':>7} {'A':>5} {'B_sym/A (audit)':>16} {'R = B_AME-B_sym':>18} {'R/A':>10}")
    for lab, a, r in zip(sec_labels, sec_A, sec_R):
        print(f"{lab:>7} {int(a):>5} {B_SYM_PER_A_FROM_AUDIT[lab]:>16} "
              f"{mp.nstr(r, 9):>18} {mp.nstr(r / a, 7):>10}")

    res_secondary = run_target(
        "SECONDARY -- residual R = B_AME - B_sym",
        sec_labels, sec_A, sec_R,
        "B_AME exact; B_sym/A READ FROM committed audit 2026-08-25 section 4 "
        "(not recomputed)")

    # --- POST-HOC, NOT PRE-REGISTERED -------------------------------------
    # The secondary target is mixed-sign, so the pre-registered fit is undefined
    # there.  Restricting to the rows where R > 0 is a DEVIATION from the
    # pre-registration and is reported here for completeness ONLY.  It is stated
    # in advance of reading it that this check cannot count as support: a subset
    # chosen after seeing which rows broke the fit is exactly the freedom the
    # pre-registration exists to remove.  It is shown because it also refutes.
    pos = [(lab, a, r) for lab, a, r in zip(sec_labels, sec_A, sec_R) if r > 0]
    if pos and len(pos) < len(sec_R):
        print(f"\n{'=' * 74}\nPOST-HOC (NOT pre-registered; cannot count as "
              f"support)\n  residual R restricted to the {len(pos)} rows with "
              f"R > 0\n{'=' * 74}")
        res_posthoc = run_target(
            "POST-HOC -- R on positive rows only",
            [x[0] for x in pos], [x[1] for x in pos], [x[2] for x in pos],
            "DEVIATION from prereg; reported only because it also refutes")
    else:
        res_posthoc = None

    print(f"\n{'=' * 74}\nPRE-REGISTERED VERDICT\n{'=' * 74}")
    for res in (res_primary, res_secondary, res_posthoc):
        if res is None:
            continue
        if res.get("sign_obstruction"):
            print(f"\n{res['target']}")
            print(f"  REFUTED on SIGN, scope (b).  Target is non-positive at "
                  f"{', '.join(res['sign_obstruction'])};")
            print(f"  c|Q_H|^(3/4) >= 0 identically.  No fit was performed.")
            continue
        f3 = res["forms"]["F3"]
        print(f"\n{res['target']}")
        for k in ("F1", "F2"):
            print(f"  {k}: max rel {res['forms'][k]['max_rel']:>14}  "
                  f"-> {res['forms'][k]['verdict']}")
        print(f"  F3: p = {f3['p']:>18}  max rel {f3['max_rel']:>14}  -> {f3['verdict']}")
        print(f"  S1: non-monotone target/A = {res['s1']['non_monotone']}; "
              f"S1 falsified = {res['s1']['s1_falsified']}")

    print("\nNo witness is emitted: this probe tests a literature-class hypothesis "
          "against\nrecorded data and wires nothing to production.  Per AGENTS.md "
          "the precision\ndiscipline applies regardless.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
