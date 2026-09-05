#!/usr/bin/env python3
"""
Front (e): should (H1) `c_3^even = -Vol(4_1)` be believed at all?

The corpus states the surviving empirical fact for (H1) as:

    "c_3 at the substrate anchor agrees with -Vol(4_1) to ~0.48%"
    (0.07% at the muon for the full keystone form)

    -- ck-dk-canonical-registry.md, and rem-qstar-decay-sector-q0.md

SECOND DEFECT, found while computing the first: **that 0.48% is the MUON
number**, not the substrate anchor's. Measured here:

    muon    |c_3 - (-Vol(4_1))| / |c_3|  =  0.479 %   <- this is the "0.48%"
    proton                               =  1.907 %   <- 4.0x worse

Since the 2026-08-07 owner directive makes the PROTON pin the default for all
new compute, "the substrate anchor" now reads as proton, and the headline
attaches the muon's figure to it. Whether or not the phrasing was defensible
when written, it is a mislabel today, and it flatters (H1) by a factor of 4.

Those percentages are RELATIVE COMPARISONS OF CENTRAL VALUES. They are quoted
without the uncertainty on the quantity being compared. That uncertainty is
already in the corpus and is enormous:

    sigma(c_3) = +/-1.262 per anchor, CAL-3 propagated
    (aomega_o2_stokes_to_observable_mechanism.py:57, S_UNCERTAINTY;
     registry section 9e; sigma(c_3) = sigma(S) identically because
     S = c_3 + Vol(4_1) and Vol(4_1) is exact)

against |c_3| ~ 2.02 -- i.e. **62% relative**. This probe does not take that
number on trust: it DERIVES sigma(c_3) = sigma(Q_beta)/(Q_N2 u^3) from the
committed CAL-3 input and checks it reproduces the quoted 1.262.

THE POINT. The O2 probe (qou-ws1w) already ruled that a near-match sitting
inside the +/-1.262 band "can be neither confirmed nor excluded, which is the
signature of a fit, not a derivation", and fired O1-remove on the A_omega -> S
bridge for exactly that reason. **That test has never been applied to (H1)
itself** -- the parent hypothesis that DEFINES S. Applying it:

    discrepancy |c_3(proton) - (-Vol(4_1))| = 0.0395  ->  0.031 sigma
    discrepancy |c_3(muon)   - (-Vol(4_1))| = 0.0097  ->  0.008 sigma

Both far inside the band. Note this cuts BOTH ways and the probe says so: the
0.031-sigma proton figure is not evidence AGAINST (H1) either. Nothing is
being measured here at all.

A 0.03-sigma agreement is not strong evidence. It is NO evidence: every
candidate within +/-1.262 agrees at least as well, and the acceptance interval
is 2.524 wide -- **51x wider than the 0.0491 genericity window** the 7/7
unrelated-constants result was computed over. So the genericity problem is
about fifty times worse than the window analysis reported.

WHAT WOULD MAKE (H1) TESTABLE. sigma(c_3) must fall below the discrepancy:

    32x  sharper Q_beta  -> the proton agreement reaches 1 sigma
    130x sharper Q_beta  -> the muon agreement reaches 1 sigma

which brackets the 25.7x that the same sigma(Q_beta) needs for the zero-location
test to resolve at the mu-p scale. All three thresholds are the SAME lever, and
they order sensibly.

Scope-(a). This does NOT refute (H1) and does not show Vol(4_1) is absent from
c_3's bar-even part. It shows the stated EVIDENCE for (H1) has no discriminating
power at present resolution, and that the "0.48%" phrasing overstates it by
omitting an error bar 32x the discrepancy. Arithmetic on committed values; no
fit, no new measurement, no c_k wired.
"""

import datetime
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import mpmath as mp
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401

from qbeta_utils import c3_target_at, substrate_ladder_quantities  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 60

ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
with mp.workdps(60):
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))

