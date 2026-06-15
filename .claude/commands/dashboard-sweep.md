---
description: Mass-binding dashboard SWEEP across the mass range — a few low (²H,⁴He), low-mid (⁷Li,⁹Be,¹²C), mid (¹⁶O,²⁴Mg,⁴⁰Ca) and high (⁵⁶Fe) isotopes. Trace forms where the tr_M compute is feasible; the colour-weighted q-CLT + magic volume everywhere as the A→∞ extrapolation, so the method's breakdown past the light nuclei is visible. No args.
---

Run the **sweep** mass-binding dashboard and present its tables verbatim.

```bash
python3 computations/mass_binding_dashboard.py --group sweep
```

Render the script's three markdown tables (Binding / Error / Mass) directly.

**Context to surface when presenting:**

- The sweep spans **low → high**: ²H, ⁴He (low) · ⁷Li, ⁹Be, ¹²C (low-mid) ·
  ¹⁶O, ²⁴Mg, ⁴⁰Ca (mid) · ⁵⁶Fe (high).
- **Feasibility is honest, not hidden.** The trace forms `B_lin / B_sym /
  B_qCLT` need the full per-knot trace `tr_M(W_atom)`, whose partition sum
  `p(3A)` explodes with A, so they print **only** for `n = 3A ≤ --max-strands`
  (default 21, i.e. A ≤ 7) and show `—` above that. The **colour-weighted
  `B_qCLT_fac`** and the **⁴He `B_magic`** are cheap (combinatorics + three
  fixed 2-nucleon sub-braid ratios) and print across the whole range as the
  **A→∞ extrapolation** — which is where the trace method's breakdown beyond the
  light nuclei is meant to show (e.g. `B_qCLT_fac` under-binds ⁵⁶Fe ~2× because
  the 2-nucleon bond ratios do not reach the iron-peak saturation).
- **B_AME** is the AME2020 experimental binding (`data/ame2020.json`); α = E₀.
- Raise `--max-strands` (e.g. `--max-strands 27` for A ≤ 9) to compute more
  trace rows — slower (the tr_M sweep is seconds at A=7, minutes by A=12).
- Same engine + caveats as `/dashboard-low`; forms defined in
  [`standard-part-functor.md`](../../content/quantum-observable-universe/appendix-surreals-archimedean/standard-part-functor.md).
  **Exploratory** — no production rewire, no fit.
