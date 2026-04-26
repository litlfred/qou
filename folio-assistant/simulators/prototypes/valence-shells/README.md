# Valence-shells prototype

Visual prototype for option (2) of the **valence structure** plan: render
each level of the GB normal-form filtration $F_\bullet H_n(q)$ as a
concentric ring (the closure of its sub-braid), at radius
$R_0 \cdot s^k$ with $s = q^{-1/2}$.

This is a **prototype** — pure Canvas2D, hand-stubbed atlas data, no
Lean / GB pipeline integration yet. Its job is to validate the visual
language before wiring it into sim 1.

Open `index.html` directly in a browser, or use URL params for
preset views:
- `?entry=alpha&kmax=2`
- `?entry=li7&mode=split`
- `?entry=c12&s=0.7`

## Screenshots (preset views)

| File | View |
|---|---|
| `shots/alpha-full.png` | ⁴He α, all shells $k = 0..4$, nested |
| `shots/alpha-k1.png`   | ⁴He α, only $k \le 1$ (backbone + valence-1) |
| `shots/alpha-k2.png`   | ⁴He α, only $k \le 2$ |
| `shots/alpha-split.png`| ⁴He α, shells exploded into a row |
| `shots/li7-full.png`   | ⁷Li in $H_{21}$, all shells |
| `shots/li7-split.png`  | ⁷Li, exploded |
| `shots/proton-full.png`| proton ($\sigma_1^3$): pure $k=3$ — single shell, "atomic" |
| `shots/c12-full.png`   | ¹²C (3α), nested |
| `shots/c12-split.png`  | ¹²C, exploded |

## Reading the picture

- **Outer ring** ($k = 0$, gold) = the valence-0 backbone — the $n$
  parallel nucleon loops with no crossings.
- **Each inner ring** ($k > 0$) = the projection $\pi_k\,\mathrm{NF}(\beta)$
  onto $F_k / F_{k-1}$, drawn as the closure of its leading sub-braid.
- **Radius** $R_0 \cdot s^k$ literally *is* the $q$-grading — bigger
  visual = larger $q$-norm = lower-valence (closer to identity).
- **Innermost ring** = the GB leading monomial, the "irreducible core".
- The **proton** (`shots/proton-full.png`) collapses to a single ring at
  $k = 3$: it has no sub-structure, so it is an **atom** of the GB
  filtration. ⁴He, ⁷Li, ¹²C show progressively richer nesting.

## Controls (live HTML)

- atlas dropdown · `k_max` slider (peel outer shells off) ·
  `s` slider with "lock to $q_0$" · nested ↔ split layout

## Path to integration (option 2)

1. Move `buildShellPipeline()` (compute filtration JSON from braid word)
   into `folio-assistant/computations/`, calling the real
   `unital-groebner-bases` GB code instead of stub data.
2. Cache one `<entry>.filtration.json` per atlas entry.
3. Add a "valence" mode toggle to `simulators/knot_periodic_table.html`
   that swaps each thumbnail's renderer for a nested-shell version
   driven by `filtration.json`.
4. Re-use sim 1's existing `renderBraidClosure(word, n)` per level —
   no new geometry primitives.
