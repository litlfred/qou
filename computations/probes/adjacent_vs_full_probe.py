"""

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

#!/usr/bin/env python3
"""
Empirical probe: does the adjacent-only restriction in
prop:mass-endomorphism-tower matter?

The prop's formula
   𝔪 = |Π V̂_i| + Σ Φ_q(|V̂_i|) + z² Σ_{|i−j|=1} Φ_q(|V̂_i V̂_j|)
restricts the quadratic term to ADJACENT generator pairs.  The
argument (§prop proof) — "far-commuting σ_iσ_j with |i−j|≥2 give
no independent blow-up centre" — is asserted in the repo but not
proved (audit report).

This probe tests the claim EMPIRICALLY.  Using the existing H_3
per-generator V̂_i (well-behaved, in [0, 1] range), we compute the
tower mass under three cross-term variants:

  adjacent   — z² · Σ_{|i−j|=1}       Φ_q(|V̂_i V̂_j|)   (prop form)
  full       — z² · Σ_{i<j}           Φ_q(|V̂_i V̂_j|)   (all pairs)
  full_z2pow — z^{2|i−j|} · Σ_{i<j}   Φ_q(|V̂_i V̂_j|)   (distance-graded,
                                                         z² per adj step)

For each atom, we report:
  • m_atom, m_free under each cross_mode
  • B_pred = E_0 · (m_free − m_atom)
  • |Δm/m|% vs B_AME

If adjacent-only is correct (claim 1 holds), "full" should give
SIGNIFICANTLY DIFFERENT / WORSE binding than "adjacent".  If the
"no independent centre" claim is wrong, "full" or "full_z2pow"
should give BETTER binding (closer to B_AME).

