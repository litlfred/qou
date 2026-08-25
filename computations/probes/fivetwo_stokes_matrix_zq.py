#!/usr/bin/env python3
"""fivetwo_stokes_matrix_zq.py — the exact Z[q^±] Stokes prefactor of 5₂,
its DEFINING inversion relation (GGM Conjecture 1(b), eq 4), and its
identification as the FW↔GGM Jacobian prefactor between the 5₂ Andersen–
Kashaev state integral I_{0,0}=Z_{5₂} and the median-Borel resummation of
Φ_{5₂}.

LITERATURE TRANSCRIPTION + IDENTIFICATION — NOT a QOU c₃ derivation.
Nothing is fitted; nothing is wired to production; c₃ is NOT claimed derived.

Source: Garoufalidis–Gu–Mariño, *The resurgent structure of quantum knot
invariants* (arXiv:2007.10190v2, CMP 2021; `library/arxiv-2007.10190v2/2007.10190v2.pdf`),
§3 (the equation x⁻²(1−x)³ = 1 and the 5₂ knot), eqs (22)–(29).
Registered as `garoufalidis-gu-mariño2021`.

WHAT WAS ALREADY IN THE CORPUS (cited, NOT duplicated):
  • `qbeta_g3_5two_analytic_hm_tower.py` (PR #4011): the exact rational
    q-series arithmetic for the H^ε_{k,m}(q) tower and the fundamental
    solution W₋₁(q) (GGM eqs 24/25, App. A).
  • `qbeta_g3_5two_stokes_sandwich.py` (PR #4013): assembles S⁺(q), S⁻(q)
    from eqs (29a/b) and verifies K1 (q→0 limits = printed factorizations,
    Stokes constants {3,4,9}), K2 (integrality of every entry as a
    Z[q^±] series), K3 (det S± = 1).  This probe *reuses* that assembly.
  • `qbeta_5two_chirality_state_integral_probe.py` (PR #4475, bean
    qou-u5xq): the AK state integral I_{0,0}=Z_{5₂}=∫Φ_b³e^{−2πiv²}dv on
    the substrate ray, quadrature-vs-factorization matched.
  • `docs/audits/2026-08-01-fantini-wheeler-summability-c3-borel-reframe.md`:
    the FW framing — median-Borel(Φ_{5₂}) is a Z[q^±]-combination of the
    I_{m,ℓ}, with the Stokes matrix as the wall-crossing (Jacobian) data.

WHAT THIS PROBE ADDS (genuinely new, verified here):
  V1 — GGM Conjecture 1(b), the INVERSION RELATION  S⁺(q)ᵀ S⁻(q) = I
       (eq 4), verified as an exact q-series to O(q^ORD).  This is the
       defining consistency/cocycle property of the Stokes PAIR and is
       NOT checked anywhere else in the corpus (the sandwich probe checks
       only q→0, integrality, det).  It is the multiplicative companion
       to the realness lemma `ratio_star_fixed_of_shared_law`
       (G3RealnessConjugationBrick.lean, PR #4485).
  V2 — det W₋₁(q) = 2 (eq 26) and the fundamental W-sandwich identity
       (eq 28): ½·W₋₁(q)·J·W₋₁(q⁻¹)ᵀ = [[1,0,0],[0,0,1],[0,1,3−q⁰]],
       J = antidiag(1,2,1).  These are the certificates that make S±
       well-defined; verified here as exact q-series (NEW cross-check).
  V3 — the 5₂ Stokes-constant read-off {3,4,9} and the σ₁σ₁ entry ↔
       DGG rotated 3D-index tie (Conjecture 2, eq 5).
  V4 — the prefactor IDENTIFICATION: I_{0,0}=Z_{5₂} and S±(q) are two
       contractions of the SAME fundamental solution W₋₁ (eq 29 vs the
       eq-110 factorization used by the chirality probe); the integer
       matrices L±,R± + the frame phase e^{πi/4} ARE the Jacobian
       prefactor.  Reports the leading one-instanton contribution the
       prefactor makes to the resummation at the substrate, and states
       the residual toward FULL numeric equality (median resummation of
       the perturbative ϕ_{σⱼ}(τ), eq 20 — NOT done here → gap bean).

Run:
  python3 -u computations/probes/fivetwo_stokes_matrix_zq.py \
      2>&1 | tee /tmp/fivetwo_stokes_matrix_zq.log
"""
from __future__ import annotations

import importlib.util
import sys
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp

mp.mp.dps = 60

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

# ---- reuse the corpus S± assembly (which imports the H-tower) ----
_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_5two_stokes_sandwich",
    _HERE / "qbeta_g3_5two_stokes_sandwich.py")
_sw = importlib.util.module_from_spec(_spec)
# prevent the sandwich module's main() from running on import
_sw.__name__ = "qbeta_g3_5two_stokes_sandwich"
_spec.loader.exec_module(_sw)

