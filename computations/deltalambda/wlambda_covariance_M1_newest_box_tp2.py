#!/usr/bin/env python3
"""Total positivity of the newest-box law, and the shift inequality (bean qou-jmgu).

K_n(s, a) = n!·Pr(newest Plancherel-growth box has i+j = s and |j−i| = a), an integer
(see wlambda_covariance_M1_newest_box_form.newest_box_table). Checked exactly:

  (TP2-par)  K_n(s1,a1)K_n(s2,a2) ≥ K_n(s1,a2)K_n(s2,a1) for s1<s2, a1<a2, all four of one
             parity. It gives E[c²|s] ≤ E[c²|s+2] (monotone likelihood ratio), hence one
             sign change of ρ_n on each parity class of s.
  (SHIFT)    E[c² | s+1] ≥ E[(|c|+1)² | s]. Wherever it holds, E[c²|s] ≤ E[c²|s+1].
             Reported: the largest s where it fails, against the proved lower-half edge
             2+√(n−1). If every failure lies at or below that edge, single crossing follows at n.

Neither statement is proved for all n. Exact integer arithmetic; no float. No fit.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wlambda_covariance_M1_newest_box_form as nb  # noqa: E402


def kernel(n):
    K = {}
    for (s, c, m), w in nb.newest_box_table(n).items():
        K[(s, abs(c))] = K.get((s, abs(c)), 0) + w
    return K


def tp2_parity_violations(K):
    S = sorted({s for s, a in K})
    A = sorted({a for s, a in K})
    bad = 0
    for i, s1 in enumerate(S):
        for s2 in S[i + 1:]:
            if (s2 - s1) % 2:
                continue
            for j, a1 in enumerate(A):
                if (a1 - s1) % 2:
                    continue
                for a2 in A[j + 1:]:
                    if (a2 - a1) % 2:
                        continue
                    if K.get((s1, a1), 0) * K.get((s2, a2), 0) < \
                            K.get((s1, a2), 0) * K.get((s2, a1), 0):
                        bad += 1
    return bad


def shift_failures(K):
    T, A1, A2 = {}, {}, {}
    for (s, a), w in K.items():
        T[s] = T.get(s, 0) + w
        A1[s] = A1.get(s, 0) + w * a
        A2[s] = A2.get(s, 0) + w * a * a
    S = sorted(T)
    return [s for s in S[:-1] if A2[s + 1] * T[s] < (A2[s] + 2 * A1[s] + T[s]) * T[s + 1]]


def main():
    ntp = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    nsh = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    rows, tp_ok, sh_ok = [], True, True
    for n in range(5, max(ntp, nsh) + 1):
        K = kernel(n)
        row = {"n": n}
        if n <= ntp:
            v = tp2_parity_violations(K)
            row["tp2_parity_violations"] = v
            tp_ok &= v == 0
        if n <= nsh:
            f = shift_failures(K)
            inside = all((s - 2) ** 2 <= n - 1 for s in f)
            row["shift_fail_max_s"] = max(f) if f else None
            row["shift_failures_inside_lower_half"] = inside
            sh_ok &= inside
        rows.append(row)
        print(row, flush=True)
    print(f"RESULT TP2-par n=5..{ntp}: {tp_ok}; shift failures inside lower half n=5..{nsh}: {sh_ok}")
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "substrate"))
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-M1-newest-box-tp2", engine="python-exact")
        w.set_description(
            "Newest Plancherel-growth box law K_n(s,a), s=i+j, a=|j−i|: same-parity TP2 "
            "(⇒ E[c²|s]≤E[c²|s+2], one sign change of ρ_n per parity class) and the shift "
            "inequality E[c²|s+1] ≥ E[(|c|+1)²|s], whose failures all lie inside the proved "
            "lower half (s ≤ 2+√(n−1)) for the checked n, giving single crossing there. Neither "
            "is proved for all n; the limit shape suggests the shift inequality eventually "
            "fails above the lower-half edge. No fit; nothing wired.")
        w.add_data("rows", rows)
        w.add_assertion("tp2_parity_and_shift", computed=str(int(tp_ok and sh_ok)), expected="1",
                        tolerance=0, source=f"TP2-par n≤{ntp}; shift n≤{nsh}")
        print(f"Witness: {w.save()}")
    except ImportError as e:
        print(f"(witness skipped — witness_base unavailable: {e})")
    return 0 if tp_ok and sh_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
