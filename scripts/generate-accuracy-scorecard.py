#!/usr/bin/env python3
"""Generate, redisplay, HTML-render, and QA-gate QOU's ACCURACY.md scorecard.

All numeric computations run at 80 decimal places (`mp.dps = 80`) with zero
binary64 (`float`) conversions. `ACCURACY.md` is rendered deterministically from
`scripts/templates/accuracy-scorecard.md.tmpl` and 12 repository witnesses /
reference datasets, omitting transient git `HEAD` SHAs and wall-clock timestamps
so `--check` remains commit-stable unless an upstream witness moves.

Usage:
    python3 scripts/generate-accuracy-scorecard.py --write
    python3 scripts/generate-accuracy-scorecard.py --print
    python3 scripts/generate-accuracy-scorecard.py --check [--qa-report] [--html-out _site/accuracy/index.html]
    python3 scripts/generate-accuracy-scorecard.py --self-test

`--write` also emits the authors'-note content block
`folio/quantum-observable-universe/authors-note/accuracy-dashboard.{md,ts}` from
`scripts/templates/accuracy-dashboard.md.tmpl`, built from the same computed
values; `--check` fails when that block drifts.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import html
import json
import re
import shutil
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

from mpmath import mp, mpf, nint

mp.dps = 80

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_REL = "scripts/templates/accuracy-scorecard.md.tmpl"
ACCURACY_REL = "ACCURACY.md"
README_REL = "README.md"
QA_OUT_REL = "test/results/compute-qa/accuracy-scorecard.json"
DASHBOARD_TEMPLATE_REL = "scripts/templates/accuracy-dashboard.md.tmpl"
DASHBOARD_MD_REL = "folio/quantum-observable-universe/authors-note/accuracy-dashboard.md"
DASHBOARD_TS_REL = "folio/quantum-observable-universe/authors-note/accuracy-dashboard.ts"

TEN_3 = mpf("1e3")
TEN_6 = mpf("1e6")
TEN_9 = mpf("1e9")
TEN_15 = mpf("1e15")
HUNDRED = mpf("100")

UPSTREAM_SPECS: list[tuple[str, str]] = [
    ("computations/master-atlas-80dps.witness.json", "§1, §2, §3.1, §3.3, §3.4"),
    ("computations/per-observable-100x-status.witness.json", "§2, §3.1a, §3.2a (tower E_0), §3.4a"),
    ("computations/alpha-em-schwinger-ladder.witness.json", "§1, §2, §3.3a, §5.1"),
    ("computations/alpha/alpha_em_two_loop_bloch_schwinger_probe.witness.json", "§1, §2, §3.3a, §5.1"),
    ("computations/alpha/alpha-em-seifert-kappa-pairing.witness.json", "§3.3a, §5.1"),
    ("computations/atom-electron-mass.witness.json", "§3.3a"),
    ("computations/probes/electroweak-bring-schwinger-bridge.witness.json", "§2, §3.4a, §5.1"),
    ("computations/mass-table-comprehensive.witness.json", "§2, §3.1b–c, §3.2b, §3.4b, §3.5b, §4"),
    ("computations/data/ame2020.json", "§2, §3.1b–c, §3.2a–b, §3.4b, §3.5b"),
    ("computations/probes/gap1b_4he_tetrahedral_k4_flux_ring/gap1b-4he-tetrahedral-k4-flux-ring.witness.json", "§2, §3.2a, §3.5b"),
    ("computations/probes/gap2b_mtau_s3_circulant_koide_test/gap2b-mtau-s3-circulant-koide-probe.witness.json", "§2, §3.1a"),
    ("computations/probes/gap3b_t29_composite_decay_threshold/gap3b-t29-composite-decay-threshold.witness.json", "§2, §3.5a"),
    ("computations/u1-hypercharge-assignment.witness.json", "§2, §3.3a"),
    ("computations/charge-coulomb-tn3he-derived.witness.json", "§2, §3.3a"),
    ("computations/mirror-nuclei-coulomb-systematics.witness.json", "§2, §3.3a"),
    ("computations/beta-decay-from-q.witness.json", "§2, §3.4a, §5.1"),
    ("computations/probes/alpha_decay_n126_and_derived_qalpha/alpha_decay_n126_qalpha_probe.witness.json", "§2, §3.5a–b"),
    ("computations/probes/gg_deuteron_bond/gg-deuteron-bond.witness.json", "§3.2a (ruled trace-pipeline row)"),
    ("computations/scorecard-epistemic-status.witness.json", "§2, §3.1a, §3.2a, §3.3a, §3.4a (row labels)"),
]

FORBIDDEN_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("internal-convention-label", re.compile(r"(?i)\bconvention\s+[abcd]\b")),
    ("internal-markov-symbol", re.compile(r"\bz_[cCdD]\b")),
    ("internal-cal-tag", re.compile(r"(?i)\bcal-[1234]\b")),
    ("internal-bean-id", re.compile(r"(?i)\bqou-[a-z0-9]{4}\b")),
]


def _m(val: Any) -> mpf:
    """Convert a JSON string or integer/decimal token to 80-dps mpf via str."""
    return mpf(str(val))


def _median(xs: list[mpf]) -> mpf:
    if not xs:
        return mpf(0)
    s = sorted(xs)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / mpf(2)


def _mean(xs: list[mpf]) -> mpf:
    if not xs:
        return mpf(0)
    return sum(xs, mpf(0)) / mpf(len(xs))


def _fmt_fixed(val: mpf, places: int, signed: bool = False) -> str:
    scale = mpf(10) ** places
    rounded_int = int(nint(val * scale))
    neg = rounded_int < 0
    aval = abs(rounded_int)
    digits = str(aval).zfill(places + 1)
    if places == 0:
        body = digits
    else:
        body = f"{digits[:-places]}.{digits[-places:]}"
    if neg:
        return f"-{body}"
    if signed and rounded_int > 0:
        return f"+{body}"
    return body


def _fmt_sci(val: mpf, sig: int = 3, signed: bool = False) -> str:
    if val == 0:
        return "0"
    aval = abs(val)
    sign = "-" if val < 0 else ("+" if signed else "")
    if mpf("1e-2") <= aval < mpf("1e4"):
        return f"{sign}{mp.nstr(aval, sig)}"
    exp_i = int(mp.floor(mp.log10(aval)))
    mant = aval / (mpf(10) ** exp_i)
    if abs(mant) >= mpf("9.9995"):
        mant /= mpf(10)
        exp_i += 1
    return f"{sign}{_fmt_fixed(mant, max(sig - 1, 1))}e{exp_i:+d}"


def _fmt_ppq(rel_frac: mpf) -> str:
    ppq = abs(rel_frac) * TEN_15
    if ppq == 0:
        return "0"
    if ppq < TEN_6:
        return _fmt_fixed(ppq, 1)
    return _fmt_sci(ppq, 3)


def _fmt_rel_human(rel_frac: mpf, signed: bool = True) -> str:
    aval = abs(rel_frac)
    if aval == 0:
        return "0"
    if aval < mpf("1e-6"):
        return f"{_fmt_fixed(rel_frac * TEN_9, 3, signed=signed)} ppb"
    if aval < mpf("1e-3"):
        return f"{_fmt_fixed(rel_frac * TEN_6, 2, signed=signed)} ppm"
    return f"{_fmt_fixed(rel_frac * HUNDRED, 2, signed=signed)}%"


def _sha12_and_json(path: Path) -> tuple[str, dict[str, Any]]:
    raw_bytes = path.read_bytes()
    sha12 = hashlib.sha256(raw_bytes).hexdigest()[:12]
    data = json.loads(raw_bytes.decode("utf-8"))
    return sha12, data


def _strip_folio_generated_blocks(readme_text: str) -> str:
    return re.sub(
        r"<!--\s*folio:[a-z0-9_-]+:begin\s*-->.*?<!--\s*folio:[a-z0-9_-]+:end\s*-->",
        "",
        readme_text,
        flags=re.DOTALL | re.IGNORECASE,
    )


def load_and_validate_upstream(root: Path) -> tuple[dict[str, dict[str, Any]], dict[str, str], list[str]]:
    loaded: dict[str, dict[str, Any]] = {}
    hashes: dict[str, str] = {}
    errors: list[str] = []
    for rel, _sections in UPSTREAM_SPECS:
        p = root / rel
        if not p.is_file():
            errors.append(f"missing upstream file: {rel}")
            continue
        try:
            sha12, obj = _sha12_and_json(p)
        except Exception as exc:
            errors.append(f"invalid JSON in {rel}: {exc}")
            continue
        hashes[rel] = sha12
        loaded[rel] = obj
        if "allPassed" in obj and obj["allPassed"] is not True:
            errors.append(f"witness gate failed (`allPassed != True`): {rel}")
    return loaded, hashes, errors


def check_consumed_witness_staleness(root: Path) -> tuple[list[str], list[str]]:
    """Every consumed witness must still describe its producer.

    `allPassed` and byte-identity say nothing about whether the numbers on the
    scorecard would come out the same if the producers ran today. Two
    directions are checked, for every witness in UPSTREAM_SPECS that names a
    producer:

      SELF  the producer file changed since the witness (`scriptHash`);
      CONE  a first-party module in the producer's transitive import cone was
            committed after the witness's `computedAt`
            (`witness_import_cone_staleness_audit.py`; provenance-only modules
            such as witness.py are ignored, as there).

    SELF is an error. CONE is returned as a warning, printed by --check but
    not failing it: it is a commit-time heuristic, and a comment-only commit
    to a cone module trips it. Worse, WitnessBuilder keeps the on-disk stamp
    when a re-run reproduces the payload, so a re-run that proves nothing
    moved cannot clear it (measured 2026-11-27: atom-electron-mass and
    alpha_decay_n126_qalpha_probe re-ran byte-identical and stay flagged).
    Re-run the flagged producer and diff the payload; a move is the finding.
    Modules whose age a shallow clone cannot tell are skipped, so a shallow run
    is a lower bound. Bean qou-myts (B3).

    Returns (errors, warnings).
    """
    if root.resolve() != REPO_ROOT.resolve():
        return [], []  # self-test fixtures carry no git history
    comp = REPO_ROOT / "computations"
    if str(comp) not in sys.path:
        sys.path.insert(0, str(comp))
    try:
        import witness_import_cone_staleness_audit as cone_audit
        from witness_dependency_drift import check_self_staleness
    except Exception as exc:  # noqa: BLE001 — report, never pass silently
        return [f"witness staleness check could not load: {exc}"], []
    index = cone_audit._build_producer_index([comp, REPO_ROOT / "tools"])
    errors: list[str] = []
    warnings: list[str] = []
    for rel, _sections in UPSTREAM_SPECS:
        wp = root / rel
        try:
            w = json.loads(wp.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001 — load_and_validate_upstream reports it
            continue
        script_file = w.get("scriptFile") or (
            Path(str(w["producer"])).name if w.get("producer") else None)
        if not script_file:
            continue  # reference data (e.g. ame2020.json), no producer
        cands = index.get(script_file, [])
        if not cands:
            errors.append(f"producer `{script_file}` of {rel} not found")
            continue
        producer = cone_audit._resolve_producer(cands, wp)
        if check_self_staleness(wp, index) is not None:
            errors.append(f"witness SELF-stale (producer changed since it ran): {rel}")
            continue
        try:
            when = datetime.fromisoformat(str(w.get("computedAt")))
        except ValueError:
            errors.append(f"witness has no usable computedAt: {rel}")
            continue
        if when.tzinfo is None:
            when = when.replace(tzinfo=timezone.utc)
        movers = []
        for mod in cone_audit.import_cone(producer, index):
            rel_mod = cone_audit._rel(mod)
            if cone_audit._is_provenance_only(rel_mod):
                continue
            ct = cone_audit._git_commit_time(mod)
            if ct and ct > when:
                movers.append((ct, rel_mod))
        if movers:
            movers.sort(reverse=True)
            newest = ", ".join(f"{m} ({t.date()})" for t, m in movers[:3])
            warnings.append(
                f"witness IMPORT-CONE stale ({len(movers)} module(s) in its "
                f"producer's cone committed after {when.date()}; newest: {newest}); "
                f"re-run `{_rel_to_repo(producer)}` and diff the payload: {rel}")
    return errors, warnings


def _rel_to_repo(p: Path) -> str:
    try:
        return str(p.resolve().relative_to(REPO_ROOT.resolve()))
    except ValueError:
        return str(p)


def render_scorecard(root: Path) -> tuple[str, list[str]]:
    """Render ACCURACY.md only (kept for callers that need the scorecard alone)."""
    scorecard, _dashboard, errors = render_all(root)
    return scorecard, errors


def render_all(root: Path) -> tuple[str, str, list[str]]:
    """Render ACCURACY.md and the authors'-note accuracy-dashboard block.

    Both come from one pass over the same witnesses, so the dashboard can never
    quote a number the scorecard does not.
    """
    loaded, hashes, errors = load_and_validate_upstream(root)
    tmpl_path = root / TEMPLATE_REL
    if not tmpl_path.is_file():
        errors.append(f"missing scorecard template: {TEMPLATE_REL}")
    dash_tmpl_path = root / DASHBOARD_TEMPLATE_REL
    if not dash_tmpl_path.is_file():
        errors.append(f"missing dashboard template: {DASHBOARD_TEMPLATE_REL}")
    if errors:
        return "", "", errors

    tmpl = tmpl_path.read_text(encoding="utf-8")
    dash_tmpl = dash_tmpl_path.read_text(encoding="utf-8")

    ma = loaded["computations/master-atlas-80dps.witness.json"]["data"]
    po = loaded["computations/per-observable-100x-status.witness.json"]["data"]
    mt = loaded["computations/mass-table-comprehensive.witness.json"]["data"]
    ame = loaded["computations/data/ame2020.json"]["entries"]
    g1 = loaded["computations/probes/gap1b_4he_tetrahedral_k4_flux_ring/gap1b-4he-tetrahedral-k4-flux-ring.witness.json"]["data"]
    g2 = loaded["computations/probes/gap2b_mtau_s3_circulant_koide_test/gap2b-mtau-s3-circulant-koide-probe.witness.json"]["data"]
    u1 = loaded["computations/u1-hypercharge-assignment.witness.json"]["data"]
    cc = loaded["computations/charge-coulomb-tn3he-derived.witness.json"]["data"]
    mn = loaded["computations/mirror-nuclei-coulomb-systematics.witness.json"]["data"]
    bd_top = loaded["computations/beta-decay-from-q.witness.json"]
    bd = bd_top.get("data", bd_top)
    ad = loaded["computations/probes/alpha_decay_n126_and_derived_qalpha/alpha_decay_n126_qalpha_probe.witness.json"]["data"]

    # Per-row epistemic labels come from their own witness, never from this file
    # (owner dispatch 2026-11-27). A row without a label is a render error.
    es_rows = loaded["computations/scorecard-epistemic-status.witness.json"]["data"]["rows"]
    gg_bond = loaded["computations/probes/gg_deuteron_bond/gg-deuteron-bond.witness.json"]["data"]

    def _status(rid: str) -> str:
        if rid not in es_rows:
            errors.append(f"no epistemic-status label for row `{rid}`")
            return "Unclassified"
        return es_rows[rid]["status"]

    def _st(rid: str) -> str:
        return f"**{_status(rid)}**"

    anc = ma["anchors"]
    obs = ma["observables"]
    po_by_obs = {r["obs"]: r for r in po["rows"]}

    # ── Section 1: Calibration baseline & precision floors ────────────────────
    m_e = _m(anc["m_e_MeV"])
    m_e_sig = _m(anc["m_e_sigma_MeV"])
    me_ppb = (m_e_sig / m_e) * TEN_9
    me_ppq = (m_e_sig / m_e) * TEN_15

    r_pe = _m(anc["mass_ratio_p_e"])
    r_pe_sig = _m(anc["mass_ratio_p_e_sigma"])
    rpe_ppb = (r_pe_sig / r_pe) * TEN_9
    rpe_ppq = (r_pe_sig / r_pe) * TEN_15

    q0 = _m(anc["q0_proton_80dps"])
    q0_sig = _m(anc["q0_proton_sigma"])
    q0_ppb = _m(anc["q0_proton_rel_ppb"])
    q0_ppq = (q0_sig / q0) * TEN_15

    m_pi = _m(anc["m_pi_pm_MeV"])
    m_pi_sig = _m(anc["m_pi_pm_sigma_MeV"])
    mpi_ppb = (m_pi_sig / m_pi) * TEN_9
    mpi_ppq = (m_pi_sig / m_pi) * TEN_15

    z_markov = _m(anc["markov_z_proton_80dps"])
    hbar_q = _m(anc["hbar_q_proton_80dps"])
    ha_q = _m(anc["ha_proton_80dps"])
    # Propagate sigma(q0) to z(q) = q^3/(q^2+1), hbar_q = 1 - 1/q, h_A = q - 1/q
    dz_dq = (q0 ** 2 * (q0 ** 2 + mpf(3))) / ((q0 ** 2 + mpf(1)) ** 2)
    z_sig = abs(dz_dq) * q0_sig
    dhbar_dq = mpf(1) / (q0 ** 2)
    hbar_sig = dhbar_dq * q0_sig
    dha_dq = mpf(1) + mpf(1) / (q0 ** 2)
    ha_sig = dha_dq * q0_sig

    calib_rows = [
        f"| Electron mass | $m_e$ | `{_fmt_fixed(m_e, 11)} MeV` | `{_fmt_sci(m_e_sig, 3)} MeV` | `{_fmt_fixed(me_ppb, 4)}` | `{_fmt_sci(me_ppq, 4)}` | Calibration input 1 (overall MeV unit) |",
        f"| Proton/electron ratio | $m_p / m_e$ | `{_fmt_fixed(r_pe, 9)}` | `{_fmt_sci(r_pe_sig, 3)}` | `{_fmt_fixed(rpe_ppb, 5)}` | `{_fmt_sci(rpe_ppq, 4)}` | Calibration input 2 (dimensionless baryon ratio) |",
        f"| Charged-pion mass | $m_{{\\pi^\\pm}}$ | `{_fmt_fixed(m_pi, 5)} MeV` | `{_fmt_fixed(m_pi_sig, 5)} MeV` | `{_fmt_fixed(mpi_ppb, 1)}` | `{_fmt_sci(mpi_ppq, 4)}` | Calibration input 3 (meson-sector scale) |",
        f"| Deformation parameter | $q_0$ | `{_fmt_fixed(q0, 18)}` | `{_fmt_sci(q0_sig, 4)}` | `{_fmt_fixed(q0_ppb, 6)}` | `{_fmt_fixed(q0_ppq, 1)}` | Solved from $m_p / m_e$ (tightest framework anchor) |",
        f"| Canonical Markov weight | $z = q_0^3/(q_0^2+1)$ | `{_fmt_fixed(z_markov, 18)}` | `{_fmt_sci(z_sig, 4)}` | `{_fmt_fixed((z_sig / z_markov) * TEN_9, 6)}` | `{_fmt_fixed((z_sig / z_markov) * TEN_15, 1)}` | Derived Hecke–Markov trace parameter |",
        f"| Quantum Planck & Hecke step | $\\hbar_q,\\; h_A$ | `{_fmt_fixed(hbar_q, 12)}, {_fmt_fixed(ha_q, 12)}` | `{_fmt_sci(hbar_sig, 3)}, {_fmt_sci(ha_sig, 3)}` | `{_fmt_fixed((hbar_sig / hbar_q) * TEN_9, 4)}` | `{_fmt_fixed((hbar_sig / hbar_q) * TEN_15, 1)}` | $\\hbar_q = 1 - q_0^{{-1}},\\; h_A = q_0 - q_0^{{-1}}$ |",
    ]

    nuc_sig_ppbs = [_m(n["sigma_pred_constituent_ppb"]) for n in ma["nuclide_summary"]]
    nuc_sig_min = min(nuc_sig_ppbs)
    nuc_sig_max = max(nuc_sig_ppbs)

    alpha_fb = obs["alpha_em_inv_form_b"]
    alpha_fc = obs["alpha_em_inv_form_c_bloch_b3"]
    alpha_seif = obs["alpha_em_inv_cs_seifert"]
    alpha_cs = obs["alpha_em_inv_cs"]
    ry_fb = obs["rydberg_form_b_eV"]
    ry_fc = obs["rydberg_form_c_eV"]
    vew_obs = obs["v_ew_GeV"]
    nvew_obs = obs["N_v_ew"]
    alpha_exp = _m(alpha_fb["exp"])
    alpha_exp_sig = _m(alpha_fb["sigma_exp"])
    alpha_exp_ppb = (alpha_exp_sig / alpha_exp) * TEN_9
    alpha_exp_ppq = (alpha_exp_sig / alpha_exp) * TEN_15
    alpha_fb_ppb = _m(alpha_fb["rel_ppb"])
    alpha_fb_ppq = abs(alpha_fb_ppb) * TEN_6
    alpha_fb_pull = _m(alpha_fb["pull_exp"])
    alpha_fc_ppb = _m(alpha_fc["rel_ppb"])
    alpha_fc_ppq = abs(alpha_fc_ppb) * TEN_6
    alpha_fc_pull = _m(alpha_fc["pull_exp"])
    alpha_seif_ppb = _m(alpha_seif["rel_ppb"])
    alpha_seif_pull = _m(alpha_seif["pull_exp"])
    ry_fb_ppb = _m(ry_fb["rel_ppb"])
    ry_fb_zcomb = _m(ry_fb["z_comb"])
    ry_fc_ppb = _m(ry_fc["rel_ppb"])
    ry_fc_zcomb = _m(ry_fc["z_comb"])
    vew_pred = _m(vew_obs["pred"])
    vew_exp = _m(vew_obs["exp"])
    vew_sig_exp = _m(vew_obs["sigma_exp"])
    vew_ppb = _m(vew_obs["rel_ppb"])
    vew_pull = _m(vew_obs["pull_exp"])
    nv_pred = _m(nvew_obs["pred"])

    # ── Join mass-table-comprehensive with AME2020 ────────────────────────────
    mt_by_zn = {(int(r["Z"]), int(r["N"])): r for r in mt["rows"]}
    ame_by_zn = {(int(e["Z"]), int(e["N"])): e for e in ame}

    m_p_exp = _m(obs["m_p_MeV"]["exp"])
    m_p_sig = _m(obs["m_p_MeV"]["sigma_exp"])
    m_n_exp = _m(obs["m_n_MeV"]["exp"])
    m_n_sig = _m(obs["m_n_MeV"]["sigma_exp"])

    nuclide_records: list[dict[str, Any]] = []
    for e in ame:
        z, n, a = int(e["Z"]), int(e["N"]), int(e["A"])
        if a < 2 or e.get("binding_energy_per_A_estimated") or e.get("binding_energy_per_A_keV") is None:
            continue
        r = mt_by_zn.get((z, n))
        if r is None:
            continue
        m_pred = _m(r["m_symbolic_MeV"])
        b_pred = _m(r["B_pred_MeV"])
        b_exp = _m(e["binding_energy_total_keV"]) / TEN_3
        b_sig = _m(e["binding_energy_per_A_unc_keV"]) * mpf(a) / TEN_3
        m_exp = mpf(z) * m_p_exp + mpf(n) * m_n_exp - b_exp
        m_sig = mp.sqrt((mpf(z) * m_p_sig) ** 2 + (mpf(n) * m_n_sig) ** 2 + b_sig ** 2)
        m_rel = abs(m_pred - m_exp) / m_exp
        b_rel = abs(b_pred - b_exp) / b_exp if b_exp > 0 else mpf(0)
        m_pull = abs(m_pred - m_exp) / m_sig if m_sig > 0 else mpf("1e99")
        b_pull = abs(b_pred - b_exp) / b_sig if b_sig > 0 else mpf("1e99")
        nuclide_records.append(
            dict(
                Z=z, N=n, A=a, el=str(e["element"]),
                m_pred=m_pred, m_exp=m_exp, m_rel=m_rel, m_pull=m_pull,
                b_pred=b_pred, b_exp=b_exp, b_rel=b_rel, b_pull=b_pull,
            )
        )

    bands = [
        ("Very Low-$A$ ($2\\text{--}16$)", lambda a: 2 <= a <= 16, "Light cluster regime; 1D chain misses 3D plaquettes"),
        ("Low/Mid-$A$ ($17\\text{--}56$)", lambda a: 17 <= a <= 56, "Approach to iron peak ($B_{\\mathrm{AME}}/A \\to 8.79\\;\\mathrm{MeV}$)"),
        ("High-$A$ Med ($57\\text{--}150$)", lambda a: 57 <= a <= 150, "Shell-saturated plateau; nucleonic rest mass dominates $M$"),
        ("Very High-$A$ ($\\ge 151$)", lambda a: a >= 151, "Coulomb-softened heavy regime ($B_{\\mathrm{AME}}/A \\approx 7.6\\;\\mathrm{MeV}$)"),
        ("**All Measured ($A \\ge 2$)**", lambda a: a >= 2, "Uniform `~0.57%` mass accuracy from constituent $(m_p, m_n)$"),
    ]

    mass_band_rows: list[str] = []
    binding_band_rows: list[str] = []
    for b_label, b_fn, b_note in bands:
        sub = [x for x in nuclide_records if b_fn(x["A"])]
        m_rels = [x["m_rel"] for x in sub]
        b_rels = [x["b_rel"] for x in sub]
        m_1s = sum(1 for x in sub if x["m_pull"] <= mpf(1))
        m_3s = sum(1 for x in sub if x["m_pull"] <= mpf(3))
        pos_b = sum(1 for x in sub if x["b_pred"] > 0)
        bpa_pred = _mean([x["b_pred"] / mpf(x["A"]) for x in sub])
        bpa_exp = _mean([x["b_exp"] / mpf(x["A"]) for x in sub])
        mass_band_rows.append(
            f"| {b_label} | `{len(sub)}` | `{_fmt_fixed(_mean(m_rels) * HUNDRED, 3)}%` | "
            f"`{_fmt_fixed(_median(m_rels) * HUNDRED, 3)}%` | `{_fmt_ppq(_median(m_rels))}` | "
            f"`{_fmt_fixed(min(m_rels) * HUNDRED, 3)}% / {_fmt_fixed(max(m_rels) * HUNDRED, 3)}%` | "
            f"`{m_1s} / {m_3s}` | {b_note} |"
        )
        binding_band_rows.append(
            f"| {b_label} | `{len(sub)}` | `{pos_b}/{len(sub)} (100%)` | "
            f"`{_fmt_fixed(_mean(b_rels) * HUNDRED, 2)}%` | `{_fmt_fixed(_median(b_rels) * HUNDRED, 2)}%` | "
            f"`{_fmt_ppq(_median(b_rels))}` | `{_fmt_fixed(bpa_pred, 3)}` | `{_fmt_fixed(bpa_exp, 3)}` |"
        )

    # ── Elementary / Hadron table (3.1a) ──────────────────────────────────────
    r2a = g2["part_a_quadratic_resolvent"]["R2a_qou_bare_vol41"]
    g2_emp = g2["empirical_benchmarks"]
    mtau_pred = _m(r2a["pred_m_tau_over_m_e"])
    mtau_exp_cod = _m(g2_emp["m_tau_over_m_e_codata_2022"])
    mtau_sig_cod = _m(g2_emp["m_tau_over_m_e_codata_uncert"])
    mtau_rel_cod = _m(r2a["rel_err_vs_codata_2022"])
    mtau_pull_cod = _m(r2a["sigma_pull_vs_codata_2022"])
    mtau_rel_p24 = _m(r2a["rel_err_vs_pdg_2024"])
    mtau_pull_p24 = _m(r2a["sigma_pull_vs_pdg_2024"])

    def _elem_row(label: str, key: str, po_key: str | None, status_txt: str) -> str:
        o = obs[key]
        pred = _m(o["pred"])
        exp = _m(o["exp"])
        spred = _m(o["sigma_pred"])
        sexp = _m(o["sigma_exp"])
        rel_ppb = _m(o["rel_ppb"])
        rel_frac = rel_ppb / TEN_9
        pull = _m(o["pull_exp"])
        unit = f" {o['units']}" if o["units"] and o["units"] != "None" else ""
        if o["is_calibration_pin"]:
            b100 = "Anchor (input)"
        elif po_key and po_key in po_by_obs:
            b100 = "Yes (`0.20x`)" if po_by_obs[po_key].get("beats_100x_experimental") is True else "No"
        else:
            b100 = "Yes" if abs(pred - exp) <= sexp / HUNDRED else "No"
        return (
            f"| {label} | `{_fmt_fixed(pred, 9)}{unit}` | `{_fmt_fixed(exp, 9)} ± {_fmt_sci(sexp, 2)}{unit}` | "
            f"`{_fmt_sci(spred, 3)}{unit}` | `{_fmt_rel_human(rel_frac)}` | `{_fmt_ppq(rel_frac)}` | "
            f"`{_fmt_fixed(pull, 2)}σ` | {b100} | {status_txt} |"
        )

    elem_rows = [
        _elem_row("Electron $m_e$", "m_e_MeV", "m_e", _st("m_e") + ": calibration input 1"),
        _elem_row("Muon $m_\\mu$", "m_mu_MeV", "m_mu", _st("m_mu") + " (proton $q_0$)"),
        (
            f"| Tau/electron $m_\\tau / m_e$ | `{_fmt_fixed(mtau_pred, 6)}` | "
            f"`{_fmt_fixed(mtau_exp_cod, 2)} ± {_fmt_fixed(mtau_sig_cod, 2)}` | "
            f"`—` | `{_fmt_rel_human(mtau_rel_cod)}` (`{_fmt_rel_human(mtau_rel_p24)}` PDG-24) | "
            f"`{_fmt_ppq(mtau_rel_cod)}` | "
            f"**`{_fmt_fixed(mtau_pull_cod, 2, signed=True)}σ`** (`{_fmt_fixed(mtau_pull_p24, 2, signed=True)}σ` PDG-24) | "
            f"No | {_st('m_tau_over_m_e')} (`KoideTopologicalProtectionHypothesis`, `< 1σ`) |"
        ),
        _elem_row("Charged pion $m_{\\pi^\\pm}$", "m_pi_pm_MeV", None, _st("m_pi") + ": calibration input 3"),
        _elem_row("Meson ratio $m_{K^\\pm}/m_{\\pi^\\pm}$", "mk_over_mpi", "m_K/m_pi", _st("mk_over_mpi") + " (the $(3,4)$ fusion pair is scan-selected; `< 0.002σ`)"),
        _elem_row("Charged kaon $m_{K^\\pm}$", "m_k_pm_MeV", None, _st("m_k") + " (inherits $m_K/m_\\pi$; `< 0.002σ`)"),
        _elem_row("Proton $m_p$", "m_p_MeV", "m_p", _st("m_p") + ": calibration input 2 ($q_0$ pin)"),
        _elem_row("Neutron $m_n$", "m_n_MeV", "m_n", _st("m_n") + " ($m_p + m_e + Q_{\\beta^-}$)"),
        _elem_row("Nucleon split $\\Delta m_{np}$", "delta_m_np_MeV", "Delta_pn", _st("delta_m_np") + " (`C1–C3`)"),
    ]

    # ── Representative nuclide benchmarks (3.1c) ──────────────────────────────
    nuc_summary_by_zn = {(int(n["Z"]), int(n["N"])): n for n in ma["nuclide_summary"]}
    m3a = g1["part2a_fixed_radius_plaquette_summary"]["models"]["M3a_kA_plaquette_pos"]
    b_he4_m3a = _m(m3a["per_A"]["A=4"]["bind_exact_in_Eosc_MeV"])

    rep_specs = [
        ("${}^2\\mathrm{H}$", 1, 1),
        ("${}^3\\mathrm{H}$", 1, 2),
        ("${}^4\\mathrm{He}$ ($K_4$ `M3a`)", 2, 2),
        ("${}^{12}\\mathrm{C}$", 6, 6),
        ("${}^{16}\\mathrm{O}$", 8, 8),
        ("${}^{40}\\mathrm{Ca}$", 20, 20),
        ("${}^{56}\\mathrm{Fe}$", 26, 30),
        ("${}^{120}\\mathrm{Sn}$", 50, 70),
        ("${}^{208}\\mathrm{Pb}$", 82, 126),
        ("${}^{238}\\mathrm{U}$", 92, 146),
    ]
    rep_rows: list[str] = []
    for sym, z, n in rep_specs:
        a = z + n
        ns = nuc_summary_by_zn[(z, n)]
        sig_ppb = _m(ns["sigma_pred_constituent_ppb"])
        e = ame_by_zn[(z, n)]
        b_exp = _m(e["binding_energy_total_keV"]) / TEN_3
        m_exp = mpf(z) * m_p_exp + mpf(n) * m_n_exp - b_exp
        if (z, n) == (2, 2):
            b_pred = b_he4_m3a
            m_pred = mpf(2) * _m(obs["m_p_MeV"]["pred"]) + mpf(2) * _m(obs["m_n_MeV"]["pred"]) - b_pred
        else:
            r = mt_by_zn[(z, n)]
            m_pred = _m(r["m_symbolic_MeV"])
            b_pred = _m(r["B_pred_MeV"])
        m_err_pct = (m_pred - m_exp) / m_exp * HUNDRED
        b_err_pct = (b_pred - b_exp) / b_exp * HUNDRED
        rep_rows.append(
            f"| {sym} | `({z}, {n}, {a})` | `{_fmt_fixed(m_pred, 4)}` | `{_fmt_fixed(m_exp, 4)}` | "
            f"`{_fmt_fixed(m_err_pct, 3, signed=True)}%` | `{_fmt_fixed(sig_ppb, 4)}` | "
            f"`{_fmt_fixed(b_pred, 3)}` | `{_fmt_fixed(b_exp, 3)}` | `{_fmt_fixed(b_err_pct, 2, signed=True)}%` |"
        )

    # ── Few-body binding table (3.2a) ─────────────────────────────────────────
    m5a = g1["part2a_fixed_radius_plaquette_summary"]["models"]["M5a_analytic_hoefsmit_plaq_cumulant"]
    j_hp = g1["part2b_jacobi_variational_battery"]["J_var_selfbound_E0__hall_post_fixed_eta2"]
    j_un = g1["part2b_jacobi_variational_battery"]["J_var_selfbound_E0__unrestricted_etaA"]

    b2_ame = _m(ame_by_zn[(1, 1)]["binding_energy_total_keV"]) / TEN_3
    b3h_ame = _m(ame_by_zn[(1, 2)]["binding_energy_total_keV"]) / TEN_3
    b3he_ame = _m(ame_by_zn[(2, 1)]["binding_energy_total_keV"]) / TEN_3
    b4_ame = _m(ame_by_zn[(2, 2)]["binding_energy_total_keV"]) / TEN_3

    b2_chain = _m(mt_by_zn[(1, 1)]["B_pred_MeV"])
    b3_chain = _m(mt_by_zn[(1, 2)]["B_pred_MeV"])

    def _fb_cell(b_val: mpf, b_ref: mpf) -> str:
        pct = (b_val - b_ref) / b_ref * HUNDRED
        return f"`{_fmt_fixed(b_val, 3)}` (`{_fmt_fixed(pct, 2, signed=True)}%`)"

    b2_m3a = _m(m3a["per_A"]["A=2"]["bind_exact_in_Eosc_MeV"])
    b3_m3a = _m(m3a["per_A"]["A=3"]["bind_exact_in_Eosc_MeV"])
    b4_m3a = b_he4_m3a

    b2_m5a = _m(m5a["per_A"]["A=2"]["bind_exact_in_Eosc_MeV"])
    b3_m5a = _m(m5a["per_A"]["A=3"]["bind_exact_in_Eosc_MeV"])
    b4_m5a = _m(m5a["per_A"]["A=4"]["bind_exact_in_Eosc_MeV"])

    b2_jhp = _m(j_hp["per_A"]["A=2"]["bind_MeV"])
    b3_jhp = _m(j_hp["per_A"]["A=3"]["bind_MeV"])
    b4_jhp = _m(j_hp["per_A"]["A=4"]["bind_MeV"])

    b2_jun = _m(j_un["per_A"]["A=2"]["bind_MeV"])
    b3_jun = _m(j_un["per_A"]["A=3"]["bind_MeV"])
    b4_jun = _m(j_un["per_A"]["A=4"]["bind_MeV"])

    # Ruled trace pipeline: gamma-gamma bond V(2)^3 between the V^3 nucleons (selected by the
    # cheapest-passing rule, owner card 1, 2026-11-25), log law B = -E_0 ln(tr_atom/tr_free) at the
    # ruled tower E_0. The trace ratio is read from the producer; only the E_0 chart is applied here.
    gg_rows = gg_bond["results"]["V^3"]["rows"]
    gg_sel = [r for r in gg_rows if r["bond"] == "V(2)^3" and r["reading3_every_level"] is True]
    if len(gg_sel) != 1:
        errors.append("gg-deuteron-bond: expected exactly one passing V(2)^3 row at m = 3")
        b2_gg = mpf(0)
    else:
        b2_gg = -_m(po["qbeta_ruled_base"]["E0_MeV"]) * mp.log(_m(gg_sel[0]["ratio"]))

    fewbody_rows = [
        (
            f"| AME2020 Experimental Reference | `{_fmt_fixed(b2_ame, 5)}` | `{_fmt_fixed(b3h_ame, 5)}` | "
            f"`{_fmt_fixed(b3he_ame, 5)}` | `{_fmt_fixed(b4_ame, 5)}` | "
            f"`{_fmt_fixed(b3h_ame / b2_ame, 3)}` (`3H`) | `{_fmt_fixed(b4_ame / b2_ame, 3)}` |"
        ),
        (
            f"| 1D Symbolic Hecke Chain (`mass-table`) | {_fb_cell(b2_chain, b2_ame)} | {_fb_cell(b3_chain, b3h_ame)} | "
            f"`—` (omitted) | `—` (omitted) | `{_fmt_fixed(b3_chain / b2_chain, 3)}` | `3.000` (asymptotic) |"
        ),
        (
            f"| Ruled trace pipeline (γγ bond $V(2)^3$, tower $E_0$, log law) | "
            f"`{_fmt_fixed(b2_gg, 5)}` (`{_fmt_fixed((b2_gg - b2_ame) / b2_ame * HUNDRED, 2, signed=True)}%`) | "
            f"`—` (p = n cell) | `—` (p = n cell) | `—` (not computed) | `—` | `—` |"
        ),
        (
            f"| 3D $K_A$ Plaquette Exact (`M3a`, $E_{{\\mathrm{{osc}}}}$) | {_fb_cell(b2_m3a, b2_ame)} | "
            f"{_fb_cell(b3_m3a, b3h_ame)} | {_fb_cell(b3_m3a, b3he_ame)} | {_fb_cell(b4_m3a, b4_ame)} | "
            f"`{_fmt_fixed(_m(m3a['scaling_ratios_exact_vs_A2']['A3_over_A2']), 3)}` | "
            f"`{_fmt_fixed(_m(m3a['scaling_ratios_exact_vs_A2']['A4_over_A2']), 3)}` |"
        ),
        (
            f"| Analytic Hoefsmit Plaquette Cumulant (`M5a`) | {_fb_cell(b2_m5a, b2_ame)} | "
            f"{_fb_cell(b3_m5a, b3h_ame)} | {_fb_cell(b3_m5a, b3he_ame)} | {_fb_cell(b4_m5a, b4_ame)} | "
            f"`{_fmt_fixed(_m(m5a['scaling_ratios_exact_vs_A2']['A3_over_A2']), 3)}` | "
            f"`{_fmt_fixed(_m(m5a['scaling_ratios_exact_vs_A2']['A4_over_A2']), 3)}` |"
        ),
        (
            f"| Self-Bound Jacobi Variational (Hall–Post $\\eta_2$) | {_fb_cell(b2_jhp, b2_ame)} | "
            f"{_fb_cell(b3_jhp, b3h_ame)} | {_fb_cell(b3_jhp, b3he_ame)} | {_fb_cell(b4_jhp, b4_ame)} | "
            f"`{_fmt_fixed(_m(j_hp['scaling_ratios_vs_A2']['A3_over_A2']), 3)}` | "
            f"`{_fmt_fixed(_m(j_hp['scaling_ratios_vs_A2']['A4_over_A2']), 3)}` |"
        ),
        (
            f"| Self-Bound Jacobi Variational (Unrestricted $\\eta_A^*$) | {_fb_cell(b2_jun, b2_ame)} | "
            f"{_fb_cell(b3_jun, b3h_ame)} | {_fb_cell(b3_jun, b3he_ame)} | {_fb_cell(b4_jun, b4_ame)} | "
            f"`{_fmt_fixed(_m(j_un['scaling_ratios_vs_A2']['A3_over_A2']), 3)}` | "
            f"`{_fmt_fixed(_m(j_un['scaling_ratios_vs_A2']['A4_over_A2']), 3)}` |"
        ),
    ]
    _fb_status = ["Reference", _st("hecke_1d_chain"), _st("ruled_trace_2h")] + [_st("ka_rows")] * (
        len(fewbody_rows) - 3
    )
    fewbody_rows = [row + f" {st} |" for row, st in zip(fewbody_rows, _fb_status)]

    # ── Category 3: Charge, EM, Coulomb, Molecular ────────────────────────────
    alpha_cs_ppb = _m(alpha_cs["rel_ppb"])
    alpha_cs_pull = _m(alpha_cs["pull_exp"])
    tanh_ln_q0 = _m(cc["coulomb_strong_ratio_tanh_ln_q0"])
    coul_dhe = _m(cc["derived_coulomb_dHe_MeV"])
    coul_ame = _m(cc["ame_split_MeV"])
    coul_rel = (coul_dhe - coul_ame) / coul_ame
    coul_frac = _m(cc["fraction_of_split_covered"])
    coul_short = _m(cc["remaining_factor"])
    mirror_mean = _m(mn["ratio_mean"])
    mirror_rms = _m(mn["ratio_rms_scatter"])
    mirror_rel = mirror_mean - mpf(1)

    charge_rows = [
        (
            f"| Electric charge quantization $Q(p), Q(n)$ | `+1, 0` ($c = {u1['Q1_c_structural_status']['value']}$) | "
            f"`+1, 0` ($\\|Q_p + Q_e\\|/e < 10^{{-21}}$) | `0` (exact) | `0` | Exact | "
            f"{_st('charge_Q')}: proved topological writhe $Q = \\tfrac{{1}}{{2}}\\operatorname{{writhe}}(H)$ |"
        ),
        (
            f"| Fine-structure $\\alpha_{{\\mathrm{{EM}}}}^{{-1}}$ (Schwinger Form B, 4-topology) | `{_fmt_fixed(_m(alpha_fb['pred']), 9)}` | "
            f"`{_fmt_fixed(alpha_exp, 9)} ± 2.1e-8` | `{_fmt_fixed(alpha_fb_ppb, 3, signed=True)} ppb` | "
            f"`{_fmt_ppq(alpha_fb_ppb / TEN_9)}` | `{_fmt_fixed(alpha_fb_pull, 2, signed=True)}σ` | "
            f"{_st('alpha_form_b')}: 4-topology `(1 - h_A^2 α)` loop factor proved; value conditional on `ArchimedeanLimit`, `BlochSuslinUniqueness`, `BringZeroModeBlochClass` |"
        ),
        (
            f"| Fine-structure $\\alpha_{{\\mathrm{{EM}}}}^{{-1}}$ (2-loop Bloch-$B_3$ Form C) | `{_fmt_fixed(_m(alpha_fc['pred']), 9)}` | "
            f"`{_fmt_fixed(alpha_exp, 9)} ± 2.1e-8` | `{_fmt_fixed(alpha_fc_ppb, 3, signed=True)} ppb` | "
            f"`{_fmt_ppq(alpha_fc_ppb / TEN_9)}` | **`{_fmt_fixed(alpha_fc_pull, 2, signed=True)}σ`** | "
            f"{_st('alpha_form_c')}: two-loop Bloch-$B_3(\\mathbb{{C}})$ trilogarithm defect (within $1\\sigma_{{\\mathrm{{exp}}}}$!) |"
        ),
        (
            f"| Fine-structure $\\alpha_{{\\mathrm{{EM}}}}^{{-1}}$ ($8\\times 8$ Seifert $\\kappa_{{\\mathrm{{Seifert}}}}$) | `{_fmt_fixed(_m(alpha_seif['pred']), 9)}` | "
            f"`{_fmt_fixed(alpha_exp, 9)} ± 2.1e-8` | `{_fmt_fixed(alpha_seif_ppb, 2, signed=True)} ppb` | "
            f"`{_fmt_ppq(alpha_seif_ppb / TEN_9)}` | `{_fmt_fixed(alpha_seif_pull, 1, signed=True)}σ` | "
            f"{_st('alpha_seifert')}: homological $b_1(\\Sigma_4)=8$ Seifert pairing (`19.1x` closer than Witten $2\\times 2$) |"
        ),
        (
            f"| Fine-structure $\\alpha_{{\\mathrm{{EM}}}}^{{-1}}$ (legacy Witten $2\\times 2$ CS) | `{_fmt_fixed(_m(alpha_cs['pred']), 9)}` | "
            f"`{_fmt_fixed(alpha_exp, 9)} ± 2.1e-8` | `{_fmt_fixed(alpha_cs_ppb, 2, signed=True)} ppb` | "
            f"`{_fmt_ppq(alpha_cs_ppb / TEN_9)}` | `{_fmt_fixed(alpha_cs_pull, 1, signed=True)}σ` | "
            f"{_st('alpha_legacy_cs')}: legacy $2\\times 2$ Chern–Simons baseline (`-0.468 ppm` gap vs Form B) |"
        ),
        (
            f"| Rydberg constant $R_\\infty h c$ (Schwinger Form B) | `{_fmt_fixed(_m(ry_fb['pred']), 9)} eV` | "
            f"`{_fmt_fixed(_m(ry_fb['exp']), 9)} ± 1.5e-11 eV` | `{_fmt_fixed(ry_fb_ppb, 3, signed=True)} ppb` | "
            f"`{_fmt_ppq(ry_fb_ppb / TEN_9)}` | `{_fmt_fixed(ry_fb_zcomb, 2, signed=True)}σ` ($z_{{\\mathrm{{comb}}}}$) | "
            f"{_st('rydberg_form_b')}: $\\tfrac{{1}}{{2}}m_e c^2 \\alpha_{{\\mathrm{{EM}}}}^2$ with Form B $\\alpha$ ($\\sigma_{{\\mathrm{{pred}}}} = 0.313\\;\\mathrm{{ppb}}$ from $m_e$) |"
        ),
        (
            f"| Rydberg constant $R_\\infty h c$ (2-loop Bloch-$B_3$ Form C) | `{_fmt_fixed(_m(ry_fc['pred']), 9)} eV` | "
            f"`{_fmt_fixed(_m(ry_fc['exp']), 9)} ± 1.5e-11 eV` | `{_fmt_fixed(ry_fc_ppb, 3, signed=True)} ppb` | "
            f"`{_fmt_ppq(ry_fc_ppb / TEN_9)}` | **`{_fmt_fixed(ry_fc_zcomb, 2, signed=True)}σ`** ($z_{{\\mathrm{{comb}}}}$) | "
            f"{_st('rydberg_form_c')}: two-loop Bloch-$B_3$ Rydberg (within $1\\sigma_{{\\mathrm{{comb}}}}$!) |"
        ),
        (
            f"| Bare topological ${{}}^3\\mathrm{{H}}\\text{{--}}{{}}^3\\mathrm{{He}}$ Coulomb | `{_fmt_fixed(coul_dhe, 4)} MeV` | "
            f"`{_fmt_fixed(coul_ame, 4)} MeV` | `{_fmt_fixed(coul_rel * HUNDRED, 2, signed=True)}%` (`{_fmt_fixed(coul_frac * HUNDRED, 1)}%` covered) | "
            f"`{_fmt_ppq(coul_rel)}` | `{_fmt_fixed(coul_short, 2)}x` short | {_st('coulomb_3h_3he')}: zero-fit $\\tanh(\\ln q_0) B_{{pp}}$ on the ruled nucleon word; scope-limited negative, nuclear-geometry factor open |"
        ),
        (
            f"| Mirror-nuclei Coulomb systematics ($N={len(mn['mirror_pairs'])}$, $A=3\\text{{--}}39$) | "
            f"Ratio `{_fmt_fixed(mirror_mean, 4)}` | `1.0000` (AME2020 splits) | "
            f"`{_fmt_fixed(mirror_rel * HUNDRED, 2, signed=True)}%` mean | `{_fmt_ppq(mirror_rel)}` | "
            f"`±{_fmt_fixed(mirror_rms * HUNDRED, 2)}%` RMS | {_st('mirror_coulomb')}: uniform-sphere Coulomb with $R=(\\hbar c/m_\\pi)A^{{1/3}}$ (coefficient 1 on $\\hbar c/m_\\pi$ selected, $A^{{1/3}}$ assumed; not $r_0=1.2$ fm); ratio rises with $A$, `{_fmt_fixed(_m(mn['ratio_trend_in_A']['ratio_at_A3']), 3)}` at $A=3$, so quote per $A$ |"
        ),
    ]

    mol_specs = [
        ("$\\theta(\\mathrm{CH_4})$", "Exact $T_d$ tetrahedral ($4$ single bonds)", "theta_ch4_deg", "°"),
        ("$\\theta(\\mathrm{CO_2})$", "Exact $D_{\\infty h}$ linear ($2$ double bonds)", "theta_co2_deg", "°"),
        ("$\\theta(\\mathrm{NH_3})$", "$C_{3v}$ $AX_3E_1$ ($q$ bond vs $q^3$ lone pair)", "theta_nh3_deg", "°"),
        ("$\\theta(\\mathrm{H_2O})$", "$C_{2v}$ $AX_2E_2$ ($2\\times q$ vs $2\\times q^3$)", "theta_h2o_deg", "°"),
        ("$\\theta(\\mathrm{C_2H_4})$", "$C_{2v}$ planar $AX_3$ ($q^2$ double vs $q$ single)", "theta_c2h4_deg", "°"),
        ("$\\theta(\\mathrm{H_2S})$", "Orthogonal $p$-orbital baseline", "theta_h2s_deg", "°"),
        ("$L_{\\mathrm{vap}}(\\mathrm{H_2O})$", "Hydrogen-bond $q$-plaquette enthalpy", "L_h2o_kJmol", " kJ/mol"),
    ]
    mol_rows: list[str] = []
    mol_1s = 0
    mol_3s = 0
    for m_name, m_sym, m_key, m_unit in mol_specs:
        mo = obs[m_key]
        pred = _m(mo["pred"])
        exp = _m(mo["exp"])
        res = _m(mo["residual"])
        rel_frac = _m(mo["rel_ppb"]) / TEN_9
        pull = _m(mo["pull_exp"])
        if abs(pull) <= mpf(1):
            mol_1s += 1
        if abs(pull) <= mpf(3):
            mol_3s += 1
        mol_rows.append(
            f"| {m_name} | {m_sym} | `{_fmt_fixed(pred, 4)}{m_unit}` | `{_fmt_fixed(exp, 4)}{m_unit}` | "
            f"`{_fmt_fixed(res, 4, signed=True)}{m_unit}` | `{_fmt_rel_human(rel_frac)}` | "
            f"`{_fmt_ppq(rel_frac)}` | `{_fmt_fixed(pull, 2, signed=True)}σ` |"
        )

    # ── Category 4: Beta-decay benchmarks & 1,010 transitions ─────────────────
    qbeta_base = _m(obs["q_beta_base_MeV"]["pred"])
    nv_crossing = _m(bd["G_F_decomposition"]["N_v_crossing_count"])

    beta_bench_specs = [
        ("Free neutron $n \\to p e^- \\bar\\nu_e$", "Conditional $T^3$ weight-trace split (`V^3`)", "q_beta_base_MeV", "Conditional (`C1–C3`)"),
        ("${}^3\\mathrm{H} \\to {}^3\\mathrm{He}$", "Bare monotone transfer-matrix skein shift", "qbeta_3H_MeV", "Zero-fit TM proxy"),
        ("${}^{14}\\mathrm{C} \\to {}^{14}\\mathrm{N}$", "Bare monotone transfer-matrix skein shift", "qbeta_14C_MeV", "Zero-fit TM proxy (`-8.11%`)"),
        ("${}^{60}\\mathrm{Co} \\to {}^{60}\\mathrm{Ni}$", "Bare monotone transfer-matrix skein shift", "qbeta_60Co_MeV", "Zero-fit TM proxy"),
        ("${}^{90}\\mathrm{Sr} \\to {}^{90}\\mathrm{Y}$", "Bare monotone transfer-matrix skein shift", "qbeta_90Sr_MeV", "Zero-fit TM proxy"),
        ("${}^{137}\\mathrm{Cs} \\to {}^{137}\\mathrm{Ba}$", "Bare monotone transfer-matrix skein shift", "qbeta_137Cs_MeV", "Zero-fit TM proxy"),
        ("${}^{210}\\mathrm{Bi} \\to {}^{210}\\mathrm{Po}$", "Bare monotone transfer-matrix skein shift", "qbeta_210Bi_MeV", "Zero-fit TM proxy"),
    ]
    beta_bench_rows: list[str] = []
    for b_lbl, b_form, b_key, b_stat in beta_bench_specs:
        bo = obs[b_key]
        pred = _m(bo["pred"])
        exp = _m(bo["exp"])
        rel_frac = _m(bo["rel_ppb"]) / TEN_9
        pull = _m(bo["pull_exp"])
        beta_bench_rows.append(
            f"| {b_lbl} | {b_form} | `{_fmt_fixed(pred, 5)} MeV` | `{_fmt_fixed(exp, 5)} MeV` | "
            f"`{_fmt_rel_human(rel_frac)}` | `{_fmt_ppq(rel_frac)}` | `{_fmt_fixed(pull, 1, signed=True)}σ` | {_st('q_beta_free_neutron' if b_key == 'q_beta_base_MeV' else 'beta_tm_rows')}: {b_stat} |"
        )
    beta_bench_rows.append(
        f"| Electroweak VEV $v_{{\\mathrm{{weak}}}}$ ($N_v = {_fmt_fixed(nv_pred, 6)}$) | "
        f"Bring–Schwinger fixed point $1/\\alpha_v = T_{{\\mathrm{{EW}}}} - \\alpha_v H(1 - \\hbar_q^2 \\alpha_v)$ | "
        f"`{_fmt_fixed(vew_pred, 6)} GeV` | `{_fmt_fixed(vew_exp, 6)} ± {_fmt_sci(vew_sig_exp, 2)} GeV` | "
        f"**`{_fmt_fixed(vew_ppb, 2, signed=True)} ppb`** | `{_fmt_ppq(vew_ppb / TEN_9)}` | "
        f"**`{_fmt_fixed(vew_pull, 2, signed=True)}σ`** | {_st('v_weak')}: Bring–Schwinger fixed point ($G_F$ within $1\\sigma_{{\\mathrm{{exp}}}}$!) |"
    )

    beta_records: list[dict[str, Any]] = []
    for e in ame:
        z, n, a = int(e["Z"]), int(e["N"]), int(e["A"])
        if e.get("beta_decay_energy_estimated") or e.get("beta_decay_energy_keV") is None:
            continue
        q_exp = _m(e["beta_decay_energy_keV"]) / TEN_3
        if q_exp <= mpf("0.01"):
            continue
        if (z, n) not in mt_by_zn or (z + 1, n - 1) not in mt_by_zn:
            continue
        # Ruled-law masses (free baseline + T_z-even bond, PR #9675). The old
        # m_symbolic gave every composite row the same -1.793 MeV
        # (computations/probes/composite_beta_sign_decomposition_probe.py).
        _mk = "m_ruled_MeV" if mt_by_zn[(z, n)].get("m_ruled_MeV") else "m_symbolic_MeV"
        if not mt_by_zn[(z + 1, n - 1)].get(_mk):
            continue
        q_pred = _m(mt_by_zn[(z, n)][_mk]) - _m(mt_by_zn[(z + 1, n - 1)][_mk]) - m_e
        rel = abs(q_pred - q_exp) / q_exp
        beta_records.append(dict(Z=z, N=n, A=a, q_pred=q_pred, q_exp=q_exp, rel=rel, exo=(q_pred > 0)))

    beta_band_defs = [
        ("Free Neutron ($A = 1$)", lambda a: a == 1, "Exothermic (`0.325` vs `0.782 MeV`, `-58.4%`)"),
        ("Very Low-$A$ ($2\\text{--}16$)", lambda a: 2 <= a <= 16, "Missing 3D cluster + symmetry energy"),
        ("Low/Mid-$A$ ($17\\text{--}56$)", lambda a: 17 <= a <= 56, "Missing Pauli asymmetry + Coulomb shift"),
        ("High-$A$ Med ($57\\text{--}150$)", lambda a: 57 <= a <= 150, "Isobaric parabola absent in 1D Q-CLT chain"),
        ("Very High-$A$ ($\\ge 151$)", lambda a: a >= 151, "Large $Z$ Coulomb gradient omitted"),
        ("**All Measured ($A \\ge 1$)**", lambda a: a >= 1, "Ruled-law $B$: sign from the $T_z$-even bond, flat $Q$ until Coulomb / $T(T+1)$ terms land"),
    ]
    beta_band_rows: list[str] = []
    for bb_lbl, bb_fn, bb_diag in beta_band_defs:
        sub = [x for x in beta_records if bb_fn(x["A"])]
        rels = [x["rel"] for x in sub]
        exo = sum(1 for x in sub if x["exo"])
        beta_band_rows.append(
            f"| {bb_lbl} | `{len(sub)}` | `{exo}/{len(sub)}` | `{_fmt_fixed(_mean(rels) * HUNDRED, 1)}%` | "
            f"`{_fmt_fixed(_median(rels) * HUNDRED, 1)}%` | `{_fmt_ppq(_median(rels))}` | {bb_diag} |"
        )

    # ── Category 5: Alpha-decay Gamow WKB & 1,051 derived Q_alpha ────────────
    alpha_gamow_rows: list[str] = []
    dex_open: list[mpf] = []
    for em in ad["part_a_baseline_gamow_emitters"]["emitters"]:
        nuc = em["nuclide"]
        z_s, n_s, a_s = em["Z"], em["N"], em["A"]
        q_a = _m(em["Q_alpha_AME_MeV"])
        t_exp = _m(em["T_half_exp_s"])
        t_wkb = _m(em["T_half_WKB_s"])
        dex = _m(em["log10_T_WKB_over_T_exp_dex"])
        if nuc != "210Po":
            dex_open.append(abs(dex))
        fac = mpf(10) ** abs(dex)
        note = "Closed $N=126$ shell ($S_\\alpha^{\\mathrm{emp}} = 0.0553$)" if nuc == "210Po" else str(em["regime"])
        alpha_gamow_rows.append(
            f"| `{nuc}` (bare WKB, $S_\\alpha=1$) | `({z_s}, {n_s}, {a_s})` | `{_fmt_fixed(q_a, 4)}` | "
            f"`{_fmt_sci(t_exp, 3)}` | `{_fmt_sci(t_wkb, 3)}` | `{_fmt_fixed(dex, 3, signed=True)}` | "
            f"`{_fmt_fixed(fac, 2)}x` | {note} |"
        )

    mj = ad["part_b_n126_preformation_mechanisms"]["mayer_jensen_combinatorial"]
    po210_em = [e for e in ad["part_a_baseline_gamow_emitters"]["emitters"] if e["nuclide"] == "210Po"][0]
    t_po210_mj = _m(mj["Po210_T_half_with_S_MJ_joint_s"])
    dex_po210_mj = _m(mj["Po210_T_half_S_MJ_joint_dex_err"])
    alpha_gamow_rows.append(
        f"| **`210Po` + Mayer–Jensen $S_\\alpha^{{\\mathrm{{MJ}}}}=1/20$** | `(84, 126, 210)` | "
        f"`{_fmt_fixed(_m(po210_em['Q_alpha_AME_MeV']), 4)}` | `{_fmt_sci(_m(po210_em['T_half_exp_s']), 3)}` | "
        f"`{_fmt_sci(t_po210_mj, 3)}` | **`{_fmt_fixed(dex_po210_mj, 3, signed=True)}`** | "
        f"**`{_fmt_fixed(mpf(10) ** abs(dex_po210_mj), 2)}x`** | Parameter-free $(1h_{{9/2}}, 3p_{{1/2}}/2g_{{9/2}})$ shell preformation |"
    )

    # The production mass table (1D chain, Q-CLT) has its own 4He. The rows below
    # labelled "mixed" pair chain parents/daughters with the K4-plaquette 4He
    # (gap1b M3a); the "chain only" row uses the chain's own 4He so that one
    # model supplies all three bindings (bean qou-q0gw).
    # (2,2) has no mass-table row, so the chain's 4He is its own alpha-line
    # extrapolation B(8Be) - [B(12C) - B(8Be)], as in alpha_qalpha_inheritance_probe.py.
    b_he4_chain = 2 * _m(mt_by_zn[(4, 4)]["B_pred_MeV"]) - _m(mt_by_zn[(6, 6)]["B_pred_MeV"])
    alpha_records: list[dict[str, Any]] = []
    for e in ame:
        z, n, a = int(e["Z"]), int(e["N"]), int(e["A"])
        if z < 2 or n < 2 or a < 6:
            continue
        if e.get("binding_energy_per_A_estimated") or e.get("binding_energy_per_A_keV") is None:
            continue
        ed = ame_by_zn.get((z - 2, n - 2))
        if ed is None or ed.get("binding_energy_per_A_estimated") or ed.get("binding_energy_per_A_keV") is None:
            continue
        if (z, n) not in mt_by_zn or (z - 2, n - 2) not in mt_by_zn:
            continue
        b_par_exp = _m(e["binding_energy_total_keV"]) / TEN_3
        b_dau_exp = _m(ed["binding_energy_total_keV"]) / TEN_3
        q_exp = b_dau_exp + b4_ame - b_par_exp
        if q_exp <= mpf("0.5"):
            continue
        b_par_pred = _m(mt_by_zn[(z, n)]["B_pred_MeV"])
        b_dau_pred = _m(mt_by_zn[(z - 2, n - 2)]["B_pred_MeV"])
        q_pred = b_dau_pred + b_he4_m3a - b_par_pred
        rel = abs(q_pred - q_exp) / q_exp
        # Self-consistent arm: the chain model's own 4He, not the K4-plaquette one.
        q_chain = b_dau_pred + b_he4_chain - b_par_pred
        alpha_records.append(dict(Z=z, N=n, A=a, q_pred=q_pred, q_exp=q_exp, rel=rel, exo=(q_pred > 0),
                                  q_chain=q_chain, rel_chain=abs(q_chain - q_exp) / q_exp))

    alpha_derived_rows: list[str] = []
    for ab_lbl, ab_fn, ab_note in [
        ("High-$A$ Med ($57\\text{--}150$, mixed: chain + $K_4$ ${}^4\\mathrm{He}$)", lambda a: 57 <= a <= 150, "1D chain underbinds parent/daughter slope $\\Delta B/\\Delta A$"),
        ("Very High-$A$ ($\\ge 151$, mixed: chain + $K_4$ ${}^4\\mathrm{He}$)", lambda a: a >= 151, "Over-exothermic ($Q_\\alpha^{\\mathrm{pred}} \\approx 21\\;\\mathrm{MeV}$) without shell/Coulomb"),
        ("**All Measured Exothermic ($A \\ge 6$, mixed)**", lambda a: a >= 6, "All `1,051` exothermic; ~93% of the $Q_\\alpha$ error is inherited from the binding slope"),
    ]:
        sub = [x for x in alpha_records if ab_fn(x["A"])]
        rels = [x["rel"] for x in sub]
        exo = sum(1 for x in sub if x["exo"])
        q_p_med = _median([x["q_pred"] for x in sub])
        q_e_med = _median([x["q_exp"] for x in sub])
        alpha_derived_rows.append(
            f"| {ab_lbl} | `N = {len(sub)}` | `{exo}/{len(sub)} (100%)` | "
            f"Med `{_fmt_fixed(q_p_med, 2)}` vs `{_fmt_fixed(q_e_med, 2)} MeV` | "
            f"Med `{_fmt_fixed(_median(rels) * HUNDRED, 1)}%` (Mean `{_fmt_fixed(_mean(rels) * HUNDRED, 1)}%`) | "
            f"`{_fmt_ppq(_median(rels))}` | {ab_note} |"
        )

    rels_ch = [x["rel_chain"] for x in alpha_records]
    exo_ch = sum(1 for x in alpha_records if x["q_chain"] > 0)
    alpha_derived_rows.append(
        f"| **Chain only, self-consistent ($A \\ge 6$)** | `N = {len(alpha_records)}` | "
        f"`{exo_ch}/{len(alpha_records)}` | "
        f"Med `{_fmt_fixed(_median([x['q_chain'] for x in alpha_records]), 2)}` vs "
        f"`{_fmt_fixed(_median([x['q_exp'] for x in alpha_records]), 2)} MeV` | "
        f"Med `{_fmt_fixed(_median(rels_ch) * HUNDRED, 1)}%` (Mean `{_fmt_fixed(_mean(rels_ch) * HUNDRED, 1)}%`) | "
        f"`{_fmt_ppq(_median(rels_ch))}` | Chain ${{}}^4\\mathrm{{He}}$ (extrapolated) = `{_fmt_fixed(b_he4_chain, 2)} MeV`; "
        f"one $\\alpha$-line slope for every pair, so $Q_\\alpha$ is constant (`AlphaQInheritance.lean`) |"
    )

    part_c_by_nuc = {h["nuclide"]: h for h in ad["part_c_derived_qalpha_benchmark"]["heavy_emitters"]}
    for nuc_c in ["210Po", "212Po", "238U"]:
        hc = part_c_by_nuc[nuc_c]
        q_ame_c = _m(hc["Q_alpha_AME_MeV"])
        m_fcc = hc["models"]["H2_FCC_k12_std"]
        q_fcc = _m(m_fcc["Q_alpha_QOU_MeV"])
        dex_fcc = _m(m_fcc["log10_T_QOU_over_T_exp_dex"])
        rel_fcc = (q_fcc - q_ame_c) / q_ame_c
        alpha_derived_rows.append(
            f"| FCC $k=12$ cluster model (`H2_FCC_k12_std`) | `{nuc_c}` | `Yes` | "
            f"`{_fmt_fixed(q_fcc, 2)}` vs `{_fmt_fixed(q_ame_c, 2)} MeV` | "
            f"`{_fmt_fixed(rel_fcc * HUNDRED, 1, signed=True)}%` (`+{_fmt_fixed(dex_fcc, 2)} dex` in $T_{{1/2}}$) | "
            f"`{_fmt_ppq(rel_fcc)}` | Gamow sensitivity `{_fmt_fixed(_m(hc['d_log10_T_d_Qalpha_dex_per_MeV']), 2)} dex/MeV` |"
        )

    # ── Section 2: Executive Scorecard Rows ───────────────────────────────────
    all_m_rels = [x["m_rel"] for x in nuclide_records]
    all_b_rels = [x["b_rel"] for x in nuclide_records]
    all_beta_rels = [x["rel"] for x in beta_records]
    all_alpha_rels = [x["rel"] for x in alpha_records]

    mk_ppb_val = _m(obs["mk_over_mpi"]["rel_ppb"])
    elem_med_ppm = (abs(_m(obs["m_mu_MeV"]["rel_ppb"])) / TEN_3 + abs(mtau_rel_cod) * TEN_6) / mpf(2)
    # Within 1σ counting only rows the status witness labels Derived (owner dispatch
    # 2026-11-27): the honest headline. Pairs are (row id, display label, pull or None).
    def _derived_within(pairs: list[tuple[str, str, Any]], n_total: int) -> str:
        hits = [lbl for rid, lbl, pull in pairs
                if pull is not None and abs(pull) <= mpf(1) and _status(rid) == "Derived"]
        return f"**`{len(hits)} / {n_total}`**" + (f" ({', '.join(hits)})" if hits else "")

    cat1_pairs = [
        ("m_mu", "$m_\\mu$", _m(obs["m_mu_MeV"]["pull_exp"])),
        ("m_tau_over_m_e", "$m_\\tau/m_e$", mtau_pull_cod),
        ("mk_over_mpi", "$m_K/m_\\pi$", _m(obs["mk_over_mpi"]["pull_exp"])),
        ("m_k", "$m_K$", _m(obs["m_k_pm_MeV"]["pull_exp"])),
        ("m_n", "$m_n$", _m(obs["m_n_MeV"]["pull_exp"])),
        ("delta_m_np", "$\\Delta m_{np}$", _m(obs["delta_m_np_MeV"]["pull_exp"])),
    ]
    cat3_pairs = [
        ("charge_Q", "$Q$", mpf(0)),
        ("alpha_form_b", "Form B $\\alpha_{\\mathrm{EM}}$", alpha_fb_pull),
        ("alpha_form_c", "Form C $\\alpha_{\\mathrm{EM}}$", alpha_fc_pull),
        ("alpha_seifert", "Seifert $\\alpha_{\\mathrm{EM}}$", alpha_seif_pull),
        ("alpha_legacy_cs", "CS $\\alpha_{\\mathrm{EM}}$", alpha_cs_pull),
        ("rydberg_form_b", "Form B $R_\\infty$", ry_fb_zcomb),
        ("rydberg_form_c", "Form C $R_\\infty$", ry_fc_zcomb),
    ] + [("vsepr", "VSEPR", mpf(0))] * mol_1s
    cat4_pairs = [("v_weak", "$v_{\\mathrm{weak}}$", vew_pull)] + [
        ("q_beta_free_neutron" if k == "q_beta_base_MeV" else "beta_tm_rows", k, _m(obs[k]["pull_exp"]))
        for _l, _f, k, _s in beta_bench_specs
    ]
    def _group(pairs: list[tuple[str, str, Any]]) -> str:
        seen: dict[str, list[str]] = {}
        for rid, lbl, _p in pairs:
            names = seen.setdefault(_status(rid), [])
            if lbl not in names:
                names.append(lbl)
        order = ["Derived", "Selected", "Conditional", "Unclassified", "Calibration"]
        return "; ".join(f"{k} ({', '.join(seen[k])})" for k in order if k in seen)

    exec_rows = [
        (
            f"| **1. Mass** (Elementary & Hadrons) | $m_\\mu, m_\\tau/m_e, m_K/m_\\pi, m_K, m_n$ (+ 3 pins) | `6` (+3 pins) | "
            f"`81.1 ppm` (`136 ppb` excl. $m_n, m_\\tau$) | `{_fmt_fixed(elem_med_ppm, 1)} ppm` (`211 ppb` $m_\\mu$) | `5.14e+07` to `4.86e+11` | "
            f"**`3 / 6`** ($m_K/m_\\pi, m_K, m_\\tau/m_e$) | **`3 / 6`** ($m_K/m_\\pi, m_K, m_\\tau/m_e$) | "
            f"**High** on selected $m_K/m_\\pi$ (`{_fmt_fixed(mk_ppb_val, 3, signed=True)} ppb`, `<0.002σ`), $m_\\mu$ (`+211 ppb`), & cond. $m_\\tau/m_e$ (`{_fmt_fixed(mtau_pull_cod, 2, signed=True)}σ` / `{_fmt_fixed(mtau_pull_p24, 2, signed=True)}σ` PDG-24); $m_n$ (`-486 ppm`) open | "
            f"**Not at `1 ppQ`** (input floor `3.13e5 ppQ`) | {_group(cat1_pairs)} |"
        ),
        (
            f"| **1. Mass** (Nuclear Rest Mass $A \\ge 2$) | Symbolic Q-CLT `m_symbolic_MeV` vs AME2020 | `{len(nuclide_records)}` | "
            f"`{_fmt_fixed(_mean(all_m_rels) * HUNDRED, 3)}%` | `{_fmt_fixed(_median(all_m_rels) * HUNDRED, 3)}%` | "
            f"`{_fmt_ppq(_median(all_m_rels))}` | `0 / {len(nuclide_records)}` | `0 / {len(nuclide_records)}` | "
            f"**`~99.4%` bulk accuracy** (constituent $Z m_p + N m_n$); `~0.57%` residual from binding | "
            f"**Not at `1 ppQ`** (`~5.8e12 ppQ`) | Principled 1D Q-CLT proxy |"
        ),
        (
            f"| **2. Binding Energy** ($A = 2\\text{{--}}4$ & $A \\ge 2$) | 3D $K_A$ plaquette ($A \\le 4$) & 1D Q-CLT ($A \\ge 2$) | "
            f"`4` ($K_A$) / `{len(nuclide_records)}` (Q-CLT) | `7.13%` ($K_A$) / `{_fmt_fixed(_mean(all_b_rels) * HUNDRED, 1)}%` (Q-CLT) | "
            f"`4.96%` ($K_A$) / `{_fmt_fixed(_median(all_b_rels) * HUNDRED, 1)}%` (Q-CLT) | `3.65e+13` ($K_4$) to `{_fmt_ppq(_median(all_b_rels))}` | "
            f"`0 / {len(nuclide_records)}` | `0 / {len(nuclide_records)}` | "
            f"**Few-body $K_4$ (selected cell)** (`+1.8%` ${{}}^2\\mathrm{{H}}$, `+3.65%` ${{}}^4\\mathrm{{He}}$); **$A \\ge 5$ underbound `~69%`** | "
            f"**Not at `1 ppQ`** | {_status('ka_rows')} ($K_A$, $A \\le 4$: grid cell nearest AME, Table 3.2a note); Open saturation ($A \\ge 5$) |"
        ),
        (
            f"| **3. Charge, $\\alpha_{{\\mathrm{{EM}}}}$, $R_\\infty$ & Geometry** | $Q$, $\\alpha_{{\\mathrm{{EM}}}}^{{-1}}$ (Form B/C & Seifert), $R_\\infty h c$, Coulomb (`8`), VSEPR (`7`) | `22` | "
            f"`0` ($Q$), `-0.365 ppb` (Form B) / `-0.024 ppb` (Form C), `+0.725 ppb` ($R_\\infty$) | `0.20%` (across non-exact) | "
            f"`0` ($Q$), `{_fmt_ppq(alpha_fc_ppb / TEN_9)}` (Form C), `{_fmt_ppq(alpha_fb_ppb / TEN_9)}` (Form B) | "
            f"`{3 + mol_1s} / 22` ($Q$, Form C $\\alpha_{{\\mathrm{{EM}}}}$, Form C $R_\\infty$, $\\mathrm{{CH_4, CO_2}}$) | `{5 + mol_3s} / 22` (+ Form B $\\alpha_{{\\mathrm{{EM}}}} \\& R_\\infty$) | "
            f"**Exact** $Q$; **proved 4-topo Form B** (`-2.38σ`), **cond. Form C** (`-0.16σ`), **Seifert CS** (`-24.5 ppb`), **$R_\\infty$** (`+0.725 ppb`) | "
            f"$Q$ exact (`0 ppQ`); Form B `3.65e5 ppQ`, Form C `2.41e4 ppQ` | {_group(cat3_pairs)}; 1-loop $h_A^2$ factor proved |"
        ),
        (
            f"| **4. Weak $\\beta$-Decay & $v_{{\\mathrm{{weak}}}}$** | $v_{{\\mathrm{{weak}}}}$ ($N_v$), free $n$, `6` TM skein, `{len(beta_records) - 1}` composite $\\beta^-$ | `{len(beta_records) + 1}` | "
            f"`{_fmt_fixed(vew_ppb, 2, signed=True)} ppb` ($v_{{\\mathrm{{weak}}}}$), `-58.4%` ($n$), `{_fmt_fixed(_mean(all_beta_rels) * HUNDRED, 1)}%` (table) | "
            f"`71.7%` (TM), `{_fmt_fixed(_median(all_beta_rels) * HUNDRED, 1)}%` (table) | `2.94e+07` ($v_{{\\mathrm{{weak}}}}$) to `{_fmt_ppq(_median(all_beta_rels))}` | "
            f"`1 / {len(beta_records) + 1}` ($v_{{\\mathrm{{weak}}}}$, `-0.11σ`) | `1 / {len(beta_records) + 1}` ($v_{{\\mathrm{{weak}}}}$) | "
            f"**Sub-`30 ppb` $v_{{\\mathrm{{weak}}}}$ (`-0.11σ`)**; keV–MeV TM (`-8.1%` ${{}}^{{14}}\\mathrm{{C}}$); isobaric table (`{sum(1 for x in beta_records if x["exo"] and x["A"] > 1)}/{len(beta_records)-1}` exo.) | "
            f"**Not at `1 ppQ`** (`2.94e7 ppQ` on $v_{{\\mathrm{{weak}}}}$) | Cond. ($v_{{\\mathrm{{weak}}}}$, `C1–C3` on $n$); Open ($A \\ge 2$) |"
        ),
        (
            f"| **5. $\\alpha$-Decay & Fission** | `7` WKB emitters ($Q_{{\\mathrm{{exp}}}}$), $N=126$ ${{}}^{{210}}\\mathrm{{Po}}$, `{len(alpha_records)}` derived $Q_\\alpha$ | `{len(alpha_records)}` (+7 WKB) | "
            f"`{_fmt_fixed(_mean(dex_open), 2)} dex` (WKB @ $Q_{{\\mathrm{{exp}}}}$); `{_fmt_fixed(_mean(all_alpha_rels) * HUNDRED, 1)}%` ($Q_\\alpha$) | "
            f"`{_fmt_fixed(_median(dex_open), 2)} dex` (`+0.044 dex` ${{}}^{{210}}\\mathrm{{Po}}$ MJ); `{_fmt_fixed(_median(all_alpha_rels) * HUNDRED, 1)}%` ($Q_\\alpha$) | `{_fmt_ppq(_median(all_alpha_rels))}` | "
            f"`0 / {len(alpha_records)}` | `0 / {len(alpha_records)}` | "
            f"**Strong WKB + $N=126$ preformation** (`10.6%` $T_{{1/2}}$); **derived heavy $Q_\\alpha$ open** (`3–48 dex`) | "
            f"**Not at `1 ppQ`** | Derived WKB/MJ; Open heavy $Q_\\alpha$ |"
        ),
    ]
    _exec_derived = [
        _derived_within(cat1_pairs, 6),
        f"`0 / {len(nuclide_records)}`",
        f"`0 / {len(nuclide_records)}`",
        _derived_within(cat3_pairs, 22),
        _derived_within(cat4_pairs, len(beta_records) + 1),
        f"`0 / {len(alpha_records)}`",
    ]
    exec_rows = [row + f" {cell} |" for row, cell in zip(exec_rows, _exec_derived, strict=True)]

    # ── Section 5.3: Deterministic Witness Provenance Rows ────────────────────
    prov_rows: list[str] = []
    for rel, sections in UPSTREAM_SPECS:
        obj = loaded[rel]
        if "allPassed" in obj:
            g_status = "`allPassed: true`"
        elif rel.endswith("ame2020.json"):
            g_status = f"Reference dataset (`{len(obj['entries'])}` entries)"
        else:
            g_status = "Audit witness (`verified`)"
        prov_rows.append(f"| [`{rel}`]({rel}) | `{hashes[rel]}` | {g_status} | {sections} |")

    replacements: dict[str, str] = {
        "CALIBRATION_BASELINE_ROWS": "\n".join(calib_rows),
        "Q0_FLOOR_PPQ": _fmt_fixed(q0_ppq, 1),
        "Q0_FLOOR_PPB": _fmt_fixed(q0_ppb, 6),
        "ME_FLOOR_PPQ": _fmt_sci(me_ppq, 4),
        "ME_FLOOR_PPB": _fmt_fixed(me_ppb, 4),
        "NUCLIDE_SIGMA_MIN_PPB": _fmt_fixed(nuc_sig_min, 3),
        "NUCLIDE_SIGMA_MAX_PPB": _fmt_fixed(nuc_sig_max, 3),
        "ALPHA_EXP_PPQ": _fmt_sci(alpha_exp_ppq, 4),
        "ALPHA_EXP_PPB": _fmt_fixed(alpha_exp_ppb, 4),
        "ALPHA_FORMB_ABS_PPQ": _fmt_sci(alpha_fb_ppq, 3),
        "ALPHA_FORMB_REL_PPB": _fmt_fixed(alpha_fb_ppb, 3, signed=True),
        "ALPHA_FORMB_PULL": _fmt_fixed(alpha_fb_pull, 2, signed=True),
        "ALPHA_FORMC_ABS_PPQ": _fmt_sci(alpha_fc_ppq, 3),
        "ALPHA_FORMC_REL_PPB": _fmt_fixed(alpha_fc_ppb, 3, signed=True),
        "ALPHA_FORMC_PULL": _fmt_fixed(alpha_fc_pull, 2, signed=True),
        "ALPHA_SEIFERT_REL_PPB": _fmt_fixed(alpha_seif_ppb, 2, signed=True),
        "RY_FORMB_REL_PPB": _fmt_fixed(ry_fb_ppb, 3, signed=True),
        "RY_FORMB_ZCOMB": _fmt_fixed(ry_fb_zcomb, 2, signed=True),
        "RY_FORMC_REL_PPB": _fmt_fixed(ry_fc_ppb, 3, signed=True),
        "RY_FORMC_ZCOMB": _fmt_fixed(ry_fc_zcomb, 2, signed=True),
        "EXECUTIVE_SCORECARD_ROWS": "\n".join(exec_rows),
        "ELEMENTARY_MASS_ROWS": "\n".join(elem_rows),
        "MK_MPI_REL_PPB": _fmt_fixed(_m(obs["mk_over_mpi"]["rel_ppb"]), 3, signed=True),
        "MK_MPI_PULL": _fmt_fixed(_m(obs["mk_over_mpi"]["pull_exp"]), 4, signed=True),
        "MMU_REL_PPB": _fmt_fixed(_m(obs["m_mu_MeV"]["rel_ppb"]), 2, signed=True),
        "MMU_PULL": _fmt_fixed(_m(obs["m_mu_MeV"]["pull_exp"]), 2, signed=True),
        "DQ_MU_P_PPB": _fmt_fixed(_m(anc["dq_muon_minus_proton_ppb"]), 2, signed=True),
        "MTAU_ME_PRED": _fmt_fixed(mtau_pred, 4),
        "MTAU_CODATA_PPM": _fmt_fixed(mtau_rel_cod * TEN_6, 2, signed=True),
        "MTAU_CODATA_PULL": _fmt_fixed(mtau_pull_cod, 2, signed=True),
        "MTAU_PDG24_PPM": _fmt_fixed(mtau_rel_p24 * TEN_6, 2, signed=True),
        "MTAU_PDG24_PULL": _fmt_fixed(mtau_pull_p24, 2, signed=True),
        "MN_REL_PPM": _fmt_fixed(_m(obs["m_n_MeV"]["rel_ppb"]) / TEN_3, 1, signed=True),
        "N_MEAS_NUCLIDES": f"{len(nuclide_records):,}",
        "NUCLEAR_MASS_BAND_ROWS": "\n".join(mass_band_rows),
        "REPRESENTATIVE_NUCLIDE_ROWS": "\n".join(rep_rows),
        "FEWBODY_BINDING_ROWS": "\n".join(fewbody_rows),
        "BINDING_BAND_ROWS": "\n".join(binding_band_rows),
        "M3A_B4_B2": _fmt_fixed(_m(m3a["scaling_ratios_exact_vs_A2"]["A4_over_A2"]), 3),
        "M3A_B4_MEV": _fmt_fixed(b4_m3a, 3),
        "CHARGE_EM_ROWS": "\n".join(charge_rows),
        "MOLECULAR_ROWS": "\n".join(mol_rows),
        "ALPHA_CS_REL_PPB": _fmt_fixed(alpha_cs_ppb, 2, signed=True),
        "TANH_LN_Q0": _fmt_fixed(tanh_ln_q0, 6),
        "COULOMB_3H3HE_COVERED_PCT": _fmt_fixed(coul_frac * HUNDRED, 1),
        "MIRROR_MEAN_RATIO": _fmt_fixed(mirror_mean, 4),
        "MIRROR_RMS_PCT": _fmt_fixed(mirror_rms * HUNDRED, 2),
        "BETA_BENCHMARK_ROWS": "\n".join(beta_bench_rows),
        "N_BETA_TOTAL": f"{len(beta_records):,}",
        "N_BETA_COMPOSITE": f"{len(beta_records) - 1:,}",
        "N_BETA_COMPOSITE_EXO": f"{sum(1 for x in beta_records if x['exo'] and x['A'] > 1):,}",
        "BETA_BAND_ROWS": "\n".join(beta_band_rows),
        "QBETA_BASE_MEV": _fmt_fixed(qbeta_base, 6),
        "NV_CROSSING": f"{int(nint(nv_crossing)):,}",
        "NV_PRED_6": _fmt_fixed(nv_pred, 6),
        "VEW_PRED_6": _fmt_fixed(vew_pred, 6),
        "VEW_REL_PPB": _fmt_fixed(vew_ppb, 2, signed=True),
        "VEW_PULL": _fmt_fixed(vew_pull, 2, signed=True),
        "ALPHA_GAMOW_ROWS": "\n".join(alpha_gamow_rows),
        "N_ALPHA_TOTAL": f"{len(alpha_records):,}",
        "ALPHA_DERIVED_ROWS": "\n".join(alpha_derived_rows),
        "N_TOTAL_ISOTOPES": f"{int(mt['summary']['total_isotopes']):,}",
        "WITNESS_PROVENANCE_ROWS": "\n".join(prov_rows),
    }

    rendered = tmpl
    for key, val in replacements.items():
        rendered = rendered.replace("{{" + key + "}}", val)

    unreplaced = re.findall(r"\{\{[A-Z0-9_]+\}\}", rendered)
    if unreplaced:
        errors.append(f"unreplaced template placeholders: {', '.join(sorted(set(unreplaced)))}")

    # ── Authors'-note accuracy dashboard (compact, PDF-width) ────────────────
    # Five columns, short cells, rendered from the values computed above.
    def _pct(frac: mpf, places: int = 1) -> str:
        return f"${_fmt_fixed(frac * HUNDRED, places, signed=True)}\\%$"

    def _rel(frac: mpf) -> str:
        aval = abs(frac)
        if aval < mpf("1e-6"):
            places = 2 if aval < mpf("1e-9") else 0
            return f"${_fmt_fixed(frac * TEN_9, places, signed=True)}$ ppb"
        if aval < mpf("1e-3"):
            return f"${_fmt_fixed(frac * TEN_6, 0, signed=True)}$ ppm"
        return _pct(frac)

    def _sig(pull: mpf) -> str:
        return f" (${_fmt_fixed(abs(pull), 1)}\\sigma$)"

    def _obs_row(label: str, key: str, places: int, status: str, with_pull: bool = True) -> str:
        o = obs[key]
        frac = _m(o["rel_ppb"]) / TEN_9
        pull = _sig(_m(o["pull_exp"])) if with_pull else ""
        return (
            f"| {label} | ${_fmt_fixed(_m(o['pred']), places)}$ | ${_fmt_fixed(_m(o['exp']), places)}$ | "
            f"{_rel(frac)}{pull} | {status} |"
        )

    def _bind_row(label: str, b_pred: mpf, b_ref: mpf, places: int, status: str) -> str:
        return (
            f"| {label} | ${_fmt_fixed(b_pred, places)}$ | ${_fmt_fixed(b_ref, places)}$ | "
            f"{_pct((b_pred - b_ref) / b_ref)} | {status} |"
        )

    b56_pred = _m(mt_by_zn[(26, 30)]["B_pred_MeV"])
    b56_ame = _m(ame_by_zn[(26, 30)]["binding_energy_total_keV"]) / TEN_3
    n_beta_comp = len(beta_records) - 1
    n_beta_comp_exo = sum(1 for x in beta_records if x["exo"] and x["A"] >= 2)
    beta_comp_med = _median([x["rel"] for x in beta_records if x["A"] >= 2])
    dash_rows = [
        _obs_row("Muon mass (MeV)", "m_mu_MeV", 7, _status("m_mu")),
        (
            f"| Tau-to-electron mass ratio | ${_fmt_fixed(mtau_pred, 2)}$ | ${_fmt_fixed(mtau_exp_cod, 2)}$ | "
            f"{_rel(mtau_rel_cod)}{_sig(mtau_pull_cod)} | {_status('m_tau_over_m_e')} |"
        ),
        _obs_row("Kaon-to-pion mass ratio", "mk_over_mpi", 7, _status("mk_over_mpi"), with_pull=False),
        _obs_row("Inverse fine-structure constant", "alpha_em_inv_form_b", 9, _status("alpha_form_b")),
        _obs_row("Electroweak scale (GeV)", "v_ew_GeV", 5, _status("v_weak")),
        _obs_row("Neutron mass (MeV)", "m_n_MeV", 4, _status("m_n"), with_pull=False),
        _obs_row("Neutron–proton mass difference (MeV)", "delta_m_np_MeV", 4, _status("delta_m_np"), with_pull=False),
        _obs_row("Neutron $\\beta$-decay $Q$-value (MeV)", "q_beta_base_MeV", 4, _status("q_beta_free_neutron"), with_pull=False),
        (
            f"| $\\beta^-$ decays of nuclei, exothermic | ${n_beta_comp_exo}$ of ${n_beta_comp}$ | "
            f"${n_beta_comp}$ of ${n_beta_comp}$ | median ${_fmt_fixed(beta_comp_med * HUNDRED, 0)}\\%$ in $Q$ | Open |"
        ),
        _bind_row("Deuteron binding (MeV)", b2_m3a, b2_ame, 3, _status("ka_rows")),
        _bind_row("Deuteron binding, ruled trace pipeline (MeV)", b2_gg, b2_ame, 5, _status("ruled_trace_2h")),
        _bind_row("Helium-4 binding (MeV)", b4_m3a, b4_ame, 2, _status("ka_rows")),
        _bind_row("Iron-56 binding (MeV)", b56_pred, b56_ame, 1, "Open"),
        (
            f"| Binding, all ${len(nuclide_records)}$ nuclides with $A \\ge 2$ | chain proxy | AME2020 | "
            f"median ${_fmt_fixed(_median(all_b_rels) * HUNDRED, 0)}\\%$ low | Open |"
        ),
    ]
    dash_replacements: dict[str, str] = {
        "DASHBOARD_ROWS": "\n".join(dash_rows),
        "BINDING_MEDIAN_PCT": _fmt_fixed(_median(all_b_rels) * HUNDRED, 0),
    }
    dashboard = dash_tmpl
    for key, val in dash_replacements.items():
        dashboard = dashboard.replace("{{" + key + "}}", val)
    unreplaced_d = re.findall(r"\{\{[A-Z0-9_]+\}\}", dashboard)
    if unreplaced_d:
        errors.append(f"unreplaced dashboard placeholders: {', '.join(sorted(set(unreplaced_d)))}")

    return rendered, dashboard, errors


def dashboard_manifest() -> str:
    """The `.ts` manifest of the dashboard block (fixed; written alongside the `.md`)."""
    return (
        'import { prose } from "../../schema/builders";\n'
        "\n"
        "/**\n"
        " * GENERATED by scripts/generate-accuracy-scorecard.py --write from the\n"
        " * same 80-dps witness values as ACCURACY.md. Do not edit the .md by hand;\n"
        " * edit scripts/templates/accuracy-dashboard.md.tmpl or the generator.\n"
        " * `--check` fails when either file drifts from the render.\n"
        " */\n"
        "export default prose({\n"
        '  label: "prose:accuracy-dashboard",\n'
        '  title: "Accuracy dashboard",\n'
        "});\n"
    )


def check_hygiene(text: str, label: str = "ACCURACY.md") -> list[str]:
    errs: list[str] = []
    for name, pat in FORBIDDEN_PATTERNS:
        m = pat.search(text)
        if m:
            line_no = text[: m.start()].count("\n") + 1
            errs.append(f"{label}:{line_no}: forbidden {name} token `{m.group(0)}`")
    return errs


def check_readme_link(root: Path) -> list[str]:
    readme_path = root / README_REL
    if not readme_path.is_file():
        return [f"missing {README_REL}"]
    authored = _strip_folio_generated_blocks(readme_path.read_text(encoding="utf-8"))
    if not re.search(r"\]\(\.?/?ACCURACY\.md(?:#[^)]*)?\)", authored):
        return [f"{README_REL} does not contain an authored markdown link to `ACCURACY.md` outside `<!-- folio:* -->` blocks"]
    return []


def _inline_md_to_html(s: str) -> str:
    """Convert inline markdown + code + links (preserving $...$ for KaTeX) to HTML."""
    tokens: list[str] = []

    def _stash(fragment: str) -> str:
        idx = len(tokens)
        tokens.append(fragment)
        return f"\x00TOK{idx}\x00"

    # Stash inline code first
    s = re.sub(r"`([^`]+)`", lambda m: _stash(f"<code>{html.escape(m.group(1))}</code>"), s)
    # Stash display and inline math for KaTeX auto-render
    s = re.sub(r"\$\$(.+?)\$\$", lambda m: _stash(f"\\[{html.escape(m.group(1))}\\]"), s)
    s = re.sub(r"\$([^$]+)\$", lambda m: _stash(f"\\({html.escape(m.group(1))}\\)"), s)
    # Escape remaining HTML
    s = html.escape(s)
    # Links [label](href)
    def _link(m: re.Match[str]) -> str:
        lbl, href = m.group(1), m.group(2)
        if not href.startswith(("http://", "https://", "#", "/")):
            href = f"https://github.com/litlfred/qou/blob/main/{href}"
        return f'<a href="{href}">{lbl}</a>'

    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", _link, s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)

    for idx, frag in enumerate(tokens):
        s = s.replace(f"\x00TOK{idx}\x00", frag)
    return s


def markdown_to_standalone_html(md_text: str) -> str:
    """Render ACCURACY.md to a clean standalone HTML document without a <nav> element
    so `rail-standalone-pages.ts --foreign-site` injects the QOU navigation rail."""
    lines = md_text.splitlines()
    out: list[str] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        if stripped == "---":
            out.append("<hr>")
            i += 1
            continue
        if stripped.startswith("```"):
            lang = stripped[3:].strip()
            code_lines: list[str] = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(html.escape(lines[i]))
                i += 1
            i += 1
            cls = f' class="language-{html.escape(lang)}"' if lang else ""
            out.append(f"<pre><code{cls}>" + "\n".join(code_lines) + "</code></pre>")
            continue
        m_head = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m_head:
            lvl = len(m_head.group(1))
            title_raw = m_head.group(2)
            slug = re.sub(r"[^a-z0-9]+", "-", title_raw.lower()).strip("-")
            out.append(f'<h{lvl} id="{slug}">{_inline_md_to_html(title_raw)}</h{lvl}>')
            i += 1
            continue
        if stripped.startswith("|") and i + 1 < n and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            headers = [c.strip() for c in stripped.strip("|").split("|")]
            aligns_raw = [c.strip() for c in lines[i + 1].strip().strip("|").split("|")]
            aligns = [
                "right" if a.endswith(":") and not a.startswith(":")
                else "center" if a.startswith(":") and a.endswith(":")
                else "left"
                for a in aligns_raw
            ]
            i += 2
            out.append('<div class="table-wrap"><table><thead><tr>')
            for col_i, h_cell in enumerate(headers):
                al = aligns[col_i] if col_i < len(aligns) else "left"
                out.append(f'<th style="text-align:{al}">{_inline_md_to_html(h_cell)}</th>')
            out.append("</tr></thead><tbody>")
            while i < n and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                out.append("<tr>")
                for col_i, c_val in enumerate(cells):
                    al = aligns[col_i] if col_i < len(aligns) else "left"
                    out.append(f'<td style="text-align:{al}">{_inline_md_to_html(c_val)}</td>')
                out.append("</tr>")
                i += 1
            out.append("</tbody></table></div>")
            continue
        if stripped.startswith("- ") or re.match(r"^\d+\.\s+", stripped):
            is_ol = bool(re.match(r"^\d+\.\s+", stripped))
            tag = "ol" if is_ol else "ul"
            out.append(f"<{tag}>")
            while i < n:
                cur = lines[i].strip()
                if is_ol and re.match(r"^\d+\.\s+", cur):
                    item_txt = re.sub(r"^\d+\.\s+", "", cur)
                elif not is_ol and cur.startswith("- "):
                    item_txt = cur[2:]
                else:
                    break
                out.append(f"<li>{_inline_md_to_html(item_txt)}</li>")
                i += 1
            out.append(f"</{tag}>")
            continue
        if stripped.startswith("$$") and stripped.endswith("$$") and len(stripped) > 4:
            out.append(f'<div class="math-display">\\[{html.escape(stripped[2:-2])}\\]</div>')
            i += 1
            continue
        para: list[str] = []
        while i < n and lines[i].strip() and not lines[i].strip().startswith(("#", "|", "- ", "```", "---")):
            if re.match(r"^\d+\.\s+", lines[i].strip()):
                break
            para.append(lines[i].strip())
            i += 1
        out.append(f"<p>{_inline_md_to_html(' '.join(para))}</p>")

    body_html = "\n".join(out)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Observational Accuracy &amp; Precision Scorecard — Quantum Observable Universe</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" crossorigin="anonymous">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" crossorigin="anonymous"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" crossorigin="anonymous"
    onload="renderMathInElement(document.body,{{delimiters:[{{left:'\\\\[',right:'\\\\]',display:true}},{{left:'\\\\(',right:'\\\\)',display:false}}]}});"></script>
  <style>
    :root {{
      --bg: #ffffff; --fg: #1b1f24; --muted: #57606a; --border: #d0d7de;
      --surface: #f6f8fa; --accent: #0969da;
    }}
    @media (prefers-color-scheme: dark) {{
      :root {{
        --bg: #0d1117; --fg: #e6edf3; --muted: #8b949e; --border: #30363d;
        --surface: #161b22; --accent: #58a6ff;
      }}
    }}
    body {{
      margin: 0; background: var(--bg); color: var(--fg);
      font: 15px/1.6 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}
    main.qou-scorecard {{ max-width: 1240px; margin: 0 auto; padding: 2rem 1.25rem 4rem; }}
    h1, h2, h3, h4 {{ line-height: 1.25; margin-top: 2rem; margin-bottom: 0.75rem; }}
    h1 {{ font-size: 1.9rem; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; margin-top: 0.5rem; }}
    h2 {{ font-size: 1.4rem; border-bottom: 1px solid var(--border); padding-bottom: 0.35rem; }}
    h3 {{ font-size: 1.15rem; }}
    h4 {{ font-size: 1.0rem; color: var(--muted); }}
    a {{ color: var(--accent); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    code {{ font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 0.88em; background: var(--surface); padding: 0.12em 0.35em; border-radius: 4px; }}
    pre {{ background: var(--surface); padding: 0.9rem 1rem; border-radius: 6px; overflow-x: auto; border: 1px solid var(--border); }}
    pre code {{ background: none; padding: 0; }}
    hr {{ border: 0; border-top: 1px solid var(--border); margin: 2rem 0; }}
    .table-wrap {{ overflow-x: auto; margin: 1rem 0 1.5rem; border: 1px solid var(--border); border-radius: 6px; }}
    table {{ border-collapse: collapse; width: 100%; font-size: 0.88rem; }}
    th, td {{ padding: 0.45rem 0.65rem; border-bottom: 1px solid var(--border); vertical-align: top; }}
    th {{ background: var(--surface); font-weight: 600; white-space: nowrap; }}
    tr:last-child td {{ border-bottom: 0; }}
    .math-display {{ margin: 1rem 0; overflow-x: auto; }}
  </style>
</head>
<body>
<main class="qou-scorecard">
{body_html}
</main>
</body>
</html>
"""


