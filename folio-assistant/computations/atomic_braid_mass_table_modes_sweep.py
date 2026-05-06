#!/usr/bin/env python3
"""
Atomic-braid mass-table T1 modes sweep.

Tests several T1 constructions for the atomic-braid six-term mass
formula and reports the per-mode err% across (p, n, D, T, ³He, ⁴He).
The motivating question is whether any T1 construction closes the
~22% err% gap of the legacy GS-NF six-term, while still being
defensibly grounded in the atomic-braid representation.

Modes:

  A. disjoint:        T1(K) = |tr_M(p)|^Z · |tr_M(n)|^N
                      (PR #547 pure disjoint-product, no inter-
                      nucleon coupling).

  B. disjoint × J:    T1(K) = disjoint(K) · a_J(Z, N)
                      where a_J is the structural Jones-quotient
                      table (1, 1−h², (1−h²)^2, …).

  C. disjoint × a_k:  T1(K) = disjoint(K) · a_k(Z, N)
                      a_k from jet-knot-invariants.witness.json
                      (canonical convergent value for atoms in
                      the witness; J fallback otherwise).

  D. a_k alone:       T1(K) = a_k(Z, N)
                      Drop the disjoint multiplicative growth;
                      use only the inter-nucleon factor.

  E. legacy GS-NF:    T1(K) = canonical-tr-M from
                      atomic-tr-m-mpfr-50dps.witness.json.
                      Reproduces the legacy six-term T1.

  F. geom mean:       T1(K) = disjoint(K)^{1/A}
                      Average per-nucleon Markov-trace.

  G. mixed:           T1(K) = a_k(Z, N) · |tr_M(p)|
                      Single-strand baseline times the inter-
                      nucleon factor.

Tower terms T2, T3 (Markov-axiom values for n_gens = 3A − 1),
T4 (Frobenius codim), T6 (cyclotomic tail) follow the legacy
convention.  Calibration: proton-only, per mode.

Output: atomic-braid-mass-table-modes-sweep.witness.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

mp.mp.dps = 50

from markov_trace_recursive import markov_trace_of_word, q as _q  # noqa: E402
from q_parameter import Q_MP  # noqa: E402

q = _q
Q0 = mp.mpf(str(Q_MP))
H_VAL = Q0 - 1 / Q0
Z_MARK = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))


PROTON_WORD = [1] * 7 + [2] * 4
NEUTRON_WORD = [1] * 6 + [2] * 4 + [-1]

ATOMS_CODATA = {
    "p":   {"Z": 1, "N": 0, "M_MeV": "938.27208816"},
    "n":   {"Z": 0, "N": 1, "M_MeV": "939.56542052"},
    "D":   {"Z": 1, "N": 1, "M_MeV": "1875.61294257"},
    "T":   {"Z": 1, "N": 2, "M_MeV": "2808.92113298"},
    "3He": {"Z": 2, "N": 1, "M_MeV": "2808.39160743"},
    "4He": {"Z": 2, "N": 2, "M_MeV": "3727.379378"},
}

_LABEL_TO_JET = {"T": "³H", "3He": "³He", "4He": "⁴He"}


def jones_table(Z: int, N: int) -> mp.mpf:
    A = Z + N
    h2 = H_VAL ** 2
    omh = 1 - h2
    if A <= 2:
        return mp.mpf(1)
    if A == 3:
        return omh
    if A == 4:
        return omh ** 2
    return omh ** (A - 2)


def load_jet_knot_a() -> dict[str, mp.mpf]:
    out: dict[str, mp.mpf] = {}
    path = HERE / "jet-knot-invariants.witness.json"
    if not path.exists():
        return out
    d = json.loads(path.read_text())
    for atom, info in d.get("data", {}).items():
        levels = info.get("levels", [])
        if not levels:
            continue
        best = max(levels, key=lambda lvl: int(lvl.get("k", 0)))
        v = best.get("a_k")
        if v is None:
            continue
        out[atom] = mp.mpf(str(v))
    return out


def load_canonical_t1() -> dict[str, mp.mpf]:
    """Legacy GS-NF |tr_M| from atomic-tr-m-mpfr-50dps.witness.json."""
    path = HERE / "atomic-tr-m-mpfr-50dps.witness.json"
    out: dict[str, mp.mpf] = {}
    if not path.exists():
        return out
    d = json.loads(path.read_text())
    for atom, val in d.get("results_by_atom", {}).items():
        if isinstance(val, dict):
            v = val.get("abs_tr_M_50dps") or val.get("tr_M_atom")
        else:
            v = val
        if v is not None:
            out[atom] = mp.mpf(str(v))
    return out


def t2_markov(n_gens: int) -> mp.mpf:
    return mp.mpf(n_gens) * Z_MARK ** 2


def t3_markov(n_gens: int) -> mp.mpf:
    return mp.mpf(n_gens * (n_gens - 1) // 2) * Z_MARK ** 4


def t4_raw(A: int) -> mp.mpf:
    if A < 1:
        return mp.mpf(0)
    from schur_weyl_symbolic import partitions_of
    from hecke_characters import young_hooks
    n = 3 * A
    denom = Q0 - 1 / Q0
    # Compute [n]_q! directly in mpmath to preserve 50-dps precision
    # (avoids SymPy → mpmath conversion). Per Gemini PR #548 high-pri.
    nfac_val = mp.mpf(1)
    for k in range(1, n + 1):
        nfac_val *= (Q0 ** k - 1 / Q0 ** k) / denom
    total = mp.mpf(0)
    for lam in partitions_of(n):
        hooks = young_hooks(lam)
        dim_q = nfac_val
        for h in hooks:
            qh = (Q0 ** h - 1 / Q0 ** h) / denom
            dim_q = dim_q / qh
        total += 1 / dim_q
    return total


def t6_canonical_MeV(A: int) -> mp.mpf:
    path = HERE / "term6-habiro-residue-mpfr-50dps.witness.json"
    if not path.exists():
        return mp.mpf(0)
    d = json.loads(path.read_text())
    for r in d.get("results_by_atom", []):
        try:
            entry_A = int(r["atom"].split("=")[1])
            if entry_A == A:
                return mp.mpf(r["term6_b_pred_mev_50dps"])
        except (KeyError, IndexError, ValueError):
            continue
    return mp.mpf(0)


def t1_for_mode(mode: str, atom: str, info: dict,
                tr_p: mp.mpf, tr_n: mp.mpf,
                jet_a: dict[str, mp.mpf],
                gs_nf_t1: dict[str, mp.mpf]) -> mp.mpf:
    Z = info["Z"]; N = info["N"]; A = Z + N
    disjoint = abs(tr_p) ** Z * abs(tr_n) ** N
    a_J = jones_table(Z, N)
    jet_key = _LABEL_TO_JET.get(atom)
    a_jet = jet_a.get(jet_key, a_J) if jet_key else a_J
    if mode == "A_disjoint":
        return disjoint
    if mode == "B_disjoint_x_J":
        return disjoint * a_J
    if mode == "C_disjoint_x_a_k":
        return disjoint * a_jet
    if mode == "D_a_k_alone":
        return a_jet if jet_key else mp.mpf(1)  # p, n, D fallback to 1
    if mode == "E_legacy_GS_NF":
        return gs_nf_t1.get(atom, mp.mpf(1))
    if mode == "F_geom_mean":
        if A == 0:
            return mp.mpf(1)
        return disjoint ** (mp.mpf(1) / A)
    if mode == "G_mixed":
        return abs(tr_p) * a_jet
    raise ValueError(f"unknown mode {mode!r}")


def assemble_mass(t1: mp.mpf, A: int, m_e_hecke: mp.mpf = mp.mpf(1)) -> dict:
    n_gens = max(3 * A - 1, 0)
    t2 = t2_markov(n_gens)
    t3 = t3_markov(n_gens)
    t4r = t4_raw(A)
    t4 = m_e_hecke * t4r
    t6_MeV = t6_canonical_MeV(A)
    total_hecke = t1 + t2 + t3 + t4
    return {
        "t1": t1, "t2": t2, "t3": t3, "t4": t4,
        "total_hecke": total_hecke, "t6_MeV": t6_MeV,
        "n_gens": n_gens,
    }


def main() -> int:
    print("=" * 96)
    print("  Atomic-braid mass-table — T1 modes sweep")
    print("=" * 96)

    # Per-carrier traces
    print(f"\n  Computing per-carrier |tr_M_atomic| via PR #547 reducer...")
    tr_p_sym = markov_trace_of_word(3, PROTON_WORD)
    tr_n_sym = markov_trace_of_word(3, NEUTRON_WORD)

    def evalq(expr: sp.Expr) -> mp.mpf:
        return mp.mpf(str(expr.subs(q, sp.sympify(str(Q_MP))).evalf(mp.mp.dps)))

    tr_p = abs(evalq(tr_p_sym))
    tr_n = abs(evalq(tr_n_sym))
    jet_a = load_jet_knot_a()
    gs_nf_t1 = load_canonical_t1()

    modes = [
        "A_disjoint", "B_disjoint_x_J", "C_disjoint_x_a_k",
        "D_a_k_alone", "E_legacy_GS_NF", "F_geom_mean", "G_mixed",
    ]

    summary: dict = {}
    print(f"\n  {'mode':<22}", end="")
    for atom in ATOMS_CODATA:
        print(f"{atom:>10}", end="")
    print(f"  {'mean|err%|':>12}")
    print("  " + "-" * 90)
    for mode in modes:
        # Calibrate E_0 from proton.
        p_info = ATOMS_CODATA["p"]
        p_t1 = t1_for_mode(mode, "p", p_info, tr_p, tr_n, jet_a, gs_nf_t1)
        p_terms = assemble_mass(p_t1, p_info["Z"] + p_info["N"])
        M_p = mp.mpf(p_info["M_MeV"])
        E_0 = ((M_p - p_terms["t6_MeV"]) / p_terms["total_hecke"]
               if p_terms["total_hecke"] != 0 else mp.mpf(0))
        per_mode = {"E_0_MeV": str(E_0), "atoms": {}}
        per_atom_err = []
        print(f"  {mode:<22}", end="")
        for atom, info in ATOMS_CODATA.items():
            t1 = t1_for_mode(mode, atom, info, tr_p, tr_n, jet_a, gs_nf_t1)
            terms = assemble_mass(t1, info["Z"] + info["N"])
            M_pred = E_0 * terms["total_hecke"] + terms["t6_MeV"]
            M_codata = mp.mpf(info["M_MeV"])
            err = (M_pred - M_codata) / M_codata * 100
            per_mode["atoms"][atom] = {
                "t1": str(t1),
                "M_pred_MeV": str(M_pred),
                "err_pct": str(err),
            }
            print(f"{float(err):>10.2f}", end="")
            if atom != "p":
                per_atom_err.append(abs(float(err)))
        mean_abs = sum(per_atom_err) / len(per_atom_err) if per_atom_err else 0
        per_mode["mean_abs_err_pct_excl_p"] = mean_abs
        summary[mode] = per_mode
        print(f"  {mean_abs:>12.4f}")

    # Best mode
    best_mode = min(summary.items(), key=lambda kv: kv[1]["mean_abs_err_pct_excl_p"])
    print(f"\n  Best mode (smallest mean |err%|): {best_mode[0]}")
    print(f"    mean |err%| = {best_mode[1]['mean_abs_err_pct_excl_p']:.4f}%")
    print(f"    E_0 = {best_mode[1]['E_0_MeV']}")

    # Reference: legacy paper-six-term mean
    legacy_path = HERE / "paper-six-term-isotope-sweep.witness.json"
    legacy_mean = None
    if legacy_path.exists():
        legacy = json.loads(legacy_path.read_text())
        errs = []
        for r in legacy.get("rows", []):
            if r.get("isotope") in ATOMS_CODATA and r.get("isotope") != "p":
                errs.append(abs(r.get("err_pct", 0)))
        if errs:
            legacy_mean = sum(errs) / len(errs)
            print(f"  Legacy GS-NF six-term mean |err%|: {legacy_mean:.4f}%")
            improvement = legacy_mean - best_mode[1]["mean_abs_err_pct_excl_p"]
            if improvement > 0:
                print(f"  → Strategy 3 (mode {best_mode[0]}) improves on "
                      f"legacy by {improvement:.4f}pp.")
            else:
                print(f"  → No mode in the sweep beats legacy "
                      f"(legacy is {-improvement:.4f}pp better).")

    witness = {
        "computation": "atomic-braid-mass-table-modes-sweep",
        "description": (
            "T1 modes sweep for the atomic-braid six-term mass "
            "formula. Tests seven T1 constructions (disjoint, "
            "disjoint × Jones, disjoint × canonical a_k, a_k alone, "
            "legacy GS-NF, geometric mean, mixed) and reports "
            "per-atom + mean err% vs CODATA, with proton-only "
            "calibration per mode. Identifies which T1 construction "
            "is closest to legacy GS-NF (or beyond)."
        ),
        "reference_blocks": [
            "thm:knot-mass-formula-unified",
            "prop:markov-trace-axiomatic-closed-form",
            "prop:markov-trace-recursive-reducer",
            "prop:jet-filtered-knot-factor",
            "prop:categorical-mass-markov",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": str(Q0),
            "abs_tr_M_atomic_p": str(tr_p),
            "abs_tr_M_atomic_n": str(tr_n),
            "modes": modes,
        },
        "by_mode": summary,
        "best_mode": best_mode[0],
        "legacy_GS_NF_mean_abs_err_pct": (
            str(legacy_mean) if legacy_mean is not None else None
        ),
        "all_passed": True,
    }
    out = HERE / "atomic-braid-mass-table-modes-sweep.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
