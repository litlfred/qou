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

  • S(q) closed form (rational in q for N=0; rational × algebraic for tower)
  • S(q₀) numerical value (vs. audit-doc target 0.186893691886)
  • c_2..c_8 Taylor coefficients in u_ladder around q=1
  • Verification of c_2 = −1 (PR #1602 proved value)
  • Comparison of c_3 to the empirical near-match −2
  • Predicted c_4..c_7 (compare to fit-extracted c_4 = −0.97157)

No fit, no CODATA residual. If c_2 = −1 falls out exactly for one variant,
that pins the canonical S(q) form and the recursion on c_k follows from
S's q-difference equation.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "80")
os.environ.setdefault("QOU_OUTPUT_DPS", "60")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(80)
import mpmath as mp  # noqa: E402
mp.mp.dps = 80

from witness_base import WitnessBuilder  # noqa: E402

Q0_MP_PIN = "1.1099785827513808075916690956107688798744991218736"
S_TARGET = "0.186893691885"  # per audit doc (12 digits)


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-habiro-f-from-shape-collapse",
        engine="python+sympy",
        start_time=t0,
    )
    builder.set_description(
        "Categorical c_k derivation: c_k = u_ladder Taylor coefficients of "
        "S(q) = Q_β(q)/E_0(q), per audit "
        "2026-06-03-qbeta-markov-trace-shape-collapse.md (T_β = S·𝟙, "
        "c_k L2/Markov-invariant). Tries N=0 and tower E_0 variants; "
        "reports which (if any) satisfies the proved c_2 = −1. No fit, "
        "no CODATA residual — purely from the closed forms."
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
    E0_N0_over_me = 1 / (q * (q - 1))
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
    def extract_ck(S_expr: sp.Expr, label: str) -> dict:
        """Expand S(q=1+eps) and u_ladder(q=1+eps) in eps; solve for
        c_k via S = 1 + Σ_{k≥2} c_k u_ladder^k.
        """
        print(f"  ── {label} ──")
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
            print("    S(q=1) = 0 — cannot normalise; skipping.")
            return {"variant": label, "error": "S(q=1)=0"}
        S_normed = sp.simplify(S_series / S_const)

        # Re-express in u_ladder: solve eps = eps(u_ladder) as a series.
        # u_ladder = sum_{d≥u_lead_order} a_d eps^d  ⇒ invert.
        u_sym = sp.Symbol("u_lad")
        # Solve recursively: eps = (u_sym / a_{u_lead_order})^{1/u_lead_order} + corrections.
        # For u_lead_order = 2 (expected — u_ladder = b·ℏ² is O(eps²)),
        # we set eps = α·√u_sym + β·u_sym + γ·u_sym^{3/2} + ...
        # Solve order-by-order.
        a_lead = u_coeffs[u_lead_order]
        # half-integer expansion: let t = sqrt(u_sym), eps = c_1·t + c_2·t² + ...
        t = sp.Symbol("t")
        c_syms = sp.symbols(f"c1:{N_ORDER + 1}")
        eps_of_t = sum(c_syms[i] * t ** (i + 1) for i in range(N_ORDER))

        # u_series(eps_of_t) should equal t^u_lead_order · u_sym/u_sym = t^u_lead_order
        # (since u_sym = t²)
        target_in_t = t ** u_lead_order  # u_sym ≡ t²; if u_lead_order=2 want t²
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
            "variant": label,
            "S_at_qeq1": str(S_const),
            "c_k": {str(k): str(v) for k, v in c_k.items()},
            "odd_residue_in_t": float(odd_residue_num),
            "u_lead_order_in_eps": int(u_lead_order),
        }

    print("  TAYLOR EXTRACTION (c_k from u_ladder expansion)")
    print()
    res_N0 = extract_ck(S_N0, "S_N0 = (2q+1-q²)(q²-1)/(2q²)")
    print()
    res_tower = extract_ck(S_tower, "S_tower = S_N0 · (1-ℏ_q²)")
    print()

    # --- Verdict ------------------------------------------------------------
    proved_c2 = sp.Integer(-1)
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print()
    print(f"  PROVED c_2 = -1 (PR #1602 / categorical bar-even constraint)")
    print()
    for res in (res_N0, res_tower):
        c2 = sp.sympify(res.get("c_k", {}).get("2", "0"))
        match = sp.simplify(c2 - proved_c2) == 0
        c2_num = float(sp.N(c2, 15))
        print(f"  {res['variant'][:40]:<40}  c_2 = {c2_num:+.8f}  "
              f"{'✓ matches' if match else '✗ no match'}")
    print()
    print("  Empirical c_3 cross-anchor average ≈ -2 (canonical-framing audit)")
    for res in (res_N0, res_tower):
        c3 = sp.sympify(res.get("c_k", {}).get("3", "0"))
        c3_num = float(sp.N(c3, 15))
        print(f"  {res['variant'][:40]:<40}  c_3 = {c3_num:+.8f}")
    print()
    print("  Fit-extracted c_4 (qbeta-1ppq-achieved) = -0.97157")
    for res in (res_N0, res_tower):
        c4 = sp.sympify(res.get("c_k", {}).get("4", "0"))
        c4_num = float(sp.N(c4, 15))
        print(f"  {res['variant'][:40]:<40}  c_4 = {c4_num:+.8f}")
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

    # Assertions
    for res in (res_N0, res_tower):
        c2 = sp.sympify(res.get("c_k", {}).get("2", "0"))
        c2_num = float(sp.N(c2 - proved_c2, 20))
        builder.add_assertion(
            f"{res['variant'][:30].replace(' ', '_')}_c2_eq_minus_one",
            computed=c2_num,
            expected=0.0,
            tolerance=1e-15,
            source=(f"{res['variant']}: c_2 should equal -1 (PR #1602 "
                    "proved; bar-even constraint). Non-match identifies "
                    "this E_0 variant as the wrong canonical form."),
        )

    builder.save()
    print(f"\n  Witness: qbeta-habiro-f-from-shape-collapse.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
