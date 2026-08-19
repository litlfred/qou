#!/usr/bin/env python3
"""_helium_habiro_coefficient_extract.py — Phase 5q ³He / ⁴He Habiro
coefficients via the canonical closed form.

Per [`docs/audits/2026-06-01-qbeta-habiro-phi8-interpretation.md`] and
[`docs/coordination/2026-06-01-qbeta-habiro-followup.md`] (Track 3),
the strand-doubling Φ_16 / Φ_32 falsifiable predictions require
³He and ⁴He Habiro coefficients.  The existing
`habiro-coefficients-atomic.witness.json` only ships p, n, D.

CLOSED FORMS (per the task spec):

    tr_M(³He, q) = τ_p(q)² · τ_n(q) · z(q)²
    tr_M(⁴He, q) = τ_p(q)² · τ_n(q)² · z(q)² · (z(q) − h(q))

where
    z(q) = 1 / (q^{1/2} + q^{-1/2})
    h(q) = q − q^{-1}

and τ_p, τ_n are the H_3 Markov traces of the canonical proton /
neutron 3-strand braid words (chi_lambda_braid convention — production
pipeline default).  These closed forms correspond to the canonical
interface kinds for Z=2,N=1 ("ppn" → +, +) and Z=2,N=2 ("ppnn" → +, +, −).

APPROACH (symbolic-first):
  1. Read τ_p(q), τ_n(q) **as symbolic rationals in q** from the
     existing `habiro-coefficients-atomic.witness.json` (its "p" and
     "n" entries carry `tr_M_in_q` strings already).
  2. Multiply by z(q)^k · (z(q)−h(q))^l per the closed forms.
  3. Convert to u-polynomial via `to_u_polynomial` (q = u²).
  4. Run `cyclotomic_expansion` to extract a_m coefficients.
  5. Verify reconstruction is exact and numerical match at q₀ holds
     to ≤ 1e-10 (much tighter than the 10-ppm spec).

This is the most compute-conservative path: no fresh y_λ · χ_λ
recompute over partitions of 9 (³He) or 12 (⁴He) — those would each
require minutes of symbolic work.  Instead we reuse the already-verified
symbolic τ_p, τ_n and the cheap interface multiplication, exactly as
the parent `closed_form_tau_M` module documents.

OUTPUTS:
  - habiro-coefficients-helium-3.witness.json
  - habiro-coefficients-helium-4.witness.json

Per AGENTS.md long-compute discipline:
    python3 -u _helium_habiro_coefficient_extract.py 2>&1 | tee /tmp/helium_habiro.log

Ref: prop:full-pole-structure-mass-trace
Ref: prop:constit-factor-tau-M-proton-identity
Ref: closed_form_tau_M.py (canonical closed-form module)
Ref: habiro_coefficients_atomic.py (cyclotomic expansion engine)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

# Reuse the canonical extraction primitives.
from habiro_coefficients_atomic import (  # noqa: E402
    to_u_polynomial,
    cyclotomic_expansion,
    reconstruct,
)
from q_parameter import Q_MP as _Q_CANONICAL  # noqa: E402


def _markov_z_q(q: sp.Symbol) -> sp.Expr:
    """z(q) = q^3 / (q^2 + 1) -- the production Markov parameter.

    Was 1/(q^{1/2} + q^{-1/2}), convention C, excised by the owner ruling of
    2026-08-09. Nothing flagged it: the audit keyed off an assignment TARGET
    and this computes straight into its return, so it had no name to match.
    """
    return q**3 / (q**2 + 1)


def _hecke_h_q(q: sp.Symbol) -> sp.Expr:
    """h(q) = q − q^{-1}."""
    return q - 1 / q


def _load_p_n_symbolic(habiro_path: Path, q: sp.Symbol):
    """Return (tau_p_in_q, tau_n_in_q) parsed from the existing witness."""
    data = json.loads(habiro_path.read_text())
    p_str = data["results"]["p (proton, A=1)"]["tr_M_in_q"]
    n_str = data["results"]["n (neutron, A=1)"]["tr_M_in_q"]
    # The strings use `q`, `sqrt(q)`, `q**(k/2)`; sympify resolves them
    # against the local `q` symbol.
    tau_p = sp.sympify(p_str, locals={"q": q})
    tau_n = sp.sympify(n_str, locals={"q": q})
    return tau_p, tau_n


def _build_closed_form(Z: int, N: int, tau_p, tau_n, q):
    """tr_M(⁴He) / tr_M(³He) per the spec's closed forms.

    Mirrors the canonical interface-kinds for (Z, N) under the
    chi_lambda_braid convention (production default):
      - p-p interface contributes z
      - p-n interface contributes z (chi_lambda_braid: averaging collapses)
      - n-n interface contributes z - h
    """
    z = _markov_z_q(q)
    h = _hecke_h_q(q)
    if (Z, N) == (2, 1):
        # ³He: ppn  →  p-p (z), p-n (z)  →  z²
        return tau_p ** 2 * tau_n * z ** 2
    if (Z, N) == (2, 2):
        # ⁴He: ppnn → p-p (z), p-n (z), n-n (z-h)  →  z² · (z-h)
        return tau_p ** 2 * tau_n ** 2 * z ** 2 * (z - h)
    raise ValueError(f"Unsupported (Z, N) = ({Z}, {N})")


def analyse_helium(label: str, Z: int, N: int, q,
                   tau_p, tau_n, q0_mp,
                   max_m: int = 64) -> dict:
    """Extract Habiro coefficients for ³He or ⁴He."""
    t0 = time.perf_counter()
    print(f"\n── {label} (Z={Z}, N={N}) ──")

    tr_M_q = _build_closed_form(Z, N, tau_p, tau_n, q)
    print(f"  tr_M closed-form built (free symbols: {tr_M_q.free_symbols})")
    print(f"    elapsed: {time.perf_counter() - t0:.2f} s")

    # Combine into a single rational in q before u-substitution; this
    # is the same `sp.together` discipline as habiro_coefficients_atomic.
    tr_M_q = sp.together(tr_M_q)
    print(f"  → together-reduced; chars = {len(str(tr_M_q))}")
    print(f"    elapsed: {time.perf_counter() - t0:.2f} s")

    u = sp.Symbol('u', positive=True, real=True)
    p_u, shift, denom = to_u_polynomial(tr_M_q, q, u)
    deg_p = int(sp.Poly(p_u, u).degree()) if p_u != 0 else 0
    print(f"  → p(u) := u^{shift} · denom · tr_M(u²)")
    print(f"     deg p(u) = {deg_p}")
    print(f"     denom (in u) = {denom}")
    print(f"    elapsed: {time.perf_counter() - t0:.2f} s")

    coeffs = cyclotomic_expansion(p_u, u, max_m=max_m)
    print(f"  Habiro coefficients (in u = q^{{1/2}}):")
    for entry in coeffs:
        flag = "✓" if entry["integral"] else "✗"
        a_repr = entry["a_m"]
        if len(a_repr) > 120:
            a_repr = a_repr[:117] + "..."
        print(f"    a_{entry['m']}(u) = {a_repr}    "
              f"deg = {entry['deg_a_m']}, integral: {flag}")
    print(f"    elapsed: {time.perf_counter() - t0:.2f} s")

    # Verify reconstruction is exact.
    recon = reconstruct(coeffs, u)
    diff = sp.expand(recon - p_u)
    recon_matches = (diff == 0)
    if recon_matches:
        print(f"  ✓ reconstruction matches  Σ a_m·(u;u)_m  =  p(u)")
    else:
        print(f"  ✗ reconstruction error:  diff has length {len(str(diff))} chars")
    print(f"    elapsed: {time.perf_counter() - t0:.2f} s")

    # Numerical check at q₀ via mpmath (50 dps).
    mp.mp.dps = 50
    q0 = q0_mp
    u0 = mp.sqrt(q0)
    # Evaluate tr_M_q at q₀ symbolically (then to float).
    tr_M_at_q0 = float(mp.mpf(str(sp.N(tr_M_q.subs(q, sp.Rational(str(q0))), 30))))
    # And via the p(u) / denom reconstruction.
    p_in_u_at_u0_mpf = mp.mpf(str(sp.N(p_u.subs(u, sp.Rational(str(u0))), 30)))
    denom_expr = sp.sympify(denom, locals={"u": u, "check_q": u})
    denom_at_u0_mpf = mp.mpf(str(sp.N(denom_expr.subs(u, sp.Rational(str(u0))), 30)))
    if shift:
        u0_shift = u0 ** shift
    else:
        u0_shift = mp.mpf(1)
    # Reconstruct: tr_M(q₀) = p(u₀) / (u₀^{shift} · denom(u₀))
    tr_M_via_u = float(p_in_u_at_u0_mpf / (u0_shift * denom_at_u0_mpf))
    rel_err = abs(tr_M_at_q0 - tr_M_via_u) / abs(tr_M_at_q0) if tr_M_at_q0 != 0 else 0.0

    print(f"  tr_M({label}) @ q_0 = {tr_M_at_q0:+.12e}")
    print(f"     via u-poly:        {tr_M_via_u:+.12e}")
    print(f"     rel diff:          {rel_err:.3e}")
    print(f"    elapsed: {time.perf_counter() - t0:.2f} s")

    return {
        "Z": Z, "N": N, "include_inter": True,
        "tr_M_in_q": str(tr_M_q),
        "shift": int(shift),
        "denom_in_u": denom,
        "p_in_u": str(p_u),
        "deg_p_u": deg_p,
        "habiro_coefficients": coeffs,
        "all_integral": all(c["integral"] for c in coeffs),
        "reconstruction_matches": recon_matches,
        "tr_M_at_q0": tr_M_at_q0,
        "tr_M_at_q0_via_u_poly": tr_M_via_u,
        "tr_M_at_q0_rel_err": rel_err,
    }


def _write_witness(path: Path, key: str, body: dict, q0_float: float,
                   description: str, reference_blocks: list[str]) -> None:
    """Write witness in atomic-witness-compatible format.

    The parent design script `qbeta_habiro_cross_pair_factorization.py`
    expects a top-level `habiro_coefficients` field plus a few metadata
    fields when reading helium-{3,4} witnesses (see `load_atom_from_external`).
    We also include the structural fields from the atomic witness so
    downstream consumers can treat the helium witnesses interchangeably.
    """
    witness = {
        "computation": f"habiro-coefficients-{key}",
        "description": description,
        "reference_blocks": reference_blocks,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": q0_float,
            "engine": "sympy Poly + sequential cyclotomic division "
                      "(via closed_form_tau_M closed form)",
            "pn_convention": "chi_lambda_braid (production default)",
            "source": "habiro-coefficients-atomic.witness.json (τ_p, τ_n)",
        },
        # The parent design script reads `habiro_coefficients` flat.
        "habiro_coefficients": body["habiro_coefficients"],
        # Plus the same shape as the atomic witness's per-entry record.
        "Z": body["Z"],
        "N": body["N"],
        "include_inter": body["include_inter"],
        "tr_M_in_q": body["tr_M_in_q"],
        "shift": body["shift"],
        "denom_in_u": body["denom_in_u"],
        "p_in_u": body["p_in_u"],
        "deg_p_u": body["deg_p_u"],
        "all_integral": body["all_integral"],
        "reconstruction_matches": body["reconstruction_matches"],
        "tr_M_at_q0": body["tr_M_at_q0"],
        "tr_M_at_q0_via_u_poly": body["tr_M_at_q0_via_u_poly"],
        "tr_M_at_q0_rel_err": body["tr_M_at_q0_rel_err"],
    }
    path.write_text(json.dumps(witness, indent=2, default=str))
    print(f"  Witness: {path}")


def main() -> int:
    t_overall = time.perf_counter()
    print("=" * 80)
    print("HABIRO COEFFICIENTS — ³He / ⁴He (Phase 5q closed-form route)")
    print("=" * 80)

    q0_float = float(_Q_CANONICAL)
    q0_mp = mp.mpf(str(_Q_CANONICAL))
    print(f"q_0 = {q0_float:.16f}")

    habiro_path = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
    if not habiro_path.exists():
        print(f"  FATAL: {habiro_path} not found")
        return 2

    q = sp.Symbol('q', positive=True, real=True)
    print("  Loading symbolic τ_p, τ_n from atomic witness …")
    tau_p, tau_n = _load_p_n_symbolic(habiro_path, q)
    print(f"     τ_p chars = {len(str(tau_p))}")
    print(f"     τ_n chars = {len(str(tau_n))}")
    print(f"     elapsed: {time.perf_counter() - t_overall:.2f} s")

    results = {}

    # ³He: Z=2, N=1
    try:
        results["he3"] = analyse_helium(
            "³He (helium-3, A=3)", 2, 1, q, tau_p, tau_n, q0_mp,
            max_m=48,
        )
    except Exception as exc:
        print(f"  ³He: ERROR {type(exc).__name__}: {exc}")
        import traceback
        traceback.print_exc()
        results["he3"] = {"error": f"{type(exc).__name__}: {exc}"}

    print(f"\n>>> elapsed after ³He: {time.perf_counter() - t_overall:.2f} s")

    # ⁴He: Z=2, N=2
    try:
        results["he4"] = analyse_helium(
            "⁴He (helium-4, A=4)", 2, 2, q, tau_p, tau_n, q0_mp,
            max_m=64,
        )
    except Exception as exc:
        print(f"  ⁴He: ERROR {type(exc).__name__}: {exc}")
        import traceback
        traceback.print_exc()
        results["he4"] = {"error": f"{type(exc).__name__}: {exc}"}

    print(f"\n>>> elapsed after ⁴He: {time.perf_counter() - t_overall:.2f} s")

    # ─── Write witnesses ────────────────────────────────────────
    reference_blocks = [
        "def:habiro-ring",
        "prop:full-pole-structure-mass-trace",
        "prop:constit-factor-tau-M-proton-identity",
        "prop:interface-knot-markov-z",
        "thm:knot-mass-formula-unified",
    ]
    if "error" not in results.get("he3", {}):
        _write_witness(
            _pb.witness_path("habiro-coefficients-helium-3.witness.json", HERE),
            "helium-3", results["he3"], q0_float,
            description=(
                "Habiro / cyclotomic expansion tr_M(³He, q) = Σ_m a_m·(u;u)_m "
                "(u = q^{1/2}) for helium-3 (Z=2, N=1) via the Phase 5q closed "
                "form tr_M(³He) = τ_p² · τ_n · z². Unlocks the strand-doubling "
                "Φ_16 falsifiable prediction for (³He−D) per "
                "docs/audits/2026-06-01-qbeta-habiro-phi8-interpretation.md."
            ),
            reference_blocks=reference_blocks,
        )

    if "error" not in results.get("he4", {}):
        _write_witness(
            _pb.witness_path("habiro-coefficients-helium-4.witness.json", HERE),
            "helium-4", results["he4"], q0_float,
            description=(
                "Habiro / cyclotomic expansion tr_M(⁴He, q) = Σ_m a_m·(u;u)_m "
                "(u = q^{1/2}) for helium-4 (Z=2, N=2) via the Phase 5q closed "
                "form tr_M(⁴He) = τ_p² · τ_n² · z² · (z−h). Unlocks the strand-"
                "doubling Φ_32 falsifiable prediction for (⁴He−³He) per "
                "docs/audits/2026-06-01-qbeta-habiro-phi8-interpretation.md."
            ),
            reference_blocks=reference_blocks,
        )

    print("\n── Summary ──")
    for label, r in results.items():
        if "error" in r:
            print(f"  {label}: ERROR {r['error']}")
            continue
        print(f"  {label}: deg p(u) = {r['deg_p_u']:>3}, "
              f"#Habiro coeffs = {len(r['habiro_coefficients']):>2}, "
              f"all integral: {r['all_integral']}, "
              f"reconstruction: {r['reconstruction_matches']}, "
              f"rel_err @ q_0: {r.get('tr_M_at_q0_rel_err', 'n/a'):.2e}")

    total = time.perf_counter() - t_overall
    print(f"\n  total elapsed: {total:.1f} s")
    return 0 if all("error" not in r for r in results.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