_tw = _sw._tw          # the H-tower module
NS = _sw.NS            # exact-series truncation order (q^0..q^NS)
ORD = 18              # order to which q-series identities are asserted

# GGM 5₂ q→0 Stokes factorizations (eq analog of 96/97; sandwich targets)
S_P_TARGET = _sw.S_P_TARGET   # [[1,4,0],[0,1,0],[-3,-9,1]]
S_M_TARGET = _sw.S_M_TARGET   # [[1,0,3],[-4,1,-3],[0,0,1]]

Q0 = mp.mpf(
    "1.10997859555733471989976322048322502665620840878015368660798114614493")


# ------------------------------------------------------------------ helpers
def _identity_series():
    I = [[_tw._zero() for _ in range(3)] for _ in range(3)]
    for i in range(3):
        I[i][i] = _tw._qpow(0)   # constant 1
    return I


def _is_identity(S):
    """S == I as a q-series to O(q^ORD)?"""
    for i in range(3):
        for j in range(3):
            want1 = (i == j)
            for t in range(ORD + 1):
                c = S[i][j][t]
                if t == 0 and want1 and c != 1:
                    return False
                if t == 0 and not want1 and c != 0:
                    return False
                if t > 0 and c != 0:
                    return False
    return True


def _all_integer_series(S):
    return all(
        c.denominator == 1
        for row in S for e in row for c in e[: ORD + 1])


def _assemble_S():
    """Reproduce the sandwich probe's winning-convention S⁺(q), S⁻(q)."""
    Wq_raw = _sw.series_mat_raw()
    Wqi_raw = _sw.series_mat_ext()
    for conv in (False, True):
        Wq = _sw.flip(Wq_raw) if conv else Wq_raw
        Wqi = _sw.flip(Wqi_raw) if conv else Wqi_raw
        Sp = _sw.sandwich(Wq, Wqi, _sw.L_P, _sw.R_P, first_is_qi=True)
        Sm = _sw.sandwich(Wq, Wqi, _sw.L_M, _sw.R_M, first_is_qi=False)
        sp0 = [[Sp[i][j][0] for j in range(3)] for i in range(3)]
        sm0 = [[Sm[i][j][0] for j in range(3)] for i in range(3)]
        k1 = (sp0 == [[Fr(x) for x in r] for r in S_P_TARGET]) and \
             (sm0 == [[Fr(x) for x in r] for r in S_M_TARGET])
        if k1:
            return Wq, Wqi, Sp, Sm, ("J3-flipped" if conv else "unflipped")
    raise RuntimeError("neither convention reproduced the q→0 targets")


def _det3_series(S):
    m = _tw._mul
    s = _tw._sub
    a = _tw._add
    t1 = m(S[0][0], s(m(S[1][1], S[2][2]), m(S[1][2], S[2][1])))
    t2 = m(S[0][1], s(m(S[1][0], S[2][2]), m(S[1][2], S[2][0])))
    t3 = m(S[0][2], s(m(S[1][0], S[2][1]), m(S[1][1], S[2][0])))
    return a(s(t1, t2), t3)


