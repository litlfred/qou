#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath consumer; Rust binary
# returns f64 χ^λ values which we combine with y_λ(q_0) from
# `wedderburn_jones_markov.y_lambda_at(n, q_0)` at mpmath precision.
"""Canonical |tr_M(β_canonical(Z, N))| via Rust + Python combiner.

This is the canonical-side consumer described in
`docs/audits/2026-05-17-knot-fusion-step1-audit.md` §"Gap to
canonical |tr_M| at 1 ppb":

    |tr_M(β)| = | Σ_λ y_λ(q_0) · χ^λ(β) |
              = (1/averaging_denominator) · | Σ_λ y_λ · χ^λ_unnormalised |

where:
- `χ^λ(β)` for canonical atomic β at H_n is computed by the Rust
  binary `hecke-canonical-chi` (release build, f64 Hoefsmit
  seminormal with averaged-crossing expansion); the binary returns
  the UNNORMALISED 2^k sum.
- `y_λ(q_0)` is loaded from
  `wedderburn_jones_markov.y_lambda_at(n, q_0)`.
- `averaging_denominator = 2^k` where k = number of averaged
  crossings in the canonical decomposition.

Replaces the broken `rho_k_full_via_wenzl_lr.py` consumer (which
used tensor-product LR; off by ~80 % vs Hoefsmit on D/T/³He per
`cross_check_trM_wenzl_lr_1ppb.py`).

Python backup: `per_irrep_pole_atom.py` (sympy, symbolic-q;
slower but no f64 round-off, handles partial chi caches).

Workplan ref: `docs/audits/2026-05-17-1ppb-workplan-v4.md`
§"Wenzl LR consumer bug" → §"Step 2 plan".
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 30

REPO_ROOT = HERE.parent.parent
BIN_CANDIDATES = [
    REPO_ROOT / "tools" / "hecke-engine" / "target" / "release"
    / "hecke-canonical-chi",
    REPO_ROOT / "tools" / "hecke-engine" / "target" / "debug"
    / "hecke-canonical-chi",
    Path(shutil.which("hecke-canonical-chi") or "/nonexistent"),
]

CTYPE_TO_SIGN = {"sigma": 1, "sigma_inv": -1, "averaged": 0}

# Atoms with cached y_λ(q_0) (n=2..12 from y-lambda-at-q0.witness.json).
ATOMS = [
    (1, 0, "p"),
    (0, 1, "n"),
    (1, 1, "D"),
    (1, 2, "T"),
    (2, 1, "3He"),
    (2, 2, "4He"),
]


def find_binary() -> Path | None:
    for c in BIN_CANDIDATES:
        if c.exists():
            return c
    return None


def canonical_word_for(Z: int, N: int) -> tuple[int, list[list[int]]]:
    """Return (n_strands, word) for the canonical (Z, N) atomic
    braid in the binary's wire format."""
    from canonical_braid_crossings import atom_canonical_crossings
    pairs = atom_canonical_crossings(Z, N)
    # 0-based gen → 1-based per the binary's wire format.
    word = [[CTYPE_TO_SIGN[ctype], int(g) + 1] for (g, ctype) in pairs]
    n_strands = 3 * (Z + N)
    return n_strands, word


