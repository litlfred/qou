#!/usr/bin/env python3
"""
fl_kernel_sign_structure.py — structural narrowing of the Δ_λ covariance-kernel SIGN (qou-x631).

The Δ_λ super-exponential growth bound (#3939) reduces (#3959) to the covariance kernel

    T₃ = Σ_{λ⊢k} (f^λ)² χ^λ(3-cycle) ≤ 0
       ⇔ cov(k) := Σ_{λ⊢k} (f^λ)³ (Σ_□ c(□)² − C(k,2)) ≤ 0
       ⇔ Cov_Planch(f^λ, Σ_□ c(□)²) ≤ 0.

Prior phases: #3998 verified k≤40 + free-cumulant framing; Phase 1 (#4xxx) ruled out
ROUTE 1 (holonomic recurrence / inductive) and ROUTE 2 (β-monotonicity of the biased
content-spread); Phase 2 (#4066) verified the RSK form literally and gave the tilted-limit-
shape heuristic for the sign. The kernel remains OPEN.

This probe attacks the SIGN structurally and records TWO further decisive narrowings, each a
scope-(a) structural fact (not a numerical near-match), that constrain HOW a proof can go:

  NARROWING A — FKG / correlation-inequality on the DOMINANCE lattice is DEAD.
    A Harris/FKG proof of Cov_Planch(f^λ, Σc²) ≤ 0 on the partition dominance lattice would need
    f^λ and Σc² to be OPPOSITELY MONOTONE on that lattice (plus a log-supermodular measure).
    We show BOTH functions FAIL monotonicity: each is EXTREMAL (f small / Σc² large) at BOTH
    dominance extremes — the single row (k) and the single column (1^k) — and opposite in the
    middle. So the anti-correlation is a "middle-vs-extremes" (concentration) effect, NOT an
    order-driven one. This complements Phase-1's ruled-out β-monotonicity: neither the exponent
    order (β) nor the partition order (dominance) drives the sign. Explicit covering-pair
    witnesses of BOTH signs of Δf and ΔΣc² are emitted.

  NARROWING B — TRANSPOSE PARITY (route b) provably CANNOT sign T₃; it only kills T₂.
    Under conjugation λ↔λ': f^{λ'}=f^λ (transpose of SYT) and, since c(i,j)=j−i flips sign,
      • Σc(λ') = −Σc(λ)   (content is transpose-ODD)  ⇒ Σ_λ (f^λ)³ Σc = 0  ⇒ T₂ = 0,
      • Σc²(λ') = Σc²(λ)  (content-SQUARE is transpose-EVEN, squares kill the sign).
    Hence EACH cov(k) summand (f^λ)³(Σc²−C(k,2)) is INDIVIDUALLY conjugation-invariant, so the
    transpose involution is a SYMMETRY of the kernel, contributing zero information about its
    sign. This is the rigorous form of the Phase-2 "one candidate scope-(b)" observation: the
    transpose route provably closes only the ODD moment (T₂), never the EVEN one (T₃).
    Formalized sorry-free in Lean (see YoungDiagramTranspose.lean).

Discipline: scope-(a) structural narrowing; no fit; nothing wired; no c_k; L2 unchanged (2/7).
In-sandbox (pure int + Fraction, no numpy). Records dead routes so they are not retried.

# Ref: [sniady2006asymptotics] https://doi.org/10.1007/s00440-005-0479-7
"""
from __future__ import annotations

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
KMAX = 16          # dominance / transpose structural checks
KMAX_COV = 30      # cov(k) sign re-anchor


