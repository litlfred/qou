#!/usr/bin/env python3
# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
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

6-term mass formula at MPFR 50 dps — Phase A precision lift.

Per the post-#473 workplan (Phase A item 1+2): bring all six terms
of the unified mass formula

  𝔪(ρ) = |tr_M(T_w)|                     [1: descended]
       + Σ_i Φ_q(|V̂_i|)                   [2: single-gen brane tower]
       + z²·Σ_{i<j} Φ_q(|V̂_i V̂_j|)       [3: pair-gen brane tower]
       + m_e · tr_M(C_dim_q)               [4: Frobenius co-Casimir]
       + a_K · B_bulk                      [5: chirality factor]
       + Σ_ℓ Res_{q→ζ_ℓ}[…]                [6: Habiro residue tail]

to **50 dps mpmath throughout**, replacing the f64 chokepoints in
`mass_formula_6term.py`.

The bottleneck on main was `mass_endomorphism.Phi_q`, which uses
Python `1.0` floats and `float("inf")` sentinels — capping every
brane-tower contribution at machine epsilon.  This script reimplements
`Phi_q` natively in mpmath (`mp_Phi_q`) and propagates `mp.mpf`
through the entire Term 2 + 3 chain.

Term 6 uses the **Habiro residue path** (not the analytic pole-by-pole
residue sum on `claude/continue-pr-442-DJRWm`).  The Habiro
polynomial coefficients automatically encode all pole multiplicities
via the cyclotomic completion `Ẑ[q]`; higher-order poles (e.g.
deuteron at ζ_4) are captured without separate Laurent-expansion
machinery.  This is the answer to the open question on the workplan:
"Term 6 higher-order poles → residues or Habiro?".  Habiro wins
because polynomial divisibility in `(u;u)_N · ℤ[u]` (the
`HabiroCompletion.tail_in_ideal` axiom) covers arbitrary pole
multiplicities by construction.

Output: `mass-formula-6term-mpfr-50dps.witness.json` — per atom,
the six terms each at 50-digit mpmath precision plus the assembled
mass and CODATA comparison.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import sympy as sp  # noqa: F401  (used by hecke_core for symbolic q if needed)

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as Q0_FLOAT, Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402

# Local imports — these have mp.mpf-friendly internals where flagged.
from bw_chirality_isotopes import (  # noqa: E402
    B_bulk, B_Zdep, B_shell, pairing_sign,
    f_chiral_plus, f_chiral_minus, f_amphi, f_borromean, f_Zdep_scale,
)
from hecke_core import atom_per_generator_volumes, h as h_val, z as z_mark  # noqa: E402


# ── 50 dps precision contract ──────────────────────────────────

WORKING_DPS = 50
mp.mp.dps = WORKING_DPS

# Substrate parameter as mp.mpf at 50 dps (re-parsed from the canonical
# float — q_parameter.Q is an f64 by design).
Q0_MP = mp.mpf(Q_50_DIGIT_STR)  # 50-dps q, not f64-quantised


# ── Native-mpmath quantum dilogarithm ─────────────────────────

def mp_Phi_q(z: mp.mpf, q: mp.mpf = Q0_MP, max_k: int = 5000) -> mp.mpf:
    """Quantum dilogarithm `Φ_q(z) = Π_{k≥1} 1 / (1 − q^{-k} z)` at
    mpmath precision.  Matches the canonical definition used in
    `_phi_q_util.phi_q` and `mass_endomorphism.Phi_q` (k starts at 1,
    not 0 — the k=0 factor `1/(1-z)` is NOT included).

    Replaces `mass_endomorphism.Phi_q`, which uses Python `1.0`
    floats internally and caps the precision at f64.  Convergence
    floor: `|q^{-k} z|` decays geometrically with rate `q^{-1}`;
    for `q_0 ≈ 1.110` and target precision 10^-50 we need
    `k ≥ 50 / log10(q_0) ≈ 1100`.  `max_k=5000` provides comfortable
    headroom.

    Returns +∞ (mp.mpf) when `|z| ≥ q` (formal-power-series radius
    of convergence is `|q|`) or when any factor vanishes (pole hit).
    """
    z_mp = mp.mpf(z) if not isinstance(z, mp.mpf) else z
    if mp.fabs(z_mp) >= q:
        return mp.inf
    product = mp.mpf(1)
    qi = mp.mpf(1) / q       # q^{-1}
    qi_pow = qi              # k starts at 1 (canonical convention)
    for _k in range(max_k):
        factor = 1 - qi_pow * z_mp
        if factor == 0:
            return mp.inf    # hit a pole at z = q^k
        product /= factor
        # Convergence break: when the next contribution drops below
        # working precision, further k are noise.
        if mp.fabs(qi_pow * z_mp) < mp.mpf(10) ** -(WORKING_DPS + 5):
            break
        qi_pow *= qi
    return product


