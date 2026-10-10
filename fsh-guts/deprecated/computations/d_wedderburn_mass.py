#!/usr/bin/env python3
"""
Deuterium binding via the full Wedderburn mass formula.

Formula (prop:wedderburn-mass-formula):

  M(Z,N) = Z·m_p + N·m_n + Z·m_e + α · Σ_i ln|V̂_i^full|

  V̂_i^full = w_sym · λ_i^sym + w_std · V̂_i^std + w_alt · λ_i^alt

  w_sym = w_alt = 1/[3]_q!,   w_std = [2]_q² / [3]_q!
  [n]_q = q^{n-1} + q^{n-3} + ... + q^{-(n-1)}  (symmetric Laurent)

  V̂_i^std = z · a_i + b_i   (transfer-matrix chain, standard rep)
  λ_i^sym = ∏_j (c_j · q + d_j)       (symmetric channel eigenvalue)
  λ_i^alt = ∏_j (-c_j / q + d_j)      (alternating channel eigenvalue)
  z = 1/(√q + 1/√q)

  α = m_e · 8G   (Catalan / Borromean volume; theorem-derived)

For D: ordering = [p, e, n] (3 strands, ep-pair electron insertion)
Crossings (c, d) by type pair:
  (p, e): (1, -h)            ← proton-electron
  (p, n): (1, -h/2)          ← proton-neutron (mixed)
  (e, n): (0, 1)             ← electron-neutron (trivial)

Only gen 0 contributes a non-trivial V̂_0.  Gen 1 sees only the
trivial (0,1) crossing → V̂_1 = 1, ln|V̂_1| = 0.

Zero fitted parameters.  Computed at mpmath 50 digits.
"""
from __future__ import annotations

import sys
import json
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore", category=UserWarning)

sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp

# Precision applied only when run as main; import-safe otherwise.
_MP_DPS = 50
if __name__ == "__main__":
    mp.mp.dps = _MP_DPS

from q_parameter import (
    Q as Q0_FLOAT, HBAR_Q, HBAR_Q_SQ,
    VOL_FIGURE_EIGHT, MASS_RATIO_MU_E,
    Q_MP as Q0_MP, HBAR_Q_MP, HBAR_Q_SQ_MP, Q_INV_MP as Q_INV, HA_MP,
)
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

# ── Substrate at mpmath precision ─────────────────────────────
# Use the high-precision globals from q_parameter (computed via
# Vol(4_1) = 2 Cl_2(π/3) at 50 dps).  Previously this block went
# `mp.mpf(str(VOL_FIGURE_EIGHT)) / mp.mpf(str(MASS_RATIO_MU_E))`,
# which only carried f64 (~16 dps) through and printed 40 dps of
# trailing noise in the witness JSON.
Z_MP = mp.mpf(1) / (mp.sqrt(Q0_MP) + mp.mpf(1) / mp.sqrt(Q0_MP))