# The quoted band, for cross-check only — DERIVED below, not used as input.
QUOTED_SIGMA_C3 = mp.mpf("1.262")
# The genericity window width, from sleak_offset_genericity_check.py.
GENERICITY_WINDOW_WIDTH = mp.mpf("0.0491423421")


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def _sigma_qbeta() -> tuple[mp.mpf, str]:
    """CAL-3 one-sigma uncertainty on Q_beta, read from the committed witness.

    Same explicit field the qstar experimental-budget probe reads
    (`data.Q_beta_n_MeV_err`), not a heuristic search — so the two probes are
    demonstrably using the same input.
    """
    with open(ROOT / "computations" / "cal-3-q-beta.witness.json") as f:
        w = json.load(f)
    return mp.mpf(str(w["data"]["Q_beta_n_MeV_err"])), w["data"]["Q_beta_n_MeV_quoted"]


def main() -> int:
    q_p = q_at()
    q_m = q_muon_at()
    sigma_qb, qb_quoted = _sigma_qbeta()

    print("=" * 78)
    print("Front (e) — is (H1) c_3^even = -Vol(4_1) supported by its stated evidence?")
    print("=" * 78)
    print(f"\n  Vol(4_1) = {mp.nstr(VOL41, 14)}   (exact: 2*Cl_2(pi/3))")
    print(f"  Q_beta = {qb_quoted}")
    print(f"  sigma(Q_beta) from the committed CAL-3 witness = "
          f"{mp.nstr(sigma_qb, 6)} MeV = {mp.nstr(sigma_qb * 10**6, 4)} eV")

    print("\n" + "-" * 78)
    print("STEP 1 — derive sigma(c_3) rather than quote it")
    print("-" * 78)
    print("\n  c_3 = (Q_beta/Q_N2 - 1)/u^3  =>  dc_3/dQ_beta = 1/(Q_N2 u^3)")

    rows = {}
    for name, q in (("proton", q_p), ("muon", q_m)):
        s = substrate_ladder_quantities(q)
        u = s["u"]
        c3 = c3_target_at(q, QCOD, ME)
        # Q_N2 recovered exactly from the extractor's own definition
        q_n2 = QCOD / (1 + c3 * u ** 3)
        dc3_dqb = 1 / (q_n2 * u ** 3)
        sigma_c3 = dc3_dqb * sigma_qb
        rows[name] = {"q": mp.nstr(q, 22), "u": mp.nstr(u, 14),
                      "c3": mp.nstr(c3, 14), "Q_N2": mp.nstr(q_n2, 14),
                      "dc3_dQbeta": mp.nstr(dc3_dqb, 12),
                      "sigma_c3": mp.nstr(sigma_c3, 12)}
        print(f"\n  {name:7s} u = {mp.nstr(u, 10)}   Q_N2 = {mp.nstr(q_n2, 12)} MeV")
        print(f"          dc_3/dQ_beta = {mp.nstr(dc3_dqb, 10)} /MeV")
        print(f"          sigma(c_3)   = {mp.nstr(sigma_c3, 10)}")

    sigma_c3_p = mp.mpf(rows["proton"]["sigma_c3"])
    sigma_c3_m = mp.mpf(rows["muon"]["sigma_c3"])
    xcheck = abs(sigma_c3_p - QUOTED_SIGMA_C3) / QUOTED_SIGMA_C3
    print(f"\n  cross-check vs the corpus's quoted +/-1.262: rel.err "
          f"{mp.nstr(xcheck, 4)}  (derived, not assumed)")

    print("\n" + "-" * 78)
    print("STEP 2 — what the quoted agreements are worth in sigma")
    print("-" * 78)
    sig = {}
    for name, q, sc3 in (("proton", q_p, sigma_c3_p), ("muon", q_m, sigma_c3_m)):
        c3 = c3_target_at(q, QCOD, ME)
        disc = abs(c3 - (-VOL41))
        rel_pct = disc / abs(c3) * 100
        n_sigma = disc / sc3
        sig[name] = {"discrepancy": mp.nstr(disc, 12),
                     "relative_pct": mp.nstr(rel_pct, 6),
                     "n_sigma": mp.nstr(n_sigma, 6)}
        tag = "  <- THIS is the corpus's \"0.48%\"" if name == "muon" else ""
        print(f"\n  {name:7s} |c_3 - (-Vol(4_1))| = {mp.nstr(disc, 10)}")
        print(f"          quoted as             {mp.nstr(rel_pct, 5)} %{tag}")
        print(f"          actually              {mp.nstr(n_sigma, 5)} sigma")
    print(f"\n  sigma(c_3)/|c_3| = {mp.nstr(sigma_c3_p / abs(c3_target_at(q_p, QCOD, ME)) * 100, 5)} %"
          f"  — the quantity is 62%-uncertain; a 0.5% central-value match says nothing.")

    print("\n" + "-" * 78)
    print("STEP 3 — how much worse this makes the genericity problem")
    print("-" * 78)
    accept_width = 2 * sigma_c3_p
    ratio = accept_width / GENERICITY_WINDOW_WIDTH
    c3p = c3_target_at(q_p, QCOD, ME)
    lo, hi = -(c3p + sigma_c3_p), -(c3p - sigma_c3_p)
    print(f"\n  1-sigma acceptance for V in c_3 ~ -V:  [{mp.nstr(lo, 8)}, {mp.nstr(hi, 8)}]")
    print(f"  width                                  {mp.nstr(accept_width, 8)}")
    print(f"  genericity window width (7/7 result)   {mp.nstr(GENERICITY_WINDOW_WIDTH, 8)}")
    print(f"  ratio                                  {mp.nstr(ratio, 8)} x")
    print("\n  The 7/7-unrelated-constants genericity result was computed over a")
    print(f"  window {mp.nstr(ratio, 4)}x NARROWER than the experimental acceptance. So it")
    print("  UNDERSTATES the problem by that factor.")

    print("\n" + "-" * 78)
    print("STEP 4 — what would make (H1) testable")
    print("-" * 78)
    need_p = sigma_c3_p / mp.mpf(sig["proton"]["discrepancy"])
    need_m = sigma_c3_m / mp.mpf(sig["muon"]["discrepancy"])
    print(f"\n  sigma(Q_beta) improvement for the agreement to reach 1 sigma:")
    print(f"    proton anchor   {mp.nstr(need_p, 6)} x")
    print(f"    muon anchor     {mp.nstr(need_m, 6)} x")
    print("\n  For comparison, the zero-location test needs 25.68x (PR #5084) for")
    print("  sigma(q*) to fall below the mu-p pin spread. All three are the SAME")
    print("  lever -- a sharper neutron Q_beta -- and they order sensibly.")

    assertions = [
        {"name": "sigma_c3_derived_matches_quoted_1262",
         "passed": bool(xcheck < mp.mpf("0.01")),
         "detail": "derived sigma(c_3) vs quoted 1.262, rel.err " + mp.nstr(xcheck, 4)},
        {"name": "proton_agreement_below_one_tenth_sigma",
         "passed": bool(mp.mpf(sig["proton"]["n_sigma"]) < mp.mpf("0.1"))},
        {"name": "muon_agreement_below_one_tenth_sigma",
         "passed": bool(mp.mpf(sig["muon"]["n_sigma"]) < mp.mpf("0.1"))},
        {"name": "acceptance_much_wider_than_genericity_window",
         "passed": bool(ratio > 10),
         "detail": mp.nstr(ratio, 6) + "x"},
        {"name": "quoted_048pct_is_the_muon_not_the_substrate_anchor",
         "passed": bool(abs(mp.mpf(sig["muon"]["relative_pct"]) - mp.mpf("0.48"))
                        < mp.mpf("0.01")
                        and mp.mpf(sig["proton"]["relative_pct"]) > mp.mpf("1.5")),
         "detail": "muon " + mp.nstr(mp.mpf(sig["muon"]["relative_pct"]), 4)
                   + "% vs proton " + mp.nstr(mp.mpf(sig["proton"]["relative_pct"]), 4)
                   + "% — the headline quotes the muon figure"},
        {"name": "H1_not_refuted_only_unsupported",
         "passed": True,
         "detail": "scope-(a): no invariant forbids a 4_1-volume ingredient; the "
                   "0.031-sigma proton figure is not evidence against (H1) either"},
    ]
    all_passed = all(a["passed"] for a in assertions)

    with open(os.path.abspath(__file__), "rb") as f:
        src = f.read()

    witness = {
        "computation": "qbeta-h1-significance-against-cal3-band",
        "description": (
            "Front (e): the stated evidence for (H1) c_3^even = -Vol(4_1) has no "
            "discriminating power at present resolution. The corpus quotes 'c_3 agrees "
            "with -Vol(4_1) to ~0.48%' (0.07% muon), which compares CENTRAL VALUES "
            "while omitting sigma(c_3) = +/-1.262 CAL-3 propagated — 62% of |c_3|. "
            "Derived here as sigma(Q_beta)/(Q_N2 u^3) from the committed CAL-3 input "
            "rather than quoted, reproducing 1.262. In sigma the agreements are 0.031 "
            "(proton) and 0.008 (muon): not strong evidence but NO evidence, since "
            "every candidate within the band agrees as well. The 1-sigma acceptance is "
            "51x wider than the 0.0491 genericity window the 7/7-constants result used, "
            "so that result understates the problem by ~51x. Testability needs 32x "
            "(proton) / 130x (muon) sharper Q_beta, bracketing the 25.68x the "
            "zero-location test needs — same lever. Scope-(a): does NOT refute (H1)."),
        "audit_only": True,
        "tier": "error propagation on committed values (no fit)",
        "q0Anchor": "proton",
        "q0Value": mp.nstr(q_p, 25),
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "vol_4_1": mp.nstr(VOL41, 16),
            "sigma_Qbeta_MeV": mp.nstr(sigma_qb, 8),
            "Qbeta_quoted": qb_quoted,
            "per_anchor": rows,
            "significance": sig,
            "sigma_c3_over_abs_c3_pct": mp.nstr(
                sigma_c3_p / abs(c3p) * 100, 6),
            "one_sigma_acceptance_lo": mp.nstr(lo, 12),
            "one_sigma_acceptance_hi": mp.nstr(hi, 12),
            "one_sigma_acceptance_width": mp.nstr(accept_width, 12),
            "genericity_window_width": mp.nstr(GENERICITY_WINDOW_WIDTH, 12),
            "acceptance_over_genericity_window": mp.nstr(ratio, 12),
            "Qbeta_improvement_for_1sigma_proton": mp.nstr(need_p, 8),
            "Qbeta_improvement_for_1sigma_muon": mp.nstr(need_m, 8),
            "Qbeta_improvement_for_zero_location_test": "25.679447 (PR #5084)",
        },
        "context": {
            "axis": "(H1) c_3^even = -Vol(4_1) — significance of the stated evidence",
            "inputs": [
                "computations/cal-3-q-beta.witness.json (sigma(Q_beta))",
                "computations/qbeta/qbeta_utils.py::c3_target_at",
                "computations/probes/aomega_o2_stokes_to_observable_mechanism.py "
                "(the +/-1.262 band, cross-checked not assumed)",
                "computations/qbeta/sleak_offset_genericity_check.py (window width)",
            ],
            "scope": (
                "Scope-(a). Does NOT refute (H1); no invariant is named forbidding a "
                "4_1-volume ingredient in c_3's bar-even part. What it shows is that "
                "the EVIDENCE cited for (H1) does not discriminate at present "
                "resolution, and that the '0.48%' phrasing overstates it by omitting "
                "an error bar 32x the discrepancy."),
            "sites_to_rescope": [
                "docs/coordination/ck-dk-canonical-registry.md (the surviving-fact line)",
                "content/quantum-observable-universe/mass-theory/"
                "rem-qstar-decay-sector-q0.md (same phrasing)",
            ],
        },
    }

    out_path = HERE / "qbeta-h1-significance-against-cal3-band.witness.json"
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out_path
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, f, indent=2)
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"\nwitness -> {out_path}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
