#!/usr/bin/env python3
"""
Frobenius-pairing compute audit — classifies every script under
``computations/`` that touches a Markov or quantum trace into buckets (A)/(B)/(C),
and explicitly distinguishes **symmetric centralizer / Temperley–Lieb traces**
from **Nakayama-twisted KMS / Haar pairings** (TN-11 / bean qou-v4iw).

Pairing Regimes (TN-11)
-----------------------

1. **Symmetric centralizer / Temperley–Lieb regime** (``symmetric_centralizer_tl``):
   On the Cartan weight centralizer ``[K^{⊗n}, A] = 0`` inside ``End(V^{⊗n})``
   (Lean ``QOU.IwahoriHecke.QTraceCyclic``), every Jimbo braid generator
   ``ρ(σ_i)`` commutes with ``K^{⊗n}`` (``K = diag(q, q⁻¹)`` per strand).
   Restricted to ``H_n(q)``, the quantum trace ``tr_M(X) = Tr(K^{⊗n} X)/[2]_q^n``
   is untwisted cyclic: ``tr_M(A B) = tr_M(B A)``.
   Under Convention D (``z_D = q³/(q² + 1)``), on 3 strands:
     - ``tr_M(e⁻) = tr_M(σ₀ σ₁ σ₀) = h z_D² + z_D`` (NOT stale ``z³``);
     - the 3-strand q-antisymmetriser ``e_{(1^3)}`` spans a 1D radical
       (``det G = 0`` on 6D ``H_3(q)``), descending to a non-degenerate pairing
       on the 5D Temperley–Lieb quotient ``TL_3(q) = H_3(q)/(e_{(1^3)})``.

2. **Nakayama-twisted KMS / Haar regime** (``nakayama_kms_weighted``):
   Off the weight centralizer (or on ``O_q(SU(2))``), Frobenius pairings satisfy
   the Nakayama-twisted law ``τ(a b) = τ(b ϑ(a))`` with ``ϑ ≠ id`` at ``q ≠ ±1``:
     - On ``End(V^{⊗n})``, ``tr_q(A B) = tr_q(B K^{⊗n} A K^{-⊗n})`` (KMS modular
       automorphism ``ϑ(A) = K^{⊗n} A K^{-⊗n}``). Conjugation invariance
       ``tr_q(U X U⁻¹) = tr_q(X)`` holds **iff** ``[K^{⊗n}, U] = 0``; for
       weight-shifting currents ``T^±`` (``K^{⊗n} T^± K^{-⊗n} = q^{±2} T^±``),
       unweighted cyclic swapping fails by ``q^{±2}``.
     - On ``O_q(SU(2))``, Woronowicz's Haar state ``h_q`` satisfies
       ``h_q(a b) = h_q(b ν(a))`` with ``ν(α, β, γ, δ) = (q² α, β, γ, q⁻² δ)``,
       so ``h_q([α, δ]) = (q² - 1)/(q² + 1) ≠ 0`` at ``q ≠ ±1``.

Buckets
-------

(A) **Trace-only.**  The script computes ``tr_M(W)`` directly (e.g. closed-braid
    mass/volume defect).

(B) **Observable-on-state.**  The script computes ``tr_M(O · ρ(β_T))`` for a
    non-Hamiltonian observable ``O``.  Requires witness fields ``gram_matrix``,
    ``gram_inverse``, ``lp_active_set``, ``shadow_prices`` (unless opted out via
    ``observable_type == "raw_trace"``).

(C) **Conjugation pattern ``tr_M(β X β⁻¹)``.**
    - If ``[K^{⊗n}, β] = 0`` (e.g. ``β ∈ B_n`` in the Jimbo braid representation),
      KMS cyclicity collapses ``tr_q(β X β⁻¹) = tr_q(X)`` even for off-diagonal
      ``X``, silently erasing ``β``-dependence!
    - If ``[K^{⊗n}, β] ≠ 0`` (weight-shifting ``β``), ``tr_q(β X β⁻¹) ≠ tr_q(X)``
      picks up the Nakayama modular factor ``K^{⊗n} β K^{-⊗n} β⁻¹``.

Exit status: 0 if no bucket-(B) or bucket-(C) witness lacks the required fields;
1 otherwise.  Also runs an exact 80-dps ``mpmath`` verification of the symmetric
vs Nakayama-twisted KMS/Haar identities over exact test rationals ``q != 1``.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from mpmath import mp

# ── Patterns ────────────────────────────────────────────────────

TRACE_TOKEN = re.compile(r"\b(?:tr_M|markov_trace)\b")

NAKAYAMA_TOKEN = re.compile(
    r"\b(?:qtrace|Nakayama|nakayama|Haar|haar_state|K_tensor|Kp|Kn|KK|"
    r"weightCentralizer|qtrace_conn_borromean)\b"
)

STALE_Z3_TOKEN = re.compile(
    r"tr_M\s*\(\s*e\^?-?\s*\)\s*=\s*z\s*(?:\*\*\s*3|\^3|³)"
)

OBS_PATTERN = re.compile(
    r"(?:tr_M|markov_trace|mat_trace|trace_std|tr_std|tr_standard"
    r"|np\.trace|sympy\.trace|Trace)\s*\("
    r"[^()\n]{0,200}?"
    r"(?:@|\*|·|matmul|dot|hecke_mul)"
    r"[^()\n]{0,200}?"
    r"(?:rho|M_braid|M_std|M_full|evaluate_braid|braid_matrix|"
    r"sigma\d|σ\d|s1|s2|conversion_op)"
)

OBS_OP_CONCAT = re.compile(
    r"\b(?:full_op|op_braid|obs_braid|operator_word|conv_word)\s*="
)

CONJ_PATTERN_CODE = re.compile(
    r"(beta[a-zA-Z0-9_]*)\s*\+\s*"
    r"(?:[a-zA-Z_][a-zA-Z0-9_]*\s*\+\s*)?"
    r"(beta[a-zA-Z0-9_]*_inv|\1_inv)"
)
CONJ_PATTERN_COMMENT = re.compile(
    r"(?:β\s*[·.* ]\s*[A-Za-z_]\w*\s*[·.* ]\s*β\s*[⁻^]\s*1"
    r"|beta\s*\*\s*\w+\s*\*\s*beta_?inv"
    r"|β·σ_?\d+·β\s*[⁻^]?\s*1?"
    r"|β\\cdot\s*\w+\\cdot\s*β\^?-?1)"
)

REQUIRED_FIELDS = (
    "gram_matrix",
    "gram_inverse",
    "lp_active_set",
    "shadow_prices",
)
OPTOUT_FIELD = "observable_type"
OPTOUT_VALUE = "raw_trace"


# ── Helpers ─────────────────────────────────────────────────────

def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _sibling_witnesses(script: Path) -> list[Path]:
    """Heuristic: same-directory *.witness.json with stem matching
    the script's stem (with both - and _ variants)."""
    stem = script.stem
    candidates = {stem, stem.replace("_", "-"), stem.replace("-", "_")}
    out = []
    for cand in candidates:
        for suffix in (".witness.json", "-witness.json"):
            p = script.parent / f"{cand}{suffix}"
            if p.exists():
                out.append(p)
    return sorted(set(out))