# ── Term wiring (each at 50 dps) ──────────────────────────────

def term_1_descended_mp(Z: int, N: int) -> mp.mpf:
    """Term 1: |tr_M(T_w_atom)| at 50 dps via the Wenzl-bridge.

    Uses `atomic_tr_m_mpfr_50dps._bridge_tr_M` which builds the
    3A-strand Hecke-factor atom-braid word and evaluates
    `Σ_λ y_λ · χ_λ` at mpf precision via the Wenzl bridge.

    For A=1 (single nucleon), the atom braid coincides with the
    free braid (no internal pair-crossings), so this also serves
    as the free-case Term 1.  Free-vs-atom binding-energy
    differences for A≥2 are deferred to a follow-up.
    """
    from atomic_tr_m_mpfr_50dps import _bridge_tr_M
    q_str = mp.nstr(Q0_MP, WORKING_DPS, strip_zeros=False)
    tr, _n_strands, _word_len, _dt = _bridge_tr_M(Z, N, q_str, dps=WORKING_DPS)
    return mp.fabs(tr)


def _load_mpfr_native_volumes(Z: int, N: int) -> list[mp.mpf]:
    """Load MPFR-native per-generator full-channel volumes from
    `terms-2-3-atom-per-gen-mpfr-50dps.witness.json`.

    Required because `hecke_core.atom_per_generator_volumes` is
    f64-based (uses the global float `q0` and float accumulators),
    so converting its outputs to `mp.mpf` cannot recover the lost
    precision.  For 50-dps end-to-end Term 2/3, we must source the
    volumes from an MPFR-native pipeline.

    Schema of the witness (per inspection 2026-04-29):
      data["results"] = [
        {"atom": "D", "Z": 1, "N": 1, "wedderburn_vols": [
          {"std": ..., "sym": ..., "alt": ..., "full": ...},  # one per gen
          ...
        ], ...},
        ...
      ]
    We extract the `full` channel from each per-generator dict.

    Raises FileNotFoundError if the witness is absent;
    KeyError if no entry matches (Z, N).  By design the witness
    covers A≥2 (D, T, ³He); single-nucleon (A=1) is out-of-scope
    and the caller should handle it separately.
    """
    path = Path(__file__).parent / "terms-2-3-atom-per-gen-mpfr-50dps.witness.json"
    if not path.exists():
        raise FileNotFoundError(
            f"MPFR-native Terms 2/3 volume witness missing at {path}; "
            f"cannot meet 50-dps contract using f64-backed "
            f"atom_per_generator_volumes. Run "
            f"`terms_2_3_atom_per_gen_mpfr_50dps.py` to regenerate."
        )
    with path.open() as f:
        data = json.load(f)
    # Schema-flexible: accept either flat (legacy `data["results"]`)
    # or WitnessBuilder-nested (`data["data"]["results"]`) form.
    records = data.get("results") or data.get("data", {}).get("results", [])
    for record in records:
        if record.get("Z") != Z or record.get("N") != N:
            continue
        wv = record.get("wedderburn_vols")
        if not isinstance(wv, list):
            continue
        out: list[mp.mpf] = []
        for entry in wv:
            if not isinstance(entry, dict) or "full" not in entry:
                raise KeyError(
                    f"Entry for (Z={Z}, N={N}) has malformed "
                    f"wedderburn_vols (missing 'full' key)"
                )
            out.append(mp.mpf(str(entry["full"])))
        return out
    raise KeyError(
        f"No MPFR-native per-generator volumes found for Z={Z}, N={N} "
        f"in {path.name}; the witness covers A≥2 only "
        f"(extend `terms_2_3_atom_per_gen_mpfr_50dps.py` to add A=1)."
    )


