#!/usr/bin/env python3
"""
Probe — L2 error ATTRIBUTION for the light isotopes (²H–⁷Li).

The L2 goal (`docs/precision-goals.md`) asks, per observable O, for
`σ_pred(O) ≤ σ_exp(O)/100`. For the light nuclei the predicted mass misses
by 1e-4 – 6e-3 RELATIVE, i.e. ~1e9 – 1e12 times the target. The obvious
question — and the one this probe answers with numbers rather than prose —
is *which term* carries that miss.

The predicted mass is a two-term object:

    M_pred(Z, N) = Z·m_p,can + N·m_n,can  −  B_model
                   \_______________________/    \______/
                     CONSTITUENT term             BINDING term

so the mass error decomposes EXACTLY (no cross terms, the split is linear):

    δM ≡ M_pred − M_meas = [Z·δm_p + N·δm_n]  −  [B_model − B_AME]
                            \______________/     \_______________/
                              δ_const               δ_bind

This probe evaluates both legs for every low isotope and reports each as
MeV, as a relative error, and as a MULTIPLE OF THE 1 ppQ (1e-15) L2 target,
plus the share of |δM| each leg carries.

What it is NOT: this is an audit, not a new prediction. Every input is read
from the existing canonical pipeline (`mass_binding_dashboard._row`, itself
the Jones–Markov trace at α = E₀) and AME2020. Nothing here is fitted and
nothing is wired to production. The conclusion it certifies is a NEGATIVE
one about attribution, which is exactly what it should be used for:

    the light-isotope L2 miss is ~100 % binding. The constituent leg is
    ~1e6 times smaller than the binding leg at every A ≥ 2, so no amount
    of nucleon-mass precision work moves L2 for a nucleus.

Scope note (per AGENTS.md §"Before declaring refuted"): this is a
scope-(a) statement about the CURRENT B_model forms, not a structural
exclusion of anything. It says where the error IS, not what cannot fix it.

NO WITNESS — deliberately (2026-08-10). Every number here descends from
`mass_binding_dashboard._constants()`, which sources the 50-dps q₀ and then
casts to `float` ONCE at its own boundary ("cast ONCE at the boundary" in
that function). The whole dashboard is therefore an f64 display pipeline by
construction, and a witness built from it would enshrine 413 raw-float64
fields — which is what the NO-FLOAT64 ratchet
(`witness_raw_float64_audit.py`) exists to stop. The honest options were
(a) carry mpf from the source, which is impossible without rewriting the
dashboard's numeric core, or (b) do not emit. Baselining the file was not an
option (`scripts/precision-gates.sh`: "Fix AT THE PRODUCER. Do not add a
file to a baseline"). This probe takes (b) and prints instead.

That constraint is itself part of the answer this probe is asked for: the
light-isotope binding path cannot even REPRESENT a 1e-15 effect today, let
alone predict one. The attribution below is an O(1e-3) accounting question,
where f64's ~16 digits are ample.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02). Keeps
# flat-namespace imports working from the `probes/` cluster subdirectory.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys

import mass_binding_dashboard as mbd  # noqa: E402

# The L2 compute-precision goal, as a relative error (1 part per quadrillion).
PPQ = 1e-15

# The binding forms carried per row, in the dashboard's own key names.
# `B_sym` is the production/DERIVED exact log-trace; the others are shown so
# the attribution is not an artefact of one form's particular failure.
BINDING_FORMS = ("B_sym", "B_qCLT_fac", "B_can0", "B_can_bor", "B_vol", "E_gate")


def _rows():
    """Evaluate the canonical low-isotope rows, exactly as /dashboard-low does."""
    me, q0, E0 = mbd._constants()
    Lbond = mbd._bond_type_L()
    nucleon_msym = mbd._nucleon_msym(E0)
    mp_can, mn_can = mbd._nucleon_mass_canonical(me, q0)
    ame = mbd._ame_table()
    sel = mbd.GROUPS["low"]
    rows = [mbd._row(nm, Z, N, E0, me, Lbond, nucleon_msym, ame, 21)
            for (nm, Z, N) in sel]
    return rows, float(mp_can), float(mn_can), float(me), float(q0), float(E0)


def _f(v):
    """Display/scalar boundary: mpf → float. Attribution ratios are O(1)–O(1e12);
    f64 carries ~16 digits, which is ~4 orders more than any ratio reported."""
    return None if v is None else float(v)


def main() -> int:
    rows, mp_can, mn_can, me, q0, E0 = _rows()

    # ---- constituent-leg errors, measured against CODATA -------------------
    # m_p is the ANCHOR (q₀ is pinned from m_p/m_e), so its residual is a
    # round-trip, not an accuracy. m_n IS a genuine prediction. Both are read
    # from the same canonical nucleon-mass routine the dashboard uses.
    import codata_constants as codata
    mp_ref = float(codata.M_P_MEV_VALIDATION)
    mn_ref = float(codata.M_N_MEV_VALIDATION)
    d_mp = mp_can - mp_ref
    d_mn = mn_can - mn_ref

    out = []
    for r in rows:
        Z, N = r["Z"], r["N"]
        A = Z + N
        B_AME = _f(r.get("B_AME"))
        if B_AME is None:
            continue
        # Measured nuclear mass, exactly as the dashboard's mass table builds
        # it: the CODATA constituent sum minus the AME2020 binding.
        M_meas = Z * mp_ref + N * mn_ref - B_AME

        d_const = Z * d_mp + N * d_mn

        per_form = {}
        for key in BINDING_FORMS:
            B = _f(r.get(key))
            if B is None:
                continue
            d_bind = B - B_AME             # model minus experiment
            d_M = d_const - d_bind         # M = Zm_p + Nm_n − B
            tot = abs(d_const) + abs(d_bind)
            per_form[key] = {
                "B_model_MeV": B,
                "delta_bind_MeV": d_bind,
                "delta_M_MeV": d_M,
                "rel_err_M": d_M / M_meas,
                "rel_err_M_over_ppq_target": abs(d_M / M_meas) / PPQ,
                "bind_share_of_abs_error": abs(d_bind) / tot if tot else None,
                "const_share_of_abs_error": abs(d_const) / tot if tot else None,
                "bind_over_const_ratio": (abs(d_bind) / abs(d_const)
                                          if d_const else None),
                "B_AME_over_B_model": B_AME / B if B else None,
                # How much binding per nucleon each form delivers, against the
                # ~8 MeV/A empirical saturation plateau. This is the single
                # most diagnostic number: the trace forms plateau near ~2.5.
                "B_model_per_A_MeV": B / A,
            }

        # The ACTUAL L2 target for this isotope. L2 is `sigma_pred <= sigma_exp/100`,
        # so the target is set by AME2020's own uncertainty on the mass — it is NOT
        # 1 ppQ. 1 ppQ is the L1 *compute* target and is a different leg entirely
        # (see docs/precision-goals.md: "'1 ppQ' by itself is ambiguous").
        sigma_B = _f(r.get("sigma_AME"))
        sigma_rel = (sigma_B / M_meas) if sigma_B else None
        l2_target_rel = (sigma_rel / 100.0) if sigma_rel else None

        out.append({
            "iso": r["name"], "Z": Z, "N": N, "A": A,
            "M_meas_MeV": M_meas,
            "sigma_exp_rel_mass": sigma_rel,
            "l2_target_rel_mass": l2_target_rel,
            "B_AME_MeV": B_AME,
            "B_AME_per_A_MeV": B_AME / A,
            "sigma_exp_B_MeV": _f(r.get("sigma_AME")),
            "delta_const_MeV": d_const,
            "delta_const_rel": d_const / M_meas,
            "delta_const_over_ppq_target": abs(d_const / M_meas) / PPQ,
            "forms": per_form,
        })

    # ---- headline aggregates ----------------------------------------------
    # Worst-case and typical binding-share, over the production form B_sym.
    shares = [o["forms"]["B_sym"]["bind_share_of_abs_error"]
              for o in out if "B_sym" in o["forms"]]
    ratios = [o["forms"]["B_sym"]["bind_over_const_ratio"]
              for o in out if "B_sym" in o["forms"]
              and o["forms"]["B_sym"]["bind_over_const_ratio"] is not None]
    min_share = min(shares) if shares else None
    min_ratio = min(ratios) if ratios else None

    # The falsifiable content of this probe: binding dominates everywhere. If
    # any light isotope had a competitive constituent leg, this would fail.
    dominates = bool(min_share is not None and min_share > 0.99)

    # ---- human-readable table ---------------------------------------------
    print(f"\nL2 error attribution — light isotopes (q₀ = {q0!r}, α = E₀ = {E0:.6f} MeV)")
    print(f"constituent inputs: δm_p = {d_mp:+.3e} MeV ({d_mp/mp_ref:+.3e} rel, ANCHOR round-trip)")
    print(f"                    δm_n = {d_mn:+.3e} MeV ({d_mn/mn_ref:+.3e} rel, PREDICTION)\n")
    print("| iso | A | B_AME | B_sym | δ_const (MeV) | δ_bind (MeV) | bind/const | δM/M | × 1ppQ target |")
    print("| --- | --: | ----: | ----: | ------------: | -----------: | ---------: | ---: | ------------: |")
    for o in out:
        f = o["forms"].get("B_sym")
        if not f:
            continue
        print(f"| {o['iso']:<3} | {o['A']:>2} | {o['B_AME_MeV']:>6.2f} | "
              f"{f['B_model_MeV']:>6.2f} | {o['delta_const_MeV']:>+13.3e} | "
              f"{f['delta_bind_MeV']:>+12.3f} | {f['bind_over_const_ratio']:>10,.0f} | "
              f"{f['rel_err_M']:>+.3e} | {f['rel_err_M_over_ppq_target']:>13.3e} |")
    print("\nL2 — the real per-isotope target is sigma_exp/100 on the MASS, not 1 ppQ:")
    print("| iso | A | σ_exp(M) | L2 target | δM/M (B_sym) | L2 miss | binding accuracy L2 needs |")
    print("| --- | --: | -------: | --------: | -----------: | ------: | ------------------------: |")
    for o in out:
        f = o["forms"].get("B_sym")
        t = o.get("l2_target_rel_mass")
        if not f or not t:
            continue
        miss = abs(f["rel_err_M"]) / t
        # What L2 demands of the BINDING term specifically: the whole mass-error
        # budget has to fit inside the target, and binding is the only live leg.
        # Note this is BRUTAL: sigma_exp is quoted on the mass, but binding is
        # only ~0.1-0.8 % of the mass, so the budget in eV is tiny compared to B.
        need_B_eV = t * o["M_meas_MeV"] * 1e6
        need_B_rel = need_B_eV / (o["B_AME_MeV"] * 1e6)
        print(f"| {o['iso']:<3} | {o['A']:>2} | {o['sigma_exp_rel_mass']:.2e} | {t:.2e} | "
              f"{f['rel_err_M']:+.2e} | {miss:>7.1e} | {need_B_eV:>8.4f} eV of "
              f"{o['B_AME_MeV']:>5.1f} MeV ({need_B_rel:.1e} rel) |")

    print(f"\nB/A plateau — experiment vs the trace form (MeV per nucleon):")
    print("| iso | A | B_AME/A | B_sym/A |")
    print("| --- | --: | ------: | ------: |")
    for o in out:
        f = o["forms"].get("B_sym")
        if not f:
            continue
        print(f"| {o['iso']:<3} | {o['A']:>2} | {o['B_AME_per_A_MeV']:>7.3f} | "
              f"{f['B_model_per_A_MeV']:>7.3f} |")

    print(f"\nbinding leg carries > 99 % of |δM| on every row: {dominates}")
    print(f"  smallest binding/constituent ratio across ²H–⁷Li: {min_ratio:,.0f}×"
          if min_ratio else "  (insufficient rows)")
    print("  ⇒ driving m_p and m_n to exact CODATA moves the light-isotope L2 miss")
    print("    by less than one part in 1e5 of itself. L2 for nuclei is a BINDING problem.")
    print("\n(no witness by design — see module docstring: the dashboard is an f64")
    print(" display pipeline, so a witness here would enshrine raw float64.)")
    return 0 if dominates else 1


if __name__ == "__main__":
    sys.exit(main())
