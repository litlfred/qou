#!/usr/bin/env python3
"""
B3 slice (bean ciei) -- the Habiro/ladder basis carries index-alternating bar-parity.

Pre-stated in ledger SS4-sexies (commit d193553c) BEFORE this run.

  B3-K1  Kashaev shadow: omega_k(x=1, q) = (q;q)_k * (q^-1;q^-1)_k exactly
         (the x=1 specialization of the 4_1 cyclotomic basis is the
         bar-symmetric Kashaev double).
  B3-K2  index-alternating parity:
         (q^-1;q^-1)_k = (-1)^k * q^{-k(k+1)/2} * (q;q)_k exactly --
         the one-sided basis element (q;q)_k is bar-EVEN for even k and
         bar-ODD for odd k, up to a monomial twist.

Consequence (structural, fibre-level): a bar-even element expanded in the
one-sided Habiro basis sources bar-ODD content through odd-index basis
vectors -- the Stage-B parity re-mix is supplied by the BASIS. The u-side
transfer (u = b*hbar_q^2 is a real composite) remains open.

Exact symbolic. NO anchors, NO c_k value, NO fit, NO wiring.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp


def _repo_head_sha():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=os.path.dirname(os.path.abspath(__file__)), text=True,
        ).strip()
    except Exception:
        return None


def main():
    q, x = sp.symbols("q x", positive=True)
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    def poch(k, base):
        """(base; base)_k = prod_{j=1}^k (1 - base^j)."""
        p = sp.Integer(1)
        for j in range(1, k + 1):
            p *= (1 - base**j)
        return p

    def omega(k):
        w = sp.Integer(1)
        for j in range(1, k + 1):
            w *= (x + 1 / x - q**j - q ** (-j))
        return w

    # --- B3-K1: omega_k(x=1) = (q;q)_k (q^-1;q^-1)_k, k = 0..6. ---
    k1 = all(
        sp.simplify(sp.cancel(sp.together(
            omega(k).subs(x, 1) - poch(k, q) * poch(k, 1 / q)))) == 0
        for k in range(0, 7)
    )
    check("B3K1_omega_x1_equals_kashaev_double_k0_6", k1)

    # --- B3-K2: (q^-1;q^-1)_k = (-1)^k q^{-k(k+1)/2} (q;q)_k, k = 1..8. ---
    k2 = all(
        sp.simplify(sp.cancel(sp.together(
            poch(k, 1 / q)
            - (-1) ** k * q ** sp.Rational(-k * (k + 1), 2) * poch(k, q)))) == 0
        for k in range(1, 9)
    )
    check("B3K2_poch_bar_twist_minus1_k_qpow_k1_8", k2)

    # Parity readout per index (recorded): twist sign alternates with k.
    parity_by_index = {k: ("even" if k % 2 == 0 else "odd") for k in range(1, 9)}

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "B3 slice PASS -- the one-sided Habiro basis (q;q)_k has INDEX-ALTERNATING "
        "bar-parity: bar((q;q)_k) = (-1)^k q^{-k(k+1)/2} (q;q)_k (Lean factor "
        "certificate pochFactor_bar_twist + full product pochNum_bar_twist, ZBarParity "
        "SS7). The x=1 shadow of the 4_1 cyclotomic basis is the bar-symmetric Kashaev "
        "double (q;q)_k(q^-1;q^-1)_k. Consequence: a bar-EVEN element (the 4_1 "
        "skeleton, C_k = 1) expanded one-sidedly sources bar-ODD content through "
        "odd-index basis vectors -- the Stage-B parity re-mix is supplied by the "
        "BASIS, not the coefficients. Fibre-level only; the u-side transfer stays "
        "open. NOT a closure, NO c_k value, nothing wired."
        if all_passed else
        "KILL -- an identity failed symbolically; the parity-re-mix-via-basis "
        "picture is wrong. Record and fall back to carrier-side re-mix."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-b3-ladder-basis-parity",
        "description": "B3 slice (bean ciei): Kashaev shadow of the 4_1 cyclotomic "
                       "basis at x=1 + index-alternating bar-parity of the one-sided "
                       "Habiro basis (q;q)_k. Pre-stated in ledger SS4-sexies "
                       "(commit d193553c).",
        "audit_only": True,
        "tier": "structural-exact (symbolic identities; no fit, no anchors)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "sympy",
        "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "kashaev_shadow": "omega_k(x=1) = (q;q)_k (q^-1;q^-1)_k",
            "basis_bar_twist": "(q^-1;q^-1)_k = (-1)^k q^{-k(k+1)/2} (q;q)_k",
            "parity_by_index": parity_by_index,
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone, bean ciei (I-B step B3, first slice)",
            "prestatement": "docs/coordination/z-ck-fmap-keystone.md SS4-sexies (commit d193553c)",
            "b1_b2": "computations/qbeta/qbeta-b1-fourone-cyclotomic-rebasing.witness.json",
            "lean_certificate": "QOU.QBeta.pochFactor_bar_twist / pochNum_bar_twist (ZBarParity SS7)",
            "stage_b_parity_remix": "1ppq-qbeta.md cont. 19 (level bar-parity ladder)",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-b3-ladder-basis-parity.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)

    print("=== B3 slice : ladder-basis index parity ===")
    print("VERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