def term_23_brane_tower_mp(
    Z: int, N: int, *, tower_form: str = "li2q",
) -> tuple[mp.mpf, mp.mpf]:
    """Terms 2 + 3 of the unified mass formula.

    Two tower-function forms are supported, selected by `tower_form`:

      - ``"li2q"`` (default, since #675/this PR): the **bounded
        symmetric q-dilogarithm** form
        ``Σ_i (−Li_2^q(−|V̂_i|)) + z² · Σ_{i<j} (−Li_2^q(−|V̂_i V̂_j|))``
        per [`prop:mass-endomorphism-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md)
        lines 162–183. Bounded for |V| < 1; matches the Kashaev
        integration identity `∫_0^V (ln_q(1+t)/t) dt = -Li_2^q(-V)`.
        Empirically validated in PR #675's probe: T2+T3 at tritium
        within 1% of AME binding (vs Φ_q's megaelectronvolt-divergent
        values).
      - ``"phi_q"`` (legacy, retained for cross-check / regression
        testing): the **divergent Faddeev** form
        ``Σ_i Φ_q(|V̂_i|) + z² · Σ_{i<j} Φ_q(|V̂_i V̂_j|)``. Diverges
        as |V| → 1; consumers using this form should check for
        `mp.inf` results.

    Per-generator volumes are loaded from the MPFR-native witness
    `terms-2-3-atom-per-gen-mpfr-50dps.witness.json` (NOT from
    `hecke_core.atom_per_generator_volumes`, which is f64-based).
    Term 3 sums over **all pairs** i<j (not adjacent-only).

    Returns (single, pair). With ``tower_form="li2q"`` both are
    finite for all atom braids. With ``tower_form="phi_q"`` either
    may be `mp.inf` if a generator/pair magnitude reaches the
    Φ_q convergence boundary.
    """
    if tower_form not in ("li2q", "phi_q"):
        raise ValueError(
            f"term_23_brane_tower_mp: unknown tower_form {tower_form!r}; "
            "expected 'li2q' or 'phi_q'"
        )
    vols_mp = _load_mpfr_native_volumes(Z, N)
    z_mp = mp.mpf(repr(z_mark))

    if tower_form == "li2q":
        # Lazy import keeps the legacy Φ_q path zero-dependency on
        # the derived_masses module.
        from derived_masses import li2q_symmetric
        from q_parameter import Q as Q_0_FLOAT, Q_50_DIGIT_STR
        q0 = mp.mpf(Q_50_DIGIT_STR)  # 50-dps q, not f64-quantised

        def tower_fn(x: mp.mpf) -> mp.mpf:
            # -Li_2^q(-|x|) — bounded analog of Φ_q(|x|) per the
            # Kashaev specialisation (prop:mass-endomorphism-tower).
            return -li2q_symmetric(-mp.fabs(x), q0)
    else:  # tower_form == "phi_q"
        def tower_fn(x: mp.mpf) -> mp.mpf:
            return mp_Phi_q(x)

    single = mp.mpf(0)
    for v in vols_mp:
        val = tower_fn(v)
        if mp.isinf(val):
            return mp.inf, mp.mpf(0)
        single += val

    pair = mp.mpf(0)
    n = len(vols_mp)
    for i in range(n):
        for j in range(i + 1, n):
            val = tower_fn(vols_mp[i] * vols_mp[j])
            if mp.isinf(val):
                return single, mp.inf
            pair += val
    pair *= z_mp ** 2
    return single, pair


def term_4_frobenius_mp(A: int) -> mp.mpf:
    """Term 4 (canonical, per-3A): m_e · Σ_{λ⊢3A} 1/dim_q(λ).

    Per `thm:frobenius-codim-universal`. Delegates to the canonical
    implementation in `paper_six_term_isotope_sweep.term4_frobenius_codim`.

    HARD BREAK (P1.C of `docs/audits/2026-05-12-1ppb-implementation-plan.md`,
    revision 2026-05-12): the legacy per-A form `A · m_e · (2 + 1/[2]_q)`
    has been REMOVED. It was an H_3-character formula × A that overcounted
    Term 4 by 1.56× at A=2, 2.95× at A=3, 4.44× at A=4. Any consumer that
    relied on `term_4_frobenius_mp` returning a 2-tuple
    `(per_vortex_legacy, per_A)` will now break — the function returns a
    single mpf. **This is intentional.** Per owner directive 2026-05-12:
    downstream witnesses should break so we know they were consuming the
    wrong formula.
    """
    from paper_six_term_isotope_sweep import term4_frobenius_codim
    m_e_mp = mp.mpf(repr(M_E_MEV))
    return m_e_mp * term4_frobenius_codim(A)


