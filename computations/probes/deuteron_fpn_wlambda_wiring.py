#!/usr/bin/env python3
"""Wire the deuteron `f_pn` extraction against the keystone Step-1 `W_λ` gate.

EXPLORATORY — derive-or-refute, ZERO free parameters, no production rewire.

Context (PR #2503 offer; #2507 binding anchor; #2525 gate)
----------------------------------------------------------
The s5-so3 keystone's Step-1 falsifiable gate emits, per partition `λ ⊢ n`, the
q-Plancherel weight

    W_λ = d_q(λ)² / [n]_q!          (the WRT(S³/2I) per-block weight target).

The binding side (chirality × topology probe, #2507) localized the ENTIRE light-
nuclei residual that is *not* the ⁴He α-cluster term to ONE owner-gated magnitude:
the deuteron pn-channel suppression

    f_pn = 0.588      (the value that reproduces AME B(²H) = 2.224566 MeV exactly).

The corpus already flags `f_pn = 0.588` as **owner-gated to this keystone** — "no
substrate channel lands 0.588" (`2026-06-20-chirality-forces-complete-graph-
topology.md`). This script is the offered **wiring**: it consumes whatever `W_λ`
the gate emits and extracts / checks the deuteron `f_pn` against it. The point is a
binding-side falsifiable target for the gate — a SECOND anchor besides the m_τ
lepton tower.

What this does (no fit)
-----------------------
1. Extracts the deuteron `f_pn` two parameter-free ways:
     • f_required = exp(−B_AME/E₀)            (the magnitude to explain; 0.58776)
     • f_std      = std Hecke channel z·c + d (the production-adjacent kernel; over-binds)
2. Emits the gate's `W_λ` at the deuteron level. The pn bond uses the STANDARD
   Hecke channel `V_std = z·c + d`, whose eigenvalue is the **standard
   representation**; at the Borromean level `n = 3` (where the keystone generation
   blocks live, per #2525) the standard rep is `λ = (2,1)`. So the gate's binding-
   side weight for the pn bond is `W_(2,1)` at `n = 3`.
3. WIRES: `deuteron_fpn_from_Wmap(Wmap, E0)` takes ANY `W_λ` dict at `n = 3`
   (so a future *geometric* W_λ — the open WRT realization — flows through the same
   harness) and returns the predicted pn binding. Run here against the gate's
   current *algebraic* `W_λ` as the baseline.
4. Reports the falsifiable verdict (bracket / match / refute).

Reuse (no duplication; compute-author discipline)
-------------------------------------------------
  • channel construction + E₀ + q₀  ← `hecke_channel_binding_probe`
  • the gate's `W_λ` emitter         ← `keystone_wlambda_Z_defect_n_scaling`
    (merged to main via PR #2525)

Output: deuteron-fpn-wlambda-wiring.witness.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

# Reuse the canonical channel construction (PR #2461/#2481) — q₀, E₀, the std channel.
# Same-directory module under computations/probes/, so a plain import is stable.
from hecke_channel_binding_probe import channels, BONDS, E0, Q0, h, z  # noqa: E402

mp.mp.dps = 50

AME_D = mp.mpf("2.224566")          # AME2020 B(²H), the only bound 2-nucleon system
STD_REP_N3 = (2, 1)                  # standard rep at n=3 = the pn std-channel block


# ── The gate's W_λ emitter, inlined for self-containment ─────────────────────
# W_λ = d_q(λ)² / [n]_q!  with balanced quantum integers and the q-hook-length
# formula. This is the SAME q-Plancherel weight the Step-1 gate emits
# (`docs/audits/scripts/keystone_wlambda_Z_defect_n_scaling.py`, PR #2525) — a
# textbook identity, inlined here rather than imported so this probe does NOT
# couple a computations/ probe to an audit one-off script (no canonical shared
# qdim module exists; see the audit script for the same formula).

def _qint(m, q):
    return mp.mpf(m) if q == 1 else (q ** m - q ** (-m)) / (q - q ** (-1))


def gate_qfact(n, q):
    r = mp.mpf(1)
    for k in range(1, n + 1):
        r *= _qint(k, q)
    return r


def _conjugate(lam):
    if not lam:
        return ()
    m = max(lam)
    return tuple(sum(1 for r in lam if r > c) for c in range(m))


def _hooks(lam):
    lamp = _conjugate(lam)
    hs = []
    for i, row in enumerate(lam):
        for j in range(row):
            hs.append((row - (j + 1)) + (lamp[j] - (i + 1)) + 1)
    return hs


def gate_qdim(lam, q):
    denom = mp.mpf(1)
    for hk in _hooks(lam):
        denom *= _qint(hk, q)
    return gate_qfact(sum(lam), q) / denom


def gate_partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, mx), 0, -1):
        for rest in gate_partitions(n - first, first):
            yield (first,) + rest


def gate_Z(n, q):
    fact = gate_qfact(n, q)
    return sum(gate_qdim(lam, q) ** 2 / fact for lam in gate_partitions(n))

# Substrate flavour split δ = Δm_{n−p}/M_N for the Bring-color-weighted convention.
M_P = mp.mpf("938.27208943")
M_N_ = mp.mpf("939.56542194")
M_N_MEAN = (M_P + M_N_) / 2
DELTA = (M_N_ - M_P) / M_N_MEAN


def bring_color_weighted_fpn():
    """The PRODUCTION Bring-color-weighted pn factor (not the abstract std channel).

    `f_pn = z − h·(½ − δ/4)`, `z = √q/(q+1)`, `δ = Δm_{n−p}/M_N` — the substrate-pure
    realisation documented at `closed_form_tau_M.py::pn_convention="bring_color_weighted"`
    and `prearchimedean_bond_factor.py`, and named in the inter-nucleon-channel-color-tube
    Lean block. This is the Bring-color leg; it still rides `z = √q/(q+1)`, NOT the
    coral-fibre coordinate `z₀ = √q − 1/√q` where the open *geometric* W_λ lives.
    """
    return z - h * (mp.mpf(1) / 2 - DELTA / 4)


def gate_W(lam, q):
    """The gate's q-Plancherel weight W_λ = d_q(λ)² / [n]_q! (n = |λ|)."""
    return gate_qdim(lam, q) ** 2 / gate_qfact(sum(lam), q)


