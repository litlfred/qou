#!/usr/bin/env python3
"""Option-E front 4 — the MULTIPLICATIVE connected 4-body cumulant b₄ at ⁴He.

Δ_λ closure, GAP-A-4, interface-operator / 4-body route. This probe re-derives
(cleanly, 0-fit) the framework's *multiplicative* connected 4-body Ursell cumulant
and reports it as a fraction of the ⁴He AME target — a distinct object from the
sibling `A4InterfaceMagnitude` (`−ln det(I+G)` writhe-determinant surjectivity gate,
branch claude/a4-interface-magnitude-2026-08-02).

THE CONSTRUCTION (canonical multiplicative binding, `interface_4body_assembly_probe.py`,
`binding_canonical.py`):

    B(K) = E₀ · τ_vac · (1 − ∏ᵢ fᵢ)

with E₀ = m_e/(q₀(q₀−1)), τ_vac = τ_p^Z τ_n^N the free constituents, and the product
over the interface pair-factors on the genuine many-body COMPLETE GRAPH K_A (all
C(A,2) pairs):  pp = z,  nn = z − h,  pn = z (production) or z − h/2 (bar-invariant).

The connected 4-body cumulant is the 4th forward finite difference of the binding
sequence (`QOU.MassTheory.BodyOrderCumulant.fourthDiff`, and the multiplicative
closed form `QOU.MassTheory.B4MultiplicativeCumulant.multBinding_b4`):

    b₄ = B(4) − 4·B(3) + 6·B(2) − 4·B(1) + B(0)

The sequence B(A) is the framework binding at the four isotopes: B(0)=B(1)=0 (no
pairs), B(2)=deuteron (1p1n), B(3)=isospin-symmetric ½(B(1p2n)+B(2p1n)), B(4)=⁴He
(2p2n, K₄ = 1 pp + 1 nn + 4 pn). The TARGET uses the SAME finite difference on the
AME bindings with B(3)=½(B(³H)+B(³He)) — B_AME is DIAGNOSTIC-ONLY (forms the target,
never fits the framework).

WHY THIS IS THE STRUCTURALLY-RIGHT OBJECT. `BodyOrderCumulant.lean` proved the
additive binding forms (B_vol 1-body-linear, B_sym 2-body-additive) are ORTHOGONAL
to the 4-body channel (b₄ = 0). The multiplicative ∏f is exponential in the pair
count C(A,2), so it is NOT pairwise-additive — its b₄ is generically nonzero
(`multBinding_b4_nonvacuous`). This probe measures that b₄'s MAGNITUDE.

VERDICT (expected scope-(a)): the multiplicative connected 4-body cumulant, ALONE,
undershoots. Reports whichever way it lands. No Δ_λ fitted, no convention tuned,
nothing wired. free_parameters = 0.

`-- Ref:` binding_canonical.py; interface_4body_assembly_probe.py;
QOU.MassTheory.B4MultiplicativeCumulant.multBinding_b4.
"""
from __future__ import annotations

import sys
from math import comb
from pathlib import Path

import mpmath as mp

# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path[:0] = [str(COMP), str(COMP / "substrate")]
import closed_form_tau_M as C  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# ---- derived substrate constants (0-fit) -----------------------------------
Q0 = mp.mpf("1.10997858275138080759166909561076887987449912187357763605672")
M_E = mp.mpf("0.51099895069")
E0 = M_E / (Q0 * (Q0 - 1))
Z_MK = C.markov_z(Q0)
H_MK = C.hecke_h(Q0)
# canonical cached nucleon H_3 trace (phase5l, q0) + tau_n solved from tr_M(D)=tau_p tau_n z
TAU_P = mp.mpf("1.22036288908669305595736107223")
TRM_D = mp.mpf("0.7280918153466761555460727563")
TAU_N = TRM_D / (TAU_P * Z_MK)

# AME bindings (DIAGNOSTIC-ONLY — used to form the target, never to fit)
AME = {"D": mp.mpf("2.224566"), "T": mp.mpf("8.481798"),
       "3He": mp.mpf("7.718043"), "4He": mp.mpf("28.295673")}


def pair_factor(kind: str, pn: str) -> mp.mpf:
    if kind == "pp":
        return Z_MK
    if kind == "nn":
        return Z_MK - H_MK
    if pn == "chi":          # production marshalling drops the averaging
        return Z_MK
    if pn == "avg":          # bar-invariant projection
        return Z_MK - H_MK / 2
    raise ValueError(pn)