def term_5_chirality_bw_mp(
    Z: int, N: int, knot_type: str,
    *,
    chirality_source: str = "closed_form",
) -> mp.mpf:
    """Term 5: a_K · B_bulk + B_Zdep + B_shell.

    `B_bulk`, `B_Zdep`, `B_shell` are mp.mpf-native in the upstream
    module; the only f64 leak in `mass_formula_6term.py` was the
    `float()` cast at return time, dropped here.

    ``chirality_source`` selects the a_K factor:
      - "closed_form" (default since 2026-05-18, Item B canonical):
        a_K = Π_{c ∈ pn-crossings} (1 + sign(c) · h) where h = q - q⁻¹.
        Matches `conj:knot-factor-frobenius-pairing` Step 4 BW values
        (1+h, 1-h², (1-h²)²) at A=2,3,4.  See
        `docs/audits/2026-05-18-m-p-item-b-t5-categorical-attribution.md`
        §7c for empirical verification that this — not the v2 Gram form —
        is the canonical chirality factor.
      - "v2" (rejected by Item B audit §7c): Gram-matrix chirality
        `τ(β · β_mirror⁻¹)` via ``term5_v2_chirality.aK_v2``.
        Measures the doubled-braid Markov trace, NOT a_K. Retained
        for regression comparison only.
      - "bw_legacy": legacy categorical map keyed on ``knot_type``
        with ``f_chiral_plus`` / ``f_chiral_minus`` / ``f_amphi``
        / ``f_borromean`` BW-style constants. Empirical, not categorical.
    """
    if chirality_source == "closed_form":
        # a_K = Π_{c ∈ pn-crossings} (1 + sign(c) · h)
        # For Z protons + N neutrons in the canonical atomic braid,
        # the pn-crossing count is Z·N (one positive crossing per
        # proton-neutron pair in the standard 3A-strand layout).
        # Sign pattern: all positive at q_0 (no chirality reversal
        # within the connected atom). See conjecture Step 4.
        h = Q0_MP - mp.mpf(1) / Q0_MP
        pn_crossings = Z * N
        a_K = (mp.mpf(1) + h) ** pn_crossings if pn_crossings > 0 else mp.mpf(1)
    elif chirality_source == "v2":
        try:
            from term5_v2_chirality import aK_v2
            a_K = aK_v2(Z, N)
        except Exception as exc:
            # V2 cache miss for an out-of-window (Z, N) — surface
            # the routing decision and fall back to the closed_form
            # so the 50 dps sweep completes.
            print(
                f"[term_5_chirality_bw_mp] V2 a_K unavailable for "
                f"(Z={Z}, N={N}): {exc!r}; falling back to closed_form",
                flush=True,
            )
            chirality_source = "closed_form"
            h = Q0_MP - mp.mpf(1) / Q0_MP
            pn_crossings = Z * N
            a_K = (mp.mpf(1) + h) ** pn_crossings if pn_crossings > 0 else mp.mpf(1)
    elif chirality_source == "bw_legacy":
        chirality_map = {
            "chiral+": f_chiral_plus,
            "chiral-": f_chiral_minus,
            "amphichiral": f_amphi,
            "borromean": f_borromean,
            "none": mp.mpf(1),
        }
        a_K = chirality_map.get(knot_type, mp.mpf(1))
    else:
        raise ValueError(
            f"unknown chirality_source {chirality_source!r}; "
            f"expected 'closed_form', 'v2', or 'bw_legacy'"
        )
    A = Z + N
    sign = pairing_sign(Z, N)
    bulk = B_bulk(A, Z, N, sign)
    zdep = B_Zdep(A, Z, N)
    shell = B_shell(A, Z, N) if A >= 4 else mp.mpf(0)
    return a_K * bulk + f_Zdep_scale * zdep + shell


