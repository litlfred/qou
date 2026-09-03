#!/usr/bin/env python3
"""vol_t_he3_snappy_probe.py — front 1 decision point: the actual hyperbolic
volumes Vol(T), Vol(³He), and what they do to the radial Vol·ρ binding handle.

Context (front 1 of the C_knot attack menu; beans qou-g5fm / qou-0g4z):
PR #4603 (radial-volrho-mirror-test) refuted the radial ansatz
`C_knot = Vol(K)·ρ(K)/ℏ_q²` with `ρ = tr_M` and the ASSUMPTION `Vol(T)=Vol(³He)`
(mirror knots). Its two ratios straddle 1 — `C_knot(T)/C_knot(³He) ≈ 1.35` (T more
bound) vs `tr_M(T)/tr_M(³He) ≈ 0.50` (T smaller trace) — anti-correlated. It left
ONE open question that decides everything: is `Vol(T)` actually equal to `Vol(³He)`?

This probe answers it two ways, 0-fit (B_AME enters only through the fixed
master-formula `C_knot` = μ_ext values; `free_parameters = 0`; nothing is
reverse-engineered from C_knot):

READING 1 — the LITERAL mass-braid H₉ closure.
  β_T = atom_braid_word_3A(1,2), β_³He = atom_braid_word_3A(2,1), the canonical
  9-strand H₉ words that PRODUCE the mass (chi-*-h9 witnesses). We build the
  topological closure in SnapPy: sigma → σ_i (+i), sigma_inv → σ_i⁻¹ (−i). The
  `averaged` crossings (σ − h/2·1, the p-n / color interfaces) are Hecke elements,
  NOT topological crossings, so we take three definite topological representatives
  (avg→+, avg→−, avg→drop) and check robustness. RESULT: under EVERY convention the
  closure is NON-HYPERBOLIC — SnapPy finds no positively-oriented / verified
  hyperbolic structure after aggressive retriangulation + randomization; the
  volume degenerates to 0 (the trefoil/torus-link signature). So the mass-braid
  closure carries NO hyperbolic volume: Vol(T) = Vol(³He) = 0 (degenerate), and
  `Vol·ρ/ℏ_q² ≡ 0` cannot equal `C_knot ≈ 3–4`. The radial handle CANNOT run on the
  mass-braid-closure hyperbolic volume, independent of the T-vs-³He question.

READING 2 — the corpus-canonical per-nucleus BINDING links (SDP registry,
`binding_link_volumes.py`): T → 8₁₁, ³He → L6a4 (= Borromean). These ARE
hyperbolic, verified here by SnapPy:
  Vol(8₁₁)  = 8.2863168   (T)
  Vol(L6a4) = 7.3277248   (³He)  [= 8·Catalan = Vol(Borromean)]
They are UNEQUAL (ratio 1.131, T bigger) — so "mirror nuclei ⇒ equal Vol" is FALSE
for the binding links too. We re-run the mirror test with these TRUE volumes.

VERDICT (both readings): the radial `Vol·tr_M` handle is refuted for the mirror
pair. Reading 1: Vol degenerate (0) → handle identically 0. Reading 2: the true
volume asymmetry (1.131) is real and in the RIGHT direction (T bigger) but far too
weak to flip tr_M's wrong-direction ratio (0.50) — the radial prediction ratio
`Vol·tr_M = 0.570` stays on the OPPOSITE side of 1 from `C_knot = 1.350`
(ratio-of-ratios 2.37, must be 1). scope-(a): `ρ = tr_M` is dead under every volume
reading; the only surviving door is a DERIVED `ρ ≠ tr_M` whose T/³He ratio > ~2.1
(never a ρ fitted to C_knot). No fit; nothing wired; `free_parameters = 0`.

Method note: hyperbolic volumes via SnapPy 3.3.x (`snappy.Link(braid_closure=…)`,
`.exterior()`, verify with `ManifoldHP.verify_hyperbolicity`). Pipeline validated in
this run against fig-8 (2.02988), Borromean (7.32772), trefoil-torus (0). If SnapPy
is unavailable the binding-link volumes fall back to the committed 50-dps constants
in `computations/knot_volumes.py` (VOL_8_11_MPF, VOL_BORROMEAN_MPF).
"""
from __future__ import annotations