def partitions_of(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for i in range(min(n, m), 0, -1):
        for rest in partitions_of(n - i, i):
            yield (i,) + rest


def conjugate(lam):
    if not lam:
        return ()
    return tuple(sum(1 for p in lam if p > j) for j in range(lam[0]))


def hook_dim(lam):
    """f^λ = |λ|! / ∏ hook lengths (number of SYT)."""
    if not lam:
        return 1
    conj = conjugate(lam)
    prod = 1
    for i, li in enumerate(lam):
        for j in range(li):
            hook = (li - j) + (conj[j] - i) - 1
            prod *= hook
    return math.factorial(sum(lam)) // prod


def content_sum(lam):
    return sum(j - i for i, li in enumerate(lam) for j in range(li))


def content_sq(lam):
    return sum((j - i) ** 2 for i, li in enumerate(lam) for j in range(li))


def dominates(lam, mu):
    """lam ⊵ mu in dominance order (both ⊢ same k)."""
    a = b = 0
    L = max(len(lam), len(mu))
    for t in range(L):
        a += lam[t] if t < len(lam) else 0
        b += mu[t] if t < len(mu) else 0
        if a < b:
            return False
    return True


def covering_pairs(parts):
    """Dominance covering pairs (lam ⊵ mu, lam≠mu, no strict intermediate)."""
    S = list(parts)
    covers = []
    for lam in S:
        for mu in S:
            if lam == mu or not dominates(lam, mu):
                continue
            # covering: no nu with lam ⊳ nu ⊳ mu strictly
            if any(nu != lam and nu != mu and dominates(lam, nu) and dominates(nu, mu)
                   for nu in S):
                continue
            covers.append((lam, mu))
    return covers


def main():
    out = {
        "schema": "witness/v1",
        "computation": "fl_kernel_sign_structure",
        "description": "Structural narrowings of the Δ_λ covariance-kernel sign: FKG-on-dominance "
                       "dead + transpose-parity cannot sign T₃ (only kills T₂).",
        "generated": datetime.now(timezone.utc).isoformat(),
        "discipline": "scope-(a) structural narrowing; no fit; nothing wired; no c_k; L2 2/7",
    }

    # ---------- Re-anchor: cov(k) ≤ 0 and its covariance reading ----------
    cov = {}
    for k in range(3, KMAX_COV + 1):
        parts = list(partitions_of(k))
        Ck2 = k * (k - 1) // 2
        val = sum(hook_dim(l) ** 3 * (content_sq(l) - Ck2) for l in parts)
        cov[k] = val
    out["cov_all_nonpos"] = all(v <= 0 for v in cov.values())
    out["cov_values"] = {str(k): cov[k] for k in cov}
    assert out["cov_all_nonpos"], "cov(k) should be ≤ 0 (re-anchor failed)"

    # ---------- NARROWING B: transpose parity ----------
    transpose_ok = True
    fixed_points_zero_contentsum = True
    for k in range(1, KMAX + 1):
        for lam in partitions_of(k):
            cj = conjugate(lam)
            # f invariant, Σc² invariant (even), Σc anti-invariant (odd):
            if hook_dim(cj) != hook_dim(lam):
                transpose_ok = False
            if content_sq(cj) != content_sq(lam):
                transpose_ok = False
            if content_sum(cj) != -content_sum(lam):
                transpose_ok = False
            if lam == cj and content_sum(lam) != 0:
                fixed_points_zero_contentsum = False
    # the odd-moment vanishing Σ_λ (f^λ)³ Σc = 0 (⇔ T₂ = 0):
    t2_form = {}
    for k in range(1, KMAX + 1):
        s = sum(hook_dim(l) ** 3 * content_sum(l) for l in partitions_of(k))
        t2_form[k] = s
    out["transpose_summand_invariant"] = transpose_ok
    out["selfconjugate_contentsum_zero"] = fixed_points_zero_contentsum
    out["t2_content_form_all_zero"] = all(v == 0 for v in t2_form.values())
    out["narrowing_B"] = (
        "transpose involution fixes every cov summand (f even-power, Σc² even) ⇒ cannot sign T₃; "
        "it makes Σc odd ⇒ Σ(f^λ)³Σc = 0 ⇒ T₂=0 only."
    )
    assert transpose_ok and out["t2_content_form_all_zero"] and fixed_points_zero_contentsum

    # ---------- NARROWING A: FKG-on-dominance dead ----------
    # For each k show f^λ and Σc² are BOTH non-monotone on dominance: exhibit covering pairs
    # (lam ⊵ mu) with Δf := f^lam − f^mu of BOTH signs, and ΔΣc² of BOTH signs.
    fkg_report = {}
    f_nonmono_all = sq_nonmono_all = True
    for k in range(4, KMAX + 1):
        parts = list(partitions_of(k))
        covers = covering_pairs(parts)
        df_pos = df_neg = dsq_pos = dsq_neg = None
        for (lam, mu) in covers:
            df = hook_dim(lam) - hook_dim(mu)
            dsq = content_sq(lam) - content_sq(mu)
            if df > 0 and df_pos is None:
                df_pos = (lam, mu, df)
            if df < 0 and df_neg is None:
                df_neg = (lam, mu, df)
            if dsq > 0 and dsq_pos is None:
                dsq_pos = (lam, mu, dsq)
            if dsq < 0 and dsq_neg is None:
                dsq_neg = (lam, mu, dsq)
        f_nonmono = df_pos is not None and df_neg is not None
        sq_nonmono = dsq_pos is not None and dsq_neg is not None
        f_nonmono_all = f_nonmono_all and f_nonmono
        sq_nonmono_all = sq_nonmono_all and sq_nonmono
        # extremes coincide: (k) and (1^k) both have f=1 and equal Σc²
        row, col = (k,), tuple([1] * k)
        fkg_report[str(k)] = {
            "n_covers": len(covers),
            "f_nonmonotone": f_nonmono,
            "contentsq_nonmonotone": sq_nonmono,
            "df_increasing_example": None if df_pos is None else
                [list(df_pos[0]), list(df_pos[1]), df_pos[2]],
            "df_decreasing_example": None if df_neg is None else
                [list(df_neg[0]), list(df_neg[1]), df_neg[2]],
            "row_extreme": {"f": hook_dim(row), "csq": content_sq(row)},
            "col_extreme": {"f": hook_dim(col), "csq": content_sq(col)},
            "extremes_coincide": hook_dim(row) == hook_dim(col) == 1
                                 and content_sq(row) == content_sq(col),
        }
    out["fkg_dominance_dead"] = bool(f_nonmono_all and sq_nonmono_all)
    out["fkg_per_k"] = fkg_report
    out["narrowing_A"] = (
        "f^λ and Σc² are BOTH non-monotone on the dominance lattice (extremal at both extremes "
        "(k),(1^k); opposite in the middle) ⇒ no Harris/FKG correlation inequality on dominance "
        "order can yield Cov(f,Σc²) ≤ 0. Complements ruled-out β-monotonicity (Phase 1)."
    )
    assert out["fkg_dominance_dead"], "expected f and Σc² both non-monotone on dominance"

    out["verdict"] = (
        "Kernel still OPEN. Two structural proof-routes further eliminated: FKG-on-dominance "
        "(NARROWING A) and transpose-parity-signs-T₃ (NARROWING B, now Lean sorry-free). "
        "The sign is a genuine middle-vs-extremes concentration effect, order-blind and "
        "parity-blind."
    )

    wpath = HERE / "fl-kernel-sign-structure.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    out.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        out, script_path=__file__, engine=None, q0_anchor=False)
    wpath.write_text(json.dumps(out, indent=2) + "\n")
    print("cov(k) ≤ 0 all k≤%d: %s" % (KMAX_COV, out["cov_all_nonpos"]))
    print("NARROWING B — transpose summand-invariant: %s | T₂ content-form all zero: %s"
          % (out["transpose_summand_invariant"], out["t2_content_form_all_zero"]))
    print("NARROWING A — FKG-on-dominance dead (f & Σc² both non-monotone): %s"
          % out["fkg_dominance_dead"])
    for k in ("4", "6", "8"):
        r = fkg_report[k]
        print("  k=%s: f↑ex=%s  f↓ex=%s  extremes_coincide=%s"
              % (k, r["df_increasing_example"], r["df_decreasing_example"],
                 r["extremes_coincide"]))
    print("wrote", wpath.name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