def deuteron_fpn_from_Wmap(Wmap: dict, E0_=E0, ame=AME_D) -> dict:
    """Predict the deuteron pn binding from a gate-emitted ``W_λ`` map at n=3.

    ``Wmap`` is ``{partition: weight}`` for ``λ ⊢ 3`` — whatever the Step-1 gate
    emits (the current *algebraic* ``d_q²/[n]_q!`` here; a future *geometric*
    WRT(S³/2I) realization plugs in unchanged). To keep that "plugs in unchanged"
    promise honest across sources, the key is accepted either as the tuple
    ``(2, 1)`` (in-process emitter) or its string form ``"(2, 1)"`` (a witness
    JSON round-trip), and the weight is coerced to ``mp.mpf`` (JSON serializes it
    as a string). The deuteron pn bond rides the standard channel ``V_std``, whose
    block is the standard rep ``λ = (2,1)``, so the gate's binding-side magnitude
    for that bond is ``W_(2,1)``.

    Units: ``ame`` and ``E_pred`` are both MeV — ``E_pred = E0_·ln(1/W)`` with
    ``E0_`` in MeV and ``ln(1/W)`` dimensionless — so they are compared directly;
    ``ame`` is NOT rescaled by ``E0_``.
    """
    raw_w = Wmap.get(STD_REP_N3, Wmap.get(str(STD_REP_N3)))
    if raw_w is None:
        raise KeyError(f"standard-rep block {STD_REP_N3} not found in Wmap")
    w = mp.mpf(raw_w)
    f_req = mp.exp(-ame / E0_)
    bound = (0 < w < 1)
    E_pred = E0_ * mp.log(1 / w) if bound else None
    return {
        "block": STD_REP_N3,
        "f_pn_pred": w,
        "bound": bool(bound),
        "E_pred_MeV": E_pred,
        "miss_E_pct": (abs(E_pred - ame) / ame * 100 if E_pred is not None else None),
        "miss_f_pct": abs(w - f_req) / f_req * 100,
    }