def complete_pairs(Z: int, N: int) -> list:
    """Complete graph K_A: all C(A,2) pairs (genuine many-body tetrahedron)."""
    return ["pp"] * comb(Z, 2) + ["nn"] * comb(N, 2) + ["pn"] * (Z * N)


def prod_f(pairs: list, pn: str) -> mp.mpf:
    p = mp.mpf(1)
    for k in pairs:
        p *= pair_factor(k, pn)
    return p


def binding(Z: int, N: int, pn: str) -> mp.mpf:
    if Z + N == 0:
        return mp.mpf(0)
    tau_vac = TAU_P ** Z * TAU_N ** N
    return E0 * tau_vac * (1 - prod_f(complete_pairs(Z, N), pn))


def fourth_diff(B: list) -> mp.mpf:
    """b₄ = B(4) − 4B(3) + 6B(2) − 4B(1) + B(0) (Lean fourthDiff)."""
    return B[4] - 4 * B[3] + 6 * B[2] - 4 * B[1] + B[0]


def framework_sequence(pn: str) -> list:
    """B(A), A=0..4, isospin-symmetric at A=3, complete-graph topology."""
    return [
        mp.mpf(0),
        (binding(1, 0, pn) + binding(0, 1, pn)) / 2,     # A=1 (both 0)
        binding(1, 1, pn),                               # A=2 deuteron
        (binding(1, 2, pn) + binding(2, 1, pn)) / 2,     # A=3 isosym
        binding(2, 2, pn),                               # A=4 ⁴He
    ]