def run_check(root: Path, qa_report: bool = False, html_out: Path | None = None) -> int:
    t0_ns = time.monotonic_ns()
    rendered, dashboard, errors = render_all(root)
    if rendered:
        errors.extend(check_hygiene(rendered, ACCURACY_REL))
        errors.extend(check_hygiene(dashboard, DASHBOARD_MD_REL))
        acc_path = root / ACCURACY_REL
        if not acc_path.is_file():
            errors.append(f"{ACCURACY_REL} does not exist on disk (run `--write`)")
        elif acc_path.read_text(encoding="utf-8") != rendered:
            errors.append(f"{ACCURACY_REL} is out of date with upstream witnesses/template (run `python3 scripts/generate-accuracy-scorecard.py --write`)")
        for rel, want in ((DASHBOARD_MD_REL, dashboard), (DASHBOARD_TS_REL, dashboard_manifest())):
            p = root / rel
            if not p.is_file():
                errors.append(f"{rel} does not exist on disk (run `--write`)")
            elif p.read_text(encoding="utf-8") != want:
                errors.append(f"{rel} is out of date with upstream witnesses/template (run `python3 scripts/generate-accuracy-scorecard.py --write`)")
        if html_out is not None and not errors:
            html_doc = markdown_to_standalone_html(rendered)
            errors.extend(check_hygiene(html_doc, str(html_out)))
            if not errors:
                html_out.parent.mkdir(parents=True, exist_ok=True)
                html_out.write_text(html_doc, encoding="utf-8")
    errors.extend(check_readme_link(root))
    stale_errors, stale_warnings = check_consumed_witness_staleness(root)
    errors.extend(stale_errors)
    for w in stale_warnings:
        print(f"WARN accuracy-scorecard: {w}", file=sys.stderr)

    elapsed_ms = (time.monotonic_ns() - t0_ns) // 1_000_000
    seconds_dec = f"{elapsed_ms // 1000}.{(elapsed_ms % 1000) // 100}"

    if errors:
        msg = "\n".join(["FAIL accuracy-scorecard:"] + [f"  - {e}" for e in errors])
        print(msg, file=sys.stderr)
        verdict = "fail"
        reason = errors[0]
        code = 1
    else:
        msg = (
            f"PASS accuracy-scorecard: {ACCURACY_REL} and the accuracy-dashboard block byte-identical to 80-dps render "
            f"({len(UPSTREAM_SPECS)} upstream inputs verified, 0 hygiene leaks, {README_REL} linked, {seconds_dec}s)"
        )
        print(msg)
        verdict = "pass"
        reason = ""
        code = 0

    if qa_report:
        qa_path = root / QA_OUT_REL
        qa_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "$schema": "qou-compute-qa/v1",
            "gate": "accuracy-scorecard",
            "node": "Task_Staleness",
            "title": "Observational accuracy scorecard drift & witness gate",
            "verdict": verdict,
            "reason": reason,
            "mode": "strict",
            "exit_codes": [code],
            "seconds": json.loads(seconds_dec),
            "output_sha256": hashlib.sha256((msg + "\n").encode("utf-8")).hexdigest(),
            "output_head": "\n".join(msg.splitlines()[:14]),
            # The verdict in the shared QA vocabulary, as scripts/compute-qa.py writes it.
            "counts": {verdict: 1},
        }
        qa_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    return code