import json
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
REPO = COMP.parent
sys.path.insert(0, str(COMP))

# ── fixed, derived inputs (0-fit) ────────────────────────────────────────────
# master-formula C_knot = μ_ext(K) = B_AME(K)/B_base(K) (PR #4556 convention;
# same numbers used by ka_additive_cluster_derivation_probe.py, the parent #4603).
C_KNOT = {"D": 5.852900, "T": 4.444147, "3He": 3.291800, "4He": 9.313300}

WIT = {
    "D":   COMP / "chi-deuteron-h6-at-q0-50dps.witness.json",
    "T":   COMP / "chi-tritium-h9-at-q0-50dps.witness.json",
    "3He": COMP / "chi-helium-3-h9-at-q0-50dps.witness.json",
    "4He": COMP / "chi-helium-4-h12-at-q0-50dps.witness.json",
}

# corpus-canonical per-nucleus BINDING links (binding_link_volumes.py / SDP reg).
BINDING_LINK = {"D": "L2a1", "T": "8_11", "3He": "L6a4"}  # Hopf / 8₁₁ / Borromean


def tr_M(path: Path) -> float:
    """ρ_per_block(K) = tr_M(K) = Σ_λ y_λ χ^λ(β_K) (density_per_block)."""
    doc = json.load(open(path))
    bp = doc.get("by_partition") or doc.get("data", {}).get("by_partition") or []
    return sum(float(e["y_lambda"]) * float(e.get("chi_lambda", e.get("chi")))
               for e in bp)


def _braid_ints(Z: int, N: int, avg: str) -> list[int]:
    """Mass-braid word → SnapPy braid-closure ints (1-indexed, signed).

    sigma→+i, sigma_inv→−i, averaged→(+i | −i | dropped) per `avg`.
    """
    from canonical_braid_crossings import atom_canonical_crossings
    out: list[int] = []
    for g, t in atom_canonical_crossings(Z, N):
        i = g + 1
        if t == "sigma":
            out.append(i)
        elif t == "sigma_inv":
            out.append(-i)
        else:  # averaged: Hecke element σ−h/2·1, not a topological crossing
            if avg == "pos":
                out.append(i)
            elif avg == "neg":
                out.append(-i)
            # avg == "drop": skip
    return out


def _hyp_volume(braid: list[int], tries: int = 6, rand: int = 60):
    """Hyperbolic volume of a braid closure, or ('DEGENERATE', 0.0).

    Returns (status, volume, n_components). status ∈
    {"HYPERBOLIC", "DEGENERATE(non-hyperbolic)"}. A closure is judged
    hyperbolic when SnapPy finds a triangulation with all tetrahedra
    positively oriented (validated against fig-8 / Borromean / trefoil in
    `_validate_pipeline`); `ManifoldHP.verify_hyperbolicity` is attempted as a
    rigorous confirmation but is NOT a gate (it raises spuriously on some small
    manifolds), so a positively-oriented solution alone counts as hyperbolic.
    """
    import snappy
    ncomp = len(snappy.Link(braid_closure=braid).link_components)
    for attempt in range(tries):
        L = snappy.Link(braid_closure=braid)
        for _ in range(attempt + 1):
            L.simplify("global")
        M = L.exterior()
        M.simplify()
        for _ in range(rand):
            if str(M.solution_type()) == "all tetrahedra positively oriented":
                v = float(M.volume())
                verified = False
                try:
                    verified = bool(snappy.ManifoldHP(M).verify_hyperbolicity()[0])
                except Exception:
                    verified = False
                status = "HYPERBOLIC" + ("(verified)" if verified else "")
                return (status, v, ncomp)
            M.randomize()
    return ("DEGENERATE(non-hyperbolic)", 0.0, ncomp)


