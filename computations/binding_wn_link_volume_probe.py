#!/usr/bin/env python3
"""EXPLORATORY — option #1 of the θ_λ magnitude gate: is the jet-filtration
residue weight w_n(K) the HYPERBOLIC VOLUME of the n-body inter-nucleon sub-link?
(Bean t7qv; companion to binding_wn_kernel_derive_refute.py.)

The jet-filtration binding is B_strong = Σ_{n=2}^{A} m_e·a_D^(n)·w_n(K) with the
na-Stokes SW period a_D^(n) the DERIVED extensive kernel (a q-Hermite / Rogers–
Szegő eigenfunction — companion probe) and w_n(K) the OPEN multiplier. The audit
doc's option #1 (the literal "hyperbolic volumes via non-abelian Stokes") reads
w_n as the hyperbolic volume of the n-body sub-link of the Borromean atom knot
𝓑_K, since a_D^(n) is the na-Stokes surface integral over the Vol>0 components.

This probe runs the STRUCTURAL (formalize-first) test against that hypothesis,
using the corpus-witnessed link volumes (SnapPy is unavailable in this sandbox;
values are from computations/substrate/knot-volumes.witness.json + the SDP
binding-link registry recorded in binding_link_volumes.py):

  Hopf L2a1            Vol = 0          (Seifert-fibred, non-hyperbolic)
  2-unlink            Vol = 0          (Brunnian: any 1-of-3 Borromean removed)
  Whitehead L5a1       Vol = 3.663862   (= 4·Catalan)
  Borromean L6a4       Vol = 7.327725   (= 8·Catalan = 2·Vol(Whitehead))
  8_11                Vol = 8.286316
  figure-8 4_1         Vol = 2.029883   (= 3·Cl₂(π/3))

DISCIPLINE: no fit, no wiring, no tier change; the "refuted" verdict is
classified (a) scope-limited vs (b) structural-with-cited-invariant per AGENTS.md
"Before declaring refuted". The single-binding-link route (B = m_e·Vol(K)·Δtr per
atom) is a documented honest negative (binding_link_volumes.py); this tests the
distinct PER-BODY-ORDER volume reading, and does not re-run it.
"""
from __future__ import annotations
import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))
import _path_bridge  # noqa: F401,E402
from _precision import set_compute_dps  # noqa: E402
try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:
    _HAVE_WB = False

set_compute_dps()
_NS = mp.mp.dps

CATALAN = mp.catalan
VOL = {
    "Hopf L2a1": mp.mpf(0),
    "2-unlink": mp.mpf(0),
    "Whitehead L5a1": 4 * CATALAN,
    "Borromean L6a4": 8 * CATALAN,
    "8_11": mp.mpf("8.286316155818656"),
    "fig-8 4_1": 2 * mp.im(mp.polylog(2, mp.exp(mp.j * mp.pi / 3))),
}

# Universal per-body-order weights extracted in the companion probe (Coulomb-
# corrected AME; D / avg(³H,³He) / ⁴He; no fit).
W = {2: mp.mpf("4.35337"), 3: mp.mpf("9.33061"), 4: mp.mpf("15.9194")}


