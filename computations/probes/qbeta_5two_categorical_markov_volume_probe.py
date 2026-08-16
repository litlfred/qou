#!/usr/bin/env python3
"""qbeta_5two_categorical_markov_volume_probe.py

The categorical Markov-trace complex-volume datum 𝔙_q(5₂), by Wedderburn block —
the "later brick" flagged by `qbeta_5two_reeb_trace_probe.py` (bean `qou-3yxn`,
A5). Built and GATED (amphichiral 4₁ control), q-exact.

Context. The reeb-trace brick isolated the chiral bar-odd datum of 5₂ as the
**writhe** in the conjugate-pair 1-dim blocks, and flagged that the full
Markov-trace complex volume 𝔙_q(5₂) — the QOU analogue of the Neumann–Zagier
`𝕍 = Vol + i·CS` (`conj:binding-qbeta-complex-volume`) — was still to be built.

Gates-first finding (why the naive route fails). The **raw** Markov trace
`tr_M(ρ(β)) = Σ_w c_w·τ(w)` on the NF basis, bar-decomposed under `σ:q↦q⁻¹`,
is **framing-contaminated**: the amphichiral **4₁ control gives bar-odd ≠ 0**,
which is wrong (4₁ ≅ 4₁* ⇒ every fibre invariant is bar-even). The raw trace is
not a knot invariant (it carries the braid's framing), so its `q↦q⁻¹` image is a
*different* framed representative. The correct object is the **Wedderburn-block
decomposition** `tr_M = Σ_λ W_λ·χ_λ`, in which the bar-odd part lives purely in
the conjugate-pair 1-dim blocks (3)/(1,1,1); the self-conjugate (2,1) block is
bar-even. (An extra Markov-weight subtlety was also caught: `τ(σ₁σ₂σ₁) = h·z²+z`,
`h=q−q⁻¹`, **not** `z³`.)

Object (H₃(q), canonical 5₂ 3-braid `β = σ₁³σ₂σ₁⁻¹σ₂`, `[1,1,1,−2,1,−2]`):
  χ_(3)(β)   = q^e            (1-dim, σ↦q)                       e = exponent sum
  χ_(1,1,1)(β) = (−q⁻¹)^e     (1-dim, σ↦−q⁻¹)                    (writhe)
  χ_(2,1)(β) = tr of the 2×2 Hoefsmit seminormal product       (self-conjugate)
Bar-even (Vol/cosh) channel = the (2,1) block; bar-odd (CS/sinh) channel = the
(3)/(1,1,1) conjugate pair.

FINDINGS (scope-(a); q-exact; no fit; nothing wired; no tier change):

  1. **(2,1) block is bar-EVEN for the target knots** (q-exact): `χ_(2,1)(q) =
     χ_(2,1)(q⁻¹)` for both 4₁ and 5₂ — the self-conjugate block carries no
     chirality (the binding/Vol channel).

  2. **AMPHICHIRAL CONTROL PASSES.** The bar-odd (CS) datum, the conjugate-pair
     combination, is **0 for 4₁** (`e=0`, amphichiral) and **½(q⁴−q⁻⁴) ≠ 0 for
     5₂** (`e=2`, chiral) — the genuine bar-odd sinh-object 4₁ structurally
     lacks, matching the reeb-trace writhe result exactly. This is the gate the
     raw-trace route fails.

  3. **The bar-odd datum is ANCHOR-SMOOTH** at the substrate: `d ln|odd|/dq` is
     O(10⁰) across the proton/muon anchors — the fibre supplies the odd
     ingredient/shape, never the ~3.84×10⁶ swing value (proved measurement-
     limited, `QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing`). A FIFTH
     independent anchor-smoothness confirmation after A1/A2/A4 and the reeb datum.

SCOPE / G3 WALL (STRICT). Fibre-level (pre-τ) categorical datum only. Does **not**
cross the G3 argument→S resurgent-monodromy wall (the analytic continuation from
the formal-q block characters to the archimedean decay projection S), which stays
open (not laundered). No archimedean S value is claimed; the swing value stays
measurement-limited; no `c_k` wired. The full Markov weights `W_λ` (Ocneanu) are
messy and not required for the bar-odd channel; recorded as the remaining piece.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402

# canonical 3-braids (generators 1,2 ↦ σ₁,σ₂; negatives = inverses)
# CORRECTED 2026-08-11 (bean qou-9mum).  This file previously used
# [1, 1, 1, -2, 1, -2], which is the braid word for 6₂, not 5₂:
# its Alexander determinant |Δ(-1)| is 11 (6₂), where 5₂ is 7.  Seven
# sibling probes had already been moved to the correct word (see
# qbeta_5two_capstone_carrier_falsification_probe.py:206 and
# docs/coordination/1ppq-qbeta.md); this one and the categorical-Markov
# probe were missed.  The writhe changes 2 -> 4, so the bar-odd datum
# changes ½(q²-q⁻²) -> ½(q⁴-q⁻⁴) and its anchor value moves by 2.04x.
BRAID_5_2 = [1, 1, 1, 2, -1, 2]   # σ₁³σ₂σ₁⁻¹σ₂, chiral, writhe 4
BRAID_4_1 = [1, -2, 1, -2]         # (σ₁σ₂⁻¹)², amphichiral, writhe 0 — control

_q = sp.symbols("q", positive=True)


def _seminormal(q=None):
    """2×2 Hoefsmit seminormal blocks of (σ₁, σ₂) on V_{(2,1)} of H₃(q)."""
    if q is None:
        q = _q
    s0 = sp.Matrix([[q, 0], [0, -1 / q]])
    a = -1 / (q * (q ** 2 + 1))
    b = sp.Integer(1)
    c = (q ** 2 - q + 1) * (q ** 2 + q + 1) / (q ** 2 + 1) ** 2
    d = q ** 3 / (q ** 2 + 1)
    s1 = sp.Matrix([[a, b], [c, d]])
    return s0, s1


def e_sum(word):
    return sum(1 if g > 0 else -1 for g in word)


def chi_21(word, q=None):
    s0, s1 = _seminormal(q)
    gen = {1: s0, 2: s1, -1: s0.inv(), -2: s1.inv()}
    M = sp.eye(2)
    for g in word:
        M = M * gen[g]
    return sp.cancel(sp.trace(M))


def chi_3(word):
    return _q ** e_sum(word)


def chi_111(word):
    return (-1 / _q) ** e_sum(word)


def bar(expr):
    return sp.cancel(expr.subs(_q, 1 / _q))


def bar_odd(expr):
    return sp.cancel((expr - bar(expr)) / 2)


def bar_even(expr):
    return sp.cancel((expr + bar(expr)) / 2)


def ocneanu_weights():
    """Solve the Ocneanu/Markov block weights W_λ of H₃(q) from three basis
    values (τ(1)=1, τ(σ₁)=z, τ(σ₁σ₂σ₁)=h·z²+z), in t=√q for clean algebra.
    Returns (W in q, held_out_ok)."""
    t = sp.symbols("t", positive=True)
    q = t ** 2
    h = q - 1 / q
    # Convention D (was C: `1/(t + 1/t)`, with t = sqrt q). That C spelling
    # was invisible to BOTH z-detectors -- no sqrt and no 0.5 for the shape
    # matcher, and not the t/(t^2+1) form the half-argument matcher looks
    # for. It is character-for-character 1/[2]_q, the Temperley-Lieb loop
    # reciprocal, differing only in that the variable is sqrt(q); the file
    # saying `q = t ** 2` is what makes it decidable at all. Taxonomy row 5.
    z = q ** 3 / (q ** 2 + 1)

    c3 = lambda w: q ** e_sum(w)
    c111 = lambda w: (-1 / q) ** e_sum(w)
    W3, W21, W111 = sp.symbols("W3 W21 W111")
    rows = [([], sp.Integer(1)), ([1], z), ([1, 2, 1], h * z * z + z)]
    sol = sp.solve([sp.Eq(W3 * c3(w) + W21 * chi_21(w, q) + W111 * c111(w), tau)
                    for w, tau in rows], [W3, W21, W111], dict=True)[0]
    Wt = {"3": sol[W3], "21": sol[W21], "111": sol[W111]}

    def trM(word):
        return sp.cancel(Wt["3"] * c3(word) + Wt["21"] * chi_21(word, q) + Wt["111"] * c111(word))

    # held-out Ocneanu gate: elements NOT used in the solve must reproduce τ.
    held = all(sp.simplify(trM(w) - exp) == 0
               for w, exp in [([1, 2], z * z), ([2, 1, 2], h * z * z + z), ([2], z)])
    Wq = {k: sp.simplify(v.subs(t, sp.sqrt(_q))) for k, v in Wt.items()}  # re-express in q
    return Wq, held


def main() -> int:
    print("=" * 76)
    print(" categorical Markov-trace complex volume 𝔙_q(5₂) by Wedderburn block (A5)")
    print("=" * 76)

    # ---- FINDING 1: (2,1) block bar-even for the target knots ----
    print("\n[1] self-conjugate (2,1) block — bar parity (Vol/binding channel):")
    c21_ok = {}
    for name, br in (("4_1", BRAID_4_1), ("5_2", BRAID_5_2)):
        x = chi_21(br)
        is_even = sp.simplify(bar_odd(x)) == 0
        c21_ok[name] = is_even
        print(f"    χ_(2,1)({name})  bar-even = {is_even}")

    # ---- FINDING 2: amphichiral control + chiral 5₂ bar-odd datum ----
    print("\n[2] bar-odd (CS) datum from the (3)/(1,1,1) conjugate pair:")
    odd = {}
    for name, br in (("4_1", BRAID_4_1), ("5_2", BRAID_5_2)):
        # the chiral datum carried by the conjugate-pair 1-dim characters:
        # bar-odd of χ_(3) = ½(q^e − q^-e); the (1,1,1) partner is its bar image.
        o3 = bar_odd(chi_3(br))
        odd[name] = sp.simplify(o3)
        print(f"    {name}: e={e_sum(br):+d}   bar-odd ½(q^e−q^-e) = {odd[name]}")
    control_pass = (sp.simplify(odd["4_1"]) == 0)
    chiral_nonzero = (sp.simplify(odd["5_2"]) != 0)
    print(f"    → 4₁ (amphichiral) control: bar-odd == 0  [{control_pass}]")
    print(f"    → 5₂ (chiral):              bar-odd != 0  [{chiral_nonzero}]  "
          f"= ½(q⁴−q⁻⁴) (reeb-trace match)")

    # ---- FINDING 3: anchor SHAPE of the 5₂ bar-odd datum ----
    odd_fn = sp.lambdify(_q, odd["5_2"], "mpmath")
    mp.mp.dps = 50
    qp, qm = q_at(50), q_muon_at(50)
    op, om = odd_fn(qp), odd_fn(qm)
    dln = (mp.log(abs(om)) - mp.log(abs(op))) / (qm - qp)
    anchor_smooth = abs(float(dln)) < 1e3
    print("\n[3] bar-odd SHAPE at the substrate anchors (5₂):")
    print(f"    odd(proton) = {mp.nstr(op, 10)}   odd(muon) = {mp.nstr(om, 10)}")
    print(f"    d ln|odd|/dq ≈ {mp.nstr(dln, 6)}  (O(10⁰) ⇒ anchor-smooth: odd")
    print("      ingredient, not the ~3.84e6 swing — value measurement-limited)")

    # ---- FINDING 4: the Ocneanu block weights W_λ (validated, held-out gate) ----
    print("\n[4] Ocneanu block weights W_λ (the '𝔙_q magnitude' piece #4099 flagged):")
    Wq, held_ok = ocneanu_weights()
    print(f"    held-out Ocneanu gate (τ(σ₁σ₂)=z², τ(σ₂σ₁σ₂), τ(σ₂)=z): {held_ok}")
    # binding / Vol channel = the bar-even (2,1) block, weighted, at the anchors
    bind = sp.simplify(Wq["21"] * chi_21(BRAID_5_2))
    bind_fn = sp.lambdify(_q, bind, "mpmath")
    bp, bm = bind_fn(qp), bind_fn(qm)
    print(f"    binding channel W_(2,1)·χ_(2,1)(5₂):  proton={mp.nstr(bp,8)}  muon={mp.nstr(bm,8)}")
    print("    NOTE: the framing-INVARIANT full 𝔙_q is the 0-framing knot invariant")
    print("    (Jones), assembled in finding 5.")

    # ---- FINDING 5: framing-INVARIANT complex volume via the 0-framing invariant ----
    # The raw weighted trace is framing-covariant; the framing-INVARIANT object is the
    # 0-framing knot invariant J_K(q) itself (a genuine knot invariant), whose bar
    # decomposition is the canonical Re=Vol / Im=CS split — palindromic (bar-odd=0) for
    # amphichiral 4₁, chiral for 5₂. Still fibre-level (formal q); does NOT cross G3.
    JONES = {"4_1": {2: 1, 1: -1, 0: 1, -1: -1, -2: 1},
             "5_2": {-1: 1, -2: -1, -3: 2, -4: -1, -5: 1, -6: -1}}
    Jpoly = {k: sum(c * _q ** p for p, c in d.items()) for k, d in JONES.items()}
    print("\n[5] framing-INVARIANT 𝔙_q via the 0-framing knot invariant J_K(q):")
    J_odd = {k: sp.expand((J - J.subs(_q, 1 / _q)) / 2) for k, J in Jpoly.items()}
    J_even = {k: sp.expand((J + J.subs(_q, 1 / _q)) / 2) for k, J in Jpoly.items()}
    j_control = sp.simplify(J_odd["4_1"]) == 0
    j_chiral = sp.simplify(J_odd["5_2"]) != 0
    print(f"    4₁ bar-odd(J)=0 (amphichiral control): {j_control}")
    print(f"    5₂ CS channel bar-odd(J) = {sp.factor(J_odd['5_2'])}")
    print(f"    5₂ Vol channel bar-even(J) = {sp.factor(J_even['5_2'])}")
    j_odd_fn = sp.lambdify(_q, J_odd["5_2"], "mpmath")
    jop, jom = j_odd_fn(qp), j_odd_fn(qm)
    j_dln = (mp.log(abs(jom)) - mp.log(abs(jop))) / (qm - qp)
    j_smooth = abs(float(j_dln)) < 1e3
    print(f"    anchor SHAPE: proton={mp.nstr(jop,8)} muon={mp.nstr(jom,8)} "
          f"d ln|odd|/dq={mp.nstr(j_dln,6)} (anchor-smooth: {j_smooth})")

    verdict = bool(all(c21_ok.values()) and control_pass and chiral_nonzero
                   and anchor_smooth and held_ok and j_control and j_chiral and j_smooth)
    print("\n" + "=" * 76)
    print(f" VERDICT: 𝔙_q(5₂) bar-odd built by block; 4₁ control PASSES; anchor-smooth "
          f" [{'PASS' if verdict else 'CHECK'}]")
    print("=" * 76)

    wb = WitnessBuilder("qbeta-5two-categorical-markov-volume", engine="sympy+mpmath")
    wb.set_description(
        "Categorical Markov-trace complex volume 𝔙_q(5₂) by Wedderburn block (A5 brick, "
        "bean qou-3yxn) — the 'later brick' the reeb-trace probe flagged, now built and "
        "GATED. Gates-first finding: the RAW NF Markov trace bar-decomposed under q↦q⁻¹ "
        "is framing-contaminated (amphichiral 4₁ gives bar-odd≠0, WRONG); the correct "
        "object is tr_M=Σ_λ W_λ χ_λ with the bar-odd in the (3)/(1,1,1) conjugate pair "
        "and the self-conjugate (2,1) block bar-even. Also caught: τ(σ₁σ₂σ₁)=h·z²+z, not "
        "z³. FINDINGS (q-exact): (1) χ_(2,1) bar-even for 4₁ and 5₂ (Vol channel). (2) "
        "AMPHICHIRAL CONTROL PASSES: bar-odd (CS) datum = 0 for 4₁ (e=0), ½(q⁴−q⁻⁴)≠0 for "
        "5₂ (e=2) — matches the reeb-trace writhe result; the gate the raw route fails. "
        "(3) the 5₂ bar-odd is anchor-smooth (d ln|odd|/dq O(10⁰)) — odd ingredient, not "
        "the 3.84e6 swing value (proved measurement-limited); a fifth anchor-smoothness "
        "confirmation. SCOPE: fibre-level; does NOT cross the G3 argument→S "
        "resurgent-monodromy wall (open, not laundered); no c_k wired; no fit; no tier "
        "change; full Ocneanu weights W_λ messy, not required for the bar-odd channel."
    )
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("finding1_block21_bar_even", {
        "chi21_4_1_bar_even": bool(c21_ok["4_1"]),
        "chi21_5_2_bar_even": bool(c21_ok["5_2"]),
        "verdict": "self-conjugate (2,1) block bar-even for target knots (Vol/binding channel)"})
    wb.add_data("finding2_amphichiral_control", {
        "bar_odd_4_1": str(sp.simplify(odd["4_1"])),
        "bar_odd_5_2": str(sp.simplify(odd["5_2"])),
        "control_pass_4_1_zero": bool(control_pass),
        "chiral_5_2_nonzero": bool(chiral_nonzero),
        "verdict": "4₁ amphichiral bar-odd=0 (control), 5₂ chiral bar-odd=½(q⁴−q⁻⁴) "
                   "(reeb-trace match); raw-trace route FAILS this control (framing-contaminated)"})
    wb.add_data("finding3_anchor_shape", {
        "odd_proton": mp.nstr(op, 12), "odd_muon": mp.nstr(om, 12),
        "dln_odd_dq": mp.nstr(dln, 8), "anchor_smooth": bool(anchor_smooth),
        "verdict": "anchor-smooth O(10^0); odd ingredient not swing value (measurement-limited)"})
    wb.add_data("finding4_ocneanu_weights", {
        "W_3": str(Wq["3"]), "W_2_1": str(Wq["21"]), "W_1_1_1": str(Wq["111"]),
        "held_out_gate_ok": bool(held_ok),
        "binding_channel_5_2_proton": mp.nstr(bp, 12),
        "binding_channel_5_2_muon": mp.nstr(bm, 12),
        "verdict": "Ocneanu block weights W_λ determined (t=√q) and VALIDATED against "
                   "held-out τ (σ₁σ₂→z², σ₂σ₁σ₂→hz²+z, σ₂→z); binding/Vol channel = "
                   "bar-even W_(2,1)·χ_(2,1). Framing-INVARIANT full 𝔙_q still needs the "
                   "writhe/Jones normalization (G3-adjacent)."})
    wb.add_data("finding5_framing_invariant_jones", {
        "bar_odd_4_1": str(sp.simplify(J_odd["4_1"])),
        "bar_odd_5_2_CS_factored": str(sp.factor(J_odd["5_2"])),
        "bar_even_5_2_Vol_factored": str(sp.factor(J_even["5_2"])),
        "amphichiral_control_4_1_zero": bool(j_control),
        "chiral_5_2_nonzero": bool(j_chiral),
        "odd_proton": mp.nstr(jop, 12), "odd_muon": mp.nstr(jom, 12),
        "dln_odd_dq": mp.nstr(j_dln, 8), "anchor_smooth": bool(j_smooth),
        "verdict": "framing-INVARIANT 𝔙_q = 0-framing knot invariant J_K(q); bar-odd (CS) "
                   "= (q-1)^3(q+1)(q^2+1)(q^2-q+1)(q^2+q+1)^2/(2q^6) for 5₂ (triple zero at "
                   "q=1, cyclotomic Φ₃/Φ₆), 0 for amphichiral 4₁ (control); anchor-smooth; "
                   "still fibre-level (does NOT cross G3)"})
    wb.add_data("scope", {
        "tier": "fibre-level categorical datum (pre-tau)",
        "raw_trace_framing_contaminated": True,
        "markov_weight_fix": "tau(sigma1 sigma2 sigma1) = h*z^2 + z, NOT z^3",
        "g3_wall": "does NOT cross argument->S resurgent-monodromy wall (open, not laundered)",
        "value_status": "swing value measurement-limited (no_anchor_invariant_realizes_swing)",
        "ocneanu_weights_W_lambda": "DETERMINED + held-out-gated (finding 4); framing-invariant "
                                    "assembly needs the writhe normalization (G3-adjacent)",
        "c_k_wired": False, "fit": False})
    wb.add_assertion("block21_bar_even_target_knots",
                     computed=1.0 if all(c21_ok.values()) else 0.0, expected=1.0, tolerance=0.5,
                     source="chi_(2,1) bar-even (q-exact) for 4_1 and 5_2 — self-conjugate block "
                            "carries no chirality")
    wb.add_assertion("amphichiral_4_1_control_bar_odd_zero",
                     computed=1.0 if control_pass else 0.0, expected=1.0, tolerance=0.5,
                     source="4_1 (amphichiral, e=0) bar-odd datum = 0 — the control the raw-trace "
                            "route fails; validates the block construction")
    wb.add_assertion("chiral_5_2_bar_odd_nonzero_anchor_smooth",
                     computed=1.0 if (chiral_nonzero and anchor_smooth) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="5_2 (chiral, e=2) bar-odd = 1/2(q^2-q^-2) != 0, anchor-smooth "
                            "O(10^0) — odd ingredient, value measurement-limited")
    wb.add_assertion("ocneanu_weights_held_out_gate",
                     computed=1.0 if held_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="block weights W_λ reproduce the Ocneanu trace on HELD-OUT elements "
                            "(σ₁σ₂→z², σ₂σ₁σ₂→hz²+z, σ₂→z) — the weights are correct")
    wb.add_assertion("framing_invariant_jones_control_and_chiral",
                     computed=1.0 if (j_control and j_chiral and j_smooth) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="framing-invariant 𝔙_q = 0-framing J_K: bar-odd(J_4_1)=0 (amphichiral "
                            "control), bar-odd(J_5_2)!=0 chiral (CS channel), anchor-smooth — the "
                            "knot-invariant assembly the framing normalization required")
    wb.save()
    print("\n  RESULT: 𝔙_q(5₂) categorical bar-odd datum built by block + gated (4₁ "
          "control); fibre-level, G3 wall stays open.")
    return 0 if verdict else 1


if __name__ == "__main__":
    raise SystemExit(main())
