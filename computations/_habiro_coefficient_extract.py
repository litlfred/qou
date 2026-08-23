#!/usr/bin/env python3
"""_habiro_coefficient_extract.py — mass-table-wide Habiro infrastructure
(PR #1642 follow-up).

Generalises the per-atom extractors (PR #1618 helium-3/⁴He;
PR #1642 ⁵Li/⁶Li/⁷Li/⁷Be) to **every canonical atom** in the
production mass-table list (`mass_at_3A_proper.py::ATOMS`).

Per AGENTS.md "Exception: batch audit-job runs" — this is a single
infra sweep generating:

  * one `habiro-coefficients-<atom>.witness.json` per canonical atom
    in a consistent schema matching the lithium-7 / beryllium-7 format,
  * one `habiro-coefficients-mass-table-summary.witness.json` collating
    cyclotomic / Φ_8 / Φ_1·Φ_2 stats across the full set,
  * mirror-pair sweep across every isospin pair (Z, N) ↔ (N, Z) in
    the canonical set, plus all distinct difference pairs (X − Y).

The Phase 5q closed form (`closed_form_tau_M.py`) provides
`tr_M(K, q) = τ_p^Z · τ_n^N · Π_i interface_factor(kind_i, q)` for
every (Z, N), with `canonical_interface_kinds(Z, N)` choosing the
±/averaged kinds under the production `chi_lambda_braid` convention.

OUTPUTS (per atom):
  * habiro-coefficients-<slug>.witness.json with:
      - Z, N, A, interface_kinds, tr_M_in_q, p_in_u, shift, denom_in_u,
        deg_p_u, habiro_coefficients (M-deep list of integer
        coefficients), all_integral, reconstruction_matches,
        tr_M_at_q0, tr_M_at_q0_via_u_poly, rel_err.

OUTPUTS (sweep):
  * habiro-coefficients-mass-table-summary.witness.json with:
      - per-atom: A, Z, N, label, max_m, deg_p_u, all_integral.
      - per-mirror-pair: phi_1, phi_2, phi_4, phi_8 multiplicities
        in the difference reconstruction.
      - phi_8 multiplicity scaling table (A-step → mult).

OUTPUTS (audit):
  * `docs/audits/2026-06-01-qbeta-habiro-mass-table-mirror-pair-tests.md`.

Per AGENTS.md long-compute discipline:
    python3 -u _habiro_coefficient_extract.py 2>&1 \
        | tee /tmp/mass_table_habiro.log

Ref: prop:full-pole-structure-mass-trace
Ref: prop:constit-factor-tau-M-proton-identity
Ref: closed_form_tau_M.py (canonical closed-form module)
Ref: habiro_coefficients_atomic.py (cyclotomic expansion engine)
Ref: _lithium_beryllium_habiro_coefficient_extract.py (per-atom template)
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

from witness_base import WitnessBuilder  # noqa: E402
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402
from habiro_coefficients_atomic import (  # noqa: E402
    to_u_polynomial,
    cyclotomic_expansion,
    reconstruct,
    str_in_u,
)
from closed_form_tau_M import canonical_interface_kinds  # noqa: E402
from q_parameter import Q_MP as _Q_CANONICAL  # noqa: E402
from q_parameter import Q_50_DIGIT_STR as _Q_CANONICAL_STR  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

# Raise working precision BEFORE any mpf is built from a decimal string.
# Idempotent, and deliberately at module scope: `mp.mpf("1.10997…")` parsed
# at the default 15 dps keeps 15 digits and pads the rest from binary64,
# and that is true of the *compliant-looking* string form too — the timing
# is what decides, not the argument type (bean qou-j6gb).
set_compute_dps()


# ──────────────────────────────────────────────────────────────────────
# Canonical atom list
# ──────────────────────────────────────────────────────────────────────
#
# Each entry: (label, slug, Z, N, max_m).  Slug is used for the witness
# filename `habiro-coefficients-<slug>.witness.json`.  max_m is chosen
# so the cyclotomic expansion terminates exactly (≈ 16·A is more than
# enough for A ≤ 12).
#
# This list mirrors:
#   * `mass_at_3A_proper.py::ATOMS` (the canonical mass-table list)
#   * `habiro_coefficients_atomic.py::_ATOM_CHI_LABEL_BY_ZN` (the chi
#      cache).
#
# p, n, D, T, ³He, ⁴He are extracted from the existing atomic witness
# (re-extracted here uniformly so all witnesses share one schema and
# one engine version).
ATOMS: list[tuple[str, str, int, int, int]] = [
    ("p (proton, A=1)",      "proton",      1, 0,  48),
    ("n (neutron, A=1)",     "neutron",     0, 1,  48),
    ("D (deuteron, A=2)",    "deuteron",    1, 1,  64),
    ("T (tritium, A=3)",     "tritium",     1, 2,  80),
    ("³He (helium-3, A=3)",  "helium-3",    2, 1,  80),
    ("⁴He (helium-4, A=4)",  "helium-4",    2, 2,  96),
    ("⁵Li (lithium-5, A=5)", "lithium-5",   3, 2, 112),
    ("⁵He (helium-5, A=5)",  "helium-5",    2, 3, 112),
    ("⁶Li (lithium-6, A=6)", "lithium-6",   3, 3, 128),
    ("⁶Be (beryllium-6, A=6)","beryllium-6", 4, 2, 128),
    ("⁶He (helium-6, A=6)",  "helium-6",    2, 4, 128),
    ("⁷Li (lithium-7, A=7)", "lithium-7",   3, 4, 144),
    ("⁷Be (beryllium-7, A=7)","beryllium-7", 4, 3, 144),
    ("⁸Be (beryllium-8, A=8)","beryllium-8", 4, 4, 160),
    ("⁸Li (lithium-8, A=8)", "lithium-8",   3, 5, 160),
    ("⁸B (boron-8, A=8)",    "boron-8",     5, 3, 160),
    ("⁹Be (beryllium-9, A=9)","beryllium-9", 4, 5, 176),
    ("⁹B (boron-9, A=9)",    "boron-9",     5, 4, 176),
    ("¹⁰Be (beryllium-10, A=10)","beryllium-10", 4, 6, 192),
    ("¹⁰B (boron-10, A=10)", "boron-10",    5, 5, 192),
    ("¹⁰C (carbon-10, A=10)","carbon-10",   6, 4, 192),
    # A=12 / A=14.  These five (with ⁶He above) have committed witnesses
    # written by THIS producer but had been dropped from the list, so a run
    # regenerated 20 of the 25 committed atoms and left the rest on whatever
    # convention they were last built under.  That is how a silently
    # mixed-convention mass table arises; see
    # docs/audits/2026-08-23-habiro-mass-table-convention-c-attribution.md.
    ("¹²B (boron-12, A=12)", "boron-12",    5, 7, 224),
    ("¹²N (nitrogen-12, A=12)","nitrogen-12", 7, 5, 224),
    ("¹⁴C (carbon-14, A=14)","carbon-14",   6, 8, 256),
    ("¹⁴O (oxygen-14, A=14)","oxygen-14",   8, 6, 256),
]


# ──────────────────────────────────────────────────────────────────────
# Symbolic primitives
# ──────────────────────────────────────────────────────────────────────


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
    """Return (τ_p, τ_n) parsed from the existing atomic witness."""
    data = json.loads(habiro_path.read_text())
    p_str = data["results"]["p (proton, A=1)"]["tr_M_in_q"]
    n_str = data["results"]["n (neutron, A=1)"]["tr_M_in_q"]
    tau_p = sp.sympify(p_str, locals={"q": q})
    tau_n = sp.sympify(n_str, locals={"q": q})
    return tau_p, tau_n


def _interface_product_symbolic(Z: int, N: int, q: sp.Symbol) -> sp.Expr:
    """Symbolic per-interface product matching `canonical_interface_kinds`
    under the production `chi_lambda_braid` convention."""
    z = _markov_z_q(q)
    h = _hecke_h_q(q)
    kinds = canonical_interface_kinds(Z, N, pn_convention="chi_lambda_braid")
    expr = sp.Integer(1)
    for kind in kinds:
        if kind == "positive":
            expr = expr * z
        elif kind == "negative":
            expr = expr * (z - h)
        elif kind == "averaged":
            expr = expr * (z - h / 2)
        else:
            raise ValueError(f"unknown interface kind {kind!r}")
    return expr


def _build_closed_form(Z: int, N: int, tau_p, tau_n, q):
    """tr_M(𝓑_K) = τ_p^Z · τ_n^N · Π interface_factor(kind, q)."""
    # For pure-proton or pure-neutron atoms (A=1), the closed-form
    # τ_p^Z · τ_n^N is exactly correct (no interfaces).  The atomic
    # witness encodes those τ values directly, so we reuse them.
    return tau_p ** Z * tau_n ** N * _interface_product_symbolic(Z, N, q)


# ──────────────────────────────────────────────────────────────────────
# Per-atom analysis
# ──────────────────────────────────────────────────────────────────────


def analyse_atom(label: str, Z: int, N: int, q,
                  tau_p, tau_n, q0_mp,
                  max_m: int = 64) -> dict:
    """Extract Habiro coefficients for (Z, N)."""
    t0 = time.perf_counter()
    print(f"\n── {label} (Z={Z}, N={N}, A={Z+N}) ──")
    kinds = canonical_interface_kinds(Z, N, pn_convention="chi_lambda_braid")
    print(f"  canonical_interface_kinds = {kinds}")

    tr_M_q = _build_closed_form(Z, N, tau_p, tau_n, q)
    tr_M_q = sp.together(tr_M_q)
    print(f"  → tr_M closed-form built (chars = {len(str(tr_M_q))})")
    print(f"    elapsed: {time.perf_counter() - t0:.2f} s")

    u = sp.Symbol('u', positive=True, real=True)
    p_u, shift, denom = to_u_polynomial(tr_M_q, q, u)
    deg_p = int(sp.Poly(p_u, u).degree()) if p_u != 0 else 0
    print(f"  → p(u) := u^{shift} · denom · tr_M(u²)")
    print(f"     deg p(u) = {deg_p}, denom = {denom}")
    print(f"    elapsed: {time.perf_counter() - t0:.2f} s")

    coeffs = cyclotomic_expansion(p_u, u, max_m=max_m)
    n_nonzero = sum(
        1 for c in coeffs
        if sp.sympify(c["a_m"], locals={"u": u, "check_q": u}) != 0
    )
    print(f"  Habiro coefficients: {len(coeffs)} terms ({n_nonzero} nonzero)")
    print(f"    elapsed: {time.perf_counter() - t0:.2f} s")

    recon = reconstruct(coeffs, u)
    diff = sp.expand(recon - p_u)
    recon_matches = (diff == 0)
    print(f"  reconstruction matches Σ a_m·(u;u)_m: {recon_matches}")

    # Numerical check at q₀ (50-dps mpmath).
    mp.mp.dps = 50
    q0 = q0_mp
    u0 = mp.sqrt(q0)
    try:
        tr_M_at_q0_mp = mp.mpf(str(sp.N(
            tr_M_q.subs(q, sp.Rational(str(q0))), 30
        )))
        tr_M_at_q0 = float(tr_M_at_q0_mp)
    except Exception:
        tr_M_at_q0_mp = mp.mpf('nan')
        tr_M_at_q0 = float('nan')
    check_error = None
    try:
        p_in_u_at_u0 = mp.mpf(str(sp.N(
            p_u.subs(u, sp.Rational(str(u0))), 30
        )))
        # BOTH names deliberately. `to_u_polynomial(expr, q, check_q)` renders
        # its returned strings using whatever SYMBOL the caller passes, and the
        # callers pass `u` — so current strings say "u". Older witnesses in this
        # family say "check_q", from a caller that passed a symbol of that name.
        # The previous mapping was {"check_q": u} ALONE, which meant a modern
        # "u"-string parsed to a fresh Symbol('u') with no assumptions; that is
        # NOT equal to Symbol('u', positive=True, real=True), so `.subs` silently
        # no-opped and the NaN below was published instead of a value.
        denom_expr = sp.sympify(denom, locals={"u": u, "check_q": u})
        denom_at_u0 = mp.mpf(str(sp.N(
            denom_expr.subs(u, sp.Rational(str(u0))), 30
        )))
        u0_shift = u0 ** shift if shift else mp.mpf(1)
        tr_M_via_u_mp = p_in_u_at_u0 / (u0_shift * denom_at_u0)
        tr_M_via_u = float(tr_M_via_u_mp)
        # Carry the residual as mpmath.mpf.  Computing it from the two float64
        # casts instead would floor the diagnostic at ~1e-16 and report the
        # arithmetic rather than the agreement (AGENTS.md, NO-FLOAT64).
        if tr_M_at_q0_mp != 0 and not mp.isnan(tr_M_at_q0_mp):
            rel_err_mp = (abs(tr_M_at_q0_mp - tr_M_via_u_mp)
                          / abs(tr_M_at_q0_mp))
        else:
            rel_err_mp = mp.mpf(0)
        rel_err = float(rel_err_mp)
    except Exception as exc:
        # Record WHY, and as null rather than NaN.
        #
        # This handler used to write float('nan') into both fields and print the
        # reason to stdout, where it was lost. Two consequences, both real: the
        # witness became invalid JSON (there is no NaN token in JSON, so a
        # strict parser rejected the whole file), and a silent failure looked
        # like a computed value.
        #
        # The failure it was hiding: `sp.sympify(denom, locals={"check_q": u})`
        # mapped the wrong NAME, so the parsed expression got a fresh
        # `Symbol('u')` with no assumptions, which is NOT equal to the
        # `Symbol('u', positive=True, real=True)` used here. `.subs(u, ...)`
        # then silently no-opped, `sp.N` returned an expression rather than a
        # number, and `mp.mpf(str(<expression>))` raised ValueError. Fixed at
        # the sympify sites; this handler stays for anything else, but now says
        # what happened.
        print(f"  numerical check FAILED: {exc}")
        tr_M_via_u = None
        rel_err = None
        rel_err_mp = None
        check_error = f"{type(exc).__name__}: {exc}"
    _fmt = lambda v, f: (f"{v:{f}}" if v is not None else "n/a")   # noqa: E731
    print(f"  tr_M @ q_0 = {_fmt(tr_M_at_q0, '+.6e')}, "
          f"via u-poly = {_fmt(tr_M_via_u, '+.6e')}, "
          f"rel diff = {_fmt(rel_err, '.3e')}")
    print(f"    elapsed: {time.perf_counter() - t0:.2f} s")

    return {
        "Z": Z, "N": N, "A": Z + N,
        "interface_kinds": list(kinds),
        "include_inter": True,
        "tr_M_in_q": str(tr_M_q),
        "shift": int(shift),
        "denom_in_u": denom,
        # `u` here IS the canonical symbol, so this is already normalised —
        # routed through str_in_u anyway so the invariant is stated at every
        # serialization site rather than held in someone's head (bean qou-0ndb).
        "p_in_u": str_in_u(p_u, u),
        "deg_p_u": deg_p,
        "habiro_coefficients": coeffs,
        "n_nonzero": n_nonzero,
        "all_integral": all(c["integral"] for c in coeffs),
        "reconstruction_matches": recon_matches,
        "tr_M_at_q0": tr_M_at_q0,
        "tr_M_at_q0_via_u_poly": tr_M_via_u,
        "tr_M_at_q0_check_error": check_error,
        "tr_M_at_q0_rel_err": rel_err,
        # The same residual before the float64 cast.  The summary reads THIS
        # one, so the mass-table summary carries no raw float64 at all.
        "tr_M_at_q0_rel_err_exact": (
            mp.nstr(rel_err_mp, 30) if rel_err_mp is not None else None),
    }


def _write_witness(path: Path, slug: str, body: dict, q0_float: float,
                   description: str, reference_blocks: list[str]) -> None:
    """Write per-atom witness via WitnessBuilder.wrap_legacy so the
    file carries `engine`, `scriptFile`, `commitSha`, `scriptHash`,
    `computedAt`, `durationMs` provenance required by
    `witness_provenance_audit.py`.
    """
    payload = {
        "computation": f"habiro-coefficients-{slug}",
        "description": description,
        "reference_blocks": reference_blocks,
        "parameters": {
            # The canonical 50-digit string, not the float64 cast: this witness
            # is the one place the whole table is summarised, so a float64 here
            # is a float64 in the table's own header.
            "q_0": _Q_CANONICAL_STR,
            "pn_convention": "chi_lambda_braid (legacy production marshalling)",
            "source": "habiro-coefficients-atomic.witness.json (τ_p, τ_n)",
            "generator": "_habiro_coefficient_extract.py",
        },
        "habiro_coefficients": body["habiro_coefficients"],
        "Z": body["Z"],
        "N": body["N"],
        "A": body["A"],
        "interface_kinds": body["interface_kinds"],
        "include_inter": body["include_inter"],
        "tr_M_in_q": body["tr_M_in_q"],
        "shift": body["shift"],
        "denom_in_u": body["denom_in_u"],
        "p_in_u": body["p_in_u"],
        "deg_p_u": body["deg_p_u"],
        "n_nonzero": body["n_nonzero"],
        "all_integral": body["all_integral"],
        "reconstruction_matches": body["reconstruction_matches"],
        "tr_M_at_q0": body["tr_M_at_q0"],
        "tr_M_at_q0_via_u_poly": body["tr_M_at_q0_via_u_poly"],
        "tr_M_at_q0_rel_err": body["tr_M_at_q0_rel_err"],
    }
    wb = WitnessBuilder.wrap_legacy(
        name=f"habiro-coefficients-{slug}",
        payload=payload,
        script_path=__file__,
        engine="sympy Poly + sequential cyclotomic division (via closed_form_tau_M closed form)",
        output_dir=path.parent,
    )
    wb.add_data("lean_uniqueness_ref", lean_uniqueness_ref(slug))
    wb.save()
    print(f"  → wrote {path.name}")


# ──────────────────────────────────────────────────────────────────────
# Mirror-pair audit
# ──────────────────────────────────────────────────────────────────────


def _coeff_to_sympy(a_m_str: str, u: sp.Symbol) -> sp.Expr:
    return sp.sympify(a_m_str, locals={"u": u, "check_q": u})


def _multiplicity(expr: sp.Expr, factor: sp.Expr, u: sp.Symbol) -> int:
    """Count how many times `factor` divides `expr` over ℤ[u]."""
    m = 0
    residue = expr
    while True:
        try:
            quo, rem = sp.div(sp.expand(residue), factor, u)
        except sp.PolynomialError:
            break
        if rem != 0:
            break
        residue = quo
        m += 1
    return m


def mirror_pair_diff(x: dict, y: dict, u: sp.Symbol) -> dict:
    """Δa_m(X − Y), reconstructed; factor + cyclotomic multiplicities.

    Returns dict with phi_1 / phi_2 / phi_4 / phi_8 multiplicities,
    plus the full factored form (truncated for storage)."""
    # Difference the TRACES over a common denominator, not the a_m.
    #
    # p_X(u) = u^{shift_X}·denom_X(u)·tr_X(u²) by construction, so
    # Σ Δa_m·(u;u)_m = p_X − p_Y = denom_X·tr_X − denom_Y·tr_Y, which is
    # proportional to (tr_X − tr_Y) ONLY when denom_X == denom_Y. Under
    # convention C the mirror partners happened to share a denominator and the
    # coefficient shortcut was silently valid. Under D they do not — all seven
    # canonical pairs differ — so the old form subtracted two differently
    # normalised objects and destroyed the cyclotomic structure, reporting
    # Φ_1 = Φ_2 = Φ_4 = Φ_8 = 0 on every pair. Φ_1 = 0 was the tell: at q = 1
    # the mirror halves coincide, so (u−1) MUST divide a true difference.
    #
    # Differencing the traces is correct in both conventions and is what the
    # Φ_k multiplicity is defined on (bean qou-0ndb).
    q_local = sp.Symbol('q', positive=True, real=True)

    def _num_den(entry):
        tr = sp.sympify(entry["tr_M_in_q"], locals={"q": q_local})
        tr_u = sp.powsimp(sp.expand(tr.subs(q_local, u ** 2)), force=True)
        return sp.fraction(sp.together(tr_u))

    nx, dx = _num_den(x)
    ny, dy = _num_den(y)
    diff_expr = sp.expand(sp.expand(nx * dy) - sp.expand(ny * dx))
    if diff_expr == 0:
        return {
            "diff_zero": True,
            "phi_1_mult": 0, "phi_2_mult": 0,
            "phi_4_mult": 0, "phi_8_mult": 0,
            "factored": "0", "len_factored": 1,
        }

    mult_phi_1 = _multiplicity(diff_expr, u - 1, u)
    mult_phi_2 = _multiplicity(diff_expr, u + 1, u)
    mult_phi_4 = _multiplicity(diff_expr, u ** 2 + 1, u)
    mult_phi_8 = _multiplicity(diff_expr, u ** 4 + 1, u)

    factored = sp.factor(diff_expr)
    factored_str = str(factored)
    factored_short = factored_str if len(factored_str) <= 800 \
        else factored_str[:800] + "..."

    return {
        "diff_zero": False,
        "phi_1_mult": mult_phi_1,
        "phi_2_mult": mult_phi_2,
        "phi_4_mult": mult_phi_4,
        "phi_8_mult": mult_phi_8,
        "factored": factored_short,
        "len_factored": len(factored_str),
    }


def find_mirror_pairs(atoms: list[tuple[str, str, int, int, int]]) -> \
        list[tuple[str, str, str, str, int, int]]:
    """Return list of (label_X, label_Y, slug_X, slug_Y, Z_X, N_X) with
    Z_X = N_Y, N_X = Z_Y, Z_X > N_X (avoids reflection duplicates).
    """
    by_zn = {(Z, N): (label, slug) for label, slug, Z, N, _ in atoms}
    pairs = []
    for (Zx, Nx), (label_x, slug_x) in by_zn.items():
        if Zx <= Nx:
            continue  # take Z_X > N_X representative only
        if (Nx, Zx) in by_zn:
            label_y, slug_y = by_zn[(Nx, Zx)]
            pairs.append((label_x, label_y, slug_x, slug_y, Zx, Nx))
    return pairs


# ──────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────


def main() -> int:
    t_overall = time.perf_counter()
    print("=" * 80)
    print("HABIRO COEFFICIENTS — MASS-TABLE-WIDE EXTRACT (Phase 5q closed-form)")
    print("=" * 80)

    q0_float = float(_Q_CANONICAL)
    # `mp.mpf(str(_Q_CANONICAL))` — the previous form — round-tripped q₀
    # through whatever `mp.dps` happened to be in force. At the default 15
    # that kept 15 digits, and analyse_atom then raised dps to 50 and did
    # `sp.Rational(str(q0))`, minting an exact rational from a value whose
    # last 34 digits were the binary64 expansion:
    #     1.1099785827513799496557567181298509240150451660156   (was)
    #     1.1099785827513808075916690956107688798744991218736   (is)
    # 7.7e-16 relative — small, but it anchored tr_M_at_q0 in all 20
    # per-atom witnesses. Source the digits from the canonical 50-digit
    # string instead, so the value cannot depend on ambient dps.
    q0_mp = mp.mpf(_Q_CANONICAL_STR)
    print(f"q_0 = {q0_float:.16f}")
    print(f"Plan: {len(ATOMS)} canonical atoms")

    habiro_path = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
    if not habiro_path.exists():
        print(f"  FATAL: {habiro_path} not found")
        return 2

    q = sp.Symbol('q', positive=True, real=True)
    u = sp.Symbol('u', positive=True, real=True)
    print("\nLoading symbolic τ_p, τ_n from atomic witness …")
    tau_p, tau_n = _load_p_n_symbolic(habiro_path, q)
    print(f"  τ_p chars = {len(str(tau_p))}")
    print(f"  τ_n chars = {len(str(tau_n))}")

    reference_blocks = [
        "def:habiro-ring",
        "prop:full-pole-structure-mass-trace",
        "prop:constit-factor-tau-M-proton-identity",
        "prop:interface-knot-markov-z",
        "thm:knot-mass-formula-unified",
    ]

    results: dict[tuple[int, int], dict] = {}
    failures: list[tuple[str, str]] = []
    for label, slug, Z, N, max_m in ATOMS:
        t_atom = time.perf_counter()
        try:
            r = analyse_atom(label, Z, N, q, tau_p, tau_n, q0_mp, max_m=max_m)
            results[(Z, N)] = r
            _write_witness(
                HERE / f"habiro-coefficients-{slug}.witness.json",
                slug, r, q0_float,
                description=(
                    f"Habiro / cyclotomic expansion tr_M(A={Z+N}, q) "
                    f"= Σ_m a_m·(u;u)_m (u = q^{{1/2}}) via the Phase 5q "
                    f"closed form. Mass-table-wide extraction "
                    f"(PR #1642 follow-up infrastructure); covers Z={Z}, "
                    f"N={N} under chi_lambda_braid (production) "
                    f"pn-convention. Feeds (i) mirror-pair Φ_k universality "
                    f"audit, (ii) Φ_8-multiplicity scaling-law table, and "
                    f"(iii) Q_β Habiro element keystone search."
                ),
                reference_blocks=reference_blocks,
            )
        except Exception as exc:
            print(f"  {label}: ERROR {type(exc).__name__}: {exc}")
            import traceback
            traceback.print_exc()
            failures.append((label, f"{type(exc).__name__}: {exc}"))
            results[(Z, N)] = {"error": str(exc)}
        print(f"  >>> {label}: total {time.perf_counter() - t_atom:.2f} s; "
              f"overall {time.perf_counter() - t_overall:.2f} s")

    # ─── Mirror-pair sweep ──────────────────────────────────────────
    print("\n" + "=" * 80)
    print("MIRROR-PAIR SWEEP — isospin (Z, N) ↔ (N, Z)")
    print("=" * 80)
    pairs = find_mirror_pairs(ATOMS)
    mirror_records: list[dict] = []
    for label_x, label_y, slug_x, slug_y, Zx, Nx in pairs:
        t_pair = time.perf_counter()
        rx = results.get((Zx, Nx))
        ry = results.get((Nx, Zx))
        if not rx or not ry or "error" in rx or "error" in ry:
            print(f"  {label_x} vs {label_y}: SKIPPED "
                  f"(missing/errored data)")
            continue
        try:
            diff_info = mirror_pair_diff(rx, ry, u)
        except Exception as exc:
            print(f"  {label_x} − {label_y}: ERROR {exc}")
            continue
        A = Zx + Nx
        record = {
            "pair": f"{slug_x}_minus_{slug_y}",
            "label_X": label_x, "label_Y": label_y,
            "Z_X": Zx, "N_X": Nx, "A": A,
            **diff_info,
        }
        mirror_records.append(record)
        print(f"  {label_x} − {label_y} (A={A}): "
              f"Φ_1={diff_info['phi_1_mult']}, "
              f"Φ_2={diff_info['phi_2_mult']}, "
              f"Φ_4={diff_info['phi_4_mult']}, "
              f"Φ_8={diff_info['phi_8_mult']}, "
              f"factored={diff_info['len_factored']} chars; "
              f"{time.perf_counter() - t_pair:.2f} s")

    # ─── Φ_8 multiplicity scaling-law table ─────────────────────────
    scaling_rows = []
    by_A: dict[int, list[dict]] = {}
    for rec in mirror_records:
        by_A.setdefault(rec["A"], []).append(rec)
    for A_val in sorted(by_A):
        for rec in by_A[A_val]:
            scaling_rows.append({
                "A": A_val,
                "pair": rec["pair"],
                "phi_1_mult": rec["phi_1_mult"],
                "phi_2_mult": rec["phi_2_mult"],
                "phi_4_mult": rec["phi_4_mult"],
                "phi_8_mult": rec["phi_8_mult"],
                "phi_1_phi_2": min(rec["phi_1_mult"], rec["phi_2_mult"]),
            })

    print("\nΦ_k MULTIPLICITY SCALING TABLE (mirror pairs):")
    print(f"  {'A':>3}  {'pair':>32}  Φ_1  Φ_2  Φ_4  Φ_8")
    for row in scaling_rows:
        print(f"  {row['A']:>3}  {row['pair']:>32}  "
              f"{row['phi_1_mult']:>3}  {row['phi_2_mult']:>3}  "
              f"{row['phi_4_mult']:>3}  {row['phi_8_mult']:>3}")

    # ─── Φ_1 / Φ_2 universality verdict ─────────────────────────────
    phi_1_universal = all(r["phi_1_mult"] >= 1 for r in mirror_records)
    phi_2_universal = all(r["phi_2_mult"] >= 1 for r in mirror_records)
    phi_8_universal = all(r["phi_8_mult"] >= 1 for r in mirror_records)
    print("\nUNIVERSALITY:")
    print(f"  Φ_1 (= u−1) divides every mirror difference: {phi_1_universal}")
    print(f"  Φ_2 (= u+1) divides every mirror difference: {phi_2_universal}")
    print(f"  Φ_8 (= u⁴+1) divides every mirror difference: {phi_8_universal}")

    # ─── Summary witness ────────────────────────────────────────────
    summary = {
        "computation": "habiro-coefficients-mass-table-summary",
        "description": (
            "Mass-table-wide Habiro coefficient extraction summary. "
            "Per-atom statistics (deg p(u), Habiro depth, integrality) "
            "plus mirror-pair cyclotomic multiplicity sweep (Φ_1, Φ_2, "
            "Φ_4, Φ_8). Generated by _habiro_coefficient_extract.py as "
            "the infrastructure parent of the per-atom "
            "habiro-coefficients-<atom>.witness.json files. "
            "Feeds PR #1642 follow-up: Q_β Habiro element keystone "
            "search, mirror-pair universal-prefactor falsifiability "
            "test, and Φ_8 multiplicity scaling-law tabulation."
        ),
        "reference_blocks": reference_blocks + [
            "PR #1579 (Habiro element factorization)",
            "PR #1642 (Q_β Wenzl-Habiro keystone)",
            "PR #1625 (Φ_8 mechanism — level-2 Wenzl annihilator)",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": _Q_CANONICAL_STR,
            "pn_convention": "chi_lambda_braid (legacy production marshalling)",
            "generator": "_habiro_coefficient_extract.py",
        },
        "atoms": [
            {
                "label": label, "slug": slug, "Z": Z, "N": N, "A": Z + N,
                "max_m": max_m,
                "extracted": (Z, N) in results
                              and "error" not in results[(Z, N)],
                "deg_p_u": (results[(Z, N)].get("deg_p_u")
                            if (Z, N) in results
                            and "error" not in results[(Z, N)] else None),
                "n_habiro_coeffs": (
                    len(results[(Z, N)].get("habiro_coefficients", []))
                    if (Z, N) in results
                    and "error" not in results[(Z, N)] else None),
                "n_nonzero": (results[(Z, N)].get("n_nonzero")
                              if (Z, N) in results
                              and "error" not in results[(Z, N)] else None),
                "all_integral": (results[(Z, N)].get("all_integral")
                                  if (Z, N) in results
                                  and "error" not in results[(Z, N)] else None),
                "reconstruction_matches": (
                    results[(Z, N)].get("reconstruction_matches")
                    if (Z, N) in results
                    and "error" not in results[(Z, N)] else None),
                "tr_M_at_q0_rel_err": (
                    results[(Z, N)].get("tr_M_at_q0_rel_err_exact")
                    if (Z, N) in results
                    and "error" not in results[(Z, N)] else None),
                "interface_kinds": (results[(Z, N)].get("interface_kinds")
                                     if (Z, N) in results
                                     and "error" not in results[(Z, N)] else None),
            }
            for label, slug, Z, N, max_m in ATOMS
        ],
        "mirror_pairs": mirror_records,
        "phi_k_scaling_table": scaling_rows,
        "verdicts": {
            "phi_1_universal_across_mirror_pairs": phi_1_universal,
            "phi_2_universal_across_mirror_pairs": phi_2_universal,
            "phi_8_universal_across_mirror_pairs": phi_8_universal,
            "n_atoms_extracted": sum(
                1 for r in results.values() if "error" not in r),
            "n_mirror_pairs_tested": len(mirror_records),
            "failures": [
                {"label": lbl, "error": err}
                for (lbl, err) in failures
            ],
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        name="habiro-coefficients-mass-table-summary",
        payload=summary,
        script_path=__file__,
        engine="sympy Poly + sequential cyclotomic division",
        output_dir=HERE,
    )
    summary_path = wb.save()
    print(f"\n  → wrote {summary_path.name}")

    total = time.perf_counter() - t_overall
    print(f"\nTOTAL ELAPSED: {total:.1f} s")
    print(f"FAILURES: {len(failures)}")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
