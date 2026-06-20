#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

Atom binding via the CANONICAL Jones-Markov trace.

Wires markov_trace_canonical.tr_M_element (Direction 1 of the
validity audit) into the atom braid-word binding calculation:

  B(Z, N) = E_0 · ( tr_M(W_free) − tr_M(W_atom) )   [signed; categorical]

where tr_M is the Markov-axioms-satisfying trace matching
prop:categorical-mass-markov's explicit values table — NOT the
Plancherel-weighted form used in hecke_core.atom_markov_trace and
mass_at_3A_proper.binding_3A (both deviate from the prop's z =
1/(q^{1/2} + q^{-1/2}) ≈ 0.499).

Result is compared to:
  • binding_3A (Plancherel)         — current best H_{3A} path
  • tower_binding_full (H_3 tower)  — current per-gen path
  • AME experimental binding        — ground truth

For small A (D, T, 3He, 4He), the full atom braid word reduces to a
symbolic Hecke element; the canonical trace gives an exact value
in q that we evaluate at q₀ = 1.11.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
import time
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from markov_trace_canonical import tr_M_element
from hecke_symbolic import (
    SymbolicHeckeDivision, SymbolicHeckeElement, HA as H_SYMB, q as q_sym,
)
from mass_at_3A_proper import atom_braid_word_3A
from experimental_constants import Q_NEUTRON_MEV as _Q_BETA_N
from q_parameter import Q as q0, HA as h_q  # canonical aliases per AGENTS.md §7
from witness_base import WitnessBuilder  # noqa: E402
# AME 2020 binding-energy comparison targets + proton mass (validation-only,
# NOT calibration inputs — per AGENTS.md §"Canonical derivation chain" the
# 3 calibrations are CAL-1 m_e, CAL-2 𝔇_β, CAL-3 𝔇_π; these AME values
# are used ONLY for the err = pred - AME_B_* comparison in the __main__
# print loop below). Added via PR #1105 (codata_constants AME extension).
from codata_constants import (
    M_P_MEV_VALIDATION,
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)


def build_atom_symbolic(Z: int, N: int, *, include_inter: bool = True,
                          m_pp: int = 1, m_pn: int = 1,
                          m_nn: int = 1,
                          reduce_every: int = 4,
                          max_terms: int = 50000,
                          ) -> SymbolicHeckeElement:
    """Build atom braid as SymbolicHeckeElement using symbolic q.

    Incremental Gröbner-Shirshov reduction: apply `div.reduce()` after
    every `reduce_every` factors multiplied in, instead of letting
    the flat product expand to millions of terms before a single
    final reduction.  This matches the pattern in
    `nuclear-braid-exact.py::build_nuclear_braid_incremental`.

    Parameters
    ----------
    reduce_every : int
        Number of factors to multiply in between reduction steps.
        Setting this to 1 reduces after every factor (safest, slowest
        per-factor); 4 matches a nucleon intra-shell (two gens × two
        factors); setting it to infinity reproduces the legacy flat
        build (blows up at 4He).  Default 4.
    max_terms : int
        Abort if the intermediate element exceeds this many terms
        after a reduction step.  Matches the nuclear-braid-exact
        default; raises RuntimeError if hit.
    """
    word = atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                include_inter=include_inter)

    def _factor_from(c_f: float, d_f: float, g: int
                      ) -> SymbolicHeckeElement:
        if abs(c_f) < 1e-12:
            c = sp.Integer(0)
        else:
            c = sp.Integer(1)
        if abs(d_f) < 1e-12:
            d = sp.Integer(0)
        elif abs(d_f - 1.0) < 1e-12:
            d = sp.Integer(1)
        elif abs(d_f + h_q) < 1e-6:
            d = -H_SYMB
        elif abs(d_f + h_q / 2) < 1e-6:
            d = -H_SYMB / 2
        else:
            d = sp.nsimplify(d_f)
        return SymbolicHeckeElement({(g,): c, (): d})

    div = SymbolicHeckeDivision()
    elem = SymbolicHeckeElement.identity()
    since_last_reduce = 0
    for (c_f, d_f, g) in word:
        elem = elem * _factor_from(c_f, d_f, g)
        since_last_reduce += 1
        if since_last_reduce >= reduce_every:
            elem, _ = div.reduce(elem, engine='laurent')
            since_last_reduce = 0
            if elem.n_terms() > max_terms:
                raise RuntimeError(
                    f"atom-braid build exceeded max_terms={max_terms} "
                    f"(Z={Z}, N={N}, gen={g}); current terms = "
                    f"{elem.n_terms()}")
    if since_last_reduce > 0:
        elem, _ = div.reduce(elem, engine='laurent')
    return elem


