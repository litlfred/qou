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
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "docs" / "audits" / "scripts"))

# Reuse the canonical channel construction (PR #2461/#2481) — q₀, E₀, the std channel.
from hecke_channel_binding_probe import channels, BONDS, E0, Q0, h, z  # noqa: E402

# Reuse the gate's W_λ emitter exactly as merged in PR #2525 (no re-implementation):
# qdim / qfact / partitions / Z are the gate primitives; W_λ = d_q² / [n]_q!.
from keystone_wlambda_Z_defect_n_scaling import (  # noqa: E402
    Z as gate_Z,
    partitions as gate_partitions,
    qdim as gate_qdim,
    qfact as gate_qfact,
)

mp.mp.dps = 50

AME_D = mp.mpf("2.224566")          # AME2020 B(²H), the only bound 2-nucleon system
STD_REP_N3 = (2, 1)                  # standard rep at n=3 = the pn std-channel block


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

    print("\n  [3] Wiring  f_pn  ←  W_(2,1):")
    print(f"      f_pn_pred (gate algebraic W_(2,1)) = {mp.nstr(pred['f_pn_pred'], 8)}"
          f"   → E = {mp.nstr(pred['E_pred_MeV'], 7)} MeV"
          f"  (under-binds {mp.nstr((AME_D - pred['E_pred_MeV']) / AME_D * 100, 4)}%)")
    print(f"      miss vs required f_pn = {mp.nstr(pred['miss_f_pct'], 4)}%   "
          f"miss vs AME binding = {mp.nstr(pred['miss_E_pct'], 4)}%")

    # ---- falsifiable verdict ------------------------------------------------
    brackets = (f_std < f_required < pred["f_pn_pred"])
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
        "pn_block": str(STD_REP_N3),
        "f_pn_pred_from_gate_Wlambda": str(pred["f_pn_pred"]),
        "E_pred_from_gate_Wlambda_MeV": str(pred["E_pred_MeV"]),
        "miss_f_pct_vs_required": str(pred["miss_f_pct"]),
        "miss_E_pct_vs_AME": str(pred["miss_E_pct"]),
        "bracket_fstd_lt_freq_lt_W21": bool(brackets),
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
