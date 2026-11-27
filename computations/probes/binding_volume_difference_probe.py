#!/usr/bin/env python3
"""
binding_volume_difference_probe.py — does a DERIVED hyperbolic-volume
difference B = ρ·[Vol(atom) − Vol(free)] close A≥3 binding?
(Derive-or-refute; no AME fit, no hand-assigned census knots.)

MOTIVATION. Per kashaev-as-archimedean-realization.md, the Archimedean
mass of a knot is Vol(K) = 2π·lim_{N→∞} log|J_N(K)|/N, i.e. the trace is
the EXPONENTIAL of a volume: tr ~ exp(Vol). The binding endomorphism
B = m_e·Vol(𝓑₃)·Δtr uses the LINEAR trace difference Δtr = |tr_free| −
|tr_atom|, which is the linearisation exp(Vol) ≈ 1+Vol — exact only for
small Vol (the deuteron, +0.19%). For A≥3 the trace saturates while the
true volume keeps growing. So the "un-truncated", extensive object should
be a VOLUME difference. This probe tests three candidate volumes, each
built from DERIVED objects only (no census-knot assignment, which is a
per-isotope fit — see mass-volume-factorization caveat + PR #1421):

  A. log Markov trace at q₀ : Vol_q := log|tr_M|  (algebraic quantum
     volume at the REAL substrate, before the N→∞ archimedean limit).
  B. cosh-inversion         : tr = 2cosh(ℓ/2) ⇒ ℓ = 2·arccosh(|tr|/2)
     (the hyperbolic translation length, keeping the cosh structure).
  C. SnapPy hyperbolic Vol  : geodesic volume of the actual derived
     braid CLOSURE (atom_braid_word_3A), free vs interface-inclusive.

RESULT (honest triple refutation):
  A. log: no single DERIVED ρ closes it — ρ∈{m_e, E₀, m_e·8G} give
     −55…−90% (the κ_needed spans 313%; see binding_log_scale_investigation).
  B. cosh-inversion: DEGENERATE — every |tr_M| < 2 (elliptic regime,
     tr = 2cos(θ/2)), so there is no real translation length / volume.
  C. SnapPy: EVALUATED FOR THE FIRST TIME 2026-09-07 (bean qou-m6gp).
     Until then `_snappy_braid_vols` returned (None, None, False) on
     ImportError and SnapPy was absent, so the "non-hyperbolic, Vol≈0"
     bullet that stood here was never measured. Measured, it is WRONG on
     both counts and the leg fails for a different, structural reason:

     (i) `atom_braid_word_3A` is a Hecke element, not a braid: 2A+1 of
         its letters are weight-1 averages over crossing sign, so tr_M is a
         weighted sum over 2^(2A+1) BRANCH closures (32 / 128 / 128 / 512
         for ²H / ³H / ³He / ⁴He). The old helper mapped EVERY letter to a
         positive generator, a lossy projection that is not one of the
         branches; its closure is degenerate (Vol ~ 1e-4) and is kept here
         only as `positive_projection_legacy` for the record.
     (ii) Sign-faithfully, every per-nucleon 3-strand branch closure IS
         hyperbolic on the live (alternating-core, `qou-hu1f` 2026-09-05)
         word: 2-component links L7a6 (4.7495), L11n202 (8.1957), L9n10
         (9.9665), L9a21 (11.9429), L11a252 (16.1911) — SnapPy geometric
         solutions, identified from the census. The 2026-08-25 "monotone
         ⇒ #T(2,k) ⇒ Vol = 0" result was true of the GROUPED word and is
         stale for the live one.
     (iii) Every inter-nucleon interface is a SINGLE letter, so each atom
         branch closure is the CONNECTED SUM of its per-nucleon branch
         closures — closure(β₁·σ_k^±·β₂) = closure(β₁) # closure(β₂) —
         verified by `deconnect_sum` on all 800 atom branches (exactly A
         summands each). The simplicial volume of a link exterior is the
         sum of the hyperbolic volumes of its JSJ pieces (Gromov, Soma),
         and the JSJ pieces of a connected sum / split union are those
         of the summands, so Vol(atom) − Vol(free) ≡ 0 on EVERY
         branch, hence for every branch weighting and for every ρ:
         B_C = ρ·0 = 0, residual −100 % on ²H, ³H, ³He, ⁴He.

INTERPRETATION (revised 2026-09-07). The refutation of C is scope-(b),
with the invariants named: the single-letter-interface closure identity
and connected-sum additivity of simplicial volume. What it excludes is
narrow — a binding read as a hyperbolic-volume DIFFERENCE between the
interface-inclusive and free closures of THIS word. It does NOT exclude an
absolute-volume reading (the per-nucleon pieces now carry Vol 4.7–16.2,
not 0), a non-additive functional of the pieces, or an interface built
from more than one letter; those are open, not refuted. Legs A and B are
unchanged. The old interpretation — that nonzero volume needs the
hand-assigned census knots (#1421) — no longer holds as stated: the
derived word's branch closures are hyperbolic; what vanishes is the
difference, which is the intensive/extensive gap in topological guise.
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

import itertools
import sys
from pathlib import Path

from mpmath import mp, mpf, fabs, log, catalan

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP, HA_MP  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from codata_constants import (  # noqa: E402
    Q_BETA_MEV,
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)
from binding_canonical import binding_canonical  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402


def _real(s):
    s = str(s).strip("()")
    try:
        return mpf(s)
    except (ValueError, TypeError):
        body = s[:-1] if s.endswith("j") else s
        for i in range(len(body) - 1, 0, -1):
            if body[i] in "+-" and body[i - 1] not in "eE":
                return mpf(body[:i] or "0")
        return mpf("0")


def _letter_kinds(word, h):
    """Classify each Hecke letter (c, d, g) of the atom word.

    Returns a list of (gen_1based, kind, w_plus, w_minus) where kind is +1
    for σ (d = 0), −1 for σ⁻¹ (d = −h) and 0 for an averaged, non-braid
    letter, and c·σ + d·1 = w_plus·σ + w_minus·σ⁻¹ under σ⁻¹ = σ − h, i.e.
    w_minus = −d/h, w_plus = c + d/h (exact mpf, no float)."""
    out = []
    tol = mpf("1e-30")
    for (c, d, g) in word:
        c, d = mpf(str(c)), mpf(str(d))
        r = d / h
        if fabs(r) < tol:
            kind = +1
        elif fabs(r + 1) < tol:
            kind = -1
        else:
            kind = 0
        out.append((g + 1, kind, c + r, -r))
    return out


def _geometric(M, tries=24):
    """Retriangulate until SnapPy finds a geometric solution; returns the
    solution-type string it settled on."""
    for _ in range(tries):
        sol = M.solution_type()
        if "positively" in sol:
            return sol
        M.randomize()
    return M.solution_type()


def _hp_volume(M):
    """Quad-double volume as an mpf. NOT verified (SnapPy `verified=True`
    needs Sage, absent here); quad-double is good to ~1e-30 on a geometric
    solution, and it is serialized at HP_DPS."""
    import snappy  # noqa: E402
    return mpf(str(snappy.ManifoldHP(M).volume()))


HP_DPS = 28      # quad-double: honest, sits ~1e-28 from any binary64
F64_DPS = 15     # anything that passed through a Python float
# Raise precision BEFORE building any module-scope mpf (module-const gate);
# idempotent alongside the call in main().
set_compute_dps()
PIECE_MATCH_TOL = mpf("1e-8")


def _nucleon_branch_table(Z1, N1, h):
    """All sign branches of one nucleon's 3-strand free word: the prime
    pieces every atom closure is built from. Keyed by the sign tuple over
    that nucleon's averaged letters."""
    import snappy  # noqa: E402
    kinds = _letter_kinds(atom_braid_word_3A(Z1, N1, include_inter=False), h)
    avg = [i for i, (_g, k, _wp, _wm) in enumerate(kinds) if k == 0]
    table = {}
    for signs in itertools.product((+1, -1), repeat=len(avg)):
        it = iter(signs)
        braid, weight = [], mpf(1)
        for (g, k, wp, wm) in kinds:
            s = k if k != 0 else next(it)
            braid.append(s * g)
            if k == 0:
                weight *= wp if s > 0 else wm
        L = snappy.Link(braid_closure=braid)
        M = L.exterior()
        sol = _geometric(M)
        hyp = "positively" in sol
        Ls = L.copy()
        Ls.simplify("global")
        try:
            ident = [str(x) for x in M.identify()]
        except Exception:  # noqa: BLE001 — identify() is best-effort
            ident = []
        table[signs] = {
            "signs": list(signs),
            "weight": weight,
            "components": len(L.link_components),
            "crossings_simplified": len(Ls.crossings),
            "solution_type": sol,
            "geometric": hyp,
            "vol_f64": mpf(str(float(M.volume()))),
            "vol_hp": _hp_volume(M) if hyp else None,
            "identify": ident,
        }
    return kinds, avg, table


