#!/usr/bin/env python3
"""deltalambda_cyclotomic_sign_map_probe.py — does the mixed-sign of the Masbaum
cyclotomic coefficients supply the Δ_λ chirality sign that the KL-positivity
prune (Option-E PROBE-4) said was missing?

CONTEXT (bean qou-42u7; fresh-look qou-do3a). Δ_λ closure is blocked: the target
carries a chirality sign sgn(w_0^{S_{λ'}}) that is MIXED across partitions, but
KL multiplicities are non-negative (KL positivity), so a Σ_w n^w_λ X_w sum cannot
supply it (PROBE-4 prune, Lean-proved QOU.BraidsAndKnots.deltaSign_mixed). The Nakayama
route was refuted (gives +1); the ribbon/content grading q^{2(n(λ')-n(λ))} was
pruned. The Masbaum cyclotomic coefficients C_{K,n}(q) ARE mixed-sign — a fresh
candidate mixed-sign source. This probe tests, cheaply and decisively, whether
that sign can realise the Δ_λ row-grading sign.

TESTS:
 (1) IDENTITY  sgn(w_0^{S_{λ'}}) = (-1)^{n(λ)},  n(λ)=Σ(i-1)λ_i=Σ_j C(λ'_j,2).
     Confirms the Δ_λ chirality sign IS the row-grading (-1)^{n(λ)} at q²=-1.
 (2) CYCLOTOMIC SIGN  sgn(C_{5₂,n}(q₀)) = (-1)^n  (Masbaum, real q₀>1).
 (3) INDEX-MATCHING (the decisive step).  Δ_λ's sign varies WITHIN a fixed n
     (it depends on λ); the cyclotomic coefficient gives ONE sign per integer n.
     Can a per-n quantity supply a per-λ sign?  Test whether (-1)^{n(λ)} is
     constant over λ⊢n (if so, per-n suffices; if not, index-mismatch wall).
 (4) AGGREGATE  does the cyclotomic per-n sign (-1)^n match a natural
     partition AGGREGATE Σ_{λ⊢n} (-1)^{n(λ)} · w  (w ∈ {1, f^λ})?  If yes, the
     cyclotomic route supplies the tr_M-level (aggregate) chirality but NOT the
     per-partition resolution — locating the true remaining step (the
     GS-filtration partition-refinement, bean qou-my68).

HONEST framing: scope-(a). A negative on (3) is a *narrowing* (the mixed sign is
at the wrong resolution), not a refutation of the cyclotomic ingredient. No fit;
no c_k; nothing wired.

Run: python3 -u computations/probes/deltalambda_cyclotomic_sign_map_probe.py \\
       2>&1 | tee /tmp/deltalambda_sign_map.log
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import subprocess

import sympy as sp
from sympy.combinatorics.partitions import IntegerPartition
from sympy.utilities.iterables import partitions

# q_parameter lives in computations/substrate/ (bean qou-9ugp); the anchor must
# be read from it, not from qou_substrate.constants, or the witness gets no
# q0 stamp. Idempotent.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent.parent,
              _Path_qp(__file__).resolve().parent.parent / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


def _repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "computations")) and \
           os.path.exists(os.path.join(d, "AGENTS.md")):
            return d
        d = os.path.dirname(d)
    raise RuntimeError("repo root not found")


def _head_sha():
    for ev in ("GITHUB_SHA", "GIT_COMMIT_SHA"):
        v = os.environ.get(ev)
        if v and v.strip():
            return v.strip()
    sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=_repo_root(), text=True).strip()
    if not sha:
        raise RuntimeError("empty commitSha")
    return sha


def part_list(n):
    """All partitions of n as descending tuples."""
    out = []
    for p in partitions(n):
        lam = []
        for part, mult in sorted(p.items(), reverse=True):
            lam.extend([part] * mult)
        out.append(tuple(lam))
    return out


def conjugate(lam):
    if not lam:
        return ()
    m = max(lam)
    return tuple(sum(1 for a in lam if a >= i) for i in range(1, m + 1))


def n_of(lam):
    """n(λ) = Σ (i-1) λ_i."""
    return sum(i * a for i, a in enumerate(lam))


def sign_w0_young(lam):
    """sgn(w_0^{S_{λ'}}) = ∏_j (-1)^{C(λ'_j, 2)} = (-1)^{Σ_j C(λ'_j,2)}.
    The longest element of a symmetric group S_m has length C(m,2); the Young
    subgroup S_{λ'} = ∏_j S_{λ'_j}, so ℓ(w_0) = Σ_j C(λ'_j, 2)."""
    lp = conjugate(lam)
    ell = sum(c * (c - 1) // 2 for c in lp)
    return (-1) ** ell


def n_syt(lam):
    """f^λ = number of standard Young tableaux = hook-length formula."""
    n = sum(lam)
    lp = conjugate(lam)
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - j - 1
            leg = lp[j] - i - 1
            prod *= (arm + leg + 1)
    return sp.factorial(n) // prod


# Masbaum 5_2 = K_2 cyclotomic coefficient sign (real q>1): sgn(C_{5_2,n}) = (-1)^n
def masbaum_c52_sign(n, q0):
    # `str(q0)`, not `float(q0)` (bean qou-9ugp): the caller now passes the
    # 50-digit anchor string, and routing it through a Python float threw
    # away 33 of those digits before sympy widened the result back to 30.
    # Only the SIGN is consumed downstream, so this never changed a verdict
    # -- but a float64 bottleneck inside an exact-arithmetic routine is a
    # defect whether or not it happens to be masked.
    a = sp.sqrt(sp.Float(str(q0), 30))
    s = sp.Integer(0)
    for k in range(0, n + 1):
        # a-binomial [n,k]
        def qfact(m):
            r = sp.Integer(1)
            for i in range(1, m + 1):
                r *= (a ** i - a ** (-i)) / (a - a ** (-1))
            return r
        binom = qfact(n) / (qfact(k) * qfact(n - k))
        s += a ** (k ** 2 - 2 * k - 3 * n * k) * binom
    cval = (-1) ** n * a ** sp.Rational(5 * n ** 2 + 7 * n, 2) * s
    return 1 if float(sp.N(cval)) > 0 else -1


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update({k: v for k, v in kw.items() if v is not None})
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 78)
    print(" Δ_λ sign-map test: cyclotomic mixed-sign vs the row-grading (-1)^{n(λ)}")
    print("=" * 78)

    # (1) IDENTITY sgn(w_0^{S_{λ'}}) = (-1)^{n(λ)}
    print("\n (1) sgn(w_0^{S_{λ'}}) = (-1)^{n(λ)} for all λ⊢n, n=2..7:")
    id_ok = True
    per_n_spread = {}
    for n in range(2, 8):
        signs = []
        for lam in part_list(n):
            s_w0 = sign_w0_young(lam)
            s_row = (-1) ** n_of(lam)
            signs.append(s_row)
            if s_w0 != s_row:
                id_ok = False
                print(f"    MISMATCH n={n} λ={lam}: w0={s_w0} row={s_row}")
        per_n_spread[n] = signs
    print(f"    identity holds for all tested λ: {id_ok}")
    check("chirality_sign_eq_row_grading", id_ok,
          source="sgn(w_0^{S_{λ'}}) = (-1)^{Σ_j C(λ'_j,2)} = (-1)^{n(λ)} — the Δ_λ "
                 "chirality sign IS the row-grading (-1)^{n(λ)} (= q^{2n(λ)} at "
                 "q²=-1). Confirms the Nakayama-witness framing.")

    # (2) cyclotomic sign sgn(C_{5₂,n}) = (-1)^n
    print("\n (2) sgn(C_{5₂,n}(q₀)) = (-1)^n  (Masbaum, q₀=1.10998):")
    # q0 read BY NAME (bean qou-9ugp, 2026-09-03). It was the bare float64
    # literal 1.10997859555733471 -- the RETIRED self-certified muon pin A,
    # superseded 2026-08-22. No comparison leg here, so the 2026-08-30 owner
    # ruling puts it on the proton default (an 11.54 ppb move). Only the sign
    # of C_{5_2,n} is consumed, and no pin move of that size can flip it.
    q0 = Q_50_DIGIT_STR
    cyc_ok = True
    for n in range(1, 5):
        s = masbaum_c52_sign(n, q0)
        exp = (-1) ** n
        ok = (s == exp)
        cyc_ok = cyc_ok and ok
        print(f"    n={n}: sgn(C_{{5₂,{n}}})={s:+d}  (-1)^n={exp:+d}  {'ok' if ok else 'FAIL'}")
    check("cyclotomic_coeff_sign_is_minus1_pow_n", cyc_ok,
          source="the Masbaum 5₂ cyclotomic coefficient has sgn(C_{5₂,n})=(-1)^n "
                 "at real q₀>1 (the (-1)^n prefactor times a positive q-binomial "
                 "sum) — one sign per INTEGER n")

    # (3) INDEX-MATCHING: is (-1)^{n(λ)} constant over λ⊢n?  (decisive)
    print("\n (3) INDEX-MATCHING — is the sign constant within a fixed n?")
    all_constant = True
    for n in range(2, 8):
        s = per_n_spread[n]
        pos = sum(1 for x in s if x > 0)
        neg = len(s) - pos
        constant = (pos == 0 or neg == 0)
        all_constant = all_constant and constant
        print(f"    n={n}: {pos}+ / {neg}-  over {len(s)} partitions  "
              f"({'constant' if constant else 'MIXED within n'})")
    # decisive: cyclotomic (per-n) can supply per-λ sign ONLY if constant within n
    index_match_possible = all_constant
    print(f"    per-n cyclotomic sign can resolve per-λ Δ_λ sign: {index_match_possible}")
    check("index_matching_wall_is_real", not index_match_possible,
          source="(-1)^{n(λ)} is MIXED across partitions of the same n (e.g. n=3: "
                 "λ=(3)→+, (2,1)→-, (1³)→-), while the cyclotomic coefficient gives "
                 "ONE sign per integer n. So the cyclotomic mixed-sign is at the "
                 "WRONG RESOLUTION — it cannot, alone, supply the per-partition Δ_λ "
                 "sign. scope-(a) narrowing, not an ingredient refutation: the "
                 "per-λ resolution is the GS-filtration refinement (bean qou-my68). "
                 "This check PASSES when the wall is confirmed real.")

    # (4) AGGREGATE: does (-1)^n match a natural partition aggregate?
    print("\n (4) AGGREGATE Σ_{λ⊢n} (-1)^{n(λ)} · w  vs cyclotomic (-1)^n:")
    agg_rows = []
    match_unweighted = True
    match_syt = True
    for n in range(1, 8):
        A1 = sum((-1) ** n_of(lam) for lam in part_list(n))
        Af = sum((-1) ** n_of(lam) * int(n_syt(lam)) for lam in part_list(n))
        cyc = (-1) ** n
        s1 = 0 if A1 == 0 else (1 if A1 > 0 else -1)
        sf = 0 if Af == 0 else (1 if Af > 0 else -1)
        agg_rows.append({"n": n, "sum_unweighted": int(A1), "sum_syt": int(Af),
                         "cyc_sign": cyc})
        if s1 != cyc:
            match_unweighted = False
        if sf != cyc:
            match_syt = False
        print(f"    n={n}: Σ(-1)^n(λ)={A1:+d} (sgn {s1:+d}), "
              f"Σ(-1)^n(λ)f^λ={Af:+d} (sgn {sf:+d}), cyc (-1)^n={cyc:+d}")
    check("aggregate_also_fails_to_match", not match_syt,
          source="the SYT-weighted aggregate Σ_{λ⊢n}(-1)^{n(λ)} f^λ sign does NOT "
                 "match the cyclotomic per-n sign (-1)^n (mismatch at n=1,2,4,5,6) "
                 "— so the cyclotomic coefficient does not even carry the correctly "
                 "signed tr_M-level aggregate chirality. The negative is STRENGTHENED: "
                 "cyclotomic sign fails to supply Δ_λ both per-partition AND in "
                 "aggregate. Passes = confirmed non-match (the strengthened negative).")

    all_passed = all(a["passed"] for a in assertions)
    # honest verdict independent of the (4) 'match' framing
    verdict = (
        "HONEST NEGATIVE (scope-(a)) — the direct cyclotomic-sign route does NOT "
        "close Δ_λ. What holds: (i) the Δ_λ chirality sign sgn(w_0^{S_{λ'}}) = "
        "(-1)^{n(λ)} EXACTLY (row-grading at q²=-1; the per-n spread 1+/2- (n=3), "
        "6+/5- (n=6) reproduces the corpus PROBE-4 deltaSign, cross-validating the "
        "identity); (ii) the Masbaum coefficients ARE mixed-sign, sgn(C_{5₂,n})="
        "(-1)^n. What FAILS: the mixed sign is at the WRONG RESOLUTION — (-1)^{n(λ)} "
        "is mixed WITHIN each n (per-partition), while the cyclotomic coefficient "
        "carries ONE sign per INTEGER n, so it cannot resolve the per-λ sign; and "
        "the SYT-weighted AGGREGATE Σ(-1)^{n(λ)}f^λ does not even sign-match (-1)^n "
        "(n=1,2,4,5,6), so it is not the signed tr_M aggregate either. CONCLUSION: "
        "the KL-prune EVASION via cyclotomic signs is REFUTED as a direct Δ_λ "
        "source — a real mixed sign exists but neither resolves per-partition nor "
        "matches in aggregate. This NARROWS the search: any cyclotomic→Δ_λ route "
        "MUST go through a partition-refinement that splits C_{K,n} into per-λ "
        "pieces (the GS-filtration bridge, bean qou-my68) — the naive sign-transfer "
        "is closed. No fit; no c_k wired."
    )
    print("\nVERDICT:", verdict)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "deltalambda-cyclotomic-sign-map",
        "description": "Tests whether the Masbaum cyclotomic coefficient mixed-sign "
                       "supplies the Δ_λ row-grading sign (-1)^{n(λ)}. Identity "
                       "sgn(w_0^{S_{λ'}})=(-1)^{n(λ)} confirmed; cyclotomic sign is "
                       "per-integer-n while Δ_λ sign is per-partition — index-"
                       "matching wall. scope-(a): needs GS-filtration refinement "
                       "(qou-my68). No fit; no c_k.",
        "audit_only": True,
        "tier": "symbolic-exact (partition combinatorics)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "sympy",
        "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {"aggregate_table": agg_rows, "verdict": verdict},
        "context": {
            "axis": "Δ_λ closure — cyclotomic mixed-sign KL-prune evasion test",
            "beans": ["qou-42u7", "qou-do3a", "qou-my68"],
            "relatedPrune": "Option-E PROBE-4 KL-positivity "
                            "(QOU.BraidsAndKnots.deltaSign_mixed); Nakayama refutation "
                            "(deltalambda-grho-nakayama-morphism)",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "deltalambda-cyclotomic-sign-map.witness.json")
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    print("\nwitness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