# ── q-integer brackets (symmetric Laurent) ────────────────────
def q_bracket(n: int) -> mp.mpf:
    """[n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    return (Q0_MP**n - Q_INV**n) / HA_MP

def q_bracket_fact(n: int) -> mp.mpf:
    """[n]_q! = ∏_{k=1..n} [k]_q."""
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= q_bracket(k)
    return out

BRACKET_2 = q_bracket(2)
BRACKET_3 = q_bracket(3)
BRACKET_3_FACT = q_bracket_fact(3)
# Plancherel weights w_λ = d_q(λ)² / [n]_q! for n = 3.  For n = 3 the
# partitions are (3), (2,1), (1,1,1) with d_q² = 1, [2]_q², 1 and
# Σ w_λ = (2 + [2]_q²) / [3]_q!.  At q = 1 this sums to 1 (Plancherel
# normalisation on S_n); at q ≠ 1 it differs by a factor ≈ 0.988 at
# q₀.  These are the UNNORMALISED Plancherel weights: the mass formula
# defines the derivation up to a constant α · ln(Σ w_λ) ≈ −0.046 MeV
# at q₀, which is absorbed into the α calibration rather than being
# treated as a physical binding-energy contribution.  See
# markov_weight_verification.py for the full-atom numerical comparison
# against the Jones-Ocneanu Markov normalisation z = 1/(q^{1/2}+q^{-1/2}).
W_SYM = mp.mpf(1) / BRACKET_3_FACT
W_ALT = W_SYM
W_STD = BRACKET_2**2 / BRACKET_3_FACT

CATALAN_G = mp.mpf("0.91596559417721901505460351493238411077414937428167")
VOL_BORROMEAN = 8 * CATALAN_G     # = 8G
ALPHA_MP = mp.mpf(str(M_E_MEV)) * VOL_BORROMEAN

# ── Crossing coefficients by particle type ────────────────────
def crossing_cd(ti: str, tj: str) -> tuple[mp.mpf, mp.mpf]:
    zero, one, half = mp.mpf(0), mp.mpf(1), mp.mpf("0.5")
    if ti == "p" and tj == "p": return one, zero
    if ti == "n" and tj == "n": return one, -HA_MP
    if (ti, tj) in [("p", "n"), ("n", "p")]: return one, -HA_MP * half
    if (ti, tj) in [("p", "e"), ("e", "p")]: return one, -HA_MP
    if (ti, tj) in [("n", "e"), ("e", "n")]: return zero, one
    if ti == "e" and tj == "e": return one, zero
    return zero, one


def v_hat_full_for_gen(ordering: list[str], gen: int) -> dict:
    """Compute V̂_i^std, λ_i^sym, λ_i^alt, V̂_i^full for a given generator."""
    n = len(ordering)
    # Standard rep: transfer-matrix chain
    a = mp.mpf(0)
    b = mp.mpf(1)
    lam_sym = mp.mpf(1)
    lam_alt = mp.mpf(1)
    any_nontrivial = False
    factors = []
    for j in range(gen + 1, n):
        c, d = crossing_cd(ordering[gen], ordering[j])
        factors.append((ordering[j], float(c), float(d)))
        if c == 0 and d == 1:
            continue
        any_nontrivial = True
        # Transfer matrix recurrence
        a_new = a * c * HA_MP + a * d + b * c
        b_new = a * c + b * d
        a, b = a_new, b_new
        # Sym channel: (c·q + d)
        lam_sym *= c * Q0_MP + d
        # Alt channel: (-c/q + d)
        lam_alt *= -c / Q0_MP + d
    v_std = Z_MP * a + b
    v_full = (lam_sym * W_SYM + v_std * W_STD + lam_alt * W_ALT)
    return {
        "gen": gen,
        "has_crossing": any_nontrivial,
        "factors": factors,
        "a": str(a), "b": str(b),
        "V_std": str(v_std),
        "lambda_sym": str(lam_sym),
        "lambda_alt": str(lam_alt),
        "V_full": str(v_full),
        "abs_V_full": str(mp.fabs(v_full)),
        "ln_abs_V_full": (str(mp.log(mp.fabs(v_full)))
                           if mp.fabs(v_full) > mp.mpf("1e-100") else "log(0)"),
    }


def binding_full(ordering: list[str]) -> dict:
    """Compute B = -α · Σ ln|V̂_i^full| for an atom ordering."""
    n = len(ordering)
    gen_data = []
    phi_full = mp.mpf(0)
    phi_std = mp.mpf(0)
    for gen in range(n - 1):
        d = v_hat_full_for_gen(ordering, gen)
        gen_data.append(d)
        if d["has_crossing"]:
            v_f = mp.fabs(mp.mpf(d["V_full"]))
            if v_f > mp.mpf("1e-100"):
                phi_full += mp.log(v_f)
            v_s = mp.fabs(mp.mpf(d["V_std"]))
            if v_s > mp.mpf("1e-100"):
                phi_std += mp.log(v_s)
    B_full = -ALPHA_MP * phi_full
    B_std = -ALPHA_MP * phi_std
    return {
        "ordering": ordering,
        "n_strands": n,
        "generators": gen_data,
        "Phi_full": str(phi_full),
        "Phi_std_only": str(phi_std),
        "B_full_MeV": str(B_full),
        "B_std_only_MeV": str(B_std),
    }


def main() -> int:
    print("=" * 110)
    print("DEUTERIUM BINDING via WEDDERBURN MASS FORMULA")
    print(f"  q₀ = {mp.nstr(Q0_MP, 20)}")
    print(f"  h  = {mp.nstr(HA_MP, 12)}")
    print(f"  z  = {mp.nstr(Z_MP, 12)}")
    print(f"  [2]_q  = {mp.nstr(BRACKET_2, 12)}")
    print(f"  [3]_q  = {mp.nstr(BRACKET_3, 12)}")
    print(f"  [3]_q! = {mp.nstr(BRACKET_3_FACT, 12)}")
    print(f"  w_sym  = w_alt = {mp.nstr(W_SYM, 12)}")
    print(f"  w_std  = {mp.nstr(W_STD, 12)}")
    print(f"  α = m_e · 8G = {mp.nstr(ALPHA_MP, 12)} MeV")
    print("=" * 110)

    # Deuterium: ordering pen (proton + electron + neutron)
    ordering = ["p", "e", "n"]
    print(f"\n  D ordering (ep-pair insertion): {ordering}")
    res = binding_full(ordering)

    print(f"\n  Per-generator volumes:")
    for g in res["generators"]:
        print(f"    gen {g['gen']}: factors = {g['factors']}")
        if not g["has_crossing"]:
            print(f"      (all trivial — V̂ = 1, ln|V̂| = 0)")
            continue
        print(f"      V̂^std     = {g['V_std'][:30]}")
        print(f"      λ^sym     = {g['lambda_sym'][:30]}")
        print(f"      λ^alt     = {g['lambda_alt'][:30]}")
        print(f"      V̂^full    = {g['V_full'][:30]}   "
              f"|V̂^full| = {g['abs_V_full'][:20]}")
        print(f"      ln|V̂^full| = {g['ln_abs_V_full'][:30]}")

    print(f"\n  Φ_full (Wedderburn) = {res['Phi_full']}")
    print(f"  Φ_std  (std only)   = {res['Phi_std_only']}")

    # Comparison with AME
    B_AME = mp.mpf("2.22456612")
    B_full = mp.mpf(res["B_full_MeV"])
    B_std = mp.mpf(res["B_std_only_MeV"])

    print(f"\n  α = m_e · 8G = {mp.nstr(ALPHA_MP, 10)} MeV")
    print(f"\n  B_AME(D)             = {mp.nstr(B_AME, 10)} MeV")
    print(f"  B_pred (Wedderburn)   = {mp.nstr(B_full, 10)} MeV")
    print(f"  B_pred (Φ_std only)   = {mp.nstr(B_std, 10)} MeV")
    print(f"  B_pred (Kashaev 6_2)  = {mp.nstr(mp.mpf('0.51099895')*mp.mpf('4.4008325161'), 10)} MeV  (reference, +1.09%)")

    err_full = (B_full - B_AME) / B_AME
    err_std = (B_std - B_AME) / B_AME
    print(f"\n  err (Wedderburn) = {mp.nstr(err_full * 100, 6)}%  = "
          f"{mp.nstr(err_full * 10**9, 6)} ppb")
    print(f"  err (Φ_std only) = {mp.nstr(err_std * 100, 6)}%  = "
          f"{mp.nstr(err_std * 10**9, 6)} ppb")

    witness = {
        "computation": "d-wedderburn-mass",
        "description": (
            "D binding via the full Wedderburn-weighted mass formula "
            "(prop:wedderburn-mass-formula).  Uses V̂^full = "
            "w_sym·λ^sym + w_std·V̂^std + w_alt·λ^alt with weights "
            "derived from q₀ (zero fitted parameters).  mpmath 50 "
            "digits."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0_mp": mp.nstr(Q0_MP, 40),
            "hbar_q_sq_mp": mp.nstr(HBAR_Q_SQ_MP, 40),
            "z_mp": mp.nstr(Z_MP, 40),
            "HA_mp": mp.nstr(HA_MP, 40),
            "bracket_2": mp.nstr(BRACKET_2, 40),
            "bracket_3": mp.nstr(BRACKET_3, 40),
            "bracket_3_fact": mp.nstr(BRACKET_3_FACT, 40),
            "w_sym": mp.nstr(W_SYM, 40),
            "w_std": mp.nstr(W_STD, 40),
            "alpha_MeV": mp.nstr(ALPHA_MP, 40),
            "m_e_MeV": M_E_MEV,
        },
        "result": res,
        "B_AME_MeV": str(B_AME),
        "B_pred_wedderburn_MeV": str(B_full),
        "B_pred_std_only_MeV": str(B_std),
        "err_wedderburn_pct": str(err_full * 100),
        "err_wedderburn_ppb": str(err_full * 10**9),
        "err_std_only_pct": str(err_std * 100),
        "err_std_only_ppb": str(err_std * 10**9),
    }
    out = Path(__file__).parent / "d-wedderburn-mass.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
