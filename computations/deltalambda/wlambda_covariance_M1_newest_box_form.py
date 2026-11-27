#!/usr/bin/env python3
"""M₁ as a covariance of the newest Plancherel-growth box (bean qou-jmgu).

Statement checked (exact Fraction / integer arithmetic, no float):

Let ν ~ Plancherel(n−1) and add one box x with the transition probability f^{ν+x}/(n f^ν).
Write (i, j) for its 1-indexed position, s = i + j, c = j − i, m = min(i, j). Then

    E[c²] = n − 1,
    ρ_n(s) = E[1{i+j = s}(c² − (n−1))] / ((n−1)(n−2)),          (newest-box form of ρ_n)
    M₁(n) = (n/3) Cov(s, c²),
    P(n)  = (n/3) Cov(|c|, c²),
    N(n)  = −(2n/3) Cov(m, c²),     M₁ = P − N  (since s = |c| + 2m).

The ρ_n of the newest-box form is compared with the last-three-box form of
wlambda_covariance_M1_jucys_murphy_form.plancherel_growth_side, and M₁, P with the hook-formula
side partition_side. The derivation (Kerov's interlacing identity applied to the last two boxes)
is in docs/audits/2026-11-27-covariance-kernel-M1-newest-box-form.md.

Also measured:
  * lower half of single crossing: ρ_n(s) ≤ 0 whenever (s−2)² ≤ n−1 (proved in the audit;
    checked here),
  * single crossing of ρ_n for n = 4..NSC,
  * two candidate sufficient conditions, both FAIL: E[c² | s] non-decreasing in s, and
    Cov(s, c²) ≥ 0 under every single transition measure p_ν.
Scope (a): nothing here proves single crossing for all n. No fit; nothing wired.
"""
import sys
from fractions import Fraction as F
from math import factorial
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wlambda_covariance_M1_jucys_murphy_form as jm  # noqa: E402


def newest_box_table(n):
    """Integer weights W[(s, c, m)] = f^ν f^{ν+x}; divide by n! for probabilities."""
    W = {}
    for nu in jm._parts(n - 1):
        fn = jm._dim(nu)
        for lam, i0, j0 in jm._addable(nu):
            i, j = i0 + 1, j0 + 1
            key = (i + j, j - i, min(i, j))
            W[key] = W.get(key, 0) + fn * jm._dim(lam)
    return W


def moments(n, W):
    nf = factorial(n)
    E = lambda g: F(sum(w * g(*k) for k, w in W.items()), nf)  # noqa: E731
    Ec2 = E(lambda s, c, m: c * c)
    cov = lambda g: E(lambda s, c, m: g(s, c, m) * c * c) - E(g) * Ec2  # noqa: E731
    return Ec2, cov(lambda s, c, m: s), cov(lambda s, c, m: abs(c)), cov(lambda s, c, m: m)


def rho_newest(n, W):
    d = factorial(n) * (n - 1) * (n - 2)
    r = {}
    for (s, c, m), w in W.items():
        r[s] = r.get(s, 0) + w * (c * c - (n - 1))
    return {s: F(v, d) for s, v in r.items()}


def sign_pattern(n, W):
    """Exact sign of ρ_n(s) per s (integers, no division)."""
    num = {}
    for (s, c, m), w in W.items():
        num[s] = num.get(s, 0) + w * (c * c - (n - 1))
    return {s: (v > 0) - (v < 0) for s, v in num.items()}


def single_crossing(sg):
    nz = [sg[s] for s in sorted(sg) if sg[s] != 0]
    ch = sum(1 for a, b in zip(nz, nz[1:]) if a != b)
    t = next((s for s in sorted(sg) if sg[s] > 0), None)
    return ch == 1 and nz[0] < 0, t


def monotone_regression_ok(W):
    num, den = {}, {}
    for (s, c, m), w in W.items():
        num[s] = num.get(s, 0) + w * c * c
        den[s] = den.get(s, 0) + w
    S = sorted(den)
    vals = [F(num[s], den[s]) for s in S]
    bad = [S[k + 1] for k in range(len(S) - 1) if vals[k + 1] < vals[k]]
    return not bad, bad


def per_nu_negative(k):
    """Partitions ν ⊢ k with Cov_{p_ν}(s, c²) < 0 under the transition measure of ν."""
    neg = []
    for nu in jm._parts(k):
        fn = jm._dim(nu)
        rows = [(jm._dim(lam), i0 + j0 + 2, (j0 - i0) ** 2) for lam, i0, j0 in jm._addable(nu)]
        Z = (k + 1) * fn
        Es = F(sum(w * s for w, s, q in rows), Z)
        Eq = F(sum(w * q for w, s, q in rows), Z)
        Esq = F(sum(w * s * q for w, s, q in rows), Z)
        if Esq - Es * Eq < 0:
            neg.append(nu)
    return neg


