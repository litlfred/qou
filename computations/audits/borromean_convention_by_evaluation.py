#!/usr/bin/env python3
"""Which convention does each undeclared Borromean tracer ACTUALLY implement?

Bean `qou-yk03` / registry R5. `docs/coordination/trace_convention_registry_validate.py`
reports 22 warnings of the form

    R5 <file>::<symbol> computes a Borromean Markov trace without declaring
       its convention

and the obvious response -- read each function and write a `convention X`
comment above it -- is the exact failure this registry exists to record. Its
own R9 docstring:

    "R4 and R5 compare a DOCSTRING STRING to a REGISTRY STRING and never look
     at a number. On 2026-08-09 a stale docstring and a stale registry agreed
     with each other, and this validator reported `PASS, 0 errors` while the
     repo held four convention-C production entry points, three convention
     hybrids (D in one factor, C in another inside one function) and a
     symbolic path serving convention C out of a JSON witness cache. Every one
     of those is invisible to a string comparison and none survives an
     evaluation."

So a declaration written from reading is worth nothing; it would satisfy R5
while leaving R9's defect class untouched, and would additionally make the
registry ASSERT something nobody measured. This audit settles each one by
CALLING IT at the substrate q0 and comparing against the registry's own
reference values:

    convention C  value_at_beta_bor = 0.99836662258571596689547601136759437451
    convention D  value_at_beta_bor = 0.99856216383678726595121313514665020209

They differ at the 4th decimal, so the two are cleanly separable and a
"neither" verdict is meaningful rather than a tolerance artefact.

ISOLATION. Each candidate is called in its OWN SUBPROCESS. Several of these
modules do work at import (some write witnesses), and a shared interpreter
would let one module's `mp.dps` or `sys.path` mutation decide another's
verdict -- the same in-process coupling that produced the "passed only in
isolation" misclassification recorded in AGENTS.md's producer-runner notes.

ARGUMENT SHAPES. The 22 do not share a signature: some take `q`, some the
Hecke variable `h = q - 1/q`, some `(q, q_inv)`, some nothing. The worker
introspects the signature and supplies q0-derived values by parameter NAME,
and reports `uncallable` rather than guessing when a name is unrecognised. A
guessed argument is a fabricated verdict.

WHAT A VERDICT DOES AND DOES NOT LICENSE. `D` means the function reproduces
the registry's convention-D Borromean value at q0 -- it does NOT mean the
function is correct, in production, or that its docstring is right. `C` is a
migration item, not a defect to silently rewrite: AGENTS.md records that
deliberate C references exist and MUST STAY C. `neither` most often means the
function is not a normalised Borromean z-trace at all (a bare character, an
unnormalised sum, a volume) and is a candidate for `discovery.exempt`, which
is a registry edit and not a source edit.

No float64: mpmath at the module default dps; values compared as mpf.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
REGISTRY = ROOT / "docs/coordination/trace-convention-registry.json"

# (file, symbol) exactly as the validator reports them.
CANDIDATES = [
    ("computations/_h4_substrate.py", "trM_borromean_closed"),
    ("computations/_li_2_q_util.py", "borromean_markov_trace_h2"),
    ("computations/alpha/alpha_k_jones_markov_h12.py", "tr_M_borromean"),
    ("computations/gamma_gamma_pair_production_decomposition.py",
     "markov_trace_borromean_via_jones"),
    ("computations/hecke/phi0_normalization_disproof.py", "trM_borromean"),
    ("computations/mu_p_pin_sensitivity_map.py", "trM_borromean"),
    ("computations/ocneanu_12_alt_knot_geometries.py", "trM_borromean_closed"),
    ("computations/ocneanu_12_bring_zero_mode_variants.py", "trM_borromean_closed"),
    ("computations/ocneanu_12_em_correction_candidate.py", "trM_borromean_closed"),
    ("computations/ocneanu_12_qdeformation_discriminator.py", "trM_borromean_closed"),
    ("computations/ocneanu_12_route_reexam.py", "trM_borromean_closed"),
    ("computations/ocneanu_54ppb_residual_exploration.py", "trM_borromean_closed"),
    ("computations/probes/gap_a4_T18_markov_normalization_probe.py",
     "tr_M_borromean_closed_form"),
    ("computations/probes/m_pi_hecke_prediction_probe.py", "trM_borromean"),
    ("computations/probes/tau_all_orders_h6_empirical.py", "trM_borromean"),
    ("computations/rt_habiro_borromean_cross_validation.py",
     "tr_M_borromean_closed_form"),
    ("computations/run_jones_markov_atlas_all_atoms.py", "tr_M_borromean"),
    ("computations/two_quark_hopf_vs_borromean_sdp.py", "tr_M_borromean"),
    ("computations/two_quark_volume_weighted_clean.py", "tr_M_borromean"),
    ("computations/volume_def_reconcile.py", "borromean_trM_normalized"),
    ("computations/yekutieli_borromean_h2_extraction.py",
     "borromean_markov_trace_at_q"),
    # GENERATED MIRROR of computations/_li_2_q_util.py. Never hand-edit; it is
    # produced by scripts/sync-qou-mass-vendor.py, so the source's fix
    # propagates here. Included so the count matches the validator's.
    ("qou-mass/src/qou_mass/_internal/_li_2_q_util.py", "borromean_markov_trace_h2"),
]

WORKER = r'''
import sys, json, inspect
from pathlib import Path
root, rel, sym = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, str(Path(root) / "computations"))
try:
    import _path_bridge  # noqa: F401
except Exception:
    pass
out = {"file": rel, "symbol": sym}
try:
    from mpmath import mp
    from qou_substrate.constants import Q_50_DIGIT_STR
    mp.dps = 60
    q0 = mp.mpf(Q_50_DIGIT_STR)
    import importlib.util
    p = Path(root) / rel
    spec = importlib.util.spec_from_file_location("_cand_" + sym, p)
    m = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = m
    spec.loader.exec_module(m)
    fn = getattr(m, sym)
    sig = inspect.signature(fn)
    # Supply arguments BY PARAMETER NAME. An unrecognised required parameter is
    # reported, never guessed: a guessed argument is a fabricated verdict.
    supply = {
        "q": q0, "q_val": q0, "q0": q0, "qv": q0,
        "q_inv": 1 / q0, "qi": 1 / q0,
        "h": q0 - 1 / q0, "h_val": q0 - 1 / q0,
    }
    kwargs, unknown = {}, []
    for name, par in sig.parameters.items():
        if par.kind in (par.VAR_POSITIONAL, par.VAR_KEYWORD):
            continue
        if name in supply:
            kwargs[name] = supply[name]
        elif par.default is not par.empty:
            continue
        else:
            unknown.append(name)
    if unknown:
        out["verdict"] = "uncallable"
        out["reason"] = "unrecognised required parameter(s): " + ",".join(unknown)
    else:
        v = fn(**kwargs)
        out["value"] = mp.nstr(mp.mpf(str(v)), 30)
except Exception as e:
    out["verdict"] = "uncallable"
    out["reason"] = type(e).__name__ + ": " + str(e)[:160]
print("__RESULT__" + json.dumps(out))
'''


def main() -> int:
    reg = json.loads(REGISTRY.read_text())
    ref = {c["id"]: c.get("value_at_beta_bor") for c in reg["conventions"]}
    from mpmath import mp
    mp.dps = 60
    refC, refD = mp.mpf(ref["C"]), mp.mpf(ref["D"])
    tol = mp.mpf("1e-12")

    worker = Path(ROOT / "computations/audits/_borromean_conv_worker.py")
    worker.write_text(WORKER)
    rows, tally = [], {}
    try:
        for rel, sym in CANDIDATES:
            r = subprocess.run(
                [sys.executable, str(worker), str(ROOT), rel, sym],
                capture_output=True, text=True, timeout=180, cwd=str(ROOT))
            rec = {"file": rel, "symbol": sym, "verdict": "uncallable",
                   "reason": "worker produced no result"}
            for line in (r.stdout or "").splitlines():
                if line.startswith("__RESULT__"):
                    rec = json.loads(line[len("__RESULT__"):])
                    break
            if "value" in rec:
                v = mp.mpf(rec["value"])
                dC, dD = abs(v - refC), abs(v - refD)
                if dD < tol:
                    rec["verdict"] = "D"
                elif dC < tol:
                    rec["verdict"] = "C"
                else:
                    rec["verdict"] = "neither"
                rec["dist_to_C"] = mp.nstr(dC, 6)
                rec["dist_to_D"] = mp.nstr(dD, 6)
            rows.append(rec)
            tally[rec["verdict"]] = tally.get(rec["verdict"], 0) + 1
    finally:
        worker.unlink(missing_ok=True)

    print(f"reference  C = {mp.nstr(refC, 24)}")
    print(f"reference  D = {mp.nstr(refD, 24)}   (differ at the 4th decimal)\n")
    print(f"{'verdict':<10} {'file::symbol'}")
    for rec in rows:
        print(f"{rec['verdict']:<10} {rec['file']}::{rec['symbol']}")
        if rec["verdict"] == "uncallable":
            print(f"           -> {rec.get('reason', '')[:110]}")
        elif rec["verdict"] == "neither":
            print(f"           -> value {rec.get('value', '')[:26]}  "
                  f"dC={rec.get('dist_to_C', '')[:10]} dD={rec.get('dist_to_D', '')[:10]}")
    print("\ntally:", tally)

    out = ROOT / "computations/audits/borromean-convention-by-evaluation.json"
    out.write_text(json.dumps({
        "schema": "borromean-convention-by-evaluation/v1",
        "bean": "qou-yk03",
        "reference_values": {"C": str(refC), "D": str(refD)},
        "tolerance": "1e-12",
        "method": "each candidate called in its own subprocess at the substrate "
                  "q0; arguments supplied BY PARAMETER NAME, never guessed. A "
                  "verdict of D means the function reproduces the registry's "
                  "convention-D Borromean value -- NOT that it is correct, in "
                  "production, or that its docstring agrees. C is a migration "
                  "item, not a defect to rewrite: deliberate C references exist "
                  "and must stay C. 'neither' usually means the function is not "
                  "a normalised Borromean z-trace at all and is a candidate for "
                  "discovery.exempt, which is a registry edit, not a source one.",
        "tally": tally,
        "rows": rows,
    }, indent=2) + "\n")
    print(f"wrote {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