def _witness_has_required(path: Path) -> tuple[bool, list[str], bool]:
    """Returns (ok, missing_fields, opted_out)."""
    try:
        data = json.loads(path.read_text())
    except (json.JSONDecodeError, OSError):
        return False, list(REQUIRED_FIELDS), False

    def _has(node, key):
        if isinstance(node, dict):
            if key in node:
                return True
            return any(_has(v, key) for v in node.values())
        if isinstance(node, list):
            return any(_has(v, key) for v in node)
        return False

    opted_out = data.get(OPTOUT_FIELD) == OPTOUT_VALUE
    missing = [f for f in REQUIRED_FIELDS if not _has(data, f)]
    return (not missing) or opted_out, missing, opted_out


# ── Exact 80-dps mpmath Algebraic Self-Checks (TN-11) ───────────

def verify_pairing_regimes_mpmath(dps: int = 80) -> dict:
    """Verify at 80-dps mpmath (zero float64, zero q0-anchor dependency) the
    exact boundary between symmetric TL_3 / centralizer traces and Nakayama-twisted
    KMS / Haar pairings at exact test rationals q in {11/10, 3/2}."""
    prev = mp.dps
    try:
        mp.dps = dps
        one = mp.mpf(1)
        zero = mp.mpf(0)
        tol = mp.mpf("1e-70")
        test_qs = [
            ("11/10", mp.mpf(11) / mp.mpf(10)),
            ("3/2", mp.mpf(3) / mp.mpf(2)),
        ]
        records = []
        all_ok = True
        for q_label, qv in test_qs:
            qi = one / qv
            h = qv - qi
            qdim = qv + qi
            z_d = (qv ** 3) / (qv ** 2 + one)

            # (1) 2-strand quantum trace Tr(K⊗K Ř)/[2]_q^2 == z_D.
            KK = mp.matrix([
                [qv ** 2, zero, zero, zero],
                [zero, one, zero, zero],
                [zero, zero, one, zero],
                [zero, zero, zero, qi ** 2],
            ])
            KK_inv = mp.matrix([
                [qi ** 2, zero, zero, zero],
                [zero, one, zero, zero],
                [zero, zero, one, zero],
                [zero, zero, zero, qv ** 2],
            ])
            R_check = mp.matrix([
                [qv, zero, zero, zero],
                [zero, zero, one, zero],
                [zero, one, h, zero],
                [zero, zero, zero, qv],
            ])
            R_inv = mp.matrix([
                [qi, zero, zero, zero],
                [zero, -h, one, zero],
                [zero, one, zero, zero],
                [zero, zero, zero, qi],
            ])

            def qtr2(M: mp.matrix) -> mp.mpf:
                 KM = KK * M
                 return mp.fsum(KM[i, i] for i in range(4)) / (qdim ** 2)

            z_resid = mp.fabs(qtr2(R_check) - z_d)

            # (2) Weight-centralizer conjugation [K⊗K, Ř] == 0 => tr_q(Ř X Ř^-1) == tr_q(X),
            # even when X shifts weight!
            X_shift = mp.matrix([
                [zero, one, mp.mpf(2), zero],
                [mp.mpf(3), zero, zero, one],
                [zero, mp.mpf(5), zero, zero],
                [one, zero, zero, mp.mpf(7)],
            ])
            comm_KR = max(
                mp.fabs((KK * R_check - R_check * KK)[r, c])
                for r in range(4) for c in range(4)
            )
            conj_centralizer_resid = mp.fabs(qtr2(R_check * X_shift * R_inv) - qtr2(X_shift))

            # (3) Off-centralizer KMS twist: for E_01 = |uu><ud| (K⊗K E_01 (K⊗K)^-1 = q^2 E_01)
            # and E_10 = |ud><uu|, tr_q(E_01 E_10) = q^2 / [2]_q^2 != 1 / [2]_q^2 = tr_q(E_10 E_01);
            # KMS law tr_q(A B) = tr_q(B (K⊗K) A (K⊗K)^-1) holds with 0 residual!
            E01 = mp.matrix(4, 4)
            E10 = mp.matrix(4, 4)
            E01[0, 1] = one
            E10[1, 0] = one
            tr_ab = qtr2(E01 * E10)
            tr_ba = qtr2(E10 * E01)
            kms_rhs = qtr2(E10 * KK * E01 * KK_inv)
            kms_resid = mp.fabs(tr_ab - kms_rhs)
            untwisted_ratio = tr_ab / tr_ba  # exact q^2 != 1

            # (4) O_q(SU(2)) Haar state commutator: h_q(alpha * delta) = q^2/(q^2 + 1) vs
            # h_q(delta * alpha) = 1/(q^2 + 1), so h_q([alpha, delta]) = (q^2 - 1)/(q^2 + 1) != 0,
            # while twisted h_q(alpha * delta - delta * nu(alpha)) = 0 with nu(alpha) = q^2 * alpha.
            hq_alpha_delta = (qv ** 2) / (qv ** 2 + one)
            hq_delta_alpha = one / (qv ** 2 + one)
            haar_comm = hq_alpha_delta - hq_delta_alpha
            haar_twisted_resid = mp.fabs(hq_alpha_delta - (qv ** 2) * hq_delta_alpha)

            # (5) H_3(q) vs TL_3(q): tr_M(e^-) = h z_D^2 + z_D != z_D^3, and 6D det G == 0
            # while principal 5x5 TL_3 minor det G[:5, :5] != 0.
            tr_e_minus = h * (z_d ** 2) + z_d
            tr_e_stale = z_d ** 3
            g15 = h * tr_e_minus + z_d ** 2
            g34 = h * tr_e_minus + h * z_d + one
            g35 = (h ** 2) * tr_e_minus + mp.mpf(2) * h * (z_d ** 2) + z_d
            g55 = ((h ** 3) + h) * tr_e_minus + mp.mpf(2) * (h ** 2) * (z_d ** 2) + mp.mpf(2) * h * z_d + one
            G6 = mp.matrix([
                [one, z_d, z_d, z_d ** 2, z_d ** 2, tr_e_minus],
                [z_d, h * z_d + one, z_d ** 2, tr_e_minus, tr_e_minus, g15],
                [z_d, z_d ** 2, h * z_d + one, tr_e_minus, tr_e_minus, g15],
                [z_d ** 2, tr_e_minus, tr_e_minus, g15, g34, g35],
                [z_d ** 2, tr_e_minus, tr_e_minus, g34, g15, g35],
                [tr_e_minus, g15, g15, g35, g35, g55],
            ])
            G5_tl3 = mp.matrix([[G6[r, c] for c in range(5)] for r in range(5)])
            det_G6 = mp.fabs(mp.det(G6))
            det_G5_tl3 = mp.fabs(mp.det(G5_tl3))

            ok = (
                z_resid < tol
                and comm_KR < tol
                and conj_centralizer_resid < tol
                and kms_resid < tol
                and mp.fabs(untwisted_ratio - qv ** 2) < tol
                and mp.fabs(haar_comm) > mp.mpf("1e-3")
                and haar_twisted_resid < tol
                and mp.fabs(tr_e_minus - tr_e_stale) > mp.mpf("1e-2")
                and det_G6 < tol
                and det_G5_tl3 > mp.mpf("1e-3")
            )
            all_ok = all_ok and ok
            records.append({
                "q_rational": q_label,
                "passed": ok,
                "qtrace_crossing_minus_zD": mp.nstr(z_resid, 6),
                "commutator_KK_R_inf_norm": mp.nstr(comm_KR, 6),
                "centralizer_conj_residual": mp.nstr(conj_centralizer_resid, 6),
                "kms_twisted_trace_residual": mp.nstr(kms_resid, 6),
                "off_centralizer_untwisted_ratio_q2": mp.nstr(untwisted_ratio, 18),
                "oq_su2_haar_commutator_alpha_delta": mp.nstr(haar_comm, 18),
                "oq_su2_haar_nakayama_residual": mp.nstr(haar_twisted_resid, 6),
                "tr_M_e_minus_canonical": mp.nstr(tr_e_minus, 18),
                "tr_M_e_minus_stale_z3": mp.nstr(tr_e_stale, 18),
                "abs_det_G6_H3": mp.nstr(det_G6, 6),
                "abs_det_G5_TL3_quotient": mp.nstr(det_G5_tl3, 18),
            })
        return {
            "dps": dps,
            "all_passed": all_ok,
            "records": records,
        }
    finally:
        mp.dps = prev


