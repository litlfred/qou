#!/usr/bin/env python3
"""
🛑 PORTED 2026-10-10 (beans `qou-g16t` / `qou-47sx`, issue litlfred/qou#7552).
Everything below the line of `═` further down is the ORIGINAL 2026-05 analysis,
kept as the record of what this script used to measure.  Its numbers came from
`pyhecke.atom.atom_per_generator_volumes` (hardcoded H_3 Wedderburn weights,
documented as wrong for A ≥ 2) and the float64 `Phi_q`, and they are NOT what
the script computes now.  Do not quote them as current.

What changed:

* Volumes: `mass_at_3A_proper.per_generator_V_hat_3A(Z, N)`, the canonical
  H_{3A} replacement, run with `QOU_H3A_MPF=1` so the seminormal matrices are
  built at mpf, not seeded from binary64 q.
* Kernel: `mass_endomorphism.Phi_q_mp`, the mpf twin of `Phi_q`.  Its pole is
  at |z| = q₀ ≈ 1.10998 (the first factor 1 − z/q₀ vanishes there).
* Removed: the hardcoded `E_0 = 7.947423e-04` MeV conversion and the printed
  "-736.6 MeV" total, neither of which this script ever computed.

What the port shows, measured 2026-10-10 (read the witness for the digits):

* The per-generator volumes take the same short list of values in every atom:
  proton quark generators |V̂| = 0.67139, 1.05511; neutron 0.55166, 1.08837;
  the two inter-nucleon values 7.19e-5 and 0.10453.  None reaches the pole.
* The neutron's second generator, 1.08837, is about 2 % below q₀, so
  Φ_q = 2.77e7 there and it dominates every sum it appears in.  The old H_3
  volumes were all below 1, which kept the sums at ~1e6.
* Σ Φ_q: proton 5.29e6, neutron 2.77e7, deuteron 3.30e7, tritium 6.07e7,
  helium-3 3.83e7.  So ³He − T = −2.24e7 Hecke units: the OPPOSITE sign of the
  old +0.6e6 and about 37× larger.  The finding of the original analysis —
  Φ_q amplifies small per-generator p/n differences enormously — survives the
  port and gets stronger; its numbers do not.
* ⁴He (A = 4, 12 strands) is NOT computed: under `QOU_H3A_MPF=1`
  `syt_prefix_cache` hands an mpf matrix to `scipy.sparse`, which rejects
  `dtype=object`.  Recorded as a gap in the witness, not filled with float64.
════════════════════════════════════════════════════════════════════════════
**CONTEXT (per `li2q-phiq-bar-symmetrization`).** This script is a
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

Retired-label note: a block named above with a backticked stem and no
`prop:`/`conj:` prefix has NO carrier in folio/ — it was demoted to
_deprecated/ and is recorded in docs/audits/2026-10-11-retired-label-records.md §A,
with the statement it carried and the command to recover its content.
"""
from __future__ import annotations

import os

# The mpf seminormal path in mass_at_3A_proper is opt-in and read at import
# time, so it must be set before that module is imported.
os.environ.setdefault("QOU_H3A_MPF", "1")

import _path_bridge  # noqa: F401, E402 — substrate modules live in substrate/
import json  # noqa: E402
import sys  # noqa: E402
from datetime import datetime, timezone  # noqa: E402
from pathlib import Path  # noqa: E402

from mpmath import mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from mass_at_3A_proper import per_generator_V_hat_3A  # noqa: E402
from mass_endomorphism import Phi_q_mp, q0_mp  # noqa: E402

ATOMS = [
    ("proton", 1, 0), ("neutron", 0, 1),
    ("deuteron", 1, 1), ("tritium", 1, 2),
    ("helium-3", 2, 1), ("helium-4", 2, 2),
]


def diagnose_atom(label, Z, N):
    A = Z + N
    inter = (A >= 2)
    base = {"atom": label, "Z": Z, "N": N, "A": A, "include_inter": inter}
    try:
        vols = per_generator_V_hat_3A(Z, N, include_inter=inter)
    except ValueError as e:
        # Not a refusal defined by the cone: scipy.sparse rejecting an mpf
        # matrix.  Report it as a gap; do not fall back to float64.
        return {**base, "computed": False,
                "gap": f"per_generator_V_hat_3A raised {type(e).__name__}: {e}"}
    abs_vols = [abs(mp.mpf(v["full"])) for v in vols]
    phis = [Phi_q_mp(x) for x in abs_vols]
    poles = [i for i, x in enumerate(abs_vols) if x >= q0_mp]
    finite = [p for p in phis if p != mp.inf]
    return {
        **base,
        "computed": True,
        "n_generators": len(vols),
        "abs_per_gen": [fmt(x) for x in abs_vols],
        "phi_q_per_gen": [fmt(p) for p in phis],
        "generators_at_or_past_pole": poles,
        "sum_phi_q": fmt(mp.fsum(phis)),
        "sum_phi_q_finite_generators": fmt(mp.fsum(finite)),
        "max_abs_v": fmt(max(abs_vols)),
    }