def _snappy_leg_c(Z, N, h):
    """Observable C, sign-faithful. Returns a dict with `status` in
    {"unevaluated", "evaluated"}; an ImportError is a distinct verdict and
    never a refutation."""
    try:
        import snappy  # noqa: E402
    except ImportError as exc:
        return {"status": "unevaluated",
                "reason": f"SnapPy not importable: {exc}"}
    A = Z + N
    # --- prime pieces: per-nucleon branch closures -----------------------
    p_kinds, p_avg, p_tab = _nucleon_branch_table(1, 0, h)
    n_kinds, n_avg, n_tab = _nucleon_branch_table(0, 1, h)
    nucleons = ([("p", p_kinds, p_avg, p_tab)] * Z
                + [("n", n_kinds, n_avg, n_tab)] * N)
    pieces_all = list(p_tab.values()) + list(n_tab.values())

    # --- the free word must be the shifted concatenation of the nucleon words
    free_kinds = _letter_kinds(atom_braid_word_3A(Z, N, include_inter=False), h)
    expect = []
    for i, (_lab, kinds, _avg, _tab) in enumerate(nucleons):
        expect += [(g + 3 * i, k) for (g, k, _wp, _wm) in kinds]
    free_is_concat = [(g, k) for (g, k, _wp, _wm) in free_kinds] == expect

    # --- the atom word: enumerate every branch -----------------------------
    atom_kinds = _letter_kinds(atom_braid_word_3A(Z, N, include_inter=True), h)
    atom_avg = [i for i, (_g, k, _wp, _wm) in enumerate(atom_kinds) if k == 0]
    inter_gens = {3 * k + 3 for k in range(A - 1)}   # 1-based interface gens
    branches = []
    whole_sols = {}
    n_pieces_total = n_pieces_geom = n_pieces_matched = 0
    max_abs_diff = mpf(0)
    for signs in itertools.product((+1, -1), repeat=len(atom_avg)):
        it = iter(signs)
        braid, weight = [], mpf(1)
        nuc_signs = [[] for _ in range(A)]
        for (g, k, wp, wm) in atom_kinds:
            s = k if k != 0 else next(it)
            braid.append(s * g)
            if k == 0:
                weight *= wp if s > 0 else wm
                if g not in inter_gens:
                    nuc_signs[(g - 1) // 3].append(s)
        # free-branch volume: the matching nucleon pieces, split union
        vol_free = mpf(0)
        for i, (_lab, _kinds, _avg, tab) in enumerate(nucleons):
            rec = tab[tuple(nuc_signs[i])]
            vol_free += rec["vol_hp"] if rec["vol_hp"] is not None else mpf(0)
        # atom branch: whole closure + connected-sum decomposition
        L = snappy.Link(braid_closure=braid)
        M = L.exterior()
        sol_whole = _geometric(M, tries=6)
        whole_sols[sol_whole] = whole_sols.get(sol_whole, 0) + 1
        Ls = L.copy()
        Ls.simplify("global")
        parts = Ls.deconnect_sum()
        vol_atom = mpf(0)
        n_pieces_total += len(parts)
        for part in parts:
            Mp = part.exterior()
            solp = _geometric(Mp)
            if "positively" in solp:
                n_pieces_geom += 1
            vf64 = mpf(str(float(Mp.volume())))
            comps = len(part.link_components)
            match = None
            for rec in pieces_all:
                if (rec["components"] == comps
                        and fabs(rec["vol_f64"] - vf64) < PIECE_MATCH_TOL):
                    match = rec
                    break
            if match is not None:
                n_pieces_matched += 1
                vol_atom += match["vol_hp"]
            else:
                vol_atom += _hp_volume(Mp) if "positively" in solp else vf64
        diff = vol_atom - vol_free
        max_abs_diff = max(max_abs_diff, fabs(diff))
        branches.append({
            "weight": weight, "vol_free": vol_free, "vol_atom": vol_atom,
            "diff": diff, "n_pieces": len(parts),
            "whole_closure_solution": sol_whole,
            "whole_closure_cusps": M.num_cusps(),
        })
    wsum = sum(b["weight"] for b in branches)

    def wmean(key):
        return sum(b["weight"] * b[key] for b in branches) / wsum

    # --- the legacy lossy projection, for the record ------------------------
    legacy = {}
    for cfg, inter in (("free", False), ("atom", True)):
        w = atom_braid_word_3A(Z, N, include_inter=inter)
        M = snappy.Link(braid_closure=[g + 1 for (_c, _d, g) in w]).exterior()
        sol = _geometric(M, tries=6)
        legacy[cfg] = {"vol_f64": mpf(str(float(M.volume()))),
                       "solution_type": sol, "cusps": M.num_cusps(),
                       "geometric": "positively" in sol}

    return {
        "status": "evaluated",
        "snappy_version": snappy.__version__,
        "verified_volumes": False,
        "volume_precision": (
            f"quad-double (ManifoldHP), serialized at {HP_DPS} significant "
            "digits; NOT verified (SnapPy verified=True needs Sage)"),
        "n_branches": len(branches),
        "n_averaged_letters": len(atom_avg),
        "free_word_is_shifted_concatenation_of_nucleon_words": free_is_concat,
        "pieces_total": n_pieces_total,
        "pieces_geometric": n_pieces_geom,
        "pieces_matched_to_nucleon_table": n_pieces_matched,
        "pieces_per_branch_all_equal_A": all(b["n_pieces"] == A for b in branches),
        "whole_closure_solution_types": whole_sols,
        "whole_closure_geometric_count": sum(
            v for k, v in whole_sols.items() if "positively" in k),
        "whole_closure_cusps": sorted({b["whole_closure_cusps"] for b in branches}),
        "vol_free_min": min(b["vol_free"] for b in branches),
        "vol_free_max": max(b["vol_free"] for b in branches),
        "vol_free_weighted_mean": wmean("vol_free"),
        "vol_atom_min": min(b["vol_atom"] for b in branches),
        "vol_atom_max": max(b["vol_atom"] for b in branches),
        "vol_atom_weighted_mean": wmean("vol_atom"),
        "delta_vol_weighted_mean": wmean("diff"),
        "delta_vol_max_abs_over_branches": max_abs_diff,
        "nucleon_pieces": {"proton": list(p_tab.values()),
                           "neutron": list(n_tab.values())},
        "positive_projection_legacy": legacy,
    }


def _ser(obj, dps=HP_DPS):
    """Serialize mpf → string at an honest precision; leave the rest."""
    if isinstance(obj, mpf):
        return fmt(obj, dps=dps)
    if isinstance(obj, dict):
        return {k: _ser(v, F64_DPS if str(k).endswith("f64") else dps)
                for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_ser(v, dps) for v in obj]
    return obj


def main():
    set_compute_dps()
    wb = WitnessBuilder("binding-volume-difference-probe", engine="mpmath")

    q = Q_MP
    m_e = mpf(str(M_E_MEV))
    VOL_B3 = 8 * catalan
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(m_e, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    rho_cands = {"m_e": m_e, "E_0": E0, "m_e*8G": m_e * VOL_B3}

    AME = {
        "D": float(AME_B_DEUTERON_MEV_VALIDATION),
        "T": float(AME_B_TRITIUM_MEV_VALIDATION),
        "3He": float(AME_B_HE3_MEV_VALIDATION),
        "4He": float(AME_B_HE4_MEV_VALIDATION),
    }
    cases = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]

    print("=" * 72)
    print("VOLUME-DIFFERENCE BINDING PROBE  B = ρ·[Vol(atom) − Vol(free)]")
    print("=" * 72)

    data = {}
    for iso, Z, N in cases:
        r = binding_canonical(Z, N, Q_beta_n_mev=float(Q_BETA_MEV),
                              use_closed_form=True, verbose=False)
        tf = fabs(_real(r["tr_M_free"]))
        ta = fabs(_real(r["tr_M_atom"]))
        # A. log volume (algebraic quantum volume at q0)
        dVol_log = log(tf) - log(ta)  # = log(tf/ta) > 0
        # B. cosh-inversion: |tr| < 2 ⇒ elliptic, no real length
        cosh_ok = (tf >= 2) and (ta >= 2)
        data[iso] = {"tf": tf, "ta": ta, "dVol_log": dVol_log,
                     "cosh_defined": bool(cosh_ok)}

    # ---- Observable A: log volume, derived ρ ----
    print("\n[A] log-trace volume  ΔVol = log|tr_free/tr_atom|, derived ρ:")
    A_res = {}
    for name, rho in rho_cands.items():
        errs = {}
        for iso, _, _ in cases:
            Bp = rho * data[iso]["dVol_log"]
            errs[iso] = (Bp - mpf(str(AME[iso]))) / mpf(str(AME[iso])) * 100
        A_res[name] = errs
        print(f"  ρ={name:8s} ({mp.nstr(rho, 6)}): "
              + "  ".join(f"{i}{float(errs[i]):+5.0f}%" for i, _, _ in cases))

    # ---- Observable B: cosh-inversion ----
    print("\n[B] cosh-inversion ℓ = 2·arccosh(|tr|/2):")
    n_elliptic = sum(1 for iso, _, _ in cases if not data[iso]["cosh_defined"])
    for iso, _, _ in cases:
        d = data[iso]
        print(f"  {iso:4s}: |tr_free|={float(d['tf']):.3f} "
              f"|tr_atom|={float(d['ta']):.3f}  "
              f"→ {'loxodromic' if d['cosh_defined'] else 'ELLIPTIC (|tr|<2): no real length'}")
    print(f"  → {n_elliptic}/4 elliptic: cosh-volume undefined (degenerate).")

    # ---- Observable C: SnapPy hyperbolic volume of derived braid closure ----
    # Evaluated for the first time 2026-09-07 (bean qou-m6gp). An ImportError is
    # a DISTINCT verdict (`status: unevaluated`), never a refutation.
    print("\n[C] SnapPy hyperbolic Vol of the derived branch closures "
          "(sign-faithful; see module docstring):")
    h = mpf(str(HA_MP))
    C_res = {}
    for iso, Z, N in cases:
        C_res[iso] = _snappy_leg_c(Z, N, h)
        c = C_res[iso]
        if c["status"] != "evaluated":
            print(f"  {iso:4s}: {c['status']} — {c['reason']}")
            continue
        print(f"  {iso:4s}: {c['n_branches']} branches; pieces "
              f"{c['pieces_geometric']}/{c['pieces_total']} geometric, "
              f"{c['pieces_matched_to_nucleon_table']} matched; "
              f"whole closures geometric: {c['whole_closure_geometric_count']}"
              f"/{c['n_branches']} ({', '.join(c['whole_closure_solution_types'])}); "
              f"Vol_free [{mp.nstr(c['vol_free_min'], 6)}, {mp.nstr(c['vol_free_max'], 6)}] "
              f"wmean {mp.nstr(c['vol_free_weighted_mean'], 8)}; "
              f"Vol_atom wmean {mp.nstr(c['vol_atom_weighted_mean'], 8)}; "
              f"max|ΔVol| over branches {mp.nstr(c['delta_vol_max_abs_over_branches'], 3)}")
    snappy_ran = all(C_res[iso]["status"] == "evaluated" for iso, _, _ in cases)
    if snappy_ran:
        print("  per-nucleon branch closures (prime pieces):")
        for lab in ("proton", "neutron"):
            for rec in C_res["D"]["nucleon_pieces"][lab]:
                print(f"    {lab:7s} signs={rec['signs']} comps={rec['components']} "
                      f"{rec['solution_type']}  Vol={mp.nstr(rec['vol_hp'], 12) if rec['vol_hp'] is not None else '-'}  "
                      f"{rec['identify']}")
        # B_C = ρ · ΔVol with the SAME derived ρ candidates as leg A. ΔVol is the
        # branch-weighted mean of Vol(atom) − Vol(free); it is identically zero by
        # connected-sum additivity, and the max over branches is reported so that
        # "zero" is a measurement, not an assertion.
        print("\n  B_C = ρ·[Vol(atom) − Vol(free)], derived ρ (ΔVol ≡ 0 ⇒ −100 % everywhere):")
        C_errs = {}
        for name, rho in rho_cands.items():
            errs = {}
            for iso, _, _ in cases:
                dV = C_res[iso]["delta_vol_weighted_mean"]
                Bc = rho * dV
                errs[iso] = (Bc - mpf(str(AME[iso]))) / mpf(str(AME[iso])) * 100
            C_errs[name] = errs
            print(f"  ρ={name:8s}: "
                  + "  ".join(f"{i}{float(errs[i]):+7.2f}%" for i, _, _ in cases))
        any_hyp_piece = any(C_res[iso]["pieces_geometric"] > 0 for iso, _, _ in cases)
        all_additive = all(
            C_res[iso]["pieces_per_branch_all_equal_A"]
            and C_res[iso]["pieces_matched_to_nucleon_table"] == C_res[iso]["pieces_total"]
            and C_res[iso]["free_word_is_shifted_concatenation_of_nucleon_words"]
            for iso, _, _ in cases)
        max_dV = max(C_res[iso]["delta_vol_max_abs_over_branches"] for iso, _, _ in cases)
        C_closes = any(max(abs(e) for e in errs.values()) <= 10 for errs in C_errs.values())
        print(f"  → pieces hyperbolic: {any_hyp_piece}; every atom branch = connected sum of "
              f"its A nucleon pieces: {all_additive}; max|ΔVol| = {mp.nstr(max_dV, 3)}")
    else:
        C_errs = {}
        any_hyp_piece = all_additive = C_closes = False
        max_dV = None
        print("  → SnapPy NOT IMPORTABLE: observable C was NOT EVALUATED."
              "  This is not a refutation of C.")

    print(f"\n{'Triple' if snappy_ran else 'Double (C not evaluated)'} "
          "refutation: no DERIVED volume difference (log / cosh /")
    print("SnapPy) closes A≥3. For C the reason is structural: each interface is one")
    print("letter, so every branch closure is a connected sum of the per-nucleon")
    print("closures and the volume DIFFERENCE vanishes identically — even though the")
    print("per-nucleon pieces are themselves hyperbolic on the live word.")

    wb.set_description(
        "Derive-or-refute: does B = ρ·[Vol(atom)−Vol(free)] close A≥3 "
        "binding, using DERIVED volumes (no census-knot fit)? Three "
        "observables all fail: (A) log|tr_M| volume — no derived ρ closes "
        "it (−55…−90%); (B) cosh-inversion — every |tr_M|<2 (elliptic), no "
        "real length; (C) SnapPy on the derived word's 2^(2A+1) sign-branch "
        "closures — EVALUATED 2026-09-07 (qou-m6gp): the per-nucleon pieces "
        "ARE hyperbolic (2-component links, Vol 4.75–16.19), but every "
        "inter-nucleon interface is a single letter, so each atom branch "
        "closure is the connected sum of its nucleon pieces and "
        "Vol(atom) − Vol(free) ≡ 0 by additivity of simplicial volume; "
        "B_C = ρ·0 = 0 for every ρ (−100 %). Scope-(b) on the DIFFERENCE "
        "only; an absolute-volume reading is NOT excluded. The earlier "
        "'non-hyperbolic, Vol≈0' wording was never measured and is wrong "
        "for the live (alternating-core) word."
    )
    wb.add_data("log_volume_errs_pct", _ser(A_res))
    wb.add_data("cosh_inversion", {
        iso: {"abs_tr_free": mp.nstr(data[iso]["tf"], 6),
              "abs_tr_atom": mp.nstr(data[iso]["ta"], 6),
              "loxodromic": data[iso]["cosh_defined"]}
        for iso, _, _ in cases})
    wb.add_data("snappy_branch_closures", _ser(C_res))
    wb.add_data("snappy_volume_diff_errs_pct", _ser(C_errs))
    # Per-observable verdicts, COMPUTED rather than declared.  "Closes A≥3" is
    # given a deliberately GENEROUS 10% window: making it easier for a candidate
    # to count as closing makes finding none a STRONGER negative, not a weaker
    # one.  (At 25% the answer is still none — the best ρ is 69% off on ⁴He.)
    CLOSE_TOL_PCT = 10.0
    rho_closing = sorted(
        name for name, errs in A_res.items()
        if max(abs(e) for e in errs.values()) <= CLOSE_TOL_PCT)
    observables = {
        "log_volume": {
            "evaluated": True,
            "closes_A3": bool(rho_closing),
            "closing_rho": rho_closing,
        },
        "cosh_inversion": {
            "evaluated": True,
            # A cosh length exists only for a loxodromic trace; every case
            # being elliptic is precisely why this observable cannot close.
            "closes_A3": n_elliptic == 0,
            "n_elliptic": n_elliptic,
            "n_cases": len(cases),
        },
        "snappy_braid_closure": {
            "evaluated": snappy_ran,
            "closes_A3": bool(C_closes),
            "pieces_hyperbolic": bool(any_hyp_piece),
            "every_branch_is_connected_sum_of_nucleon_pieces": bool(all_additive),
            "max_abs_delta_vol_over_all_branches": (
                fmt(max_dV, dps=HP_DPS) if max_dV is not None else None),
        },
    }
    n_evaluated = sum(1 for o in observables.values() if o["evaluated"])
    n_closing = sum(1 for o in observables.values()
                    if o["evaluated"] and o["closes_A3"])
    wb.add_data("observables", observables)
    wb.add_data("observables_evaluated", n_evaluated)
    wb.add_data("observables_total", len(observables))
    wb.add_data("snappy_available", snappy_ran)
    if not snappy_ran:
        wb.add_caveat(
            "Observable C (SnapPy hyperbolic volume of the derived branch "
            "closures) was NOT EVALUATED in this run: SnapPy is not importable. "
            "`_snappy_leg_c` reports this as a distinct `unevaluated` status; "
            "it is not a refutation. The refutation recorded here rests on "
            "observables A and B only (beans qou-26f2, qou-m6gp)."
        )
    else:
        wb.add_caveat(
            "Observable C volumes are SnapPy ManifoldHP (quad-double) on "
            "geometric solutions, serialized at 28 significant digits; they "
            "are NOT verified (SnapPy verified=True requires Sage, absent). "
            "Piece identification is by (components, double-precision volume "
            "within 1e-8) against the per-nucleon table; the structural claim "
            "(atom branch = connected sum of nucleon pieces) is checked by "
            "`deconnect_sum` piece counts, not by the volumes."
        )
    wb.add_data("conclusion", {
        "log_volume": "refuted — no derived ρ closes (κ spans 313%)",
        "cosh_inversion": "degenerate — all |tr_M|<2 (elliptic regime)",
        "snappy_braid_closure": (
            "refuted, scope-(b) — Vol(atom) − Vol(free) ≡ 0 on every branch "
            "because each interface is one letter (closure = connected sum of "
            "nucleon pieces; simplicial volume additive). The pieces ARE "
            "hyperbolic; only the DIFFERENCE vanishes. Not excluded: an "
            "absolute-volume reading, a non-additive functional, a multi-letter "
            "interface." if snappy_ran
            else "NOT EVALUATED — SnapPy not importable (distinct verdict, not "
                 "a refutation)"),
        "interpretation": "no derived real-q volume DIFFERENCE repairs the "
                          "linear truncation: legs A/B fail numerically, leg C "
                          "vanishes structurally (connected-sum additivity — "
                          "the intensive/extensive gap in topological guise). "
                          "The pre-2026-09-07 claim that the derived closures "
                          "are non-hyperbolic is retracted for the live word.",
    })
    wb.add_assertion(
        "no_derived_volume_difference_closes_A3",
        computed=n_closing,
        expected=0,
        tolerance=0,
        unit="observables",
        source=(
            f"Of the {n_evaluated} of {len(observables)} observables that were "
            f"actually EVALUATED, {n_closing} close A≥3. (A) log|tr| volume: no "
            f"derived ρ brings all four isotopes within a generous ±"
            f"{CLOSE_TOL_PCT:g}% — the best is ~69% off on ⁴He; a generous "
            "window makes zero hits a stronger negative, not a weaker one. "
            f"(B) cosh-inversion: {n_elliptic}/{len(cases)} traces elliptic "
            "(|tr|<2), so no real length exists and the observable cannot "
            "close. (C) SnapPy: "
            + (f"evaluated on {sum(C_res[i]['n_branches'] for i, _, _ in cases)} "
               f"sign-branch closures; nucleon pieces hyperbolic={any_hyp_piece}; "
               f"every branch a connected sum of its nucleon pieces={all_additive}; "
               f"max|Vol(atom)−Vol(free)| over all branches = "
               f"{fmt(max_dV, dps=6)} ⇒ B_C = 0 for every ρ."
               if snappy_ran else
               "NOT EVALUATED — SnapPy is not importable, so this leg is absent "
               "from the count rather than counted as a refutation; see the "
               "caveat.")
            + " Was computed=1/expected=1 (bean qou-26f2), which passed at the "
            "value that refutes the claim and hid C never having run."
        ),
    )
    wb.save()


if __name__ == "__main__":
    main()