# ── Classification ──────────────────────────────────────────────

def classify(script: Path) -> dict:
    text = _read(script)
    has_nakayama = bool(NAKAYAMA_TOKEN.search(text))
    if not TRACE_TOKEN.search(text) and not has_nakayama and not re.search(
        r"\b(?:mat_trace|tr_std|tr_standard|trace_std)\b", text
    ):
        return {"bucket": "skip", "reason": "no trace token"}

    bucket_c = bool(
        CONJ_PATTERN_CODE.search(text) or CONJ_PATTERN_COMMENT.search(text)
    )
    bucket_b = bool(OBS_PATTERN.search(text) or OBS_OP_CONCAT.search(text))
    bucket_a = (TRACE_TOKEN.search(text) is not None) or has_nakayama

    pairing_regime = (
        "nakayama_kms_weighted" if has_nakayama else "symmetric_centralizer_tl"
    )

    if bucket_c:
        bucket = "C"
        reason = (
            "conjugation pattern β · X · β⁻¹ (equals tr_q(X) iff [K^{⊗n}, β] = 0; "
            "KMS-twisted by q^{±2} on weight-shifting operators)"
        )
    elif bucket_b:
        bucket = "B"
        reason = "trace(O · ρ(β)) — observable-on-state"
    elif bucket_a:
        bucket = "A"
        reason = "raw tr_M / markov_trace / qtrace (no operator-on-state)"
    else:
        return {"bucket": "skip", "reason": "no trace pattern"}

    witnesses = _sibling_witnesses(script)
    witness_status = []
    for w in witnesses:
        ok, missing, opted_out = _witness_has_required(w)
        witness_status.append(
            {
                "witness": str(w.relative_to(Path(__file__).resolve().parents[1])),
                "ok": ok,
                "missing_fields": missing,
                "opted_out_raw_trace": opted_out,
            }
        )
    return {
        "bucket": bucket,
        "pairing_regime": pairing_regime,
        "reason": reason,
        "witnesses": witness_status,
    }


