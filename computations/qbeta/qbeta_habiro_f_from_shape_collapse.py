#!/usr/bin/env python3
"""qbeta_habiro_f_from_shape_collapse.py — diagnostic: S(q) = Q_β/E_0
is the SDP-constraint object, NOT the ladder-normalization object.

FINDING (negative result, structurally informative).

The SHAPE-collapse audit doc
(`docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md`) states:

  T_β^Markov = S · 𝟙          (rank-1; A^T G^{-1} A = 1 symbolically)
  c_k(L2) = c_k(Markov)        (algebraic identity; Step 4 diagnostic)
  "c_k come from u_ladder Taylor of S(q) = Q_β(q) / E_0(q)"

This probe takes that statement literally: substitutes the closed forms

  Q_β(q)      = m_e · (2q + 1 − q²)·(q+1) / (2q³)     (1 < q < 1+√2)
  E_0(N=0)(q) = m_e / [q(q − 1)]
  E_0(tower)  = E_0(N=0) / (1 − ℏ_q²)

and Taylor-expands S(q) = Q_β/E_0 in u_ladder = b·ℏ_q² around q = 1.

VERDICT: S(q=1) = 0 for BOTH N=0 and tower variants — the (q-1) zero of
Q_β meets the 1/(q-1) pole of E_0 with the wrong residue alignment; the
quotient lands at the origin, not at 1. Consequently every Taylor
coefficient of S/S(1) is undefined and the "c_k from S Taylor" recipe
gives 0/0.

What this means STRUCTURALLY: the `S = Q_β/E_0` referenced in the audit
doc is the SDP-constraint scalar (its NUMERICAL value at q₀ is the
target 0.186893691886 the SDP solves for). It is NOT the ladder
normalization. Inspection of `qbeta_1ppq_achieved.py` confirms: the
actual ladder factors are

  Q_β = Q_A · cos(α_eff) · (1 − b²·ℏ⁴) · (1 + c_3·b³·ℏ⁶) · (1 + c_4·b⁴·ℏ⁸) · …

with Q_A and α_eff drawn from the operator-valued N=3 witness — i.e. the
ladder normalizes against `Q_A · cos(α_eff)`, NOT against `E_0`.

So the categorical f-construction needs the SYMBOLIC closed forms of
Q_A(q) and α(q) — eigenphase / amplitude quantities derived from the
SDP. Those are the missing pieces for the keystone, not the S(q) = Q_β/E_0
that the audit doc cited.

This probe is the read-only diagnostic that pins down the gap. It does
NOT fabricate a c_k value; it shows that the literal reading of the
audit doc's recipe is degenerate, and identifies the next sub-task:
locate / derive symbolic Q_A(q) and α(q).

Closed forms (per Agent-located audits + `derived_masses.py`):

  Q_β(q) = m_e · |q² − 2q − 1|·(q+1) / (2q³)
         = m_e · (2q + 1 − q²)·(q+1) / (2q³)   for 1 < q < 1+√2
  E_0(N=0)(q)   = m_e / [q(q − 1)]
  E_0(tower)(q) = E_0(N=0)(q) / (1 − ℏ_q²)

  ⇒ S(N=0)(q)   = (2q+1−q²)(q+1)(q−1) / (2q²)
                = (2q+1−q²)(q²−1)     / (2q²)
  ⇒ S(tower)(q) = S(N=0)(q) · (1 − ℏ_q²)

  u_ladder = b · ℏ_q² where b = √(q⁴+q²+1)/(q²+1).

This probe tries BOTH E_0 variants (N=0 and tower) and reports for each:

  • S(q) closed form (rational in q for both N=0 and tower variants)
  • S(q₀) numerical value (vs. audit-doc target 0.186893691886)
  • S(q=1) value — the diagnostic gate

**Diagnostic outcome (this probe demonstrates):** S(q=1) = 0 for BOTH
variants, so the Taylor expansion of S/S(1) around q=1 is degenerate
(0/0) and the c_k recipe cannot be evaluated. The proved c_2 = −1
(PR #1602) cannot be recovered from this S — which is the proof that
`S = Q_β/E_0` is the SDP-constraint scalar, NOT the ladder
normalization. The c_k must come from a different normalization
(see commit body for the actual ladder structure).
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
# Single sys.path insertion in the _path_bridge import above already adds
# `__file__.parent.parent` (= computations/), which is the
# same dir as `HERE.parent`. No second insertion needed for the
# `_precision` / `witness_base` imports below.

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "80")
os.environ.setdefault("QOU_OUTPUT_DPS", "60")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(80)
import mpmath as mp  # noqa: E402
mp.mp.dps = 80

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

Q0_MP_PIN = Q_50_DIGIT_STR
S_TARGET = "0.186893691885"  # per audit doc (12 digits)


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-habiro-f-from-shape-collapse",
        engine="python+sympy",
        start_time=t0,
    )
    builder.set_description(
        "Diagnostic: demonstrates that S = Q_β/E_0 is NOT the c_k ladder "
        "normalization, because S(q=1) = 0 for both N=0 and tower E_0 "
        "variants (Q_β·(q-1) zero meets E_0 1/(q-1) pole with wrong "
        "residue). Hence the 'c_k from u_ladder Taylor of S(q)' recipe of "
        "audit 2026-06-03-qbeta-markov-trace-shape-collapse.md is "
        "degenerate when S is interpreted as Q_β/E_0. The actual ladder "
        "uses Q_β/[Q_A · cos(α_eff)] from the operator-valued N=3 witness "
        "(see qbeta_1ppq_achieved.py). No fit, no CODATA residual — "
        "purely from the closed forms."
    )
    builder.set_content_block("prop:q-beta-categorical-precision-ladder")

    print("=" * 78)
    print(" Q_β HABIRO KEYSTONE — c_k from S(q) closed form (categorical route)")
    print("=" * 78)
    print()

    q = sp.Symbol("q", positive=True)
    eps = sp.Symbol("eps")  # q = 1 + eps
    N_ORDER = 9  # expand to eps^N_ORDER to read off c_2..c_8 from u^k=eps^(2k)

    # --- Q_β / m_e ----------------------------------------------------------
    # 1 < q < 1 + √2 ⇒ q² − 2q − 1 < 0 ⇒ |q² − 2q − 1| = 2q + 1 − q²
    Q_beta_over_me = (2 * q + 1 - q ** 2) * (q + 1) / (2 * q ** 3)

    # --- E_0 / m_e (two variants) -------------------------------------------
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0_N0_over_me = _qbeta_e0.order_zero_scaled(1, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    hbar_q_sq = (q - 1) ** 2 / q ** 2
    E0_tower_over_me = E0_N0_over_me / (1 - hbar_q_sq)

    # --- S(q) variants ------------------------------------------------------
    S_N0 = sp.cancel(Q_beta_over_me / E0_N0_over_me)
    S_tower = sp.cancel(Q_beta_over_me / E0_tower_over_me)

    # --- u_ladder = b · ℏ_q² ------------------------------------------------
    b_q = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
    u_ladder = sp.cancel(b_q * hbar_q_sq)

    print("  CLOSED FORMS")
    print(f"    S_N0(q)    = {sp.simplify(S_N0)}")
    print(f"    S_tower(q) = {sp.simplify(S_tower)}")
    print(f"    u_ladder   = {u_ladder}")
    print()

    # --- Numerical sanity at q₀ ---------------------------------------------
    q0 = mp.mpf(Q0_MP_PIN)
    target = mp.mpf(S_TARGET)
    S_N0_at_q0 = mp.mpf(str(sp.N(S_N0.subs(q, sp.Float(str(q0), 50)), 50)))
    S_tower_at_q0 = mp.mpf(str(sp.N(S_tower.subs(q, sp.Float(str(q0), 50)), 50)))
    print("  NUMERICAL SANITY at q₀")
    print(f"    S_N0(q₀)    = {mp.nstr(S_N0_at_q0, 15)}  "
          f"(rel-err vs target = "
          f"{mp.nstr(abs(S_N0_at_q0 - target) / target, 3)})")
    print(f"    S_tower(q₀) = {mp.nstr(S_tower_at_q0, 15)}  "
          f"(rel-err vs target = "
          f"{mp.nstr(abs(S_tower_at_q0 - target) / target, 3)})")
    print(f"    target      = {mp.nstr(target, 15)}")
    print()

    # --- Taylor expand each S in eps, then re-express in u_ladder ----------
    def extract_ck(S_expr: sp.Expr, variant_id: str, label: str) -> dict:
        """Expand S(q=1+eps) and u_ladder(q=1+eps) in eps; solve for
        c_k via S = 1 + Σ_{k≥2} c_k u_ladder^k.

        `variant_id` is an ASCII-safe stable identifier (e.g. "S_N0",
        "S_tower") used in assertion names; `label` is the human-readable
        formula displayed in the verdict and stored in `source`.
        """
        print(f"  ── {variant_id}: {label} ──")
        S_series = sp.series(S_expr.subs(q, 1 + eps), eps, 0, N_ORDER + 1).removeO()
        u_series = sp.series(u_ladder.subs(q, 1 + eps), eps, 0, N_ORDER + 1).removeO()
        S_poly = sp.Poly(sp.expand(S_series), eps)
        u_poly = sp.Poly(sp.expand(u_series), eps)

        # Leading order of u_ladder in eps
        u_coeffs = {d: u_poly.nth(d) for d in range(N_ORDER + 1)}
        u_lead_order = next(d for d in range(N_ORDER + 1) if u_coeffs[d] != 0)
        print(f"    u_ladder leading order in eps:  ε^{u_lead_order}")
        print(f"    u_ladder leading coefficient:   {u_coeffs[u_lead_order]}")

        # S leading order
        S_coeffs = {d: S_poly.nth(d) for d in range(N_ORDER + 1)}
        S_const = S_coeffs[0]
        print(f"    S(q=1) = {S_const}")

        # Normalised S/S(1) = 1 + c_2 u² + c_3 u³ + ...
        if S_const == 0:
            print("    S(q=1) = 0 — DIAGNOSTIC FINDING; "
                  "this S is not the ladder normalization.")
            return {
                "variant_id": variant_id,
                "variant": label,
                "S_at_qeq1": "0",
                "error": "S(q=1)=0",
                "diagnostic": (
                    "S(q=1) vanishes; Q_β · (q-1) zero meets E_0 1/(q-1) "
                    "pole with wrong residue, so Q_β/E_0 is not the ladder "
                    "normalization. Audit doc conflated SDP-constraint S "
                    "with ladder S."
                ),
            }
        # Inversion machinery only handles u_lead_order == 2 (the expected
        # u_ladder = b·ℏ² ∼ O(eps²) case). Bail out clearly otherwise.
        if u_lead_order != 2:
            print(f"    u_lead_order = {u_lead_order} ≠ 2 — "
                  "inversion parameterization is hard-coded for "
                  "u_lead_order == 2; bailing out.")
            return {
                "variant_id": variant_id,
                "variant": label,
                "S_at_qeq1": str(S_const),
                "u_lead_order_in_eps": int(u_lead_order),
                "error": "u-lead-order-not-2",
            }
        S_normed = sp.simplify(S_series / S_const)

        # Re-express in u_ladder: solve eps = eps(u_ladder) as a series.
        # For u_lead_order == 2 (u_ladder = b·ℏ² is O(eps²)), the inverse
        # has a half-integer expansion in u_sym; parameterise via
        # t = √u_sym so eps = c_1·t + c_2·t² + ... and match coefficients.
        t = sp.Symbol("t")
        c_syms = sp.symbols(f"c1:{N_ORDER + 1}")
        eps_of_t = sum(c_syms[i] * t ** (i + 1) for i in range(N_ORDER))

        u_in_t = sp.series(
            u_series.subs(eps, eps_of_t), t, 0, N_ORDER + 2
        ).removeO()
        # Match coefficients order by order
        u_in_t_expanded = sp.expand(u_in_t)
        eqs = []
        for d in range(1, N_ORDER + 1):
            coeff_d = u_in_t_expanded.coeff(t, d)
            wanted = 1 if d == u_lead_order else 0
            eqs.append(coeff_d - wanted)
        sol = sp.solve(eqs[:N_ORDER], c_syms[:N_ORDER], dict=True)
        if not sol:
            print(f"    inversion failed at order {N_ORDER}")
            return {"variant": label, "error": "inversion-failed"}
        sol = sol[0]
        eps_of_t_solved = eps_of_t.subs(sol)
        print(f"    eps(t) (t = √u_ladder) = "
              f"{sp.nsimplify(sp.series(eps_of_t_solved, t, 0, 4).removeO())} + ...")

        # Now S_normed(eps_of_t_solved) = 1 + c_2·t⁴ + c_3·t⁶ + ... (since
        # u_sym = t² ⇒ u_sym^k = t^{2k}).
        S_in_t = sp.series(
            S_normed.subs(eps, eps_of_t_solved), t, 0, 2 * (N_ORDER + 1)
        ).removeO()
        S_in_t = sp.expand(S_in_t)
        print(f"    S/S(1) in t = √u_ladder, low orders:")
        for d in range(0, 2 * N_ORDER + 1, 1):
            coef = S_in_t.coeff(t, d)
            if coef != 0:
                print(f"      t^{d}: {sp.nsimplify(coef, rational=False)}")

        # c_k = coefficient of u_ladder^k = t^{2k}
        c_k = {}
        for k in range(0, N_ORDER + 1):
            coef = sp.nsimplify(S_in_t.coeff(t, 2 * k), rational=False)
            c_k[k] = coef
            if k >= 1 and coef != 0:
                # also check intermediate odd t-orders should vanish
                pass
        # Report
        print(f"    c_2 = {c_k.get(2)}")
        print(f"    c_3 = {c_k.get(3)}")
        print(f"    c_4 = {c_k.get(4)}")
        print(f"    c_5 = {c_k.get(5)}")
        print(f"    c_6 = {c_k.get(6)}")
        print(f"    c_7 = {c_k.get(7)}")
        print(f"    c_8 = {c_k.get(8)}")

        # Check odd-t orders vanish (i.e. S is a series in u_ladder, not √u_ladder)
        odd_residue = sum(abs(S_in_t.coeff(t, 2 * k + 1))
                          for k in range(N_ORDER))
        odd_residue_num = float(sp.N(odd_residue, 20))
        print(f"    Σ |odd t-orders|  = {odd_residue_num:.6e}   "
              f"(0 ⇒ true u_ladder series)")

        return {
            "variant_id": variant_id,
            "variant": label,
            "S_at_qeq1": str(S_const),
            "c_k": {str(k): str(v) for k, v in c_k.items()},
            "odd_residue_in_t": float(odd_residue_num),
            "u_lead_order_in_eps": int(u_lead_order),
        }

    print("  TAYLOR EXTRACTION (c_k from u_ladder expansion)")
    print()
    res_N0 = extract_ck(S_N0, "S_N0", "(2q+1-q²)(q²-1)/(2q²)")
    print()
    res_tower = extract_ck(S_tower, "S_tower", "S_N0 · (1-ℏ_q²)")
    print()

    # --- Verdict ------------------------------------------------------------
    print("=" * 78)
    print(" VERDICT — diagnostic: S(q=1) = 0 for both Q_β/E_0 variants")
    print("=" * 78)
    print()
    print("  EXPECTED if S=Q_β/E_0 were the ladder normalization:")
    print("    S(q=1) = 1 and c_2 = -1 (PR #1602 / bar-even constraint).")
    print()
    print("  OBSERVED:")
    for res in (res_N0, res_tower):
        tag = f"{res['variant_id']} = {res['variant'][:30]}"
        S_at_1 = res.get("S_at_qeq1", "?")
        err = res.get("error")
        if err == "S(q=1)=0":
            print(f"  {tag:<40}  S(q=1) = 0  "
                  "(degenerate; not the ladder normalization)")
        elif err:
            print(f"  {tag:<40}  error: {err}")
        else:
            c2_str = res.get("c_k", {}).get("2", "?")
            print(f"  {tag:<40}  S(q=1) = {S_at_1}  "
                  f"c_2 = {c2_str}")
    print()
    print("  CONCLUSION: the `S = Q_β/E_0` of the SHAPE-collapse audit doc")
    print("  is the SDP-constraint scalar (numerical at q₀), not the ladder")
    print("  normalization. The categorical f-construction needs symbolic")
    print("  Q_A(q) and α(q) from the operator-valued N=3 witness.")
    print()

    builder.add_data("closed_forms", {
        "Q_beta_over_me": str(sp.simplify(Q_beta_over_me)),
        "E0_N0_over_me": str(sp.simplify(E0_N0_over_me)),
        "E0_tower_over_me": str(sp.simplify(E0_tower_over_me)),
        "S_N0": str(sp.simplify(S_N0)),
        "S_tower": str(sp.simplify(S_tower)),
        "u_ladder": str(u_ladder),
    })
    builder.add_data("numerical_sanity_at_q0", {
        "q_0": mp.nstr(q0, 50),
        "target_S_at_q0": mp.nstr(target, 15),
        "S_N0_at_q0": mp.nstr(S_N0_at_q0, 15),
        "S_tower_at_q0": mp.nstr(S_tower_at_q0, 15),
        "S_N0_rel_err": mp.nstr(abs(S_N0_at_q0 - target) / target, 5),
        "S_tower_rel_err": mp.nstr(abs(S_tower_at_q0 - target) / target, 5),
    })
    builder.add_data("S_N0_results", res_N0)
    builder.add_data("S_tower_results", res_tower)

    # Assertions — record the diagnostic POSITIVELY. The probe's job is to
    # demonstrate that S = Q_β/E_0 has S(q=1) = 0 for both E_0 variants,
    # which proves that S is NOT the ladder normalization. So each variant
    # asserts S(q=1) = 0 (passing if the diagnostic holds) rather than
    # c_2 = −1 (which would require S to be the correct normalization).
    for res in (res_N0, res_tower):
        if res.get("error") == "S(q=1)=0":
            S_at_1_num = 0.0
        else:
            S_at_1 = sp.sympify(res.get("S_at_qeq1", "0"))
            S_at_1_num = float(sp.N(S_at_1, 20))
        builder.add_assertion(
            f"{res['variant_id']}_S_at_qeq1_eq_zero",
            computed=abs(S_at_1_num),
            expected=0.0,
            tolerance=1e-15,
            source=(f"{res['variant_id']} = {res['variant']}: diagnostic "
                    "— S(q=1) should equal 0 (Q_β · (q-1) zero meets E_0 "
                    "1/(q-1) pole). Pass ⇒ confirms this S is the "
                    "SDP-constraint scalar, NOT the ladder normalization. "
                    "The categorical f-construction needs symbolic "
                    "Q_A(q) and α(q), not Q_β/E_0."),
        )

    # q0 anchor: `independent`, declared rather than inherited.

    # Measured, not assumed -- see the reason (bean qou-o922).

    builder.save({"q0Anchor": "independent",

            "q0AnchorReason": (

                'Reads no substrate value. PROVED by running this producer under'

                'QOU_Q0_ANCHOR=muon and =proton and diffing the emitted witness:'

                'the only non-ephemeral leaves that differ are q0Anchor and'

                'q0Value THEMSELVES -- every substantive field is byte-identical,'

                'so the pin changes the label and nothing else. Its previous'

                '`muon` label was therefore a false claim that this producer'

                'computed at that anchor. `independent` is the honest'

                'disposition; a q0_anchor_manifest entry would be the WRONG fix,'

                'promoting a false claim into a declared one. Bean qou-o922,'

                'class (ii).'

            )})
    print(f"\n  Witness: qbeta-habiro-f-from-shape-collapse.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