def main() -> int:
    print("  Corpus-witnessed link volumes (Catalan G = "
          f"{mp.nstr(CATALAN, 8)}):")
    for k, v in VOL.items():
        print(f"     {k:16s} Vol = {mp.nstr(v, 8)}")
    print(f"\n  extracted per-body-order weights: "
          f"w_2,w_3,w_4 = {mp.nstr(W[2],5)}, {mp.nstr(W[3],5)}, {mp.nstr(W[4],5)}")
    r32 = W[3] / W[2]
    print(f"     w_3/w_2 = {mp.nstr(r32,6)}   w_4/w_3 = {mp.nstr(W[4]/W[3],6)}")

    # ── Test 1: LITERAL w_n = Vol(n-body sub-link of the Borromean atom) ──────
    #   Brunnian invariant: removing any one of the 3 Borromean components leaves
    #   the 2-component UNLINK (Vol=0). The deuteron bond is Hopf (Vol=0,
    #   Seifert-fibred). So the n=2 sub-link is NON-HYPERBOLIC ⇒ w_2 = 0.
    print("\n  Test 1 — literal w_n = Vol(n-body sub-link):")
    w2_pred = VOL["2-unlink"]  # = Vol(Hopf) = 0, the n=2 sub-link
    print(f"     n=2 sub-link (Brunnian ⇒ 2-unlink; bond ⇒ Hopf): Vol = "
          f"{mp.nstr(w2_pred,4)}")
    print(f"     but extracted w_2 = {mp.nstr(W[2],5)} ≠ 0")
    test1_refuted_b = (w2_pred == 0) and (W[2] != 0)
    print(f"     ⇒ literal sub-link volume REFUTED at n=2 (scope-(b): the n=2 "
          f"sub-link is provably non-hyperbolic): {test1_refuted_b}")

    # ── Test 2: re-choose links — Whitehead:Borromean scaling for (w_2,w_3) ───
    #   Vol(Borromean) = 2·Vol(Whitehead) EXACTLY (both ∝ Catalan). Does the
    #   observed w_3/w_2 match this parameter-free 1:2?
    print("\n  Test 2 — Whitehead:Borromean (= 1:2 exact) vs observed w_3/w_2:")
    ratio_wh_bor = VOL["Borromean L6a4"] / VOL["Whitehead L5a1"]
    err2 = abs(r32 / ratio_wh_bor - 1)
    print(f"     Vol(Borromean)/Vol(Whitehead) = {mp.nstr(ratio_wh_bor,6)} (exact 2)")
    print(f"     observed w_3/w_2 = {mp.nstr(r32,6)}   rel err {mp.nstr(err2*100,3)}%"
          f"{'  ← CLOSES' if err2 <= mp.mpf('0.05') else '  (near-miss, not ≤5%)'}")
    print(f"     NB structurally incoherent: this assigns the n=2 bond to the "
          f"Whitehead link, but the SDP binding-link registry assigns the")
    print(f"     deuteron bond to the Hopf link (Vol 0) — the two link choices "
          f"conflict; the 1:2 is a numerical coincidence of Catalan multiples.")

    any_close = err2 <= mp.mpf("0.05")
    verdict = (
        "REFUTED. (b) The LITERAL option #1 (w_n = hyperbolic volume of the "
        "n-body sub-link of the Borromean atom 𝓑_K) is STRUCTURALLY EXCLUDED at "
        "n=2: the 2-body sub-link is non-hyperbolic (Vol=0) — the Borromean rings "
        "are Brunnian, so removing any one component leaves the 2-component "
        "unlink, and the SDP binding-link registry independently assigns the "
        "deuteron bond to the Hopf link (Seifert-fibred, Vol=0). Either way the "
        "n=2 volume vanishes, but the extracted w_2 = 4.353 > 0. Cited invariant: "
        "Brunnian / Seifert-fibred non-hyperbolicity (Vol=0). (a) Re-choosing the "
        "links (Whitehead for n=2, Borromean for n=3) gives the parameter-free "
        "1:2 Catalan ratio vs observed w_3/w_2 = 2.143 — a 7.2% NEAR-MISS, not a "
        "closure, AND it contradicts the registry's Hopf assignment for the "
        "deuteron bond, so the match is a numerical coincidence of Catalan "
        "multiples, not a derivation. Net: the volume route does not supply w_n. "
        "Consistent with the companion probe (w_n is the gated W_λ multiplier, "
        "sub-geometric); the na-Stokes kernel a_D^(n) stays permanent. No "
        "production touch; no value wired; no tier change."
        if not any_close else
        "The n-body sub-link volumes reproduce w_n zero-parameter — promote for "
        "categorical derivation (surface, do not wire)."
    )
    print("\n### VERDICT")
    print("  " + verdict.replace(". ", ".\n  "))

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("binding-wn-link-volume-probe", engine="mpmath",
                                output_dir=HERE)
            wb.set_description(
                "EXPLORATORY: tests option #1 — is the jet-filtration residue weight "
                "w_n the hyperbolic volume of the n-body inter-nucleon sub-link? "
                "Structurally REFUTED at n=2 (the 2-body Borromean sub-link is the "
                "unlink / the deuteron bond is Hopf, Vol=0, but w_2>0); the "
                "Whitehead:Borromean 1:2 Catalan ratio is a 7.2% near-miss that "
                "conflicts with the SDP Hopf assignment. No fit; no wiring.")
            wb.add_data("link_volumes", {k: mp.nstr(v, _NS) for k, v in VOL.items()})
            wb.add_data("w_universal", {str(n): mp.nstr(W[n], _NS) for n in W})
            wb.add_data("test1_literal_sublink_refuted_scope_b", bool(test1_refuted_b))
            wb.add_data("test2_whitehead_borromean_ratio", {
                "predicted_1to2": mp.nstr(ratio_wh_bor, _NS),
                "observed_w3_over_w2": mp.nstr(r32, _NS),
                "rel_err": mp.nstr(err2, _NS),
                "note": "7.2% near-miss; Catalan-multiple coincidence; conflicts with Hopf registry",
            })
            wb.add_data("verdict", verdict)
            wb.add_assertion(
                name="wn_link_volume_refuted_or_closes",
                computed=str(int(not any_close)), expected="1", tolerance=0,
                source=("1 = link-volume route does not supply w_n (n=2 non-hyperbolic, "
                        "scope-(b)); 0 = volumes reproduce w_n → promote."))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness emit skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
