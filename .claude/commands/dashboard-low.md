---
description: Mass-binding dashboard for the LOW isotopes (²H–⁷Li). Prints three tables — binding B, error (B_AME/B), and mass M — for every standard-part form (B_lin / B_sym / B_qCLT / B_qCLT_fac / B_magic) against AME2020, all from the one canonical Jones–Markov trace at α = E₀. No args.
---

Run the **low-isotope** mass-binding dashboard and present its tables verbatim.

```bash
python3 computations/mass_binding_dashboard.py --group low
```

Render the script's three markdown tables (Binding / Error / Mass) directly to
the user — they are already GitHub-flavoured markdown. Then, if useful, add a
one-line reading.

**Context to surface when presenting:**

- Every binding form is evaluated from the **one canonical transfer trace**
  `tr_m_atom_zn`; **B_AME** is the AME2020 experimental binding
  (`data/ame2020.json`). α = E₀ = m_e/(q₀(q₀−1)) ≈ 4.186 MeV (derived).
- **The forms** are defined in
  [`standard-part-functor.md`](../../content/quantum-observable-universe/appendix-surreals-archimedean/standard-part-functor.md):
  - `B_lin = α·s` (linear, saturates) · `B_sym = α·ln(tr_free/tr_atom)` (exact
    log-trace = **archimedean** realization) · `B_qCLT = α·(A−1)·ℓ̄(D)` (uniform,
    no p↔n weighting) · `B_qCLT_fac = α·(A−1)·⟨bond-type L⟩` (**p↔n
    colour-weighted** q-CLT) · `B_magic = 2·m_e·A·8G` (⁴He only).
- **B_sym is compositional:** `B_sym = m_sym(atom) − Σ m_sym(free GB components)`
  with `m_sym(W) = −α·ln(tr_M(W))`, because the free word factorises
  `tr_free = tr_p^Z·tr_n^N`.
- This is the multi-isotope view of the single-pipeline probe
  `binding_single_pipeline_comparison.py` (PR #2320). **Exploratory** — no
  production rewire, no fit.

Sibling command: `/dashboard-sweep` (a low→high spread).