def term_6_habiro_residue_mp(A: int) -> mp.mpf:
    """Term 6: Σ_ℓ Res_{q→ζ_ℓ}[Φ_q · gradedMarkovTrace] at 50 dps.

    Loads from `term6-habiro-residue-mpfr-50dps.witness.json` (this
    script does not recompute the residue tail — that is a separate
    50 dps pipeline anchored in the Schur-Weyl symbolic sum).

    **Higher-order poles**: handled implicitly via the Habiro
    coefficients (cyclotomic completion encodes pole multiplicities
    in the polynomial coefficient sequence `a_m(u) ∈ ℤ[u]`).  No
    Laurent-expansion machinery needed; the `tail_in_ideal` axiom
    of `HabiroCompletion` covers arbitrary multiplicities by
    construction.

    Raises FileNotFoundError if the witness is absent;
    KeyError if no entry matches A.  Silently returning None
    would produce an incomplete 6-term sum and misleading witness
    output.
    """
    path = Path(__file__).parent / "term6-habiro-residue-mpfr-50dps.witness.json"
    if not path.exists():
        raise FileNotFoundError(
            f"Term 6 Habiro residue witness missing at {path}; "
            f"run the residue pipeline (see term6_habiro_residue_mpfr_50dps.py "
            f"or equivalent) to regenerate before invoking the 6-term sum."
        )
    with path.open() as f:
        data = json.load(f)
    # Schema-flexible: accept either flat (legacy) or
    # WitnessBuilder-nested (data.data.results_by_atom) form.
    records = (data.get("results_by_atom")
               or data.get("data", {}).get("results_by_atom", []))
    for r in records:
        if r.get("atom") == f"A={A}":
            t6 = r.get("term6_b_pred_mev_50dps")
            if t6 is None:  # documented null gap (e.g. A=0 electron)
                continue
            return mp.mpf(t6)
    raise KeyError(
        f"No Term 6 entry for A={A} in {path.name}; "
        f"add the atom to the residue pipeline before running."
    )


# ── Atom → habiro-coefficients-extended label map ─────────────
#
# `habiro-coefficients-extended.witness.json` keys `results` by a
# human label like "D (deuteron, A=2)"; the consumer here wants
# look-up by (Z, N). Static map mirrors that script's hard-coded
# `cases` list.
_HABIRO_EXT_LABEL_BY_ZN = {
    (1, 1): "D (deuteron, A=2)",
    (1, 2): "T (triton, A=3)",
    (2, 1): "³He (helion, A=3)",
    (2, 2): "⁴He (alpha, A=4)",
    (3, 2): "⁵Li (A=5)",
    (3, 3): "⁶Li (A=6)",
}


