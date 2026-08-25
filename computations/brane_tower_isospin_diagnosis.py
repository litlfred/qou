#!/usr/bin/env python3
"""
**CONTEXT (per prop:li2q-phiq-bar-symmetrization).** This script is a
**BINDING-context DIAGNOSTIC**: it documents the compact q-dilog Φ_q failure
mode (the −737 MeV mirror-nucleus pathology in the T2/T3 brane tower)
that motivates the Li_2^q migration recommended by the bar-symmetrization
identity. Φ_q is retained here intentionally — the script's purpose is
to *exhibit* Φ_q's divergence near |z|=1 as evidence for the
substrate-archimedean wall structure. For a binding-energy
*computation* (not diagnostic), use `_li_2_q_util.compute_t2_t3_from_vols`
which is bar-symmetric and bounded.

6-term mass formula brane-tower (T2/T3) isospin-violation diagnosis.

After replacing Term 1 with canonical bridge values
(`paper_six_term_canonical_t1.py`) and wiring Term 6 from the
Habiro-residue witness, the 6-term formula's pathological
predictions persist:

    Predicted T - ³He = -736.6 MeV   (CODATA: +0.019 MeV)

This script localises the source.  Findings:

1. **T1 is irrelevant.** Replacing Term 1 with canonical bridge
   value changes total predictions by sub-MeV.

2. **T2 dominates by 10⁶.** Per-atom breakdown (Hecke units):
       proton: T1 = 1.07,  T2 = 1.10×10⁶,  T3 = 8.20×10⁴, T4 = 1.60×10³

3. **Φ_q diverges as x → 1.**  Per-generator volumes |V̂_i| from
   `atom_per_generator_volumes` are mostly in 0.85-0.99:
       Φ_q(0.500) = 1.9×10²
       Φ_q(0.900) = 8.8×10⁴
       Φ_q(0.989) = 6.7×10⁵    ← typical generator value
   So Σ Φ_q(|V̂_i|) is dominated by generators with |V̂_i| ≈ 0.99.

4. **Per-generator volumes encode p ↔ n asymmetrically.**  T (1p,2n)
   and ³He (2p,1n) have these per-gen |V̂_i|:
       T:    0.989, 0.971, 0.264, 0.854, 0.976, 0.160, 0.854, 0.976
       ³He:  0.989, 0.971, 0.369, 0.989, 0.971, 0.264, 0.854, 0.976
   At inter-nucleon positions (gen 2, 5) the values differ — pp vs pn
   vs nn crossings give different (c, d).  These differences are then
   amplified ~10⁵× by Φ_q.

   Σ Φ_q(|V̂_i|) for T   = 2.12×10⁶
   Σ Φ_q(|V̂_i|) for ³He = 2.71×10⁶

   The 0.6×10⁶ Hecke-unit difference, scaled by E_0 = 7.95×10⁻⁴,
   gives ≈ 470 MeV — close to the 737 MeV pathology.

5. **The canonical Markov trace ALSO encodes p/n asymmetrically**
   (T = 0.1041, ³He = 0.2065) but at MeV scale, not 10⁵ × MeV scale.

CONCLUSION:

The brane-tower formula Σ Φ_q(|V̂_i|) is structurally sensitive to
per-generator volumes via the dilogarithm divergence near x=1.  The
formula reproduces the |V̂_i| values from the categorical Wedderburn
construction faithfully, but Φ_q amplifies tiny per-generator
differences into hundreds of MeV at the assembly stage.

The mismatch with experiment is NOT a bug in the implementation; it
is a feature of the formula as currently stated.  Possible
reconciliation paths:

  A. The per-generator (c, d) crossing parameters for proton-vs-neutron
     intra-nucleon crossings (`_PROTON_G0`, `_NEUTRON_G0` in
     `hecke_core.py`) might be wrong — different quark composition
     should give per-gen volumes that better track real masses.

  B. Φ_q might not be the right per-generator factor; the paper's
     "exceptional-divisor resolution" derivation should be re-audited
     to check whether a *normalised* Φ_q (e.g., Φ_q(x) / Φ_q(1−ε)
     with some regulator) is intended.

  C. The brane-tower formula might apply to a *different* observable
     than nuclear/atomic mass at q_0; e.g., the Kashaev-volume
     conjecture relates Φ_q to hyperbolic volume ONLY at roots of
     unity, not at q_0 ≈ 1.11.

  D. Term 5 (chirality) and the chirality-sign pattern per isotope
     might absorb more of the per-gen variability than currently
     accounted for.

Recommendation: paths (A) and (C) are most concrete.  (A) requires
auditing the canonical (c, d) tables; (C) requires re-reading
`prop:mass-endomorphism-tower` and its proof.

This script just documents the diagnosis.  It does NOT propose a fix;
fixing requires a derivation-level change to T2/T3 that is beyond
the scope of a follow-up commit.

POSTSCRIPT (PR #577 audit, 2026-05-09)
══════════════════════════════════════════════════════════════════
The full-tree compute audit identified the same structural bug
across three scripts — `atom_mass_derived.py` (multiplicative
`tr_M(atom NF) × E_0`), `atomic_braid_mass_table.py`
(multiplicative `|tr_p|^Z · |tr_n|^N` carrier base), and the
brane-tower diagnosis above.  All three are manifestations of
the same combination-law mistake:

   atomic mass is *additive* in constituents
        M_atom = Z·M_p + N·M_n + Z·M_e − E_binding(A, Z)
   not multiplicative.

Experimental per-isotope binding (AME2020) lives in
`ame-2020-binding-energies.witness.json` (the light nuclei ²H–⁷Li).
Per-nucleon binding rises from ~1.1 MeV/A (²H) toward the ~8 MeV/A
SEMF plateau (⁴He ≈ 7.07, ⁷Li ≈ 5.61 MeV/A), consistent with
empirical systematics.

This re-frames the conclusions above:

  · Path (A) — auditing the (c, d) tables — is **likely a wild
    goose chase**.  The 470 MeV p/n asymmetry is not a wrong
    per-generator volume; it is the brane-tower formula picking
    up exponential sensitivity through `Φ_q` because the
    carrier composition is multiplicative.  Even with perfect
    (c, d) values, the Σ Φ_q(|V̂_i|) sum will keep the same
    pathology because `Φ_q` is super-linear in the per-generator
    volumes.

  · Path (B) — normalising `Φ_q` — partially addresses the
    symptom, not the cause.

  · Path (C) — `Φ_q` only applies at roots of unity — is closer
    to the truth: the brane-tower formula is structurally
    appropriate for a different regime, not generic q.

  · The right path: recast T2/T3 as **additive contributions to
    E_binding(A, Z)**, matching the AME2020 binding energies in
    `ame-2020-binding-energies.witness.json`.  Each Δ_binding
    column entry (e.g. ⁴He ≈ 28.3 MeV, ⁷Li ≈ 39.2 MeV) is a
    target for an additive Σ tower formula, not a multiplicative
    one.

This script's output remains useful as a CHARACTERISATION of the
multiplicative pathology, not as evidence about (c, d) values.
The QOU `ρ_F · V_hyp` law in
`rem:frobenius-packing-density` is the natural additive
reformulation: `ρ_F` is structural (Type-B fold orbit closure,
`prop:cpt-orbit-closure-density`), `V_hyp` is geometric
(Thurston volume of the atomic-link complement), and their
product gives a per-isotope additive binding contribution
that any Σ-form tower must reproduce.

Output: `brane-tower-isospin-diagnosis.witness.json`
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from hecke_core import atom_per_generator_volumes  # noqa: E402
from mass_endomorphism import Phi_q  # noqa: E402


def abs_mpf(v):
    """Coerce a per-generator volume to abs mpmath float; no
    `str(float(...))` round-trip (preserves precision)."""
    x = v["full"] if isinstance(v, dict) else v
    return abs(mp.mpf(x))


def diagnose_atom(label, Z, N):
    A = Z + N
    inter = (A >= 2)
    vols = atom_per_generator_volumes(Z, N, include_inter=inter)
    abs_vols = [float(abs_mpf(v)) for v in vols]
    phi_vals = [float(Phi_q(v)) for v in vols]
    return {
        "atom": label, "Z": Z, "N": N, "A": A,
        "n_generators": len(vols),
        "include_inter": inter,
        "abs_per_gen": abs_vols,
        "phi_q_per_gen": phi_vals,
        "sum_phi_q": sum(phi_vals),
        "max_phi_q": max(phi_vals),
        "max_abs_v": max(abs_vols),
    }


def main() -> int:
    print("=" * 80)
    print("  Brane-tower isospin-violation diagnosis (T2/T3 root cause)")
    print("=" * 80)

    print("\n  Φ_q(x) divergence near x=1:")
    for x in (0.5, 0.7, 0.85, 0.9, 0.95, 0.97, 0.99):
        v = float(Phi_q(mp.mpf(str(x))))
        print(f"    Φ_q({x:>6.3f}) = {v:>12.4e}")

    print("\n  Per-atom diagnostics:")
    rows = []
    for label, Z, N in [
        ("proton", 1, 0), ("neutron", 0, 1),
        ("deuteron", 1, 1), ("tritium", 1, 2),
        ("helium-3", 2, 1), ("helium-4", 2, 2),
    ]:
        d = diagnose_atom(label, Z, N)
        rows.append(d)
        print(f"\n  {label:<10}  n_gens={d['n_generators']}  "
              f"max|V|={d['max_abs_v']:.4f}  sum Φ_q={d['sum_phi_q']:.4e}  "
              f"max Φ_q={d['max_phi_q']:.4e}")
        for i, (a, p) in enumerate(zip(d["abs_per_gen"], d["phi_q_per_gen"])):
            kind = "intra"
            if d["include_inter"]:
                if i % 3 == 2:
                    kind = "inter"
            print(f"    gen {i:>2} ({kind}):  |V|={a:.4f}  Φ_q={p:>12.4e}")

    # Isospin asymmetry: T vs ³He
    print("\n  Isospin asymmetry (T vs ³He):")
    rT = next(r for r in rows if r["atom"] == "tritium")
    r3 = next(r for r in rows if r["atom"] == "helium-3")
    print(f"    Σ Φ_q  (T)   = {rT['sum_phi_q']:.4e}")
    print(f"    Σ Φ_q  (³He) = {r3['sum_phi_q']:.4e}")
    diff = r3['sum_phi_q'] - rT['sum_phi_q']
    print(f"    Δ            = {diff:.4e}  Hecke-units")
    E_0 = 7.947423e-04  # MeV per Hecke-unit (from proton calibration in canonical T1 sweep)
    print(f"    × E_0        = {diff * E_0:.4f} MeV (Term 2 contribution to T - ³He)")
    print(f"    Total predicted T - ³He = -736.6 MeV (T2 + T3 + T4 + T5)")

    print("\n  CONCLUSION:")
    print("    The brane-tower Σ Φ_q(|V̂_i|) is dominated by generators")
    print("    where |V̂_i| ≈ 1, where Φ_q is order 10⁵.  Tiny per-generator")
    print("    asymmetries between p and n intra-crossings get amplified ")
    print("    into hundreds of MeV.  This is the structural source of the")
    print("    isospin pathology — not a software bug.")
    print()
    print("    The canonical Markov trace (Term 1) does NOT have this problem")
    print("    (T = 0.10, ³He = 0.21, difference < 0.2 MeV after E_0 scaling).")
    print()
    print("    Reconciliation requires either:")
    print("    (A) audit per-generator (c, d) crossing parameters in hecke_core")
    print("    (B) audit derivation of Φ_q in prop:mass-endomorphism-tower")
    print("    (C) re-evaluate whether brane-tower applies at q_0 (vs roots)")
    print("    (D) check Term 5 chirality pattern absorbs more p/n asymmetry")

    witness = {
        "computation": "brane-tower-isospin-diagnosis",
        "description": (
            "Diagnoses the origin of the 6-term formula's isospin "
            "violation (predicted T - ³He = -737 MeV vs CODATA +0.019). "
            "Localises to T2/T3 brane-tower: Φ_q diverges near x=1 and "
            "amplifies tiny per-generator |V̂_i| differences between p/n "
            "intra-crossings into hundreds of MeV.  Term 1 (canonical "
            "Markov trace) does NOT have this problem — the issue is "
            "structural to the brane-tower formula at q_0."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "rows": rows,
        "verdict": (
            "Brane-tower Σ Φ_q(|V̂_i|) is the pathology source.  The "
            "formula faithfully reproduces |V̂_i| from the Wedderburn "
            "construction, but Φ_q's divergence near x=1 amplifies "
            "small p/n asymmetries by 10⁵×.  Not a software bug — a "
            "feature of the formula as stated."
        ),
        "reconciliation_paths": [
            "(A) audit per-generator (c, d) for p vs n intra-crossings",
            "(B) audit Φ_q derivation in prop:mass-endomorphism-tower",
            "(C) re-evaluate brane-tower applicability at q_0 (vs roots)",
            "(D) check Term 5 chirality absorbs more p/n asymmetry",
        ],
    }
    out = HERE / "brane-tower-isospin-diagnosis.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