def main() -> int:
    print("=" * 78)
    print(" 5₂ Z[q^±] Stokes prefactor — inversion relation (eq 4) + "
          "AK-integral tie")
    print("=" * 78)

    Wq, Wqi, Sp, Sm, conv = _assemble_S()
    print(f"\n[assembly] winning convention: {conv} "
          f"(q→0 limits match GGM eq-29 factorizations)")
    sp0 = [[int(Sp[i][j][0]) for j in range(3)] for i in range(3)]
    sm0 = [[int(Sm[i][j][0]) for j in range(3)] for i in range(3)]
    print(f"           S⁺(0) = {sp0}")
    print(f"           S⁻(0) = {sm0}")

    # ---- V1: eq (4) inversion  S⁺(q)ᵀ S⁻(q) = I  (NEW) ----
    SpT = _sw.transpose(Sp)
    prod = _sw.smat_mul(SpT, Sm)
    v1 = _is_identity(prod)
    print(f"\n[V1] eq(4) inversion  S⁺(q)ᵀ·S⁻(q) = I  to O(q^{ORD}): {v1}")
    # also print a couple of entries to O(q^3) as evidence
    diag00 = [str(prod[0][0][t]) for t in range(4)]
    off01 = [str(prod[0][1][t]) for t in range(4)]
    print(f"     (0,0) series = {diag00}  (want [1,0,0,0])")
    print(f"     (0,1) series = {off01}  (want [0,0,0,0])")

    # sanity: inversion already holds exactly at q→0 on the integer targets
    prod0 = [[sum(sp0[k][i] * sm0[k][j] for k in range(3))
              for j in range(3)] for i in range(3)]   # (S⁺(0)ᵀ S⁻(0))
    v1_0 = prod0 == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(f"     q→0 integer check  S⁺(0)ᵀ S⁻(0) = I: {v1_0}")

    # ---- V2: det W₋₁(q)=2 (eq 26) + eq (28) W-sandwich (NEW cross-check) ----
    detW = _det3_series(Wq)
    v2a = (abs(detW[0]) == 2 and all(detW[t] == 0 for t in range(1, ORD + 1)))
    print(f"\n[V2] det W₋₁(q) = ±2 (eq 26): {v2a}  (const term "
          f"{int(detW[0])})")
    # eq (28) at m=0:  ½·W₋₁(q)·J·W₋₁(q⁻¹)ᵀ = [[1,0,0],[0,0,1],[0,1,3−1]]
    J = [[0, 0, 1], [0, 2, 0], [1, 0, 0]]     # antidiag(1,2,1) (eq 27/28)
    core = _sw.smat_mul(_sw.smat_mul_int(Wq, J), _sw.transpose(Wqi))
    half = [[_tw._smul(Fr(1, 2), core[i][j]) for j in range(3)]
            for i in range(3)]
    target28 = {(0, 0): [1], (1, 2): [1], (2, 1): [1], (2, 2): [2]}
    v2b = True
    for i in range(3):
        for j in range(3):
            head = target28.get((i, j), [])
            for t in range(ORD + 1):
                want = head[t] if t < len(head) else 0
                if half[i][j][t] != want:
                    v2b = False
    print(f"     eq(28) ½·W₋₁(q)·J·W₋₁(q⁻¹)ᵀ = [[1,0,0],[0,0,1],"
          f"[0,1,2]] to O(q^{ORD}): {v2b}")

    # ---- integrality + det S± re-cross-check ----
    v_int = _all_integer_series(Sp) and _all_integer_series(Sm)
    dP, dM = _det3_series(Sp), _det3_series(Sm)
    v_det = (dP[0] == 1 and dM[0] == 1 and
             all(dP[t] == 0 and dM[t] == 0 for t in range(1, ORD + 1)))
    print(f"\n[xchk] S± ∈ M₃(Z[q^±]) to O(q^{ORD}): {v_int};  "
          f"det S± = 1: {v_det}")

    # ---- V3: Stokes constants + 3D-index tie ----
    stokes_constants = sorted(
        {abs(v) for r in sp0 for v in r if abs(v) not in (0, 1)} |
        {abs(v) for r in sm0 for v in r if abs(v) not in (0, 1)})
    # σ₁σ₁ = (0,0) entry of S⁺ is the DGG rotated 3D-index (Conj 2, eq 5)
    s11_series = [int(Sp[0][0][t]) for t in range(ORD + 1)]
    # GGM p.19 prints Ind^rot_{5₂}(q) = 1 − 12q + 3q² + 74q³ + 90q⁴ + O(q⁵)
    GGM_INDEX_PRINTED = [1, -12, 3, 74, 90]
    v3_match = s11_series[:5] == GGM_INDEX_PRINTED
    print(f"\n[V3] 5₂ Stokes constants (|entries|>1) = {stokes_constants}")
    print(f"     σ₁σ₁ = S⁺₀₀(q) = Ind^rot_{{5₂}}(q) (Conj 2) leading = "
          f"{s11_series[:8]}")
    print(f"     matches GGM p.19 printed Ind^rot (1−12q+3q²+74q³+90q⁴): "
          f"{v3_match}")

    # ---- V4: prefactor identification + leading one-instanton contribution
    # GGM eq (21): V(σ1) = ReV + i ImV = Vol(5₂) + i·CS(5₂).
    ReV = mp.mpf("2.82812208833455")    # hyperbolic volume of 5₂ complement
    ImV = mp.mpf("1.37919181633454")    # Chern–Simons action
    # substrate ray τ = iβ, β = ln q₀/(2π); the leading Borel singularity of
    # Φ_{σ1} sits at the action ζ = V(σ1)/(2π); the one-instanton weight that
    # the Stokes prefactor multiplies is e^{−ζ/τ} = e^{−V(σ1)/(2πτ)}.
    beta = mp.log(Q0) / (2 * mp.pi)
    tau = mp.mpc(0, 1) * beta
    Vsig1 = mp.mpc(ReV, ImV)
    one_inst = mp.e ** (-Vsig1 / (2 * mp.pi * tau))
    # leading Stokes constant on the σ1σ1 channel = O(q) coeff of Ind^rot
    s_lead = s11_series[1]
    print(f"\n[V4] prefactor identification (structural):")
    print("     I_{0,0}=Z_{5₂} and S±(q) are two contractions of the SAME")
    print("     fundamental solution W₋₁ (eq 29 vs the eq-110 factorization")
    print("     used by qbeta_5two_chirality_state_integral_probe). The")
    print("     integer matrices L±,R± + frame phase e^{πi/4} are the Jacobian")
    print("     prefactor of the FW↔GGM median-resummation correspondence.")
    print(f"     leading one-instanton weight e^(−V(σ1)/2πτ) at substrate = "
          f"{mp.nstr(one_inst, 8)}")
    print(f"     leading σ₁σ₁ Stokes constant (O(q) of Ind^rot) = {s_lead}")
    lead_disc = s_lead * one_inst
    print(f"     ⇒ leading (S−I)Φ contribution to median resummation ≈ "
          f"{mp.nstr(lead_disc, 8)}")

    all_ok = v1 and v1_0 and v2a and v2b and v_int and v_det and v3_match
    print("\n" + "=" * 78)
    print(f" RESULT: {'ALL CHECKS PASS' if all_ok else 'SOME CHECK FAILED'}")
    print("=" * 78)

    # ---------------------------------------------------------------- witness
    w = WitnessBuilder("fivetwo-stokes-matrix-zq", output_dir=str(_HERE))
    w.set_description(
        "Exact Z[q^±] Stokes prefactor of 5₂ (GGM 2007.10190 eqs 22-29): "
        "verifies the inversion relation S⁺(q)ᵀS⁻(q)=I (Conjecture 1b, "
        "eq 4) as an exact q-series (NEW — not checked elsewhere in the "
        "corpus), the det-W=2 (eq 26) and W-sandwich (eq 28) fundamental-"
        "solution certificates, S± integrality and det=1, the 5₂ Stokes "
        "constants {3,4,9}, and identifies the pair (L±,R±,frame phase) "
        "as the FW↔GGM Jacobian prefactor connecting the AK state "
        "integral I_{0,0}=Z_{5₂} (PR #4475) to the median-Borel "
        "resummation of Φ_{5₂}. Multiplicative companion to the realness "
        "lemma ratio_star_fixed_of_shared_law (PR #4485).")
    w.set_content_block("conj:im-q-physical-role")
    w.add_parameter("source", "GGM arXiv:2007.10190v2 §3, eqs (22)-(29)")
    w.add_parameter("q0_anchor", "muon")
    w.add_parameter("q0", str(Q0))
    w.add_parameter("series_order_asserted", ORD)
    w.add_parameter("assembly_convention", conv)
    w.add_data("S_plus_q0", sp0)
    w.add_data("S_minus_q0", sm0)
    w.add_data("V1_prod_00_series_to_q3", diag00)
    w.add_data("V1_prod_01_series_to_q3", off01)
    w.add_data("V2_detW_const", int(detW[0]))
    w.add_data("V3_stokes_constants", stokes_constants)
    w.add_data("V3_sigma11_index_rot_leading", s11_series[:8])
    w.add_data("V4_ReV_sigma1_vol", str(ReV))
    w.add_data("V4_ImV_sigma1_cs", str(ImV))
    w.add_data("V4_one_instanton_weight_substrate", mp.nstr(one_inst, 12))
    w.add_data("V4_leading_sigma11_stokes_constant", int(s_lead))
    w.add_data("V4_leading_disc_contribution", mp.nstr(lead_disc, 12))
    w.add_data("discipline",
               "literature transcription of GGM 2007.10190; no fit; "
               "nothing wired; c₃ read-off downstream and NOT claimed")
    w.add_data("prefactor_identification",
               "I_{0,0}=Z_{5₂} and S±(q) are two contractions of the same "
               "fundamental solution W₋₁ (eq 29 vs eq-110 factorization); "
               "L±,R± + frame phase e^{πi/4} are the FW↔GGM Jacobian "
               "prefactor.")
    w.add_assertion("V1_inversion_S+T_S-_eq_I", int(v1), 1)
    w.add_assertion("V1_inversion_q0_integer_check", int(bool(v1_0)), 1)
    w.add_assertion("V2_detW_eq_2", int(v2a), 1)
    w.add_assertion("V2_eq28_W_sandwich", int(v2b), 1)
    w.add_assertion("xchk_S_integral", int(v_int), 1)
    w.add_assertion("xchk_det_S_eq_1", int(v_det), 1)
    w.add_assertion("V3_sigma11_matches_GGM_printed_index", int(v3_match), 1)
    w.add_assertion("all_checks_pass", int(all_ok), 1)
    w.add_caveat(
        "Literature transcription + identification, NOT a QOU c₃ derivation. "
        "Residual toward FULL numeric equality with the median-Borel "
        "resummation of Φ_{5₂}: the median resummation of the perturbative "
        "ϕ_{σⱼ}(τ) (eq 20) is NOT performed here — that is the open gap "
        "(gap bean). No fit; nothing wired to production; c₃ NOT claimed "
        "derived.")
    out = w.save()
    print(f"\nwitness → {out}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