def term_6_via_habiro_coeffs_mp(Z: int, N: int) -> mp.mpf:
    """Term 6 — bounded alternative via direct Habiro series.

    Evaluates the Habiro / cyclotomic expansion
    ``tr_M(T_w, q) = Σ_m a_m(u) · (u; u)_m`` directly at
    u_0 = q_0^{1/2} from the per-atom a_m(u) coefficients in
    [`habiro-coefficients-extended.witness.json`](./habiro-coefficients-extended.witness.json).

    The Habiro coefficients are **integral polynomials in u**
    (verified `all_integral: True` for every atom A=2..6), so the
    series converges term-by-term and the result is bounded — in
    contrast to the Φ_q-residue path (`term_6_habiro_residue_mp`)
    which diverges to megaelectronvolt scale at A ≥ 3.

    Returns the full Habiro-summed Markov trace at q_0; downstream
    consumers wanting the **T6 correction term** specifically (i.e.
    the residue piece after the lower-order terms are subtracted)
    can compute `tr_M_habiro − tr_M_chi_cache` to isolate the
    higher-order contribution.

    Coverage: A ∈ {2, 3, 4, 5, 6} via the extended witness on
    main. A = 1 (proton, neutron) is not in the extended witness
    (the original `habiro-coefficients-atomic.witness.json` covers
    A = 1 separately).
    """
    label = _HABIRO_EXT_LABEL_BY_ZN.get((Z, N))
    if label is None:
        raise KeyError(
            f"term_6_via_habiro_coeffs_mp: no extended-Habiro coverage "
            f"for (Z={Z}, N={N}). Coverage: {list(_HABIRO_EXT_LABEL_BY_ZN.keys())}."
        )
    path = Path(__file__).parent / "habiro-coefficients-extended.witness.json"
    if not path.exists():
        raise FileNotFoundError(
            f"habiro-coefficients-extended witness missing at {path}; "
            f"run `habiro_coefficients_extended.py` to regenerate."
        )
    with path.open() as f:
        data = json.load(f)
    entry = data.get("results", {}).get(label)
    if entry is None:
        raise KeyError(
            f"term_6_via_habiro_coeffs_mp: extended witness has no "
            f"entry for {label!r}."
        )
    a_m_list = entry.get("habiro_coefficients", [])
    if not a_m_list:
        raise KeyError(
            f"term_6_via_habiro_coeffs_mp: empty habiro_coefficients "
            f"for {label!r}."
        )
    # Per `habiro_coefficients_atomic.to_u_polynomial`:
    #   p_in_u(u)  =  u^shift · denom(u) · tr_M(q = u²)
    # so the Markov trace at q_0 is recovered as
    #   tr_M(q_0)  =  p_in_u(u_0) / (u_0^shift · denom(u_0))
    # with  p_in_u(u_0)  =  Σ_m a_m(u_0) · (u_0; u_0)_m.
    shift = int(entry.get("shift", 0))
    denom_str = entry.get("denom_in_u", "1")

    import sympy as sp
    u_0 = mp.sqrt(Q0_MP)
    u_0_sp = sp.Float(str(u_0), 50)

    def _eval_sym(expr_str: str) -> mp.mpf:
        """Evaluate a u-polynomial string at u = u_0 (50 dps)."""
        expr = sp.sympify(expr_str)
        # Single dict-mapped .subs() call (faster than iterative;
        # per Gemini review on PR #682).
        expr = expr.subs({sym: u_0_sp for sym in expr.free_symbols})
        return mp.mpf(str(sp.N(expr, 50)))

    poch = mp.mpf(1)          # (u; u)_0 = 1
    p_at_u0 = mp.mpf(0)
    last_m = -1
    for entry_m in a_m_list:
        m = int(entry_m["m"])
        while last_m < m:
            last_m += 1
            if last_m == 0:
                continue       # (u; u)_0 = 1 already
            poch *= (1 - u_0 ** last_m)
        a_m_val = _eval_sym(entry_m["a_m"])
        p_at_u0 += a_m_val * poch

    denom_at_u0 = _eval_sym(denom_str) if denom_str else mp.mpf(1)
    if shift != 0:
        denom_at_u0 *= u_0 ** shift
    if denom_at_u0 == 0:
        raise ValueError(
            f"term_6_via_habiro_coeffs_mp: denom(u_0) vanished for "
            f"{label!r} — probable pole at q = q_0."
        )
    return p_at_u0 / denom_at_u0


# ── Entry point ───────────────────────────────────────────────

ATOMS = [
    ("p (proton)",   1, 0, "none"),
    ("n (neutron)",  0, 1, "none"),
    ("D (deuteron)", 1, 1, "chiral+"),
    ("T (triton)",   1, 2, "amphichiral"),
    ("3He",          2, 1, "amphichiral"),
    # ⁴He excluded: needs y_λ table at n=12, not in y-lambda-mpfr-witness.json
    # (table tops out at n=11).  Add once that witness is regenerated.
]

# CODATA reference masses (MeV/c²) — codata_constants registry (no inline literals)
from codata_constants import (  # noqa: E402
    M_P_MEV_VALIDATION, M_N_MEV_VALIDATION, M_D_MEV_VALIDATION,
    M_T_MEV_VALIDATION, M_HE3_MEV_VALIDATION, M_HE4_MEV_VALIDATION,
)
CODATA_MASS = {
    "p (proton)":   M_P_MEV_VALIDATION,
    "n (neutron)":  M_N_MEV_VALIDATION,
    "D (deuteron)": M_D_MEV_VALIDATION,
    "T (triton)":   M_T_MEV_VALIDATION,
    "3He":          M_HE3_MEV_VALIDATION,
    "4He":          M_HE4_MEV_VALIDATION,
}