def run_selftest() -> int:
    """Verify `--check` passes on a valid fixture and fails on all 4 defect classes."""
    rendered, dashboard, errs = render_all(REPO_ROOT)
    if errs:
        print("SELFTEST FAIL: live repository failed render_all: " + "; ".join(errs), file=sys.stderr)
        return 1

    with tempfile.TemporaryDirectory() as td_raw:
        td = Path(td_raw).resolve()
        # Symlink upstream witnesses and copy mutable files
        for rel, _ in UPSTREAM_SPECS:
            dst = td / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.symlink_to(REPO_ROOT / rel)
        tmpl_dst = td / TEMPLATE_REL
        tmpl_dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO_ROOT / TEMPLATE_REL, tmpl_dst)
        shutil.copy2(REPO_ROOT / DASHBOARD_TEMPLATE_REL, td / DASHBOARD_TEMPLATE_REL)
        (td / ACCURACY_REL).write_text(rendered, encoding="utf-8")
        dash_md = td / DASHBOARD_MD_REL
        dash_md.parent.mkdir(parents=True, exist_ok=True)
        dash_md.write_text(dashboard, encoding="utf-8")
        (td / DASHBOARD_TS_REL).write_text(dashboard_manifest(), encoding="utf-8")
        (td / README_REL).write_text(
            "# QOU\n\n| **Observational scorecard** | [ACCURACY.md](ACCURACY.md) |\n",
            encoding="utf-8",
        )

        # 1. Clean baseline must pass
        if run_check(td) != 0:
            print("SELFTEST FAIL: clean fixture did not pass", file=sys.stderr)
            return 1

        # 2. Stale ACCURACY.md must fail
        (td / ACCURACY_REL).write_text(rendered + "\n<!-- drift -->\n", encoding="utf-8")
        if run_check(td) == 0:
            print("SELFTEST FAIL: drifted ACCURACY.md was not caught", file=sys.stderr)
            return 1
        (td / ACCURACY_REL).write_text(rendered, encoding="utf-8")

        # 2b. Drifted accuracy-dashboard content block must fail
        dash_md.write_text(dashboard.replace("|", "| ", 1), encoding="utf-8")
        if run_check(td) == 0:
            print("SELFTEST FAIL: drifted accuracy-dashboard block was not caught", file=sys.stderr)
            return 1
        dash_md.write_text(dashboard, encoding="utf-8")

        # 3. Forbidden internal token in template+render must fail
        bad_tok = "Conven" + "tion C"
        tmpl_orig = tmpl_dst.read_text(encoding="utf-8")
        tmpl_dst.write_text(tmpl_orig + f"\n<!-- {bad_tok} -->\n", encoding="utf-8")
        bad_render, _ = render_scorecard(td)
        (td / ACCURACY_REL).write_text(bad_render, encoding="utf-8")
        if run_check(td) == 0:
            print("SELFTEST FAIL: forbidden convention token was not caught", file=sys.stderr)
            return 1
        tmpl_dst.write_text(tmpl_orig, encoding="utf-8")
        (td / ACCURACY_REL).write_text(rendered, encoding="utf-8")

        # 4. Missing or folio-generated-only README link must fail
        (td / README_REL).write_text(
            "# QOU\n<!-- folio:toc:begin -->\n[ACCURACY.md](ACCURACY.md)\n<!-- folio:toc:end -->\n",
            encoding="utf-8",
        )
        if run_check(td) == 0:
            print("SELFTEST FAIL: missing authored README link was not caught", file=sys.stderr)
            return 1
        (td / README_REL).write_text(
            "# QOU\n\n| **Observational scorecard** | [ACCURACY.md](ACCURACY.md) |\n",
            encoding="utf-8",
        )

        # 5. Upstream witness with allPassed=False must fail
        w_rel = "computations/u1-hypercharge-assignment.witness.json"
        w_dst = td / w_rel
        w_dst.unlink()
        w_obj = json.loads((REPO_ROOT / w_rel).read_text(encoding="utf-8"))
        w_obj["allPassed"] = False
        w_dst.write_text(json.dumps(w_obj), encoding="utf-8")
        if run_check(td) == 0:
            print("SELFTEST FAIL: `allPassed: false` witness was not caught", file=sys.stderr)
            return 1

    print("SELFTEST PASS: clean fixture + 5 defect classes (scorecard drift, dashboard drift, hygiene, README link, witness failure) verified.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate, redisplay, or QA-gate ACCURACY.md at 80-dps.")
    ap.add_argument("--write", action="store_true", help="Render and write ACCURACY.md at repository root")
    ap.add_argument("--print", dest="do_print", action="store_true", help="Print rendered ACCURACY.md markdown to stdout")
    ap.add_argument("--check", action="store_true", help="Run strict QA gate (witnesses, byte-identity, hygiene, README link)")
    ap.add_argument("--qa-report", action="store_true", help="Write qou-compute-qa/v1 report to test/results/compute-qa/accuracy-scorecard.json")
    ap.add_argument("--html-out", default=None, help="Write standalone HTML scorecard page to the given path (e.g. _site/accuracy/index.html)")
    ap.add_argument("--self-test", action="store_true", help="Run negative-control self-tests on the QA detector")
    args = ap.parse_args()

    if args.self_test:
        return run_selftest()

    if not (args.write or args.do_print or args.check or args.html_out):
        ap.error("specify at least one of --write, --print, --check, --html-out, or --self-test")

    html_path = Path(args.html_out) if args.html_out else None

    if args.write or args.do_print or (html_path is not None and not args.check):
        rendered, dashboard, errors = render_all(REPO_ROOT)
        if errors:
            for e in errors:
                print(f"ERROR: {e}", file=sys.stderr)
            return 1
        hyg = check_hygiene(rendered, ACCURACY_REL) + check_hygiene(dashboard, DASHBOARD_MD_REL)
        if hyg:
            for e in hyg:
                print(f"ERROR: {e}", file=sys.stderr)
            return 1
        if args.write:
            out_path = REPO_ROOT / ACCURACY_REL
            out_path.write_text(rendered, encoding="utf-8")
            print(f"wrote {ACCURACY_REL} ({len(rendered.splitlines())} lines, {len(rendered)} bytes)")
            (REPO_ROOT / DASHBOARD_MD_REL).write_text(dashboard, encoding="utf-8")
            (REPO_ROOT / DASHBOARD_TS_REL).write_text(dashboard_manifest(), encoding="utf-8")
            print(f"wrote {DASHBOARD_MD_REL} and {DASHBOARD_TS_REL}")
        if html_path is not None and not args.check:
            html_doc = markdown_to_standalone_html(rendered)
            html_hyg = check_hygiene(html_doc, str(html_path))
            if html_hyg:
                for e in html_hyg:
                    print(f"ERROR: {e}", file=sys.stderr)
                return 1
            html_path.parent.mkdir(parents=True, exist_ok=True)
            html_path.write_text(html_doc, encoding="utf-8")
            print(f"wrote {html_path}")
        if args.do_print:
            sys.stdout.write(rendered)

    if args.check:
        return run_check(REPO_ROOT, qa_report=args.qa_report, html_out=html_path)

    return 0


if __name__ == "__main__":
    sys.exit(main())
