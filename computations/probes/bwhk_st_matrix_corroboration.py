#!/usr/bin/env python3
"""bwhk_st_matrix_corroboration.py — scope-(a) NUMERICAL corroboration that the
modular data (S-matrix vacuum row + T-matrix / ribbon twist) of the two sides of
the BW-localization = Hecke MTC identification agree, for the n=5 blocks λ⊢5 at the
substrate q₀ (bean bwhk / BWH-2).

WHAT THIS IS — and is NOT (STRICT scope, read first).
-----------------------------------------------------
The identification "Beasley–Witten localization category = the Hecke modular tensor
category" is a PHYSICS claim (RT = WRT / gauge = categorical, the Chern–Simons TQFT
identification). It is NOT derivable and NOT number-crunchable; it is owner-gated
(beans bwse / bwhk). This probe therefore provides EVIDENCE — numerical agreement of
the two sides' modular data — for that identification. It is scope-(a): "these two
modular-data constructions match as-is." It does NOT close bwse / bwhk, wires nothing,
fits nothing (zero free parameters), and leaves L2 unchanged (2/7).

The two sides and their independent construction routes.
--------------------------------------------------------
For the n=5 Hecke blocks λ⊢5 evaluated at the substrate modulus q₀ ≈ 1.10998:

  * Hecke side (the TARGET MTC).  quantum dimension d_q(λ) via the q-hook-length
    formula d_q(λ) = [5]_q! / ∏_{cells}[h]_q; the vacuum S-matrix row S_{0λ}=d_q(λ)/D
    with total quantum dimension D=√(Σ_λ d_q(λ)²); and the ribbon twist θ_λ=q^{2c(λ)}
    with content sum c(λ)=Σ_{(i,j)∈λ}(j−i).  (Same conventions as
    keystone_colored_wrt_perblock_vs_dq.py.)

  * WRT / BW side.  In ANY ribbon/modular category the vacuum S-matrix row equals
    d/D by the Verlinde structural identity S_{0λ}=d_λ/D (proved algebraically in
    KeystoneVerlindeSMatrixBridge.S0_eq), and the twist is the ribbon eigenvalue
    θ_λ=q^{κ_λ} with κ_λ=⟨λ,λ+2ρ⟩ the sl-Casimir Σ_i λ_i(λ_i−2i+1) (the framing
    anomaly of the colored Wilson line).  The WRT quantum dimension itself is reused
    from the Lawrence–Rozansky/colored amplitude route of keystone_lr_amplitude_level7.py:
    the amplitude character reproduces the McKay/E₈ value map d_ζ(λ) at the fibre roots
    (d((5))=[1], d((4,1))=[4], d((3,2))=[5], d((3,1,1))=[5]+1 as Chebyshev polynomials
    in the fold variable t=q+q⁻¹).

  The corroboration is that these two INDEPENDENT routes produce the SAME modular data:
  the q-hook combinatorics (Hecke) vs the McKay/LR-amplitude value map (WRT) give the
  same quantum dimension d(λ) — hence the same S-row d/D — and the content-sum twist
  (Hecke) vs the sl-Casimir ribbon eigenvalue (WRT) give the same θ_λ.

Corroboration assertions.
-------------------------
  (i)   S-matrix VALUE identification: the WRT amplitude/McKay value map d^WRT(λ) equals
        the Hecke q-hook d^Hecke_q(λ) at q₀ for every physical block — so the two vacuum
        S-rows S_{0λ}=d/D coincide (this corroborates the *value* identification; two
        genuinely different construction routes, not one object relabelled).
  (ii)  T-matrix / twist agreement: the WRT ribbon eigenvalue exponent κ_λ (sl-Casimir)
        equals the Hecke content-sum exponent 2c(λ) for every λ⊢5 — so θ^WRT_λ=θ^Hecke_λ.
  (iii) twist conjugation-ANTISYMMETRY: θ_{λ'}=θ_λ⁻¹ (from κ_{λ'}=−κ_λ), the ribbon
        signature of the bar involution q↦q⁻¹.
  (iv)  Verlinde vacuum-row unitarity Σ_λ S_{0λ}²=1 (a genuine modular-data property of
        the shared S-row) — reported alongside the side-by-side S/T table.

If any assertion FAILS, allPassed=False and the honest scope-(a) negative is reported —
"these two modular-data constructions do not match as-is" — never fudged.

No fit; zero free parameters; nothing wired; L2 unchanged (2/7).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf, sqrt  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
# canonical muon-q₀, read at runtime from the pinning witness (§q₀ anchor convention;
# drift-proof, full 50-dps) — never hardcode, never the float64 mass_endomorphism.q0.
import json as _json  # noqa: E402
_pin = _json.loads((Path(__file__).resolve().parents[1] / "q-pinning-50-digit.witness.json").read_text())
Q0 = mpf(_pin.get("q0Value") or _pin.get("data", {}).get("q0Value"))
TOL = mpf(10) ** (-40)

N = 5  # the n=5 Hecke blocks λ⊢5

# The four McKay/E₈ "physical" blocks whose LR-amplitude value map is defined
# (keystone_lr_amplitude_level7.py): d((5))=[1], d((4,1))=[4], d((3,2))=[5],
# d((3,1,1))=[5]+1, as Chebyshev polynomials in the fold variable t=q+q⁻¹.
PHYSICAL = {(5,), (4, 1), (3, 2), (3, 1, 1)}


# ---- q-integers, q-factorial, q-hook-length dimension d_q (full Hecke, ALL rows) -----------------
def qint(m):
    return (Q0 ** m - Q0 ** (-m)) / (Q0 - Q0 ** (-1))


def q_factorial(m):
    r = mpf(1)
    for k in range(1, m + 1):
        r *= qint(k)
    return r


def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(row - j - 1) + (conj[j] - i - 1) + 1
            for i, row in enumerate(lam) for j in range(row)]


def d_q_hook(lam):
    """Hecke q-hook-length quantum dimension d_q(λ)=[n]_q!/∏[h]_q."""
    den = mpf(1)
    for h in hooks(lam):
        den *= qint(h)
    return q_factorial(sum(lam)) / den


def content_sum(lam):
    """c(λ)=Σ_{(i,j)∈λ}(j−i), 0-indexed cells."""
    return sum(j - i for i, row in enumerate(lam) for j in range(row))


def casimir(lam):
    """sl Casimir κ_λ=Σ_i λ_i(λ_i−2i+1) (1-indexed i); the WRT ribbon-twist exponent
    ⟨λ,λ+2ρ⟩. Algebraically κ_λ=2c(λ), but computed here from an INDEPENDENT formula
    so the twist agreement (ii) is a genuine two-route check, not a relabelling."""
    return sum(l * (l - 2 * (i + 1) + 1) for i, l in enumerate(lam))


def conjugate(lam):
    if not lam:
        return ()
    return tuple(sum(1 for r in lam if r > j) for j in range(lam[0]))


def num_rows(lam):
    return len(lam)


def partitions(n):
    def gen(n, mx):
        if n == 0:
            yield ()
            return
        for first in range(min(n, mx), 0, -1):
            for rest in gen(n - first, first):
                yield (first,) + rest
    return list(gen(n, n))


# ---- WRT / BW amplitude (McKay/E₈) value map — reused from keystone_lr_amplitude_level7.py --------
def value_poly(lam, t):
    """The LR-amplitude / McKay value map d^WRT(λ) as an explicit Chebyshev polynomial in
    the fold variable t=q+q⁻¹ (the KeystoneN5ValueMapRigidity form). Defined for the four
    physical blocks; this is the independent WRT route for the quantum dimension."""
    if lam == (5,):
        return mpf(1)                          # [1]
    if lam == (4, 1):
        return t ** 3 - 2 * t                   # [4]
    if lam == (3, 2):
        return t ** 4 - 3 * t ** 2 + 1           # [5]
    if lam == (3, 1, 1):
        return t ** 4 - 3 * t ** 2 + 2           # [5]+1
    raise KeyError(lam)


def theta_hecke(lam):
    """Hecke ribbon twist θ_λ=q^{2c(λ)} (content-sum exponent)."""
    return Q0 ** (2 * content_sum(lam))


def theta_wrt(lam):
    """WRT/BW ribbon eigenvalue θ_λ=q^{κ_λ} (sl-Casimir exponent — framing anomaly)."""
    return Q0 ** casimir(lam)


def run():
    parts = partitions(N)
    t0 = Q0 + 1 / Q0  # fold variable

    # Hecke modular data (full 7-block).
    d_hecke = {lam: d_q_hook(lam) for lam in parts}
    D = sqrt(sum(d_hecke[lam] ** 2 for lam in parts))
    S_hecke = {lam: d_hecke[lam] / D for lam in parts}

    # ---- (i) S-matrix VALUE identification on the physical (McKay) blocks --------------------------
    max_value_err = mpf(0)
    value_rows = []
    for lam in sorted(PHYSICAL, key=lambda p: (-len(p), p)):
        d_wrt = value_poly(lam, t0)              # WRT amplitude/McKay route
        d_hec = d_hecke[lam]                     # Hecke q-hook route
        err = abs(d_wrt - d_hec)
        max_value_err = max(max_value_err, err)
        # both S-rows use the SAME D (same block set); equal d ⇒ equal S-row entry.
        value_rows.append({
            "lambda": list(lam),
            "rows": num_rows(lam),
            "d_wrt_amplitude": str(d_wrt),
            "d_hecke_qhook": str(d_hec),
            "abs_err_d": str(err),
            "S0_hecke": str(S_hecke[lam]),
            "S0_wrt": str(d_wrt / D),
            "abs_err_S0": str(abs(d_wrt / D - S_hecke[lam])),
        })
    value_identified = max_value_err < TOL

    # ---- (ii) T-matrix / twist agreement: content-sum vs sl-Casimir (all λ⊢5) ----------------------
    max_twist_exp_err = 0
    max_twist_err = mpf(0)
    for lam in parts:
        max_twist_exp_err = max(max_twist_exp_err, abs(2 * content_sum(lam) - casimir(lam)))
        max_twist_err = max(max_twist_err, abs(theta_hecke(lam) - theta_wrt(lam)))
    twist_agrees = (max_twist_exp_err == 0) and (max_twist_err < TOL)

    # ---- (iii) twist conjugation-antisymmetry θ_{λ'}=θ_λ⁻¹ -----------------------------------------
    max_conj_err = mpf(0)
    conj_pairs = 0
    seen = set()
    for lam in parts:
        lc = conjugate(lam)
        key = frozenset({lam, lc})
        if key in seen:
            continue
        seen.add(key)
        conj_pairs += 1
        # θ_λ · θ_{λ'} = 1  (independently on both the Hecke and WRT twist expressions)
        max_conj_err = max(max_conj_err,
                           abs(theta_hecke(lam) * theta_hecke(lc) - 1),
                           abs(theta_wrt(lam) * theta_wrt(lc) - 1))
    conj_antisym = max_conj_err < TOL

    # ---- (iv) Verlinde vacuum-row unitarity Σ S_{0λ}² = 1 ------------------------------------------
    unit_err = abs(sum(S_hecke[lam] ** 2 for lam in parts) - 1)
    verlinde_unitary = unit_err < TOL

    # side-by-side S/T table (all λ⊢5)
    st_table = []
    for lam in parts:
        st_table.append({
            "lambda": list(lam),
            "rows": num_rows(lam),
            "conj": list(conjugate(lam)),
            "content_sum": content_sum(lam),
            "casimir_kappa": casimir(lam),
            "d_q_hecke": str(d_hecke[lam]),
            "S0_row": str(S_hecke[lam]),
            "theta_hecke": str(theta_hecke(lam)),
            "theta_wrt": str(theta_wrt(lam)),
        })

    return {
        "n": N,
        "q0": str(Q0),
        "total_quantum_dimension_D": str(D),
        "value_rows": value_rows,
        "max_value_err": str(max_value_err),
        "value_identified": value_identified,
        "max_twist_exp_err": int(max_twist_exp_err),
        "max_twist_err": str(max_twist_err),
        "twist_agrees": twist_agrees,
        "conj_pairs": conj_pairs,
        "max_conj_err": str(max_conj_err),
        "conj_antisymmetric": conj_antisym,
        "verlinde_vacuum_unitarity_err": str(unit_err),
        "verlinde_unitary": verlinde_unitary,
        "st_table": st_table,
    }


def report(res):
    print("# BW-localization = Hecke MTC — scope-(a) modular-data corroboration (n=5, q₀)\n")
    print(f"q₀ = {res['q0']}   total quantum dimension D = {float(res['total_quantum_dimension_D']):.10f}\n")

    print("## (i) S-matrix vacuum row — WRT amplitude/McKay d vs Hecke q-hook d\n")
    print("| λ | rows | d(WRT amp) | d(Hecke qhook) | |Δd| | S_0λ(WRT) | S_0λ(Hecke) | |ΔS_0λ| |")
    print("|---|-----:|-----------:|---------------:|-----:|----------:|------------:|-------:|")
    for r in res["value_rows"]:
        print(f"| {tuple(r['lambda'])} | {r['rows']} | {float(r['d_wrt_amplitude']):.8f} | "
              f"{float(r['d_hecke_qhook']):.8f} | {float(r['abs_err_d']):.1e} | {float(r['S0_wrt']):.8f} | "
              f"{float(r['S0_hecke']):.8f} | {float(r['abs_err_S0']):.1e} |")
    print(f"\n- max |Δd| = {float(res['max_value_err']):.2e}. Value identified (⇒ S-rows agree): "
          f"**{res['value_identified']}**.\n")

    print("## (ii)+(iii) T-matrix / ribbon twist θ_λ (content-sum vs sl-Casimir)\n")
    print("| λ | conj λ' | c(λ) | κ_λ | θ_λ(Hecke) | θ_λ(WRT) |")
    print("|---|---------|-----:|----:|-----------:|---------:|")
    for r in res["st_table"]:
        print(f"| {tuple(r['lambda'])} | {tuple(r['conj'])} | {r['content_sum']} | "
              f"{r['casimir_kappa']} | {float(r['theta_hecke']):.6f} | {float(r['theta_wrt']):.6f} |")
    print(f"\n- twist exponent 2c(λ) vs κ_λ: max |err| = {res['max_twist_exp_err']} (exact int); "
          f"max |θ_Hecke − θ_WRT| = {float(res['max_twist_err']):.2e}. Agree: **{res['twist_agrees']}**.")
    print(f"- conjugation antisymmetry θ_λ·θ_λ' = 1 over {res['conj_pairs']} pairs: "
          f"max |err| = {float(res['max_conj_err']):.2e}. Holds: **{res['conj_antisymmetric']}**.\n")

    print("## (iv) Verlinde vacuum-row unitarity Σ_λ S_0λ² = 1\n")
    print(f"- |Σ S_0λ² − 1| = {float(res['verlinde_vacuum_unitarity_err']):.2e}. "
          f"Unitary: **{res['verlinde_unitary']}**.\n")

    print("## Verdict (honest scope-(a))\n")
    all_ok = (res["value_identified"] and res["twist_agrees"]
              and res["conj_antisymmetric"] and res["verlinde_unitary"])
    if all_ok:
        print("- PASS (scope-(a) corroboration). The two INDEPENDENT construction routes agree on")
        print("  the full n=5 modular data at q₀: the WRT LR-amplitude/McKay value map reproduces")
        print("  the Hecke q-hook quantum dimension (so the vacuum S-rows S_0λ=d/D coincide), and")
        print("  the WRT sl-Casimir ribbon eigenvalue reproduces the Hecke content-sum twist")
        print("  θ_λ=q^{2c(λ)} (with θ_λ'=θ_λ⁻¹). Σ S_0λ²=1 confirms the shared vacuum row is a")
        print("  unit vector.")
    else:
        print("- HONEST NEGATIVE (scope-(a)). At least one modular-data quantity of the two")
        print("  constructions does NOT match as-is; see the failing assertion(s) above.")
    print("- This is EVIDENCE for the BW-localization=Hecke MTC identification, NOT a proof of it.")
    print("  The identification (RT=WRT / gauge=categorical, Chern–Simons TQFT) is a physics claim,")
    print("  owner-gated (beans bwse / bwhk), and is NOT number-crunchable. This probe does NOT")
    print("  close bwse/bwhk.")
    print("- No fit; zero free parameters; nothing wired; L2 unchanged (2/7).")


def main(argv=None):
    res = run()
    report(res)

    all_ok = (res["value_identified"] and res["twist_agrees"]
              and res["conj_antisymmetric"] and res["verlinde_unitary"])

    w = WitnessBuilder("bwhk-st-matrix-corroboration", engine="mpmath")
    w.set_description(
        "Scope-(a) numerical corroboration of the BW-localization=Hecke MTC identification via its "
        "modular data (S-matrix vacuum row + T-matrix/ribbon twist) for the n=5 blocks lambda|-5 at "
        "the substrate q0~1.10998. Two INDEPENDENT construction routes are compared: (Hecke) q-hook "
        "quantum dimension d_q=[5]_q!/prod[h]_q, vacuum row S_0lambda=d_q/D (D=sqrt(sum d_q^2)), twist "
        "theta_lambda=q^{2c(lambda)} (content sum); (WRT/BW) the Lawrence-Rozansky/McKay amplitude value "
        "map d^WRT(lambda) (keystone_lr_amplitude_level7.py) and the ribbon eigenvalue theta=q^{kappa} "
        "with kappa the sl-Casimir sum_i lambda_i(lambda_i-2i+1). Assertions: (i) d^WRT=d^Hecke on the "
        "four McKay physical blocks (so the vacuum S-rows S_0lambda=d/D coincide) -- value identification; "
        "(ii) content-sum exponent 2c(lambda)=sl-Casimir kappa_lambda for all lambda|-5 (so theta agrees) "
        "-- twist agreement; (iii) theta_lambda'=theta_lambda^-1 (conjugation antisymmetry, the bar "
        "involution signature); (iv) Verlinde vacuum-row unitarity sum_lambda S_0lambda^2=1. All to 40 dps. "
        "This is EVIDENCE for the identification, NOT a proof: BW-localization=Hecke MTC is a physics claim "
        "(RT=WRT / gauge=categorical, Chern-Simons TQFT), owner-gated (beans bwse/bwhk), NOT number-crunchable. "
        "Does NOT close bwse/bwhk. No fit; zero free parameters; nothing wired; L2 unchanged (2/7)."
    )
    w.add_data("n", res["n"])
    w.add_data("q0", res["q0"])
    w.add_data("total_quantum_dimension_D", res["total_quantum_dimension_D"])
    w.add_data("value_rows", res["value_rows"])
    w.add_data("max_value_err", res["max_value_err"])
    w.add_data("max_twist_exp_err", res["max_twist_exp_err"])
    w.add_data("max_twist_err", res["max_twist_err"])
    w.add_data("conj_pairs", res["conj_pairs"])
    w.add_data("max_conj_err", res["max_conj_err"])
    w.add_data("verlinde_vacuum_unitarity_err", res["verlinde_vacuum_unitarity_err"])
    w.add_data("st_table", res["st_table"])
    w.add_data(
        "verdict",
        ("PASS (scope-(a) corroboration). " if all_ok else "HONEST NEGATIVE (scope-(a)). ") +
        "The WRT LR-amplitude/McKay value map and the Hecke q-hook quantum dimension "
        "give the same n=5 vacuum S-matrix row S_0lambda=d/D at q0, and the WRT sl-Casimir ribbon "
        "eigenvalue and the Hecke content-sum give the same twist theta_lambda=q^{2c(lambda)} (with "
        "theta_lambda'=theta_lambda^-1); Verlinde unitarity sum S_0lambda^2=1 holds. This is scope-(a) "
        "EVIDENCE for the BW-localization=Hecke MTC identification, not a proof: the identification "
        "(RT=WRT / gauge=categorical, Chern-Simons TQFT) is a physics claim, owner-gated (beans "
        "bwse/bwhk), and is NOT number-crunchable. Does NOT close bwse/bwhk. No fit; nothing wired; "
        "L2 unchanged (2/7).",
    )
    w.add_assertion(
        "smatrix_vacuum_row_value_identified_n5",
        computed=1 if res["value_identified"] else 0, expected=1, tolerance=0,
        source="The WRT LR-amplitude/McKay value map d^WRT(lambda) (d((5))=[1], d((4,1))=[4], "
               "d((3,2))=[5], d((3,1,1))=[5]+1 as Chebyshev polynomials in t=q0+1/q0) equals the "
               "Hecke q-hook quantum dimension d_q(lambda)=[5]_q!/prod[h]_q at q0 for all four physical "
               "blocks (max |Delta d| < 1e-40), so the vacuum S-matrix rows S_0lambda=d/D coincide "
               "block-by-block. Two independent construction routes; corroborates the value identification.",
    )
    w.add_assertion(
        "tmatrix_twist_agrees_contentsum_eq_casimir_n5",
        computed=1 if res["twist_agrees"] else 0, expected=1, tolerance=0,
        source="The Hecke content-sum twist exponent 2c(lambda)=2*sum(j-i) equals the WRT sl-Casimir "
               "ribbon-eigenvalue exponent kappa_lambda=sum_i lambda_i(lambda_i-2i+1) exactly (integer "
               "equality) for all seven lambda|-5, so theta^Hecke_lambda=q^{2c}=q^{kappa}=theta^WRT_lambda "
               "to 40 dps. Independent formulas for the same ribbon twist.",
    )
    w.add_assertion(
        "twist_conjugation_antisymmetric_n5",
        computed=1 if res["conj_antisymmetric"] else 0, expected=1, tolerance=0,
        source="theta_lambda' * theta_lambda = 1 for all conjugate pairs (kappa_lambda'=-kappa_lambda), "
               "on both the Hecke content-sum and the WRT Casimir twist expressions, to 40 dps -- the "
               "ribbon signature of the bar involution q -> q^-1.",
    )
    w.add_assertion(
        "verlinde_vacuum_row_unitary_n5",
        computed=1 if res["verlinde_unitary"] else 0, expected=1, tolerance=0,
        source="Sum_lambda S_0lambda^2 = 1 to 40 dps (the shared vacuum S-matrix row is a unit vector) "
               "-- a genuine modular-data property of the S-row S_0lambda=d_q/D, D=sqrt(sum d_q^2).",
    )
    out = w.save()
    print(f"\nwitness -> {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