def main() -> int:
    print("=" * 80)
    print("  Brane-tower isospin diagnosis — PORTED to H_{3A} volumes + mpf Φ_q")
    print("=" * 80)
    print(f"\n  pole: Φ_q(z) = +inf for |z| ≥ q₀ = {mp.nstr(q0_mp, 15)}")

    print("\n  Φ_q(x) near x = 1 (mpf):")
    divergence = []
    for s in ("0.5", "0.7", "0.85", "0.9", "0.95", "0.97", "0.99", "1.05", "1.08"):
        v = Phi_q_mp(mp.mpf(s))
        divergence.append({"x": s, "phi_q": fmt(v)})
        print(f"    Φ_q({s:>5}) = {mp.nstr(v, 8)}")

    print("\n  Per-atom diagnostics:")
    rows = []
    for label, Z, N in ATOMS:
        d = diagnose_atom(label, Z, N)
        rows.append(d)
        if not d["computed"]:
            print(f"\n  {label:<10}  NOT COMPUTED — {d['gap'][:110]}")
            continue
        print(f"\n  {label:<10}  n_gens={d['n_generators']}  "
              f"poles at gens {d['generators_at_or_past_pole']}  "
              f"Σ Φ_q = {mp.nstr(mp.mpf(d['sum_phi_q']), 8)}")
        for i, (a, p) in enumerate(zip(d["abs_per_gen"], d["phi_q_per_gen"])):
            kind = "inter" if d["include_inter"] and i % 3 == 2 else "intra"
            print(f"    gen {i:>2} ({kind}):  |V|={mp.nstr(mp.mpf(a), 10)}  "
                  f"Φ_q={mp.nstr(mp.mpf(p), 8)}")

    rT = next(r for r in rows if r["atom"] == "tritium")
    r3 = next(r for r in rows if r["atom"] == "helium-3")
    t_inf = mp.mpf(rT["sum_phi_q"]) == mp.inf
    h_inf = mp.mpf(r3["sum_phi_q"]) == mp.inf
    if t_inf or h_inf:
        asym = None
        asym_note = ("undefined: Σ Φ_q is +inf for "
                     + ", ".join(n for n, f in (("tritium", t_inf), ("helium-3", h_inf)) if f)
                     + " because a neutron generator volume is at or past the pole")
    else:
        asym = fmt(mp.mpf(r3["sum_phi_q"]) - mp.mpf(rT["sum_phi_q"]))
        asym_note = "Σ Φ_q(³He) − Σ Φ_q(T), Hecke units"
    print(f"\n  Isospin asymmetry (³He − T): {asym if asym is not None else asym_note}")

    witness = {
        "computation": "brane-tower-isospin-diagnosis",
        "description": (
            "Ported 2026-10-10: per-generator H_{3A} volumes "
            "(per_generator_V_hat_3A, mpf seminormal path) fed to the mpf "
            "Phi_q_mp kernel.  Replaces the 2026-05 run on hardcoded H_3 "
            "weights and float64 Phi_q, whose numbers are superseded."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "auditOnly": True,
        "volume_source": "mass_at_3A_proper.per_generator_V_hat_3A (QOU_H3A_MPF=1)",
        "kernel": "mass_endomorphism.Phi_q_mp",
        "pole_q0": fmt(q0_mp),
        "phi_q_divergence": divergence,
        "rows": rows,
        "isospin_asymmetry_hecke_units": asym,
        "isospin_asymmetry_note": asym_note,
        "verdict": (
            "Under the canonical H_{3A} volumes no generator reaches the "
            "Phi_q pole at q0, but the neutron's second quark generator "
            "(|V_hat| = 1.08837, about 2 % below q0) gives Phi_q = 2.77e7 and "
            "dominates every sum it enters.  Sigma Phi_q(3He) - Sigma "
            "Phi_q(T) = -2.24e7 Hecke units, opposite in sign and ~37x the "
            "2026-05 H_3 figure.  Helium-4 is not computed (mpf matrices "
            "rejected by scipy.sparse)."
        ),
    }
    out = HERE / "brane-tower-isospin-diagnosis.witness.json"
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
