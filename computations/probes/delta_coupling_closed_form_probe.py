#!/usr/bin/env python3


# polynomial_q_not_applicable: probe of closed-form candidates at q_0
"""P3.A — Closed-form `f` candidate probe for Δ_coupling at magic shells.

Per docs/audits/2026-05-11-1ppb-gap-narrowing-plan.md §Path A and
content/quantum-observable-universe/braids-and-knots/conj-magic-shell-stabilization.md:160,
the cross-coupling residual at the doubly-magic ⁴He shell is

    Δ_coupling(2, 2) = Δ_cat(⁴He) − 2 · Δ_cat(³He) ≈ +13.20 MeV

where, for each atom 𝔥 ∈ {p, n, D, T, ³He, ⁴He}, the canonical
**substrate-derived** per-atom residual is

    Δ_cat(𝔥) := AME(𝔥) − m_e · ρ_𝔥 · |τ(β_𝔥)|

(`probe_magic_shell_empirical_instantiation.py:8`).  All six per-atom
Δ_cat values are computed once and emitted to
`magic-shell-empirical-instantiation.witness.json`; this probe LOADS
them from that witness rather than recomputing or hardcoding raw AME
values.

The cross-coupling residuals consumed below are the canonical
Δ_cat differences (NOT raw binding-energy differences):

    Δ_coupling(2, 2) := Δ_cat(⁴He) − 2 · Δ_cat(³He)         [doubly-magic]
    Δ_coupling(2, 1) := Δ_cat(³He) − Δ_cat(D) − Δ_cat(p)    [³He = D + p]
    Δ_coupling(1, 2) := Δ_cat(T)   − Δ_cat(D) − Δ_cat(n)    [T   = D + n]

The 2-decomposition for ⁴He counts the ³He sub-clusters
(combinatorial: (4 choose 3) = 4 sub-clusters / 2 per pair = 2);
the (D, free-nucleon) decompositions for ³He and T follow the
atomic-braid-recipe topology (`recursive-atom-knot-atlas.md`).
There is no "modeling choice" — the decomposition is determined
by the substrate braid topology, and the residuals are per-atom
Δ_cat differences derived from the same Markov-trace formula.

P3.A asks: which structural closed form `f` reproduces these
Δ_coupling values when evaluated at the appropriate substrate
parameter `t`?  The gap-narrowing plan (P1.1) lists four candidates:

  C1  f₁(t) = log(1/t)
  C2  f₂(t) = 1/t − 1
  C3  f₃(t) = log Φ_q^{(∞)}(t)        (log of full Faddeev dilogarithm)
  C4  f₄(t) = KLR canonical-basis dim count at the relevant shell

evaluated at three natural substrate values of `t`:
  - t = q_0 ≈ 1.110            (full substrate parameter)
  - t = q_0 − 1 = 1/q_0·E_0    (β-decay-energy normalisation)
  - t = h(q_0) = q_0 − q_0⁻¹   (Hecke deformation parameter)

The probe reports the multiplicative factor `Δ_coupling / (E_0 · f(t))`
needed to match the anchor.  A candidate is "structurally promising"
if that factor is a small rational (or matches a known categorical
invariant such as Z + N − 2) on multiple anchors; cross-anchor
consistency is reported separately.

This is a DIAGNOSTIC PROBE, NOT a fit.  Per AGENTS.md three-cal
discipline, calibrating Δ_coupling to AME is forbidden — this script
identifies which closed form the structural derivation should target,
not which one to tune.

Output: delta-coupling-closed-form-probe.witness.json
Reference blocks:
  - conj:magic-shell-stabilization
  - prop:beta-decay-energy-scale
  - thm:knot-mass-formula-unified
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import mpmath as mp

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from derived_masses import e_0_full_mev  # noqa: E402

# ── Canonical Δ_cat anchors (loaded from witness; computed once) ────
#
# The per-atom Δ_cat values are produced by
# `probe_magic_shell_empirical_instantiation.py` and persisted to
# `magic-shell-empirical-instantiation.witness.json` (~83 s of
# symbolic Hecke compute for all six atoms).  This script consumes
# the witness rather than recomputing.  If the witness is missing
# (e.g. fresh checkout), run the upstream probe first.

_MSEI_PATH = _pb.witness_path("magic-shell-empirical-instantiation.witness.json", HERE)


def _load_delta_cat() -> dict[str, mp.mpf]:
    """Return atom-name → Δ_cat (MeV, 50dps mpmath) from the canonical
    `magic-shell-empirical-instantiation` witness.  Atom names follow
    the upstream probe convention: {proton, neutron, deuteron, tritium,
    he3, he4}."""
    if not _MSEI_PATH.exists():
        raise FileNotFoundError(
            f"canonical Δ_cat witness missing: {_MSEI_PATH.name}.  "
            f"Run probe_magic_shell_empirical_instantiation.py first."
        )
    msei = json.loads(_MSEI_PATH.read_text())
    per_atom = msei["data"]["per_atom_delta_cat"]
    out: dict[str, mp.mpf] = {}
    for atom, row in per_atom.items():
        if "delta_cat_MeV_50dps" not in row:
            raise KeyError(
                f"Δ_cat witness atom {atom!r} has no delta_cat_MeV_50dps "
                f"(error: {row.get('error', '?')})"
            )
        out[atom] = mp.mpf(row["delta_cat_MeV_50dps"])
    return out


def _build_anchors(dc: dict[str, mp.mpf]) -> list[tuple[str, mp.mpf, str]]:
    """Construct the canonical cross-coupling residuals as Δ_cat
    differences.  Returns a list of (label, value_MeV, formula_str).

    The decompositions are determined by the atomic-braid-recipe
    topology (`recursive-atom-knot-atlas.md`):
      ⁴He: 4 strands of 3-baryon NF → 2 ³He sub-clusters per pair
      ³He = D + p (³He braid factors as deuteron-braid + proton-braid)
      T   = D + n (T   braid factors as deuteron-braid + neutron-braid)

    Δ_coupling is the residual after subtracting the per-sub-cluster
    Δ_cat contributions.  All terms are per-atom Δ_cat values from
    the same Markov-trace formula — no raw AME bindings, no
    "modeling choice".
    """
    return [
        (
            "(2,2)_doubly_magic",
            dc["he4"] - 2 * dc["he3"],
            "Δ_cat(⁴He) − 2·Δ_cat(³He)",
        ),
        (
            "(2,1)_3He_eq_D_plus_p",
            dc["he3"] - dc["deuteron"] - dc["proton"],
            "Δ_cat(³He) − Δ_cat(D) − Δ_cat(p)",
        ),
        (
            "(1,2)_T_eq_D_plus_n",
            dc["tritium"] - dc["deuteron"] - dc["neutron"],
            "Δ_cat(T) − Δ_cat(D) − Δ_cat(n)",
        ),
    ]


def f1_log_inv(t):
    """C1:  f₁(t) = log(1/t).  Vanishes at t=1 (q→1 base point)."""
    return -mp.log(t)


def f2_inv_minus_1(t):
    """C2:  f₂(t) = 1/t − 1.  Linear-leading at t→1."""
    return 1 / t - 1


def f3_log_phi_q_full(t):
    """C3:  f₃(t) = log Φ_q^{(∞)}(t)  where Φ_q is the full Faddeev
    quantum dilogarithm (infinite product form).  Numerically:

        Φ_q^{(∞)}(t) = Σ_{n≥0} t^n / (q;q)_n

    Truncated at n_max = 60 (sufficient at q_0 ≈ 1.11; per-term ratio
    ≈ t·q^n / (1−q^{n+1}) decays fast enough by n=60).
    """
    q = Q0
    total = mp.mpf(0)
    qq_n = mp.mpf(1)  # (q;q)_0 = 1
    t_n = mp.mpf(1)   # t^0 = 1
    for n in range(60):
        if n > 0:
            qq_n = qq_n * (1 - q ** n)  # extend (q;q)_{n-1} → (q;q)_n
            t_n = t_n * t
        if abs(qq_n) < mp.mpf("1e-50"):
            break
        total += t_n / qq_n
    if total <= 0:
        return mp.nan
    return mp.log(total)


def f4_klr_dim(_t):
    """C4:  f₄ = KLR canonical-basis dimension count at the doubly-magic
    (2,2) shell.  For S_4 (4 strands) under the KLR algebra the canonical
    basis has |dim| = number of standard Young tableaux of size 4 = 14
    (sum of f^λ for λ ⊢ 4: 1 + 3 + 2 + 3 + 1 = wait — actually 1+3+2+3+1 is
    for f^λ of partitions [4],[3,1],[2,2],[2,1,1],[1^4] = 1, 3, 2, 3, 1 → 10).

    For the (2,2) shell the relevant block is the one with content vector
    (1, 1, −1, −1) for S_4, dim = 2 (the [2,2] partition).

    This candidate is t-independent — included as a "what if Δ_coupling
    is purely combinatorial" sanity check.
    """
    return mp.mpf(2)  # dim of S_4 partition [2,2]


CANDIDATES = [
    ("C1_log_inv_t",       f1_log_inv,         "log(1/t)"),
    ("C2_inv_t_minus_1",   f2_inv_minus_1,     "1/t - 1"),
    ("C3_log_phi_q_full",  f3_log_phi_q_full,  "log Φ_q^{(∞)}(t)"),
    ("C4_klr_dim",         f4_klr_dim,         "KLR canonical-basis dim count"),
]


def t_values():
    """Three natural substrate values to evaluate `t` at."""
    h = Q0 - 1 / Q0
    return [
        ("q_0",        Q0),
        ("q_0_minus_1", Q0 - 1),
        ("h(q_0)",     h),
    ]


def main() -> int:
    print("=" * 78)
    print("P3.A — closed-form f candidate probe for Δ_coupling (multi-anchor)")
    print("=" * 78)
    print(f"  q_0          = {mp.nstr(Q0, 12)}")
    print(f"  E_0 (full)   = {mp.nstr(e_0_full_mev(), 12)} MeV")
    print()
    print(f"  Loading canonical Δ_cat values from "
          f"{_MSEI_PATH.name} ...")
    delta_cat = _load_delta_cat()
    print("  Per-atom Δ_cat (substrate-derived, AME − m_e·ρ·|τ|):")
    for atom in ("proton", "neutron", "deuteron", "tritium", "he3", "he4"):
        if atom in delta_cat:
            print(f"    Δ_cat({atom:<9}) = {mp.nstr(delta_cat[atom], 8):>14} MeV")
    print()
    anchors = _build_anchors(delta_cat)
    print(f"  Canonical Δ_coupling cross-coupling residuals:")
    for a_name, a_val, formula in anchors:
        print(f"    Δ_coupling{a_name:<22} = {mp.nstr(a_val, 8):>12} MeV "
              f"  ({formula})")
    print()

    E_0 = e_0_full_mev()
    rows = []

    for anchor_name, anchor_val, formula in anchors:
        print(f"-- anchor {anchor_name} = {mp.nstr(anchor_val, 6)} MeV "
              + "-" * 25)
        for cand_name, fn, label_human in CANDIDATES:
            for t_name, t_val in t_values():
                try:
                    fval = fn(t_val)
                    if mp.isnan(fval) or mp.isinf(fval):
                        raise ValueError("non-finite")
                    # Direct prediction in MeV: E_0 · f(t)
                    pred_MeV = E_0 * fval
                    # Multiplicative factor needed to match anchor:
                    if pred_MeV == 0:
                        factor = mp.nan
                    else:
                        factor = anchor_val / pred_MeV
                    # Also: pure-combinatorial form (no E_0 prefactor)
                    if fval == 0:
                        factor_no_E0 = mp.nan
                    else:
                        factor_no_E0 = anchor_val / fval
                    row = {
                        "anchor": anchor_name,
                        "anchor_formula": formula,
                        "anchor_MeV": float(anchor_val),
                        "candidate": cand_name,
                        "candidate_human": label_human,
                        "t_name": t_name,
                        "t_value": float(t_val),
                        "f_at_t": float(fval),
                        "E0_times_f_MeV": float(pred_MeV),
                        "factor_to_match_Delta": float(factor),
                        "factor_no_E0_prefactor": float(factor_no_E0),
                    }
                    rows.append(row)
                    print(f"  {cand_name:<22} @ t={t_name:<12} "
                          f"f={float(fval):+.4e}  "
                          f"E0·f={float(pred_MeV):+9.4f} MeV  "
                          f"need×{float(factor):+8.4f}")
                except Exception as exc:  # noqa: BLE001
                    row = {
                        "anchor": anchor_name,
                        "anchor_formula": formula,
                        "anchor_MeV": float(anchor_val),
                        "candidate": cand_name,
                        "candidate_human": label_human,
                        "t_name": t_name,
                        "t_value": float(t_val),
                        "error": f"{type(exc).__name__}: {exc}",
                    }
                    rows.append(row)
                    print(f"  {cand_name:<22} @ t={t_name:<12} ERROR: {exc}")
        print()

    # Identify candidates whose multiplicative factor is closest to
    # a small integer or simple fraction — the structurally-promising
    # ones.  A candidate that produces *consistent* small-rational
    # factors across multiple anchors is a much stronger lead than one
    # that hits a small rational on a single anchor.
    print()
    print("Candidates with |factor| close to 1, 2, 3, 4, 1/2, 1/3, 1/4:")
    SIMPLE = [mp.mpf(k) for k in (1, 2, 3, 4)] + \
             [mp.mpf(1) / k for k in (2, 3, 4)]
    promising = []
    for r in rows:
        f = r.get("factor_to_match_Delta")
        if f is None or not mp.isfinite(mp.mpf(f)):
            continue
        for s in SIMPLE:
            gap = abs(mp.mpf(f) - s) / s
            if gap < mp.mpf("0.05"):  # within 5%
                promising.append((r, float(s), float(gap)))
                print(f"  ✓ {r['anchor']:<22} {r['candidate']} @ {r['t_name']}: "
                      f"factor ≈ {f:+.4f}, near {float(s):.4f} "
                      f"(gap {float(gap)*100:.2f}%)")

    # Cross-anchor consistency: which (candidate, t) pairs land near a
    # small rational on >= 2 anchors?  Those are the structurally-
    # informative leads.
    print()
    print("Cross-anchor consistency (small-rational matches on ≥2 anchors):")
    by_pair: dict[tuple[str, str], list[tuple[str, float, float]]] = {}
    for (r, near, gap) in promising:
        key = (r["candidate"], r["t_name"])
        by_pair.setdefault(key, []).append((r["anchor"], near, gap))
    cross_consistent = []
    for (cand, tn), hits in sorted(by_pair.items()):
        if len(hits) >= 2:
            anchors_hit = ", ".join(h[0] for h in hits)
            print(f"  ★ {cand} @ {tn}: matches on {len(hits)} anchors "
                  f"({anchors_hit})")
            cross_consistent.append({
                "candidate": cand,
                "t_name": tn,
                "anchors_matched": [h[0] for h in hits],
                "near_values": [h[1] for h in hits],
                "fractional_gaps": [h[2] for h in hits],
            })
    if not cross_consistent:
        print("  (none — single-anchor matches only)")

    builder = WitnessBuilder("delta-coupling-closed-form-probe", engine="mpmath")
    builder.set_description(
        "P3.A diagnostic probe: which closed form `f` reproduces the "
        "canonical magic-shell cross-coupling residuals Δ_coupling(Z,N) "
        "when evaluated at a natural substrate value t (q_0, q_0−1, or "
        "h(q_0))? Anchors are loaded from the canonical "
        "`magic-shell-empirical-instantiation.witness.json` (computed "
        "once); each is a Δ_cat difference where Δ_cat(𝔥) := AME(𝔥) − "
        "m_e·ρ·|τ(β_𝔥)| is the substrate-derived per-atom residual. "
        "Decompositions (⁴He → 2 ³He sub-clusters, ³He → D+p, T → D+n) "
        "follow the atomic-braid-recipe topology — combinatorial, not "
        "a modeling choice. Tests four candidates from the gap-narrowing "
        "plan: log(1/t), 1/t−1, log Φ_q^{(∞)}(t), KLR canonical-basis "
        "dim. Candidates whose multiplicative match-factor is a small "
        "rational on ≥2 anchors identify structural targets for the "
        "derivation; no fitting performed."
    )
    builder.set_content_block("conj:magic-shell-stabilization")
    builder.add_parameter("q_0", str(Q0))
    builder.add_parameter("E_0_full_MeV", str(e_0_full_mev()))
    builder.add_parameter("anchors_MeV",
                          {n: str(v) for (n, v, _f) in anchors})
    builder.add_parameter("anchor_formulas",
                          {n: f for (n, _v, f) in anchors})
    builder.add_parameter("delta_cat_per_atom_MeV",
                          {a: str(v) for (a, v) in delta_cat.items()})
    builder.add_parameter("upstream_witness",
                          "magic-shell-empirical-instantiation.witness.json")
    builder.add_data("rows", rows)
    builder.add_data("promising_matches", [
        {"row": r, "near_value": near, "fractional_gap": gap}
        for (r, near, gap) in promising
    ])
    builder.add_data("cross_anchor_consistent_leads", cross_consistent)
    out = builder.save()
    print(f"\n  → wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
