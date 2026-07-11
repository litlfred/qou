#!/usr/bin/env python3
"""
Verification of the 2026-07-08 "Exact topological derivation of the Q_β c_3
keystone" claim (docs/audits/2026-07-08-qbeta-keystone-derivation.md; commit
e21a942632). Runs the proton+muon CROSS-ANCHOR test the claim skipped (registry
§8 flip-flop guard), and the claim's OWN O(u³) residual bound. Self-contained;
NO fit, NO wiring, NO c_k value changed, NO tier change.

The claim: c_3 = -Vol(4_1) + u - (10/3)·u²  is an "exact topological derivation".
The verdict (scope-(a), per the refuted-discipline): this is a MUON-ANCHORED
numerical NEAR-MATCH, not a derivation — it matches the muon anchor to ~0.07% and
MISSES the proton anchor by the entire ~2.4% cross-anchor swing. The formula's
only q-dependence is u=b·ℏ_q², which is anchor-invariant to ~2×10⁻⁷, so it returns
ONE value while c_3 swings 2.4%. The numerical observation is real and worth
recording; the "PROVEN / exact derivation" scope is wrong.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import mpmath as mp

mp.mp.dps = 40


def _find_repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "computations")) and \
           os.path.exists(os.path.join(d, "AGENTS.md")):
            return d
        d = os.path.dirname(d)
    raise RuntimeError("repo root not found")


_REPO_ROOT = _find_repo_root()


def _repo_head_sha():
    # CI env vars first (minimal containers without a full clone still carry these).
    for env_var in ("GITHUB_SHA", "GIT_COMMIT_SHA"):
        v = os.environ.get(env_var)
        if v and v.strip():
            return v.strip()
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=_REPO_ROOT, text=True).strip()
    except (subprocess.SubprocessError, OSError) as e:
        raise RuntimeError(f"cannot resolve commitSha ({e}) — refusing to emit witness") from e
    if not sha:
        raise RuntimeError("empty commitSha — refusing to emit witness without provenance")
    # NOTE: deliberately RAISE rather than return "unknown" (Gemini's suggested
    # fallback). Per I14 PROV_MISSING, a witness must never carry fake provenance —
    # a loud failure is better than laundering an empty commitSha.
    return sha


def main():
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    Vol41 = 2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))

    # Substrate u = b·ℏ_q², ℏ_q = 1 − 1/q0, at BOTH documented anchors. The claim
    # hardcodes u = 0.008505403136757 (muon-anchored, single value). We derive b
    # from that + the muon ℏ_q, then evaluate u at BOTH anchors to show it is
    # anchor-invariant to ~2×10⁻⁷ (so the formula returns one value).
    q_muon = mp.mpf("1.10997859555733471")
    q_proton = mp.mpf("1.10997858275138")
    u_claim = mp.mpf("0.008505403136757")
    hbar_muon = 1 - 1 / q_muon
    b = u_claim / hbar_muon ** 2
    u_muon = b * (1 - 1 / q_muon) ** 2
    u_proton = b * (1 - 1 / q_proton) ** 2
    print(f"=== substrate u at both anchors (b={mp.nstr(b,8)}) ===")
    print(f"  u_muon   = {mp.nstr(u_muon,12)}")
    print(f"  u_proton = {mp.nstr(u_proton,12)}")
    print(f"  u relative anchor difference = {mp.nstr(abs(u_proton/u_muon-1),3)} "
          f"(⇒ formula is effectively anchor-invariant)")
    check("u_is_anchor_invariant_to_1e6", abs(u_proton / u_muon - 1) < mp.mpf("1e-6"))

    def formula(u):
        return -Vol41 + u - mp.mpf(10) / 3 * u ** 2

    f_muon = formula(u_muon)
    f_proton = formula(u_proton)

    # Canonical c_3 at both anchors (merged cross-anchor verdict 2026-07-06).
    c3_muon = mp.mpf("-2.02018812814143946")
    c3_proton = mp.mpf("-2.06934257711516784")

    miss_muon = abs(f_muon / c3_muon - 1)
    miss_proton = abs(f_proton / c3_proton - 1)
    print(f"\n=== cross-anchor test (the claim skipped this) ===")
    print(f"  formula(u_muon)   = {mp.nstr(f_muon,10)}  vs c_3 muon   {mp.nstr(c3_muon,10)}"
          f"  → miss {mp.nstr(miss_muon,3)}")
    print(f"  formula(u_proton) = {mp.nstr(f_proton,10)}  vs c_3 proton {mp.nstr(c3_proton,10)}"
          f"  → miss {mp.nstr(miss_proton,3)}")
    # Muon near-match is real (< 0.1%); proton misses by the whole swing (> 2%).
    check("muon_is_a_near_match_lt_0p1pct", miss_muon < mp.mpf("1e-3"))
    check("proton_missed_by_full_swing_gt_2pct", miss_proton > mp.mpf("0.02"))

    # The claim's OWN bound: "residual zero within O(u³) truncation".
    u3_bound_rel = u_muon ** 3 / abs(c3_muon)
    print(f"\n=== the claim's own O(u³) bound vs the actual muon residual ===")
    print(f"  claimed O(u³) rel bound = {mp.nstr(u3_bound_rel,3)}")
    print(f"  actual muon residual    = {mp.nstr(miss_muon,3)}")
    print(f"  actual/claimed ratio    = {mp.nstr(miss_muon/u3_bound_rel,4)}×  "
          f"(residual is FAR larger than the claimed truncation bound)")
    check("muon_residual_exceeds_claimed_u3_bound_by_100x",
          miss_muon / u3_bound_rel > 100)

    # Cross-anchor swing: formula is fixed, c_3 swings.
    c3_swing = abs(c3_proton / c3_muon - 1)
    f_swing = abs(f_proton / f_muon - 1)
    print(f"\n=== fixed formula vs swinging c_3 ===")
    print(f"  c_3 cross-anchor swing     = {mp.nstr(c3_swing,3)}")
    print(f"  formula cross-anchor swing = {mp.nstr(f_swing,3)} (≈0 ⇒ cannot track c_3)")
    check("formula_cannot_reproduce_swing", f_swing < mp.mpf("1e-6") < c3_swing)

    # Sector check: -Vol(4_1) (even/amphichiral, CS=0) ≠ the c_3 near-match -2
    # (= J_Hopf(q=1), odd/chiral). They are numerically close but different sectors.
    hopf_shadow = mp.mpf(-2)  # C_Hopf(2) = J_Hopf(q=1), the odd-channel near-match
    print(f"\n=== sector conflation ===")
    print(f"  -Vol(4_1) = {mp.nstr(-Vol41,8)} (EVEN/amphichiral, CS=0)  vs  "
          f"J_Hopf(1) = {int(hopf_shadow)} (ODD/chiral)  Δ={mp.nstr(abs(-Vol41-hopf_shadow),3)}")
    check("vol41_and_hopf_shadow_are_distinct_sectors",
          abs(-Vol41 - hopf_shadow) > mp.mpf("0.02"))

    all_passed = all(x["passed"] for x in assertions)
    verdict = (
        "SCOPE-(a) re-scope of the 2026-07-08 'exact topological derivation' of "
        "c_3. The formula c_3 = -Vol(4_1)+u-(10/3)u² is a MUON-ANCHORED numerical "
        f"near-match (miss {mp.nstr(miss_muon,3)}), NOT a derivation: it MISSES the "
        f"proton anchor by {mp.nstr(miss_proton,3)} — the entire {mp.nstr(c3_swing,3)} "
        "cross-anchor swing — because its only q-dependence is u (anchor-invariant "
        "to ~2×10⁻⁷), so it returns one fixed value while c_3 swings. Its OWN 'residual "
        f"zero within O(u³)' claim is false: the muon residual is {mp.nstr(miss_muon/u3_bound_rel,3)}× "
        "the claimed bound. It conflates sectors (-Vol(4_1)=-2.030 is the EVEN/"
        "amphichiral CS=0 face; the c_3 near-match -2 = J_Hopf(1) is the ODD/chiral "
        "face — #3487). And its Lean 'certification' proves def=def by rfl on "
        "hardcoded decimal literals (Vol_4_1, u, 10/3) — zero content (anti-laundering "
        "§'Axiomatization is NOT a Proof'). The numerical near-match is real and worth "
        "recording; the 'PROVEN / exact derivation' scope violates the registry §8 "
        "flip-flop guard (mandatory proton+muon cross-anchor test). c_3 stays tier "
        "empirical. No fit; no c_k value; no wiring; no tier change."
        if all_passed else
        "INCONCLUSIVE — a cross-anchor/bound/sector assertion did not hold as expected."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-c3-keystone-overclaim-verification",
        "description": "Cross-anchor + O(u³)-bound + sector verification re-scoping "
                       "the 2026-07-08 'exact topological derivation' of c_3 from "
                       "PROVEN to muon-anchored fit (fails proton cross-anchor).",
        "audit_only": True,
        "tier": "structural-exact (cross-anchor test; refutes the 'exact' scope, keeps the near-match)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "formula_value": mp.nstr(f_muon, 10),
            "miss_muon": mp.nstr(miss_muon, 4),
            "miss_proton": mp.nstr(miss_proton, 4),
            "c3_cross_anchor_swing": mp.nstr(c3_swing, 4),
            "muon_residual_vs_claimed_u3_bound_ratio": mp.nstr(miss_muon / u3_bound_rel, 4),
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone: c_3 over-claim re-scope",
            "target": "docs/audits/2026-07-08-qbeta-keystone-derivation.md (commit e21a942632)",
            "discipline": "registry §8 flip-flop guard (proton+muon cross-anchor); "
                          "anti-laundering 'Axiomatization is NOT a Proof'",
            "correct_sector_split": "#3487 parity↔chirality: -Vol=even/amphichiral, "
                                    "-2=J_Hopf odd/chiral",
            "production_safe": "grep clean — canonical_mass/registry/dashboards NOT wired",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-c3-keystone-overclaim-verification.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("\nVERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
