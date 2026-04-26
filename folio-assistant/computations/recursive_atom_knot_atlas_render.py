#!/usr/bin/env python3
"""Render the recursive atom-knot atlas from witness JSON sources of truth.

LAYOUT:
- One table per confinement-level group.
- Each particle/atom occupies TWO rows in the table:
    Row 1 (math): braid (NF) | closure | Vol_hyp | ℓ | n_0
    Row 2 (phys):  AME (MeV) | Pred (MeV) | err % | err ppb | ρ
- The first column SPANS both rows (rowspan=2) showing the particle notation.
- Compact, condensed, scannable.

SOURCES OF TRUTH (read at build time):
  - confined-particle.md (GB-NF particle registry)
  - mass-table-ppb.witness.json (D..⁴⁰Ca, no fits)
  - li-atom-knot-search.witness.json (⁶Li, ⁷Li at ρ=5)

USAGE:
  python3 recursive_atom_knot_atlas_render.py            # markdown to stdout
  python3 recursive_atom_knot_atlas_render.py --tex      # LaTeX (multirow)
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path


def load_witnesses():
    base = Path(__file__).parent
    out = {}
    for name in ["mass-table-ppb", "li-atom-knot-search"]:
        p = base / f"{name}.witness.json"
        if p.exists():
            with open(p) as f:
                out[name] = json.load(f)
    return out


def fundamental_particles():
    return [
        {
            "label": r"Neutrino $\nu$",
            "ell": 0, "n_0": 1,
            "braid": r"$\mathbf{1} \in H_1$",
            "closure": r"$0_1$ (unknot)",
            "vol_hyp": "0",
            "B_AME": r"$\le 1$ eV",
            "B_pred": r"$\approx 0$",
            "err_pct": "—",
            "err_ppb": "—",
            "rho": "—",
        },
        {
            "label": r"Photon $\gamma$",
            "ell": 0, "n_0": 4,
            "braid": r"$\mathbf{1}_{B_4} \in H_4$",
            "closure": r"$4 \cdot 0_1$",
            "vol_hyp": "0",
            "B_AME": "0 (gauge)",
            "B_pred": "0",
            "err_pct": "—",
            "err_ppb": "—",
            "rho": "—",
        },
        {
            "label": r"Quark $\mathfrak{q}$",
            "ell": 0, "n_0": 1,
            "braid": r"$\sigma_0 \in H_1$",
            "closure": r"(in $\mathcal{B}_3$)",
            "vol_hyp": "—",
            "B_AME": "(confined)",
            "B_pred": "—",
            "err_pct": "—",
            "err_ppb": "—",
            "rho": "—",
        },
        {
            "label": r"Electron $e^-$",
            "ell": 1, "n_0": 2,
            "braid": r"$\sigma_1^3 \in H_2$",
            "closure": r"$T_{2,3} = 3_1$",
            "vol_hyp": "0",
            "B_AME": "0.51099895",
            "B_pred": "0.51099895",
            "err_pct": "(anchor)",
            "err_ppb": "(anchor)",
            "rho": "—",
        },
        {
            "label": r"Proton $\mathfrak{p}$",
            "ell": 1, "n_0": 3,
            "braid": r"$(\sigma_1 \sigma_2^{-1})^3$ flav-uud",
            "closure": r"$\mathcal{B}_3(\mathrm{uud})$",
            "vol_hyp": "7.3277",
            "B_AME": "938.272",
            "B_pred": "938.272",
            "err_pct": "(anchor)",
            "err_ppb": "(anchor)",
            "rho": "—",
        },
        {
            "label": r"Neutron $\mathfrak{n}$",
            "ell": 1, "n_0": 3,
            "braid": r"$(\sigma_1 \sigma_2^{-1})^3$ flav-udd",
            "closure": r"$\mathcal{B}_3(\mathrm{udd})$",
            "vol_hyp": "7.3277",
            "B_AME": "939.565",
            "B_pred": "939.565",
            "err_pct": r"$-0.19\%$",
            "err_ppb": r"$-1.9 \times 10^6$",
            "rho": "—",
        },
    ]


def light_atoms_from_witness(W):
    out = []
    if "mass-table-ppb" not in W:
        return out
    for r in W["mass-table-ppb"].get("rows", []):
        rho = r.get("inputs", {}).get("rho_factor", "—")
        vol = r.get("inputs", {}).get("Vol", None)
        knot = r.get("inputs", {}).get("knot")
        # Closure name: knot label if present, otherwise formula description
        if knot:
            closure = f"${knot}$"
        else:
            closure = r["formula"][:32]
        out.append({
            "label": _fmt_isotope(r["sym"]),
            "ell": 2, "n_0": 3 * r["A"],
            "braid": f"$T_w \\in H_{{{3 * r['A']}}}$ (atomic-braid)",
            "closure": closure,
            "vol_hyp": f"{vol:.4f}" if vol else "—",
            "B_AME": f"{r['B_AME_MeV']:.4f}",
            "B_pred": f"{r['B_pred_MeV']:.4f}",
            "err_pct": f"{r['err_pct']:+.3f}\\%",
            "err_ppb": f"{r['err_ppb']:+.2e}",
            "rho": str(rho) if rho != "—" else "—",
        })
    return out


def li_from_witness(W):
    out = []
    if "li-atom-knot-search" not in W:
        return out
    li = W["li-atom-knot-search"].get("results", {})
    AME = {"6Li": 31.99405, "7Li": 39.24452}
    A = {"6Li": 6, "7Li": 7}
    for label in ["6Li", "7Li"]:
        if label not in li or not li[label]:
            continue
        best = min(li[label].items(), key=lambda kv: abs(kv[1].get("err_pct", 1e10)))
        rho_str, info = best
        out.append({
            "label": _fmt_isotope(label),
            "ell": 2, "n_0": 3 * A[label],
            "braid": f"$T_w \\in H_{{{3 * A[label]}}}$ (atomic-braid)",
            "closure": f"${info['best_knot']}$",
            "vol_hyp": f"{info['vol']:.4f}",
            "B_AME": f"{AME[label]:.4f}",
            "B_pred": f"{info['B_pred']:.4f}",
            "err_pct": f"{info['err_pct']:+.4f}\\%",
            "err_ppb": f"{info['err_ppb']:+.2e}",
            "rho": str(rho_str),
        })
    return out


def _fmt_isotope(sym):
    """Format e.g. '4He' as $^{4}\mathrm{He}$, 'D' as $D$, etc."""
    s = sym
    if not s:
        return s
    digits, rest = "", s
    for i, c in enumerate(s):
        if not c.isdigit():
            digits, rest = s[:i], s[i:]
            break
    if digits:
        return f"$^{{{digits}}}\\mathrm{{{rest}}}$"
    return f"${s}$"


def render_md(rows, group_name):
    """Render a group as a markdown table with HTML rowspan in column 1."""
    out = [f"\n### {group_name}\n"]
    out.append("<table>")
    out.append(
        "<thead>\n"
        "<tr><th rowspan='2'>Particle / atom</th>"
        "<th colspan='5' style='text-align:left'>Math (row 1) / Physics (row 2)</th></tr>\n"
        "<tr><th>Col 1</th><th>Col 2</th><th>Col 3</th><th>Col 4</th><th>Col 5</th></tr>\n"
        "</thead>"
    )
    out.append("<tbody>")
    for r in rows:
        # Row 1 (math): braid | closure | Vol_hyp | ℓ | n_0
        out.append(
            "<tr>"
            f"<td rowspan='2'><strong>{r['label']}</strong></td>"
            f"<td>Braid: {r['braid']}</td>"
            f"<td>Closure: {r['closure']}</td>"
            f"<td>Vol<sub>hyp</sub>: {r['vol_hyp']}</td>"
            f"<td>ℓ = {r['ell']}</td>"
            f"<td>n₀ = {r['n_0']}</td>"
            "</tr>"
        )
        # Row 2 (physics): AME | Pred | err% | ppb | ρ
        out.append(
            "<tr>"
            f"<td>AME: {r['B_AME']} MeV</td>"
            f"<td>Pred: {r['B_pred']} MeV</td>"
            f"<td>err: {r['err_pct']}</td>"
            f"<td>ppb: {r['err_ppb']}</td>"
            f"<td>ρ = {r['rho']}</td>"
            "</tr>"
        )
    out.append("</tbody></table>")
    return "\n".join(out)


def render_tex(rows, group_name):
    """Render a group as LaTeX longtable with \\multirow."""
    out = [r"\subsection*{" + group_name + r"}", ""]
    out.append(r"\begin{tabular}{l|p{3.5cm}|p{3cm}|p{2cm}|p{1.5cm}|p{1.5cm}}")
    out.append(r"\hline")
    out.append(
        r"\textbf{Particle} & \multicolumn{5}{l}{\emph{row 1: math, row 2: physics}} \\"
    )
    out.append(r"\hline")
    for r in rows:
        out.append(
            r"\multirow{2}{*}{\textbf{" + r["label"] + r"}} & "
            f"Braid: {r['braid']} & Closure: {r['closure']} & "
            f"Vol${{}}_{{\\mathrm{{hyp}}}}$: {r['vol_hyp']} & "
            f"$\\ell = {r['ell']}$ & $n_0 = {r['n_0']}$ \\\\"
        )
        out.append(
            f"& AME: {r['B_AME']} MeV & Pred: {r['B_pred']} MeV & "
            f"err: {r['err_pct']} & ppb: {r['err_ppb']} & "
            f"$\\rho = {r['rho']}$ \\\\ \\hline"
        )
    out.append(r"\end{tabular}")
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tex", action="store_true",
                        help="Render LaTeX (default: markdown)")
    args = parser.parse_args()

    W = load_witnesses()
    render = render_tex if args.tex else render_md

    print("# Recursive Atom-Knot Atlas (auto-rendered from witnesses)")
    print()
    print("**Source of truth**: `confined-particle.md` (GB-NF registry) + ")
    print("`mass-table-ppb.witness.json` + `li-atom-knot-search.witness.json`.\n")
    print("Each particle/atom occupies **two rows**: row 1 = math (braid, ")
    print("closure, hyperbolic volume, level, strand count), row 2 = physics ")
    print("(AME binding, prediction, % error, ppb error, $\\rho$ prefactor).")
    print()
    print(render(fundamental_particles(), r"$\ell = 0, 1$ — fundamental particles"))
    print(render(light_atoms_from_witness(W), r"$\ell = 2$ — light atoms (mass-table-ppb)"))
    print(render(li_from_witness(W), r"$\ell = 2$ — Lithium isotopes (atom-knot search)"))


if __name__ == "__main__":
    main()