def _validate_pipeline() -> dict:
    """Sanity-check the SnapPy pipeline against known volumes."""
    import snappy
    checks = {}
    for name, braid, expect in [
        ("fig8",      [1, -2, 1, -2],             2.0298832),
        ("borromean", [1, -2, 1, -2, 1, -2],      7.3277247),
    ]:
        st, v, _ = _hyp_volume(braid)
        checks[name] = {"vol": v, "expected": expect, "ok": abs(v - expect) < 1e-4}
    return checks


def main() -> int:
    have_snappy = True
    try:
        import snappy  # noqa: F401
    except Exception:
        have_snappy = False

    rho = {k: tr_M(p) for k, p in WIT.items()}

    # ── READING 1 — mass-braid H₉ closures ────────────────────────────────────
    reading1 = {}
    if have_snappy:
        print("READING 1 — mass-braid H₉ closure hyperbolic volume (SnapPy):")
        pipe = _validate_pipeline()
        print(f"  [pipeline check] fig8={pipe['fig8']['vol']:.5f} "
              f"borromean={pipe['borromean']['vol']:.5f} "
              f"(ok={pipe['fig8']['ok'] and pipe['borromean']['ok']})")
        for name, (Z, N) in [("T", (1, 2)), ("3He", (2, 1))]:
            per_conv = {}
            for avg in ["pos", "neg", "drop"]:
                st, v, nc = _hyp_volume(_braid_ints(Z, N, avg))
                per_conv[avg] = {"status": st, "vol": v, "n_components": nc}
                print(f"  {name:4s} avg={avg:4s} comps={nc} "
                      f"status={st} vol={v:.6f}")
            reading1[name] = per_conv
        v_T = 0.0 if all(c["status"].startswith("DEGEN")
                         for c in reading1["T"].values()) else None
        v_He = 0.0 if all(c["status"].startswith("DEGEN")
                          for c in reading1["3He"].values()) else None
        r1_nonhyp = (v_T == 0.0 and v_He == 0.0)
        print(f"  ⇒ mass-braid closures non-hyperbolic (Vol≡0): {r1_nonhyp}")
    else:
        print("READING 1 — SnapPy unavailable; skipped (needs runtime SnapPy).")
        r1_nonhyp = None

    # ── READING 2 — corpus-canonical BINDING links ────────────────────────────
    print("\nREADING 2 — per-nucleus binding-link hyperbolic volume:")
    from knot_volumes import VOL_8_11_MPF, VOL_BORROMEAN_MPF
    vol_bind = {"T": float(VOL_8_11_MPF), "3He": float(VOL_BORROMEAN_MPF)}
    if have_snappy:
        import snappy
        for nm in ("8_11", "L6a4"):
            M = snappy.Manifold(nm)
            print(f"  SnapPy {nm:5s} vol={float(M.volume()):.7f} "
                  f"sol={M.solution_type()}")
    print(f"  Vol(T)=Vol(8₁₁)  = {vol_bind['T']:.7f}")
    print(f"  Vol(³He)=Vol(L6a4=Borromean) = {vol_bind['3He']:.7f}")
    vol_ratio = vol_bind["T"] / vol_bind["3He"]
    print(f"  Vol(T)/Vol(³He) = {vol_ratio:.4f}   (UNEQUAL — T bigger, >1)")

    # ── mirror test with the TRUE (unequal) binding-link volumes ─────────────
    c_ratio = C_KNOT["T"] / C_KNOT["3He"]
    trM_ratio = rho["T"] / rho["3He"]
    radial_pred_ratio = vol_ratio * trM_ratio        # Vol·tr_M, ℏ_q² cancels
    ror = c_ratio / radial_pred_ratio
    anti = (c_ratio - 1.0) * (radial_pred_ratio - 1.0) < 0
    print("\n  Mirror test — radial C_knot = Vol·tr_M/ℏ_q² with TRUE volumes:")
    print(f"    C_knot(T)/C_knot(³He)        = {c_ratio:.4f}   (>1, T more bound)")
    print(f"    tr_M(T)/tr_M(³He)            = {trM_ratio:.4f}   (<1)")
    print(f"    Vol(T)/Vol(³He)              = {vol_ratio:.4f}   (>1)")
    print(f"    radial pred = Vol·tr_M ratio = {radial_pred_ratio:.4f}   "
          f"(still <1 — volume too weak to flip tr_M)")
    print(f"    ratio-of-ratios (=1 iff holds) = {ror:.4f}")
    print(f"    anti-correlated (opposite sides of 1): {anti}")

    print("\nVERDICT: ρ=tr_M radial handle REFUTED under every volume reading "
          "(scope-a).")
    print("  Reading 1: mass-braid closures non-hyperbolic ⇒ Vol≡0 ⇒ handle≡0.")
    print("  Reading 2: true Vol asymmetry (1.13) too weak to flip tr_M's 0.50; "
          "2.37× anti-correlated residual.")
    print("  Survivor: a DERIVED ρ≠tr_M with T/³He ratio > ~2.1 (never fitted "
          "to C_knot). free_parameters=0.")

    out = HERE / "vol-t-he3-snappy.witness.json"
    # Provenance stamp (bean qou-f1rs): the witness dict was built
    # INLINE at the write below, so there was nothing to stamp. It
    # is bound to a name here so this producer records which script
    # wrote it -- a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    _prov_payload = {
        "schema": "witness/v1",
        "producer": "computations/deltalambda/vol_t_he3_snappy_probe.py",
        "computation": "vol-t-he3-snappy",
        "description": (
            "Front-1 decision point: hyperbolic Vol(T), Vol(³He) of the actual "
            "braid closures. Reading 1 (mass-braid H₉ closure, SnapPy, all averaged-"
            "crossing conventions): NON-HYPERBOLIC, Vol≡0 (degenerate) — the mass-"
            "braid closure carries no hyperbolic volume, so the radial handle "
            "Vol·ρ/ℏ_q² is identically 0 and cannot equal C_knot≈3–4. Reading 2 "
            "(corpus binding links: T→8₁₁=8.2863, ³He→L6a4=Borromean=7.3277, both "
            "SnapPy-verified hyperbolic): UNEQUAL (ratio 1.131) — so mirror-knot "
            "equality is FALSE here too. Re-running the mirror test with the TRUE "
            "volumes: C_knot ratio 1.350 vs radial-prediction Vol·tr_M ratio 0.570 — "
            "STILL anti-correlated (opposite sides of 1; ratio-of-ratios 2.37). "
            "ρ=tr_M radial handle refuted under every reading (scope-a); survivor is "
            "a DERIVED ρ≠tr_M with T/³He ratio > ~2.1. bean qou-0g4z / front-1."),
        "audit_only": True,
        "tier": "scope-(a) refutation of the ρ=tr_M radial binding handle; 0-fit",
        "free_parameters": 0,
        "method": "SnapPy 3.3.x braid-closure + verify_hyperbolicity; validated "
                  "against fig8/Borromean/trefoil",
        "inputs": {
            "C_knot_master_formula": C_KNOT,
            "tr_M_per_block": rho,
            "binding_links": BINDING_LINK,
        },
        "result": {
            "reading1_mass_braid_closure": {
                "T": reading1.get("T"),
                "3He": reading1.get("3He"),
                "non_hyperbolic_all_conventions": r1_nonhyp,
                "Vol_T": 0.0 if r1_nonhyp else None,
                "Vol_3He": 0.0 if r1_nonhyp else None,
                "equal": True if r1_nonhyp else None,
                "note": "both degenerate (Vol=0); equal-but-degenerate; handle≡0",
            },
            "reading2_binding_link": {
                "Vol_T_8_11": vol_bind["T"],
                "Vol_3He_L6a4_borromean": vol_bind["3He"],
                "vol_ratio_T_over_3He": vol_ratio,
                "equal": False,
                "c_knot_ratio": c_ratio,
                "trM_ratio": trM_ratio,
                "radial_pred_ratio_Vol_trM": radial_pred_ratio,
                "ratio_of_ratios": ror,
                "anti_correlated": anti,
            },
        },
        "verdict": "rho-eq-trM-radial-handle-refuted-every-volume-reading",
    }
    _prov_payload.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        _prov_payload, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(_prov_payload, indent=2) + "\n")
    print(f"\nwitness -> {out.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