def main() -> int:
    f_required = mp.exp(-AME_D / E0)
    f_std = channels(*BONDS["pn"])["std"]          # z·1 + (−h/2)
    E_std = E0 * mp.log(1 / f_std)

    # The gate's algebraic W_λ at the deuteron level (n=3).
    Wmap3 = {lam: gate_W(lam, Q0) for lam in gate_partitions(3)}
    Z3 = gate_Z(3, Q0)

    pred = deuteron_fpn_from_Wmap(Wmap3)

    print("=" * 84)
    print("  Deuteron f_pn  ×  keystone Step-1 W_λ gate  —  wiring probe (EXPLORATORY, no fit)")
    print(f"  q₀ = {mp.nstr(Q0, 12)}   E₀ = m_e/(q₀(q₀−1)) = {mp.nstr(E0, 8)} MeV")
    print("=" * 84)

    print("\n  [1] Deuteron f_pn extraction (parameter-free):")
    print(f"      f_required = exp(−B_AME/E₀) = {mp.nstr(f_required, 8)}"
          f"   → E = {mp.nstr(AME_D, 7)} MeV  (= AME, the magnitude to explain)")
    print(f"      f_std      = z·c + d        = {mp.nstr(f_std, 8)}"
          f"   → E = {mp.nstr(E_std, 7)} MeV  (over-binds "
          f"{mp.nstr((E_std - AME_D) / AME_D * 100, 4)}%)")

    print(f"\n  [2] Gate W_λ at the deuteron level (n=3, Σ = Z(3) = {mp.nstr(Z3, 8)}):")
    for lam in gate_partitions(3):
        w = Wmap3[lam]
        tag = "  ← pn std-channel block (standard rep)" if lam == STD_REP_N3 else ""
        print(f"      W_{str(lam):<10} = {mp.nstr(w, 8):>10}   d_q = "
              f"{mp.nstr(gate_qdim(lam, Q0), 7)}{tag}")
    # Exact leading defect coefficient (sibling closed form, PR #2536-era):
    #   1 − Z(n) = C(n)·h² + O(h⁴),  C(n) = −n(n−1)(2n−13)/144.
    # At the deuteron level n=3 this is C(3) = 7/24 — the geometric W_λ must
    # reproduce this exact defect structure (and the sign change at n=7), not
    # just the per-block weights.
    C3 = mp.mpf(-3 * 2 * (2 * 3 - 13)) / 144
    print(f"      defect 1−Z(3) = {mp.nstr(1 - Z3, 7)}  =  C(3)·h² + O(h⁴),  "
          f"C(3) = 7/24 = {mp.nstr(C3, 7)}  (closed form C(n)=−n(n−1)(2n−13)/144;")
    print(f"        C(3)·h² = {mp.nstr(C3 * h ** 2, 7)}; sign change at n=7 — the geometric "
          "target the W_λ realization must also reproduce)")

    print("\n  [3] Wiring  f_pn  ←  W_(2,1):")
    print(f"      f_pn_pred (gate algebraic W_(2,1)) = {mp.nstr(pred['f_pn_pred'], 8)}"
          f"   → E = {mp.nstr(pred['E_pred_MeV'], 7)} MeV"
          f"  (under-binds {mp.nstr((AME_D - pred['E_pred_MeV']) / AME_D * 100, 4)}%)")
    print(f"      miss vs required f_pn = {mp.nstr(pred['miss_f_pct'], 4)}%   "
          f"miss vs AME binding = {mp.nstr(pred['miss_E_pct'], 4)}%")

    # ---- [2b] Bring-coordinate cross-check (NOT just the algebraic weight) ---
    f_bring = bring_color_weighted_fpn()
    E_bring = E0 * mp.log(1 / f_bring)
    z0_coral = mp.sqrt(Q0) - 1 / mp.sqrt(Q0)         # Bring coral-fibre coordinate
    kappa_b3 = mp.mpf(3) / 16                          # Yekutieli Stokes h²-action of 𝓑₃
    trM_b3 = mp.mpf("1.00673")                         # tr_M(𝓑₃,q₀) (Yekutieli extraction)
    print("\n  [2b] Bring-coordinate cross-check (does the GEOMETRY land 0.588, "
          "not just the algebraic W_λ?):")
    print(f"      bond-factor coordinate   z = √q/(q+1)        = {mp.nstr(z, 8)}  "
          "(what every f = c·z + d factor uses)")
    print(f"      coral-fibre coordinate   z₀ = √q − 1/√q      = {mp.nstr(z0_coral, 8)}  "
          "(where the OPEN geometric W_λ lives — UNUSED by any f_pn compute)")
    print(f"      Bring-color-weighted f_pn = z − h(½ − δ/4)   = {mp.nstr(f_bring, 8)}  "
          f"→ E = {mp.nstr(E_bring, 7)} MeV  (δ = {mp.nstr(DELTA, 4)}; over-binds)")
    print(f"      Yekutieli Stokes 𝓑₃: h²-action κ = 3/16 = {mp.nstr(kappa_b3, 6)}, "
          f"tr_M(𝓑₃,q₀) = {mp.nstr(trM_b3, 6)} (an ACTION/trace > 1, not a per-bond f<1)")
    print("      ⇒ the production Bring-color convention gives 0.395 — the SAME lower")
    print("        bracket as the abstract std channel (δ-split ~0.001 is negligible);")
    print("        no available compute, algebraic OR Bring-coordinate, lands 0.588.")

    # ---- falsifiable verdict ------------------------------------------------
    brackets = (f_std < f_required < pred["f_pn_pred"])
    bring_on_lower_bracket = abs(f_bring - f_std) < mp.mpf("0.01")
    print("\n  [4] VERDICT (falsifiable, derive-or-refute):")
    print(f"      bracket  f_std < f_required < W_(2,1)  :  "
          f"{mp.nstr(f_std, 6)} < {mp.nstr(f_required, 6)} < "
          f"{mp.nstr(pred['f_pn_pred'], 6)}   → {'YES' if brackets else 'NO'}")
    print("      • The bare std channel OVER-binds (0.395, E 3.89); the gate's")
    print("        q-Plancherel weight W_(2,1) UNDER-binds (0.661, E 1.74). The")
    print("        required magnitude 0.588 (E 2.22) sits strictly BETWEEN them.")
    print("      • So the *algebraic* W_λ the gate emits does NOT by itself land")
    print("        f_pn = 0.588 (REFUTE for the naive direct-weight map) — but it")
    print("        BRACKETS it from above, the std channel from below. This is the")
    print("        binding-side target the *geometric* W_λ realization (WRT(S³/2I),")
    print("        still owner-gated) must hit: f_pn = 0.58776, E = 2.2246 MeV,")
    print(f"        inside the open interval ({mp.nstr(f_std, 5)}, "
          f"{mp.nstr(pred['f_pn_pred'], 5)}).")
    print("      • To test a geometric W_λ: pass its emitted {λ:weight} dict at")
    print("        n=3 to deuteron_fpn_from_Wmap(); the same harness reports the")
    print("        refute/match against AME with no further wiring.")

    witness = {
        "computation": "deuteron-fpn-wlambda-wiring",
        "kind": "exploratory-probe",
        "description": (
            "Wires the owner-gated deuteron f_pn = 0.588 magnitude against the "
            "keystone Step-1 W_λ = d_q²/[n]_q! gate. Extracts f_pn (required / std) "
            "and the gate's W_(2,1) at n=3 (the pn std-channel block), reports the "
            "falsifiable bracket. Reuses hecke_channel_binding_probe (channel) and "
            "keystone_wlambda_Z_defect_n_scaling (W_λ emitter, PR #2525). No fit."
        ),
        "engine": "mpmath", "dps": 50,
        "q0": str(Q0), "E0_MeV": str(E0),
        "ame_B_deuteron_MeV": str(AME_D),
        "f_pn_required": str(f_required),
        "f_pn_std_channel": str(f_std),
        "E_std_channel_MeV": str(E_std),
        "gate_Wlambda_n3": {str(lam): str(Wmap3[lam]) for lam in gate_partitions(3)},
        "gate_Z3": str(Z3),
        "gate_defect_closed_form": {
            "formula": "1 - Z(n) = C(n)*h^2 + O(h^4), C(n) = -n(n-1)(2n-13)/144",
            "C3": str(C3),
            "C3_times_h2": str(C3 * h ** 2),
            "defect_Z3": str(1 - Z3),
            "sign_change_n": 7,
            "note": ("Exact leading defect coefficient (sibling closed form). The "
                     "geometric W_λ realization must reproduce this Z(n) structure "
                     "(C(3)=7/24, sign change at n=7), not just the per-block weights."),
        },
        "pn_block": str(STD_REP_N3),
        "f_pn_pred_from_gate_Wlambda": str(pred["f_pn_pred"]),
        "E_pred_from_gate_Wlambda_MeV": str(pred["E_pred_MeV"]),
        "miss_f_pct_vs_required": str(pred["miss_f_pct"]),
        "miss_E_pct_vs_AME": str(pred["miss_E_pct"]),
        "bracket_fstd_lt_freq_lt_W21": bool(brackets),
        "bring_coordinate_crosscheck": {
            "z_markov_bond_factor": str(z),
            "z0_coral_fibre": str(z0_coral),
            "f_pn_bring_color_weighted": str(f_bring),
            "E_bring_MeV": str(E_bring),
            "delta_flavour_split": str(DELTA),
            "yekutieli_b3_stokes_kappa": str(kappa_b3),
            "trM_b3_q0": str(trM_b3),
            "bring_color_on_lower_bracket": bool(bring_on_lower_bracket),
            "note": (
                "The PRODUCTION Bring-color-weighted convention (f_pn=z−h(½−δ/4), "
                "closed_form_tau_M.py::bring_color_weighted) gives 0.39486 — the same "
                "lower bracket as the abstract std channel (δ-split negligible). It "
                "rides z=√q/(q+1), NOT the coral-fibre z₀=√q−1/√q (0.10439) where the "
                "open geometric W_λ lives. The genuine Bring-surface geometric object "
                "that DOES exist (Yekutieli non-abelian Stokes h²-action of 𝓑₃, "
                "κ=3/16, tr_M(𝓑₃,q₀)=1.00673) is an action/trace >1, not a per-bond "
                "suppression. So no available compute — algebraic OR Bring-coordinate "
                "— lands 0.588; it remains the open coral-fibre (z₀) geometric W_λ."
            ),
        },
        "verdict": (
            "REFUTE (naive direct-weight map): the algebraic W_λ the gate emits "
            "under-binds (W_(2,1)=0.661, E=1.74) while the std channel over-binds "
            "(0.395, E=3.89); the required f_pn=0.58776 (E=2.2246) is strictly "
            "bracketed between them. The magnitude stays owner-gated to the "
            "GEOMETRIC W_λ realization (WRT(S³/2I)), for which this is now a sharp, "
            "second binding-side falsifiable target alongside the m_τ tower: any "
            "index reproducing W_λ must land f_pn in (0.395, 0.661) and at 0.58776."
        ),
        "discipline": "EXPLORATORY — derive-or-refute, zero free parameters, no production rewire.",
        "refs": [
            "PR #2503 (DG attack plan + f_pn wiring offer)",
            "PR #2507 (chirality × topology binding; f_pn=0.588 localization)",
            "PR #2525 (W_λ Z(n) defect gate emitter)",
            "docs/audits/2026-06-20-chirality-forces-complete-graph-topology.md",
            "docs/coordination/s5-so3-keystone.md",
        ],
    }
    out = HERE.parent / "deuteron-fpn-wlambda-wiring.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness: {out}")
    print("=" * 84)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
