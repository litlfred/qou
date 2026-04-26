#!/usr/bin/env python3
"""Render the recursive atom-knot atlas from witness JSON sources of truth.

LAYOUT — condensed 2-row format with EXPLICIT COLUMN HEADERS:

  | Particle | Z | N | e | ℓ | n₀ | Braid (NF)         | Closure          | Vol_hyp |
  |  rowspan |   |   |   |   |    | AME (MeV)          | Pred (MeV)       | err ppb (ρ) |

- Row 1 (math): Z, N, e (electron count), ℓ, n₀, braid in σ_* generators,
  Markov closure (named knot/link OR recursive structure),
  hyperbolic volume.
- Row 2 (physics): AME binding (MeV), prediction (MeV), error in
  WHOLE ppb integers (no 10^), and ρ prefactor.
- Magic-number markers (★ for shell-closure, etc.) shown next to Z/N.

For atoms WITHOUT a single-knot identification (⁸Be onward in
mass-table-ppb), the closure column shows the RECURSIVE structure
(e.g. "$^{4}\\mathrm{He} \\sharp\\,^{4}\\mathrm{He} + c_{\\alpha\\alpha}$")
rather than the literal formula text.

For atoms with no explicit braid word in NF yet, the braid column
shows "(see [recursive constituents]) — atomic-braid in $H_{n_0}$"
rather than just "T_w ∈ H_n".

SOURCES OF TRUTH:
  - confined-particle.md (GB-NF particle registry)
  - mass-table-ppb.witness.json
  - li-atom-knot-search.witness.json
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

# Magic numbers (nuclear shell closures): 2, 8, 20, 28, 50, 82, 126
MAGIC = {2, 8, 20, 28, 50, 82, 126}


def load_witnesses():
    base = Path(__file__).parent
    out = {}
    for name in ["mass-table-ppb", "li-atom-knot-search"]:
        p = base / f"{name}.witness.json"
        if p.exists():
            with open(p) as f:
                out[name] = json.load(f)
    return out


def fmt_ppb_int(ppb_float):
    """Format ppb as whole integer; preserve sign; no 10^ notation."""
    if ppb_float is None:
        return "—"
    s = f"{int(round(ppb_float)):+,d}"
    return s


def fmt_isotope(sym):
    """Format e.g. '4He' as $^{4}\\mathrm{He}$."""
    digits = ""
    rest = sym
    for i, c in enumerate(sym):
        if not c.isdigit():
            digits, rest = sym[:i], sym[i:]
            break
    if digits:
        return f"$^{{{digits}}}\\mathrm{{{rest}}}$"
    return f"${sym}$"


def fmt_knot(name):
    """Format knot/link names with LaTeX subscripts.

    - "8_11" → "$8_{11}$" (Rolfsen)
    - "K11a259" → "$K_{11a259}$" (Hoste-Thistlethwaite knot)
    - "L11a62" → "$L_{11a62}$" (HT link)
    - "L11a62(0,0)(0,0)" → "$L_{11a62}(0,0)(0,0)$" (Dehn fillings)
    """
    import re
    if not name or name == "?":
        return name
    # Strip Dehn-filling suffix like (0,0)(0,0)
    m = re.match(r"^([^(]+)(\(.*\))?$", name)
    base = m.group(1) if m else name
    fillings = m.group(2) if m and m.group(2) else ""
    # Rolfsen-style: digits_index, e.g. "8_11"
    m2 = re.match(r"^(\d+)_(\d+)$", base)
    if m2:
        return f"${m2.group(1)}_{{{m2.group(2)}}}{fillings}$"
    # Hoste-Thistlethwaite-style: <K|L><digits><a|n><digits>
    m3 = re.match(r"^([KL])(\d+[an]\d+)$", base)
    if m3:
        return f"${m3.group(1)}_{{{m3.group(2)}}}{fillings}$"
    return f"${base}{fillings}$"


def magic_marker(n):
    """Return ★ if n is a magic number, else empty."""
    return " ★" if n in MAGIC else ""


def closure_for_row(r):
    """Return the right closure label depending on what the witness has.

    For an explicit knot/link name (e.g. K11a259), use that.
    For α-cluster recursive formulas, expand into recursive notation.
    For pure A·8G magic-rule, show the rule.
    """
    knot = r.get("inputs", {}).get("knot")
    if knot:
        return fmt_knot(knot)
    formula = r.get("formula", "")
    # Recursive α-cluster: "2·B(⁴He_derived) + 1·c_αα" → recursive notation
    if "B(⁴He_derived)" in formula:
        # Parse n_α and n_pairs
        import re
        m = re.match(r"(\d+)·B\(.*\) \+ (\d+)·c_αα", formula)
        if m:
            n_alpha, n_pair = int(m.group(1)), int(m.group(2))
            if n_pair == 0:
                return f"${n_alpha} \\cdot {{}}^{{4}}\\mathrm{{He}}$"
            return (f"${n_alpha} \\cdot {{}}^{{4}}\\mathrm{{He}}"
                    f" + {n_pair} \\cdot c_{{\\alpha\\alpha}}$")
    # Pure ⁴He magic-A formula: "2·m_e · 4·8G"
    if "8G" in formula:
        return f"$A \\cdot 8G$ magic-A"
    return formula[:40]  # fallback


def braid_label(n_0, recursive_constituents=None):
    """Return a useful braid-column label; if no NF available, point at
    the recursive constituents."""
    if recursive_constituents:
        return (f"recursive: {recursive_constituents} — atomic-braid in "
                f"$H_{{{n_0}}}$")
    return f"atomic-braid in $H_{{{n_0}}}$ (NF pending)"


def fundamental_particles():
    """Hard-coded ℓ=0, ℓ=1 from confined-particle.md registry."""
    return [
        {"label": r"Neutrino $\nu$", "Z": 0, "N": 0, "e": 0,
         "ell": 0, "n_0": 1,
         "braid": r"$\mathbf{1} \in H_1$", "closure": r"$0_1$ (unknot)",
         "vol_hyp": "0",
         "AME": r"$\le 1$ eV", "pred": r"$\approx 0$ MeV",
         "err_ppb_str": "—", "rho": "—"},
        {"label": r"Photon $\gamma$", "Z": 0, "N": 0, "e": 0,
         "ell": 0, "n_0": 4,
         "braid": r"$\mathbf{1}_{B_4} \in H_4$",
         "closure": r"$4 \cdot 0_1$ (4-strand id)",
         "vol_hyp": "0", "AME": "0 MeV", "pred": "0 MeV",
         "err_ppb_str": "—", "rho": "—"},
        {"label": r"Quark $\mathfrak{q}$", "Z": 0, "N": 0, "e": 0,
         "ell": 0, "n_0": 1,
         "braid": r"$\sigma_0 \in H_1$",
         "closure": r"(in $\mathcal{B}_3$)",
         "vol_hyp": "—", "AME": "(confined)", "pred": "—",
         "err_ppb_str": "—", "rho": "—"},
        {"label": r"Electron $e^-$", "Z": 0, "N": 0, "e": 1,
         "ell": 1, "n_0": 2,
         "braid": r"$\sigma_1^3 \in H_2$",
         "closure": r"$T_{2,3} = 3_1$ (trefoil)",
         "vol_hyp": "0", "AME": "0.51099895 MeV", "pred": "0.51099895 MeV",
         "err_ppb_str": "(anchor)", "rho": "—"},
        {"label": r"Proton $\mathfrak{p}$", "Z": 1, "N": 0, "e": 0,
         "ell": 1, "n_0": 3,
         "braid": r"$(\sigma_1 \sigma_2^{-1})^3$ flav-uud",
         "closure": r"$\mathcal{B}_3(\mathrm{uud})$",
         "vol_hyp": "7.3277", "AME": "938.272 MeV", "pred": "938.272 MeV",
         "err_ppb_str": "(anchor)", "rho": "—"},
        {"label": r"Neutron $\mathfrak{n}$", "Z": 0, "N": 1, "e": 0,
         "ell": 1, "n_0": 3,
         "braid": r"$(\sigma_1 \sigma_2^{-1})^3$ flav-udd",
         "closure": r"$\mathcal{B}_3(\mathrm{udd})$",
         "vol_hyp": "7.3277", "AME": "939.565 MeV", "pred": "939.565 MeV",
         "err_ppb_str": "(anchor)", "rho": "—"},
    ]


def light_atoms_from_witness(W):
    out = []
    if "mass-table-ppb" not in W:
        return out
    for r in W["mass-table-ppb"].get("rows", []):
        Z, N, A = r["Z"], r["N"], r["A"]
        rho = r.get("inputs", {}).get("rho_factor", "—")
        vol = r.get("inputs", {}).get("Vol", None)
        # For α-cluster formulas the explicit braid in NF isn't available
        # — show recursive constituents.
        if "B(⁴He_derived)" in r.get("formula", ""):
            import re
            m = re.match(r"(\d+)·B\(.*\) \+ (\d+)·c_αα", r["formula"])
            if m:
                n_alpha = int(m.group(1))
                braid_str = (f"recursive: {n_alpha} $\\times {{}}^{{4}}\\mathrm{{He}}$"
                             f" $\\bowtie c_{{\\alpha\\alpha}}$ — atomic-braid in "
                             f"$H_{{{3 * A}}}$")
            else:
                braid_str = f"atomic-braid in $H_{{{3 * A}}}$"
        elif "8G" in r.get("formula", ""):
            braid_str = (f"$A \\cdot 8G$ magic-A formula — atomic-braid in "
                         f"$H_{{{3 * A}}}$")
        else:
            knot = r.get("inputs", {}).get("knot", "?")
            braid_str = f"closure = {fmt_knot(knot)} — atomic-braid in $H_{{{3 * A}}}$"
        out.append({
            "label": fmt_isotope(r["sym"]),
            "Z": Z, "N": N, "e": Z,
            "ell": 2, "n_0": 3 * A,
            "braid": braid_str,
            "closure": closure_for_row(r),
            "vol_hyp": f"{vol:.4f}" if vol else "—",
            "AME": f"{r['B_AME_MeV']:.4f} MeV",
            "pred": f"{r['B_pred_MeV']:.4f} MeV",
            "err_ppb_str": fmt_ppb_int(r['err_ppb']),
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
    Z = {"6Li": 3, "7Li": 3}
    N = {"6Li": 3, "7Li": 4}
    for label in ["6Li", "7Li"]:
        if label not in li or not li[label]:
            continue
        best = min(li[label].items(), key=lambda kv: abs(kv[1].get("err_pct", 1e10)))
        rho_str, info = best
        out.append({
            "label": fmt_isotope(label),
            "Z": Z[label], "N": N[label], "e": Z[label],
            "ell": 2, "n_0": 3 * A[label],
            "braid": (f"closure = {fmt_knot(info['best_knot'])} — atomic-braid"
                      f" in $H_{{{3 * A[label]}}}$"),
            "closure": fmt_knot(info['best_knot']),
            "vol_hyp": f"{info['vol']:.4f}",
            "AME": f"{AME[label]:.4f} MeV",
            "pred": f"{info['B_pred']:.4f} MeV",
            "err_ppb_str": fmt_ppb_int(info['err_ppb']),
            "rho": str(rho_str),
        })
    return out


def render_md(rows, group_name):
    """HTML rowspan'd table with explicit column descriptions."""
    out = [f"\n### {group_name}\n"]
    out.append("<table>")
    out.append("<thead>")
    # Two-row header explaining what each cell means
    out.append(
        "<tr>"
        "<th rowspan='2'>Particle / atom</th>"
        "<th colspan='3'>Composition</th>"
        "<th colspan='2'>Confinement</th>"
        "<th colspan='3'>Math (row 1) / Physics (row 2)</th>"
        "</tr>"
    )
    out.append(
        "<tr>"
        "<th>Z</th><th>N</th><th>e<sup>−</sup></th>"
        "<th>ℓ</th><th>n₀</th>"
        "<th>Braid (NF) / AME (MeV)</th>"
        "<th>Closure / Pred (MeV)</th>"
        "<th>Vol<sub>hyp</sub> / err ppb (ρ)</th>"
        "</tr>"
    )
    out.append("</thead>")
    out.append("<tbody>")
    for r in rows:
        z_mark = magic_marker(r['Z']) if isinstance(r['Z'], int) else ""
        n_mark = magic_marker(r['N']) if isinstance(r['N'], int) else ""
        # Row 1: math
        out.append(
            "<tr>"
            f"<td rowspan='2'><strong>{r['label']}</strong></td>"
            f"<td>{r['Z']}{z_mark}</td><td>{r['N']}{n_mark}</td><td>{r['e']}</td>"
            f"<td>{r['ell']}</td><td>{r['n_0']}</td>"
            f"<td>{r['braid']}</td>"
            f"<td>{r['closure']}</td>"
            f"<td>Vol<sub>hyp</sub>: {r['vol_hyp']}</td>"
            "</tr>"
        )
        # Row 2: physics
        out.append(
            "<tr>"
            "<td colspan='5'><em>(physics)</em></td>"
            f"<td>AME: {r['AME']}</td>"
            f"<td>Pred: {r['pred']}</td>"
            f"<td>err: {r['err_ppb_str']} ppb (ρ={r['rho']})</td>"
            "</tr>"
        )
    out.append("</tbody></table>")
    return "\n".join(out)