def compute_tr_m(Z: int, N: int, label: str,
                 *, q_val: float | None = None,
                 timeout_sec: int = 600) -> dict:
    bin_path = find_binary()
    if bin_path is None:
        return {
            "atom": label, "Z": Z, "N": N,
            "tr_M_q0_unavail_reason": (
                "hecke-canonical-chi binary not built. Build via: "
                "cd tools/hecke-engine && cargo build --release "
                "--bin hecke-canonical-chi"
            ),
        }
    from q_parameter import Q as Q_FLOAT, Q_50_DIGIT_STR
    if q_val is None:
        q_val = Q_FLOAT
    n_strands, word = canonical_word_for(Z, N)
    spec = {
        "n_strands": n_strands,
        "q": q_val,
        "q_str": Q_50_DIGIT_STR,
        "label": label,
        "word": word,
    }
    # Default Rust path: MPFR at 50 dps (per user direction
    # "only do arbitrary precision w/ >= 50 dps").  Pass --dps 0
    # to fall back to f64 for fast prototyping.
    result = subprocess.run(
        [str(bin_path), "--dps", "50"],
        input=json.dumps(spec),
        capture_output=True, text=True, timeout=timeout_sec,
    )
    if result.returncode != 0:
        return {
            "atom": label, "Z": Z, "N": N,
            "tr_M_q0_unavail_reason": (
                f"hecke-canonical-chi exit {result.returncode}: "
                f"{result.stderr[:300]}"
            ),
        }
    rust_out = json.loads(result.stdout)
    averaging_denom = int(rust_out["averaging_denominator"])

    # Combine χ^λ × y_λ(q_0).
    from wedderburn_jones_markov import y_lambda_at
    y_table = y_lambda_at(n_strands, q_val)

    # Match Rust output precision; default ≥50 dps per user
    # direction "only do arbitrary precision w/ >= 50 dps".
    rust_dps = int(rust_out["chi_lambda_terms"][0]["precision_dps"]) \
        if rust_out["chi_lambda_terms"] else 50
    if rust_dps > mp.mp.dps:
        mp.mp.dps = rust_dps
    tr_m_sum = mp.mpf(0)
    contributions = []
    for term in rust_out["chi_lambda_terms"]:
        lam = tuple(term["lambda"])
        # Rust now returns chi as a decimal string at `precision_dps`
        # precision (MPFR path).  Parse directly into mpmath at
        # mp.mp.dps for end-to-end ≥50 dps precision.
        chi_str = term.get("chi_q_normalised") \
            or term.get("chi_q_f64_normalised")  # legacy field
        chi_at_q0 = mp.mpf(str(chi_str))
        y_lam = y_table.get(lam)
        if y_lam is None:
            return {
                "atom": label, "Z": Z, "N": N,
                "tr_M_q0_unavail_reason": (
                    f"y_λ table at H_{n_strands} missing λ={lam}"
                ),
            }
        # y_lam is typically a sympy.Float at 30+ dps; `mp.mpf(str(y_lam))`
        # preserves that precision.  The matching `chi_f64` is at the
        # f64 floor (~15 sig figs) from the Rust binary, so the product
        # carries the f64-side floor; widening `y_at_q0` to mp precision
        # avoids stacking *two* downcasts (per gemini review on #683).
        y_at_q0 = mp.mpf(str(y_lam))
        chi_at_q0 = mp.mpf(repr(chi_f64))
        c = y_at_q0 * chi_at_q0
        tr_m_sum += c
        contributions.append({
            "lambda": list(lam),
            "chi_normalised": mp.nstr(chi_at_q0, 30),
            "y_q0": mp.nstr(y_at_q0, 30),
            "contribution": mp.nstr(c, 30),
        })
    return {
        "atom": label, "Z": Z, "N": N,
        "n_strands": n_strands,
        "n_crossings": rust_out["n_crossings"],
        "n_averaged_crossings": rust_out["n_averaged_crossings"],
        "averaging_denominator": averaging_denom,
        "rust_duration_ms": rust_out["duration_ms"],
        "tr_M_q0_mp30dps": mp.nstr(tr_m_sum, 30),
        "abs_tr_M_q0_mp30dps": mp.nstr(abs(tr_m_sum), 30),
        "top5_contributions": sorted(
            contributions,
            key=lambda d: abs(mp.mpf(d["contribution"])),
            reverse=True,
        )[:5],
    }


def main() -> int:
    rows = []
    for (Z, N, label) in ATOMS:
        print(f"\n→ Canonical |tr_M({label})| at H_{3*(Z+N)} via Rust...")
        row = compute_tr_m(Z, N, label)
        rows.append(row)
        if "tr_M_q0_unavail_reason" in row:
            print(f"  ✗ {row['tr_M_q0_unavail_reason']}")
        else:
            print(f"  |tr_M| = {row['abs_tr_M_q0_mp30dps']}  "
                  f"({row['rust_duration_ms']} ms Rust, "
                  f"k_avg={row['n_averaged_crossings']}, "
                  f"denom={row['averaging_denominator']})")

    out = {
        "computation": "canonical-tr-m-via-rust",
        "description": (
            "Canonical |tr_M(β_canonical(Z, N))| via Rust+Python: the "
            "Rust binary `hecke-canonical-chi` computes per-partition "
            "χ^λ(β) at H_n via direct f64 Hoefsmit (with averaged-"
            "crossing expansion), and this script combines with "
            "y_λ(q_0) from wedderburn_jones_markov to yield "
            "|tr_M| = (1/2^k) · |Σ_λ y_λ · χ^λ_unnormalised|. Replaces "
            "the broken tensor-product `rho_k_full_via_wenzl_lr.py`."
        ),
        "rows": rows,
    }
    out_path = (
        WitnessBuilder.wrap_legacy(
            "canonical-tr-m-via-rust", out,
            script_path=__file__, engine="rust+mpmath",
        )
        .set_audit_only(
            "docs/audits/2026-05-17-knot-fusion-step1-audit.md")
        .save()
    )
    print(f"\n→ wrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
