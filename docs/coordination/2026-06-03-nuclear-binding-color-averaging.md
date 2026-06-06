# Coordination ledger — nuclear A=3 binding + color-averaging wiring

**Goal.** Close the A=3 binding residuals from the operator-valued /
extensive-bond-sum direction, and **wire color-averaging (the
`bring_color_weighted` interface) everywhere it is missing in the mass +
binding pipelines** — even where it is not today's dominant error, because
it will be later. Owner directive 2026-06-03.

**Driving PR:** #1754 (`claude/nuclear-a3-dpn-2026-06-03`).

## Scope map

| PR | branch | relationship | action |
|----|--------|-------------|--------|
| **#1754** | nuclear-a3-dpn | **this** | multiplicity ✅; color audit + charge crossing + per-bond growth in flight |
| #1725 | extensive-bond-sum | **MERGED** — my C(A,2) multiplicity extends its scalar bond-sum to per-block | consume (on main) |
| #1569 | avg-crossing-foundational-identity | overlap: the averaged crossing `σ−h/2` I am color-weighting | intent posted (#1569 comment) |
| #1741 | wire-native-chi-incremental | overlap: `pyhecke_native` H₉ path (I built it locally) | intent posted (#1741 comment) |
| #1521/#1523/#1549 | α_EM Habiro `[2]_q(1−h²α)` / Schwinger | **dependency** for the charge/EM crossing (task 1, T−³He Coulomb) | coordinate when task 1 starts |
| #1762 | 1ppq-roadmap / VolDensity bridge | mass pipeline (color averaging applies to `vol_density_borromean`) | monitor |
| #1752 / #1753 / #1742 | Q_β SDP / m_μ / bar-pairing | my session siblings (mass/binding) | aware |

## Findings carried in (from this session)

- A=3 −60 % deficit was **multiplicity**, not observation/Δ_λ. C(A,2)
  per-block typed bond sum → A=3 at −11 %/−19 % (zero fit).
- **Color-averaged crossing** (`bring_color_weighted`, `f = z − h(1/2−δ/4)`,
  δ from `flavor_split_subleading`): right *sign* for B_nn>B_pp but
  **~200× too small** (±0.046 %) for the 0.76 MeV T−³He split → that split
  is **charge/Coulomb (α_EM)**, a separate larger sector.
- Color averaging lives at the **Δm_pn scale (0.14 %)** — correct and
  derived, must be wired everywhere for completeness even though it is not
  the dominant A=3 residual.

## Work queue (this tranche)

1. **Color-averaging wiring audit (task 3, emphasized).** Full compute
   audit of mass + binding pipelines: find every interface using the
   color-blind `−h/2` and wire `bring_color_weighted`. Update audit docs.
2. **Charge/EM-weighted crossing (task 1).** T−³He Coulomb via α_EM
   (coordinate with #1521/#1523/#1549).
3. **Per-bond growth (task 2).** Embedded-bond H₉ traces (Rust kernel built)
   for the ~−15 % bulk A=3 residual.

## Review triage

- #1754: 4 Gemini/Copilot threads — all **accept**, fixed in `ce069d1f5b`,
  resolved + consolidated status posted.

## Coordination comments posted

- #1569 (intent — color-weighting the avg crossing): comment 4616225400.
- #1741 (intent — pyhecke_native overlap): comment 4616225857.