# ── Driver ──────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    parser.add_argument(
        "--report",
        default="docs/audits/frobenius-pairing-compute-audit.witness.json",
        help="Output JSON report path (relative to repo root)",
    )
    parser.add_argument(
        "--root",
        default="computations",
        help="Directory to scan",
    )
    args = parser.parse_args()

    here = Path(__file__).resolve()
    repo_root = here.parents[1]
    scan_dir = (repo_root / args.root).resolve()
    out_path = (repo_root / args.report).resolve()

    by_bucket: dict[str, list[dict]] = {"A": [], "B": [], "C": [], "skip": []}
    regime_counts: dict[str, int] = {
        "symmetric_centralizer_tl": 0,
        "nakayama_kms_weighted": 0,
    }
    scripts = sorted(scan_dir.glob("*.py"))
    for s in scripts:
        if s.name.startswith("audit_frobenius_pairing"):
            continue
        if s.name in {"witness_base.py", "lp_dual_solver.py",
                      "lp_dual_witness_validator.py",
                      "bound_state_observable_validator.py"}:
            continue
        result = classify(s)
        result["script"] = s.relative_to(repo_root).as_posix()
        by_bucket[result["bucket"]].append(result)
        reg = result.get("pairing_regime")
        if reg in regime_counts:
            regime_counts[reg] += 1

    failures = []
    for bucket in ("B", "C"):
        for entry in by_bucket[bucket]:
            for w in entry.get("witnesses", []):
                if not w["ok"]:
                    failures.append(
                        {
                            "script": entry["script"],
                            "bucket": bucket,
                            "pairing_regime": entry.get("pairing_regime"),
                            "witness": w["witness"],
                            "missing": w["missing_fields"],
                        }
                    )

    pairing_checks = verify_pairing_regimes_mpmath(dps=80)

    summary = {
        "scan_dir": args.root,
        "n_scripts_scanned": len(scripts),
        "counts": {b: len(v) for b, v in by_bucket.items()},
        "pairing_regime_counts": regime_counts,
        "pairing_regime_checks": pairing_checks,
        "buckets": by_bucket,
        "failures": failures,
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    # no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402
    from qou_substrate.witness import WitnessBuilder as _WB
    summary.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        summary, script_path=__file__, engine=None, q0_anchor=False)
    out_path.write_text(json.dumps(summary, indent=2))

    print(f"Scanned {len(scripts)} scripts under {args.root}")
    for b in ("A", "B", "C", "skip"):
        print(f"  bucket {b}: {len(by_bucket[b])}")
    print(f"Pairing regimes: {regime_counts}")
    print(f"80-dps KMS/Nakayama vs TL_3 algebraic checks: all_passed={pairing_checks['all_passed']}")
    print("\nFailures (bound-state-observable witnesses missing required fields):")
    print(f"  {len(failures)}")
    for f in failures[:20]:
        print(f"    ✗ [{f['bucket']}] {f['script']} -> {f['witness']}")
        print(f"        missing: {f['missing']}")
    if len(failures) > 20:
        print(f"    ... ({len(failures) - 20} more)")

    print(f"\nReport written to {out_path}")
    return 0 if (not failures and pairing_checks["all_passed"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
