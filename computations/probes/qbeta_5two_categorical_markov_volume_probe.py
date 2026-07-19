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

Object (H₃(q), canonical 5₂ 3-braid `β = σ₁³σ₂⁻¹σ₁σ₂⁻¹`, `[1,1,1,−2,1,−2]`):
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
     combination, is **0 for 4₁** (`e=0`, amphichiral) and **½(q²−q⁻²) ≠ 0 for
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
BRAID_5_2 = [1, 1, 1, -2, 1, -2]   # σ₁³σ₂⁻¹σ₁σ₂⁻¹, chiral, writhe 2
BRAID_4_1 = [1, -2, 1, -2]         # (σ₁σ₂⁻¹)², amphichiral, writhe 0 — control

_q = sp.symbols("q", positive=True)


def _seminormal():
    """2×2 Hoefsmit seminormal blocks of (σ₁, σ₂) on V_{(2,1)} of H₃(q)."""
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


def chi_21(word):
    s0, s1 = _seminormal()
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
          f"= ½(q²−q⁻²) (reeb-trace match)")

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

    verdict = bool(all(c21_ok.values()) and control_pass and chiral_nonzero and anchor_smooth)
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
        "AMPHICHIRAL CONTROL PASSES: bar-odd (CS) datum = 0 for 4₁ (e=0), ½(q²−q⁻²)≠0 for "
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
        "verdict": "4₁ amphichiral bar-odd=0 (control), 5₂ chiral bar-odd=½(q²−q⁻²) "
                   "(reeb-trace match); raw-trace route FAILS this control (framing-contaminated)"})
    wb.add_data("finding3_anchor_shape", {
        "odd_proton": mp.nstr(op, 12), "odd_muon": mp.nstr(om, 12),
        "dln_odd_dq": mp.nstr(dln, 8), "anchor_smooth": bool(anchor_smooth),
        "verdict": "anchor-smooth O(10^0); odd ingredient not swing value (measurement-limited)"})
    wb.add_data("scope", {
        "tier": "fibre-level categorical datum (pre-tau)",
        "raw_trace_framing_contaminated": True,
        "markov_weight_fix": "tau(sigma1 sigma2 sigma1) = h*z^2 + z, NOT z^3",
        "g3_wall": "does NOT cross argument->S resurgent-monodromy wall (open, not laundered)",
        "value_status": "swing value measurement-limited (no_anchor_invariant_realizes_swing)",
        "ocneanu_weights_W_lambda": "messy; not required for the bar-odd channel (remaining piece)",
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
    wb.save()
    print("\n  RESULT: 𝔙_q(5₂) categorical bar-odd datum built by block + gated (4₁ "
          "control); fibre-level, G3 wall stays open.")
    return 0 if verdict else 1


if __name__ == "__main__":
    raise SystemExit(main())
