# Valence-shells prototype — *small scope: neutron, proton, ¹H*

Visual prototype for the **valence structure** plan: render each level of
the GB normal-form filtration $F_\bullet H_n(q)$ as a concentric ring (the
closure of its sub-braid), at radius $R_0 \cdot s^k$ with $s = q^{-1/2}$.

This is a **prototype** — pure Canvas2D, hand-stubbed atlas data, no
Lean / GB pipeline integration yet. Its job is to validate the visual
language before wiring it into sim 1.

## Scope

Three smallest objects, designed to give visual contrast:

| Entry | Braid | $H_n$ | Non-empty shells |
|---|---|---|---|
| **proton**  | $\sigma_1^3$         | $H_3$ | $k=0$ (3 quark loops) + $k=3$ (proton core) |
| **neutron** | $\sigma_1^2 \sigma_2$| $H_3$ | $k=0$ (3 quark loops) + $k=3$ (neutron core) |
| **¹H**      | $\sigma_1^3 \cdot \sigma_3$ | $H_4$ | $k=0$ (3 quarks + e⁻) + $k=1$ (p–e⁻ binding) + $k=3$ (proton core) |

The point: **proton and neutron** have a single non-trivial shell ($k=3$) — they are
**atoms** of the GB filtration. **¹H** has *two* non-trivial shells — adding the
electron creates a new $k=1$ binding shell *outside* the proton core, while leaving
the proton's $k=3$ core intact and visible at its own (smaller) radius.

## Screenshots

| File | View |
|---|---|
| `shots/proton-full.png`  | proton — backbone + $k=3$ core |
| `shots/neutron-full.png` | neutron — backbone + $k=3$ core |
| `shots/h1-full.png`      | ¹H, all shells nested |
| `shots/h1-k1.png`        | ¹H, $k_\max=1$ — proton core hidden, only e⁻ binding visible |
| `shots/h1-k3.png`        | ¹H, $k_\max=3$ — adds proton core |
| `shots/h1-split.png`     | ¹H, exploded into a row (compare backbone, binding, core side-by-side) |
| `shots/proton-split.png` | proton, exploded |
| `shots/neutron-split.png`| neutron, exploded |

## Reading the picture

- **Outer gold ring** ($k = 0$) = the valence-0 backbone — $n$ parallel loops
  with no crossings (3 quarks for p/n, 3 quarks + 1 electron for ¹H).
- **Pink ring** ($k = 1$) only present in ¹H — single proton–electron binding
  crossing $\sigma_3$ (electron lane swaps with adjacent quark lane).
- **Green ring** ($k = 3$) = the proton/neutron core: leading sub-braid drawn
  as the closure of $\sigma_1^3$ (or $\sigma_1^2 \sigma_2$ for neutron).
- **Radius shrinks as $R_0 \cdot s^k$** — the scaling literally *is* the
  $\mathrm{gr}_k$ projection.
- White dots mark crossing locations.

## Controls (live HTML)

- atlas dropdown (3 entries) · `k_max` slider (peel outer shells off) ·
  `s` slider with "lock to $q_0 = 1.1097$" · nested ↔ split layout
- URL params for screenshots: `?entry=h1&kmax=1&mode=split&s=0.62`

## Path to integration (option 2 of the plan)

1. Move filtration computation into `folio-assistant/computations/`,
   calling the real `unital-groebner-bases` GB code instead of the
   3-entry hand-stub above.
2. Cache one `<entry>.filtration.json` per atlas entry (start with these three).
3. Add a "valence" mode toggle to `simulators/knot_periodic_table.html`
   that swaps each thumbnail's renderer for a nested-shell version
   driven by `filtration.json`.
4. Re-use sim 1's existing `renderBraidClosure(word, n)` per level —
   no new geometry primitives.

## Known caveats

- Stub data only — the `mult` and `leading` fields are illustrative.
- The "lock q" button uses $s = 1/\sqrt{q_0} \approx 0.949$; the visual
  default $s = 0.62$ from the spec is kept as the slider home position
  because it reads better on screen. We need to decide which to ship.