def binding_canonical(Z: int, N: int, *, m_pp=1, m_pn=1, m_nn=1,
                        Q_beta_n_mev: float = float(_Q_BETA_N),
                        reduce_before_trace: bool = True,
                        use_closed_form: bool = False,
                        use_transfer: bool = True,
                        verbose: bool = False,
                        **kwargs) -> dict:
    """Binding via canonical Markov trace.

    B = Q_β(n) · (tr_M(W_free) − tr_M(W_atom)),   [SIGNED categorical
    difference — see the in-body note; the double-modulus form was a
    non-archimedean misuse]
    Q_β(n) = 0.78233341 MeV (free-neutron β-decay Q-value, CAL-3
    per [`prop:three-calibration-inputs`](../../content/quantum-observable-universe/braids-and-knots/three-calibration-inputs.md)).

    **Naming note (2026-05-17, this branch).** This binding-scale
    parameter is the **β-decay Q-value $Q_\\beta(n)$**, **NOT** the
    canonical energy scale $E_0 = m_e/(q_0(q_0-1)) \\approx 4.186$
    MeV (a different quantity, ~5× larger). Earlier revisions
    misnamed this parameter `E_0`; the value used here is correct
    (the formula in [`prop:categorical-mass-markov`](../../content/quantum-observable-universe/braids-and-knots/categorical-mass-markov.md)
    requires $Q_\\beta$-scaled dimensionless trace differences),
    only the name was wrong. The function now exposes the parameter
    with its correct identifier. **Dimensional note.** `Q_beta_n_mev`
    enters the formula `B = Q_β(n) · (tr_M(W_free) - tr_M(W_atom))`
    as the **MeV-dimensioned multiplier** of a dimensionless trace
    difference; no further $E_0$ scaling is applied (in particular,
    do *not* multiply the result by `e_0_full_mev()` — that would
    double-scale).

    Callers that previously passed `E_0=...` must update to
    `Q_beta_n_mev=...`. The old keyword is captured by `**kwargs`
    and raises an explicit `AssertionError` with the migration
    message; any other unexpected keyword raises `TypeError`. The
    single internal caller `kahler_lift.py:343` is updated in the
    same commit.
    """
    assert "E_0" not in kwargs, (
        "binding_canonical: the `E_0` keyword is deprecated; the "
        "parameter was misnamed and is now `Q_beta_n_mev` (the "
        "free-neutron β-decay Q-value, NOT the canonical energy "
        "scale E_0 ≈ 4.186 MeV). Pass `Q_beta_n_mev=...` instead."
    )
    if kwargs:
        raise TypeError(
            f"binding_canonical: unexpected keyword arguments "
            f"{sorted(kwargs)}"
        )
    A = Z + N
    n_strands = 3 * A

    # ── Fast path: fine-Bratteli transfer matrix (DEFAULT) ───────
    # Lossless Σ_{λ ⊢ 3A} y_λ χ^λ over ALL p(3A) partitions via the
    # monotone-word transfer matrix — no d_λ wall, no native dep, full
    # 50-dps (the legacy symbolic path below collapses to float64 via
    # complex(sp.N(...)) and lossily nsimplify's the color-weighted δ,
    # so the transfer path is both faster AND more precise here).
    # ~5000× the symbolic tr_M_element path (⁶Li 0.16 s vs ~17 min);
    # transfer ≡ char_fast (full Hoefsmit) to 4.7e-15. Honours the
    # no-truncation precision ruling — ALL partitions kept, the speed is
    # from the transfer sweep, NOT from dropping partitions (see
    # docs/audits/2026-06-10-binding-active-set-compute-optimization.md).
    # use_closed_form=True still takes precedence: it is the
    # strict_averaged-convention path retained for that family of callers
    # (mass_table_comprehensive, binding_factor_f_*, …).
    if use_transfer and not use_closed_form:
        import mpmath as mp
        from tr_m_atom_via_transfer import tr_m_atom_zn
        tr_atom_mp, tr_free_mp, chi_atom, wall = tr_m_atom_zn(
            Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn, dps=50)
        # Signed categorical scalar Δtr = tr_M(W_free) − tr_M(W_atom);
        # Im(q_0)=0 ⇒ real at the substrate anchor. Q_β(n) is the MeV-
        # dimensioned multiplier of the dimensionless trace difference.
        delta_tr = tr_free_mp - tr_atom_mp
        B = mp.mpf(str(Q_beta_n_mev)) * delta_tr
        if verbose:
            print(f"  transfer tr_M (all λ={len(chi_atom)}, lossless): "
                  f"atom={mp.nstr(tr_atom_mp, 12)} "
                  f"free={mp.nstr(tr_free_mp, 12)}  {wall:.3f}s")
        return {
            "status": "solved",
            "Z": Z, "N": N, "A": A,
            "tr_M_atom": mp.nstr(tr_atom_mp, mp.mp.dps),
            "tr_M_free": mp.nstr(tr_free_mp, mp.mp.dps),
            "Q_beta_n_MeV": Q_beta_n_mev,
            "B_MeV": float(B),
            "n_atom_terms": -1,
            "n_free_terms": -1,
            "use_closed_form": False,
            "use_transfer": True,
            "n_partitions": len(chi_atom),
            "wall_sec": wall,
        }

    div = SymbolicHeckeDivision() if reduce_before_trace else None

    # ── Fast path: closed-form tr_M(𝓑_K) (Phase 5q identity) ────
    # When `use_closed_form=True`, skip the symbolic H_{3A} tr_M
    # recursion entirely. The Phase 5c.1 + 5l identity gives
    #   tr_M(𝓑_K)      = tr_M^3(p)^Z · tr_M^3(n)^N · ∏_i f_i(q)
    #   tr_M(𝓑_K^vac) = tr_M^3(p)^Z · tr_M^3(n)^N           (no interfaces)
    # where the H_3 building blocks tr_M^3(p), tr_M^3(n) are computed
    # ONCE at q_0 and reused for every (Z, N). For A=3 this cuts the
    # 5-12 k-op sympy aggregation entirely; for A≥4 it sidesteps the
    # H_{3A} partition sum which is the asymptotic bottleneck per
    # cheat-sheet §5 Migration Backlog #4.
    if use_closed_form:
        try:
            from closed_form_tau_M import closed_form_tau_M
            from tr_m_wenzl_bridge_mpfr import tr_M_via_wenzl_bridge_mpfr
            from hecke_core import (
                _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
            )
            import mpmath as mp
            from q_parameter import Q_50_DIGIT_STR

            t0 = time.time()
            q_val = mp.mpf(Q_50_DIGIT_STR)
            # tau_p, tau_n via the Wenzl bridge at H_3 — same
            # entry point as the production atom-level code, with
            # Python fallback when pyhecke_native is unavailable.
            def _nucleon_word(g0, g1):
                return (
                    [(c, d, 0) for c, d in g0]
                    + [(c, d, 1) for c, d in g1]
                )
            tau_p = tr_M_via_wenzl_bridge_mpfr(
                _nucleon_word(_PROTON_G0, _PROTON_G1),
                3, Q_50_DIGIT_STR, dps=50,
            )
            tau_n = tr_M_via_wenzl_bridge_mpfr(
                _nucleon_word(_NEUTRON_G0, _NEUTRON_G1),
                3, Q_50_DIGIT_STR, dps=50,
            )
            # `strict_averaged` matches the symbolic path's literal
            # σ - h/2 factor for p-n interfaces (the convention in
            # `_factor_from` inside build_atom_symbolic). The default
            # `chi_lambda_braid` convention treats averaged as σ (the
            # production marshalling for chi_lambda_braid) which
            # gives a different numerical value here.
            tr_atom_mp = closed_form_tau_M(
                Z, N, q_val, tau_p, tau_n,
                pn_convention="strict_averaged",
            )
            # Free config = no interface factors → just the constit part.
            tr_free_mp = (mp.mpf(tau_p) ** Z) * (mp.mpf(tau_n) ** N)
            dt = time.time() - t0
            tr_atom = complex(float(tr_atom_mp), 0.0)
            tr_free = complex(float(tr_free_mp), 0.0)
            atom_n_terms = -1  # not computed in closed-form path
            free_n_terms = -1
            tr_atom_sym = None
            tr_free_sym = None
        except Exception as e:
            return {"status": "closed_form_error", "error": str(e),
                    "Z": Z, "N": N, "A": A}
    else:
        # ── Legacy symbolic path ──────────────────────────────
        atom_elem = build_atom_symbolic(Z, N, include_inter=True,
                                          m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
        free_elem = build_atom_symbolic(Z, N, include_inter=False,
                                          m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)

        if reduce_before_trace:
            atom_elem, _ = div.reduce(atom_elem, engine='laurent')
            free_elem, _ = div.reduce(free_elem, engine='laurent')

        if verbose:
            print(f"  atom NF: {atom_elem.n_terms()} terms;  "
                  f"free NF: {free_elem.n_terms()} terms")

        t0 = time.time()
        try:
            # `simplify=False`: skip the `sp.simplify` step in tr_M_element.
            # At A=3 the aggregated total has ~5000-12000 sympy ops; calling
            # `simplify` exceeds 30 minutes (³He) while the recursion itself
            # runs in seconds.  Numerical evaluation at q=q₀ (below) is
            # unaffected.  See #508 Phase 2 part 2.
            tr_atom_sym = tr_M_element(atom_elem, n_strands, simplify=False)
            tr_free_sym = tr_M_element(free_elem, n_strands, simplify=False)
        except (NotImplementedError, RecursionError) as e:
            return {"status": "trace_error", "error": str(e),
                    "Z": Z, "N": N, "A": A,
                    "n_atom_terms": atom_elem.n_terms(),
                    "n_free_terms": free_elem.n_terms()}
        dt = time.time() - t0
        atom_n_terms = atom_elem.n_terms()
        free_n_terms = free_elem.n_terms()

        try:
            tr_atom = complex(sp.N(tr_atom_sym.subs(q_sym, q0)))
            tr_free = complex(sp.N(tr_free_sym.subs(q_sym, q0)))
        except Exception as e:
            return {"status": "eval_error", "error": str(e)}

    tr_atom_r = tr_atom.real if abs(tr_atom.imag) < 1e-6 else tr_atom
    tr_free_r = tr_free.real if abs(tr_free.imag) < 1e-6 else tr_free
    # Categorical binding scalar is the SIGNED trace difference
    #   Δtr = tr_M(W_free) − tr_M(W_atom).
    # The double-modulus form |tr_M(W_free)| − |tr_M(W_atom)| was a
    # non-archimedean misuse (per
    # docs/audits/2026-06-01-paper-modulus-nonarchimedean-audit.md): it
    # applies the archimedean observation `|·|` to each trace BEFORE the
    # difference, which is neither the signed categorical scalar nor the
    # bar-norm `tr_M·\bar{tr_M}`.  The per-mass positivity observation is
    # a no-op here (both traces are real & positive at q_0 ∈ ℝ), so the
    # signed difference IS the archimedean binding — and it correctly
    # preserves the binding/anti-binding SIGN, which the double-modulus
    # form would distort whenever a trace is negative.
    delta_tr = tr_free_r - tr_atom_r                      # signed categorical scalar
    # Archimedean realization at the substrate anchor: Im(q_0) = 0
    # (the `lusztig_q_0_imaginary_part_zero` constraint), so the physical
    # observable is the real part.  `.real` is taken explicitly (not as a
    # silent collapse) and works uniformly for float / Python-complex /
    # mpmath.mpc (the latter does NOT subclass Python `complex`, so an
    # isinstance guard would be fragile — per Gemini review on PR #1738).
    B = Q_beta_n_mev * delta_tr.real
    return {
        "status": "solved",
        "Z": Z, "N": N, "A": A,
        "tr_M_atom": str(tr_atom_r),
        "tr_M_free": str(tr_free_r),
        "Q_beta_n_MeV": Q_beta_n_mev,
        "B_MeV": float(B),
        "n_atom_terms": atom_n_terms,
        "n_free_terms": free_n_terms,
        "use_closed_form": use_closed_form,
    }


def binding_observe_last(Z: int, N: int, *, dps: int = 50):
    """**Observe-LAST binding variant (DIAGNOSTIC — not a production closure).**

    Sibling to `binding_canonical` (observe-EARLY: the step-5 scalar collapse
    `B_pred = Q_β·(tr_free − tr_atom)`).  This variant carries the per-Wedderburn-
    block q-Reeb phase `θ_λ` to a τ-LAST collapse (step 9), per the observe-last
    reframe (`docs/audits/2026-06-17-singlet-channel-bsym-exploration.md` §6b/§6c):

        θ_λ^X = arccos(χ_λ^X/d_λ)        (|·|≤1, rotation channel)
              | arccosh(|χ_λ^X/d_λ|)     (growth channel)
        B_observe_last = Q_β · Σ_λ y_λ (θ_λ^free − θ_λ^atom)        [additive]

    **STATUS (read before consuming).** The additive collapse above is *refuted*
    as the binding-residual mechanism: small, negative, and SHRINKS with A,
    whereas the documented residual `Δ_λ(K)=B_AME/B_pred ≈ q₀^(10A−5)=q₀^(5(2A−1))`
    is large, positive, and GROWS with A.  A bounded additive phase sum cannot be
    geometric in A; the residual is a **per-object multiplicative q₀⁵** (one factor
    per nucleon + one per inter-nucleon bond), whose categorical derivation from
    the `W_free`/`W_atom` jet–crossing bookkeeping is OPEN (9b workplan H1;
    research-grade Subgoal-2 — must NOT be closed by a fit ansatz, Δ_λ gate).
    This function exposes the observe-last *carrier infrastructure* (the per-λ θ
    vector the canonical step-5 trace collapses), NOT a wired binding closure.
    `residual_law_*` is the EMPIRICAL near-match shown for reference only and is
    deliberately NOT applied to produce a binding number.

    NO FLOAT (owner ruling 2026-06-09): all mpmath at the 50-dps floor; values
    returned as full-precision decimal strings.
    """
    import mpmath as mp
    from reduced_block_kernel import chi_all_lambda_reduced_block
    from wedderburn_jones_markov import y_lambda_at
    from hecke_characters import specht_dim

    if mp.mp.dps < dps:
        mp.mp.dps = dps
    n = 3 * (Z + N)
    A = Z + N
    qb = mp.mpf(str(_Q_BETA_N))
    q0v = mp.mpf(str(q0))

    def _theta(chi, d):
        r = chi / d
        return mp.acos(r) if abs(r) <= 1 else mp.acosh(abs(r))

    y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, q0).items()}
    chi_atom = chi_all_lambda_reduced_block(
        atom_braid_word_3A(Z, N, include_inter=True), n)
    chi_free = chi_all_lambda_reduced_block(
        atom_braid_word_3A(Z, N, include_inter=False), n)
    parts = list(y.keys())
    tr_atom = mp.fsum(y[l] * chi_atom.get(l, mp.mpf(0)) for l in parts)
    tr_free = mp.fsum(y[l] * chi_free.get(l, mp.mpf(0)) for l in parts)
    B_pred = qb * (abs(tr_free) - abs(tr_atom))                 # observe-early

    dim = {l: mp.mpf(specht_dim(l)) for l in parts}
    th = {l: (_theta(chi_free.get(l, mp.mpf(0)), dim[l]),
              _theta(chi_atom.get(l, mp.mpf(0)), dim[l])) for l in parts}
    B_late = qb * mp.fsum(y[l] * (th[l][0] - th[l][1]) for l in parts)  # REFUTED

    resid_exp = 5 * (2 * A - 1)            # 10A−5 = per-object (A nucleons + A−1 bonds)
    return {
        "Z": Z, "N": N, "A": A, "n_strands": n,
        "Q_beta_n_MeV": str(qb),
        "B_pred_observe_early_MeV": str(B_pred),
        "B_observe_last_additive_MeV": str(B_late),    # refuted: small/neg/shrinks
        "per_lambda_theta": {str(list(l)): {"theta_free": str(th[l][0]),
                                            "theta_atom": str(th[l][1])}
                             for l in parts},
        "residual_law_exponent_10A_5": resid_exp,      # reference only (NOT applied)
        "residual_law_factor_q0pow": str(q0v ** resid_exp),
        "status": "DIAGNOSTIC: additive observe-last refuted; per-object q₀⁵ "
                  "closure OPEN (held); carrier infra for the 9b H1 derivation. "
                  "NOT a production binding closure.",
    }


