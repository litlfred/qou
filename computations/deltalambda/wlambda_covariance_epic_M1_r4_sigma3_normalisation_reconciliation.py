#!/usr/bin/env python3
"""R_4 vs omega3: the two corpus readings RECONCILED, from characters.

Gap qou-k5r5.  The corpus carries two formulas for the free cumulant R_4 and
labels one of them "naive":

    Lean r4Value                     R_4 = 3*omega3 - n     (recorded TRUE)
    "naive Sigma_3 = R_4 + R_2"      R_4 =   omega3 - n     (recorded FALSE)

`wlambda_covariance_epic_M1_A1_sigmah_in_free_cumulants.py` settles WHICH holds
by exact arithmetic over the transition measure.  It does not settle WHY the
other fails, and the wording it leaves behind reads as though Biane/Kerov's
identity `Sigma_3 = R_4 + R_2` were itself wrong.  That reading is what this
probe exists to refute, because it is the more damaging of the two errors: an
agent who believes the textbook identity is false in this corpus will avoid the
whole Kerov-polynomial apparatus.

WHAT IS ACTUALLY WRONG.  Nothing, in the identity.  The corpus's `omega3` is
NOT `Sigma_3`.  They differ by the class-size convention:

    Sigma_3(lam) := (n)_3 * chi^lam(3-cyc) / f^lam        falling factorial
    omega3(lam)  := sum_cells c^2 - C(n,2)                as the corpus defines it
    |C_{(3,1^{n-3})}| = (n)_3 / 3                          <- the factor of 3

so `Sigma_3 = 3 * omega3`, and substituting `omega3` where `Sigma_3` belongs
divides R_4's omega3-coefficient by 3.  That substitution is the defect; the
identity is untouched.

WHAT THIS PROBE MEASURES, from CHARACTERS rather than from either recorded
formula, so it is independent of both:

  1. chi^lam(3-cyc, 1^{n-3}) by Murnaghan-Nakayama (exact integers), and f^lam
     by the hook-length formula;
  2. Sigma_3 := (n)_3 * chi / f;
  3. R_2, R_4 from the transition measure (imported from the A1 probe, so the
     free-cumulant machinery is the corpus's own, not a second implementation);
  4. the four claims below.

Claims A and B are the reconciliation.  C is the Lean form, and it is DERIVED
here (A + B => C) rather than re-asserted -- which is the point: the two live
formulas are one identity plus one normalisation, not two rival conventions.
D exhibits the failing substitution so the record shows what "naive" meant.

NO float anywhere (Fraction end to end).  scope-(a); no fit; nothing wired; no
c_k; L2 unchanged.  Gap qou-k5r5 stays OPEN -- this fixes a definition, not the
gap.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys
from fractions import Fraction as F

_HERE = pathlib.Path(__file__).resolve().parent


def _load_a1():
    """Import the A1 probe for transition_atoms / free_cumulants / omega3.

    Reusing the corpus's own free-cumulant code is deliberate: a second
    implementation could agree with my reading of R_4 and disagree with the
    corpus's, which would prove nothing about the corpus.
    """
    src = _HERE / "wlambda_covariance_epic_M1_A1_sigmah_in_free_cumulants.py"
    spec = importlib.util.spec_from_file_location("_m1_a1_free_cumulants", src)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield []
        return
    for p in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - p, p):
            yield [p] + rest


def hook_dim(lam):
    """f^lam by the hook-length formula (exact integer)."""
    if not lam:
        return 1
    n = sum(lam)
    conj = [0] * lam[0]
    for p in lam:
        for j in range(p):
            conj[j] += 1
    num = 1
    for k in range(1, n + 1):
        num *= k
    den = 1
    for i, p in enumerate(lam):
        for j in range(p):
            den *= (p - j) + (conj[j] - i) - 1
    assert num % den == 0
    return num // den


def _rim_hooks(lam, size):
    """Yield (mu, height) for every removable rim hook of the given size.

    Uses the beta-number (first-column hook lengths) form of Murnaghan-Nakayama:
    removing a rim hook of length r is subtracting r from one beta-number, if
    the result is non-negative and not already present.  The height is the
    number of beta-numbers strictly between the new and old value.
    """
    lam = [p for p in lam if p > 0]
    k = len(lam)
    beta = [lam[i] + (k - 1 - i) for i in range(k)]
    out = []
    for i, b in enumerate(beta):
        nb = b - size
        if nb < 0 or nb in beta:
            continue
        newbeta = sorted((beta[:i] + beta[i + 1:]) + [nb], reverse=True)
        ht = sum(1 for x in beta if nb < x < b)
        m = len(newbeta)
        mu = [newbeta[j] - (m - 1 - j) for j in range(m)]
        mu = [p for p in mu if p > 0]
        out.append((mu, ht))
    return out


def chi_three_cycle(lam):
    """chi^lam on the class (3, 1^{n-3}), exact integer, by Murnaghan-Nakayama.

    One rim hook of length 3 is removed; the remainder is evaluated on the
    identity class, where the character is the dimension.
    """
    total = 0
    for mu, ht in _rim_hooks(lam, 3):
        total += (-1) ** ht * hook_dim(mu)
    return total


def sigma3_from_characters(lam):
    """Sigma_3 = (n)_3 * chi^lam(3-cyc) / f^lam, exact Fraction."""
    n = sum(lam)
    falling = n * (n - 1) * (n - 2)
    return F(falling * chi_three_cycle(lam), hook_dim(lam))


def main() -> int:
    a1 = _load_a1()
    NMAX = 8

    rows = []
    for n in range(3, NMAX + 1):
        for lam in partitions(n):
            atoms = a1.transition_atoms(lam)
            _, R, _ = a1.free_cumulants(atoms, 4)
            rows.append({
                "lam": tuple(lam), "n": n,
                "R2": R[2], "R4": R[4],
                "omega3": a1.omega3(lam, n),
                "Sigma3": sigma3_from_characters(lam),
            })

    print("=" * 78)
    print("  R_4 vs omega3 — the two readings reconciled, measured from characters")
    print("=" * 78)
    print(f"# {len(rows)} partitions, n = 3..{NMAX}; Fraction end to end, no float")
    print(f"# {'lam':<18}{'n':>3}{'Sigma_3':>10}{'3*omega3':>10}{'R_4+R_2':>10}"
          f"{'3o3-n':>8}{'o3-n':>8}{'R_4':>8}")
    for r in rows[:12]:
        print(f"# {str(list(r['lam'])):<18}{r['n']:>3}{str(r['Sigma3']):>10}"
              f"{str(3 * r['omega3']):>10}{str(r['R4'] + r['R2']):>10}"
              f"{str(3 * r['omega3'] - r['n']):>8}{str(r['omega3'] - r['n']):>8}"
              f"{str(r['R4']):>8}")
    print("#   ... (%d more)" % (len(rows) - 12))

    checks = []

    # A — the reconciliation: the corpus's omega3 is Sigma_3 / 3.
    A = all(r["Sigma3"] == 3 * r["omega3"] for r in rows)
    checks.append(("A  Sigma_3 == 3 * omega3  (the class-size convention)", A))

    # B — Biane/Kerov, stated in its OWN symbol.  This is the identity the
    #     corpus's 'naive' label reads as impugning.
    B = all(r["Sigma3"] == r["R4"] + r["R2"] for r in rows)
    checks.append(("B  Sigma_3 == R_4 + R_2   (Biane/Kerov, textbook)", B))

    # C — the Lean r4Value form, DERIVED from A and B rather than re-asserted.
    C = all(r["R4"] == 3 * r["omega3"] - r["n"] for r in rows)
    checks.append(("C  R_4 == 3*omega3 - n    (Lean r4Value)", C))

    # R_2 = n is what turns B into C once A is in hand; check it explicitly so
    # the derivation below has no unstated step.
    R2n = all(r["R2"] == r["n"] for r in rows)
    checks.append(("   R_2 == n", R2n))

    # D — the failing substitution, exhibited rather than merely asserted.
    bad = [r for r in rows if r["R4"] != r["omega3"] - r["n"]]
    D = len(bad) > 0
    checks.append((f"D  R_4 == omega3 - n is FALSE ({len(bad)}/{len(rows)} partitions)", D))

    # E — A and B and R_2=n together GIVE C.  Verified as an implication on the
    #     data, so the three are one statement and not three measurements.
    E = all((r["R4"] + r["R2"] == 3 * r["omega3"]) and (r["R2"] == r["n"])
            and (r["R4"] == 3 * r["omega3"] - r["n"]) for r in rows)
    checks.append(("E  (A and B and R_2=n)  =>  C, on every partition", E))

    print("#")
    for label, ok in checks:
        print(f"#   [{'PASS' if ok else 'FAIL'}] {label}")

    if bad:
        w = bad[0]
        print("#")
        print("#   smallest failing partition for the naive substitution:")
        print(f"#     lam = {list(w['lam'])}, n = {w['n']}: R_4 = {w['R4']}, "
              f"omega3 - n = {w['omega3'] - w['n']}, 3*omega3 - n = {3 * w['omega3'] - w['n']}")

    print("#")
    print("# CONCLUSION.  Biane/Kerov's Sigma_3 = R_4 + R_2 holds on every partition")
    print("#   tested (B).  The corpus's omega3 is Sigma_3/3 (A), because Sigma_3 is")
    print("#   normalised by the falling factorial (n)_3 while the 3-cycle class has")
    print("#   size (n)_3/3.  Substituting omega3 for Sigma_3 in the identity is what")
    print("#   produces the false R_4 = omega3 - n (D).  The Lean r4Value form (C) is")
    print("#   the identity written in the corpus's own normalisation, so the two")
    print("#   readings are ONE identity plus ONE convention, not rival conventions.")
    print("#")
    print("# CONSEQUENCE for kappa = Cov(Sum_h, R_4)/(3 n^{5/2}): it inherits this")
    print("#   normalisation.  A slip is a factor of 3, so it CANNOT explain kappa's")
    print("#   0.3 % gap (~0.0591 vs sqrt(2)/24 = 0.058926).  Gap qou-k5r5 stays OPEN.")

    ok = all(c[1] for c in checks)
    print(f"\nRESULT: {sum(1 for c in checks if c[1])}/{len(checks)} checks pass")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