def main():
    nid = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    nsc = int(sys.argv[2]) if len(sys.argv) > 2 else 45
    knu = int(sys.argv[3]) if len(sys.argv) > 3 else 14
    ok = True
    id_rows = []
    print("identity check: newest-box form vs three-box form vs hook formula")
    for n in range(4, nid + 1):
        W = newest_box_table(n)
        Ec2, cs, cabs, cm = moments(n, W)
        M_pg, P_pg, rho_old = jm.plancherel_growth_side(n)
        part = jm.partition_side(n)
        rn = rho_newest(n, W)
        good = (Ec2 == n - 1
                and all(rn.get(s, 0) == rho_old.get(s, 0) for s in set(rn) | set(rho_old))
                and F(n, 3) * cs == part["M1"] == M_pg
                and F(n, 3) * cabs == part["P"] == P_pg
                and -F(2 * n, 3) * cm == part["P"] - part["M1"])
        ok &= good
        id_rows.append({"n": n, "M1": str(part["M1"]), "P": str(part["P"]),
                        "N": str(part["P"] - part["M1"]), "E_c2": str(Ec2), "match": good})
        print(f"  n={n}: M1={part['M1']} P={part['P']} N={part['P'] - part['M1']}  {good}")
    sc_rows, lower_ok, sc_ok, mono_first_fail = [], True, True, None
    print("single crossing, lower half, monotone regression")
    for n in range(4, nsc + 1):
        W = newest_box_table(n)
        sg = sign_pattern(n, W)
        sc, t = single_crossing(sg)
        low = all(sg[s] <= 0 for s in sg if (s - 2) ** 2 <= n - 1)
        mono, bad = monotone_regression_ok(W)
        if not mono and mono_first_fail is None:
            mono_first_fail = {"n": n, "decrease_into_s": bad}
        sc_ok &= sc
        lower_ok &= low
        sc_rows.append({"n": n, "single_crossing": sc, "threshold_s": t, "lower_half": low,
                        "monotone_regression": mono})
        print(f"  n={n}: SC {sc} t={t} lower-half {low} monotone {mono}", flush=True)
    ok &= sc_ok and lower_ok
    nu_rows = []
    print("per-ν transition covariance Cov_{p_ν}(s, c²) < 0")
    for k in range(1, knu + 1):
        neg = per_nu_negative(k)
        nu_rows.append({"k": k, "negative_count": len(neg), "examples": [list(x) for x in neg[:3]]})
        print(f"  |ν|={k}: {len(neg)} negative {neg[:3]}", flush=True)
    print(f"RESULT identities n=4..{nid}: {all(r['match'] for r in id_rows)}; "
          f"SC n=4..{nsc}: {sc_ok}; lower half: {lower_ok}; "
          f"monotone regression first fails: {mono_first_fail}")
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "substrate"))
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-M1-newest-box-form", engine="python-exact")
        w.set_description(
            "Newest-box form of the covariance-kernel first moment: with the n-th Plancherel-"
            "growth box at (i,j), s=i+j, c=j−i, m=min(i,j): E[c²]=n−1, M₁=(n/3)Cov(s,c²), "
            "P=(n/3)Cov(|c|,c²), N=−(2n/3)Cov(m,c²), and ρ_n(s)=E[1{s}(c²−(n−1))]/((n−1)(n−2)), "
            "all equal exactly to the three-box and hook-formula sides. Lower half of single "
            "crossing (ρ_n≤0 for (s−2)²≤n−1) checked; single crossing checked; two candidate "
            "sufficient conditions (monotone regression, per-ν covariance) FAIL. Single crossing "
            "for all n is NOT proved. No fit; nothing wired.")
        w.add_data("identity_rows", id_rows)
        w.add_data("single_crossing_rows", sc_rows)
        w.add_data("monotone_regression_first_failure", mono_first_fail)
        w.add_data("per_nu_negative_covariance", nu_rows)
        w.add_assertion("m1_newest_box_form", computed=str(int(ok)), expected="1", tolerance=0,
                        source=f"identities n=4..{nid}; SC + lower half n=4..{nsc}")
        print(f"Witness: {w.save()}")
    except ImportError as e:
        print(f"(witness skipped — witness_base unavailable: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
