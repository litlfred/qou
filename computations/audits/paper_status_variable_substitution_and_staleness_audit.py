#!/usr/bin/env python3
"""paper_status_variable_substitution_and_staleness_audit.py

End-to-end reproducible audit and dependency trace of:
  1. Variable Substitution (`ValueRegistry` `:val[...]` & Liquid `{{ qou... }}`)
     vs hardcoded numerical predictions, residuals (`ppb`/`ppm`/`ppQ`/`sigma`/`%`),
     and tables across Status/Scorecard docs, Main Paper chapters, and Appendices.
  2. Stale Witnesses relative to current compute (producer `scriptHash` drift,
     `upstream_witness_hashes` `sha256` drift, unrecorded upstream staleness,
     muon/proton `q0Anchor` straddles, and wave-2 module supersession).
  3. Exact Script Upgrade Matrix for Wave-2 formulae:
     - Pillar 1: Corrected Photon (`alpha_EM` — CS resummation + Bring-Schwinger cubic)
     - Pillar 2: Two-Term QED (`M = M_QCD + M_QED` & consistent `q_2t` pin)
     - Pillar 3: GPMT Modified-Trace Completion, Mirror-Projected `alpha_D^proj`,
       Normalized 4-row `q`-Plancherel `Z_{3A}^{(4)}(q_0)`, & Untruncated `E_0^tower`.

Read-only across all existing files; writes ONLY:
  `computations/audits/paper-status-variable-substitution-and-staleness-audit.witness.json`
with zero `float64` values (`set_compute_dps(50)` + `_precision.fmt`).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

_HERE = Path(__file__).resolve().parent          # computations/audits
_COMP = _HERE.parent                             # computations
_REPO = _COMP.parent                             # repo root
if str(_COMP) not in sys.path:
    sys.path.insert(0, str(_COMP))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
from mpmath import mpf  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.constants import (  # noqa: E402
    q_at,
    q_muon_at,
    q_two_term_borromean_at,
)
from qou_substrate.witness import (  # noqa: E402
    WitnessBuilder,
    file_content_hash,
    q0_comparison,
)
from codata_constants import M_E_MEV  # noqa: E402
from canonical_mass import (  # noqa: E402
    gpmt_dmod_111,
    gpmt_dmod_211,
    gpmt_dmod_1111,
    neutron_mass_two_term_mev,
    np_qed_splitting_borromean_conn_mev,
    proton_qed_self_energy_borromean_mev,
)
from coulomb_energy import (  # noqa: E402
    coulomb_energy_mev,
    mirror_displacement_mev,
)
from meson_em_sinh_closed_form import alpha_em_inv_derived  # noqa: E402

# Set minimum 50-dps baseline per repository precision rule; heavy evaluations
# below run inside mp.workdps(70) so 50-digit fmt(..., dps=50) has 20 guard digits.
set_compute_dps(50)

SELF_WITNESS_NAME = "paper-status-variable-substitution-and-staleness-audit"
SELF_WITNESS_FILE = f"{SELF_WITNESS_NAME}.witness.json"

MAIN_CHAPTERS: list[str] = [
    "introduction",
    "quantum-universes",
    "quantum-observable-universes",
    "models-of-qous",
    "lifting-and-descent",
    "braids-and-knots",
    "brings-surface",
    "knots-particles-confinement",
    "eightfold-way",
    "mass-endomorphism",
    "climax-volume-mass",
    "mass-theory",
    "nuclear-interactions",
    "gravity-spacetime",
    "predicted-spectra",
    "observations",
    "molecular-construction",
    "organic-chemistry",
    "fluid-dynamics",
    "stochastic-mechanics",
    "information-theory",
    "measurement-observation",
    "q-geometric-langlands",
]

APPENDICES: list[str] = [
    "appendix-knot-periodic-table",
    "appendix-knot-operations",
    "appendix-knot-operations-archimedean",
    "appendix-transfer-matrices",
    "appendix-mass-binding-algorithms",
    "appendix-standard-model",
    "appendix-nf-witnesses",
    "appendix-qvalues",
    "appendix-surreals",
    "appendix-surreals-archimedean",
]

BACKMATTER: list[str] = [
    "glossary",
    "index-of-definitions",
    "notation",
]

STATUS_DOC_PATHS: list[str] = [
    "docs/precision-goals.md",
    "docs/observable-sector-tracker.md",
    "docs/audits/onepb-status-dashboard.md",
    "docs/coordination/1ppb.md",
]

LIQUID_RE = re.compile(
    r"\{\{\s*([A-Za-z_][\w-]*(?:\.[A-Za-z0-9_][\w-]*)+)([^}]*)\}\}"
)
VAL_RE = re.compile(r":val\[([A-Za-z_][A-Za-z0-9_]*)\](?:\{([^}]*)\})?")
LEANVAL_RE = re.compile(r":leanval\[([A-Za-z_][A-Za-z0-9_]*)\](?:\{([^}]*)\})?")
RESIDUAL_RE = re.compile(
    r"(?:[+-]?\d+(?:\.\d+)?(?:\s*(?:\\times|×)\s*10\^\{?[+-]?\d+\}?|[eE][+-]?\d+)?"
    r"\s*(?:ppb|ppm|ppQ|\\sigma|σ|%))"
)
KEY_OBS_LITERAL_RE = re.compile(
    r"(?:\b137\.03\d*|\b938\.272\d*|\b939\.565\d*|\b0\.510998\d*"
    r"|\b206\.768\d*|\b105\.658\d*|\b0\.7823\d*|\b1\.2933\d*"
    r"|\b4\.1859\d*|\b4\.2278\d*|\b246\.2\d*|\b1\.109978\d*)"
)
PIPE_TABLE_ROW_RE = re.compile(r"^\|.*\|$", re.M)


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _json_get_path(doc: Any, dotted_path: str) -> tuple[bool, Any]:
    cur = doc
    for seg in dotted_path.split("."):
        if isinstance(cur, dict) and seg in cur:
            cur = cur[seg]
        elif isinstance(cur, list) and seg.isdigit() and int(seg) < len(cur):
            cur = cur[int(seg)]
        else:
            return False, None
    return True, cur


def _solve_bring_schwinger_cubic(q: mpf) -> tuple[mpf, mpf]:
    """Solve Form A quadratic and Form B cubic from alpha_em_schwinger_ladder_probe.py:
      T = q * [9]_q * [10]_q + 8 / (12 * pi),  H = [2]_q / (8 * pi),  h^2 = (q - 1/q)^2
      Form A: H * alpha^2 + T * alpha - 1 = 0
      Form B: -H * h^2 * alpha^3 + H * alpha^2 + T * alpha - 1 = 0  (1/alpha = T + alpha*H*(1 - h^2*alpha))
    Returns (alpha_inv_formA, alpha_inv_formB).
    """
    def qb(n: int) -> mpf:
        return (q**n - q ** (-n)) / (q - mpf(1) / q)

    h2 = (q - mpf(1) / q) ** 2
    t_term = q * qb(9) * qb(10) + mpf(8) / (mpf(12) * mp.pi)
    h_term = qb(2) / (mpf(8) * mp.pi)
    a_form_a = (-t_term + mp.sqrt(t_term * t_term + mpf(4) * h_term)) / (mpf(2) * h_term)
    a = a_form_a
    for _ in range(35):
        f_val = -h_term * h2 * (a**3) + h_term * (a**2) + t_term * a - mpf(1)
        df_val = -mpf(3) * h_term * h2 * (a**2) + mpf(2) * h_term * a + t_term
        da = f_val / df_val
        a -= da
        if abs(da) < mpf("1e-68"):
            break
    return mpf(1) / a_form_a, mpf(1) / a


def compute_wave2_reference_values() -> dict[str, Any]:
    """Compute 50-dps wave-2 reference quantities in pure mpmath (zero float64)."""
    with mp.workdps(70):
        m_e = mpf(str(M_E_MEV))
        q_p1 = q_at(dps=70)
        q_2t = q_two_term_borromean_at(dps=70)
        q_mu = q_muon_at(dps=70)

        qpin_path = _COMP / "q-pinning-50-digit.witness.json"
        qpin_doc = json.loads(qpin_path.read_text(encoding="utf-8"))
        q_frozen_str = str(qpin_doc["derived_50_digit"]["q"])
        q_frozen = mpf(q_frozen_str)

        def q_bal(k: int, q: mpf) -> mpf:
            return (q**k - q ** (-k)) / (q - mpf(1) / q)

        alpha_inv_bare = q_p1 * q_bal(9, q_p1) * q_bal(10, q_p1)
        alpha_inv_cs = alpha_em_inv_derived(q_p1, order=None)
        alpha_inv_form_a, alpha_inv_cubic = _solve_bring_schwinger_cubic(q_p1)
        alpha_inv_codata2022 = mpf("137.035999177")

        err_cs_ppb = (
            (alpha_inv_cs - alpha_inv_codata2022) / alpha_inv_codata2022 * mpf("1e9")
        )
        err_form_a_ppb = (
            (alpha_inv_form_a - alpha_inv_codata2022)
            / alpha_inv_codata2022
            * mpf("1e9")
        )
        err_cubic_ppb = (
            (alpha_inv_cubic - alpha_inv_codata2022)
            / alpha_inv_codata2022
            * mpf("1e9")
        )

        mp_qed_self = proton_qed_self_energy_borromean_mev(k_weighted=False)
        np_qed_conn = np_qed_splitting_borromean_conn_mev(weighting="plain")
        mn_2t = neutron_mass_two_term_mev(weighting="plain")
        ec_he3 = coulomb_energy_mev(2, 3)
        mirror_a3 = mirror_displacement_mev(2, 1, 3)

        hbar_q = (q_p1 - mpf(1)) / q_p1
        e0_m0 = m_e / (q_p1 * (q_p1 - mpf(1)))
        e0_tower = e0_m0 / (mpf(1) - hbar_q**2)
        e0_closed = (m_e * q_p1) / ((q_p1 - mpf(1)) * (mpf(2) * q_p1 - mpf(1)))
        e0_shift_ppb = (e0_tower - e0_m0) / e0_m0 * mpf("1e9")

        h_2t = q_2t - mpf(1) / q_2t
        z_d_2t = (q_2t**3) / (q_2t**2 + mpf(1))
        alpha_d_unproj = (z_d_2t - mpf(1)) * h_2t / mpf(2)
        alpha_d_proj = alpha_d_unproj - (h_2t**2) / mpf(4)

        dmod_111 = gpmt_dmod_111(q_2t)
        dmod_211 = gpmt_dmod_211(q_2t)
        dmod_1111 = gpmt_dmod_1111(q_2t)

        dq_2t_vs_p1_ppb = (q_2t - q_p1) / q_p1 * mpf("1e9")
        dq_frozen_vs_mu_ppb = (q_frozen - q_mu) / q_mu * mpf("1e9")
        dq_frozen_vs_p1_ppb = (q_frozen - q_p1) / q_p1 * mpf("1e9")

        return {
            "q0_proton_1term": fmt(q_p1, dps=50),
            "q0_two_term_borromean": fmt(q_2t, dps=50),
            "q0_muon_live_codata2022": fmt(q_mu, dps=50),
            "q0_pinning_witness_frozen_muon": fmt(q_frozen, dps=50),
            "dq_two_term_minus_1term_ppb": fmt(dq_2t_vs_p1_ppb, dps=50),
            "dq_frozen_witness_minus_live_muon_ppb": fmt(dq_frozen_vs_mu_ppb, dps=50),
            "dq_frozen_witness_minus_1term_proton_ppb": fmt(dq_frozen_vs_p1_ppb, dps=50),
            "alpha_em_inv_bare_q9q10": fmt(alpha_inv_bare, dps=50),
            "alpha_em_inv_cs_resummed": fmt(alpha_inv_cs, dps=50),
            "alpha_em_inv_cs_err_ppb": fmt(err_cs_ppb, dps=50),
            "alpha_em_inv_bring_form_a_quadratic": fmt(alpha_inv_form_a, dps=50),
            "alpha_em_inv_bring_form_a_err_ppb": fmt(err_form_a_ppb, dps=50),
            "alpha_em_inv_bring_schwinger_cubic": fmt(alpha_inv_cubic, dps=50),
            "alpha_em_inv_bring_schwinger_cubic_err_ppb": fmt(err_cubic_ppb, dps=50),
            "proton_qed_self_energy_borromean_mev": fmt(mp_qed_self, dps=50),
            "np_qed_splitting_borromean_conn_mev": fmt(np_qed_conn, dps=50),
            "neutron_mass_two_term_mev_at_q2t": fmt(mn_2t, dps=50),
            "coulomb_energy_3he_mev_at_q2t": fmt(ec_he3, dps=50),
            "mirror_displacement_a3_mev_at_q2t": fmt(mirror_a3, dps=50),
            "E0_truncated_M0_mev": fmt(e0_m0, dps=50),
            "E0_untruncated_tower_mev": fmt(e0_tower, dps=50),
            "E0_closed_form_me_q_over_qm1_2qm1_mev": fmt(e0_closed, dps=50),
            "E0_tower_minus_M0_rel_ppb": fmt(e0_shift_ppb, dps=50),
            "alpha_D_unprojected_at_q2t": fmt(alpha_d_unproj, dps=50),
            "alpha_D_mirror_projected_at_q2t": fmt(alpha_d_proj, dps=50),
            "gpmt_dmod_111_at_q2t": fmt(dmod_111, dps=50),
            "gpmt_dmod_211_at_q2t": fmt(dmod_211, dps=50),
            "gpmt_dmod_1111_at_q2t": fmt(dmod_1111, dps=50),
            "_raw_mpf": {
                "q_p1": q_p1,
                "q_2t": q_2t,
                "q_mu": q_mu,
                "alpha_inv_cubic": alpha_inv_cubic,
                "alpha_inv_codata2022": alpha_inv_codata2022,
                "e0_tower": e0_tower,
                "e0_closed": e0_closed,
            },
        }


def parse_value_registry() -> list[dict[str, Any]]:
    """Balanced-brace parse of WITNESSED_VALUES entries in folio/values/registry.ts."""
    reg_path = _REPO / "folio/values/registry.ts"
    raw_text = reg_path.read_text(encoding="utf-8")
    # Strip // line comments and /* ... */ block comments outside string literals
    cleaned_chars: list[str] = []
    i = 0
    n_len = len(raw_text)
    in_s: str | None = None
    esc_s = False
    while i < n_len:
        ch = raw_text[i]
        if in_s:
            cleaned_chars.append(ch)
            if esc_s:
                esc_s = False
            elif ch == "\\":
                esc_s = True
            elif ch == in_s:
                in_s = None
            i += 1
        else:
            if ch in ("\"", "'", "`"):
                in_s = ch
                cleaned_chars.append(ch)
                i += 1
            elif ch == "/" and i + 1 < n_len and raw_text[i + 1] == "/":
                while i < n_len and raw_text[i] != "\n":
                    i += 1
            elif ch == "/" and i + 1 < n_len and raw_text[i + 1] == "*":
                i += 2
                while i + 1 < n_len and not (
                    raw_text[i] == "*" and raw_text[i + 1] == "/"
                ):
                    i += 1
                i += 2
            else:
                cleaned_chars.append(ch)
                i += 1
    text = "".join(cleaned_chars)

    entries: list[dict[str, Any]] = []
    pat = re.compile(r"([A-Za-z_][A-Za-z0-9_]*)\s*:\s*Object\.freeze\(\{")
    pos = 0
    while True:
        m = pat.search(text, pos)
        if not m:
            break
        key = m.group(1)
        brace_start = m.end() - 1
        depth = 0
        in_str: str | None = None
        esc = False
        end_idx = brace_start
        for idx in range(brace_start, len(text)):
            ch = text[idx]
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == in_str:
                    in_str = None
            else:
                if ch in ("\"", "'", "`"):
                    in_str = ch
                elif ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
                    if depth == 0:
                        end_idx = idx
                        break
        body = text[brace_start + 1 : end_idx]
        pos = end_idx + 1

        def _extract_str(field: str) -> str:
            fm = re.search(
                rf"{field}\s*:\s*((?:\"[^\"]*\"\s*\+?\s*)+)", body, re.S
            )
            if not fm:
                return ""
            parts = re.findall(r"\"([^\"]*)\"", fm.group(1))
            return "".join(parts)

        wfile = _extract_str("witnessFile")
        wpath = _extract_str("witnessPath")
        if not wfile:
            continue
        nr_m = re.search(r"needsReview\s*:\s*(true|false)", body)
        needs_review = nr_m.group(1) == "true" if nr_m else False
        entries.append(
            {
                "name": key,
                "witnessFile": wfile,
                "witnessPath": wpath,
                "needsReview": needs_review,
            }
        )
    return entries


def scan_witness_corpus() -> dict[str, Any]:
    """Scan all live *.witness.json under computations/ for staleness and anchor state."""
    witness_files = sorted(
        p
        for p in _COMP.rglob("*.witness.json")
        if "_deprecated" not in p.parts
        and "fsh-guts" not in p.parts
        and p.name != SELF_WITNESS_FILE
    )

    py_by_basename: dict[str, list[Path]] = {}
    for py in _COMP.rglob("*.py"):
        if "_deprecated" in py.parts or "fsh-guts" in py.parts:
            continue
        py_by_basename.setdefault(py.name, []).append(py)

    by_rel: dict[str, dict[str, Any]] = {}
    script_hash_stale: list[str] = []
    upstream_hash_stale: list[str] = []
    missing_script: list[str] = []
    muon_anchored: list[str] = []

    for wp in witness_files:
        rel = wp.relative_to(_REPO).as_posix()
        try:
            doc = json.loads(wp.read_text(encoding="utf-8"))
        except Exception:
            continue
        sfile = doc.get("scriptFile")
        shash = doc.get("scriptHash")
        anchor = doc.get("q0Anchor")
        computed_at = str(doc.get("computedAt", ""))

        prod_rel: str | None = None
        live_shash: str | None = None
        is_shash_stale = False
        if isinstance(sfile, str) and sfile:
            cand = wp.parent / sfile
            if not cand.exists():
                cands = py_by_basename.get(sfile, [])
                cand = cands[0] if cands else cand
            if cand.exists():
                prod_rel = cand.relative_to(_REPO).as_posix()
                live_shash = file_content_hash(str(cand))
                if isinstance(shash, str) and shash and shash != live_shash:
                    is_shash_stale = True
                    script_hash_stale.append(rel)
            else:
                missing_script.append(rel)
        else:
            missing_script.append(rel)

        upstreams = []
        if isinstance(doc.get("data"), dict):
            raw_up = doc["data"].get("upstream_witness_hashes")
            if isinstance(raw_up, list):
                upstreams = raw_up

        drifted_upstreams: list[dict[str, str]] = []
        for u in upstreams:
            if not isinstance(u, dict):
                continue
            up_file = str(u.get("path") or u.get("file") or "")
            rec_sha = str(u.get("sha256") or "")
            if not up_file or not rec_sha:
                continue
            cands_up = [
                _REPO / up_file,
                _COMP / up_file,
                wp.parent / up_file,
            ]
            up_path = next((cp for cp in cands_up if cp.exists()), None)
            if up_path is not None:
                cur_sha = _sha256_file(up_path)
                if cur_sha != rec_sha:
                    drifted_upstreams.append(
                        {
                            "upstream": up_path.relative_to(_REPO).as_posix(),
                            "recorded_sha256_prefix": rec_sha[:12],
                            "live_sha256_prefix": cur_sha[:12],
                        }
                    )
            else:
                drifted_upstreams.append(
                    {
                        "upstream": up_file,
                        "recorded_sha256_prefix": rec_sha[:12],
                        "live_sha256_prefix": "MISSING",
                    }
                )
        if drifted_upstreams:
            upstream_hash_stale.append(rel)

        if anchor == "muon":
            muon_anchored.append(rel)

        by_rel[rel] = {
            "producer": prod_rel or (str(sfile) if sfile else "NONE"),
            "recorded_scriptHash": str(shash or ""),
            "live_scriptHash": str(live_shash or ""),
            "scriptHash_stale": is_shash_stale,
            "upstream_sha256_stale": bool(drifted_upstreams),
            "drifted_upstreams": drifted_upstreams,
            "upstream_count_recorded": len(upstreams),
            "q0Anchor": str(anchor or "UNSTAMPED"),
            "computedAt": computed_at,
        }

    return {
        "total_live_witnesses": len(by_rel),
        "scriptHash_stale_count": len(script_hash_stale),
        "upstream_sha256_stale_count": len(upstream_hash_stale),
        "missing_producer_script_count": len(missing_script),
        "muon_anchored_count": len(muon_anchored),
        "by_rel": by_rel,
        "muon_anchored_files": muon_anchored,
    }


def audit_variable_substitution(
    reg_entries: list[dict[str, Any]],
    witness_index: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """Audit pipeline mechanics, ValueRegistry, Liquid, .ts witness blocks, and hardcoded prose."""
    qou_dir = _REPO / "folio/quantum-observable-universe"

    # Pipeline check: verify render-markdown.ts lacks :val substitution & liquid-values.ts flat lookup
    render_md_path = (
        _REPO.parent
        / "folio-assistant/cat-harness-tools/pipeline/render-markdown.ts"
    )
    render_tex_path = (
        _REPO.parent
        / "folio-assistant/cat-harness-tools/pipeline/render-latex.ts"
    )
    liquid_ts_path = (
        _REPO.parent
        / "folio-assistant/cat-harness-tools/pipeline/liquid-values.ts"
    )

    render_md_txt = (
        render_md_path.read_text(encoding="utf-8") if render_md_path.exists() else ""
    )
    render_tex_txt = (
        render_tex_path.read_text(encoding="utf-8") if render_tex_path.exists() else ""
    )
    liquid_ts_txt = (
        liquid_ts_path.read_text(encoding="utf-8") if liquid_ts_path.exists() else ""
    )

    render_md_calls_val = (
        "renderValue" in render_md_txt or "substituteValuesInMath" in render_md_txt
    )
    render_tex_calls_val = (
        "renderValue" in render_tex_txt and "substituteValuesInMath" in render_tex_txt
    )
    liquid_flat_only = '${entry}.witness.json' in liquid_ts_txt

    def _scan_group(md_paths: list[Path]) -> dict[str, Any]:
        liq_files = 0
        liq_occ = 0
        val_files = 0
        val_occ = 0
        tbl_data_total = 0
        tbl_data_wired = 0
        inline_tbl_files = 0
        inline_tbl_num_unwired = 0
        res_files_unwired = 0
        res_files_wired = 0
        res_occ = 0
        obs_files_unwired = 0
        obs_occ = 0
        wired_details: list[dict[str, Any]] = []
        val_usage_counter: dict[str, int] = {}
        liquid_entries_used: dict[str, int] = {}

        for p in md_paths:
            txt = p.read_text(encoding="utf-8", errors="replace")
            lh = LIQUID_RE.findall(txt)
            vh = VAL_RE.findall(txt)
            wired = bool(lh or vh)
            if lh:
                liq_files += 1
                liq_occ += len(lh)
                for key, _flt in lh:
                    parts = key.split(".")
                    if len(parts) >= 3 and parts[0] == "qou":
                        entry_key = f"{parts[1]}/{parts[2]}"
                        liquid_entries_used[entry_key] = (
                            liquid_entries_used.get(entry_key, 0) + 1
                        )
            if vh:
                val_files += 1
                val_occ += len(vh)
                for vname, _attrs in vh:
                    val_usage_counter[vname] = val_usage_counter.get(vname, 0) + 1
            if wired:
                wired_details.append(
                    {
                        "file": p.relative_to(_REPO).as_posix(),
                        "liquid_refs": len(lh),
                        "val_refs": len(vh),
                        "liquid_targets": sorted(
                            {
                                f"{k.split('.')[1]}/{k.split('.')[2]}"
                                for k, _ in lh
                                if len(k.split(".")) >= 3 and k.startswith("qou.")
                            }
                        ),
                        "val_names": sorted({n for n, _ in vh}),
                    }
                )

            if re.search(r"-table\d*-data\.md$", p.name):
                tbl_data_total += 1
                if wired:
                    tbl_data_wired += 1
            else:
                rows = PIPE_TABLE_ROW_RE.findall(txt)
                if len(rows) >= 3:
                    inline_tbl_files += 1
                    if not wired and any(re.search(r"\d+\.\d+", r) for r in rows):
                        inline_tbl_num_unwired += 1

            stripped = LIQUID_RE.sub("", VAL_RE.sub("", txt))
            rh = RESIDUAL_RE.findall(stripped)
            if rh:
                res_occ += len(rh)
                if wired:
                    res_files_wired += 1
                else:
                    res_files_unwired += 1
            oh = KEY_OBS_LITERAL_RE.findall(stripped)
            if oh:
                obs_occ += len(oh)
                if not wired:
                    obs_files_unwired += 1

        return {
            "summary": {
                "md_files": len(md_paths),
                "liquid_wired_files": liq_files,
                "liquid_occurrences": liq_occ,
                "val_wired_files": val_files,
                "val_occurrences": val_occ,
                "total_wired_files": len(wired_details),
                "table_data_md_total": tbl_data_total,
                "table_data_md_wired": tbl_data_wired,
                "table_data_md_unwired": tbl_data_total - tbl_data_wired,
                "inline_pipe_table_files": inline_tbl_files,
                "inline_pipe_table_numeric_unwired": inline_tbl_num_unwired,
                "unwired_files_with_hardcoded_residuals": res_files_unwired,
                "wired_files_also_with_hardcoded_residuals": res_files_wired,
                "hardcoded_residual_occurrences": res_occ,
                "unwired_files_with_key_observable_literals": obs_files_unwired,
                "hardcoded_key_observable_literal_occurrences": obs_occ,
            },
            "wired_files": wired_details,
            "val_usage_counter": val_usage_counter,
            "liquid_entries_used": liquid_entries_used,
        }

    main_mds = sorted(
        p for ch in MAIN_CHAPTERS for p in (qou_dir / ch).rglob("*.md")
    )
    app_mds = sorted(
        p for ch in APPENDICES for p in (qou_dir / ch).rglob("*.md")
    )
    back_mds = sorted(
        p for ch in BACKMATTER for p in (qou_dir / ch).rglob("*.md")
    )
    status_mds = [
        _REPO / rel for rel in STATUS_DOC_PATHS if (_REPO / rel).exists()
    ]

    main_res = _scan_group(main_mds)
    app_res = _scan_group(app_mds)
    back_res = _scan_group(back_mds)
    status_res = _scan_group(status_mds)

    # Merge usage counters across manuscript
    all_val_usages: dict[str, int] = {}
    for d in (
        main_res["val_usage_counter"],
        app_res["val_usage_counter"],
        back_res["val_usage_counter"],
    ):
        for k, v in d.items():
            all_val_usages[k] = all_val_usages.get(k, 0) + v

    all_liquid_entries: dict[str, int] = {}
    for d in (
        main_res["liquid_entries_used"],
        app_res["liquid_entries_used"],
        back_res["liquid_entries_used"],
    ):
        for k, v in d.items():
            all_liquid_entries[k] = all_liquid_entries.get(k, 0) + v

    # Validate ValueRegistry entries against on-disk witnesses
    broken_registry_entries: list[dict[str, Any]] = []
    placeholder_registry_entries: list[dict[str, Any]] = []
    stale_backing_registry_entries: list[dict[str, Any]] = []
    unused_registry_entries: list[str] = []
    registry_witness_files = sorted({e["witnessFile"] for e in reg_entries})

    for e in reg_entries:
        wfile = e["witnessFile"]
        wpath = e["witnessPath"]
        name = e["name"]
        if all_val_usages.get(name, 0) == 0:
            unused_registry_entries.append(name)
        if e["needsReview"]:
            placeholder_registry_entries.append(e)
        full_w = _REPO / wfile
        if not full_w.exists():
            broken_registry_entries.append({**e, "reason": "witness_file_missing"})
        else:
            doc = json.loads(full_w.read_text(encoding="utf-8"))
            ok, _val = _json_get_path(doc, wpath)
            if not ok:
                broken_registry_entries.append(
                    {**e, "reason": "witness_path_missing_in_json"}
                )
        winfo = witness_index.get(wfile)
        if winfo and (winfo["scriptHash_stale"] or winfo["upstream_sha256_stale"]):
            stale_backing_registry_entries.append(
                {
                    "name": name,
                    "witnessFile": wfile,
                    "scriptHash_stale": winfo["scriptHash_stale"],
                    "upstream_sha256_stale": winfo["upstream_sha256_stale"],
                    "q0Anchor": winfo["q0Anchor"],
                }
            )

    # Scan .ts files in folio/quantum-observable-universe for witness strings (scalar & array)
    ts_files = sorted(
        p for p in qou_dir.rglob("*.ts") if "lean" not in p.parts
    )
    ts_witness_refs: dict[str, list[str]] = {}
    ts_block_count = 0
    wit_in_ts_re = re.compile(
        r"[\"']([^\"'\s]+\.witness\.json)[\"']"
    )
    for tsp in ts_files:
        ttxt = tsp.read_text(encoding="utf-8", errors="replace")
        hits = wit_in_ts_re.findall(ttxt)
        if hits:
            ts_block_count += len(hits)
            trel = tsp.relative_to(_REPO).as_posix()
            for h in hits:
                if (_REPO / h).exists():
                    norm = (_REPO / h).resolve().relative_to(_REPO).as_posix()
                elif (tsp.parent / h).exists():
                    norm = (tsp.parent / h).resolve().relative_to(_REPO).as_posix()
                elif (_COMP / h).exists():
                    norm = f"computations/{h}"
                else:
                    norm = h
                ts_witness_refs.setdefault(norm, []).append(trel)

    # Scan .lean files for :leanval[...]
    lean_files = sorted((qou_dir / "lean").rglob("*.lean"))
    leanval_occ = 0
    leanval_files = 0
    for lp in lean_files:
        ltxt = lp.read_text(encoding="utf-8", errors="replace")
        lh = LEANVAL_RE.findall(ltxt)
        if lh:
            leanval_files += 1
            leanval_occ += len(lh)

    high_priority_hardcoded_stale_sites: list[dict[str, Any]] = [
        {
            "section": "status_docs",
            "file": "docs/precision-goals.md",
            "lines": "347, 733",
            "hardcoded_claim": "Delta m_pn row says 658 ppb / misses ~151.7x (contradicting lines 55 & 390: 1.009e+8 ppb / 2.327e+7x)",
            "live_compute_status": "Two-term QED + mirror-projected alpha_D^proj + GPMT shifts nucleon sector; 0 variable substitutions in docs/",
        },
        {
            "section": "status_docs",
            "file": "docs/observable-sector-tracker.md",
            "lines": "60-69, 258-261",
            "hardcoded_claim": "L2 table says 1/5 scoreable, ships excised 2-term m_K/m_pi=23.44 ppb, m_mu=209.8 ppb, Q_beta=1248 ppb, m_n=2.389 ppb, Delta_pn=755.6 ppb, cites muon alpha^-1=137.035944, marks G_Fermi & Higgs VEV OPEN",
            "live_compute_status": "Live per-observable-100x-status has 3/6 <=100x (alpha_em_inv 0.3652 ppb / 2.38x via Bring-Schwinger cubic); electroweak_bring_schwinger_bridge_probe derives v & G_F",
        },
        {
            "section": "status_docs",
            "file": "docs/audits/onepb-status-dashboard.md",
            "lines": "45-64",
            "hardcoded_claim": "5 atoms, Max relative Delta = 2.94e-15, max_non_anchor_delta_ppb = 92.79 ppb",
            "live_compute_status": "Live cross-check-trM-1ppb.witness.json has 6 atoms, Max rel Delta = 1.208e-49, max_non_anchor_delta_ppb = 2.7755e-8 ppb",
        },
        {
            "section": "appendices",
            "file": "folio/quantum-observable-universe/appendix-standard-model/sm-params-gauge-couplings.md",
            "lines": "22, 24",
            "hardcoded_claim": "Hardcodes retired CODATA-2018 alpha_EM residuals: 1.67 ppb (Form A), +0.313 ppb, 2.1 sigma, c_2 approx +8.1e-4, 209x short",
            "live_compute_status": "Live alpha-em-schwinger-ladder.witness.json (CODATA-2022): +0.9937 ppb (Form A), -0.3652 ppb (Form B cubic, 2.38 sigma), c_2 = -9.4e-4, 238.3x",
        },
        {
            "section": "appendices",
            "file": "folio/quantum-observable-universe/appendix-qvalues/per-observable-100x-status-dashboard.md",
            "lines": "1-15",
            "hardcoded_claim": "Prose disclaimer 'Numbers are not inlined here' — prints ZERO numerical status rows in rendered PDF",
            "live_compute_status": "Backed in .ts by computations/per-observable-100x-status.witness.json, which is never templated via Liquid",
        },
        {
            "section": "appendices",
            "file": "folio/quantum-observable-universe/appendix-mass-binding-algorithms/mba-step09a-mass-identity.md",
            "lines": "90-94",
            "hardcoded_claim": "Claims canonical_mass.py has a formula fallback and omits all 2-term QED & GPMT functions",
            "live_compute_status": "Fallback removed 2026-07-19; canonical_mass.py now exports proton_qed_self_energy_borromean_mev, np_qed_splitting_borromean_conn_mev, neutron_mass_two_term_mev, gpmt_dmod_*",
        },
        {
            "section": "appendices",
            "file": "folio/quantum-observable-universe/appendix-knot-periodic-table/recursive-atom-knot-atlas-registry.md",
            "lines": "80-4782",
            "hardcoded_claim": "4,782-line generated atlas with only 1 Liquid ref (Vol_4_1_str -> stale q-pinning-50-digit) and hardcoded CODATA-2018 m_p=938.27208816, m_n=939.56542052 + 1-term QED masses",
            "live_compute_status": "atlas_render_canonical_table.py must be updated to CODATA-2022 + 2-term QED + GPMT",
        },
        {
            "section": "main_paper",
            "file": "folio/quantum-observable-universe/predicted-spectra/em-coupling-bring-zero-mode.md",
            "lines": "26-36, 58-60",
            "hardcoded_claim": "Hardcodes muon-pin q_0=1.109978595642739..., bare 136.823219729, 137.035426320, and tentative alpha/(4*pi) -> +5.7e-8",
            "live_compute_status": "Targeted by alpha-em-schwinger-ladder.witness.json (proton pin bare 136.823208854, CS 137.035935094, Bring-Schwinger cubic 137.035999127)",
        },
        {
            "section": "main_paper",
            "file": "folio/quantum-observable-universe/observations/mass-comparison-table.md",
            "lines": "21, 33-39, 53",
            "hardcoded_claim": "Uses Liquid q-pinning-50-digit (stale muon q_0!) alongside hardcoded superseded Delta_S Q_beta=0.4491 MeV (-42.59%, m_n-m_p=0.9557 MeV) and '\\text{MeV}$ MeV' typo; all 4 companion *-table*-data.md files have 0 substitutions",
            "live_compute_status": "Ruled nuc11_interleaved gives 0.6519 MeV (-16.68%); wave-2 2-term QED + mirror-projected alpha_D^proj + GPMT updates nucleon splitting",
        },
        {
            "section": "main_paper",
            "file": "folio/quantum-observable-universe/mass-theory/neutron-proton-splitting.md",
            "lines": "13",
            "hardcoded_claim": "Hybrid CODATA-2022 minus CODATA-2018 subtraction: 939.56542194 - 938.27208816 = 1.29333378 MeV labelled 'CODATA 2022 splitting'",
            "live_compute_status": "True CODATA-2022 splitting is 939.56542194 - 938.27208943 = 1.29333251 MeV (982 ppb discrepancy in prose target)",
        },
        {
            "section": "main_paper",
            "file": "folio/quantum-observable-universe/mass-theory/isospin-mass-split-em-localisation.md",
            "lines": "1-40",
            "hardcoded_claim": "Retains retired Convention-C narrative alongside outdated EM splitting prose",
            "live_compute_status": "Superseded by connected Borromean V^3 two-term QED splitting (np_qed_splitting_borromean_conn_mev)",
        },
    ]

    total_manuscript_md = (
        main_res["summary"]["md_files"]
        + app_res["summary"]["md_files"]
        + back_res["summary"]["md_files"]
    )
    total_manuscript_wired = (
        main_res["summary"]["total_wired_files"]
        + app_res["summary"]["total_wired_files"]
        + back_res["summary"]["total_wired_files"]
    )
    total_tbl_data = (
        main_res["summary"]["table_data_md_total"]
        + app_res["summary"]["table_data_md_total"]
        + back_res["summary"]["table_data_md_total"]
    )
    total_tbl_wired = (
        main_res["summary"]["table_data_md_wired"]
        + app_res["summary"]["table_data_md_wired"]
        + back_res["summary"]["table_data_md_wired"]
    )

    with mp.workdps(70):
        wired_md_frac = fmt(
            mpf(total_manuscript_wired) / mpf(total_manuscript_md), dps=50
        )
        wired_tbl_frac = fmt(
            mpf(total_tbl_wired) / mpf(total_tbl_data), dps=50
        )

    return {
        "pipeline_mechanisms": {
            "legacy_val_directive": {
                "registry_file": "folio/values/registry.ts",
                "registered_entries_count": len(reg_entries),
                "distinct_witness_files_count": len(registry_witness_files),
                "rendered_in_latex": render_tex_calls_val,
                "rendered_in_markdown_site": render_md_calls_val,
                "pipeline_defect": (
                    "render-markdown.ts calls resolveLiquidValues(mdContent) ONLY and "
                    "never invokes renderValue / substituteValuesInMath; :val[...] "
                    "tokens leak un-substituted into rendered Markdown/site output."
                ),
            },
            "liquid_knowledge_graph_binding": {
                "config_file": "qou.json",
                "resolver_file": "../folio-assistant/cat-harness-tools/pipeline/liquid-values.ts",
                "flat_directory_lookup_only": liquid_flat_only,
                "pipeline_defect": (
                    "liquid-values.ts resolves join(dir, '${entry}.witness.json') "
                    "with SEG regex forbidding '/', so witnesses in subdirectories "
                    "(computations/qbeta/, computations/probes/, computations/deltalambda/, "
                    "computations/audits/) cannot be addressed via {{ qou.computations... }}."
                ),
                "distinct_entries_used_in_manuscript": all_liquid_entries,
            },
            "ts_computation_witness_blocks": {
                "ts_files_scanned": len(ts_files),
                "computation_witness_declarations": ts_block_count,
                "distinct_witnesses_referenced": len(ts_witness_refs),
                "substitutes_prose_or_tables": False,
            },
            "leanval_directives": {
                "lean_files_scanned": len(lean_files),
                "lean_files_with_leanval": leanval_files,
                "leanval_occurrences": leanval_occ,
            },
        },
        "value_registry_health": {
            "broken_entries": broken_registry_entries,
            "needs_review_placeholders": placeholder_registry_entries,
            "entries_with_stale_backing_witness": stale_backing_registry_entries,
            "unused_entries_count": len(unused_registry_entries),
            "used_entries_in_md": all_val_usages,
        },
        "coverage_by_section": {
            "status_scorecard_docs": status_res["summary"],
            "main_paper_chapters": main_res["summary"],
            "appendices": app_res["summary"],
            "backmatter": back_res["summary"],
            "manuscript_total_md_files": total_manuscript_md,
            "manuscript_total_wired_md_files": total_manuscript_wired,
            "manuscript_wired_md_fraction_50dps": wired_md_frac,
            "manuscript_total_table_data_files": total_tbl_data,
            "manuscript_wired_table_data_files": total_tbl_wired,
            "manuscript_wired_table_fraction_50dps": wired_tbl_frac,
        },
        "all_wired_manuscript_files": (
            main_res["wired_files"]
            + app_res["wired_files"]
            + back_res["wired_files"]
        ),
        "high_priority_hardcoded_stale_sites": high_priority_hardcoded_stale_sites,
        "_ts_witness_refs": ts_witness_refs,
    }


def build_critical_stale_witness_trace(
    corpus_scan: dict[str, Any],
    var_audit: dict[str, Any],
    reg_entries: list[dict[str, Any]],
) -> dict[str, Any]:
    """Trace producer -> witness -> downstream consumers for stale witnesses."""
    by_rel = corpus_scan["by_rel"]
    ts_refs: dict[str, list[str]] = var_audit["_ts_witness_refs"]

    reg_by_witness: dict[str, list[str]] = {}
    for e in reg_entries:
        reg_by_witness.setdefault(e["witnessFile"], []).append(e["name"])

    liq_by_witness: dict[str, list[str]] = {}
    for wf in var_audit["all_wired_manuscript_files"]:
        for tgt in wf["liquid_targets"]:
            if tgt.startswith("computations/"):
                wrel = f"{tgt}.witness.json"
                liq_by_witness.setdefault(wrel, []).append(wf["file"])

    dashboard_upstreams: dict[str, list[str]] = {
        "computations/m-p-substrate-identity-50dps.witness.json": [
            "computations/per_observable_100x_status.py"
        ],
        "computations/m-p-borromean-verification-50dps.witness.json": [
            "computations/per_observable_100x_status.py"
        ],
        "computations/cal-3-q-beta.witness.json": [
            "computations/per_observable_100x_status.py"
        ],
        "computations/alpha-em-schwinger-ladder.witness.json": [
            "computations/per_observable_100x_status.py (UNTRACKED in add_upstream!)"
        ],
        "computations/qbeta/qbeta-ck-cache.witness.json": [
            "computations/per_observable_100x_status.py (UNTRACKED in add_upstream!)"
        ],
        "computations/qbeta/qbeta-option-e-required-level.witness.json": [
            "computations/per_observable_100x_status.py (UNTRACKED in add_upstream!)"
        ],
        "computations/qbeta/qbeta-published-form-is-the-inadmissible-z1.witness.json": [
            "computations/per_observable_100x_status.py (UNTRACKED in add_upstream!)"
        ],
        "computations/codata-reconciliation.witness.json": [
            "computations/onepb_status_dashboard.py (UNTRACKED in add_upstream!)"
        ],
        "computations/cross-check-trM-1ppb.witness.json": [
            "computations/onepb_status_dashboard.py (UNTRACKED in add_upstream!)"
        ],
        "computations/demazure-markov-trace.witness.json": [
            "computations/onepb_status_dashboard.py (UNTRACKED in add_upstream!)"
        ],
        "computations/confinement-operator-selection.witness.json": [
            "computations/onepb_status_dashboard.py (UNTRACKED in add_upstream!)"
        ],
        "computations/rho-f-volume-binding-gap.witness.json": [
            "computations/onepb_status_dashboard.py (UNTRACKED in add_upstream!)"
        ],
    }

    critical_keys = sorted(
        set(reg_by_witness)
        | set(liq_by_witness)
        | set(dashboard_upstreams)
        | {
            "computations/per-observable-100x-status.witness.json",
            "computations/onepb-status-dashboard.witness.json",
            "computations/mass-binding-dashboard.witness.json",
            "computations/proton-mass-codata-50dps.witness.json",
            "computations/atomic-mass-via-rho-k.witness.json",
            "computations/binding-K-direct.witness.json",
            "computations/canonical-isotope-witness-Z00.witness.json",
            "computations/canonical-isotope-witness-Z01.witness.json",
            "computations/canonical-isotope-witness-Z02.witness.json",
        }
    )

    critical_traces: list[dict[str, Any]] = []
    for wrel in critical_keys:
        info = by_rel.get(wrel)
        if not info:
            continue
        consumers: list[str] = []
        if wrel in reg_by_witness:
            consumers.append(
                f"ValueRegistry({len(reg_by_witness[wrel])} keys: {', '.join(reg_by_witness[wrel][:4])})"
            )
        if wrel in liq_by_witness:
            consumers.append(
                f"Liquid({len(liq_by_witness[wrel])} .md files)"
            )
        if wrel in dashboard_upstreams:
            consumers.extend(dashboard_upstreams[wrel])
        if wrel in ts_refs:
            consumers.append(f"TSManifest({len(ts_refs[wrel])} block(s))")
        if wrel == "computations/onepb-status-dashboard.witness.json":
            consumers.append("docs/audits/onepb-status-dashboard.md")
        if wrel == "computations/mass-binding-dashboard.witness.json":
            consumers.append("computations/mass_binding_dashboard.py consumers")

        special_defect = ""
        if wrel == "computations/q-pinning-50-digit.witness.json":
            special_defect = (
                "Frozen pre-CODATA-2022 muon pin (1.10997859555733..., -0.077 ppb off live muon, "
                "+11.11 ppb off proton); read by derived_masses._q_0() causing silent proton/muon "
                "pin straddle inside m_p_substrate_identity_50dps.py, and substituted into 13 .md files!"
            )
        elif wrel == "computations/onepb-status-dashboard.witness.json":
            special_defect = (
                "Silently stale (2026-09-08, q0Anchor=muon): onepb_status_dashboard.py omits "
                "add_upstream(), hiding newer regenerations of cross-check-trM-1ppb (2026-10-13) "
                "and confinement-operator-selection (2026-11-15) plus 3 scriptHash-stale upstreams."
            )
        elif wrel == "computations/per-observable-100x-status.witness.json":
            special_defect = (
                "Omits 4 read witnesses from add_upstream() (alpha-em-schwinger-ladder, 3 qbeta "
                "witnesses), omits electroweak v/G_F row, uses finite-diff q_2t with inverted "
                "derivative sign note, and mixes Form-B cubic alpha_EM with CS alpha_EM."
            )
        elif wrel == "computations/mass-binding-dashboard.witness.json":
            special_defect = (
                "Producer mass_binding_dashboard.py is uncommitted-dirty in working tree; "
                "Tables 1-7 still use 1-term float64 proton_neutron_mass_mev(), truncated M=0 E_0, "
                "unnormalized W_lambda_float, and float64 pyhecke E_HARTREE_EV."
            )

        is_stale_any = (
            info["scriptHash_stale"]
            or info["upstream_sha256_stale"]
            or bool(special_defect)
        )
        if is_stale_any:
            critical_traces.append(
                {
                    "witness": wrel,
                    "producer": info["producer"],
                    "computedAt": info["computedAt"],
                    "q0Anchor": info["q0Anchor"],
                    "scriptHash_stale": info["scriptHash_stale"],
                    "upstream_sha256_stale": info["upstream_sha256_stale"],
                    "drifted_upstreams": info["drifted_upstreams"],
                    "downstream_consumers": consumers,
                    "defect_summary": special_defect
                    or (
                        "Producer scriptHash changed without witness regeneration"
                        if info["scriptHash_stale"]
                        else "Upstream witness sha256 changed without downstream regeneration"
                    ),
                }
            )

    ts_shash_stale = sorted(
        w for w in ts_refs if w in by_rel and by_rel[w]["scriptHash_stale"]
    )
    ts_upstream_stale = sorted(
        w for w in ts_refs if w in by_rel and by_rel[w]["upstream_sha256_stale"]
    )

    return {
        "corpus_summary": {
            "total_live_witnesses": corpus_scan["total_live_witnesses"],
            "scriptHash_stale_count": corpus_scan["scriptHash_stale_count"],
            "upstream_sha256_stale_count": corpus_scan["upstream_sha256_stale_count"],
            "missing_producer_script_count": corpus_scan["missing_producer_script_count"],
            "muon_anchored_count": corpus_scan["muon_anchored_count"],
            "ts_declared_witnesses_total": len(ts_refs),
            "ts_declared_scriptHash_stale_count": len(ts_shash_stale),
            "ts_declared_upstream_sha256_stale_count": len(ts_upstream_stale),
        },
        "critical_stale_witness_traces": critical_traces,
        "ts_declared_scriptHash_stale_witnesses": ts_shash_stale,
        "ts_declared_upstream_sha256_stale_witnesses": ts_upstream_stale,
    }


def scan_script_upgrade_surface() -> dict[str, Any]:
    """Scan live computations/**/*.py for wave-2 formula upgrade requirements."""
    live_pys = sorted(
        p
        for p in _COMP.rglob("*.py")
        if "_deprecated" not in p.parts
        and "fsh-guts" not in p.parts
        and "__pycache__" not in p.parts
        and p.name != Path(__file__).name
    )

    muon_137_scripts: list[str] = []
    codata2018_alpha_scripts: list[str] = []
    pyhecke_alpha_f64_scripts: list[str] = []
    bare_q9q10_without_derived_scripts: list[str] = []
    truncated_e0_scripts: list[str] = []
    untruncated_e0_scripts: list[str] = []
    unnorm_plancherel_scripts: list[str] = []
    norm_plancherel_scripts: list[str] = []
    unproj_alpha_d_scripts: list[str] = []
    proj_alpha_d_scripts: list[str] = []

    q9q10_re = re.compile(r"q_int[^\n]*9[^\n]*10|q_bal[^\n]*9[^\n]*10|\[9\].*\[10\]")
    e0_m0_re = re.compile(
        r"m_e\w*[^\n]*/\s*\(\s*q\w*\s*\*\s*\(\s*q\w*\s*-\s*(?:1|mpf\(1\)|mp\.mpf\(1\)|one)",
        re.I,
    )
    e0_tower_re = re.compile(
        r"1\s*-\s*hbar_q\w*\s*\*\*\s*2|one\s*-\s*hbar_q\w*\s*\*\*\s*2|2\s*\*\s*q\w*\s*-\s*(?:1|mpf\(1\))",
        re.I,
    )
    planch_re = re.compile(r"W_lambda|plancherel", re.I)
    planch_z_re = re.compile(
        r"frobenius_plancherel_Z_bounded_rows|Hankel4RowPlancherelEvaluator|Z_3A"
    )
    alpha_d_re = re.compile(r"alpha_D")
    alpha_d_proj_re = re.compile(r"alpha_D_proj|h\s*\*\*\s*2\s*\)\s*/\s*(?:4|mp\.mpf\(4\)|mpf\(4\))|h_q0\s*\*\*\s*2\s*/\s*4")

    for p in live_pys:
        rel = p.relative_to(_REPO).as_posix()
        txt = p.read_text(encoding="utf-8", errors="replace")

        if "137.035944" in txt or "137.035943" in txt:
            muon_137_scripts.append(rel)
        if "137.035999084" in txt:
            codata2018_alpha_scripts.append(rel)
        if (
            "pyhecke" in txt
            and any(
                sym in txt
                for sym in ("ALPHA_EM_INV_DERIVED", "alpha_em", "E_HARTREE_EV")
            )
        ) or ("hecke_core" in txt and "ALPHA_EM" in txt):
            pyhecke_alpha_f64_scripts.append(rel)
        if (
            q9q10_re.search(txt)
            and "alpha_em_inv_derived" not in txt
            and "schwinger" not in rel
        ):
            bare_q9q10_without_derived_scripts.append(rel)

        if e0_m0_re.search(txt):
            if e0_tower_re.search(txt):
                untruncated_e0_scripts.append(rel)
            else:
                truncated_e0_scripts.append(rel)

        if planch_re.search(txt):
            if planch_z_re.search(txt):
                norm_plancherel_scripts.append(rel)
            else:
                unnorm_plancherel_scripts.append(rel)

        if alpha_d_re.search(txt):
            if alpha_d_proj_re.search(txt):
                proj_alpha_d_scripts.append(rel)
            else:
                unproj_alpha_d_scripts.append(rel)

    prioritized_upgrade_queue: list[dict[str, Any]] = [
        {
            "priority": "P0-Library-Facade",
            "script": "computations/substrate/q_parameter.py",
            "pillars": ["Pillar-2-TwoTermQED"],
            "current_defect": "Exports only 1-term Q_50_DIGIT_STR; q_pinning_50_digit.py still emits frozen muon pin in q-pinning-50-digit.witness.json",
            "required_upgrade": "Re-export q_two_term_borromean_at / Q_TWO_TERM_50_DIGIT_STR alongside Q_50_DIGIT_STR; regenerate q-pinning-50-digit.witness.json with explicit proton & 2-term Borromean keys so Liquid consumers stop reading frozen muon q_0",
        },
        {
            "priority": "P0-Library-Facade",
            "script": "computations/canonical_mass.py",
            "pillars": ["Pillar-2-TwoTermQED", "Pillar-3-GPMT-E0Tower"],
            "current_defect": "proton_neutron_mass_mev() returns 1-term float64 tuple; proton_qed_self_energy_borromean_mev / np_qed_splitting_borromean_conn_mev / neutron_mass_two_term_mev do not accept explicit q=q_2t (they read 1-term m-p-substrate-identity-50dps.witness.json); lacks canonical E_0^tower helper",
            "required_upgrade": "Add explicit q= parameter defaulting to q_two_term_borromean_at(), add pure-mpf proton_neutron_mass_two_term_mev(q=None), export e0_hadronic_tower_mev(q), and wire mirror-projected alpha_D^proj + GPMT cumulant helpers",
        },
        {
            "priority": "P0-Library-Facade",
            "script": "computations/coulomb_energy.py",
            "pillars": ["Pillar-1-CorrectedPhoton", "Pillar-2-TwoTermQED"],
            "current_defect": "alpha_em_hbar_c_mev_fm / coulomb_energy_mev / mirror_displacement_mev hardcode 1-term Q_50_DIGIT_STR and CS _alpha_em_inv_derived without optional q=q_2t or Bring-Schwinger Form-B cubic",
            "required_upgrade": "Accept optional q= parameter (supporting q_two_term_borromean_at) and Form-B Bring-Schwinger cubic alpha_EM option",
        },
        {
            "priority": "P0-Library-Facade",
            "script": "computations/derived_masses.py",
            "pillars": ["Pillar-2-TwoTermQED", "Pillar-3-GPMT-E0Tower"],
            "current_defect": "_q_0() reads stale muon q-pinning-50-digit.witness.json (lines 90-105); lines 602, 685 use unprojected alpha_D and truncated E_0^(M=0)",
            "required_upgrade": "Switch _q_0() to proton/2-term pin from qou_substrate.constants, add q_2t + alpha_D^proj = alpha_D - h^2/4 + E_0^tower support",
        },
        {
            "priority": "P0-Library-Facade",
            "script": "computations/m_p_substrate_identity_50dps.py",
            "pillars": ["Pillar-2-TwoTermQED", "Pillar-3-GPMT-E0Tower"],
            "current_defect": "Silent proton/muon pin straddle: evaluates m_p at proton Q_50_DIGIT_STR then calls derived_masses.q_beta_kashiwara_n2_mev() which defaults to stale muon _q_0(); triggers sha256 drift in proton-mass-codata-50dps.witness.json",
            "required_upgrade": "Pass explicit proton/q_2t pin into Q_beta / m_n computation, record 2-term QED nucleon outputs, and regenerate proton-mass-codata-50dps.witness.json",
        },
        {
            "priority": "P0-Library-Facade",
            "script": "computations/substrate/hecke_core.py",
            "pillars": ["Pillar-1-CorrectedPhoton"],
            "current_defect": "Lines 87-97 re-export float64 pyhecke.constants.{ALPHA_EM_INV_DERIVED, alpha_em, E_HARTREE_EV}",
            "required_upgrade": "Replace float64 coupling/Hartree exports with mpmath-backed accessors from alpha_em_inv_derived / Bring-Schwinger cubic",
        },
        {
            "priority": "P1-Dashboard",
            "script": "computations/per_observable_100x_status.py",
            "pillars": [
                "Pillar-1-CorrectedPhoton",
                "Pillar-2-TwoTermQED",
                "Pillar-3-GPMT-E0Tower",
            ],
            "current_defect": "(1) Uses Form-B cubic on alpha_em_inv row (-0.3652 ppb) but CS-resummed alpha_em_inv_derived on m_K/m_pi row; (2) lines 1529-1532 use linear finite-difference q0_two_term_plain instead of q_two_term_borromean_at() and line 1549 states inverted sign d(m_p^QCD/m_e)/dq > 0; (3) omits v/G_F electroweak row; (4) omits 4 read witnesses in add_upstream()",
            "required_upgrade": "Use exact q_two_term_borromean_at(70), fix derivative sign note, unify Form-B Bring-Schwinger cubic alpha_EM, add v/G_F row + mirror-projected alpha_D^proj + GPMT Q_beta/m_n row, and register all upstream witnesses in add_upstream()",
        },
        {
            "priority": "P1-Dashboard",
            "script": "computations/onepb_status_dashboard.py",
            "pillars": [
                "Pillar-1-CorrectedPhoton",
                "Pillar-2-TwoTermQED",
                "Pillar-3-GPMT-E0Tower",
            ],
            "current_defect": "Never calls builder.add_upstream(); witness frozen at 2026-09-08 (q0Anchor=muon); writes hardcoded docs/audits/onepb-status-dashboard.md with stale 5-atom / 92.79 ppb figures",
            "required_upgrade": "Register all upstream witnesses via add_upstream(), regenerate stale upstreams (codata-reconciliation, demazure-markov-trace, rho-f-volume-binding-gap), switch to proton/q_2t pin, and regenerate witness + markdown report",
        },
        {
            "priority": "P1-Dashboard",
            "script": "computations/mass_binding_dashboard.py",
            "pillars": [
                "Pillar-1-CorrectedPhoton",
                "Pillar-2-TwoTermQED",
                "Pillar-3-GPMT-E0Tower",
            ],
            "current_defect": "Tables 1-7 use 1-term float64 proton_neutron_mass_mev(), float64 pyhecke E_HARTREE_EV (lines 85, 296), truncated M=0 E_0 = m_e/(q(q-1)) (line 331), and unnormalized W_lambda_float (lines 175, 654, 671)",
            "required_upgrade": "Promote 2-term QED nucleon + mirror/Coulomb shifts, q_2t pin, pure-mpf derived alpha_EM atomic electron binding, untruncated E_0^tower, GPMT dmod_(1^3)/(2,1^2)/(1^4), and Z_{3A}^{(4)}(q_0) normalization across all tables",
        },
        {
            "priority": "P1-Wave2-Core",
            "script": "computations/two_term_qed_isotope_and_nucleon_compute.py",
            "pillars": ["Pillar-2-TwoTermQED", "Pillar-3-GPMT-E0Tower"],
            "current_defect": "Line 240 structural_finding prose states inverted derivative sign ('d(m_p^QCD/m_e)/dq > 0 ... +0.233 ppb') contradicting computed witness (+8.058 ppb, shift -203.15 ppb); line 306 uses unprojected alpha_D; lines 415, 440 scale B_sym & GPMT by truncated E0_order0",
            "required_upgrade": "Fix line 240 derivative sign prose, add mirror-projected alpha_D^proj = alpha_D - h^2/4 branch, and evaluate B_sym / GPMT MeV shifts with untruncated E0_tower",
        },
        {
            "priority": "P1-Wave2-Core",
            "script": "computations/probes/electroweak_bring_schwinger_bridge_probe.py",
            "pillars": ["Pillar-1-CorrectedPhoton"],
            "current_defect": "Line 92 hardcodes CODATA alpha_inv_codata = mpf('137.035999177') inside schwinger_1loop_alpha_pi instead of derived alpha_EM",
            "required_upgrade": "Replace experimental alpha_inv_codata input with parameter-free Form-B Bring-Schwinger cubic / alpha_em_inv_derived(q0)",
        },
        {
            "priority": "P2-Table-Producer",
            "script": "computations/borromean_binding_recompute.py",
            "pillars": [
                "Pillar-1-CorrectedPhoton",
                "Pillar-2-TwoTermQED",
                "Pillar-3-GPMT-E0Tower",
            ],
            "current_defect": "Line 124 uses truncated M=0 E_0 = m_e/(q(q-1)); lacks 2-term QED nucleon/Coulomb/mirror terms and GPMT modified trace",
            "required_upgrade": "Wire E_0^tower, coulomb_energy_mev / mirror_displacement_mev, 2-term nucleon masses at q_2t, and GPMT (1^3) completion",
        },
        {
            "priority": "P2-Table-Producer",
            "script": "computations/atom_electron_mass.py",
            "pillars": [
                "Pillar-1-CorrectedPhoton",
                "Pillar-2-TwoTermQED",
                "Pillar-3-GPMT-E0Tower",
            ],
            "current_defect": "Line 76 uses truncated M=0 E_0; uses CS alpha_em_inv_mp rather than Form-B cubic and 1-term nuclear inputs",
            "required_upgrade": "Add Form-B Bring-Schwinger cubic option, E_0^tower, and 2-term QED nuclear mass integration",
        },
        {
            "priority": "P2-Table-Producer",
            "script": "computations/canonical_isotope_witness.py",
            "pillars": ["Pillar-2-TwoTermQED", "Pillar-3-GPMT-E0Tower"],
            "current_defect": "All 119 emitted canonical-isotope-witness-Z00..Z118.witness.json (.ts-wired) have stale upstream sha256 against m-p-substrate-identity-50dps and m-p-borromean-verification-50dps and use 1-term QED",
            "required_upgrade": "Wire 2-term QED nucleon + Coulomb + GPMT + Z_{3A}^{(4)} normalization and regenerate Z00..Z118 witnesses",
        },
        {
            "priority": "P2-Table-Producer",
            "script": "computations/canonical_mass_table_extended.py",
            "pillars": ["Pillar-2-TwoTermQED", "Pillar-3-GPMT-E0Tower"],
            "current_defect": "Uses 1-term proton_neutron_mass_mev() without two-term QED self-energy, Coulomb/mirror displacement, or GPMT/Plancherel Z_{3A}^{(4)}",
            "required_upgrade": "Upgrade to 2-term QED nucleon + coulomb_energy_mev + E_0^tower + normalized 4-row Plancherel",
        },
        {
            "priority": "P2-Table-Producer",
            "script": "computations/atlas_render_canonical_table.py",
            "pillars": ["Pillar-2-TwoTermQED", "Pillar-3-GPMT-E0Tower"],
            "current_defect": "Emits 4,782-line recursive-atom-knot-atlas-registry.md with CODATA-2018 m_p/m_n literals and 1-term QED masses",
            "required_upgrade": "Update to CODATA-2022 + 2-term QED + E_0^tower and regenerate appendix atlas",
        },
        {
            "priority": "P2-Table-Producer",
            "script": "computations/mass_table_ppb.py",
            "pillars": ["Pillar-2-TwoTermQED", "Pillar-3-GPMT-E0Tower"],
            "current_defect": "Uses 1-term nucleon masses and pre-GPMT binding pipeline",
            "required_upgrade": "Switch to 2-term QED nucleon + Coulomb + GPMT + E_0^tower",
        },
        {
            "priority": "P2-Table-Producer",
            "script": "computations/level1-qvalues.py",
            "pillars": ["Pillar-2-TwoTermQED", "Pillar-3-GPMT-E0Tower"],
            "current_defect": "Computes Q-values from 1-term masses without connected Borromean QED splitting, mirror_displacement_mev, or alpha_D^proj",
            "required_upgrade": "Incorporate 2-term QED nucleon/mirror splittings, alpha_D^proj, and E_0^tower",
        },
        {
            "priority": "P2-Table-Producer",
            "script": "computations/free-neutron-decay.py",
            "pillars": ["Pillar-2-TwoTermQED", "Pillar-3-GPMT-E0Tower"],
            "current_defect": "Uses pre-wave-2 1-term Q_beta without connected Borromean QED + mirror-projected alpha_D^proj",
            "required_upgrade": "Wire 2-term QED splitting + alpha_D^proj + E_0^tower at q_2t",
        },
        {
            "priority": "P3-Sector-Sweep",
            "script": "computations/b_over_a_evaluator.py",
            "pillars": ["Pillar-1-CorrectedPhoton", "Pillar-2-TwoTermQED", "Pillar-3-GPMT-E0Tower"],
            "current_defect": "Line 126 hardcodes float64 CODATA ALPHA_EM = 1.0 / 137.035999084; unnormalized Plancherel; truncated E_0",
            "required_upgrade": "Use derived pure-mpf alpha_EM, coulomb_energy_mev, Z_{3A}^{(4)}(q_0), and E_0^tower",
        },
        {
            "priority": "P3-Sector-Sweep",
            "script": "computations/probes/coulomb_mirror_killswitch_probe.py",
            "pillars": ["Pillar-1-CorrectedPhoton", "Pillar-2-TwoTermQED"],
            "current_defect": "Consumes hardcoded 1.43996 MeV*fm CODATA Coulomb constant instead of coulomb_energy.alpha_hbar_c_mev_fm(q)",
            "required_upgrade": "Import derived pure-mpf alpha_hbar_c_mev_fm / mirror_displacement_mev from coulomb_energy.py",
        },
        {
            "priority": "P3-Sector-Sweep",
            "script": "computations/deltalambda/wlambda_binding_a3_mirror_selection.py",
            "pillars": ["Pillar-1-CorrectedPhoton", "Pillar-2-TwoTermQED", "Pillar-3-GPMT-E0Tower"],
            "current_defect": "Uses hardcoded 1.43996 Coulomb literal and pre-GPMT A=3 mirror evaluation",
            "required_upgrade": "Switch to coulomb_energy.mirror_displacement_mev, gpmt_dmod_111, and E_0^tower",
        },
    ]

    return {
        "corpus_pattern_counts": {
            "live_python_scripts_scanned": len(live_pys),
            "pillar1_muon_137_035944_scripts_count": len(muon_137_scripts),
            "pillar1_codata2018_137_035999084_scripts_count": len(
                codata2018_alpha_scripts
            ),
            "pillar1_pyhecke_hecke_core_f64_alpha_scripts_count": len(
                pyhecke_alpha_f64_scripts
            ),
            "pillar1_bare_q9q10_without_derived_helper_count": len(
                bare_q9q10_without_derived_scripts
            ),
            "pillar3_truncated_M0_E0_scripts_count": len(truncated_e0_scripts),
            "pillar3_untruncated_tower_E0_scripts_count": len(
                untruncated_e0_scripts
            ),
            "pillar3_unnormalized_plancherel_scripts_count": len(
                unnorm_plancherel_scripts
            ),
            "pillar3_normalized_4row_plancherel_scripts_count": len(
                norm_plancherel_scripts
            ),
            "pillar3_unprojected_alpha_D_scripts_count": len(
                unproj_alpha_d_scripts
            ),
            "pillar3_mirror_projected_alpha_D_scripts_count": len(
                proj_alpha_d_scripts
            ),
        },
        "flagged_script_lists": {
            "pillar1_muon_137_035944_scripts": muon_137_scripts,
            "pillar1_codata2018_137_035999084_scripts": codata2018_alpha_scripts,
            "pillar1_pyhecke_hecke_core_f64_alpha_scripts": pyhecke_alpha_f64_scripts,
            "pillar1_bare_q9q10_without_derived_helper": bare_q9q10_without_derived_scripts,
            "pillar3_unnormalized_plancherel_scripts": unnorm_plancherel_scripts,
            "pillar3_unprojected_alpha_D_scripts": unproj_alpha_d_scripts,
            "pillar3_truncated_M0_E0_scripts_sample": truncated_e0_scripts[:40],
            "pillar3_truncated_M0_E0_scripts_total": len(truncated_e0_scripts),
        },
        "algebraic_guardrail_notes": {
            "E0_tower_exact_simplification": (
                "With hbar_q = (q - 1)/q, E_0^tower = E_0^(M=0) / (1 - hbar_q^2) "
                "= [m_e / (q(q - 1))] / [(2q - 1)/q^2] = m_e * q / ((q - 1)(2q - 1)) "
                "approx 4.227483 MeV (+0.9915% over M=0 4.185981 MeV). Note: do NOT "
                "confuse (1 - hbar_q^2) with (q^2 - 1), which would give m_e / ((q-1)^2(q+1)) "
                "approx 42.2 MeV (10x error)."
            ),
            "two_term_pin_derivative_sign": (
                "d ln(m_p^QCD/m_e) / d ln q approx -20.997 < 0 at q_0, so subtracting "
                "positive M_p^QED > 0 lowers target M_p^QCD and INCREASES q_2t above "
                "1-term q_proton by +11.17 ppb (closing 96.2% of the 211.2 ppb mu-p gap)."
            ),
        },
        "prioritized_upgrade_queue": prioritized_upgrade_queue,
    }


def run_audit(write_witness: bool = True) -> tuple[dict[str, Any], Path | None]:
    ref50 = compute_wave2_reference_values()
    raw_mpf = ref50.pop("_raw_mpf")

    reg_entries = parse_value_registry()
    corpus_scan = scan_witness_corpus()
    var_audit = audit_variable_substitution(reg_entries, corpus_scan["by_rel"])
    stale_trace = build_critical_stale_witness_trace(
        corpus_scan, var_audit, reg_entries
    )
    var_audit.pop("_ts_witness_refs", None)
    upgrade_matrix = scan_script_upgrade_surface()

    wb = WitnessBuilder(SELF_WITNESS_NAME, engine="mpmath")
    wb.set_description(
        "End-to-end audit and dependency trace of (1) ValueRegistry :val[...] and "
        "Liquid {{ qou... }} variable substitution vs hardcoded prose/tables across "
        "status docs, 23 main paper chapters, and 10 appendices; (2) stale witnesses "
        "(producer scriptHash drift, upstream sha256 drift, unrecorded dashboard "
        "upstreams, and muon/proton pin straddles); and (3) the Wave-2 script upgrade "
        "matrix for Corrected Photon alpha_EM, Two-Term QED + q_2t pin, and GPMT + "
        "mirror-projected alpha_D^proj + normalized 4-row q-Plancherel + E_0^tower."
    )
    wb.set_audit_only(
        "docs/audits/2026-11-18-two-term-qed-downstream-and-211ppb-audit.md"
    )

    wb.add_parameter("compute_dps_floor", 50)
    wb.add_parameter("serialization_dps", 50)
    wb.add_parameter("main_chapters_count", len(MAIN_CHAPTERS))
    wb.add_parameter("appendices_count", len(APPENDICES))
    wb.add_parameter("status_docs_count", len(STATUS_DOC_PATHS))

    wb.add_data("wave2_reference_values_50dps", ref50)
    wb.add_data("variable_substitution_audit", var_audit)
    wb.add_data("witness_staleness_audit", stale_trace)
    wb.add_data("script_upgrade_matrix", upgrade_matrix)

    # Non-tautological assertions verifying real corpus & algebraic invariants
    wb.add_assertion(
        name="witness_corpus_scan_nonempty",
        computed=1 if corpus_scan["total_live_witnesses"] > 3000 else 0,
        expected=1,
        source="Live witness corpus under computations/ must exceed 3,000 files",
    )
    wb.add_assertion(
        name="upstream_witness_sha256_drift_detected",
        computed=1 if corpus_scan["upstream_sha256_stale_count"] > 0 else 0,
        expected=1,
        source="Must resolve data.upstream_witness_hashes['path'] and catch real upstream sha256 drift",
    )
    wb.add_assertion(
        name="value_registry_parsed_and_rho_q_defect_detected",
        computed=1
        if (
            len(reg_entries) >= 68
            and any(
                b["name"] == "rho_q"
                for b in var_audit["value_registry_health"]["broken_entries"]
            )
        )
        else 0,
        expected=1,
        source="folio/values/registry.ts has >=68 entries and broken rho_q path is caught",
    )
    wb.add_assertion(
        name="manuscript_md_scan_complete",
        computed=1
        if var_audit["coverage_by_section"]["manuscript_total_md_files"] > 3600
        else 0,
        expected=1,
        source="All 23 main chapters + 10 appendices + 3 backmatter chapters scanned",
    )
    with mp.workdps(70):
        rel_cubic_err = abs(
            raw_mpf["alpha_inv_cubic"] - raw_mpf["alpha_inv_codata2022"]
        ) / raw_mpf["alpha_inv_codata2022"]
        wb.add_assertion(
            name="bring_schwinger_cubic_closes_alpha_em_sub_ppb",
            computed=fmt(rel_cubic_err, dps=50),
            expected="0",
            tolerance="1e-9",
            source="1-loop Bring-Schwinger cubic closes 1/alpha_EM within 1 ppb of CODATA 2022 (-0.3652 ppb)",
        )
        wb.add_assertion(
            name="two_term_borromean_pin_increases_q0_over_1term",
            computed=1 if raw_mpf["q_2t"] > raw_mpf["q_p1"] else 0,
            expected=1,
            source="Since d(m_p^QCD/m_e)/dq < 0, subtracting M_p^QED > 0 increases q_2t above q_proton_1term",
        )
        wb.add_assertion(
            name="E0_tower_matches_closed_form_me_q_over_qm1_2qm1",
            computed=fmt(raw_mpf["e0_tower"], dps=50),
            expected=fmt(raw_mpf["e0_closed"], dps=50),
            tolerance="1e-48",
            source="E_0^(0) / (1 - hbar_q^2) == m_e * q / ((q - 1)(2q - 1))",
        )

    saved_path: Path | None = None
    if write_witness:
        stamp = q0_comparison(
            muon=raw_mpf["q_mu"],
            proton=raw_mpf["q_p1"],
            reason=(
                "Audit cross-compares 1-term proton, 2-term Borromean proton, "
                "live CODATA-2022 muon, and frozen pre-CODATA-2022 muon pins across "
                "witnesses, ValueRegistry, Liquid bindings, and manuscript prose."
            ),
        )
        saved_path = wb.save(stamp)
        saved_doc = json.loads(saved_path.read_text(encoding="utf-8"))
        import witness_raw_float64_audit as _f64_audit

        raw_floats = _f64_audit.count_raw_floats(saved_doc)
        if raw_floats != 0:
            raise RuntimeError(
                f"NO-FLOAT64 violation: emitted witness has {raw_floats} raw float64 field(s)!"
            )
        return saved_doc, saved_path

    return wb.build(), None


def _self_test() -> int:
    doc, path = run_audit(write_witness=False)
    import witness_raw_float64_audit as _f64_audit

    n_f64 = _f64_audit.count_raw_floats(doc)
    assert n_f64 == 0, f"Expected 0 raw float64 fields, got {n_f64}"
    assert doc["allPassed"] is True, "All audit assertions must pass"
    assert path is None
    print("SELF-TEST PASSED: 0 raw float64 fields, all assertions passed.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--self-test",
        action="store_true",
        help="Run in-memory audit + raw-float64 self-check without writing witness.",
    )
    args = ap.parse_args()
    if args.self_test:
        return _self_test()

    doc, saved_path = run_audit(write_witness=True)
    cov = doc["data"]["variable_substitution_audit"]["coverage_by_section"]
    stale = doc["data"]["witness_staleness_audit"]["corpus_summary"]
    upg = doc["data"]["script_upgrade_matrix"]["corpus_pattern_counts"]

    print("=" * 78)
    print("PAPER / STATUS VARIABLE-SUBSTITUTION & WITNESS STALENESS AUDIT")
    print("=" * 78)
    print(
        f"  Manuscript .md wired       : {cov['manuscript_total_wired_md_files']} / "
        f"{cov['manuscript_total_md_files']} files "
        f"(tables wired: {cov['manuscript_wired_table_data_files']} / "
        f"{cov['manuscript_total_table_data_files']})"
    )
    print(
        f"  Status docs wired          : "
        f"{cov['status_scorecard_docs']['total_wired_files']} / "
        f"{cov['status_scorecard_docs']['md_files']}"
    )
    print(
        f"  Live witnesses scanned     : {stale['total_live_witnesses']} "
        f"(scriptHash stale: {stale['scriptHash_stale_count']}, "
        f"upstream sha256 stale: {stale['upstream_sha256_stale_count']}, "
        f"muon-anchored: {stale['muon_anchored_count']})"
    )
    print(
        f"  Live .py scripts scanned   : {upg['live_python_scripts_scanned']} "
        f"(truncated M=0 E_0: {upg['pillar3_truncated_M0_E0_scripts_count']}, "
        f"unnorm Plancherel: {upg['pillar3_unnormalized_plancherel_scripts_count']}, "
        f"unproj alpha_D: {upg['pillar3_unprojected_alpha_D_scripts_count']})"
    )
    print(f"  All assertions passed      : {doc['allPassed']}")
    print(f"  Emitted witness            : {saved_path}")
    return 0 if doc["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