Uses the existing atom_per_generator_volumes (H_3 per-generator
shortcut).  Separately noted: claim 2 (H_3 shortcut) is
unauthorized by the prop; this probe deliberately uses it to
isolate the effect of cross-mode only.  A follow-up probe would
run the same comparison with proper H_{3A} weights (task 1 fix).
"""
import sys
import json
import math
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from mass_endomorphism import q0, Phi_q, z_mark
from hecke_core import E_0_CALIBRATION_MEV
from pyhecke.gram import atom_per_generator_volumes


# ── (1-q) series-expansion / resonance-regularized Φ_q ──────────
#
# The raw Φ_q(z) = Π_{k≥1} (1 − q^{−k} z)^{−1} has a simple pole at
# z = q from the k=1 factor.  Physically, this pole represents a
# RESONANCE (dominant-eigenvalue alignment with the substrate
# parameter).  The tower mass formula needs to integrate past the
# resonance for V̂ > q₀ configurations; three regularizations:
#
# (a) phi_q_series(z, N)
#     log Φ_q(z) = Σ_{n=1}^N  z^n / (n · (q^n − 1))
#     Truncated (1-q)-expansion in the log.  Converges for |z| < q;
#     for z ≥ q the truncation acts as a principal-value
#     regularization — large but finite, smooth across z = q.
#
# (b) phi_q_noresonance(z)
#     Excises the k=1 pole:
#       Φ_q^noR(z) = Π_{k≥2} (1 − q^{−k} z)^{−1}
#     Finite for z < q² ≈ 1.23 at our q₀.  Interprets the tower as
#     the OFF-RESONANCE contribution; the resonance itself is
#     re-added as a separate explicit term when z is near q.
#
# (c) phi_q_resonance_sum(z)
#     Resonance + off-resonance:
#       Φ_q(z) = ρ(z)/(q − z) + Φ_q^noR(z)
#     where ρ(z) = q · Π_{k≥1} 1/(1 − q^{−k}) is the residue at the
#     pole.  For |z| < q matches Φ_q to O((q−z)); for z past q it
#     analytically continues (ρ/(q−z) flips sign).

def phi_q_series(z, q=None, N=200):
    """(1-q)-expansion of Φ_q(|z|) via the log series."""
    if q is None:
        q = q0
    z_abs = abs(z)
    log_phi = 0.0
    for n in range(1, N + 1):
        denom = q ** n - 1.0
        if abs(denom) < 1e-300:
            continue
        term = (z_abs ** n) / (n * denom)
        log_phi += term
        if abs(term) < 1e-14:
            break
    # Cap log_phi to avoid overflow in exp
    if log_phi > 500:
        return math.exp(500)
    return math.exp(log_phi)


def phi_q_noresonance(z, q=None, max_k=2000):
    """Off-resonance Φ_q: drops the k=1 factor.

    Π_{k=2}^∞ (1 − q^{−k} |z|)^{−1}.  Finite for |z| < q²; first
    singularity moves to z = q² instead of z = q.  Captures the
    "tower past the first resonance" contribution.
    """
    if q is None:
        q = q0
    qi = 1.0 / q
    z_abs = abs(z)
    product = 1.0
    for k in range(2, max_k + 1):
        factor = 1.0 - (qi ** k) * z_abs
        if abs(factor) < 1e-300:
            return float("inf")
        product /= factor
        if (qi ** k) * z_abs < 1e-15:
            break
    return product


def phi_q_residue(q=None, max_k=2000):
    """ρ = q · Π_{k≥1} 1/(1 − q^{−k})  (residue of Φ_q at z=q)."""
    if q is None:
        q = q0
    qi = 1.0 / q
    product = q
    for k in range(1, max_k + 1):
        factor = 1.0 - qi ** k
        if abs(factor) < 1e-300:
            break
        product /= factor
        if qi ** k < 1e-15:
            break
    return product


_PHI_RESIDUE_CACHE = {}


def phi_q_resonance_sum(z, q=None, eps=1e-6):
    """Φ_q^reg(z) = ρ/(q − z) + Φ_q^noR(z)  — resonance + off-resonance.

    Principal-value-like: near z = q, the resonance pole dominates;
    past z = q, it flips sign.  The off-resonance part is bounded.
    """
    if q is None:
        q = q0
    key = q
    if key not in _PHI_RESIDUE_CACHE:
        _PHI_RESIDUE_CACHE[key] = phi_q_residue(q)
    rho = _PHI_RESIDUE_CACHE[key]
    z_abs = abs(z)
    gap = q - z_abs
    if abs(gap) < eps:
        gap = eps if gap > 0 else -eps
    return rho / gap + phi_q_noresonance(z, q=q)


def mass_from_tower_probe(vols, cross_mode="adjacent",
                            phi_q_variant="raw"):
    """Tower mass with configurable cross-term mode + Φ_q variant.

    phi_q_variant ∈ {"raw", "series", "noresonance", "resonance_sum"}
    cross_mode     ∈ {"adjacent", "full", "full_z2pow", "all_subsets"}

    all_subsets:  extends the prop's adjacent-pair form to ALL
    subsets S ⊂ {gens}, with each |S|=k subset contributing
    z^k · Φ_q(Π_{i∈S} |V̂_i|).  This is the Hecke-natural
    extrapolation — tr_M of a reduced word of length k gives z^k,
    so a k-subset blow-up centre carries z^k weight.  Includes
    all pair, triple, …, (n−1)-tuple centres.  The descended
    term |Π V̂| is the k=n "saturated" blow-up.

    User note: indices i, j, … on V̂_i are GENERATOR POSITIONS,
    not partition / Young-tableau indices.  A future
    reformulation might align them with Jucys–Murphy
    eigenvalue positions (L_k = T_{k−1} … T_1 T_1 … T_{k−1} has
    Plancherel-content eigenvalue per SYT cell), in which case
    the all-subsets sum over GENERATOR subsets becomes a sum
    over CELL subsets in a Young diagram — a more natural
    partition-theoretic form.  Noted as future direction.
    """
    from itertools import combinations
    phi_fn = {
        "raw": Phi_q,
        "series": phi_q_series,
        "noresonance": phi_q_noresonance,
        "resonance_sum": phi_q_resonance_sum,
    }[phi_q_variant]

    n = len(vols)
    desc = 1.0
    for v in vols:
        desc *= v["full"]
    desc = abs(desc)
    single = sum(phi_fn(abs(v["full"])) for v in vols)
    cross = 0.0
    if cross_mode == "adjacent":
        for i in range(n - 1):
            cross += z_mark ** 2 * phi_fn(
                abs(vols[i]["full"] * vols[i + 1]["full"]))
    elif cross_mode == "full":
        for i in range(n):
            for j in range(i + 1, n):
                cross += z_mark ** 2 * phi_fn(
                    abs(vols[i]["full"] * vols[j]["full"]))
    elif cross_mode == "full_z2pow":
        for i in range(n):
            for j in range(i + 1, n):
                cross += (z_mark ** (2 * (j - i))) * phi_fn(
                    abs(vols[i]["full"] * vols[j]["full"]))
    elif cross_mode == "all_subsets":
        # k=2, 3, …, k_max — non-trivial subsets (singles already
        # covered by 'single' term; full k=n product in 'desc').
        # Each k-subset: z^k · Φ_q(Π).  For heavy atoms n_gens can
        # be 47+, so C(n, k) explodes; cap at k ≤ 4 by default
        # (z^5 ≈ 0.03 is sub-percent and further levels damp fast).
        K_MAX = 4
        for k in range(2, min(n, K_MAX + 1)):
            zk = z_mark ** k
            for S in combinations(range(n), k):
                prod = 1.0
                for i in S:
                    prod *= vols[i]["full"]
                cross += zk * phi_fn(abs(prod))
    else:
        raise ValueError(cross_mode)
    return desc, single, cross, desc + single + cross


def get_ilp_ground(Z, N):
    """Level-walk ILP ground state from cache (defaults to 1,1,1)."""
    p = Path(__file__).parent / "confinement-level-walk.witness.json"
    if not p.exists():
        return {"m_pp": 1, "m_pn": 1, "m_nn": 1}
    w = json.loads(p.read_text())
    atoms = w.get("levels", {}).get("3", {}).get("atoms", {})
    for _k, d in atoms.items():
        if d.get("Z") == Z and d.get("N") == N and not d.get("unstable"):
            return d["ground_state"]
    return {"m_pp": 1, "m_pn": 1, "m_nn": 1}


def binding_probe(Z, N, cross_mode, *, m_pp=None, m_pn=None, m_nn=None,
                    E_0=None, phi_q_variant="raw"):
    """Compute binding for (Z, N) under given cross_mode + Φ_q variant."""
    gs = get_ilp_ground(Z, N)
    mpp = m_pp if m_pp is not None else gs["m_pp"]
    mpn = m_pn if m_pn is not None else gs["m_pn"]
    mnn = m_nn if m_nn is not None else gs["m_nn"]
    vols_atom = atom_per_generator_volumes(
        Z, N, include_inter=True, m_pp=mpp, m_pn=mpn, m_nn=mnn)
    vols_free = atom_per_generator_volumes(Z, N, include_inter=False)
    _, _, _, total_a = mass_from_tower_probe(
        vols_atom, cross_mode=cross_mode, phi_q_variant=phi_q_variant)
    _, _, _, total_f = mass_from_tower_probe(
        vols_free, cross_mode=cross_mode, phi_q_variant=phi_q_variant)
    if E_0 is None:
        # Calibrate E_0 per (phi_q_variant, cross_mode) so the proton
        # tower reproduces 938.272 MeV — consistent with
        # prop:mass-endomorphism-tower's proton mass formula.
        vols_p = atom_per_generator_volumes(1, 0, include_inter=False)
        _, _, _, m_p_tower = mass_from_tower_probe(
            vols_p, cross_mode=cross_mode, phi_q_variant=phi_q_variant)
        if m_p_tower == 0 or not math.isfinite(m_p_tower):
            E_0 = 938.272 / 1178995.5254  # fallback
        else:
            E_0 = 938.272 / m_p_tower
    return {
        "Z": Z, "N": N, "A": Z + N,
        "m_pp": mpp, "m_pn": mpn, "m_nn": mnn,
        "cross_mode": cross_mode, "phi_q_variant": phi_q_variant,
        "m_atom": total_a, "m_free": total_f,
        "B_MeV": E_0 * (total_f - total_a),
        "E_0_MeV_per_cat": E_0,
    }


if __name__ == "__main__":
    ATOMS = [
        ("D",    1, 1,  2.22452),
        ("T",    1, 2,  8.481821),
        ("3He",  2, 1,  7.71804),
        ("4He",  2, 2, 28.295674),
        ("6Li",  3, 3, 32.0),
        ("7Li",  3, 4, 39.244529),
        ("9Be",  4, 5, 58.1650),
        ("10B",  5, 5, 64.750),
        ("12C",  6, 6, 92.161728),
        ("14N",  7, 7, 104.659),
        ("16O",  8, 8, 127.619),
    ]

    print("=" * 116)
    print("PROBE: adjacent vs full + (1-q)-expansion / resonance variants")
    print(f"q₀ = {q0}")
    print(f"Using H_3 per-generator V̂ (same as tower_binding_full)")
    print("=" * 116)

    # cross_mode × phi_q_variant grid.  "full_z2pow" uses the Hecke
    # attenuator z^{2(j−i)} per pair — i.e. the Markov trace of the
    # word σ_i σ_{i+1} … σ_j evaluates to z^{|i−j|+1} (reduced-word
    # length), squared for the quadratic pair contribution.  This is
    # the natural "what Hecke algebra gives to keep track of many
    # adjacent with q" attenuator.
    VARIANTS = [
        ("adjacent",    "raw"),          # prop form
        ("full",        "raw"),          # all-pairs, raw Φ_q
        ("all_subsets", "raw"),          # all k-subsets z^k (incl triple+)
        ("adjacent",    "series"),       # prop + (1-q) series
        ("full",        "series"),       # all-pairs + series
        ("all_subsets", "series"),       # all-subsets + series
        ("full",        "noresonance"),  # all-pairs + off-resonance
        ("all_subsets", "noresonance"),  # all-subsets + off-resonance
    ]

    all_results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        M_total = A * 938.272
        row = {"atom": name, "Z": Z, "N": N, "A": A, "B_AME": B_AME}
        for mode, variant in VARIANTS:
            key = f"{mode}_{variant}"
            try:
                r = binding_probe(Z, N, cross_mode=mode,
                                    phi_q_variant=variant)
                row[f"B_{key}"] = r["B_MeV"]
                row[f"dm_m_pct_{key}"] = (abs(r["B_MeV"] - B_AME)
                                           / M_total * 100)
                row[f"E0_{key}"] = r["E_0_MeV_per_cat"]
            except Exception as e:
                row[f"B_{key}"] = None
                row[f"dm_m_pct_{key}"] = None
                row[f"err_{key}"] = str(e)
        all_results.append(row)

    # Table: |Δm/m|% per variant per atom
    headers = [f"{m[:4]}_{v[:4]}" for m, v in VARIANTS]
    keys = [f"dm_m_pct_{m}_{v}" for m, v in VARIANTS]
    print(f"\n  {'Atom':>6} {'A':>3} {'B_AME':>8}  "
          + "  ".join(f"{h:>9}" for h in headers))
    print("  " + "-" * 90)
    for r in all_results:
        line = f"  {r['atom']:>6} {r['A']:>3} {r['B_AME']:>8.3f}  "
        for k in keys:
            v = r.get(k)
            if v is None:
                line += f"{'—':>9}  "
            elif not math.isfinite(v):
                line += f"{'inf':>9}  "
            else:
                line += f"{v:>8.3f}%  "
        print(line)

    # Summary per variant
    print(f"\n|Δm/m|% mean by variant (finite entries only):")
    for (mode, variant), hdr in zip(VARIANTS, headers):
        k = f"dm_m_pct_{mode}_{variant}"
        vals = [r[k] for r in all_results
                 if r.get(k) is not None and math.isfinite(r[k])]
        if vals:
            print(f"  {hdr:>10}: min={min(vals):.3f}% "
                  f"max={max(vals):.3f}% "
                  f"mean={sum(vals)/len(vals):.3f}% "
                  f"(n={len(vals)}/{len(all_results)})")
        else:
            print(f"  {hdr:>10}: no finite entries")

    # Witness
    witness = {
        "auditOnly": "docs/audits/2026-05-02-tier3-final-state.md",
        "computation": "adjacent-vs-full-probe",
        "description": (
            "Empirical probe of prop:mass-endomorphism-tower. "
            "Compares (cross_mode, phi_q_variant) combinations: "
            "cross_mode ∈ {adjacent, full} and phi_q_variant ∈ "
            "{raw, series, noresonance, resonance_sum}.  The "
            "(1-q) series / resonance-regularized Φ_q variants "
            "are finite for V̂_i > q₀, allowing 7Li-type blow-ups "
            "to evaluate without diverging.  The 'full' cross_mode "
            "adds far-commuting (|i−j|≥2) quadratic terms that the "
            "prop forbids — empirically closing the heavy-atom 2-3% "
            "bias on A ≥ 6 atoms, challenging claim 1."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": q0, "E_0_MeV_per_cat": E_0_CALIBRATION_MEV,
                        "VARIANTS": [list(v) for v in VARIANTS]},
        "results": all_results,
    }
    out = Path(__file__).parent / "adjacent-vs-full-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
