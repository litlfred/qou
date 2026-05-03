#!/usr/bin/env python3
"""
Term 6 of the six-term mass formula via Markov-peel symbolic `tr_M(q)`.

`thm:six-term-mass-formula-complete` defines

    Term 6  =  Σ_{ℓ ≥ 2}  Res_{q = ζ_ℓ}[tr_M(T_w)] / (q₀ − ζ_ℓ)

where ζ_ℓ = exp(2πi / ℓ) is a primitive ℓ-th root of unity and the
sum runs over the simple poles of `tr_M(T_w)` in q (per
`prop:full-pole-structure-mass-trace`, the Markov trace of any atomic
braid is meromorphic in q with simple poles at every primitive root
of unity).

This module is the production evaluator for Term 6.  It hangs off
`markov_peel.tr_M_atomic`, which returns the symbolic tr_M(q) as a
sympy expression — `sympy.residue` then extracts each pole residue
exactly, with zero numerical drift.

Pre-recursive-ascent (i.e. with the Hoefsmit + Wenzl path) Term 6
was effectively unreachable: building tr_M(q) symbolically required
multiplying dim-462 sympy matrices through the braid, which is the
bottleneck that motivated #508.  The recursive-ascent path returns
a symbolic rational function in q in seconds–minutes per atom,
making Term 6 a one-line residue extraction.

Witness:  term6-residues-at-roots.witness.json
Reference: thm:six-term-mass-formula-complete (Term 6),
           prop:full-pole-structure-mass-trace (pole structure)

Usage:
    python folio-assistant/computations/term6_residues_at_roots.py
    python folio-assistant/computations/term6_residues_at_roots.py --max-ell 12
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import sympy as sp
import mpmath

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from markov_peel import tr_M_atomic                      # noqa: E402
from hecke_symbolic import q as q_sym                     # noqa: E402
from q_parameter import Q as Q0                           # noqa: E402
from witness_base import WitnessBuilder                   # noqa: E402

# Pin precision floor; matches the markov-peel witness convention.
mpmath.mp.dps = 50


# Atom spectrum.  Beyond ⁴He the symbolic tr_M(q) has thousands of
# polynomial terms, and `sp.residue` slows; default is the cheap
# spectrum.  --include-li adds ⁵Li (and could be extended).
ATOMS_DEFAULT = [
    ("proton",   1, 0),
    ("neutron",  0, 1),
    ("deuteron", 1, 1),
    ("tritium",  1, 2),
    ("helium-3", 2, 1),
    ("helium-4", 2, 2),
]


def residues_at_roots(
    tr_sym, *, max_ell: int = 4, per_ell_timeout_sec: int = 60
) -> list[dict]:
    """Compute Res_{q = ζ_ℓ}[tr_sym(q)] for ℓ = 2, ..., max_ell.

    Each ℓ is wrapped in a SIGALRM-based timeout because
    `sp.simplify` of expressions involving roots of unity at composite
    ℓ can be slow (we observed ~22 s for ℓ = 5 on the proton's
    138-op rational form, so atoms with ~5000-op expressions can
    exceed several minutes per ℓ).

    Returns one row per ℓ with the residue as a sympy expression and
    its numerical magnitude; rows with vanishing residue are kept
    (they're physical information — the pole at that ζ_ℓ doesn't
    contribute).  Failed rows include an `error` field and skip the
    residue contribution to Term 6.
    """
    import signal

    class _Timeout(Exception):
        pass

    def _alarm(_signum, _frame):
        raise _Timeout()

    rows = []
    for ell in range(2, max_ell + 1):
        zeta = sp.exp(2 * sp.pi * sp.I / ell)
        signal.signal(signal.SIGALRM, _alarm)
        signal.alarm(per_ell_timeout_sec)
        try:
            res = sp.residue(tr_sym, q_sym, zeta)
            # `sp.cancel` is significantly faster than `sp.simplify`
            # for rational expressions and is sufficient here — the
            # residues are rational functions of q with roots-of-unity
            # algebraic-number coefficients.  Using `simplify` was a
            # 22 s bottleneck on the proton's ζ_5 case (see PR #526
            # discussion).
            res_simp = sp.cancel(res)
            signal.alarm(0)
        except _Timeout:
            signal.alarm(0)
            rows.append({
                "ell": ell,
                "zeta_symbolic": str(zeta),
                "residue_symbolic": None,
                "residue_value": None,
                "residue_abs": None,
                "error": f"timeout > {per_ell_timeout_sec}s",
            })
            continue
        except (NotImplementedError, RecursionError) as exc:
            signal.alarm(0)
            rows.append({
                "ell": ell,
                "zeta_symbolic": str(zeta),
                "residue_symbolic": None,
                "residue_value": None,
                "residue_abs": None,
                "error": f"{type(exc).__name__}: {exc}",
            })
            continue

        try:
            res_num = complex(sp.N(res_simp, 30))
            res_abs = abs(res_num)
        except Exception:  # noqa: BLE001
            res_num = None
            res_abs = None
        rows.append({
            "ell": ell,
            "zeta_symbolic": str(zeta),
            "residue_symbolic": str(res_simp),
            "residue_value": str(res_num) if res_num is not None else None,
            "residue_abs": (
                f"{res_abs:.6e}" if res_abs is not None else None
            ),
        })
    return rows


def term6_contribution_at_q0(rows) -> str:
    """Sum Σ_{ℓ ≥ 2} Res_{q=ζ_ℓ} / (q₀ − ζ_ℓ) for the residue rows
    that successfully evaluated.  Returns the mpmath-string form.

    Magnitudes only — for any individual atom many residues vanish
    (cf. proton: only ζ_2 has a non-zero residue out of {2,3,4,6}).
    """
    total = mpmath.mpc(0)
    q0_mp = mpmath.mpf(str(Q0))
    for row in rows:
        if row.get("residue_value") in (None, "None"):
            continue
        ell = row["ell"]
        zeta = mpmath.exp(2 * mpmath.pi * mpmath.mpc(0, 1) / ell)
        try:
            res = mpmath.mpmathify(row["residue_value"])
        except Exception:  # noqa: BLE001
            continue
        denom = q0_mp - zeta
        # Tolerance scales with the current precision floor — at 50 dps
        # the smallest representable magnitude is ~10^-50; we treat
        # anything within ~10 digits of that as "effectively zero" and
        # skip to avoid spurious divisions.  Per Gemini policy
        # (PR #526), the bound tracks `mp.dps` rather than a hardcode.
        if abs(denom) < mpmath.power(10, -mpmath.mp.dps + 10):
            continue
        total += res / denom
    return mpmath.nstr(total, 30)


def compute_atom(
    Z: int, N: int, *, max_ell: int, per_ell_timeout_sec: int = 60
) -> dict:
    """Run Term 6 for atom (Z, N) at the given pole-truncation order."""
    A = Z + N
    t0 = time.time()
    tr_sym = tr_M_atomic(Z, N)
    t_peel = time.time() - t0

    t0 = time.time()
    tr_simp = sp.cancel(tr_sym)
    t_cancel = time.time() - t0

    t0 = time.time()
    rows = residues_at_roots(
        tr_simp, max_ell=max_ell,
        per_ell_timeout_sec=per_ell_timeout_sec,
    )
    t_res = time.time() - t0

    contribution = term6_contribution_at_q0(rows)
    return {
        "Z": Z,
        "N": N,
        "A": A,
        "max_ell": max_ell,
        "tr_M_symbolic_ops": int(sp.count_ops(tr_simp)),
        "elapsed_peel_sec": round(t_peel, 3),
        "elapsed_cancel_sec": round(t_cancel, 3),
        "elapsed_residues_sec": round(t_res, 3),
        "residues": rows,
        "term6_at_q0": contribution,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--max-ell", type=int, default=4,
        help=(
            "Pole-truncation order: include residues at ζ_ℓ for ℓ ≤ this. "
            "Default 4 (small enough for proton+neutron+D in <2 min); "
            "increase for finer truncation at higher CPU cost."
        ),
    )
    parser.add_argument(
        "--per-ell-timeout", type=int, default=60,
        help="SIGALRM cap (seconds) per ℓ for sp.simplify of the residue.",
    )
    parser.add_argument(
        "--atoms", type=str, default="proton,neutron,deuteron",
        help=(
            "Comma-separated atom labels to run.  Default: lightest 3 "
            "(witness for fuller spectrum requires a longer run "
            "budget — sp.residue scales with the symbolic ops in tr_M)."
        ),
    )
    args = parser.parse_args()
    selected = set(args.atoms.split(","))

    print(
        f"Term 6 residues at primitive roots ζ_ℓ "
        f"(ℓ = 2..{args.max_ell}) — Markov-peel symbolic tr_M(q)",
        flush=True,
    )
    print("=" * 72, flush=True)

    rows = []
    for label, Z, N in ATOMS_DEFAULT:
        if label not in selected:
            continue
        print(f"\n=== {label} (Z={Z}, N={N}, A={Z + N}) ===", flush=True)
        try:
            row = compute_atom(
                Z, N, max_ell=args.max_ell,
                per_ell_timeout_sec=args.per_ell_timeout,
            )
            row["atom"] = label
            print(
                f"  peel={row['elapsed_peel_sec']:.1f}s  "
                f"cancel={row['elapsed_cancel_sec']:.2f}s  "
                f"residues={row['elapsed_residues_sec']:.2f}s  "
                f"ops={row['tr_M_symbolic_ops']}",
                flush=True,
            )
            for r in row["residues"]:
                if r.get("residue_value") in (None, "None"):
                    print(
                        f"    ζ_{r['ell']}: residue = ZERO or unevaluable",
                        flush=True,
                    )
                else:
                    print(
                        f"    ζ_{r['ell']}: residue = {r['residue_symbolic']}",
                        flush=True,
                    )
            print(f"  Σ Res/(q₀−ζ_ℓ) = {row['term6_at_q0']}", flush=True)
            rows.append(row)
        except Exception as exc:  # noqa: BLE001
            print(f"  FAILED: {type(exc).__name__}: {exc}", flush=True)
            rows.append({
                "atom": label, "Z": Z, "N": N, "A": Z + N,
                "error": f"{type(exc).__name__}: {exc}",
            })

    w = WitnessBuilder("term6-residues-at-roots", engine="sympy")
    w.set_description(
        f"Term 6 of thm:six-term-mass-formula-complete via Markov-peel "
        f"symbolic tr_M(q): Σ_{{ℓ≥2}} Res_{{q=ζ_ℓ}}[tr_M(T_w)] / (q₀ − ζ_ℓ), "
        f"with ℓ truncated at {args.max_ell}.  This evaluation is enabled "
        f"by the Markov-axiom recursive ascent (#508 / PR #516) returning "
        f"tr_M as a symbolic rational function in q; the Hoefsmit per-block "
        f"path could not produce the symbolic form needed for residue "
        f"extraction at A ≥ 4."
    )
    w.set_content_block("thm:six-term-mass-formula-complete")
    w.add_parameter("q0", str(Q0))
    w.add_parameter("max_ell", args.max_ell)
    w.add_data("results", rows)
    out_path = w.save()
    print(f"\n  → wrote {out_path}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