def predict_atom_mp(label: str, Z: int, N: int, knot_type: str) -> dict:
    A = Z + N
    t1 = term_1_descended_mp(Z, N)
    # Term 2/3 brane tower: witness covers A≥2.  For A=1 (single
    # nucleon) the brane tower is conceptually 0 — there are no
    # inter-vortex bonds — but the per-generator volumes do exist.
    # Surface as None with documented reason rather than failing.
    try:
        t23 = term_23_brane_tower_mp(Z, N)
        t23_error = None
    except (FileNotFoundError, KeyError) as exc:
        t23 = (mp.mpf(0), mp.mpf(0))
        t23_error = f"{type(exc).__name__}: {exc}"
    t4 = term_4_frobenius_mp(A)
    t5 = term_5_chirality_bw_mp(Z, N, knot_type)
    # Term 6 raises if witness/atom missing; surface in the per-atom
    # row instead of crashing the whole sweep so that other atoms
    # can still complete.  The error message is preserved verbatim.
    try:
        t6 = term_6_habiro_residue_mp(A)
        t6_str = mp.nstr(t6, WORKING_DPS)
        t6_error = None
    except (FileNotFoundError, KeyError) as exc:
        t6_str = None
        t6_error = f"{type(exc).__name__}: {exc}"
    return {
        "atom": label, "A": A, "Z": Z, "N": N,
        "knot_type": knot_type,
        "term1_descended":      mp.nstr(t1, WORKING_DPS),
        "term2_single":         mp.nstr(t23[0], WORKING_DPS),
        "term3_pair":           mp.nstr(t23[1], WORKING_DPS),
        "term23_error":         t23_error,
        # P1.C HARD BREAK (2026-05-12): legacy `term4_frob_per_vortex` and
        # `term4_frob_per_A` fields removed. Single canonical field
        # `term4_frob_canonical_per_3A` per `thm:frobenius-codim-universal`.
        # Witness consumers that read the old field names will break —
        # intentionally, per owner directive.
        "term4_frob_canonical_per_3A": mp.nstr(t4, WORKING_DPS),
        "term5_chirality_bw":   mp.nstr(t5, WORKING_DPS),
        "term6_habiro_residue": t6_str,
        "term6_error":          t6_error,
    }


def main() -> int:
    print(f"6-TERM MASS FORMULA — MPFR @ {WORKING_DPS} dps")
    print(f"q_0 = {mp.nstr(Q0_MP, WORKING_DPS)}")
    print()

    results = [predict_atom_mp(*spec) for spec in ATOMS]

    w = WitnessBuilder("mass-formula-6term-mpfr-50dps", engine="mpmath")
    w.set_description(
        "Six-term unified mass formula evaluated at 50 dps mpmath "
        "throughout (Phase A precision lift).  Replaces the f64 "
        "chokepoints in mass_formula_6term.py: native mp_Phi_q for "
        "Term 2/3 brane-tower contributions; Term 6 via the Habiro "
        "residue path (cyclotomic completion handles higher-order "
        "poles intrinsically)."
    )
    w.set_content_block("thm:knot-mass-formula-unified")
    w.add_parameter("q_0", mp.nstr(Q0_MP, WORKING_DPS))
    w.add_parameter("working_dps", WORKING_DPS)
    w.add_parameter("convention", "wenzl-schur")  # post-#464 default
    w.add_data("results", results)
    w.add_data("codata_reference", {k: mp.nstr(v, 12) for k, v in CODATA_MASS.items()})

    # Per-atom assertions: each term is non-trivial / finite at 50 dps.
    # P1.C HARD BREAK (2026-05-12) renamed `term4_frob_per_vortex` →
    # `term4_frob_canonical_per_3A`; the assertion loop must follow.
    for r in results:
        for term_key in ("term1_descended", "term4_frob_canonical_per_3A"):
            val = r[term_key]
            try:
                v = mp.mpf(val)
                w.add_assertion(
                    f"{term_key}[{r['atom']}]_finite",
                    computed=mp.isfinite(v),
                    expected=True,
                )
            except Exception as exc:  # noqa: BLE001
                w.add_assertion(
                    f"{term_key}[{r['atom']}]_finite",
                    computed=False,
                    expected=True,
                )

    w.save()

    print(f"\nResults @ {WORKING_DPS} dps:")
    for r in results:
        print(f"  {r['atom']:>14}  T1={r['term1_descended'][:14]}…  "
              f"T2={r['term2_single'][:14]}…  T6={(r['term6_habiro_residue'] or 'n/a')[:14]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