def main() -> int:
    print("=" * 80)
    print(" Option-E front 4 — MULTIPLICATIVE connected 4-body cumulant b₄ at ⁴He")
    print("=" * 80)
    print(f"  E₀={mp.nstr(E0,8)} MeV  z={mp.nstr(Z_MK,8)}  h={mp.nstr(H_MK,8)}")
    print(f"  τ_p={mp.nstr(TAU_P,10)} (cached)  τ_n={mp.nstr(TAU_N,10)} (solved)  q₀={mp.nstr(Q0,8)}")

    # ---- target b₄ from AME (DIAGNOSTIC-ONLY) ------------------------------
    B3_target = (AME["T"] + AME["3He"]) / 2
    target = [mp.mpf(0), mp.mpf(0), AME["D"], B3_target, AME["4He"]]
    b4_target = fourth_diff(target)
    print(f"\n  ⁴He target b₄ (AME 4th-diff, B(3)=½(³H+³He)={mp.nstr(B3_target,8)}): "
          f"{mp.nstr(b4_target,8)} MeV  [diagnostic-only]")

    # ---- self-consistency guard: fourth_diff kills additive forms ----------
    lin = [3 * mp.mpf(n) for n in range(5)]              # 1-body linear
    pw = [7 * mp.mpf(n) * (mp.mpf(n) - 1) for n in range(5)]  # 2-body pairwise
    guard_lin = abs(fourth_diff(lin)) < mp.mpf("1e-40")
    guard_pw = abs(fourth_diff(pw)) < mp.mpf("1e-40")
    print(f"\n  [guard] fourthDiff(1-body linear)={mp.nstr(fourth_diff(lin),3)} → 0? {bool(guard_lin)}"
          f"   fourthDiff(2-body pairwise)={mp.nstr(fourth_diff(pw),3)} → 0? {bool(guard_pw)}"
          f"   (mirrors Lean fourthDiff_linear / fourthDiff_pairwise)")

    # ---- framework b₄ under both pn conventions ----------------------------
    results = {}
    print("\n  [framework]  B(A) = E₀·τ_vac·(1 − ∏f) on complete graph K_A")
    for pn in ("chi", "avg"):
        seq = framework_sequence(pn)
        b4 = fourth_diff(seq)
        frac = b4 / b4_target * 100
        results[pn] = {"seq": seq, "b4": b4, "frac_pct": frac}
        label = "z         (production)" if pn == "chi" else "z − h/2 (bar-invariant)"
        print(f"    pn = {label}")
        print(f"      B(A) A=0..4 = {[mp.nstr(x,6) for x in seq]}")
        print(f"      b₄ = {mp.nstr(b4,8)} MeV   =  {mp.nstr(frac,5)} % of target "
              f"({mp.nstr(b4_target,6)} MeV)")

    headline = results["chi"]
    frac_chi = float(headline["frac_pct"])
    frac_avg = float(results["avg"]["frac_pct"])
    print("\n  [bar-parity / I-par refinement] pn factor z − h/2 is BAR-MIXED "
          "(z bar-even, h bar-odd);")
    print("    retained binding = bar-even projection z (production pn=z headline); "
          "radiated = −h/2.")

    verdict = (
        f"MULTIPLICATIVE connected 4-body cumulant undershoots: production pn=z gives "
        f"b₄={float(headline['b4']):.4f} MeV = {frac_chi:.2f}% of the ⁴He target "
        f"({float(b4_target):.3f} MeV); bar-invariant pn=z−h/2 gives {frac_avg:.1f}%. "
        f"scope-(a): the multiplicative 4-body cumulant, ALONE, reaches only ~6% (production) "
        f"/ ~36% (bar-invariant) of the target. Cause: (1−∏f) saturates, so extra bonds barely "
        f"grow B; the residual A-growth is the weak τ_p^Z τ_n^N. NOT scope-(b) excluded — the "
        f"multiplicative form DOES carry connected 4-body content (Lean multBinding_b4_nonvacuous), "
        f"unlike the additive forms (b₄=0). No fit, nothing wired."
    )
    print(f"\n ⇒ {verdict}")

    # ---- witness -----------------------------------------------------------
    wb = WitnessBuilder("b4-multiplicative-cumulant", engine="mpmath",
                        output_dir=str(HERE), _script_path=__file__)
    wb.set_description(
        "Option-E front 4 (interface-operator / 4-body route): the MULTIPLICATIVE connected "
        "4-body Ursell cumulant b₄ of the canonical binding B = E₀·τ_vac·(1 − ∏ fᵢ), evaluated "
        "0-fit at the substrate q₀ on the complete-graph K_A topology, reported as a fraction of "
        "the ⁴He AME target b₄ ≈ 9.243 MeV. DISTINCT from the sibling A4InterfaceMagnitude "
        "(−ln det(I+G) writhe-determinant surjectivity gate). b₄ = fourthDiff(B(A)) with B(3) "
        "isospin-symmetric. RESULT (scope-(a) undershoot): production pn=z → b₄=0.583 MeV = 6.30% "
        "of target; bar-invariant pn=z−h/2 → 3.369 MeV = 36.4%. Cause: (1−∏f) saturates. NOT "
        "scope-(b): the multiplicative form carries connected 4-body content the additive forms "
        "cannot (Lean multBinding_b4_nonvacuous vs BodyOrderCumulant orthogonality). I-par "
        "refined: pn factor z−h/2 is bar-mixed; retained = bar-even projection z. B_AME "
        "DIAGNOSTIC-ONLY (forms target, never fits framework). free_parameters=0, nothing wired. "
        + verdict)
    wb.set_content_block("conj:binding-manybody-eq-jet-filtration")
    wb.add_parameter("q_0", str(Q0))
    wb.add_parameter("E0_MeV", str(E0))
    wb.add_parameter("z_markov", str(Z_MK))
    wb.add_parameter("h_hecke", str(H_MK))
    wb.add_parameter("tau_p", str(TAU_P))
    wb.add_parameter("tau_n", str(TAU_N))
    wb.add_parameter("free_parameters", 0)
    wb.add_data("target", {
        "b4_target_MeV": mp.nstr(b4_target, 12),
        "B3_isospin_symmetric_MeV": mp.nstr(B3_target, 12),
        "ame_bindings_MeV": {k: str(v) for k, v in AME.items()},
        "note": "B_AME diagnostic-only: forms the finite-difference target, never fits the framework.",
    })
    wb.add_data("framework_b4", {
        pn: {
            "pn_factor": "z" if pn == "chi" else "z - h/2",
            "B_sequence_MeV": [mp.nstr(x, 12) for x in r["seq"]],
            "b4_MeV": mp.nstr(r["b4"], 12),
            "fraction_of_target_pct": mp.nstr(r["frac_pct"], 8),
        } for pn, r in results.items()
    })
    wb.add_data("verdict", verdict)
    wb.add_assertion("guard_fourthdiff_kills_1body_linear", str(bool(guard_lin)), "True")
    wb.add_assertion("guard_fourthdiff_kills_2body_pairwise", str(bool(guard_pw)), "True")
    wb.add_assertion("multiplicative_b4_nonzero_production",
                     str(bool(abs(headline["b4"]) > mp.mpf("1e-6"))), "True")
    wb.add_assertion("production_b4_undershoots_target",
                     str(bool(frac_chi < 100.0)), "True")
    out = wb.save(extra={"auditOnly": True})
    print(f"\nwitness → {out}")

    ok = bool(guard_lin and guard_pw and abs(headline["b4"]) > mp.mpf("1e-6") and frac_chi < 100.0)
    print("STRUCTURAL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