def render_tex(rows, group_name):
    out = [r"\subsection*{" + group_name + r"}", ""]
    out.append(r"\begin{tabular}{l|ccc|cc|p{3cm}|p{2.5cm}|p{2.5cm}}")
    out.append(r"\hline")
    out.append(
        r"\textbf{Particle} & Z & N & $e^-$ & $\ell$ & $n_0$ & "
        r"Braid (NF) / AME & Closure / Pred & Vol${}_{\mathrm{hyp}}$ / err ppb \\"
    )
    out.append(r"\hline")
    for r in rows:
        z_mark = magic_marker(r['Z']) if isinstance(r['Z'], int) else ""
        n_mark = magic_marker(r['N']) if isinstance(r['N'], int) else ""
        out.append(
            r"\multirow{2}{*}{\textbf{" + r["label"] + r"}}"
            f" & {r['Z']}{z_mark} & {r['N']}{n_mark} & {r['e']}"
            f" & {r['ell']} & {r['n_0']}"
            f" & {r['braid']} & {r['closure']}"
            f" & Vol: {r['vol_hyp']} \\\\ "
        )
        out.append(
            r"& \multicolumn{5}{c|}{\emph{(physics)}}"
            f" & AME: {r['AME']}"
            f" & Pred: {r['pred']}"
            f" & err: {r['err_ppb_str']} ppb ($\\rho$={r['rho']}) \\\\ \\hline"
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

    print("# Recursive Atom-Knot Atlas (auto-rendered from witnesses)\n")
    print("**Source of truth**: `confined-particle.md` (GB-NF registry) + ")
    print("`mass-table-ppb.witness.json` + `li-atom-knot-search.witness.json`.\n")
    print("## Table layout\n")
    print(
        "Each particle/atom has TWO rows. **Column 1** spans both "
        "(particle notation). **Row 1** shows the math: Z, N, e⁻ count, "
        "confinement level ℓ, strand count n₀, the braid in σ_* generators "
        "(NF), the Markov closure as a named knot/link or recursive "
        "structure, and hyperbolic volume.  **Row 2** shows the physics: "
        "AME binding, model prediction, error in **whole-integer ppb** "
        "(no scientific notation), and the ρ prefactor in "
        "$B = \\rho \\cdot m_e \\cdot \\mathrm{Vol}_{\\mathrm{hyp}}$.\n"
    )
    print("Magic-number markers: ★ next to Z or N indicates a nuclear shell "
          "closure (Z, N ∈ {2, 8, 20, 28, 50, 82, 126}).\n")
    print("Braid label conventions:\n")
    print("- For atoms with an explicit hyperbolic-knot identification, "
          "the closure is shown directly (e.g. $K_{11a259}$, $L_{11a62}$).\n")
    print("- For α-cluster atoms (⁸Be onward), the closure shows the "
          "**recursive** structure $n \\cdot {}^{4}\\mathrm{He} + "
          "n_{\\alpha\\alpha} \\cdot c_{\\alpha\\alpha}$ rather than literal "
          "formula text — this captures the cluster decomposition.\n")
    print("- For ⁴He, the closure shows the magic-A rule "
          "$A \\cdot 8 G$ since no single-knot identification "
          "applies (it's the 4-nucleon shell-closure formula).\n")
    print("- The braid column shows `closure = <knot>` for atoms with a "
          "knot ID, and `recursive: ...` for cluster-derived atoms — making "
          "it informative rather than the bare $T_w \\in H_n$.\n")
    print(render(fundamental_particles(), r"$\ell = 0, 1$ — fundamental particles"))
    print(render(light_atoms_from_witness(W), r"$\ell = 2$ — light atoms (mass-table-ppb)"))
    print(render(li_from_witness(W), r"$\ell = 2$ — Lithium isotopes (atom-knot search)"))


if __name__ == "__main__":
    main()