if __name__ == "__main__":
    # AME 2020 binding-energy comparison targets imported from the
    # central codata_constants registry (validation-only; not CAL inputs).
    # Previously hardcoded inline: (2.22452, 8.481821, 7.71804, 28.295674);
    # the tritium value was a typo (correct AME 2020 = 8.481798). Now
    # loaded from `ame-2020-binding-energies.witness.json` via the
    # AME_B_*_MEV_VALIDATION constants (PR #1105).
    ATOMS = [
        ("D",    1, 1, float(AME_B_DEUTERON_MEV_VALIDATION)),
        ("T",    1, 2, float(AME_B_TRITIUM_MEV_VALIDATION)),
        ("3He",  2, 1, float(AME_B_HE3_MEV_VALIDATION)),
        ("4He",  2, 2, float(AME_B_HE4_MEV_VALIDATION)),
        ("6Li",  3, 3, 31.994526),
    ]
    print("=" * 100)
    print("BINDING via CANONICAL Jones-Markov trace "
          "(prop:categorical-mass-markov)")
    print(f"q₀ = {q0}, Q_β(n) = {float(_Q_BETA_N)} MeV (β-decay Q-value, CAL-3)")
    print("=" * 100)
    results = []
    print(f"  {'Atom':>6} {'A':>3} {'3A':>3} {'B_AME':>8} "
          f"{'|tr_atom|':>12} {'|tr_free|':>12} "
          f"{'B_pred':>10} {'|Δm/m|%':>9} {'time':>8}")
    print("  " + "-" * 96)
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        r = binding_canonical(Z, N, verbose=False)
        if r.get("status") != "solved":
            print(f"  {name:>6} {A:>3} {3*A:>3}  "
                  f"STATUS: {r.get('status')}: "
                  f"{r.get('error', '')[:60]}")
            results.append(r)
            continue
        tr_a = complex(r["tr_M_atom"].replace("(", "").replace(")", ""))
        tr_f = complex(r["tr_M_free"].replace("(", "").replace(")", ""))
        # Proton mass from codata_constants registry (CODATA 2022, full
        # precision); was hardcoded inline as 938.272.
        M_total = A * float(M_P_MEV_VALIDATION)
        dm = abs(r["B_MeV"] - B_AME) / M_total * 100
        print(f"  {name:>6} {A:>3} {3*A:>3} {B_AME:>8.3f} "
              f"{abs(tr_a):>12.6e} {abs(tr_f):>12.6e} "
              f"{r['B_MeV']:>+10.4f} {dm:>8.4f}%")
        results.append({**r, "atom": name, "B_AME_MeV": B_AME,
                         "delta_m_over_m_pct": dm})

    # Coerce sympy/mpmath fragments to JSON-serialisable types so
    # WitnessBuilder.save() (which does strict json.dumps) succeeds.
    safe_results = json.loads(json.dumps(results, default=str))
    builder = (
        WitnessBuilder("binding-canonical", engine="sympy+mpmath")
        .set_description(
            "Atom binding via the canonical Jones-Markov trace "
            "(Direction 1 of validity audit): matches the prop's "
            "explicit-values table tr_M(σ_0)=z, tr_M(σ_0σ_1)=z², "
            "tr_M(σ_0σ_1σ_0)=hz²+z. Replaces the Plancherel-"
            "weighted trace used in binding_3A and "
            "atom_markov_trace. Binding = Q_β(n)·(tr_M_free − "
            f"tr_M_atom) [SIGNED categorical difference; the double-"
            f"modulus |·|−|·| was a non-archimedean misuse] with "
            f"Q_β(n) = {float(_Q_BETA_N):.8f} MeV (free-"
            "neutron β-decay Q-value, CAL-3 calibration input — "
            "NOT the canonical E_0 = m_e/(q_0(q_0-1)) ≈ 4.186 MeV). "
            "DIAGNOSTIC ONLY: predicted B values are 5–40× smaller "
            "than AME because Q_β is the wrong energy scale; the "
            "primary canonical mass-prediction pipeline is "
            "canonical-mass-table-extended.witness.json. This "
            "witness is retained for the Direction 1 validity "
            "audit of the Jones-Markov trace itself."
        )
        .set_audit_only("docs/audits/categorical-vs-fitted-q-decay-ba.md")
        .add_parameter("q0", q0)
        .add_parameter("Q_beta_n_MeV", float(_Q_BETA_N))
        .add_data("results", safe_results)
    )
    out = builder.save()
    print(f"\nWitness: {out}")
